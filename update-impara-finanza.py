#!/usr/bin/env python3
"""Add missing educational concepts to impara-finanza.html from recent articles."""
import re, os

BASE = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE, 'impara-finanza.html')

with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

def card(href, title, desc, source, color):
    return f'''
                <a href="{href}" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-{color}-500 hover:border-{color}-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">{title}</h3>
                    <p class="text-sm text-gray-600">{desc}</p>
                    <span class="text-xs text-{color}-600 font-semibold mt-2 inline-block">→ Spiegato in: {source}</span>
                </a>'''

# ============================================================
# VALUTAZIONI E MULTIPLI (blue) — add before </div></section> of that section
# ============================================================
valutazioni_cards = ''.join([
    card('articolo-wall-street-10mar-mixed-oil-crash-oracle.html',
         'Revenue Miss: Cosa Significa e Perché Impatta',
         'Quando i ricavi sono sotto il consensus degli analisti. Impatta più dell\'EPS perché segnala debolezza della domanda, non solo margini.',
         'Wall Street 10 Mar', 'blue'),
    card('articolo-oracle-10mar-earnings-cloud-ai-44-percento.html',
         'Earnings "Beat" vs "Miss"',
         'Come leggere i risultati trimestrali rispetto alle attese di Wall Street. La reazione del titolo dipende dal consensus, non dal dato assoluto.',
         'Oracle Earnings 10 Mar', 'blue'),
    card('articolo-broadcom-q1-fy26-5mar-ai-100b-target.html',
         'Run-Rate: Come Si Calcola',
         'Proiezione annualizzata basata su dati parziali. Es: revenue Q1 × 4 = run-rate annuo. Utile ma può essere fuorviante per business stagionali.',
         'Broadcom Q1 5 Mar', 'blue'),
    card('articolo-walmart-q4-19feb-ricavi-guidance.html',
         'Comparable Sales (Comp Sales)',
         'Crescita delle vendite a parità di punti vendita. Esclude nuove aperture e chiusure. La metrica regina del retail per valutare la crescita organica.',
         'Walmart Q4 19 Feb', 'blue'),
])

# ============================================================
# MACROECONOMIA E BANCHE CENTRALI (cyan)
# ============================================================
macro_cards = ''.join([
    card('articolo-fed-minutes-19feb-hawkish-pause-tassi.html',
         'Hawkish vs Dovish',
         'Hawkish: atteggiamento restrittivo della banca centrale (tassi alti). Dovish: accomodante (tassi bassi). Le parole dei banchieri centrali muovono i mercati.',
         'Fed Minutes 19 Feb', 'cyan'),
    card('articolo-fed-minutes-19feb-hawkish-pause-tassi.html',
         'PCE (Personal Consumption Expenditures)',
         'L\'indicatore di inflazione preferito dalla Fed. Misura la variazione dei prezzi dei beni e servizi acquistati dai consumatori. Più ampio del CPI.',
         'Fed Minutes 19 Feb', 'cyan'),
    card('articolo-ppi-inflazione-27feb-fed-tassi-pce.html',
         'PPI, CPI e PCE — Le Tre Misure di Inflazione',
         'PPI misura i prezzi alla produzione, CPI al consumo, PCE i consumi personali. La Fed guarda soprattutto il Core PCE per decidere sui tassi.',
         'PPI e Inflazione 27 Feb', 'cyan'),
    card('articolo-jobs-report-6mar-nfp-92k-disoccupazione.html',
         'Non-Farm Payrolls (NFP) e Jobs Report',
         'Il dato mensile sull\'occupazione USA, pubblicato il primo venerdì del mese. Uno dei market mover più potenti. Esclude settore agricolo.',
         'Jobs Report 6 Mar', 'cyan'),
    card('articolo-iran-guerra-giorno6-5mar-economia-mercati.html',
         'Stagflazione: Cos\'è e Perché È Pericolosa',
         'Combinazione di stagnazione economica e inflazione alta. Lo scenario peggiore per le banche centrali: alzare i tassi peggiora la crescita, abbassarli peggiora l\'inflazione.',
         'Iran Guerra Giorno 6 · 5 Mar', 'cyan'),
    card('articolo-btp-valore-27feb-tassi-collocamento-marzo.html',
         'Cedola Step-Up vs Cedola Fissa',
         'Le cedole step-up crescono nel tempo (es. 2% → 3%), premiando chi tiene il titolo fino a scadenza. Le fisse pagano sempre lo stesso importo.',
         'BTP Valore 27 Feb', 'cyan'),
    card('articolo-trump-dazi-globali-15-section-122-25feb.html',
         'Section 122 vs IEEPA — Poteri Presidenziali sui Dazi',
         'Due strumenti legali USA per imporre tariffe. Section 122 è limitata (150 giorni, 15% max). IEEPA è più potente ma richiede emergenza nazionale.',
         'Trump Dazi Globali 25 Feb', 'cyan'),
    card('articolo-trump-dazi-globali-15-section-122-25feb.html',
         'Come i Dazi Impattano i Mercati',
         'I dazi aumentano i costi per importatori e consumatori, alimentano l\'inflazione, riducono i margini aziendali e possono innescare guerre commerciali.',
         'Trump Dazi Globali 25 Feb', 'cyan'),
])

