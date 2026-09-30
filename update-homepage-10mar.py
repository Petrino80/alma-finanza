#!/usr/bin/env python3
"""FASE 3: Update homepage index.html with March 10, 2026 data."""
import re, os

BASE = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE, 'index.html')

with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

original_size = len(html)

# ============================================================
# 1. UPDATE TICKER
# ============================================================
# Replace the entire ticker-content div
old_ticker_start = '<div class="ticker-content">'
old_ticker_end_marker = '</div>\n    </div>'  # closing of ticker-content + ticker-tape

# Find ticker content boundaries
ticker_start_idx = html.index(old_ticker_start)
# Find the closing </div> for ticker-content (after the duplicate block)
# The ticker-content has items then "<!-- Duplicate for seamless loop -->" then duplicate items then </div>
ticker_content_end = html.index('</div>\n    </div>\n\n    <!-- Header -->')

new_ticker_content = '''<div class="ticker-content">
            <div class="ticker-item" data-ticker="dow"><a href="https://finance.yahoo.com/quote/%5EDJI" target="_blank">🇺🇸 Dow <span class="negative">47.706 (-0,07%)</span></a></div>
            <div class="ticker-item" data-ticker="sp500"><a href="https://finance.yahoo.com/quote/%5EGSPC" target="_blank">🇺🇸 S&P 500 <span class="negative">6.781 (-0,21%)</span></a></div>
            <div class="ticker-item" data-ticker="nasdaq"><a href="https://finance.yahoo.com/quote/%5EIXIC" target="_blank">🇺🇸 Nasdaq <span class="positive">22.697 (+0,01%)</span></a></div>
            <div class="ticker-item" data-ticker="ftsemib"><a href="https://finance.yahoo.com/quote/FTSEMIB.MI" target="_blank">🇮🇹 FTSE MIB <span class="positive">45.201 (+2,67%)</span></a></div>
            <div class="ticker-item" data-ticker="oracle"><a href="https://finance.yahoo.com/quote/ORCL" target="_blank">🚀 Oracle <span class="positive">$185 (+9%)</span></a></div>
            <div class="ticker-item" data-ticker="dax"><a href="https://finance.yahoo.com/quote/%5EGDAXI" target="_blank">🇩🇪 DAX <span class="positive">23.935 (+2,4%)</span></a></div>
            <div class="ticker-item" data-ticker="cac"><a href="https://finance.yahoo.com/quote/%5EFCHI" target="_blank">🇫🇷 CAC 40 <span class="positive">8.096 (+2,3%)</span></a></div>
            <div class="ticker-item" data-ticker="oil"><a href="https://finance.yahoo.com/quote/CL%3DF" target="_blank">🛢️ WTI <span class="negative">$83 (-12%)</span></a></div>
            <div class="ticker-item" data-ticker="gold"><a href="https://finance.yahoo.com/quote/GC%3DF" target="_blank">Oro <span class="negative">$5.090 (-1,3%)</span></a></div>
            <div class="ticker-item" data-ticker="btc"><a href="https://finance.yahoo.com/quote/BTC-USD" target="_blank">Bitcoin <span class="positive">$69.000 (+2,5%)</span></a></div>
            <div class="ticker-item" data-ticker="deesc"><a href="articolo-petrolio-10mar-crash-trump-iran-fine-guerra.html" target="_blank">🕊️ <span class="positive">DE-ESCALATION IRAN: Petrolio crolla -12%, Trump apre ai negoziati</span></a></div>
            <!-- Duplicate for seamless loop -->
            <div class="ticker-item" data-ticker="dow"><a href="https://finance.yahoo.com/quote/%5EDJI" target="_blank">🇺🇸 Dow <span class="negative">47.706 (-0,07%)</span></a></div>
            <div class="ticker-item" data-ticker="sp500"><a href="https://finance.yahoo.com/quote/%5EGSPC" target="_blank">🇺🇸 S&P 500 <span class="negative">6.781 (-0,21%)</span></a></div>
            <div class="ticker-item" data-ticker="nasdaq"><a href="https://finance.yahoo.com/quote/%5EIXIC" target="_blank">🇺🇸 Nasdaq <span class="positive">22.697 (+0,01%)</span></a></div>
            <div class="ticker-item" data-ticker="ftsemib"><a href="https://finance.yahoo.com/quote/FTSEMIB.MI" target="_blank">🇮🇹 FTSE MIB <span class="positive">45.201 (+2,67%)</span></a></div>
            <div class="ticker-item" data-ticker="oracle"><a href="https://finance.yahoo.com/quote/ORCL" target="_blank">🚀 Oracle <span class="positive">$185 (+9%)</span></a></div>
            <div class="ticker-item" data-ticker="dax"><a href="https://finance.yahoo.com/quote/%5EGDAXI" target="_blank">🇩🇪 DAX <span class="positive">23.935 (+2,4%)</span></a></div>
            <div class="ticker-item" data-ticker="cac"><a href="https://finance.yahoo.com/quote/%5EFCHI" target="_blank">🇫🇷 CAC 40 <span class="positive">8.096 (+2,3%)</span></a></div>
            <div class="ticker-item" data-ticker="oil"><a href="https://finance.yahoo.com/quote/CL%3DF" target="_blank">🛢️ WTI <span class="negative">$83 (-12%)</span></a></div>
            <div class="ticker-item" data-ticker="gold"><a href="https://finance.yahoo.com/quote/GC%3DF" target="_blank">Oro <span class="negative">$5.090 (-1,3%)</span></a></div>
            <div class="ticker-item" data-ticker="btc"><a href="https://finance.yahoo.com/quote/BTC-USD" target="_blank">Bitcoin <span class="positive">$69.000 (+2,5%)</span></a></div>
            <div class="ticker-item" data-ticker="deesc"><a href="articolo-petrolio-10mar-crash-trump-iran-fine-guerra.html" target="_blank">🕊️ <span class="positive">DE-ESCALATION IRAN: Petrolio crolla -12%, Trump apre ai negoziati</span></a></div>
        </div>'''

