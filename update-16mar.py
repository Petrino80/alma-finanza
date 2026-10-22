#!/usr/bin/env python3
"""Aggiornamento 16 Marzo 2026 — Homepage, sitemap, categorie, impara la finanza"""
import re

# ============================================================
# 1) HOMEPAGE — index.html
# ============================================================
with open('index.html', 'r') as f:
    html = f.read()

# --- TICKER ---
old_ticker_start = '<div class="ticker-item" data-ticker="dow">'
new_ticker_block = '''<div class="ticker-item" data-ticker="dow"><a href="https://finance.yahoo.com/quote/%5EDJI" target="_blank">🇺🇸 Dow <span class="positive">47.200 (+1,39%)</span></a></div>
            <div class="ticker-item" data-ticker="sp500"><a href="https://finance.yahoo.com/quote/%5EGSPC" target="_blank">🇺🇸 S&P 500 <span class="positive">6.697 (+0,97%)</span></a></div>
            <div class="ticker-item" data-ticker="nasdaq"><a href="https://finance.yahoo.com/quote/%5EIXIC" target="_blank">🇺🇸 Nasdaq <span class="positive">22.387 (+1,27%)</span></a></div>
            <div class="ticker-item" data-ticker="ftsemib"><a href="https://finance.yahoo.com/quote/FTSEMIB.MI" target="_blank">🇮🇹 FTSE MIB <span class="negative">44.086 (-0,51%)</span></a></div>
            <div class="ticker-item" data-ticker="nvidia"><a href="articolo-wall-street-16mar-rimbalzo-nvidia-gtc-meta-layoffs.html">🚀 <span class="positive">Nvidia +2,23%: GTC 2026, chip Feynman</span></a></div>
            <div class="ticker-item" data-ticker="meta"><a href="articolo-meta-16mar-licenziamenti-20-percento-ai-costi.html">📉 <span class="positive">Meta +2,89%: licenzia 20% per AI</span></a></div>
            <div class="ticker-item" data-ticker="intel"><a href="https://finance.yahoo.com/quote/INTC" target="_blank">💻 <span class="positive">Intel +6,29%</span></a></div>
            <div class="ticker-item" data-ticker="dax"><a href="https://finance.yahoo.com/quote/%5EGDAXI" target="_blank">🇩🇪 DAX <span class="positive">+0,39%</span></a></div>
            <div class="ticker-item" data-ticker="oil"><a href="https://finance.yahoo.com/quote/CL%3DF" target="_blank">🛢️ WTI <span class="negative">$94,93 (-3,83%)</span></a></div>
            <div class="ticker-item" data-ticker="gold"><a href="https://finance.yahoo.com/quote/GC%3DF" target="_blank">🥇 Oro <span class="negative">$5.020 (-0,40%)</span></a></div>
            <div class="ticker-item" data-ticker="btc"><a href="https://finance.yahoo.com/quote/BTC-USD" target="_blank">₿ <span class="positive">Bitcoin $73.882 (+4%)</span></a></div>
            <div class="ticker-item" data-ticker="fed"><a href="articolo-wall-street-16mar-rimbalzo-nvidia-gtc-meta-layoffs.html">🏛️ <span class="negative">Fed FOMC mercoledì 18 marzo</span></a></div>
            <!-- Duplicate for seamless loop -->
            <div class="ticker-item" data-ticker="dow"><a href="https://finance.yahoo.com/quote/%5EDJI" target="_blank">🇺🇸 Dow <span class="positive">47.200 (+1,39%)</span></a></div>
            <div class="ticker-item" data-ticker="sp500"><a href="https://finance.yahoo.com/quote/%5EGSPC" target="_blank">🇺🇸 S&P 500 <span class="positive">6.697 (+0,97%)</span></a></div>
            <div class="ticker-item" data-ticker="nasdaq"><a href="https://finance.yahoo.com/quote/%5EIXIC" target="_blank">🇺🇸 Nasdaq <span class="positive">22.387 (+1,27%)</span></a></div>
            <div class="ticker-item" data-ticker="ftsemib"><a href="https://finance.yahoo.com/quote/FTSEMIB.MI" target="_blank">🇮🇹 FTSE MIB <span class="negative">44.086 (-0,51%)</span></a></div>
            <div class="ticker-item" data-ticker="nvidia"><a href="articolo-wall-street-16mar-rimbalzo-nvidia-gtc-meta-layoffs.html">🚀 <span class="positive">Nvidia +2,23%: GTC 2026, chip Feynman</span></a></div>
            <div class="ticker-item" data-ticker="meta"><a href="articolo-meta-16mar-licenziamenti-20-percento-ai-costi.html">📉 <span class="positive">Meta +2,89%: licenzia 20% per AI</span></a></div>
            <div class="ticker-item" data-ticker="intel"><a href="https://finance.yahoo.com/quote/INTC" target="_blank">💻 <span class="positive">Intel +6,29%</span></a></div>
            <div class="ticker-item" data-ticker="dax"><a href="https://finance.yahoo.com/quote/%5EGDAXI" target="_blank">🇩🇪 DAX <span class="positive">+0,39%</span></a></div>
            <div class="ticker-item" data-ticker="oil"><a href="https://finance.yahoo.com/quote/CL%3DF" target="_blank">🛢️ WTI <span class="negative">$94,93 (-3,83%)</span></a></div>
            <div class="ticker-item" data-ticker="gold"><a href="https://finance.yahoo.com/quote/GC%3DF" target="_blank">🥇 Oro <span class="negative">$5.020 (-0,40%)</span></a></div>
            <div class="ticker-item" data-ticker="btc"><a href="https://finance.yahoo.com/quote/BTC-USD" target="_blank">₿ <span class="positive">Bitcoin $73.882 (+4%)</span></a></div>
            <div class="ticker-item" data-ticker="fed"><a href="articolo-wall-street-16mar-rimbalzo-nvidia-gtc-meta-layoffs.html">🏛️ <span class="negative">Fed FOMC mercoledì 18 marzo</span></a></div>'''

