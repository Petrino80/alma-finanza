#!/usr/bin/env python3
"""Aggiornamento completo 12 marzo 2026 — FASE 3+4+5"""
import re, os

os.chdir('/Users/ferrarapetrino/Downloads/files-2')

# ============================================================
# FASE 3a — HOMEPAGE: Ticker
# ============================================================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace entire ticker content (both original + duplicate for loop)
old_ticker_start = '<div class="ticker-content">'
old_ticker_end = '</div></div>\n    </div>'

new_ticker = '''<div class="ticker-content">
            <div class="ticker-item" data-ticker="dow"><a href="https://finance.yahoo.com/quote/%5EDJI" target="_blank">🇺🇸 Dow <span class="negative">46.678 (-1,56%)</span></a></div>
            <div class="ticker-item" data-ticker="sp500"><a href="https://finance.yahoo.com/quote/%5EGSPC" target="_blank">🇺🇸 S&P 500 <span class="negative">6.673 (-1,50%)</span></a></div>
            <div class="ticker-item" data-ticker="nasdaq"><a href="https://finance.yahoo.com/quote/%5EIXIC" target="_blank">🇺🇸 Nasdaq <span class="negative">22.312 (-1,78%)</span></a></div>
            <div class="ticker-item" data-ticker="ftsemib"><a href="https://finance.yahoo.com/quote/FTSEMIB.MI" target="_blank">🇮🇹 FTSE MIB <span class="negative">44.460 (-0,70%)</span></a></div>
            <div class="ticker-item" data-ticker="leonardo"><a href="https://finance.yahoo.com/quote/LDO.MI" target="_blank">🚀 Leonardo <span class="positive">+6,0% (Piano 2030)</span></a></div>
            <div class="ticker-item" data-ticker="dax"><a href="https://finance.yahoo.com/quote/%5EGDAXI" target="_blank">🇩🇪 DAX <span class="negative">23.466 (-0,74%)</span></a></div>
            <div class="ticker-item" data-ticker="cac"><a href="https://finance.yahoo.com/quote/%5EFCHI" target="_blank">🇫🇷 CAC 40 <span class="negative">7.995 (-0,58%)</span></a></div>
            <div class="ticker-item" data-ticker="oil"><a href="https://finance.yahoo.com/quote/CL%3DF" target="_blank">🛢️ WTI <span class="positive">$95,73 (+9,72%)</span></a></div>
            <div class="ticker-item" data-ticker="brent"><a href="articolo-petrolio-12mar-brent-100-dollari-hormuz-crisi.html">🛢️ <span class="negative">BRENT SOPRA $100: prima volta dal 2022. Hormuz chiuso</span></a></div>
            <div class="ticker-item" data-ticker="gold"><a href="https://finance.yahoo.com/quote/GC%3DF" target="_blank">Oro <span class="negative">$5.156 (-0,39%)</span></a></div>
            <div class="ticker-item" data-ticker="btc"><a href="https://finance.yahoo.com/quote/BTC-USD" target="_blank">Bitcoin <span class="negative">$69.688 (-0,4%)</span></a></div>
            <div class="ticker-item" data-ticker="oracle"><a href="articolo-oracle-12mar-q3-earnings-cloud-ai-243-percento.html">💻 <span class="positive">Oracle +10% AH: cloud +44%, AI +243%</span></a></div>
            <!-- Duplicate for seamless loop -->
            <div class="ticker-item" data-ticker="dow"><a href="https://finance.yahoo.com/quote/%5EDJI" target="_blank">🇺🇸 Dow <span class="negative">46.678 (-1,56%)</span></a></div>
            <div class="ticker-item" data-ticker="sp500"><a href="https://finance.yahoo.com/quote/%5EGSPC" target="_blank">🇺🇸 S&P 500 <span class="negative">6.673 (-1,50%)</span></a></div>
            <div class="ticker-item" data-ticker="nasdaq"><a href="https://finance.yahoo.com/quote/%5EIXIC" target="_blank">🇺🇸 Nasdaq <span class="negative">22.312 (-1,78%)</span></a></div>
            <div class="ticker-item" data-ticker="ftsemib"><a href="https://finance.yahoo.com/quote/FTSEMIB.MI" target="_blank">🇮🇹 FTSE MIB <span class="negative">44.460 (-0,70%)</span></a></div>
            <div class="ticker-item" data-ticker="leonardo"><a href="https://finance.yahoo.com/quote/LDO.MI" target="_blank">🚀 Leonardo <span class="positive">+6,0% (Piano 2030)</span></a></div>
            <div class="ticker-item" data-ticker="dax"><a href="https://finance.yahoo.com/quote/%5EGDAXI" target="_blank">🇩🇪 DAX <span class="negative">23.466 (-0,74%)</span></a></div>
            <div class="ticker-item" data-ticker="cac"><a href="https://finance.yahoo.com/quote/%5EFCHI" target="_blank">🇫🇷 CAC 40 <span class="negative">7.995 (-0,58%)</span></a></div>
            <div class="ticker-item" data-ticker="oil"><a href="https://finance.yahoo.com/quote/CL%3DF" target="_blank">🛢️ WTI <span class="positive">$95,73 (+9,72%)</span></a></div>
            <div class="ticker-item" data-ticker="brent"><a href="articolo-petrolio-12mar-brent-100-dollari-hormuz-crisi.html">🛢️ <span class="negative">BRENT SOPRA $100: prima volta dal 2022. Hormuz chiuso</span></a></div>
            <div class="ticker-item" data-ticker="gold"><a href="https://finance.yahoo.com/quote/GC%3DF" target="_blank">Oro <span class="negative">$5.156 (-0,39%)</span></a></div>
            <div class="ticker-item" data-ticker="btc"><a href="https://finance.yahoo.com/quote/BTC-USD" target="_blank">Bitcoin <span class="negative">$69.688 (-0,4%)</span></a></div>
            <div class="ticker-item" data-ticker="oracle"><a href="articolo-oracle-12mar-q3-earnings-cloud-ai-243-percento.html">💻 <span class="positive">Oracle +10% AH: cloud +44%, AI +243%</span></a></div>
        </div></div>
    </div>'''

