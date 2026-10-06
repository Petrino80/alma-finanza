#!/usr/bin/env python3
"""Update all 4 category pages with missing articles from index.html."""
import re, os, html as htmlmod
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# 1. EXTRACT ALL ARTICLES FROM INDEX.HTML
# ============================================================
with open(os.path.join(BASE, 'index.html'), 'r', encoding='utf-8') as f:
    idx_html = f.read()

# Extract theme-card articles
pattern = r'<a href="(articolo-[^"]+)"[^>]*class="theme-card[^"]*".*?<span class="cat-tag[^"]*">([^<]+)</span>.*?<h3[^>]*>([^<]+)</h3>.*?<p class="text-sm text-gray-400[^"]*">([^<]+)</p>.*?<span class="text-xs text-gray-300[^"]*">([^<]+)</span>'
matches = re.findall(pattern, idx_html, re.DOTALL)

articles = []
seen_hrefs = set()
for href, cat, title, desc, date_str in matches:
    if href in seen_hrefs:
        continue
    seen_hrefs.add(href)
    articles.append({
        'href': href,
        'cat': cat.strip(),
        'title': title.strip(),
        'desc': desc.strip(),
        'date_str': date_str.strip()
    })

print(f"📊 Trovati {len(articles)} articoli unici in index.html")

# ============================================================
# 2. PARSE DATES
# ============================================================
MESI = {'Gen': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'Mag': 5, 'Giu': 6,
        'Lug': 7, 'Ago': 8, 'Set': 9, 'Ott': 10, 'Nov': 11, 'Dic': 12}

GIORNI_SETTIMANA = {0: 'Lunedì', 1: 'Martedì', 2: 'Mercoledì', 3: 'Giovedì',
                     4: 'Venerdì', 5: 'Sabato', 6: 'Domenica'}

MESI_NOME = {1: 'Gennaio', 2: 'Febbraio', 3: 'Marzo', 4: 'Aprile', 5: 'Maggio',
             6: 'Giugno', 7: 'Luglio', 8: 'Agosto', 9: 'Settembre', 10: 'Ottobre',
             11: 'Novembre', 12: 'Dicembre'}

for art in articles:
    # Parse "10 Mar 2026" or "6 Feb 2026" or "4 Feb 2026"
    parts = art['date_str'].split()
    day = int(parts[0])
    month = MESI.get(parts[1], 1)
    year = int(parts[2])
    art['date'] = datetime(year, month, day)
    dow = GIORNI_SETTIMANA[art['date'].weekday()]
    art['date_long'] = f"{dow}, {day} {MESI_NOME[month]} {year}"
    art['date_key'] = art['date'].strftime('%Y-%m-%d')

# ============================================================
# 3. CATEGORY MAPPING
# ============================================================
# Map cat-tag labels to category pages
WALL_STREET_CATS = {
    'Wall Street', 'S&P 500', 'Tech/AI', 'Tech & AI', 'AI & Chip', 'AI / Tech',
    'AI Software', 'Macro', 'Macro USA', 'Macro & Fed', 'Macroeconomia',
    'Fed Policy', 'Inflazione', 'Consumer', 'Corporate & Retail',
    'E-Commerce & M&A', 'EV / Tech', 'Airlines', 'Pharma', 'CRM + AI',
    'Microsoft', 'Meta Earnings', 'Tech/Media', 'Educazione', 'Sell-off',
    'Gaming Tech', 'Geopolitica & Dazi', 'Musk Empire', 'Confronto Mercati',
    'Small Cap', 'Small Caps', 'Geopolitica', 'Europa', 'Mercati Asia', 'Asia',
    'UK Defense', 'Streaming', 'Tesla Q1', 'FTSE MIB'
}

MILANO_CATS = {
    'Piazza Affari', 'Italia', 'FTSE MIB', 'Ferrari', 'Banche Italiane',
    'Olimpiadi 2026', 'Corporate', 'Energia & Industria', 'AI & Chip',
    'Energia & AI'
}

CRYPTO_CATS = {
    'Crypto', 'Bitcoin', 'Bitcoin ATH', 'Crypto & Oro'
}

COMMODITIES_CATS = {
    'Commodities', 'Oro', 'Oro ATH', 'Argento', 'Energy', 'Energy Tech'
}

# Assign articles to categories
cat_articles = {
    'wall-street': [],
    'milano': [],
    'crypto': [],
    'commodities': []
}

for art in articles:
    c = art['cat']
    if c in WALL_STREET_CATS:
        cat_articles['wall-street'].append(art)
    if c in MILANO_CATS:
        cat_articles['milano'].append(art)
    if c in CRYPTO_CATS:
        cat_articles['crypto'].append(art)
    if c in COMMODITIES_CATS:
        cat_articles['commodities'].append(art)