# Replace ticker content
ticker_pattern = r'<div class="ticker-item" data-ticker="dow">.*?</div>\s*</div>'
# Simpler: replace between ticker-content and closing
old_ticker = html[html.index('<div class="ticker-item" data-ticker="dow">'):html.index('</div></div>\n    </div>\n\n    <!-- Header -->')]
html = html.replace(old_ticker, new_ticker_block + '\n        ')

# --- DATE in header ---
html = html.replace('Sabato 14 Marzo 2026', 'Lunedì 16 Marzo 2026')

# --- STATS BAR ---
# Dow
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">46.678</div>\n                <div class="text-xs negative">-739 (-1,56%)</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">47.200</div>\n                <div class="text-xs positive">+649 (+1,39%)</div>'
)
# S&P
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">6.673</div>\n                <div class="text-xs negative">-102 (-1,50%)</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">6.697</div>\n                <div class="text-xs positive">+65 (+0,97%)</div>'
)
# MIB
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">44.460</div>\n                <div class="text-xs negative">-0,70%</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">44.086</div>\n                <div class="text-xs negative">-225 (-0,51%)</div>'
)
# WTI
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$96</div>\n                <div class="text-xs positive">+9,72%</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$94,93</div>\n                <div class="text-xs negative">-3,83%</div>'
)
# Oro
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$5.156</div>\n                <div class="text-xs negative">-0,39%</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$5.020</div>\n                <div class="text-xs negative">-0,40%</div>'
)
# Bitcoin
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$69.688</div>\n                <div class="text-xs negative">-0,4%</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$73.882</div>\n                <div class="text-xs positive">+4,00%</div>'
)

