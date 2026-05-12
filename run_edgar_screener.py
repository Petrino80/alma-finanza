#!/usr/bin/env python3
"""
SEC EDGAR Daily Screener – Entry Point
Alma Finanza · https://almafinanza.it

Scarica ogni giorno alle 22:00 ora italiana i filing SEC (Form 4, 8-K, SC 13D/G),
seleziona i segnali positivi, applica l'analisi Warren Buffett e genera
una shortlist di opportunità di investimento con tesi AI in italiano.

USO:
  python run_edgar_screener.py                  # esegui subito (one-shot)
  python run_edgar_screener.py --daemon         # avvia daemon (22:00 IT ogni giorno)
  python run_edgar_screener.py --date 2026-05-10  # analizza data specifica
  python run_edgar_screener.py --help

VARIABILI D'AMBIENTE:
  ANTHROPIC_API_KEY   – chiave API Anthropic (obbligatoria per analisi AI)
"""
import argparse
import logging
import os
import sys
from datetime import date

# ── Logging setup ──────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s – %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("edgar_output/screener.log", mode="a", encoding="utf-8"),
    ],
)
# Silence noisy third-party loggers
for noisy in ("urllib3", "requests", "httpx", "yfinance"):
    logging.getLogger(noisy).setLevel(logging.WARNING)

logger = logging.getLogger("edgar_screener")


def main() -> None:
    os.makedirs("edgar_output", exist_ok=True)

    parser = argparse.ArgumentParser(
        description="SEC EDGAR Form Screener – Alma Finanza",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--daemon",
        action="store_true",
        help="Avvia il daemon: esegue automaticamente alle 22:00 ora italiana ogni giorno",
    )
    parser.add_argument(
        "--date",
        metavar="YYYY-MM-DD",
        help="Analizza una data specifica invece di oggi",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="(Solo con --daemon) Simula le esecuzioni senza scaricare dati reali",
    )
    parser.add_argument(
        "--no-ai",
        action="store_true",
        help="Salta le analisi AI (utile se ANTHROPIC_API_KEY non disponibile)",
    )
    args = parser.parse_args()

    # Check API key
    if not os.environ.get("ANTHROPIC_API_KEY") and not args.no_ai:
        logger.warning(
            "⚠️  ANTHROPIC_API_KEY non impostata. "
            "L'analisi AI sarà disabilitata. "
            "Usa: export ANTHROPIC_API_KEY=sk-ant-... oppure passa --no-ai"
        )

    if args.no_ai:
        # Patch config to disable AI
        from edgar_screener.config import cfg
        cfg.anthropic_api_key = ""

    if args.daemon:
        logger.info("Avvio in modalità daemon – 22:00 IT")
        from edgar_screener.scheduler import run_daemon
        run_daemon(dry_run=args.dry_run)
    else:
        target_date = None
        if args.date:
            try:
                target_date = date.fromisoformat(args.date)
            except ValueError:
                logger.error("Formato data non valido: %s (usa YYYY-MM-DD)", args.date)
                sys.exit(1)

        logger.info("Esecuzione one-shot%s", f" per {target_date}" if target_date else " (oggi)")
        from edgar_screener.scheduler import run_once
        result = run_once(target_date=target_date)

        if result.get("status") == "ok":
            print("\n" + "=" * 60)
            print(f"✅ Screening completato – {result['date']}")
            print(f"   Form 4 analizzati:   {result['form4_hits']}")
            print(f"   8-K analizzati:      {result['form8k_hits']}")
            print(f"   SC 13D/G analizzati: {result['sc13_hits']}")
            print(f"   Form salvati:        {result['forms_saved']} documenti")
            print(f"   Indice form:         {result['forms_index']}")
            print(f"   Segnali positivi:    {result['insider_positives']} insider buy "
                  f"+ {result['corporate_positives']} eventi aziendali")
            print(f"   Opportunità totali:  {result['opportunities']}")
            print(f"   Shortlist finale:    {result['shortlist_count']}")
            print(f"   Report HTML:         {result['html_report']}")
            print(f"   Report JSON:         {result['json_report']}")
            print("=" * 60)
        elif result.get("status") == "no_signals":
            print(f"\n⚪ Nessun segnale positivo rilevato per il {result['date']}.")
        else:
            print(f"\n❌ Errore: {result}")
            sys.exit(1)


if __name__ == "__main__":
    main()
