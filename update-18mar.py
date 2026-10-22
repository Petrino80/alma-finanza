#!/usr/bin/env python3
"""Aggiornamento 18 Marzo 2026 — Homepage, sitemap, categorie, impara-finanza"""
import re

# ============================================================
# 1. INDEX.HTML
# ============================================================
with open('index.html', 'r') as f:
    html = f.read()

# --- TICKER ---
old_ticker_start = '            <div class="ticker-item" data-ticker="dow"><a href="https://finance.yahoo.com/quote/%5EDJI"'
new_ticker_block = '''            <div class="ticker-item" data-ticker="dow"><a href="https://finance.yahoo.com/quote/%5EDJI" target="_blank">🇺🇸 Dow <span class="negative">46.225 (-1,63%)</span></a></div>
            <div class="ticker-item" data-ticker="sp500"><a href="https://finance.yahoo.com/quote/%5EGSPC" target="_blank">🇺🇸 S&P 500 <span class="negative">6.624 (-1,36%)</span></a></div>
            <div class="ticker-item" data-ticker="nasdaq"><a href="https://finance.yahoo.com/quote/%5EIXIC" target="_blank">🇺🇸 Nasdaq <span class="negative">22.152 (-1,46%)</span></a></div>
            <div class="ticker-item" data-ticker="ftsemib"><a href="https://finance.yahoo.com/quote/FTSEMIB.MI" target="_blank">🇮🇹 FTSE MIB <span class="negative">44.741 (-0,33%)</span></a></div>
            <div class="ticker-item" data-ticker="fed"><a href="articolo-fed-18mar-tassi-fermi-ppi-inflazione-powell.html">🏛️ <span class="negative">Fed hawkish: PPI +0,7%, solo 1 taglio</span></a></div>
            <div class="ticker-item" data-ticker="micron"><a href="articolo-micron-18mar-earnings-record-hbm4-nvidia.html">🚀 <span class="positive">Micron: EPS $12,20 vs $9,31 atteso</span></a></div>
            <div class="ticker-item" data-ticker="enel"><a href="articolo-ftse-mib-18mar-enel-acea-buzzi-cucinelli.html">📉 <span class="negative">Enel -3,35%, Acea -11,3%</span></a></div>
            <div class="ticker-item" data-ticker="dax"><a href="https://finance.yahoo.com/quote/%5EGDAXI" target="_blank">🇩🇪 DAX <span class="negative">23.515 (-0,91%)</span></a></div>
            <div class="ticker-item" data-ticker="oil"><a href="articolo-geopolitica-18mar-iran-hormuz-petrolio-stagflazione.html">🛢️ WTI <span class="positive">$98,42 (+2,5%)</span></a></div>
            <div class="ticker-item" data-ticker="gold"><a href="https://finance.yahoo.com/quote/GC%3DF" target="_blank">🥇 Oro <span class="negative">$4.880 (-2,8%)</span></a></div>
            <div class="ticker-item" data-ticker="btc"><a href="https://finance.yahoo.com/quote/BTC-USD" target="_blank">₿ <span class="negative">Bitcoin $71.275 (-4,57%)</span></a></div>
            <div class="ticker-item" data-ticker="vix"><a href="https://finance.yahoo.com/quote/%5EVIX" target="_blank">⚠️ <span class="negative">VIX 25,09 (+12,16%)</span></a></div>
            <!-- Duplicate for seamless loop -->
            <div class="ticker-item" data-ticker="dow"><a href="https://finance.yahoo.com/quote/%5EDJI" target="_blank">🇺🇸 Dow <span class="negative">46.225 (-1,63%)</span></a></div>
            <div class="ticker-item" data-ticker="sp500"><a href="https://finance.yahoo.com/quote/%5EGSPC" target="_blank">🇺🇸 S&P 500 <span class="negative">6.624 (-1,36%)</span></a></div>
            <div class="ticker-item" data-ticker="nasdaq"><a href="https://finance.yahoo.com/quote/%5EIXIC" target="_blank">🇺🇸 Nasdaq <span class="negative">22.152 (-1,46%)</span></a></div>
            <div class="ticker-item" data-ticker="ftsemib"><a href="https://finance.yahoo.com/quote/FTSEMIB.MI" target="_blank">🇮🇹 FTSE MIB <span class="negative">44.741 (-0,33%)</span></a></div>
            <div class="ticker-item" data-ticker="fed"><a href="articolo-fed-18mar-tassi-fermi-ppi-inflazione-powell.html">🏛️ <span class="negative">Fed hawkish: PPI +0,7%, solo 1 taglio</span></a></div>
            <div class="ticker-item" data-ticker="micron"><a href="articolo-micron-18mar-earnings-record-hbm4-nvidia.html">🚀 <span class="positive">Micron: EPS $12,20 vs $9,31 atteso</span></a></div>
            <div class="ticker-item" data-ticker="enel"><a href="articolo-ftse-mib-18mar-enel-acea-buzzi-cucinelli.html">📉 <span class="negative">Enel -3,35%, Acea -11,3%</span></a></div>
            <div class="ticker-item" data-ticker="dax"><a href="https://finance.yahoo.com/quote/%5EGDAXI" target="_blank">🇩🇪 DAX <span class="negative">23.515 (-0,91%)</span></a></div>
            <div class="ticker-item" data-ticker="oil"><a href="articolo-geopolitica-18mar-iran-hormuz-petrolio-stagflazione.html">🛢️ WTI <span class="positive">$98,42 (+2,5%)</span></a></div>
            <div class="ticker-item" data-ticker="gold"><a href="https://finance.yahoo.com/quote/GC%3DF" target="_blank">🥇 Oro <span class="negative">$4.880 (-2,8%)</span></a></div>
            <div class="ticker-item" data-ticker="btc"><a href="https://finance.yahoo.com/quote/BTC-USD" target="_blank">₿ <span class="negative">Bitcoin $71.275 (-4,57%)</span></a></div>
            <div class="ticker-item" data-ticker="vix"><a href="https://finance.yahoo.com/quote/%5EVIX" target="_blank">⚠️ <span class="negative">VIX 25,09 (+12,16%)</span></a></div>'''