html = html[:ticker_start_idx] + new_ticker_content + html[ticker_content_end:]
print("✅ 1. Ticker aggiornato con dati 10 Marzo")

# ============================================================
# 2. UPDATE DATE IN HEADER
# ============================================================
html = html.replace(
    'Venerdì 6 Marzo 2026',
    'Martedì 10 Marzo 2026'
)
print("✅ 2. Data header aggiornata")

# ============================================================
# 3. UPDATE STATS BAR
# ============================================================
old_stats = '''<div class="stats-bar bg-gray-100 dark:bg-slate-800/40 mb-8">
            <div class="stat-item bg-white dark:bg-[#0f172a]/80">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">Dow Jones</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">47.501</div>
                <div class="text-xs negative">-453 (-0.9%)</div>
            </div>
            <div class="stat-item bg-white dark:bg-[#0f172a]/80">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">S&amp;P 500</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">6.740</div>
                <div class="text-xs negative">-91 (-1.3%)</div>
            </div>
            <div class="stat-item bg-white dark:bg-[#0f172a]/80">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">FTSE MIB</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">44.152</div>
                <div class="text-xs negative">-1.0%</div>
            </div>
            <div class="stat-item bg-white dark:bg-[#0f172a]/80">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">WTI Crude</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">$90.90</div>
                <div class="text-xs negative">+12.2%</div>
            </div>
            <div class="stat-item bg-white dark:bg-[#0f172a]/80 hidden md:block">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">Oro</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">$5.085</div>
                <div class="text-xs text-gray-400 dark:text-slate-500">-0.5%</div>
            </div>
            <div class="stat-item bg-white dark:bg-[#0f172a]/80 hidden md:block">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">Bitcoin</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">$68.300</div>
                <div class="text-xs negative">-3.5%</div>
            </div>'''

new_stats = '''<div class="stats-bar bg-gray-100 dark:bg-slate-800/40 mb-8">
            <div class="stat-item bg-white dark:bg-[#0f172a]/80">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">Dow Jones</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">47.706</div>
                <div class="text-xs negative">-34 (-0,07%)</div>
            </div>
            <div class="stat-item bg-white dark:bg-[#0f172a]/80">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">S&amp;P 500</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">6.781</div>
                <div class="text-xs negative">-14 (-0,21%)</div>
            </div>
            <div class="stat-item bg-white dark:bg-[#0f172a]/80">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">FTSE MIB</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">45.201</div>
                <div class="text-xs positive">+2,67%</div>
            </div>
            <div class="stat-item bg-white dark:bg-[#0f172a]/80">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">WTI Crude</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">$83</div>
                <div class="text-xs negative">-12%</div>
            </div>
            <div class="stat-item bg-white dark:bg-[#0f172a]/80 hidden md:block">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">Oro</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">$5.090</div>
                <div class="text-xs negative">-1,3%</div>
            </div>
            <div class="stat-item bg-white dark:bg-[#0f172a]/80 hidden md:block">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">Bitcoin</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">$69.000</div>
                <div class="text-xs positive">+2,5%</div>
            </div>'''

html = html.replace(old_stats, new_stats)
print("✅ 3. Stats bar aggiornata")