# ============================================================
# MECCANISMI DI MERCATO (purple)
# ============================================================
meccanismi_cards = ''.join([
    card('articolo-wall-street-24feb-rimbalzo-turnaround-tuesday.html',
         'Turnaround Tuesday',
         'Pattern statistico: dopo un lunedì di sell-off, il martedì tende a rimbalzare. Causato da ribilanciamenti istituzionali e caccia ai minimi.',
         'Wall Street 24 Feb', 'purple'),
    card('articolo-wall-street-28feb-settimana-mese-febbraio-chiusura.html',
         '"Sell the News" — Vendere sulla Notizia',
         'Quando il mercato scende nonostante notizie positive. Gli investitori avevano già comprato sull\'attesa e vendono alla conferma. "Buy the rumor, sell the news."',
         'Wall Street 28 Feb', 'purple'),
    card('articolo-wall-street-28feb-settimana-mese-febbraio-chiusura.html',
         'VIX — L\'Indice della Paura',
         'Misura la volatilità attesa dell\'S&P 500 nei prossimi 30 giorni. Sopra 20 = nervosismo. Sopra 30 = paura. Sale quando i mercati scendono.',
         'Wall Street 28 Feb', 'purple'),
    card('articolo-iran-guerra-giorno6-5mar-economia-mercati.html',
         'Risk-Off: Fuga dal Rischio',
         'Quando gli investitori vendono asset rischiosi (azioni, crypto) e comprano beni rifugio (oro, Treasury, CHF). Tipico in periodi di crisi o guerra.',
         'Iran Guerra Giorno 6 · 5 Mar', 'purple'),
    card('articolo-ftse-mib-5mar-nexi-amplifon-campari.html',
         'Short Selling — Vendita allo Scoperto',
         'Vendere azioni prese in prestito per ricomprarle a prezzo inferiore. Profitto sulla differenza. Rischio illimitato se il titolo sale invece di scendere.',
         'FTSE MIB 5 Mar', 'purple'),
    card('articolo-ftse-mib-6mar-difesa-leonardo-avio.html',
         'Perché la Difesa Sale Quando il Mercato Scende',
         'I titoli della difesa sono anti-ciclici in contesti geopolitici: guerra → più spesa militare → più ordini. Correlazione inversa con il sentiment generale.',
         'FTSE MIB 6 Mar', 'purple'),
    card('articolo-wall-street-19feb-dow-calo-walmart-fed.html',
         'Guidance e Consensus degli Analisti',
         'La guidance è la previsione dell\'azienda sui risultati futuri. Il consensus è la media delle stime degli analisti. Il confronto tra i due muove i titoli.',
         'Wall Street 19 Feb', 'purple'),
])

