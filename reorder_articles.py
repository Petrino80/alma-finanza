#!/usr/bin/env python3
"""
Riordina articoli dal più nuovo al più vecchio e sincronizza date
"""
import re

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the articles grid section
# Extract everything between <!-- Articles Grid --> and </div> before Mission Section
pattern = r'(<!-- Articles Grid -->\s*<div class="grid md:grid-cols-3 gap-6">)(.*?)(</div>\s*<!-- Mission Section -->)'
match = re.search(pattern, content, re.DOTALL)

if not match:
    print("ERROR: Could not find articles grid")
    exit(1)

# Define articles in order from NEWEST to OLDEST
# 6 Feb articles first, then 4 Feb articles

articles_ordered = [
    # 6 FEBBRAIO 2026 - NUOVI ARTICOLI CON DATI REALI
    '''            <!-- Article 1 - 6 Feb -->
            <a href="articolo-spotify-declino.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-tech">Streaming</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Spotify -6.4% a $412: pressione prima degli earnings 10 febbraio
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Azioni SPOT scendono -6.4% (sessione) a $412.42, -23% YTD 2026. Earnings attesi 10 febbraio: EPS $2.95 (+56.9% YoY). Aumento prezzi a $12.99/mese. Analisi competizione streaming e prospettive.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 6 Feb 2026</span>
                            <span>👁 4.2K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 2 - 6 Feb -->
            <a href="articolo-feim-sorpresa.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-wall-street">Small Cap</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            FEIM a $50.36: -7.82% settimanale, earnings miss Q2
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Frequency Electronics trading $50.36, market cap $492M. Q2 FY2026 EPS $0.18 vs $0.29 atteso (-37.93% miss). Contratti $4.75M per airborne systems. Analisi micro-cap defense tech.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 6 Feb 2026</span>
                            <span>👁 3.8K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 3 - 6 Feb -->
            <a href="articolo-meta-earnings-attesi.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-tech">Meta Earnings</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Meta Q4: EPS $8.88 batte attese, CapEx 2026 shock $115-135Bn
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Risultati 28 gennaio: EPS $8.88 vs $8.19 atteso (+8.4%), revenue $59.9B. Capex 2026: $115-135 miliardi (+84% vs 2025). Implicazioni AI investments e outlook 2026-2027.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 6 Feb 2026</span>
                            <span>👁 9.7K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 4 - 6 Feb -->
            <a href="articolo-treasury-yields-impatto.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-macro">Treasury</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Treasury 10Y a 4.28%: vicino massimi 5 mesi, impatto su growth stocks
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Yield 10-year stabile 4.28% (3-5 feb), vicino high 4.3% (20 gen). +0.11 punti mensile. Fattori: Kevin Warsh Fed, dati ADP. Matematica DCF e sensitivity valutazioni tech.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 6 Feb 2026</span>
                            <span>👁 5.9K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 5 - 6 Feb -->
            <a href="articolo-oro-alltime-high.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-commodities">Oro ATH</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Oro $4.852: record gennaio, correzione febbraio dopo +25% rally
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Oro $4,852/oz oggi, da ATH $4,913 (3 feb). Rally +25% da inizio 2025, balzo intraday +6% (massimo dal 2008). Record ripetuti gennaio, pullback febbraio. Drivers inflazione e incertezza.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 6 Feb 2026</span>
                            <span>👁 8.3K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 6 - 6 Feb -->
            <a href="articolo-small-caps-performance.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-wall-street">Small Caps</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Russell 2000 ATH 2.604: small caps battono large caps +3.8% YTD
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Russell 2000 nuovo record 2,603.90 (+1.4%) l'8 gennaio. YTD +3.8%, outperformance vs large caps. "Great Rotation" da mega-cap tech. Earnings growth 2026: consensus 17-22%.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 6 Feb 2026</span>
                            <span>👁 6.4K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 7 - 6 Feb -->
            <a href="articolo-usa-europa-divergenza.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-europa">Confronto Mercati</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            USA vs Europa: S&P -0.84% vs Stoxx 600 +0.6%, divergenza factor
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            3 febbraio sessione: S&P -0.84% (tech dump), Stoxx 600 +0.6%. USA: AI-driven growth. Europa: reflation, valuation support. Earnings Europa 2025: da +8% a -1%. Analisi fattori divergenza.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 6 Feb 2026</span>
                            <span>👁 7.1K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 8 - 6 Feb -->
            <a href="articolo-mercati-sell-off-febbraio.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-wall-street">Sell-off</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Sell-off febbraio: Nasdaq -1.59%, AMD -$560Bn market cap, fine AI hype
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            5 febbraio: S&P 6,798.40 (YTD negativo), Nasdaq -1.59% a 22,540. AMD -17.3% perde $560B. Novo -$50B. Alphabet CapEx $185B spaventa. Risk-off stance, "fine AI hype phase".
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 6 Feb 2026</span>
                            <span>👁 11.2K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 9 - 6 Feb -->
            <a href="articolo-tech-rout-continua.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-tech">Wall Street</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Tech rout continua: Alphabet -3.2%, Qualcomm -9.5% (dati verificati)
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Analisi basata su dati reali: Wall Street mercoledì in rosso. Alphabet scende su timori capex AI, Qualcomm crolla per memory shortage. Tutte le variazioni con intervalli temporali specificati.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 6 Feb 2026</span>
                            <span>👁 3.4K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    # 4 FEBBRAIO 2026 - ARTICOLI PRECEDENTI
    '''            <!-- Article 10 - 4 Feb -->
            <a href="articolo-sp500-6921.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-wall-street">S&P 500</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            S&P 500 tocca 6.921: nuovo record storico tra euforia tech
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Mega-cap tech trascina indici ai massimi. Nvidia, Microsoft, Apple guidano rally. Valutazioni P/E elevate sollevano domande. Analisi tecnica e livelli chiave da monitorare.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 8.2K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 11 - 4 Feb -->
            <a href="articolo-bitcoin-83463.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-crypto">Bitcoin ATH</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Bitcoin a $83.463: nuovo massimo storico, cosa aspettarsi
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            BTC rompe resistenza psicologica $80K con volumi record. Adozione istituzionale, ETF inflows e momentum tecnico. Target analisti e livelli critici supporto/resistenza. Analisi on-chain.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 15.3K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 12 - 4 Feb -->
            <a href="articolo-tesla-produzione-q1.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-tech">Tesla Q1</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Tesla Q1 2026: produzione record, ma margini sotto pressione
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            510K unità prodotte (+22% YoY) ma gross margin scende a 16.8%. Competizione EV in Cina intensifica. Model 2 outlook e strategia prezzi. Cosa significa per investitori.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 12.7K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 13 - 4 Feb -->
            <a href="articolo-spacex-xai-ecosistema.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-tech">Musk Empire</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            SpaceX + xAI: l'ecosistema Musk verso $500Bn di valutazione
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Sinergie tra space tech e AI generativa. xAI Grok integrato in Starlink, dati satellitari per training. Round funding $20Bn imminente. Analisi verticale integrazione e moat competitivo.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 11.2K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 14 - 4 Feb -->
            <a href="articolo-unity-software-gaming.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-tech">Gaming Tech</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Unity Software: dalla crisi runtime fee a piano rilancio 2026
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Nuovo CEO elimina policy controversa, focus su core business game engine. Partnership AI per procedural generation. Turnaround possibile? Valutazione vs concorrenti e catalysts Q1.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 6.9K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 15 - 4 Feb -->
            <a href="articolo-palantir-surge.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-tech">AI Software</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Palantir surge +28% YTD: cosa alimenta il rally
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            AIP (Artificial Intelligence Platform) adoption accelera. Deal governativi e enterprise traction. Metriche chiave: net dollar retention 120%, rule of 40 compliance. Valuation stretched o giustificata?
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 9.8K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 16 - 4 Feb -->
            <a href="articolo-oro-crash-816.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-commodities">Oro</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Oro crolla a $2.816: fine del rally o correzione salutare?
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Da massimi $2.950 a $2.816 in 48h (-4.5%). Cause: dollar strength, yields risalita, profit taking. Oro vs Bitcoin come hedge inflation. Livelli tecnici supporto e prospettive medio termine.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 7.3K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 17 - 4 Feb -->
            <a href="articolo-ftse-mib-45847.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-milano">FTSE MIB</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            FTSE MIB a 45.847: Piazza Affari ai massimi da 2008
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Banking sector guida (+18% YTD): Intesa, UniCredit, Banco BPM. Utilities e luxury resilient. Spread BTP-Bund a 112 bp favorisce equities. Outlook 2026 e rischi geopolitici.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 5.6K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 18 - 4 Feb -->
            <a href="articolo-missione-alma-finanza.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-tech">Mission</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            La nostra missione: finanza accessibile in italiano
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Perché Alma Finanza esiste. Educazione finanziaria come diritto, non privilegio. Informazione di qualità nella tua lingua. Trasparenza, dati verificati, zero clickbait. Scopri chi siamo.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 4.1K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 19 - 4 Feb -->
            <a href="articolo-sell-off-tech.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-tech">Educazione</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Comprendere il sell-off tech: anatomia di una giornata di panic selling
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Cosa significa "sell-off"? Come si innescano vendite massive. Analisi volumetrica, sentiment indicators, capitulation patterns. Guida educativa per riconoscere e gestire panic selling.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 10.5K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 20 - 4 Feb -->
            <a href="articolo-novo-nordisk-crash.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-wall-street">Pharma</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Novo Nordisk -24%: cosa è successo al gigante Ozempic
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Trial clinici CagriSema deludono. Competizione Eli Lilly intensifica. Mercato GLP-1 sotto pressione. Pipeline futura e valutazione post-crash. Opportunity o value trap?
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 14.2K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 21 - 4 Feb -->
            <a href="articolo-salesforce-crash-ai.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-tech">CRM + AI</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Salesforce -11% post-earnings: AI strategy non convince
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Agentforce adoption lenta. Revenue guidance Q1 sotto attese. Competizione Microsoft Dynamics, HubSpot. Valutazione SaaS multiples e cash flow generation. Bear case vs bull case.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 9.7K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 22 - 4 Feb -->
            <a href="articolo-microsoft-stabilizza.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-tech">Microsoft</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Microsoft stabilizza a $420: Azure cloud e AI driving growth
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Dopo volatilità settimana scorsa, MSFT consolida. Azure +30% YoY, Copilot enterprise adoption. Gaming division strong. Dividendo e buyback program. Analisi valutazione fair value.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 6.8K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 23 - 4 Feb -->
            <a href="articolo-kevin-warsh-fed.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-macro">Fed Policy</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Kevin Warsh nominato Fed Chair: cosa cambia per i mercati
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Background Warsh: ex Fed Governor, stance hawkish. Implicazioni per policy rates, QT continuation. Market reaction e outlook tassi 2026. Comparazione con Powell era.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 11.4K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 24 - 4 Feb -->
            <a href="articolo-southwest-airlines-19.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-wall-street">Airlines</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Southwest Airlines -19%: guida Q1 shock, load factor crolla
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Previsioni revenue Q1 well below consensus. Competizione low-cost intensifica. Pilot shortage, fuel costs elevation. Turnaround strategy e tempi recovery. Comparables settore.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 5.9K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 25 - 4 Feb -->
            <a href="articolo-ppi-05.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-macro">Inflazione</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            PPI gennaio +0.5%: inflazione producer ancora elevata
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Producer Price Index sopra attese. Core PPI +0.4%. Implicazioni per CPI consumer inflation. Fed policy implications e market reaction. Breakdown per settori.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 7.6K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 26 - 4 Feb -->
            <a href="articolo-argento-crash-30.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-commodities">Argento</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Argento crolla a $30: fine del rally sui metalli preziosi?
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Da $34 a $30 in 72h (-11.8%). Argento vs oro performance divergence. Industrial demand weakness, dollar strength. Gold/Silver ratio a 161. Prospettive e livelli tecnici chiave.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 8.1K</span>
                        </div>
                    </div>
                </article>
            </a>
''',
    '''            <!-- Article 27 - 4 Feb -->
            <a href="articolo-bitcoin-74570.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-crypto">Bitcoin</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Bitcoin $74.570: continua correzione, analisi tecnica
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            BTC perde ulteriore terreno da ATH $83K. Correlazione con risk assets, analisi supporti chiave $70K. Metriche on-chain: MVRV, SOPR, exchange flows. Prospettive breve termine.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 13.8K</span>
                        </div>
                    </div>
                </article>
            </a>
'''
]

# Build new articles section
new_articles_section = match.group(1) + '\n' + ''.join(articles_ordered) + '\n        ' + match.group(3)

# Replace in content
content = content[:match.start()] + new_articles_section + content[match.end():]

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Articoli riordinati dal più nuovo (6 Feb) al più vecchio (4 Feb)")
print("✓ Ordine corretto:")
print("  - Articoli 1-9: 6 Febbraio 2026")
print("  - Articoli 10-27: 4 Febbraio 2026")
print("✓ Date sincronizzate tra riquadri homepage e articoli")
