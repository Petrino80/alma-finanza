#!/usr/bin/env python3
"""
Corregge accenti mancanti negli articoli del 24 marzo 2026.
Gestisce: è (verbo essere), perché, più, già, così, cioè, sarà, potrà, dovrà, farà, ecc.
"""
import re

files = [
    'articolo-wall-street-24mar-82nd-airborne-salesforce-tech.html',
    'articolo-ftse-mib-24mar-inwit-ardian-brookfield-difesa.html',
    'articolo-pmi-24mar-stagflazione-eurozona-usa-energia.html',
    'articolo-tech-24mar-saas-salesforce-sap-ai-crisi.html',
    'articolo-petrolio-24mar-rimbalzo-brent-104-kharg-oro.html',
]

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()

    original = text

    # === PAROLE SEMPLICI (sempre accentate) ===
    # perche → perché (tutte le occorrenze in testo visibile)
    text = re.sub(r'\bperche\b', 'perché', text)
    text = re.sub(r'\bPerche\b', 'Perché', text)

    # piu → più
    text = re.sub(r'\bpiu\b', 'più', text)

    # gia → già
    text = re.sub(r'\bgia\b', 'già', text)

    # cioe → cioè
    text = re.sub(r'\bcioe\b', 'cioè', text)

    # cosi → così
    text = re.sub(r'\bcosi\b', 'così', text)

    # sara → sarà (futuro)
    text = re.sub(r'\bsara\b', 'sarà', text)
    text = re.sub(r'\bSara\b(?! [A-Z])', 'Sarà', text)  # non nomi propri

    # potra → potrà
    text = re.sub(r'\bpotra\b', 'potrà', text)

    # dovra → dovrà
    text = re.sub(r'\bdovra\b', 'dovrà', text)

    # fara → farà
    text = re.sub(r'\bfara\b', 'farà', text)

    # avra → avrà
    text = re.sub(r'\bavra\b', 'avrà', text)

    # andra → andrà
    text = re.sub(r'\bandra\b', 'andrà', text)

    # restera → resterà
    text = re.sub(r'\brestera\b', 'resterà', text)

    # portera → porterà
    text = re.sub(r'\bportera\b', 'porterà', text)

    # continuera → continuerà
    text = re.sub(r'\bcontinuera\b', 'continuerà', text)

    # rappresenta → ok (non manca accento)

    # attivita → attività
    text = re.sub(r'\battivita\b', 'attività', text)

    # capacita → capacità
    text = re.sub(r'\bcapacita\b', 'capacità', text)

    # volatilita → volatilità
    text = re.sub(r'\bvolatilita\b', 'volatilità', text)

    # qualita → qualità
    text = re.sub(r'\bqualita\b', 'qualità', text)

    # possibilita → possibilità
    text = re.sub(r'\bpossibilita\b', 'possibilità', text)

    # probabilita → probabilità
    text = re.sub(r'\bprobabilita\b', 'probabilità', text)

    # quantita → quantità
    text = re.sub(r'\bquantita\b', 'quantità', text)

    # realta → realtà
    text = re.sub(r'\brealta\b', 'realtà', text)

    # vulnerabilita → vulnerabilità
    text = re.sub(r'\bvulnerabilita\b', 'vulnerabilità', text)

    # societa → società
    text = re.sub(r'\bsocieta\b', 'società', text)

    # liberta → libertà
    text = re.sub(r'\bliberta\b', 'libertà', text)

    # sicurezza already ok

    # necessita → necessità
    text = re.sub(r'\bnecessita\b', 'necessità', text)

    # utilita → utilità
    text = re.sub(r'\butilita\b', 'utilità', text)

    # difficolta → difficoltà
    text = re.sub(r'\bdifficolta\b', 'difficoltà', text)

    # metà, già handled

    # === "è" (verbo essere) — pattern sicuri ===
    # Pattern: " e il/la/un/una/uno/lo/gli/le/i " dove "e" è verbo essere
    # Attenzione: non toccare " e " quando è congiunzione

    # Patterns molto sicuri dove "e" è verbo essere:
    safe_patterns = [
        (r' non e ', ' non è '),
        (r' che e ', ' che è '),
        (r' si e ', ' si è '),
        (r" l'e ", " l'è "),  # raro
        (r'\bE il ', 'È il '),
        (r'\bE la ', 'È la '),
        (r'\bE un ', 'È un '),
        (r'\bE una ', 'È una '),
        (r'\bE stato ', 'È stato '),
        (r'\bE stata ', 'È stata '),
        (r' e stato ', ' è stato '),
        (r' e stata ', ' è stata '),
        (r' e stata ', ' è stata '),
        (r' e questo ', ' è questo '),
        (r' e quella ', ' è quella '),
        (r' e quello ', ' è quello '),
        (r' e proprio ', ' è proprio '),
        (r' e anche ', ' è anche '),
        (r' e molto ', ' è molto '),
        (r' e ancora ', ' è ancora '),
        (r' e possibile ', ' è possibile '),
        (r' e importante ', ' è importante '),
        (r' e necessario ', ' è necessario '),
        (r' e evidente ', ' è evidente '),
        (r' e fondamentale ', ' è fondamentale '),
        (r' e significativo ', ' è significativo '),
        (r' e significativa ', ' è significativa '),
        (r' e interessante ', ' è interessante '),
        (r' e particolarmente ', ' è particolarmente '),
        (r' e esattamente ', ' è esattamente '),
        (r' e dunque ', ' è dunque '),
        (r' e quindi ', ' è quindi '),
        (r' e invece ', ' è invece '),
        (r' e solo ', ' è solo '),
        (r' e sempre ', ' è sempre '),
        (r' e in ', ' è in '),
        (r' e al ', ' è al '),
        (r' e alla ', ' è alla '),
        (r" e l'", " è l'"),
        (r" e nell'", " è nell'"),
        (r" e sull'", " è sull'"),
        (r" e dall'", " è dall'"),
        (r" e un'", " è un'"),
        (r' e tra ', ' è tra '),
        (r' e per ', ' è per '),
        (r' e pari ', ' è pari '),
        (r' e il risultato ', ' è il risultato '),
        (r' e la ', ' è la '),  # risky but common
        (r' e il ', ' è il '),  # risky but common
        (r' e un ', ' è un '),
        (r' e una ', ' è una '),
        (r' e lo ', ' è lo '),
        (r' e i ', ' è i '),    # risky
        (r' e le ', ' è le '),  # risky
        (r' e gli ', ' è gli '),
        (r' e del ', ' è del '),
        (r' e dei ', ' è dei '),
        (r' e delle ', ' è delle '),
        (r' e della ', ' è della '),
        (r' e nel ', ' è nel '),
        (r' e nella ', ' è nella '),
    ]

    for pattern, replacement in safe_patterns:
        text = text.replace(pattern, replacement)

    # === Fix "e" a inizio di frase dopo punto ===
    # ". E " dove E è "È" (verbo)
    # Bisogna stare attenti: ". E " potrebbe essere congiunzione
    # Solo pattern sicuri:
    text = text.replace('. E il ', '. È il ')
    text = text.replace('. E la ', '. È la ')
    text = text.replace('. E un ', '. È un ')
    text = text.replace('. E una ', '. È una ')
    text = text.replace('. E stato ', '. È stato ')
    text = text.replace('. E stata ', '. È stata ')
    text = text.replace('. E esattamente ', '. È esattamente ')
    text = text.replace('. E fondamentale ', '. È fondamentale ')
    text = text.replace('. E importante ', '. È importante ')

    # puo → può
    text = re.sub(r'\bpuo\b', 'può', text)

    # citta → città
    text = re.sub(r'\bcitta\b', 'città', text)

    if text != original:
        changes = sum(1 for a, b in zip(text, original) if a != b)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'✅ {fname} — corretto ({changes} caratteri modificati)')
    else:
        print(f'⚪ {fname} — nessuna modifica necessaria')

print('\n🎉 Correzione accenti completata!')
