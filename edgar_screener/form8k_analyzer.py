"""
Form 8-K and SC 13D/13G analyzer.

Uses Claude AI to classify 8-K filings and activist 13D/13G disclosures.
Only positive corporate events (buybacks, guidance raises, strategic deals,
activist entry) are passed to the Buffett analysis stage.
"""
import logging
import re
from dataclasses import dataclass, field
from typing import List, Optional

import anthropic

from .config import cfg
from .edgar_client import EdgarClient

logger = logging.getLogger(__name__)

# 8-K items that are worth analyzing (others are routine / irrelevant)
RELEVANT_8K_ITEMS = {
    "1.01",  # Material agreement
    "1.03",  # Bankruptcy → negative but important
    "2.01",  # Acquisition or disposition of significant assets
    "2.02",  # Results of Operations (earnings)
    "2.04",  # Triggering event for accelerated debt
    "3.01",  # Notice of rating downgrade
    "4.02",  # Restatement of financial statements → very negative
    "5.01",  # Change in control
    "5.02",  # Departure/appointment of directors or executives
    "7.01",  # Regulation FD (guidance, material info)
    "8.01",  # Other events (buybacks, special dividends, etc.)
}

SCREENING_PROMPT = """Sei un analista finanziario esperto. Analizza questo filing SEC e classifica il segnale.

Tipo di filing: {form_type}
Società: {company_name}
Data: {file_date}

TESTO DEL FILING (estratto):
{filing_text}

Rispondi SOLO con JSON valido in questo formato esatto:
{{
  "signal": "POSITIVE" | "NEUTRAL" | "NEGATIVE",
  "reason_it": "spiegazione breve in italiano (max 150 caratteri)",
  "event_type": "buyback" | "earnings_beat" | "guidance_raise" | "acquisition" | "strategic_deal" | "activist_entry" | "management_change" | "earnings_miss" | "guidance_cut" | "restatement" | "rating_downgrade" | "bankruptcy" | "routine" | "other",
  "magnitude": "HIGH" | "MEDIUM" | "LOW"
}}

Criteri:
- POSITIVE: buyback di azioni, utili sopra attese + guidance alzata, acquisizione strategica di valore, accordo rilevante, ingresso attivista noto
- NEUTRAL: cambio management senza contesto, accordi minori, aggiornamenti routinari
- NEGATIVE: mancanza utili + guidance tagliata, restatement, downgrade rating, bancarotta, scandali
"""


@dataclass
class CorporateEvent:
    form_type: str = ""
    accession_no: str = ""
    file_date: str = ""
    company_name: str = ""
    issuer_cik: str = ""
    issuer_ticker: str = ""
    signal: str = "NEUTRAL"
    reason: str = ""
    event_type: str = "other"
    magnitude: str = "LOW"
    filing_excerpt: str = ""


def _extract_filing_text(client: EdgarClient, cik: str, accession: str) -> str:
    """Download and extract text content from a filing."""
    index = client.get_filing_index(cik, accession)
    documents = index.get("documents", [])

    # Prefer the primary document (htm/txt)
    for doc in documents:
        doc_type = doc.get("type", "").upper()
        filename = doc.get("filename", "")
        if doc_type in ("8-K", "8-K/A", "SC 13D", "SC 13G", "SC 13D/A", "SC 13G/A"):
            if filename.lower().endswith((".htm", ".html", ".txt")):
                try:
                    text = client.get_filing_document(cik, accession, filename)
                    return _clean_html(text)[:6000]  # limit for AI
                except Exception:
                    continue

    # Fallback: first htm/txt document
    for doc in documents:
        fn = doc.get("filename", "")
        if fn.lower().endswith((".htm", ".html", ".txt")):
            try:
                text = client.get_filing_document(cik, accession, fn)
                return _clean_html(text)[:6000]
            except Exception:
                continue

    return ""


