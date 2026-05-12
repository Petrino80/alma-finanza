"""
Fixture data for --mock mode. Simulates realistic EDGAR filing responses
so the full pipeline can be tested without network access.
"""
from datetime import date
from typing import Dict, List


# ── Mock filing hits (same structure as real EDGAR search results) ────────────

def mock_form4_hits(target_date: date) -> List[Dict]:
    d = target_date.isoformat()
    return [
        {
            "_id": "0000320193-26-001234",
            "_source": {
                "entity_name": "APPLE INC",
                "form_type": "4",
                "cik": "320193",
                "file_date": d,
                "filename": f"edgar/data/320193/0000320193-26-001234.txt",
                "items": "",
                "primary_doc": "xslF345X05/form4.xml",
            },
        },
        {
            "_id": "0001652044-26-005678",
            "_source": {
                "entity_name": "ALPHABET INC",
                "form_type": "4",
                "cik": "1652044",
                "file_date": d,
                "filename": f"edgar/data/1652044/0001652044-26-005678.txt",
                "items": "",
                "primary_doc": "form4.xml",
            },
        },
        {
            "_id": "0000789019-26-009999",
            "_source": {
                "entity_name": "MICROSOFT CORP",
                "form_type": "4",
                "cik": "789019",
                "file_date": d,
                "filename": f"edgar/data/789019/0000789019-26-009999.txt",
                "items": "",
                "primary_doc": "form4.xml",
            },
        },
    ]


def mock_form8k_hits(target_date: date) -> List[Dict]:
    d = target_date.isoformat()
    return [
        {
            "_id": "0000320193-26-002345",
            "_source": {
                "entity_name": "APPLE INC",
                "form_type": "8-K",
                "cik": "320193",
                "file_date": d,
                "filename": f"edgar/data/320193/0000320193-26-002345.txt",
                "items": "2.02,8.01",
                "primary_doc": "8k.htm",
            },
        },
        {
            "_id": "0001018724-26-003456",
            "_source": {
                "entity_name": "AMAZON COM INC",
                "form_type": "8-K",
                "cik": "1018724",
                "file_date": d,
                "filename": f"edgar/data/1018724/0001018724-26-003456.txt",
                "items": "8.01",
                "primary_doc": "8k.htm",
            },
        },
    ]


def mock_sc13_hits(target_date: date) -> List[Dict]:
    d = target_date.isoformat()
    return [
        {
            "_id": "0001067983-26-004567",
            "_source": {
                "entity_name": "BERKSHIRE HATHAWAY INC",
                "form_type": "SC 13G",
                "cik": "1067983",
                "file_date": d,
                "filename": f"edgar/data/1067983/0001067983-26-004567.txt",
                "items": "",
                "primary_doc": "sc13g.htm",
            },
        },
    ]


# ── Mock XML/HTML documents ───────────────────────────────────────────────────

def mock_form4_xml_large_buy(
    issuer_name: str = "APPLE INC",
    issuer_cik: str = "0000320193",
    issuer_ticker: str = "AAPL",
    owner_name: str = "COOK TIMOTHY D",
    owner_title: str = "CEO",
    shares: str = "50000",
    price: str = "175.50",
    file_date: str = "2026-05-12",
) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<ownershipDocument>
  <schemaVersion>X0508</schemaVersion>
  <documentType>4</documentType>
  <periodOfReport>{file_date}</periodOfReport>
  <issuer>
    <issuerCik>{issuer_cik}</issuerCik>
    <issuerName>{issuer_name}</issuerName>
    <issuerTradingSymbol>{issuer_ticker}</issuerTradingSymbol>
  </issuer>
  <reportingOwner>
    <reportingOwnerId>
      <rptOwnerName>{owner_name}</rptOwnerName>
    </reportingOwnerId>
    <reportingOwnerRelationship>
      <isDirector>1</isDirector>
      <isOfficer>1</isOfficer>
      <officerTitle>{owner_title}</officerTitle>
    </reportingOwnerRelationship>
  </reportingOwner>
  <nonDerivativeTable>
    <nonDerivativeTransaction>
      <securityTitle><value>Common Stock</value></securityTitle>
      <transactionDate><value>{file_date}</value></transactionDate>
      <transactionCoding>
        <transactionFormType>4</transactionFormType>
        <transactionCode>P</transactionCode>
        <equitySwapInvolved>0</equitySwapInvolved>
      </transactionCoding>
      <transactionAmounts>
        <transactionShares><value>{shares}</value></transactionShares>
        <transactionPricePerShare><value>{price}</value></transactionPricePerShare>
        <transactionAcquiredDisposedCode><value>A</value></transactionAcquiredDisposedCode>
      </transactionAmounts>
      <postTransactionAmounts>
        <sharesOwnedFollowingTransaction><value>1050000</value></sharesOwnedFollowingTransaction>
      </postTransactionAmounts>
      <ownershipNature>
        <directOrIndirectOwnership><value>D</value></directOrIndirectOwnership>
      </ownershipNature>
    </nonDerivativeTransaction>
  </nonDerivativeTable>
