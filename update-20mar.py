#!/usr/bin/env python3
"""Aggiornamento 20 Marzo 2026 - Alma Finanza"""
import re

# ============================================================
# 1. INDEX.HTML
# ============================================================
with open('index.html', 'r') as f:
    html = f.read()

# --- TICKER ---
old_ticker_start = '        <div class="ticker-content">'
new_ticker_items = '''        <div class="ticker-content">
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EDJI" target="_blank">🇺🇸 Dow <span class="negative">45.577 (-0,96%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EGSPC" target="_blank">🇺🇸 S&P 500 <span class="negative">6.506 (-1,51%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EIXIC" target="_blank">🇺🇸 Nasdaq <span class="negative">21.648 (-2,01%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/FTSEMIB.MI" target="_blank">🇮🇹 FTSE MIB <span class="negative">42.841 (-1,97%)</span></a></div>
            <div class="ticker-item"><a href="articolo-supermicro-20mar-scandalo-smuggling-nvidia-cina.html">🔴 <span class="negative">Super Micro -20%: scandalo smuggling chip</span></a></div>
            <div class="ticker-item"><a href="articolo-fedex-20mar-earnings-record-guidance-economia.html">🟢 <span class="positive">FedEx +9% dopo earnings record</span></a></div>
            <div class="ticker-item"><a href="articolo-geopolitica-20mar-iran-kuwait-raffineria-hormuz.html">🔥 <span class="negative">Iran colpisce raffineria Kuwait</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EGDAXI" target="_blank">🇩🇪 DAX <span class="negative">22.380 (-2,01%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/GC%3DF" target="_blank">🥇 Oro <span class="negative">$4.500 (-1,8%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/BTC-USD" target="_blank">₿ <span class="positive">Bitcoin $70.800 (+1,0%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EVIX" target="_blank">⚠️ <span class="negative">VIX 26,78 (+11%)</span></a></div>
            <!-- Duplicate for seamless loop -->
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EDJI" target="_blank">🇺🇸 Dow <span class="negative">45.577 (-0,96%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EGSPC" target="_blank">🇺🇸 S&P 500 <span class="negative">6.506 (-1,51%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EIXIC" target="_blank">🇺🇸 Nasdaq <span class="negative">21.648 (-2,01%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/FTSEMIB.MI" target="_blank">🇮🇹 FTSE MIB <span class="negative">42.841 (-1,97%)</span></a></div>
            <div class="ticker-item"><a href="articolo-supermicro-20mar-scandalo-smuggling-nvidia-cina.html">🔴 <span class="negative">Super Micro -20%: scandalo smuggling chip</span></a></div>
            <div class="ticker-item"><a href="articolo-fedex-20mar-earnings-record-guidance-economia.html">🟢 <span class="positive">FedEx +9% dopo earnings record</span></a></div>
            <div class="ticker-item"><a href="articolo-geopolitica-20mar-iran-kuwait-raffineria-hormuz.html">🔥 <span class="negative">Iran colpisce raffineria Kuwait</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EGDAXI" target="_blank">🇩🇪 DAX <span class="negative">22.380 (-2,01%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/GC%3DF" target="_blank">🥇 Oro <span class="negative">$4.500 (-1,8%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/BTC-USD" target="_blank">₿ <span class="positive">Bitcoin $70.800 (+1,0%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EVIX" target="_blank">⚠️ <span class="negative">VIX 26,78 (+11%)</span></a></div>
                </div></div>'''

# Replace everything from ticker-content to the closing </div></div>
html = re.sub(
    r'        <div class="ticker-content">.*?</div></div>\s*</div>',
    new_ticker_items + '\n    </div>',
    html, count=1, flags=re.DOTALL
)

# --- DATE ---
html = html.replace('Giovedì 19 Marzo 2026', 'Venerdì 20 Marzo 2026')

# --- STATS BAR ---
html = html.replace(
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">46.021</div>
                <div class="text-xs negative">-204 (-0,44%)</div>''',
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">45.577</div>
                <div class="text-xs negative">-444 (-0,96%)</div>'''
)
html = html.replace(
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">6.606</div>
                <div class="text-xs negative">-18 (-0,27%)</div>''',
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">6.506</div>
                <div class="text-xs negative">-100 (-1,51%)</div>'''
)
html = html.replace(
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">43.701</div>
                <div class="text-xs negative">-1.040 (-2,32%)</div>''',
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">42.841</div>
                <div class="text-xs negative">-860 (-1,97%)</div>'''
)
html = html.replace(
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">$96,14</div>
                <div class="text-xs negative">-0,19%</div>''',
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">$93,80</div>
                <div class="text-xs negative">-2,4%</div>'''
)
html = html.replace(
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">$4.551</div>
                <div class="text-xs negative">-5,44%</div>''',
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">$4.500</div>
                <div class="text-xs negative">-1,8%</div>'''
)
html = html.replace(
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">$69.370</div>
                <div class="text-xs negative">-2,67%</div>''',
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">$70.800</div>
                <div class="text-xs positive">+1,0%</div>'''
)

