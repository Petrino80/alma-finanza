#!/usr/bin/env python3
"""
Fix script for dark mode issues found during audit:
1. Add anti-flash script to all structural pages (missing from structural script)
2. Add toggle button to category pages and simple pages (missing from structural script)
3. Fix index.html Mission, Disclaimer, Newsletter sections for dark mode
4. Fix footer text colors on articles (inverted light/dark)
"""

import glob
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ANTI_FLASH_SCRIPT = '    <script>(function(){var t=localStorage.getItem(\'alma-theme\');if(t===\'dark\'||(!t&&window.matchMedia(\'(prefers-color-scheme:dark)\').matches))document.documentElement.classList.add(\'dark\')})()</script>'

TOGGLE_HTML = '''                <div class="theme-toggle bg-gray-200 dark:bg-slate-700" onclick="toggleTheme()" title="Cambia tema">
                    <div class="toggle-circle bg-white dark:bg-slate-900 shadow-md">
                        <span class="ico-sun">☀️</span><span class="ico-moon" style="display:none">🌙</span>
                    </div>
                </div>'''


def fix_anti_flash(content, filename):
    """Add anti-flash script after GA config if missing."""
    if "alma-theme" in content and "localStorage.getItem" in content.split('</head>')[0]:
        print(f"    ✓ Anti-flash already present in {filename}")
        return content

    # Try inserting after GA config
    ga_patterns = [
        "gtag('config','G-E88FFDTPMP');</script>",
        "gtag('config', 'G-E88FFDTPMP');</script>",
    ]

    for ga in ga_patterns:
        if ga in content:
            content = content.replace(ga, ga + '\n' + ANTI_FLASH_SCRIPT)
            print(f"    ✅ Added anti-flash script to {filename}")
            return content

    print(f"    ⚠️  Could not find GA pattern in {filename}")
    return content


def fix_category_toggle(content, filename):
    """Add toggle button to category page headers."""
    if 'toggleTheme()' in content and 'theme-toggle' in content.split('</header>')[0]:
        print(f"    ✓ Toggle already present in header of {filename}")
        return content

    # Category pages have: </nav>\n            </div>\n        </div>\n    </header>
    # We need to add toggle after </nav> and wrap nav + toggle in a flex container

    # Pattern: the nav element in category pages
    nav_match = re.search(
        r'(                <!-- Navigation -->\n                <nav class="flex space-x-6 text-sm font-semibold">.*?</nav>)',
        content, re.DOTALL
    )

    if nav_match:
        old_nav = nav_match.group(1)
        # Add dark classes to nav links
        new_nav = old_nav
        new_nav = new_nav.replace(
            'class="text-gray-600 hover:text-teal-600"',
            'class="text-gray-600 dark:text-slate-400 hover:text-teal-600 dark:hover:text-teal-400"'
        )
        # Add toggle after nav
        new_nav_with_toggle = new_nav + '\n' + TOGGLE_HTML
        content = content.replace(old_nav, new_nav_with_toggle)
        print(f"    ✅ Added toggle button to {filename}")
    else:
        print(f"    ⚠️  Could not find nav pattern in {filename}")

    return content


def fix_simple_page_toggle(content, filename):
    """Add toggle button to simple pages (dashboard, quote, impara-finanza, in-costruzione)."""
    if 'toggleTheme()' in content and 'theme-toggle' in content.split('</header>')[0]:
        print(f"    ✓ Toggle already present in header of {filename}")
        return content

    # Simple pages have various header structures - find the closing of header nav area
    # Pattern: look for "Torna alla Home</a>" link and add toggle after it
    torna_pattern = re.search(
        r'(<a href="index\.html"[^>]*>[^<]*(?:Torna alla Home|Home)[^<]*</a>)',
        content
    )

    if torna_pattern:
        old_link = torna_pattern.group(1)
        # Wrap in flex container with toggle
        new_section = old_link + '\n' + TOGGLE_HTML
        content = content.replace(old_link, new_section, 1)
        print(f"    ✅ Added toggle button to {filename}")
    else:
        print(f"    ⚠️  Could not find nav link in {filename}")

    return content


