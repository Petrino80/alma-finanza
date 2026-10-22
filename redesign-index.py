#!/usr/bin/env python3
"""
redesign-index.py

Transforms the current index.html into the Modern Minimal design from Preview E.
Reads index.html, rewrites the body content while preserving all article links/data,
and overwrites index.html with the new design.

Usage:
    python3 redesign-index.py
"""

import re
import os

# ──────────────────────────────────────────────────────────
# Color mapping: old border hex -> (tw_accent, tag_bg_light, tag_text_light, tag_bg_dark, tag_text_dark, tag_border_dark)
# ──────────────────────────────────────────────────────────
COLOR_MAP = {
    '#1d4ed8': ('blue-500',   'blue-50',    'blue-700',    'blue-500/15',    'blue-400',    'blue-500/20'),
    '#1e40af': ('blue-500',   'blue-50',    'blue-700',    'blue-500/15',    'blue-400',    'blue-500/20'),
    '#15803d': ('emerald-500','green-50',   'green-700',   'emerald-500/15', 'emerald-400', 'emerald-500/20'),
    '#059669': ('emerald-500','green-50',   'green-700',   'emerald-500/15', 'emerald-400', 'emerald-500/20'),
    '#d97706': ('amber-500',  'amber-50',   'amber-700',   'amber-500/15',   'amber-400',   'amber-500/20'),
    '#dc2626': ('red-500',    'red-50',     'red-700',     'red-500/15',     'red-400',     'red-500/20'),
    '#ef4444': ('red-500',    'red-50',     'red-700',     'red-500/15',     'red-400',     'red-500/20'),
    '#991b1b': ('red-500',    'red-50',     'red-700',     'red-500/15',     'red-400',     'red-500/20'),
    '#7c3aed': ('purple-500', 'purple-50',  'purple-700',  'purple-500/15',  'purple-400',  'purple-500/20'),
    '#0d9488': ('teal-500',   'teal-50',    'teal-700',    'teal-500/15',    'teal-400',    'teal-500/20'),
    '#0369a1': ('sky-500',    'sky-50',     'sky-700',     'sky-500/15',     'sky-400',     'sky-500/20'),
    '#ea580c': ('orange-500', 'orange-50',  'orange-700',  'orange-500/15',  'orange-400',  'orange-500/20'),
    '#f97316': ('orange-500', 'orange-50',  'orange-700',  'orange-500/15',  'orange-400',  'orange-500/20'),
    '#475569': ('slate-500',  'slate-100',  'slate-700',   'slate-500/15',   'slate-400',   'slate-500/20'),
    '#4f46e5': ('indigo-500', 'indigo-50',  'indigo-700',  'indigo-500/15',  'indigo-400',  'indigo-500/20'),
    '#16a34a': ('green-500',  'green-50',   'green-700',   'emerald-500/15', 'emerald-400', 'emerald-500/20'),
    '#1e3a8a': ('blue-500',   'blue-50',    'blue-700',    'blue-500/15',    'blue-400',    'blue-500/20'),
}

# Category badge class -> color hex for fallback
CAT_BADGE_COLOR_MAP = {
    'cat-wall-street': '#1d4ed8',
    'cat-milano':      '#15803d',
    'cat-crypto':      '#d97706',
    'cat-europa':      '#4f46e5',
    'cat-macro':       '#dc2626',
    'cat-tech':        '#7c3aed',
    'cat-commodities': '#d97706',
}

DEFAULT_COLOR = '#16a34a'  # green for read-badge cards with no explicit border color


def get_color_tuple(hex_color):
    """Get color tuple from hex, with fallback to green."""
    hex_color = hex_color.lower().strip()
    if hex_color in COLOR_MAP:
        return COLOR_MAP[hex_color]
    return COLOR_MAP[DEFAULT_COLOR]


def extract_border_color(style_str):
    """Extract border color hex from style attribute."""
    m = re.search(r'border:\s*\d+px\s+solid\s+(#[0-9a-fA-F]+)', style_str or '')
    if m:
        return m.group(1).lower()
    return None