# ============================================================
# MODELLI DI BUSINESS (teal)
# ============================================================
business_cards = ''.join([
    card('articolo-etsy-depop-ebay-19feb-vendita-1-2b.html',
         'M&A: Accretion vs Dilution',
         'Un\'acquisizione è "accretive" se aumenta l\'EPS dell\'acquirente, "dilutive" se lo riduce. Driver chiave: prezzo pagato, sinergie attese, metodo di finanziamento.',
         'Etsy/Depop/eBay 19 Feb', 'teal'),
    card('articolo-etsy-depop-ebay-19feb-vendita-1-2b.html',
         'GMV (Gross Merchandise Value)',
         'Valore totale delle merci vendute su una piattaforma, prima di commissioni e resi. Metrica chiave per marketplace come Etsy, eBay, Amazon.',
         'Etsy/Depop/eBay 19 Feb', 'teal'),
    card('articolo-walmart-q4-19feb-ricavi-guidance.html',
         'Buyback — Riacquisto di Azioni Proprie',
         'L\'azienda ricompra le proprie azioni sul mercato, riducendo il flottante. Aumenta l\'EPS e segnala fiducia del management nel valore dell\'azienda.',
         'Walmart Q4 19 Feb', 'teal'),
    card('articolo-ftse-mib-27feb-mps-mediobanca-saipem.html',
         'Piano Industriale e OPS',
         'Il piano industriale definisce gli obiettivi strategici pluriennali. L\'OPS (Offerta Pubblica di Scambio) è un\'acquisizione pagata con azioni anziché cash.',
         'FTSE MIB 27 Feb', 'teal'),
])

# ============================================================
# METRICHE SETTORIALI (amber)
# ============================================================
metriche_cards = ''.join([
    card('articolo-amd-meta-deal-100b-gpu-ai-24feb.html',
         'Training vs Inferenza nell\'AI',
         'Il training è la fase di apprendimento del modello AI (richiede molte GPU). L\'inferenza è l\'uso del modello addestrato per fare previsioni (meno compute).',
         'AMD-Meta Deal 24 Feb', 'amber'),
    card('articolo-marvell-6mar-earnings-ai-chip-16-percento.html',
         'Chip ASIC — Application-Specific Integrated Circuit',
         'Chip progettati su misura per un\'applicazione specifica (es. AI inference). Più efficienti delle GPU generiche ma meno flessibili. Marvell e Broadcom leader.',
         'Marvell 6 Mar', 'amber'),
    card('articolo-broadcom-q1-fy26-5mar-ai-100b-target.html',
         'XPU — Acceleratore AI Custom',
         'Chip personalizzato progettato per un singolo hyperscaler (Google, Meta, etc). Broadcom ne produce per 3 dei 5 maggiori cloud provider mondiali.',
         'Broadcom Q1 5 Mar', 'amber'),
    card('articolo-oracle-10mar-earnings-cloud-ai-44-percento.html',
         'Infrastruttura Cloud Computing',
         'Servizi di computing on-demand (IaaS, PaaS, SaaS). Oracle, AWS, Azure, Google Cloud competono. Crescita trainata da AI e migrazione enterprise.',
         'Oracle 10 Mar', 'amber'),
    card('articolo-nvidia-earnings-preview-25feb-blackwell-q4.html',
         'Margine Lordo e Pricing Power',
         'Il margine lordo (ricavi - costo del venduto / ricavi) indica il pricing power dell\'azienda. Nvidia ha margini >70% grazie al monopolio GPU AI.',
         'Nvidia Preview 25 Feb', 'amber'),
    card('articolo-ftse-mib-5mar-nexi-amplifon-campari.html',
         'Svalutazione dell\'Avviamento (Goodwill Impairment)',
         'Quando il valore di un\'acquisizione risulta inferiore a quanto pagato. La svalutazione è una perdita contabile che riduce il patrimonio netto.',
         'FTSE MIB 5 Mar', 'amber'),
    card('articolo-ftse-mib-5mar-nexi-amplifon-campari.html',
         'Margine EBITDA — Perché Conta Più dei Ricavi',
         'Il margine EBITDA (EBITDA/Ricavi) misura l\'efficienza operativa. Un\'azienda può crescere nei ricavi ma perdere valore se il margine si comprime.',
         'FTSE MIB 5 Mar', 'amber'),
])

