# MASTER PROMPT — Aggiornamento Quotidiano Alma Finanza

**Copia e incolla questo prompt ogni giorno per aggiornare il sito.**

---

## ✅ OPERAZIONI PRE-AUTORIZZATE — NON CHIEDERE MAI CONFERMA PER QUESTE:

Tutte le operazioni qui sotto sono approvate in anticipo per ogni aggiornamento quotidiano.
Claude NON deve chiedere conferma, approvazione o permesso per nessuna di queste azioni.

**Ricerca dati e foto:**
- WebSearch per dati di mercato, notizie, chiusure borse
- WebSearch per cercare foto su Unsplash, Pexels, Wikimedia Commons
- Scaricare foto da Unsplash, Pexels o Wikimedia Commons (licenza libera verificata)
- Navigare pagine web per verificare dati o trovare foto

**Creazione e modifica file:**
- Creare nuovi file articolo HTML (articolo-*.html)
- Modificare index.html (homepage)
- Creare e modificare le pagine archivio (archivio.html, archivio-AAAA-MM.html)
- Modificare sitemap.xml
- Modificare categoria-wall-street.html, categoria-borsa-milano.html, categoria-crypto.html, categoria-commodities.html
- Modificare impara-finanza.html
- Modificare glossario.html
- Modificare img/repertorio/crediti.json (registro crediti fotografici)
- Salvare nuove foto in img/repertorio/ (dopo verifica licenza)

**Script Python:**
- Eseguire applica-foto-articolo.py (applica foto + firma + tempo lettura agli articoli)
- Eseguire applica-foto-articolo.py --elenco (mostra foto disponibili)
- Eseguire converti-home.py e converti-home.py --applica (aggiorna schede homepage)
- Eseguire impagina-home.py e impagina-home.py --applica (impagina homepage e archivi)
- Qualsiasi script Python di utilità già presente nel progetto

**Ridimensionamento immagini:**
- Ridimensionare foto a 1600px con PIL/Pillow (qualità 84, progressiva)

**Git:**
- git add per i file dell'aggiornamento quotidiano
- git commit con messaggio descrittivo
- git push origin main

---

## IL PROMPT DA USARE:

