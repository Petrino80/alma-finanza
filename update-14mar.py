import re

# ============================================================
# AGGIORNAMENTO 14 MARZO 2026 — FASE 3-4-5
# Dati chiusura borse USA 13 marzo 2026
# ============================================================

# --- FASE 3: HOMEPAGE ---
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# a) TICKER — aggiorna valori
old_ticker_block = '''            <div class="ticker-item" data-ticker="dow"><a href="https://finance.yahoo.com/quote/%5EDJI" target="_blank">🇺🇸 Dow <span class="negative">46.678 (-1,56%)</span></a></div>
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
            <div class="ticker-item" data-ticker="oracle"><a href="articolo-oracle-12mar-q3-earnings-cloud-ai-243-percento.html">💻 <span class="positive">Oracle +10% AH: cloud +44%, AI +243%</span></a></div>'''

new_ticker_block = '''            <div class="ticker-item" data-ticker="dow"><a href="https://finance.yahoo.com/quote/%5EDJI" target="_blank">🇺🇸 Dow <span class="negative">46.558 (-0,26%)</span></a></div>
            <div class="ticker-item" data-ticker="sp500"><a href="https://finance.yahoo.com/quote/%5EGSPC" target="_blank">🇺🇸 S&P 500 <span class="negative">6.632 (-0,61%)</span></a></div>
            <div class="ticker-item" data-ticker="nasdaq"><a href="https://finance.yahoo.com/quote/%5EIXIC" target="_blank">🇺🇸 Nasdaq <span class="negative">22.105 (-0,93%)</span></a></div>
            <div class="ticker-item" data-ticker="ftsemib"><a href="https://finance.yahoo.com/quote/FTSEMIB.MI" target="_blank">🇮🇹 FTSE MIB <span class="negative">44.316 (-0,31%)</span></a></div>
            <div class="ticker-item" data-ticker="adobe"><a href="articolo-adobe-13mar-ceo-narayen-dimissioni-ai-cannibalizza-arr.html">📉 <span class="negative">Adobe -8,85%: CEO dimissioni, AI cannibalizza ARR</span></a></div>
            <div class="ticker-item" data-ticker="stellantis"><a href="articolo-ftse-mib-13mar-stellantis-cinesi-eni-leonardo-upgrade.html">🚗 <span class="negative">Stellantis -4,37%: voci cessione asset a cinesi</span></a></div>
            <div class="ticker-item" data-ticker="dax"><a href="https://finance.yahoo.com/quote/%5EGDAXI" target="_blank">🇩🇪 DAX <span class="negative">23.447 (-0,60%)</span></a></div>
            <div class="ticker-item" data-ticker="oil"><a href="https://finance.yahoo.com/quote/CL%3DF" target="_blank">🛢️ WTI <span class="negative">$93,39 (-2,44%)</span></a></div>
            <div class="ticker-item" data-ticker="brent"><a href="https://finance.yahoo.com/quote/BZ%3DF" target="_blank">🛢️ Brent <span class="positive">$101,07 (sopra $100)</span></a></div>
            <div class="ticker-item" data-ticker="gold"><a href="https://finance.yahoo.com/quote/GC%3DF" target="_blank">Oro <span class="negative">$5.040 (-1,12%)</span></a></div>
            <div class="ticker-item" data-ticker="btc"><a href="articolo-bitcoin-13mar-rally-74k-digital-gold-outperformance.html">₿ <span class="positive">Bitcoin $73.300 (+8% marzo)</span></a></div>
            <div class="ticker-item" data-ticker="michigan"><a href="articolo-dollar-general-13mar-michigan-sentiment-consumatori-crisi.html">📊 <span class="negative">Michigan Sentiment 55,5: minimi 2026</span></a></div>'''

html = html.replace(old_ticker_block, new_ticker_block, 2)  # Replace both copies (for loop)
print("✅ Ticker aggiornato")

# b) DATA header
html = html.replace('Venerdì 13 Marzo 2026', 'Sabato 14 Marzo 2026')
print("✅ Data header aggiornata")

