#!/usr/bin/env python3
"""
Aggiunge traduzioni italiane tra parentesi ai termini tecnici inglesi
negli articoli del 23 marzo 2026.
"""
import re

# === ARTICOLO 1: WALL STREET ===
f1 = 'articolo-wall-street-23mar-rally-trump-iran-pausa.html'
with open(f1, 'r') as f:
    c = f.read()

# small cap (solo nel testo visibile, non nei meta)
c = c.replace('le small cap — piu esposte al ciclo domestico', 'le small cap (piccola capitalizzazione) — piu esposte al ciclo domestico')
c = c.replace('Le small cap e i settori ciclici', 'Le small cap (piccola capitalizzazione) e i settori ciclici')

# futures (nel testo, non nei meta/schema)
c = c.replace('i futures azionari sono schizzati', 'i futures (contratti a termine) azionari sono schizzati')

# risk-on (seconda e terza occorrenza senza traduzione)
c = c.replace('risk-on (propensione al rischio) generalizzato.</p>', 'risk-on (propensione al rischio) generalizzato.</p>')  # already ok
c = c.replace('<strong>risk-on generalizzato</strong>', '<strong>risk-on (propensione al rischio) generalizzato</strong>')

# Consumer Discretionary
c = c.replace('Consumer Discretionary</strong> ha guidato', 'Consumer Discretionary (beni voluttuari)</strong> ha guidato')
c = c.replace('>Consumer Discretionary</td>', '>Consumer Discretionary (beni voluttuari)</td>')

# mega-cap
c = c.replace('mega-cap tecnologici', 'mega-cap (grandissima capitalizzazione) tecnologici')

# risk-off
c = c.replace('sentiment risk-off', 'sentiment risk-off (avversione al rischio)')

# war premium - gia ha "premio di rischio geopolitico" ma aggiungere traduzione dopo war premium
c = c.replace('(war premium) che rappresenta', '(war premium, premio di guerra) che rappresenta')

# front-month
c = c.replace('futures front-month', 'futures front-month (scadenza piu vicina)')

# consensus
c = c.replace('analisi di consensus degli analisti', 'analisi di consensus (consenso) degli analisti')

# earnings
c = c.replace('dati macro e earnings rende', 'dati macro e earnings (risultati trimestrali) rende')

with open(f1, 'w') as f:
    f.write(c)
print(f'✅ {f1} aggiornato')


# === ARTICOLO 2: FTSE MIB ===
f2 = 'articolo-ftse-mib-23mar-poste-tim-opas-rimbalzo.html'
with open(f2, 'r') as f:
    c = f.read()

# future (contratti a termine) - attenzione: "I future segnalavano"
c = c.replace('I future segnalavano', 'I future (contratti a termine) segnalavano')

# intraday
c = c.replace('violenza dell&rsquo;inversione intraday', 'violenza dell&rsquo;inversione intraday (intra-giornaliera)')
c = c.replace('massimo di giornata a', 'massimo intraday (intra-giornaliero) a', 1)

# M&A
c = c.replace('da manuale delle fusioni e acquisizioni', 'da manuale delle M&amp;A (fusioni e acquisizioni)')

# gap
c = c.replace('Questo gap &mdash;', 'Questo gap (divario) &mdash;')

# rating
c = c.replace('sotto osservazione il rating di Poste', 'sotto osservazione il rating (giudizio) di Poste')

# target
c = c.replace('<strong>TIM</strong>, il target dell', '<strong>TIM</strong>, il target (bersaglio) dell')

# trading
c = c.replace('esposte al trading e alla volatilit', 'esposte al trading (negoziazione) e alla volatilit')

# relief rally
c = c.replace('classico <strong>relief rally</strong>', 'classico <strong>relief rally (rally di sollievo)</strong>')
c = c.replace('il rimbalzo &egrave; un relief rally', 'il rimbalzo &egrave; un relief rally (rally di sollievo)')

# cash -> contanti
c = c.replace('combinazione di <strong>denaro contante e azioni proprie</strong>', 'combinazione di <strong>cash (contanti) e azioni proprie</strong>')