```
Aggiornamento quotidiano Alma Finanza — [DATA 15 giugno 2026 - aggiornamento borse/news real time]

FASE 1 — RICERCA DATI REALI (OBBLIGATORIA — NON SALTARE MAI):
⛔ PRIMA di scrivere qualsiasi articolo, esegui WebSearch per TUTTI i dati. Non esiste eccezione.

Dati da cercare:
- Indici USA: Dow Jones, S&P 500, Nasdaq (valori indice, NON prezzi ETF)
- Indici Europa: FTSE MIB, DAX, CAC 40
- Commodities: Oro, Petrolio WTI
- Bitcoin
- Titoli protagonisti della giornata (top gainers/losers)
- Notizie macro principali (Fed, dazi, earnings, geopolitica)

📅 DATA DI RIFERIMENTO — UNA SOLA DATA PER ARTICOLO, UGUALE OVUNQUE:
La data di un articolo è il GIORNO A CUI SONO AGGIORNATI I DATI E LE INFORMAZIONI USATI,
non il giorno in cui l'articolo viene scritto o pubblicato.
- Articolo su una seduta di borsa → la data è il giorno di QUELLA seduta.
  Esempio: l'aggiornamento parte all'una di notte di mercoledì 11 novembre con le chiusure
  di martedì 10 → la data è MARTEDÌ 10 NOVEMBRE, in tutti i punti elencati sotto.
- Articolo che usa anche notizie successive alla chiusura (weekend, analisi) → la data è il
  giorno dell'ULTIMA informazione usata.
- La data si stabilisce QUI, in FASE 1, leggendola dalle fonti ("chiusura di lunedì 9"),
  mai dall'orologio. Va scritta prima di cominciare gli articoli e non si cambia più.
- Il giorno della settimana si ricava da quella data con un calendario, mai a memoria.
- ECCEZIONE: se l'utente indica espressamente un'altra data nella richiesta ("con data
  12 novembre"), vale la data chiesta dall'utente. In assenza di indicazioni vale la regola.

⛔ LA STESSA DATA deve comparire, identica, in TUTTI questi punti:
   1. nome del file (articolo-...-10nov-....html)
   2. banner dell'articolo: occhiello e riga "Redazione Alma Finanza · <data>"
   3. data nella testata dell'articolo (con il giorno della settimana giusto)
   4. meta article:published_time e datePublished nello Schema.org (stesso giorno)
   5. firma: il --data di applica-foto-articolo.py (stesso giorno)
   6. riga .n-meta del riquadro in homepage ("10 novembre · ...")
   7. blocco <!-- GIORNO AAAA-MM-GG | ... --> in index.html
   8. sezione del giorno nelle pagine categoria
   9. publication_date e lastmod nella sitemap
   Se anche uno solo è diverso, il lettore vede una data sul riquadro e un'altra dentro
   l'articolo: è un errore da correggere PRIMA del commit.

⚠️ REGOLA ASSOLUTA — NON INVENTARE MAI NESSUN DATO:
- Se non trovi un dato con WebSearch → scrivilo come "—" nell'articolo
- MAI usare dati da training/memoria come fonte — sono inaffidabili
- I dati di training possono essere obsoleti, pre-split, riferiti a periodi sbagliati

⚠️ REGOLA SPECIALE PER EARNINGS (risultati trimestrali aziendali):
Gli EPS (utili per azione), i ricavi (revenue) e le guidance sono dati PUBBLICATI e verificabili.
Se un articolo riguarda risultati trimestrali di una specifica azienda (es. Nvidia, Apple, LVMH):
1. Cerca OBBLIGATORIAMENTE con WebSearch: "[azienda] earnings Q[X] [anno] EPS results"
2. Verifica EPS effettivo, EPS atteso dal consensus, revenue effettiva, revenue attesa
3. Se i risultati non sono ancora pubblici → non scrivere l'articolo con numeri inventati, aspetta o scegli un altro tema
4. MAI fornire agli agenti background dati earnings inventati — gli agenti li pubblicheranno senza verificare
❌ ERRORE COMMESSO IL 20/05/2026: EPS Nvidia inventato come $9,82 (sbagliato) invece di $1,87 (reale).
   Causa: dati di training confusi con prezzi pre-split 2024 + FASE 1 saltata completamente.

FASE 2 — SCRIVI 3 ARTICOLI:
Crea 3 articoli HTML seguendo queste regole INVIOLABILI:

Distribuzione consigliata (adattabile alle notizie del giorno):
1. Wall Street / mercati USA (obbligatorio)
2. Piazza Affari / FTSE MIB (obbligatorio)
3. Uno su azienda piu' interessante delle sedute 


Formato articoli — REGOLE FISSE, MAI CAMBIARE:
- File: articolo-[topic]-[DDmese]-[dettaglio].html (es: articolo-wall-street-26feb-nvidia-rally.html)
  [DDmese] è la DATA DI RIFERIMENTO stabilita in FASE 1 (il giorno dei dati), non il giorno in cui si scrive
- Google Analytics: G-E88FFDTPMP in ogni file
- Anti-flash dark mode script subito dopo GA: <script>(function(){var t=localStorage.getItem('alma-theme');if(t==='dark'||(!t&&window.matchMedia('(prefers-color-scheme:dark)').matches))document.documentElement.classList.add('dark')})()</script>
- Tailwind CSS con darkMode:'class': <script>tailwind.config={darkMode:"class"}</script>
- Header/Logo: Lobster "A" teal-500 + Montserrat "LMA FINANZA" con dark:text-white
- Theme toggle button (☀️/🌙) nell'header con localStorage persistence
- Banner colorato con categoria, titolo h1, data, "Redazione Alma Finanza"
- Lead paragraph con i dati chiave
- Contenuto con h2 per sezioni, dati in grassetto, tabelle .data-table per indici/titoli
- Classi .positive (verde) e .negative (rosso) per variazioni, con dark mode overrides
- MINIMO 2 info-box educativi per articolo: <div class="info-box"><h3>💡 Impara: [Concetto]</h3><p>...</p></div>
- Ogni variazione % DEVE specificare l'intervallo temporale (giorno, settimana, mese, YTD)
- Footer STANDARD (MAI cambiare): "Alma Finanza" in Lobster teal-400, copyright 2026, disclaimer, con dark mode classes
- Dark mode CSS completo: .dark body, .dark .article-content h2, .dark .lead, .dark .info-box, .dark .data-table th, .dark .positive, .dark .negative, .dark strong
- Tono informativo, MAI dare consigli finanziari, spiegare i concetti
- Toggle JS prima di </body> con toggleTheme(), updateIcons(), localStorage e system preference listener
- SEO obbligatorio in ogni articolo (inserire prima di </head>):
  • Open Graph: og:type, og:title, og:description, og:url, og:site_name, og:locale, article:published_time, article:author, article:section
  • Twitter Card: twitter:card, twitter:title, twitter:description
  • Canonical: <link rel="canonical" href="https://www.almafinanza.com/[nome-file].html">
  • Schema.org JSON-LD: @type NewsArticle con headline, description, url, datePublished, author, publisher, inLanguage

FASE 2B — FOTO, FIRMA E TEMPO DI LETTURA (per OGNI articolo, obbligatorio):

Ogni articolo deve aprirsi con una FOTOGRAFIA, la firma di testata e il tempo di lettura.

⚠️ SUL SITO SI USANO FOTO VERE, non immagini generate. Le foto stanno nella libreria
di repertorio img/repertorio/, sono tutte a licenza libera verificata su Wikimedia Commons,
e il credito fotografico si stampa da solo sotto l'immagine (obbligatorio per le licenze CC).

   # vedi le foto disponibili e i loro temi
   python3 applica-foto-articolo.py --elenco

   # applica la foto e scrivi la firma
   python3 applica-foto-articolo.py <articolo>.html --foto piazza-affari --data 2026-09-02T17:50

   Corrispondenze tipiche:
     piazza-affari   → articoli su FTSE MIB / Borsa di Milano
     nyse            → articoli su Wall Street / S&P 500 / Dow / Nasdaq
     fed             → articoli su tassi, Fed, inflazione, banche centrali
     petrolio        → petrolio, Brent, WTI, energia, Stretto di Hormuz, geopolitica
     semiconduttori  → chip, tech, AI, Nvidia, STM

   Senza --foto lo script prova a dedurre il tema dal titolo. Se nessuna foto è pertinente,
   NON forzarne una a caso: cerca una foto dedicata su una delle fonti autorizzate sotto,
   scaricala in img/repertorio/ e AGGIUNGI LA VOCE in img/repertorio/crediti.json con
   tutti i campi. Senza credito la foto non si pubblica.

   FONTI AUTORIZZATE PER FOTO NUOVE (in ordine di preferenza per qualità):
   1. Unsplash (unsplash.com) — licenza Unsplash, uso commerciale e editoriale OK, attribuzione
      facoltativa ma raccomandata. Cerca in inglese (es. "NYSE trading floor", "oil refinery",
      "Wall Street trader"). Scarica la versione "Full" o almeno 1600 px di larghezza.
      In crediti.json: licenza "Unsplash License", fonte = URL della foto su unsplash.com.
   2. Pexels (pexels.com) — licenza Pexels (CC0 equivalente), nessun obbligo di attribuzione.
      Ottima per business, finanza, economia. In crediti.json: licenza "Pexels License".
   3. Wikimedia Commons (commons.wikimedia.org) — preferire foto CC BY o CC BY-SA ≥ 4.0;
      verificare sempre licenza e autore aprendo la pagina del file.

⛔ REGOLA ASSOLUTA — MAI LA STESSA FOTO SU DUE ARTICOLI:
   Ogni fotografia si usa UNA VOLTA SOLA, su un solo articolo. Due articoli con la stessa
   immagine — soprattutto in giornate vicine che trattano gli stessi temi — fanno sembrare
   la homepage un blocco duplicato.

   Lo script lo verifica da solo e si RIFIUTA di procedere se la foto è già impegnata,
   suggerendo le alternative libere sullo stesso tema. Quando non ce ne sono:
   1. cerca una foto nuova su Unsplash o Pexels (preferiti) oppure Wikimedia Commons
      — deve essere ORIZZONTALE (larghezza > altezza) e ad alta risoluzione
   2. verifica autore e licenza
   3. scaricala in img/repertorio/ con un nome parlante (es. wall-street-trader.jpg, oil-refinery.jpg)
   4. registrala in crediti.json con soggetto, autore, licenza, fonte e temi
   Non usare MAI --forza per aggirare il controllo negli aggiornamenti quotidiani.

⛔ REGOLA FREQUENZA SOGGETTO — MAX 1 VOLTA OGNI 25 GIORNI PER SOGGETTO GENERICO:
   Alcuni soggetti fotografici rappresentano categorie intere (NYSE per Wall Street,
   Palazzo Mezzanotte / Piazza Affari per la Borsa di Milano, la Fed di Washington per
   le banche centrali). Usarli ogni giorno satura la homepage e la fa sembrare un archivio.

   SOGGETTI CON LIMITE 1/25gg (verificare la data dell'ultimo utilizzo prima di usarli):
   - piazza-affari.jpg / palazzo-mezzanotte → Borsa di Milano generica
   - nyse.jpg / nyse-2.jpg → Wall Street / NYSE generica
   - fed.jpg / fed-washington.jpg → sede della Federal Reserve

   Se meno di 25 giorni separano l'aggiornamento odierno dall'ultimo uso di quel soggetto:
   ✓ Usa invece la foto dell'azienda o del titolo protagonista dell'articolo (Stellantis,
     Moncler, Nvidia, ecc.) — è sempre più specifica e più interessante.
   ✓ Oppure scarica una foto alternativa da Unsplash, Pexels o Wikimedia Commons
     (un'altra piazza finanziaria, un trader, un grafico di borsa, la sede della banca).

   Per articoli su un'azienda o una persona specifica (Stellantis, Nvidia, un amministratore
   delegato) vale la pena cercare la foto dedicata: è molto più pertinente del repertorio.

   VIETATO ANCHE LO STESSO SOGGETTO RIPETUTO. Non basta che il file sia diverso: due schede
   vicine non devono mostrare la stessa cosa da un'altra angolazione (niente «Wall Street da
   cinquanta inquadrature»). Se l'articolo cita un titolo, un'azienda o un luogo, la foto di
   QUELLO è sempre preferibile a una veduta generica di borsa. Esempi già in libreria:
   Micron/AMD → wafer di silicio; Moderna → sede di Cambridge; Ifo tedesco → skyline di
   Francoforte; rendimenti Treasury → Tesoro americano; Banca Generali → palazzo Generali;
   Hormuz → portacontainer; retail USA → Walmart o Home Depot; Prysmian → rete elettrica;
   guidance AI → centro dati.

⛔ PESO DELLE IMMAGINI — SEMPRE 1600 px DI LARGHEZZA MASSIMA:
   Le foto di Wikimedia arrivano anche a 12 MB l'una: così la homepage diventa illeggibile
   su rete mobile. Ogni foto va salvata ridimensionata a 1600 px sul lato lungo, JPEG
   qualità 84, progressiva. Circa 100-500 KB a foto.

     python3 -c "
     from PIL import Image
     im = Image.open('img/repertorio/<foto>.jpg').convert('RGB')
     if im.width > 1600: im = im.resize((1600, round(im.height*1600/im.width)), Image.LANCZOS)
     im.save('img/repertorio/<foto>.jpg', 'JPEG', quality=84, optimize=True, progressive=True)"

   Scarica preferibilmente la miniatura già ridotta dall'API di Commons (iiurlwidth=1600)
   invece del file originale.

⚠️  ATTENZIONE ai fotogrammi verticali: la scheda taglia in orizzontale, quindi un ritratto
   o una foto in verticale viene sfigurata. Controlla sempre larghezza > altezza prima di
   scaricare.

L'IMMAGINE GENERATA DAI DATI resta utile per i SOCIAL (LinkedIn), dove il testo
sull'immagine funziona meglio. Si crea così, e NON va inserita nell'articolo:

   python3 genera-immagine-articolo.py \
     --slug <nome-file-articolo-senza-estensione> \
     --categoria "Wall Street" --colore blue \
     --occhiello "Chiusura del 2 settembre 2026" \
     --titolo "Titolo breve, 40-110 caratteri" \
     --numero "7.686" --numero-label "S&P 500" --numero-var "−0,30%" --numero-dir down \
     --dato "Dow|−0,70%|down" --dato "Nasdaq|−0,12%|down" --dato "Energia|in rally|up"

   • --colore deve corrispondere al banner della categoria:
     blue = Wall Street · emerald = Piazza Affari · red = Macro/Geopolitica
     amber = Commodities/Energia · purple = Tech/AI · sky = Corporate
   • --numero-dir: up (verde) / down (rosso) / flat
   • --slug DEVE coincidere esattamente col nome del file HTML, altrimenti l'immagine non si collega
   • Usa SOLO dati verificati in FASE 1

La firma e il tempo di lettura li scrive applica-foto-articolo.py insieme alla foto:
la riga "A Alma Finanza · <data> · Lettura N min", con i minuti calcolati sul testo reale
(200 parole al minuto) e la data che diventa relativa ("3 ore fa") per le prime 24 ore.

   --data: il GIORNO è sempre la DATA DI RIFERIMENTO stabilita in FASE 1 (il giorno dei dati),
   anche se l'articolo viene scritto dopo mezzanotte o il giorno seguente. L'ORA è quella
   della chiusura raccontata: dopo le 22:00 italiane per la chiusura USA, dopo le 17:30 per
   Piazza Affari.

⚠️ La firma è sempre di testata ("Alma Finanza"), mai di un autore singolo.

FASE 2C — "PERCHÉ CONTA" (obbligatorio in ogni articolo e in ogni card):

Ogni articolo e ogni scheda in homepage deve dire al lettore non specialista perché la
notizia lo riguarda. Due righe, subito dopo il titolo, nella forma:

    <strong class="text-gray-700 dark:text-slate-300 font-semibold">Perché conta:</strong> spiegazione...

Regole di scrittura:
- Deve collegare il fatto a una conseguenza concreta, non ripetere il dato.
  ✗ "Il Brent sale del 4,50% oltre i 92 dollari" (è già nel titolo)
  ✓ "Da Hormuz passa circa un quinto del petrolio mondiale. Se il greggio resta sopra
     i 90 dollari l'inflazione torna a salire, e la Fed ha un motivo in più per non
     tagliare i tassi."
- Massimo due frasi, in italiano piano, senza gergo.
- Va SOSTITUITO al vecchio sommario denso fatto di dati separati da "·".
  I numeri di dettaglio si spostano nella riga in fondo alla card, insieme alla data
  e al tempo di lettura ("Brent +4,50% · WTI ~$87,30 · 1 Set" / "Leggi · 6 min →").

Nelle card della homepage, sopra il testo va la stessa foto dell'articolo:

    <img src="img/repertorio/<foto>.jpg" alt="<soggetto della foto>" width="1200" height="630"
         loading="lazy" class="w-full block object-cover" style="aspect-ratio:1200/630">

FASE 3 — AGGIORNA HOMEPAGE (index.html):
⚠️ NON CAMBIARE MAI LA DISPOSIZIONE DELLA HOMEPAGE descritta qui sotto. Solo aggiornare i contenuti.
Design: Modern Minimal con switch light/dark.

📐 DISPOSIZIONE APPROVATA IL 10 NOVEMBRE 2026 (sostituisce la griglia uniforme del 3 settembre).
   Decide dove stanno gli elementi nella pagina.

🎨 STILE DEI RIQUADRI (dall'11 novembre 2026): la foto sfuma nel fondo scuro.
   Riquadro scuro, foto nella parte alta che sfuma nel nero, categoria in pillola colorata,
   titolo e "Perché conta" in chiaro, dati in pillole (verdi se salgono, rosse se scendono).
   Nel primo piano il titolo sta sopra la foto. Spigoli da 6px. Logo e font NON si toccano.
   ⛔ Lo stile sta tutto nel CSS generato da impagina-home.py: il MARKUP delle schede resta
      quello di sempre (vedi sotto). Non scrivere colori, altezze o stili a mano sulle schede.
   ⛔ Lo stile precedente (riquadri chiari) è conservato in due copie di riserva FERME, che non
      si usano e non si aggiornano negli aggiornamenti quotidiani:
        - impagina-home-stile-precedente.py  (con --applica ripristina lo stile chiaro)
        - index-stile-precedente.html        (fotografia della homepage dell'11 novembre, noindex)

⚙️ COME SI AGGIORNA LA HOMEPAGE (convertita alla nuova disposizione il 10 novembre 2026):
   La homepage e le pagine archivio le impagina lo script impagina-home.py. A mano si fa UNA cosa:

   1. In index.html, subito sotto il commento <!-- NUOVO-GIORNO -->, incolla il blocco del giorno,
      con una scheda .n-card per articolo (la più importante PER PRIMA):

         <!-- GIORNO 2026-11-11 | Mercoledì 11 Novembre 2026 -->
         <a href="articolo-....html" class="n-card group"> ... </a>
         <a href="articolo-....html" class="n-card group"> ... </a>
         <a href="articolo-....html" class="n-card group"> ... </a>
         <!-- /GIORNO -->

   2. Esegui lo script:

         python3 impagina-home.py              # scrive index-nuovo.html, per controllare
         python3 impagina-home.py --applica --parola "Termine|traduzione italiana"

   Lo script fa tutto il resto: porta in primo piano la giornata più recente, fa scendere la
   precedente in Ultime notizie, sposta in archivio la giornata oltre la decima, rigenera le
   pagine archivio e il loro indice, ricalcola il conteggio degli articoli, aggiorna la data
   in testata, assegna data-cat alle schede, toglie i doppioni e aggiorna la sitemap.
   Il GIORNO DELLA SETTIMANA lo ricava dalla data (AAAA-MM-GG): se nel commento è sbagliato
   lo corregge da solo. La DATA invece deve essere giusta: controllala.

   ⛔ NON modificare a mano primo piano, sezioni giorno, blocco archivio e pagine archivio-*.html:
      sono generati e alla prossima esecuzione verrebbero riscritti. Per correggere una scheda
      già pubblicata si modifica la scheda dentro il suo blocco GIORNO e si riesegue lo script.
   ⛔ Dopo --applica lo script stampa quante schede ha verificato: il numero deve essere quello
      di prima più gli articoli di oggi. Se si ferma con un errore, non fare commit.
   ⛔ Lo script controlla anche le DATE delle giornate in homepage: per gli articoli di oggi non
      deve comparire nessuna riga "DATE DIVERSE". Se compare, correggi il punto sbagliato
      (riquadro, blocco GIORNO o articolo) e riesegui. Se la riga riguarda articoli di giornate
      PRECEDENTI, non correggerla di tua iniziativa: segnalala all'utente.

STRUTTURA FISSA DELLA HOMEPAGE (dall'alto in basso, MAI modificare l'ordine):
1. Ticker Live (widget TradingView) — è l'UNICA barra dei mercati
2. Header: Logo "ALMA FINANZA" + Data + Cerca + Toggle ☀️/🌙 (invariato)
3. Navigation Bar con due gruppi (invariata):
   - Sezioni: Dashboard Live | Wall Street | Borsa Milano | Crypto | Commodities
   - Risorse: Impara la Finanza | Glossario | Analisi Tecnica
4. IN PRIMO PIANO — gli articoli del giorno più recente: uno grande e due a fianco
5. ULTIME NOTIZIE — titolo + filtri per categoria
6. Sezioni giorno — una per ogni giornata precedente, fino a 10 giornate in tutto
7. Fascia Quiz + Parola del giorno — subito dopo la PRIMA sezione giorno
8. Blocco Archivio — titolo, conteggio articoli, pillole dei mesi e pulsante "Mostra i giorni precedenti"
9. Mission Section ("Perché Alma Finanza")
10. Disclaimer Legale
11. Newsletter CTA + EmailJS
12. Footer 4 colonne (Logo+desc | Sezioni | Risorse | Legal) + disclaimer esteso

⛔ LA STATS BAR STATICA NON ESISTE PIÙ nella nuova disposizione (i 6 riquadri di chiusura
   sotto la navigazione): ripeteva gli indici del ticker e restava con caselle "—" quando un
   dato mancava. I mercati li mostra solo il Ticker Live. Il banner grande del Quiz in cima
   alla pagina non esiste più: il Quiz è la fascia sottile al punto 7.

a) TICKER LIVE (barra scorrevole in alto):
   - È un widget TradingView: i dati sono in tempo reale e NON si aggiornano a mano
   - Non sostituirlo con valori statici e non aggiungere una seconda barra di mercato
   - Si tocca solo se l'utente chiede di cambiare l'elenco dei simboli

b) DATA nell'header:
   - Formato: "Mercoledì 26 Febbraio 2026"
   - Giorno della settimana CORRETTO in italiano

c) IN PRIMO PIANO (subito sotto la navigazione):
   - Contiene gli articoli della giornata di OGGI, al massimo 3: la notizia principale in
     grande a sinistra (circa tre quinti della larghezza) e due riquadri impilati a fianco
   - Sopra, l'occhiello: "In primo piano · <giorno> <data>"
   - La principale è la notizia più importante del giorno (di norma Wall Street o macro):
     è la PRIMA nell'ordine. Mostra foto, categoria, titolo, "Perché conta" e riga dei dati.
     I due riquadri a fianco mostrano foto, categoria, titolo e riga dei dati
   - Se oggi c'è 1 solo articolo: la principale occupa tutta la larghezza
     Se oggi ce ne sono 2: principale + un solo riquadro a fianco, alto quanto la principale
     Se oggi ce ne sono 4 o più: i primi 3 in primo piano, gli altri in una sezione giorno
     "Oggi · <giorno> <data>" in cima a Ultime notizie, con la regola f). La sezione "Oggi" sta
     SOTTO il titolo "Ultime notizie", MAI dentro o subito sotto il primo piano: lo fa da solo
     impagina-home.py, che mette la fascia Quiz + Parola del giorno subito dopo di essa
   - Quando arriva una giornata nuova, gli articoli che erano in primo piano SCENDONO nella
     prima sezione giorno di Ultime notizie (non si cancellano, non si riscrivono)
   - Le schede sono sempre .n-card: stesso design, cambia solo la misura

d) ULTIME NOTIZIE e filtri per categoria:
   - Titolo "Ultime notizie" e, sulla stessa riga, i pulsanti filtro:
     Tutte | Wall Street | Piazza Affari | Macro | Tech / AI | Commodities | Aziende
     Compaiono solo i filtri che hanno almeno un articolo nelle giornate in homepage:
     un filtro non deve mai lasciare la pagina vuota
   - Ogni scheda porta l'attributo data-cat con UNO di questi valori:
     wall (Wall Street) · milano (Piazza Affari) · macro (Macro, Fed, Geopolitica)
     tech (Tech / AI) · commod (Commodities, Crypto) · corp (Corporate)
   - Il filtro mostra o nasconde le schede; una sezione giorno rimasta senza schede visibili
     si nasconde tutta; il conteggio "N articoli" del giorno si aggiorna
   - Dopo ogni filtro le righe si ricalcolano con la regola f) sulle sole schede visibili:
     nemmeno a filtro attivo devono restare spazi vuoti

e) SEZIONI GIORNO e schede articolo:
   - Una sezione per ogni giornata, dalla più recente alla più vecchia. Ogni sezione ha la
     sua intestazione e il SUO contenitore griglia, che contiene SOLO le schede di quel giorno
   - Intestazione del giorno (stile separatore, uguale per tutte le giornate):
     ```html
     <div class="col-span-full flex items-center gap-3 mt-6 mb-2">
         <div class="w-10 h-0.5 rounded-full bg-gray-200 dark:bg-slate-700/40"></div>
         <h2 class="text-sm font-bold montserrat-font text-gray-400 dark:text-slate-600 uppercase tracking-wider">[GIORNO E DATA]</h2>
         <div class="flex-1 h-0.5 rounded-full bg-gray-100 dark:bg-slate-800/20"></div>
     </div>
     ```
     ⚠️ UNA sola intestazione per giornata: mai due titoli con la stessa data uno sotto l'altro

Markup di ogni scheda (classe .n-card, design invariato):

   <a href="<articolo>.html" class="n-card group" data-cat="milano">
       <img class="n-thumb" src="img/repertorio/<foto>.jpg" alt="<soggetto della foto>"
            loading="lazy" width="1200" height="800">
       <div class="n-body">
           <div class="n-cat">Piazza Affari</div>
           <h3>Titolo della notizia</h3>
           <p class="n-why"><b>Perché conta:</b> due righe che spiegano al lettore
              perché la notizia lo riguarda</p>
           <div class="n-meta"><span>1 settembre</span></div>
       </div>
   </a>

Regole:
   - La categoria in .n-cat va SENZA emoji (l'etichetta è già in maiuscoletto)
   - Titolo e "Perché conta" sono tagliati automaticamente a tre righe: scrivili brevi.
     Per la scheda il titolo deve stare entro 85 caratteri circa: oltre viene troncato con
     i puntini. Se il titolo dell'articolo è più lungo, nella scheda usane una versione breve
   - In .n-meta va UNA riga di testo: prima la data, poi i dati chiave, separati da " · "
     es. "11 novembre · S&P −0,4% · Nasdaq −0,7% · CPI +3,8% a/a"
     La pagina la trasforma da sola: la data a sinistra e i dati in pillole. Nei riquadri
     normali si vedono i PRIMI DUE dati: metti per primi i più importanti. Un dato con "+"
     diventa verde, con "−" rosso: scrivi sempre il segno davanti alla variazione
   - La foto è la STESSA dell'articolo (vedi FASE 2B), mai una diversa
   - La DATA in .n-meta e quella del blocco GIORNO sono la DATA DI RIFERIMENTO dell'articolo
     (FASE 1): identiche a quella scritta dentro l'articolo. impagina-home.py lo controlla
     e stampa "DATE DIVERSE" per ogni riquadro che non coincide
   - L'ORDINE delle schede dentro il giorno conta: la prima è la più importante (vedi f)

f) GIORNI CON 1, 2, 4, 5 ARTICOLI — MAI SPAZI VUOTI (regola adattiva):
   La griglia è a 3 colonne. Quando gli articoli del giorno non sono un multiplo di 3, quelli
   "in più" si allargano nella PRIMA riga del giorno, che è quella delle notizie più importanti:

     1 articolo   → 1 riquadro a tutta larghezza, in orizzontale (foto a sinistra, testo a destra)
     2 articoli   → 2 riquadri a metà larghezza
     3 articoli   → 3 riquadri normali
     4 articoli   → il primo a tutta larghezza, poi 3 normali
     5 articoli   → i primi 2 a metà larghezza, poi 3 normali
     6, 7, 8…     → stesso schema: resto 1 = il primo a tutta larghezza; resto 2 = i primi due a metà

   ⛔ La larghezza la decide il CSS in base al NUMERO di schede nel contenitore del giorno.
      NON scrivere MAI a mano classi col-span / md:col-span-2 sulle schede e NON inserire
      schede vuote o segnaposto per pareggiare la riga.

      Regola CSS di riferimento (griglia a 6 colonne, una scheda normale ne occupa 2):
      ```css
      .giorno-griglia { display:grid; grid-template-columns:repeat(6,1fr); }
      .giorno-griglia > .n-card { grid-column:span 2; }
      /* resto 2: i primi due a metà larghezza */
      .giorno-griglia > .n-card:first-child:nth-last-child(3n+2),
      .giorno-griglia > .n-card:first-child:nth-last-child(3n+2) + .n-card { grid-column:span 3; }
      /* resto 1: il primo a tutta larghezza, in orizzontale */
      .giorno-griglia > .n-card:first-child:nth-last-child(3n+1) { grid-column:span 6; flex-direction:row; }
      ```
   - Per funzionare, il contenitore del giorno deve avere come figli diretti SOLO le schede
   - Tablet: 2 colonne; con un numero dispari di articoli la prima scheda prende tutta la riga
     Telefono: 1 colonna, nessuna regola speciale
   - La stessa regola vale nelle pagine archivio mensile (vedi g)
   - Verifica dopo ogni aggiornamento: nessuna riga della homepage deve finire con uno spazio vuoto

📱 TELEFONO — DIMENSIONI E REGOLE (valgono per ogni aggiornamento, verificarle prima del commit):
   Una sola colonna, nessuno scorrimento orizzontale: la pagina deve essere larga quanto lo schermo.
   - Primo piano: la notizia principale è alta 380px, le altre due 200px (titolo sopra la foto)
   - Riquadri delle sezioni giorno (anche "Oggi"): 424px di altezza, tutti uguali, un riquadro per riga
   - Titolo della scheda: al massimo 85 caratteri circa; "Perché conta": due righe
   - Riga dei dati (.n-meta): la data e POI I PRIMI DUE DATI, che insieme non devono superare
     circa 34 caratteri, altrimenti su telefono la pillola viene troncata con i puntini.
     ✓ "Nasdaq +1,60% · S&P +1,31%"   ✓ "Ricavi +68,8% · Cassa 800 mln €"
     ✗ "Ricavi nove mesi +68,8% · Cassa netta ~800 mln €"   (niente "~", niente nomi lunghi)
     Metti in testa i due dati più importanti: gli altri non si vedono nei riquadri normali
   - Articoli (pagina dell'articolo) a 390px e a 360px di larghezza:
       • la foto di testa non deve uscire dallo schermo: nella <figure> usare "-mx-4 md:-mx-10"
         (applica-foto-articolo.py lo scrive già così); "-mx-6" fa scorrere la pagina di lato
       • le tabelle .data-table restano DENTRO lo schermo, senza colonne nascoste e senza scorrimento
         interno. Aggiungere sempre nel <style> dell'articolo:
         @media (max-width:640px){ .data-table{table-layout:auto;} .data-table th,.data-table td{padding:.5rem .4rem;font-size:.74rem;line-height:1.35;overflow-wrap:break-word;} .data-table th{font-size:.7rem;} }
         e, per le tabelle con 5 colonne o più: @media (max-width:380px){ .data-table th,.data-table td{overflow-wrap:anywhere;font-size:.68rem;padding:.45rem .3rem;} }
       • ⛔ MAI "display:block" o "overflow-x:auto" sulle tabelle: nasconde le colonne a destra e
         allunga le righe. Le tabelle con più di 4 colonne vanno evitate: meglio due tabelle strette
   - VERIFICA OBBLIGATORIA prima del commit, con il browser a 390px e a 360px: sulla homepage, sugli
     articoli nuovi e sulle pagine categoria deve essere vero che larghezza della pagina = larghezza
     dello schermo, nessuna pillola troncata, nessun titolo tagliato, nessuna tabella che esce

g) ULTIMI 10 GIORNI IN HOMEPAGE, IL RESTO NELL'ARCHIVIO MENSILE:
   - La homepage mostra gli articoli delle ULTIME 10 GIORNATE DI PUBBLICAZIONE: la giornata in
     primo piano più 9 sezioni giorno. Si contano le giornate in cui è uscito almeno un
     articolo, non i giorni di calendario (così la pagina non si svuota dopo una pausa)
   - A ogni aggiornamento, se le giornate in homepage diventano 11, la più VECCHIA si SPOSTA
     (sezione intera: intestazione + schede, senza modificarle) in cima alla pagina archivio
     del suo mese
   - Pagine archivio: archivio-AAAA-MM.html, una per mese (es. archivio-2026-11.html).
     Stessa testata e stesso footer della homepage, titolo "Archivio · Novembre 2026",
     sezioni giorno dalla più recente alla più vecchia, stesse schede .n-card, stessa regola f).
     Se la pagina del mese non esiste ancora: crearla, aggiungerla ad archivio.html (indice
     dei mesi, dal più recente) e alla sitemap
   - Blocco Archivio in fondo alla homepage (dopo l'ultima sezione giorno), in un riquadro unico
     con questi quattro elementi, in quest'ordine:
       1. il titolo "Archivio"
       2. una riga di testo: "<N> articoli dal febbraio 2026, ordinati per giorno."
          dove <N> è il totale degli articoli pubblicati (homepage + archivi) e il mese è
          quello del primo articolo: li ricalcola lo script a ogni esecuzione
       3. le pillole dei mesi: i 4 mesi più recenti (es. Novembre | Ottobre | Settembre | Agosto),
          ognuna collegata alla sua pagina archivio-AAAA-MM.html, più una pillola "…" che porta
          ad archivio.html (indice di tutti i mesi)
       4. il pulsante scuro "Mostra i giorni precedenti", che porta alla pagina archivio del
          mese in cui cade la giornata appena uscita dalla homepage
     Il sito è statico: pillole e pulsante sono collegamenti, non un caricamento dinamico.
     Su telefono gli elementi si impilano: titolo, riga di testo, pillole, pulsante
   - ⛔ SPOSTARE NON È CANCELLARE. Nessun articolo sparisce: dopo ogni aggiornamento il numero
     totale di schede (homepage + tutte le pagine archivio) non deve mai diminuire, e ogni
     file articolo-*.html deve essere raggiungibile da almeno una di queste pagine
   - Le pagine categoria NON hanno il limite dei 10 giorni: restano complete

h) FASCIA QUIZ + PAROLA DEL GIORNO (dopo la prima sezione giorno):
   - Quiz: fascia sottile su una riga (icona, "Quiz del mese", una frase, pulsante "Inizia"),
     collegata a quiz.html. Sostituisce il banner grande in cima alla pagina
   - Parola del giorno: un riquadro accanto al Quiz con UN termine del glossario — termine
     inglese, traduzione italiana, collegamento a glossario.html. Si aggiorna a ogni
     aggiornamento: preferire un termine aggiunto oggi (FASE 5B) o legato alla notizia principale

Per rifare in blocco le schede della homepage (per esempio dopo aver assegnato foto nuove
a un gruppo di articoli) si usa converti-home.py, che è RIESEGUIBILE quante volte serve:

   python3 converti-home.py            # scrive index-nuovo.html, per controllare prima
   python3 converti-home.py --applica  # sovrascrive index.html (backup in index-backup.html)

   La mappa DEDICATE in cima allo script associa ogni articolo alla sua foto: aggiungi lì
   le voci nuove. Lo script riconosce sia le schede storiche (.theme-card) sia quelle già
   convertite (.n-card), quindi non serve ripartire dal backup.

   Prima di applicare, verifica sempre con un diff che le uniche righe cambiate siano
   quelle delle immagini, e che il bilanciamento dei <div> resti ✅ ok.

⛔ FOTO: una per scheda, MAI ripetuta e MAI con lo stesso soggetto di un'altra scheda
   vicina. Non mettere Wall Street fotografata da più angolazioni: se due articoli
   dello stesso giorno parlano di mercati americani, uno prende il NYSE e l'altro il
   Nasdaq MarketSite, oppure il titolo citato nel pezzo (Nvidia, Jensen Huang, l'oro).
   La scelta migliore è sempre il SOGGETTO CITATO nell'articolo: MPS per un pezzo sulle
   banche, Fiat 500 per Stellantis, la piattaforma offshore per Saipem ed Eni.
   Vedi l'elenco completo con: python3 applica-foto-articolo.py --elenco

Schema colori per categorie (banner degli articoli, badge delle pagine categoria e pillola
di categoria nei riquadri della homepage, che la colora da sola in base a data-cat):
- Wall Street: blue-500, bg-blue-50, text-blue-700
- Piazza Affari: emerald-500, bg-green-50, text-green-700
- Macro/Fed: red-500, bg-red-50, text-red-700
- Tech/AI: purple-500, bg-purple-50, text-purple-700
- Commodities: amber-500, bg-amber-50, text-amber-700
- Europa: blue-500, bg-blue-50, text-blue-700
- Geopolitica: red-500, bg-red-50, text-red-700
- Corporate: sky-500, bg-sky-50, text-sky-700
- Crypto: amber-500, bg-amber-50, text-amber-700

i) SITEMAP (sitemap.xml):
   - Aggiungi i 3 nuovi articoli nella sitemap.xml
   - Ogni articolo con <url>, <loc>, <lastmod>, <changefreq>never</changefreq>, <priority>0.9</priority>
   - Includere <news:news> con publication name "Alma Finanza", language "it", publication_date e title
   - Aggiornare <lastmod> della homepage alla data odierna
   - I nuovi URL vanno SOPRA quelli precedenti (articoli più recenti prima)
   - Nei <news:title> il carattere & va scritto &amp; (es. S&amp;P 500): senza, la sitemap non è XML valido
   - Pagine archivio (FASE 3g): archivio.html e ogni archivio-AAAA-MM.html vanno in sitemap,
     senza blocco <news:news>, changefreq monthly, priority 0.5; aggiornare <lastmod> quando
     vi si sposta una giornata

FASE 4 — AGGIORNA PAGINE CATEGORIA:
Per OGNI nuovo articolo, aggiungilo alla pagina categoria corrispondente:
- categoria-wall-street.html → articoli Wall Street, Tech/AI, Macro USA, Fed, Earnings USA, Geopolitica
- categoria-borsa-milano.html → articoli Piazza Affari, FTSE MIB, aziende italiane
- categoria-crypto.html → articoli Bitcoin, Crypto
- categoria-commodities.html → articoli Petrolio, Oro, Argento, Materie prime

Per ogni pagina categoria:
- Se la data di oggi non ha ancora una sezione, aggiungila IN CIMA (prima delle date precedenti):
  ```html
  <section class="mb-12">
      <div class="flex items-center mb-6">
          <h2 class="text-2xl font-bold text-gray-900 dark:text-white montserrat-font">[Giorno], [Data completa]</h2>
          <div class="ml-4 flex-1 h-px bg-gray-300 dark:bg-slate-700"></div>
      </div>
      <div class="grid md:grid-cols-3 gap-6">
          <!-- cards qui -->
      </div>
  </section>
  ```
- Ogni card nella pagina categoria:
  ```html
  <a href="[articolo].html" class="block">
      <article class="bg-white dark:bg-[#0f172a]/60 rounded-lg shadow dark:shadow-[0_4px_24px_rgba(0,0,0,0.3)] overflow-hidden article-card hover:shadow-xl transition-shadow cursor-pointer" style="position: relative;">
          <span class="read-badge">Leggi</span>
          <div class="p-6">
              <span class="category-badge" style="background:#dbeafe;color:#1e40af;">[Sottocategoria]</span>
              <h2 class="text-xl font-bold text-gray-900 dark:text-white mt-3 mb-2 montserrat-font">TITOLO</h2>
              <p class="text-gray-600 dark:text-slate-400 text-sm mb-4">DESCRIZIONE</p>
              <div class="flex items-center justify-between text-xs text-gray-500 dark:text-slate-500">
                  <span>📰 [Data breve]</span>
                  <span class="text-teal-500 font-semibold">Leggi →</span>
              </div>
          </div>
      </article>
  </a>
  ```

FASE 5 — AGGIORNA "IMPARA LA FINANZA" (impara-finanza.html):
Per ogni info-box educativo nei 3 nuovi articoli, aggiungi un concept-card alla sezione giusta:

Sezioni disponibili (con colore bordo):
- 📊 Valutazioni e Multipli (blue)
- 🌍 Macroeconomia e Banche Centrali (cyan)
- ⚙️ Meccanismi di Mercato (purple)
- 💼 Modelli di Business (teal)
- 📈 Metriche Settoriali (amber)
- ⚠️ Gestione del Rischio (red)
- 📉 Analisi Tecnica (indigo)
- 🌍 Geopolitica e Mercati (rose)
- ⚡ Energia & Infrastrutture (orange)
- 🏦 Settore Finanziario & Bancario (emerald)
- 🏭 Settori e Aziende Specifiche (rose)

Formato concept-card:
```html
<a href="[articolo].html" class="concept-card bg-white p-5 rounded-lg shadow border-l-4 border-[COLORE]-500 hover:border-[COLORE]-600">
    <h3 class="font-bold text-lg mb-2 text-gray-900">[Titolo concetto]</h3>
    <p class="text-sm text-gray-600">[Spiegazione breve 1-2 frasi]</p>
    <span class="text-xs text-[COLORE]-600 font-semibold mt-2 inline-block">→ Spiegato in: [Nome articolo breve]</span>