# c) STATS BAR — aggiorna i 6 valori
# Dow
html = re.sub(r'(data-stat="dow"[^>]*>)\s*<div class="text-lg font-black[^"]*">[^<]*</div>\s*<div class="text-xs[^"]*">[^<]*</div>',
    r'\1<div class="text-lg font-black text-gray-900 dark:text-white">46.558</div><div class="text-xs negative">-0,26%</div>', html)
# S&P
html = re.sub(r'(data-stat="sp500"[^>]*>)\s*<div class="text-lg font-black[^"]*">[^<]*</div>\s*<div class="text-xs[^"]*">[^<]*</div>',
    r'\1<div class="text-lg font-black text-gray-900 dark:text-white">6.632</div><div class="text-xs negative">-0,61%</div>', html)
# MIB
html = re.sub(r'(data-stat="mib"[^>]*>)\s*<div class="text-lg font-black[^"]*">[^<]*</div>\s*<div class="text-xs[^"]*">[^<]*</div>',
    r'\1<div class="text-lg font-black text-gray-900 dark:text-white">44.316</div><div class="text-xs negative">-0,31%</div>', html)
# WTI
html = re.sub(r'(data-stat="wti"[^>]*>)\s*<div class="text-lg font-black[^"]*">[^<]*</div>\s*<div class="text-xs[^"]*">[^<]*</div>',
    r'\1<div class="text-lg font-black text-gray-900 dark:text-white">$93,39</div><div class="text-xs negative">-2,44%</div>', html)
# Oro
html = re.sub(r'(data-stat="oro"[^>]*>)\s*<div class="text-lg font-black[^"]*">[^<]*</div>\s*<div class="text-xs[^"]*">[^<]*</div>',
    r'\1<div class="text-lg font-black text-gray-900 dark:text-white">$5.040</div><div class="text-xs negative">-1,12%</div>', html)
# BTC
html = re.sub(r'(data-stat="btc"[^>]*>)\s*<div class="text-lg font-black[^"]*">[^<]*</div>\s*<div class="text-xs[^"]*">[^<]*</div>',
    r'\1<div class="text-lg font-black text-gray-900 dark:text-white">$73.300</div><div class="text-xs positive">+8% marzo</div>', html)
print("✅ Stats bar aggiornata")

# d) HERO — sostituire con Adobe crash
old_hero_left = '''                    <div class="flex items-center gap-2 mb-4">
                        <div class="dot bg-red-500"></div>
                        <span class="bg-red-500/10 dark:bg-red-500/20 text-red-700 dark:text-red-400 px-2 py-0.5 rounded text-xs font-bold">Breaking · 12 Mar</span>
                    </div>
                    <h1 class="text-2xl md:text-3xl font-black text-gray-900 dark:text-white leading-tight mb-3">Brent sopra $100: lo shock petrolifero affonda Wall Street</h1>
                    <div class="accent-line mb-4"></div>
                    <p class="text-gray-500 dark:text-slate-500 text-sm leading-relaxed mb-6">Lo Stretto di Hormuz chiuso dal nuovo leader iraniano Khamenei trascina il Brent oltre $100 per la prima volta dal 2022. Dow -1,56% a 46.678, S&P -1,50%. Airlines in caduta libera. Oracle unico bagliore: +10% AH.</p>
                    <a href="articolo-wall-street-12mar-shock-petrolio-sp500-dow-minimi-2026.html" class="inline-flex items-center text-teal-600 dark:text-teal-400 text-sm font-semibold group">
                        Leggi l'articolo completo
                        <svg class="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                    </a>'''

