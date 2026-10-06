#!/usr/bin/env python3
"""Aggiornamento 17 Marzo 2026 — homepage, sitemap, categorie, impara-finanza"""
import re

# ========== INDEX.HTML ==========
with open('index.html', 'r') as f:
    html = f.read()

# 1. TICKER — replace all ticker items
old_ticker_start = '<div class="ticker-content">'
old_ticker_end = '</div></div>\n    </div>'
ticker_start_idx = html.index(old_ticker_start)
ticker_end_idx = html.index(old_ticker_end, ticker_start_idx) + len(old_ticker_end)

ticker_items = '''<div class="ticker-item" data-ticker="dow"><a href="https://finance.yahoo.com/quote/%5EDJI" target="_blank">🇺🇸 Dow <span class="positive">46.993 (+0,10%)</span></a></div>
            <div class="ticker-item" data-ticker="sp500"><a href="https://finance.yahoo.com/quote/%5EGSPC" target="_blank">🇺🇸 S&P 500 <span class="positive">6.716 (+0,25%)</span></a></div>
            <div class="ticker-item" data-ticker="nasdaq"><a href="https://finance.yahoo.com/quote/%5EIXIC" target="_blank">🇺🇸 Nasdaq <span class="positive">22.479 (+0,47%)</span></a></div>
            <div class="ticker-item" data-ticker="ftsemib"><a href="https://finance.yahoo.com/quote/FTSEMIB.MI" target="_blank">🇮🇹 FTSE MIB <span class="positive">44.347 (+0,10%)</span></a></div>
            <div class="ticker-item" data-ticker="amplifon"><a href="articolo-ftse-mib-17mar-amplifon-crolla-gn-hearing-banche.html">📉 <span class="negative">Amplifon -13,57%: acquisizione GN Hearing</span></a></div>
            <div class="ticker-item" data-ticker="nvidia"><a href="articolo-nvidia-17mar-gtc-vera-rubin-trilione-ordini.html">🚀 <span class="positive">Nvidia GTC: $1T ordini Vera Rubin</span></a></div>
            <div class="ticker-item" data-ticker="hormuz"><a href="articolo-hormuz-17mar-iran-petrolio-crisi-stretto.html">🛢️ <span class="negative">Hormuz: Iran colpisce UAE, WTI $96</span></a></div>
            <div class="ticker-item" data-ticker="dax"><a href="https://finance.yahoo.com/quote/%5EGDAXI" target="_blank">🇩🇪 DAX <span class="positive">23.727 (+0,69%)</span></a></div>
            <div class="ticker-item" data-ticker="oil"><a href="https://finance.yahoo.com/quote/CL%3DF" target="_blank">🛢️ WTI <span class="positive">$96 (+1,1%)</span></a></div>
            <div class="ticker-item" data-ticker="gold"><a href="https://finance.yahoo.com/quote/GC%3DF" target="_blank">🥇 Oro <span class="positive">$5.020 (+0,28%)</span></a></div>
            <div class="ticker-item" data-ticker="btc"><a href="https://finance.yahoo.com/quote/BTC-USD" target="_blank">₿ <span class="negative">Bitcoin $73.717 (-0,22%)</span></a></div>
            <div class="ticker-item" data-ticker="fed"><a href="articolo-wall-street-17mar-sp500-nasdaq-fed-hormuz.html">🏛️ <span class="negative">FOMC domani 18 marzo: tassi fermi?</span></a></div>'''

new_ticker = f'''{old_ticker_start}
            {ticker_items}
            <!-- Duplicate for seamless loop -->
            {ticker_items}
        </div></div>
    </div>'''

html = html[:ticker_start_idx] + new_ticker + html[ticker_end_idx:]

# 2. DATE in header
html = html.replace('Lunedì 16 Marzo 2026', 'Martedì 17 Marzo 2026')

