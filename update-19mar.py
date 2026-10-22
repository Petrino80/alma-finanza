#!/usr/bin/env python3
"""Aggiornamento 19 Marzo 2026 — Alma Finanza
Updates: index.html (ticker, date, stats, hero, cards), sitemap.xml,
         categoria-wall-street.html, categoria-borsa-milano.html,
         categoria-commodities.html, impara-finanza.html
"""
import re

# ============================================================
# 1. INDEX.HTML — Ticker
# ============================================================
with open('index.html', 'r') as f:
    html = f.read()

# --- Ticker ---
old_ticker_start = '<div class="ticker-content">'
old_ticker_end = '<!-- Duplicate for seamless loop -->'

new_ticker_items = '''<div class="ticker-content">
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EDJI" target="_blank">🇺🇸 Dow <span class="negative">46.021 (-0,44%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EGSPC" target="_blank">🇺🇸 S&P 500 <span class="negative">6.606 (-0,27%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EIXIC" target="_blank">🇺🇸 Nasdaq <span class="negative">22.090 (-0,28%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/FTSEMIB.MI" target="_blank">🇮🇹 FTSE MIB <span class="negative">43.701 (-2,32%)</span></a></div>
            <div class="ticker-item"><a href="articolo-ftse-mib-19mar-inwit-crollo-eni-bce-tassi.html">📉 <span class="negative">Inwit -15,6%: TIM-Fastweb torri</span></a></div>
            <div class="ticker-item"><a href="articolo-micron-19mar-earnings-record-sell-news-hbm4.html">🔴 <span class="negative">Micron -7% dopo earnings record</span></a></div>
            <div class="ticker-item"><a href="articolo-bce-19mar-tassi-fermi-inflazione-rialzo-lagarde.html">🏛️ <span class="negative">BCE: tassi fermi, inflazione 2,6%</span></a></div>
            <div class="ticker-item"><a href="articolo-lng-19mar-iran-qatar-ras-laffan-europa-italia.html">🔥 <span class="negative">Qatar LNG -17%: Iran colpisce Ras Laffan</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EGDAXI" target="_blank">🇩🇪 DAX <span class="negative">23.447 (-0,60%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/GC%3DF" target="_blank">🥇 Oro <span class="negative">$4.551 (-5,44%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/BTC-USD" target="_blank">₿ <span class="negative">Bitcoin $69.370 (-2,67%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EVIX" target="_blank">⚠️ <span class="negative">VIX 24,92 (+13%)</span></a></div>
            <!-- Duplicate for seamless loop -->
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EDJI" target="_blank">🇺🇸 Dow <span class="negative">46.021 (-0,44%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EGSPC" target="_blank">🇺🇸 S&P 500 <span class="negative">6.606 (-0,27%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EIXIC" target="_blank">🇺🇸 Nasdaq <span class="negative">22.090 (-0,28%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/FTSEMIB.MI" target="_blank">🇮🇹 FTSE MIB <span class="negative">43.701 (-2,32%)</span></a></div>
            <div class="ticker-item"><a href="articolo-ftse-mib-19mar-inwit-crollo-eni-bce-tassi.html">📉 <span class="negative">Inwit -15,6%: TIM-Fastweb torri</span></a></div>
            <div class="ticker-item"><a href="articolo-micron-19mar-earnings-record-sell-news-hbm4.html">🔴 <span class="negative">Micron -7% dopo earnings record</span></a></div>
            <div class="ticker-item"><a href="articolo-bce-19mar-tassi-fermi-inflazione-rialzo-lagarde.html">🏛️ <span class="negative">BCE: tassi fermi, inflazione 2,6%</span></a></div>
            <div class="ticker-item"><a href="articolo-lng-19mar-iran-qatar-ras-laffan-europa-italia.html">🔥 <span class="negative">Qatar LNG -17%: Iran colpisce Ras Laffan</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EGDAXI" target="_blank">🇩🇪 DAX <span class="negative">23.447 (-0,60%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/GC%3DF" target="_blank">🥇 Oro <span class="negative">$4.551 (-5,44%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/BTC-USD" target="_blank">₿ <span class="negative">Bitcoin $69.370 (-2,67%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EVIX" target="_blank">⚠️ <span class="negative">VIX 24,92 (+13%)</span></a></div>
                </div></div>'''