</a>
```

Regole:
- Ogni info-box dell'articolo diventa un concept-card nella sezione appropriata
- Evita duplicati: se il concetto esiste già, non aggiungerlo di nuovo
- Aggiungi alla fine della griglia esistente nella sezione corretta
- Se un concetto non rientra in nessuna sezione, valuta se crearne una nuova

FASE 5B — AGGIORNA GLOSSARIO FINANZIARIO (glossario.html):
Per ogni termine tecnico inglese usato nei 3 nuovi articoli, verifica se è già presente nel glossario. Se NON è presente, aggiungilo.

Procedura:
1. Scorri i 3 articoli e raccogli TUTTI i termini tecnici inglesi usati (quelli con traduzione italiana tra parentesi, come da regola linguistica del progetto)
2. Leggi glossario.html e verifica quali termini sono già presenti (cerca nel data-term delle glossary-card)
3. Per ogni termine NUOVO (non ancora nel glossario), aggiungilo nella sezione alfabetica corretta

Formato glossary-card per ogni nuovo termine:
```html
<div class="glossary-card bg-white rounded-xl p-5 shadow-sm border border-gray-100" data-term="[termine inglese lowercase] [traduzione italiana lowercase]">
    <h3 class="font-bold text-gray-900 text-lg">[Termine Inglese]</h3>
    <p class="text-teal-600 text-sm font-semibold mb-2">[traduzione italiana]</p>
    <p class="text-gray-600 text-sm leading-relaxed">[Spiegazione chiara e accessibile in 2-3 frasi. Usa linguaggio semplice per chi sta imparando la finanza.]</p>
    <a href="[articolo-di-riferimento].html" class="text-xs text-teal-500 font-semibold mt-2 inline-block hover:underline">→ [Nome articolo breve]</a>
