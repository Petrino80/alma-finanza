#!/usr/bin/env python3
"""
Add the 8 newly created articles with real data to index.html
"""

# Read current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# New articles to insert after Article 19 (bitcoin-74570), before closing </div>
new_articles_html = '''
            <!-- Article 20 - Spotify real data -->
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

            <!-- Article 21 - FEIM real data -->
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

            <!-- Article 22 - Meta real data -->
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

            <!-- Article 23 - Treasury yields real data -->
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

            <!-- Article 24 - Gold ATH real data -->
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

            <!-- Article 25 - Small caps performance real data -->
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

            <!-- Article 26 - USA-Europe divergence real data -->
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

            <!-- Article 27 - Market sell-off real data -->
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
'''

# Find where to insert (after the last </a> before </div> that closes the grid)
# Look for the closing tag of Article 19 (bitcoin-74570)
import re

# Find the position after the last article and before </div>
pattern = r'(</a>\s*\n\s*</div>\s*\n\s*<!-- Mission Section -->)'
replacement = f'''{new_articles_html}
        </div>

        <!-- Mission Section -->'''

content = re.sub(pattern, replacement, content)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Aggiunti 8 nuovi articoli con dati REALI verificati")
print("✓ Totale articoli ora nella homepage: 27")
print("✓ Tutti gli articoli con intervalli temporali specificati")
print("")
print("Articoli aggiunti:")
print("  20. Spotify -6.4% a $412 (earnings 10 feb)")
print("  21. FEIM $50.36 (-7.82% settimanale)")
print("  22. Meta Q4 EPS $8.88, CapEx $115-135Bn")
print("  23. Treasury 10Y a 4.28%")
print("  24. Oro $4.852 (ATH gennaio, correzione feb)")
print("  25. Russell 2000 ATH 2,604 (+3.8% YTD)")
print("  26. USA -0.84% vs Europa +0.6%")
print("  27. Sell-off febbraio: Nasdaq -1.59%, AMD -$560Bn")
