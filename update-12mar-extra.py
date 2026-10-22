#!/usr/bin/env python3
"""Aggiornamento extra 12 marzo 2026 — UiPath + Salesforce"""
import re, os

os.chdir('/Users/ferrarapetrino/Downloads/files-2')

# ============================================================
# HOMEPAGE — Aggiungi 2 nuove theme-cards
# ============================================================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Insert 2 new cards after the Morgan Stanley card (last of 12 March)
new_cards = '''
            <!-- UiPath 12 mar -->
            <a href="articolo-uipath-12mar-q4-earnings-agentic-ai-rpa-paradosso.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-purple-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-purple-50 dark:bg-purple-500/15 text-purple-700 dark:text-purple-400 border border-transparent dark:border-purple-500/20">Tech/AI</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">UiPath batte le stime Q4 ma crolla -9%: il paradosso dell'AI che minaccia l'automazione</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">EPS $0,30 vs $0,25. Primo utile GAAP. ARR $1,85B (+11%). Ma guidance FY27 delude: +9-10%. L'RPA è morta? Il titolo -27% YTD.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">12 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

            <!-- Salesforce 12 mar -->
            <a href="articolo-salesforce-12mar-buyback-50mld-debito-25mld-agentforce.html" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-sky-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-sky-50 dark:bg-sky-500/15 text-sky-700 dark:text-sky-400 border border-transparent dark:border-sky-500/20">Corporate</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">Salesforce: buyback record $50 mld con $25 mld di debito. Benioff scommette su Agentforce</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">La più grande emissione obbligazionaria nel software. ASR da $25B il 16 marzo. Anthropic +$811M. CRM a 15x utili, -28% YTD. Target $283.</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">12 Mar 2026</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>

'''

# Insert before the day separator "11 Marzo 2026"
marker = '<!-- Day separator: 11 Marzo -->'
if marker in html:
    html = html.replace(marker, new_cards + '            ' + marker)
    print("✅ Homepage: +2 nuove theme-cards (UiPath + Salesforce)")
else:
    print("❌ Day separator 11 Marzo non trovato")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# ============================================================
# SITEMAP — Aggiungi 2 nuovi URL
# ============================================================
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

new_urls = '''    <url>
        <loc>https://www.almafinanza.com/articolo-uipath-12mar-q4-earnings-agentic-ai-rpa-paradosso.html</loc>
        <lastmod>2026-03-12</lastmod>
        <changefreq>never</changefreq>
        <priority>0.9</priority>
        <news:news>
            <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
            <news:publication_date>2026-03-12</news:publication_date>
            <news:title>UiPath batte le stime Q4 ma crolla -9%: paradosso AI vs RPA</news:title>
        </news:news>
    </url>
    <url>
        <loc>https://www.almafinanza.com/articolo-salesforce-12mar-buyback-50mld-debito-25mld-agentforce.html</loc>
        <lastmod>2026-03-12</lastmod>
        <changefreq>never</changefreq>
        <priority>0.9</priority>
        <news:news>
            <news:publication><news:name>Alma Finanza</news:name><news:language>it</news:language></news:publication>
            <news:publication_date>2026-03-12</news:publication_date>
            <news:title>Salesforce: buyback record $50 mld con $25 mld di debito</news:title>
        </news:news>
    </url>
'''

# Insert after the Morgan Stanley article URL
morgan_marker = 'articolo-morgan-stanley-12mar-private-credit-riscatti-crisi.html'
morgan_end = sitemap.find(morgan_marker)
if morgan_end > 0:
    # Find the end of this <url> block
    url_end = sitemap.find('</url>', morgan_end) + len('</url>')
    sitemap = sitemap[:url_end] + '\n' + new_urls + sitemap[url_end:]
    print("✅ Sitemap: +2 nuovi URL")
else:
    print("❌ Morgan Stanley URL non trovato in sitemap")

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap)

# ============================================================
# CATEGORIA WALL STREET — Aggiungi UiPath + Salesforce
# ============================================================
with open('categoria-wall-street.html', 'r', encoding='utf-8') as f:
    cat_ws = f.read()

# Find the March 12 section grid and add 2 more cards
# The grid was just created with 3 articles, find the closing </div></section> of the 12 Marzo section
march12_grid = 'Giovedì, 12 Marzo 2026'
if march12_grid in cat_ws:
    # Find the grid container end (</div>) after the 3 existing cards
    grid_pos = cat_ws.find(march12_grid)
    # Find the third </a> after the grid position, then add before the closing </div>
    rest = cat_ws[grid_pos:]
    # Count 3 </a> closings (existing 3 articles)
    pos = grid_pos
    for i in range(3):
        next_close = cat_ws.find('</a>', pos + 1)
        if next_close > 0:
            pos = next_close + len('</a>')

    new_cat_cards = '''
                <a href="articolo-uipath-12mar-q4-earnings-agentic-ai-rpa-paradosso.html" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#f3e8ff;color:#6b21a8;">Tech/AI</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">UiPath batte Q4 ma crolla -9%: il paradosso AI nell'automazione</h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">EPS $0,30 vs $0,25. Primo utile GAAP. Ma guidance FY27 delude. L'RPA è obsoleta? ARR $1,85B (+11%).</p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 12 Mar 2026</span>
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
                                <span>📰 12 Mar 2026</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>
'''
    cat_ws = cat_ws[:pos] + '\n' + new_cat_cards + cat_ws[pos:]
    print("✅ categoria-wall-street.html: +2 articoli (UiPath + Salesforce)")
