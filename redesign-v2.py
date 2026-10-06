#!/usr/bin/env python3
"""
Redesign index.html to Modern Minimal (Preview E).
Approach: targeted replacements instead of full parsing.
"""
import re, os

BASE = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE, 'index.html')

with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

print(f"Read {len(html)} bytes")

# ========== 1. ADD NEW CSS CLASSES ==========
# Insert new classes right before </style>
new_css = """
        /* === MODERN MINIMAL === */
        .stats-bar{display:flex;gap:1px;border-radius:12px;overflow:hidden;}
        .stat-item{flex:1;padding:1rem;text-align:center;transition:background 0.4s;}
        .theme-card{border-radius:12px;overflow:hidden;transition:all 0.3s ease;}
        .theme-card:hover{transform:translateY(-3px);}
        .hero-box{border-radius:16px;overflow:hidden;transition:background 0.4s,border-color 0.4s;}
        .cat-tag{font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;padding:0.2rem 0.6rem;border-radius:4px;display:inline-block;}
        .accent-line{width:40px;height:3px;background:#14b8a6;border-radius:2px;}
        .dot{width:8px;height:8px;border-radius:50%;display:inline-block;}
"""
html = html.replace('    </style>', new_css + '    </style>')
print("Added new CSS classes")

# ========== 2. REPLACE HEADER + NAV ==========
# Find and replace from <!-- Header --> to </nav> (end of nav bar)
old_header_start = '    <!-- Header -->'
old_nav_end = '    </nav>'

# Find the positions
h_start = html.find(old_header_start)
nav_end = html.find(old_nav_end, h_start)
if h_start >= 0 and nav_end >= 0:
    nav_end += len(old_nav_end)

    new_header = """    <!-- Header -->
    <header class="sticky top-0 z-50 bg-white/92 dark:bg-[#0c1017]/92 backdrop-blur-xl border-b border-gray-100 dark:border-slate-800/20 transition-colors duration-300">
        <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
            <div class="flex items-center space-x-2">
                <span class="lobster-font text-5xl text-teal-500">A</span>
                <span class="montserrat-font text-3xl font-black text-gray-900 dark:text-white">LMA FINANZA</span>
            </div>
            <div class="hidden md:flex items-center space-x-8">
                <a href="categoria-wall-street.html" class="text-sm text-gray-500 dark:text-slate-500 hover:text-gray-900 dark:hover:text-white font-medium transition">Wall Street</a>
                <a href="categoria-borsa-milano.html" class="text-sm text-gray-500 dark:text-slate-500 hover:text-gray-900 dark:hover:text-white font-medium transition">Milano</a>
                <a href="categoria-crypto.html" class="text-sm text-gray-500 dark:text-slate-500 hover:text-gray-900 dark:hover:text-white font-medium transition">Crypto</a>
                <a href="categoria-commodities.html" class="text-sm text-gray-500 dark:text-slate-500 hover:text-gray-900 dark:hover:text-white font-medium transition">Commodities</a>
                <a href="dashboard.html" class="text-sm px-4 py-2 bg-gray-900 dark:bg-teal-600 text-white rounded-lg font-semibold hover:bg-gray-800 dark:hover:bg-teal-500 transition">Dashboard</a>
            </div>
            <div class="flex items-center gap-4">
                <div class="text-xs text-gray-400 dark:text-slate-600 hidden md:block">Venerdì 6 Marzo 2026</div>
                <div class="theme-toggle bg-gray-200 dark:bg-slate-700" onclick="toggleTheme()" title="Cambia tema">
                    <div class="toggle-circle bg-white dark:bg-slate-900 shadow-md">
                        <span class="ico-sun">☀️</span><span class="ico-moon" style="display:none">🌙</span>
                    </div>
                </div>
            </div>
        </div>
    </header>"""

    html = html[:h_start] + new_header + html[nav_end:]
    print("Replaced header + removed nav bar")
else:
    print("WARNING: Could not find header/nav boundaries")

# ========== 3. ADD STATS BAR + REPLACE HERO + SECTION TITLE ==========
# Replace from <!-- Main Content --> through the "Articoli Ultimi 7 Giorni" section
old_main_start = '    <!-- Main Content -->\n    <main class="max-w-7xl mx-auto px-4 py-8">'
# Find the first card link to know where cards start
first_card_marker = '<!-- ====== ARTICOLI 6 MARZO 2026 ====== -->'

