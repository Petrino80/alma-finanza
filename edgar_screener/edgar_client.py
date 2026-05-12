"""
Low-level HTTP client for SEC EDGAR APIs.
Enforces rate limits and provides retry logic per SEC guidelines.
"""
import time
import logging
import xml.etree.ElementTree as ET
from datetime import date, timedelta
from typing import Any, Dict, List, Optional
from urllib.parse import urlencode

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .config import cfg

logger = logging.getLogger(__name__)


class EdgarClient:
    """Thread-safe EDGAR HTTP client with automatic rate limiting."""

    def __init__(self):
        self._last_request_time: float = 0.0
        self._session = self._build_session()

    # ── session / HTTP ─────────────────────────────────────────────────────────

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
        resp = self._session.get(url, timeout=30)
        resp.raise_for_status()
        return resp

    def get_json(self, url: str, **params) -> Any:
        return self._get(url, **params).json()

    def get_text(self, url: str, **params) -> str:
        return self._get(url, **params).text

    def get_xml(self, url: str, **params) -> ET.Element:
        text = self.get_text(url, **params)
        return ET.fromstring(text)

    # ── EDGAR EFTS search ─────────────────────────────────────────────────────

    def search_filings(
        self,
        forms: List[str],
        start_date: date,
        end_date: Optional[date] = None,
        max_results: int = 200,
    ) -> List[Dict]:
        """
        Full-text search of EDGAR filings for given form types and date range.
        Returns list of filing metadata dicts.
        """
        if end_date is None:
            end_date = start_date

        all_hits: List[Dict] = []
        from_offset = 0
        page_size = 40  # EDGAR max per page

        while from_offset < max_results:
            params = {
                "forms": ",".join(forms),
                "dateRange": "custom",
                "startdt": start_date.isoformat(),
                "enddt": end_date.isoformat(),
                "from": from_offset,
                "hits.hits._source": "period_of_report,file_date,entity_name,file_num,form_type,items",
            }
            url = cfg.edgar_efts_url
            try:
                resp = self._get(url, **params)
                data = resp.json()
            except Exception as exc:
                logger.warning("EFTS search error: %s", exc)
                break

            hits = data.get("hits", {}).get("hits", [])
            if not hits:
                break
            all_hits.extend(hits)
            from_offset += len(hits)
            if len(hits) < page_size:
                break

        return all_hits

    # ── Company / ticker resolution ───────────────────────────────────────────

    _ticker_map: Optional[Dict[str, Dict]] = None  # CIK -> {cik, name, ticker}

    def _load_ticker_map(self) -> Dict[str, Dict]:
        if self.__class__._ticker_map is None:
            logger.info("Loading EDGAR company tickers…")
            data = self.get_json(f"{cfg.edgar_base_url}/files/company_tickers.json")
            self.__class__._ticker_map = {
                str(v["cik_str"]): v for v in data.values()
            }
        return self.__class__._ticker_map

    def ticker_for_cik(self, cik: str) -> Optional[str]:
        m = self._load_ticker_map()
        entry = m.get(str(int(cik)))  # normalise leading zeros
        return entry["ticker"] if entry else None

    def name_for_cik(self, cik: str) -> Optional[str]:
        m = self._load_ticker_map()
        entry = m.get(str(int(cik)))
        return entry["title"] if entry else None

    # ── Filing document fetching ───────────────────────────────────────────────

    def get_filing_index(self, cik: str, accession_no: str) -> Dict:
        """
        Fetch the JSON filing index for a given CIK + accession number.
        Accession number format: 0001234567-24-001234
        """
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
        """Fetch the raw text/XML of a specific document within a filing."""
        acc_nodash = accession_no.replace("-", "")
        cik_padded = str(int(cik)).zfill(10)
        url = (
            f"{cfg.edgar_base_url}/Archives/edgar/data/{cik_padded}/"
            f"{acc_nodash}/{filename}"
        )
        return self.get_text(url)

    def get_company_facts(self, cik: str) -> Dict:
        """XBRL company facts (multi-year financial data)."""
        cik_padded = str(int(cik)).zfill(10)
        url = f"{cfg.edgar_data_url}/api/xbrl/companyfacts/CIK{cik_padded}.json"
        try:
            return self.get_json(url)
        except Exception:
            return {}

    # ── Utility ───────────────────────────────────────────────────────────────

    @staticmethod
    def accession_from_hit(hit: Dict) -> Optional[str]:
        """Extract accession number from EFTS hit _id."""
        return hit.get("_id")  # already formatted as 0001234567-24-001234

    @staticmethod
    def filing_date_for_hit(hit: Dict) -> str:
        return hit.get("_source", {}).get("file_date", "")

    @staticmethod
    def entity_name_for_hit(hit: Dict) -> str:
        return hit.get("_source", {}).get("entity_name", "")

    @staticmethod
    def cik_from_filing_id(accession: str) -> str:
        """The first 10 digits of an accession number are the filer CIK."""
        return str(int(accession.split("-")[0]))