# Also add specific articles by href pattern
for art in articles:
    h = art['href']
    if 'wall-street' in h or 'dow-' in h or 'sp500' in h:
        if art not in cat_articles['wall-street']:
            cat_articles['wall-street'].append(art)
    if 'ftse-mib' in h or 'milano' in h or 'piazza-affari' in h:
        if art not in cat_articles['milano']:
            cat_articles['milano'].append(art)
    if 'bitcoin' in h or 'crypto' in h or 'coinbase' in h:
        if art not in cat_articles['crypto']:
            cat_articles['crypto'].append(art)
    if 'petrolio' in h or 'oro-' in h or 'oil' in h or 'argento' in h or 'gold' in h or 'wti' in h:
        if art not in cat_articles['commodities']:
            cat_articles['commodities'].append(art)

for key in cat_articles:
    print(f"  {key}: {len(cat_articles[key])} articoli totali")

# ============================================================
# 4. READ EXISTING CATEGORY PAGES AND FIND MISSING ARTICLES
# ============================================================
CAT_FILES = {
    'wall-street': 'categoria-wall-street.html',
    'milano': 'categoria-borsa-milano.html',
    'crypto': 'categoria-crypto.html',
    'commodities': 'categoria-commodities.html'
}

CAT_BADGE_CLASS = {
    'wall-street': 'cat-wall-street',
    'milano': 'cat-milano',
    'crypto': 'cat-crypto',
    'commodities': 'cat-commodities'
}

CAT_BADGE_LABEL = {
    'wall-street': 'Wall Street',
    'milano': 'Piazza Affari',
    'crypto': 'Crypto',
    'commodities': 'Commodities'
}

def get_existing_hrefs(filepath):
    """Extract all article hrefs already in a category page."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    return set(re.findall(r'href="(articolo-[^"]+)"', content))

def make_card_html(art, badge_label):
    """Generate HTML for one article card in category page format."""
    return f'''
                <a href="{art['href']}" class="block">
                    <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                        <span class="read-badge">Leggi</span>
                        <div class="p-6">
                            <span class="category-badge" style="background:#dbeafe;color:#1e40af;">{art['cat']}</span>
                            <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">
                                {htmlmod.escape(art['title'])}
                            </h2>
                            <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">
                                {htmlmod.escape(art['desc'])}
                            </p>
                            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                                <span>📰 {art['date_str']}</span>
                                <span class="text-teal-500 font-semibold">Leggi →</span>
                            </div>
                        </div>
                    </article>
                </a>'''

def make_date_section(date_long, cards_html):
    """Generate HTML for a date section with cards."""
    return f'''
        <section class="mb-12">
            <div class="flex items-center mb-6">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">{date_long}</h2>
                <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
            </div>

            <div class="grid md:grid-cols-3 gap-6">
{cards_html}
            </div>
        </section>
'''

# ============================================================
# 5. UPDATE EACH CATEGORY PAGE
# ============================================================
for cat_key, cat_file in CAT_FILES.items():
    filepath = os.path.join(BASE, cat_file)
    existing = get_existing_hrefs(filepath)

    # Filter to only new articles (not already in the page)
    new_arts = [a for a in cat_articles[cat_key] if a['href'] not in existing]

    if not new_arts:
        print(f"\n✅ {cat_file}: nessun articolo nuovo da aggiungere")
        continue

    # Sort by date descending
    new_arts.sort(key=lambda a: a['date'], reverse=True)

    # Group by date
    from collections import OrderedDict
    date_groups = OrderedDict()
    for art in new_arts:
        key = art['date_key']
        if key not in date_groups:
            date_groups[key] = {'date_long': art['date_long'], 'articles': []}
        date_groups[key]['articles'].append(art)

    # Generate HTML for all new date sections
    new_sections_html = ''
    for dk, dg in date_groups.items():
        cards = ''
        for art in dg['articles']:
            cards += make_card_html(art, CAT_BADGE_LABEL[cat_key])
        new_sections_html += make_date_section(dg['date_long'], cards)

    # Read the category page
    with open(filepath, 'r', encoding='utf-8') as f:
        page_html = f.read()

    # Find the first <section with date content and insert before it
    # Pattern: find the first <!-- date --> or <section class="mb-12"> after main content starts
    first_section_match = re.search(r'(\n        <!-- \d+ \w+ \d+ -->)', page_html)
    if first_section_match:
        insert_pos = first_section_match.start()
        page_html = page_html[:insert_pos] + new_sections_html + page_html[insert_pos:]
    else:
        # Try alternative: find first <section class="mb-12">
        first_section = page_html.find('<section class="mb-12">')
        if first_section > 0:
            # Find the line start
            line_start = page_html.rfind('\n', 0, first_section) + 1
            page_html = page_html[:line_start] + new_sections_html + page_html[line_start:]
        else:
            print(f"⚠️  {cat_file}: non trovato punto di inserimento!")
            continue

    # Write updated page
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(page_html)

    print(f"\n✅ {cat_file}: aggiunti {len(new_arts)} articoli in {len(date_groups)} sezioni data:")
    for dk, dg in date_groups.items():
        print(f"   {dg['date_long']}: {len(dg['articles'])} articoli")
