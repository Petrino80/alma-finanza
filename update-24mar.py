#!/usr/bin/env python3
"""
Aggiornamento 24 Marzo 2026 — FASI 3-5
Homepage, sitemap, categorie, impara la finanza
"""
import re

# ========== FASE 3a: INDEX.HTML — Data header ==========
with open('index.html','r') as f:
    html = f.read()

# Data header
html = html.replace('Lunedì 23 Marzo 2026', 'Martedì 24 Marzo 2026')

# ========== FASE 3c: Stats Bar ==========
# Dow
html = html.replace(
    '<div class="text-xs text-gray-400 dark:text-slate-600 mb-1">Dow Jones</div>\n                <div class="text-lg font-bold text-gray-900 dark:text-white">46.208</div>\n                <div class="text-xs positive">+631 (+1,38%)</div>',
    '<div class="text-xs text-gray-400 dark:text-slate-600 mb-1">Dow Jones</div>\n                <div class="text-lg font-bold text-gray-900 dark:text-white">46.124</div>\n                <div class="text-xs negative">-84 (-0,18%)</div>'
)
# S&P
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">6.581</div>\n                <div class="text-xs positive">+75 (+1,15%)</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">6.556</div>\n                <div class="text-xs negative">-25 (-0,37%)</div>'
)
# MIB
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">43.190</div>\n                <div class="text-xs positive">+349 (+0,81%)</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">43.369</div>\n                <div class="text-xs positive">+179 (+0,42%)</div>'
)
# WTI
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$89,45</div>\n                <div class="text-xs positive">-8,94%</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$92,00</div>\n                <div class="text-xs negative">+4,0%</div>'
)
# Oro
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$4.406</div>\n                <div class="text-xs negative">-3,69%</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$4.384</div>\n                <div class="text-xs negative">-0,97%</div>'
)
# Bitcoin
html = html.replace(
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$70.903</div>\n                <div class="text-xs positive">+3,9%</div>',
    '<div class="text-lg font-bold text-gray-900 dark:text-white">$71.782</div>\n                <div class="text-xs positive">+1,2%</div>'
)

# ========== FASE 3d: Hero Article ==========
old_hero = '''        <!-- Hero -->
        <div class="hero-box bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 mb-10">
            <div class="grid md:grid-cols-3">
                <div class="md:col-span-2 p-8 md:p-12">
                    <div class="flex items-center gap-3 mb-4">
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
                        Leggi l'articolo completo
                        <svg class="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                    </a>
                </div>
                <div class="flex items-center justify-center p-8 bg-gray-50 dark:bg-[#0a0f19]/50 border-l border-gray-100 dark:border-slate-700/20">
                    <div class="text-center">
                        <div class="text-5xl font-black text-gray-900 dark:text-white mb-1">-9%</div>
                        <div class="text-sm text-gray-500 dark:text-slate-500 mb-3">WTI Crude — Trump pausa Iran</div>
                        <div class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-emerald-50 dark:bg-emerald-500/15 text-emerald-600 dark:text-emerald-400">Dow +631 · Poste OPAS TIM €10,8B</div>
                        <div class="mt-4 space-y-1 text-xs text-gray-400 dark:text-slate-600">
                            <div>S&P +1,15% · DAX +2,2% · MIB +0,81%</div>
                            <div>Oro -3,69% · BTC +3,9%</div>
                        </div>
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
                        <span class="text-xs font-bold text-red-600 dark:text-red-400 uppercase tracking-wider">Breaking · 24 Mar 2026</span>
                    </div>
                    <h1 class="text-3xl md:text-4xl font-black text-gray-900 dark:text-white mb-4 leading-tight montserrat-font">
                        82ª Airborne in rotta verso l'Iran: petrolio rimbalza +4%, tech crolla. PMI segnalano stagflazione
                    </h1>
                    <div class="accent-line mb-4"></div>
                    <p class="text-gray-500 dark:text-slate-400 text-lg leading-relaxed mb-6">
                        Il Pentagono invia 3.000 soldati della 82ª Divisione Airborne in Medio Oriente. Obiettivo: isola di Kharg, hub del 90% dell'export petrolifero iraniano. WTI rimbalza a $92, Brent a $104. Salesforce -6,23% guida il crollo tech. PMI Flash: crescita al minimo, prezzi in impennata. Inwit +9,8% a Milano su rumors Ardian-Brookfield.
                    </p>
                    <a href="articolo-wall-street-24mar-82nd-airborne-salesforce-tech.html" class="inline-flex items-center text-teal-600 dark:text-teal-400 font-semibold text-sm hover:text-teal-700 dark:hover:text-teal-300 transition group">
                        Leggi l'articolo completo
                        <svg class="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                    </a>
                </div>
                <div class="flex items-center justify-center p-8 bg-gray-50 dark:bg-[#0a0f19]/50 border-l border-gray-100 dark:border-slate-700/20">
                    <div class="text-center">
                        <div class="text-5xl font-black text-gray-900 dark:text-white mb-1">-0,37%</div>
                        <div class="text-sm text-gray-500 dark:text-slate-500 mb-3">S&P 500 — 82ª Airborne in Iran</div>
                        <div class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-red-50 dark:bg-red-500/15 text-red-600 dark:text-red-400">WTI +4% · CRM -6,23% · Inwit +9,8%</div>
                        <div class="mt-4 space-y-1 text-xs text-gray-400 dark:text-slate-600">
                            <div>Dow -0,18% · Nasdaq -0,84% · MIB +0,42%</div>
                            <div>Brent $104 · Oro $4.384 · BTC $71.782</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </div>'''