def _clean_html(text: str) -> str:
    """Strip HTML tags and collapse whitespace."""
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&lt;", "<", text)
    text = re.sub(r"&gt;", ">", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _has_relevant_8k_items(hit: dict) -> bool:
    """Quick check: does the 8-K contain any relevant items?"""
    source = hit.get("_source", {})
    items = source.get("items", "") or ""
    for item in RELEVANT_8K_ITEMS:
        if item in items:
            return True
    return False


def _screen_with_ai(
    ai: anthropic.Anthropic,
    form_type: str,
    company_name: str,
    file_date: str,
    filing_text: str,
) -> dict:
    """Use Claude Haiku to classify a filing. Returns parsed signal dict."""
    if not filing_text.strip():
        return {"signal": "NEUTRAL", "reason_it": "Testo non disponibile", "event_type": "routine", "magnitude": "LOW"}

    prompt = SCREENING_PROMPT.format(
        form_type=form_type,
        company_name=company_name,
        file_date=file_date,
        filing_text=filing_text[:5000],
    )
    try:
        msg = ai.messages.create(
            model=cfg.screening_model,
            max_tokens=256,
            messages=[{"role": "user", "content": prompt}],
        )
        raw = msg.content[0].text.strip()
        # Extract JSON even if model adds prose
        json_match = re.search(r"\{.*\}", raw, re.DOTALL)
        if json_match:
            import json
            return json.loads(json_match.group())
    except Exception as exc:
        logger.warning("AI screening error: %s", exc)

    return {"signal": "NEUTRAL", "reason_it": "Errore analisi AI", "event_type": "other", "magnitude": "LOW"}


def analyze_form8k_filings(
    client: EdgarClient, hits: List[dict]
) -> List[CorporateEvent]:
    """Download and screen 8-K filings; return POSITIVE events."""
    if not cfg.anthropic_api_key:
        logger.warning("ANTHROPIC_API_KEY non impostato – screening 8-K AI disabilitato")
        return []

    ai = anthropic.Anthropic(api_key=cfg.anthropic_api_key)
    positive: List[CorporateEvent] = []
    total = len(hits)

    for i, hit in enumerate(hits, 1):
        accession = client.accession_from_hit(hit)
        file_date = client.filing_date_for_hit(hit)
        company_name = client.entity_name_for_hit(hit)
        form_type = hit.get("_source", {}).get("form_type", "8-K")

        if not accession:
            continue

        # Skip 8-K without relevant items (fast filter, no HTTP needed)
        if form_type in ("8-K", "8-K/A") and not _has_relevant_8k_items(hit):
            logger.debug("[%d/%d] 8-K skip (no relevant items): %s", i, total, company_name)
            continue

        cik = client.cik_from_filing_id(accession)
        logger.info("[%d/%d] %s %s – %s", i, total, form_type, accession, company_name)

        filing_text = _extract_filing_text(client, cik, accession)
        result = _screen_with_ai(ai, form_type, company_name, file_date, filing_text)

        if result.get("signal") != "POSITIVE":
            logger.debug("  ⚪ %s: %s", result.get("signal"), result.get("reason_it"))
            continue

        ticker = client.ticker_for_cik(cik) or ""
        event = CorporateEvent(
            form_type=form_type,
            accession_no=accession,
            file_date=file_date,
            company_name=company_name,
            issuer_cik=cik,
            issuer_ticker=ticker,
            signal="POSITIVE",
            reason=result.get("reason_it", ""),
            event_type=result.get("event_type", "other"),
            magnitude=result.get("magnitude", "LOW"),
            filing_excerpt=filing_text[:800],
        )
        positive.append(event)
        logger.info("  ✅ POSITIVO [%s]: %s – %s", event.magnitude, company_name, event.reason)

    return positive


def analyze_sc13_filings(
    client: EdgarClient, hits: List[dict]
) -> List[CorporateEvent]:
    """Analyze SC 13D (activist) and SC 13G (institutional) filings."""
    if not cfg.anthropic_api_key:
        return []

    ai = anthropic.Anthropic(api_key=cfg.anthropic_api_key)
    positive: List[CorporateEvent] = []

    for hit in hits:
        accession = client.accession_from_hit(hit)
        file_date = client.filing_date_for_hit(hit)
        company_name = client.entity_name_for_hit(hit)
        form_type = hit.get("_source", {}).get("form_type", "SC 13D")

        if not accession:
            continue

        cik = client.cik_from_filing_id(accession)
        logger.info("SC 13D/G %s – %s (%s)", accession, company_name, form_type)

        filing_text = _extract_filing_text(client, cik, accession)
        result = _screen_with_ai(ai, form_type, company_name, file_date, filing_text)

        # SC 13D by known activists is inherently interesting → lower bar
        if form_type.startswith("SC 13D") and result.get("signal") != "NEGATIVE":
            result["signal"] = "POSITIVE"
            if not result.get("reason_it"):
                result["reason_it"] = "Ingresso investitore attivista (SC 13D)"

        if result.get("signal") != "POSITIVE":
            continue

        ticker = client.ticker_for_cik(cik) or ""
        event = CorporateEvent(
            form_type=form_type,
            accession_no=accession,
            file_date=file_date,
            company_name=company_name,
            issuer_cik=cik,
            issuer_ticker=ticker,
            signal="POSITIVE",
            reason=result.get("reason_it", ""),
            event_type=result.get("event_type", "activist_entry"),
            magnitude=result.get("magnitude", "MEDIUM"),
            filing_excerpt=filing_text[:800],
        )
        positive.append(event)
        logger.info("  ✅ POSITIVO SC: %s – %s", company_name, event.reason)

    return positive