# 3. STATS BAR
html = html.replace('>47.200<', '>46.993<')
html = html.replace('+649 (+1,39%)', '+47 (+0,10%)')
html = html.replace('>6.697<', '>6.716<')
html = html.replace('+65 (+0,97%)', '+17 (+0,25%)')
html = html.replace('>44.086<', '>44.347<')
html = html.replace('-225 (-0,51%)', '+44 (+0,10%)')
# Fix MIB from negative to positive
html = html.replace('<div class="text-xs negative">-225 (-0,51%)</div>', '<div class="text-xs positive">+44 (+0,10%)</div>')
# Also handle already-replaced text
html = html.replace('<div class="text-xs negative">+44 (+0,10%)</div>', '<div class="text-xs positive">+44 (+0,10%)</div>')
html = html.replace('>$94,93<', '>$96,00<')
html = html.replace('-3,83%', '+1,13%')
# Fix WTI from negative to positive in stats
html = html.replace('<div class="text-xs negative">+1,13%</div>', '<div class="text-xs positive">+1,13%</div>', 1)
html = html.replace('>$5.020<', '>$5.020<')  # gold roughly same
html = html.replace('-0,40%', '+0,28%')
html = html.replace('<div class="text-xs negative">+0,28%</div>', '<div class="text-xs positive">+0,28%</div>', 1)
html = html.replace('>$73.882<', '>$73.717<')
html = html.replace('+4,00%', '-0,22%')
html = html.replace('<div class="text-xs positive">-0,22%</div>', '<div class="text-xs negative">-0,22%</div>', 1)

# 4. HERO — replace entirely
old_hero = '''<div class="hero-box bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 mb-10">
            <div class="grid md:grid-cols-3">
                <div class="md:col-span-2 p-8 md:p-12">
                    <div class="flex items-center gap-3 mb-4">
                        <div class="dot bg-emerald-500 animate-pulse"></div>
                        <span class="text-xs font-bold text-emerald-600 dark:text-emerald-400 uppercase tracking-wider">Breaking · 16 Mar 2026</span>
                    </div>
                    <h1 class="text-3xl md:text-4xl font-black text-gray-900 dark:text-white mb-4 leading-tight montserrat-font">
                        Wall Street rimbalza: Nvidia GTC infiamma il tech, Meta +3% su maxi-licenziamenti per l'AI
                    </h1>
                    <div class="accent-line mb-4"></div>
                    <p class="text-gray-500 dark:text-slate-400 text-lg leading-relaxed mb-6">
                        S&P 500 +0,97% a 6.697, Dow +649 punti, Nasdaq +1,27%. Nvidia +2,23% al GTC 2026: in arrivo il chip Feynman. Meta +2,89%: taglierà il 20% della forza lavoro per finanziare l'AI. WTI crolla -3,83% a $94,93 su riapertura parziale Hormuz.
                    </p>
                    <a href="articolo-wall-street-16mar-rimbalzo-nvidia-gtc-meta-layoffs.html" class="inline-flex items-center text-teal-600 dark:text-teal-400 font-semibold text-sm hover:text-teal-700 dark:hover:text-teal-300 transition group">
                        Leggi l'articolo completo
                        <svg class="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                    </a>
                </div>
                <div class="flex items-center justify-center p-8 bg-gray-50 dark:bg-[#0a0f19]/50 border-l border-gray-100 dark:border-slate-700/20">
                    <div class="text-center">
                        <div class="text-5xl font-black text-gray-900 dark:text-white mb-1">+0,97%</div>
                        <div class="text-sm text-gray-500 dark:text-slate-500 mb-3">S&P 500 — Rimbalzo</div>
                        <div class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-emerald-50 dark:bg-emerald-500/15 text-emerald-600 dark:text-emerald-400">Nvidia GTC · Meta layoffs</div>
                        <div class="mt-4 space-y-1 text-xs text-gray-400 dark:text-slate-600">
                            <div>Dow +649 · Nasdaq +1,27%</div>
                            <div>WTI $94,93 · BTC $73.882</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>'''