html = html.replace(old_hero, new_hero)

# ========== FASE 3e: Cards ==========
# Add 5 new cards BEFORE the insider trading card, all under "Oggi, 24 Marzo"
new_cards = '''            <!-- ====== ARTICOLI 24 MARZO 2026 ====== -->

            <!-- Wall Street 24 mar -->
            <a href="articolo-wall-street-24mar-82nd-airborne-salesforce-tech.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-blue-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-blue-50 dark:bg-blue-500/15 text-blue-700 dark:text-blue-400 border border-transparent dark:border-blue-500/20">Wall Street</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Wall Street cede: S&P -0,37%, Nasdaq -0,84%. 82&ordf; Airborne in rotta verso l'Iran</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Dow -84 a 46.124. Salesforce -6,23%, IBM -3,08%. Pentagono invia 3.000 soldati. After hours: futures +0,7% su piano di pace.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">24 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi &rarr;</span>
                    </div>
                </div>
            </a>

            <!-- FTSE MIB 24 mar -->
            <a href="articolo-ftse-mib-24mar-inwit-ardian-brookfield-difesa.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-emerald-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-green-50 dark:bg-emerald-500/15 text-green-700 dark:text-emerald-400 border border-transparent dark:border-emerald-500/20">Piazza Affari</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">FTSE MIB +0,42%: Inwit vola +9,8% su rumors Ardian-Brookfield. Difesa in rosso</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">Milano in altalena. Leonardo -3,6%, Avio -7%. Spread BTP-Bund a 92,5 pb. Brent a $104.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">24 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi &rarr;</span>
                    </div>
                </div>
            </a>

            <!-- PMI Stagflazione 24 mar -->
            <a href="articolo-pmi-24mar-stagflazione-eurozona-usa-energia.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-red-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-red-50 dark:bg-red-500/15 text-red-700 dark:text-red-400 border border-transparent dark:border-red-500/20">Macroeconomia</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">PMI Flash Marzo: stagflazione in arrivo. Eurozona a un passo dalla contrazione</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">USA: servizi 51,1, manifattura 52,4. Eurozona composito 50,5. Prezzi in impennata, crescita al minimo. Fed e BCE paralizzate.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">24 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi &rarr;</span>
                    </div>
                </div>
            </a>

            <!-- SaaS/Tech 24 mar -->
            <a href="articolo-tech-24mar-saas-salesforce-sap-ai-crisi.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-purple-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-purple-50 dark:bg-purple-500/15 text-purple-700 dark:text-purple-400 border border-transparent dark:border-purple-500/20">Tech & AI</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">La &ldquo;SaaSacre&rdquo;: Salesforce -6,23%, SAP -4%. L'AI sta uccidendo il software tradizionale</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">ServiceNow -36% YTD, HubSpot -51%. Il modello per seat in crisi. Celsius -9% per Costco Kirkland.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">24 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi &rarr;</span>
                    </div>
                </div>
            </a>

            <!-- Petrolio/Commodities 24 mar -->
            <a href="articolo-petrolio-24mar-rimbalzo-brent-104-kharg-oro.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-amber-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-amber-50 dark:bg-amber-500/15 text-amber-700 dark:text-amber-400 border border-transparent dark:border-amber-500/20">Commodities</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Petrolio rimbalza +4%: WTI a $92, Brent $104. Oro in calo per il 9&deg; giorno consecutivo</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">82&ordf; Airborne e isola di Kharg spingono il greggio. Oro $4.384 (-1%). Bitcoin $71.782 (+2%).</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">24 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi &rarr;</span>
                    </div>
                </div>
            </a>

'''

