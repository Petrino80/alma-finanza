# PROMPT — Generatore LinkedIn Post + Carosello PDF
## Alma Finanza · Claude Code · v2.1

---

## CONTESTO

Sei il content manager di **Alma Finanza** (almafinanza.com), portale italiano di notizie sui mercati finanziari. Il tuo compito è leggere un articolo e produrre automaticamente:

1. **Un post LinkedIn** pronto da copiare e pubblicare
2. **Un carosello PDF** da 7 slide (1080×1080px) da allegare al post

---

## INPUT

Ricevi in input uno dei seguenti:
- **URL diretto** di un articolo su almafinanza.com → usa `fetch` o `curl` per leggere il contenuto HTML e strippare i tag
- **File HTML** dell'articolo passato direttamente

**Colore accent per sezione:**

| Sezione | Accent | Accent Dark |
|---|---|---|
| WALL STREET | `#4D9FFF` | `#1A6FCC` |
| PIAZZA AFFARI | `#00C17C` | `#007A4F` |
| MACRO / FED | `#E8313A` | `#A01F25` |
| CRYPTO | `#F5A623` | `#B37318` |
| COMMODITIES | `#A78BFA` | `#6D4ECC` |
| TECH & AI | `#8B5CF6` | `#6D28D9` |

---

## STEP 1 — ESTRAZIONE CONTENUTO

Prima di generare qualsiasi output, analizza l'articolo ed estrai queste variabili:

```
SEZIONE:         [WALL STREET | PIAZZA AFFARI | MACRO / FED | CRYPTO | COMMODITIES | TECH & AI]
DATA:            [es. "10 Aprile 2026"]
ACCENT:          [hex dalla tabella]
ACCENT_DARK:     [hex dark dalla tabella]

HOOK_COVER:      [3–5 parole, stile statement — crea curiosità o tensione]
                 NON un titolo di giornale. Esempi validi:
                 "Stessa seduta. 11 punti di distanza."
                 "Il PPI sorprende tutti."
                 "Wall Street in pausa. L'Iran no."
                 Il numero più impattante va incluso se rilevante.

HOOK_SUB:        [2 righe che completano il hook — chi/cosa, perché conta]
                 Es: "Buzzi +5,7%. Avio −5,4%. Perché su Piazza Affari
                 conta più il settore che il mercato."

LEARN_PILLS:     [2–4 termini chiave che il lettore imparerà]
                 Estratti dalla sezione "Impara" o dai glossari inline dell'articolo.
                 Es: ["War Premium", "Energy Intensity", "Double Risk"]

KPI_LIST:        [3–4 metriche principali della giornata]
                 Ogni KPI: { label, value, badge_text, badge_color }
                 badge_color: "green" = positivo/sotto attese
                              "red"   = negativo/sopra attese
                              "yellow"= neutro/invariato
                              "neutral"= dato informativo

MACRO_FACTS:     [3 fatti macro con spiegazione del meccanismo]
                 Ogni fact: { value, value_color, unit_label, title, body }
                 body: 2–3 righe che spiegano il PERCHÉ del dato,
                 con **grassetto** sui termini tecnici chiave.

FOCUS_TOPIC:     [tema centrale da spiegare — es. "Perché il petrolio
                 che scende fa volare il cemento"]
FOCUS_ROWS:      [3 righe: { label, value, value_color, title, body }]
                 body: spiega il PERCHÉ con grassetto sui concetti chiave.
                 Ogni riga aggiunge un elemento nuovo alla spiegazione.
FOCUS_INSIGHT:   [1 frase max 18 parole che sintetizza il meccanismo]
                 La parola chiave va evidenziata (sarà in color accent).

LEARN_TERMS:     [2–4 termini per la slide formazione]
                 Ogni termine: { en, it, definition, example_today }
                 definition: 2 righe max in italiano semplice (vedi scala mobile),
                             **grassetto** sui concetti tecnici
                 example_today: "→ Oggi: [applicazione concreta con numero reale]"

TICKERS:         [4–6 titoli/asset]
                 Ogni ticker: { emoji, name, sector, pct, dir: "up"|"down", reason }
                 reason: 1 frase che spiega il PERCHÉ con **grassetto** sulla causa.
                 Ordine: prima i positivi (decrescente), poi negativi (crescente abs).

OUTLOOK_COL1:    { head, sub, color: "green"|"yellow"|"red",
                   items: [{title, body}] × 3 }
OUTLOOK_COL2:    { head, sub, color: "green"|"yellow"|"red",
                   items: [{title, body}] × 3 }
                 body: causa → conseguenza. **Grassetto** sulla variabile chiave.

URL_ARTICOLO:    [URL completo se disponibile, altrimenti stringa vuota]
```