new_hero = '''<div class="hero-box bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 mb-10">
            <div class="grid md:grid-cols-3">
                <div class="md:col-span-2 p-8 md:p-12">
                    <div class="flex items-center gap-3 mb-4">
                        <div class="dot bg-red-500 animate-pulse"></div>
                        <span class="text-xs font-bold text-red-600 dark:text-red-400 uppercase tracking-wider">Breaking · 17 Mar 2026</span>
                    </div>
                    <h1 class="text-3xl md:text-4xl font-black text-gray-900 dark:text-white mb-4 leading-tight montserrat-font">
                        Hormuz sotto attacco: Iran colpisce UAE, Amplifon crolla -14%. FOMC domani
                    </h1>
                    <div class="accent-line mb-4"></div>
                    <p class="text-gray-500 dark:text-slate-400 text-lg leading-relaxed mb-6">
                        S&P 500 +0,25% a 6.716 in attesa della Fed. Iran attacca infrastrutture energetiche UAE: Shah gas field in fiamme. Amplifon -13,57% su acquisizione GN Hearing €2,3 miliardi. Nvidia GTC: ordini da $1 trilione. Bitcoin tocca $76.000 e ritraccia. FOMC mercoledì 18 marzo.
                    </p>
                    <a href="articolo-hormuz-17mar-iran-petrolio-crisi-stretto.html" class="inline-flex items-center text-teal-600 dark:text-teal-400 font-semibold text-sm hover:text-teal-700 dark:hover:text-teal-300 transition group">
                        Leggi l'articolo completo
                        <svg class="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                    </a>
                </div>
                <div class="flex items-center justify-center p-8 bg-gray-50 dark:bg-[#0a0f19]/50 border-l border-gray-100 dark:border-slate-700/20">
                    <div class="text-center">
                        <div class="text-5xl font-black text-red-600 dark:text-red-400 mb-1">Hormuz</div>
                        <div class="text-sm text-gray-500 dark:text-slate-500 mb-3">Crisi Stretto — Terza settimana</div>
                        <div class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-red-50 dark:bg-red-500/15 text-red-600 dark:text-red-400">Iran colpisce UAE · WTI $96</div>
                        <div class="mt-4 space-y-1 text-xs text-gray-400 dark:text-slate-600">
                            <div>S&P +0,25% · FOMC domani</div>
                            <div>Amplifon -14% · BTC $73.717</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>'''

html = html.replace(old_hero, new_hero)

# 5. SECTION HEADER
html = html.replace('Oggi, 16 Marzo', 'Oggi, 17 Marzo')

