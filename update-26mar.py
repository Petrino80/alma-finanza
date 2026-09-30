#!/usr/bin/env python3
"""Aggiornamento quotidiano Alma Finanza — 26 Marzo 2026"""

import re, os

BASE = "/Users/ferrarapetrino/Downloads/files-2"

def read(f):
    with open(os.path.join(BASE, f), "r", encoding="utf-8") as fh:
        return fh.read()

def write(f, content):
    with open(os.path.join(BASE, f), "w", encoding="utf-8") as fh:
        fh.write(content)

# ============================================================
# 1) AGGIORNA DATA HEADER
# ============================================================
idx = read("index.html")

# Data header
idx = idx.replace(
    'Martedì 24 Marzo 2026',
    'Giovedì 26 Marzo 2026'
)

# ============================================================
# 2) AGGIORNA STATS BAR
# ============================================================
old_stats = '''            <div class="stat-item bg-white dark:bg-[#0f172a]/80">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">Dow Jones</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">46.124</div>
                <div class="text-xs negative">-84 (-0,18%)</div>
            </div>
            <div class="stat-item bg-white dark:bg-[#0f172a]/80">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">S&amp;P 500</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">6.556</div>
                <div class="text-xs negative">-25 (-0,37%)</div>
            </div>
            <div class="stat-item bg-white dark:bg-[#0f172a]/80">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">FTSE MIB</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">43.369</div>
                <div class="text-xs positive">+179 (+0,42%)</div>
            </div>
            <div class="stat-item bg-white dark:bg-[#0f172a]/80">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">WTI Crude</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">$92,00</div>
                <div class="text-xs negative">+4,0%</div>
            </div>
            <div class="stat-item bg-white dark:bg-[#0f172a]/80 hidden md:block">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">Oro</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">$4.384</div>
                <div class="text-xs negative">-0,97%</div>
            </div>
            <div class="stat-item bg-white dark:bg-[#0f172a]/80 hidden md:block">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">Bitcoin</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">$71.782</div>
                <div class="text-xs positive">+1,2%</div>
            </div>'''

new_stats = '''            <div class="stat-item bg-white dark:bg-[#0f172a]/80">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">Dow Jones</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">45.998</div>
                <div class="text-xs negative">-422 (-0,93%)</div>
            </div>
            <div class="stat-item bg-white dark:bg-[#0f172a]/80">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">S&amp;P 500</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">6.496</div>
                <div class="text-xs negative">-96 (-1,46%)</div>
            </div>
            <div class="stat-item bg-white dark:bg-[#0f172a]/80">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">FTSE MIB</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">43.702</div>
                <div class="text-xs negative">-311 (-0,71%)</div>
            </div>
            <div class="stat-item bg-white dark:bg-[#0f172a]/80">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">WTI Crude</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">$93,61</div>
                <div class="text-xs negative">+3,6%</div>
            </div>
            <div class="stat-item bg-white dark:bg-[#0f172a]/80 hidden md:block">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">Oro</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">$4.521</div>
                <div class="text-xs positive">+2,7%</div>
            </div>
            <div class="stat-item bg-white dark:bg-[#0f172a]/80 hidden md:block">
                <div class="text-xs text-gray-400 dark:text-slate-600 mb-1">Bitcoin</div>
                <div class="text-lg font-bold text-gray-900 dark:text-white">$69.438</div>
                <div class="text-xs negative">-2,6%</div>
            </div>'''

idx = idx.replace(old_stats, new_stats)

# ============================================================
# 3) AGGIORNA HERO
# ============================================================
old_hero_start = '        <!-- Hero -->'
old_hero_end = '        </div>\n\n        <!-- Section header -->'

