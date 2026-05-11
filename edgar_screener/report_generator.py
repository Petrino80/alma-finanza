"""
Report generator.
Produces:
  1. A JSON file with full structured data (for programmatic use)
  2. An HTML report (human-readable, Italian)
"""
import json
import logging
import os
from datetime import datetime
from typing import Any, Dict, List

from .ai_analyst import InvestmentOpportunity
from .buffett_analyzer import BuffettScore
from .config import cfg

logger = logging.getLogger(__name__)

# ── Grade color mapping ────────────────────────────────────────────────────────
GRADE_COLORS = {
    "A+": ("#065f46", "#d1fae5"),  # dark green bg, light green text
    "A":  ("#1e40af", "#dbeafe"),
    "B":  ("#92400e", "#fef3c7"),
    "C":  ("#7c3aed", "#ede9fe"),
    "D":  ("#9a3412", "#ffedd5"),
    "F":  ("#991b1b", "#fee2e2"),
}

CONVICTION_COLORS = {
    "ALTA":  "#065f46",
    "MEDIA": "#92400e",
    "BASSA": "#991b1b",
}


def _gauge_bar(score: int, max_score: int, color: str = "#2563eb") -> str:
    pct = min(100, int(score / max_score * 100))
    return (
        f'<div style="background:#e5e7eb;border-radius:4px;height:8px;margin:2px 0">'
        f'<div style="width:{pct}%;background:{color};height:100%;border-radius:4px"></div></div>'
        f'<small style="color:#6b7280">{score}/{max_score}</small>'
    )


def _metric_cell(label: str, value, suffix: str = "%", na: str = "N/D") -> str:
    if value is None:
        disp = na
        color = "#9ca3af"
    else:
        try:
            disp = f"{float(value):.1f}{suffix}"
            color = "#111827"
        except (TypeError, ValueError):
            disp = str(value)
            color = "#111827"
    return (
        f'<div style="text-align:center;padding:8px">'
        f'<div style="font-size:1.1rem;font-weight:700;color:{color}">{disp}</div>'
        f'<div style="font-size:0.7rem;color:#6b7280;margin-top:2px">{label}</div>'
        f'</div>'
    )


