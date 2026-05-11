"""
Warren Buffett fundamental analysis engine.

Fetches financial data via yfinance and SEC EDGAR XBRL, then scores
each company against Buffett's classic criteria:
  1. Economic moat (high gross margin, pricing power)
  2. Durable competitive advantage (consistent ROE, ROIC)
  3. Financial fortress (low debt, strong FCF)
  4. Trustworthy management (buybacks, insider alignment)
  5. Reasonable valuation (not overpaying for quality)
"""
import logging
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from .config import cfg

logger = logging.getLogger(__name__)


@dataclass
class BuffettScore:
    ticker: str
    company_name: str
    # Raw metrics
    roe: Optional[float] = None          # %
    roic: Optional[float] = None         # %
    gross_margin: Optional[float] = None # %
    net_margin: Optional[float] = None   # %
    debt_equity: Optional[float] = None  # ratio
    current_ratio: Optional[float] = None
    pe_ratio: Optional[float] = None
    pb_ratio: Optional[float] = None
    ev_ebitda: Optional[float] = None
    fcf_yield: Optional[float] = None    # %
    revenue_growth_3y: Optional[float] = None # %
    eps_growth_3y: Optional[float] = None     # %
    payout_ratio: Optional[float] = None      # %
    market_cap_bn: Optional[float] = None     # USD billions
    sector: str = ""
    industry: str = ""
    # Scoring
    moat_score: int = 0        # 0-30
    fortress_score: int = 0    # 0-25
    management_score: int = 0  # 0-20
    valuation_score: int = 0   # 0-25
    total_score: int = 0       # 0-100
    grade: str = "F"           # A+ A B C D F
    verdict: str = ""
    strengths: List[str] = field(default_factory=list)
    concerns: List[str] = field(default_factory=list)
    data_quality: str = "LOW"  # HIGH | MEDIUM | LOW (how complete the data is)


def _safe_pct(value) -> Optional[float]:
    """Convert a ratio (0-1) to percentage, or return None."""
    try:
        v = float(value)
        if abs(v) > 1000:  # already a percentage
            return v
        return v * 100
    except (TypeError, ValueError):
        return None


def _safe_float(value) -> Optional[float]:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def fetch_financials(ticker: str) -> Optional[BuffettScore]:
    """
    Fetch financial data from yfinance and compute Buffett score.
    Returns None if the ticker is invalid or data is too sparse.
    """
    try:
        import yfinance as yf
    except ImportError:
        logger.error("yfinance not installed – run: pip install yfinance")
        return None

    try:
        stock = yf.Ticker(ticker)
        info = stock.info
    except Exception as exc:
        logger.warning("yfinance error for %s: %s", ticker, exc)
        return None

    # Sanity check: valid ticker has a longName or shortName
    if not info or not (info.get("longName") or info.get("shortName")):
        logger.warning("No data for ticker: %s", ticker)
        return None

    score = BuffettScore(
        ticker=ticker.upper(),
        company_name=info.get("longName") or info.get("shortName", ticker),
        sector=info.get("sector", ""),
        industry=info.get("industry", ""),
    )

    # ── Profitability metrics ──────────────────────────────────────────────────
    score.roe = _safe_pct(info.get("returnOnEquity"))
    score.gross_margin = _safe_pct(info.get("grossMargins"))
    score.net_margin = _safe_pct(info.get("profitMargins"))
    score.pe_ratio = _safe_float(info.get("trailingPE"))
    score.pb_ratio = _safe_float(info.get("priceToBook"))
    score.ev_ebitda = _safe_float(info.get("enterpriseToEbitda"))
    score.current_ratio = _safe_float(info.get("currentRatio"))
    score.payout_ratio = _safe_pct(info.get("payoutRatio"))
    score.market_cap_bn = (_safe_float(info.get("marketCap")) or 0) / 1e9
    score.revenue_growth_3y = _safe_pct(info.get("revenueGrowth"))  # trailing 1Y from yf
    score.eps_growth_3y = _safe_pct(info.get("earningsGrowth"))

    # Debt/Equity
    dte = info.get("debtToEquity")
    if dte is not None:
        try:
            score.debt_equity = float(dte) / 100  # yf returns it as percentage (e.g. 50 = 0.5)
        except (TypeError, ValueError):
            pass

    # FCF yield = (FCF / market cap) * 100
    fcf = _safe_float(info.get("freeCashflow"))
    mkt_cap = _safe_float(info.get("marketCap"))
    if fcf and mkt_cap and mkt_cap > 0:
        score.fcf_yield = (fcf / mkt_cap) * 100

    # ROIC approximation: EBIT * (1 - tax_rate) / (total_assets - current_liabilities)
    # yf doesn't provide ROIC directly; use returnOnAssets as proxy when available
    roa = _safe_pct(info.get("returnOnAssets"))
    if roa is not None:
        # Rough: ROIC ≈ ROA * (1 + D/E) is common approximation
        de = score.debt_equity or 0
        score.roic = roa * (1 + de)

    # ── Score computation ──────────────────────────────────────────────────────
    score.moat_score, score.fortress_score, score.management_score, score.valuation_score = (
        _score_all(score)
    )
    score.total_score = (
        score.moat_score
        + score.fortress_score
        + score.management_score
        + score.valuation_score
    )
    score.grade = _grade(score.total_score)
    score.strengths, score.concerns = _narrative(score)
    score.verdict = _verdict(score)
    score.data_quality = _data_quality(score)

    return score


