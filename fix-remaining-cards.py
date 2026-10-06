#!/usr/bin/env python3
"""Fix remaining old-style cards that weren't caught by redesign-v2.py."""
import re, os

BASE = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE, 'index.html')

with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Category to color mapping
CAT_COLORS = {
    'wall-street': 'blue',
    'macro': 'red',
    'tech': 'purple',
    'crypto': 'amber',
    'commodities': 'amber',
    'italia': 'emerald',
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
    'green': ('green-50', 'green-700', 'green-500/15', 'green-400', 'green-500/20'),
}

def get_color_from_cat(cat_class):
    """Extract color from category-badge class like 'cat-wall-street'."""
    for key, color in CAT_COLORS.items():
        if key in cat_class:
            return color
    return 'blue'

def make_theme_card(href, color, cat_text, title, desc, date_text):
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

# Pattern for remaining read-badge cards (position: relative, no border color)
# Also handles cards with style="position: relative; border: 3px solid ..."
pat = re.compile(
    r'<a href="([^"]+)" class="block">\s*'
    r'<article[^>]*>\s*'
    r'(?:<span class="read-badge[^"]*"[^>]*>[^<]*</span>\s*)?'
    r'<div class="p-6">\s*'
    r'<span class="category-badge\s+(cat-[^"]*)"[^>]*>([^<]*)</span>\s*'
    r'<h2[^>]*>\s*(.*?)\s*</h2>\s*'
    r'<p[^>]*>\s*(.*?)\s*</p>\s*'
    r'<div[^>]*>\s*<span[^>]*>([^<]*)</span>\s*'
    r'(?:<span[^>]*>[^<]*</span>\s*)?'
    r'</div>\s*'
    r'</div>\s*'
    r'</article>\s*'
    r'</a>',
    re.DOTALL
)

count = 0
def replace_card(m):
    global count
    href = m.group(1)
    cat_class = m.group(2)
    cat_text = re.sub(r'^[^\w]*', '', m.group(3).strip())
    title = m.group(4).strip()
    desc = m.group(5).strip()
    date_raw = m.group(6).strip()
    date_text = re.sub(r'^[^\w]*', '', date_raw)

    color = get_color_from_cat(cat_class)
    count += 1
    return make_theme_card(href, color, cat_text, title, desc, date_text)

html = pat.sub(replace_card, html)
print(f"Transformed {count} remaining cards")

# Check for any still remaining old cards
remaining_old = len(re.findall(r'class="[^"]*article-card', html))
remaining_badge = len(re.findall(r'class="read-badge', html))
print(f"Remaining old article-card: {remaining_old}")
print(f"Remaining read-badge: {remaining_badge}")

# Also handle any remaining date section markers
remaining_markers = re.findall(r'<!-- (Article \d+[^-]+-[^>]*) -->', html)
if remaining_markers:
    print(f"Found {len(remaining_markers)} article comment markers (these are fine)")

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nDone! File size: {len(html)} bytes")