def _opportunity_card(opp: InvestmentOpportunity) -> str:
    bs = opp.buffett_score
    grade = bs.grade if bs else "N/D"
    grade_bg, grade_fg = GRADE_COLORS.get(grade, ("#374151", "#f9fafb"))
    conviction_color = CONVICTION_COLORS.get(opp.conviction, "#374151")

    insider_count = len(opp.insider_buys)
    total_insider_usd = sum(t.value_usd for t in opp.insider_buys)
    event_count = len(opp.corporate_events)

    insider_html = ""
    if opp.insider_buys:
        rows = "".join(
            f"<tr><td>{t.owner_name}</td><td>{t.owner_title or '—'}</td>"
            f"<td><strong>${t.value_usd:,.0f}</strong></td>"
            f"<td>{t.shares:,.0f} @ ${t.price:.2f}</td><td>{t.file_date}</td></tr>"
            for t in opp.insider_buys
        )
        insider_html = f"""
        <h4 style="margin:16px 0 8px;color:#1f2937">🔺 Insider Buy (Form 4)</h4>
        <div style="overflow-x:auto">
        <table style="width:100%;border-collapse:collapse;font-size:0.85rem">
          <thead><tr style="background:#f3f4f6">
            <th style="padding:6px;text-align:left">Insider</th>
            <th>Ruolo</th><th>Valore</th><th>Dettaglio</th><th>Data</th>
          </tr></thead>
          <tbody>{rows}</tbody>
        </table></div>"""

    events_html = ""
    if opp.corporate_events:
        ev_items = "".join(
            f"<li><strong>{ev.form_type}</strong> ({ev.event_type}): {ev.reason}</li>"
            for ev in opp.corporate_events
        )
        events_html = f"""
        <h4 style="margin:16px 0 8px;color:#1f2937">📋 Eventi Aziendali</h4>
        <ul style="margin:0;padding-left:20px;font-size:0.9rem">{ev_items}</ul>"""

    buffett_html = ""
    if bs:
        buffett_html = f"""
        <h4 style="margin:16px 0 8px;color:#1f2937">📊 Analisi Buffett</h4>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(100px,1fr));gap:8px;
                    background:#f9fafb;border-radius:8px;padding:12px;margin-bottom:12px">
          {_metric_cell("ROE", bs.roe)}
          {_metric_cell("Margine lordo", bs.gross_margin)}
          {_metric_cell("Margine netto", bs.net_margin)}
          {_metric_cell("Debito/EQ", bs.debt_equity, "x")}
          {_metric_cell("P/E", bs.pe_ratio, "x")}
          {_metric_cell("FCF yield", bs.fcf_yield)}
          {_metric_cell("EV/EBITDA", bs.ev_ebitda, "x")}
          {_metric_cell("Crescita RIC", bs.revenue_growth_3y)}
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:8px;font-size:0.8rem">
          <div><strong>Moat</strong><br>{_gauge_bar(bs.moat_score, 30, "#10b981")}</div>
          <div><strong>Fortezza</strong><br>{_gauge_bar(bs.fortress_score, 25, "#2563eb")}</div>
          <div><strong>Management</strong><br>{_gauge_bar(bs.management_score, 20, "#7c3aed")}</div>
          <div><strong>Valutazione</strong><br>{_gauge_bar(bs.valuation_score, 25, "#f59e0b")}</div>
        </div>
        {"<div style='margin-top:10px'><strong style='color:#065f46'>✅ Punti di forza:</strong><ul style='font-size:0.85rem;margin:4px 0;padding-left:18px'>" + "".join(f"<li>{s}</li>" for s in bs.strengths) + "</ul></div>" if bs.strengths else ""}
        {"<div style='margin-top:6px'><strong style='color:#991b1b'>⚠️ Preoccupazioni:</strong><ul style='font-size:0.85rem;margin:4px 0;padding-left:18px'>" + "".join(f"<li>{c}</li>" for c in bs.concerns) + "</ul></div>" if bs.concerns else ""}
        """

    thesis_html = ""
    if opp.thesis and opp.thesis != "Analisi non disponibile":
        thesis_html = f"""
        <h4 style="margin:16px 0 8px;color:#1f2937">💡 Tesi di Investimento</h4>
        <div style="background:#eff6ff;border-left:4px solid #2563eb;padding:12px;
                    border-radius:0 8px 8px 0;font-size:0.9rem;line-height:1.6">
          {opp.thesis}
        </div>"""
        if opp.catalysts:
            thesis_html += f"""
        <h4 style="margin:12px 0 4px;color:#1f2937">🚀 Catalizzatori</h4>
        <div style="font-size:0.85rem">{opp.catalysts}</div>"""
        if opp.risks:
            thesis_html += f"""
        <h4 style="margin:12px 0 4px;color:#1f2937">⚠️ Rischi</h4>
        <div style="font-size:0.85rem">{opp.risks}</div>"""

    return f"""
    <div style="background:white;border:1px solid #e5e7eb;border-radius:12px;
                margin-bottom:24px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.06)">
      <!-- header -->
      <div style="padding:16px 20px;display:flex;align-items:center;justify-content:space-between;
                  border-bottom:1px solid #e5e7eb;background:#fafafa">
        <div>
          <span style="font-size:1.5rem;font-weight:800;color:#111827">#{opp.rank} {opp.ticker}</span>
          <span style="font-size:1rem;color:#6b7280;margin-left:10px">{opp.company_name}</span>
          <span style="font-size:0.8rem;color:#9ca3af;margin-left:8px">{opp.sector}</span>
        </div>
        <div style="display:flex;align-items:center;gap:10px">
          <div style="background:{grade_bg};color:{grade_fg};padding:6px 14px;border-radius:20px;
                      font-weight:700;font-size:1.1rem">Grade {grade}</div>
          <div style="background:#f3f4f6;padding:6px 12px;border-radius:20px;font-size:0.85rem">
            Score AI: <strong>{opp.final_score:.1f}/10</strong>
          </div>
          <div style="color:{conviction_color};font-weight:700;font-size:0.9rem">
            Conviction: {opp.conviction}
          </div>
        </div>
      </div>
      <!-- signal badges -->
      <div style="padding:10px 20px;background:#f0fdf4;border-bottom:1px solid #d1fae5;
                  display:flex;gap:10px;flex-wrap:wrap">
        {f'<span style="background:#dcfce7;color:#166534;padding:3px 10px;border-radius:12px;font-size:0.8rem">🔺 {insider_count} Insider Buy – ${total_insider_usd:,.0f}</span>' if insider_count else ""}
        {f'<span style="background:#dbeafe;color:#1e40af;padding:3px 10px;border-radius:12px;font-size:0.8rem">📋 {event_count} {"Eventi" if event_count > 1 else "Evento"} aziendale</span>' if event_count else ""}
        {f'<span style="background:#fef9c3;color:#854d0e;padding:3px 10px;border-radius:12px;font-size:0.8rem">⏱ Orizzonte: {opp.time_horizon} termine</span>' if opp.time_horizon else ""}
        {f'<span style="background:#e0e7ff;color:#3730a3;padding:3px 10px;border-radius:12px;font-size:0.8rem">📈 {opp.expected_return}</span>' if opp.expected_return else ""}
      </div>
      <!-- body -->
      <div style="padding:16px 20px">
        {insider_html}
        {events_html}
        {buffett_html}
        {thesis_html}
      </div>
    </div>"""


