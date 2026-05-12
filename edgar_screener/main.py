"""
Main orchestrator for the SEC EDGAR daily screening pipeline.

Pipeline steps:
  1. Download Form 4, 8-K, SC 13D/13G filings for target date from EDGAR
  2. Save raw form documents to edgar_output/forms/ (browsable)
  3. Screen Form 4 for insider open-market purchases (positive signal)
  4. Screen 8-K / SC 13D with Claude AI for positive corporate events
  5. De-duplicate companies and run Warren Buffett fundamental analysis
  6. Run Claude AI analysis to build investment thesis per company
  7. Generate final shortlist with Claude Opus
  8. Write HTML + JSON reports to edgar_output/
"""
import logging
import os
import re
import shutil
from datetime import date
from typing import Dict, List, Optional

from .buffett_analyzer import analyze_companies
from .config import cfg
from .edgar_client import EdgarClient
from .form4_analyzer import analyze_form4_filings
from .form8k_analyzer import analyze_form8k_filings, analyze_sc13_filings, _clean_html
from .ai_analyst import run_full_analysis
from .report_generator import generate_html_report, generate_json_report

logger = logging.getLogger(__name__)


def _save_forms(
    client: EdgarClient,
    hits: List[dict],
    form_type: str,
    base_dir: str,
    max_save: int = 50,
) -> List[Dict]:
    """
    Download and save the first max_save form documents regardless of signal.
    Uses primary_doc from the hit when available (EFTS), falls back to filing index.
    Returns list of saved file metadata for the index page.
    """
    saved = []
    folder = os.path.join(base_dir, form_type.replace(" ", "_").replace("/", "_"))
    os.makedirs(folder, exist_ok=True)

    # Limit to first max_save hits
    for hit in hits[:max_save]:
        accession = client.accession_from_hit(hit)
        entity = client.entity_name_for_hit(hit)
        file_date = client.filing_date_for_hit(hit)
        if not accession:
            continue

        cik = client.cik_from_hit(hit)
        ticker = client.ticker_for_cik(cik) or ""

        # 1. Try primary_doc embedded in hit (from EFTS or form.idx)
        primary_file = client.primary_doc_from_hit(hit)

        # 2. Fallback: fetch filing index JSON
        if not primary_file:
            index = client.get_filing_index(cik, accession)
            documents = index.get("documents", [])
            for doc in documents:
                dt = doc.get("type", "").upper().replace("/A", "").strip()
                fn = doc.get("filename", "")
                if dt in ("4", "8-K", "SC 13D", "SC 13G") and fn.lower().endswith(
                    (".xml", ".htm", ".html", ".txt")
                ):
                    primary_file = fn
                    break
            # Any htm/txt/xml if still nothing
            if not primary_file:
                for doc in documents:
                    fn = doc.get("filename", "")
                    if fn.lower().endswith((".htm", ".html", ".txt", ".xml")):
                        primary_file = fn
                        break

        # 3. Last resort: guess filename from accession
        if not primary_file:
            acc_nodash = accession.replace("-", "")
            primary_file = f"{acc_nodash}.xml" if form_type == "4" else f"{acc_nodash}.htm"

        try:
            raw = client.get_filing_document(cik, accession, primary_file)
        except Exception as exc:
            logger.debug("Skip %s (%s): %s", accession, primary_file, exc)
            continue

        # Save as HTML for easy browser viewing
        safe_name = re.sub(r"[^a-zA-Z0-9_\-]", "_", accession)
        out_filename = f"{file_date}_{safe_name}.html"
        out_path = os.path.join(folder, out_filename)

        if primary_file.endswith(".xml"):
            content = (
                f"<!DOCTYPE html><html><head><meta charset='UTF-8'>"
                f"<title>{entity} – {form_type} – {file_date}</title>"
                f"<style>body{{font-family:monospace;white-space:pre-wrap;padding:20px}}"
                f"</style></head><body>{raw.replace('<','&lt;').replace('>','&gt;')}"
                f"</body></html>"
            )
        else:
            header = (
                f"<div style='background:#1e3a5f;color:white;padding:12px 20px;"
                f"font-family:sans-serif'>"
                f"<strong>{entity}</strong> &nbsp;|&nbsp; {form_type} &nbsp;|&nbsp; {file_date}"
                f"&nbsp;|&nbsp; Ticker: {ticker or 'N/D'}"
                f"&nbsp;&nbsp;<a href='../forms_index.html' style='color:#93c5fd'>← Tutti i form</a>"
                f"</div>"
            )
            content = header + raw

        with open(out_path, "w", encoding="utf-8", errors="replace") as f:
            f.write(content)

        saved.append({
            "form_type": form_type,
            "entity": entity,
            "ticker": ticker,
            "cik": cik,
            "date": file_date,
            "accession": accession,
            "file": out_path,
            "filename": out_filename,
            "folder": form_type.replace(" ", "_").replace("/", "_"),
        })

    logger.info("  → %d file %s salvati in %s", len(saved), form_type, folder)
    return saved