# Direct string replacement for hero
old_hero = idx[idx.index('        <!-- Hero -->'):idx.index('        <!-- Section header -->')]
new_hero = (
    '        <!-- Hero -->\n'
    '        <div class="hero-box bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 mb-10">\n'
    '            <div class="grid md:grid-cols-3">\n'
    '                <div class="md:col-span-2 p-8 md:p-12">\n'
    '                    <div class="flex items-center gap-3 mb-4">\n'
    '                        <div class="dot bg-red-500 animate-pulse"></div>\n'
    '                        <span class="text-xs font-bold text-red-600 dark:text-red-400 uppercase tracking-wider">Breaking &middot; 26 Mar 2026</span>\n'
    '                    </div>\n'
    '                    <h1 class="text-3xl md:text-4xl font-black text-gray-900 dark:text-white mb-4 leading-tight montserrat-font">\n'
    '                        Iran rifiuta il cessate il fuoco USA: mercati in rosso, petrolio a $106. Meta -7%, Nasdaq -2%\n'
    '                    </h1>\n'
    '                    <div class="accent-line mb-4"></div>\n'
    '                    <p class="text-gray-500 dark:text-slate-400 text-lg leading-relaxed mb-6">\n'
    '                        Tehran definisce la proposta a 15 punti &ldquo;massimalista e irragionevole&rdquo; e presenta 5 controproposte. Brent +3,8% a $106, WTI a $93,61. Wall Street crolla: S&amp;P -1,46%, Nasdaq -2,01%. Meta taglia 700 posti e perde il 7%. Recordati +4,75% a Milano su OPA CVC a &euro;52. Oro rimbalza a $4.521 come Safe Haven (bene rifugio).\n'
    '                    </p>\n'
    '                    <a href="articolo-wall-street-26mar-iran-rifiuto-meta-crollo.html" class="inline-flex items-center text-teal-600 dark:text-teal-400 font-semibold text-sm hover:text-teal-700 dark:hover:text-teal-300 transition group">\n'
    "                        Leggi l'articolo completo\n"
    '                        <svg class="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>\n'
    '                    </a>\n'
    '                </div>\n'
    '                <div class="flex items-center justify-center p-8 bg-gray-50 dark:bg-[#0a0f19]/50 border-l border-gray-100 dark:border-slate-700/20">\n'
    '                    <div class="text-center">\n'
    '                        <div class="text-5xl font-black text-gray-900 dark:text-white mb-1">-1,46%</div>\n'
    '                        <div class="text-sm text-gray-500 dark:text-slate-500 mb-3">S&amp;P 500 &mdash; Iran rifiuta cessate il fuoco</div>\n'
    '                        <div class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-red-50 dark:bg-red-500/15 text-red-600 dark:text-red-400">Brent $106 &middot; Meta -7% &middot; Recordati +4,75%</div>\n'
    '                        <div class="mt-4 space-y-1 text-xs text-gray-400 dark:text-slate-600">\n'
    '                            <div>Dow -0,93% &middot; Nasdaq -2,01% &middot; MIB -0,71%</div>\n'
    '                            <div>WTI $93,61 &middot; Oro $4.521 &middot; BTC $69.438</div>\n'
    '                        </div>\n'
    '                    </div>\n'
    '                </div>\n'
    '            </div>\n'
    '        </div>\n'
    '        </div>\n\n'
)
idx = idx.replace(old_hero, new_hero)

# ============================================================
# 4) AGGIORNA SECTION HEADER + NUOVE CARDS
# ============================================================
old_section = '''        <div class="flex items-center gap-3 mb-6">
            <div class="accent-line"></div>
            <h2 class="text-lg font-bold montserrat-font text-gray-900 dark:text-white">Oggi, 24 Marzo</h2>
        </div>

        <!-- Articles Grid -->
        <div class="grid md:grid-cols-3 gap-5">

            <!-- ====== ARTICOLI 24 MARZO 2026 ====== -->'''

