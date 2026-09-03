#!/usr/bin/env python3
"""
Converte la homepage di Alma Finanza alla nuova impaginazione a griglia uniforme.

Approccio conservativo: cambia SOLO il contenuto delle schede e le classi che ne
alteravano la dimensione. Non tocca i contenitori, i separatori di giornata, il
ticker, la ricerca, i widget e gli script: così la struttura della pagina non si rompe.

    python3 converti-home.py            # scrive index-nuovo.html
    python3 converti-home.py --applica  # sostituisce index.html (dopo backup)
"""

import argparse
import pathlib
import re
import shutil

BASE = pathlib.Path(__file__).parent
SRC = BASE / "index.html"

TINTE = {
    "wall street": ("#1e40af", "WALL ST"), "piazza affari": ("#047857", "MILANO"),
    "borsa milano": ("#047857", "MILANO"), "macro": ("#b91c1c", "MACRO"),
    "geopolitica": ("#b91c1c", "MONDO"), "fed": ("#b91c1c", "FED"),
    "tech": ("#6d28d9", "TECH"), "ai": ("#6d28d9", "AI"),
    "crypto": ("#b45309", "CRYPTO"), "commodities": ("#b45309", "MATERIE"),
    "energia": ("#b45309", "ENERGIA"), "corporate": ("#0369a1", "CORPORATE"),
}


def tinta(cat):
    c = cat.lower()
    for k, v in TINTE.items():
        if k in c:
            return v
    return ("#4d5860", "ALMA")


def pulisci(t):
    t = re.sub(r"[\U0001F000-\U0001FAFF☀-➿️]", "", t)
    return re.sub(r"\s+", " ", t).strip(" ·-")


CSS_NUOVO = """
        /* ===== SCHEDE UNIFORMI ===== */
        :root{ --n-surface:#ffffff; --n-sunken:#f6f7f8; --n-ink:#0d1117;
               --n-ink2:#4d5860; --n-ink3:#8a949c; --n-rule:#e6e9eb; --n-rule2:#d2d7da; --n-teal:#0d8f81; }
        .dark{ --n-surface:#111721; --n-sunken:#151c26; --n-ink:#eef2f5;
               --n-ink2:#9fadb8; --n-ink3:#6d7a85; --n-rule:#1e2733; --n-rule2:#2a3542; --n-teal:#2dd4bf; }
        .n-card{display:flex !important;flex-direction:column;height:100%;
          border:1px solid var(--n-rule);border-radius:6px;overflow:hidden;
          background:var(--n-surface);transition:border-color .18s;text-decoration:none}
        .n-card:hover{border-color:var(--n-rule2);transform:none}
        .n-card .n-thumb{width:100%;aspect-ratio:3/2;object-fit:cover;background:var(--n-sunken);flex:none}
        .n-card .n-ph{width:100%;aspect-ratio:3/2;flex:none;display:grid;place-items:center;
          font-family:'Montserrat',sans-serif;font-weight:800;font-size:12.5px;letter-spacing:.1em}
        .n-card .n-body{padding:16px 18px 18px;display:flex;flex-direction:column;gap:9px;flex:1}
        .n-cat{font-size:10.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--n-ink3)}
        .n-card h3{font-family:'Montserrat',sans-serif;font-weight:800;font-size:18px;line-height:1.22;
          letter-spacing:-.015em;color:var(--n-ink);
          display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;
          min-height:calc(1.22em*3);margin:0}
        .n-card:hover h3{color:var(--n-teal)}
        .n-why{font-size:13.5px;line-height:1.5;color:var(--n-ink2);margin:0;
          display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;
          min-height:calc(1.5em*3)}
        .n-why b{color:var(--n-ink);font-weight:700}
        .n-meta{margin-top:auto;padding-top:10px;border-top:1px solid var(--n-rule);
          font-size:11.5px;color:var(--n-ink3);display:flex;gap:8px;font-variant-numeric:tabular-nums}
        /* Qualunque contenitore di schede diventa una griglia uniforme, senza
           dover riscrivere l'HTML storico che ha markup eterogeneo. */
        div:has(> .n-card){
          display:grid !important;
          grid-template-columns:repeat(3,minmax(0,1fr)) !important;
          gap:30px !important;
          align-items:stretch !important;
          float:none !important;
        }
        @media(max-width:900px){div:has(> .n-card){grid-template-columns:repeat(2,minmax(0,1fr)) !important;gap:26px !important}}
        @media(max-width:620px){div:has(> .n-card){grid-template-columns:minmax(0,1fr) !important;gap:24px !important}}
        /* neutralizza le vecchie classi che rendevano alcune schede più larghe */
        .n-card{grid-column:auto !important}
"""