</ownershipDocument>"""


def mock_form4_xml_small_sale(
    issuer_name: str = "ALPHABET INC",
    issuer_cik: str = "0001652044",
    issuer_ticker: str = "GOOGL",
    owner_name: str = "PICHAI SUNDAR",
    file_date: str = "2026-05-12",
) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<ownershipDocument>
  <schemaVersion>X0508</schemaVersion>
  <documentType>4</documentType>
  <periodOfReport>{file_date}</periodOfReport>
  <issuer>
    <issuerCik>{issuer_cik}</issuerCik>
    <issuerName>{issuer_name}</issuerName>
    <issuerTradingSymbol>{issuer_ticker}</issuerTradingSymbol>
  </issuer>
  <reportingOwner>
    <reportingOwnerId>
      <rptOwnerName>{owner_name}</rptOwnerName>
    </reportingOwnerId>
    <reportingOwnerRelationship>
      <isOfficer>1</isOfficer>
      <officerTitle>CEO</officerTitle>
    </reportingOwnerRelationship>
  </reportingOwner>
  <nonDerivativeTable>
    <nonDerivativeTransaction>
      <securityTitle><value>Class A Common Stock</value></securityTitle>
      <transactionDate><value>{file_date}</value></transactionDate>
      <transactionCoding>
        <transactionFormType>4</transactionFormType>
        <transactionCode>S</transactionCode>
        <equitySwapInvolved>0</equitySwapInvolved>
      </transactionCoding>
      <transactionAmounts>
        <transactionShares><value>500</value></transactionShares>
        <transactionPricePerShare><value>180.00</value></transactionPricePerShare>
        <transactionAcquiredDisposedCode><value>D</value></transactionAcquiredDisposedCode>
      </transactionAmounts>
      <postTransactionAmounts>
        <sharesOwnedFollowingTransaction><value>2500000</value></sharesOwnedFollowingTransaction>
      </postTransactionAmounts>
      <ownershipNature>
        <directOrIndirectOwnership><value>D</value></directOrIndirectOwnership>
      </ownershipNature>
    </nonDerivativeTransaction>
  </nonDerivativeTable>
</ownershipDocument>"""


def mock_form4_xml_option_exercise(
    issuer_name: str = "MICROSOFT CORP",
    issuer_cik: str = "0000789019",
    issuer_ticker: str = "MSFT",
    file_date: str = "2026-05-12",
) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<ownershipDocument>
  <schemaVersion>X0508</schemaVersion>
  <documentType>4</documentType>
  <periodOfReport>{file_date}</periodOfReport>
  <issuer>
    <issuerCik>{issuer_cik}</issuerCik>
    <issuerName>{issuer_name}</issuerName>
    <issuerTradingSymbol>{issuer_ticker}</issuerTradingSymbol>
  </issuer>
  <reportingOwner>
    <reportingOwnerId>
      <rptOwnerName>NADELLA SATYA</rptOwnerName>
    </reportingOwnerId>
    <reportingOwnerRelationship>
      <isOfficer>1</isOfficer>
      <officerTitle>CEO</officerTitle>
    </reportingOwnerRelationship>
  </reportingOwner>
  <nonDerivativeTable>
    <nonDerivativeTransaction>
      <securityTitle><value>Common Stock</value></securityTitle>
      <transactionDate><value>{file_date}</value></transactionDate>
      <transactionCoding>
        <transactionFormType>4</transactionFormType>
        <transactionCode>M</transactionCode>
        <equitySwapInvolved>0</equitySwapInvolved>
      </transactionCoding>
      <transactionAmounts>
        <transactionShares><value>10000</value></transactionShares>
        <transactionPricePerShare><value>0</value></transactionPricePerShare>
        <transactionAcquiredDisposedCode><value>A</value></transactionAcquiredDisposedCode>
      </transactionAmounts>
      <postTransactionAmounts>
        <sharesOwnedFollowingTransaction><value>800000</value></sharesOwnedFollowingTransaction>
      </postTransactionAmounts>
      <ownershipNature>
        <directOrIndirectOwnership><value>D</value></directOrIndirectOwnership>
      </ownershipNature>
    </nonDerivativeTransaction>
  </nonDerivativeTable>