# Insert new cards before the insider trading card
html = html.replace(
    '            <!-- ====== ARTICOLI 24 MARZO 2026 ====== -->\n\n            <!-- Insider Trading 24 mar -->',
    new_cards + '            <!-- Insider Trading 24 mar -->'
)

# Remove the old "====== ARTICOLI 24 MARZO 2026 ======" comment that's now duplicated
# The new cards already have the comment at the top

with open('index.html','w') as f:
    f.write(html)
print('✅ index.html aggiornato')

# ========== FASE 3f: SITEMAP ==========
with open('sitemap.xml','r') as f:
    sitemap = f.read()

# Update homepage lastmod
sitemap = sitemap.replace(
    '<loc>https://www.almafinanza.com/</loc>\n      <lastmod>2026-03-23</lastmod>',
    '<loc>https://www.almafinanza.com/</loc>\n      <lastmod>2026-03-24</lastmod>'
)

new_sitemap_entries = '''
  <!-- Articoli 24 Marzo 2026 -->
  <url>
      <loc>https://www.almafinanza.com/articolo-wall-street-24mar-82nd-airborne-salesforce-tech.html</loc>
      <lastmod>2026-03-24</lastmod>
      <changefreq>never</changefreq>
      <priority>0.8</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-24</news:publication_date>
          <news:title>Wall Street cede: S&amp;P -0,37%, Nasdaq -0,84%. 82ª Airborne in rotta verso l'Iran</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-ftse-mib-24mar-inwit-ardian-brookfield-difesa.html</loc>
      <lastmod>2026-03-24</lastmod>
      <changefreq>never</changefreq>
      <priority>0.8</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-24</news:publication_date>
          <news:title>FTSE MIB +0,42%: Inwit vola +9,8% su rumors Ardian-Brookfield. Difesa in rosso</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-pmi-24mar-stagflazione-eurozona-usa-energia.html</loc>
      <lastmod>2026-03-24</lastmod>
      <changefreq>never</changefreq>
      <priority>0.8</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-24</news:publication_date>
          <news:title>PMI Flash Marzo: stagflazione in arrivo. Eurozona a un passo dalla contrazione</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-tech-24mar-saas-salesforce-sap-ai-crisi.html</loc>
      <lastmod>2026-03-24</lastmod>
      <changefreq>never</changefreq>
      <priority>0.8</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-24</news:publication_date>
          <news:title>La "SaaSacre": Salesforce -6,23%, SAP -4%. L'AI sta uccidendo il software tradizionale</news:title>
      </news:news>
  </url>
  <url>
      <loc>https://www.almafinanza.com/articolo-petrolio-24mar-rimbalzo-brent-104-kharg-oro.html</loc>
      <lastmod>2026-03-24</lastmod>
      <changefreq>never</changefreq>
      <priority>0.8</priority>
      <news:news>
          <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
          <news:publication_date>2026-03-24</news:publication_date>
          <news:title>Petrolio rimbalza +4%: WTI a $92, Brent $104. Oro in calo per il 9° giorno</news:title>
      </news:news>
  </url>

'''