def strip_emojis_prefix(text):
    """Remove leading emoji characters and whitespace from category text."""
    # Remove common emoji patterns at start
    text = text.strip()
    # Remove emoji-like unicode chars at the beginning
    cleaned = re.sub(r'^[\U0001F000-\U0001FFFF\u2600-\u27BF\u2702-\u27B0]+\s*', '', text)
    return cleaned.strip()


def extract_category_text(header_span_text=None, badge_text=None):
    """Extract clean category text from either header span or badge."""
    text = header_span_text or badge_text or 'Finanza'
    # Remove emoji prefixes
    text = strip_emojis_prefix(text)
    # Remove date parts like "• 6 Mar 2026"
    text = re.split(r'\s*[·•]\s*\d+\s', text)[0].strip()
    return text


def extract_date_from_card(card_html):
    """Extract date string from various card formats."""
    # Try gradient-header format: "• 6 Mar 2026" in the span
    m = re.search(r'[·•]\s*(\d+\s+\w+\s+\d{4})', card_html)
    if m:
        return m.group(1).strip()
    # Try read-badge format: date in the footer
    m = re.search(r'(?:🕐\s*)?(\d+\s+\w+\s+\d{4})', card_html)
    if m:
        return m.group(1).strip()
    return ''


def build_new_card(href, title, category, description, date, color_hex):
    """Build a single new theme-card HTML."""
    ct = get_color_tuple(color_hex)
    accent, tag_bg_l, tag_txt_l, tag_bg_d, tag_txt_d, tag_brd_d = ct

    # Escape any HTML entities in title/description
    title = title.strip()
    description = description.strip()
    category = category.strip()
    date = date.strip()

    return f'''            <a href="{href}" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
                <div class="h-1.5 bg-{accent}"></div>
                <div class="p-5">
                    <span class="cat-tag bg-{tag_bg_l} dark:bg-{tag_bg_d} text-{tag_txt_l} dark:text-{tag_txt_d} border border-transparent dark:border-{tag_brd_d}">{category}</span>
                    <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">{title}</h3>
                    <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">{description}</p>
                    <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                        <span class="text-xs text-gray-300 dark:text-slate-600">{date}</span>
                        <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi &rarr;</span>
                    </div>
                </div>
            </a>'''


def parse_gradient_header_card(card_html):
    """Parse a gradient-header style card (newer format with colored gradient header)."""
    # Extract href
    href_m = re.search(r'<a\s+href="([^"]+)"', card_html)
    if not href_m:
        return None
    href = href_m.group(1)

    # Extract border color from style
    style_m = re.search(r'style="[^"]*border:\s*\d+px\s+solid\s+(#[0-9a-fA-F]+)', card_html)
    color_hex = style_m.group(1).lower() if style_m else DEFAULT_COLOR

    # Extract category from the header span (text-xs font-bold uppercase)
    cat_m = re.search(r'<span\s+class="text-xs\s+font-bold\s+uppercase[^"]*"[^>]*>(.*?)</span>', card_html, re.DOTALL)
    category = ''
    if cat_m:
        category = re.sub(r'<[^>]+>', '', cat_m.group(1)).strip()
        category = extract_category_text(header_span_text=category)

    # Extract title from h3
    title_m = re.search(r'<h3[^>]*>(.*?)</h3>', card_html, re.DOTALL)
    title = ''
    if title_m:
        title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip()
        # Normalize whitespace
        title = re.sub(r'\s+', ' ', title)

    # Extract description from p tag in the p-4 div
    desc = ''
    # For the newer format, description is in the div.p-4 > p
    desc_m = re.search(r'<div\s+class="p-4">\s*<p[^>]*>(.*?)</p>', card_html, re.DOTALL)
    if desc_m:
        desc = re.sub(r'<[^>]+>', '', desc_m.group(1)).strip()
        desc = re.sub(r'\s+', ' ', desc)

    # Extract date
    date = extract_date_from_card(card_html)

    return {
        'href': href,
        'title': title,
        'category': category,
        'description': desc,
        'date': date,
        'color_hex': color_hex,
    }