# Replace entire ticker-content div
ticker_pattern = r'<div class="ticker-content">.*?</div></div>\s*</div>'
html = re.sub(ticker_pattern, new_ticker_items + '\n    </div>', html, flags=re.DOTALL)

# --- Date ---
html = html.replace('Mercoledì 18 Marzo 2026', 'Giovedì 19 Marzo 2026')

# --- Stats Bar ---
html = html.replace('>46.225</div>\n                <div class="text-xs negative">-768 (-1,63%)</div>', '>46.021</div>\n                <div class="text-xs negative">-204 (-0,44%)</div>')
html = html.replace('>6.624</div>\n                <div class="text-xs negative">-91 (-1,36%)</div>', '>6.606</div>\n                <div class="text-xs negative">-18 (-0,27%)</div>')
html = html.replace('>44.741</div>\n                <div class="text-xs negative">-146 (-0,33%)</div>', '>43.701</div>\n                <div class="text-xs negative">-1.040 (-2,32%)</div>')
html = html.replace('>$98,42</div>\n                <div class="text-xs positive">+2,5%</div>', '>$96,14</div>\n                <div class="text-xs negative">-0,19%</div>')
html = html.replace('>$4.880</div>\n                <div class="text-xs negative">-2,8%</div>', '>$4.551</div>\n                <div class="text-xs negative">-5,44%</div>')
html = html.replace('>$71.275</div>\n                <div class="text-xs negative">-4,57%</div>', '>$69.370</div>\n                <div class="text-xs negative">-2,67%</div>')