# Find and replace ticker
ticker_match = re.search(r'<div class="ticker-content">.*?</div></div>\n    </div>', html, re.DOTALL)
if ticker_match:
    html = html[:ticker_match.start()] + new_ticker + html[ticker_match.end():]
    print("✅ Ticker aggiornato")
else:
    print("❌ Ticker non trovato")

# ============================================================
# FASE 3b — HOMEPAGE: Data header
# ============================================================
html = html.replace('Mercoledì 11 Marzo 2026', 'Giovedì 12 Marzo 2026')
print("✅ Data aggiornata: Giovedì 12 Marzo 2026")

# ============================================================
# FASE 3c — HOMEPAGE: Stats Bar
# ============================================================
# Dow
html = re.sub(
    r'(<div class="text-xs text-gray-400 dark:text-slate-600 mb-1">Dow Jones</div>\s*<div class="text-lg font-bold text-gray-900 dark:text-white">)[\d.]+</div>\s*<div class="text-xs \w+">.*?</div>',
    r'\g<1>46.678</div>\n                <div class="text-xs negative">-739 (-1,56%)</div>',
    html
)
# S&P
html = re.sub(
    r'(<div class="text-xs text-gray-400 dark:text-slate-600 mb-1">S&amp;P 500</div>\s*<div class="text-lg font-bold text-gray-900 dark:text-white">)[\d.]+</div>\s*<div class="text-xs \w+">.*?</div>',
    r'\g<1>6.673</div>\n                <div class="text-xs negative">-102 (-1,50%)</div>',
    html
)
# MIB
html = re.sub(
    r'(<div class="text-xs text-gray-400 dark:text-slate-600 mb-1">FTSE MIB</div>\s*<div class="text-lg font-bold text-gray-900 dark:text-white">)[\d.]+</div>\s*<div class="text-xs \w+">.*?</div>',
    r'\g<1>44.460</div>\n                <div class="text-xs negative">-0,70%</div>',
    html
)
# WTI
html = re.sub(
    r'(<div class="text-xs text-gray-400 dark:text-slate-600 mb-1">WTI Crude</div>\s*<div class="text-lg font-bold text-gray-900 dark:text-white">)\$[\d.]+</div>\s*<div class="text-xs \w+">.*?</div>',
    r'\g<1>$96</div>\n                <div class="text-xs positive">+9,72%</div>',
    html
)
# Oro
html = re.sub(
    r'(<div class="text-xs text-gray-400 dark:text-slate-600 mb-1">Oro</div>\s*<div class="text-lg font-bold text-gray-900 dark:text-white">)\$[\d.]+</div>\s*<div class="text-xs \w+">.*?</div>',
    r'\g<1>$5.156</div>\n                <div class="text-xs negative">-0,39%</div>',
    html
)
# Bitcoin
html = re.sub(
    r'(<div class="text-xs text-gray-400 dark:text-slate-600 mb-1">Bitcoin</div>\s*<div class="text-lg font-bold text-gray-900 dark:text-white">)\$[\d.]+</div>\s*<div class="text-xs \w+">.*?</div>',
    r'\g<1>$69.688</div>\n                <div class="text-xs negative">-0,4%</div>',
    html
)
print("✅ Stats bar aggiornata (6 valori)")

