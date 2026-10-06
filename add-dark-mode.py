#!/usr/bin/env python3
"""
Alma Finanza — Dark Mode Batch Updater
Aggiunge supporto Light/Dark a tutti gli articoli e pagine strutturali.
"""

import glob
import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# BLOCCHI CONDIVISI
# ============================================================

TAILWIND_DARK_CONFIG = '''    <script>tailwind.config={darkMode:'class'}</script>'''

# Script che va nel <head> per prevenire flash of wrong theme
ANTI_FLASH_SCRIPT = '''    <script>(function(){var t=localStorage.getItem('alma-theme');if(t==='dark'||(!t&&window.matchMedia('(prefers-color-scheme:dark)').matches))document.documentElement.classList.add('dark')})()</script>'''

# Script completo per il toggle, va prima di </body>
TOGGLE_SCRIPT = '''    <script>
    function toggleTheme(){var h=document.documentElement,d=h.classList.contains('dark');if(d){h.classList.remove('dark');localStorage.setItem('alma-theme','light')}else{h.classList.add('dark');localStorage.setItem('alma-theme','dark')}updateIcons()}
    function updateIcons(){var d=document.documentElement.classList.contains('dark');document.querySelectorAll('.ico-sun').forEach(function(e){e.style.display=d?'none':'inline'});document.querySelectorAll('.ico-moon').forEach(function(e){e.style.display=d?'inline':'none'})}
    window.matchMedia('(prefers-color-scheme:dark)').addEventListener('change',function(e){if(!localStorage.getItem('alma-theme')){if(e.matches)document.documentElement.classList.add('dark');else document.documentElement.classList.remove('dark');updateIcons()}});
    updateIcons();
    </script>'''

# CSS dark mode overrides da aggiungere nel blocco <style>
DARK_CSS_OVERRIDES = '''
        /* === DARK MODE === */
        .dark body,.dark .bg-gray-50{background:#0c1017!important;}
        .dark .bg-white{background:rgba(15,23,42,0.6)!important;border-color:rgba(51,65,85,0.3)!important;}
        .dark .article-content h2{color:#f1f5f9!important;}
        .dark .article-content p,.dark .article-content li{color:#94a3b8!important;}
        .dark .lead{color:#cbd5e1!important;}
        .dark .info-box{background:rgba(15,23,42,0.6)!important;border-color:rgba(51,65,85,0.5)!important;}
        .dark .info-box h3{color:#93c5fd!important;}
        .dark .info-box p{color:#94a3b8!important;}
        .dark .data-table th{background:#0f172a!important;}
        .dark .data-table td{border-color:rgba(51,65,85,0.3)!important;color:#cbd5e1!important;}
        .dark .data-table tr:nth-child(even) td{background:rgba(30,41,59,0.4)!important;}
        .dark .positive{color:#34d399!important;}
        .dark .negative{color:#f87171!important;}
        .dark strong{color:#e2e8f0;}
        .dark .bg-yellow-50{background:rgba(234,179,8,0.1)!important;}
        .dark .text-yellow-800{color:#fde047!important;}
        .dark .bg-red-50{background:rgba(239,68,68,0.1)!important;}
        .dark .text-red-800{color:#fca5a5!important;}
        .dark .shadow-sm,.dark .shadow-md{box-shadow:0 4px 24px rgba(0,0,0,0.3)!important;}
        .theme-toggle{position:relative;width:52px;height:28px;border-radius:14px;cursor:pointer;transition:background 0.4s;display:inline-flex;align-items:center;}
        .theme-toggle .toggle-circle{position:absolute;top:3px;left:3px;width:22px;height:22px;border-radius:50%;transition:transform 0.4s cubic-bezier(0.68,-0.55,0.27,1.55),background 0.4s;display:flex;align-items:center;justify-content:center;font-size:12px;}
        .dark .theme-toggle .toggle-circle{transform:translateX(24px);}'''


