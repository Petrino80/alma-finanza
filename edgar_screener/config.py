"""Configuration for SEC EDGAR screener."""
import os
from dataclasses import dataclass, field
from typing import List


@dataclass
class Config:
    # ── SEC EDGAR ──────────────────────────────────────────────────────────────
    # Required by SEC: identify your application
    edgar_user_agent: str = "AlmaFinanza admin@almafinanza.it"
    edgar_base_url: str = "https://www.sec.gov"
    edgar_efts_url: str = "https://efts.sec.gov/LATEST/search-index"
    edgar_data_url: str = "https://data.sec.gov"
    # Max 10 req/sec per SEC policy
    edgar_request_delay: float = 0.12

    # Forms to download and analyze each day
    forms_to_download: List[str] = field(default_factory=lambda: [
        "4",       # Insider trading
        "8-K",     # Material corporate events
        "SC 13D",  # Activist investors (>5% stake, intent to influence)
        "SC 13G",  # Institutional/passive investors (>5% stake)
    ])

    # ── ANTHROPIC ──────────────────────────────────────────────────────────────
    anthropic_api_key: str = field(
        default_factory=lambda: os.environ.get("ANTHROPIC_API_KEY", "")
    )
    # Haiku for high-volume initial screening (fast & cheap)
    screening_model: str = "claude-haiku-4-5-20251001"
    # Sonnet for Buffett analysis (balanced quality/cost)
    analysis_model: str = "claude-sonnet-4-6"
    # Opus for final investment recommendation (best quality)
    recommendation_model: str = "claude-opus-4-7"

    # ── FORM 4 SCREENING THRESHOLDS ────────────────────────────────────────────
    # Minimum USD value of insider purchase to be considered significant
    min_insider_purchase_usd: float = 100_000
    # Transaction codes that indicate a genuine buy (not exercise, tax, gift)
    positive_transaction_codes: List[str] = field(
        default_factory=lambda: ["P"]  # P = open-market purchase
    )
    # Transaction codes that are neutral (tax withholding, pre-planned sales)
    neutral_transaction_codes: List[str] = field(
        default_factory=lambda: ["F", "M", "C", "E", "X", "G", "V"]
    )

    # ── WARREN BUFFETT CRITERIA ────────────────────────────────────────────────
    min_roe: float = 15.0          # Return on Equity %
    max_debt_equity: float = 0.5   # Debt/Equity ratio
    min_net_margin: float = 10.0   # Net profit margin %
    min_gross_margin: float = 35.0 # Gross margin % (pricing power / moat)
    min_roic: float = 12.0         # Return on Invested Capital %
    max_pe_ratio: float = 30.0     # Max trailing P/E (generous for quality)
    min_current_ratio: float = 1.2 # Liquidity floor
    min_years_data: int = 3        # Minimum years of financial history required

    # ── OUTPUT ─────────────────────────────────────────────────────────────────
    output_dir: str = "edgar_output"
    max_results_per_form: int = 200   # Max filings to fetch per form type per day
    max_companies_to_analyze: int = 15 # Cap Buffett analysis (API cost control)


# Singleton instance
cfg = Config()