def parse_read_badge_card(card_html):
    """Parse a read-badge style card (older format with badge and no gradient header)."""
    # Extract href
    href_m = re.search(r'<a\s+href="([^"]+)"', card_html)
    if not href_m:
        return None
    href = href_m.group(1)

    # Extract border color from style
    style_m = re.search(r'style="[^"]*border:\s*\d+px\s+solid\s+(#[0-9a-fA-F]+)', card_html)
    color_hex = DEFAULT_COLOR
    if style_m:
        color_hex = style_m.group(1).lower()

    # Extract category from category-badge span
    cat_text = ''
    # First try: <span class="category-badge cat-xxx">TEXT</span>
    cat_m = re.search(r'<span\s+class="category-badge\s*(cat-[\w-]+)?"[^>]*>(.*?)</span>', card_html, re.DOTALL)
    if cat_m:
        cat_class = cat_m.group(1) or ''
        cat_text = re.sub(r'<[^>]+>', '', cat_m.group(2)).strip()
        cat_text = strip_emojis_prefix(cat_text)
        if cat_class:
            # If we got a cat class but no explicit border, use the class mapping
            if color_hex == DEFAULT_COLOR and cat_class in CAT_BADGE_COLOR_MAP:
                color_hex = CAT_BADGE_COLOR_MAP[cat_class]
        else:
            # No cat-* class: try to extract color from the badge's inline style
            badge_color_m = re.search(
                r'<span\s+class="category-badge"[^>]*style="[^"]*background:\s*(?:linear-gradient\([^)]*,\s*)?(#[0-9a-fA-F]+)',
                card_html
            )
            if badge_color_m:
                color_hex = badge_color_m.group(1).lower()

    # Extract title from h2
    title_m = re.search(r'<h2[^>]*>(.*?)</h2>', card_html, re.DOTALL)
    title = ''
    if title_m:
        title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip()
        title = re.sub(r'\s+', ' ', title)

    # Extract description from p.text-gray-600
    desc = ''
    desc_m = re.search(r'<p\s+class="text-gray-600[^"]*"[^>]*>(.*?)</p>', card_html, re.DOTALL)
    if desc_m:
        desc = re.sub(r'<[^>]+>', '', desc_m.group(1)).strip()
        desc = re.sub(r'\s+', ' ', desc)

    # Extract date
    date = extract_date_from_card(card_html)

    return {
        'href': href,
        'title': title,
        'category': cat_text or 'Finanza',
        'description': desc,
        'date': date,
        'color_hex': color_hex,
    }


def parse_all_cards(cards_section):
    """Parse all article cards from the grid section, preserving date separators."""
    results = []  # list of dicts: either {'type': 'separator', 'date_text': ...} or {'type': 'card', ...}

    # Split by date separator comments
    # Pattern: <!-- ====== ARTICOLI DATE ====== --> or <!-- ====== FINE ARTICOLI ... ====== -->
    parts = re.split(r'(<!--\s*=+\s*(?:ARTICOLI|FINE ARTICOLI|Article)\s+.*?=+\s*-->)', cards_section)

    for part in parts:
        part_stripped = part.strip()
        if not part_stripped:
            continue

        # Check if this is a date separator comment
        sep_m = re.match(r'<!--\s*=+\s*ARTICOLI\s+(.*?)\s*=+\s*-->', part_stripped)
        if sep_m:
            date_text = sep_m.group(1).strip()
            results.append({'type': 'separator', 'date_text': date_text})
            continue

        # Check for FINE ARTICOLI - skip these
        if re.match(r'<!--\s*=+\s*FINE ARTICOLI', part_stripped):
            continue

        # Now parse individual card blocks within this part
        # Split into individual card <a> blocks
        # Cards are wrapped in <a href="..." class="block"> ... </a>
        card_blocks = re.findall(
            r'(<a\s+href="[^"]+"\s+class="block">\s*<article.*?</article>\s*</a>)',
            part,
            re.DOTALL
        )

        for card_html in card_blocks:
            # Determine card type: gradient-header or read-badge
            has_gradient_header = bool(re.search(r'bg-gradient-to-r\s+from-', card_html))
            has_read_badge = bool(re.search(r'class="read-badge"', card_html))

            if has_gradient_header and not has_read_badge:
                card_data = parse_gradient_header_card(card_html)
            else:
                card_data = parse_read_badge_card(card_html)

            if card_data:
                card_data['type'] = 'card'
                results.append(card_data)

    return results


