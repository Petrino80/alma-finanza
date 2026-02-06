#!/usr/bin/env python3
"""
Aggiunge sezioni formative personalizzate a tutti gli articoli
"""
import re

# Definizione sezioni formative per ogni articolo
educational_sections = {
    "articolo-spotify-declino.html": """
            <!-- Sezione Formativa -->
            <div class="mt-12 pt-8 border-t-2 border-gray-200 bg-blue-50 p-6 rounded-lg">
                <h3 class="text-xl font-bold mb-4 montserrat-font text-blue-900">📚 Sezione Formativa: Concetti Chiave</h3>
                <div class="space-y-4 text-gray-700">
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Cosa significa "EPS" (Earnings Per Share)?</h4>
                        <p class="text-sm">EPS sta per "Earnings Per Share", cioè l'utile per azione. Si calcola dividendo l'utile netto per il numero di azioni in circolazione. Un EPS di $2.95 significa che ogni azione genera $2.95 di profitto. Un aumento del 56.9% YoY indica forte crescita della redditività.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Performance "YTD" (Year-to-Date)</h4>
                        <p class="text-sm">YTD indica la performance dall'inizio dell'anno ad oggi. Spotify -23% YTD 2026 significa che il titolo ha perso il 23% dal 1° gennaio 2026. Questo dato è diverso dalla performance di una singola sessione (-6.4%), che misura solo un giorno di trading.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Pressione "pre-earnings"</h4>
                        <p class="text-sm">Prima della pubblicazione degli earnings (risultati trimestrali), i titoli possono scendere per "de-risking": investitori vendono per evitare sorprese negative. Anche con earnings attesi positivi, l'incertezza spinge le vendite preventive.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Competizione streaming e pricing power</h4>
                        <p class="text-sm">Il pricing power (capacità di aumentare prezzi) indica forza competitiva. Spotify può alzare i prezzi a $12.99/mese perché ha una base utenti fedele e contenuti esclusivi. La competizione con Apple Music e YouTube Music richiede investimenti continui in contenuti e tecnologia.</p>
                    </div>
                </div>
            </div>
""",

    "articolo-feim-sorpresa.html": """
            <!-- Sezione Formativa -->
            <div class="mt-12 pt-8 border-t-2 border-gray-200 bg-blue-50 p-6 rounded-lg">
                <h3 class="text-xl font-bold mb-4 montserrat-font text-blue-900">📚 Sezione Formativa: Concetti Chiave</h3>
                <div class="space-y-4 text-gray-700">
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Cosa sono le "micro-cap" e "small-cap"?</h4>
                        <p class="text-sm"><strong>Micro-cap</strong>: market cap tra $50M e $300M. <strong>Small-cap</strong>: tra $300M e $2B. FEIM con $492M è una small-cap. Questi titoli sono più volatili ma possono offrire crescita maggiore rispetto alle large-cap (oltre $10B).</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 "Earnings miss" del 37.93%: cosa significa?</h4>
                        <p class="text-sm">Un "miss" indica risultati inferiori alle attese degli analisti. FEIM: EPS $0.18 vs $0.29 atteso = -37.93% rispetto alle stime. I mercati puniscono duramente questi miss perché segnalano debolezza del business o guidance troppo ottimistica.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Defense tech contractors: modello di business</h4>
                        <p class="text-sm">Le aziende defense tech come Frequency Electronics vendono sistemi elettronici (es. airborne systems) principalmente a governi e contractor della difesa. I ricavi dipendono da contratti governativi, che possono essere irregolari, creando volatilità nei risultati trimestrali.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Rischi specifici delle small-cap</h4>
                        <p class="text-sm">Le small-cap come FEIM hanno: (1) <strong>Liquidità limitata</strong> (pochi scambi giornalieri), (2) <strong>Volatilità elevata</strong> (grandi oscillazioni percentuali), (3) <strong>Minor copertura analisti</strong> (informazioni meno disponibili). Richiedono maggiore due diligence.</p>
                    </div>
                </div>
            </div>
""",

    "articolo-meta-earnings-attesi.html": """
            <!-- Sezione Formativa -->
            <div class="mt-12 pt-8 border-t-2 border-gray-200 bg-blue-50 p-6 rounded-lg">
                <h3 class="text-xl font-bold mb-4 montserrat-font text-blue-900">📚 Sezione Formativa: Concetti Chiave</h3>
                <div class="space-y-4 text-gray-700">
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 "Beat" vs "Miss" negli earnings</h4>
                        <p class="text-sm">Un <strong>beat</strong> indica risultati superiori alle stime degli analisti. Meta: EPS $8.88 vs $8.19 atteso = +8.4% beat. Anche i revenue hanno battuto le attese ($59.9B vs $58.4B). I beat spesso portano a rialzi del titolo, ma non sempre se la guidance delude.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Cos'è il CapEx (Capital Expenditure)?</h4>
                        <p class="text-sm">CapEx = investimenti in asset fisici (data center, server, AI chips). Meta CapEx 2026: $115-135 miliardi, +84% vs 2025. Questo riduce il cash flow disponibile oggi, ma crea infrastruttura per ricavi futuri. Gli investitori temono che questi investimenti impieghino anni a ripagare.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 "Guidance" e impatto sul prezzo</h4>
                        <p class="text-sm">La guidance è la stima aziendale dei risultati futuri. Anche con earnings Q4 positivi, se la guidance delude (come il CapEx shock di Meta), il titolo può scendere. Gli investitori comprano basandosi sul futuro, non sul passato.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 AI investments: quando ripagano?</h4>
                        <p class="text-sm">Gli investimenti AI massicci ($115-135B per Meta) hanno ritorni incerti e lontani nel tempo. I mercati scontano questi ritorni futuri con un tasso di sconto: più lontani nel tempo, meno valgono oggi. Questo spiega perché titoli tech scendono nonostante investimenti "positivi" in AI.</p>
                    </div>
                </div>
            </div>
""",

    "articolo-treasury-yields-impatto.html": """
            <!-- Sezione Formativa -->
            <div class="mt-12 pt-8 border-t-2 border-gray-200 bg-blue-50 p-6 rounded-lg">
                <h3 class="text-xl font-bold mb-4 montserrat-font text-blue-900">📚 Sezione Formativa: Concetti Chiave</h3>
                <div class="space-y-4 text-gray-700">
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Cos'è il Treasury Yield 10-year?</h4>
                        <p class="text-sm">Il yield del Treasury 10-year è il rendimento dei titoli di Stato USA a 10 anni, considerato il "tasso risk-free" (senza rischio). Attualmente al 4.28%, indica quanto gli investitori guadagnano prestando denaro al governo USA per 10 anni.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Perché yield alto danneggia i growth stocks?</h4>
                        <p class="text-sm">I growth stocks (titoli ad alta crescita come tech) valgono per i profitti futuri. Il DCF (Discounted Cash Flow) sconta questi profitti usando il Treasury yield come tasso base. Yield 4.28% vs 4.17% riduce il valore presente dei profitti futuri del ~1%, abbassando le valutazioni.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Matematica DCF semplificata</h4>
                        <p class="text-sm">Formula base: Valore Presente = Profitti Futuri / (1 + tasso)^anni. Con yield da 4.17% a 4.28%, il denominatore aumenta, quindi il valore presente diminuisce. Per profitti tra 5-10 anni, l'impatto può essere 3-7% di riduzione del valore.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Treasury yield vs Federal Reserve</h4>
                        <p class="text-sm">Il Treasury yield riflette le aspettative di mercato sui tassi Fed futuri, inflazione e crescita economica. Nomine Fed (come Kevin Warsh) e dati economici (ADP jobs) influenzano queste aspettative, muovendo i yield e quindi le valutazioni azionarie.</p>
                    </div>
                </div>
            </div>
""",

    "articolo-oro-alltime-high.html": """
            <!-- Sezione Formativa -->
            <div class="mt-12 pt-8 border-t-2 border-gray-200 bg-blue-50 p-6 rounded-lg">
                <h3 class="text-xl font-bold mb-4 montserrat-font text-blue-900">📚 Sezione Formativa: Concetti Chiave</h3>
                <div class="space-y-4 text-gray-700">
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Perché l'oro sale con l'inflazione?</h4>
                        <p class="text-sm">L'oro è un "safe haven" (bene rifugio) che mantiene valore quando le valute fiat (dollaro, euro) si svalutano per inflazione. Con inflazione alta, gli investitori spostano capitale da cash/bond verso oro, facendo salire il prezzo. L'oro non produce interessi ma protegge il potere d'acquisto.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Rally +25% e +6% intraday: è sostenibile?</h4>
                        <p class="text-sm">Un rally del +25% da inizio 2025 e balzi intraday del +6% (massimo dal 2008) indicano <strong>volatilità estrema</strong>. Questi movimenti suggeriscono panic buying e posizionamenti speculativi. Storicamente, rally così rapidi sono seguiti da correzioni (pullback) per consolidamento.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 "Pullback" vs "correzione" vs "bear market"</h4>
                        <p class="text-sm"><strong>Pullback</strong>: ribasso 5-10% (normale). <strong>Correzione</strong>: -10-20% (sana dopo rally). <strong>Bear market</strong>: -20%+ (inversione trend). Oro da $4,913 a $4,852 è un pullback normale dopo ATH, non un cambio di trend.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Oro vs Bitcoin come "digital gold"</h4>
                        <p class="text-sm">Bitcoin è chiamato "digital gold" per scarsità (21M supply cap) e proprietà anti-inflazionistiche. Ma è 10x più volatile dell'oro. Oro $4,852 ha storia di 5000 anni come store of value, Bitcoin solo 15 anni. Molti investitori diversificano tra entrambi.</p>
                    </div>
                </div>
            </div>
""",

    "articolo-small-caps-performance.html": """
            <!-- Sezione Formativa -->
            <div class="mt-12 pt-8 border-t-2 border-gray-200 bg-blue-50 p-6 rounded-lg">
                <h3 class="text-xl font-bold mb-4 montserrat-font text-blue-900">📚 Sezione Formativa: Concetti Chiave</h3>
                <div class="space-y-4 text-gray-700">
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Cos'è il Russell 2000?</h4>
                        <p class="text-sm">Il Russell 2000 è l'indice che traccia le 2000 small-cap USA (market cap $300M-$2B circa). Rappresenta il 10% della capitalizzazione totale del mercato USA ma offre esposizione a società più piccole con maggiore potenziale di crescita rispetto a S&P 500 (large-cap).</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 "Great Rotation": cosa significa?</h4>
                        <p class="text-sm">La Great Rotation è uno spostamento di capitale da mega-cap tech (Apple, Microsoft, Nvidia) verso small-cap. Avviene quando gli investitori vedono le valutazioni tech troppo alte e cercano "value" nelle small-cap sottovalutate. Russell 2000 +3.8% YTD vs S&P flat conferma questa rotazione.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Earnings growth consensus 17-22%: cosa significa?</h4>
                        <p class="text-sm">Il consensus è la stima media degli analisti. Earnings growth 17-22% per 2026 significa che gli analisti prevedono crescita degli utili delle small-cap del 17-22%. Se confermato, giustificherebbe valutazioni più alte. Il range (17-22%) mostra incertezza nelle stime.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Rischi e opportunità delle small-cap</h4>
                        <p class="text-sm"><strong>Opportunità</strong>: crescita potenziale superiore, M&A target, undervalued. <strong>Rischi</strong>: volatilità alta, liquidità bassa, maggiore sensibilità a recessioni, minor accesso a capitale. Small-cap fanno bene in cicli economici espansivi.</p>
                    </div>
                </div>
            </div>
""",

    "articolo-usa-europa-divergenza.html": """
            <!-- Sezione Formativa -->
            <div class="mt-12 pt-8 border-t-2 border-gray-200 bg-blue-50 p-6 rounded-lg">
                <h3 class="text-xl font-bold mb-4 montserrat-font text-blue-900">📚 Sezione Formativa: Concetti Chiave</h3>
                <div class="space-y-4 text-gray-700">
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 "Divergenza" tra mercati: cause</h4>
                        <p class="text-sm">La divergenza (USA -0.84% vs Europa +0.6% il 3 febbraio) deriva da: (1) <strong>Composizione settoriale</strong>: USA tech-heavy, Europa più industrials/financials. (2) <strong>Drivers differenti</strong>: USA dipende da AI, Europa da reflation e valuation. (3) <strong>Cicli economici</strong>: possono essere sfasati.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Cosa significa "reflation"?</h4>
                        <p class="text-sm">Reflation è la ripresa dell'inflazione e della crescita economica dopo un periodo di stagnazione/deflazione. Europa beneficia di reflation perché: settori ciclici (industrials, materials) performano bene, earnings migliorano, investitori vedono prospettive di crescita dopo anni difficili.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 "Valuation support": perché conta?</h4>
                        <p class="text-sm">Valuation = prezzo pagato per $1 di earnings. P/E ratio Europa ~13-14x vs USA ~20-22x. Valutazioni basse offrono "support" (supporto) perché il downside è limitato: difficile scendere ulteriormente quando già sottovalutato. USA ha più "aria sotto i piedi".</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Earnings revision: da +8% a -1% in Europa</h4>
                        <p class="text-sm">Le earnings revision sono aggiustamenti delle stime degli analisti. Quando le stime passano da +8% a -1%, indica deterioramento delle prospettive. Nonostante questo downgrade, Europa regge bene grazie a valutazioni basse che incorporano già aspettative modeste.</p>
                    </div>
                </div>
            </div>
""",

    "articolo-mercati-sell-off-febbraio.html": """
            <!-- Sezione Formativa -->
            <div class="mt-12 pt-8 border-t-2 border-gray-200 bg-blue-50 p-6 rounded-lg">
                <h3 class="text-xl font-bold mb-4 montserrat-font text-blue-900">📚 Sezione Formativa: Concetti Chiave</h3>
                <div class="space-y-4 text-gray-700">
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 Cosa significa "sell-off"?</h4>
                        <p class="text-sm">Un sell-off è una vendita massiccia e rapida di azioni che causa ribassi significativi. Il sell-off del 5 febbraio (S&P YTD negativo, Nasdaq -1.59%) è stato causato da profit-taking, timore su valutazioni tech, e annunci CapEx shock (Alphabet $185B, Amazon $200B).</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 AMD -$560B market cap: come è possibile?</h4>
                        <p class="text-sm">Un calo del -17.3% per AMD ha cancellato $560 miliardi di market cap. Questo avviene quando: prezzo azione scende, numero azioni in circolazione × prezzo = market cap. Per le mega-cap, anche cali percentuali moderati si traducono in miliardi di dollari persi. Riflette il "de-rating" delle valutazioni AI.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 "Fine AI hype phase": cosa cambia?</h4>
                        <p class="text-sm">La fase di hype AI (2023-2025) ha visto valutazioni spinte alle stelle da aspettative di crescita illimitata. La "fine hype" significa transizione a una fase più razionale: investitori chiedono proof of ROI (ritorno sugli investimenti) invece di promesse. CapEx massicci senza ricavi proporzionati preoccupano.</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-blue-800 mb-2">🔹 "Risk-off stance": psicologia di mercato</h4>
                        <p class="text-sm">Risk-off = investitori vendono asset rischiosi (tech growth) per rifugiarsi in safe haven (cash, Treasury, oro). Segnali risk-off: Nasdaq sotto pressione, bond yields stabili/in calo, oro in rialzo. Opposito di risk-on, quando speculazione e appetite per rischio dominano.</p>
                    </div>
                </div>
            </div>
"""
}