# --- HERO ---
old_hero = '''<div class="hero-box bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 mb-10">
            <div class="grid md:grid-cols-3">
                <div class="md:col-span-2 p-8 md:p-12">
                    <div class="flex items-center gap-3 mb-4">
                        <div class="dot bg-red-500 animate-pulse"></div>
                        <span class="text-xs font-bold text-red-600 dark:text-red-400 uppercase tracking-wider">Breaking · 14 Mar 2026</span>
                    </div>
                    <h1 class="text-3xl md:text-4xl font-black text-gray-900 dark:text-white mb-4 leading-tight montserrat-font">
                        Adobe crolla -8,85%: il CEO si dimette dopo 18 anni e l\'AI cannibalizza il business
                    </h1>
                    <div class="accent-line mb-4"></div>
                    <p class="text-gray-500 dark:text-slate-400 text-lg leading-relaxed mb-6">
                        Shantanu Narayen lascia dopo 18 anni. Q1 record ($6,4B) ma Net New ARR miss: $70M persi per clienti che generano immagini con AI. Wall Street chiude la quarta seduta in calo, terza settimana rossa. S&P e Dow ai minimi da novembre.
                    </p>
                    <a href="articolo-adobe-13mar-ceo-narayen-dimissioni-ai-cannibalizza-arr.html" class="inline-flex items-center text-teal-600 dark:text-teal-400 font-semibold text-sm hover:text-teal-700 dark:hover:text-teal-300 transition group">
                        Leggi l\'articolo completo
                        <svg class="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                    </a>
                </div>
                <div class="flex items-center justify-center p-8 bg-gray-50 dark:bg-[#0a0f19]/50 border-l border-gray-100 dark:border-slate-700/20">
                    <div class="text-center">
                        <div class="text-5xl font-black text-gray-900 dark:text-white mb-1">-8,85%</div>
                        <div class="text-sm text-gray-500 dark:text-slate-500 mb-3">Adobe (ADBE)</div>
                        <div class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-red-50 dark:bg-red-500/15 text-red-600 dark:text-red-400">CEO dimissioni · ARR miss</div>
                        <div class="mt-4 space-y-1 text-xs text-gray-400 dark:text-slate-600">
                            <div>S&P -0,61% · Nasdaq -0,93%</div>
                            <div>BTC $73.300 · Michigan 55,5</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </div>'''

new_hero = '''<div class="hero-box bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 mb-10">
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
        </div>
        </div>'''

html = html.replace(old_hero, new_hero)

# --- SECTION HEADER ---
html = html.replace('Oggi, 14 Marzo', 'Oggi, 16 Marzo')

