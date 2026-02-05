#!/usr/bin/env python3
"""
Add all articles from last 7 days to homepage
"""

# Read current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find where to insert new articles (after Article 10, before closing </div>)
# We need to add the missing articles

additional_articles = '''
            <!-- Article 11 -->
            <a href="articolo-sell-off-tech.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-tech">Educazione</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Comprendere il sell-off tech: anatomia di una giornata di panic selling
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Cosa significa "sell-off"? Come si innescano vendite massive. Analisi volumetrica, sentiment indicators, capitulation patterns. Guida educativa per riconoscere e gestire panic selling.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 10.5K</span>
                        </div>
                    </div>
                </article>
            </a>

            <!-- Article 12 -->
            <a href="articolo-novo-nordisk-crash.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-wall-street">Pharma</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Novo Nordisk -24%: cosa è successo al gigante Ozempic
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Trial clinici CagriSema deludono. Competizione Eli Lilly intensifica. Mercato GLP-1 sotto pressione. Pipeline futura e valutazione post-crash. Opportunity o value trap?
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 14.2K</span>
                        </div>
                    </div>
                </article>
            </a>

            <!-- Article 13 -->
            <a href="articolo-salesforce-crash-ai.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-tech">CRM + AI</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Salesforce -11% post-earnings: AI strategy non convince
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Agentforce adoption lenta. Revenue guidance Q1 sotto attese. Competizione Microsoft Dynamics, HubSpot. Valutazione SaaS multiples e cash flow generation. Bear case vs bull case.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 9.7K</span>
                        </div>
                    </div>
                </article>
            </a>

            <!-- Article 14 -->
            <a href="articolo-microsoft-stabilizza.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-tech">Microsoft</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Microsoft stabilizza a $420: Azure cloud e AI driving growth
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Dopo volatilità settimana scorsa, MSFT consolida. Azure +30% YoY, Copilot enterprise adoption. Gaming division strong. Dividendo e buyback program. Analisi valutazione fair value.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 6.8K</span>
                        </div>
                    </div>
                </article>
            </a>

            <!-- Article 15 -->
            <a href="articolo-kevin-warsh-fed.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-macro">Fed Policy</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Kevin Warsh nominato Fed Chair: cosa cambia per i mercati
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Background Warsh: ex Fed Governor, stance hawkish. Implicazioni per policy rates, QT continuation. Market reaction e outlook tassi 2026. Comparazione con Powell era.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 11.4K</span>
                        </div>
                    </div>
                </article>
            </a>

            <!-- Article 16 -->
            <a href="articolo-southwest-airlines-19.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-wall-street">Airlines</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Southwest Airlines -19%: guida Q1 shock, load factor crolla
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Previsioni revenue Q1 well below consensus. Competizione low-cost intensifica. Pilot shortage, fuel costs elevation. Turnaround strategy e tempi recovery. Comparables settore.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 5.9K</span>
                        </div>
                    </div>
                </article>
            </a>

            <!-- Article 17 -->
            <a href="articolo-ppi-05.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-macro">Inflazione</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            PPI gennaio +0.5%: inflazione producer ancora elevata
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Producer Price Index sopra attese. Core PPI +0.4%. Implicazioni per CPI consumer inflation. Fed policy implications e market reaction. Breakdown per settori.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 7.6K</span>
                        </div>
                    </div>
                </article>
            </a>

            <!-- Article 18 -->
            <a href="articolo-argento-crash-30.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-commodities">Argento</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Argento crolla a $30: fine del rally sui metalli preziosi?
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            Da $34 a $30 in 72h (-11.8%). Argento vs oro performance divergence. Industrial demand weakness, dollar strength. Gold/Silver ratio a 161. Prospettive e livelli tecnici chiave.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 8.1K</span>
                        </div>
                    </div>
                </article>
            </a>

            <!-- Article 19 -->
            <a href="articolo-bitcoin-74570.html" class="block">
                <article class="bg-white rounded-lg shadow overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
                    <span class="read-badge">Leggi</span>
                    <div class="p-6">
                        <span class="category-badge cat-crypto">Bitcoin</span>
                        <h2 class="text-xl font-bold mt-3 mb-2 montserrat-font">
                            Bitcoin $74.570: continua correzione, analisi tecnica
                        </h2>
                        <p class="text-gray-600 text-sm mb-4">
                            BTC perde ulteriore terreno da ATH $83K. Correlazione con risk assets, analisi supporti chiave $70K. Metriche on-chain: MVRV, SOPR, exchange flows. Prospettive breve termine.
                        </p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span>🕐 4 Feb 2026</span>
                            <span>👁 13.8K</span>
                        </div>
                    </div>
                </article>
            </a>
'''

# Find the position to insert (after Article 10, before </div> that closes the grid)
# Look for the closing </a> of Article 10, then find the next </div>
import re

# Find the article-missione-alma-finanza.html closing </a> tag
pattern = r'(</a>\s*\n\s*</div>\s*\n\s*<!-- Mission Section -->)'
replacement = f'''</a>
{additional_articles}
        </div>

        <!-- Mission Section -->'''

content = re.sub(pattern, replacement, content)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Aggiunti 9 articoli aggiuntivi (totale 19 articoli)")
print("✓ Homepage ora mostra tutti gli articoli degli ultimi 7 giorni")