# 6. ADD 6 NEW CARDS before the 16 March articles
new_cards = '''
            <!-- ====== ARTICOLI 17 MARZO 2026 ====== -->

            <!-- Wall Street 17 mar -->
            <a href="articolo-wall-street-17mar-sp500-nasdaq-fed-hormuz.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-blue-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-blue-50 dark:bg-blue-500/15 text-blue-700 dark:text-blue-400 border border-transparent dark:border-blue-500/20">Wall Street</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Wall Street sale con cautela: S&P +0,25%, Nasdaq +0,47%. FOMC domani, Hormuz pesa</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Dow +47 a 46.993, seconda seduta consecutiva in rialzo. Mercati attendono FOMC 18 marzo. Qualcomm +3,4% su $20B buyback. Lululemon -8% AH.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">17 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- FTSE MIB 17 mar -->
            <a href="articolo-ftse-mib-17mar-amplifon-crolla-gn-hearing-banche.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-emerald-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-green-50 dark:bg-emerald-500/15 text-green-700 dark:text-emerald-400 border border-transparent dark:border-emerald-500/20">Piazza Affari</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Amplifon crolla -13,57% su acquisizione GN Hearing. FTSE MIB +0,10% a 44.347</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Deal da €2,3 miliardi scuote il settore. MFE -7,78%, Nexi -6,30%. STM +2,66% su Nvidia GTC. Banca Generali +1,14%.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">17 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Hormuz 17 mar -->
            <a href="articolo-hormuz-17mar-iran-petrolio-crisi-stretto.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-red-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-red-50 dark:bg-red-500/15 text-red-700 dark:text-red-400 border border-transparent dark:border-red-500/20">Geopolitica</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Stretto di Hormuz: la crisi che tiene in scacco il petrolio mondiale. WTI a $96</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Traffico -90%, 21 attacchi a navi. Iran colpisce UAE: Shah gas field in fiamme. Pipeline alternative al limite. IEA rilascia riserve.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">17 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Nvidia GTC 17 mar -->
            <a href="articolo-nvidia-17mar-gtc-vera-rubin-trilione-ordini.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-purple-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-purple-50 dark:bg-purple-500/15 text-purple-700 dark:text-purple-400 border border-transparent dark:border-purple-500/20">Tech/AI</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Nvidia GTC 2026: Jensen Huang vede $1 trilione di ordini. Vera Rubin e il futuro dell'AI</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Piattaforma Vera Rubin, DLSS 5, partnership Groq (35x tokens/watt), Uber autonoma in 28 città. 110 robot e 1M GPU deployate.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">17 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Lululemon 17 mar -->
            <a href="articolo-lululemon-17mar-earnings-guidance-debole-proxy-battle.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-sky-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-sky-50 dark:bg-sky-500/15 text-sky-700 dark:text-sky-400 border border-transparent dark:border-sky-500/20">Corporate</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Lululemon crolla -8%: guidance 2026 delude, proxy battle con il fondatore. -52% in un anno</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Q4 batte le stime ma outlook debole. Americas in calo, margine lordo -550bps. CEO dimissionario, P/E da 40x a 12x.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">17 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- S&P e guerre 17 mar -->
            <a href="articolo-spx-17mar-borse-guerre-pearl-harbor-storia.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-red-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-red-50 dark:bg-red-500/15 text-red-700 dark:text-red-400 border border-transparent dark:border-red-500/20">Analisi storica</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Borse e guerre: da Pearl Harbor alla crisi Iran. Come si comporta l'S&P 500?</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">In 20 conflitti post-WWII, l'S&P cala in media -6% e recupera in 28 giorni. Pearl Harbor: -20% poi +87%. Golfo: -17% poi +24%.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">17 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Day separator 16 Marzo -->
            <div class="col-span-full flex items-center gap-3 mt-6 mb-2">
                <div class="w-10 h-0.5 rounded-full bg-gray-200 dark:bg-slate-700/40"></div>
                <h2 class="text-sm font-bold montserrat-font text-gray-400 dark:text-slate-600 uppercase tracking-wider">16 Marzo 2026</h2>
                <div class="flex-1 h-0.5 rounded-full bg-gray-100 dark:bg-slate-800/20"></div>
            </div>

'''

html = html.replace('<!-- ====== ARTICOLI 16 MARZO 2026 ======', new_cards + '<!-- ====== ARTICOLI 16 MARZO 2026 ======')

with open('index.html', 'w') as f:
    f.write(html)
print('✅ index.html aggiornato')

# ========== SITEMAP.XML ==========
with open('sitemap.xml', 'r') as f:
    sitemap = f.read()

# Update homepage lastmod
sitemap = sitemap.replace('<lastmod>2026-03-16</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>1.0</priority>', '<lastmod>2026-03-17</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>1.0</priority>')