# Insert after the insider trading entry
sitemap = sitemap.replace(
    '  <!-- Articolo Insider Trading 24 Marzo 2026 -->',
    new_sitemap_entries + '  <!-- Articolo Insider Trading 24 Marzo 2026 -->'
)

with open('sitemap.xml','w') as f:
    f.write(sitemap)
print('✅ sitemap.xml aggiornato')

# ========== FASE 4: CATEGORIE ==========

# --- categoria-wall-street.html ---
with open('categoria-wall-street.html','r') as f:
    cat_ws = f.read()

new_ws_section = '''    <section class="mb-12">
        <div class="flex items-center mb-6">
            <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Martedì, 24 Marzo 2026</h2>
            <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
        </div>
        <div class="grid md:grid-cols-3 gap-6">
            <a href="articolo-wall-street-24mar-82nd-airborne-salesforce-tech.html" class="block">
                <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge" style="background:#dbeafe;color:#1e40af;">Wall Street</span>
                        <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Wall Street cede: S&P -0,37%, Nasdaq -0,84%. 82ª Airborne in rotta verso l'Iran</h2>
                        <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Dow -84 a 46.124. Salesforce -6,23%, IBM -3,08%. Pentagono invia 3.000 soldati. After hours: futures +0,7% su piano di pace.</p>
                        <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                            <span>📰 24 Mar 2026</span>
                            <span class="text-teal-500 font-semibold">Leggi →</span>
                        </div>
                    </div>
                </article>
            </a>
            <a href="articolo-pmi-24mar-stagflazione-eurozona-usa-energia.html" class="block">
                <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge" style="background:#fee2e2;color:#991b1b;">Macroeconomia</span>
                        <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">PMI Flash Marzo: stagflazione in arrivo. Eurozona a un passo dalla contrazione</h2>
                        <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">USA: servizi 51,1, manifattura 52,4. Eurozona composito 50,5. Prezzi in impennata, crescita al minimo.</p>
                        <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                            <span>📰 24 Mar 2026</span>
                            <span class="text-teal-500 font-semibold">Leggi →</span>
                        </div>
                    </div>
                </article>
            </a>
            <a href="articolo-tech-24mar-saas-salesforce-sap-ai-crisi.html" class="block">
                <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge" style="background:#f3e8ff;color:#6b21a8;">Tech & AI</span>
                        <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">La "SaaSacre": Salesforce -6,23%, SAP -4%. L'AI sta uccidendo il software tradizionale</h2>
                        <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">ServiceNow -36% YTD, HubSpot -51%. Il modello per seat in crisi. Celsius -9% per Costco Kirkland.</p>
                        <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                            <span>📰 24 Mar 2026</span>
                            <span class="text-teal-500 font-semibold">Leggi →</span>
                        </div>
                    </div>
                </article>
            </a>
        </div>
    </section>

'''

# Insert before the first existing section
cat_ws = cat_ws.replace(
    '    <!-- ====== SEZIONE 23 MARZO',
    new_ws_section + '    <!-- ====== SEZIONE 23 MARZO'
)
# If the marker doesn't exist, try alternative
if new_ws_section not in cat_ws:
    cat_ws = cat_ws.replace(
        '    <section class="mb-12">\n        <div class="flex items-center mb-6">\n            <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Lunedì, 23 Marzo 2026</h2>',
        new_ws_section + '    <section class="mb-12">\n        <div class="flex items-center mb-6">\n            <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Lunedì, 23 Marzo 2026</h2>'
    )