def build_day_separator(date_text):
    """Build a day separator HTML element."""
    return f'''
            <div class="col-span-full flex items-center gap-3 mt-4 mb-2">
                <div class="w-10 h-0.5 rounded-full bg-gray-200 dark:bg-slate-700/40"></div>
                <h2 class="text-sm font-bold montserrat-font text-gray-400 dark:text-slate-600 uppercase tracking-wider">{date_text}</h2>
                <div class="flex-1 h-0.5 rounded-full bg-gray-100 dark:bg-slate-800/20"></div>
            </div>'''


# ──────────────────────────────────────────────────────────
# NEW CSS STYLES (replaces old article-card, category-badge, etc.)
# ──────────────────────────────────────────────────────────
NEW_CSS = """        /* Stats Bar */
        .stats-bar{display:flex;gap:1px;border-radius:12px;overflow:hidden;transition:background 0.4s;}
        .stat-item{flex:1;padding:1rem;text-align:center;transition:background 0.4s;}

        /* Theme Cards */
        .theme-card{border-radius:12px;overflow:hidden;transition:all 0.3s ease;}
        .theme-card:hover{transform:translateY(-3px);}

        /* Hero Box */
        .hero-box{border-radius:16px;overflow:hidden;transition:background 0.4s,border-color 0.4s;}

        /* Cat Tags */
        .cat-tag{font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;padding:0.2rem 0.6rem;border-radius:4px;display:inline-block;transition:all 0.4s;}

        /* List Items */
        .list-item{display:flex;align-items:stretch;padding:1.25rem 0;transition:all 0.2s ease;}
        .list-item:hover{margin:0 -1rem;padding-left:1rem;padding-right:1rem;border-radius:8px;}
        .list-item:last-child{border-bottom:none!important;}

        /* Accent */
        .accent-line{width:40px;height:3px;background:#14b8a6;border-radius:2px;}
        .dot{width:8px;height:8px;border-radius:50%;display:inline-block;}"""


# ──────────────────────────────────────────────────────────
# NEW HEADER
# ──────────────────────────────────────────────────────────
NEW_HEADER = """    <!-- Header -->
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
                <div class="text-xs text-gray-400 dark:text-slate-600 hidden md:block">Venerd\u00ec 6 Marzo 2026</div>
                <div class="theme-toggle bg-gray-200 dark:bg-slate-700" onclick="toggleTheme()" title="Cambia tema">
                    <div class="toggle-circle bg-white dark:bg-slate-900 shadow-md">
                        <span class="ico-sun">\u2600\ufe0f</span><span class="ico-moon" style="display:none">\U0001f319</span>
                    </div>
                </div>
            </div>
        </div>
    </header>"""


# ──────────────────────────────────────────────────────────
# STATS BAR
# ──────────────────────────────────────────────────────────
STATS_BAR = """    <div class="max-w-6xl mx-auto px-4 pt-8">
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
    </div>"""