# --- Hero ---
old_hero = '''                    <div class="flex items-center gap-3 mb-4">
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
                        Leggi l'articolo completo
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

new_hero = '''                    <div class="flex items-center gap-3 mb-4">
                        <div class="dot bg-red-500 animate-pulse"></div>
                        <span class="text-xs font-bold text-red-600 dark:text-red-400 uppercase tracking-wider">Breaking · 19 Mar 2026</span>
                    </div>
                    <h1 class="text-3xl md:text-4xl font-black text-gray-900 dark:text-white mb-4 leading-tight montserrat-font">
                        Iran colpisce Ras Laffan: 17% del GNL mondiale fuori gioco. FTSE MIB -2,3%, BCE ferma, oro crolla -5%
                    </h1>
                    <div class="accent-line mb-4"></div>
                    <p class="text-gray-500 dark:text-slate-400 text-lg leading-relaxed mb-6">
                        Missili iraniani devastano Ras Laffan in Qatar: 12,8 milioni di tonnellate di LNG fuori uso per 3-5 anni. Italia perde il 44% delle forniture GNL. Gas TTF +23% a €67,5/MWh. FTSE MIB -2,32%, Inwit crolla -15,6%. BCE lascia tassi al 2%. Dow -204 a 46.021, S&P -0,27%. Oro -5,44% a $4.551. Micron -7% nonostante EPS record.
                    </p>
                    <a href="articolo-lng-19mar-iran-qatar-ras-laffan-europa-italia.html" class="inline-flex items-center text-teal-600 dark:text-teal-400 font-semibold text-sm hover:text-teal-700 dark:hover:text-teal-300 transition group">
                        Leggi l'articolo completo
                        <svg class="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                    </a>
                </div>
                <div class="flex items-center justify-center p-8 bg-gray-50 dark:bg-[#0a0f19]/50 border-l border-gray-100 dark:border-slate-700/20">
                    <div class="text-center">
                        <div class="text-5xl font-black text-gray-900 dark:text-white mb-1">-17%</div>
                        <div class="text-sm text-gray-500 dark:text-slate-500 mb-3">LNG Qatar — Iran colpisce Ras Laffan</div>
                        <div class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-red-50 dark:bg-red-500/15 text-red-600 dark:text-red-400">Gas TTF +23% · Force Majeure Italia</div>
                        <div class="mt-4 space-y-1 text-xs text-gray-400 dark:text-slate-600">
                            <div>FTSE MIB -2,32% · Inwit -15,6%</div>
                            <div>Oro -5,44% · BTC $69.370</div>
                        </div>
                    </div>
                </div>'''

html = html.replace(old_hero, new_hero)

# --- Section header ---
html = html.replace('>Oggi, 18 Marzo</h2>', '>Oggi, 19 Marzo</h2>')

# --- New cards + day separator ---
new_cards = '''
            <!-- ====== ARTICOLI 19 MARZO 2026 ====== -->

            <!-- Wall Street 19 mar -->
            <a href="articolo-wall-street-19mar-dow-sp500-petrolio-119-micron.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-blue-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-blue-50 dark:bg-blue-500/15 text-blue-700 dark:text-blue-400 border border-transparent dark:border-blue-500/20">Wall Street</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Dow -204, petrolio sfiora $119 poi rientra: Netanyahu promette riapertura Hormuz</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">S&P -0,27% a 6.606, Nasdaq -0,28%. Dow era -500 poi recupera. Micron -7% su CapEx $25B. Russell 2000 unico in verde +0,65%. VIX 24,92.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">19 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- FTSE MIB 19 mar -->
            <a href="articolo-ftse-mib-19mar-inwit-crollo-eni-bce-tassi.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-emerald-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-green-50 dark:bg-emerald-500/15 text-green-700 dark:text-emerald-400 border border-transparent dark:border-emerald-500/20">Piazza Affari</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">FTSE MIB crolla -2,32%: Inwit -15,6% su TIM-Fastweb torri, Eni unica positiva</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Milano a 43.701. BCE ferma tassi al 2%. Prysmian -5,39%, STM -4,52%. Volumi €4,82 miliardi. Gas TTF +23%.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">19 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- BCE 19 mar -->
            <a href="articolo-bce-19mar-tassi-fermi-inflazione-rialzo-lagarde.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-red-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-red-50 dark:bg-red-500/15 text-red-700 dark:text-red-400 border border-transparent dark:border-red-500/20">Macro & BCE</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">BCE ferma i tassi al 2%: inflazione rivista al 2,6%, la guerra cambia tutto</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Sesta pausa consecutiva. Crescita 2026 tagliata a 0,9%. Morgan Stanley: niente tagli nel 2026. Mercati prezzano 2-3 rialzi.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">19 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Micron 19 mar -->
            <a href="articolo-micron-19mar-earnings-record-sell-news-hbm4.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-purple-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-purple-50 dark:bg-purple-500/15 text-purple-700 dark:text-purple-400 border border-transparent dark:border-purple-500/20">Tech/AI</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Micron, earnings record ma il titolo crolla -7%: CapEx $25B spaventa, HBM4 per Nvidia</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">EPS $12,20 vs $8,79 atteso (+40%). Revenue $23,9B (+196% YoY). Q3 guidance $33,5B. Nvidia e Broadcom -2%. Il paradosso del sell the news.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">19 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- LNG/Iran 19 mar -->
            <a href="articolo-lng-19mar-iran-qatar-ras-laffan-europa-italia.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-red-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-red-50 dark:bg-red-500/15 text-red-700 dark:text-red-400 border border-transparent dark:border-red-500/20">Geopolitica</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Iran colpisce Ras Laffan: 17% del GNL mondiale fuori gioco per 5 anni. Italia perde fornitore n.1</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">12,8 mln tonnellate/anno di LNG sidelined. Force majeure su contratti Italia. TTF +23% a €67,5. Petrolio sfiora $119. US LNG grande vincitore.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">19 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Day separator 18 Marzo -->
            <div class="col-span-full flex items-center gap-3 mt-6 mb-2">
                <div class="w-10 h-0.5 rounded-full bg-gray-200 dark:bg-slate-700/40"></div>
                <h2 class="text-sm font-bold montserrat-font text-gray-400 dark:text-slate-600 uppercase tracking-wider">18 Marzo 2026</h2>
                <div class="flex-1 h-0.5 rounded-full bg-gray-100 dark:bg-slate-800/20"></div>
            </div>