# ============================================================
# GESTIONE DEL RISCHIO (red)
# ============================================================
rischio_cards = ''.join([
    card('articolo-wall-street-5mar-dow-crollo-iran-petrolio.html',
         'Fuel Hedging — Copertura Carburante',
         'Le compagnie aeree bloccano il prezzo del carburante con contratti futures per proteggersi da rialzi improvvisi. Chi non copre subisce il pieno impatto dei picchi.',
         'Wall Street 5 Mar', 'red'),
    card('articolo-bitcoin-oro-28feb-iran-guerra-safe-haven.html',
         'Asset "Safe Haven" — Beni Rifugio',
         'Asset che tendono a mantenere o aumentare il valore durante le crisi: oro, Treasury USA, franco svizzero, yen. Bitcoin sta emergendo come potenziale safe haven digitale.',
         'Bitcoin e Oro 28 Feb', 'red'),
    card('articolo-bitcoin-oro-28feb-iran-guerra-safe-haven.html',
         'Liquidazione nel Trading Crypto',
         'Chiusura forzata di una posizione a leva quando il collaterale scende sotto la soglia minima. $580M liquidati in 24h durante il crash Iran.',
         'Bitcoin e Oro 28 Feb', 'red'),
    card('articolo-wall-street-27feb-dow-calo-ppi-netflix.html',
         'Termination Fee — Penale di Uscita',
         'Clausola contrattuale che impone il pagamento di una penale se un\'operazione di M&A salta. Protegge il venditore se l\'acquirente si ritira.',
         'Wall Street 27 Feb', 'red'),
])

# ============================================================
# ENERGIA & INFRASTRUTTURE (orange)
# ============================================================
energia_cards = ''.join([
    card('articolo-petrolio-6mar-wti-90-record-settimana-hormuz.html',
         'WTI vs Brent — Le Due Benchmark del Petrolio',
         'WTI (West Texas Intermediate): benchmark USA, più leggero. Brent: benchmark europeo/globale, estratto nel Mare del Nord. Il Brent premia solitamente 2-5$ in più.',
         'Petrolio WTI $90 · 6 Mar', 'orange'),
    card('articolo-petrolio-stretto-hormuz-28feb-iran-spike-oil.html',
         'Stretto di Hormuz — Il Collo di Bottiglia del Mondo',
         'Passaggio largo 33 km tra Iran e Oman. Transita il 20% del petrolio mondiale. La sua chiusura farebbe esplodere i prezzi dell\'energia globale.',
         'Petrolio Hormuz 28 Feb', 'orange'),
    card('articolo-europa-10mar-rally-dax-cac-petrolio-giu.html',
         'Premio di Rischio Geopolitico sul Petrolio',
         'Il sovrapprezzo che il mercato paga per il rischio di interruzioni dell\'offerta durante conflitti. Può aggiungere $10-20 al prezzo del barile. Svanisce con la de-escalation.',
         'Europa Rally 10 Mar', 'orange'),
    card('articolo-petrolio-10mar-crash-trump-iran-fine-guerra.html',
         'Riserve Petrolifere Strategiche (SPR)',
         'Scorte di petrolio governative per emergenze. Gli USA hanno la più grande SPR al mondo (~400M barili). Usate per stabilizzare i prezzi in caso di crisi.',
         'Petrolio Crash 10 Mar', 'orange'),
    card('articolo-petrolio-5mar-iran-petroliera-wti-81.html',
         'Perché il Petrolio Alto Colpisce le Azioni',
         'Il petrolio caro aumenta i costi delle aziende (trasporti, materie prime), comprime i margini, alimenta l\'inflazione e spinge la Fed ad alzare i tassi.',
         'Petrolio $81 · 5 Mar', 'orange'),
    card('articolo-ftse-mib-10mar-rimbalzo-unicredit-stm.html',
         'TTF — Il Prezzo del Gas Europeo',
         'Title Transfer Facility: benchmark del gas naturale in Europa, quotato in €/MWh. L\'Italia è particolarmente esposta perché dipende dal gas per il 40% dell\'energia.',
         'FTSE MIB 10 Mar', 'orange'),
])