def generate_html_report(
    opportunities: List[InvestmentOpportunity],
    shortlist: Dict[str, Any],
    analysis_date: str,
    output_path: str,
) -> None:
    """Write the full HTML report."""

    shortlist_items = shortlist.get("shortlist", [])
    market_context = shortlist.get("market_context", "")

    shortlist_html = ""
    for item in shortlist_items:
        pot_color = {"Alto": "#065f46", "Medio": "#92400e", "Speculativo": "#991b1b"}.get(
            item.get("potenziale", ""), "#374151"
        )
        shortlist_html += f"""
        <div style="background:white;border:1px solid #e5e7eb;border-radius:10px;
                    padding:16px;margin-bottom:14px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
            <div>
              <span style="font-size:1.3rem;font-weight:800">#{item.get('rank')} {item.get('ticker')}</span>
              <span style="color:#6b7280;margin-left:8px">{item.get('company')}</span>
            </div>
            <div style="display:flex;gap:8px">
              <span style="background:#f3f4f6;padding:3px 10px;border-radius:12px;font-size:0.8rem">
                Rischio: {item.get('rischio')}
              </span>
              <span style="color:{pot_color};font-weight:700">{item.get('potenziale')}</span>
            </div>
          </div>
          <p style="margin:0 0 8px;font-size:0.9rem">{item.get('perche_comprare','')}</p>
          <div style="display:flex;gap:10px;font-size:0.8rem;color:#6b7280">
            <span>⏱ {item.get('orizzonte')}</span>
            <span>→ <strong>{item.get('azione_suggerita')}</strong></span>
          </div>
        </div>"""

    cards_html = "".join(_opportunity_card(opp) for opp in opportunities)

    html = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SEC EDGAR Screening – {analysis_date} | Alma Finanza</title>