new_sitemap_entries = '''
  <!-- Articoli 17 Marzo 2026 -->
  <url>
      <loc>https://www.almafinanza.com/articolo-wall-street-17mar-sp500-nasdaq-fed-hormuz.html</loc>
      <lastmod>2026-03-17</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-17</news:publication_date>
          <news:title>Wall Street sale: S&amp;P +0,25%, Nasdaq +0,47%, FOMC domani, Hormuz pesa</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-ftse-mib-17mar-amplifon-crolla-gn-hearing-banche.html</loc>
      <lastmod>2026-03-17</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-17</news:publication_date>
          <news:title>Amplifon crolla -13,57% su acquisizione GN Hearing. FTSE MIB +0,10%</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-hormuz-17mar-iran-petrolio-crisi-stretto.html</loc>
      <lastmod>2026-03-17</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-17</news:publication_date>
          <news:title>Stretto di Hormuz: la crisi petrolifera che tiene in scacco i mercati globali</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-nvidia-17mar-gtc-vera-rubin-trilione-ordini.html</loc>
      <lastmod>2026-03-17</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-17</news:publication_date>
          <news:title>Nvidia GTC 2026: Jensen Huang vede $1 trilione di ordini, Vera Rubin e futuro AI</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-lululemon-17mar-earnings-guidance-debole-proxy-battle.html</loc>
      <lastmod>2026-03-17</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-17</news:publication_date>
          <news:title>Lululemon crolla: guidance 2026 delude, proxy battle con il fondatore</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-spx-17mar-borse-guerre-pearl-harbor-storia.html</loc>
      <lastmod>2026-03-17</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-17</news:publication_date>
          <news:title>Borse e guerre: da Pearl Harbor alla crisi Iran. Come si comporta l&apos;S&amp;P 500?</news:title>
      </news:news>
  </url>

'''

sitemap = sitemap.replace('<!-- Articoli 16 Marzo 2026 -->', new_sitemap_entries + '  <!-- Articoli 16 Marzo 2026 -->')

with open('sitemap.xml', 'w') as f:
    f.write(sitemap)
print('✅ sitemap.xml aggiornato')

# ========== CATEGORIA-WALL-STREET.HTML ==========
with open('categoria-wall-street.html', 'r') as f:
    cat_ws = f.read()

new_ws_section = '''<section class="mb-12">
            <div class="flex items-center mb-6">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Martedì, 17 Marzo 2026</h2>
                <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
            </div>
            <div class="grid md:grid-cols-3 gap-6">
                <a href="articolo-wall-street-17mar-sp500-nasdaq-fed-hormuz.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#dbeafe;color:#1e40af;">Wall Street</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Wall Street sale: S&P +0,25%, FOMC domani</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Dow +47, Nasdaq +0,47%. Qualcomm $20B buyback. Lululemon -8% AH. Mercati attendono Fed.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 17 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>
                <a href="articolo-hormuz-17mar-iran-petrolio-crisi-stretto.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#fee2e2;color:#991b1b;">Geopolitica</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Hormuz: Iran colpisce UAE, crisi petrolio terza settimana</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Traffico -90%, WTI $96. Shah gas field in fiamme. Pipeline alternative al limite. Riserve IEA rilasciate.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 17 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>
                <a href="articolo-nvidia-17mar-gtc-vera-rubin-trilione-ordini.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#f3e8ff;color:#6b21a8;">Tech/AI</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Nvidia GTC: $1 trilione ordini, Vera Rubin, futuro AI</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Jensen Huang keynote: piattaforma Vera Rubin, DLSS 5, Groq 35x, Uber autonoma 28 città, 1M GPU deployate.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 17 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>
                <a href="articolo-lululemon-17mar-earnings-guidance-debole-proxy-battle.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#e0f2fe;color:#075985;">Corporate</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Lululemon -8%: guidance debole, proxy battle, -52% YoY</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Q4 beats ma outlook delude. Americas in calo, margine -550bps per dazi. CEO dimissionario, P/E da 40x a 12x.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 17 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>
                <a href="articolo-spx-17mar-borse-guerre-pearl-harbor-storia.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#fee2e2;color:#991b1b;">Analisi storica</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Borse e guerre: da Pearl Harbor alla crisi Iran 2026</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">S&P cala -6% in media durante le guerre e recupera in 28 giorni. Pearl Harbor +87%, Golfo +24%. Cosa dice la storia.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 17 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>
            </div>
        </section>

        '''