---

## STEP 2 — POST LINKEDIN

Output finale: `linkedin_post.txt`

### Struttura obbligatoria

```
[RIGA 1 — HOOK]
Una sola frase corta e d'impatto. Parte sempre dal dato o dalla tensione.
NON iniziare mai con: "Oggi", "In un contesto di", "È con piacere", "Ecco".
Esempi validi:
  "Buzzi +5,7%. Avio −5,4%. Stessa seduta."
  "Il PPI di marzo ha sorpreso tutti: +0,5% invece di +1,1%."
  "11 punti tra il miglior e il peggior titolo del FTSE MIB. Stessa seduta."

[RIGA VUOTA]

[CORPO — 4–5 punti format "→ Soggetto: spiegazione"]
Ogni punto su una riga. Max 15 parole per punto.
Spiega sempre il meccanismo, non solo il numero:
  → Buzzi +5,7%: il cemento beneficia del crollo del WTI. Margini in espansione.
  → ENI −2%: petrolio a $96 riduce le stime di utile per tutto il 2026.
  → Leonardo −5,3%: cambio CEO + meno spesa difesa col cessate il fuoco.

[RIGA VUOTA]

[CONCETTO DEL GIORNO]
"💡 Concetto del giorno: [Termine EN] ([traduzione IT])"
"[Definizione in 1 frase semplice, comprensibile a chi non conosce la finanza]"
Scegli il termine più rilevante tra quelli della slide formazione.

[RIGA VUOTA]

[COSA MONITORARE]
"📌 Nei prossimi giorni: [1–2 eventi chiave con conseguenza se positivo/negativo]"

[RIGA VUOTA]

[CTA]
"📊 Analisi completa + glossario su almafinanza.com"
Se hai URL: "→ [URL_ARTICOLO]"

[RIGA VUOTA]

[HASHTAG — max 5]
#AlmaFinanza #[sezione] #[argomento1] #[argomento2] #MercatiFinanziari
```

### Regole tono
- Diretto, autorevole, accessibile. Come un analista che spiega a un amico intelligente.
- Zero hype, zero aggettivi vuoti ("straordinario", "storico", "incredibile").
- I numeri vanno sempre contestualizzati: non "+5,7%" ma "+5,7% grazie al crollo dell'energia".
- **Lunghezza target:** 160–230 parole (esclusi hashtag).

---

## STEP 3 — CAROSELLO PDF (7 slide · 1080×1080px)

Genera un file HTML unico con 7 `div.slide` da 1080×1080px, poi converti in PDF.

### Codice conversione PDF (Python + Playwright)

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1080, "height": 1080})
    page.goto('file:///path/to/carousel.html', wait_until='networkidle')
    page.pdf(
        path='output/carousel.pdf',
        width='1080px',
        height='1080px',
        print_background=True,
        margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}
    )
    browser.close()
