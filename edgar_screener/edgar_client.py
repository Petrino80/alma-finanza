"""
Low-level HTTP client for SEC EDGAR APIs.
Enforces rate limits and provides retry logic per SEC guidelines.

Filing search strategy (primary): EDGAR quarterly full-index crawler.idx
  https://www.sec.gov/Archives/edgar/full-index/YYYY/QTRN/crawler.idx
  Plain-text pipe-delimited file with ALL filings for the quarter.
  Filtered in-memory by date and form type. Reliable and complete.

EFTS search (fallback): used only if crawler.idx is unavailable.
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

# Cache quarterly index in memory to avoid re-downloading within the same run
_index_cache: Dict[str, List[Dict]] = {}  # "YYYY/QTRN" -> list of all filing dicts


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
        """Rate-limited GET. Raises on HTTP errors."""
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

    # ── Primary: quarterly full-index crawler.idx ─────────────────────────────

    def _load_quarterly_index(self, target_date: date) -> List[Dict]:
        """
        Download and parse the EDGAR quarterly crawler.idx.
        Returns list of all filing dicts for the quarter (cached in memory).
        Format: Company Name|Form Type|CIK|Date Filed|Filename
        """
        qtr_key = f"{target_date.year}/{_quarter(target_date)}"
        if qtr_key in _index_cache:
            return _index_cache[qtr_key]

        url = (
            f"{cfg.edgar_base_url}/Archives/edgar/full-index/"
            f"{target_date.year}/{_quarter(target_date)}/crawler.idx"
        )
        logger.info("  Scarico indice trimestrale EDGAR: %s", url)
        try:
            resp = self._get(url)
            text = resp.text
        except Exception as exc:
            logger.error("Impossibile scaricare crawler.idx: %s", exc)
            return []

        filings: List[Dict] = []
        for line in text.splitlines():
            parts = line.split("|")
            if len(parts) < 5:
                continue
            company, form_type, cik, file_date, filename = (
                parts[0].strip(), parts[1].strip(), parts[2].strip(),
                parts[3].strip(), parts[4].strip(),
            )
            # Skip header lines
            if not file_date or file_date == "Date Filed":
                continue
            # Extract accession number from filename path
            # e.g. edgar/data/1234567/0001234567-26-001234.txt
            # or   edgar/data/1234567/0001234567-26-001234-index.htm
            base = filename.split("/")[-1]
            # Remove common suffixes
            for suffix in ("-index.htm", "-index.html", ".txt"):
                if base.endswith(suffix):
                    base = base[: -len(suffix)]
                    break
            accession = base  # already in dashed format 0001234567-26-001234
            if len(accession) < 18:  # sanity check
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
        Uses quarterly full-index as primary source (reliable, complete).
        Falls back to EFTS search API if index is unavailable.
        """
        if end_date is None:
            end_date = start_date

        # ── Try full-index first ───────────────────────────────────────────────
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
                "  Trovati %d filing [%s] per %s→%s (da indice trimestrale)",
                len(results), ", ".join(forms), date_start, date_end,
            )
            return results

        # ── Fallback: EFTS search API ──────────────────────────────────────────
        logger.warning("Fallback a EFTS search (indice non disponibile)")
        return self._search_efts(forms, start_date, end_date, max_results)

    def _search_efts(
        self,
        forms: List[str],
        start_date: date,
        end_date: date,
        max_results: int,
    ) -> List[Dict]:
        all_hits: List[Dict] = []
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
            all_hits.extend(hits)
            from_offset += len(hits)
            if len(hits) < 40:
                break
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
            m = self._load_ticker_map()
            entry = m.get(str(int(cik)))
            return entry["ticker"] if entry else None
        except Exception:
            return None

    def name_for_cik(self, cik: str) -> Optional[str]:
        try:
            m = self._load_ticker_map()
            entry = m.get(str(int(cik)))
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

    # ── Hit accessors (compatible with both index and EFTS) ───────────────────

    @staticmethod
    def accession_from_hit(hit: Dict) -> Optional[str]:
        return hit.get("_id")

    @staticmethod
    def filing_date_for_hit(hit: Dict) -> str:
        return hit.get("_source", {}).get("file_date", "")

    @staticmethod
    def entity_name_for_hit(hit: Dict) -> str:
        return hit.get("_source", {}).get("entity_name", "")

    @staticmethod
    def cik_from_hit(hit: Dict) -> str:
        """CIK from the index source field (preferred over parsing accession)."""
        cik = hit.get("_source", {}).get("cik", "")
        if cik:
            return str(int(cik))
        # Fallback: first segment of accession number
        acc = hit.get("_id", "")
        if acc:
            return str(int(acc.split("-")[0]))
        return ""

    @staticmethod
    def cik_from_filing_id(accession: str) -> str:
        return str(int(accession.split("-")[0]))