# delisting - gia spiegato come "ritiro dalla Borsa" inline, ma aggiungiamo tra parentesi la prima volta
c = c.replace('Per il <strong>delisting</strong> (ritiro dalla Borsa)', 'Per il <strong>delisting</strong> (ritiro dalla Borsa)')  # already ok

# squeeze-out
c = c.replace('allo squeeze-out delle azioni residue', 'allo squeeze-out (acquisizione forzata) delle azioni residue')

# trend
c = c.replace('un&rsquo;inversione di trend', 'un&rsquo;inversione di trend (tendenza)')

with open(f2, 'w') as f:
    f.write(c)
print(f'✅ {f2} aggiornato')


# === ARTICOLO 3: MERCATI OUTLOOK ===
f3 = 'articolo-mercati-23mar-outlook-trump-iran-scenari.html'
with open(f3, 'r') as f:
    c = f.read()

# safe haven
c = c.replace('fuga dal safe haven su riduzione rischio', 'fuga dal safe haven (bene rifugio) su riduzione rischio')

# risk-on (nel testo)
c = c.replace("risk-on: ritorno dell'appetito per il rischio", "risk-on (propensione al rischio): ritorno dell'appetito per il rischio")
c = c.replace('del sentiment risk-on/risk-off', 'del sentiment (umore) risk-on/risk-off (propensione/avversione al rischio)')

# Bullish
c = c.replace('A — Bullish: accordo', 'A — Bullish (rialzista): accordo')
c = c.replace('Scenario A — Bullish (25%', 'Scenario A — Bullish (rialzista, 25%')

# Base case
c = c.replace('B — Base case: deadline estesa', 'B — Base case (scenario base): deadline (scadenza) estesa')
c = c.replace('Scenario B — Base case (50%', 'Scenario B — Base case (scenario base, 50%')

# Bearish
c = c.replace('C — Bearish: colloqui falliscono', 'C — Bearish (ribassista): colloqui falliscono')
c = c.replace('Scenario C — Bearish (25%', 'Scenario C — Bearish (ribassista, 25%')

# sell-off
c = c.replace('>sell-off 3-5%</td>', '>sell-off (ondata di vendite) 3-5%</td>')
c = c.replace('subisce un sell-off del', 'subisce un sell-off (ondata di vendite) del')

# trading range
c = c.replace('un <strong>trading range</strong>', 'un <strong>trading range (fascia di oscillazione)</strong>')

# range-bound
c = c.replace('>range-bound, alta volatilita</td>', '>range-bound (in fascia laterale), alta volatilita</td>')

# framework
c = c.replace('un framework negoziale', 'un framework (accordo quadro) negoziale')
c = c.replace('un framework negoziale', 'un framework (accordo quadro) negoziale')  # second occurrence if any

# short squeeze - gia spiegato nel testo
c = c.replace('Lo short squeeze:</strong> chi aveva scommesso al ribasso deve comprare per chiudere le posizioni', 'Lo short squeeze (chiusura forzata delle posizioni ribassiste):</strong> chi aveva scommesso al ribasso deve comprare per chiudere le posizioni')

# front-month
c = c.replace('futures front-month quotati', 'futures front-month (scadenza piu vicina) quotati')

# PMI - aggiungere traduzione italiana
c = c.replace("PMI (Purchasing Managers' Index)", "PMI (Purchasing Managers' Index, indice dei direttori degli acquisti)")

# Earnings
c = c.replace('<strong>Earnings — GameStop', '<strong>Earnings (risultati trimestrali) — GameStop')

# disruption
c = c.replace('le disruption sulle catene', 'le disruption (interruzioni) sulle catene')

# rerouting
c = c.replace('dal rerouting delle navi', 'dal rerouting (deviazione) delle navi')

# deadline (la prima menzione principale)
c = c.replace('La deadline del 28 marzo viene estesa', 'La deadline (scadenza) del 28 marzo viene estesa')

# relief rally - gia tradotto come "rally del sollievo" nel titolo h2, bene