# ============================================================
# FASE 3d — HOMEPAGE: Hero
# ============================================================
old_hero = re.search(r'<!-- Hero -->.*?</div>\s*</div>\s*</div>\s*</div>\s*</div>', html, re.DOTALL)
if old_hero:
    new_hero = '''<!-- Hero -->
        <div class="hero-box bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 mb-10">
            <div class="grid md:grid-cols-3">
                <div class="md:col-span-2 p-8 md:p-12">
                    <div class="flex items-center gap-3 mb-4">
                        <div class="dot bg-red-500 animate-pulse"></div>
                        <span class="text-xs font-bold text-red-600 dark:text-red-400 uppercase tracking-wider">Breaking · 12 Mar 2026</span>
                    </div>
                    <h1 class="text-3xl md:text-4xl font-black text-gray-900 dark:text-white mb-4 leading-tight montserrat-font">
                        Brent sopra $100: shock petrolio affonda Wall Street ai minimi 2026. Leonardo +6%. Oracle batte tutto.
                    </h1>
                    <div class="accent-line mb-4"></div>
                    <p class="text-gray-500 dark:text-slate-400 text-lg leading-relaxed mb-6">
                        WTI +9,72% a $96, Brent $100,46. Dow -1,56%, S&P -1,50%, Nasdaq -1,78% ai minimi annuali. Leonardo vola +6% con piano 2030. Generali utile record 4,3 mld. Morgan Stanley limita riscatti. Oracle +10% after hours.
                    </p>
                    <a href="articolo-petrolio-12mar-brent-100-dollari-hormuz-crisi.html" class="inline-flex items-center text-teal-600 dark:text-teal-400 font-semibold text-sm hover:text-teal-700 dark:hover:text-teal-300 transition group">
                        Leggi l'articolo completo
                        <svg class="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                    </a>
                </div>
                <div class="flex items-center justify-center p-8 bg-gray-50 dark:bg-[#0a0f19]/50 border-l border-gray-100 dark:border-slate-700/20">
                    <div class="text-center">
                        <div class="text-5xl font-black text-gray-900 dark:text-white mb-1">$100</div>
                        <div class="text-sm text-gray-500 dark:text-slate-500 mb-3">Brent al barile</div>
                        <div class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-red-50 dark:bg-red-500/15 text-red-600 dark:text-red-400">Giorno +9,22%</div>
                        <div class="mt-4 space-y-1 text-xs text-gray-400 dark:text-slate-600">
                            <div>Hormuz chiuso · Dow -1,56%</div>
                            <div>Leonardo +6% · Oracle +10% AH</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>'''
    html = html[:old_hero.start()] + new_hero + html[old_hero.end():]
    print("✅ Hero aggiornato: Brent $100 + shock petrolio")
else:
    print("❌ Hero non trovato")

# ============================================================
# FASE 3e — HOMEPAGE: Section header + 5 nuove theme-cards
# ============================================================
# Update section header
html = html.replace('Oggi, 11 Marzo', 'Oggi, 12 Marzo')
print("✅ Section header aggiornato: Oggi, 12 Marzo")