# --- HERO ---
old_hero = '''                    <div class="flex items-center gap-3 mb-4">
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
                        Leggi l\'articolo completo'''

new_hero = '''                    <div class="flex items-center gap-3 mb-4">
                        <div class="dot bg-red-500 animate-pulse"></div>
                        <span class="text-xs font-bold text-red-600 dark:text-red-400 uppercase tracking-wider">Breaking · 20 Mar 2026</span>
                    </div>
                    <h1 class="text-3xl md:text-4xl font-black text-gray-900 dark:text-white mb-4 leading-tight montserrat-font">
                        Triple Witching travolge Wall Street: Nasdaq -2%, Super Micro crolla -20%. Iran colpisce Kuwait
                    </h1>
                    <div class="accent-line mb-4"></div>
                    <p class="text-gray-500 dark:text-slate-400 text-lg leading-relaxed mb-6">
                        $5,7 trilioni di opzioni in scadenza nel Triple Witching Friday. S&P 500 -1,51% sotto la media mobile a 200 giorni, Nasdaq -2,01%. Super Micro -20% dopo arresto cofondatore per smuggling chip Nvidia in Cina. FedEx +9% su earnings record. Iran colpisce raffineria Kuwait con droni. FTSE MIB -1,97% a 42.841.
                    </p>
                    <a href="articolo-wall-street-20mar-triple-witching-fedex-supermicro.html" class="inline-flex items-center text-teal-600 dark:text-teal-400 font-semibold text-sm hover:text-teal-700 dark:hover:text-teal-300 transition group">
                        Leggi l\'articolo completo'''

html = html.replace(old_hero, new_hero)

# Hero right panel
old_hero_right = '''                        <div class="text-5xl font-black text-gray-900 dark:text-white mb-1">-17%</div>
                        <div class="text-sm text-gray-500 dark:text-slate-500 mb-3">LNG Qatar — Iran colpisce Ras Laffan</div>
                        <div class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-red-50 dark:bg-red-500/15 text-red-600 dark:text-red-400">Gas TTF +23% · Force Majeure Italia</div>
                        <div class="mt-4 space-y-1 text-xs text-gray-400 dark:text-slate-600">
                            <div>FTSE MIB -2,32% · Inwit -15,6%</div>
                            <div>Oro -5,44% · BTC $69.370</div>'''

new_hero_right = '''                        <div class="text-5xl font-black text-gray-900 dark:text-white mb-1">-2,01%</div>
                        <div class="text-sm text-gray-500 dark:text-slate-500 mb-3">Nasdaq — Triple Witching Friday</div>
                        <div class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-red-50 dark:bg-red-500/15 text-red-600 dark:text-red-400">SMCI -20% · FedEx +9% · VIX 26,78</div>
                        <div class="mt-4 space-y-1 text-xs text-gray-400 dark:text-slate-600">
                            <div>S&P 500 -1,51% · FTSE MIB -1,97%</div>
                            <div>WTI $93,80 · BTC $70.800</div>'''

html = html.replace(old_hero_right, new_hero_right)

# --- SECTION HEADER + NEW CARDS ---
old_section = '''        <!-- Section header -->
        <div class="flex items-center gap-3 mb-6">
            <div class="accent-line"></div>
            <h2 class="text-lg font-bold montserrat-font text-gray-900 dark:text-white">Oggi, 19 Marzo</h2>
        </div>

        <!-- Articles Grid -->
        <div class="grid md:grid-cols-3 gap-5">'''

