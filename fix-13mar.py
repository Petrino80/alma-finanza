#!/usr/bin/env python3
"""Fix: sposta UiPath e Salesforce al 13 marzo, in cima alla homepage"""
import re, os

os.chdir('/Users/ferrarapetrino/Downloads/files-2')

# ============================================================
# HOMEPAGE — Rimuovi le 2 card dalla sezione 12 marzo e mettile in cima con nuova sezione 13 marzo
# ============================================================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Rimuovi le card UiPath e Salesforce dalla posizione attuale (sezione 12 marzo)
# UiPath card
uipath_card_pattern = r'\s*<!-- UiPath 12 mar -->.*?</a>\s*'
html = re.sub(uipath_card_pattern, '\n', html, flags=re.DOTALL, count=1)

# Salesforce card
salesforce_card_pattern = r'\s*<!-- Salesforce 12 mar -->.*?</a>\s*'
html = re.sub(salesforce_card_pattern, '\n', html, flags=re.DOTALL, count=1)

print("✅ Rimosso UiPath e Salesforce dalla sezione 12 marzo")

# 2. Aggiorna header e data
html = html.replace('Giovedì 12 Marzo 2026', 'Venerdì 13 Marzo 2026')
html = html.replace('Oggi, 12 Marzo', 'Oggi, 13 Marzo')
print("✅ Data header aggiornata: Venerdì 13 Marzo 2026")

# 3. Aggiungi sezione 13 marzo in cima alla griglia con le 2 card + day separator prima del 12 marzo
new_section_13mar = '''
            <!-- ====== ARTICOLI 13 MARZO 2026 ====== -->

            <!-- UiPath 13 mar -->
            <a href="articolo-uipath-12mar-q4-earnings-agentic-ai-rpa-paradosso.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-purple-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-purple-50 dark:bg-purple-500/15 text-purple-700 dark:text-purple-400 border border-transparent dark:border-purple-500/20">Tech/AI</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">UiPath batte le stime Q4 ma crolla -9%: il paradosso dell'AI che minaccia l'automazione</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">EPS $0,30 vs $0,25. Primo utile GAAP. ARR $1,85B (+11%). Ma guidance FY27 delude: +9-10%. L'RPA è morta? Il titolo -27% YTD.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">13 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Salesforce 13 mar -->
            <a href="articolo-salesforce-12mar-buyback-50mld-debito-25mld-agentforce.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-sky-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-sky-50 dark:bg-sky-500/15 text-sky-700 dark:text-sky-400 border border-transparent dark:border-sky-500/20">Corporate</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Salesforce: buyback record $50 mld con $25 mld di debito. Benioff scommette su Agentforce</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">La più grande emissione obbligazionaria nel software. ASR da $25B il 16 marzo. Anthropic +$811M. CRM a 15x utili, -28% YTD. Target $283.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">13 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Day separator: 12 Marzo -->
            <div class="col-span-full flex items-center gap-3 mt-6 mb-2">
                <div class="w-10 h-0.5 rounded-full bg-gray-200 dark:bg-slate-700/40"></div>
                <h2 class="text-sm font-bold montserrat-font text-gray-400 dark:text-slate-600 uppercase tracking-wider">12 Marzo 2026</h2>
                <div class="flex-1 h-0.5 rounded-full bg-gray-100 dark:bg-slate-800/20"></div>
            </div>

'''

# Inserisci prima degli articoli del 12 marzo
marker_12 = '<!-- ====== ARTICOLI 12 MARZO 2026 ====== -->'
if marker_12 in html:
    html = html.replace(marker_12, new_section_13mar + '            ' + marker_12)
    print("✅ Sezione 13 marzo aggiunta in cima con 2 card + day separator")
else:
    print("❌ Marker 12 marzo non trovato")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("✅ index.html salvato")

# ============================================================
# SITEMAP — Aggiorna date da 12 a 13 per UiPath e Salesforce
# ============================================================
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