m_start = html.find(old_main_start)
fc_start = html.find(first_card_marker)

if m_start >= 0 and fc_start >= 0:
    new_main_section = """    <!-- Stats Bar -->
    <div class="max-w-6xl mx-auto px-4 pt-8">
        <div class="stats-bar bg-gray-100 dark:bg-slate-800/40 mb-8">
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
            </div>
        </div>
    </div>

    <!-- Main Content -->
    <main class="max-w-6xl mx-auto px-4 py-4">

        <!-- Hero -->
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
        </div>

        <!-- Section header -->
        <div class="flex items-center gap-3 mb-6">
            <div class="accent-line"></div>
            <h2 class="text-lg font-bold montserrat-font text-gray-900 dark:text-white">Oggi, 6 Marzo</h2>
        </div>

        <!-- Articles Grid -->
        <div class="grid md:grid-cols-3 gap-5">

            """

    html = html[:m_start] + new_main_section + html[fc_start:]
    print("Replaced hero, stats bar, section header")
else:
    print("WARNING: Could not find main/hero boundaries")

# ========== 4. TRANSFORM CARDS ==========
# Color mapping from old border colors
COLOR_MAP = {
    '#1d4ed8': 'blue',
    '#15803d': 'emerald',
    '#d97706': 'amber',
    '#dc2626': 'red',
    '#7c3aed': 'purple',
    '#0d9488': 'teal',
    '#0369a1': 'sky',
    '#ea580c': 'orange',
    '#475569': 'slate',
    '#4f46e5': 'indigo',
    '#16a34a': 'green',
}

TAG_COLORS = {
    'blue': ('blue-50', 'blue-700', 'blue-500/15', 'blue-400', 'blue-500/20'),
    'emerald': ('green-50', 'green-700', 'emerald-500/15', 'emerald-400', 'emerald-500/20'),
    'amber': ('amber-50', 'amber-700', 'amber-500/15', 'amber-400', 'amber-500/20'),
    'red': ('red-50', 'red-700', 'red-500/15', 'red-400', 'red-500/20'),
    'purple': ('purple-50', 'purple-700', 'purple-500/15', 'purple-400', 'purple-500/20'),
    'teal': ('teal-50', 'teal-700', 'teal-500/15', 'teal-400', 'teal-500/20'),
    'sky': ('sky-50', 'sky-700', 'sky-500/15', 'sky-400', 'sky-500/20'),
    'orange': ('orange-50', 'orange-700', 'orange-500/15', 'orange-400', 'orange-500/20'),
    'slate': ('slate-100', 'slate-700', 'slate-500/15', 'slate-400', 'slate-500/20'),
    'indigo': ('indigo-50', 'indigo-700', 'indigo-500/15', 'indigo-400', 'indigo-500/20'),
    'green': ('green-50', 'green-700', 'green-500/15', 'green-400', 'green-500/20'),
}

def make_theme_card(href, color, cat_text, title, desc, date_text):
    """Build a theme-card from extracted data."""
    c = TAG_COLORS.get(color, TAG_COLORS['blue'])
    return f'''            <a href="{href}" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-{color}-500"></div>
                <div class="p-5">
                    <span class="cat-tag bg-{c[0]} dark:bg-{c[2]} text-{c[1]} dark:text-{c[3]} border border-transparent dark:border-{c[4]}">{cat_text}</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">{title}</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">{desc}</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">{date_text}</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
                    </div>
                </div>
            </a>'''

# Pattern 1: Gradient header cards
# Match: <a href="URL" class="block">\n<article ... style="border: 3px solid #COLOR;">...<h3>TITLE</h3>...</article></a>
card_count = 0