new_section = '''        <!-- Section header -->
        <div class="flex items-center gap-3 mb-6">
            <div class="accent-line"></div>
            <h2 class="text-lg font-bold montserrat-font text-gray-900 dark:text-white">Oggi, 20 Marzo</h2>
        </div>

        <!-- Articles Grid -->
        <div class="grid md:grid-cols-3 gap-5">


            <!-- ====== ARTICOLI 20 MARZO 2026 ====== -->

            <!-- Wall Street 20 mar -->
            <a href="articolo-wall-street-20mar-triple-witching-fedex-supermicro.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-blue-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-blue-50 dark:bg-blue-500/15 text-blue-700 dark:text-blue-400 border border-transparent dark:border-blue-500/20">Wall Street</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Triple Witching travolge Wall Street: Nasdaq -2,01%, FedEx +9%, Super Micro -20%</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Dow -444 a 45.577, S&P -1,51% a 6.506. $5,7T di opzioni in scadenza. VIX 26,78. S&P sotto media 200 giorni.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">20 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- FTSE MIB 20 mar -->
            <a href="articolo-ftse-mib-20mar-inwit-guidance-buzzi-banche.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-emerald-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-green-50 dark:bg-emerald-500/15 text-green-700 dark:text-emerald-400 border border-transparent dark:border-emerald-500/20">Piazza Affari</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">FTSE MIB -1,97% a 42.841: Inwit -9%, banche in recupero con MPS +2,4%</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Scadenze tecniche. Buzzi +3,4%, Moncler +2% dopo upgrade. Unicredit -3,4%. DAX -2%. Settimana -2,95%.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">20 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Super Micro 20 mar -->
            <a href="articolo-supermicro-20mar-scandalo-smuggling-nvidia-cina.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-purple-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-purple-50 dark:bg-purple-500/15 text-purple-700 dark:text-purple-400 border border-transparent dark:border-purple-500/20">Tech/AI</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Super Micro crolla -20%: cofondatore arrestato per smuggling chip Nvidia in Cina</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Yih-Shyan Liaw in manette. Schema con societa fantasma in SE Asia. Titolo -81% dai massimi. Nvidia -1,66%.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">20 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- FedEx 20 mar -->
            <a href="articolo-fedex-20mar-earnings-record-guidance-economia.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-sky-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-sky-50 dark:bg-sky-500/15 text-sky-700 dark:text-sky-400 border border-transparent dark:border-sky-500/20">Corporate</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">FedEx vola +9%: EPS $5,25 batte le attese del 28%. Guidance alzata</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Revenue $24B. Utile $1,06B. FY2026 EPS alzato a $19,30-$20,10. Segnale di resilienza economia globale.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">20 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Geopolitica Iran-Kuwait 20 mar -->
            <a href="articolo-geopolitica-20mar-iran-kuwait-raffineria-hormuz.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-red-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-red-50 dark:bg-red-500/15 text-red-700 dark:text-red-400 border border-transparent dark:border-red-500/20">Geopolitica</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Iran colpisce raffineria Kuwait: Mina Al-Ahmadi in fiamme. WTI scende a $93,80</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Droni su impianto da 730.000 bbl/giorno. Arabia Saudita e Dubai sotto attacco. 7 nazioni per riapertura Hormuz. Trump: "winding down".</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">20 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Day separator 19 Marzo -->
            <div class="col-span-full flex items-center gap-3 mt-6 mb-2">
                <div class="w-10 h-0.5 rounded-full bg-gray-200 dark:bg-slate-700/40"></div>
                <h2 class="text-sm font-bold montserrat-font text-gray-400 dark:text-slate-600 uppercase tracking-wider">19 Marzo 2026</h2>
                <div class="flex-1 h-0.5 rounded-full bg-gray-100 dark:bg-slate-800/20"></div>
            </div>'''

html = html.replace(old_section, new_section)

with open('index.html', 'w') as f:
    f.write(html)
print("✅ index.html aggiornato")

# ============================================================
# 2. SITEMAP.XML
# ============================================================
with open('sitemap.xml', 'r') as f:
    sitemap = f.read()

new_urls = '''  <!-- Articoli 20 Marzo 2026 -->
  <url>
      <loc>https://www.almafinanza.com/articolo-wall-street-20mar-triple-witching-fedex-supermicro.html</loc>
      <lastmod>2026-03-20</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-20</news:publication_date>
          <news:title>Wall Street 20 marzo: Triple Witching travolge i listini, Nasdaq -2,01%. FedEx +9%, Super Micro -20%</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-ftse-mib-20mar-inwit-guidance-buzzi-banche.html</loc>
      <lastmod>2026-03-20</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-20</news:publication_date>
          <news:title>FTSE MIB -1,97% a 42.841: Inwit -9%, banche in recupero con MPS +2,4%</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-supermicro-20mar-scandalo-smuggling-nvidia-cina.html</loc>
      <lastmod>2026-03-20</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-20</news:publication_date>
          <news:title>Super Micro crolla -20%: cofondatore arrestato per smuggling chip Nvidia in Cina</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-fedex-20mar-earnings-record-guidance-economia.html</loc>
      <lastmod>2026-03-20</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-20</news:publication_date>
          <news:title>FedEx vola +9% dopo earnings record: EPS $5,25 batte le attese del 28%. Guidance alzata</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-geopolitica-20mar-iran-kuwait-raffineria-hormuz.html</loc>
      <lastmod>2026-03-20</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-20</news:publication_date>
          <news:title>Iran colpisce raffineria Kuwait con droni: Mina Al-Ahmadi in fiamme. WTI scende a $93,80</news:title>
      </news:news>
  </url>

  '''