# Replace ticker content between first ticker-item and </div></div> closing
ticker_pattern = r'(<div class="ticker-content">\n).*?(        </div></div>)'
html = re.sub(ticker_pattern, r'\1' + new_ticker_block + '\n' + r'        \2', html, flags=re.DOTALL)

# --- HEADER DATE ---
html = html.replace('Martedì 17 Marzo 2026', 'Mercoledì 18 Marzo 2026')

# --- STATS BAR ---
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">46.993</div>\n                <div class="text-xs positive">+47 (+0,10%)</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">46.225</div>\n                <div class="text-xs negative">-768 (-1,63%)</div>'
)
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">6.716</div>\n                <div class="text-xs positive">+17 (+0,25%)</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">6.624</div>\n                <div class="text-xs negative">-91 (-1,36%)</div>'
)
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">44.347</div>\n                <div class="text-xs positive">+44 (+0,10%)</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">44.741</div>\n                <div class="text-xs negative">-146 (-0,33%)</div>'
)
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$96,00</div>\n                <div class="text-xs positive">+1,13%</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$98,42</div>\n                <div class="text-xs positive">+2,5%</div>'
)
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$5.020</div>\n                <div class="text-xs positive">+0,28%</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$4.880</div>\n                <div class="text-xs negative">-2,8%</div>'
)
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$73.717</div>\n                <div class="text-xs negative">-0,22%</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$71.275</div>\n                <div class="text-xs negative">-4,57%</div>'
)

# --- HERO ---
old_hero = '''                    <div class="flex items-center gap-3 mb-4">
                        <div class="dot bg-emerald-500 animate-pulse"></div>
                        <span class="text-xs font-bold text-emerald-600 dark:text-emerald-400 uppercase tracking-wider">Breaking · 17 Mar 2026</span>
                    </div>
                    <h1 class="text-3xl md:text-4xl font-black text-gray-900 dark:text-white mb-4 leading-tight montserrat-font">
                        Wall Street sale per la seconda seduta: S&P +0,25%, FOMC domani. Amplifon crolla -14%
                    </h1>
                    <div class="accent-line mb-4"></div>
                    <p class="text-gray-500 dark:text-slate-400 text-lg leading-relaxed mb-6">
                        S&P 500 +0,25% a 6.716, Dow +47 punti a 46.993, Nasdaq +0,47% a 22.479. Mercati in attesa del FOMC di mercoledì (tassi fermi 3,50-3,75%). Nvidia GTC: $1 trilione di ordini. Amplifon -13,57% su acquisizione GN Hearing. Iran colpisce UAE, WTI a $96.
                    </p>
                    <a href="articolo-wall-street-17mar-sp500-nasdaq-fed-hormuz.html" class="inline-flex items-center text-teal-600 dark:text-teal-400 font-semibold text-sm hover:text-teal-700 dark:hover:text-teal-300 transition group">
                        Leggi l\'articolo completo
                        <svg class="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                    </a>
                </div>
                <div class="flex items-center justify-center p-8 bg-gray-50 dark:bg-[#0a0f19]/50 border-l border-gray-100 dark:border-slate-700/20">
                    <div class="text-center">
                        <div class="text-5xl font-black text-gray-900 dark:text-white mb-1">+0,25%</div>
                        <div class="text-sm text-gray-500 dark:text-slate-500 mb-3">S&P 500 — Pre-FOMC</div>
                        <div class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-emerald-50 dark:bg-emerald-500/15 text-emerald-600 dark:text-emerald-400">FOMC domani · Nvidia GTC $1T</div>
                        <div class="mt-4 space-y-1 text-xs text-gray-400 dark:text-slate-600">
                            <div>Dow +47 · Amplifon -14%</div>
                            <div>WTI $96 · BTC $73.717</div>
                        </div>
                    </div>
                </div>'''