new_hero_left = '''                    <div class="flex items-center gap-2 mb-4">
                        <div class="dot bg-red-500"></div>
                        <span class="bg-red-500/10 dark:bg-red-500/20 text-red-700 dark:text-red-400 px-2 py-0.5 rounded text-xs font-bold">Breaking · 14 Mar</span>
                    </div>
                    <h1 class="text-2xl md:text-3xl font-black text-gray-900 dark:text-white leading-tight mb-3">Adobe crolla -8,85%: il CEO si dimette e l'AI cannibalizza il business</h1>
                    <div class="accent-line mb-4"></div>
                    <p class="text-gray-500 dark:text-slate-500 text-sm leading-relaxed mb-6">Shantanu Narayen lascia dopo 18 anni. Q1 record ($6,4B) ma Net New ARR miss: $70M persi per clienti che generano immagini con AI. Wall Street chiude la quarta seduta in calo, terza settimana rossa. S&P e Dow ai minimi da novembre.</p>
                    <a href="articolo-adobe-13mar-ceo-narayen-dimissioni-ai-cannibalizza-arr.html" class="inline-flex items-center text-teal-600 dark:text-teal-400 text-sm font-semibold group">
                        Leggi l'articolo completo
                        <svg class="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                    </a>'''
html = html.replace(old_hero_left, new_hero_left)

old_hero_right = '''                    <div class="text-center">
                        <div class="text-5xl font-black text-gray-900 dark:text-white mb-1">$100</div>
                        <div class="text-sm text-gray-500 dark:text-slate-500 mb-3">Brent al barile</div>
                        <div class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-red-50 dark:bg-red-500/15 text-red-600 dark:text-red-400">Giorno +9,22%</div>
                        <div class="mt-4 space-y-1 text-xs text-gray-400 dark:text-slate-600">
                            <div>Hormuz chiuso · Dow -1,56%</div>
                            <div>Leonardo +6% · Oracle +10% AH</div>
                        </div>
                    </div>'''

new_hero_right = '''                    <div class="text-center">
                        <div class="text-5xl font-black text-gray-900 dark:text-white mb-1">-8,85%</div>
                        <div class="text-sm text-gray-500 dark:text-slate-500 mb-3">Adobe (ADBE)</div>
                        <div class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-red-50 dark:bg-red-500/15 text-red-600 dark:text-red-400">CEO dimissioni · ARR miss</div>
                        <div class="mt-4 space-y-1 text-xs text-gray-400 dark:text-slate-600">
                            <div>S&P -0,61% · Nasdaq -0,93%</div>
                            <div>BTC $73.300 · Michigan 55,5</div>
                        </div>
                    </div>'''
html = html.replace(old_hero_right, new_hero_right)
print("✅ Hero aggiornato")

# e) SECTION HEADER + 5 nuove card + separator
html = html.replace(
    '<h2 class="text-lg font-bold montserrat-font text-gray-900 dark:text-white">Oggi, 13 Marzo</h2>',
    '<h2 class="text-lg font-bold montserrat-font text-gray-900 dark:text-white">Oggi, 14 Marzo</h2>'
)