# ──────────────────────────────────────────────────────────
# HERO BOX
# ──────────────────────────────────────────────────────────
HERO_BOX = """        <div class="hero-box bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 mb-10">
            <div class="grid md:grid-cols-3">
                <div class="md:col-span-2 p-8 md:p-12">
                    <div class="flex items-center gap-3 mb-4">
                        <div class="dot bg-red-500 animate-pulse"></div>
                        <span class="text-xs font-bold text-red-600 dark:text-red-400 uppercase tracking-wider">Breaking &middot; 6 Mar 2026</span>
                    </div>
                    <h1 class="text-3xl md:text-4xl font-black text-gray-900 dark:text-white mb-4 leading-tight montserrat-font">
                        Jobs Report shock: -92K posti.<br>WTI a $90.90, record storico settimanale.
                    </h1>
                    <div class="accent-line mb-4"></div>
                    <p class="text-gray-500 dark:text-slate-400 text-lg leading-relaxed mb-6">
                        L'economia USA perde posti di lavoro per la terza volta in 5 mesi. Il petrolio segna +35% nella settimana, il balzo pi&ugrave; grande dal 1983. I mercati reagiscono con vendite diffuse.
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
                        <div class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-red-50 dark:bg-red-500/15 text-red-600 dark:text-red-400 border border-transparent dark:border-red-500/20">
                            Sett. +35.63%
                        </div>
                        <div class="mt-4 space-y-1 text-xs text-gray-400 dark:text-slate-600">
                            <div>Dow -453 &middot; S&amp;P -1.3%</div>
                            <div>NFP -92K &middot; Disocc. 4.4%</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>"""


# ──────────────────────────────────────────────────────────
# SECTION HEADER
# ──────────────────────────────────────────────────────────
SECTION_HEADER = """        <div class="flex items-center gap-3 mb-6">
            <div class="accent-line"></div>
            <h2 class="text-lg font-bold montserrat-font text-gray-900 dark:text-white">Oggi, 6 Marzo</h2>
        </div>"""