# ============================================================
# 4. UPDATE HERO
# ============================================================
old_hero = '''<!-- Hero -->
        <div class="hero-box bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 mb-10">
            <div class="grid md:grid-cols-3">
                <div class="md:col-span-2 p-8 md:p-12">
                    <div class="flex items-center gap-3 mb-4">
                        <div class="dot bg-red-500 animate-pulse"></div>
                        <span class="text-xs font-bold text-red-600 dark:text-red-400 uppercase tracking-wider">Breaking · 6 Mar 2026</span>
                    </div>
                    <h1 class="text-3xl md:text-4xl font-black text-gray-900 dark:text-white mb-4 leading-tight montserrat-font">
                        Jobs Report shock: -92K posti.<br>WTI a $90.90, record storico settimanale.
                    </h1>
                    <div class="accent-line mb-4"></div>
                    <p class="text-gray-500 dark:text-slate-400 text-lg leading-relaxed mb-6">
                        L'economia USA perde posti di lavoro per la terza volta in 5 mesi. Il petrolio segna +35% nella settimana, il balzo più grande dal 1983.
                    </p>
                    <a href="articolo-wall-street-6mar-jobs-report-petrolio-90.html" class="inline-flex items-center text-teal-600 dark:text-teal-400 font-semibold text-sm hover:text-teal-700 dark:hover:text-teal-300 transition group">
                        Leggi l'articolo completo
                        <svg class="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                    </a>
                </div>
                <div class="flex items-center justify-center p-8 bg-gray-50 dark:bg-[#0a0f19]/50 border-l border-gray-100 dark:border-slate-700/20">
                    <div class="text-center">
                        <div class="text-5xl font-black text-gray-900 dark:text-white mb-1">$90.90</div>
                        <div class="text-sm text-gray-500 dark:text-slate-500 mb-3">WTI al barile</div>
                        <div class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-red-50 dark:bg-red-500/15 text-red-600 dark:text-red-400">Sett. +35.63%</div>
                        <div class="mt-4 space-y-1 text-xs text-gray-400 dark:text-slate-600">
                            <div>Dow -453 · S&amp;P -1.3%</div>
                            <div>NFP -92K · Disocc. 4.4%</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>'''

new_hero = '''<!-- Hero -->
        <div class="hero-box bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 mb-10">
            <div class="grid md:grid-cols-3">
                <div class="md:col-span-2 p-8 md:p-12">
                    <div class="flex items-center gap-3 mb-4">
                        <div class="dot bg-emerald-500 animate-pulse"></div>
                        <span class="text-xs font-bold text-emerald-600 dark:text-emerald-400 uppercase tracking-wider">Breaking · 10 Mar 2026</span>
                    </div>
                    <h1 class="text-3xl md:text-4xl font-black text-gray-900 dark:text-white mb-4 leading-tight montserrat-font">
                        Petrolio crolla -12%: Trump apre ai negoziati con l'Iran. Europa e Milano volano.
                    </h1>
                    <div class="accent-line mb-4"></div>
                    <p class="text-gray-500 dark:text-slate-400 text-lg leading-relaxed mb-6">
                        De-escalation Iran-USA: WTI precipita da $95 a $83. FTSE MIB +2,67%, DAX +2,4%. Oracle vola +9% dopo earnings cloud record. Wall Street mista.
                    </p>
                    <a href="articolo-petrolio-10mar-crash-trump-iran-fine-guerra.html" class="inline-flex items-center text-teal-600 dark:text-teal-400 font-semibold text-sm hover:text-teal-700 dark:hover:text-teal-300 transition group">
                        Leggi l'articolo completo
                        <svg class="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                    </a>
                </div>
                <div class="flex items-center justify-center p-8 bg-gray-50 dark:bg-[#0a0f19]/50 border-l border-gray-100 dark:border-slate-700/20">
                    <div class="text-center">
                        <div class="text-5xl font-black text-gray-900 dark:text-white mb-1">$83</div>
                        <div class="text-sm text-gray-500 dark:text-slate-500 mb-3">WTI al barile</div>
                        <div class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-emerald-50 dark:bg-emerald-500/15 text-emerald-600 dark:text-emerald-400">Giorno -12%</div>
                        <div class="mt-4 space-y-1 text-xs text-gray-400 dark:text-slate-600">
                            <div>MIB +2,67% · DAX +2,4%</div>
                            <div>Oracle +9% · BTC +2,5%</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>'''

html = html.replace(old_hero, new_hero)
print("✅ 4. Hero aggiornato (de-escalation oil crash)")

# ============================================================
# 5. UPDATE SECTION HEADER "Oggi, 6 Marzo" → "Venerdì, 6 Marzo"
#    and ADD new "Oggi, 10 Marzo" section + 5 new cards
# ============================================================

# Replace the existing "Oggi, 6 Marzo" header
html = html.replace(
    '<h2 class="text-lg font-bold montserrat-font text-gray-900 dark:text-white">Oggi, 6 Marzo</h2>',
    '<h2 class="text-lg font-bold montserrat-font text-gray-900 dark:text-white">Oggi, 10 Marzo</h2>'
)
print("✅ 5a. Section header aggiornato a '10 Marzo'")