# --- NEW CARDS (insert before the 14 March cards) ---
new_cards = '''
            <!-- ====== ARTICOLI 16 MARZO 2026 ====== -->

            <!-- Wall Street 16 mar -->
            <a href="articolo-wall-street-16mar-rimbalzo-nvidia-gtc-meta-layoffs.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-blue-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-blue-50 dark:bg-blue-500/15 text-blue-700 dark:text-blue-400 border border-transparent dark:border-blue-500/20">Wall Street</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Wall Street rimbalza: Nvidia GTC infiamma i chip, Meta +3% sui maxi-licenziamenti AI</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">S&P 500 +0,97% a 6.697, Dow +649. Nvidia +2,23% al GTC: chip Feynman. Intel +6,29%, Micron +6,20%. WTI -3,83% su riapertura Hormuz.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">16 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- FTSE MIB 16 mar -->
            <a href="articolo-ftse-mib-16mar-amplifon-stm-banche-centrali.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-emerald-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-green-50 dark:bg-emerald-500/15 text-green-700 dark:text-emerald-400 border border-transparent dark:border-emerald-500/20">Piazza Affari</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">FTSE MIB debole (-0,51%): Amplifon affonda, STM +2,5% grazie a Nvidia GTC</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Milano a 44.086 punti. Spread BTP-Bund sotto 80 bps. Settimana delle 9 banche centrali: Fed mercoledì, BCE giovedì.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">16 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Meta 16 mar -->
            <a href="articolo-meta-16mar-licenziamenti-20-percento-ai-costi.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-purple-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-purple-50 dark:bg-purple-500/15 text-purple-700 dark:text-purple-400 border border-transparent dark:border-purple-500/20">Tech/AI</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Meta licenzia il 20% per finanziare l'AI: il titolo sale +3%. Il paradosso dell'efficienza</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">~15.000 posti a rischio su 79.000. CapEx AI $135B nel 2026, $600B entro 2028. 39 analisti su 44 dicono "buy", target $859.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">16 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- ETF Guida 16 mar -->
            <a href="articolo-etf-16mar-guida-investire-etf-italia.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-sky-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-sky-50 dark:bg-sky-500/15 text-sky-700 dark:text-sky-400 border border-transparent dark:border-sky-500/20">Formazione</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">ETF: cosa sono e come investire in Italia. La guida completa per principianti</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Diversificazione a basso costo con TER dallo 0,07%. IWDA, VWCE, CSPX: i migliori ETF. Come aprire un PAC su Fineco o DEGIRO.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">16 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Guida investire 16 mar -->
            <a href="articolo-investire-16mar-guida-principianti-borsa-italia.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-teal-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-teal-50 dark:bg-teal-500/15 text-teal-700 dark:text-teal-400 border border-transparent dark:border-teal-500/20">Formazione</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Investire in borsa: perché è un'opportunità e come cominciare in Italia da zero</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">€200 al mese per 30 anni = oltre €600.000. L'interesse composto, il regime fiscale italiano e i 5 passi per iniziare.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">16 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Day separator: 14 Marzo -->
            <div class="col-span-full flex items-center gap-3 mt-6 mb-2">
                <div class="w-10 h-0.5 rounded-full bg-gray-200 dark:bg-slate-700/40"></div>
                <h2 class="text-sm font-bold montserrat-font text-gray-400 dark:text-slate-600 uppercase tracking-wider">14 Marzo 2026</h2>
                <div class="flex-1 h-0.5 rounded-full bg-gray-100 dark:bg-slate-800/20"></div>
            </div>

'''

# Insert before the 14 March article block
html = html.replace('<!-- ====== ARTICOLI 14 MARZO 2026 ====== -->', new_cards + '            <!-- ====== ARTICOLI 14 MARZO 2026 ====== -->')

with open('index.html', 'w') as f:
    f.write(html)
print("✅ index.html aggiornato")

# ============================================================
# 2) SITEMAP — sitemap.xml
# ============================================================
with open('sitemap.xml', 'r') as f:
    sxml = f.read()

# Update homepage lastmod
sxml = sxml.replace('<lastmod>2026-03-14</lastmod>', '<lastmod>2026-03-16</lastmod>', 1)

new_sitemap_entries = '''
  <!-- Articoli 16 Marzo 2026 -->
  <url>
      <loc>https://www.almafinanza.com/articolo-wall-street-16mar-rimbalzo-nvidia-gtc-meta-layoffs.html</loc>
      <lastmod>2026-03-16</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-16</news:publication_date>
          <news:title>Wall Street rimbalza: Nvidia GTC infiamma il tech, Meta +3% sui maxi-licenziamenti AI</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-ftse-mib-16mar-amplifon-stm-banche-centrali.html</loc>
      <lastmod>2026-03-16</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-16</news:publication_date>
          <news:title>FTSE MIB debole: Amplifon affonda, STM brilla grazie a Nvidia GTC</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-meta-16mar-licenziamenti-20-percento-ai-costi.html</loc>
      <lastmod>2026-03-16</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-16</news:publication_date>
          <news:title>Meta licenzia il 20% per finanziare l&apos;AI: il titolo sale +3%</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-etf-16mar-guida-investire-etf-italia.html</loc>
      <lastmod>2026-03-16</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-16</news:publication_date>
          <news:title>ETF: cosa sono e come investire in Italia — Guida completa per principianti</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-investire-16mar-guida-principianti-borsa-italia.html</loc>
      <lastmod>2026-03-16</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-16</news:publication_date>
          <news:title>Investire in borsa: perch&eacute; &egrave; un&apos;opportunit&agrave; e come cominciare in Italia da zero</news:title>
      </news:news>
  </url>

'''

