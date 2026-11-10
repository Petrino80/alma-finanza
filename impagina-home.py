#!/usr/bin/env python3
"""
Impagina la homepage di Alma Finanza e le pagine archivio con la disposizione del novembre 2026:
primo piano, ultime notizie con filtri, ultime 10 giornate in homepage, il resto in archivio mensile.

Non cambia il DESIGN delle schede (.n-card): decide solo dove stanno. È rieseguibile quante volte
serve: rilegge le giornate da index.html e dalle pagine archivio-AAAA-MM.html e riscrive tutto.

USO QUOTIDIANO
  1. In index.html, subito sotto il commento <!-- NUOVO-GIORNO -->, incolla il blocco del giorno
     (una scheda per articolo, la più importante per prima):

         <!-- GIORNO 2026-11-11 | Mercoledì 11 Novembre 2026 -->
         <a href="articolo-....html" class="n-card group"> ... </a>
         <!-- /GIORNO -->

  2. python3 impagina-home.py                     # scrive index-nuovo.html, per controllare
     python3 impagina-home.py --applica           # riscrive index.html, archivi e sitemap
     python3 impagina-home.py --applica --parola "ROTE|rendimento sul patrimonio tangibile"

Lo script porta in primo piano la giornata più recente, fa scendere le altre, sposta in archivio
quelle oltre la decima, ricalcola il conteggio degli articoli e corregge da solo il giorno della
settimana nelle intestazioni (lo ricava dalla data).
"""

import argparse
import datetime
import html
import pathlib
import re
import shutil
import sys
import xml.dom.minidom

BASE = pathlib.Path(__file__).parent
SRC = BASE / "index.html"
SITO = "https://www.almafinanza.com/"
GIORNATE_IN_HOME = 10

GIORNI = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
MESI = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto",
        "Settembre", "Ottobre", "Novembre", "Dicembre"]

SCHEDA = re.compile(r'<a\s[^>]*class="[^"]*\bn-card\b[^"]*"[^>]*>[\s\S]*?</a>')
BLOCCO = re.compile(r'<!-- (PRIMO-PIANO|GIORNO) (\d{4}-\d{2}-\d{2}) \| ([^>]*?) -->([\s\S]*?)<!-- /\1 -->')
INIZIO, FINE = "<!-- DISPOSIZIONE-2026-11", "<!-- /DISPOSIZIONE-2026-11 -->"
FILTRI = [("tutte", "Tutte"), ("wall", "Wall Street"), ("milano", "Piazza Affari"), ("macro", "Macro"),
          ("tech", "Tech / AI"), ("commod", "Commodities"), ("corp", "Aziende")]


# ---------------------------------------------------------------- date e titoli