def process_article(filepath):
    """Process a single article HTML file to add dark mode support."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already processed
    if "alma-theme" in content or "darkMode:'class'" in content:
        print(f"  SKIP (already has dark mode): {os.path.basename(filepath)}")
        return False

    # 1. Add <html lang="it"> -> <html lang="it" class="">  (for dark class toggle)
    #    No change needed, JS adds class dynamically

    # 2. After Tailwind CDN, add dark config
    content = content.replace(
        '<script src="https://cdn.tailwindcss.com"></script>',
        '<script src="https://cdn.tailwindcss.com"></script>\n' + TAILWIND_DARK_CONFIG
    )

    # 3. Add anti-flash script after <head> opening or after GA
    # Insert right after the GA config line
    ga_pattern = "gtag('config','G-E88FFDTPMP');</script>"
    if ga_pattern in content:
        content = content.replace(
            ga_pattern,
            ga_pattern + '\n' + ANTI_FLASH_SCRIPT
        )
    else:
        # Alternative: some files might have the GA formatted differently
        ga_alt = "gtag('config', 'G-E88FFDTPMP');</script>"
        if ga_alt in content:
            content = content.replace(
                ga_alt,
                ga_alt + '\n' + ANTI_FLASH_SCRIPT
            )

    # 4. Add dark CSS overrides before </style>
    content = content.replace(
        '    </style>',
        DARK_CSS_OVERRIDES + '\n    </style>'
    )

    # 5. Update body class
    content = content.replace(
        '<body class="bg-gray-50">',
        '<body class="bg-white dark:bg-[#0c1017] transition-colors duration-300">'
    )

    # 6. Update header - add dark mode classes + toggle button
    # Pattern: the standard header
    old_header = '''    <header class="bg-white shadow-md sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="index.html" class="flex items-center space-x-2">
                <span class="lobster-font text-5xl text-teal-500">A</span>
                <span class="montserrat-font text-3xl font-black text-gray-900">LMA FINANZA</span>
            </a>
            <a href="index.html" class="text-gray-700 hover:text-teal-600 font-medium">&larr; Torna alla Home</a>
        </div>
    </header>'''

    new_header = '''    <header class="bg-white/92 dark:bg-[#0c1017]/92 backdrop-blur-xl shadow-md dark:shadow-none sticky top-0 z-50 border-b border-gray-100 dark:border-slate-800/20 transition-colors duration-300">
        <div class="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="index.html" class="flex items-center space-x-2">
                <span class="lobster-font text-5xl text-teal-500">A</span>
                <span class="montserrat-font text-3xl font-black text-gray-900 dark:text-white">LMA FINANZA</span>
            </a>
            <div class="flex items-center gap-4">
                <a href="index.html" class="text-gray-700 dark:text-slate-400 hover:text-teal-600 dark:hover:text-teal-400 font-medium transition">&larr; Home</a>
                <div class="theme-toggle bg-gray-200 dark:bg-slate-700" onclick="toggleTheme()" title="Cambia tema">
                    <div class="toggle-circle bg-white dark:bg-slate-900 shadow-md">
                        <span class="ico-sun">☀️</span><span class="ico-moon" style="display:none">🌙</span>
                    </div>
                </div>
            </div>
        </div>
    </header>'''

    if old_header in content:
        content = content.replace(old_header, new_header)
    else:
        # Try to match alternative header patterns (subagent-created articles)
        # These have slightly different structure but same key elements
        header_match = re.search(
            r'(<header class="bg-white shadow-md sticky top-0 z-50">.*?</header>)',
            content, re.DOTALL
        )
        if header_match:
            old_h = header_match.group(1)
            content = content.replace(old_h, new_header)

    # 7. Update main article container
    content = content.replace(
        'class="article-content bg-white rounded-lg shadow-sm p-6 md:p-10"',
        'class="article-content bg-white dark:bg-[#0f172a]/60 rounded-lg shadow-sm dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] border border-transparent dark:border-slate-700/30 p-6 md:p-10 transition-colors duration-300"'
    )

    # 8. Update footer
    old_footer = '''    <footer class="bg-gray-900 text-white py-12 mt-16">
        <div class="max-w-7xl mx-auto px-4 text-center">
            <span class="lobster-font text-4xl text-teal-400">Alma Finanza</span>
            <p class="text-gray-400 mt-4">&copy; 2026 Alma Finanza. Tutti i diritti riservati.</p>
            <p class="text-gray-500 text-sm mt-2">Le informazioni fornite sono a scopo informativo e non costituiscono consulenza finanziaria.</p>
        </div>
    </footer>'''

    new_footer = '''    <footer class="bg-white dark:bg-transparent border-t border-gray-100 dark:border-slate-800/20 text-gray-900 dark:text-white py-12 mt-16 transition-colors duration-300">
        <div class="max-w-7xl mx-auto px-4 text-center">
            <span class="lobster-font text-4xl text-teal-500">Alma Finanza</span>
            <p class="text-gray-300 dark:text-slate-600 mt-4">&copy; 2026 Alma Finanza. Tutti i diritti riservati.</p>
            <p class="text-gray-200 dark:text-slate-700 text-sm mt-2">Le informazioni fornite sono a scopo informativo e non costituiscono consulenza finanziaria.</p>
        </div>
    </footer>'''

    if old_footer in content:
        content = content.replace(old_footer, new_footer)
    else:
        # Try flexible footer match
        footer_match = re.search(
            r'(<footer class="bg-gray-900 text-white py-12 mt-16">.*?</footer>)',
            content, re.DOTALL
        )
        if footer_match:
            content = content.replace(footer_match.group(1), new_footer)

    # 9. Add toggle script before </body>
    content = content.replace(
        '</body>',
        TOGGLE_SCRIPT + '\n</body>'
    )

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True


def main():
    # Process all article files
    articles = sorted(glob.glob(os.path.join(BASE_DIR, 'articolo-*.html')))
    print(f"\n{'='*60}")
    print(f"  Alma Finanza — Dark Mode Batch Updater")
    print(f"  Trovati {len(articles)} articoli")
    print(f"{'='*60}\n")

    updated = 0
    skipped = 0
    errors = 0

    for filepath in articles:
        fname = os.path.basename(filepath)
        try:
            if process_article(filepath):
                print(f"  ✅ {fname}")
                updated += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"  ❌ ERRORE {fname}: {e}")
            errors += 1

    print(f"\n{'='*60}")
    print(f"  Completato: {updated} aggiornati, {skipped} saltati, {errors} errori")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