with open('categoria-wall-street.html','w') as f:
    f.write(cat_ws)
print('✅ categoria-wall-street.html aggiornato')

# --- categoria-borsa-milano.html ---
with open('categoria-borsa-milano.html','r') as f:
    cat_mi = f.read()

new_mi_section = '''    <section class="mb-12">
        <div class="flex items-center mb-6">
            <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Martedì, 24 Marzo 2026</h2>
            <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
        </div>
        <div class="grid md:grid-cols-3 gap-6">
            <a href="articolo-ftse-mib-24mar-inwit-ardian-brookfield-difesa.html" class="block">
                <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge" style="background:#d1fae5;color:#065f46;">Piazza Affari</span>
                        <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">FTSE MIB +0,42%: Inwit vola +9,8% su rumors Ardian-Brookfield. Difesa in rosso</h2>
                        <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Milano in altalena. Leonardo -3,6%, Avio -7%. Spread BTP-Bund a 92,5 pb. Brent a $104.</p>
                        <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                            <span>📰 24 Mar 2026</span>
                            <span class="text-teal-500 font-semibold">Leggi →</span>
                        </div>
                    </div>
                </article>
            </a>
        </div>
    </section>

'''

cat_mi = cat_mi.replace(
    '    <section class="mb-12">\n        <div class="flex items-center mb-6">\n            <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Lunedì, 23 Marzo 2026</h2>',
    new_mi_section + '    <section class="mb-12">\n        <div class="flex items-center mb-6">\n            <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Lunedì, 23 Marzo 2026</h2>'
)

with open('categoria-borsa-milano.html','w') as f:
    f.write(cat_mi)
print('✅ categoria-borsa-milano.html aggiornato')

# --- categoria-commodities.html ---
with open('categoria-commodities.html','r') as f:
    cat_co = f.read()

new_co_section = '''    <section class="mb-12">
        <div class="flex items-center mb-6">
            <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Martedì, 24 Marzo 2026</h2>
            <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
        </div>
        <div class="grid md:grid-cols-3 gap-6">
            <a href="articolo-petrolio-24mar-rimbalzo-brent-104-kharg-oro.html" class="block">
                <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge" style="background:#fef3c7;color:#92400e;">Commodities</span>
                        <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Petrolio rimbalza +4%: WTI a $92, Brent $104. Oro in calo per il 9° giorno</h2>
                        <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">82ª Airborne e isola di Kharg spingono il greggio. Oro $4.384 (-1%). Bitcoin $71.782 (+2%).</p>
                        <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                            <span>📰 24 Mar 2026</span>
                            <span class="text-teal-500 font-semibold">Leggi →</span>
                        </div>
                    </div>
                </article>
            </a>
        </div>
    </section>

'''

cat_co = cat_co.replace(
    '    <section class="mb-12">\n        <div class="flex items-center mb-6">\n            <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Lunedì, 23 Marzo 2026</h2>',
    new_co_section + '    <section class="mb-12">\n        <div class="flex items-center mb-6">\n            <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Lunedì, 23 Marzo 2026</h2>'
)

with open('categoria-commodities.html','w') as f:
    f.write(cat_co)
print('✅ categoria-commodities.html aggiornato')

# ========== FASE 5: IMPARA LA FINANZA ==========
with open('impara-finanza.html','r') as f:
    impara = f.read()

# Concept cards da aggiungere nelle sezioni appropriate