sitemap = sitemap.replace('<lastmod>2026-03-19</lastmod>\n    <changefreq>daily</changefreq>',
                          '<lastmod>2026-03-20</lastmod>\n    <changefreq>daily</changefreq>', 1)
sitemap = sitemap.replace('  <!-- Articoli 19 Marzo 2026 -->', new_urls + '<!-- Articoli 19 Marzo 2026 -->')

with open('sitemap.xml', 'w') as f:
    f.write(sitemap)
print("✅ sitemap.xml aggiornato")

# ============================================================
# 3. CATEGORIA WALL STREET
# ============================================================
with open('categoria-wall-street.html', 'r') as f:
    cat_ws = f.read()

new_ws_section = '''
                <section class="mb-12">
            <div class="flex items-center mb-6">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Venerdì, 20 Marzo 2026</h2>
                <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
            </div>
            <div class="grid md:grid-cols-3 gap-6">

                <a href="articolo-wall-street-20mar-triple-witching-fedex-supermicro.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#dbeafe;color:#1e40af;">Wall Street</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Triple Witching: Nasdaq -2,01%, FedEx +9%, Super Micro -20%</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Dow -444 a 45.577, S&P -1,51% a 6.506. $5,7T opzioni scadute. VIX 26,78. S&P sotto media 200 giorni.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 20 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

                <a href="articolo-supermicro-20mar-scandalo-smuggling-nvidia-cina.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#f3e8ff;color:#6b21a8;">Tech & AI</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Super Micro -20%: cofondatore arrestato per smuggling chip Nvidia</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Wally Liaw in manette. Schema con societa fantasma per esportare GPU in Cina. Titolo -81% dai massimi.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 20 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

                <a href="articolo-fedex-20mar-earnings-record-guidance-economia.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#e0f2fe;color:#0369a1;">Corporate</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">FedEx +9%: EPS $5,25 batte le attese del 28%. Guidance alzata</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Revenue $24B. FY2026 EPS alzato a $19,30-$20,10. Segnale di resilienza economia globale.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 20 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

                <a href="articolo-geopolitica-20mar-iran-kuwait-raffineria-hormuz.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#fee2e2;color:#991b1b;">Geopolitica</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Iran colpisce raffineria Kuwait: Mina Al-Ahmadi in fiamme</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Droni su impianto 730.000 bbl/giorno. Arabia Saudita e Dubai attaccate. WTI scende a $93,80. Trump: "winding down".</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 20 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

            </div>
        </section>

'''

cat_ws = cat_ws.replace(
    '                <section class="mb-12">\n            <div class="flex items-center mb-6">\n                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Giovedì, 19 Marzo 2026</h2>',
    new_ws_section + '                <section class="mb-12">\n            <div class="flex items-center mb-6">\n                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Giovedì, 19 Marzo 2026</h2>'
)

with open('categoria-wall-street.html', 'w') as f:
    f.write(cat_ws)
print("✅ categoria-wall-street.html aggiornato")

# ============================================================
# 4. CATEGORIA BORSA MILANO
# ============================================================
with open('categoria-borsa-milano.html', 'r') as f:
    cat_mi = f.read()

new_mi_section = '''
                <section class="mb-12">
            <div class="flex items-center mb-6">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Venerdì, 20 Marzo 2026</h2>
                <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
            </div>
            <div class="grid md:grid-cols-3 gap-6">

                <a href="articolo-ftse-mib-20mar-inwit-guidance-buzzi-banche.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#d1fae5;color:#065f46;">FTSE MIB</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">FTSE MIB -1,97%: Inwit -9%, banche in recupero con MPS +2,4%</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Milano a 42.841. Buzzi +3,4%, Moncler +2%. Unicredit -3,4%. Scadenze tecniche. Settimana -2,95%.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 20 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

            </div>
        </section>

'''

