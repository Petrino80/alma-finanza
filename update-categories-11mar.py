#!/usr/bin/env python3
"""Aggiorna le 4 pagine categoria con gli articoli dell'11 Marzo 2026"""
import re

date_section = '''    <section class="mb-12">
        <div class="flex items-center mb-6">
            <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">Mercoledì, 11 Marzo 2026</h2>
            <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
        </div>
        <div class="grid md:grid-cols-3 gap-6">
{cards}
        </div>
    </section>

'''

def make_card(href, badge_label, badge_bg, badge_color, title, desc, date_short):
    return f'''            <a href="{href}" class="block">
                <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge" style="background:{badge_bg};color:{badge_color};">{badge_label}</span>
                        <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">{title}</h2>
                        <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">{desc}</p>
                        <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                            <span>📰 {date_short}</span>
                            <span class="text-teal-500 font-semibold">Leggi →</span>
                        </div>
                    </div>
                </article>
            </a>'''

# ============================================================
# 1. WALL STREET
# ============================================================
ws_cards = []
ws_cards.append(make_card(
    "articolo-wall-street-11mar-cpi-stabile-nebius-nvidia-petrolio.html",
    "Wall Street", "#dbeafe", "#1e40af",
    "Wall Street in calo: CPI 2,4% in linea, Dow -0,61%, Nebius +16% su Nvidia $2B",
    "Dow 47.417 (-289), S&P 6.776, Nasdaq +0,08%. CPI febbraio stabile. Nebius vola su Nvidia. WTI $87.",
    "11 Mar 2026"
))
ws_cards.append(make_card(
    "articolo-nvidia-nebius-11mar-2b-ai-cloud-infrastruttura.html",
    "Tech/AI", "#f3e8ff", "#6b21a8",
    "Nvidia investe $2 miliardi in Nebius: azioni +16%, la corsa all'AI cloud",
    "Nvidia acquisisce 8,3% di Nebius. 5+ GW data center entro 2030. Oracle +9,3%. Serve Robotics +10,45%.",
    "11 Mar 2026"
))
ws_cards.append(make_card(
    "articolo-europa-11mar-dax-cede-rheinmetall-earnings.html",
    "Europa", "#dbeafe", "#1e40af",
    "Europa in rosso: DAX -1,6%, Rheinmetall -5,2% dopo earnings deludenti",
    "Stoxx 600 -0,8%. DAX 23.629. Rheinmetall -5,2% su guidance debole. Henkel -3,8%.",
    "11 Mar 2026"
))

ws_section = date_section.format(cards='\n'.join(ws_cards))

with open('categoria-wall-street.html', 'r', encoding='utf-8') as f:
    ws_html = f.read()

# Inserisci dopo il primo <main...> e il commento/sezione articoli
marker = re.search(r'(<main[^>]*>\s*)', ws_html)
if marker:
    pos = marker.end()
    ws_html = ws_html[:pos] + '\n' + ws_section + ws_html[pos:]
    with open('categoria-wall-street.html', 'w', encoding='utf-8') as f:
        f.write(ws_html)
    print("✅ categoria-wall-street.html: +3 articoli 11 marzo")

# ============================================================
# 2. BORSA MILANO
# ============================================================
mi_cards = []
mi_cards.append(make_card(
    "articolo-ftse-mib-11mar-fusione-mps-mediobanca-diasorin.html",
    "Piazza Affari", "#dcfce7", "#166534",
    "FTSE MIB -0,95% a 44.773: fusione MPS-Mediobanca, DiaSorin -6,7%",
    "Fusione MPS-Mediobanca approvata, concambio 2,45x. Mediobanca +2,1%, MPS +1,2%. ENI +2%. DiaSorin peggior titolo.",
    "11 Mar 2026"
))

mi_section = date_section.format(cards='\n'.join(mi_cards))

with open('categoria-borsa-milano.html', 'r', encoding='utf-8') as f:
    mi_html = f.read()

marker = re.search(r'(<main[^>]*>\s*)', mi_html)
if marker:
    pos = marker.end()
    mi_html = mi_html[:pos] + '\n' + mi_section + mi_html[pos:]
    with open('categoria-borsa-milano.html', 'w', encoding='utf-8') as f:
        f.write(mi_html)
    print("✅ categoria-borsa-milano.html: +1 articolo 11 marzo")

# ============================================================
# 3. COMMODITIES
# ============================================================
co_cards = []
co_cards.append(make_card(
    "articolo-petrolio-11mar-iea-riserve-400m-barili-hormuz.html",
    "Petrolio", "#fef3c7", "#92400e",
    "IEA rilascio record 400M barili, ma WTI sale +4,55% a $87: attacchi Hormuz",
    "Il più grande rilascio di riserve della storia non ferma il greggio. Brent $92. Oro -1,3%. Bitcoin $70K.",
    "11 Mar 2026"
))

co_section = date_section.format(cards='\n'.join(co_cards))

with open('categoria-commodities.html', 'r', encoding='utf-8') as f:
    co_html = f.read()

marker = re.search(r'(<main[^>]*>\s*)', co_html)
if marker:
    pos = marker.end()
    co_html = co_html[:pos] + '\n' + co_section + co_html[pos:]
    with open('categoria-commodities.html', 'w', encoding='utf-8') as f:
        f.write(co_html)
    print("✅ categoria-commodities.html: +1 articolo 11 marzo")

# ============================================================
# 4. CRYPTO (no new crypto-specific articles today, but petrolio article mentions BTC)
# ============================================================
print("ℹ️  categoria-crypto.html: nessun articolo crypto specifico l'11 marzo, skip")

print("\n🎉 Pagine categoria aggiornate!")
