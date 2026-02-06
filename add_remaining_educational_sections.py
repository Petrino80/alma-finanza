#!/usr/bin/env python3
"""
Aggiunge sezioni formative ai rimanenti 19 articoli
"""
import re

# Template sezione formativa generica per articoli senza sezione specifica
generic_educational = """
            <!-- Sezione Formativa -->
            <div class="mt-12 pt-8 border-t-2 border-gray-200 bg-blue-50 p-6 rounded-lg">
                <h3 class="text-xl font-bold mb-4 montserrat-font text-blue-900">📚 Sezione Formativa: Concetti Chiave</h3>
                <div class="space-y-4 text-gray-700">
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Come leggere i movimenti di prezzo?</h4>
                        <p class="text-sm">Quando leggi "+2.5%" o "-1.8%", identifica sempre l'intervallo temporale: intraday (singola sessione), settimanale, mensile, YTD (year-to-date), o da un dato punto. Performance diverse in intervalli diversi danno un quadro completo della dinamica del titolo.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Market cap (capitalizzazione di mercato)</h4>
                        <p class="text-sm">La market cap si calcola moltiplicando il prezzo dell'azione per il numero di azioni in circolazione. Misura il valore totale dell'azienda secondo il mercato. Large-cap (oltre $10B), mid-cap ($2-10B), small-cap ($300M-$2B), micro-cap (sotto $300M).</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Volatilità: rischio e opportunità</h4>
                        <p class="text-sm">La volatilità misura l'ampiezza delle oscillazioni di prezzo. Alta volatilità = grandi movimenti su/giù = maggior rischio MA anche maggiori opportunità di trading. Asset come crypto e small-cap tech sono più volatili di blue-chip o bond.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Sentiment di mercato</h4>
                        <p class="text-sm">Il sentiment (sentimento) è la psicologia collettiva degli investitori: ottimista (risk-on, acquisti) o pessimista (risk-off, vendite). Sentiment può sovra-reagire a notizie, creando opportunità per investitori contrarian che vanno contro la massa.</p>
                    </div>
                </div>
            </div>
"""