cat_mi = cat_mi.replace(
    '                <section class="mb-12">\n            <div class="flex items-center mb-6">\n                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Giovedì, 19 Marzo 2026</h2>',
    new_mi_section + '                <section class="mb-12">\n            <div class="flex items-center mb-6">\n                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Giovedì, 19 Marzo 2026</h2>'
)

with open('categoria-borsa-milano.html', 'w') as f:
    f.write(cat_mi)
print("✅ categoria-borsa-milano.html aggiornato")

# ============================================================
# 5. CATEGORIA COMMODITIES
# ============================================================
with open('categoria-commodities.html', 'r') as f:
    cat_co = f.read()

# Find the first section in commodities
new_co_section = '''
                <section class="mb-12">
            <div class="flex items-center mb-6">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Venerdì, 20 Marzo 2026</h2>
                <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
            </div>
            <div class="grid md:grid-cols-3 gap-6">

                <a href="articolo-geopolitica-20mar-iran-kuwait-raffineria-hormuz.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#fef3c7;color:#92400e;">Petrolio & Geopolitica</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Iran colpisce Kuwait: WTI scende a $93,80 su sforzi internazionali</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Droni su raffineria Mina Al-Ahmadi 730.000 bbl/giorno. 7 nazioni per Hormuz. USA revocano parzialmente sanzioni Iran.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 20 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

            </div>
        </section>

'''

# Find first section in commodities
first_section_match = re.search(r'(\s*<section class="mb-12">)', cat_co)
if first_section_match:
    pos = first_section_match.start()
    cat_co = cat_co[:pos] + new_co_section + cat_co[pos:]

with open('categoria-commodities.html', 'w') as f:
    f.write(cat_co)
print("✅ categoria-commodities.html aggiornato")

# ============================================================
# 6. IMPARA LA FINANZA
# ============================================================
with open('impara-finanza.html', 'r') as f:
    impara = f.read()

# Add to Meccanismi di Mercato (line ~536, before </div></section>)
new_meccanismi = '''
                <a href="articolo-wall-street-20mar-triple-witching-fedex-supermicro.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-purple-500 hover:border-purple-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Triple Witching — Scadenze Tecniche Trimestrali</h3>
                    <p class="text-sm text-gray-600">Quattro volte l'anno scadono contemporaneamente futures su indici, opzioni su indici e stock options. Il 20 marzo 2026 sono scaduti $5,7 trilioni di contratti, generando volumi e volatilita eccezionali.</p>
                    <span class="text-xs text-purple-600 font-semibold mt-2 inline-block">→ Spiegato in: Wall Street Triple Witching 20 Mar</span>
                </a>

                <a href="articolo-wall-street-20mar-triple-witching-fedex-supermicro.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-purple-500 hover:border-purple-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Export Controls sui Chip AI</h3>
                    <p class="text-sm text-gray-600">Gli USA vietano l'esportazione di chip AI avanzati (Nvidia H100/A100) verso la Cina per motivi di sicurezza nazionale. Il caso Super Micro dimostra che l'enforcement e reale: fino a 20 anni di carcere.</p>
                    <span class="text-xs text-purple-600 font-semibold mt-2 inline-block">→ Spiegato in: Super Micro Scandalo 20 Mar</span>
                </a>
'''

# Insert before closing of Meccanismi section
impara = impara.replace(
    '            </div>\n        </section>\n\n        <!-- Category: Business Models -->',
    new_meccanismi + '            </div>\n        </section>\n\n        <!-- Category: Business Models -->'
)

# Add to Macroeconomia section
new_macro = '''
                <a href="articolo-ftse-mib-20mar-inwit-guidance-buzzi-banche.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-cyan-500 hover:border-cyan-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Scadenze Tecniche Europee (Witching Day)</h3>
                    <p class="text-sm text-gray-600">In Europa, futures e opzioni sugli indici scadono simultaneamente 4 volte l'anno. I volumi possono raddoppiare o triplicare, creando movimenti di prezzo amplificati dal ribilanciamento istituzionale.</p>
                    <span class="text-xs text-cyan-600 font-semibold mt-2 inline-block">→ Spiegato in: FTSE MIB 20 Mar</span>
                </a>

                <a href="articolo-ftse-mib-20mar-inwit-guidance-buzzi-banche.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-cyan-500 hover:border-cyan-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Upgrade e Downgrade degli Analisti</h3>
                    <p class="text-sm text-gray-600">Le raccomandazioni degli analisti (outperform, neutral, underperform) e i target price influenzano il prezzo dei titoli. Un upgrade puo muovere un'azione del 2%+ in una singola seduta, come nel caso Moncler.</p>
                    <span class="text-xs text-cyan-600 font-semibold mt-2 inline-block">→ Spiegato in: FTSE MIB 20 Mar</span>
                </a>
'''

