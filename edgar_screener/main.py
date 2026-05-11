"""
Main orchestrator for the SEC EDGAR daily screening pipeline.

Pipeline steps:
  1. Download Form 4, 8-K, SC 13D/13G filings for target date from EDGAR
  2. Screen Form 4 for insider open-market purchases (positive signal)
  3. Screen 8-K / SC 13D with Claude AI for positive corporate events
  4. De-duplicate companies and run Warren Buffett fundamental analysis
  5. Run Claude AI analysis to build investment thesis per company
  6. Generate final shortlist with Claude Opus
  7. Write HTML + JSON reports to edgar_output/
"""
import logging
import os
import sys
from datetime import date, timedelta
from typing import List, Optional

from .buffett_analyzer import analyze_companies
from .config import cfg
from .edgar_client import EdgarClient
from .form4_analyzer import analyze_form4_filings
from .form8k_analyzer import analyze_form8k_filings, analyze_sc13_filings
from .ai_analyst import run_full_analysis
from .report_generator import generate_html_report, generate_json_report

logger = logging.getLogger(__name__)


def run_screening(target_date: Optional[date] = None) -> dict:
    """
    Run the full screening pipeline for target_date (defaults to yesterday
    to capture all filings including after-hours).

    Returns a summary dict with counts and output file paths.
    """
    if target_date is None:
        # At 22:00 Italian time we look at today's filings
        target_date = date.today()

    date_str = target_date.isoformat()
    logger.info("=" * 70)
    logger.info("SEC EDGAR Screening – %s", date_str)
    logger.info("=" * 70)

    client = EdgarClient()

    # ── 1. Download filing metadata ────────────────────────────────────────────
    logger.info("📥 Download Form 4 da EDGAR…")
    form4_hits = client.search_filings(
        forms=["4", "4/A"],
        start_date=target_date,
        max_results=cfg.max_results_per_form,
    )
    logger.info("  → %d Form 4 trovati", len(form4_hits))

    logger.info("📥 Download 8-K da EDGAR…")
    form8k_hits = client.search_filings(
        forms=["8-K", "8-K/A"],
        start_date=target_date,
        max_results=cfg.max_results_per_form,
    )
    logger.info("  → %d Form 8-K trovati", len(form8k_hits))

    logger.info("📥 Download SC 13D/13G da EDGAR…")
    sc13_hits = client.search_filings(
        forms=["SC 13D", "SC 13D/A", "SC 13G", "SC 13G/A"],
        start_date=target_date,
        max_results=50,
    )
    logger.info("  → %d SC 13D/13G trovati", len(sc13_hits))

    # ── 2. Screen Form 4 for insider purchases ─────────────────────────────────
    logger.info("\n🔍 Screening Form 4 (insider buying)…")
    insider_positives = analyze_form4_filings(client, form4_hits)
    logger.info("  → %d insider buy positivi", len(insider_positives))

    # ── 3. Screen 8-K and SC 13D with AI ──────────────────────────────────────
    logger.info("\n🤖 Screening 8-K con AI…")
    corporate_positives = analyze_form8k_filings(client, form8k_hits)
    logger.info("  → %d eventi aziendali positivi", len(corporate_positives))

    logger.info("\n🤖 Screening SC 13D/13G con AI…")
    sc13_positives = analyze_sc13_filings(client, sc13_hits)
    logger.info("  → %d segnali attivisti positivi", len(sc13_positives))

    all_corporate = corporate_positives + sc13_positives

    # Early exit if nothing positive
    if not insider_positives and not all_corporate:
        logger.info("\n⚪ Nessun segnale positivo rilevato oggi. Nessun report generato.")
        return {"status": "no_signals", "date": date_str}

    # ── 4. Collect unique tickers for Buffett analysis ─────────────────────────
    logger.info("\n📊 Analisi fondamentale Warren Buffett…")
    ticker_set: set = set()
    for tx in insider_positives:
        if tx.issuer_ticker:
            ticker_set.add(tx.issuer_ticker.upper())
    for ev in all_corporate:
        if ev.issuer_ticker:
            ticker_set.add(ev.issuer_ticker.upper())

    # Limit to avoid excessive API calls / time
    tickers = sorted(ticker_set)[: cfg.max_companies_to_analyze]
    logger.info("  → %d aziende uniche da analizzare: %s", len(tickers), ", ".join(tickers))

    buffett_scores = analyze_companies(tickers)
    logger.info("  → %d punteggi Buffett calcolati", len(buffett_scores))

    # ── 5-6. AI analysis + shortlist ──────────────────────────────────────────
    logger.info("\n💡 Analisi AI investment thesis + shortlist…")
    opportunities, shortlist = run_full_analysis(
        insider_positives=insider_positives,
        corporate_positives=all_corporate,
        buffett_scores=buffett_scores,
        analysis_date=date_str,
    )

    # ── 7. Write reports ───────────────────────────────────────────────────────
    os.makedirs(cfg.output_dir, exist_ok=True)
    html_path = os.path.join(cfg.output_dir, f"report_{date_str}.html")
    json_path = os.path.join(cfg.output_dir, f"report_{date_str}.json")

    generate_html_report(opportunities, shortlist, date_str, html_path)
    generate_json_report(
        opportunities,
        shortlist,
        insider_raw_count=len(form4_hits),
        corporate_raw_count=len(form8k_hits) + len(sc13_hits),
        analysis_date=date_str,
        output_path=json_path,
    )

    # Also write a "latest" symlink-style copy for easy access
    latest_html = os.path.join(cfg.output_dir, "report_latest.html")
    latest_json = os.path.join(cfg.output_dir, "report_latest.json")
    import shutil
    shutil.copy2(html_path, latest_html)
    shutil.copy2(json_path, latest_json)

    logger.info("\n✅ Screening completato!")
    logger.info("  Report HTML: %s", html_path)
    logger.info("  Report JSON: %s", json_path)
    logger.info(
        "  Shortlist: %d opportunità in %d totali analizzate",
        len(shortlist.get("shortlist", [])),
        len(opportunities),
    )

    return {
        "status": "ok",
        "date": date_str,
        "form4_hits": len(form4_hits),
        "form8k_hits": len(form8k_hits),
        "sc13_hits": len(sc13_hits),
        "insider_positives": len(insider_positives),
        "corporate_positives": len(all_corporate),
        "opportunities": len(opportunities),
        "shortlist_count": len(shortlist.get("shortlist", [])),
        "html_report": html_path,
        "json_report": json_path,
    }