new_hero = '''                    <div class="flex items-center gap-3 mb-4">
                        <div class="dot bg-red-500 animate-pulse"></div>
                        <span class="text-xs font-bold text-red-600 dark:text-red-400 uppercase tracking-wider">Breaking · 18 Mar 2026</span>
                    </div>
                    <h1 class="text-3xl md:text-4xl font-black text-gray-900 dark:text-white mb-4 leading-tight montserrat-font">
                        Dow crolla -768 punti: Fed hawkish, PPI doppio delle attese. Micron batte tutto after-hours
                    </h1>
                    <div class="accent-line mb-4"></div>
                    <p class="text-gray-500 dark:text-slate-400 text-lg leading-relaxed mb-6">
                        S&P 500 -1,36% a 6.624, peggior Fed Day dal 2024. Dow -768 a 46.225, Nasdaq -1,46%. PPI +0,7% (doppio delle attese). Fed: tassi fermi 3,50-3,75%, dot plot prevede solo 1 taglio. Powell: "Il Medio Oriente sarà un fattore chiave". Micron after-hours: EPS $12,20 vs $9,31, revenue $23,9B record.
                    </p>
                    <a href="articolo-wall-street-18mar-fed-hawkish-ppi-dow-crolla.html" class="inline-flex items-center text-teal-600 dark:text-teal-400 font-semibold text-sm hover:text-teal-700 dark:hover:text-teal-300 transition group">
                        Leggi l\'articolo completo
                        <svg class="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                    </a>
                </div>
                <div class="flex items-center justify-center p-8 bg-gray-50 dark:bg-[#0a0f19]/50 border-l border-gray-100 dark:border-slate-700/20">
                    <div class="text-center">
                        <div class="text-5xl font-black text-gray-900 dark:text-white mb-1">-1,36%</div>
                        <div class="text-sm text-gray-500 dark:text-slate-500 mb-3">S&P 500 — Fed Hawkish</div>
                        <div class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-red-50 dark:bg-red-500/15 text-red-600 dark:text-red-400">PPI +0,7% · Solo 1 taglio tassi</div>
                        <div class="mt-4 space-y-1 text-xs text-gray-400 dark:text-slate-600">
                            <div>Dow -768 · VIX 25,09</div>
                            <div>WTI $98 · BTC $71.275</div>
                        </div>
                    </div>
                </div>'''
html = html.replace(old_hero, new_hero)

# --- SECTION HEADER + NEW CARDS ---
old_section = '            <h2 class="text-lg font-bold montserrat-font text-gray-900 dark:text-white">Oggi, 17 Marzo</h2>'
new_section = '            <h2 class="text-lg font-bold montserrat-font text-gray-900 dark:text-white">Oggi, 18 Marzo</h2>'
html = html.replace(old_section, new_section)

