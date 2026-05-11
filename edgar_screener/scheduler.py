"""
Daily scheduler – runs the SEC EDGAR screening at 22:00 Italian time (CET/CEST).

Usage:
    python run_edgar_screener.py --daemon   # run as daemon, fires every day at 22:00 IT
    python run_edgar_screener.py            # run immediately (one-shot)
    python run_edgar_screener.py --date 2026-05-10  # analyze a specific date
"""
import logging
import signal
import sys
import threading
import time
from datetime import date, datetime, timezone
from typing import Optional
import zoneinfo

logger = logging.getLogger(__name__)

ITALIAN_TZ = zoneinfo.ZoneInfo("Europe/Rome")
SCHEDULE_HOUR = 22
SCHEDULE_MINUTE = 0


def _next_run_seconds() -> float:
    """Seconds until the next 22:00 Italian time."""
    now_it = datetime.now(tz=ITALIAN_TZ)
    next_run = now_it.replace(
        hour=SCHEDULE_HOUR, minute=SCHEDULE_MINUTE, second=0, microsecond=0
    )
    if now_it >= next_run:
        # Already past 22:00 today → schedule for tomorrow
        from datetime import timedelta
        next_run = next_run + timedelta(days=1)
    delta = next_run - now_it
    return delta.total_seconds()


def run_daemon(dry_run: bool = False) -> None:
    """
    Blocking daemon loop. Waits until 22:00 IT, runs screening, then waits again.
    Catches SIGINT / SIGTERM for graceful shutdown.
    """
    stop_event = threading.Event()

    def _handle_signal(signum, frame):
        logger.info("Segnale %d ricevuto – arresto daemon…", signum)
        stop_event.set()

    signal.signal(signal.SIGINT, _handle_signal)
    signal.signal(signal.SIGTERM, _handle_signal)

    logger.info("Daemon SEC EDGAR Screener avviato.")
    logger.info("Prossima esecuzione alle 22:00 ora italiana.")

    while not stop_event.is_set():
        wait_secs = _next_run_seconds()
        next_run_it = datetime.now(tz=ITALIAN_TZ).replace(
            hour=SCHEDULE_HOUR, minute=SCHEDULE_MINUTE, second=0, microsecond=0
        )
        logger.info(
            "Prossima esecuzione: %s IT (tra %.0f minuti)",
            next_run_it.strftime("%Y-%m-%d %H:%M"),
            wait_secs / 60,
        )

        # Sleep in short intervals to react to stop_event promptly
        slept = 0.0
        while slept < wait_secs and not stop_event.is_set():
            chunk = min(60.0, wait_secs - slept)
            time.sleep(chunk)
            slept += chunk

        if stop_event.is_set():
            break

        if dry_run:
            logger.info("[DRY RUN] Esecuzione screening saltata.")
            continue

        logger.info("🕙 22:00 IT – avvio screening SEC EDGAR…")
        try:
            from .main import run_screening
            result = run_screening(target_date=date.today())
            logger.info("Screening completato: %s", result)
        except Exception as exc:
            logger.error("Errore durante lo screening: %s", exc, exc_info=True)

    logger.info("Daemon SEC EDGAR Screener arrestato.")


def run_once(target_date: Optional[date] = None) -> dict:
    """Run the screening immediately for target_date."""
    from .main import run_screening
    return run_screening(target_date=target_date)