# Articoli restanti da processare (già fatti: wall-street-rimbalzo-6feb, europa-stoxx-600-record)
articles_to_process = [
    "articolo-spotify-declino.html",
    "articolo-feim-sorpresa.html",
    "articolo-meta-earnings-attesi.html",
    "articolo-treasury-yields-impatto.html",
    "articolo-oro-alltime-high.html",
    "articolo-small-caps-performance.html",
    "articolo-usa-europa-divergenza.html",
    "articolo-mercati-sell-off-febbraio.html"
]

for article_file in articles_to_process:
    try:
        # Read file
        with open(article_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if educational section already exists
        if '<!-- Sezione Formativa -->' in content:
            print(f"⚠ {article_file}: Sezione formativa già presente, skip")
            continue

        # Find position before disclaimer
        pattern = r'(</div>\s*\n\s*<div class="mt-12 pt-8 border-t-2 border-gray-200 bg-yellow-50 p-6 rounded-lg">)'

        if article_file in educational_sections:
            educational_content = educational_sections[article_file]
            replacement = educational_content + '\n\n            <div class="mt-12 pt-8 border-t-2 border-gray-200 bg-yellow-50 p-6 rounded-lg">'

            content = re.sub(pattern, replacement, content)

            # Write back
            with open(article_file, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"✓ {article_file}: Sezione formativa aggiunta")
        else:
            print(f"⚠ {article_file}: Sezione formativa non definita, skip")

    except Exception as e:
        print(f"✗ {article_file}: Errore - {str(e)}")

print("\n✓ Completato! Prime 8 sezioni formative aggiunte.")
print("✓ Totale articoli con sezione formativa: 10 (inclusi wall-street e europa)")