# Insert new cards BEFORE the 17 marzo cards
new_cards = '''
            <!-- ====== ARTICOLI 18 MARZO 2026 ====== -->

            <!-- Wall Street 18 mar -->
            <a href="articolo-wall-street-18mar-fed-hawkish-ppi-dow-crolla.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-blue-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-blue-50 dark:bg-blue-500/15 text-blue-700 dark:text-blue-400 border border-transparent dark:border-blue-500/20">Wall Street</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Dow crolla -768 punti: Fed hawkish hold, PPI +0,7% doppio delle attese. Peggior Fed Day dal 2024</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">S&P -1,36% a 6.624, Nasdaq -1,46%. VIX +12% a 25. Dot plot: solo 1 taglio tassi nel 2026. Powell: Medio Oriente fattore chiave.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">18 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- FTSE MIB 18 mar -->
            <a href="articolo-ftse-mib-18mar-enel-acea-buzzi-cucinelli.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-emerald-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-green-50 dark:bg-emerald-500/15 text-green-700 dark:text-emerald-400 border border-transparent dark:border-emerald-500/20">Piazza Affari</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">FTSE MIB -0,33%: Acea crolla -11,3%, Enel -3,35%. Cucinelli +4,15%, Buzzi +3%</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Milano a 44.741. Spread BTP-Bund sopra 75 bps. Bancari misti: BPM +2,06%, Intesa +0,81%. Stellantis -2,19%.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">18 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Micron 18 mar -->
            <a href="articolo-micron-18mar-earnings-record-hbm4-nvidia.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-purple-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-purple-50 dark:bg-purple-500/15 text-purple-700 dark:text-purple-400 border border-transparent dark:border-purple-500/20">Tech/AI</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Micron spacca le stime: EPS $12,20 vs $9,31, ricavi +196%. HBM4 per Nvidia Vera Rubin</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Revenue $23,9B record (+75% seq). Margine lordo 75%. Q3 guidance: $33,5B e EPS $19,15. Titolo -3% after-hours: sell the news.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">18 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Fed/PPI 18 mar -->
            <a href="articolo-fed-18mar-tassi-fermi-ppi-inflazione-powell.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-red-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-red-50 dark:bg-red-500/15 text-red-700 dark:text-red-400 border border-transparent dark:border-red-500/20">Macro & Fed</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Fed: tassi fermi, PPI +0,7% doppio delle attese. Dot plot: solo 1 taglio nel 2026</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">FOMC 11-1 per hold a 3,50-3,75%. PPI headline 3,4% YoY, core 3,9%. Powell: il Medio Oriente peserà sull'inflazione. E il peggio deve ancora arrivare.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">18 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Geopolitica/Petrolio 18 mar -->
            <a href="articolo-geopolitica-18mar-iran-hormuz-petrolio-stagflazione.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-amber-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-amber-50 dark:bg-amber-500/15 text-amber-700 dark:text-amber-400 border border-transparent dark:border-amber-500/20">Commodities</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Petrolio a $98: Hormuz, Iran e lo spettro della stagflazione. Oro a $4.880</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">WTI +70% dall'inizio del conflitto. 70% delle petroliere evita Hormuz. Iraq riapre pipeline Ceyhan. PPI non riflette ancora lo shock energetico bellico.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">18 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Day separator 17 Marzo -->
            <div class="col-span-full flex items-center gap-3 mt-6 mb-2">
                <div class="w-10 h-0.5 rounded-full bg-gray-200 dark:bg-slate-700/40"></div>
                <h2 class="text-sm font-bold montserrat-font text-gray-400 dark:text-slate-600 uppercase tracking-wider">17 Marzo 2026</h2>
                <div class="flex-1 h-0.5 rounded-full bg-gray-100 dark:bg-slate-800/20"></div>
            </div>

'''

old_17mar_marker = '            <!-- ====== ARTICOLI 17 MARZO 2026 ====== -->'
html = html.replace(old_17mar_marker, new_cards + '            <!-- ====== ARTICOLI 17 MARZO 2026 ====== -->')

with open('index.html', 'w') as f:
    f.write(html)
print('✅ index.html aggiornato')

# ============================================================
# 2. SITEMAP.XML
# ============================================================
with open('sitemap.xml', 'r') as f:
    sitemap = f.read()

# Update homepage lastmod
sitemap = sitemap.replace('<lastmod>2026-03-17</lastmod>', '<lastmod>2026-03-18</lastmod>')