new_section = '''        <div class="flex items-center gap-3 mb-6">
            <div class="accent-line"></div>
            <h2 class="text-lg font-bold montserrat-font text-gray-900 dark:text-white">Oggi, 26 Marzo</h2>
        </div>

        <!-- Articles Grid -->
        <div class="grid md:grid-cols-3 gap-5">

            <!-- ====== ARTICOLI 26 MARZO 2026 ====== -->

            <!-- Wall Street 26 mar -->
            <a href="articolo-wall-street-26mar-iran-rifiuto-meta-crollo.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-blue-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-blue-50 dark:bg-blue-500/15 text-blue-700 dark:text-blue-400 border border-transparent dark:border-blue-500/20">Wall Street</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Wall Street crolla dopo il rifiuto iraniano: S&amp;P -1,46%, Nasdaq -2,01%. Meta -7%</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Iran rifiuta cessate il fuoco USA. Brent a $106. AMD -6,35%, Micron -5,49%. Olaplex +48% per acquisizione Henkel.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">26 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi &rarr;</span>
                    </div>
                </div>
            </a>

            <!-- Piazza Affari 26 mar -->
            <a href="articolo-piazza-affari-26mar-recordati-opa-cvc-mps.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-emerald-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-green-50 dark:bg-emerald-500/15 text-green-700 dark:text-emerald-400 border border-transparent dark:border-emerald-500/20">Piazza Affari</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">FTSE MIB -0,71%: Recordati vola +4,75% su OPA CVC a &euro;52. Caos MPS</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">CVC punta al Delisting (revoca quotazione). Saipem +5,8%. MPS: revocati poteri a Lovaglio. Spread a 95 pb.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">26 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi &rarr;</span>
                    </div>
                </div>
            </a>

            <!-- Petrolio 26 mar -->
            <a href="articolo-petrolio-26mar-hormuz-iraq-force-majeure.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-amber-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-amber-50 dark:bg-amber-500/15 text-amber-700 dark:text-amber-400 border border-transparent dark:border-amber-500/20">Commodities</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Petrolio in fiamme: Brent $106, WTI $93,61. Hormuz bloccato, Iraq dichiara Force Majeure</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">War Premium (premio di guerra) +$15-20/barile. Traffico Hormuz -70%. Iraq: 4,5M bpd fermi. Previsioni $120 se blocco persiste.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">26 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi &rarr;</span>
                    </div>
                </div>
            </a>

            <!-- Tech/AI Arm 26 mar -->
            <a href="articolo-tech-26mar-arm-chip-agi-cpu-meta-ai.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-purple-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-purple-50 dark:bg-purple-500/15 text-purple-700 dark:text-purple-400 border border-transparent dark:border-purple-500/20">Tech &amp; AI</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Arm rivoluziona il settore: primo chip AGI CPU a 136 core. Meta primo cliente, ma taglia 700 posti</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">ARM +16%. Target $15B revenue 2031. Meta Capex (spese in conto capitale) AI: $135B. SMCI -7% per causa legale Cina.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">26 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi &rarr;</span>
                    </div>
                </div>
            </a>

            <!-- Geopolitica/Macro 26 mar -->
            <a href="articolo-geopolitica-26mar-iran-rifiuto-cessate-fuoco-oro.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-red-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-red-50 dark:bg-red-500/15 text-red-700 dark:text-red-400 border border-transparent dark:border-red-500/20">Geopolitica</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Iran rifiuta il cessate il fuoco USA: 5 controproposte. Oro rimbalza a $4.521 come Safe Haven (bene rifugio)</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Proposta 15 punti &ldquo;irragionevole&rdquo;. ONU fallisce. ECB avverte: possibile rialzo tassi. Fed in stallo. BTC in Extreme Fear.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">26 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi &rarr;</span>
                    </div>
                </div>
            </a>

            <!-- Day Separator 24 Marzo -->
            <div class="col-span-full flex items-center gap-3 mt-6 mb-2">
                <div class="w-10 h-0.5 rounded-full bg-gray-200 dark:bg-slate-700/40"></div>
                <h2 class="text-sm font-bold montserrat-font text-gray-400 dark:text-slate-600 uppercase tracking-wider">Martedì 24 Marzo</h2>
                <div class="flex-1 h-0.5 rounded-full bg-gray-100 dark:bg-slate-800/20"></div>
            </div>

            <!-- ====== ARTICOLI 24 MARZO 2026 ====== -->'''

idx = idx.replace(old_section, new_section)

write("index.html", idx)
print("✅ index.html aggiornato (data, stats, hero, cards)")

# ============================================================
# 5) AGGIORNA SITEMAP
# ============================================================
sitemap = read("sitemap.xml")

