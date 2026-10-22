#!/usr/bin/env python3
"""Aggiornamento 23 Marzo 2026 - Alma Finanza"""
import re

# ============================================================
# 1. INDEX.HTML
# ============================================================
with open('index.html', 'r') as f:
    html = f.read()

# --- TICKER ---
new_ticker_items = '''        <div class="ticker-content">
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EDJI" target="_blank">🇺🇸 Dow <span class="positive">46.208 (+1,38%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EGSPC" target="_blank">🇺🇸 S&P 500 <span class="positive">6.581 (+1,15%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EIXIC" target="_blank">🇺🇸 Nasdaq <span class="positive">21.947 (+1,38%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/FTSEMIB.MI" target="_blank">🇮🇹 FTSE MIB <span class="positive">43.190 (+0,81%)</span></a></div>
            <div class="ticker-item"><a href="articolo-mercati-23mar-outlook-trump-iran-scenari.html">🕊️ <span class="positive">Trump: pausa 5 giorni attacchi Iran</span></a></div>
            <div class="ticker-item"><a href="articolo-petrolio-23mar-crollo-trump-iran-pausa-diplomazia.html">🛢️ <span class="positive">WTI crolla -9% a $89</span></a></div>
            <div class="ticker-item"><a href="articolo-ftse-mib-23mar-poste-tim-opas-rimbalzo.html">📬 <span class="positive">Poste OPAS su TIM: €10,8 miliardi</span></a></div>
            <div class="ticker-item"><a href="articolo-asia-23mar-crollo-kospi-nikkei-hang-seng-hormuz.html">🔴 <span class="negative">Asia crolla: Kospi -6,5%</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EGDAXI" target="_blank">🇩🇪 DAX <span class="positive">+2,2%</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/GC%3DF" target="_blank">🥇 Oro <span class="negative">$4.406 (-3,69%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/BTC-USD" target="_blank">₿ <span class="positive">Bitcoin $70.903 (+3,9%)</span></a></div>
            <!-- Duplicate for seamless loop -->
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EDJI" target="_blank">🇺🇸 Dow <span class="positive">46.208 (+1,38%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EGSPC" target="_blank">🇺🇸 S&P 500 <span class="positive">6.581 (+1,15%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EIXIC" target="_blank">🇺🇸 Nasdaq <span class="positive">21.947 (+1,38%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/FTSEMIB.MI" target="_blank">🇮🇹 FTSE MIB <span class="positive">43.190 (+0,81%)</span></a></div>
            <div class="ticker-item"><a href="articolo-mercati-23mar-outlook-trump-iran-scenari.html">🕊️ <span class="positive">Trump: pausa 5 giorni attacchi Iran</span></a></div>
            <div class="ticker-item"><a href="articolo-petrolio-23mar-crollo-trump-iran-pausa-diplomazia.html">🛢️ <span class="positive">WTI crolla -9% a $89</span></a></div>
            <div class="ticker-item"><a href="articolo-ftse-mib-23mar-poste-tim-opas-rimbalzo.html">📬 <span class="positive">Poste OPAS su TIM: €10,8 miliardi</span></a></div>
            <div class="ticker-item"><a href="articolo-asia-23mar-crollo-kospi-nikkei-hang-seng-hormuz.html">🔴 <span class="negative">Asia crolla: Kospi -6,5%</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/%5EGDAXI" target="_blank">🇩🇪 DAX <span class="positive">+2,2%</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/GC%3DF" target="_blank">🥇 Oro <span class="negative">$4.406 (-3,69%)</span></a></div>
            <div class="ticker-item"><a href="https://finance.yahoo.com/quote/BTC-USD" target="_blank">₿ <span class="positive">Bitcoin $70.903 (+3,9%)</span></a></div>
                </div></div>'''

html = re.sub(
    r'        <div class="ticker-content">.*?</div></div>\s*</div>',
    new_ticker_items + '\n    </div>',
    html, count=1, flags=re.DOTALL
)

