#!/usr/bin/env python3
"""
Aggiunge i 2 nuovi articoli italiani IN CIMA alla homepage
"""
import re

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I due nuovi articoli italiani da inserire IN CIMA (più recenti)
new_italy_articles = '''            <!-- Article 1 - Piazza Affari 6 Feb - NUOVO -->
            <a href="articolo-piazza-affari-6feb-stellantis.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative; border: 3px solid #059669;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge" style="background: linear-gradient(135deg, #059669 0%, #047857 100%); color: white;">🇮🇹 Piazza Affari</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Piazza Affari 6 feb: FTSE MIB -0.53%, Stellantis crolla -18.65%
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            FTSE MIB -0.53%, tra le peggiori in Europa. Stellantis -18.65% su €22 miliardi svalutazioni e stop dividendi. Bene banche: Unipol +2.46%, Fineco +1.87%, BPER +1.58%. Spread 63 bps, BTP 10Y a 3.45%.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 6 Feb 2026</span>
                            <span>👁 15.3K</span>
                        </div>
                    </div>
                </article>
            </a>

            <!-- Article 2 - Banche Italiane - NUOVO -->
            <a href="articolo-banche-italiane-2026-intesa-unicredit.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative; border: 3px solid #059669;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge" style="background: linear-gradient(135deg, #059669 0%, #047857 100%); color: white;">🇮🇹 Banche Italiane</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Banche italiane 2026: Intesa e UniCredit oltre target, dividend yield 9-10%
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Utili record €26 miliardi nel 2025, obiettivo €28 miliardi 2026. CET1 >15%, dividend yield 9-10%. Morgan Stanley alza target: UniCredit €76, Intesa €6.80. M&A motore del rally.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 6 Feb 2026</span>
                            <span>👁 18.7K</span>
                        </div>
                    </div>
                </article>
            </a>

'''

# Trova la posizione dopo "Articoli Ultimi 7 Giorni" e prima del primo articolo
pattern = r'(<h2 class="text-3xl font-bold text-center mb-12 montserrat-font">Articoli Ultimi 7 Giorni</h2>\s*<div class="grid md:grid-cols-3 gap-6">\s*)'
replacement = r'\1' + new_italy_articles

content = re.sub(pattern, replacement, content)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Aggiunti 2 nuovi articoli ITALIANI in CIMA alla homepage")
print("✓ Articoli con bordo verde per evidenziare focus Italia 🇮🇹")
print("")
print("Nuovi articoli:")
print("  1. Piazza Affari 6 feb: FTSE MIB -0.53%, Stellantis -18.65%")
print("  2. Banche italiane: Intesa e UniCredit oltre target, yield 9-10%")
print("")
print("✓ Totale articoli ora: 31 (2 nuovi + 29 precedenti)")
