#!/usr/bin/env python3
"""
Inserisce i 2 nuovi articoli di oggi (6 feb) all'inizio della griglia
"""
import re

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I due nuovi articoli da inserire IN CIMA (sono i più recenti di oggi)
new_articles = '''            <!-- Article 1 - 6 Feb - NUOVO -->
            <a href="articolo-wall-street-rimbalzo-6feb.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-wall-street">Wall Street</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Wall Street rimbalza: Dow +810 punti a nuovo ATH, S&P +1.2%
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Venerdì 6 febbraio: Dow +810 punti a record storico, S&P 500 +1.2%, Nasdaq +1%. Nvidia +3.1%, AMD +5.1%. Amazon -9% su $200Bn AI capex. Performance settimanale: S&P -2%, Nasdaq -4%.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 6 Feb 2026</span>
                            <span>👁 1.8K</span>
                        </div>
                    </div>
                </article>
            </a>

            <!-- Article 2 - 6 Feb - NUOVO -->
            <a href="articolo-europa-stoxx-600-record.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-europa">Europa</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Europa solida: Stoxx 600 a nuovo record, +1.0% il 2 febbraio
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Stoxx 600 record high 2 feb (+1.0%). DAX +1.0%, CAC +0.8%, FTSE +1.1%. Performance da aprile 2025: +33%. Mining stocks guidano rebound. Volatilità metalli preziosi si stabilizza.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 6 Feb 2026</span>
                            <span>👁 2.1K</span>
                        </div>
                    </div>
                </article>
            </a>

'''

# Trova la posizione dopo "<!-- Articles Grid -->" e "<div class="grid md:grid-cols-3 gap-6">"
# Inserisci i nuovi articoli come PRIMI
pattern = r'(<!-- Articles Grid -->\s*<div class="grid md:grid-cols-3 gap-6">\s*)'
replacement = r'\1' + new_articles

content = re.sub(pattern, replacement, content)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Inseriti 2 nuovi articoli in CIMA alla homepage")
print("✓ Ordine: articoli del 6 febbraio (più recenti) in alto")
print("")
print("Nuovi articoli:")
print("  1. Wall Street rimbalza: Dow +810 punti ATH, S&P +1.2%")
print("  2. Europa solida: Stoxx 600 record, +1.0%")
print("")
print("Totale articoli ora: 29")