<style>
  * {{box-sizing:border-box;margin:0;padding:0}}
  body {{font-family:'Inter','Segoe UI',sans-serif;background:#f1f5f9;color:#111827;line-height:1.5}}
  .container {{max-width:1100px;margin:0 auto;padding:24px}}
  h1 {{font-size:1.8rem;font-weight:800;color:#1e3a5f}}
  h2 {{font-size:1.3rem;font-weight:700;color:#1e3a5f;margin:24px 0 12px}}
  h3 {{font-size:1.1rem;font-weight:600;margin:0 0 8px}}
  table th,table td {{padding:6px 10px;border:1px solid #e5e7eb;text-align:left}}
  table {{border-collapse:collapse;width:100%}}
</style>
</head>
<body>
<div class="container">
  <div style="background:linear-gradient(135deg,#1e3a5f,#2563eb);color:white;
              border-radius:12px;padding:24px;margin-bottom:24px">
    <div style="font-size:0.85rem;opacity:0.8;margin-bottom:4px">Alma Finanza · SEC EDGAR Daily Screener</div>
    <h1 style="color:white">📊 Report Investimenti SEC – {analysis_date}</h1>
    <p style="margin-top:8px;opacity:0.9">
      Analisi automatica dei filing SEC con screening Warren Buffett e intelligenza artificiale.
      {len(opportunities)} opportunità rilevate · {len(shortlist_items)} in shortlist finale.
    </p>
  </div>

  <!-- SHORTLIST -->
  <div style="background:white;border-radius:12px;padding:20px;margin-bottom:24px;
              border:2px solid #fbbf24;box-shadow:0 4px 12px rgba(251,191,36,0.15)">
    <h2 style="color:#92400e;margin-top:0">⭐ Shortlist Finale – Top Opportunità</h2>
    {shortlist_html if shortlist_html else "<p style='color:#6b7280'>Nessuna opportunità qualificata oggi.</p>"}
    {f'<div style="margin-top:14px;padding:12px;background:#fef3c7;border-radius:8px;font-size:0.85rem;color:#92400e"><strong>Contesto di mercato:</strong> {market_context}</div>' if market_context else ""}
  </div>

  <!-- ALL OPPORTUNITIES -->
  <h2>📋 Tutte le Opportunità Analizzate ({len(opportunities)})</h2>
  {cards_html if cards_html else '<p style="color:#6b7280;background:white;padding:20px;border-radius:8px">Nessuna opportunità con segnale positivo rilevata nei filing di oggi.</p>'}

  <!-- FOOTER -->
  <div style="margin-top:32px;padding:16px;background:#f8fafc;border-radius:8px;
              font-size:0.8rem;color:#6b7280;border:1px solid #e2e8f0">
    <strong>⚠️ Disclaimer:</strong> Questo report è generato automaticamente da algoritmi e intelligenza artificiale
    a scopo informativo ed educativo. Non costituisce consulenza finanziaria. I dati provengono da
    fonti pubbliche (SEC EDGAR, Yahoo Finance). Prima di investire, consulta un professionista abilitato.
    Dati aggiornati al: {datetime.now().strftime("%d/%m/%Y %H:%M")} (ora italiana).
    <br><br>Alma Finanza · Portale di educazione finanziaria in italiano · Metodologia: SEC EDGAR + Warren Buffett Framework + Claude AI
  </div>
</div>
</body>
</html>"""

    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    logger.info("Report HTML scritto: %s", output_path)


def generate_json_report(
    opportunities: List[InvestmentOpportunity],
    shortlist: Dict[str, Any],
    insider_raw_count: int,
    corporate_raw_count: int,
    analysis_date: str,
    output_path: str,
) -> None:
    """Write structured JSON report."""

    def opp_to_dict(opp: InvestmentOpportunity) -> dict:
        bs = opp.buffett_score
        return {
            "rank": opp.rank,
            "ticker": opp.ticker,
            "company_name": opp.company_name,
            "sector": opp.sector,
            "final_score": opp.final_score,
            "conviction": opp.conviction,
            "expected_return": opp.expected_return,
            "time_horizon": opp.time_horizon,
            "thesis": opp.thesis,
            "catalysts": opp.catalysts,
            "risks": opp.risks,
            "insider_buys": [
                {
                    "owner": t.owner_name,
                    "title": t.owner_title,
                    "shares": t.shares,
                    "price": t.price,
                    "value_usd": t.value_usd,
                    "date": t.file_date,
                }
                for t in opp.insider_buys
            ],
            "corporate_events": [
                {
                    "form_type": e.form_type,
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "magnitude": e.magnitude,
                    "date": e.file_date,
                }
                for e in opp.corporate_events
            ],
            "buffett": {
                "total_score": bs.total_score if bs else None,
                "grade": bs.grade if bs else None,
                "roe": bs.roe if bs else None,
                "gross_margin": bs.gross_margin if bs else None,
                "net_margin": bs.net_margin if bs else None,
                "debt_equity": bs.debt_equity if bs else None,
                "pe_ratio": bs.pe_ratio if bs else None,
                "fcf_yield": bs.fcf_yield if bs else None,
                "strengths": bs.strengths if bs else [],
                "concerns": bs.concerns if bs else [],
                "verdict": bs.verdict if bs else "",
            } if bs else None,
        }

    report = {
        "meta": {
            "analysis_date": analysis_date,
            "generated_at": datetime.now().isoformat(),
            "total_form4_analyzed": insider_raw_count,
            "total_8k_analyzed": corporate_raw_count,
            "opportunities_found": len(opportunities),
        },
        "shortlist": shortlist,
        "opportunities": [opp_to_dict(opp) for opp in opportunities],
    }

    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    logger.info("Report JSON scritto: %s", output_path)