# Replace gradient-header cards
pat_gradient = re.compile(
    r'<a href="([^"]+)" class="block">\s*'
    r'<article[^>]*style="[^"]*border:\s*3px solid\s*([^";]+)[^"]*"[^>]*>\s*'
    r'<div class="bg-gradient-to-r[^"]*"[^>]*>\s*'
    r'<span[^>]*>([^<]*)</span>\s*'
    r'<h3[^>]*>(.*?)</h3>\s*'
    r'</div>\s*'
    r'<div class="p-4">\s*'
    r'<p[^>]*>(.*?)</p>\s*'
    r'(?:<div[^>]*>.*?</div>\s*)?'  # optional footer
    r'</div>\s*'
    r'</article>\s*'
    r'</a>',
    re.DOTALL
)

def replace_gradient_card(m):
    global card_count
    href = m.group(1)
    border_color = m.group(2).strip()
    cat_raw = m.group(3).strip()
    title = m.group(4).strip()
    desc = m.group(5).strip()

    color = COLOR_MAP.get(border_color, 'blue')

    # Extract category name and date from "EMOJI Category • Date"
    parts = cat_raw.split('•')
    cat_text = re.sub(r'^[^\w]*', '', parts[0].strip()) if parts else cat_raw
    date_text = parts[1].strip() if len(parts) > 1 else ''

    card_count += 1
    return make_theme_card(href, color, cat_text, title, desc, date_text)

html = pat_gradient.sub(replace_gradient_card, html)
print(f"Transformed {card_count} gradient-header cards")

# Pattern 2: Read-badge cards (older format)
pat_readbadge = re.compile(
    r'<a href="([^"]+)" class="block">\s*'
    r'<article[^>]*style="[^"]*border:\s*3px solid\s*([^";]+)[^"]*"[^>]*>\s*'
    r'<span class="read-badge[^"]*"[^>]*>[^<]*</span>\s*'
    r'<div class="p-6">\s*'
    r'<span class="category-badge[^"]*">([^<]*)</span>\s*'
    r'<h2[^>]*>\s*(.*?)\s*</h2>\s*'
    r'<p[^>]*>\s*(.*?)\s*</p>\s*'
    r'<div[^>]*>\s*<span[^>]*>([^<]*)</span>\s*</div>\s*'
    r'</div>\s*'
    r'</article>\s*'
    r'</a>',
    re.DOTALL
)

rb_count = 0
def replace_readbadge_card(m):
    global rb_count
    href = m.group(1)
    border_color = m.group(2).strip()
    cat_text = re.sub(r'^[^\w]*', '', m.group(3).strip())
    title = m.group(4).strip()
    desc = m.group(5).strip()
    date_raw = m.group(6).strip()
    date_text = re.sub(r'^[^\w]*', '', date_raw)

    color = COLOR_MAP.get(border_color, 'green')
    rb_count += 1
    return make_theme_card(href, color, cat_text, title, desc, date_text)

html = pat_readbadge.sub(replace_readbadge_card, html)
print(f"Transformed {rb_count} read-badge cards")

# ========== 5. DAY SEPARATORS ==========
# Convert <!-- ====== ARTICOLI DATE ====== --> comments to styled separators
date_labels = {
    '6 MARZO 2026': None,  # Skip - already have "Oggi, 6 Marzo" header
    '5 MARZO 2026': '5 Marzo 2026',
    '28 FEBBRAIO 2026': '28 Febbraio 2026',
    '27 FEBBRAIO 2026': '27 Febbraio 2026',
    '24-25 FEBBRAIO 2026': '24-25 Febbraio 2026',
    '19 FEBBRAIO 2026': '19 Febbraio 2026',
    '18 FEBBRAIO 2026': '18 Febbraio 2026',
    '17 FEBBRAIO 2026': '17 Febbraio 2026',
    '14 FEBBRAIO 2026': '14 Febbraio 2026',
}

sep_count = 0
for key, label in date_labels.items():
    marker = f'<!-- ====== ARTICOLI {key} ====== -->'
    if marker in html:
        if label is None:
            # Just remove the comment for today's date (we already have the section header)
            html = html.replace(marker, '')
        else:
            separator = f'''
            <div class="col-span-full flex items-center gap-3 mt-6 mb-2">
                <div class="w-10 h-0.5 rounded-full bg-gray-200 dark:bg-slate-700/40"></div>
                <h2 class="text-sm font-bold montserrat-font text-gray-400 dark:text-slate-600 uppercase tracking-wider">{label}</h2>
                <div class="flex-1 h-0.5 rounded-full bg-gray-100 dark:bg-slate-800/20"></div>
            </div>
'''
            html = html.replace(marker, separator)
            sep_count += 1