# Insert 5 new March 10 cards + new "6 Marzo" day separator AFTER the existing cards grid opening
# Find the grid start and add the new cards at the very top
new_cards_block = '''
            <!-- ====== ARTICOLI 10 MARZO 2026 ====== -->

            <!-- Wall Street 10 mar -->
            <a href="articolo-wall-street-10mar-mixed-oil-crash-oracle.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-blue-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-blue-50 dark:bg-blue-500/15 text-blue-700 dark:text-blue-400 border border-transparent dark:border-blue-500/20">Wall Street</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Wall Street mista: petrolio crolla -12%, Oracle vola +9% su earnings cloud record</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Dow -0,07% a 47.706, S&P -0,21%, Nasdaq +0,01%. WTI precipita a $83 su de-escalation Iran. Oracle +9% con cloud +44% YoY. Kohl's -9%.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">10 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- FTSE MIB 10 mar -->
            <a href="articolo-ftse-mib-10mar-rimbalzo-unicredit-stm.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-emerald-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-green-50 dark:bg-emerald-500/15 text-green-700 dark:text-emerald-400 border border-transparent dark:border-emerald-500/20">Piazza Affari</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">FTSE MIB vola +2,67% a 45.201: rimbalzo guidato da Unicredit e STM</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Milano regina d'Europa. Unicredit, STM e industriali trascinano il listino. Calo del petrolio spinge utility e trasporti. Spread stabile.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">10 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Petrolio crash 10 mar -->
            <a href="articolo-petrolio-10mar-crash-trump-iran-fine-guerra.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-amber-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-amber-50 dark:bg-amber-500/15 text-amber-700 dark:text-amber-400 border border-transparent dark:border-amber-500/20">Commodities</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Petrolio crolla -12%: Trump apre ai negoziati con l'Iran, WTI da $95 a $83</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">De-escalation Iran: Trump apre a negoziati diplomatici. WTI perde $12 in una seduta. Brent sotto $86. Risk premium geopolitico si sgonfia.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">10 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Europa rally 10 mar -->
            <a href="articolo-europa-10mar-rally-dax-cac-petrolio-giu.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-blue-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-blue-50 dark:bg-blue-500/15 text-blue-700 dark:text-blue-400 border border-transparent dark:border-blue-500/20">Europa</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Europa in rally: DAX +2,4%, CAC +2,3% — Il crollo del petrolio accende i listini</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">DAX 23.935, CAC 40 8.096. De-escalation Iran libera i mercati europei. Settori industriali e auto in testa. Banche in forte rialzo.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">10 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Oracle 10 mar -->
            <a href="articolo-oracle-10mar-earnings-cloud-ai-44-percento.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-purple-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-purple-50 dark:bg-purple-500/15 text-purple-700 dark:text-purple-400 border border-transparent dark:border-purple-500/20">Tech/AI</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Oracle vola +9%: ricavi cloud +44% YoY, AI spinge la crescita record</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Earnings Q3 FY2026 sopra le attese. Cloud infrastructure +44% anno su anno. Partnership AI con hyperscaler. Target price alzati da Wall Street.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">10 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Day separator: 6 Marzo -->
            <div class="col-span-full flex items-center gap-3 mt-6 mb-2">
                <div class="w-10 h-0.5 rounded-full bg-gray-200 dark:bg-slate-700/40"></div>
                <h2 class="text-sm font-bold montserrat-font text-gray-400 dark:text-slate-600 uppercase tracking-wider">6 Marzo 2026</h2>
                <div class="flex-1 h-0.5 rounded-full bg-gray-100 dark:bg-slate-800/20"></div>
            </div>
'''

# Find the grid opening and the first card
grid_marker = '<!-- Articles Grid -->\n        <div class="grid md:grid-cols-3 gap-5">\n'
grid_idx = html.index(grid_marker) + len(grid_marker)

# Find and remove the old empty line + first comment (before "Wall Street 6 mar")
# There's a \n\n            \n\n before the first card
old_start = html[grid_idx:grid_idx+100]
# Clean up: remove old empty space before first 6 Mar card
clean_start = html.index('<!-- Wall Street 6 mar -->')

html = html[:grid_idx] + new_cards_block + '\n            ' + html[clean_start:]
print("✅ 5b. 5 nuove cards 10 Marzo aggiunte + day separator 6 Marzo")

# ============================================================
# 6. WRITE THE FILE
# ============================================================
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

new_size = len(html)
total_cards = len(re.findall(r'theme-card', html))
print(f"\n📊 Risultato:")
print(f"   File size: {original_size} → {new_size} bytes ({new_size - original_size:+d})")
print(f"   Total theme-cards: {total_cards}")
print(f"   Nuovi articoli 10 Mar: 5")