</div>
```

Regole glossario:
- Inserire il termine nella sezione della lettera corretta (es. "Spread" va nella sezione S), in ordine alfabetico
- Se la lettera non ha ancora una sezione nel glossario, crearne una nuova con il formato:
  ```html
  <!-- === [LETTERA] === -->
  <div id="[LETTERA]" class="mb-10">
      <div class="flex items-center gap-3 mb-4">
          <div class="letter-badge bg-teal-50 text-teal-700 montserrat-font">[LETTERA]</div>
          <div class="flex-1 h-px bg-gray-200 dark:bg-slate-700/30"></div>
      </div>
      <div class="space-y-3">
          <!-- cards qui -->
      </div>
  </div>
  ```
  E aggiungere il link alla lettera nella alpha-nav in cima alla pagina
- NON duplicare termini già esistenti
- Il campo data-term deve contenere il termine inglese e la traduzione italiana, tutto in lowercase, per la ricerca
- Aggiornare il conteggio termini nel tag <span id="term-count"> con il nuovo totale
- La spiegazione deve essere EDUCATIVA: spiegare il concetto come se il lettore fosse un principiante

FASE 6 — COMMIT E PUSH:
git add [3 articoli] index.html archivio.html archivio-*.html [foto nuove] img/repertorio/crediti.json sitemap.xml categoria-wall-street.html categoria-borsa-milano.html categoria-crypto.html categoria-commodities.html impara-finanza.html glossario.html && git commit && git push origin main

⚠️ ERRORI DA NON FARE MAI:
1. NON inventare dati — cerca SEMPRE con WebSearch prima di scrivere (FASE 1 non è opzionale)
2. NON saltare FASE 1 nemmeno quando si usano agenti background — i dati vanno cercati PRIMA di passarli agli agenti
3. NON usare dati da training/memoria come fonte per numeri finanziari — sono inaffidabili
4. NON inventare EPS, revenue, guidance di aziende specifiche — sono dati pubblici verificabili, cercali
5. NON cambiare la disposizione della homepage (FASE 3): ticker live, primo piano, ultime notizie con filtri, sezioni giorno, archivio
6. NON cambiare logo/header/footer degli articoli
7. NON dimenticare le info-box educative (minimo 2 per articolo)
8. NON usare prezzi ETF al posto dei valori indice nel ticker
9. NON omettere l'intervallo temporale nelle variazioni %
10. NON usare link con petrino80.github.io — solo almafinanza.com
11. NON cancellare articoli: quelli oltre le 10 giornate si SPOSTANO nell'archivio mensile (FASE 3g), mai eliminati
12. NON modificare mission/newsletter/footer della homepage
13. La data sul riquadro DEVE essere identica a quella dentro l'articolo, ed è il giorno a cui sono aggiornati i dati usati, non il giorno in cui si scrive (FASE 1, DATA DI RIFERIMENTO). Unica eccezione: una data diversa chiesta espressamente dall'utente
14. NON dimenticare di aggiornare le 4 pagine categoria con i nuovi articoli
15. NON dimenticare di aggiornare impara-finanza.html con i nuovi concetti educativi
16. NON dimenticare anti-flash script e dark mode toggle in ogni nuovo articolo
17. NON dimenticare le dark mode classes (dark:bg-*, dark:text-*) in ogni elemento
18. NON dimenticare di aggiornare glossario.html con i nuovi termini finanziari inglesi
19. NON duplicare termini già presenti nel glossario — controlla PRIMA di aggiungere
20. NON lasciare spazi vuoti nelle righe dei giorni e NON scrivere a mano classi col-span sulle schede: la larghezza la decide la regola adattiva (FASE 3f)
21. NON reintrodurre la Stats Bar statica e NON sostituire il Ticker Live con valori scritti a mano
22. NON cambiare a mano lo stile dei riquadri, il logo o i font: lo stile lo genera impagina-home.py. NON usare impagina-home-stile-precedente.py e NON toccare index-stile-precedente.html: sono copie di riserva ferme
23. NON modificare a mano le parti generate (primo piano, sezioni giorno, blocco archivio, pagine archivio): si incolla il blocco del giorno e si esegue impagina-home.py (FASE 3)
24. NON sbagliare il giorno della settimana: va ricavato dalla data, mai scritto a memoria (il 10 novembre 2026 fu pubblicato come lunedì: era martedì). Vale per la testata degli articoli e per le pagine categoria, che lo script non tocca
25. NON scrivere le tabelle degli articoli con display:block o overflow-x e NON dimenticare la regola per telefono nel <style> (FASE 3, blocco TELEFONO): le colonne a destra spariscono

📌 LEZIONE APPRESA (20/05/2026 — caso Nvidia):
- EPS Nvidia Q1 FY2027 era $1,87 vs $1,77 atteso. Fu pubblicato erroneamente come $9,82 vs $9,10.
- Errore causato da: (a) FASE 1 saltata, (b) dati inventati passati agli agenti background,
  (c) confusione con prezzi pre-split (Nvidia ha fatto 10:1 split a giugno 2024).
- Correzione richiesta: 5 file modificati + commit hotfix separato.
- Prevenzione: per articoli su earnings, WebSearch è BLOCCANTE — senza dati verificati, non si scrive.

Sia per homepage che per nuovi articoli usa il design Minimal Modern con possibilità di switch light/dark
```

