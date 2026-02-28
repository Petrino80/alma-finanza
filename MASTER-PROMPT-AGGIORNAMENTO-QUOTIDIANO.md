# MASTER PROMPT — Aggiornamento Quotidiano Alma Finanza

**Copia e incolla questo prompt ogni giorno per aggiornare il sito.**

---

## IL PROMPT DA USARE:

```
Aggiornamento quotidiano Alma Finanza — [DATA DI OGGI, es: 26 febbraio 2026]

FASE 1 — RICERCA DATI REALI:
Cerca con WebSearch i dati REALI di chiusura delle borse di oggi (o ieri sera se le borse USA sono ancora aperte). Dati richiesti:
- Indici USA: Dow Jones, S&P 500, Nasdaq (valori indice, NON prezzi ETF)
- Indici Europa: FTSE MIB, DAX, CAC 40
- Commodities: Oro, Petrolio WTI
- Bitcoin
- Titoli protagonisti della giornata (top gainers/losers)
- Notizie macro principali (Fed, dazi, earnings, geopolitica)
⚠️ NON INVENTARE MAI NESSUN DATO. Se non trovi un dato, scrivilo come "—".

FASE 2 — SCRIVI 5 ARTICOLI:
Crea 5 articoli HTML seguendo queste regole INVIOLABILI:

Distribuzione consigliata (adattabile alle notizie del giorno):
1. Wall Street / mercati USA (obbligatorio)
2. Piazza Affari / FTSE MIB (obbligatorio)
3. Uno tra: Europa, Asia, o mercati emergenti
4-5. Due tra: earnings aziendali, macro/Fed, commodities, settori specifici, tech/AI, geopolitica/dazi

Formato articoli — REGOLE FISSE, MAI CAMBIARE:
- File: articolo-[topic]-[DDmese]-[dettaglio].html (es: articolo-wall-street-26feb-nvidia-rally.html)
- Google Analytics: G-E88FFDTPMP in ogni file
- Header/Logo: Lobster "A" teal-500 + Montserrat "LMA FINANZA" (identico alla homepage)
- Banner colorato con categoria, titolo h1, data, "Redazione"
- Lead paragraph con i dati chiave
- Contenuto con h2 per sezioni, dati in grassetto, tabelle .data-table per indici/titoli
- Classi .positive (verde) e .negative (rosso) per variazioni
- MINIMO 2 info-box educativi per articolo: <div class="info-box"><h3>💡 Impara: [Concetto]</h3><p>...</p></div>
- Ogni variazione % DEVE specificare l'intervallo temporale (giorno, settimana, mese, YTD)
- Footer STANDARD (MAI cambiare): "Alma Finanza" in Lobster teal-400, copyright 2026, disclaimer
- Tono informativo, MAI dare consigli finanziari, spiegare i concetti
- SEO obbligatorio in ogni articolo (inserire prima di </head>):
  • Open Graph: og:type, og:title, og:description, og:url, og:site_name, og:locale, article:published_time, article:author, article:section
  • Twitter Card: twitter:card, twitter:title, twitter:description
  • Canonical: <link rel="canonical" href="https://www.almafinanza.com/[nome-file].html">
  • Schema.org JSON-LD: @type NewsArticle con headline, description, url, datePublished, author, publisher, inLanguage

FASE 3 — AGGIORNA HOMEPAGE (index.html):
⚠️ NON CAMBIARE MAI IL FORMATO/LAYOUT DELLA HOMEPAGE. Solo aggiornare i contenuti.

a) TICKER (barra scorrevole in alto):
   - Aggiorna tutti i valori con dati reali di chiusura
   - Minimo: Dow, S&P 500, Nasdaq, FTSE MIB + 5-8 titoli protagonisti del giorno
   - Usa valori INDICE (es: Dow 49.174), MAI prezzi ETF (es: DIA 491.74)
   - Duplica gli item per il loop continuo
   - Classe .positive o .negative in base alla direzione

b) DATA nell'header:
   - Formato completo: "Mercoledì, 26 Febbraio 2026"
   - Formato mobile: "26 Feb 2026"
   - Giorno della settimana CORRETTO in italiano

c) HERO ARTICLE (articolo principale):
   - Cambia OGNI GIORNO con l'articolo più importante
   - Pannello sinistro: badge categoria, titolo, descrizione, bottone "Leggi →"
   - Pannello destro: dato numerico grande (es: +370 Dow Jones punti)
   - Link al nuovo articolo

d) GRIGLIA ARTICOLI:
   - Aggiungi 5 nuove card IN CIMA alla griglia (sopra gli articoli precedenti)
   - Commento separatore: <!-- ====== ARTICOLI [DATA] ====== -->
   - Ogni card: <a href="..."> wrapping, gradient colorato per categoria, titolo, descrizione
   - Ordine: più recenti in alto, più vecchi in basso
   - Layout: grid md:grid-cols-3 gap-6 (MAI cambiare)

Schema colori per categorie:
- Wall Street: from-blue-700 to-blue-900, border #1d4ed8
- Piazza Affari: from-green-700 to-emerald-800, border #15803d
- Macro/Fed: from-red-700 to-rose-900, border #dc2626
- Tech/AI: from-emerald-600 to-teal-800 oppure from-purple-700 to-indigo-900
- Commodities: from-amber-600 to-yellow-700, border #d97706
- Geopolitica: from-red-700 to-rose-900, border #dc2626
- Corporate: from-sky-700 to-blue-900, border #0369a1

e) SITEMAP (sitemap.xml):
   - Aggiungi i 5 nuovi articoli nella sitemap.xml
   - Ogni articolo con <url>, <loc>, <lastmod>, <changefreq>never</changefreq>, <priority>0.9</priority>
   - Includere <news:news> con publication name "Alma Finanza", language "it", publication_date e title
   - Aggiornare <lastmod> della homepage alla data odierna
   - I nuovi URL vanno SOPRA quelli precedenti (articoli più recenti prima)

FASE 4 — COMMIT E PUSH:
git add [5 articoli] index.html sitemap.xml && git commit && git push origin main

⚠️ ERRORI DA NON FARE MAI:
1. NON inventare dati — cerca SEMPRE con WebSearch prima di scrivere
2. NON cambiare il layout della homepage (3 colonne, no layout sperimentali)
3. NON cambiare logo/header/footer degli articoli
4. NON dimenticare le info-box educative (minimo 2 per articolo)
5. NON usare prezzi ETF al posto dei valori indice nel ticker
6. NON omettere l'intervallo temporale nelle variazioni %
7. NON usare link con petrino80.github.io — solo almafinanza.com
8. NON cancellare articoli vecchi dalla homepage
9. NON modificare newsletter/footer della homepage
10. Date sulle card DEVONO corrispondere alle date dentro gli articoli
```

---

## NOTE PER L'USO:

- **Quando usarlo**: Ogni giorno dopo la chiusura delle borse (dopo le 22:00 ora italiana per avere sia Europa che USA)
- **Personalizzare**: Puoi aggiungere al prompt richieste specifiche come "un articolo su [azienda X]" o "focus su [tema Y]"
- **Esempio rapido**: Se hai fretta, puoi scrivere semplicemente: "Aggiornamento quotidiano Alma Finanza — 26 febbraio 2026" e il sistema seguirà tutte le regole sopra
- **Se qualcosa va storto**: Controlla che il sito sia online su www.almafinanza.com dopo il push