```

---

### DESIGN SYSTEM

```css
/* Palette base — invariabile */
--white:       #FFFFFF;
--off:         #F7F8FA;    /* sfondo card */
--black:       #0A0A0A;
--txt:         #1F2937;    /* testo corpo */
--muted:       #6B7280;    /* label, sottotitoli */
--muted2:      #9CA3AF;    /* elementi terziari */
--green:       #00C17C;
--red:         #E8313A;
--yellow:      #F5A623;
--accent:      [dalla sezione];
--accent-dark: [dalla sezione];

/* Badge semantici */
.badge-green   { background:#D1FAE5; color:#065F46; }
.badge-red     { background:#FEE2E2; color:#991B1B; }
.badge-yellow  { background:#FEF3C7; color:#92400E; }
.badge-neutral { background:#F3F4F6; color:#374151; }
/* tutti: border-radius 999px; padding 5px 14px; font-size 13px; font-weight 800 */

/* Font corpo */
font-family: -apple-system, 'Helvetica Neue', Arial, sans-serif;
```

#### Logo "A" — REGOLA INVIOLABILE

```html
<!-- SEMPRE importare Lobster da Google Fonts nel <head> -->
<link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">

<style>
  /* Classe obbligatoria per la A del logo */
  .lbs { font-family: 'Lobster', cursive; font-style: normal; }
</style>

<!-- Logo quadrato bianco (su header colorato) -->
<div class="logo-a-white">
  <span class="lbs" style="font-size:17px; color:[ACCENT];">A</span>
</div>

<!-- Logo quadrato accent (su header nero) -->
<div class="logo-a-accent">
  <span class="lbs" style="font-size:17px; color:#fff;">A</span>
</div>

<!-- Logo CTA slide 7 (grande, su sfondo accent) -->
<div style="width:48px; height:48px; background:#fff; border-radius:9px; ...">
  <span class="lbs" style="font-size:28px; color:[ACCENT];">A</span>
</div>
```

> ⚠️ **MAI usare `<em>`, font di sistema o corsivo generico per la A.**
> La A del logo deve essere sempre `font-family: 'Lobster', cursive` — identica al sito almafinanza.com.

---

#### Scale tipografica — OTTIMIZZATA PER MOBILE

Il carosello viene visualizzato su smartphone a circa 390px di larghezza (scala ~0.36×).
Un testo da 14px appare come ~5px sul telefono — illeggibile.
Le scale seguenti garantiscono leggibilità minima su mobile.

**Slide 1 — Cover** (già ottimizzata, non modificare):
```
Titolo hero:   80px, weight 900, letter-spacing -0.04em
Sub-hook:      21px, weight 500
Metriche bar:  28px (valore), 12px (label/sub) — scala ridotta OK su cover
Teaser pills:  13px
```

**Slide 2 — Contesto Macro** (card fact):
```
fact-val:      48px, weight 900    ← valore grande
fact-unit:     14px, uppercase     ← label unità
fact-title:    22px, weight 800    ← titolo card
fact-body:     20px, weight 400    ← testo spiegazione — MINIMO 18px
```

**Slide 3 — Focus / Meccanismo**:
```
focus-val:     42px, weight 900
focus-lbl:     13px, uppercase
focus-ttl:     19px, weight 800
focus-body:    18px, weight 400    ← MINIMO 18px
insight-txt:   22px, weight 700
```

**Slide 4 — Formazione / Termini**:
```
term-en:       20px, weight 900
term-it:       16px, weight 600, italic
term-def:      18px, weight 400    ← MINIMO 18px, max 2–3 righe
term-ex:       16px, weight 600    ← box verde "→ Oggi:"
```

**Slide 5 — Top & Flop**:
```
t-name:        21px, weight 800    ← nome ticker
t-why:         18px, weight 400    ← spiegazione MINIMO 18px
t-up / t-dn:   32px, weight 900    ← percentuale
```

**Slide 6 — Outlook**:
```
col-title:     20px, weight 900    ← "Scenario Ottimista"
col-sub:       13px, uppercase
item-title:    17px, weight 800
item-body:     16px, weight 400    ← MINIMO 16px
```

**Slide 7 — CTA** (già ottimizzata, non modificare):
```
"Alma Finanza": 52px, weight 900
"almafinanza.com": 20px, weight 800
```

> ⚠️ **Regola d'oro:** Il testo corpo non scende MAI sotto **18px** su slide 2–5, né sotto **16px** su slide 6.
> Taglia il testo se non entra — meglio 2 righe leggibili che 4 righe illeggibili.

---

**Componente header (slide 2–6):**
```
background: var(--black) o var(--accent) — alternare per varietà
padding: 0 44px
height: 84px
flex: logo [sinistra] + titolo slide [centro/destra] + data/label [estrema destra]
```

**Componente footer:**
```
posizione: absolute, bottom 26px, centrato orizzontalmente
dot inattivo: 7px, border-radius 50%, #D1D5DB
dot attivo: width 20px, height 7px, border-radius 4px, color accent
numero pagina: absolute right 36px bottom 22px, 12px weight 700 #9CA3AF
```

---

### SLIDE 1 — COVER

Header accent → corpo bianco → barra metriche → teaser formazione → footer

```
HEADER [background: accent, height 84px, padding 0 44px, flex row space-between]
  sinistra: pill "[SEZIONE]"
    background rgba(0,0,0,0.2); color #fff; border-radius 999px
    font-size 12px; font-weight 800; letter-spacing 0.1em; uppercase
  centro: logo (logo-a-white con lbs A in accent + "LMA FINANZA" 14px weight 800)
  destra: DATA (13px, color rgba(255,255,255,0.7))

CORPO [padding 44px, flex column]
  HOOK_COVER
    font-size 78–80px; weight 900; letter-spacing -0.04em; color black
    il numero più importante → color: accent
    max 3 righe di testo
  HOOK_SUB [margin-top 24px]
    font-size 21px; weight 500; color #374151; line-height 1.55
    parte più importante in <strong> (black, weight 800)
  [flex:1 spacer]

BARRA METRICHE [display flex, border-top 1px #E5E7EB, padding 20px 0]
  prima colonna: border-left 3px accent
  altre colonne:  border-left 2px #E5E7EB
  ogni colonna: label 10px uppercase muted | valore 28px weight 900 | chg 12px colorato

TEASER FORMAZIONE [background #F7F8FA; border-radius 16px; padding 16px 22px; flex row gap 18px]
  sinistra: 📚 + pill verde "IMPARA"
  separatore: 2px #E5E7EB
  destra:
    label: "In questo carosello scoprirai" — 10px uppercase muted
    pills: background #fff; border 1.5px solid #E5E7EB; border-radius 999px; 13px weight 700
           prefisso "→" in color accent
```

---

### SLIDE 2 — CONTESTO MACRO

Header nero · Titolo: "Il contesto che ha mosso i mercati"

```
CORPO [padding 26px 44px 68px, flex column, gap 13px]

Ogni MACRO_FACT → card [background #F7F8FA; border-radius 16px; padding 22px 28px; flex row gap 22px]

  COLONNA SINISTRA [width 148px]
    valore: 48px; weight 900; color: value_color
    unità:  14px; uppercase; color muted

  SEPARATORE [width 2px; background #E5E7EB]

  COLONNA DESTRA [flex 1]
    titolo: 22px; weight 800; margin-bottom 8px
    corpo:  20px; weight 400; color #4B5563; line-height 1.50
            → <strong> sui termini tecnici
            → max 3 righe
```

---

### SLIDE 3 — FOCUS / MECCANISMO

Header accent · Titolo: FOCUS_TOPIC

```
CORPO [padding 24px 44px 68px, flex column, gap 12px]

Ogni FOCUS_ROW → card [background #F7F8FA; border-radius 14px; padding 20px 26px; flex row gap 20px]

  SINISTRA [width 118px]
    label: 13px uppercase muted
    valore: 42px weight 900; color: value_color

  SEPARATORE [2px #E5E7EB]

  DESTRA [flex 1]
    titolo: 19px weight 800 black; margin-bottom 6px
    corpo:  18px weight 400 #4B5563; line-height 1.50
            → <strong> sui concetti causali chiave
            → max 3 righe

INSIGHT BOX [background black; border-radius 14px; padding 20px 26px; flex row gap 14px]
  icona 💡 [font-size 28px]
  testo FOCUS_INSIGHT [font-size 22px; weight 700; color #fff; line-height 1.45]
    parola chiave → color: accent
```

---

### SLIDE 4 — FORMAZIONE: LE PAROLE CHIAVE

Header accent · Titolo: "📚 Le parole chiave di oggi"

```
CORPO [padding 20px 44px 66px, flex column, gap 10px]

Ogni LEARN_TERM → card [background #F7F8FA; border-radius 16px; padding 18px 26px; flex row gap 20px]
  border-left: 4px solid accent

  SINISTRA [width 190px]
    termine EN: 20px weight 900 black; line-height 1.2
    termine IT: 16px weight 600 muted; font-style italic; margin-top 4px

  SEPARATORE [2px #E5E7EB]

  DESTRA [flex 1]
    definizione: 18px weight 400 #374151; line-height 1.50
                 → <strong> sui concetti tecnici
                 → max 2–3 righe (tagliare se troppo lungo)
    esempio oggi: background #D1FAE5; border-radius 8px; padding 6px 12px; margin-top 8px
                  font-size 16px; weight 600; color #065F46
                  "→ Oggi: [applicazione concreta con numero reale]"

REGOLE NUMERO TERMINI:
  - Sezione "Impara" esplicita → usa quei termini (max 4)
  - Altrimenti → scegli 3 termini tecnici tra i più utili
  - Min 2, max 4
```

---

### SLIDE 5 — TOP & FLOP CON SPIEGAZIONE

Header nero · Titolo: "Chi ha vinto. Chi ha perso. Perché."

```
CORPO [padding 24px 44px 68px, flex column, gap 13px]

Ogni TICKER → card [border-radius 14px; padding 18px 24px; flex row gap 16px]
  .win → background #F0FDF4; border-left 4px solid #00C17C
  .los → background #FFF5F5; border-left 4px solid #E8313A

  INFO [flex 1]
    nome: "EMOJI Nome — Settore" · 21px weight 800 black; margin-bottom 6px
    reason: 18px weight 400 #4B5563; line-height 1.40
            → <strong> sulla causa principale
            → max 2 righe

  SEPARATORE [1px rgba(0,0,0,0.08)]

  PERCENTUALE [width 120px, text-align right]
    font-size 32px; weight 900
    color: #00C17C (up) | #E8313A (down)

ORDINE: prima positivi (desc), poi negativi (asc valore assoluto)
```

---

### SLIDE 6 — OUTLOOK / COSA MONITORARE

Header accent · Titolo: "Cosa monitorare la prossima settimana"

```
CORPO [padding 24px 44px 68px, flex row, gap 18px]

Ogni colonna [flex 1; background #F7F8FA; border-radius 18px; padding 28px 26px; flex column]

  INTESTAZIONE COLONNA
    titolo: "EMOJI Titolo" · 20px weight 900; color: accent-dark della colonna
    sottotitolo: "Dossier [tipo]" · 13px uppercase; letter-spacing 0.08em; margin-bottom 10px
    linea decorativa: 3px; border-radius 2px; margin-bottom 18px

  Ogni ITEM [padding 14px 0; border-bottom 1px #E5E7EB; last-child no border]
    titolo: 17px weight 800 black; margin-bottom 5px
    corpo:  16px weight 400 #4B5563; line-height 1.45
            → struttura: causa → conseguenza
            → <strong> sulla variabile chiave
            → max 2 righe

COLORI COLONNE:
  col-green:  titolo/linea #00C17C  | accent-dark #007A4F
  col-yellow: titolo/linea #F5A623  | accent-dark #92400E
  col-red:    titolo/linea #E8313A  | accent-dark #991B1B
```

---

### SLIDE 7 — CHIUSURA / CTA

```
SFONDO: background accent; display flex; justify-content center; align-items center; flex column

LOGO [flex row; gap 10px; margin-bottom 44px]
  quadrato 48px bianco; border-radius 9px
  <span class="lbs" style="font-size:28px; color:[ACCENT];">A</span>
  "LMA FINANZA" 22px weight 800 color #fff

CARD BIANCA [background #fff; border-radius 24px; padding 52px 64px; text-align center; width 820px]
  "Analisi completa su"  → 12px uppercase letter-spacing 0.12em color muted
  "Alma Finanza"         → 52px weight 900 letter-spacing -0.03em color black
  linea accent           → 56px × 4px; margin 20px auto; border-radius 2px
  "almafinanza.com"      → 20px weight 800 color accent
  "La finanza nazionale e internazionale," → 15px color muted
  "spiegata in italiano. Ogni giorno."     → 15px color muted

FOOTER su sfondo accent:
  dot inattivo: rgba(255,255,255,0.35)
  dot attivo: #fff
  numero pagina: rgba(255,255,255,0.55)
```

---

## STEP 4 — OUTPUT FILES

```
output/
├── linkedin_post.txt     ← testo post pronto da copiare
├── carousel.html         ← sorgente HTML (per debug e riuso)
└── carousel.pdf          ← PDF finale, 7 pagine 1080×1080px
```

---

## REGOLE — NON DEROGABILI

### Contenuto
1. **Ogni slide deve avere testo sufficiente da leggere.** Non solo numeri. Ogni dato ha almeno 1 riga di spiegazione del meccanismo causale.
2. **Niente spazio morto.** Se una card ha meno di 2 righe, aggiungi contesto o riduci il numero di card e aumenta padding.
3. **Spiega sempre il PERCHÉ.** "Buzzi +5,7%" è un dato. "Buzzi +5,7% perché il crollo del WTI riduce i costi" è informazione.
4. **La slide formazione (slide 4) è obbligatoria** in ogni carosello.
5. **La cover deve sempre avere il teaser** "In questo carosello scoprirai" con le pill dei termini.
6. **Il post LinkedIn deve sempre avere** la sezione "💡 Concetto del giorno".

### Design
7. **Sfondo bianco** (`#FFFFFF`) su tutte le slide. Card in `#F7F8FA`. Mai sfondi scuri.
8. **Header = banda colorata** in cima (nero o accent). Niente pattern o sfumature.
9. **Badge = testo scuro su sfondo pastello.** Mai testo colorato su sfondo bianco nudo.
10. **Accent cambia per sezione** (tabella INPUT).
11. **Cover:** il numero più importante va in `color: accent` all'interno del titolo hero.
12. **Slide 7:** sfondo pieno accent — l'unica slide senza sfondo bianco.

### Logo
13. **La A di Alma Finanza è SEMPRE `font-family: 'Lobster', cursive`**, caricato da Google Fonts CDN. Mai `<em>`, mai font di sistema. Uguale al sito almafinanza.com.

### Leggibilità mobile
14. **Testo corpo (slide 2–5) non scende mai sotto 18px.** Su smartphone la scala è ~0.36×: 18px diventa ~6,5px — soglia minima accettabile.
15. **Testo corpo outlook (slide 6) non scende mai sotto 16px.**
16. **Se il testo non entra con i font minimi, taglia le parole — non ridurre il font.**
17. **Percentuali ticker (slide 5) sempre a 32px.** Devono essere leggibili a colpo d'occhio da mobile.

---

## CHIAMATA TIPO

```
Articolo: https://www.almafinanza.com/articolo-[nome].html
```