new_articles_sitemap = """
  <!-- Articoli 26 Marzo 2026 -->
  <url>
      <loc>https://www.almafinanza.com/articolo-wall-street-26mar-iran-rifiuto-meta-crollo.html</loc>
      <lastmod>2026-03-26</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-26</news:publication_date>
          <news:title>Wall Street crolla dopo il rifiuto iraniano del cessate il fuoco: S&amp;P -1,46%, Nasdaq -2,01%</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-piazza-affari-26mar-recordati-opa-cvc-mps.html</loc>
      <lastmod>2026-03-26</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-26</news:publication_date>
          <news:title>FTSE MIB -0,71%: Recordati +4,75% su OPA CVC a 52 euro. Caos MPS: revoca poteri Lovaglio</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-petrolio-26mar-hormuz-iraq-force-majeure.html</loc>
      <lastmod>2026-03-26</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-26</news:publication_date>
          <news:title>Petrolio in fiamme: Brent $106, WTI $93,61. Stretto di Hormuz bloccato, Iraq dichiara Force Majeure</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-tech-26mar-arm-chip-agi-cpu-meta-ai.html</loc>
      <lastmod>2026-03-26</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-26</news:publication_date>
          <news:title>Arm rivoluziona il settore: primo chip in-house AGI CPU a 136 core. Meta primo cliente</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-geopolitica-26mar-iran-rifiuto-cessate-fuoco-oro.html</loc>
      <lastmod>2026-03-26</lastmod>
      <changefreq>never</changefreq>
      <priority>0.9</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-26</news:publication_date>
          <news:title>Iran rifiuta il cessate il fuoco USA: 5 controproposte. Oro rimbalza a $4.521 come bene rifugio</news:title>
      </news:news>
  </url>

"""

# Insert after homepage entry and update lastmod
sitemap = sitemap.replace(
    '<lastmod>2026-03-23</lastmod>\n    <changefreq>daily</changefreq>',
    '<lastmod>2026-03-26</lastmod>\n    <changefreq>daily</changefreq>'
)

sitemap = sitemap.replace(
    '<!-- Articoli 24 Marzo 2026 -->',
    new_articles_sitemap + '  <!-- Articoli 24 Marzo 2026 -->'
)

write("sitemap.xml", sitemap)
print("✅ sitemap.xml aggiornato")

# ============================================================
# 6) AGGIORNA PAGINE CATEGORIA
# ============================================================

new_section_26mar = '''    <section class="mb-12">
        <div class="flex items-center mb-6">
            <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Giovedì, 26 Marzo 2026</h2>
            <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
        </div>
        <div class="grid md:grid-cols-3 gap-6">
'''

card_template = '''            <a href="{href}" class="block">
                <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge" style="background:{bg};color:{fg};">{cat}</span>
                        <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">{title}</h2>
                        <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">{desc}</p>
                        <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                            <span>📰 26 Mar 2026</span>
                            <span class="text-teal-500 font-semibold">Leggi →</span>
                        </div>
                    </div>
                </article>
            </a>
'''

# --- WALL STREET category ---
ws = read("categoria-wall-street.html")
ws_cards = (
    card_template.format(
        href="articolo-wall-street-26mar-iran-rifiuto-meta-crollo.html",
        bg="#dbeafe", fg="#1e40af", cat="Wall Street",
        title="Wall Street crolla: S&amp;P -1,46%, Nasdaq -2,01%. Iran rifiuta cessate il fuoco, Meta -7%",
        desc="Dow -422 a 45.998. AMD -6,35%, Micron -5,49%. Olaplex +48% per acquisizione Henkel. Treasury yields in rialzo."
    ) +
    card_template.format(
        href="articolo-tech-26mar-arm-chip-agi-cpu-meta-ai.html",
        bg="#f3e8ff", fg="#6b21a8", cat="Tech & AI",
        title="Arm lancia il primo chip in-house AGI CPU: 136 core, Meta primo cliente. SMCI -7%",
        desc="ARM +16%. Target $15B revenue 2031. Meta Capex AI $135B ma taglia 700 posti. SMCI causa legale export Cina."
    ) +
    card_template.format(
        href="articolo-geopolitica-26mar-iran-rifiuto-cessate-fuoco-oro.html",
        bg="#fee2e2", fg="#991b1b", cat="Geopolitica",
        title="Iran rifiuta proposta USA a 15 punti: 5 controproposte. ECB avverte su inflazione",
        desc="Tehran: proposta 'massimalista'. ONU fallisce. Fed in stallo. Import prices USA +1,3%. Oro $4.521 come bene rifugio."
    )
)

