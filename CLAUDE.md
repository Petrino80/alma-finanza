# Alma Finanza — Regole di Progetto

## Portale
Alma Finanza è un portale di notizie finanziarie in italiano, pubblicato su GitHub Pages, destinato a italiani che vogliono capire la finanza in modo accessibile.

## Regola Linguistica
Ogni termine tecnico in inglese, quando necessario perché di uso comune nel settore finanziario, deve essere sempre accompagnato dalla migliore traduzione italiana tra parentesi.
Esempi: "Relief Rally (rally di sollievo)", "War Premium (premio di guerra)", "Triple Witching (tripla scadenza)", "Earnings Season (stagione delle trimestrali)".
Questa regola si applica a: articoli, titoli, card homepage, info-box, sezione "Impara la Finanza", categorie.

## Git
- Commit con: `git -c user.name="Ferrara Petrino" -c user.email="ferrarapetrino@Petrinos-MacBook-Pro.local" commit`
- Google Analytics: G-E88FFDTPMP

## Stack Tecnico
- HTML statico + Tailwind CSS (CDN) con `darkMode:'class'`
- Anti-flash dark mode script nel `<head>`
- Font: Lobster (logo), Montserrat (titoli), Inter (corpo)
- Theme toggle con animazione spring: `cubic-bezier(0.68,-0.55,0.27,1.55)`
- SEO: Open Graph, Twitter Card, Schema.org NewsArticle, canonical URL, sitemap.xml con news:news

## Struttura Articoli
- Banner colorato per categoria: blu (Wall Street), emerald (Piazza Affari), rosso (Macro/Geopolitica), amber (Commodities/Crypto), viola (Tech/AI), sky (Corporate)
- Minimo 5 sezioni di contenuto, 2 tabelle dati, 2 info-box educativi
- Disclaimer e nota metodologica nel footer

## Glossario Finanziario (glossario.html)
- Ogni termine tecnico inglese usato negli articoli deve essere presente nel glossario
- Ad ogni aggiornamento quotidiano, i nuovi termini vengono aggiunti automaticamente al glossario
- Formato: termine inglese, traduzione italiana, spiegazione educativa, link all'articolo di riferimento
- Organizzato in ordine alfabetico con ricerca live e navigazione per lettera

## Aggiornamenti Giornalieri (Master Prompt)
- Script Python per aggiornamenti batch (ticker, stats, hero, card, sitemap, categorie, impara la finanza, glossario)
- 5 articoli per aggiornamento, generati in parallelo con agenti background
- Verificare sempre che l'hero sia stato aggiornato correttamente dopo l'esecuzione dello script
- Verificare che i nuovi termini finanziari siano stati aggiunti al glossario

## Homepage e Archivio (disposizione del novembre 2026)
- Homepage: Ticker Live, "In primo piano" con gli articoli di oggi, "Ultime notizie" con filtri, ultime 10 giornate; il resto nelle pagine `archivio-AAAA-MM.html`
- Le impagina `impagina-home.py`: si incolla il blocco `<!-- GIORNO AAAA-MM-GG | ... -->` sotto `<!-- NUOVO-GIORNO -->` in index.html e si esegue `python3 impagina-home.py --applica`
- Mai modificare a mano primo piano, sezioni giorno, blocco archivio e pagine archivio: sono generati
- Mai classi col-span scritte a mano sulle schede: la larghezza la decide il numero di articoli del giorno
- Data di un articolo = giorno a cui sono aggiornati i dati usati (non il giorno in cui si scrive), identica su riquadro, articolo, nome file, categorie e sitemap; salvo data diversa chiesta espressamente dall'utente
- Il giorno della settimana si ricava sempre dalla data, mai a memoria
- Telefono: nessuno scorrimento orizzontale (verificare a 390 e 360px), riga dati entro ~34 caratteri, tabelle degli articoli compatte senza display:block, foto di testa con -mx-4; regole complete nel Master Prompt (blocco TELEFONO)
- Con più di 3 articoli nel giorno, i primi 3 vanno in primo piano e gli altri nella sezione "Oggi" sotto "Ultime notizie"
- Stile dei riquadri (dall'11 novembre 2026): la foto sfuma nel fondo scuro, generato dal CSS di `impagina-home.py`; il markup `.n-card` non cambia
- `impagina-home-stile-precedente.py` e `index-stile-precedente.html` sono copie di riserva ferme dello stile chiaro: non usarle negli aggiornamenti e non aggiornarle