new_urls = '''
    <!-- 18 Marzo 2026 -->
    <url>
        <loc>https://www.almafinanza.com/articolo-wall-street-18mar-fed-hawkish-ppi-dow-crolla.html</loc>
        <lastmod>2026-03-18</lastmod>
        <changefreq>never</changefreq>
        <priority>0.9</priority>
        <news:news>
            <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
            <news:publication_date>2026-03-18</news:publication_date>
            <news:title>Dow crolla -768 punti: Fed hawkish hold, PPI +0,7% doppio delle attese</news:title>
        </news:news>
    </url>
    <url>
        <loc>https://www.almafinanza.com/articolo-ftse-mib-18mar-enel-acea-buzzi-cucinelli.html</loc>
        <lastmod>2026-03-18</lastmod>
        <changefreq>never</changefreq>
        <priority>0.9</priority>
        <news:news>
            <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
            <news:publication_date>2026-03-18</news:publication_date>
            <news:title>FTSE MIB -0,33%: Acea crolla -11,3%, Enel -3,35%, Cucinelli +4,15%</news:title>
        </news:news>
    </url>
    <url>
        <loc>https://www.almafinanza.com/articolo-micron-18mar-earnings-record-hbm4-nvidia.html</loc>
        <lastmod>2026-03-18</lastmod>
        <changefreq>never</changefreq>
        <priority>0.9</priority>
        <news:news>
            <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
            <news:publication_date>2026-03-18</news:publication_date>
            <news:title>Micron spacca le stime: EPS $12,20 vs $9,31, ricavi record +196% YoY</news:title>
        </news:news>
    </url>
    <url>
        <loc>https://www.almafinanza.com/articolo-fed-18mar-tassi-fermi-ppi-inflazione-powell.html</loc>
        <lastmod>2026-03-18</lastmod>
        <changefreq>never</changefreq>
        <priority>0.9</priority>
        <news:news>
            <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
            <news:publication_date>2026-03-18</news:publication_date>
            <news:title>Fed: tassi fermi, PPI +0,7% doppio delle attese. Dot plot: solo 1 taglio</news:title>
        </news:news>
    </url>
    <url>
        <loc>https://www.almafinanza.com/articolo-geopolitica-18mar-iran-hormuz-petrolio-stagflazione.html</loc>
        <lastmod>2026-03-18</lastmod>
        <changefreq>never</changefreq>
        <priority>0.9</priority>
        <news:news>
            <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
            <news:publication_date>2026-03-18</news:publication_date>
            <news:title>Petrolio a $98: Hormuz, Iran e lo spettro della stagflazione</news:title>
        </news:news>
    </url>
'''

# Insert new URLs after the first <url> block (homepage)
sitemap = sitemap.replace('    <!-- 17 Marzo 2026 -->', new_urls + '    <!-- 17 Marzo 2026 -->')

with open('sitemap.xml', 'w') as f:
    f.write(sitemap)
print('✅ sitemap.xml aggiornato')

# ============================================================
# 3. CATEGORIE
# ============================================================

# --- categoria-wall-street.html ---
with open('categoria-wall-street.html', 'r') as f:
    cat_ws = f.read()

new_ws_section = '''        <section class="mb-12">
            <div class="flex items-center mb-6">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Mercoledì, 18 Marzo 2026</h2>
                <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
            </div>
            <div class="grid md:grid-cols-3 gap-6">

                <a href="articolo-wall-street-18mar-fed-hawkish-ppi-dow-crolla.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#dbeafe;color:#1e40af;">Wall Street</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Dow crolla -768: Fed hawkish, PPI doppio delle attese</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">S&P -1,36% a 6.624, peggior Fed Day dal 2024. VIX +12%. Dot plot: solo 1 taglio tassi.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 18 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

                <a href="articolo-micron-18mar-earnings-record-hbm4-nvidia.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#f3e8ff;color:#7e22ce;">Tech/AI · Earnings</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Micron: EPS $12,20 vs $9,31. Revenue record $23,9B, HBM4 per Nvidia</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Quarto trimestre record consecutivo. Margine lordo 75%. Q3 guidance: $33,5B e EPS $19,15.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 18 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

                <a href="articolo-fed-18mar-tassi-fermi-ppi-inflazione-powell.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#fee2e2;color:#991b1b;">Macro & Fed</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Fed: tassi fermi, PPI +0,7%. Powell: Medio Oriente fattore chiave</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">FOMC 11-1 per hold. PPI headline 3,4% YoY, core 3,9%. Dot plot: solo 1 taglio. Il peggio deve ancora arrivare.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 18 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

                <a href="articolo-geopolitica-18mar-iran-hormuz-petrolio-stagflazione.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#fef3c7;color:#92400e;">Geopolitica · Commodities</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Petrolio a $98: Hormuz, Iran e lo spettro della stagflazione</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">WTI +70% dall'inizio del conflitto. 70% petroliere evita Hormuz. Iraq riapre Ceyhan. Oro a $4.880.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 18 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

            </div>
        </section>

'''

# Find first <section class="mb-12"> and insert before it
first_section = cat_ws.find('<section class="mb-12">')
if first_section != -1:
    # Find the indentation
    line_start = cat_ws.rfind('\n', 0, first_section) + 1
    indent = cat_ws[line_start:first_section]
    cat_ws = cat_ws[:first_section] + new_ws_section + cat_ws[first_section:]