else:
    print("❌ Sezione 12 Marzo non trovata in categoria-wall-street")

with open('categoria-wall-street.html', 'w', encoding='utf-8') as f:
    f.write(cat_ws)

# ============================================================
# IMPARA LA FINANZA — Aggiungi nuovi concept-cards
# ============================================================
with open('impara-finanza.html', 'r', encoding='utf-8') as f:
    impara = f.read()

concepts = [
    # Modelli di Business (teal)
    {
        'section': 'Modelli di Business',
        'cards': [
            {
                'href': 'articolo-uipath-12mar-q4-earnings-agentic-ai-rpa-paradosso.html',
                'color': 'teal',
                'title': 'RPA (Robotic Process Automation)',
                'desc': 'Robot software che automatizzano attività ripetitive imitando azioni umane su interfacce grafiche. Minacciata dall\'AI agentica che opera in modo più flessibile.',
                'source': 'UiPath Q4: paradosso AI-RPA'
            },
            {
                'href': 'articolo-salesforce-12mar-buyback-50mld-debito-25mld-agentforce.html',
                'color': 'teal',
                'title': 'ASR (Accelerated Share Repurchase)',
                'desc': 'Meccanismo di buyback che permette di acquistare un grande blocco di azioni immediatamente pagando una banca intermediaria. Impatto immediato sull\'EPS.',
                'source': 'Salesforce: buyback $50 mld'
            }
        ]
    },
    # Metriche Settoriali (amber)
    {
        'section': 'Metriche Settoriali',
        'cards': [
            {
                'href': 'articolo-uipath-12mar-q4-earnings-agentic-ai-rpa-paradosso.html',
                'color': 'amber',
                'title': 'Rule of 40 (SaaS)',
                'desc': 'Crescita ricavi (%) + margine operativo (%) deve superare 40. UiPath: 13+23=36 (sotto soglia). I best-in-class superano 60.',
                'source': 'UiPath Q4: paradosso AI-RPA'
            },
            {
                'href': 'articolo-uipath-12mar-q4-earnings-agentic-ai-rpa-paradosso.html',
                'color': 'amber',
                'title': 'ARR (Annual Recurring Revenue)',
                'desc': 'Valore annualizzato dei contratti ad abbonamento attivi. Misura il reddito prevedibile. L\'ARR di UiPath è $1,85 miliardi (+11%).',
                'source': 'UiPath Q4: paradosso AI-RPA'
            }
        ]
    },
    # Macroeconomia / Meccanismi (purple)
    {
        'section': 'Meccanismi di Mercato',
        'cards': [
            {
                'href': 'articolo-salesforce-12mar-buyback-50mld-debito-25mld-agentforce.html',
                'color': 'purple',
                'title': 'Debt-funded buyback — leva finanziaria per gli azionisti',
                'desc': 'Indebitarsi per comprare le proprie azioni funziona se il costo del debito (5,5%) è inferiore all\'earnings yield (6,5%). Interessi deducibili fiscalmente.',
                'source': 'Salesforce: buyback $50 mld'
            }
        ]
    }
]

for concept_group in concepts:
    section_name = concept_group['section']
    section_match = re.search(rf'({section_name})', impara)
    if section_match:
        rest = impara[section_match.end():]
        close_match = re.search(r'(</div>\s*</section>)', rest)
        if close_match:
            insert_pos = section_match.end() + close_match.start()
            cards_html = ''
            for card in concept_group['cards']:
                cards_html += f'''
                <a href="{card['href']}" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-{card['color']}-500 hover:border-{card['color']}-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">{card['title']}</h3>
                    <p class="text-sm text-gray-600">{card['desc']}</p>
                    <span class="text-xs text-{card['color']}-600 font-semibold mt-2 inline-block">→ Spiegato in: {card['source']}</span>
                </a>'''
            impara = impara[:insert_pos] + cards_html + '\n            ' + impara[insert_pos:]
            print(f"  ✅ {section_name}: +{len(concept_group['cards'])} concept-cards")
        else:
            print(f"  ⚠️ Closing tag per '{section_name}' non trovato")
    else:
        print(f"  ⚠️ Sezione '{section_name}' non trovata")

with open('impara-finanza.html', 'w', encoding='utf-8') as f:
    f.write(impara)
print("✅ impara-finanza.html aggiornata")

print("\n✅ Tutto aggiornato! Pronto per commit.")