# 1. 82ª Airborne → Geopolitica e Mercati
airborne_card = '''
                <a href="articolo-wall-street-24mar-82nd-airborne-salesforce-tech.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-rose-500 hover:border-rose-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">82ª Divisione Airborne (82nd Airborne Division)</h3>
                    <p class="text-sm text-gray-600">Unità d'élite dell'esercito USA con capacità di dispiegamento in 18 ore. La sua mobilitazione sposta i mercati perché segnala escalation militare imminente.</p>
                    <span class="text-xs text-rose-600 font-semibold mt-2 inline-block">→ Spiegato in: Wall Street 24 Mar — 82ª Airborne</span>
                </a>'''

# 2. Rotazione settoriale → Meccanismi di Mercato
rotation_card = '''
                <a href="articolo-wall-street-24mar-82nd-airborne-salesforce-tech.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-purple-500 hover:border-purple-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Rotazione Settoriale (Sector Rotation)</h3>
                    <p class="text-sm text-gray-600">Spostamento degli investimenti da settori ciclici/growth a difensivi durante crisi. Durante le guerre, si vende tech e si compra utilities, sanità e beni di consumo.</p>
                    <span class="text-xs text-purple-600 font-semibold mt-2 inline-block">→ Spiegato in: Wall Street 24 Mar — Rotazione settoriale</span>
                </a>'''

# 3. Fondi infrastrutturali → Settore Finanziario & Bancario
infra_card = '''
                <a href="articolo-ftse-mib-24mar-inwit-ardian-brookfield-difesa.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-emerald-500 hover:border-emerald-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Fondi Infrastrutturali (Infrastructure Funds)</h3>
                    <p class="text-sm text-gray-600">Fondi che investono in beni fisici essenziali: torri telecomunicazioni, autostrade, reti energetiche. Ardian e Brookfield sono tra i più grandi al mondo.</p>
                    <span class="text-xs text-emerald-600 font-semibold mt-2 inline-block">→ Spiegato in: FTSE MIB 24 Mar — Inwit e Ardian-Brookfield</span>
                </a>'''

# 4. Difesa in borsa → Settori e Aziende Specifiche
difesa_card = '''
                <a href="articolo-ftse-mib-24mar-inwit-ardian-brookfield-difesa.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-rose-500 hover:border-rose-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Titoli Difesa in Borsa: il Paradosso</h3>
                    <p class="text-sm text-gray-600">Le guerre aumentano i budget militari ma l'incertezza causa vendite. I titoli difesa spesso scendono dopo i rally iniziali per profit-taking e timori di escalation.</p>
                    <span class="text-xs text-rose-600 font-semibold mt-2 inline-block">→ Spiegato in: FTSE MIB 24 Mar — Difesa in rosso</span>
                </a>'''

# 5. PMI → Macroeconomia e Banche Centrali
pmi_card = '''
                <a href="articolo-pmi-24mar-stagflazione-eurozona-usa-energia.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-cyan-500 hover:border-cyan-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">PMI (Purchasing Managers' Index, Indice dei Direttori degli Acquisti)</h3>
                    <p class="text-sm text-gray-600">Indicatore anticipatore dell'economia: sopra 50 = espansione, sotto 50 = contrazione. Versione flash (anticipazione) e finale. Copre manifattura e servizi.</p>
                    <span class="text-xs text-cyan-600 font-semibold mt-2 inline-block">→ Spiegato in: PMI Flash Marzo — Stagflazione</span>
                </a>'''

# 6. SaaS → Modelli di Business
saas_card = '''
                <a href="articolo-tech-24mar-saas-salesforce-sap-ai-crisi.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-teal-500 hover:border-teal-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">SaaS (Software as a Service, Software come Servizio)</h3>
                    <p class="text-sm text-gray-600">Modello di business dove il software è venduto come abbonamento "per seat" (per postazione). In crisi perché l'AI sta eliminando i posti di lavoro che il SaaS automatizzava.</p>
                    <span class="text-xs text-teal-600 font-semibold mt-2 inline-block">→ Spiegato in: Tech 24 Mar — La SaaSacre</span>
                </a>'''