with open('categoria-wall-street.html', 'w') as f:
    f.write(cat_ws)
print('✅ categoria-wall-street.html aggiornato')

# --- categoria-borsa-milano.html ---
with open('categoria-borsa-milano.html', 'r') as f:
    cat_mi = f.read()

new_mi_section = '''        <section class="mb-12">
            <div class="flex items-center mb-6">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Mercoledì, 18 Marzo 2026</h2>
                <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
            </div>
            <div class="grid md:grid-cols-3 gap-6">

                <a href="articolo-ftse-mib-18mar-enel-acea-buzzi-cucinelli.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#d1fae5;color:#065f46;">Piazza Affari</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">FTSE MIB -0,33%: Acea -11,3%, Enel -3,35%, Cucinelli +4,15%</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Milano a 44.741. Spread sopra 75 bps. Buzzi +3,03% su Morgan Stanley. Bancari misti. Attesa Fed e BCE.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 18 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

            </div>
        </section>

'''

first_section = cat_mi.find('<section class="mb-12">')
if first_section != -1:
    cat_mi = cat_mi[:first_section] + new_mi_section + cat_mi[first_section:]

with open('categoria-borsa-milano.html', 'w') as f:
    f.write(cat_mi)
print('✅ categoria-borsa-milano.html aggiornato')

# --- categoria-commodities.html ---
with open('categoria-commodities.html', 'r') as f:
    cat_comm = f.read()

new_comm_section = '''        <section class="mb-12">
            <div class="flex items-center mb-6">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Mercoledì, 18 Marzo 2026</h2>
                <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
            </div>
            <div class="grid md:grid-cols-3 gap-6">

                <a href="articolo-geopolitica-18mar-iran-hormuz-petrolio-stagflazione.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#fef3c7;color:#92400e;">Petrolio · Geopolitica</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">WTI a $98: Hormuz, Iran e stagflazione. Oro $4.880</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Petrolio +70% dal conflitto. 70% petroliere evita lo stretto. Iraq riapre Ceyhan. PPI non include ancora lo shock bellico.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 18 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

            </div>
        </section>

'''

first_section = cat_comm.find('<section class="mb-12">')
if first_section != -1:
    cat_comm = cat_comm[:first_section] + new_comm_section + cat_comm[first_section:]

with open('categoria-commodities.html', 'w') as f:
    f.write(cat_comm)
print('✅ categoria-commodities.html aggiornato')

# ============================================================
# 4. IMPARA LA FINANZA
# ============================================================
with open('impara-finanza.html', 'r') as f:
    impara = f.read()

# Concept cards to add (from info-boxes in the 5 articles)
# 1. Hawkish Hold → Macroeconomia e Banche Centrali
# 2. PPI vs CPI → Macroeconomia e Banche Centrali
# 3. HBM (High Bandwidth Memory) → Metriche Settoriali
# 4. Sell the News → Meccanismi di Mercato
# 5. Dot Plot della Fed → Macroeconomia e Banche Centrali
# 6. Stretto di Hormuz → Geopolitica e Mercati
# 7. Stagflazione → Macroeconomia e Banche Centrali
# 8. Utilities e tassi di interesse → Meccanismi di Mercato
# 9. Spread BTP-Bund → Settore Finanziario & Bancario
# 10. Margine lordo e operativo → Valutazioni e Multipli

