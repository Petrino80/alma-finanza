#!/usr/bin/env python3
"""Aggiorna impara-finanza.html con i concetti educativi degli articoli dell'11 Marzo 2026"""
import re

with open('impara-finanza.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Definisco i concept-card per sezione
concepts = {
    'Macroeconomia e Banche Centrali': [
        {
            'href': 'articolo-wall-street-11mar-cpi-stabile-nebius-nvidia-petrolio.html',
            'title': 'Consumer Price Index (CPI)',
            'desc': 'Misura la variazione media dei prezzi al consumo, indicatore chiave di inflazione seguito dalla Fed. Il CPI "core" esclude alimentari ed energia per catturare il trend sottostante.',
            'source': 'Wall Street 11 Mar: CPI 2,4%',
            'color': 'cyan'
        },
        {
            'href': 'articolo-europa-11mar-dax-cede-rheinmetall-earnings.html',
            'title': 'Impatto del petrolio sulle borse europee',
            'desc': "L'Europa è importatore netto di energia: il rialzo del petrolio aumenta i costi di produzione, alimenta l'inflazione e deteriora la bilancia commerciale, penalizzando in particolare il DAX tedesco.",
            'source': 'Europa 11 Mar: DAX -1,6%',
            'color': 'cyan'
        }
    ],
    'Meccanismi di Mercato': [
        {
            'href': 'articolo-ftse-mib-11mar-fusione-mps-mediobanca-diasorin.html',
            'title': 'Fusione per incorporazione',
            'desc': "Operazione in cui una società (incorporante) assorbe un'altra (incorporata) che cessa di esistere. Gli azionisti dell'incorporata ricevono azioni dell'incorporante secondo un rapporto di concambio.",
            'source': 'FTSE MIB 11 Mar: MPS-Mediobanca',
            'color': 'purple'
        },
        {
            'href': 'articolo-ftse-mib-11mar-fusione-mps-mediobanca-diasorin.html',
            'title': 'Concambio azionario nelle fusioni',
            'desc': "Rapporto con cui le azioni dell'incorporata vengono convertite in azioni dell'incorporante. Tiene conto di capitalizzazione, patrimonio netto, redditività e sinergie. Un concambio superiore alle attese è un premio per gli azionisti.",
            'source': 'FTSE MIB 11 Mar: concambio 2,45x',
            'color': 'purple'
        },
        {
            'href': 'articolo-europa-11mar-dax-cede-rheinmetall-earnings.html',
            'title': 'Lo Stoxx 600: indice benchmark europeo',
            'desc': "Include le 600 società a maggiore capitalizzazione di 17 Paesi europei, coprendo il 90% della capitalizzazione di mercato dell'Europa. Offre una visione aggregata della salute dei mercati europei.",
            'source': 'Europa 11 Mar: Stoxx 600 -0,8%',
            'color': 'purple'
        },
        {
            'href': 'articolo-petrolio-11mar-iea-riserve-400m-barili-hormuz.html',
            'title': "Perché il rilascio delle riserve non fa scendere il petrolio",
            'desc': "Il rilascio è una misura temporanea che non risolve l'interruzione strutturale dell'offerta. 400M barili equivalgono a ~20 giorni di flusso attraverso Hormuz. Il mercato prezza il rischio di crisi prolungata.",
            'source': 'Petrolio 11 Mar: IEA 400M bbl',
            'color': 'purple'
        }
    ],
    'Modelli di Business': [
        {
            'href': 'articolo-nvidia-nebius-11mar-2b-ai-cloud-infrastruttura.html',
            'title': 'Neocloud: provider cloud specializzati per AI',
            'desc': "Nuova categoria di cloud provider (Nebius, CoreWeave, Lambda) focalizzati su infrastruttura ottimizzata per training e inference AI, con cluster GPU pre-configurati e connettività ad alta velocità.",
            'source': 'Nvidia-Nebius 11 Mar: $2B AI cloud',
            'color': 'teal'
        },
        {
            'href': 'articolo-nvidia-nebius-11mar-2b-ai-cloud-infrastruttura.html',
            'title': 'Modello invest-and-supply di Nvidia',
            'desc': "Strategia in cui Nvidia investe in aziende clienti, creando un circolo virtuoso: investimento → acquisto GPU → crescita domanda → crescita azioni → più investimenti. Simile al modello Intel degli anni 2000.",
            'source': 'Nvidia-Nebius 11 Mar: ecosistema AI',
            'color': 'teal'
        }
    ],
    'Metriche Settoriali': [
        {
            'href': 'articolo-europa-11mar-dax-cede-rheinmetall-earnings.html',
            'title': 'Il backlog nel settore difesa',
            'desc': "Valore totale degli ordini ricevuti ma non evasi. Nel settore difesa indica lavoro garantito per anni, ma il suo valore dipende dalla capacità produttiva di convertirlo in ricavi (tooling, personale, certificazioni).",
            'source': 'Europa 11 Mar: Rheinmetall €63,8B backlog',
            'color': 'amber'
        },
        {
            'href': 'articolo-ftse-mib-11mar-fusione-mps-mediobanca-diasorin.html',
            'title': 'Correlazione petrolio-titoli energetici',
            'desc': "Le società petrolifere hanno correlazione positiva col greggio: quando il petrolio sale, i ricavi aumentano a costi di estrazione stabili. L'effetto varia in base a hedging, mix gas/petrolio e struttura contrattuale.",
            'source': 'FTSE MIB 11 Mar: ENI +2%',
            'color': 'amber'
        }
    ],
    'Gestione del Rischio': [
        {
            'href': 'articolo-petrolio-11mar-iea-riserve-400m-barili-hormuz.html',
            'title': 'Correlazione inversa oro-dollaro',
            'desc': "Oro e dollaro hanno correlazione tipicamente inversa: un dollaro forte rende l'oro più costoso per chi usa altre valute. L'oro può scendere anche in crisi se il dollaro si rafforza come bene rifugio ultimo.",
            'source': 'Petrolio 11 Mar: Oro -1,3%',
            'color': 'red'
        }
    ],
    'Geopolitica e Mercati': [
        {
            'href': 'articolo-petrolio-11mar-iea-riserve-400m-barili-hormuz.html',
            'title': 'Lo Stretto di Hormuz: collo di bottiglia petrolifero',
            'desc': "Passaggio marittimo largo 33 km tra Iran e Oman dove transita il 20% dell'offerta mondiale di petrolio (~20M bbl/giorno). La sua chiusura ha impatto immediato e drammatico sui prezzi del greggio.",
            'source': 'Petrolio 11 Mar: Hormuz sotto attacco',
            'color': 'rose'
        }
    ],
    'Energia & Infrastrutture': [
        {
            'href': 'articolo-wall-street-11mar-cpi-stabile-nebius-nvidia-petrolio.html',
            'title': 'Riserve Strategiche di Petrolio (SPR)',
            'desc': "Scorte di greggio mantenute dai governi IEA per emergenze di approvvigionamento. Ogni membro detiene almeno 90 giorni di importazioni nette. Il rilascio è misura straordinaria per stabilizzare i mercati.",
            'source': 'Wall Street 11 Mar: IEA 400M bbl',
            'color': 'orange'
        },
        {
            'href': 'articolo-nvidia-nebius-11mar-2b-ai-cloud-infrastruttura.html',
            'title': 'La corsa ai gigawatt: data center e AI',
            'desc': "La capacità dei data center si misura in GW. Nebius punta a 5+ GW entro 2030 (equivalente a ~5 centrali nucleari). I data center già consumano il 2-3% dell'elettricità mondiale.",
            'source': 'Nvidia-Nebius 11 Mar: 5 GW data center',
            'color': 'orange'
        }
    ]
}

# Per ogni sezione, trovo la chiusura della griglia e inserisco prima
count = 0
for section_name, cards in concepts.items():
    for card in cards:
        concept_html = f'''        <a href="{card['href']}" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-{card['color']}-500 hover:border-{card['color']}-600">
            <h3 class="font-bold text-lg mb-2 text-gray-900">{card['title']}</h3>
            <p class="text-sm text-gray-600">{card['desc']}</p>
            <span class="text-xs text-{card['color']}-600 font-semibold mt-2 inline-block">→ Spiegato in: {card['source']}</span>
        </a>'''

        # Cerco il titolo della sezione nell'HTML
        # Le sezioni hanno format come: <h2 ...>📊 Valutazioni e Multipli</h2> followed by grid
        # Cerco il pattern della sezione e inserisco la card alla fine della griglia

        # Pattern: sezione con il nome, poi trovo </div> che chiude la griglia
        section_pattern = re.escape(section_name)
        match = re.search(section_pattern, html)
        if match:
            # Trova la fine della griglia: cerca il primo </div>\s*</section> dopo la sezione
            grid_end = html.find('</section>', match.end())
            if grid_end > 0:
                # Cerca l'ultimo </div> prima di </section> - quello chiude la griglia
                last_div = html.rfind('</div>', match.end(), grid_end)
                if last_div > 0:
                    html = html[:last_div] + '\n' + concept_html + '\n        ' + html[last_div:]
                    count += 1

with open('impara-finanza.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ impara-finanza.html: {count} nuovi concept-card aggiunti")
print("🎉 Impara la Finanza aggiornato!")