# Insert after homepage entry
sxml = sxml.replace('  <!-- Articoli 11 Marzo 2026 -->', new_sitemap_entries + '  <!-- Articoli 11 Marzo 2026 -->')

with open('sitemap.xml', 'w') as f:
    f.write(sxml)
print("✅ sitemap.xml aggiornato")

# ============================================================
# 3) CATEGORIE
# ============================================================

# --- categoria-wall-street.html ---
with open('categoria-wall-street.html', 'r') as f:
    ws = f.read()

ws_new_section = '''<section class="mb-12">
                <div class="flex items-center mb-6">
                    <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Lunedì, 16 Marzo 2026</h2>
                    <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
                </div>
                <div class="grid md:grid-cols-3 gap-6">

                    <a href="articolo-wall-street-16mar-rimbalzo-nvidia-gtc-meta-layoffs.html" class="block">
                        <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                            <span class="read-badge">Leggi</span>
                            <div class="p-6">
                                <span class="category-badge" style="background:#dbeafe;color:#1e40af;">Wall Street</span>
                                <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Wall Street rimbalza: Nvidia GTC infiamma i chip, Meta +3% sui licenziamenti AI</h2>
                                <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">S&P 500 +0,97%, Dow +649, Nasdaq +1,27%. Intel +6,29%, Micron +6,20%. WTI -3,83% su Hormuz.</p>
                                <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                    <span>📰 16 Mar 2026</span>
                                    <span class="text-teal-500 font-semibold">Leggi →</span>
                                </div>
                            </div>
                        </article>
                    </a>

                    <a href="articolo-meta-16mar-licenziamenti-20-percento-ai-costi.html" class="block">
                        <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                            <span class="read-badge">Leggi</span>
                            <div class="p-6">
                                <span class="category-badge" style="background:#f3e8ff;color:#6b21a8;">Tech/AI</span>
                                <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Meta licenzia il 20% per finanziare l'AI: il titolo sale +3%</h2>
                                <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">~15.000 posti a rischio. CapEx AI $135B nel 2026. Il paradosso dell'efficienza: meno dipendenti, più valore.</p>
                                <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                    <span>📰 16 Mar 2026</span>
                                    <span class="text-teal-500 font-semibold">Leggi →</span>
                                </div>
                            </div>
                        </article>
                    </a>

                    <a href="articolo-etf-16mar-guida-investire-etf-italia.html" class="block">
                        <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                            <span class="read-badge">Leggi</span>
                            <div class="p-6">
                                <span class="category-badge" style="background:#e0f2fe;color:#0369a1;">Formazione</span>
                                <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">ETF: cosa sono e come investire in Italia</h2>
                                <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Guida completa: diversificazione, TER, replica fisica vs sintetica, i migliori ETF e come aprire un PAC.</p>
                                <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                    <span>📰 16 Mar 2026</span>
                                    <span class="text-teal-500 font-semibold">Leggi →</span>
                                </div>
                            </div>
                        </article>
                    </a>

                    <a href="articolo-investire-16mar-guida-principianti-borsa-italia.html" class="block">
                        <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                            <span class="read-badge">Leggi</span>
                            <div class="p-6">
                                <span class="category-badge" style="background:#f0fdfa;color:#0f766e;">Formazione</span>
                                <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Investire in borsa: come cominciare in Italia da zero</h2>
                                <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Interesse composto, regime fiscale italiano, i 5 passi per iniziare. €200/mese per 30 anni = oltre €600.000.</p>
                                <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                    <span>📰 16 Mar 2026</span>
                                    <span class="text-teal-500 font-semibold">Leggi →</span>
                                </div>
                            </div>
                        </article>
                    </a>

                </div>
            </section>

            '''

# Find insertion point — first <section class="mb-12">
ws = ws.replace('<section class="mb-12">', ws_new_section + '<section class="mb-12">', 1)
with open('categoria-wall-street.html', 'w') as f:
    f.write(ws)