new_14mar_cards = '''
            <!-- ====== ARTICOLI 14 MARZO 2026 ====== -->

            <!-- Wall Street 13 mar -->
            <a href="articolo-wall-street-13mar-sp500-nasdaq-quarta-seduta-calo-adobe.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-blue-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-blue-50 dark:bg-blue-500/15 text-blue-700 dark:text-blue-400 border border-transparent dark:border-blue-500/20">Wall Street</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Wall Street: quarta seduta in calo, Adobe crolla -8,85%. Terza settimana rossa</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">S&P -0,61% a 6.632, Nasdaq -0,93%, Dow -0,26%. Adobe -8,85%: CEO Narayen dimissioni. Michigan Sentiment 55,5, minimi 2026.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">14 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- FTSE MIB 13 mar -->
            <a href="articolo-ftse-mib-13mar-stellantis-cinesi-eni-leonardo-upgrade.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-emerald-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-green-50 dark:bg-emerald-500/15 text-green-700 dark:text-emerald-400 border border-transparent dark:border-emerald-500/20">Piazza Affari</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Stellantis crolla -4,37% su voci cessione ai cinesi. ENI +2,69%, Leonardo upgrade JP Morgan</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">FTSE MIB 44.316 (-0,31%). Bloomberg: Xiaomi e Xpeng trattano per asset europei. Enel +2,36%. Banche deboli: UniCredit -2,41%.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">14 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Adobe 13 mar -->
            <a href="articolo-adobe-13mar-ceo-narayen-dimissioni-ai-cannibalizza-arr.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-purple-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-purple-50 dark:bg-purple-500/15 text-purple-700 dark:text-purple-400 border border-transparent dark:border-purple-500/20">Tech/AI</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Adobe crolla -8,85%: CEO Narayen si dimette. L'AI cannibalizza lo stock photography</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Q1 record $6,4B (+12%), EPS $6,06 beat. Ma Net New ARR miss: $400M vs $450M. $70M persi per AI. 9 analisti tagliano target.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">14 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Dollar General / Michigan 13 mar -->
            <a href="articolo-dollar-general-13mar-michigan-sentiment-consumatori-crisi.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-red-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-red-50 dark:bg-red-500/15 text-red-700 dark:text-red-400 border border-transparent dark:border-red-500/20">Macro/Consumi</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Dollar General crolla e Michigan ai minimi 2026: il consumatore USA è sotto assedio</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">DG -6% su guidance FY2026 debole. Michigan Sentiment 55,5. Inflazione attesa 3,4%. Benzina $3,57 strangola i redditi bassi.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">14 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Bitcoin 13 mar -->
            <a href="articolo-bitcoin-13mar-rally-74k-digital-gold-outperformance.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-amber-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-amber-50 dark:bg-amber-500/15 text-amber-700 dark:text-amber-400 border border-transparent dark:border-amber-500/20">Crypto</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Bitcoin verso $74.000: outperformance su azioni e oro, 5 mesi di calo interrotti</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">BTC +8% a marzo, massimo da febbraio. Decorrelazione da S&P 500. Il "redemption trade" attira capitali. Dollaro forte non frena la corsa.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">14 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Day separator: 13 Marzo -->
            <div class="col-span-full flex items-center gap-3 mt-6 mb-2">
                <div class="w-10 h-0.5 rounded-full bg-gray-200 dark:bg-slate-700/40"></div>
                <h2 class="text-sm font-bold montserrat-font text-gray-400 dark:text-slate-600 uppercase tracking-wider">13 Marzo 2026</h2>
                <div class="flex-1 h-0.5 rounded-full bg-gray-100 dark:bg-slate-800/20"></div>
            </div>

            '''

# Insert new cards before the existing 13 Marzo section
html = html.replace(
    '            <!-- ====== ARTICOLI 13 MARZO 2026 ====== -->',
    new_14mar_cards + '<!-- ====== ARTICOLI 13 MARZO 2026 ====== -->'
)
print("✅ 5 nuove card + day separator aggiunti in cima alla griglia")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("✅ index.html salvato")


# --- SITEMAP ---
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

new_sitemap_entries = '''
  <!-- Articoli 14 Marzo 2026 -->
  <url>
      <loc>https://www.almafinanza.com/articolo-wall-street-13mar-sp500-nasdaq-quarta-seduta-calo-adobe.html</loc>
      <lastmod>2026-03-14</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-14</news:publication_date>
          <news:title>Wall Street: quarta seduta in calo, Adobe crolla -8,85%. Terza settimana rossa</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-ftse-mib-13mar-stellantis-cinesi-eni-leonardo-upgrade.html</loc>
      <lastmod>2026-03-14</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-14</news:publication_date>
          <news:title>FTSE MIB: Stellantis crolla -4,37% su voci cessione ai cinesi. ENI vola, Leonardo upgrade</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-adobe-13mar-ceo-narayen-dimissioni-ai-cannibalizza-arr.html</loc>
      <lastmod>2026-03-14</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-14</news:publication_date>
          <news:title>Adobe crolla -8,85%: CEO Narayen si dimette. L'AI cannibalizza lo stock photography</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-dollar-general-13mar-michigan-sentiment-consumatori-crisi.html</loc>
      <lastmod>2026-03-14</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-14</news:publication_date>
          <news:title>Dollar General crolla e Michigan Sentiment ai minimi 2026: consumatore USA sotto assedio</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-bitcoin-13mar-rally-74k-digital-gold-outperformance.html</loc>
      <lastmod>2026-03-14</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-14</news:publication_date>
          <news:title>Bitcoin verso $74.000: outperformance su azioni e oro, 5 mesi di calo interrotti</news:title>
      </news:news>
  </url>

'''

