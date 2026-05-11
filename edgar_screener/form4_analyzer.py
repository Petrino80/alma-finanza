"""
Form 4 (Insider Trading) analyzer.

Classifies each transaction as:
  POSITIVE  – insider buying open-market shares (code P) with meaningful size
  NEUTRAL   – tax withholding (F), option exercise (M/C/X/E), gift (G)
  NEGATIVE  – open-market sale (S) not covered by 10b5-1 plan footnote

Only POSITIVE signals pass through to the Buffett analysis stage.
"""
import logging
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from .config import cfg
from .edgar_client import EdgarClient

logger = logging.getLogger(__name__)


@dataclass
class InsiderTransaction:
    form_type: str = "4"
    accession_no: str = ""
    file_date: str = ""
    # Issuer
    issuer_cik: str = ""
    issuer_name: str = ""
    issuer_ticker: str = ""
    # Insider
    owner_name: str = ""
    owner_title: str = ""
    is_director: bool = False
    is_officer: bool = False
    is_ten_pct_owner: bool = False
    # Transaction
    security_title: str = "Common Stock"
    transaction_code: str = ""
    acquired_disposed: str = ""   # A or D
    shares: float = 0.0
    price: float = 0.0
    value_usd: float = 0.0
    shares_owned_after: float = 0.0
    footnotes: str = ""
    # Classification
    signal: str = "NEUTRAL"   # POSITIVE | NEUTRAL | NEGATIVE
    signal_reason: str = ""


def _text(elem: Optional[ET.Element], path: str, default: str = "") -> str:
    if elem is None:
        return default
    node = elem.find(path)
    if node is None or node.text is None:
        return default
    return node.text.strip()


def _float(elem: Optional[ET.Element], path: str) -> float:
    try:
        return float(_text(elem, path, "0"))
    except ValueError:
        return 0.0


def _is_10b5_plan(footnotes: str) -> bool:
    """Detect pre-planned Rule 10b5-1 sales (reduces negative signal weight)."""
    lower = footnotes.lower()
    return "10b5-1" in lower or "10b51" in lower or "prearranged" in lower


def _classify(tx: InsiderTransaction) -> Tuple[str, str]:
    """Return (signal, reason) for a transaction."""
    code = tx.transaction_code.upper()
    disp = tx.acquired_disposed.upper()

    # Genuine open-market purchase
    if code == "P" and disp == "A":
        if tx.value_usd >= cfg.min_insider_purchase_usd:
            role = tx.owner_title or ("Director" if tx.is_director else "Insider")
            return (
                "POSITIVE",
                f"{role} acquista ${tx.value_usd:,.0f} ({tx.shares:,.0f} azioni a "
                f"${tx.price:.2f}) – codice P, mercato aperto",
            )
        else:
            return (
                "NEUTRAL",
                f"Acquisto codice P ma valore troppo basso (${tx.value_usd:,.0f} < "
                f"${cfg.min_insider_purchase_usd:,.0f})",
            )

    # Tax withholding / vesting coverage – completely neutral
    if code in ("F",):
        return "NEUTRAL", "Vendita per copertura fiscale su RSU/opzioni (codice F)"

    # Option exercise or conversion – neutral unless also sold immediately
    if code in ("M", "C", "X", "E"):
        return "NEUTRAL", f"Esercizio/conversione derivativo (codice {code})"

    # Gift – neutral
    if code == "G":
        return "NEUTRAL", "Trasferimento in dono (codice G)"

    # Open-market sale
    if code == "S" and disp == "D":
        if _is_10b5_plan(tx.footnotes):
            return "NEUTRAL", "Vendita nell'ambito di piano 10b5-1 preordinato"
        return "NEGATIVE", f"Vendita mercato aperto: {tx.shares:,.0f} azioni a ${tx.price:.2f}"

    # Disposition to company (buyback of insider shares, e.g. SARs)
    if code == "D":
        return "NEUTRAL", "Disposizione alla società (codice D)"

    return "NEUTRAL", f"Codice transazione non classificato: {code}"