print("✅ categoria-wall-street.html aggiornato")

# --- categoria-borsa-milano.html ---
with open('categoria-borsa-milano.html', 'r') as f:
    bm = f.read()

bm_new_section = '''<section class="mb-12">
                <div class="flex items-center mb-6">
                    <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Lunedì, 16 Marzo 2026</h2>
                    <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
                </div>
                <div class="grid md:grid-cols-3 gap-6">

                    <a href="articolo-ftse-mib-16mar-amplifon-stm-banche-centrali.html" class="block">
                        <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                            <span class="read-badge">Leggi</span>
                            <div class="p-6">
                                <span class="category-badge" style="background:#d1fae5;color:#065f46;">Piazza Affari</span>
                                <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">FTSE MIB debole (-0,51%): Amplifon affonda, STM +2,5% grazie a Nvidia GTC</h2>
                                <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Milano a 44.086. Spread sotto 80 bps. Settimana delle 9 banche centrali: Fed e BCE in arrivo.</p>
                                <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                    <span>📰 16 Mar 2026</span>
                                    <span class="text-teal-500 font-semibold">Leggi →</span>
                                </div>
                            </div>
                        </article>
                    </a>

                </div>
            </section>

            '''

bm = bm.replace('<section class="mb-12">', bm_new_section + '<section class="mb-12">', 1)
with open('categoria-borsa-milano.html', 'w') as f:
    f.write(bm)
print("✅ categoria-borsa-milano.html aggiornato")

# --- categoria-crypto.html (no new crypto articles today, but BTC is mentioned in Wall Street article) ---
# No crypto-specific article today, skip
print("ℹ️  categoria-crypto.html: nessun articolo crypto specifico oggi")

# --- categoria-commodities.html (no new commodities article today) ---
print("ℹ️  categoria-commodities.html: nessun articolo commodities specifico oggi")

# ============================================================
# 4) IMPARA LA FINANZA — impara-finanza.html
# ============================================================
with open('impara-finanza.html', 'r') as f:
    imp = f.read()

# New concept cards from the 5 articles:
# Art 1 - Wall Street: "GTC e gli eventi catalizzatori" → ⚙️ Meccanismi di Mercato (purple)
# Art 1 - Wall Street: "Buy the Dip" → ⚙️ Meccanismi di Mercato (purple)
# Art 2 - FTSE MIB: "Lo spread BTP-Bund" → 🏦 Settore Finanziario (emerald)
# Art 2 - FTSE MIB: "Settimane delle banche centrali" → 🌍 Macroeconomia (cyan)
# Art 3 - Meta: "Paradosso licenziamenti" → ⚙️ Meccanismi di Mercato (purple)
# Art 3 - Meta: "CapEx e investimenti in AI" → 📈 Metriche Settoriali (amber)
# Art 4 - ETF: "TER" → 📈 Metriche Settoriali (amber)
# Art 4 - ETF: "Replica fisica vs sintetica" → ⚙️ Meccanismi di Mercato (purple)
# Art 5 - Investire: "Interesse composto" → 🌍 Macroeconomia (cyan)
# Art 5 - Investire: "Regime fiscale italiano" → 🌍 Macroeconomia (cyan)