# 7. Private Label → Modelli di Business
private_label_card = '''
                <a href="articolo-tech-24mar-saas-salesforce-sap-ai-crisi.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-teal-500 hover:border-teal-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Private Label (Marchio del Distributore)</h3>
                    <p class="text-sm text-gray-600">Prodotti venduti con il marchio del rivenditore (es. Kirkland di Costco) a prezzi inferiori. Minaccia crescente per i brand affermati in tutti i settori.</p>
                    <span class="text-xs text-teal-600 font-semibold mt-2 inline-block">→ Spiegato in: Tech 24 Mar — Celsius vs Costco Kirkland</span>
                </a>'''

# 8. Kharg Island → Energia & Infrastrutture
kharg_card = '''
                <a href="articolo-petrolio-24mar-rimbalzo-brent-104-kharg-oro.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-orange-500 hover:border-orange-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Isola di Kharg (Kharg Island)</h3>
                    <p class="text-sm text-gray-600">Hub petrolifero che gestisce il 90% delle esportazioni di greggio iraniano. Obiettivo strategico chiave: la sua occupazione darebbe agli USA un'enorme leva negoziale.</p>
                    <span class="text-xs text-orange-600 font-semibold mt-2 inline-block">→ Spiegato in: Petrolio 24 Mar — Rimbalzo e Kharg</span>
                </a>'''

# 9. Oro e tassi → Gestione del Rischio
oro_tassi_card = '''
                <a href="articolo-petrolio-24mar-rimbalzo-brent-104-kharg-oro.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-red-500 hover:border-red-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Oro e Tassi di Interesse: la Correlazione Inversa</h3>
                    <p class="text-sm text-gray-600">L'oro non paga cedole né dividendi. Quando i tassi salgono, i titoli di Stato diventano più attraenti e l'oro perde appeal come bene rifugio, anche durante le guerre.</p>
                    <span class="text-xs text-red-600 font-semibold mt-2 inline-block">→ Spiegato in: Petrolio 24 Mar — Oro in caduta</span>
                </a>'''

# Insert cards into appropriate sections
# Geopolitica e Mercati
impara = impara.replace(
    '<!-- /Geopolitica e Mercati -->',
    airborne_card + '\n                <!-- /Geopolitica e Mercati -->'
)

# Meccanismi di Mercato
impara = impara.replace(
    '<!-- /Meccanismi di Mercato -->',
    rotation_card + '\n                <!-- /Meccanismi di Mercato -->'
)

# Settore Finanziario & Bancario
impara = impara.replace(
    '<!-- /Settore Finanziario -->',
    infra_card + '\n                <!-- /Settore Finanziario -->'
)

# Settori e Aziende Specifiche
impara = impara.replace(
    '<!-- /Settori e Aziende -->',
    difesa_card + '\n                <!-- /Settori e Aziende -->'
)

# Macroeconomia e Banche Centrali
impara = impara.replace(
    '<!-- /Macroeconomia -->',
    pmi_card + '\n                <!-- /Macroeconomia -->'
)

# Modelli di Business
impara = impara.replace(
    '<!-- /Modelli di Business -->',
    saas_card + private_label_card + '\n                <!-- /Modelli di Business -->'
)

# Energia & Infrastrutture
impara = impara.replace(
    '<!-- /Energia -->',
    kharg_card + '\n                <!-- /Energia -->'
)

# Gestione del Rischio
impara = impara.replace(
    '<!-- /Gestione del Rischio -->',
    oro_tassi_card + '\n                <!-- /Gestione del Rischio -->'
)

with open('impara-finanza.html','w') as f:
    f.write(impara)
print('✅ impara-finanza.html aggiornato')

print('\n🎉 Aggiornamento 24 Marzo completato!')
print('Attendere completamento agenti articoli prima di commit.')