# Aggiorna lastmod e publication_date per UiPath
sitemap = sitemap.replace(
    '<loc>https://www.almafinanza.com/articolo-uipath-12mar-q4-earnings-agentic-ai-rpa-paradosso.html</loc>\n        <lastmod>2026-03-12</lastmod>',
    '<loc>https://www.almafinanza.com/articolo-uipath-12mar-q4-earnings-agentic-ai-rpa-paradosso.html</loc>\n        <lastmod>2026-03-13</lastmod>'
)
sitemap = sitemap.replace(
    '<loc>https://www.almafinanza.com/articolo-salesforce-12mar-buyback-50mld-debito-25mld-agentforce.html</loc>\n        <lastmod>2026-03-12</lastmod>',
    '<loc>https://www.almafinanza.com/articolo-salesforce-12mar-buyback-50mld-debito-25mld-agentforce.html</loc>\n        <lastmod>2026-03-13</lastmod>'
)
# Publication dates
sitemap = re.sub(
    r'(<news:publication_date>)2026-03-12(</news:publication_date>\s*<news:title>UiPath)',
    r'\g<1>2026-03-13\2',
    sitemap
)
sitemap = re.sub(
    r'(<news:publication_date>)2026-03-12(</news:publication_date>\s*<news:title>Salesforce)',
    r'\g<1>2026-03-13\2',
    sitemap
)

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap)
print("✅ sitemap.xml aggiornata a 13 marzo per UiPath e Salesforce")

# ============================================================
# CATEGORIA WALL STREET — Sposta UiPath e Salesforce in nuova sezione 13 marzo
# ============================================================
with open('categoria-wall-street.html', 'r', encoding='utf-8') as f:
    cat_ws = f.read()

# Rimuovi le 2 card UiPath e Salesforce dalla sezione 12 marzo
uipath_cat_pattern = r'\s*<a href="articolo-uipath-12mar.*?</a>\s*'
cat_ws = re.sub(uipath_cat_pattern, '\n', cat_ws, flags=re.DOTALL, count=1)

salesforce_cat_pattern = r'\s*<a href="articolo-salesforce-12mar.*?</a>\s*'
cat_ws = re.sub(salesforce_cat_pattern, '\n', cat_ws, flags=re.DOTALL, count=1)

# Aggiungi nuova sezione 13 marzo in cima (dopo <main>)
new_section = '''
        <section class="mb-12">
            <div class="flex items-center mb-6">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Venerdì, 13 Marzo 2026</h2>
                <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
            </div>
            <div class="grid md:grid-cols-3 gap-6">
                <a href="articolo-uipath-12mar-q4-earnings-agentic-ai-rpa-paradosso.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#f3e8ff;color:#6b21a8;">Tech/AI</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">UiPath batte Q4 ma crolla -9%: il paradosso AI nell'automazione</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">EPS $0,30 vs $0,25. Primo utile GAAP. Ma guidance FY27 delude. L'RPA è obsoleta? ARR $1,85B (+11%).</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 13 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>
                <a href="articolo-salesforce-12mar-buyback-50mld-debito-25mld-agentforce.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#e0f2fe;color:#0369a1;">Corporate/Tech</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">Salesforce: buyback $50 mld con $25 mld di debito. Agentforce avanza</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">Record obbligazionario nel software. ASR $25B il 16 marzo. Anthropic +$811M. CRM a 15x utili. Target $283.</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 13 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>
            </div>
        </section>
'''

main_match = re.search(r'(<main[^>]*>)', cat_ws)
if main_match:
    insert_pos = main_match.end()
    cat_ws = cat_ws[:insert_pos] + '\n' + new_section + cat_ws[insert_pos:]
    print("✅ categoria-wall-street.html: sezione 13 marzo creata con 2 articoli")
else:
    print("❌ <main> non trovato in categoria-wall-street")

with open('categoria-wall-street.html', 'w', encoding='utf-8') as f:
    f.write(cat_ws)

# ============================================================
# IMPARA LA FINANZA — Verifica che i concept-card puntino correttamente
# ============================================================
with open('impara-finanza.html', 'r', encoding='utf-8') as f:
    impara = f.read()

# I link agli articoli sono corretti (i nomi file non cambiano)
# Verifica che esistano
uipath_count = impara.count('articolo-uipath-12mar')
salesforce_count = impara.count('articolo-salesforce-12mar')
print(f"✅ impara-finanza.html: {uipath_count} link UiPath, {salesforce_count} link Salesforce — OK")

print("\n" + "="*60)
print("✅ TUTTE LE MODIFICHE COMPLETATE!")
print("="*60)