'''

# Insert new cards before the 18 March articles
html = html.replace('            <!-- ====== ARTICOLI 18 MARZO 2026 ======', new_cards + '\n            <!-- ====== ARTICOLI 18 MARZO 2026 ======')

with open('index.html', 'w') as f:
    f.write(html)
print("✅ index.html aggiornato")


# ============================================================
# 2. SITEMAP.XML
# ============================================================
with open('sitemap.xml', 'r') as f:
    sitemap = f.read()

# Update homepage lastmod
sitemap = sitemap.replace('<lastmod>2026-03-18</lastmod>', '<lastmod>2026-03-19</lastmod>', 1)

new_urls = '''
  <!-- Articoli 19 Marzo 2026 -->
  <url>
      <loc>https://www.almafinanza.com/articolo-wall-street-19mar-dow-sp500-petrolio-119-micron.html</loc>
      <lastmod>2026-03-19</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-19</news:publication_date>
          <news:title>Wall Street 19 marzo: Dow -204, petrolio sfiora $119 poi rientra su Netanyahu-Hormuz</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-ftse-mib-19mar-inwit-crollo-eni-bce-tassi.html</loc>
      <lastmod>2026-03-19</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-19</news:publication_date>
          <news:title>FTSE MIB -2,32%: Inwit crolla -15,6%, Eni unica positiva. BCE ferma tassi, gas +23%</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-bce-19mar-tassi-fermi-inflazione-rialzo-lagarde.html</loc>
      <lastmod>2026-03-19</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-19</news:publication_date>
          <news:title>BCE ferma i tassi al 2%: inflazione rivista al 2,6%, la guerra cambia tutto</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-micron-19mar-earnings-record-sell-news-hbm4.html</loc>
      <lastmod>2026-03-19</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-19</news:publication_date>
          <news:title>Micron, earnings record ma -7%: CapEx $25B e paradosso sell the news. HBM4 per Nvidia</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-lng-19mar-iran-qatar-ras-laffan-europa-italia.html</loc>
      <lastmod>2026-03-19</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-19</news:publication_date>
          <news:title>Iran colpisce Ras Laffan: 17% del GNL mondiale fuori gioco per 5 anni. Italia perde fornitore n.1</news:title>
      </news:news>
  </url>

'''

# Insert before the 17 March articles
sitemap = sitemap.replace('  <!-- Articoli 17 Marzo 2026 -->', new_urls + '  <!-- Articoli 17 Marzo 2026 -->')

with open('sitemap.xml', 'w') as f:
    f.write(sitemap)
print("✅ sitemap.xml aggiornato")


# ============================================================
# 3. CATEGORIA-WALL-STREET.HTML (Wall Street, BCE, Micron, LNG)
# ============================================================
with open('categoria-wall-street.html', 'r') as f:
    cat_ws = f.read()

new_ws_section = '''
                <section class="mb-12">
            <div class="flex items-center mb-6">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Giovedì, 19 Marzo 2026</h2>
                <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
            </div>
            <div class="grid md:grid-cols-3 gap-6">

                <a href="articolo-wall-street-19mar-dow-sp500-petrolio-119-micron.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#dbeafe;color:#1e40af;">Wall Street</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Dow -204, petrolio sfiora $119 poi rientra su Netanyahu-Hormuz</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">S&P -0,27% a 6.606, Nasdaq -0,28%. Micron -7% su CapEx $25B. Russell 2000 unico in verde +0,65%. VIX 24,92.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 19 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

                <a href="articolo-bce-19mar-tassi-fermi-inflazione-rialzo-lagarde.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#fee2e2;color:#991b1b;">Macro & BCE</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">BCE ferma i tassi al 2%: inflazione rivista al 2,6%, guerra cambia tutto</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Sesta pausa consecutiva. Crescita 2026 tagliata a 0,9%. Morgan Stanley: niente tagli nel 2026. Mercati prezzano rialzi.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 19 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

                <a href="articolo-micron-19mar-earnings-record-sell-news-hbm4.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#f3e8ff;color:#6b21a8;">Tech & AI</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Micron, earnings record ma -7%: CapEx $25B e paradosso sell the news</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">EPS $12,20 vs $8,79 (+40%). Revenue $23,9B (+196% YoY). HBM4 per Nvidia Vera Rubin. Nvidia e Broadcom -2%.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 19 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

                <a href="articolo-lng-19mar-iran-qatar-ras-laffan-europa-italia.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#fee2e2;color:#991b1b;">Geopolitica</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Iran colpisce Ras Laffan: 17% del GNL mondiale fuori gioco per 5 anni</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">12,8 mln ton/anno sidelined. Force majeure su contratti Italia. TTF +23% a €67,5. US LNG grande vincitore.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 19 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

            </div>
        </section>

