#!/usr/bin/env python3
"""
Alma Finanza — Dark Mode per pagine strutturali (index.html, categorie, ecc.)
"""
import os, re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ANTI_FLASH = '    <script>(function(){var t=localStorage.getItem("alma-theme");if(t==="dark"||(!t&&window.matchMedia("(prefers-color-scheme:dark)").matches))document.documentElement.classList.add("dark")})()</script>'

TAILWIND_DARK = '    <script>tailwind.config={darkMode:"class"}</script>'

TOGGLE_JS = '''    <script>
    function toggleTheme(){var h=document.documentElement,d=h.classList.contains('dark');if(d){h.classList.remove('dark');localStorage.setItem('alma-theme','light')}else{h.classList.add('dark');localStorage.setItem('alma-theme','dark')}updateIcons()}
    function updateIcons(){var d=document.documentElement.classList.contains('dark');document.querySelectorAll('.ico-sun').forEach(function(e){e.style.display=d?'none':'inline'});document.querySelectorAll('.ico-moon').forEach(function(e){e.style.display=d?'inline':'none'})}
    window.matchMedia('(prefers-color-scheme:dark)').addEventListener('change',function(e){if(!localStorage.getItem('alma-theme')){if(e.matches)document.documentElement.classList.add('dark');else document.documentElement.classList.remove('dark');updateIcons()}});
    updateIcons();
    </script>'''

# Toggle HTML snippet
TOGGLE_HTML = '''<div class="theme-toggle bg-gray-200 dark:bg-slate-700" onclick="toggleTheme()" title="Cambia tema"><div class="toggle-circle bg-white dark:bg-slate-900 shadow-md"><span class="ico-sun">☀️</span><span class="ico-moon" style="display:none">🌙</span></div></div>'''

# Dark CSS for index and categories
INDEX_DARK_CSS = '''
        /* === DARK MODE === */
        .dark .ticker-tape{background:linear-gradient(to right,#0c1017,#0f1520)!important;border-color:rgba(20,184,166,0.2)!important;}
        .dark .ticker-item{color:#64748b;}
        .dark .ticker-item a{color:#64748b;}
        .dark .ticker-item a:hover{color:#14b8a6;}
        .dark .positive{color:#34d399!important;}
        .dark .negative{color:#f87171!important;}
        .dark .article-card{background:rgba(15,23,42,0.6)!important;border-color:rgba(51,65,85,0.3)!important;}
        .dark .article-card:hover{border-color:rgba(20,184,166,0.4)!important;box-shadow:0 4px 24px rgba(0,0,0,0.3)!important;}
        .dark .article-card p{color:#94a3b8!important;}
        .dark .article-card h3{color:#f1f5f9!important;}
        .dark .shadow-sm,.dark .shadow-md,.dark .shadow-lg{box-shadow:0 4px 24px rgba(0,0,0,0.3)!important;}
        .dark .bg-gray-50{background:#0c1017!important;}
        .dark .bg-white{background:rgba(15,23,42,0.6)!important;}
        .dark .text-gray-900{color:#f1f5f9!important;}
        .dark .text-gray-600,.dark .text-gray-700{color:#94a3b8!important;}
        .dark .text-gray-500{color:#64748b!important;}
        .dark .text-gray-400{color:#475569!important;}
        .dark .border-gray-200,.dark .border-gray-100{border-color:rgba(51,65,85,0.2)!important;}
        .dark .vertical-switch{background:rgba(30,41,59,0.6)!important;}
        .dark .vertical-switch button{color:#94a3b8;}
        .dark .vertical-switch button.active{background:#14b8a6;color:white;}
        .dark .category-badge{opacity:0.9;}
        .dark .read-badge{box-shadow:0 4px 6px rgba(20,184,166,0.2)!important;}
        .theme-toggle{position:relative;width:52px;height:28px;border-radius:14px;cursor:pointer;transition:background 0.4s;display:inline-flex;align-items:center;}
        .theme-toggle .toggle-circle{position:absolute;top:3px;left:3px;width:22px;height:22px;border-radius:50%;transition:transform 0.4s cubic-bezier(0.68,-0.55,0.27,1.55),background 0.4s;display:flex;align-items:center;justify-content:center;font-size:12px;}
        .dark .theme-toggle .toggle-circle{transform:translateX(24px);}'''


