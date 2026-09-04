#!/usr/bin/env python3
"""
Mette una fotografia in apertura di un articolo di Alma Finanza.

Usa la libreria di repertorio in img/repertorio/, tutte foto a licenza libera
verificate su Wikimedia Commons. Il credito fotografico viene stampato
automaticamente sotto l'immagine, come richiedono le licenze CC BY e CC BY-SA.

    # elenca le foto disponibili
    python3 applica-foto-articolo.py --elenco

    # applica una foto a un articolo
    python3 applica-foto-articolo.py articolo-xxx.html --foto piazza-affari --data 2026-09-02T17:50

    # se la firma c'è già (messa da aggiungi-firma-immagine.py) sostituisce
    # l'immagine generata con la fotografia
    python3 applica-foto-articolo.py articolo-xxx.html --foto nyse --sostituisci

Se non passi --foto, lo script prova a indovinare il tema dal titolo dell'articolo.
"""

import argparse
import json
import pathlib
import re
import sys

BASE = pathlib.Path(__file__).parent
LIB = BASE / "img" / "repertorio"
ANCORA = '<div class="accent-line"></div>'
ANCORE_ALTERNATIVE = [
    re.compile(r'<article[^>]*class="[^"]*article-content[^"]*"[^>]*>'),
    re.compile(r'<div[^>]*class="[^"]*article-content[^"]*"[^>]*>'),
    re.compile(r'<main[^>]*class="[^"]*article-content[^"]*"[^>]*>'),
]


def carica_crediti():
    with open(LIB / "crediti.json", encoding="utf-8") as fh:
        return {k: v for k, v in json.load(fh).items() if not k.startswith("_")}


def indovina(titolo: str, crediti: dict):
    t = titolo.lower()
    punteggi = {}
    for chiave, meta in crediti.items():
        punteggi[chiave] = sum(1 for tema in meta["temi"] if tema in t)
    migliore = max(punteggi, key=punteggi.get)
    return migliore if punteggi[migliore] > 0 else None


def tempo_lettura(html: str) -> int:
    corpo = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", " ", html)
    corpo = re.sub(r"<[^>]+>", " ", corpo)
    return max(1, round(len(corpo.split()) / 200))


def data_estesa(iso: str) -> str:
    mesi = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno",
            "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]
    d = iso.split("T")[0].split("-")
    return f"{int(d[2])} {mesi[int(d[1]) - 1]} {d[0]}"


def figura(meta: dict) -> str:
    return f"""
            <figure class="-mx-6 md:-mx-10 mb-7">
                <img src="img/repertorio/{meta['file']}" alt="{meta['soggetto']}"
                     class="w-full block object-cover" style="aspect-ratio:1200/560" loading="eager">
                <figcaption class="px-6 md:px-10 pt-2 text-xs text-gray-400 dark:text-slate-500">
                    {meta['soggetto']} · Foto: {meta['autore']}, {meta['licenza']}
                </figcaption>
            </figure>"""


def firma(iso: str, minuti: int) -> str:
    return f"""
            <div class="flex flex-wrap items-center gap-x-2 gap-y-1 text-xs text-gray-400 dark:text-slate-500 mb-6">
                <span class="lobster-font text-xl text-teal-500 leading-none">A</span>
                <span class="font-semibold text-gray-600 dark:text-slate-300">Alma Finanza</span>
                <span aria-hidden="true">·</span>
                <time datetime="{iso}" data-pub>{data_estesa(iso)}</time>
                <span aria-hidden="true">·</span>
                <span>Lettura {minuti} min</span>
            </div>"""