'''

# Insert before the 18 March section
cat_ws = cat_ws.replace('                <section class="mb-12">\n            <div class="flex items-center mb-6">\n                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Mercoledì, 18 Marzo 2026</h2>', new_ws_section + '                <section class="mb-12">\n            <div class="flex items-center mb-6">\n                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Mercoledì, 18 Marzo 2026</h2>')

with open('categoria-wall-street.html', 'w') as f:
    f.write(cat_ws)
print("✅ categoria-wall-street.html aggiornato")


# ============================================================
# 4. CATEGORIA-BORSA-MILANO.HTML (FTSE MIB)
# ============================================================
with open('categoria-borsa-milano.html', 'r') as f:
    cat_mi = f.read()

new_mi_section = '''
                <section class="mb-12">
            <div class="flex items-center mb-6">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Giovedì, 19 Marzo 2026</h2>
                <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
            </div>
            <div class="grid md:grid-cols-3 gap-6">

                <a href="articolo-ftse-mib-19mar-inwit-crollo-eni-bce-tassi.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#d1fae5;color:#065f46;">FTSE MIB</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">FTSE MIB crolla -2,32%: Inwit -15,6%, Eni unica positiva. BCE ferma tassi</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Milano a 43.701. Prysmian -5,39%, STM -4,52%. BCE lascia tassi al 2%. Gas TTF +23% a €67,5.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 19 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

            </div>
        </section>

'''

# Find the first section in borsa-milano
first_mi_marker = cat_mi.find('<section class="mb-12">')
if first_mi_marker > 0:
    cat_mi = cat_mi[:first_mi_marker] + new_mi_section + cat_mi[first_mi_marker:]

with open('categoria-borsa-milano.html', 'w') as f:
    f.write(cat_mi)
print("✅ categoria-borsa-milano.html aggiornato")


# ============================================================
# 5. CATEGORIA-COMMODITIES.HTML (LNG article)
# ============================================================
with open('categoria-commodities.html', 'r') as f:
    cat_comm = f.read()

new_comm_section = '''
                <section class="mb-12">
            <div class="flex items-center mb-6">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Giovedì, 19 Marzo 2026</h2>
                <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
            </div>
            <div class="grid md:grid-cols-3 gap-6">

                <a href="articolo-lng-19mar-iran-qatar-ras-laffan-europa-italia.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#fef3c7;color:#92400e;">Gas & LNG</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Iran colpisce Ras Laffan: 17% del GNL mondiale fuori gioco. TTF +23%</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">12,8 mln ton/anno sidelined per 3-5 anni. Force majeure su Italia. Brent sfiora $119 poi rientra. US LNG vincitore.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 19 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

            </div>
        </section>