# Add to Meccanismi di Mercato section
meccanismi_cards = '''
                    <a href="articolo-wall-street-16mar-rimbalzo-nvidia-gtc-meta-layoffs.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-purple-500 hover:border-purple-600">
                        <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">GTC e gli eventi catalizzatori</h3>
                        <p class="text-sm text-gray-600 dark:text-slate-400">Le conferenze tecnologiche come il GTC di Nvidia possono muovere interi settori. L'effetto "catalizzatore" amplifica la volatilità nei giorni dell'evento.</p>
                        <span class="text-xs text-purple-600 dark:text-purple-400 font-semibold mt-2 inline-block">→ Spiegato in: Wall Street rimbalza — Nvidia GTC</span>
                    </a>
                    <a href="articolo-wall-street-16mar-rimbalzo-nvidia-gtc-meta-layoffs.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-purple-500 hover:border-purple-600">
                        <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Buy the Dip: comprare sui cali</h3>
                        <p class="text-sm text-gray-600 dark:text-slate-400">Strategia che consiste nell'acquistare dopo un ribasso significativo, scommettendo sul recupero. Funziona nei mercati rialzisti di lungo termine, ma richiede disciplina.</p>
                        <span class="text-xs text-purple-600 dark:text-purple-400 font-semibold mt-2 inline-block">→ Spiegato in: Wall Street rimbalza — Buy the Dip</span>
                    </a>
                    <a href="articolo-meta-16mar-licenziamenti-20-percento-ai-costi.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-purple-500 hover:border-purple-600">
                        <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Il paradosso dei licenziamenti</h3>
                        <p class="text-sm text-gray-600 dark:text-slate-400">Perché le azioni salgono quando un'azienda annuncia licenziamenti? Il mercato premia l'efficienza operativa e il miglioramento dei margini attesi.</p>
                        <span class="text-xs text-purple-600 dark:text-purple-400 font-semibold mt-2 inline-block">→ Spiegato in: Meta licenzia il 20%</span>
                    </a>
                    <a href="articolo-etf-16mar-guida-investire-etf-italia.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-purple-500 hover:border-purple-600">
                        <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Replica fisica vs sintetica negli ETF</h3>
                        <p class="text-sm text-gray-600 dark:text-slate-400">Un ETF a replica fisica acquista i titoli dell'indice. Uno a replica sintetica usa derivati (swap) per replicare il rendimento. La replica fisica è più trasparente ma può avere costi maggiori.</p>
                        <span class="text-xs text-purple-600 dark:text-purple-400 font-semibold mt-2 inline-block">→ Spiegato in: Guida ETF Italia</span>
                    </a>'''

# Find the Meccanismi di Mercato section and add before its closing </div>
if '⚙️ Meccanismi di Mercato' in imp:
    # Find the section, add cards before the next </section> or closing grid div
    idx = imp.index('⚙️ Meccanismi di Mercato')
    # Find the closing </div> of the grid within this section
    # Look for the next </section> after this point
    section_end = imp.index('</section>', idx)
    grid_end = imp.rfind('</div>', idx, section_end)
    imp = imp[:grid_end] + meccanismi_cards + '\n                ' + imp[grid_end:]

# Add to Macroeconomia section
macro_cards = '''
                    <a href="articolo-ftse-mib-16mar-amplifon-stm-banche-centrali.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-cyan-500 hover:border-cyan-600">
                        <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Le settimane delle banche centrali</h3>
                        <p class="text-sm text-gray-600 dark:text-slate-400">Quando Fed, BCE e altre banche centrali decidono sui tassi nella stessa settimana, la volatilità aumenta. I mercati attendono le dichiarazioni per capire la direzione della politica monetaria.</p>
                        <span class="text-xs text-cyan-600 dark:text-cyan-400 font-semibold mt-2 inline-block">→ Spiegato in: FTSE MIB — Banche centrali</span>
                    </a>
                    <a href="articolo-investire-16mar-guida-principianti-borsa-italia.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-cyan-500 hover:border-cyan-600">
                        <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">L'interesse composto</h3>
                        <p class="text-sm text-gray-600 dark:text-slate-400">Einstein lo chiamò l'ottava meraviglia del mondo. Reinvestendo i rendimenti, il capitale cresce in modo esponenziale. €200/mese al 7% annuo diventano oltre €600.000 in 30 anni.</p>
                        <span class="text-xs text-cyan-600 dark:text-cyan-400 font-semibold mt-2 inline-block">→ Spiegato in: Guida investire in borsa</span>
                    </a>
                    <a href="articolo-investire-16mar-guida-principianti-borsa-italia.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-cyan-500 hover:border-cyan-600">
                        <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Il regime fiscale italiano per gli investimenti</h3>
                        <p class="text-sm text-gray-600 dark:text-slate-400">In Italia i capital gain sono tassati al 26% (12,5% per titoli di stato). Esistono due regimi: dichiarativo (il risparmiatore calcola) e amministrato (la banca fa tutto).</p>
                        <span class="text-xs text-cyan-600 dark:text-cyan-400 font-semibold mt-2 inline-block">→ Spiegato in: Guida investire in borsa</span>
                    </a>'''