ws_insert = new_section_26mar + ws_cards + "        </div>\n    </section>\n\n    "

# Find insertion point
ws_insert_marker = re.search(r'(<section class="mb-12">\s*<div class="flex items-center mb-6">\s*<h2[^>]*>.*?24 Marzo)', ws, re.DOTALL)
if ws_insert_marker:
    ws = ws[:ws_insert_marker.start()] + ws_insert + ws[ws_insert_marker.start():]
    write("categoria-wall-street.html", ws)
    print("✅ categoria-wall-street.html aggiornata")
else:
    # Try alternative
    ws = ws.replace('<!-- Articoli -->', '<!-- Articoli -->\n\n' + ws_insert)
    write("categoria-wall-street.html", ws)
    print("✅ categoria-wall-street.html aggiornata (alt)")

# --- BORSA MILANO category ---
bm = read("categoria-borsa-milano.html")
bm_cards = card_template.format(
    href="articolo-piazza-affari-26mar-recordati-opa-cvc-mps.html",
    bg="#dcfce7", fg="#166534", cat="Piazza Affari",
    title="FTSE MIB -0,71%: Recordati +4,75% su OPA CVC a €52. MPS: revocati poteri a Lovaglio",
    desc="Saipem +5,8%, ENI +1,98%, Ferrari +2,6%. Spread BTP-Bund a 95 pb. Unicredit -1,79%, Nexi -2%."
)

bm_insert = new_section_26mar + bm_cards + "        </div>\n    </section>\n\n    "

bm_marker = re.search(r'(<section class="mb-12">\s*<div class="flex items-center mb-6">\s*<h2[^>]*>.*?24 Marzo)', bm, re.DOTALL)
if bm_marker:
    bm = bm[:bm_marker.start()] + bm_insert + bm[bm_marker.start():]
    write("categoria-borsa-milano.html", bm)
    print("✅ categoria-borsa-milano.html aggiornata")
else:
    bm = bm.replace('<!-- Articoli -->', '<!-- Articoli -->\n\n' + bm_insert)
    write("categoria-borsa-milano.html", bm)
    print("✅ categoria-borsa-milano.html aggiornata (alt)")

# --- COMMODITIES category ---
cm = read("categoria-commodities.html")
cm_cards = card_template.format(
    href="articolo-petrolio-26mar-hormuz-iraq-force-majeure.html",
    bg="#fef3c7", fg="#92400e", cat="Commodities",
    title="Petrolio: Brent $106, WTI $93,61. Hormuz bloccato, Iraq Force Majeure (causa di forza maggiore)",
    desc="War Premium +$15-20/barile. Traffico Hormuz -70%. Iraq 4,5M bpd fermi. Gas TTF +34%. Previsioni $120."
)

cm_insert = new_section_26mar + cm_cards + "        </div>\n    </section>\n\n    "

cm_marker = re.search(r'(<section class="mb-12">\s*<div class="flex items-center mb-6">\s*<h2[^>]*>.*?24 Marzo)', cm, re.DOTALL)
if cm_marker:
    cm = cm[:cm_marker.start()] + cm_insert + cm[cm_marker.start():]
    write("categoria-commodities.html", cm)
    print("✅ categoria-commodities.html aggiornata")
else:
    cm = cm.replace('<!-- Articoli -->', '<!-- Articoli -->\n\n' + cm_insert)
    write("categoria-commodities.html", cm)
    print("✅ categoria-commodities.html aggiornata (alt)")

# --- CRYPTO category (no crypto-specific articles today, but Bitcoin mentioned) ---
print("ℹ️  Nessun articolo crypto specifico oggi — categoria-crypto.html non aggiornata")

print("\n🎉 Script completato! Tutti i file aggiornati per il 26 Marzo 2026.")