def converti(m):
    blocco = m.group(0)
    href = re.search(r'<a href="([^"]+)"', blocco).group(1)
    tit = re.search(r'<h3[^>]*>([\s\S]*?)</h3>', blocco)
    if not tit:
        return blocco

    foto = re.search(r'src="(img/repertorio/[^"]+)"[^>]*alt="([^"]*)"', blocco)
    cat = re.search(r'cat-tag[^>]*>([\s\S]*?)</span>', blocco)
    som = re.search(r'<p class="text-sm[^"]*"[^>]*>([\s\S]*?)</p>', blocco)
    dat = re.search(r'<span class="text-xs text-gray-300[^"]*">([^<]*)</span>', blocco)

    categoria = pulisci(cat.group(1)) if cat else "Alma Finanza"
    titolo = re.sub(r"\s+", " ", tit.group(1)).strip()
    sommario = re.sub(r"\s+", " ", som.group(1)).strip() if som else ""
    data = dat.group(1).strip() if dat else ""

    if foto:
        media = (f'<img class="n-thumb" src="{foto.group(1)}" alt="{foto.group(2)}" '
                 f'loading="lazy" width="1200" height="800">')
    else:
        col, sigla = tinta(categoria)
        media = f'<div class="n-ph" style="background:{col}14;color:{col}">{sigla}</div>'

    return (f'<a href="{href}" class="n-card group">\n'
            f'                {media}\n'
            f'                <div class="n-body">\n'
            f'                    <div class="n-cat">{categoria}</div>\n'
            f'                    <h3>{titolo}</h3>\n'
            f'                    <p class="n-why">{sommario}</p>\n'
            f'                    <div class="n-meta"><span>{data}</span></div>\n'
            f'                </div>\n'
            f'            </a>')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--applica", action="store_true")
    args = ap.parse_args()

    s = SRC.read_text(encoding="utf-8")
    prima = len(re.findall(r'<a href="articolo-[^"]+" class="theme-card', s))
    div_prima = s.count("<div"), s.count("</div>")

    if "n-card" not in s:
        i = s.rfind("</style>")
        s = s[:i] + CSS_NUOVO + "\n    " + s[i:]

    # Solo le schede articolo. I contenitori, i separatori e i widget restano intatti.
    s = re.sub(r'<a href="articolo-[^"]+" class="theme-card[\s\S]*?</a>', converti, s)

    # L'hero con il riquadro colorato dei numeri non esiste più: l'articolo in evidenza
    # compare come prima scheda della griglia, così tutte le voci hanno la stessa misura.
    hero = re.search(r'\s*<!-- Hero -->[\s\S]*?<!-- Quiz Teaser Card -->', s)
    if hero:
        s = s[:hero.start()] + "\n\n        <!-- Quiz Teaser Card -->" + s[hero.end():]
        print("  hero rimosso: si entra direttamente nella griglia")
    else:
        print("  ⚠️  hero non trovato: controlla il markup")

    dopo = len(re.findall(r'class="n-card', s))
    div_dopo = s.count("<div"), s.count("</div>")

    out = SRC if args.applica else BASE / "index-nuovo.html"
    if args.applica:
        shutil.copy(SRC, BASE / "index-backup.html")
    out.write_text(s, encoding="utf-8")

    print(f"  schede trovate:    {prima}")
    print(f"  schede convertite: {dopo}")
    print(f"  <div> prima:  {div_prima[0]} aperti / {div_prima[1]} chiusi")
    print(f"  <div> dopo:   {div_dopo[0]} aperti / {div_dopo[1]} chiusi")
    print(f"  bilanciamento {'✅ ok' if div_dopo[0] == div_dopo[1] else '❌ ROTTO'}")
    print(f"  scritto: {out.name}")


if __name__ == "__main__":
    main()