# Insert after <!-- Homepage --> section
sitemap = sitemap.replace(
    '\n  <!-- Articoli 13 Marzo',
    new_sitemap_entries + '  <!-- Articoli 13 Marzo'
)
# If that didn't match, try alternative
if new_sitemap_entries not in sitemap:
    sitemap = sitemap.replace(
        '\n  <!-- Articoli 12 Marzo',
        new_sitemap_entries + '  <!-- Articoli 12 Marzo'
    )

# Update homepage lastmod
sitemap = re.sub(r'(<loc>https://www\.almafinanza\.com/</loc>\s*<lastmod>)2026-03-\d{2}', r'\g<1>2026-03-14', sitemap)

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap)
print("✅ sitemap.xml aggiornata con 5 nuovi articoli")


# --- FASE 4: CATEGORIE ---

# CATEGORIA WALL STREET (articoli 1, 3, 4 = WS, Adobe/Tech, Dollar General/Macro)
with open('categoria-wall-street.html', 'r', encoding='utf-8') as f:
    cat_ws = f.read()

new_ws_section = '''        <section class="mb-12">
            <div class="flex items-center mb-6">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Sabato, 14 Marzo 2026</h2>
                <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
            </div>
            <div class="grid md:grid-cols-3 gap-6">
                <a href="articolo-wall-street-13mar-sp500-nasdaq-quarta-seduta-calo-adobe.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#dbeafe;color:#1e40af;">Wall Street</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Wall Street: quarta seduta in calo, Adobe -8,85%. Terza settimana rossa</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">S&P -0,61% a 6.632, Nasdaq -0,93%, Dow -0,26%. Adobe crolla dopo dimissioni CEO Narayen. Michigan Sentiment ai minimi 2026.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 14 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>
                <a href="articolo-adobe-13mar-ceo-narayen-dimissioni-ai-cannibalizza-arr.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#f3e8ff;color:#6b21a8;">Tech/AI</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Adobe -8,85%: CEO Narayen si dimette. L'AI cannibalizza lo stock photography</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Q1 record $6,4B ma Net New ARR miss. $70M persi per AI. 9 analisti tagliano target. Titolo -23% YTD, -60% dai massimi.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 14 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>
                <a href="articolo-dollar-general-13mar-michigan-sentiment-consumatori-crisi.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#fef2f2;color:#991b1b;">Macro/Consumi</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Dollar General e Michigan ai minimi 2026: consumatore USA sotto assedio</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">DG -6% su guidance debole. Michigan Sentiment 55,5. Inflazione attesa 3,4%. Benzina $3,57 strangola le famiglie a basso reddito.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 14 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>
            </div>
        </section>

'''

# Find first <section in the main content area
cat_ws = cat_ws.replace(
    '        <section class="mb-12">\n            <div class="flex items-center mb-6">\n                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Venerdì, 13 Marzo 2026</h2>',
    new_ws_section + '        <section class="mb-12">\n            <div class="flex items-center mb-6">\n                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Venerdì, 13 Marzo 2026</h2>'
)
# Fallback if 13 March section doesn't exist
if new_ws_section not in cat_ws:
    cat_ws = cat_ws.replace(
        '        <section class="mb-12">\n            <div class="flex items-center mb-6">\n                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Gioved',
        new_ws_section + '        <section class="mb-12">\n            <div class="flex items-center mb-6">\n                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Gioved'
    )

with open('categoria-wall-street.html', 'w', encoding='utf-8') as f:
    f.write(cat_ws)
print("✅ categoria-wall-street.html aggiornata (+3 articoli)")