# Add 5 new cards + day separator before the 11 March cards
new_cards = '''
            <!-- ====== ARTICOLI 12 MARZO 2026 ====== -->

            <!-- Wall Street 12 mar -->
            <a href="articolo-wall-street-12mar-shock-petrolio-sp500-dow-minimi-2026.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-blue-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-blue-50 dark:bg-blue-500/15 text-blue-700 dark:text-blue-400 border border-transparent dark:border-blue-500/20">Wall Street</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Wall Street crolla: shock petrolio, S&P 500 e Dow ai minimi 2026. Brent sopra $100</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Dow -739 a 46.678, S&P -1,50%, Nasdaq -1,78%. Brent $100,46. Airlines in caduta: Southwest -7%. Goldman -4,47%. Oracle +10% AH.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">12 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- FTSE MIB 12 mar -->
            <a href="articolo-ftse-mib-12mar-leonardo-piano-2030-generali-record.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-emerald-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-green-50 dark:bg-emerald-500/15 text-green-700 dark:text-emerald-400 border border-transparent dark:border-emerald-500/20">Piazza Affari</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Leonardo vola +6% con piano 2030: 142 mld di ordini. Generali record 4,3 mld. Banche in rosso</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">FTSE MIB -0,7%. Leonardo +6% piano industriale. Generali dividendo 1,64€ e buyback 500 mln. MPS -4,6%, Mediobanca -4,4%.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">12 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Petrolio 12 mar -->
            <a href="articolo-petrolio-12mar-brent-100-dollari-hormuz-crisi.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-amber-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-amber-50 dark:bg-amber-500/15 text-amber-700 dark:text-amber-400 border border-transparent dark:border-amber-500/20">Commodities</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Brent sopra $100: prima volta dal 2022. WTI +9,72%. Hormuz chiuso, Iraq ferma export</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Brent $100,46 (+9,22%), WTI $95,73. Khamenei: Hormuz resta chiuso. Tre navi colpite. Iraq chiude terminali. Rilascio IEA inefficace.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">12 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Oracle 12 mar -->
            <a href="articolo-oracle-12mar-q3-earnings-cloud-ai-243-percento.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-purple-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-purple-50 dark:bg-purple-500/15 text-purple-700 dark:text-purple-400 border border-transparent dark:border-purple-500/20">Tech/AI</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Oracle batte tutto: cloud +44%, AI infra +243%, titolo +10% AH. Guidance FY27 a $90 mld</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Q3: ricavi $17,2B (+22%), cloud $8,9B. AI infrastructure +243%, multicloud DB +531%. RPO $553B (+325%). EPS $1,79 beat.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">12 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Morgan Stanley Private Credit 12 mar -->
            <a href="articolo-morgan-stanley-12mar-private-credit-riscatti-crisi.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-red-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-red-50 dark:bg-red-500/15 text-red-700 dark:text-red-400 border border-transparent dark:border-red-500/20">Finanza/Macro</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Crisi private credit: Morgan Stanley limita i riscatti. BlackRock e Cliffwater seguono</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">North Haven ($8 mld): investitori chiedono 11%, ricevono 5%. L'AI minaccia il software. Goldman -4,47%. Timori contagio sistemico.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">12 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Day separator: 11 Marzo -->
            <div class="col-span-full flex items-center gap-3 mt-6 mb-2">
                <div class="w-10 h-0.5 rounded-full bg-gray-200 dark:bg-slate-700/40"></div>
                <h2 class="text-sm font-bold montserrat-font text-gray-400 dark:text-slate-600 uppercase tracking-wider">11 Marzo 2026</h2>
                <div class="flex-1 h-0.5 rounded-full bg-gray-100 dark:bg-slate-800/20"></div>
            </div>

'''

# Insert before the 11 March articles
marker = '<!-- ====== ARTICOLI 11 MARZO 2026 ====== -->'
if marker in html:
    html = html.replace(marker, new_cards + '            ' + marker)
    print("✅ 5 nuove theme-cards + day separator aggiunti")
else:
    print("❌ Marker 11 marzo non trovato")

# Save homepage
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("✅ index.html salvato")

# ============================================================
# FASE 3f — SITEMAP
# ============================================================
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

# Update homepage lastmod
sitemap = re.sub(r'(<url>\s*<loc>https://www\.almafinanza\.com/</loc>\s*<lastmod>)\d{4}-\d{2}-\d{2}(</lastmod>)', r'\g<1>2026-03-12\2', sitemap)