# ── Scoring sub-functions ──────────────────────────────────────────────────────

def _score_all(s: BuffettScore) -> Tuple[int, int, int, int]:
    moat = _score_moat(s)
    fortress = _score_fortress(s)
    mgmt = _score_management(s)
    valuation = _score_valuation(s)
    return moat, fortress, mgmt, valuation


def _score_moat(s: BuffettScore) -> int:
    """Economic moat: gross margin, ROE, net margin. Max 30 pts."""
    pts = 0
    # Gross margin (pricing power) – max 12
    if s.gross_margin is not None:
        if s.gross_margin >= 60:   pts += 12
        elif s.gross_margin >= 45: pts += 9
        elif s.gross_margin >= 35: pts += 6
        elif s.gross_margin >= 20: pts += 3
    # ROE – max 10
    if s.roe is not None:
        if s.roe >= 25:   pts += 10
        elif s.roe >= 18: pts += 7
        elif s.roe >= 12: pts += 4
        elif s.roe >= 8:  pts += 1
    # Net margin – max 8
    if s.net_margin is not None:
        if s.net_margin >= 20:  pts += 8
        elif s.net_margin >= 15: pts += 6
        elif s.net_margin >= 10: pts += 4
        elif s.net_margin >= 5:  pts += 2
    return min(pts, 30)


def _score_fortress(s: BuffettScore) -> int:
    """Financial fortress: debt, liquidity, FCF. Max 25 pts."""
    pts = 0
    # Debt/Equity – max 10
    if s.debt_equity is not None:
        if s.debt_equity <= 0.1:  pts += 10
        elif s.debt_equity <= 0.3: pts += 8
        elif s.debt_equity <= 0.5: pts += 5
        elif s.debt_equity <= 1.0: pts += 2
    else:
        pts += 5  # no debt data: partial credit
    # Current ratio – max 7
    if s.current_ratio is not None:
        if s.current_ratio >= 2.5:  pts += 7
        elif s.current_ratio >= 2.0: pts += 5
        elif s.current_ratio >= 1.5: pts += 3
        elif s.current_ratio >= 1.2: pts += 1
    # FCF yield – max 8
    if s.fcf_yield is not None:
        if s.fcf_yield >= 7:   pts += 8
        elif s.fcf_yield >= 5: pts += 6
        elif s.fcf_yield >= 3: pts += 4
        elif s.fcf_yield >= 1: pts += 2
    return min(pts, 25)


def _score_management(s: BuffettScore) -> int:
    """Management quality proxy: ROIC, revenue/EPS growth. Max 20 pts."""
    pts = 0
    # ROIC – max 10
    if s.roic is not None:
        if s.roic >= 20:   pts += 10
        elif s.roic >= 15: pts += 7
        elif s.roic >= 10: pts += 4
        elif s.roic >= 5:  pts += 1
    # Revenue growth – max 5
    if s.revenue_growth_3y is not None:
        if s.revenue_growth_3y >= 15:  pts += 5
        elif s.revenue_growth_3y >= 10: pts += 3
        elif s.revenue_growth_3y >= 5:  pts += 1
    # EPS growth – max 5
    if s.eps_growth_3y is not None:
        if s.eps_growth_3y >= 20:  pts += 5
        elif s.eps_growth_3y >= 12: pts += 3
        elif s.eps_growth_3y >= 5:  pts += 1
    return min(pts, 20)


def _score_valuation(s: BuffettScore) -> int:
    """Valuation reasonableness. Max 25 pts."""
    pts = 0
    # P/E ratio – max 10
    if s.pe_ratio is not None and s.pe_ratio > 0:
        if s.pe_ratio <= 12:   pts += 10
        elif s.pe_ratio <= 18: pts += 8
        elif s.pe_ratio <= 25: pts += 5
        elif s.pe_ratio <= 35: pts += 2
    # EV/EBITDA – max 8
    if s.ev_ebitda is not None and s.ev_ebitda > 0:
        if s.ev_ebitda <= 8:   pts += 8
        elif s.ev_ebitda <= 12: pts += 6
        elif s.ev_ebitda <= 18: pts += 4
        elif s.ev_ebitda <= 25: pts += 2
    # P/B ratio – max 7
    if s.pb_ratio is not None and s.pb_ratio > 0:
        if s.pb_ratio <= 1.5:  pts += 7
        elif s.pb_ratio <= 3.0: pts += 5
        elif s.pb_ratio <= 5.0: pts += 3
        elif s.pb_ratio <= 8.0: pts += 1
    return min(pts, 25)