def _generate_forms_index(all_saved: List[Dict], date_str: str, output_dir: str) -> None:
    """Generate a browsable HTML index of all downloaded forms."""
    by_type: Dict[str, List[Dict]] = {}
    for s in all_saved:
        by_type.setdefault(s["form_type"], []).append(s)

    sections = ""
    for ftype, items in sorted(by_type.items()):
        rows = ""
        for item in sorted(items, key=lambda x: x["entity"]):
            rel_path = os.path.join(item["folder"], item["filename"])
            rows += (
                f"<tr>"
                f"<td><a href='{rel_path}' target='_blank'>{item['entity']}</a></td>"
                f"<td><strong>{item['ticker'] or '—'}</strong></td>"
                f"<td>{item['date']}</td>"
                f"<td style='font-size:0.8rem;color:#6b7280'>{item['accession']}</td>"
                f"</tr>"
            )
        sections += f"""
        <h2 style='margin:24px 0 8px;color:#1e3a5f'>{ftype} ({len(items)} filing)</h2>
        <table style='width:100%;border-collapse:collapse;font-size:0.9rem'>
          <thead><tr style='background:#f3f4f6'>
            <th style='padding:8px;text-align:left'>Azienda</th>
            <th>Ticker</th><th>Data</th><th>Accession</th>
          </tr></thead>
          <tbody>{rows}</tbody>
        </table>"""

    html = f"""<!DOCTYPE html>
<html lang='it'>
<head><meta charset='UTF-8'>
<title>Form SEC scaricati – {date_str} | Alma Finanza</title>
<style>
  body{{font-family:'Inter',sans-serif;background:#f1f5f9;color:#111827;padding:24px;max-width:1100px;margin:0 auto}}
  table th,table td{{padding:8px 12px;border:1px solid #e5e7eb;text-align:left}}
  a{{color:#2563eb;text-decoration:none}} a:hover{{text-decoration:underline}}
</style>
</head>
<body>
  <div style='background:linear-gradient(135deg,#1e3a5f,#2563eb);color:white;
              border-radius:12px;padding:20px;margin-bottom:24px'>
    <div style='font-size:0.85rem;opacity:0.8'>Alma Finanza · SEC EDGAR Raw Forms</div>
    <h1 style='color:white;margin:4px 0'>📂 Form SEC scaricati – {date_str}</h1>
    <p style='opacity:0.9;margin:4px 0'>{len(all_saved)} documenti totali &nbsp;|&nbsp;
      <a href='report_latest.html' style='color:#93c5fd'>→ Apri Report Analisi</a>
    </p>
  </div>
  {sections if sections else "<p>Nessun form scaricato.</p>"}
  <div style='margin-top:24px;font-size:0.8rem;color:#9ca3af'>
    Fonte: SEC EDGAR · Alma Finanza · {date_str}
  </div>
</body>
</html>"""

    index_path = os.path.join(output_dir, "forms_index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)
    logger.info("  → Indice form: %s", index_path)


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

    # ── 2. Save raw forms to disk (browsable) ─────────────────────────────────
    forms_dir = os.path.join(cfg.output_dir, f"forms_{date_str}")
    logger.info("\n💾 Salvataggio form su disco in %s…", forms_dir)
    all_saved: List[Dict] = []
    all_saved += _save_forms(client, form4_hits, "4", forms_dir)
    all_saved += _save_forms(client, form8k_hits, "8-K", forms_dir)
    all_saved += _save_forms(client, sc13_hits, "SC 13D", forms_dir)
    _generate_forms_index(all_saved, date_str, forms_dir)
    # Copy index to output root for easy access
    shutil.copy2(
        os.path.join(forms_dir, "forms_index.html"),
        os.path.join(cfg.output_dir, "forms_index.html"),
    )
    logger.info("  → Totale form salvati: %d", len(all_saved))

    # ── 3. Screen Form 4 for insider purchases ─────────────────────────────────
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

    # Early exit if nothing positive – but forms_index is already saved above
    if not insider_positives and not all_corporate:
        from . import edgar_client as _ec_mod
        if _ec_mod.edgar_blocked:
            logger.error(
                "\n🚫 EDGAR bloccato (403): impossibile scaricare i filing. "
                "L'IP di questo ambiente è probabilmente in una subnet cloud "
                "bloccata da SEC. Esegui lo script da un IP residenziale/aziendale."
            )
            return {
                "status": "edgar_blocked",
                "date": date_str,
                "form4_hits": 0,
                "form8k_hits": 0,
                "sc13_hits": 0,
                "forms_saved": 0,
                "forms_index": os.path.join(cfg.output_dir, "forms_index.html"),
                "error": "EDGAR ha rifiutato le richieste con 403 Forbidden (IP bloccato)",
            }
        logger.info(
            "\n⚪ Nessun segnale positivo rilevato oggi. "
            "I form scaricati sono comunque disponibili in: %s",
            os.path.join(cfg.output_dir, "forms_index.html"),
        )
        return {
            "status": "no_signals",
            "date": date_str,
            "form4_hits": len(form4_hits),
            "form8k_hits": len(form8k_hits),
            "sc13_hits": len(sc13_hits),
            "forms_saved": len(all_saved),
            "forms_index": os.path.join(cfg.output_dir, "forms_index.html"),
        }

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
        "forms_saved": len(all_saved),
        "forms_index": os.path.join(cfg.output_dir, "forms_index.html"),
        "insider_positives": len(insider_positives),
        "corporate_positives": len(all_corporate),
        "opportunities": len(opportunities),
        "shortlist_count": len(shortlist.get("shortlist", [])),
        "html_report": html_path,
        "json_report": json_path,
    }