new_urls = '''
    <!-- 12 Marzo 2026 -->
    <url>
        <loc>https://www.almafinanza.com/articolo-wall-street-12mar-shock-petrolio-sp500-dow-minimi-2026.html</loc>
        <lastmod>2026-03-12</lastmod>
        <changefreq>never</changefreq>
        <priority>0.9</priority>
        <news:news>
            <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
            <news:publication_date>2026-03-12</news:publication_date>
            <news:title>Wall Street crolla: shock petrolio affonda S&amp;P 500 e Dow ai minimi 2026</news:title>
        </news:news>
    </url>
    <url>
        <loc>https://www.almafinanza.com/articolo-ftse-mib-12mar-leonardo-piano-2030-generali-record.html</loc>
        <lastmod>2026-03-12</lastmod>
        <changefreq>never</changefreq>
        <priority>0.9</priority>
        <news:news>
            <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
            <news:publication_date>2026-03-12</news:publication_date>
            <news:title>FTSE MIB: Leonardo vola +6% con piano 2030, Generali utile record</news:title>
        </news:news>
    </url>
    <url>
        <loc>https://www.almafinanza.com/articolo-petrolio-12mar-brent-100-dollari-hormuz-crisi.html</loc>
        <lastmod>2026-03-12</lastmod>
        <changefreq>never</changefreq>
        <priority>0.9</priority>
        <news:news>
            <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
            <news:publication_date>2026-03-12</news:publication_date>
            <news:title>Brent sopra $100: prima volta dal 2022. Hormuz chiuso, Iraq ferma export</news:title>
        </news:news>
    </url>
    <url>
        <loc>https://www.almafinanza.com/articolo-oracle-12mar-q3-earnings-cloud-ai-243-percento.html</loc>
        <lastmod>2026-03-12</lastmod>
        <changefreq>never</changefreq>
        <priority>0.9</priority>
        <news:news>
            <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
            <news:publication_date>2026-03-12</news:publication_date>
            <news:title>Oracle Q3: cloud +44%, AI infra +243%, titolo +10% after hours</news:title>
        </news:news>
    </url>
    <url>
        <loc>https://www.almafinanza.com/articolo-morgan-stanley-12mar-private-credit-riscatti-crisi.html</loc>
        <lastmod>2026-03-12</lastmod>
        <changefreq>never</changefreq>
        <priority>0.9</priority>
        <news:news>
            <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
            <news:publication_date>2026-03-12</news:publication_date>
            <news:title>Morgan Stanley limita riscatti: crisi private credit si allarga</news:title>
        </news:news>
    </url>
'''

# Insert after first <url> block (homepage) — find the 11 marzo comment or first article URL
insert_marker = '<!-- 11 Marzo 2026 -->'
if insert_marker in sitemap:
    sitemap = sitemap.replace(insert_marker, new_urls + '\n    ' + insert_marker)
else:
    # Fallback: insert before first article URL
    first_article = re.search(r'(\s*<url>\s*<loc>https://www\.almafinanza\.com/articolo-)', sitemap)
    if first_article:
        sitemap = sitemap[:first_article.start()] + new_urls + sitemap[first_article.start():]

sitemap = sitemap.replace('<lastmod>2026-03-11</lastmod>\n        <changefreq>daily', '<lastmod>2026-03-12</lastmod>\n        <changefreq>daily')

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap)
print("✅ sitemap.xml aggiornata con 5 nuovi URL")

# ============================================================
# FASE 4 — PAGINE CATEGORIA
# ============================================================