# Find insertion point — before the first section
insertion_marker = cat_ws.find('<section class="mb-12">')
if insertion_marker > 0:
    # find the content area
    content_area = cat_ws.find('<!-- Articoli -->')
    if content_area > 0:
        cat_ws = cat_ws[:content_area] + '<!-- Articoli -->\n        ' + new_ws_section + cat_ws[content_area + len('<!-- Articoli -->'):]
    else:
        cat_ws = cat_ws[:insertion_marker] + new_ws_section + cat_ws[insertion_marker:]

with open('categoria-wall-street.html', 'w') as f:
    f.write(cat_ws)
print('✅ categoria-wall-street.html aggiornato')

# ========== CATEGORIA-BORSA-MILANO.HTML ==========
with open('categoria-borsa-milano.html', 'r') as f:
    cat_mi = f.read()

new_mi_section = '''<section class="mb-12">
            <div class="flex items-center mb-6">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Martedì, 17 Marzo 2026</h2>
                <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
            </div>
            <div class="grid md:grid-cols-3 gap-6">
                <a href="articolo-ftse-mib-17mar-amplifon-crolla-gn-hearing-banche.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#dcfce7;color:#166534;">Piazza Affari</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Amplifon -13,57%: acquisizione GN Hearing scuote il FTSE MIB</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">FTSE MIB +0,10% a 44.347. Deal da €2,3 miliardi. STM +2,66%, Banca Generali +1,14%. MFE -7,78%.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 17 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>
            </div>
        </section>

        '''

insertion_marker_mi = cat_mi.find('<section class="mb-12">')
if insertion_marker_mi > 0:
    content_area_mi = cat_mi.find('<!-- Articoli -->')
    if content_area_mi > 0:
        cat_mi = cat_mi[:content_area_mi] + '<!-- Articoli -->\n        ' + new_mi_section + cat_mi[content_area_mi + len('<!-- Articoli -->'):]
    else:
        cat_mi = cat_mi[:insertion_marker_mi] + new_mi_section + cat_mi[insertion_marker_mi:]

with open('categoria-borsa-milano.html', 'w') as f:
    f.write(cat_mi)
print('✅ categoria-borsa-milano.html aggiornato')

# ========== IMPARA-FINANZA.HTML ==========
with open('impara-finanza.html', 'r') as f:
    impara = f.read()

# Add concept cards to appropriate sections
# 1. FOMC e dot plot → Macroeconomia e Banche Centrali
# 2. Buyback azionario → Meccanismi di Mercato
# 3. Integrazione verticale → Modelli di Business
# 4. Spread BTP-Bund → (already exists, skip)
# 5. Collo di bottiglia energetico → Energia & Infrastrutture
# 6. Riserve petrolifere strategiche → Energia & Infrastrutture
# 7. Legge di scaling AI → Metriche Settoriali
# 8. Guida autonoma Level 4 → Settori e Aziende Specifiche
# 9. Proxy battle → Meccanismi di Mercato
# 10. Da growth a value → Valutazioni e Multipli
# 11. Buy the dip bellico → Gestione del Rischio
# 12. Effetto Hormuz vs Kuwait → Geopolitica e Mercati