# Add to Macroeconomia e Banche Centrali section
macro_cards = '''
                <a href="articolo-fed-18mar-tassi-fermi-ppi-inflazione-powell.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-cyan-500 hover:border-cyan-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Hawkish Hold</h3>
                    <p class="text-sm text-gray-600 dark:text-slate-400">Quando una banca centrale mantiene i tassi invariati ma con un tono da falco, segnalando che non intende tagliarli a breve. Spesso causa vendite sui mercati.</p>
                    <span class="text-xs text-cyan-600 dark:text-cyan-400 font-semibold mt-2 inline-block">→ Spiegato in: Fed 18 marzo — tassi fermi e PPI</span>
                </a>
                <a href="articolo-fed-18mar-tassi-fermi-ppi-inflazione-powell.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-cyan-500 hover:border-cyan-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">PPI vs CPI</h3>
                    <p class="text-sm text-gray-600 dark:text-slate-400">Il PPI misura i prezzi alla produzione (input dei produttori), il CPI i prezzi al consumo. Un PPI alto anticipa spesso un rialzo del CPI nei mesi successivi.</p>
                    <span class="text-xs text-cyan-600 dark:text-cyan-400 font-semibold mt-2 inline-block">→ Spiegato in: Fed 18 marzo — PPI +0,7%</span>
                </a>
                <a href="articolo-fed-18mar-tassi-fermi-ppi-inflazione-powell.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-cyan-500 hover:border-cyan-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Dot Plot della Fed</h3>
                    <p class="text-sm text-gray-600 dark:text-slate-400">Grafico che mostra le previsioni individuali dei membri del FOMC sui tassi futuri. Ogni punto rappresenta un membro. È uno degli strumenti più seguiti per capire la direzione della politica monetaria.</p>
                    <span class="text-xs text-cyan-600 dark:text-cyan-400 font-semibold mt-2 inline-block">→ Spiegato in: Fed 18 marzo — dot plot solo 1 taglio</span>
                </a>
                <a href="articolo-geopolitica-18mar-iran-hormuz-petrolio-stagflazione.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-cyan-500 hover:border-cyan-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Stagflazione</h3>
                    <p class="text-sm text-gray-600 dark:text-slate-400">Scenario in cui l'economia rallenta (stagnazione) mentre i prezzi aumentano (inflazione). È il peggior incubo per le banche centrali perché i loro strumenti funzionano contro uno dei due problemi, ma aggravano l'altro.</p>
                    <span class="text-xs text-cyan-600 dark:text-cyan-400 font-semibold mt-2 inline-block">→ Spiegato in: Iran, Hormuz e stagflazione</span>
                </a>'''

# Find "Macroeconomia e Banche Centrali" section and add before its closing </div>
macro_marker = '🌍 Macroeconomia e Banche Centrali'
macro_pos = impara.find(macro_marker)
if macro_pos != -1:
    # Find the grid div and its last </div> before next section
    grid_after = impara.find('<div class="grid', macro_pos)
    if grid_after != -1:
        # Find the closing </div> of this grid - look for </section>
        section_end = impara.find('</section>', grid_after)
        grid_end = impara.rfind('</div>', grid_after, section_end)
        if grid_end != -1:
            impara = impara[:grid_end] + macro_cards + '\n            ' + impara[grid_end:]

# Add to Meccanismi di Mercato
mech_cards = '''
                <a href="articolo-micron-18mar-earnings-record-hbm4-nvidia.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-purple-500 hover:border-purple-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Sell the News</h3>
                    <p class="text-sm text-gray-600 dark:text-slate-400">Fenomeno per cui un titolo scende dopo la pubblicazione di risultati eccellenti, perché le buone notizie erano già "prezzate" dal mercato. Micron -3% dopo EPS del 31% sopra le attese è un caso da manuale.</p>
                    <span class="text-xs text-purple-600 dark:text-purple-400 font-semibold mt-2 inline-block">→ Spiegato in: Micron earnings record</span>
                </a>
                <a href="articolo-ftse-mib-18mar-enel-acea-buzzi-cucinelli.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-purple-500 hover:border-purple-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Utilities e tassi di interesse</h3>
                    <p class="text-sm text-gray-600 dark:text-slate-400">Le utilities (Enel, Acea) sono sensibili ai tassi perché hanno molto debito e pagano alti dividendi. Quando i tassi salgono (o restano alti), le utilities soffrono perché i bond diventano più attraenti.</p>
                    <span class="text-xs text-purple-600 dark:text-purple-400 font-semibold mt-2 inline-block">→ Spiegato in: FTSE MIB 18 marzo</span>
                </a>'''

mech_marker = '⚙️ Meccanismi di Mercato'
mech_pos = impara.find(mech_marker)
if mech_pos != -1:
    grid_after = impara.find('<div class="grid', mech_pos)
    if grid_after != -1:
        section_end = impara.find('</section>', grid_after)
        grid_end = impara.rfind('</div>', grid_after, section_end)
        if grid_end != -1:
            impara = impara[:grid_end] + mech_cards + '\n            ' + impara[grid_end:]

# Add to Metriche Settoriali
metric_cards = '''
                <a href="articolo-micron-18mar-earnings-record-hbm4-nvidia.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-amber-500 hover:border-amber-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">HBM (High Bandwidth Memory)</h3>
                    <p class="text-sm text-gray-600 dark:text-slate-400">Memoria ad alta larghezza di banda usata nelle GPU AI. Le generazioni HBM3e, HBM4 e HBM4e sono fondamentali per addestrare e inferire modelli di intelligenza artificiale. Micron è tra i principali produttori mondiali.</p>
                    <span class="text-xs text-amber-600 dark:text-amber-400 font-semibold mt-2 inline-block">→ Spiegato in: Micron earnings HBM4</span>
                </a>'''