def add_to_category(filename, articles):
    """Add articles to a category page"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Build the new date section
    section_html = '''
        <section class="mb-12">
            <div class="flex items-center mb-6">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Giovedì, 12 Marzo 2026</h2>
                <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
            </div>
            <div class="grid md:grid-cols-3 gap-6">
'''
    for art in articles:
        section_html += f'''                <a href="{art['href']}" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:{art['badge_bg']};color:{art['badge_color']};">{art['category']}</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">{art['title']}</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">{art['desc']}</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 12 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>
'''
    section_html += '''            </div>
        </section>
'''

    # Insert after <main> tag
    main_match = re.search(r'(<main[^>]*>)', content)
    if main_match:
        insert_pos = main_match.end()
        content = content[:insert_pos] + '\n' + section_html + content[insert_pos:]
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ {filename}: +{len(articles)} articoli aggiunti")
    else:
        print(f"❌ {filename}: <main> non trovato")

# Wall Street: WS, Oracle, Morgan Stanley
add_to_category('categoria-wall-street.html', [
    {
        'href': 'articolo-wall-street-12mar-shock-petrolio-sp500-dow-minimi-2026.html',
        'badge_bg': '#dbeafe', 'badge_color': '#1e40af',
        'category': 'Wall Street',
        'title': 'Wall Street crolla: shock petrolio, S&P e Dow ai minimi 2026. Brent $100',
        'desc': 'Dow -739 a 46.678, S&P -1,50%, Nasdaq -1,78%. Brent sopra $100. Airlines in caduta. Oracle +10% AH.'
    },
    {
        'href': 'articolo-oracle-12mar-q3-earnings-cloud-ai-243-percento.html',
        'badge_bg': '#f3e8ff', 'badge_color': '#6b21a8',
        'category': 'Tech/AI',
        'title': 'Oracle batte tutto: cloud +44%, AI +243%, +10% after hours',
        'desc': 'Ricavi $17,2B (+22%), cloud $8,9B. RPO $553B (+325%). Guidance FY27 alzata a $90B.'
    },
    {
        'href': 'articolo-morgan-stanley-12mar-private-credit-riscatti-crisi.html',
        'badge_bg': '#fce7f3', 'badge_color': '#9f1239',
        'category': 'Finanza/Macro',
        'title': 'Crisi private credit: Morgan Stanley limita riscatti, contagio in atto',
        'desc': 'North Haven ($8 mld): riscatti limitati al 5%. BlackRock, Cliffwater seguono. AI minaccia software credit.'
    }
])

# Borsa Milano: FTSE MIB
add_to_category('categoria-borsa-milano.html', [
    {
        'href': 'articolo-ftse-mib-12mar-leonardo-piano-2030-generali-record.html',
        'badge_bg': '#dcfce7', 'badge_color': '#166534',
        'category': 'Piazza Affari',
        'title': 'Leonardo +6% piano 2030, Generali utile record 4,3 mld. Banche in rosso',
        'desc': 'FTSE MIB -0,7%. Leonardo: 142 mld ordini, ricavi a 30 mld. Generali dividendo 1,64€. MPS -4,6%.'
    }
])

# Commodities: Petrolio
add_to_category('categoria-commodities.html', [
    {
        'href': 'articolo-petrolio-12mar-brent-100-dollari-hormuz-crisi.html',
        'badge_bg': '#fef3c7', 'badge_color': '#92400e',
        'category': 'Petrolio',
        'title': 'Brent sopra $100: prima volta dal 2022. WTI +9,72%. Hormuz chiuso',
        'desc': 'Brent $100,46 (+9,22%), WTI $95,73. Khamenei conferma blocco. Iraq chiude terminali. Rilascio IEA inefficace.'
    }
])

print("✅ FASE 4 completata — Pagine categoria aggiornate")

# ============================================================
# FASE 5 — IMPARA LA FINANZA
# ============================================================
with open('impara-finanza.html', 'r', encoding='utf-8') as f:
    impara = f.read()

# Define concept cards to add per section
concepts = [
    # Macroeconomia e Banche Centrali (cyan)
    {
        'section': 'Macroeconomia e Banche Centrali',
        'cards': [
            {
                'href': 'articolo-wall-street-12mar-shock-petrolio-sp500-dow-minimi-2026.html',
                'color': 'cyan',
                'title': 'Capitolazione di mercato',
                'desc': 'Vendita massiccia e indiscriminata degli investitori in preda al panico. Si riconosce da volumi elevati, cali su tutti i settori e VIX in impennata.',
                'source': 'Wall Street 12 Mar: shock petrolio'
            },
            {
                'href': 'articolo-morgan-stanley-12mar-private-credit-riscatti-crisi.html',
                'color': 'cyan',
                'title': 'Private Credit e Direct Lending',
                'desc': 'Area della finanza in cui fondi specializzati erogano prestiti direttamente alle aziende, bypassando il sistema bancario. Oltre $2.000 miliardi di asset globali.',
                'source': 'Morgan Stanley: crisi private credit'
            }
        ]
    },
    # Meccanismi di Mercato (purple)
    {
        'section': 'Meccanismi di Mercato',
        'cards': [
            {
                'href': 'articolo-wall-street-12mar-shock-petrolio-sp500-dow-minimi-2026.html',
                'color': 'purple',
                'title': 'Forward P/E Compression',
                'desc': 'Durante uno shock, i multipli di valutazione si comprimono: i prezzi scendono e le stime sugli utili vengono riviste al ribasso simultaneamente.',
                'source': 'Wall Street 12 Mar: shock petrolio'
            },
            {
                'href': 'articolo-petrolio-12mar-brent-100-dollari-hormuz-crisi.html',
                'color': 'purple',
                'title': 'Contango e Backwardation',
                'desc': 'In contango i futures a lunga scadenza costano più dei brevi. In backwardation il contrario: segnale di shortage fisico immediato.',
                'source': 'Petrolio 12 Mar: Brent sopra $100'
            },
            {
                'href': 'articolo-morgan-stanley-12mar-private-credit-riscatti-crisi.html',
                'color': 'purple',
                'title': 'Gating nei fondi di investimento',
                'desc': 'Meccanismo che limita i riscatti a una percentuale massima per trimestre (5-10%), proteggendo gli investitori da vendite forzate di asset illiquidi.',
                'source': 'Morgan Stanley: crisi private credit'
            }
        ]
    },
    # Modelli di Business (teal)
    {
        'section': 'Modelli di Business',
        'cards': [
            {
                'href': 'articolo-oracle-12mar-q3-earnings-cloud-ai-243-percento.html',
                'color': 'teal',
                'title': 'IaaS vs SaaS vs PaaS',
                'desc': 'I tre livelli del cloud: Infrastructure (server virtuali), Platform (strumenti sviluppo) e Software (app complete). Oracle compete su tutti e tre.',
                'source': 'Oracle Q3: cloud +44%, AI +243%'
            },
            {
                'href': 'articolo-ftse-mib-12mar-leonardo-piano-2030-generali-record.html',
                'color': 'teal',
                'title': 'Piano industriale pluriennale',
                'desc': 'Documento strategico con cui un\'azienda quotata comunica al mercato obiettivi finanziari, crescita e dividendi per i successivi 3-5 anni.',
                'source': 'Leonardo: piano 2030'
            }
        ]
    },
    # Metriche Settoriali (amber)
    {
        'section': 'Metriche Settoriali',
        'cards': [
            {
                'href': 'articolo-oracle-12mar-q3-earnings-cloud-ai-243-percento.html',
                'color': 'amber',
                'title': 'RPO (Remaining Performance Obligations)',
                'desc': 'Valore totale dei contratti firmati ma non ancora eseguiti — il backlog di ricavi futuri garantiti. Il RPO di Oracle ha raggiunto $553 miliardi.',
                'source': 'Oracle Q3: cloud +44%, AI +243%'
            },
            {
                'href': 'articolo-ftse-mib-12mar-leonardo-piano-2030-generali-record.html',
                'color': 'amber',
                'title': 'Combined Ratio (Assicurazioni Danni)',
                'desc': 'Loss Ratio + Expense Ratio. Sotto 100% = profitto tecnico. Il 92,6% di Generali indica 7,4€ di margine ogni 100€ di premi.',
                'source': 'Generali utile record 4,3 mld'
            }
        ]
    },
    # Gestione del Rischio (red)
    {
        'section': 'Gestione del Rischio',
        'cards': [
            {
                'href': 'articolo-wall-street-12mar-shock-petrolio-sp500-dow-minimi-2026.html',
                'color': 'red',
                'title': 'Beta dei titoli ciclici negli shock energetici',
                'desc': 'Il beta misura la sensibilità di un titolo al mercato. Durante shock petroliferi, i ciclici (airlines, auto) mostrano beta amplificato: Southwest -7% vs S&P -1,5%.',
                'source': 'Wall Street 12 Mar: shock petrolio'
            }
        ]
    },
    # Geopolitica e Mercati (rose)
    {
        'section': 'Geopolitica e Mercati',
        'cards': [
            {
                'href': 'articolo-petrolio-12mar-brent-100-dollari-hormuz-crisi.html',
                'color': 'rose',
                'title': 'War Premium sul petrolio',
                'desc': 'Componente del prezzo che riflette il rischio geopolitico anziché i fondamentali. Stimato in $25-30/barile durante la crisi di Hormuz.',
                'source': 'Petrolio 12 Mar: Brent sopra $100'
            },
            {
                'href': 'articolo-petrolio-12mar-brent-100-dollari-hormuz-crisi.html',
                'color': 'rose',
                'title': 'Correlazione inversa oro-dollaro (petrodollar)',
                'desc': 'L\'oro scende quando il dollaro sale: i Paesi vendono le proprie valute per comprare dollari e pagare il greggio (petrodollar recycling).',
                'source': 'Petrolio 12 Mar: Brent sopra $100'
            }
        ]
    },
    # Settore Finanziario & Bancario (emerald)
    {
        'section': 'Settore Finanziario',
        'cards': [
            {
                'href': 'articolo-ftse-mib-12mar-leonardo-piano-2030-generali-record.html',
                'color': 'emerald',
                'title': 'Solvency Ratio (Solvency II)',
                'desc': 'Rapporto tra fondi propri e requisito patrimoniale nelle assicurazioni. Il 219% di Generali significa 2,19x il capitale minimo richiesto.',
                'source': 'Generali utile record 4,3 mld'
            },
            {
                'href': 'articolo-morgan-stanley-12mar-private-credit-riscatti-crisi.html',
                'color': 'emerald',
                'title': 'BDC (Business Development Company)',
                'desc': 'Società che eroga prestiti al middle market USA, obbligata a distribuire almeno il 90% del reddito come dividendi. Circa $400 miliardi di asset.',
                'source': 'Morgan Stanley: crisi private credit'
            }
        ]
    }
]

for concept_group in concepts:
    section_name = concept_group['section']
    # Find the section by its emoji+name pattern
    section_pattern = rf'({section_name}.*?)(</div>\s*</section>)'
    section_match = re.search(section_pattern, impara, re.DOTALL)

    if not section_match:
        # Try simpler match
        section_pattern = rf'({section_name})'
        section_match = re.search(section_pattern, impara)
        if section_match:
            # Find the next </div></section> after this point
            rest = impara[section_match.end():]
            close_match = re.search(r'(</div>\s*</section>)', rest)
            if close_match:
                insert_pos = section_match.end() + close_match.start()
                cards_html = ''
                for card in concept_group['cards']:
                    cards_html += f'''
                <a href="{card['href']}" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-{card['color']}-500 hover:border-{card['color']}-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">{card['title']}</h3>
                    <p class="text-sm text-gray-600">{card['desc']}</p>
                    <span class="text-xs text-{card['color']}-600 font-semibold mt-2 inline-block">→ Spiegato in: {card['source']}</span>
                </a>'''
                impara = impara[:insert_pos] + cards_html + '\n            ' + impara[insert_pos:]
                print(f"  ✅ {section_name}: +{len(concept_group['cards'])} concept-cards")
                continue

    if section_match:
        # Insert before the closing </div></section>
        insert_pos = section_match.start(2) if section_match.lastindex >= 2 else section_match.end()
        cards_html = ''
        for card in concept_group['cards']:
            cards_html += f'''
                <a href="{card['href']}" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-{card['color']}-500 hover:border-{card['color']}-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">{card['title']}</h3>
                    <p class="text-sm text-gray-600">{card['desc']}</p>
                    <span class="text-xs text-{card['color']}-600 font-semibold mt-2 inline-block">→ Spiegato in: {card['source']}</span>
                </a>'''
        impara = impara[:insert_pos] + cards_html + '\n            ' + impara[insert_pos:]
        print(f"  ✅ {section_name}: +{len(concept_group['cards'])} concept-cards")
    else:
        print(f"  ⚠️ Sezione '{section_name}' non trovata — skip")

with open('impara-finanza.html', 'w', encoding='utf-8') as f:
    f.write(impara)
print("✅ FASE 5 completata — impara-finanza.html aggiornata")

print("\n" + "="*60)
print("✅ TUTTE LE FASI 3-4-5 COMPLETATE!")
print("="*60)
