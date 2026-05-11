"""
AI-powered investment analyst using Claude.

Takes the positive signals (Form 4 insider buys, 8-K events, SC 13D)
combined with Warren Buffett scores and produces:
  - A narrative investment thesis in Italian
  - A risk/opportunity rating
  - A final shortlist with ranked investment opportunities
"""
import json
import logging
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

import anthropic

from .buffett_analyzer import BuffettScore
from .config import cfg
from .form4_analyzer import InsiderTransaction
from .form8k_analyzer import CorporateEvent

logger = logging.getLogger(__name__)


@dataclass
class InvestmentOpportunity:
    ticker: str
    company_name: str
    sector: str = ""
    # Signals that triggered this opportunity
    insider_buys: List[InsiderTransaction] = field(default_factory=list)
    corporate_events: List[CorporateEvent] = field(default_factory=list)
    # Fundamental analysis
    buffett_score: Optional[BuffettScore] = None
    # AI analysis
    thesis: str = ""          # Investment thesis in Italian
    risks: str = ""
    catalysts: str = ""
    time_horizon: str = ""    # "breve" | "medio" | "lungo" termine
    conviction: str = ""      # "ALTA" | "MEDIA" | "BASSA"
    expected_return: str = "" # "Alto potenziale" | "Moderato" | "Speculativo"
    final_score: float = 0.0  # 0-10
    rank: int = 0


ANALYSIS_PROMPT = """Sei un analista finanziario senior specializzato in value investing, metodologia Warren Buffett.

Hai ricevuto i seguenti dati su {company} (ticker: {ticker}):

## SEGNALI DAI FILING SEC
{signals_text}

## ANALISI FONDAMENTALE (Metodo Warren Buffett)
Punteggio Buffett: {buffett_total}/100 (Grade: {buffett_grade})
- Moat (vantaggio competitivo): {moat}/30
- Fortezza finanziaria: {fortress}/25
- Qualità management: {mgmt}/20
- Valutazione: {valuation}/25

Metriche chiave:
- ROE: {roe}
- Margine lordo: {gross_margin}
- Margine netto: {net_margin}
- Debito/Equity: {debt_equity}
- P/E: {pe}
- EV/EBITDA: {ev_ebitda}
- FCF yield: {fcf_yield}
- Crescita ricavi: {rev_growth}

Punti di forza: {strengths}
Preoccupazioni: {concerns}

## ISTRUZIONE
Produci un'analisi di investimento professionale in italiano. Rispondi SOLO con JSON valido:
{{
  "thesis": "Tesi di investimento narrativa (2-3 paragrafi, tono professionale, riferimenti a Buffett)",
  "catalysts": "Catalizzatori principali che potrebbero sbloccare valore (bullet points in italiano)",
  "risks": "Rischi principali da monitorare (bullet points in italiano)",
  "time_horizon": "breve" oppure "medio" oppure "lungo",
  "conviction": "ALTA" oppure "MEDIA" oppure "BASSA",
  "expected_return": "Alto potenziale (>30% a 12m)" oppure "Moderato (10-30%)" oppure "Speculativo (<10% atteso o alta incertezza)",
  "final_score": <float 0.0-10.0>,
  "summary_it": "Riassunto in 2 righe per lettori non esperti"
}}
"""

SHORTLIST_PROMPT = """Sei il chief investment officer di un fondo value italiano.

Hai analizzato {n} opportunità di investimento emerse dai filing SEC di oggi ({date}).
Ecco i dati sintetici:

{opportunities_summary}

Crea una shortlist finale delle TOP {top_n} opportunità con maggior potenziale di rendimento,
considerando: qualità dei fondamentali Buffett, segnali insider, momentum aziendale, rischio/rendimento.

Rispondi SOLO con JSON valido:
{{
  "shortlist": [
    {{
      "rank": 1,
      "ticker": "...",
      "company": "...",
      "perche_comprare": "Spiegazione concisa in italiano (2-3 frasi)",
      "potenziale": "Alto" oppure "Medio" oppure "Speculativo",
      "rischio": "Basso" oppure "Medio" oppure "Alto",
      "orizzonte": "6-12 mesi" oppure "12-24 mesi" oppure "3-5 anni",
      "azione_suggerita": "Acquisto immediato" oppure "Monitorare" oppure "Attendere conferma"
    }}
  ],
  "market_context": "Contesto di mercato generale e nota metodologica (italiano)"
}}
"""


