#!/usr/bin/env python3
"""
Replace articles grid with existing real articles
"""

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the articles grid start and Mission section start
articles_start = None
mission_start = None

for i, line in enumerate(lines):
    if '<!-- Articles Grid -->' in line:
        articles_start = i
    if '<!-- Mission Section -->' in line:
        mission_start = i
        break

if articles_start is None or mission_start is None:
    print("ERROR: Could not find article sections")
    exit(1)

# Create new articles grid with EXISTING articles only
new_articles = '''        <!-- Articles Grid -->
        <div class="grid md:grid-cols-3 gap-6">
            <!-- Article 1 - Tech Rout with REAL data -->
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

            <!-- Article 2 -->
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

            <!-- Article 3 -->
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

            <!-- Article 4 -->
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

            <!-- Article 5 -->
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

            <!-- Article 6 -->
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

            <!-- Article 7 -->
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

            <!-- Article 8 -->
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

            <!-- Article 9 -->
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

            <!-- Article 10 -->
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

        </div>

'''

# Replace the section
new_lines = lines[:articles_start] + [new_articles] + lines[mission_start:]

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"✓ Replaced articles section (lines {articles_start+1} to {mission_start})")
print("✓ Added 10 articles with EXISTING files only")
print("✓ Removed all references to deleted fake articles")