# Sezioni formative specifiche per alcuni articoli chiave
specific_sections = {
    "articolo-bitcoin-83463.html": """
            <!-- Sezione Formativa -->
            <div class="mt-12 pt-8 border-t-2 border-gray-200 bg-blue-50 p-6 rounded-lg">
                <h3 class="text-xl font-bold mb-4 montserrat-font text-blue-900">📚 Sezione Formativa: Concetti Chiave</h3>
                <div class="space-y-4 text-gray-700">
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Perché Bitcoin è così volatile?</h4>
                        <p class="text-sm">Bitcoin ha volatilità 3-5x superiore a S&P 500 per: (1) <strong>Mercato 24/7</strong> senza interruzioni, (2) <strong>Liquidità frammentata</strong> su centinaia di exchange, (3) <strong>Leva alta</strong> nei derivati crypto, (4) <strong>Sentiment-driven</strong>: notizie e tweet muovono il prezzo drasticamente.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Cos'è il "weekend dump" in crypto?</h4>
                        <p class="text-sm">Nei weekend, la liquidità crypto cala perché: mercati tradizionali chiusi, meno trader istituzionali attivi, minor volume. Questo rende Bitcoin più suscettibile a movimenti bruschi. Vendite algoritmiche o panic selling nel weekend possono causare "dump" (crolli rapidi).</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Bitcoin come "risk asset" vs "safe haven"</h4>
                        <p class="text-sm">Bitcoin era chiamato "digital gold" e safe haven, ma oggi si comporta come <strong>risk asset</strong>: quando mercati scendono (risk-off), Bitcoin spesso scende di più. Correlazione con Nasdaq ~0.7-0.8. Oro vero mantiene meglio il ruolo di rifugio.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 "Settimana da dimenticare": context matters</h4>
                        <p class="text-sm">Una settimana negativa va contestualizzata: -5% settimanale dopo +50% mensile è diverso da -5% in downtrend. Per Bitcoin, movimenti -3-7% settimanali sono normali. Solo ribassi oltre -15-20% indicano veri cambi di trend.</p>
                    </div>
                </div>
            </div>
""",

    "articolo-novo-nordisk-crash.html": """
            <!-- Sezione Formativa -->
            <div class="mt-12 pt-8 border-t-2 border-gray-200 bg-blue-50 p-6 rounded-lg">
                <h3 class="text-xl font-bold mb-4 montserrat-font text-blue-900">📚 Sezione Formativa: Concetti Chiave</h3>
                <div class="space-y-4 text-gray-700">
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Perché pharma scende su "regulatory news"?</h4>
                        <p class="text-sm">Le aziende farmaceutiche dipendono da approvazioni FDA/EMA. Notizie negative su trial clinici, side effects, o mancate approvazioni possono cancellare miliardi di ricavi futuri in un giorno. Il mercato sconta immediatamente questi rischi con sell-off rapidi.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Pipeline drugs e valutazione pharma</h4>
                        <p class="text-sm">La pipeline (farmaci in sviluppo) vale spesso 30-50% della market cap di un'azienda pharma. Ogni farmaco in Phase 2/3 ha una probability of success (PoS) stimata. Quando un drug chiave fallisce, quella % di valore evapora istantaneamente.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 "Binary events" nel biotech</h4>
                        <p class="text-sm">I binary events (FDA decision, trial readout) hanno solo 2 outcome: successo (+20-50%) o fallimento (-30-60%). Investire in pharma pre-catalyst significa accettare questo rischio binario. La diversificazione è cruciale.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Market cap loss: $50B in perspective</h4>
                        <p class="text-sm">Novo Nordisk perde $50B = 10-15% della market cap. Per context: $50B è più di market cap di United Airlines o Spotify. Questi numeri giganti riflettono aspettative enormi su blockbuster drugs (Ozempic, Wegovy) e quanto rapidamente possono evaporare.</p>
                    </div>
                </div>
            </div>
""",

    "articolo-salesforce-crash-ai.html": """
            <!-- Sezione Formativa -->
            <div class="mt-12 pt-8 border-t-2 border-gray-200 bg-blue-50 p-6 rounded-lg">
                <h3 class="text-xl font-bold mb-4 montserrat-font text-blue-900">📚 Sezione Formativa: Concetti Chiave</h3>
                <div class="space-y-4 text-gray-700">
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 "AI disruption" vs "AI opportunity"</h4>
                        <p class="text-sm">L'AI può essere disruption (minaccia) o opportunity (opportunità). Per Salesforce, l'AI minaccia il business model: chatbot AI potrebbero sostituire i software CRM tradizionali. Aziende che non si adattano rischiano di diventare obsolete (vedi Blockbuster vs Netflix).</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 SaaS multiples compression</h4>
                        <p class="text-sm">Le aziende SaaS (Software-as-a-Service) sono valutate su multipli di revenue (Price/Sales). Quando growth rallenta o concorrenza aumenta, questi multipli "comprimono": da 10x revenue a 5x = -50% del prezzo anche senza cambi negli utili. Salesforce soffre questa compression.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 "Sticky" business model nel SaaS</h4>
                        <p class="text-sm">Il business SaaS è "sticky" (appiccicoso): clienti non cambiano software facilmente per switching costs alti. Ma l'AI abbassa questi costi: migrare a nuovo CRM AI-native diventa più facile. La stickiness che proteggeva Salesforce si erode.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 "Winner-take-all" dynamics nell'AI</h4>
                        <p class="text-sm">I mercati AI tendono a winner-take-all: il miglior modello/prodotto conquista 70-80% del mercato (vedi Google Search, Facebook social). Salesforce rischia di non essere il "winner" nell'AI CRM, cedendo quote a startup AI-first più agili.</p>
                    </div>
                </div>
            </div>
""",

    "articolo-palantir-surge.html": """
            <!-- Sezione Formativa -->
            <div class="mt-12 pt-8 border-t-2 border-gray-200 bg-blue-50 p-6 rounded-lg">
                <h3 class="text-xl font-bold mb-4 montserrat-font text-blue-900">📚 Sezione Formativa: Concetti Chiave</h3>
                <div class="space-y-4 text-gray-700">
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Cos'è un "growth stock"?</h4>
                        <p class="text-sm">I growth stocks sono aziende che crescono velocemente (revenue +30-50%/anno) ma spesso non sono ancora profittevoli o hanno P/E altissimi. Palantir è un classico growth stock: valutato per crescita futura, non utili presenti. Volatili ma con potenziale upside enorme.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Government contracts vs commercial business</h4>
                        <p class="text-sm">Palantir divide revenue tra <strong>Gov</strong> (contratti governativi: difesa, intelligence, stabilissimi ma slow growth) e <strong>Commercial</strong> (aziende private: più volatili ma crescita rapida). Mix ideale: Gov per stabilità, Commercial per growth. Investitori premiano Commercial expansion.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 "Data analytics platform": moat tecnologico</h4>
                        <p class="text-sm">Il moat (fossato competitivo) di Palantir è la piattaforma proprietaria Foundry/Gotham: integra dati complessi meglio della concorrenza. Una volta implementata in un'organizzazione, è difficile sostituirla (high switching costs). Questo crea revenue ricorrente.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Valutazione growth: Price/Sales ratio</h4>
                        <p class="text-sm">Growth stocks si valutano spesso con Price/Sales (P/S) invece di P/E perché molti non hanno ancora utili. P/S di 20-30x è normale per high-growth tech. Se growth rallenta, P/S comprime rapidamente = crash del prezzo anche senza perdite.</p>
                    </div>
                </div>
            </div>
""",

    "articolo-kevin-warsh-fed.html": """
            <!-- Sezione Formativa -->
            <div class="mt-12 pt-8 border-t-2 border-gray-200 bg-blue-50 p-6 rounded-lg">
                <h3 class="text-xl font-bold mb-4 montserrat-font text-blue-900">📚 Sezione Formativa: Concetti Chiave</h3>
                <div class="space-y-4 text-gray-700">
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Chi è il Fed Chair e perché conta?</h4>
                        <p class="text-sm">Il Fed Chair guida la Federal Reserve (banca centrale USA) e decide i tassi di interesse, influenzando tutta l'economia. Un Chair "hawkish" (pro-tassi alti contro inflazione) danneggia growth stocks. Un Chair "dovish" (pro-crescita, tassi bassi) favorisce le azioni. La nomina è cruciale.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 "Hawkish" vs "Dovish": linguaggio Fed</h4>
                        <p class="text-sm"><strong>Hawkish</strong> = falco, aggressivo contro inflazione, alza tassi, negativo per azioni. <strong>Dovish</strong> = colomba, priorità crescita/occupazione, taglia tassi, positivo per azioni. Kevin Warsh è noto come hawkish, preoccupando investitori growth.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Come i tassi Fed influenzano le azioni?</h4>
                        <p class="text-sm">Tassi Fed alti → Treasury yields alti → tasso di sconto DCF alto → valutazioni growth giù. Esempio: +1% nei tassi Fed può portare -10-15% in Nasdaq. I settori più sensibili: tech, real estate, small-cap (dipendono da capitale a basso costo).</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Market reaction a nomine Fed</h4>
                        <p class="text-sm">Il mercato sconta immediatamente le nomine Fed: se hawkish → sell-off anticipato, se dovish → rally. Reazione può essere esagerata nel breve, ma direzione è spesso corretta. Seguire le conferenze stampa Fed (FOMC) è essenziale per capire policy shifts.</p>
                    </div>
                </div>
            </div>
"""
}