def process_index(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()

    if 'alma-theme' in c:
        print(f"  SKIP (already done): {os.path.basename(filepath)}")
        return False

    # 1. Tailwind dark config
    c = c.replace(
        '<script src="https://cdn.tailwindcss.com"></script>',
        '<script src="https://cdn.tailwindcss.com"></script>\n' + TAILWIND_DARK
    )

    # 2. Anti-flash script
    # After GA config
    for ga in ["gtag('config', 'G-E88FFDTPMP');</script>", "gtag('config','G-E88FFDTPMP');</script>"]:
        if ga in c:
            c = c.replace(ga, ga + '\n' + ANTI_FLASH)
            break

    # 3. Dark CSS before </style>
    c = c.replace('    </style>', INDEX_DARK_CSS + '\n    </style>')

    # 4. Body class
    c = c.replace(
        '<body class="bg-gray-50">',
        '<body class="bg-white dark:bg-[#0c1017] transition-colors duration-300">'
    )

    # 5. Header - add dark classes + toggle
    # index.html header pattern
    c = c.replace(
        '<header class="bg-white border-b-2 border-gray-200 sticky top-0 z-50 shadow-sm">',
        '<header class="bg-white/92 dark:bg-[#0c1017]/92 backdrop-blur-xl border-b border-gray-100 dark:border-slate-800/20 sticky top-0 z-50 shadow-sm dark:shadow-none transition-colors duration-300">'
    )

    # Logo dark text
    c = c.replace(
        '<div class="text-lg md:text-2xl font-bold text-gray-900">lma Finanza</div>',
        '<div class="text-lg md:text-2xl font-bold text-gray-900 dark:text-white">lma Finanza</div>'
    )

    # Date text dark
    c = c.replace(
        '<div class="text-xs md:text-sm text-gray-600 montserrat-font">',
        '<div class="text-xs md:text-sm text-gray-600 dark:text-slate-500 montserrat-font">'
    )

    # Add toggle after date div - find the closing of the date/header area
    # Insert toggle before the date div
    c = c.replace(
        '''                <!-- Date - Compact on mobile -->
                <div class="text-xs md:text-sm text-gray-600 dark:text-slate-500 montserrat-font">''',
        f'''                <!-- Theme Toggle + Date -->
                <div class="flex items-center gap-3">
                    {TOGGLE_HTML}
                    <div class="text-xs md:text-sm text-gray-600 dark:text-slate-500 montserrat-font">'''
    )
    # Close the extra div
    c = c.replace(
        '''                    <span class="hidden md:inline"> • Aggiornato oggi</span>
                </div>
            </div>
        </div>
    </header>''',
        '''                    <span class="hidden md:inline"> • Aggiornato oggi</span>
                    </div>
                </div>
            </div>
        </div>
    </header>'''
    )

    # 6. Nav bar dark
    c = c.replace(
        '<nav class="bg-gray-50 border-b border-gray-200 py-3',
        '<nav class="bg-gray-50 dark:bg-[#0f1520] border-b border-gray-200 dark:border-slate-800/20 py-3'
    )
    # Nav links
    c = c.replace(
        'class="text-sm font-bold text-gray-900 montserrat-font">📂 Sezioni:</span>',
        'class="text-sm font-bold text-gray-900 dark:text-slate-300 montserrat-font">📂 Sezioni:</span>'
    )
    c = c.replace(
        'class="text-sm font-bold text-gray-900 montserrat-font">📚 Risorse:</span>',
        'class="text-sm font-bold text-gray-900 dark:text-slate-300 montserrat-font">📚 Risorse:</span>'
    )
    # All nav text-gray-700 links
    c = c.replace(
        'class="text-sm text-gray-700 hover:text-teal-600 transition">Wall Street</a>',
        'class="text-sm text-gray-700 dark:text-slate-400 hover:text-teal-600 dark:hover:text-teal-400 transition">Wall Street</a>'
    )
    c = c.replace(
        'class="text-sm text-gray-700 hover:text-teal-600 transition">Borsa Milano</a>',
        'class="text-sm text-gray-700 dark:text-slate-400 hover:text-teal-600 dark:hover:text-teal-400 transition">Borsa Milano</a>'
    )
    c = c.replace(
        'class="text-sm text-gray-700 hover:text-teal-600 transition">Crypto</a>',
        'class="text-sm text-gray-700 dark:text-slate-400 hover:text-teal-600 dark:hover:text-teal-400 transition">Crypto</a>'
    )
    c = c.replace(
        'class="text-sm text-gray-700 hover:text-teal-600 transition">Commodities</a>',
        'class="text-sm text-gray-700 dark:text-slate-400 hover:text-teal-600 dark:hover:text-teal-400 transition">Commodities</a>'
    )
    c = c.replace(
        'class="text-sm text-gray-700 hover:text-teal-600 transition">Impara la Finanza</a>',
        'class="text-sm text-gray-700 dark:text-slate-400 hover:text-teal-600 dark:hover:text-teal-400 transition">Impara la Finanza</a>'
    )
    c = c.replace(
        'class="text-sm text-gray-700 hover:text-teal-600 transition">Glossario</a>',
        'class="text-sm text-gray-700 dark:text-slate-400 hover:text-teal-600 dark:hover:text-teal-400 transition">Glossario</a>'
    )
    c = c.replace(
        'class="text-sm text-gray-700 hover:text-teal-600 transition">Analisi Tecnica</a>',
        'class="text-sm text-gray-700 dark:text-slate-400 hover:text-teal-600 dark:hover:text-teal-400 transition">Analisi Tecnica</a>'
    )
    # Mobile nav
    c = c.replace(
        'class="text-xs font-bold text-gray-900 montserrat-font block mb-2">📂 Sezioni</span>',
        'class="text-xs font-bold text-gray-900 dark:text-slate-300 montserrat-font block mb-2">📂 Sezioni</span>'
    )
    c = c.replace(
        'class="text-xs font-bold text-gray-900 montserrat-font block mb-2">📚 Risorse</span>',
        'class="text-xs font-bold text-gray-900 dark:text-slate-300 montserrat-font block mb-2">📚 Risorse</span>'
    )
    # Mobile nav links (text-xs text-gray-700)
    c = c.replace(
        'class="text-xs text-gray-700 hover:text-teal-600 transition block"',
        'class="text-xs text-gray-700 dark:text-slate-400 hover:text-teal-600 dark:hover:text-teal-400 transition block"',
    )

    # 7. Section headers
    c = c.replace(
        'class="text-2xl font-bold montserrat-font text-gray-900">📰 Articoli Ultimi 7 Giorni</h2>',
        'class="text-2xl font-bold montserrat-font text-gray-900 dark:text-white">📰 Articoli Ultimi 7 Giorni</h2>'
    )

    # 8. Footer dark mode
    old_footer_start = '<footer class="bg-gray-800 text-white'
    new_footer_start = '<footer class="bg-white dark:bg-transparent border-t border-gray-100 dark:border-slate-800/20 text-gray-900 dark:text-white transition-colors duration-300'
    if old_footer_start in c:
        c = c.replace(old_footer_start, new_footer_start)

    # Try other footer pattern
    c = c.replace(
        '<footer class="bg-gray-900 text-white',
        '<footer class="bg-white dark:bg-transparent border-t border-gray-100 dark:border-slate-800/20 text-gray-900 dark:text-white transition-colors duration-300'
    )

    # Footer inner text colors
    c = c.replace(
        '<span class="lobster-font text-4xl text-teal-400">Alma Finanza</span>',
        '<span class="lobster-font text-4xl text-teal-500">Alma Finanza</span>'
    )

    # 9. Toggle JS before </body>
    c = c.replace('</body>', TOGGLE_JS + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(c)
    return True


def process_category(filepath):
    """Process category pages - similar structure to index."""
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()

    if 'alma-theme' in c:
        print(f"  SKIP: {os.path.basename(filepath)}")
        return False

    # 1. Tailwind dark config
    c = c.replace(
        '<script src="https://cdn.tailwindcss.com"></script>',
        '<script src="https://cdn.tailwindcss.com"></script>\n' + TAILWIND_DARK
    )

    # 2. Anti-flash
    for ga in ["gtag('config', 'G-E88FFDTPMP');</script>", "gtag('config','G-E88FFDTPMP');</script>"]:
        if ga in c:
            c = c.replace(ga, ga + '\n' + ANTI_FLASH)
            break

    # 3. Dark CSS
    c = c.replace('    </style>', INDEX_DARK_CSS + '\n    </style>')

    # 4. Body
    c = c.replace(
        '<body class="bg-gray-50">',
        '<body class="bg-white dark:bg-[#0c1017] transition-colors duration-300">'
    )

    # 5. Header dark
    c = c.replace(
        'class="bg-white border-b-2 border-gray-200 sticky top-0 z-50 shadow-sm"',
        'class="bg-white/92 dark:bg-[#0c1017]/92 backdrop-blur-xl border-b border-gray-100 dark:border-slate-800/20 sticky top-0 z-50 shadow-sm dark:shadow-none transition-colors duration-300"'
    )

    # Header - simple pattern with just logo
    c = c.replace(
        'class="bg-white shadow-md sticky top-0 z-50"',
        'class="bg-white/92 dark:bg-[#0c1017]/92 backdrop-blur-xl shadow-md dark:shadow-none sticky top-0 z-50 border-b border-gray-100 dark:border-slate-800/20 transition-colors duration-300"'
    )

    # Logo text dark
    c = re.sub(
        r'(font-black text-gray-900)(?!.*dark:)',
        r'\1 dark:text-white',
        c
    )

    # "Torna alla Home" dark
    c = c.replace(
        'class="text-gray-700 hover:text-teal-600 font-medium"',
        'class="text-gray-700 dark:text-slate-400 hover:text-teal-600 dark:hover:text-teal-400 font-medium transition"'
    )

    # Add toggle next to "Torna alla Home"
    c = c.replace(
        '>&larr; Torna alla Home</a>\n        </div>\n    </header>',
        f'>&larr; Home</a>\n                {TOGGLE_HTML}\n            </div>\n        </div>\n    </header>'
    )

    # Fix: wrap the right side in a flex container if not already
    c = c.replace(
        '>&larr; Home</a>',
        '>&larr; Home</a>'
    )

    # Nav dark
    c = c.replace(
        'class="bg-gray-50 border-b border-gray-200',
        'class="bg-gray-50 dark:bg-[#0f1520] border-b border-gray-200 dark:border-slate-800/20'
    )

    # Nav text dark
    c = re.sub(
        r'class="text-sm text-gray-700 hover:text-teal-600(?! dark:)',
        'class="text-sm text-gray-700 dark:text-slate-400 hover:text-teal-600 dark:hover:text-teal-400',
        c
    )
    c = re.sub(
        r'class="text-xs text-gray-700 hover:text-teal-600(?! dark:)',
        'class="text-xs text-gray-700 dark:text-slate-400 hover:text-teal-600 dark:hover:text-teal-400',
        c
    )

    # Section headings
    c = re.sub(
        r'(font-bold montserrat-font text-gray-900)(?!.*dark:)',
        r'\1 dark:text-white',
        c
    )
    c = re.sub(
        r'(text-lg font-bold text-gray-800)(?!.*dark:)',
        r'\1 dark:text-slate-200',
        c
    )

    # Dividers
    c = c.replace('class="h-px bg-gray-300', 'class="h-px bg-gray-300 dark:bg-slate-800')

    # Footer
    c = c.replace(
        '<footer class="bg-gray-900 text-white',
        '<footer class="bg-white dark:bg-transparent border-t border-gray-100 dark:border-slate-800/20 text-gray-900 dark:text-white transition-colors duration-300'
    )
    c = c.replace(
        '<span class="lobster-font text-4xl text-teal-400">Alma Finanza</span>',
        '<span class="lobster-font text-4xl text-teal-500">Alma Finanza</span>'
    )

    # Toggle JS
    c = c.replace('</body>', TOGGLE_JS + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(c)
    return True


def process_simple_page(filepath):
    """Process simpler pages like dashboard, quote, impara-finanza, in-costruzione."""
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()

    if 'alma-theme' in c:
        print(f"  SKIP: {os.path.basename(filepath)}")
        return False

    # 1. Tailwind dark config
    c = c.replace(
        '<script src="https://cdn.tailwindcss.com"></script>',
        '<script src="https://cdn.tailwindcss.com"></script>\n' + TAILWIND_DARK
    )

    # 2. Anti-flash
    for ga in ["gtag('config', 'G-E88FFDTPMP');</script>", "gtag('config','G-E88FFDTPMP');</script>"]:
        if ga in c:
            c = c.replace(ga, ga + '\n' + ANTI_FLASH)
            break

    # 3. General dark overrides in style
    dark_css = '''
        /* === DARK MODE === */
        .dark .bg-gray-50,.dark .bg-gray-100{background:#0c1017!important;}
        .dark .bg-white{background:rgba(15,23,42,0.6)!important;}
        .dark .text-gray-900,.dark .text-gray-800{color:#f1f5f9!important;}
        .dark .text-gray-700,.dark .text-gray-600{color:#94a3b8!important;}
        .dark .text-gray-500{color:#64748b!important;}
        .dark .text-gray-400{color:#475569!important;}
        .dark .border-gray-200,.dark .border-gray-100,.dark .border-gray-300{border-color:rgba(51,65,85,0.2)!important;}
        .dark .shadow-sm,.dark .shadow-md,.dark .shadow-lg{box-shadow:0 4px 24px rgba(0,0,0,0.3)!important;}
        .dark .positive{color:#34d399!important;}
        .dark .negative{color:#f87171!important;}
        .theme-toggle{position:relative;width:52px;height:28px;border-radius:14px;cursor:pointer;transition:background 0.4s;display:inline-flex;align-items:center;}
        .theme-toggle .toggle-circle{position:absolute;top:3px;left:3px;width:22px;height:22px;border-radius:50%;transition:transform 0.4s cubic-bezier(0.68,-0.55,0.27,1.55),background 0.4s;display:flex;align-items:center;justify-content:center;font-size:12px;}
        .dark .theme-toggle .toggle-circle{transform:translateX(24px);}'''

    if '</style>' in c:
        c = c.replace('    </style>', dark_css + '\n    </style>')

    # 4. Body class
    if '<body class="bg-gray-50">' in c:
        c = c.replace('<body class="bg-gray-50">', '<body class="bg-white dark:bg-[#0c1017] transition-colors duration-300">')
    elif '<body class="bg-gray-100">' in c:
        c = c.replace('<body class="bg-gray-100">', '<body class="bg-white dark:bg-[#0c1017] transition-colors duration-300">')
    elif '<body' in c and 'dark:' not in c.split('<body')[1].split('>')[0]:
        c = re.sub(r'<body([^>]*)>', r'<body\1 style="transition:background 0.3s">', c, count=1)

    # 5. Header dark (various patterns)
    c = c.replace(
        'class="bg-white shadow-md sticky top-0 z-50"',
        'class="bg-white/92 dark:bg-[#0c1017]/92 backdrop-blur-xl shadow-md dark:shadow-none sticky top-0 z-50 border-b border-gray-100 dark:border-slate-800/20 transition-colors duration-300"'
    )

    # Logo dark
    c = re.sub(
        r'(font-black text-gray-900)(?!.*dark:text)',
        r'\1 dark:text-white',
        c
    )

    # Footer
    c = c.replace(
        '<footer class="bg-gray-900 text-white',
        '<footer class="bg-white dark:bg-transparent border-t border-gray-100 dark:border-slate-800/20 text-gray-900 dark:text-white transition-colors duration-300'
    )
    c = c.replace(
        '<span class="lobster-font text-4xl text-teal-400">Alma Finanza</span>',
        '<span class="lobster-font text-4xl text-teal-500">Alma Finanza</span>'
    )

    # Toggle JS
    if TOGGLE_JS.strip()[:30] not in c:
        c = c.replace('</body>', TOGGLE_JS + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(c)
    return True


def main():
    print("\n" + "="*60)
    print("  Alma Finanza — Dark Mode: Pagine Strutturali")
    print("="*60 + "\n")

    # Index
    print("📄 index.html:")
    fp = os.path.join(BASE_DIR, 'index.html')
    if os.path.exists(fp):
        if process_index(fp):
            print("  ✅ index.html aggiornato")

    # Categories
    cats = ['categoria-wall-street.html', 'categoria-borsa-milano.html',
            'categoria-crypto.html', 'categoria-commodities.html']
    print("\n📁 Categorie:")
    for cat in cats:
        fp = os.path.join(BASE_DIR, cat)
        if os.path.exists(fp):
            if process_category(fp):
                print(f"  ✅ {cat}")
        else:
            print(f"  ⚠️ Non trovato: {cat}")

    # Simple pages
    simples = ['dashboard.html', 'quote.html', 'impara-finanza.html', 'in-costruzione.html']
    print("\n📄 Altre pagine:")
    for page in simples:
        fp = os.path.join(BASE_DIR, page)
        if os.path.exists(fp):
            if process_simple_page(fp):
                print(f"  ✅ {page}")
        else:
            print(f"  ⚠️ Non trovato: {page}")

    print("\n" + "="*60)
    print("  Completato!")
    print("="*60 + "\n")


if __name__ == '__main__':
    main()