print(f"Inserted {sep_count} day separators")

# ========== 6. HANDLE OLDER ARTICLES (10 feb and before) ==========
# These might have different date markers or no markers at all
# Let's find any remaining <!-- ====== ... ====== --> patterns
remaining = re.findall(r'<!-- ====== (.*?) ====== -->', html)
for r in remaining:
    marker = f'<!-- ====== {r} ====== -->'
    label = r.replace('ARTICOLI ', '').title()
    separator = f'''
            <div class="col-span-full flex items-center gap-3 mt-6 mb-2">
                <div class="w-10 h-0.5 rounded-full bg-gray-200 dark:bg-slate-700/40"></div>
                <h2 class="text-sm font-bold montserrat-font text-gray-400 dark:text-slate-600 uppercase tracking-wider">{label}</h2>
                <div class="flex-1 h-0.5 rounded-full bg-gray-100 dark:bg-slate-800/20"></div>
            </div>
'''
    html = html.replace(marker, separator)
    sep_count += 1
    print(f"  Extra separator: {label}")

# ========== 7. REPLACE FOOTER ==========
old_footer_start = '    <!-- Footer -->'
old_footer_end_marker = '    </footer>'
f_start = html.find(old_footer_start)
f_end = html.find(old_footer_end_marker, f_start)
if f_start >= 0 and f_end >= 0:
    f_end += len(old_footer_end_marker)
    new_footer = """    <!-- Footer -->
    <footer class="mt-16 py-12 bg-white dark:bg-transparent border-t border-gray-100 dark:border-slate-800/20 transition-colors">
        <div class="max-w-6xl mx-auto px-4">
            <div class="text-center mb-8">
                <span class="lobster-font text-4xl text-teal-500">A</span>
                <span class="montserrat-font text-2xl font-black text-gray-900 dark:text-white ml-1">LMA FINANZA</span>
            </div>
            <div class="flex flex-wrap justify-center gap-6 md:gap-8 mb-8 text-sm">
                <a href="categoria-wall-street.html" class="text-gray-400 dark:text-slate-600 hover:text-teal-500 transition">Wall Street</a>
                <a href="categoria-borsa-milano.html" class="text-gray-400 dark:text-slate-600 hover:text-teal-500 transition">Borsa Milano</a>
                <a href="categoria-crypto.html" class="text-gray-400 dark:text-slate-600 hover:text-teal-500 transition">Crypto</a>
                <a href="categoria-commodities.html" class="text-gray-400 dark:text-slate-600 hover:text-teal-500 transition">Commodities</a>
                <a href="dashboard.html" class="text-gray-400 dark:text-slate-600 hover:text-teal-500 transition">Dashboard</a>
                <a href="impara-finanza.html" class="text-gray-400 dark:text-slate-600 hover:text-teal-500 transition">Impara</a>
            </div>
            <p class="text-gray-300 dark:text-slate-700 text-center text-sm">&copy; 2026 Alma Finanza. Tutti i diritti riservati.</p>
            <p class="text-gray-200 dark:text-slate-700 text-center text-xs mt-2 max-w-2xl mx-auto">Le informazioni fornite sono a scopo informativo e non costituiscono consulenza finanziaria. Investire comporta rischi.</p>
        </div>
    </footer>"""
    html = html[:f_start] + new_footer + html[f_end:]
    print("Replaced footer")

# ========== 8. RESTYLE TICKER ==========
html = html.replace(
    '<div class="ticker-tape" style="position:relative;">',
    '<div class="ticker-tape py-1.5 bg-gray-50 dark:bg-[#0f1520] border-b border-gray-200 dark:border-slate-800/80" style="position:relative;">'
)
print("Restyled ticker")

# ========== 9. GLOBAL REPLACEMENTS ==========
html = html.replace('max-w-7xl', 'max-w-6xl')
print("Updated max-w to 6xl")

# ========== WRITE ==========
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

total_cards = card_count + rb_count
print(f"\nDone! Total cards transformed: {total_cards}")
print(f"File size: {len(html)} bytes")