# Lista articoli da processare
articles_to_process = [
    "articolo-argento-crash-30.html",
    "articolo-bitcoin-74570.html",
    "articolo-bitcoin-83463.html",
    "articolo-ftse-mib-45847.html",
    "articolo-kevin-warsh-fed.html",
    "articolo-microsoft-stabilizza.html",
    "articolo-missione-alma-finanza.html",
    "articolo-novo-nordisk-crash.html",
    "articolo-oro-crash-816.html",
    "articolo-palantir-surge.html",
    "articolo-ppi-05.html",
    "articolo-salesforce-crash-ai.html",
    "articolo-sell-off-tech.html",
    "articolo-southwest-airlines-19.html",
    "articolo-sp500-6921.html",
    "articolo-spacex-xai-ecosistema.html",
    "articolo-tech-rout-continua.html",
    "articolo-tesla-produzione-q1.html",
    "articolo-unity-software-gaming.html"
]

success_count = 0
skip_count = 0

for article_file in articles_to_process:
    try:
        # Read file
        with open(article_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if educational section already exists
        if '<!-- Sezione Formativa -->' in content:
            print(f"⚠ {article_file}: Sezione formativa già presente, skip")
            skip_count += 1
            continue

        # Find position before disclaimer
        pattern = r'(</div>\s*\n\s*<div class="mt-12 pt-8 border-t-2 border-gray-200 bg-yellow-50 p-6 rounded-lg">)'

        # Use specific section if available, otherwise generic
        if article_file in specific_sections:
            educational_content = specific_sections[article_file]
        else:
            educational_content = generic_educational

        replacement = educational_content + '\n\n            <div class="mt-12 pt-8 border-t-2 border-gray-200 bg-yellow-50 p-6 rounded-lg">'

        content = re.sub(pattern, replacement, content)

        # Write back
        with open(article_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✓ {article_file}: Sezione formativa aggiunta")
        success_count += 1

    except Exception as e:
        print(f"✗ {article_file}: Errore - {str(e)}")

print(f"\n✓ Completato!")
print(f"✓ Sezioni aggiunte: {success_count}")
print(f"⚠ Già presenti: {skip_count}")
print(f"\n✓ TOTALE articoli con sezione formativa: {10 + success_count} su 29")