# CATEGORIA BORSA MILANO (articolo 2 = FTSE MIB Stellantis)
with open('categoria-borsa-milano.html', 'r', encoding='utf-8') as f:
    cat_mi = f.read()

new_mi_section = '''        <section class="mb-12">
            <div class="flex items-center mb-6">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Sabato, 14 Marzo 2026</h2>
                <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
            </div>
            <div class="grid md:grid-cols-3 gap-6">
                <a href="articolo-ftse-mib-13mar-stellantis-cinesi-eni-leonardo-upgrade.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#d1fae5;color:#065f46;">Piazza Affari</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Stellantis -4,37% su voci cessione ai cinesi. ENI +2,69%, Leonardo upgrade JP Morgan</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">FTSE MIB 44.316 (-0,31%). Bloomberg: Xiaomi e Xpeng trattano per Maserati e asset europei. Enel +2,36%. Banche deboli.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 14 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>
            </div>
        </section>

'''

# Insert before the first existing section
first_section = cat_mi.find('        <section class="mb-12">')
if first_section != -1:
    cat_mi = cat_mi[:first_section] + new_mi_section + cat_mi[first_section:]

with open('categoria-borsa-milano.html', 'w', encoding='utf-8') as f:
    f.write(cat_mi)
print("✅ categoria-borsa-milano.html aggiornata (+1 articolo)")


# CATEGORIA CRYPTO (articolo 5 = Bitcoin)
with open('categoria-crypto.html', 'r', encoding='utf-8') as f:
    cat_cr = f.read()

new_cr_section = '''        <section class="mb-12">
            <div class="flex items-center mb-6">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Sabato, 14 Marzo 2026</h2>
                <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
            </div>
            <div class="grid md:grid-cols-3 gap-6">
                <a href="articolo-bitcoin-13mar-rally-74k-digital-gold-outperformance.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#fef3c7;color:#92400e;">Crypto</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Bitcoin verso $74.000: outperformance su azioni e oro, 5 mesi di calo interrotti</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">BTC +8% a marzo. Decorrelazione da S&P 500 durante crisi Iran. "Redemption trade" attira capitali. Massimo da febbraio.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 14 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>
            </div>
        </section>

'''

first_section_cr = cat_cr.find('        <section class="mb-12">')
if first_section_cr != -1:
    cat_cr = cat_cr[:first_section_cr] + new_cr_section + cat_cr[first_section_cr:]

with open('categoria-crypto.html', 'w', encoding='utf-8') as f:
    f.write(cat_cr)
print("✅ categoria-crypto.html aggiornata (+1 articolo)")


# --- FASE 5: IMPARA LA FINANZA ---
with open('impara-finanza.html', 'r', encoding='utf-8') as f:
    impara = f.read()

# Info-boxes dai 5 articoli:
# Art1 WS: Net New ARR, Consumer Sentiment Index
# Art2 FTSE: Carve-out, Target price/raccomandazioni
# Art3 Adobe: Paradosso del cannibale AI, Key Man Risk, NRR Net Revenue Retention
# Art4 DG: Dollar General termometro, Tassa benzina/moltiplicatore consumi
# Art5 BTC: Redemption trade/decorrelazione, Zona accumulazione/cicli Bitcoin

# Sezione Valutazioni e Multipli (blue) — Net New ARR, NRR
new_valutazioni = '''
                <a href="articolo-adobe-13mar-ceo-narayen-dimissioni-ai-cannibalizza-arr.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-blue-500 hover:border-blue-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Net New ARR (Annual Recurring Revenue)</h3>
                    <p class="text-sm text-gray-600">Misura i nuovi ricavi ricorrenti acquisiti in un trimestre, al netto di disdette e downgrade. Per le aziende SaaS è la metrica più importante perché anticipa la crescita futura.</p>
                    <span class="text-xs text-blue-600 font-semibold mt-2 inline-block">→ Spiegato in: Adobe crolla -8,85%</span>
                </a>
                <a href="articolo-adobe-13mar-ceo-narayen-dimissioni-ai-cannibalizza-arr.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-blue-500 hover:border-blue-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Net Revenue Retention (NRR)</h3>
                    <p class="text-sm text-gray-600">Misura quanti ricavi un'azienda SaaS mantiene dalla base clienti esistente, inclusi upgrade e cancellazioni. Un NRR sopra 100% indica crescita organica dal portafoglio clienti.</p>
                    <span class="text-xs text-blue-600 font-semibold mt-2 inline-block">→ Spiegato in: Adobe crolla -8,85%</span>
                </a>'''