SCRIPT_TEMPO = """
<script>
(function(){
  document.querySelectorAll('time[data-pub]').forEach(function(el){
    var d = new Date(el.getAttribute('datetime'));
    if (isNaN(d)) return;
    var min = Math.floor((Date.now() - d.getTime())/60000);
    if (min < 1) { el.textContent = 'adesso'; }
    else if (min < 60) { el.textContent = min + (min===1?' minuto fa':' minuti fa'); }
    else if (min < 1440) { var h = Math.floor(min/60); el.textContent = h + (h===1?' ora fa':' ore fa'); }
  });
})();
</script>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--foto", help="chiave della foto in crediti.json")
    ap.add_argument("--data", help="data e ora di pubblicazione, es. 2026-09-02T17:50")
    ap.add_argument("--sostituisci", action="store_true",
                    help="rimpiazza un'immagine generata già presente")
    ap.add_argument("--elenco", action="store_true", help="mostra le foto disponibili")
    ap.add_argument("--forza", action="store_true",
                    help="usa la foto anche se è già presente in un altro articolo")
    args = ap.parse_args()

    crediti = carica_crediti()

    if args.elenco:
        print("\nFoto disponibili in img/repertorio/:\n")
        for k, m in crediti.items():
            print(f"  {k:<16} {m['soggetto']}")
            print(f"  {'':<16} {m['autore']} · {m['licenza']}")
            print(f"  {'':<16} temi: {', '.join(m['temi'])}\n")
        return

    if not args.file:
        sys.exit("Manca il file dell'articolo (oppure usa --elenco)")

    p = pathlib.Path(args.file)
    if not p.exists():
        sys.exit(f"File non trovato: {p}")
    html = p.read_text(encoding="utf-8")

    titolo = re.search(r"<title>([^<]*)", html)
    titolo = titolo.group(1) if titolo else p.stem

    chiave = args.foto or indovina(titolo, crediti)
    if not chiave:
        sys.exit(f"✗ {p.name}: non riesco a scegliere una foto dal titolo. Indica --foto (vedi --elenco)")
    if chiave not in crediti:
        sys.exit(f"✗ foto sconosciuta: {chiave}. Vedi --elenco")
    meta = crediti[chiave]

    if not (LIB / meta["file"]).exists():
        sys.exit(f"✗ manca il file {LIB / meta['file']}")

    # REGOLA: mai la stessa foto su due articoli diversi.
    gia_usata = []
    for altro in sorted(BASE.glob("articolo-*.html")):
        if altro.name == p.name:
            continue
        try:
            if f'img/repertorio/{meta["file"]}' in altro.read_text(encoding="utf-8"):
                gia_usata.append(altro.name)
        except Exception:
            pass
    if gia_usata and not args.forza:
        liberi = [k for k, m in crediti.items()
                  if set(m["temi"]) & set(meta["temi"])
                  and not any(f'img/repertorio/{m["file"]}' in a.read_text(encoding="utf-8", errors="ignore")
                              for a in BASE.glob("articolo-*.html"))]
        msg = [f"✗ la foto '{chiave}' è già usata in: {', '.join(gia_usata[:3])}",
               "  Regola: mai la stessa foto su due articoli."]
        if liberi:
            msg.append(f"  Alternative libere sullo stesso tema: {', '.join(liberi)}")
        else:
            msg.append("  Nessuna alternativa libera sul tema: cercane una nuova su Wikimedia Commons,")
            msg.append("  scaricala in img/repertorio/ e registrala in crediti.json.")
        msg.append("  (--forza per procedere comunque)")
        sys.exit("\n".join(msg))

    # Caso 1: c'è già una figura di apertura (immagine generata o altra foto) → sostituiscila.
    # Cerca sia img/articoli/ (grafiche) sia img/repertorio/ (fotografie), così non si
    # finisce mai con due immagini nello stesso articolo.
    esistente = re.search(
        r'<figure[^>]*>\s*<img src="img/(?:articoli|repertorio)/[^"]+"[\s\S]*?</figure>', html)
    if esistente:
        if not args.sostituisci:
            sys.exit(f"↷ {p.name}: c'è già un'immagine di apertura. Usa --sostituisci per rimpiazzarla")
        html = html[:esistente.start()] + figura(meta).strip() + html[esistente.end():]
        p.write_text(html, encoding="utf-8")
        print(f"✅ {p.name} — foto '{chiave}' al posto dell'immagine precedente")
        return

    # Caso 2: nessuna immagine, inserisci firma (se manca) e foto
    if not args.data and "data-pub" not in html:
        sys.exit("Serve --data per scrivere la firma")

    blocco = ("" if "data-pub" in html else firma(args.data, tempo_lettura(html))) + figura(meta)

    if ANCORA in html:
        html = html.replace(ANCORA, ANCORA + blocco, 1)
    else:
        for rx in ANCORE_ALTERNATIVE:
            m = rx.search(html)
            if m:
                html = html[: m.end()] + blocco + html[m.end():]
                break
        else:
            sys.exit(f"✗ {p.name}: non trovo un punto di inserimento riconoscibile")

    if "data-pub" in html and "data-pub'" not in html and SCRIPT_TEMPO.strip() not in html:
        html = html.replace("</body>", SCRIPT_TEMPO + "\n</body>", 1)

    p.write_text(html, encoding="utf-8")
    print(f"✅ {p.name} — foto '{chiave}' ({meta['autore']}, {meta['licenza']})")


if __name__ == "__main__":
    main()