def fix_index_sections(content):
    """Fix Mission, Disclaimer, and Newsletter sections in index.html for dark mode."""

    # Fix Mission section
    content = content.replace(
        '<section class="bg-white rounded-lg shadow-xl overflow-hidden my-16 border-t-4 border-teal-500">',
        '<section class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow-xl dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden my-16 border-t-4 border-teal-500 transition-colors duration-300">'
    )

    # Fix the quote box inside Mission
    content = content.replace(
        'class="bg-gradient-to-r from-teal-50 to-blue-50 rounded-xl p-6 mb-8 border-l-4 border-teal-500"',
        'class="bg-gradient-to-r from-teal-50 to-blue-50 dark:from-slate-800 dark:to-slate-900 rounded-xl p-6 mb-8 border-l-4 border-teal-500 transition-colors duration-300"'
    )

    # Fix quote text
    content = content.replace(
        '<p class="text-gray-800 italic text-lg leading-relaxed">',
        '<p class="text-gray-800 dark:text-slate-300 italic text-lg leading-relaxed">'
    )

    # Fix teal-100 checkmark backgrounds for dark mode
    content = content.replace(
        'class="w-6 h-6 bg-teal-100 rounded-full flex items-center justify-center flex-shrink-0 mt-1"',
        'class="w-6 h-6 bg-teal-100 dark:bg-teal-900/40 rounded-full flex items-center justify-center flex-shrink-0 mt-1"'
    )

    # Fix Disclaimer section
    content = content.replace(
        '<section class="bg-gradient-to-br from-amber-50 to-orange-50 rounded-lg shadow p-4 mt-12 border-l-4 border-amber-500">',
        '<section class="bg-gradient-to-br from-amber-50 to-orange-50 dark:from-amber-950/30 dark:to-orange-950/30 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] p-4 mt-12 border-l-4 border-amber-500 transition-colors duration-300">'
    )

    # Fix disclaimer text
    content = content.replace(
        '<h3 class="text-base font-bold text-gray-900 mb-2 montserrat-font">Disclaimer Legale</h3>',
        '<h3 class="text-base font-bold text-gray-900 dark:text-amber-200 mb-2 montserrat-font">Disclaimer Legale</h3>'
    )

    # Fix disclaimer paragraph
    content = content.replace(
        '<p class="text-xs text-gray-700 leading-relaxed">',
        '<p class="text-xs text-gray-700 dark:text-slate-400 leading-relaxed">'
    )

    # Fix Newsletter CTA input
    content = content.replace(
        'class="flex-1 px-4 py-3 rounded-lg text-gray-900"',
        'class="flex-1 px-4 py-3 rounded-lg text-gray-900 dark:bg-slate-800 dark:text-white dark:placeholder-slate-500"'
    )

    # Fix Newsletter CTA button
    content = content.replace(
        'class="bg-white text-teal-600 px-6 py-3 rounded-lg font-semibold hover:bg-gray-100 transition">',
        'class="bg-white dark:bg-slate-900 text-teal-600 dark:text-teal-400 px-6 py-3 rounded-lg font-semibold hover:bg-gray-100 dark:hover:bg-slate-800 transition">'
    )

    print("    ✅ Fixed Mission, Disclaimer, Newsletter sections")
    return content


def fix_article_footer(content, filename):
    """Fix inverted footer text colors in articles."""
    changed = False

    # Fix footer copyright line - text-gray-300 is too light for light mode
    if 'class="text-gray-300 dark:text-slate-600' in content:
        content = content.replace(
            'class="text-gray-300 dark:text-slate-600',
            'class="text-gray-500 dark:text-slate-600'
        )
        changed = True

    # Fix footer disclaimer - text-gray-200 is too light for light mode
    if 'class="text-gray-200 dark:text-slate-700' in content:
        content = content.replace(
            'class="text-gray-200 dark:text-slate-700',
            'class="text-gray-400 dark:text-slate-700'
        )
        changed = True

    if changed:
        print(f"    ✅ Fixed footer text colors in {filename}")

    return content


def main():
    print(f"\n{'='*60}")
    print(f"  Alma Finanza — Dark Mode Fix Script")
    print(f"{'='*60}\n")

    # 1. Fix index.html
    print("📄 index.html:")
    index_path = os.path.join(BASE_DIR, 'index.html')
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = fix_anti_flash(content, 'index.html')
    content = fix_index_sections(content)
    content = fix_article_footer(content, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

    # 2. Fix category pages
    print("\n📁 Categorie:")
    categories = [
        'categoria-wall-street.html',
        'categoria-borsa-milano.html',
        'categoria-crypto.html',
        'categoria-commodities.html',
    ]
    for cat in categories:
        path = os.path.join(BASE_DIR, cat)
        if not os.path.exists(path):
            print(f"    ⚠️  {cat} not found")
            continue
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = fix_anti_flash(content, cat)
        content = fix_category_toggle(content, cat)
        content = fix_article_footer(content, cat)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

    # 3. Fix simple pages
    print("\n📄 Altre pagine:")
    simple_pages = [
        'dashboard.html',
        'quote.html',
        'impara-finanza.html',
        'in-costruzione.html',
    ]
    for page in simple_pages:
        path = os.path.join(BASE_DIR, page)
        if not os.path.exists(path):
            print(f"    ⚠️  {page} not found")
            continue
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = fix_anti_flash(content, page)
        content = fix_simple_page_toggle(content, page)
        content = fix_article_footer(content, page)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

    # 4. Fix article footer text colors
    print("\n📰 Articoli (fix footer colors):")
    articles = sorted(glob.glob(os.path.join(BASE_DIR, 'articolo-*.html')))
    fixed = 0
    for filepath in articles:
        fname = os.path.basename(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        old_content = content
        content = fix_article_footer(content, fname)
        if content != old_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            fixed += 1

    print(f"\n    {fixed} articoli con footer corretto")

    print(f"\n{'='*60}")
    print(f"  Completato!")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
