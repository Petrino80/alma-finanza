#!/usr/bin/env python3
"""
Aggiunge a un articolo di Alma Finanza la riga di firma e l'immagine di apertura.

Inserisce, subito dopo il filetto colorato che apre il corpo dell'articolo:
  · la firma di testata — la A in Lobster, "Alma Finanza", la data e il tempo di lettura
  · l'immagine generata da genera-immagine-articolo.py

Il tempo di lettura si calcola sul testo reale (200 parole al minuto).
La data diventa "2 ore fa" per le prime 24 ore, poi torna alla data estesa.

Uso:
    python3 aggiungi-firma-immagine.py articolo-xxx.html --data 2026-09-01T18:30
    python3 aggiungi-firma-immagine.py articolo-xxx.html --data 2026-09-01T18:30 --senza-immagine
"""

import argparse
import pathlib
import re
import sys

ANCORA = '<div class="accent-line"></div>'

# Sul sito convivono due impaginazioni di articolo. La firma va inserita
# subito dopo l'apertura del corpo, qualunque sia il template.
ANCORE_ALTERNATIVE = [
    re.compile(r'<article[^>]*class="[^"]*article-content[^"]*"[^>]*>'),
    re.compile(r'<div[^>]*class="[^"]*article-content[^"]*"[^>]*>'),
]

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


def tempo_lettura(html: str) -> int:
    corpo = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", " ", html)
    corpo = re.sub(r"<[^>]+>", " ", corpo)
    parole = len(corpo.split())
    return max(1, round(parole / 200))


def data_estesa(iso: str) -> str:
    mesi = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno",
            "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]
    d = iso.split("T")[0].split("-")
    return f"{int(d[2])} {mesi[int(d[1]) - 1]} {d[0]}"


def blocco(slug: str, iso: str, minuti: int, alt: str, con_immagine: bool) -> str:
    figura = ""
    if con_immagine:
        figura = f"""
            <figure class="-mx-6 md:-mx-10 mb-7">
                <img src="img/articoli/{slug}.jpg" alt="{alt}"
                     class="w-full h-auto block" width="1200" height="630" loading="eager">
            </figure>"""
    return f"""{ANCORA}

            <div class="flex flex-wrap items-center gap-x-2 gap-y-1 text-xs text-gray-400 dark:text-slate-500 mb-6">
                <span class="lobster-font text-xl text-teal-500 leading-none">A</span>
                <span class="font-semibold text-gray-600 dark:text-slate-300">Alma Finanza</span>
                <span aria-hidden="true">·</span>
                <time datetime="{iso}" data-pub>{data_estesa(iso)}</time>
                <span aria-hidden="true">·</span>
                <span>Lettura {minuti} min</span>
            </div>{figura}"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--data", required=True, help="data e ora di pubblicazione, es. 2026-09-01T18:30")
    ap.add_argument("--senza-immagine", action="store_true")
    args = ap.parse_args()

    p = pathlib.Path(args.file)
    if not p.exists():
        sys.exit(f"File non trovato: {p}")

    html = p.read_text(encoding="utf-8")

    if "data-pub" in html:
        sys.exit(f"↷ {p.name}: la firma c'è già, non tocco nulla")

    slug = p.stem
    minuti = tempo_lettura(html)
    titolo = re.search(r"<title>([^<]*)", html)
    alt = (titolo.group(1).split("|")[0].strip() if titolo else slug).replace('"', "'")
    corpo = blocco(slug, args.data, minuti, alt, not args.senza_immagine)

    if ANCORA in html:
        html = html.replace(ANCORA, corpo, 1)
    else:
        # Template senza filetto: inserisci subito dopo l'apertura del corpo articolo
        for rx in ANCORE_ALTERNATIVE:
            m = rx.search(html)
            if m:
                inserto = corpo.replace(ANCORA, "", 1).lstrip("\n")
                html = html[: m.end()] + "\n\n            " + inserto + html[m.end():]
                break
        else:
            sys.exit(f"✗ {p.name}: non trovo un punto di inserimento riconoscibile")
    html = html.replace("</body>", SCRIPT_TEMPO + "\n</body>", 1)

    p.write_text(html, encoding="utf-8")
    print(f"✅ {p.name} — lettura {minuti} min" + ("" if args.senza_immagine else f", immagine img/articoli/{slug}.jpg"))


if __name__ == "__main__":
    main()
