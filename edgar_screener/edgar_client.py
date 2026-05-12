"""
Low-level HTTP client for SEC EDGAR APIs.
Enforces rate limits and provides retry logic per SEC guidelines.

Filing search strategy:
  PRIMARY  – EDGAR quarterly full-index (form.idx, fixed-width, stabile da anni)
  FALLBACK – EFTS search API con parsing corretto degli _id (accession:filename)
"""
import io
import time
import logging
import xml.etree.ElementTree as ET
from datetime import date
from typing import Any, Dict, List, Optional
from urllib.parse import urlencode

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .config import cfg

logger = logging.getLogger(__name__)

# Cache quarterly index in memory (avoid re-download within same run)
_index_cache: Dict[str, List[Dict]] = {}


def _quarter(d: date) -> str:
    return f"QTR{(d.month - 1) // 3 + 1}"


class EdgarClient:
    """Thread-safe EDGAR HTTP client with automatic rate limiting."""

    def __init__(self):
        self._last_request_time: float = 0.0
        self._session = self._build_session()

    # ── Session / HTTP ─────────────────────────────────────────────────────────

    def _build_session(self) -> requests.Session:
        session = requests.Session()
        session.headers.update({
            "User-Agent": cfg.edgar_user_agent,
            "Accept-Encoding": "gzip, deflate",
            "Accept": "application/json, text/html, */*",
        })
        retry = Retry(
            total=4,
            backoff_factor=2,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"],
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("https://", adapter)
        return session

    def _get(self, url: str, **params) -> requests.Response:
        elapsed = time.time() - self._last_request_time
        if elapsed < cfg.edgar_request_delay:
            time.sleep(cfg.edgar_request_delay - elapsed)
        self._last_request_time = time.time()
        if params:
            url = f"{url}?{urlencode(params)}"
        logger.debug("GET %s", url)
        resp = self._session.get(url, timeout=60)
        resp.raise_for_status()
        return resp

    def get_json(self, url: str, **params) -> Any:
        return self._get(url, **params).json()

    def get_text(self, url: str, **params) -> str:
        return self._get(url, **params).text

    def get_xml(self, url: str, **params) -> ET.Element:
        return ET.fromstring(self.get_text(url, **params))

    # ── Primary: EDGAR quarterly form.idx (fixed-width, reliable) ────────────

    def _load_quarterly_index(self, target_date: date) -> List[Dict]:
        """
        Download EDGAR quarterly form.idx (fixed-width, sorted by form type).
        Returns all filing dicts for the quarter, cached in memory.

        Format (fixed-width, columns separated by multiple spaces):
          Form Type   Company Name           CIK         Date Filed  Filename
          4           ACME CORP              0001234567  2026-05-11  edgar/data/...
        """
        qtr_key = f"{target_date.year}/{_quarter(target_date)}"
        if qtr_key in _index_cache:
            return _index_cache[qtr_key]

        url = (
            f"{cfg.edgar_base_url}/Archives/edgar/full-index/"
            f"{target_date.year}/{_quarter(target_date)}/form.idx"
        )
        logger.info("  Scarico indice EDGAR: %s", url)
        try:
            resp = self._get(url)
            text = resp.text
        except Exception as exc:
            logger.warning("Impossibile scaricare form.idx: %s", exc)
            _index_cache[qtr_key] = []
            return []

        filings: List[Dict] = []
        lines = text.splitlines()

        # Detect column positions from header line
        # Header looks like:
        # "Form Type   Company Name                          CIK         Date Filed  Filename"
        col_company = col_cik = col_date = col_file = None
        for line in lines[:10]:
            if "Company Name" in line and "CIK" in line:
                col_company = line.index("Company Name")
                col_cik = line.index("CIK")
                col_date = line.index("Date Filed")
                col_file = line.index("Filename")
                break

        if col_company is None:
            # Fallback: try fixed standard positions (common in EDGAR)
            col_company, col_cik, col_date, col_file = 12, 74, 86, 98

        for line in lines:
            # Skip blank lines and header/separator lines
            if not line.strip() or line.startswith("-") or "Form Type" in line:
                continue
            if len(line) <= col_file:
                continue
            try:
                form_type = line[:col_company].strip()
                company = line[col_company:col_cik].strip()
                cik = line[col_cik:col_date].strip()
                file_date = line[col_date:col_file].strip()
                filename = line[col_file:].strip()
            except Exception:
                continue

            if not form_type or not file_date or len(file_date) != 10:
                continue

            # Extract accession number from filename
            # e.g. edgar/data/1234567/0001234567-26-001234.txt
            base = filename.split("/")[-1]
            for suffix in (".txt", "-index.htm", "-index.html"):
                if base.endswith(suffix):
                    base = base[: -len(suffix)]
                    break
            accession = base  # format: 0001234567-26-001234

            if len(accession) < 18:
                continue

            filings.append({
                "_id": accession,
                "_source": {
                    "entity_name": company,
                    "form_type": form_type,
                    "cik": cik,
                    "file_date": file_date,
                    "filename": filename,
                    "items": "",
                    "primary_doc": None,  # unknown from form.idx
                },
            })

        logger.info("  Indice caricato: %d filing totali in %s", len(filings), qtr_key)
        _index_cache[qtr_key] = filings
        return filings

    def search_filings(
        self,
        forms: List[str],
        start_date: date,
        end_date: Optional[date] = None,
        max_results: int = 200,
    ) -> List[Dict]:
        """
        Return filing metadata for given form types and date range.
        Primary: quarterly form.idx. Fallback: EFTS search API.
        """
        if end_date is None:
            end_date = start_date

        quarterly = self._load_quarterly_index(start_date)
        if quarterly:
            forms_upper = {f.upper() for f in forms}
            date_start = start_date.isoformat()
            date_end = end_date.isoformat()
            results = []
            for hit in quarterly:
                src = hit["_source"]
                ft = src.get("form_type", "").upper()
                fd = src.get("file_date", "")
                if ft in forms_upper and date_start <= fd <= date_end:
                    results.append(hit)
                    if len(results) >= max_results:
                        break
            logger.info(
                "  Trovati %d filing [%s] per %s (da indice trimestrale)",
                len(results), ", ".join(forms), date_start,
            )
            return results

        # ── Fallback: EFTS ─────────────────────────────────────────────────────
        logger.warning("Fallback a EFTS (form.idx non disponibile)")
        return self._search_efts(forms, start_date, end_date, max_results)

    def _search_efts(
        self, forms: List[str], start_date: date, end_date: date, max_results: int
    ) -> List[Dict]:
        """
        EFTS search. Normalises _id from 'accession:filename' to just 'accession',
        storing the filename in _source.primary_doc for direct document access.
        """
        all_hits: List[Dict] = []
        seen_accessions: set = set()
        from_offset = 0

        while from_offset < max_results:
            params = {
                "forms": ",".join(forms),
                "dateRange": "custom",
                "startdt": start_date.isoformat(),
                "enddt": end_date.isoformat(),
                "from": from_offset,
            }
            try:
                data = self._get(cfg.edgar_efts_url, **params).json()
            except Exception as exc:
                logger.warning("EFTS error: %s", exc)
                break
            hits = data.get("hits", {}).get("hits", [])
            if not hits:
                break

            for hit in hits:
                raw_id = hit.get("_id", "")
                # EFTS sometimes returns 'accession:primary_doc.xml'
                if ":" in raw_id:
                    accession, primary_doc = raw_id.split(":", 1)
                else:
                    accession = raw_id
                    primary_doc = None

                if accession in seen_accessions:
                    continue
                seen_accessions.add(accession)

                hit["_id"] = accession
                src = hit.setdefault("_source", {})
                if primary_doc:
                    src["primary_doc"] = primary_doc
                # Derive CIK from accession if not present
                if not src.get("cik") and accession:
                    src["cik"] = str(int(accession.split("-")[0]))

                all_hits.append(hit)

            from_offset += len(hits)
            if len(hits) < 40:
                break

        logger.info("  EFTS: trovati %d filing unici [%s]", len(all_hits), ", ".join(forms))
        return all_hits

    # ── Company / ticker resolution ───────────────────────────────────────────

    _ticker_map: Optional[Dict[str, Dict]] = None

    def _load_ticker_map(self) -> Dict[str, Dict]:
        if self.__class__._ticker_map is None:
            logger.info("Carico mappa ticker EDGAR…")
            data = self.get_json(f"{cfg.edgar_base_url}/files/company_tickers.json")
            self.__class__._ticker_map = {
                str(v["cik_str"]): v for v in data.values()
            }
        return self.__class__._ticker_map

    def ticker_for_cik(self, cik: str) -> Optional[str]:
        try:
            entry = self._load_ticker_map().get(str(int(cik)))
            return entry["ticker"] if entry else None
        except Exception:
            return None

    def name_for_cik(self, cik: str) -> Optional[str]:
        try:
            entry = self._load_ticker_map().get(str(int(cik)))
            return entry["title"] if entry else None
        except Exception:
            return None

    # ── Filing document fetching ───────────────────────────────────────────────

    def get_filing_index(self, cik: str, accession_no: str) -> Dict:
        acc_nodash = accession_no.replace("-", "")
        cik_padded = str(int(cik)).zfill(10)
        url = (
            f"{cfg.edgar_base_url}/Archives/edgar/data/{cik_padded}/"
            f"{acc_nodash}/{acc_nodash}-index.json"
        )
        try:
            return self.get_json(url)
        except Exception:
            return {}

    def get_filing_document(self, cik: str, accession_no: str, filename: str) -> str:
        acc_nodash = accession_no.replace("-", "")
        cik_padded = str(int(cik)).zfill(10)
        url = (
            f"{cfg.edgar_base_url}/Archives/edgar/data/{cik_padded}/"
            f"{acc_nodash}/{filename}"
        )
        return self.get_text(url)

    def get_company_facts(self, cik: str) -> Dict:
        cik_padded = str(int(cik)).zfill(10)
        url = f"{cfg.edgar_data_url}/api/xbrl/companyfacts/CIK{cik_padded}.json"
        try:
            return self.get_json(url)
        except Exception:
            return {}

    # ── Hit accessors ──────────────────────────────────────────────────────────

    @staticmethod
    def accession_from_hit(hit: Dict) -> Optional[str]:
        return hit.get("_id")  # already cleaned (no :filename)

    @staticmethod
    def filing_date_for_hit(hit: Dict) -> str:
        return hit.get("_source", {}).get("file_date", "")

    @staticmethod
    def entity_name_for_hit(hit: Dict) -> str:
        return hit.get("_source", {}).get("entity_name", "")

    @staticmethod
    def primary_doc_from_hit(hit: Dict) -> Optional[str]:
        """Return the primary document filename if known (from EFTS _id or index)."""
        return hit.get("_source", {}).get("primary_doc")

    @staticmethod
    def cik_from_hit(hit: Dict) -> str:
        cik = hit.get("_source", {}).get("cik", "")
        if cik:
            try:
                return str(int(cik))
            except ValueError:
                pass
        acc = hit.get("_id", "")
        if acc:
            try:
                return str(int(acc.split("-")[0]))
            except (ValueError, IndexError):
                pass
        return ""

    @staticmethod
    def cik_from_filing_id(accession: str) -> str:
        return str(int(accession.split("-")[0]))