def _grade(total: int) -> str:
    if total >= 85: return "A+"
    if total >= 75: return "A"
    if total >= 65: return "B"
    if total >= 55: return "C"
    if total >= 40: return "D"
    return "F"


def _data_quality(s: BuffettScore) -> str:
    fields = [s.roe, s.gross_margin, s.net_margin, s.debt_equity,
              s.pe_ratio, s.fcf_yield, s.current_ratio]
    filled = sum(1 for f in fields if f is not None)
    if filled >= 6: return "HIGH"
    if filled >= 4: return "MEDIUM"
    return "LOW"


def _narrative(s: BuffettScore) -> Tuple[List[str], List[str]]:
    strengths, concerns = [], []

    if s.gross_margin and s.gross_margin >= 45:
        strengths.append(f"Margine lordo eccellente ({s.gross_margin:.1f}%) → pricing power elevato")
    if s.roe and s.roe >= 18:
        strengths.append(f"ROE {s.roe:.1f}% – capitale allocato in modo eccellente")
    if s.debt_equity is not None and s.debt_equity <= 0.3:
        strengths.append(f"Debito/Equity molto basso ({s.debt_equity:.2f}) → solidità finanziaria")
    if s.fcf_yield and s.fcf_yield >= 5:
        strengths.append(f"FCF yield {s.fcf_yield:.1f}% – generazione di cassa abbondante")
    if s.net_margin and s.net_margin >= 15:
        strengths.append(f"Margine netto {s.net_margin:.1f}% – efficienza operativa superiore")
    if s.pe_ratio and 0 < s.pe_ratio <= 18:
        strengths.append(f"P/E {s.pe_ratio:.1f}x – valutazione interessante per la qualità")
    if s.roic and s.roic >= 15:
        strengths.append(f"ROIC stimato {s.roic:.1f}% – vantaggio competitivo durevole")

    if s.gross_margin and s.gross_margin < 25:
        concerns.append(f"Margine lordo basso ({s.gross_margin:.1f}%) – pricing power limitato")
    if s.roe and s.roe < 12:
        concerns.append(f"ROE {s.roe:.1f}% sotto il minimo Buffett del 15%")
    if s.debt_equity is not None and s.debt_equity > 0.8:
        concerns.append(f"Debito/Equity elevato ({s.debt_equity:.2f}) – rischio finanziario")
    if s.pe_ratio and s.pe_ratio > 35:
        concerns.append(f"P/E {s.pe_ratio:.1f}x – valutazione onerosa, margine di sicurezza ridotto")
    if s.net_margin and s.net_margin < 5:
        concerns.append(f"Margine netto molto basso ({s.net_margin:.1f}%)")
    if s.current_ratio and s.current_ratio < 1.0:
        concerns.append(f"Current ratio {s.current_ratio:.2f} – potenziale rischio liquidità")

    return strengths, concerns


def _verdict(s: BuffettScore) -> str:
    if s.grade == "A+":
        return ("Azienda eccezionale con moat durevole e valutazione ragionevole. "
                "Buffett comprerebbe senza esitazione.")
    if s.grade == "A":
        return ("Business di alta qualità con solidi fondamentali. "
                "Candidato ideale per portafoglio di lungo periodo.")
    if s.grade == "B":
        return ("Buona azienda con alcuni punti di forza Buffett. "
                "Valutare al margine di sicurezza adeguato.")
    if s.grade == "C":
        return ("Azienda nella media. Manca di elementi chiave del metodo Buffett. "
                "Solo a valutazione molto bassa.")
    if s.grade == "D":
        return ("Fondamentali deboli. Rischio elevato. Non in linea con i criteri di Buffett.")
    return "Non supera i criteri minimi. Evitare per investimento value."


def analyze_companies(tickers: List[str]) -> List[BuffettScore]:
    """Run Buffett analysis on a list of tickers. Returns sorted by total_score desc."""
    results: List[BuffettScore] = []
    for ticker in tickers:
        if not ticker:
            continue
        logger.info("Analisi Buffett: %s", ticker)
        score = fetch_financials(ticker)
        if score is not None:
            results.append(score)
        else:
            logger.warning("  ⚠️ Dati non disponibili per %s", ticker)

    results.sort(key=lambda s: s.total_score, reverse=True)
    return results