def titolo_da_data(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{GIORNI[d.weekday()]} {d.day} {MESI[d.month - 1]} {d.year}"


def titolo_normale(titolo):
    """True se il titolo è una data semplice («Lunedì, 10 Novembre 2026»): in quel caso si riscrive dalla data."""
    t = html.unescape(titolo).replace(",", " ")
    return re.fullmatch(r"\s*(?:[A-Za-zìÌ]+\s+)?\d{1,2}\s+[A-Za-z]+(?:\s+\d{4})?\s*", t) is not None


def data_da_intestazione(testo):
    """«Giovedì 17 Aprile» → 2026-04-17. Per gli intervalli («24-25 Febbraio») vale l'ultimo giorno."""
    t = html.unescape(testo)
    mese = next((i for i, m in enumerate(MESI) if m.lower() in t.lower()), None)
    numeri = [int(n) for n in re.findall(r"(?<!\d)(\d{1,2})(?!\d)", t)]
    if mese is None or not numeri:
        return None
    anno = re.search(r"20\d\d", t)
    return datetime.date(int(anno.group(0)) if anno else 2026, mese + 1, max(numeri)).isoformat()


# ---------------------------------------------------------------- schede

def categoria(testo):
    """Chiave del filtro a partire dall'etichetta della scheda. Conta la prima parola chiave che compare."""
    t = " " + html.unescape(testo).lower() + " "
    chiavi = [
        ("milano", ("piazza", "ftse", "borsa mil", "italia", "titoli di stato", "btp")),
        ("wall", ("wall", "nasdaq", "dow", "weekly", "outlook", "earnings")),
        ("tech", ("tech", " ai ", "semicond", "ipo")),
        ("macro", ("macro", "fed", "geopol", "bce", "europa", "asia", "dazi", "finanza/")),
        ("commod", ("commod", "crypto", "oro", "petrol", "energia")),
    ]
    trovate = [(t.find(p), k) for k, parole in chiavi for p in parole if p in t]
    return min(trovate)[1] if trovate else "corp"


def prepara(scheda):
    """Aggiunge data-cat se manca e toglie le misure scritte a mano; il resto del markup non si tocca."""
    scheda = scheda.strip()
    apertura = scheda[:scheda.index(">") + 1]
    # la larghezza la decide la regola adattiva: via le vecchie classi col-span e le altezze forzate sulla foto
    pulita = re.sub(r"\s+(?:(?:sm|md|lg):)?col-span-(?:\d+|full)", "", apertura)
    scheda = pulita + scheda[len(apertura):]
    scheda = re.sub(r'(<img class="n-thumb"[^>]*?)\sstyle="[^"]*max-height[^"]*"', r"\1", scheda, count=1)
    apertura = pulita
    if "data-cat=" in apertura:
        return scheda
    cat = re.search(r'class="n-cat"[^>]*>([\s\S]*?)</div>', scheda)
    chiave = categoria(re.sub(r"<[^>]+>", "", cat.group(1)) if cat else "")
    return (apertura[:-1] + f' data-cat="{chiave}">' + scheda[len(apertura):]).strip()


def href(scheda):
    return re.search(r'href="([^"]+)"', scheda).group(1)


# ---------------------------------------------------------------- lettura delle giornate

def leggi_storico(pagina):
    """Homepage non ancora convertita: intestazioni <h2> e schede in sequenza, markup eterogeneo."""
    zona = pagina[pagina.index("<main"):pagina.index("<!-- Mission Section -->")]
    gruppi, ultima = [], None
    for m in re.finditer(r"<h2[^>]*>([\s\S]*?)</h2>|" + SCHEDA.pattern, zona):
        if m.group(0).startswith("<h2"):
            testo = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
            data = data_da_intestazione(testo)
            if "Fine 14 Febbraio" in testo:                 # coda storica: tutto ciò che precede il 14 febbraio
                data, testo = "2026-02-13", "Prima del 14 Febbraio 2026"
            elif data is None:                              # intestazione senza data: si sistema a fine lettura
                data = ultima
            elif not titolo_normale(testo) and not re.search(r"20\d\d", testo):
                testo += " 2026"
            ultima = data
            if gruppi and gruppi[-1]["data"] == data and not gruppi[-1]["schede"]:
                gruppi.pop()                                # intestazione doppia per la stessa giornata
            gruppi.append({"data": data, "titolo": testo, "schede": [], "senza_data": data_da_intestazione(testo) is None})
        else:
            gruppi[-1]["schede"].append(m.group(0))
    gruppi = [g for g in gruppi if g["schede"]]
    for i, g in enumerate(gruppi[:-1]):                     # una rubrica senza data prende quella della giornata successiva
        if g["senza_data"] and "Prima del" not in g["titolo"]:
            g["data"] = gruppi[i + 1]["data"]
    return gruppi


def leggi_nuovo(pagine):
    """Homepage già convertita: blocchi <!-- GIORNO ... --> in index.html e nelle pagine archivio."""
    gruppi = []
    for testo in pagine:
        for m in BLOCCO.finditer(testo):
            schede = SCHEDA.findall(m.group(4))
            if schede:
                gruppi.append({"data": m.group(2), "titolo": html.unescape(m.group(3)).strip(), "schede": schede})
    gruppi.sort(key=lambda g: g["data"], reverse=True)      # stabile: a parità di data resta l'ordine di lettura
    return gruppi


def ripulisci(gruppi):
    """Titoli uniformi, niente schede doppie, data-cat su ogni scheda."""
    viste, puliti = set(), []
    for g in gruppi:
        schede = []
        for s in g["schede"]:
            if href(s) not in viste:
                viste.add(href(s))
                schede.append(prepara(s))
        if not schede:
            continue
        titolo = titolo_da_data(g["data"]) if titolo_normale(g["titolo"]) else g["titolo"]
        if puliti and puliti[-1]["data"] == g["data"] and puliti[-1]["titolo"] == titolo:
            puliti[-1]["schede"] += schede                  # stessa giornata letta in due blocchi
        else:
            puliti.append({"data": g["data"], "titolo": titolo, "schede": schede})
    return puliti


# ---------------------------------------------------------------- markup

def rientra(schede, spazi):
    return "\n".join(" " * spazi + s for s in schede)


def sezione(g, ident):
    n = len(g["schede"])
    return f'''        <!-- GIORNO {g["data"]} | {g["titolo"]} -->
        <section class="giorno" id="{ident}" data-giorno="{g["data"]}">
            <div class="giorno-testa flex items-center gap-3 mt-6 mb-4">
                <div class="w-10 h-0.5 rounded-full bg-gray-200 dark:bg-slate-700/40"></div>
                <h2 class="text-sm font-bold montserrat-font text-gray-400 dark:text-slate-600 uppercase tracking-wider">{g["titolo"]}</h2>
                <span class="giorno-n">{n} articol{"o" if n == 1 else "i"}</span>
                <div class="flex-1 h-0.5 rounded-full bg-gray-100 dark:bg-slate-800/20"></div>
            </div>
            <div class="giorno-griglia">
{rientra(g["schede"], 16)}
            </div>
        </section>
        <!-- /GIORNO -->
'''


def sezioni(gruppi):
    usati, out = {}, []
    for g in gruppi:
        usati[g["data"]] = usati.get(g["data"], 0) + 1
        ident = "g-" + g["data"] + ("" if usati[g["data"]] == 1 else f"-{usati[g['data']]}")
        out.append(sezione(g, ident))
    return out


def primo_piano(g):
    resto = ""
    if len(g["schede"]) > 3:
        resto = f'''
        <div class="giorno-griglia pp-resto">
{rientra(g["schede"][3:], 12)}
        </div>'''
    return f'''        <!-- PRIMO-PIANO {g["data"]} | {g["titolo"]} -->
        <div class="pp-occhiello"><b>In primo piano</b> · {g["titolo"]}</div>
        <div class="primo-piano">
{rientra(g["schede"][:3], 12)}
        </div>{resto}
        <!-- /PRIMO-PIANO -->
'''


def nome_mese(chiave):
    return f"{MESI[int(chiave[5:7]) - 1]} {chiave[:4]}"


def file_mese(chiave):
    return f"archivio-{chiave}.html"


def fascia(parola):
    termine, traduzione = parola
    return f'''        <!-- Fascia quiz + parola del giorno -->
        <div class="fascia">
            <a class="fascia-quiz" href="quiz.html">
                <span class="fq-ico">🎯</span>
                <span class="fq-txt"><b>Quiz del mese</b><span>10 domande su mercati, indici, IPO e strumenti. Chi fa 10/10 partecipa all'estrazione del premio.</span></span>
                <span class="fq-btn">Inizia →</span>
            </a>
            <a class="fascia-parola" href="glossario.html">
                <span class="fp-lbl">Parola del giorno</span>
                <!-- PAROLA --><b>{html.escape(termine)}</b><span class="fp-it">{html.escape(traduzione)}</span><!-- /PAROLA -->
                <span class="fp-go">Apri il glossario →</span>
            </a>
        </div>
'''


def blocco_archivio(totale, mesi, primo_mese, bersaglio):
    pillole = "".join(f'<a href="{file_mese(m)}">{MESI[int(m[5:7]) - 1]}</a>' for m in mesi[:4])
    return f'''        <!-- Blocco archivio -->
        <div class="arch">
            <div><h2>Archivio</h2><p>{totale} articoli dal {nome_mese(primo_mese).lower()}, ordinati per giorno.</p></div>
            <div class="arch-mesi">{pillole}<a href="archivio.html" title="Tutti i mesi">…</a></div>
            <a class="arch-btn" href="{bersaglio}">Mostra i giorni precedenti</a>
        </div>
'''


def corpo_home(gruppi, parola):
    in_home, in_archivio = gruppi[:GIORNATE_IN_HOME], gruppi[GIORNATE_IN_HOME:]
    mesi = sorted({g["data"][:7] for g in in_archivio}, reverse=True)
    totale = sum(len(g["schede"]) for g in gruppi)
    # si mostrano solo i filtri che hanno almeno un articolo nelle giornate in homepage: mai un filtro che svuota la pagina
    presenti = {re.search(r'data-cat="(\w+)"', sch).group(1) for g in in_home[1:] for sch in g["schede"]}
    bottoni = "".join(
        '<button type="button" data-f="%s"%s>%s</button>' % (k, ' class="on"' if k == "tutte" else "", e)
        for k, e in FILTRI if k == "tutte" or k in presenti)
    blocchi = sezioni(in_home[1:])
    prima, altre = "\n".join(blocchi[:1]), "\n".join(blocchi[1:])
    bersaglio = file_mese(in_archivio[0]["data"][:7]) + "#g-" + in_archivio[0]["data"] if in_archivio else "archivio.html"
    return f'''{INIZIO}: primo piano, ultime notizie con filtri, {GIORNATE_IN_HOME} giornate, archivio mensile.
             Pagina generata da impagina-home.py: per aggiungere un giorno incolla il blocco qui sotto ed esegui lo script. -->
        <!-- NUOVO-GIORNO -->

{primo_piano(in_home[0])}
        <div class="un-bar">
            <h2>Ultime notizie</h2>
            <div class="filtri">{bottoni}</div>
        </div>

{prima}
{fascia(parola)}
{altre}
{blocco_archivio(totale, mesi, min(g["data"][:7] for g in gruppi), bersaglio) if mesi else ""}
        {FINE}

'''


# ---------------------------------------------------------------- stile e script della disposizione

STORICO = "div:has(> .n-card):not(.giorno-griglia):not(.primo-piano)"
TUTTA = ".giorno-griglia:not(.filtrata) > .n-card:first-child:nth-last-child(3n+1), .giorno-griglia.filtrata > .n-card.ad-tutta, .primo-piano > .n-card:only-child"
META = (".giorno-griglia:not(.filtrata) > .n-card:first-child:nth-last-child(3n+2), "
        ".giorno-griglia:not(.filtrata) > .n-card:first-child:nth-last-child(3n+2) + .n-card, "
        ".giorno-griglia.filtrata > .n-card.ad-meta")


def con(selettori, coda):
    """Applica lo stesso discendente a ogni selettore di una lista: «a, b» + « h3» → «a h3, b h3»."""
    return ", ".join(s.strip() + coda for s in selettori.split(","))


CSS = f'''        /* ===== DISPOSIZIONE 2026-11 (generata da impagina-home.py: non modificare a mano) ===== */
        /* contenitori storici di schede, fuori dalla nuova disposizione: griglia uniforme come prima */
        {STORICO}{{display:grid !important;grid-template-columns:repeat(3,minmax(0,1fr)) !important;gap:30px !important;align-items:stretch !important;float:none !important}}
        {STORICO} > .n-card{{grid-column:auto !important}}
        @media(max-width:900px){{{STORICO}{{grid-template-columns:repeat(2,minmax(0,1fr)) !important;gap:26px !important}}}}
        @media(max-width:620px){{{STORICO}{{grid-template-columns:minmax(0,1fr) !important;gap:24px !important}}}}
        .n-card[hidden]{{display:none !important}}

        /* primo piano: la notizia principale e due a fianco */
        .pp-occhiello{{font-size:11.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--n-ink3);margin:22px 0 12px}}
        .pp-occhiello b{{color:var(--n-teal)}}
        .primo-piano{{display:grid;grid-template-columns:minmax(0,1.55fr) minmax(0,1fr);gap:22px}}
        .primo-piano > .n-card:first-child{{grid-row:1 / span 2}}
        .primo-piano > .n-card:first-child .n-thumb, .primo-piano > .n-card:first-child .n-ph{{aspect-ratio:2/1}}
        .primo-piano > .n-card:first-child .n-body{{padding:20px 22px 20px}}
        .primo-piano > .n-card:first-child h3{{font-size:26px;line-height:1.18;min-height:0;-webkit-line-clamp:4}}
        .primo-piano > .n-card:first-child .n-why{{font-size:15px;min-height:0;-webkit-line-clamp:4}}
        .primo-piano > .n-card:not(:first-child) .n-thumb, .primo-piano > .n-card:not(:first-child) .n-ph{{aspect-ratio:16/6}}
        .primo-piano > .n-card:not(:first-child) .n-body{{padding:13px 16px 14px;gap:7px}}
        .primo-piano > .n-card:not(:first-child) h3{{font-size:15.5px;line-height:1.25;min-height:0}}
        .primo-piano > .n-card:not(:first-child) .n-why{{display:none}}
        .primo-piano > .n-card:nth-child(2):last-child{{grid-row:1 / span 2}}
        .primo-piano > .n-card:nth-child(2):last-child .n-thumb, .primo-piano > .n-card:nth-child(2):last-child .n-ph{{aspect-ratio:3/2}}
        .primo-piano > .n-card:only-child{{grid-column:1 / -1}}
        .pp-resto{{margin-top:22px}}

        /* ultime notizie e filtri */
        .un-bar{{display:flex;align-items:center;gap:16px;flex-wrap:wrap;margin:40px 0 2px}}
        .un-bar h2{{font-family:'Montserrat',sans-serif;font-weight:800;font-size:22px;letter-spacing:-.01em;color:var(--n-ink);margin-right:auto}}
        .filtri{{display:flex;gap:8px;flex-wrap:wrap}}
        .filtri button{{font:600 13px 'Inter',sans-serif;color:var(--n-ink2);background:var(--n-surface);border:1px solid var(--n-rule);padding:7px 13px;border-radius:6px;cursor:pointer;transition:border-color .15s,color .15s}}
        .filtri button:hover{{border-color:var(--n-ink3);color:var(--n-ink)}}
        .filtri button.on{{background:var(--n-ink);color:var(--n-surface);border-color:var(--n-ink)}}
        .giorno-n{{font-size:11px;font-weight:600;color:var(--n-ink3);white-space:nowrap}}
        .giorno[hidden]{{display:none}}

        /* giornate: gli articoli in più rispetto ai multipli di tre si allargano nella prima riga */
        .giorno-griglia{{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:30px;align-items:stretch}}
        .giorno-griglia > .n-card{{grid-column:span 2}}
        @media(min-width:901px){{
          {META}{{grid-column:span 3}}
          {con(META, " .n-thumb")}, {con(META, " .n-ph")}{{aspect-ratio:16/9}}
          {TUTTA}{{grid-column:1 / -1;flex-direction:row;height:340px}}
          {con(TUTTA, " .n-thumb")}, {con(TUTTA, " .n-ph")}{{width:52%;height:100%;aspect-ratio:auto}}
          {con(TUTTA, " .n-body")}{{justify-content:center;padding:26px 30px 24px}}
          {con(TUTTA, " h3")}{{font-size:23px;line-height:1.2;min-height:0}}
          {con(TUTTA, " .n-why")}{{font-size:14.5px;min-height:0;-webkit-line-clamp:4}}
          {con(TUTTA, " .n-meta")}{{margin-top:14px}}
        }}
        @media(max-width:900px){{
          .primo-piano{{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}}
          .primo-piano > .n-card:first-child{{grid-column:1 / -1;grid-row:auto}}
          .primo-piano > .n-card:nth-child(2):last-child{{grid-column:1 / -1;grid-row:auto}}
          .primo-piano > .n-card:first-child h3{{font-size:22px}}
          .giorno-griglia{{grid-template-columns:repeat(2,minmax(0,1fr));gap:26px}}
          .giorno-griglia > .n-card{{grid-column:auto}}
          .giorno-griglia:not(.filtrata) > .n-card:first-child:nth-last-child(odd), .giorno-griglia.filtrata > .n-card.ad-dispari{{grid-column:1 / -1}}
        }}
        @media(max-width:620px){{
          .primo-piano{{grid-template-columns:minmax(0,1fr)}}
          .primo-piano > .n-card:not(:first-child) .n-thumb, .primo-piano > .n-card:not(:first-child) .n-ph{{aspect-ratio:3/2}}
          .giorno-griglia{{grid-template-columns:minmax(0,1fr);gap:24px}}
          .un-bar{{margin-top:30px}}
          .filtri{{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;margin:0 -16px;padding:0 16px;max-width:100vw}}
          .filtri button{{flex-shrink:0}}
        }}

        /* fascia quiz + parola del giorno */
        .fascia{{display:grid;grid-template-columns:minmax(0,2fr) minmax(0,1fr);gap:22px;margin:30px 0 8px}}
        .fascia-quiz{{display:flex;align-items:center;gap:16px;padding:18px 22px;border-radius:8px;color:#fff;background:linear-gradient(120deg,#0f766e,#14b8a6 70%,#2dd4bf);text-decoration:none}}
        .fq-ico{{font-size:32px}}
        .fq-txt{{display:flex;flex-direction:column;gap:3px;margin-right:auto;font-size:13.5px;color:rgba(255,255,255,.88)}}
        .fq-txt b{{font-family:'Montserrat',sans-serif;font-size:18px;font-weight:800;color:#fff}}
        .fq-btn{{font-size:13.5px;font-weight:700;background:#fff;color:#0f766e;padding:10px 18px;border-radius:999px;white-space:nowrap}}
        .fascia-parola{{display:flex;flex-direction:column;justify-content:center;gap:2px;padding:16px 20px;border-radius:8px;background:#f0fdfa;border:1px solid #99e0d6;text-decoration:none}}
        .dark .fascia-parola{{background:rgba(20,184,166,.10);border-color:rgba(45,212,191,.28)}}
        .fp-lbl{{font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--n-teal)}}
        .fascia-parola b{{font-family:'Montserrat',sans-serif;font-size:21px;font-weight:800;color:var(--n-ink)}}
        .fp-it{{font-size:13px;color:var(--n-ink2)}}
        .fp-go{{font-size:12.5px;font-weight:600;color:var(--n-teal);margin-top:6px}}
        @media(max-width:620px){{.fascia{{grid-template-columns:minmax(0,1fr);gap:14px}} .fq-txt span{{display:none}}}}

        /* blocco archivio e pagine archivio */
        .arch{{margin:44px 0 24px;padding:24px 26px;background:var(--n-surface);border:1px solid var(--n-rule);border-radius:8px;display:flex;align-items:center;gap:18px;flex-wrap:wrap}}
        .arch h2{{font-family:'Montserrat',sans-serif;font-size:19px;font-weight:800;color:var(--n-ink)}}
        .arch p{{font-size:13.5px;color:var(--n-ink2);margin-top:3px}}
        .arch-mesi{{display:flex;gap:8px;flex-wrap:wrap}}
        .arch > .arch-mesi{{margin-left:auto}}
        .arch-mesi a{{font-size:13px;font-weight:600;color:var(--n-ink2);background:var(--n-sunken);padding:8px 15px;border-radius:999px;text-decoration:none}}
        .arch-mesi a:hover, .arch-mesi a.qui{{background:var(--n-ink);color:var(--n-surface)}}
        .arch-btn{{font-size:13.5px;font-weight:700;background:var(--n-ink);color:var(--n-surface);padding:11px 20px;border-radius:999px;text-decoration:none;white-space:nowrap}}
        .arch-pista{{font-size:12.5px;color:var(--n-ink3);margin:22px 0 10px}}
        .arch-pista a{{color:var(--n-teal);font-weight:600;text-decoration:none}}
        .arch-titolo{{font-family:'Montserrat',sans-serif;font-size:30px;font-weight:800;letter-spacing:-.015em;color:var(--n-ink)}}
        .arch-sotto{{font-size:14px;color:var(--n-ink2);margin:4px 0 18px}}
        .arch-indice{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;margin:8px 0 40px}}
        .arch-indice a{{display:block;padding:20px 22px;border:1px solid var(--n-rule);border-radius:6px;background:var(--n-surface);text-decoration:none;transition:border-color .18s}}
        .arch-indice a:hover{{border-color:var(--n-rule2)}}
        .arch-indice b{{display:block;font-family:'Montserrat',sans-serif;font-size:18px;font-weight:800;color:var(--n-ink)}}
        .arch-indice span{{font-size:13px;color:var(--n-ink2)}}
        .arch-piede{{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;margin:36px 0 30px}}
        @media(max-width:900px){{.arch-indice{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
        @media(max-width:620px){{.arch{{padding:20px}} .arch > .arch-mesi{{margin-left:0}} .arch-indice{{grid-template-columns:minmax(0,1fr)}} .arch-titolo{{font-size:25px}}}}
        /* ===== /DISPOSIZIONE 2026-11 ===== */
'''

JS = '''    <!-- JS-DISPOSIZIONE: filtri per categoria (generato da impagina-home.py) -->
    <script>
    (function(){
        var bottoni=document.querySelectorAll('.filtri button');
        if(!bottoni.length)return;
        function filtra(f){
            document.querySelectorAll('.giorno').forEach(function(g){
                var griglia=g.querySelector('.giorno-griglia'),visibili=[];
                griglia.querySelectorAll('.n-card').forEach(function(c){
                    var ok=f==='tutte'||c.getAttribute('data-cat')===f;
                    c.hidden=!ok;c.classList.remove('ad-tutta','ad-meta','ad-dispari');
                    if(ok)visibili.push(c);
                });
                // la riga si ricalcola sulle sole schede visibili: nessuno spazio vuoto nemmeno a filtro attivo
                griglia.classList.toggle('filtrata',f!=='tutte');
                if(f!=='tutte'&&visibili.length){
                    if(visibili.length%3===1)visibili[0].classList.add('ad-tutta');
                    if(visibili.length%3===2){visibili[0].classList.add('ad-meta');visibili[1].classList.add('ad-meta');}
                    if(visibili.length%2===1)visibili[0].classList.add('ad-dispari');
                }
                g.hidden=!visibili.length;
                var n=g.querySelector('.giorno-n');
                if(n)n.textContent=visibili.length+(visibili.length===1?' articolo':' articoli');
            });
        }
        bottoni.forEach(function(b){b.addEventListener('click',function(){
            bottoni.forEach(function(x){x.classList.remove('on');});b.classList.add('on');filtra(b.getAttribute('data-f'));
        });});
    })();
    </script>
    <!-- /JS-DISPOSIZIONE -->
'''


def aggiorna_stile(pagina):
    blocco = re.compile(r"[ \t]*/\* ===== DISPOSIZIONE 2026-11[\s\S]*?/\* ===== /DISPOSIZIONE 2026-11 ===== \*/\n")
    if blocco.search(pagina):
        return blocco.sub(lambda _: CSS, pagina, count=1)
    vecchio = re.compile(r"[ \t]*/\* Qualunque contenitore di schede diventa una griglia uniforme[\s\S]*?\.n-card\{grid-column:auto !important\}\n")
    assert vecchio.search(pagina), "non trovo le regole della griglia uniforme da sostituire"
    return vecchio.sub(lambda _: CSS, pagina, count=1)


def aggiorna_script(pagina):
    blocco = re.compile(r"[ \t]*<!-- JS-DISPOSIZIONE[\s\S]*?<!-- /JS-DISPOSIZIONE -->\n")
    if blocco.search(pagina):
        return blocco.sub(lambda _: JS, pagina, count=1)
    i = pagina.rindex("</body>")
    return pagina[:i] + JS + pagina[i:]


# ---------------------------------------------------------------- pagine archivio

def testata_archivio(pagina, titolo, descrizione, file):
    """Riusa <head>, ticker, intestazione e menu della homepage, con i metadati della pagina archivio."""
    testa = pagina[:pagina.index("<main")]
    url = SITO + file
    testa = re.sub(r"<script type=\"application/ld\+json\">[\s\S]*?</script>\s*", "", testa)
    for modello, valore in [
        (r"(<title>)[^<]*(</title>)", titolo + " | Alma Finanza"),
        (r'(<meta name="description" content=")[^"]*(")', descrizione),
        (r'(<meta property="og:title" content=")[^"]*(")', titolo + " | Alma Finanza"),
        (r'(<meta property="og:description" content=")[^"]*(")', descrizione),
        (r'(<meta property="og:url" content=")[^"]*(")', url),
        (r'(<meta name="twitter:title" content=")[^"]*(")', titolo + " | Alma Finanza"),
        (r'(<meta name="twitter:description" content=")[^"]*(")', descrizione),
        (r'(<link rel="canonical" href=")[^"]*(")', url),
    ]:
        testa = re.sub(modello, lambda m: m.group(1) + html.escape(valore) + m.group(2), testa, count=1)
    return testa


def coda_archivio(pagina):
    return pagina[pagina.index("</main>"):]


def pillole(mesi, corrente=None):
    return "".join('<a href="%s"%s>%s</a>' % (file_mese(m), ' class="qui"' if m == corrente else "", nome_mese(m)) for m in mesi)


def pagina_mese(pagina, mese, gruppi, mesi):
    n = sum(len(g["schede"]) for g in gruppi)
    titolo = f"Archivio · {nome_mese(mese)}"
    descrizione = (f"Tutti gli articoli di Alma Finanza di {nome_mese(mese).lower()}: {n} articoli in "
                   f"{len(gruppi)} giornate su Wall Street, Piazza Affari, macroeconomia, tech e materie prime.")
    i = mesi.index(mese)
    dopo = f'<a class="arch-btn" href="{file_mese(mesi[i - 1])}">← {nome_mese(mesi[i - 1])}</a>' if i > 0 else '<a class="arch-btn" href="index.html">← Ultime notizie</a>'
    prima = f'<a class="arch-btn" href="{file_mese(mesi[i + 1])}">{nome_mese(mesi[i + 1])} →</a>' if i + 1 < len(mesi) else ""
    return testata_archivio(pagina, titolo, descrizione, file_mese(mese)) + f'''<main class="max-w-6xl mx-auto px-4 py-4">
        <!-- Pagina archivio generata da impagina-home.py: non modificare a mano -->
        <div class="arch-pista"><a href="index.html">Home</a> · <a href="archivio.html">Archivio</a> · {nome_mese(mese)}</div>
        <h1 class="arch-titolo">{titolo}</h1>
        <p class="arch-sotto">{n} articoli in {len(gruppi)} giornate</p>
        <div class="arch-mesi">{pillole(mesi, mese)}</div>

{chr(10).join(sezioni(gruppi))}
        <div class="arch-piede">{dopo}{prima}</div>
    ''' + coda_archivio(pagina)


def pagina_indice(pagina, per_mese, mesi, totale, in_home):
    titolo = "Archivio degli articoli"
    descrizione = f"L'archivio completo di Alma Finanza: {totale} articoli sui mercati finanziari, ordinati per mese e per giorno."
    riquadri = f'<a href="index.html"><b>Ultime notizie</b><span>{sum(len(g["schede"]) for g in in_home)} articoli · le ultime {len(in_home)} giornate, in homepage</span></a>'
    for m in mesi:
        g = per_mese[m]
        riquadri += f'<a href="{file_mese(m)}"><b>{nome_mese(m)}</b><span>{sum(len(x["schede"]) for x in g)} articoli · {len(g)} giornate</span></a>'
    return testata_archivio(pagina, titolo, descrizione, "archivio.html") + f'''<main class="max-w-6xl mx-auto px-4 py-4">
        <!-- Pagina archivio generata da impagina-home.py: non modificare a mano -->
        <div class="arch-pista"><a href="index.html">Home</a> · Archivio</div>
        <h1 class="arch-titolo">{titolo}</h1>
        <p class="arch-sotto">{totale} articoli, ordinati per mese e per giorno.</p>
        <div class="arch-indice">{riquadri}</div>
    ''' + coda_archivio(pagina)


def aggiorna_sitemap(file):
    """Le pagine archivio devono stare in sitemap, senza blocco news. Operazione ripetibile."""
    sm = BASE / "sitemap.xml"
    s = sm.read_text(encoding="utf-8")
    oggi = datetime.date.today().isoformat()
    for f in file:
        loc = f"<loc>{SITO}{f}</loc>"
        if loc in s:
            s = re.sub(re.escape(loc) + r"\s*<lastmod>[^<]*</lastmod>", f"{loc}\n      <lastmod>{oggi}</lastmod>", s, count=1)
        else:
            voce = f"  <url>\n      {loc}\n      <lastmod>{oggi}</lastmod>\n      <changefreq>monthly</changefreq>\n      <priority>0.5</priority>\n  </url>\n"
            i = s.rindex("</urlset>")
            s = s[:i] + voce + s[i:]
    xml.dom.minidom.parseString(s.encode("utf-8"))          # se non è XML valido si ferma qui, senza scrivere
    sm.write_text(s, encoding="utf-8")


# ---------------------------------------------------------------- principale

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--applica", action="store_true", help="riscrive index.html, le pagine archivio e la sitemap")
    ap.add_argument("--parola", help='parola del giorno, nella forma "Termine|traduzione italiana"')
    args = ap.parse_args()

    pagina = SRC.read_text(encoding="utf-8")
    convertita = INIZIO in pagina
    archivi = sorted(BASE.glob("archivio-20??-??.html"))
    if convertita:
        gruppi = leggi_nuovo([pagina] + [a.read_text(encoding="utf-8") for a in archivi])
    else:
        gruppi = leggi_storico(pagina)
    prima = {href(s) for g in gruppi for s in g["schede"]}
    gruppi = ripulisci(gruppi)
    dopo = [href(s) for g in gruppi for s in g["schede"]]
    assert set(dopo) == prima and len(dopo) == len(set(dopo)), "le schede non tornano: nessun articolo deve sparire o raddoppiare"
    assert len(gruppi) > 1, "servono almeno due giornate"

    # parola del giorno: quella indicata, altrimenti quella già in pagina
    if args.parola:
        parola = tuple(p.strip() for p in args.parola.split("|", 1))
        assert len(parola) == 2 and all(parola), 'la parola va scritta come "Termine|traduzione"'
    else:
        m = re.search(r'<!-- PAROLA --><b>([^<]*)</b><span class="fp-it">([^<]*)</span><!-- /PAROLA -->', pagina)
        assert m, 'manca la parola del giorno: indicala con --parola "Termine|traduzione"'
        parola = (html.unescape(m.group(1)), html.unescape(m.group(2)))

    # homepage: stile, corpo, script; la data in testata è quella della giornata più recente
    nuova = aggiorna_stile(pagina)
    if convertita:
        i, j = nuova.index(INIZIO), nuova.index(FINE) + len(FINE)
        nuova = nuova[:i].rstrip(" ") + "        " + corpo_home(gruppi, parola) + "        " + nuova[j:].lstrip()
    else:
        a, b = nuova.index("<!-- Stats Bar -->"), nuova.index("<!-- Main Content -->")
        nuova = nuova[:a] + nuova[b:]                         # la barra statica di chiusura non esiste più
        i = nuova.index(">", nuova.index("<main")) + 1
        j = nuova.index("<!-- Mission Section -->")
        nuova = nuova[:i] + "\n\n        " + corpo_home(gruppi, parola) + "        " + nuova[j:]
    nuova, n = re.subn(r'(<div class="text-xs text-gray-400 dark:text-slate-600 hidden md:block">)[^<]*(</div>)',
                       lambda m: m.group(1) + titolo_da_data(gruppi[0]["data"]) + m.group(2), nuova, count=1)
    assert n == 1, "non trovo la data nella testata"
    nuova = aggiorna_script(nuova)

    in_home, in_archivio = gruppi[:GIORNATE_IN_HOME], gruppi[GIORNATE_IN_HOME:]
    per_mese = {}
    for g in in_archivio:
        per_mese.setdefault(g["data"][:7], []).append(g)
    mesi = sorted(per_mese, reverse=True)
    totale = len(dopo)

    print(f"giornate: {len(gruppi)} · articoli: {totale} · in homepage: {sum(len(g['schede']) for g in in_home)} "
          f"in {len(in_home)} giornate · in archivio: {totale - sum(len(g['schede']) for g in in_home)} in {len(mesi)} mesi")
    print("primo piano:", gruppi[0]["titolo"], "·", len(gruppi[0]["schede"]), "articoli")

    if not args.applica:
        (BASE / "index-nuovo.html").write_text(nuova, encoding="utf-8")
        print("scritto index-nuovo.html (anteprima). Con --applica si riscrivono index.html, archivi e sitemap.")
        return

    shutil.copy(SRC, BASE / "index-backup.html")
    SRC.write_text(nuova, encoding="utf-8")
    scritti = []
    for m in mesi:
        (BASE / file_mese(m)).write_text(pagina_mese(nuova, m, per_mese[m], mesi), encoding="utf-8")
        scritti.append(file_mese(m))
    for vecchio in archivi:                                   # un mese rimasto senza giornate non lascia pagine orfane
        if vecchio.name not in scritti:
            vecchio.unlink()
    (BASE / "archivio.html").write_text(pagina_indice(nuova, per_mese, mesi, totale, in_home), encoding="utf-8")
    aggiorna_sitemap(["archivio.html"] + scritti)

    # controllo finale sui file scritti: tutti gli articoli raggiungibili, nessuno due volte
    trovati = []
    for f in [SRC] + [BASE / x for x in scritti]:
        zona = f.read_text(encoding="utf-8")
        zona = zona[:zona.index("<!-- Mission Section -->")] if f == SRC else zona
        trovati += [href(s) for s in SCHEDA.findall(zona[zona.index("<main"):])]
    assert sorted(trovati) == sorted(dopo), "dopo la scrittura le schede non tornano"
    print(f"scritti index.html, archivio.html e {len(scritti)} pagine mensili; sitemap aggiornata; {len(trovati)} schede verificate")


if __name__ == "__main__":
    sys.exit(main())