# Sezione Macroeconomia e Banche Centrali (cyan) — Consumer Sentiment, Tassa benzina
new_macro = '''
                <a href="articolo-wall-street-13mar-sp500-nasdaq-quarta-seduta-calo-adobe.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-cyan-500 hover:border-cyan-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Consumer Sentiment Index (Michigan)</h3>
                    <p class="text-sm text-gray-600">Indicatore anticipatore dell'economia USA basato su 500 interviste. Misura fiducia consumatori, aspettative inflazione e propensione all'acquisto. Sotto 60 segnala forte stress economico.</p>
                    <span class="text-xs text-cyan-600 font-semibold mt-2 inline-block">→ Spiegato in: Wall Street quarta seduta calo</span>
                </a>
                <a href="articolo-dollar-general-13mar-michigan-sentiment-consumatori-crisi.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-cyan-500 hover:border-cyan-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Effetto "tassa sulla benzina" e moltiplicatore consumi</h3>
                    <p class="text-sm text-gray-600">L'aumento dei prezzi della benzina funziona come una tassa regressiva che colpisce di più le famiglie a basso reddito, con effetto moltiplicatore negativo sui consumi discrezionali.</p>
                    <span class="text-xs text-cyan-600 font-semibold mt-2 inline-block">→ Spiegato in: Dollar General e Michigan ai minimi</span>
                </a>'''

# Sezione Meccanismi di Mercato (purple) — Paradosso cannibale, Redemption trade
new_meccanismi = '''
                <a href="articolo-adobe-13mar-ceo-narayen-dimissioni-ai-cannibalizza-arr.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-purple-500 hover:border-purple-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Paradosso del cannibale nell'AI</h3>
                    <p class="text-sm text-gray-600">Quando un'azienda sviluppa una tecnologia che crea nuove opportunità di ricavo ma distrugge quelle esistenti. Adobe ne è l'esempio: Firefly attira clienti ma l'AI erode lo stock photography.</p>
                    <span class="text-xs text-purple-600 font-semibold mt-2 inline-block">→ Spiegato in: Adobe crolla -8,85%</span>
                </a>
                <a href="articolo-bitcoin-13mar-rally-74k-digital-gold-outperformance.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-purple-500 hover:border-purple-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Redemption Trade e decorrelazione degli asset</h3>
                    <p class="text-sm text-gray-600">Fenomeno in cui un asset sottoperformante viene rivalutato durante una crisi perché gli investitori cercano alternative non correlate ai mercati tradizionali. Bitcoin a marzo 2026 ne è l'esempio.</p>
                    <span class="text-xs text-purple-600 font-semibold mt-2 inline-block">→ Spiegato in: Bitcoin verso $74.000</span>
                </a>'''

# Sezione Gestione del Rischio (red) — Key Man Risk
new_rischio = '''
                <a href="articolo-adobe-13mar-ceo-narayen-dimissioni-ai-cannibalizza-arr.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-red-500 hover:border-red-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Key Man Risk (rischio persona chiave)</h3>
                    <p class="text-sm text-gray-600">Rischio che un'azienda dipenda eccessivamente da una singola persona chiave. Le dimissioni del CEO causano un premio di incertezza medio del 3-5%. Adobe ha perso il -8,85%.</p>
                    <span class="text-xs text-red-600 font-semibold mt-2 inline-block">→ Spiegato in: Adobe crolla -8,85%</span>
                </a>'''