# low-cost
c = c.replace('diverse low-cost stanno cancellando', 'diverse low-cost (compagnie a basso costo) stanno cancellando')

with open(f3, 'w') as f:
    f.write(c)
print(f'✅ {f3} aggiornato')


# === ARTICOLO 4: PETROLIO ===
f4 = 'articolo-petrolio-23mar-crollo-trump-iran-pausa-diplomazia.html'
with open(f4, 'r') as f:
    c = f.read()

# intraday
c = c.replace('un massimo intraday di <strong>$113</strong>, è crollato', 'un massimo intraday (intra-giornaliero) di <strong>$113</strong>, è crollato')
c = c.replace('Il range intraday del WTI', 'Il range (fascia) intraday (intra-giornaliero) del WTI')
c = c.replace('in un range estremo tra', 'in un range (fascia) estremo tra')
c = c.replace('picco intraday di <strong>$113</strong>, spinto', 'picco intraday (intra-giornaliero) di <strong>$113</strong>, spinto')

# benchmark
c = c.replace('per entrambi i benchmark dall', 'per entrambi i benchmark (indici di riferimento) dall')

# stop-loss
c = c.replace('le stop-loss saltano a catena', 'le stop-loss (ordini di vendita automatici) saltano a catena')

# shale oil / shale
c = c.replace('Produttori shale USA', 'Produttori shale (scisto) USA')
c = c.replace('di shale oil americani', 'di shale oil (petrolio da scisto) americani')

# breakeven
c = c.replace('il breakeven medio', 'il breakeven (punto di pareggio) medio')
c = c.replace('>Breakeven a $65-75', '>Breakeven (punto di pareggio) a $65-75')

# spare capacity - gia spiegato inline
c = c.replace('spare capacity) è ridotta', 'spare capacity, capacità produttiva di riserva) è ridotta')

# trading algoritmico
c = c.replace('<strong>Trading algoritmico', '<strong>Trading (negoziazione) algoritmico')

# contango e backwardation
c = c.replace('<strong>Contango vs Backwardation:</strong>', '<strong>Contango (mercato in riporto) vs Backwardation (mercato in deporto):</strong>')
c = c.replace('da backwardation a contango', 'da backwardation (deporto) a contango (riporto)')

# spot
c = c.replace('il prezzo spot supera', 'il prezzo spot (corrente) supera')

# futures (solo nel testo educativo)
c = c.replace('contratti futures a scadenza', 'contratti futures (a termine) a scadenza')
c = c.replace('dei futures petroliferi', 'dei futures (contratti a termine) petroliferi')

# jet fuel
c = c.replace('dal calo jet fuel', 'dal calo del jet fuel (carburante aeronautico)')

# outlook
c = c.replace('outlook migliorato', 'outlook (prospettive) migliorato')

# low-cost
c = c.replace('le compagnie low-cost come', 'le compagnie low-cost (a basso costo) come')

with open(f4, 'w') as f:
    f.write(c)
print(f'✅ {f4} aggiornato')


# === ARTICOLO 5: ASIA ===
f5 = 'articolo-asia-23mar-crollo-kospi-nikkei-hang-seng-hormuz.html'
with open(f5, 'r') as f:
    c = f.read()

# gap di apertura
c = c.replace('<strong>gap di apertura</strong>', '<strong>gap (divario) di apertura</strong>')
c = c.replace('gap rialzista all', 'gap (divario) rialzista all')

# gap rialzista/ribassista nell'info-box
c = c.replace('si apre con un gap rialzista', 'si apre con un gap (divario) rialzista')
c = c.replace('con un gap ribassista', 'con un gap (divario) ribassista')

# shale oil
c = c.replace('della rivoluzione dello shale oil', 'della rivoluzione dello shale oil (petrolio da scisto)')

# supply chain -> catene di approvvigionamento (gia in italiano, ok)

# safe haven - non presente

# small cap - non presente

# risk - gia in italiano "rischio"

with open(f5, 'w') as f:
    f.write(c)
print(f'✅ {f5} aggiornato')

print('\n🎉 Tutti e 5 gli articoli aggiornati con traduzioni italiane!')