def parse_form4_xml(xml_text: str, accession_no: str, file_date: str) -> List[InsiderTransaction]:
    """Parse a Form 4 XML document into InsiderTransaction records."""
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as exc:
        logger.warning("XML parse error for %s: %s", accession_no, exc)
        return []

    results: List[InsiderTransaction] = []

    # ── issuer info ────────────────────────────────────────────────────────────
    issuer = root.find("issuer")
    issuer_cik = _text(issuer, "issuerCik")
    issuer_name = _text(issuer, "issuerName")
    issuer_ticker = _text(issuer, "issuerTradingSymbol")

    # ── reporting owner ────────────────────────────────────────────────────────
    owner_block = root.find("reportingOwner")
    if owner_block is None:
        # Some Form 4/A have multiple owners
        owner_block = root.find(".//reportingOwner")

    owner_name = _text(owner_block, "reportingOwnerId/rptOwnerName")
    rel = owner_block.find("reportingOwnerRelationship") if owner_block else None
    is_director = _text(rel, "isDirector") == "1"
    is_officer = _text(rel, "isOfficer") == "1"
    is_ten_pct = _text(rel, "isTenPercentOwner") == "1"
    officer_title = _text(rel, "officerTitle")

    # ── footnotes (needed to detect 10b5-1 plans) ─────────────────────────────
    footnote_texts = [
        fn.text or "" for fn in root.findall(".//footnote")
    ]
    remarks = _text(root, "remarks")
    all_footnotes = " ".join(footnote_texts) + " " + remarks

    # ── non-derivative transactions ───────────────────────────────────────────
    for ndt in root.findall(".//nonDerivativeTransaction"):
        tx = InsiderTransaction(
            accession_no=accession_no,
            file_date=file_date,
            issuer_cik=issuer_cik,
            issuer_name=issuer_name,
            issuer_ticker=issuer_ticker,
            owner_name=owner_name,
            owner_title=officer_title,
            is_director=is_director,
            is_officer=is_officer,
            is_ten_pct_owner=is_ten_pct,
            security_title=_text(ndt, "securityTitle/value"),
            transaction_code=_text(ndt, "transactionCoding/transactionCode"),
            acquired_disposed=_text(
                ndt, "transactionAmounts/transactionAcquiredDisposedCode/value"
            ),
            footnotes=all_footnotes,
        )
        tx.shares = _float(ndt, "transactionAmounts/transactionShares/value")
        tx.price = _float(ndt, "transactionAmounts/transactionPricePerShare/value")
        tx.value_usd = tx.shares * tx.price
        tx.shares_owned_after = _float(
            ndt, "postTransactionAmounts/sharesOwnedFollowingTransaction/value"
        )
        tx.signal, tx.signal_reason = _classify(tx)
        results.append(tx)

    return results


def analyze_form4_filings(
    client: EdgarClient, hits: List[dict]
) -> List[InsiderTransaction]:
    """
    Download and analyze all Form 4 filings from EFTS hits.
    Returns only POSITIVE transactions.
    """
    positive: List[InsiderTransaction] = []
    total = len(hits)

    for i, hit in enumerate(hits, 1):
        accession = client.accession_from_hit(hit)
        file_date = client.filing_date_for_hit(hit)

        if not accession:
            continue

        # CIK is the first segment of the accession number
        cik = client.cik_from_filing_id(accession)

        logger.info("[%d/%d] Form 4 %s (CIK %s)", i, total, accession, cik)

        # Fetch filing index to find the XML document name
        index = client.get_filing_index(cik, accession)
        xml_filename = _find_form4_xml(index, accession)
        if not xml_filename:
            continue

        try:
            xml_text = client.get_filing_document(cik, accession, xml_filename)
        except Exception as exc:
            logger.warning("Cannot fetch %s/%s: %s", accession, xml_filename, exc)
            continue

        transactions = parse_form4_xml(xml_text, accession, file_date)
        for tx in transactions:
            if tx.signal == "POSITIVE":
                # Resolve ticker if missing
                if not tx.issuer_ticker:
                    tx.issuer_ticker = client.ticker_for_cik(tx.issuer_cik) or ""
                positive.append(tx)
                logger.info(
                    "  ✅ POSITIVO: %s (%s) – %s",
                    tx.issuer_name,
                    tx.issuer_ticker,
                    tx.signal_reason,
                )

    return positive


def _find_form4_xml(index: dict, accession: str) -> Optional[str]:
    """Return the filename of the Form 4 XML document from the filing index."""
    documents = index.get("documents", [])
    for doc in documents:
        doc_type = doc.get("type", "").upper()
        filename = doc.get("filename", "")
        # The primary Form 4 document is type "4" and ends with .xml
        if doc_type in ("4", "4/A") and filename.lower().endswith(".xml"):
            return filename
    # Fallback: any XML file in the filing
    for doc in documents:
        if doc.get("filename", "").lower().endswith(".xml"):
            return doc["filename"]
    # Last resort: construct from accession number
    acc_nodash = accession.replace("-", "")
    return f"{acc_nodash}.xml"
