# MASTER PROMPT — Aggiornamento Quotidiano Alma Finanza

**Copia e incolla questo prompt ogni giorno per aggiornare il sito.**

---

## IL PROMPT DA USARE:

```
Aggiornamento quotidiano Alma Finanza — [DATA, es: 11 marzo 2026 - ora chiusura borse USA]

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

FASE 3 — AGGIORNA HOMEPAGE (index.html):
⚠️ NON CAMBIARE MAI IL FORMATO/LAYOUT DELLA HOMEPAGE. Solo aggiornare i contenuti.
Design: Modern Minimal con switch light/dark.

a) TICKER (barra scorrevole in alto):
   - Aggiorna tutti i valori con dati reali di chiusura
   - Minimo: Dow, S&P 500, Nasdaq, FTSE MIB + 5-8 titoli/indici protagonisti del giorno
   - Usa valori INDICE (es: Dow 49.174), MAI prezzi ETF (es: DIA 491.74)
   - Duplica gli item per il loop continuo (seamless scroll)
   - Classe .positive o .negative in base alla direzione

b) DATA nell'header:
   - Formato: "Mercoledì 26 Febbraio 2026"
   - Giorno della settimana CORRETTO in italiano

c) STATS BAR (6 riquadri sotto header):
   - Aggiorna: Dow Jones, S&P 500, FTSE MIB, WTI Crude, Oro, Bitcoin
   - Valori + variazione giornaliera con classi .positive/.negative

d) HERO ARTICLE (articolo principale):
   - Cambia OGNI GIORNO con la notizia più importante
   - Pannello sinistro: dot pulsante, badge "Breaking · [DATA]", titolo h1, accent-line, descrizione, "Leggi l'articolo completo →"
   - Pannello destro: dato numerico grande (es: $83, +2.67%), sottotitolo, badge variazione, dati riassuntivi
   - Link al nuovo articolo
   - Colore dot/badge: emerald per positivo, red per negativo

e) GRIGLIA ARTICOLI (theme-cards):
   - Aggiungi 5 nuove theme-card IN CIMA alla griglia
   - Section header: "Oggi, [GIORNO] [MESE]" aggiornato
   - Commento separatore per data precedente
   - Ogni card segue il formato theme-card:
     ```html
     <a href="URL" class="theme-card bg-white dark:bg-[#0f172a]/60 border border-gray-100 dark:border-slate-700/30 hover:border-teal-500 dark:hover:border-teal-500/40 hover:shadow-lg dark:hover:shadow-[0_4px_24px_rgba(0,0,0,0.3)] group">
         <div class="h-1.5 bg-COLOR-500"></div>
         <div class="p-5">
             <span class="cat-tag bg-COLOR-50 dark:bg-COLOR-500/15 text-COLOR-700 dark:text-COLOR-400">CATEGORIA</span>
             <h3 class="text-base font-bold text-gray-900 dark:text-white mt-3 mb-2 leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition">TITOLO</h3>
             <p class="text-sm text-gray-400 dark:text-slate-500 leading-relaxed">DESCRIZIONE</p>
             <div class="flex items-center justify-between mt-4 pt-3 border-t border-gray-50 dark:border-slate-700/20">
                 <span class="text-xs text-gray-300 dark:text-slate-600">DATA</span>
                 <span class="text-xs text-teal-500 font-semibold opacity-0 group-hover:opacity-100 transition">Leggi →</span>
             </div>
         </div>
     </a>
     ```
   - Day separator tra date diverse:
     ```html
     <div class="col-span-full flex items-center gap-3 mt-6 mb-2">
         <div class="w-10 h-0.5 rounded-full bg-gray-200 dark:bg-slate-700/40"></div>
         <h2 class="text-sm font-bold montserrat-font text-gray-400 dark:text-slate-600 uppercase tracking-wider">[DATA PRECEDENTE]</h2>
         <div class="flex-1 h-0.5 rounded-full bg-gray-100 dark:bg-slate-800/20"></div>
     </div>
     ```

Schema colori per categorie (accent line + cat-tag):
- Wall Street: blue-500, bg-blue-50, text-blue-700
- Piazza Affari: emerald-500, bg-green-50, text-green-700
- Macro/Fed: red-500, bg-red-50, text-red-700
- Tech/AI: purple-500, bg-purple-50, text-purple-700
- Commodities: amber-500, bg-amber-50, text-amber-700
- Europa: blue-500, bg-blue-50, text-blue-700
- Geopolitica: red-500, bg-red-50, text-red-700
- Corporate: sky-500, bg-sky-50, text-sky-700
- Crypto: amber-500, bg-amber-50, text-amber-700

f) SITEMAP (sitemap.xml):
   - Aggiungi i 5 nuovi articoli nella sitemap.xml
   - Ogni articolo con <url>, <loc>, <lastmod>, <changefreq>never</changefreq>, <priority>0.9</priority>
   - Includere <news:news> con publication name "Alma Finanza", language "it", publication_date e title
   - Aggiornare <lastmod> della homepage alla data odierna
   - I nuovi URL vanno SOPRA quelli precedenti (articoli più recenti prima)

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
Per ogni info-box educativo nei 5 nuovi articoli, aggiungi un concept-card alla sezione giusta:

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

FASE 6 — COMMIT E PUSH:
git add [5 articoli] index.html sitemap.xml categoria-wall-street.html categoria-borsa-milano.html categoria-crypto.html categoria-commodities.html impara-finanza.html && git commit && git push origin main

⚠️ ERRORI DA NON FARE MAI:
1. NON inventare dati — cerca SEMPRE con WebSearch prima di scrivere
2. NON cambiare il layout della homepage (stats bar + 3 colonne theme-cards)
3. NON cambiare logo/header/footer degli articoli
4. NON dimenticare le info-box educative (minimo 2 per articolo)
5. NON usare prezzi ETF al posto dei valori indice nel ticker
6. NON omettere l'intervallo temporale nelle variazioni %
7. NON usare link con petrino80.github.io — solo almafinanza.com
8. NON cancellare articoli vecchi dalla homepage
9. NON modificare mission/newsletter/footer della homepage
10. Date sulle card DEVONO corrispondere alle date dentro gli articoli
11. NON dimenticare di aggiornare le 4 pagine categoria con i nuovi articoli
12. NON dimenticare di aggiornare impara-finanza.html con i nuovi concetti educativi
13. NON dimenticare anti-flash script e dark mode toggle in ogni nuovo articolo
14. NON dimenticare le dark mode classes (dark:bg-*, dark:text-*) in ogni elemento

Sia per homepage che per nuovi articoli usa il design Minimal Modern con possibilità di switch light/dark
```