# --- DATE ---
html = html.replace('Venerdì 20 Marzo 2026', 'Lunedì 23 Marzo 2026')

# --- STATS BAR ---
html = html.replace(
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">45.577</div>
                <div class="text-xs negative">-444 (-0,96%)</div>''',
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">46.208</div>
                <div class="text-xs positive">+631 (+1,38%)</div>'''
)
html = html.replace(
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">6.506</div>
                <div class="text-xs negative">-100 (-1,51%)</div>''',
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">6.581</div>
                <div class="text-xs positive">+75 (+1,15%)</div>'''
)
html = html.replace(
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">42.841</div>
                <div class="text-xs negative">-860 (-1,97%)</div>''',
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">43.190</div>
                <div class="text-xs positive">+349 (+0,81%)</div>'''
)
html = html.replace(
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">$93,80</div>
                <div class="text-xs negative">-2,4%</div>''',
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">$89,45</div>
                <div class="text-xs positive">-8,94%</div>'''
)
html = html.replace(
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">$4.500</div>
                <div class="text-xs negative">-1,8%</div>''',
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">$4.406</div>
                <div class="text-xs negative">-3,69%</div>'''
)
html = html.replace(
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">$70.800</div>
                <div class="text-xs positive">+1,0%</div>''',
    '''<div class="text-lg font-bold text-gray-900 dark:text-white">$70.903</div>
                <div class="text-xs positive">+3,9%</div>'''
)

# --- HERO ---
old_hero = '''                    <div class="flex items-center gap-3 mb-4">
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

new_hero = '''                    <div class="flex items-center gap-3 mb-4">
                        <div class="dot bg-emerald-500 animate-pulse"></div>
                        <span class="text-xs font-bold text-emerald-600 dark:text-emerald-400 uppercase tracking-wider">Breaking · 23 Mar 2026</span>
                    </div>
                    <h1 class="text-3xl md:text-4xl font-black text-gray-900 dark:text-white mb-4 leading-tight montserrat-font">
                        Trump annuncia pausa 5 giorni sull'Iran: borse volano, petrolio crolla -9%. Poste lancia OPAS su TIM
                    </h1>
                    <div class="accent-line mb-4"></div>
                    <p class="text-gray-500 dark:text-slate-400 text-lg leading-relaxed mb-6">
                        Rally globale dopo l'annuncio di Trump: "colloqui produttivi" con l'Iran, sospesi attacchi a infrastrutture energetiche per 5 giorni. Dow +631 a 46.208, S&P +1,15%. WTI crolla da $98 a $89 (-9%). Asia era crollata prima: Kospi -6,5%, Nikkei -3,5%. Poste Italiane lancia OPAS su TIM da €10,8 miliardi. Iran nega i colloqui. Scadenza 28 marzo.
                    </p>
                    <a href="articolo-mercati-23mar-outlook-trump-iran-scenari.html" class="inline-flex items-center text-teal-600 dark:text-teal-400 font-semibold text-sm hover:text-teal-700 dark:hover:text-teal-300 transition group">
                        Leggi l\'articolo completo'''

html = html.replace(old_hero, new_hero)

# Hero right panel
old_hero_right = '''                        <div class="text-5xl font-black text-gray-900 dark:text-white mb-1">-2,01%</div>
                        <div class="text-sm text-gray-500 dark:text-slate-500 mb-3">Nasdaq — Triple Witching Friday</div>
                        <div class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-red-50 dark:bg-red-500/15 text-red-600 dark:text-red-400">SMCI -20% · FedEx +9% · VIX 26,78</div>
                        <div class="mt-4 space-y-1 text-xs text-gray-400 dark:text-slate-600">
                            <div>S&P 500 -1,51% · FTSE MIB -1,97%</div>
                            <div>WTI $93,80 · BTC $70.800</div>'''

new_hero_right = '''                        <div class="text-5xl font-black text-gray-900 dark:text-white mb-1">-9%</div>
                        <div class="text-sm text-gray-500 dark:text-slate-500 mb-3">WTI Crude — Trump pausa Iran</div>
                        <div class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-emerald-50 dark:bg-emerald-500/15 text-emerald-600 dark:text-emerald-400">Dow +631 · Poste OPAS TIM €10,8B</div>
                        <div class="mt-4 space-y-1 text-xs text-gray-400 dark:text-slate-600">
                            <div>S&P +1,15% · DAX +2,2% · MIB +0,81%</div>
                            <div>Oro -3,69% · BTC +3,9%</div>'''

html = html.replace(old_hero_right, new_hero_right)

# --- SECTION HEADER + NEW CARDS ---
old_section = '''        <!-- Section header -->
        <div class="flex items-center gap-3 mb-6">
            <div class="accent-line"></div>
            <h2 class="text-lg font-bold montserrat-font text-gray-900 dark:text-white">Oggi, 20 Marzo</h2>
        </div>'''

new_section = '''        <!-- Section header -->
        <div class="flex items-center gap-3 mb-6">
            <div class="accent-line"></div>
            <h2 class="text-lg font-bold montserrat-font text-gray-900 dark:text-white">Oggi, 23 Marzo</h2>
        </div>'''

html = html.replace(old_section, new_section)

# Insert new cards before the 20 March cards
old_cards = '''            <!-- ====== ARTICOLI 20 MARZO 2026 ====== -->'''

new_cards = '''            <!-- ====== ARTICOLI 23 MARZO 2026 ====== -->

            <!-- Wall Street 23 mar -->
            <a href="articolo-wall-street-23mar-rally-trump-iran-pausa.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-blue-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-blue-50 dark:bg-blue-500/15 text-blue-700 dark:text-blue-400 border border-transparent dark:border-blue-500/20">Wall Street</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Wall Street rimbalza: Dow +631, S&P +1,15% dopo la pausa di Trump sull'Iran</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Nasdaq +1,38%. WTI -9%. Tesla +3%, Nvidia +2%. 4 titoli su 5 in verde. Airlines volano. VIX in calo.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">23 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- FTSE MIB 23 mar -->
            <a href="articolo-ftse-mib-23mar-poste-tim-opas-rimbalzo.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-emerald-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-green-50 dark:bg-emerald-500/15 text-green-700 dark:text-emerald-400 border border-transparent dark:border-emerald-500/20">Piazza Affari</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">FTSE MIB +0,81%: Poste lancia OPAS su TIM da €10,8 miliardi</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">TIM +4,7%, Poste -7%. Milano rimbalza dopo apertura in forte calo. Spread BTP-Bund a 97 pb.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">23 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Outlook mercati 23 mar -->
            <a href="articolo-mercati-23mar-outlook-trump-iran-scenari.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-red-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-red-50 dark:bg-red-500/15 text-red-700 dark:text-red-400 border border-transparent dark:border-red-500/20">Analisi & Scenari</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Mercati globali: tra pausa diplomatica e incertezza. Cosa aspettarsi nei prossimi giorni</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">24 giorni di guerra. WTI da $70 a $119 e ritorno a $89. Tre scenari per il 28 marzo. Iran nega colloqui. Hormuz resta minato.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">23 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Petrolio 23 mar -->
            <a href="articolo-petrolio-23mar-crollo-trump-iran-pausa-diplomazia.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-amber-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-amber-50 dark:bg-amber-500/15 text-amber-700 dark:text-amber-400 border border-transparent dark:border-amber-500/20">Commodities</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Petrolio crolla -9%: WTI a $89 dopo la pausa di Trump. Brent da $113 a $101</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Piu grande calo giornaliero da inizio conflitto. Airlines volano: Norwegian +8%. Ma Hormuz resta minato.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">23 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Asia 23 mar -->
            <a href="articolo-asia-23mar-crollo-kospi-nikkei-hang-seng-hormuz.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-blue-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-blue-50 dark:bg-blue-500/15 text-blue-700 dark:text-blue-400 border border-transparent dark:border-blue-500/20">Asia & Globali</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Asia crolla prima di Trump: Kospi -6,5%, Nikkei -3,5%, Hang Seng -3,5%</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Borse asiatiche chiudono prima della pausa diplomatica. Corea peggior seduta dal 2020. Semiconduttori devastati.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">23 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Day separator 20 Marzo -->
            <div class="col-span-full flex items-center gap-3 mt-6 mb-2">
                <div class="w-10 h-0.5 rounded-full bg-gray-200 dark:bg-slate-700/40"></div>
                <h2 class="text-sm font-bold montserrat-font text-gray-400 dark:text-slate-600 uppercase tracking-wider">20 Marzo 2026</h2>
                <div class="flex-1 h-0.5 rounded-full bg-gray-100 dark:bg-slate-800/20"></div>
            </div>

            <!-- ====== ARTICOLI 20 MARZO 2026 ====== -->'''

html = html.replace(old_cards, new_cards)

with open('index.html', 'w') as f:
    f.write(html)
print("✅ index.html aggiornato")

# ============================================================
# 2. SITEMAP.XML
# ============================================================
with open('sitemap.xml', 'r') as f:
    sitemap = f.read()

new_urls = '''  <!-- Articoli 23 Marzo 2026 -->
  <url>
      <loc>https://www.almafinanza.com/articolo-wall-street-23mar-rally-trump-iran-pausa.html</loc>
      <lastmod>2026-03-23</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-23</news:publication_date>
          <news:title>Wall Street rimbalza: Dow +631, S&amp;P +1,15% dopo la pausa di Trump sull'Iran</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-ftse-mib-23mar-poste-tim-opas-rimbalzo.html</loc>
      <lastmod>2026-03-23</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-23</news:publication_date>
          <news:title>FTSE MIB +0,81%: Poste Italiane lancia OPAS su TIM da €10,8 miliardi</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-mercati-23mar-outlook-trump-iran-scenari.html</loc>
      <lastmod>2026-03-23</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-23</news:publication_date>
          <news:title>Mercati globali: tra pausa diplomatica e incertezza. Cosa aspettarsi dopo il dietrofront di Trump</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-petrolio-23mar-crollo-trump-iran-pausa-diplomazia.html</loc>
      <lastmod>2026-03-23</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-23</news:publication_date>
          <news:title>Petrolio crolla -9%: WTI a $89 dopo la pausa di Trump. Brent da $113 a $101</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-asia-23mar-crollo-kospi-nikkei-hang-seng-hormuz.html</loc>
      <lastmod>2026-03-23</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-23</news:publication_date>
          <news:title>Asia crolla prima di Trump: Kospi -6,5%, Nikkei -3,5%, Hang Seng -3,5%</news:title>
      </news:news>
  </url>

  '''

sitemap = sitemap.replace('<lastmod>2026-03-20</lastmod>\n    <changefreq>daily</changefreq>',
                          '<lastmod>2026-03-23</lastmod>\n    <changefreq>daily</changefreq>', 1)
sitemap = sitemap.replace('  <!-- Articoli 20 Marzo 2026 -->', new_urls + '<!-- Articoli 20 Marzo 2026 -->')

with open('sitemap.xml', 'w') as f:
    f.write(sitemap)
print("✅ sitemap.xml aggiornato")

# ============================================================
# 3. CATEGORIA WALL STREET
# ============================================================
with open('categoria-wall-street.html', 'r') as f:
    cat_ws = f.read()

new_ws = '''
                <section class="mb-12">
            <div class="flex items-center mb-6">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Lunedì, 23 Marzo 2026</h2>
                <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
            </div>
            <div class="grid md:grid-cols-3 gap-6">

                <a href="articolo-wall-street-23mar-rally-trump-iran-pausa.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#dbeafe;color:#1e40af;">Wall Street</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Wall Street rimbalza: Dow +631, S&P +1,15% su pausa Trump-Iran</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Nasdaq +1,38%. WTI -9% a $89. Tesla +3%, 3M +4,38%. 4 su 5 titoli S&P in verde.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 23 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

                <a href="articolo-mercati-23mar-outlook-trump-iran-scenari.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#fee2e2;color:#991b1b;">Analisi & Scenari</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Mercati globali: pausa diplomatica e incertezza. Tre scenari</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">24 giorni di guerra. WTI da $70 a $119. Iran nega colloqui. Scadenza 28 marzo.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 23 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

                <a href="articolo-asia-23mar-crollo-kospi-nikkei-hang-seng-hormuz.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#dbeafe;color:#1e40af;">Asia & Globali</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Asia crolla prima di Trump: Kospi -6,5%, Nikkei -3,5%</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Borse asiatiche chiudono prima della pausa. Corea peggior seduta dal 2020.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 23 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

            </div>
        </section>

'''

cat_ws = cat_ws.replace(
    '\n                <section class="mb-12">\n            <div class="flex items-center mb-6">\n                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Venerdì, 20 Marzo 2026</h2>',
    new_ws + '                <section class="mb-12">\n            <div class="flex items-center mb-6">\n                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Venerdì, 20 Marzo 2026</h2>'
)

with open('categoria-wall-street.html', 'w') as f:
    f.write(cat_ws)
print("✅ categoria-wall-street.html aggiornato")

# ============================================================
# 4. CATEGORIA BORSA MILANO
# ============================================================
with open('categoria-borsa-milano.html', 'r') as f:
    cat_mi = f.read()

new_mi = '''
                <section class="mb-12">
            <div class="flex items-center mb-6">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Lunedì, 23 Marzo 2026</h2>
                <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
            </div>
            <div class="grid md:grid-cols-3 gap-6">

                <a href="articolo-ftse-mib-23mar-poste-tim-opas-rimbalzo.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#d1fae5;color:#065f46;">FTSE MIB</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">FTSE MIB +0,81%: Poste lancia OPAS su TIM da €10,8 miliardi</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">TIM +4,7%, Poste -7%. Milano rimbalza su pausa Trump-Iran. Spread BTP-Bund 97 pb.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 23 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

            </div>
        </section>

'''

cat_mi = cat_mi.replace(
    '\n                <section class="mb-12">\n            <div class="flex items-center mb-6">\n                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Venerdì, 20 Marzo 2026</h2>',
    new_mi + '                <section class="mb-12">\n            <div class="flex items-center mb-6">\n                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Venerdì, 20 Marzo 2026</h2>'
)

with open('categoria-borsa-milano.html', 'w') as f:
    f.write(cat_mi)
print("✅ categoria-borsa-milano.html aggiornato")

# ============================================================
# 5. CATEGORIA COMMODITIES
# ============================================================
with open('categoria-commodities.html', 'r') as f:
    cat_co = f.read()

new_co = '''
                <section class="mb-12">
            <div class="flex items-center mb-6">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Lunedì, 23 Marzo 2026</h2>
                <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
            </div>
            <div class="grid md:grid-cols-3 gap-6">

                <a href="articolo-petrolio-23mar-crollo-trump-iran-pausa-diplomazia.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#fef3c7;color:#92400e;">Petrolio</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Petrolio crolla -9%: WTI a $89 dopo pausa Trump</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Brent da $113 a $101. Piu grande calo da inizio conflitto. Airlines +5-8%.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 23 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>

            </div>
        </section>

'''

cat_co = cat_co.replace(
    '\n                <section class="mb-12">\n            <div class="flex items-center mb-6">\n                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Venerdì, 20 Marzo 2026</h2>',
    new_co + '                <section class="mb-12">\n            <div class="flex items-center mb-6">\n                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Venerdì, 20 Marzo 2026</h2>'
)

with open('categoria-commodities.html', 'w') as f:
    f.write(cat_co)
print("✅ categoria-commodities.html aggiornato")

# ============================================================
# 6. IMPARA LA FINANZA
# ============================================================
with open('impara-finanza.html', 'r') as f:
    impara = f.read()

# Meccanismi di Mercato: Relief Rally + War Premium
new_meccanismi = '''
                <a href="articolo-mercati-23mar-outlook-trump-iran-scenari.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-purple-500 hover:border-purple-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Relief Rally — il Rimbalzo del Sollievo</h3>
                    <p class="text-sm text-gray-600">Quando i mercati hanno prezzato lo scenario peggiore, qualsiasi miglioramento innesca un rimbalzo violento. Non significa che la crisi sia finita: spesso seguito da vendite se la realta delude.</p>
                    <span class="text-xs text-purple-600 font-semibold mt-2 inline-block">→ Spiegato in: Outlook Mercati 23 Mar</span>
                </a>

                <a href="articolo-wall-street-23mar-rally-trump-iran-pausa.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-purple-500 hover:border-purple-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Il Premio di Rischio Geopolitico nel Petrolio</h3>
                    <p class="text-sm text-gray-600">Il prezzo del petrolio include un premio sopra il valore equo quando esiste rischio di guerra. La de-escalation fa evaporare questo premio rapidamente: il 23 marzo il WTI e sceso del 9% in un giorno.</p>
                    <span class="text-xs text-purple-600 font-semibold mt-2 inline-block">→ Spiegato in: Wall Street Rally 23 Mar</span>
                </a>
'''

impara = impara.replace(
    '            </div>\n        </section>\n\n        <!-- Category: Business Models -->',
    new_meccanismi + '            </div>\n        </section>\n\n        <!-- Category: Business Models -->'
)

# Macroeconomia: Dilemma banche centrali + OPAS
new_macro = '''
                <a href="articolo-mercati-23mar-outlook-trump-iran-scenari.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-cyan-500 hover:border-cyan-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Il Dilemma delle Banche Centrali durante le Guerre</h3>
                    <p class="text-sm text-gray-600">Quando il petrolio sale per guerra, le banche centrali affrontano una scelta impossibile: alzare i tassi per combattere l'inflazione (rischiando recessione) o tagliarli per sostenere la crescita. La trappola della stagflazione.</p>
                    <span class="text-xs text-cyan-600 font-semibold mt-2 inline-block">→ Spiegato in: Outlook Mercati 23 Mar</span>
                </a>

                <a href="articolo-ftse-mib-23mar-poste-tim-opas-rimbalzo.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-cyan-500 hover:border-cyan-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">OPAS — Offerta Pubblica di Acquisto e Scambio</h3>
                    <p class="text-sm text-gray-600">Un'offerta per acquistare tutte le azioni di una societa quotata, pagando in contanti e azioni. Poste Italiane ha lanciato un'OPAS da €10,8 miliardi su TIM con soglia di adesione al 66,67% per il delisting.</p>
                    <span class="text-xs text-cyan-600 font-semibold mt-2 inline-block">→ Spiegato in: FTSE MIB Poste-TIM 23 Mar</span>
                </a>
'''

impara = impara.replace(
    '            </div>\n        </section>\n\n        <!-- Category: Meccanismi di Mercato -->',
    new_macro + '            </div>\n        </section>\n\n        <!-- Category: Meccanismi di Mercato -->'
)

# Geopolitica: Fuso orario come fattore di rischio + Dipendenza energetica asiatica
new_geo = '''
                <a href="articolo-asia-23mar-crollo-kospi-nikkei-hang-seng-hormuz.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-rose-500 hover:border-rose-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Il Fuso Orario come Fattore di Rischio</h3>
                    <p class="text-sm text-gray-600">Le borse asiatiche chiudono 8-12 ore prima di Wall Street. Breaking news nel pomeriggio USA significa che l'Asia opera su informazioni vecchie. Il 23 marzo l'Asia e crollata prima che Trump annunciasse la pausa.</p>
                    <span class="text-xs text-rose-600 font-semibold mt-2 inline-block">→ Spiegato in: Asia Crolla 23 Mar</span>
                </a>

                <a href="articolo-asia-23mar-crollo-kospi-nikkei-hang-seng-hormuz.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-rose-500 hover:border-rose-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Dipendenza Energetica Asiatica</h3>
                    <p class="text-sm text-gray-600">Corea del Sud, Giappone e Taiwan importano il 100% dell'energia. Quando Hormuz e bloccato, la loro economia e minacciata: costi produzione esplodono, surplus commerciale si riduce, valuta si indebolisce.</p>
                    <span class="text-xs text-rose-600 font-semibold mt-2 inline-block">→ Spiegato in: Asia Crolla 23 Mar</span>
                </a>
'''

impara = impara.replace(
    '            </div>\n        </section>\n\n        <!-- Category: Energia & Infrastrutture -->',
    new_geo + '            </div>\n        </section>\n\n        <!-- Category: Energia & Infrastrutture -->'
)

# Energia: Volatilita petrolio + Impatto vita quotidiana
new_energia = '''
                <a href="articolo-petrolio-23mar-crollo-trump-iran-pausa-diplomazia.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-orange-500 hover:border-orange-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Volatilita del Petrolio — Oscillazioni di $17 in un Giorno</h3>
                    <p class="text-sm text-gray-600">Quando la domanda-offerta di petrolio e tesa, qualsiasi notizia geopolitica muove i prezzi drammaticamente. Trading algoritmico amplifica i movimenti. Il 23 marzo il WTI ha oscillato tra $84 e $101 nella stessa seduta.</p>
                    <span class="text-xs text-orange-600 font-semibold mt-2 inline-block">→ Spiegato in: Petrolio Crollo 23 Mar</span>
                </a>

                <a href="articolo-petrolio-23mar-crollo-trump-iran-pausa-diplomazia.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-orange-500 hover:border-orange-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Come il Prezzo del Petrolio Influenza la Vita Quotidiana</h3>
                    <p class="text-sm text-gray-600">Dal greggio alla benzina, riscaldamento, plastica, trasporto alimentare, biglietti aerei. Quando il WTI scende da $98 a $89, i consumatori vedono gli effetti in 2-4 settimane su carburante e bollette.</p>
                    <span class="text-xs text-orange-600 font-semibold mt-2 inline-block">→ Spiegato in: Petrolio Crollo 23 Mar</span>
                </a>
'''

# Insert before closing of Energia section
impara = impara.replace(
    '        </div>\n        </section>\n\n        <!-- Category: Settore Finanziario & Bancario -->',
    new_energia + '        </div>\n        </section>\n\n        <!-- Category: Settore Finanziario & Bancario -->'
)

# Settore Finanziario: Spread BTP-Bund
new_fin = '''
                <a href="articolo-ftse-mib-23mar-poste-tim-opas-rimbalzo.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-emerald-500 hover:border-emerald-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Spread BTP-Bund — il Termometro del Rischio Italia</h3>
                    <p class="text-sm text-gray-600">La differenza tra rendimento dei BTP italiani e dei Bund tedeschi misura il premio di rischio dell'Italia. A 97 punti base il 23 marzo segnala tensione elevata: storicamente sopra 100 pb scatta l'allarme.</p>
                    <span class="text-xs text-emerald-600 font-semibold mt-2 inline-block">→ Spiegato in: FTSE MIB 23 Mar</span>
                </a>
'''

impara = impara.replace(
    '            </div>\n        </section>\n\n    </main>',
    new_fin + '            </div>\n        </section>\n\n    </main>',
    1
)

with open('impara-finanza.html', 'w') as f:
    f.write(impara)
print("✅ impara-finanza.html aggiornato")

print("\n🎉 Aggiornamento 23 Marzo 2026 completato!")