</ownershipDocument>"""


def mock_8k_html(
    company: str = "APPLE INC",
    ticker: str = "AAPL",
    file_date: str = "2026-05-12",
) -> str:
    return f"""<html><body>
<h1>Form 8-K – {company} ({ticker})</h1>
<p>Date: {file_date}</p>
<h2>Item 8.01 – Other Events</h2>
<p>The Board of Directors of {company} has authorized a new share repurchase program
of up to $90 billion. The program reflects the company's strong cash generation
and confidence in its long-term business outlook.</p>
<h2>Item 2.02 – Results of Operations</h2>
<p>Revenue: $124.3 billion (+8% YoY). EPS: $2.22 (+12% YoY). Gross margin: 47.1%.
Management raised full-year revenue guidance to $490–500 billion.</p>
</body></html>"""


def mock_sc13g_html(
    filer: str = "BERKSHIRE HATHAWAY INC",
    subject: str = "COCA COLA CO",
    subject_ticker: str = "KO",
    pct: str = "9.3",
    file_date: str = "2026-05-12",
) -> str:
    return f"""<html><body>
<h1>Schedule 13G – Amendment</h1>
<p>Filer: {filer}</p>
<p>Subject Company: {subject} ({subject_ticker})</p>
<p>Date: {file_date}</p>
<p>Percent of class: {pct}%</p>
<p>Purpose: Passive investment. Filer acquired shares in ordinary course of business.</p>
</body></html>"""


# ── Dispatch table: accession → document content ─────────────────────────────

def mock_buffett_scores() -> list:
    """Return pre-built BuffettScore objects for mock tickers."""
    from .buffett_analyzer import BuffettScore
    aapl = BuffettScore(
        ticker="AAPL",
        company_name="Apple Inc",
        sector="Technology",
        industry="Consumer Electronics",
        roe=147.0,
        roic=55.0,
        gross_margin=45.0,
        net_margin=25.0,
        debt_equity=1.5,
        current_ratio=1.05,
        pe_ratio=28.0,
        pb_ratio=45.0,
        ev_ebitda=22.0,
        fcf_yield=3.8,
        revenue_growth_3y=8.0,
        eps_growth_3y=12.0,
        payout_ratio=15.0,
        market_cap_bn=2800.0,
    )
    # Compute grade/scores manually for mock
    aapl.moat_score = 26
    aapl.fortress_score = 18
    aapl.management_score = 16
    aapl.valuation_score = 18
    aapl.total_score = 78
    aapl.grade = "A"
    aapl.data_quality = "HIGH"
    aapl.strengths = [
        "ROE eccezionale (147%)",
        "Gross margin > 45% → pricing power elevato",
        "Net margin stabile al 25%",
        "ROIC 55% → moat economico solido",
    ]
    aapl.concerns = [
        "Debt/equity 1.5 (accettabile per Apple)",
        "Current ratio < 1.2 (gestione treasury aggressiva)",
        "P/E 28x: valutazione piena",
    ]
    aapl.verdict = (
        "Apple soddisfa i criteri Buffett su profittabilità e vantaggio competitivo. "
        "La valutazione è elevata ma giustificata dall'ecosistema e dal brand."
    )
    return [aapl]


def get_mock_document(accession: str, file_date: str) -> str:
    mapping = {
        "0000320193-26-001234": mock_form4_xml_large_buy(file_date=file_date),
        "0001652044-26-005678": mock_form4_xml_small_sale(file_date=file_date),
        "0000789019-26-009999": mock_form4_xml_option_exercise(file_date=file_date),
        "0000320193-26-002345": mock_8k_html(file_date=file_date),
        "0001018724-26-003456": mock_8k_html(
            company="AMAZON COM INC", ticker="AMZN", file_date=file_date
        ),
        "0001067983-26-004567": mock_sc13g_html(file_date=file_date),
    }
    return mapping.get(accession, f"<html><body>Mock document for {accession}</body></html>")