def _format_signals(opp: InvestmentOpportunity) -> str:
    parts = []
    for tx in opp.insider_buys:
        parts.append(
            f"- INSIDER BUY (Form 4): {tx.owner_name} ({tx.owner_title}) ha acquistato "
            f"${tx.value_usd:,.0f} ({tx.shares:,.0f} azioni a ${tx.price:.2f}) il {tx.file_date}"
        )
    for ev in opp.corporate_events:
        parts.append(
            f"- EVENTO AZIENDALE ({ev.form_type}): {ev.reason} [{ev.event_type}] il {ev.file_date}"
        )
    return "\n".join(parts) if parts else "Nessun segnale specifico"


def _build_analysis_prompt(opp: InvestmentOpportunity) -> str:
    bs = opp.buffett_score

    def fmt(v, fmt_str="{:.1f}%", na="N/D"):
        return fmt_str.format(v) if v is not None else na

    return ANALYSIS_PROMPT.format(
        company=opp.company_name,
        ticker=opp.ticker,
        signals_text=_format_signals(opp),
        buffett_total=bs.total_score if bs else "N/D",
        buffett_grade=bs.grade if bs else "N/D",
        moat=bs.moat_score if bs else "N/D",
        fortress=bs.fortress_score if bs else "N/D",
        mgmt=bs.management_score if bs else "N/D",
        valuation=bs.valuation_score if bs else "N/D",
        roe=fmt(bs.roe if bs else None),
        gross_margin=fmt(bs.gross_margin if bs else None),
        net_margin=fmt(bs.net_margin if bs else None),
        debt_equity=fmt(bs.debt_equity if bs else None, "{:.2f}", "N/D"),
        pe=fmt(bs.pe_ratio if bs else None, "{:.1f}x", "N/D"),
        ev_ebitda=fmt(bs.ev_ebitda if bs else None, "{:.1f}x", "N/D"),
        fcf_yield=fmt(bs.fcf_yield if bs else None),
        rev_growth=fmt(bs.revenue_growth_3y if bs else None),
        strengths="; ".join(bs.strengths[:3]) if bs else "N/D",
        concerns="; ".join(bs.concerns[:3]) if bs else "N/D",
    )


def analyze_opportunity(
    ai: anthropic.Anthropic, opp: InvestmentOpportunity
) -> InvestmentOpportunity:
    """Run Claude Sonnet analysis on a single investment opportunity."""
    prompt = _build_analysis_prompt(opp)
    try:
        msg = ai.messages.create(
            model=cfg.analysis_model,
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )
        raw = msg.content[0].text.strip()
        import re
        json_match = re.search(r"\{.*\}", raw, re.DOTALL)
        if json_match:
            data = json.loads(json_match.group())
            opp.thesis = data.get("thesis", "")
            opp.risks = data.get("risks", "")
            opp.catalysts = data.get("catalysts", "")
            opp.time_horizon = data.get("time_horizon", "medio")
            opp.conviction = data.get("conviction", "BASSA")
            opp.expected_return = data.get("expected_return", "Speculativo")
            opp.final_score = float(data.get("final_score", 0.0))
    except Exception as exc:
        logger.warning("AI analysis error for %s: %s", opp.ticker, exc)
        opp.thesis = "Analisi non disponibile"
        opp.final_score = (opp.buffett_score.total_score / 10) if opp.buffett_score else 0.0

    return opp