if '🌍 Macroeconomia e Banche Centrali' in imp:
    idx = imp.index('🌍 Macroeconomia e Banche Centrali')
    section_end = imp.index('</section>', idx)
    grid_end = imp.rfind('</div>', idx, section_end)
    imp = imp[:grid_end] + macro_cards + '\n                ' + imp[grid_end:]

# Add to Metriche Settoriali section
metriche_cards = '''
                    <a href="articolo-meta-16mar-licenziamenti-20-percento-ai-costi.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-amber-500 hover:border-amber-600">
                        <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">CapEx e investimenti in AI</h3>
                        <p class="text-sm text-gray-600 dark:text-slate-400">Il Capital Expenditure (CapEx) è la spesa in beni strumentali. Le big tech stanno investendo centinaia di miliardi in data center AI, sacrificando profitti a breve per dominare il futuro.</p>
                        <span class="text-xs text-amber-600 dark:text-amber-400 font-semibold mt-2 inline-block">→ Spiegato in: Meta licenziamenti AI</span>
                    </a>
                    <a href="articolo-etf-16mar-guida-investire-etf-italia.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-amber-500 hover:border-amber-600">
                        <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">TER (Total Expense Ratio)</h3>
                        <p class="text-sm text-gray-600 dark:text-slate-400">Il costo annuale totale di un ETF, espresso in percentuale. Un TER dello 0,20% significa che su €10.000 investiti, paghi €20/anno. Gli ETF hanno TER molto più bassi dei fondi attivi.</p>
                        <span class="text-xs text-amber-600 dark:text-amber-400 font-semibold mt-2 inline-block">→ Spiegato in: Guida ETF Italia</span>
                    </a>'''

if '📈 Metriche Settoriali' in imp:
    idx = imp.index('📈 Metriche Settoriali')
    section_end = imp.index('</section>', idx)
    grid_end = imp.rfind('</div>', idx, section_end)
    imp = imp[:grid_end] + metriche_cards + '\n                ' + imp[grid_end:]

# Add to Settore Finanziario section
fin_cards = '''
                    <a href="articolo-ftse-mib-16mar-amplifon-stm-banche-centrali.html" class="concept-card bg-white dark:bg-[#0f172a]/60 p-5 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border-l-4 border-emerald-500 hover:border-emerald-600">
                        <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">Lo spread BTP-Bund</h3>
                        <p class="text-sm text-gray-600 dark:text-slate-400">La differenza di rendimento tra il BTP italiano e il Bund tedesco a 10 anni. Misura il rischio percepito dell'Italia: uno spread alto indica maggiore incertezza sul debito italiano.</p>
                        <span class="text-xs text-emerald-600 dark:text-emerald-400 font-semibold mt-2 inline-block">→ Spiegato in: FTSE MIB — Spread BTP-Bund</span>
                    </a>'''

if '🏦 Settore Finanziario' in imp:
    idx = imp.index('🏦 Settore Finanziario')
    section_end = imp.index('</section>', idx)
    grid_end = imp.rfind('</div>', idx, section_end)
    imp = imp[:grid_end] + fin_cards + '\n                ' + imp[grid_end:]

with open('impara-finanza.html', 'w') as f:
    f.write(imp)
print("✅ impara-finanza.html aggiornato")

print("\n🎉 AGGIORNAMENTO 16 MARZO 2026 COMPLETATO!")
print("File aggiornati: index.html, sitemap.xml, categoria-wall-street.html, categoria-borsa-milano.html, impara-finanza.html")
