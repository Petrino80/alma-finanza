#!/usr/bin/env python3
"""Aggiornamento homepage Alma Finanza - 11 Marzo 2026"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ============================================================
# 1. TICKER — Aggiorna tutti i valori a 11 Marzo 2026
# ============================================================
ticker_old_items = r'<div class="ticker-content">.*?</div></div>'

new_ticker_items = '''<div class="ticker-content">
            <div class="ticker-item" data-ticker="dow"><a href="https://finance.yahoo.com/quote/%5EDJI" target="_blank">🇺🇸 Dow <span class="negative">47.417 (-0,61%)</span></a></div>
            <div class="ticker-item" data-ticker="sp500"><a href="https://finance.yahoo.com/quote/%5EGSPC" target="_blank">🇺🇸 S&P 500 <span class="negative">6.776 (-0,08%)</span></a></div>
            <div class="ticker-item" data-ticker="nasdaq"><a href="https://finance.yahoo.com/quote/%5EIXIC" target="_blank">🇺🇸 Nasdaq <span class="positive">22.716 (+0,08%)</span></a></div>
            <div class="ticker-item" data-ticker="ftsemib"><a href="https://finance.yahoo.com/quote/FTSEMIB.MI" target="_blank">🇮🇹 FTSE MIB <span class="negative">44.773 (-0,95%)</span></a></div>
            <div class="ticker-item" data-ticker="nebius"><a href="https://finance.yahoo.com/quote/NBIS" target="_blank">🚀 Nebius <span class="positive">+16% (Nvidia $2B)</span></a></div>
            <div class="ticker-item" data-ticker="dax"><a href="https://finance.yahoo.com/quote/%5EGDAXI" target="_blank">🇩🇪 DAX <span class="negative">23.629 (-1,6%)</span></a></div>
            <div class="ticker-item" data-ticker="cac"><a href="https://finance.yahoo.com/quote/%5EFCHI" target="_blank">🇫🇷 CAC 40 <span class="negative">8.047 (-0,6%)</span></a></div>
            <div class="ticker-item" data-ticker="oil"><a href="https://finance.yahoo.com/quote/CL%3DF" target="_blank">🛢️ WTI <span class="positive">$87,25 (+4,55%)</span></a></div>
            <div class="ticker-item" data-ticker="gold"><a href="https://finance.yahoo.com/quote/GC%3DF" target="_blank">Oro <span class="negative">$5.159 (-1,3%)</span></a></div>
            <div class="ticker-item" data-ticker="btc"><a href="https://finance.yahoo.com/quote/BTC-USD" target="_blank">Bitcoin <span class="positive">$70.000 (+0,5%)</span></a></div>
            <div class="ticker-item" data-ticker="iea"><a href="articolo-petrolio-11mar-iea-riserve-400m-barili-hormuz.html" target="_blank">🛢️ <span class="negative">IEA STORICO: rilascio 400M barili, ma WTI +4,5% su attacchi Hormuz</span></a></div>
            <!-- Duplicate for seamless loop -->
            <div class="ticker-item" data-ticker="dow"><a href="https://finance.yahoo.com/quote/%5EDJI" target="_blank">🇺🇸 Dow <span class="negative">47.417 (-0,61%)</span></a></div>
            <div class="ticker-item" data-ticker="sp500"><a href="https://finance.yahoo.com/quote/%5EGSPC" target="_blank">🇺🇸 S&P 500 <span class="negative">6.776 (-0,08%)</span></a></div>
            <div class="ticker-item" data-ticker="nasdaq"><a href="https://finance.yahoo.com/quote/%5EIXIC" target="_blank">🇺🇸 Nasdaq <span class="positive">22.716 (+0,08%)</span></a></div>
            <div class="ticker-item" data-ticker="ftsemib"><a href="https://finance.yahoo.com/quote/FTSEMIB.MI" target="_blank">🇮🇹 FTSE MIB <span class="negative">44.773 (-0,95%)</span></a></div>
            <div class="ticker-item" data-ticker="nebius"><a href="https://finance.yahoo.com/quote/NBIS" target="_blank">🚀 Nebius <span class="positive">+16% (Nvidia $2B)</span></a></div>
            <div class="ticker-item" data-ticker="dax"><a href="https://finance.yahoo.com/quote/%5EGDAXI" target="_blank">🇩🇪 DAX <span class="negative">23.629 (-1,6%)</span></a></div>
            <div class="ticker-item" data-ticker="cac"><a href="https://finance.yahoo.com/quote/%5EFCHI" target="_blank">🇫🇷 CAC 40 <span class="negative">8.047 (-0,6%)</span></a></div>
            <div class="ticker-item" data-ticker="oil"><a href="https://finance.yahoo.com/quote/CL%3DF" target="_blank">🛢️ WTI <span class="positive">$87,25 (+4,55%)</span></a></div>
            <div class="ticker-item" data-ticker="gold"><a href="https://finance.yahoo.com/quote/GC%3DF" target="_blank">Oro <span class="negative">$5.159 (-1,3%)</span></a></div>
            <div class="ticker-item" data-ticker="btc"><a href="https://finance.yahoo.com/quote/BTC-USD" target="_blank">Bitcoin <span class="positive">$70.000 (+0,5%)</span></a></div>
            <div class="ticker-item" data-ticker="iea"><a href="articolo-petrolio-11mar-iea-riserve-400m-barili-hormuz.html" target="_blank">🛢️ <span class="negative">IEA STORICO: rilascio 400M barili, ma WTI +4,5% su attacchi Hormuz</span></a></div>
        </div></div>'''

html = re.sub(ticker_old_items, new_ticker_items, html, flags=re.DOTALL)
print("✅ Ticker aggiornato")

# ============================================================
# 2. DATA nell'header — da "Martedì 10 Marzo 2026" a "Mercoledì 11 Marzo 2026"
# ============================================================
html = html.replace('Martedì 10 Marzo 2026', 'Mercoledì 11 Marzo 2026')
print("✅ Data aggiornata")

# ============================================================
# 3. STATS BAR — Aggiorna i 6 riquadri
# ============================================================
# Dow Jones
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">47.706</div>\n                <div class="text-xs negative">-34 (-0,07%)</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">47.417</div>\n                <div class="text-xs negative">-289 (-0,61%)</div>'
)
# S&P 500
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">6.781</div>\n                <div class="text-xs negative">-14 (-0,21%)</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">6.776</div>\n                <div class="text-xs negative">-5 (-0,08%)</div>'
)
# FTSE MIB
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">45.201</div>\n                <div class="text-xs positive">+2,67%</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">44.773</div>\n                <div class="text-xs negative">-0,95%</div>'
)
# WTI Crude
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$83</div>\n                <div class="text-xs negative">-12%</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$87</div>\n                <div class="text-xs positive">+4,55%</div>'
)
# Oro
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$5.090</div>\n                <div class="text-xs negative">-1,3%</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$5.159</div>\n                <div class="text-xs negative">-1,3%</div>'
)
# Bitcoin
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$69.000</div>\n                <div class="text-xs positive">+2,5%</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$70.000</div>\n                <div class="text-xs positive">+0,5%</div>'
)
print("✅ Stats Bar aggiornata")

# ============================================================
# 4. HERO — Aggiorna con notizia del 11 marzo: IEA + CPI + Nebius
# ============================================================
old_hero = '''        <!-- Hero -->
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

new_hero = '''        <!-- Hero -->
        <div class="hero-box bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 mb-10">
            <div class="grid md:grid-cols-3">
                <div class="md:col-span-2 p-8 md:p-12">
                    <div class="flex items-center gap-3 mb-4">
                        <div class="dot bg-red-500 animate-pulse"></div>
                        <span class="text-xs font-bold text-red-600 dark:text-red-400 uppercase tracking-wider">Breaking · 11 Mar 2026</span>
                    </div>
                    <h1 class="text-3xl md:text-4xl font-black text-gray-900 dark:text-white mb-4 leading-tight montserrat-font">
                        IEA rilascio storico 400M barili ma petrolio sale +4,5%. CPI 2,4% in linea. Nvidia investe $2B in Nebius.
                    </h1>
                    <div class="accent-line mb-4"></div>
                    <p class="text-gray-500 dark:text-slate-400 text-lg leading-relaxed mb-6">
                        WTI +4,55% a $87 nonostante il più grande rilascio di riserve della storia. CPI febbraio 2,4% y/y, in linea con attese. Nebius vola +16% dopo investimento Nvidia. Fusione MPS-Mediobanca approvata.
                    </p>
                    <a href="articolo-petrolio-11mar-iea-riserve-400m-barili-hormuz.html" class="inline-flex items-center text-teal-600 dark:text-teal-400 font-semibold text-sm hover:text-teal-700 dark:hover:text-teal-300 transition group">
                        Leggi l'articolo completo
                        <svg class="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                    </a>
                </div>
                <div class="flex items-center justify-center p-8 bg-gray-50 dark:bg-[#0a0f19]/50 border-l border-gray-100 dark:border-slate-700/20">
                    <div class="text-center">
                        <div class="text-5xl font-black text-gray-900 dark:text-white mb-1">$87</div>
                        <div class="text-sm text-gray-500 dark:text-slate-500 mb-3">WTI al barile</div>
                        <div class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-red-50 dark:bg-red-500/15 text-red-600 dark:text-red-400">Giorno +4,55%</div>
                        <div class="mt-4 space-y-1 text-xs text-gray-400 dark:text-slate-600">
                            <div>IEA 400M bbl · Hormuz</div>
                            <div>Nebius +16% · CPI 2,4%</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>'''

html = html.replace(old_hero, new_hero)
print("✅ Hero aggiornato")

# ============================================================
# 5. SECTION HEADER — Aggiorna "Oggi, 10 Marzo" → "Oggi, 11 Marzo"
# ============================================================
html = html.replace(
    '<h2 class="text-lg font-bold montserrat-font text-gray-900 dark:text-white">Oggi, 10 Marzo</h2>',
    '<h2 class="text-lg font-bold montserrat-font text-gray-900 dark:text-white">Oggi, 11 Marzo</h2>'
)
print("✅ Section header aggiornato")

# ============================================================
# 6. GRIGLIA — Aggiungi 5 nuove theme-card + separatore "10 Marzo"
# ============================================================
new_cards_11mar = '''
            <!-- ====== ARTICOLI 11 MARZO 2026 ====== -->

            <!-- Wall Street 11 mar -->
            <a href="articolo-wall-street-11mar-cpi-stabile-nebius-nvidia-petrolio.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-blue-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-blue-50 dark:bg-blue-500/15 text-blue-700 dark:text-blue-400 border border-transparent dark:border-blue-500/20">Wall Street</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Wall Street in calo: CPI 2,4% in linea, Dow -0,61%. Petrolio risale +4,5%, Nebius vola +16%</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Dow 47.417 (-289 punti), S&P 6.776, Nasdaq +0,08%. CPI febbraio 2,4% y/y stabile. Nebius +16% su investimento Nvidia $2B. Oracle ancora +9%. WTI $87.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">11 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- FTSE MIB 11 mar -->
            <a href="articolo-ftse-mib-11mar-fusione-mps-mediobanca-diasorin.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-emerald-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-green-50 dark:bg-emerald-500/15 text-green-700 dark:text-emerald-400 border border-transparent dark:border-emerald-500/20">Piazza Affari</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">FTSE MIB -0,95% a 44.773: via libera fusione MPS-Mediobanca, DiaSorin crolla -6,7%</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Fusione MPS-Mediobanca approvata, concambio 2,45x. Mediobanca +2,1%, MPS +1,2%. ENI +2% su petrolio. DiaSorin peggior titolo. Leonardo -3,2%.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">11 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Europa 11 mar -->
            <a href="articolo-europa-11mar-dax-cede-rheinmetall-earnings.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-blue-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-blue-50 dark:bg-blue-500/15 text-blue-700 dark:text-blue-400 border border-transparent dark:border-blue-500/20">Europa</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Europa in rosso: DAX -1,6%, Rheinmetall crolla -5,2% dopo earnings deludenti</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Stoxx 600 -0,8%. DAX 23.629, CAC -0,6%. Rheinmetall -5,2% su guidance debole. Henkel -3,8%, SAP -2,2%. Tensioni Hormuz e petrolio pesano.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">11 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Petrolio IEA 11 mar -->
            <a href="articolo-petrolio-11mar-iea-riserve-400m-barili-hormuz.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-amber-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-amber-50 dark:bg-amber-500/15 text-amber-700 dark:text-amber-400 border border-transparent dark:border-amber-500/20">Commodities</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">IEA rilascio record 400M barili, ma WTI sale +4,55% a $87: attacchi a Hormuz</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Il più grande rilascio di riserve strategiche della storia non ferma il greggio. Attacchi nello Stretto di Hormuz. Brent $92. Oro -1,3%. Bitcoin $70K.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">11 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Nvidia-Nebius 11 mar -->
            <a href="articolo-nvidia-nebius-11mar-2b-ai-cloud-infrastruttura.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-purple-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-purple-50 dark:bg-purple-500/15 text-purple-700 dark:text-purple-400 border border-transparent dark:border-purple-500/20">Tech/AI</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Nvidia investe $2 miliardi in Nebius: azioni volano +16%, la corsa all'AI cloud</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Nvidia acquisisce 8,3% di Nebius per infrastruttura AI. 5+ GW di data center entro 2030. Oracle +9,3%. Serve Robotics +10%. Nasdaq +0,08%.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">11 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Day separator: 10 Marzo -->
            <div class="col-span-full flex items-center gap-3 mt-6 mb-2">
                <div class="w-10 h-0.5 rounded-full bg-gray-200 dark:bg-slate-700/40"></div>
                <h2 class="text-sm font-bold montserrat-font text-gray-400 dark:text-slate-600 uppercase tracking-wider">10 Marzo 2026</h2>
                <div class="flex-1 h-0.5 rounded-full bg-gray-100 dark:bg-slate-800/20"></div>
            </div>
'''

# Inserisci le nuove card prima del commento "====== ARTICOLI 10 MARZO 2026 ======"
html = html.replace(
    '            <!-- ====== ARTICOLI 10 MARZO 2026 ====== -->',
    new_cards_11mar + '\n            <!-- ====== ARTICOLI 10 MARZO 2026 ====== -->'
)

# Rimuovi il vecchio separatore "6 Marzo 2026" che ora è incorporato nel flusso
# No, il separatore "6 Marzo" è tra le card del 10 e del 6, resta valido.
print("✅ 5 nuove theme-card + separatore '10 Marzo' aggiunti")

# ============================================================
# SALVA
# ============================================================
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("\n🎉 Homepage aggiornata per l'11 Marzo 2026!")