concepts = {
    'Macroeconomia e Banche Centrali': [
        '''<a href="articolo-wall-street-17mar-sp500-nasdaq-fed-hormuz.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-cyan-500 hover:border-cyan-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">FOMC e Dot Plot</h3>
                    <p class="text-sm text-gray-600 dark:text-slate-400">Ogni trimestre la Fed pubblica le proiezioni dei suoi membri sui tassi. I "dots" mostrano dove ogni membro vede il tasso a fine anno, guidando le aspettative del mercato.</p>
                    <span class="text-xs text-cyan-600 dark:text-cyan-400 font-semibold mt-2 inline-block">→ Spiegato in: Wall Street 17 marzo — FOMC</span>
                </a>''',
    ],
    'Meccanismi di Mercato': [
        '''<a href="articolo-wall-street-17mar-sp500-nasdaq-fed-hormuz.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-purple-500 hover:border-purple-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Buyback azionario</h3>
                    <p class="text-sm text-gray-600 dark:text-slate-400">Il riacquisto di azioni proprie riduce le azioni in circolazione, aumentando l'EPS. Qualcomm ha annunciato $20 miliardi in buyback a marzo 2026.</p>
                    <span class="text-xs text-purple-600 dark:text-purple-400 font-semibold mt-2 inline-block">→ Spiegato in: Wall Street 17 marzo — Qualcomm</span>
                </a>''',
        '''<a href="articolo-lululemon-17mar-earnings-guidance-debole-proxy-battle.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-purple-500 hover:border-purple-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Proxy Battle (battaglia per delega)</h3>
                    <p class="text-sm text-gray-600 dark:text-slate-400">Quando un azionista importante raccoglie deleghe di voto per influenzare le decisioni aziendali. Il fondatore di Lululemon sfida il management attuale.</p>
                    <span class="text-xs text-purple-600 dark:text-purple-400 font-semibold mt-2 inline-block">→ Spiegato in: Lululemon — Proxy battle</span>
                </a>''',
    ],
    'Modelli di Business': [
        '''<a href="articolo-ftse-mib-17mar-amplifon-crolla-gn-hearing-banche.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-teal-500 hover:border-teal-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Integrazione verticale</h3>
                    <p class="text-sm text-gray-600 dark:text-slate-400">Quando un'azienda acquisisce un fornitore o produttore a monte. Amplifon, da distributore, diventa anche produttore acquisendo GN Hearing per €2,3 miliardi.</p>
                    <span class="text-xs text-teal-600 dark:text-teal-400 font-semibold mt-2 inline-block">→ Spiegato in: FTSE MIB 17 marzo — Amplifon</span>
                </a>''',
    ],
    'Energia &amp; Infrastrutture': [
        '''<a href="articolo-hormuz-17mar-iran-petrolio-crisi-stretto.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-orange-500 hover:border-orange-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Collo di bottiglia energetico (Hormuz)</h3>
                    <p class="text-sm text-gray-600 dark:text-slate-400">Lo Stretto di Hormuz è largo 33 km e da qui transita il 20% del petrolio mondiale. Una chiusura parziale provoca shock nei prezzi dell'energia globali.</p>
                    <span class="text-xs text-orange-600 dark:text-orange-400 font-semibold mt-2 inline-block">→ Spiegato in: Crisi Hormuz 17 marzo</span>
                </a>''',
        '''<a href="articolo-hormuz-17mar-iran-petrolio-crisi-stretto.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-orange-500 hover:border-orange-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Riserve petrolifere strategiche (SPR)</h3>
                    <p class="text-sm text-gray-600 dark:text-slate-400">Scorte di petrolio accumulate dai governi per emergenze. L'IEA coordina il rilascio. Gli USA hanno circa 370 milioni di barili. Strumento per calmierare i prezzi durante shock di offerta.</p>
                    <span class="text-xs text-orange-600 dark:text-orange-400 font-semibold mt-2 inline-block">→ Spiegato in: Crisi Hormuz 17 marzo</span>
                </a>''',
    ],
    'Valutazioni e Multipli': [
        '''<a href="articolo-lululemon-17mar-earnings-guidance-debole-proxy-battle.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-blue-500 hover:border-blue-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Da Growth a Value Stock</h3>
                    <p class="text-sm text-gray-600 dark:text-slate-400">Quando la crescita rallenta, il mercato rivaluta il titolo. Lululemon è passata da P/E 40x (growth) a 12-15x (value): il mercato non crede più nella narrativa di crescita.</p>
                    <span class="text-xs text-blue-600 dark:text-blue-400 font-semibold mt-2 inline-block">→ Spiegato in: Lululemon — De-rating</span>
                </a>''',
    ],
    'Metriche Settoriali': [
        '''<a href="articolo-nvidia-17mar-gtc-vera-rubin-trilione-ordini.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-amber-500 hover:border-amber-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Legge di scaling dell'AI</h3>
                    <p class="text-sm text-gray-600 dark:text-slate-400">Modelli AI più grandi richiedono hardware più potente. Ogni generazione GPU (Hopper → Blackwell → Vera Rubin) offre prestazioni esponenziali. Da miliardi a trilioni di ordini.</p>
                    <span class="text-xs text-amber-600 dark:text-amber-400 font-semibold mt-2 inline-block">→ Spiegato in: Nvidia GTC 2026</span>
                </a>''',
    ],
    'Settori e Aziende Specifiche': [
        '''<a href="articolo-nvidia-17mar-gtc-vera-rubin-trilione-ordini.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-rose-500 hover:border-rose-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Guida autonoma Level 4</h3>
                    <p class="text-sm text-gray-600 dark:text-slate-400">Il Level 4 significa che il veicolo si guida da solo in determinate condizioni. La partnership Nvidia-Uber per 28 città entro 2028 segna il passaggio al deployment commerciale di massa.</p>
                    <span class="text-xs text-rose-600 dark:text-rose-400 font-semibold mt-2 inline-block">→ Spiegato in: Nvidia GTC — Uber</span>
                </a>''',
    ],
    'Gestione del Rischio': [
        '''<a href="articolo-spx-17mar-borse-guerre-pearl-harbor-storia.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-red-500 hover:border-red-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Buy the dip bellico</h3>
                    <p class="text-sm text-gray-600 dark:text-slate-400">In 19 conflitti su 20 post-WWII, l'S&P 500 ha recuperato il calo iniziale in media in 28 giorni. Attenzione: performance passata non è garanzia di risultati futuri.</p>
                    <span class="text-xs text-red-600 dark:text-red-400 font-semibold mt-2 inline-block">→ Spiegato in: Borse e guerre — Analisi storica</span>
                </a>''',
    ],
    'Geopolitica e Mercati': [
        '''<a href="articolo-spx-17mar-borse-guerre-pearl-harbor-storia.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-rose-500 hover:border-rose-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Effetto Hormuz vs Effetto Kuwait</h3>
                    <p class="text-sm text-gray-600 dark:text-slate-400">La Guerra del Golfo 1990 è il precedente più rilevante per Iran 2026: entrambe coinvolgono Medio Oriente, petrolio e shock di offerta. Nel 1990 l'S&P perse -17% ma recuperò +24%.</p>
                    <span class="text-xs text-rose-600 dark:text-rose-400 font-semibold mt-2 inline-block">→ Spiegato in: Borse e guerre — Confronto storico</span>
                </a>''',
    ],
}

for section_name, cards in concepts.items():
    for card in cards:
        # Find the section and its grid
        section_idx = impara.find(section_name)
        if section_idx > 0:
            # Find the closing </div> of the grid after this section
            grid_start = impara.find('grid md:grid-cols', section_idx)
            if grid_start > 0:
                # Find the end of this grid's content (next </div>\n        </section>)
                section_end = impara.find('</section>', grid_start)
                grid_end = impara.rfind('</div>', grid_start, section_end)
                if grid_end > 0:
                    impara = impara[:grid_end] + '\n                ' + card + '\n            ' + impara[grid_end:]

with open('impara-finanza.html', 'w') as f:
    f.write(impara)
print('✅ impara-finanza.html aggiornato')

print('\n🎉 AGGIORNAMENTO 17 MARZO 2026 COMPLETATO!')
print('File aggiornati: index.html, sitemap.xml, categoria-wall-street.html, categoria-borsa-milano.html, impara-finanza.html')