# ──────────────────────────────────────────────────────────
# NEW FOOTER
# ──────────────────────────────────────────────────────────
NEW_FOOTER = """    <!-- Footer -->
    <footer class="mt-16 py-12 bg-white dark:bg-transparent border-t border-gray-100 dark:border-slate-800/20 transition-colors">
        <div class="max-w-6xl mx-auto px-4">
            <div class="text-center mb-8">
                <span class="lobster-font text-4xl text-teal-500">A</span>
                <span class="montserrat-font text-2xl font-black text-gray-900 dark:text-white">LMA FINANZA</span>
            </div>
            <div class="flex justify-center gap-8 mb-8 text-sm">
                <a href="categoria-wall-street.html" class="text-gray-400 dark:text-slate-600 hover:text-teal-500 transition">Wall Street</a>
                <a href="categoria-borsa-milano.html" class="text-gray-400 dark:text-slate-600 hover:text-teal-500 transition">Borsa Milano</a>
                <a href="categoria-crypto.html" class="text-gray-400 dark:text-slate-600 hover:text-teal-500 transition">Crypto</a>
                <a href="categoria-commodities.html" class="text-gray-400 dark:text-slate-600 hover:text-teal-500 transition">Commodities</a>
                <a href="dashboard.html" class="text-gray-400 dark:text-slate-600 hover:text-teal-500 transition">Dashboard</a>
                <a href="impara-finanza.html" class="text-gray-400 dark:text-slate-600 hover:text-teal-500 transition">Impara</a>
            </div>
            <p class="text-gray-300 dark:text-slate-700 text-center text-sm">&copy; 2026 Alma Finanza. Tutti i diritti riservati.</p>
            <p class="text-gray-200 dark:text-slate-700 text-center text-xs mt-2">Le informazioni fornite sono a scopo informativo e non costituiscono consulenza finanziaria.</p>
        </div>
    </footer>"""


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(script_dir, 'index.html')

    if not os.path.exists(index_path):
        print(f"ERROR: {index_path} not found!")
        return

    with open(index_path, 'r', encoding='utf-8') as f:
        html = f.read()

    print(f"Read {len(html)} bytes from index.html")

    # ──────────────────────────────────────────────────────
    # STEP 1: Replace old CSS styles in <style> block
    # ──────────────────────────────────────────────────────
    # Remove old article-card, category-badge, read-badge, vertical-switch, cat-* styles
    # and old dark mode overrides, replace with new CSS

    # Find the <style> block
    style_start = html.find('<style>')
    style_end = html.find('</style>')

    if style_start == -1 or style_end == -1:
        print("ERROR: Could not find <style> block!")
        return

    old_style_content = html[style_start + 7:style_end]

    # Remove old CSS classes and replace with new ones
    # We'll rebuild the style block keeping essential base styles

    new_style_content = """
        /* Previeni scroll orizzontale */
        html, body {
            max-width: 100%;
            overflow-x: hidden;
        }

        body {
            font-family: 'Inter', sans-serif;
            transition: background-color 0.4s ease, color 0.4s ease;
        }
        .lobster-font {
            font-family: 'Lobster', cursive;
        }
        .montserrat-font {
            font-family: 'Montserrat', sans-serif;
        }

        /* ===== TICKER ===== */
        .ticker-tape{overflow:hidden;transition:background 0.4s,border-color 0.4s;}
        .ticker-content{display:flex;animation:scroll 30s linear infinite;}
        @keyframes scroll{0%{transform:translateX(0);}100%{transform:translateX(-50%);}}
        .ticker-item{padding:0 1.5rem;white-space:nowrap;font-weight:500;font-size:0.8rem;transition:color 0.4s;}
        .ticker-item a{text-decoration:none;transition:color 0.2s;}

        /* ===== COLORS ===== */
        .positive{color:#16a34a;font-weight:600;}
        .negative{color:#dc2626;font-weight:600;}
        .dark .positive{color:#34d399;}
        .dark .negative{color:#f87171;}

""" + NEW_CSS + """

        /* ===== THEME TOGGLE ===== */
        .theme-toggle{position:relative;width:56px;height:28px;border-radius:14px;cursor:pointer;transition:background 0.4s;display:inline-flex;align-items:center;}
        .theme-toggle .toggle-circle{position:absolute;top:3px;left:3px;width:22px;height:22px;border-radius:50%;transition:transform 0.4s cubic-bezier(0.68,-0.55,0.27,1.55),background 0.4s;display:flex;align-items:center;justify-content:center;font-size:12px;}
        .dark .theme-toggle .toggle-circle{transform:translateX(28px);}
    """

    html = html[:style_start + 7] + new_style_content + html[style_end:]

    print("Replaced CSS styles")

    # ──────────────────────────────────────────────────────
    # STEP 2: Replace ticker tape styling
    # ──────────────────────────────────────────────────────
    # Find the ticker tape div and restyle it
    # Old: <div class="ticker-tape" style="position:relative;">
    # New: <div class="ticker-tape py-1.5 bg-gray-50 dark:bg-[#0f1520] border-b border-gray-200 dark:border-slate-800/80" style="position:relative;">
    html = re.sub(
        r'<div\s+class="ticker-tape"(\s+style="position:relative;")',
        r'<div class="ticker-tape py-1.5 bg-gray-50 dark:bg-[#0f1520] border-b border-gray-200 dark:border-slate-800/80"\1',
        html
    )
    print("Restyled ticker tape")

    # ──────────────────────────────────────────────────────
    # STEP 3: Replace header + nav with new single-row header
    # ──────────────────────────────────────────────────────
    # Find and replace from <!-- Header --> to end of </nav>
    # The header starts at "<!-- Header -->" and nav ends at "</nav>"
    header_start = html.find('<!-- Header -->')
    nav_end = html.find('</nav>')
    if header_start == -1 or nav_end == -1:
        print("WARNING: Could not find header/nav markers, trying alternative approach")
        # Try finding just the header
        header_start = html.find('<header')
        nav_end = html.find('</nav>')
        if nav_end == -1:
            # No nav bar, just replace the header
            header_end = html.find('</header>')
            if header_end != -1:
                nav_end = header_end + len('</header>') - len('</nav>') - 1

    if header_start != -1 and nav_end != -1:
        # Include the closing </nav> tag
        nav_end_full = nav_end + len('</nav>')
        html = html[:header_start] + NEW_HEADER + '\n' + html[nav_end_full:]
        print("Replaced header and removed nav bar")
    else:
        print("WARNING: Could not replace header/nav")

    # ──────────────────────────────────────────────────────
    # STEP 4: Replace hero + breaking news badge + section header
    #         and insert stats bar before main
    # ──────────────────────────────────────────────────────

    # First, replace the main tag to use max-w-6xl
    html = html.replace(
        '<main class="max-w-7xl mx-auto px-4 py-8">',
        '<main class="max-w-6xl mx-auto px-4 py-8">'
    )

    # Insert stats bar right after main opening tag but before the hero
    main_tag_end = html.find('<main class="max-w-6xl mx-auto px-4 py-8">')
    if main_tag_end != -1:
        # We insert stats bar BEFORE main, and adjust
        # Actually, looking at the Preview E structure, stats bar is outside main, after header
        # Let's insert it between header closing and main opening
        main_tag = '<main class="max-w-6xl mx-auto px-4 py-8">'
        insert_pos = html.find(main_tag)
        if insert_pos != -1:
            html = html[:insert_pos] + STATS_BAR + '\n\n    ' + html[insert_pos:]
            print("Inserted stats bar")

    # Now find and replace the hero article section
    # It starts at "<!-- Hero Article -->" and ends before "<!-- Breaking News Badge -->"
    hero_start = html.find('<!-- Hero Article -->')
    if hero_start == -1:
        # Try alternative
        hero_start = html.find('<!-- Main Content -->')
        if hero_start != -1:
            # Skip past the main tag
            hero_start = html.find('<article', hero_start)

    breaking_start = html.find('<!-- Breaking News Badge -->')
    articles_grid_start = html.find('<!-- Articles Grid -->')

    if hero_start == -1:
        # Find the hero article by its distinctive class
        hero_start = html.find('<article class="bg-white rounded-lg shadow-lg overflow-hidden mb-8 article-card')

    if hero_start != -1 and breaking_start != -1:
        # Replace from hero article through breaking badge and "Articoli" header
        # to just before the articles grid
        if articles_grid_start != -1:
            # Replace everything from hero_start to articles_grid_start with new hero + section header
            html = html[:hero_start] + HERO_BOX + '\n\n' + SECTION_HEADER + '\n\n' + html[articles_grid_start:]
            print("Replaced hero + breaking badge + section header")
        else:
            print("WARNING: Could not find Articles Grid marker")
    elif hero_start != -1:
        # Try to find the end of the hero article
        hero_end = html.find('</article>', hero_start)
        if hero_end != -1:
            hero_end = html.find('</a>', hero_end) + len('</a>')
            # Also remove breaking badge if it follows
            next_content = html[hero_end:hero_end + 500]
            badge_m = re.search(r'\s*<!-- Breaking News Badge -->.*?</span>\s*</div>', next_content, re.DOTALL)
            if badge_m:
                hero_end += badge_m.end()
            # Also find and replace the articles header
            header_m = re.search(r'\s*<h2[^>]*>.*?Articoli Ultimi 7 Giorni.*?</h2>', next_content, re.DOTALL)

            html = html[:hero_start] + HERO_BOX + '\n\n' + SECTION_HEADER + '\n\n' + html[hero_end:]
            print("Replaced hero section (alt approach)")

    # ──────────────────────────────────────────────────────
    # STEP 5: Replace articles grid class
    # ──────────────────────────────────────────────────────
    html = html.replace(
        '<div class="grid md:grid-cols-3 gap-6">',
        '<div class="grid md:grid-cols-3 gap-5">'
    )
    print("Updated grid gap")

    # ──────────────────────────────────────────────────────
    # STEP 6: Parse and transform all cards
    # ──────────────────────────────────────────────────────
    # Find the articles grid section
    grid_start_marker = '<div class="grid md:grid-cols-3 gap-5">'
    grid_start = html.find(grid_start_marker)
    if grid_start == -1:
        print("ERROR: Could not find articles grid!")
        return

    # Find the closing </div> of the grid (it's the one right before the Mission Section)
    # We need to find the matching closing div
    grid_content_start = grid_start + len(grid_start_marker)

    # Find the end of the grid - it's before <!-- Mission Section -->
    mission_marker = '<!-- Mission Section -->'
    mission_pos = html.find(mission_marker)
    if mission_pos == -1:
        print("ERROR: Could not find Mission Section marker!")
        return

    # The grid closes with </div> before mission section
    # Search backwards from mission_pos for the grid closing </div>
    # The pattern is: </div>\n\n followed by mission section area
    # Actually, let's find the </div> that closes the grid
    # We know the structure: after all cards there's a closing </div> then some sections

    # Find the last </a> tag before mission, then the next </div>
    pre_mission = html[grid_content_start:mission_pos]

    # Find the closing div of the grid - it's the last </div> before mission section
    # that matches the grid opening
    last_close_div = pre_mission.rfind('</div>')
    if last_close_div == -1:
        print("ERROR: Could not find grid closing div!")
        return

    grid_content = pre_mission[:last_close_div]
    grid_end_pos = grid_content_start + last_close_div

    print(f"Found grid content: {len(grid_content)} chars")

    # Parse all cards
    parsed = parse_all_cards(grid_content)
    print(f"Parsed {len(parsed)} items (cards + separators)")

    # Count cards vs separators
    card_count = sum(1 for p in parsed if p['type'] == 'card')
    sep_count = sum(1 for p in parsed if p['type'] == 'separator')
    print(f"  Cards: {card_count}, Separators: {sep_count}")

    # Build the new grid content
    new_grid_lines = ['\n']
    first_separator = True

    for item in parsed:
        if item['type'] == 'separator':
            if first_separator:
                # The first separator (6 MARZO 2026) is already covered by section header
                first_separator = False
                new_grid_lines.append(f'\n            <!-- ====== ARTICOLI {item["date_text"]} ====== -->\n')
                continue
            new_grid_lines.append(f'\n            <!-- ====== ARTICOLI {item["date_text"]} ====== -->')
            new_grid_lines.append(build_day_separator(item['date_text']))
            new_grid_lines.append('')
        elif item['type'] == 'card':
            new_grid_lines.append(build_new_card(
                item['href'],
                item['title'],
                item['category'],
                item['description'],
                item['date'],
                item['color_hex']
            ))
            new_grid_lines.append('')

    new_grid_content = '\n'.join(new_grid_lines)

    # Replace the grid content
    html = html[:grid_content_start] + new_grid_content + '\n        ' + html[grid_end_pos:]
    print("Replaced all cards with new theme-card format")

    # ──────────────────────────────────────────────────────
    # STEP 7: Replace footer
    # ──────────────────────────────────────────────────────
    footer_start = html.find('<!-- Footer -->')
    if footer_start == -1:
        footer_start = html.find('<footer')

    if footer_start != -1:
        footer_end = html.find('</footer>')
        if footer_end != -1:
            footer_end += len('</footer>')
            html = html[:footer_start] + NEW_FOOTER + '\n' + html[footer_end:]
            print("Replaced footer")
    else:
        print("WARNING: Could not find footer")

    # ──────────────────────────────────────────────────────
    # STEP 8: Update remaining max-w-7xl references
    # ──────────────────────────────────────────────────────
    html = html.replace('max-w-7xl', 'max-w-6xl')
    print("Updated all max-w-7xl to max-w-6xl")

    # ──────────────────────────────────────────────────────
    # STEP 9: Clean up any remaining old class references
    # ──────────────────────────────────────────────────────
    # Make sure body has correct classes
    html = re.sub(
        r'<body\s+class="[^"]*"',
        '<body class="bg-white dark:bg-[#0c1017] text-gray-900 dark:text-slate-300 transition-colors duration-300"',
        html
    )
    print("Updated body classes")

    # ──────────────────────────────────────────────────────
    # Write the output
    # ──────────────────────────────────────────────────────
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"\nDone! Wrote {len(html)} bytes to {index_path}")
    print("Transformation complete: index.html now uses the Modern Minimal (Preview E) design.")


if __name__ == '__main__':
    main()