---

## NOTE PER L'USO:

- **Quando usarlo**: Ogni giorno dopo la chiusura delle borse (dopo le 22:00 ora italiana per avere sia Europa che USA)
- **Personalizzare**: Puoi aggiungere al prompt richieste specifiche come "un articolo su [azienda X]" o "focus su [tema Y]"
- **Esempio rapido**: Se hai fretta, puoi scrivere semplicemente: "Aggiornamento quotidiano Alma Finanza — 11 marzo 2026" e il sistema seguirà tutte le regole sopra
- **Se qualcosa va storto**: Controlla che il sito sia online su www.almafinanza.com dopo il push

## CHECKLIST RAPIDA POST-AGGIORNAMENTO:

- [ ] 5 articoli creati con dark mode + toggle + anti-flash + SEO + info-box
- [ ] index.html: ticker, stats bar, data, hero, 5 nuove theme-cards, sitemap
- [ ] categoria-wall-street.html aggiornata
- [ ] categoria-borsa-milano.html aggiornata
- [ ] categoria-crypto.html aggiornata (se ci sono articoli crypto)
- [ ] categoria-commodities.html aggiornata (se ci sono articoli commodities)
- [ ] impara-finanza.html: nuovi concetti educativi aggiunti
- [ ] git commit + push riuscito