'''

first_comm_marker = cat_comm.find('<section class="mb-12">')
if first_comm_marker > 0:
    cat_comm = cat_comm[:first_comm_marker] + new_comm_section + cat_comm[first_comm_marker:]

with open('categoria-commodities.html', 'w') as f:
    f.write(cat_comm)
print("✅ categoria-commodities.html aggiornato")


# ============================================================
# 6. IMPARA-FINANZA.HTML — New concept cards
# ============================================================
with open('impara-finanza.html', 'r') as f:
    impara = f.read()

# Info-boxes from articles → concept-cards
# Article 1 (Wall Street): VIX, Sell the News
# Article 2 (FTSE MIB): Clausola All or Nothing, Tasso sui depositi BCE
# Article 3 (BCE): Stagflazione, Forward Guidance
# Article 4 (Micron): HBM, Paradosso CapEx
# Article 5 (LNG): Force Majeure, GNL catena valore

concepts = {
    'Gestione del Rischio': [
        '''
                <a href="articolo-wall-street-19mar-dow-sp500-petrolio-119-micron.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-red-500 hover:border-red-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">VIX — L'indice della paura</h3>
                    <p class="text-sm text-gray-600">Il VIX misura la volatilità attesa dal mercato nei prossimi 30 giorni. Sopra 20 indica nervosismo elevato, sopra 30 panico.</p>
                    <span class="text-xs text-red-600 font-semibold mt-2 inline-block">→ Spiegato in: Wall Street 19 marzo</span>
                </a>''',
    ],
    'Meccanismi di Mercato': [
        '''
                <a href="articolo-wall-street-19mar-dow-sp500-petrolio-119-micron.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-purple-500 hover:border-purple-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Sell the News</h3>
                    <p class="text-sm text-gray-600">Quando un evento atteso (earnings, lancio prodotto) si materializza, gli investitori vendono per prendere profitto. Il prezzo scende nonostante la notizia positiva.</p>
                    <span class="text-xs text-purple-600 font-semibold mt-2 inline-block">→ Spiegato in: Wall Street 19 marzo</span>
                </a>''',
        '''
                <a href="articolo-ftse-mib-19mar-inwit-crollo-eni-bce-tassi.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-purple-500 hover:border-purple-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Clausola All or Nothing</h3>
                    <p class="text-sm text-gray-600">Nei contratti infrastrutturali (torri, fibra), impone che un cliente non possa recedere su singoli siti: deve rinunciare all'intero pacchetto o mantenere tutto.</p>
                    <span class="text-xs text-purple-600 font-semibold mt-2 inline-block">→ Spiegato in: FTSE MIB 19 marzo</span>
                </a>''',
    ],
    'Macroeconomia e Banche Centrali': [
        '''
                <a href="articolo-bce-19mar-tassi-fermi-inflazione-rialzo-lagarde.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-cyan-500 hover:border-cyan-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Stagflazione</h3>
                    <p class="text-sm text-gray-600">Quando inflazione alta e crescita stagnante coesistono. Le banche centrali sono in trappola: alzare i tassi frena la crescita, abbassarli alimenta l'inflazione.</p>
                    <span class="text-xs text-cyan-600 font-semibold mt-2 inline-block">→ Spiegato in: BCE 19 marzo</span>
                </a>''',
        '''
                <a href="articolo-bce-19mar-tassi-fermi-inflazione-rialzo-lagarde.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-cyan-500 hover:border-cyan-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Forward Guidance della BCE</h3>
                    <p class="text-sm text-gray-600">La comunicazione delle banche centrali sulle future decisioni di politica monetaria. Influenza i mercati prima ancora che i tassi cambino realmente.</p>
                    <span class="text-xs text-cyan-600 font-semibold mt-2 inline-block">→ Spiegato in: BCE 19 marzo</span>
                </a>''',
        '''
                <a href="articolo-ftse-mib-19mar-inwit-crollo-eni-bce-tassi.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-cyan-500 hover:border-cyan-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Tasso sui Depositi BCE</h3>
                    <p class="text-sm text-gray-600">Il tasso che la BCE paga alle banche per i depositi overnight. È il principale strumento di politica monetaria e il riferimento per i tassi di mercato nell'Eurozona.</p>
                    <span class="text-xs text-cyan-600 font-semibold mt-2 inline-block">→ Spiegato in: FTSE MIB 19 marzo</span>
                </a>''',
    ],
    'Metriche Settoriali': [
        '''
                <a href="articolo-micron-19mar-earnings-record-sell-news-hbm4.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-amber-500 hover:border-amber-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">HBM — High Bandwidth Memory</h3>
                    <p class="text-sm text-gray-600">Memorie ad alta larghezza di banda essenziali per l'AI. Impilano chip DRAM verticalmente per offrire bandwidth 10x superiore. HBM4 è la generazione più avanzata.</p>
                    <span class="text-xs text-amber-600 font-semibold mt-2 inline-block">→ Spiegato in: Micron earnings 19 marzo</span>
                </a>''',
        '''
                <a href="articolo-micron-19mar-earnings-record-sell-news-hbm4.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-amber-500 hover:border-amber-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Il Paradosso del CapEx</h3>
                    <p class="text-sm text-gray-600">Quando un'azienda annuncia spese in conto capitale elevate, il mercato può punire il titolo anche con risultati record, perché il CapEx riduce il free cash flow atteso.</p>
                    <span class="text-xs text-amber-600 font-semibold mt-2 inline-block">→ Spiegato in: Micron earnings 19 marzo</span>
                </a>''',
    ],
    'Energia & Infrastrutture': [
        '''
                <a href="articolo-lng-19mar-iran-qatar-ras-laffan-europa-italia.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-orange-500 hover:border-orange-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Force Majeure nei Contratti Energetici</h3>
                    <p class="text-sm text-gray-600">Clausola che permette di sospendere le consegne in caso di eventi straordinari (guerra, disastri). Libera il fornitore dall'obbligo contrattuale, lasciando il compratore senza alternativa immediata.</p>
                    <span class="text-xs text-orange-600 font-semibold mt-2 inline-block">→ Spiegato in: Iran e Ras Laffan 19 marzo</span>
                </a>''',
        '''
                <a href="articolo-lng-19mar-iran-qatar-ras-laffan-europa-italia.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-orange-500 hover:border-orange-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">GNL — La Catena del Valore</h3>
                    <p class="text-sm text-gray-600">Il gas naturale liquefatto viene raffreddato a -162°C, trasportato via nave metaniera e rigassificato a destinazione. Non si può sostituire rapidamente: servono infrastrutture specifiche.</p>
                    <span class="text-xs text-orange-600 font-semibold mt-2 inline-block">→ Spiegato in: Iran e Ras Laffan 19 marzo</span>
                </a>''',
    ],
}

for section_name, cards in concepts.items():
    for card in cards:
        # Find the section and its last </div> before the next section
        section_marker = f'>{section_name}<'
        idx = impara.find(section_marker)
        if idx > 0:
            # Find the grid div after section marker
            grid_idx = impara.find('grid md:grid-cols', idx)
            if grid_idx > 0:
                # Find the closing </div> of the grid
                close_grid = impara.find('</div>', grid_idx)
                # Find all concept-cards inside this grid
                next_section = impara.find('<section', grid_idx + 1)
                if next_section == -1:
                    next_section = impara.find('</main>', grid_idx)
                # Find the last </a> before the closing </div> of grid
                search_area = impara[grid_idx:next_section]
                last_a = search_area.rfind('</a>')
                if last_a > 0:
                    insert_pos = grid_idx + last_a + 4  # after </a>
                    impara = impara[:insert_pos] + card + impara[insert_pos:]

with open('impara-finanza.html', 'w') as f:
    f.write(impara)
print("✅ impara-finanza.html aggiornato")


print("\n🎉 AGGIORNAMENTO 19 MARZO 2026 COMPLETATO!")
print("File aggiornati: index.html, sitemap.xml, categoria-wall-street.html, categoria-borsa-milano.html, categoria-commodities.html, impara-finanza.html")