def build_shortlist(
    ai: anthropic.Anthropic,
    opportunities: List[InvestmentOpportunity],
    analysis_date: str,
    top_n: int = 5,
) -> Dict[str, Any]:
    """Use Claude Opus to rank and synthesize the final investment shortlist."""
    if not opportunities:
        return {"shortlist": [], "market_context": "Nessuna opportunità rilevata oggi."}

    summary_parts = []
    for i, opp in enumerate(opportunities, 1):
        bs = opp.buffett_score
        summary_parts.append(
            f"{i}. {opp.company_name} ({opp.ticker})\n"
            f"   Buffett score: {bs.total_score if bs else 'N/D'}/100 (Grade {bs.grade if bs else 'N/D'})\n"
            f"   Score AI: {opp.final_score:.1f}/10\n"
            f"   Conviction: {opp.conviction}\n"
            f"   Rendimento atteso: {opp.expected_return}\n"
            f"   Segnali: {len(opp.insider_buys)} insider buy, {len(opp.corporate_events)} eventi\n"
            f"   Tesi breve: {opp.thesis[:200] if opp.thesis else 'N/D'}"
        )

    prompt = SHORTLIST_PROMPT.format(
        n=len(opportunities),
        date=analysis_date,
        opportunities_summary="\n\n".join(summary_parts),
        top_n=min(top_n, len(opportunities)),
    )

    try:
        msg = ai.messages.create(
            model=cfg.recommendation_model,
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}],
        )
        raw = msg.content[0].text.strip()
        import re
        json_match = re.search(r"\{.*\}", raw, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
    except Exception as exc:
        logger.error("Shortlist generation error: %s", exc)

    # Fallback: simple ranking by final_score
    fallback = sorted(opportunities, key=lambda o: o.final_score, reverse=True)[:top_n]
    return {
        "shortlist": [
            {
                "rank": i + 1,
                "ticker": o.ticker,
                "company": o.company_name,
                "perche_comprare": o.thesis[:200] if o.thesis else "",
                "potenziale": o.expected_return,
                "rischio": "Medio",
                "orizzonte": f"{o.time_horizon} termine",
                "azione_suggerita": "Monitorare",
            }
            for i, o in enumerate(fallback)
        ],
        "market_context": "Ranking automatico basato su punteggio AI.",
    }


def run_full_analysis(
    insider_positives: List[InsiderTransaction],
    corporate_positives: List[CorporateEvent],
    buffett_scores: List[BuffettScore],
    analysis_date: str,
) -> tuple[List[InvestmentOpportunity], Dict[str, Any]]:
    """
    Orchestrate the full AI analysis pipeline.
    Returns (opportunities_list, shortlist_dict).
    """
    if not cfg.anthropic_api_key:
        logger.error("ANTHROPIC_API_KEY non impostato – analisi AI non disponibile")
        return [], {}

    ai = anthropic.Anthropic(api_key=cfg.anthropic_api_key)

    # ── Group signals by ticker ────────────────────────────────────────────────
    ticker_map: Dict[str, InvestmentOpportunity] = {}

    for tx in insider_positives:
        ticker = tx.issuer_ticker.upper()
        if not ticker:
            continue
        if ticker not in ticker_map:
            ticker_map[ticker] = InvestmentOpportunity(
                ticker=ticker, company_name=tx.issuer_name
            )
        ticker_map[ticker].insider_buys.append(tx)

    for ev in corporate_positives:
        ticker = ev.issuer_ticker.upper()
        if not ticker:
            continue
        if ticker not in ticker_map:
            ticker_map[ticker] = InvestmentOpportunity(
                ticker=ticker, company_name=ev.company_name
            )
        ticker_map[ticker].corporate_events.append(ev)

    # ── Attach Buffett scores ──────────────────────────────────────────────────
    buffett_by_ticker = {bs.ticker.upper(): bs for bs in buffett_scores}
    for ticker, opp in ticker_map.items():
        opp.buffett_score = buffett_by_ticker.get(ticker)
        if opp.buffett_score:
            opp.sector = opp.buffett_score.sector

    # ── Run AI analysis on each opportunity ───────────────────────────────────
    opportunities = list(ticker_map.values())
    logger.info("Avvio analisi AI su %d opportunità…", len(opportunities))

    for i, opp in enumerate(opportunities, 1):
        logger.info("[%d/%d] Analisi AI: %s (%s)", i, len(opportunities), opp.company_name, opp.ticker)
        analyze_opportunity(ai, opp)

    # Sort by final_score desc
    opportunities.sort(key=lambda o: o.final_score, reverse=True)
    for i, opp in enumerate(opportunities, 1):
        opp.rank = i

    # ── Build shortlist ────────────────────────────────────────────────────────
    logger.info("Generazione shortlist finale con Claude Opus…")
    shortlist = build_shortlist(ai, opportunities, analysis_date)

    return opportunities, shortlist