metric_marker = '📈 Metriche Settoriali'
metric_pos = impara.find(metric_marker)
if metric_pos != -1:
    grid_after = impara.find('<div class="grid', metric_pos)
    if grid_after != -1:
        section_end = impara.find('</section>', grid_after)
        grid_end = impara.rfind('</div>', grid_after, section_end)
        if grid_end != -1:
            impara = impara[:grid_end] + metric_cards + '\n            ' + impara[grid_end:]

# Add to Geopolitica e Mercati
geo_cards = '''
                <a href="articolo-geopolitica-18mar-iran-hormuz-petrolio-stagflazione.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-rose-500 hover:border-rose-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Stretto di Hormuz</h3>
                    <p class="text-sm text-gray-600 dark:text-slate-400">Passaggio marittimo tra Iran e Oman attraverso cui transita oltre il 20% del petrolio mondiale. Il suo blocco (anche parziale) può causare shock energetici globali e impennate dell'inflazione.</p>
                    <span class="text-xs text-rose-600 dark:text-rose-400 font-semibold mt-2 inline-block">→ Spiegato in: Iran, Hormuz e stagflazione</span>
                </a>'''

geo_marker = '🌍 Geopolitica e Mercati'
geo_pos = impara.find(geo_marker)
if geo_pos != -1:
    grid_after = impara.find('<div class="grid', geo_pos)
    if grid_after != -1:
        section_end = impara.find('</section>', grid_after)
        grid_end = impara.rfind('</div>', grid_after, section_end)
        if grid_end != -1:
            impara = impara[:grid_end] + geo_cards + '\n            ' + impara[grid_end:]

# Add to Valutazioni e Multipli
val_cards = '''
                <a href="articolo-micron-18mar-earnings-record-hbm4-nvidia.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-blue-500 hover:border-blue-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Margine lordo e operativo</h3>
                    <p class="text-sm text-gray-600 dark:text-slate-400">Il margine lordo (gross margin) è il ricavo meno il costo dei beni venduti, diviso il ricavo. Il margine operativo sottrae anche le spese operative. Micron al 75% lordo e 69% operativo indica un'azienda con pricing power eccezionale.</p>
                    <span class="text-xs text-blue-600 dark:text-blue-400 font-semibold mt-2 inline-block">→ Spiegato in: Micron earnings record</span>
                </a>'''

val_marker = '📊 Valutazioni e Multipli'
val_pos = impara.find(val_marker)
if val_pos != -1:
    grid_after = impara.find('<div class="grid', val_pos)
    if grid_after != -1:
        section_end = impara.find('</section>', grid_after)
        grid_end = impara.rfind('</div>', grid_after, section_end)
        if grid_end != -1:
            impara = impara[:grid_end] + val_cards + '\n            ' + impara[grid_end:]

# Add to Settore Finanziario & Bancario
fin_cards = '''
                <a href="articolo-ftse-mib-18mar-enel-acea-buzzi-cucinelli.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-emerald-500 hover:border-emerald-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Spread BTP-Bund</h3>
                    <p class="text-sm text-gray-600 dark:text-slate-400">Differenza di rendimento tra il BTP italiano decennale e il Bund tedesco. Misura il rischio-paese percepito: più è alto, più il mercato considera l'Italia rischiosa rispetto alla Germania.</p>
                    <span class="text-xs text-emerald-600 dark:text-emerald-400 font-semibold mt-2 inline-block">→ Spiegato in: FTSE MIB 18 marzo</span>
                </a>'''

fin_marker = '🏦 Settore Finanziario & Bancario'
fin_pos = impara.find(fin_marker)
if fin_pos != -1:
    grid_after = impara.find('<div class="grid', fin_pos)
    if grid_after != -1:
        section_end = impara.find('</section>', grid_after)
        grid_end = impara.rfind('</div>', grid_after, section_end)
        if grid_end != -1:
            impara = impara[:grid_end] + fin_cards + '\n            ' + impara[grid_end:]

with open('impara-finanza.html', 'w') as f:
    f.write(impara)
print('✅ impara-finanza.html aggiornato')

print('\n🎉 AGGIORNAMENTO 18 MARZO 2026 COMPLETATO!')
print('File aggiornati: index.html, sitemap.xml, categoria-wall-street.html, categoria-borsa-milano.html, categoria-commodities.html, impara-finanza.html')