# Sezione Modelli di Business (teal) — Carve-out, Dollar General termometro
new_business = '''
                <a href="articolo-ftse-mib-13mar-stellantis-cinesi-eni-leonardo-upgrade.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-teal-500 hover:border-teal-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Carve-out aziendale</h3>
                    <p class="text-sm text-gray-600">Operazione in cui un'azienda separa una parte delle proprie attività per venderla o quotarla separatamente. A differenza dello spin-off, l'azienda madre incassa liquidità dalla cessione.</p>
                    <span class="text-xs text-teal-600 font-semibold mt-2 inline-block">→ Spiegato in: Stellantis -4,37%</span>
                </a>
                <a href="articolo-dollar-general-13mar-michigan-sentiment-consumatori-crisi.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-teal-500 hover:border-teal-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Dollar General come termometro dei consumi USA</h3>
                    <p class="text-sm text-gray-600">Con 20.000 negozi in aree rurali, Dollar General serve clienti con reddito sotto $40.000. I suoi risultati sono un indicatore anticipatore dello stress economico delle famiglie più vulnerabili.</p>
                    <span class="text-xs text-teal-600 font-semibold mt-2 inline-block">→ Spiegato in: Dollar General e Michigan</span>
                </a>'''

# Sezione Metriche Settoriali (amber) — Target price, Zona accumulazione BTC
new_metriche = '''
                <a href="articolo-ftse-mib-13mar-stellantis-cinesi-eni-leonardo-upgrade.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-amber-500 hover:border-amber-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Target price e raccomandazioni degli analisti</h3>
                    <p class="text-sm text-gray-600">Il target price esprime il prezzo atteso a 12 mesi. Le raccomandazioni (Buy/Hold/Sell) indicano la view dell'analista. Storicamente i target vengono raggiunti solo nel 50-60% dei casi.</p>
                    <span class="text-xs text-amber-600 font-semibold mt-2 inline-block">→ Spiegato in: Stellantis e Leonardo upgrade</span>
                </a>
                <a href="articolo-bitcoin-13mar-rally-74k-digital-gold-outperformance.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-amber-500 hover:border-amber-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Zona di accumulazione e cicli di Bitcoin</h3>
                    <p class="text-sm text-gray-600">Bitcoin segue cicli di 4 anni legati all'halving con tre fasi: accumulazione, espansione e distribuzione. La zona di accumulazione è tipicamente tra il -50% e -75% dal massimo.</p>
                    <span class="text-xs text-amber-600 font-semibold mt-2 inline-block">→ Spiegato in: Bitcoin verso $74.000</span>
                </a>'''

# Add concept cards to each section
# Find the closing </div> of each section's grid and add before it
def add_to_section(html, section_emoji, new_cards):
    # Find the section header
    idx = html.find(section_emoji)
    if idx == -1:
        return html
    # Find the grid container after this section
    grid_start = html.find('<div class="grid', idx)
    if grid_start == -1:
        return html
    # Find the closing </div> of the grid
    # Count nested divs
    depth = 0
    i = grid_start
    while i < len(html):
        if html[i:i+4] == '<div':
            depth += 1
        elif html[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                # Insert before this closing div
                html = html[:i] + new_cards + '\n            ' + html[i:]
                break
        i += 1
    return html

impara = add_to_section(impara, '📊 Valutazioni e Multipli', new_valutazioni)
impara = add_to_section(impara, '🌍 Macroeconomia e Banche Centrali', new_macro)
impara = add_to_section(impara, '⚙️ Meccanismi di Mercato', new_meccanismi)
impara = add_to_section(impara, '⚠️ Gestione del Rischio', new_rischio)
impara = add_to_section(impara, '💼 Modelli di Business', new_business)
impara = add_to_section(impara, '📈 Metriche Settoriali', new_metriche)

with open('impara-finanza.html', 'w', encoding='utf-8') as f:
    f.write(impara)
print("✅ impara-finanza.html aggiornata (+12 concept-cards)")

print("\n" + "="*60)
print("✅ TUTTE LE FASI 3-4-5 COMPLETATE!")
print("="*60)