# ============================================================
# SETTORE FINANZIARIO & BANCARIO (emerald)
# ============================================================
finanza_cards = ''.join([
    card('articolo-ftse-mib-19feb-fincantieri-tenaris.html',
         'Accelerated Bookbuilding (ABB)',
         'Collocamento lampo di azioni: si chiude in poche ore con sconto del 2-5% sul mercato. Usato per vendite di quote importanti senza impattare troppo il prezzo.',
         'FTSE MIB 19 Feb', 'emerald'),
    card('articolo-ftse-mib-19feb-fincantieri-tenaris.html',
         'IRAP e Impatto sulle Utility',
         'L\'IRAP (Imposta Regionale Attività Produttive) colpisce il valore della produzione. Le utility ne sono particolarmente impattate per l\'alta intensità di capitale.',
         'FTSE MIB 19 Feb', 'emerald'),
    card('articolo-ftse-mib-10mar-rimbalzo-unicredit-stm.html',
         'Perché le Banche Salgono Quando il Petrolio Crolla',
         'Petrolio basso → meno inflazione → tassi più stabili → meno rischio sui crediti. Inoltre riduce il rischio di recessione che colpirebbe i NPL bancari.',
         'FTSE MIB 10 Mar', 'emerald'),
    card('articolo-amd-meta-deal-100b-gpu-ai-24feb.html',
         'Warrant Azionario',
         'Diritto di acquistare azioni a un prezzo prestabilito entro una data futura. Usato come "dolcificante" nei deal (AMD offre warrant a Meta per garantire ordini).',
         'AMD-Meta Deal 24 Feb', 'emerald'),
])

# ============================================================
# NEW SECTION: Geopolitica & Mercati (slate/gray → use indigo)
# Add as new section after "Analisi Tecnica"
# ============================================================
geopolitica_section = '''
        <!-- Category: Geopolitica & Mercati -->
        <section class="mb-10">
            <h2 class="text-2xl font-bold mb-4 montserrat-font text-gray-900 border-b-2 border-rose-500 pb-2">
                🌍 Geopolitica e Mercati
            </h2>
            <div class="grid md:grid-cols-2 gap-4">
                <a href="articolo-iran-operation-epic-fury-28feb-usa-israele-attacco.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-rose-500 hover:border-rose-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Lo Stretto di Hormuz e l'IRGC</h3>
                    <p class="text-sm text-gray-600">Lo Stretto di Hormuz è il passaggio critico per il 20% del petrolio mondiale. L'IRGC (Guardie Rivoluzionarie) è il braccio militare-economico dell'Iran che lo controlla.</p>
                    <span class="text-xs text-rose-600 font-semibold mt-2 inline-block">→ Spiegato in: Operation Epic Fury 28 Feb</span>
                </a>

                <a href="articolo-petrolio-stretto-hormuz-28feb-iran-spike-oil.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-rose-500 hover:border-rose-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Perché il Petrolio Sale con la Guerra</h3>
                    <p class="text-sm text-gray-600">Rischio di interruzione dell'offerta → premio di rischio geopolitico. Blocchi dello Stretto di Hormuz o danni alle infrastrutture petrolifere fanno schizzare i prezzi.</p>
                    <span class="text-xs text-rose-600 font-semibold mt-2 inline-block">→ Spiegato in: Petrolio Hormuz 28 Feb</span>
                </a>

                <a href="articolo-petrolio-10mar-crash-trump-iran-fine-guerra.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-rose-500 hover:border-rose-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Perché il Petrolio Crolla con la Pace</h3>
                    <p class="text-sm text-gray-600">De-escalation → il premio di rischio geopolitico si sgonfia. Il 10 marzo il WTI perse -12% in un giorno quando Trump aprì ai negoziati con l'Iran.</p>
                    <span class="text-xs text-rose-600 font-semibold mt-2 inline-block">→ Spiegato in: Petrolio Crash 10 Mar</span>
                </a>

                <a href="articolo-iran-guerra-giorno6-5mar-economia-mercati.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-rose-500 hover:border-rose-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Come una Guerra Influenza i Tassi di Interesse</h3>
                    <p class="text-sm text-gray-600">Guerra → petrolio alto → inflazione → pressione sui tassi. Ma anche: rallentamento economico → pressione per tagliare. La Fed resta intrappolata tra due fuochi.</p>
                    <span class="text-xs text-rose-600 font-semibold mt-2 inline-block">→ Spiegato in: Iran Guerra Giorno 6 · 5 Mar</span>
                </a>

                <a href="articolo-europa-10mar-rally-dax-cac-petrolio-giu.html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-rose-500 hover:border-rose-600">
                    <h3 class="font-bold text-lg mb-2 text-gray-900">Perché il Crollo del Petrolio Fa Salire le Borse</h3>
                    <p class="text-sm text-gray-600">Meno costi energetici → margini aziendali migliori. Meno inflazione → banche centrali più accomodanti. Più fiducia → ritorno all'appetito per il rischio.</p>
                    <span class="text-xs text-rose-600 font-semibold mt-2 inline-block">→ Spiegato in: Europa Rally 10 Mar</span>
                </a>
            </div>
        </section>
'''