impara = impara.replace(
    '            </div>\n        </section>\n\n        <!-- Category: Meccanismi di Mercato -->',
    new_macro + '            </div>\n        </section>\n\n        <!-- Category: Meccanismi di Mercato -->'
)

# Add to Settori e Aziende Specifiche
new_settori = '''
                <a href="articolo-fedex-20mar-earnings-record-guidance-economia.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-rose-500 hover:border-rose-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">FedEx come Indicatore Economico</h3>
                    <p class="text-sm text-gray-600">Le aziende di logistica come FedEx sono considerate barometri dell'economia globale: se spediscono di piu, le imprese producono e vendono di piu. Earnings forti di FedEx sono un segnale bullish per l'economia.</p>
                    <span class="text-xs text-rose-600 font-semibold mt-2 inline-block">→ Spiegato in: FedEx Earnings 20 Mar</span>
                </a>

                <a href="articolo-fedex-20mar-earnings-record-guidance-economia.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-rose-500 hover:border-rose-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Earnings Season — la Stagione delle Trimestrali</h3>
                    <p class="text-sm text-gray-600">Quattro volte l'anno le aziende quotate pubblicano i risultati trimestrali. EPS, revenue e guidance vengono confrontati con il consenso degli analisti. Un "beat" spinge il titolo, un "miss" lo affonda.</p>
                    <span class="text-xs text-rose-600 font-semibold mt-2 inline-block">→ Spiegato in: FedEx Earnings 20 Mar</span>
                </a>

                <a href="articolo-supermicro-20mar-scandalo-smuggling-nvidia-cina.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-rose-500 hover:border-rose-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Concentrazione dei Ricavi — il Rischio di un Solo Cliente</h3>
                    <p class="text-sm text-gray-600">Quando un'azienda dipende da un singolo cliente per oltre il 50% dei ricavi (come SMCI con Nvidia al 63%), qualsiasi problema nella relazione puo essere devastante per il titolo.</p>
                    <span class="text-xs text-rose-600 font-semibold mt-2 inline-block">→ Spiegato in: Super Micro Scandalo 20 Mar</span>
                </a>
'''

# Find end of Settori section
impara = impara.replace(
    '            </div>\n        </section>\n\n    </main>',
    new_settori + '            </div>\n        </section>\n\n    </main>',
    1
)

# Add to Geopolitica section
new_geo = '''
                <a href="articolo-geopolitica-20mar-iran-kuwait-raffineria-hormuz.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-rose-500 hover:border-rose-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Mina Al-Ahmadi — il Cuore Petrolifero del Kuwait</h3>
                    <p class="text-sm text-gray-600">La piu grande raffineria del Kuwait processa 730.000 barili al giorno. Il Kuwait e membro OPEC con una produzione di ~2,7 milioni bbl/giorno. Un attacco alla raffineria impatta l'intera catena di approvvigionamento globale.</p>
                    <span class="text-xs text-rose-600 font-semibold mt-2 inline-block">→ Spiegato in: Iran Kuwait 20 Mar</span>
                </a>

                <a href="articolo-geopolitica-20mar-iran-kuwait-raffineria-hormuz.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-rose-500 hover:border-rose-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Sanzioni Petrolifere — Revoca Strategica</h3>
                    <p class="text-sm text-gray-600">Le sanzioni petrolifere limitano le esportazioni di un Paese per pressione politica. In crisi, possono essere temporaneamente revocate per aumentare l'offerta globale, come i 140 milioni di barili sbloccati dagli USA.</p>
                    <span class="text-xs text-rose-600 font-semibold mt-2 inline-block">→ Spiegato in: Iran Kuwait 20 Mar</span>
                </a>
'''

impara = impara.replace(
    '            </div>\n        </section>\n\n        <!-- Category: Energia & Infrastrutture -->',
    new_geo + '            </div>\n        </section>\n\n        <!-- Category: Energia & Infrastrutture -->'
)

with open('impara-finanza.html', 'w') as f:
    f.write(impara)
print("✅ impara-finanza.html aggiornato")

print("\n🎉 Aggiornamento 20 Marzo 2026 completato!")