---

## NOTE PER L'USO:

- **Quando usarlo**: Ogni giorno dopo la chiusura delle borse (dopo le 22:00 ora italiana per avere sia Europa che USA)
- **Data**: se non scrivi nulla, ogni articolo prende la data del giorno a cui si riferiscono i dati (per esempio la seduta di ieri, se lanci l'aggiornamento dopo mezzanotte). Se vuoi una data diversa, scrivila nella richiesta: vale quella
- **Personalizzare**: Puoi aggiungere al prompt richieste specifiche come "un articolo su [azienda X]" o "focus su [tema Y]"
- **Esempio rapido**: Se hai fretta, puoi scrivere semplicemente: "Aggiornamento quotidiano Alma Finanza — 11 marzo 2026" e il sistema seguirà tutte le regole sopra
- **Se qualcosa va storto**: Controlla che il sito sia online su www.almafinanza.com dopo il push

## CHECKLIST RAPIDA POST-AGGIORNAMENTO:

- [ ] 3 articoli creati con dark mode + toggle + anti-flash + SEO + info-box
- [ ] ogni articolo ha una FOTO di apertura con credito, firma "Alma Finanza" e tempo di lettura (FASE 2B)
- [ ] ogni foto nuova è registrata in img/repertorio/crediti.json con autore e licenza
- [ ] NESSUNA foto è ripetuta su due articoli (lo script blocca da solo: mai usare --forza)
- [ ] ogni articolo e ogni card hanno il blocco "Perché conta:" (FASE 2C)
- [ ] le card in homepage mostrano la miniatura dell'immagine dell'articolo
- [ ] index.html: blocco del giorno incollato sotto <!-- NUOVO-GIORNO -->; dopo lo script gli articoli di oggi sono in primo piano e la Parola del giorno è aggiornata
- [ ] nessuna riga dei giorni con spazi vuoti (regola adattiva, FASE 3f) e nessuna intestazione di giorno doppia
- [ ] TELEFONO (390 e 360px): pagina larga come lo schermo, riga dei dati entro 34 caratteri e senza pillole troncate, tabelle degli articoli dentro lo schermo, foto con -mx-4, sezione "Oggi" sotto "Ultime notizie" (FASE 3, blocco TELEFONO)
- [ ] homepage con al massimo 10 giornate; la più vecchia spostata nell'archivio mensile, nessun articolo perso (FASE 3g)
- [ ] blocco Archivio: conteggio articoli ricalcolato, pillole dei 4 mesi più recenti, pulsante "Mostra i giorni precedenti"
- [ ] sitemap.xml aggiornata e valida come XML
- [ ] impagina-home.py --applica eseguito senza errori; il numero di schede verificate è quello di ieri più gli articoli di oggi
- [ ] giorno della settimana giusto negli articoli e nelle pagine categoria (ricavato dalla data)
- [ ] UNA sola data per articolo, quella dei dati usati, identica su riquadro, articolo, nome file, pagine categoria e sitemap; nessuna riga "DATE DIVERSE" per gli articoli di oggi
- [ ] categoria-wall-street.html aggiornata
- [ ] categoria-borsa-milano.html aggiornata
- [ ] categoria-crypto.html aggiornata (se ci sono articoli crypto)
- [ ] categoria-commodities.html aggiornata (se ci sono articoli commodities)
- [ ] impara-finanza.html: nuovi concetti educativi aggiunti
- [ ] glossario.html: nuovi termini finanziari inglesi aggiunti (se presenti)
- [ ] git commit + push riuscito