# ============================================================
# NOW INSERT ALL CARDS INTO THE HTML
# ============================================================

def append_to_section(html, section_comment, new_cards):
    """Append new concept cards before the </div> of a section's grid."""
    # Find the section
    idx = html.find(section_comment)
    if idx < 0:
        print(f"  ⚠️ Section not found: {section_comment}")
        return html
    # Find the closing </div> of the grid (</div>\n        </section>)
    # From the section, find the grid div, then its closing </div>
    section_end = html.find('</section>', idx)
    # Find the </div> just before </section> — that's the grid closing
    grid_close = html.rfind('</div>', idx, section_end)
    # Insert new cards before the grid closing
    html = html[:grid_close] + new_cards + '\n            ' + html[grid_close:]
    return html

# Insert cards into each section
html = append_to_section(html, '<!-- Category: Valutazioni e Multipli -->', valutazioni_cards)
print("✅ Valutazioni e Multipli: +4 concetti")

html = append_to_section(html, '<!-- Category: Macroeconomia -->', macro_cards)
print("✅ Macroeconomia: +8 concetti")

html = append_to_section(html, '<!-- Category: Meccanismi di Mercato -->', meccanismi_cards)
print("✅ Meccanismi di Mercato: +7 concetti")

html = append_to_section(html, '<!-- Category: Business Models -->', business_cards)
print("✅ Modelli di Business: +4 concetti")

html = append_to_section(html, '<!-- Category: Metriche Settoriali -->', metriche_cards)
print("✅ Metriche Settoriali: +7 concetti")

html = append_to_section(html, '<!-- Category: Gestione del Rischio -->', rischio_cards)
print("✅ Gestione del Rischio: +4 concetti")

html = append_to_section(html, '<!-- Category: Energia & Infrastrutture -->', energia_cards)
print("✅ Energia & Infrastrutture: +6 concetti")

html = append_to_section(html, '<!-- Category: Settore Finanziario & Bancario -->', finanza_cards)
print("✅ Settore Finanziario & Bancario: +4 concetti")

# Add new Geopolitica section after Analisi Tecnica section
analisi_end = html.find('<!-- Category: Energia & Infrastrutture -->')
if analisi_end > 0:
    html = html[:analisi_end] + geopolitica_section + '\n        ' + html[analisi_end:]
    print("✅ NUOVA SEZIONE: Geopolitica e Mercati (+5 concetti)")

# Write the updated file
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

total_new = 4 + 8 + 7 + 4 + 7 + 4 + 6 + 4 + 5
print(f"\n📊 Totale: +{total_new} nuovi concetti educativi aggiunti")
print(f"   1 nuova sezione: Geopolitica e Mercati")
