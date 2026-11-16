#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Alma Finanza — compone l'edizione settimanale della newsletter dai contenuti già pubblicati sul sito.

Non inventa nulla: titoli, "Perché conta", foto e parola vengono da index.html, archivi e glossario; i numeri
degli indici vengono dai blocchi <!-- INDICI --> degli articoli di chiusura (chiusura ufficiale) e la variazione
settimanale si calcola sulla chiusura del venerdì precedente (Yahoo Finance). Se un dato non torna, la riga non esce.

Uso:
  python3 newsletter.py --numero 1 --oggetto "..." --anteprima-testo "..." --intro "..." \\
      [--settimana 2026-11-14] [--evidenza slug1,slug2,...] [--agenda "Lunedì 16|testo;Martedì 17|testo"]

Scrive in output/newsletter/ (cartella non pubblicata):
  AAAA-MM-GG-email.html      il codice da incollare in Brevo (editor "Incolla il tuo codice")
  AAAA-MM-GG-anteprima.html  la stessa pagina con le immagini locali, per controllarla prima dell'invio
  AAAA-MM-GG.txt             oggetto, testo di anteprima e versione in solo testo
e in img/newsletter/ le miniature delle foto (vanno pubblicate col sito PRIMA di inviare l'email).
I segnaposto {{ mirror }} e {{ unsubscribe }} sono quelli di Brevo: li sostituisce Brevo al momento dell'invio.
"""
import argparse, datetime, html, importlib.util, json, pathlib, re, subprocess, sys

BASE = pathlib.Path(__file__).resolve().parent
SITO = "https://www.almafinanza.com/"
BLOCCO = re.compile(r'<!-- (PRIMO-PIANO|GIORNO) (\d{4}-\d{2}-\d{2}) \| ([^>]*?) -->([\s\S]*?)<!-- /\1 -->')
SCHEDA = re.compile(r'<a\s[^>]*class="[^"]*\bn-card\b[^"]*"[^>]*>[\s\S]*?</a>')
INDICI = re.compile(r'<!--\s*INDICI\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|(.*?)-->', re.S)
ORDINE = ["^GSPC", "^IXIC", "^DJI", "FTSEMIB.MI", "^STOXX"]
GIORNI = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]
COLORI = {"wall": "#2563eb", "milano": "#059669", "macro": "#dc2626", "commod": "#d97706", "tech": "#7c3aed", "corp": "#0284c7"}
BLU, TEAL, INK, INK2, RIGA = "#0f2540", "#14b8a6", "#0f172a", "#475569", "#e2e8f0"
FONT = "'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,Helvetica,sans-serif"
FONT_T = "'Manrope'," + FONT


def testo(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def e(s):
    return html.escape(s, quote=True)


def it(v, dec=2):
    s = ("%." + str(dec) + "f") % abs(v)
    i, _, d = s.partition(".")
    i = ".".join([i[max(0, k - 3):k] for k in range(len(i), 0, -3)][::-1])
    return i + ("," + d if dec else "")


def schede_della_settimana(lun, dom):
    """Tutte le schede pubblicate fra lunedì e domenica, per giorno (più recente prima), nell'ordine della homepage."""
    pagine = [BASE / "index.html"] + sorted(BASE.glob("archivio-20??-??.html"), reverse=True)
    giorni, visti = {}, set()
    for p in pagine:
        for m in BLOCCO.finditer(p.read_text(encoding="utf-8")):
            data = m.group(2)
            if not (lun.isoformat() <= data <= dom.isoformat()):
                continue
            for s in SCHEDA.findall(m.group(4)):
                href = re.search(r'href="([^"]+)"', s).group(1)
                if href in visti:
                    continue
                visti.add(href)
                img = re.search(r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]*)"', s)
                why = re.search(r'<p class="n-why">([\s\S]*?)</p>', s)
                giorni.setdefault(data, []).append({
                    "href": href, "data": data,
                    "cat": (re.search(r'data-cat="([a-z]+)"', s) or [None, "wall"])[1],
                    "etichetta": testo(re.search(r'class="n-cat"[^>]*>([\s\S]*?)</div>', s).group(1)),
                    "titolo": testo(re.search(r"<h3[^>]*>([\s\S]*?)</h3>", s).group(1)),
                    "perche": re.sub(r"^Perché conta:\s*", "", testo(why.group(1))) if why else "",
                    "img": img.group(1) if img else None, "alt": html.unescape(img.group(2)) if img else "",
                })
    return dict(sorted(giorni.items(), reverse=True))


def numeri(lun, dom):
    """Chiusura ufficiale (dai blocchi INDICI) e variazione sulla chiusura della settimana precedente."""
    ultimo = {}
    for f in sorted(BASE.glob("articolo-*.html")):
        t = f.read_text(encoding="utf-8")
        if "INDICI |" not in t:
            continue
        for m in INDICI.finditer(t):
            if not (lun.isoformat() <= m.group(1) <= dom.isoformat()):
                continue
            for riga in m.group(2).split(";"):
                c = [x.strip() for x in riga.split("|")]
                if len(c) == 4 and (c[0] not in ultimo or m.group(1) >= ultimo[c[0]][0]):
                    ultimo[c[0]] = (m.group(1), html.unescape(c[1]), float(c[2]))
    righe = []
    for sim in [s for s in ORDINE if s in ultimo]:
        giorno, nome, chius = ultimo[sim]
        try:
            raw = subprocess.run(["curl", "-s", "-m", "25", "-A", "Mozilla/5.0",
                                  "https://query1.finance.yahoo.com/v8/finance/chart/%s?interval=1d&range=1mo" % sim.replace("^", "%5E")],
                                 capture_output=True, text=True).stdout
            r = json.loads(raw)["chart"]["result"][0]
            serie = [(datetime.datetime.fromtimestamp(t, datetime.timezone.utc).date(), c)
                     for t, c in zip(r["timestamp"], r["indicators"]["quote"][0]["close"]) if c]
        except Exception as err:
            print("   numeri: %s non disponibile (%s)" % (sim, str(err)[:50]))
            continue
        oggi = [c for d, c in serie if d.isoformat() == giorno]
        prima = [c for d, c in serie if d < lun]
        if not oggi or not prima or abs(oggi[-1] - chius) > chius * 0.0015:
            print("   numeri: %s scartato, la serie non torna con la chiusura ufficiale %s" % (sim, chius))
            continue
        righe.append((nome, chius, (chius / prima[-1] - 1) * 100, giorno))
    return righe


def parola():
    m = re.search(r'<!-- PAROLA --><b>([^<]*)</b><span class="fp-it">([^<]*)</span><!-- /PAROLA -->', (BASE / "index.html").read_text(encoding="utf-8"))
    if not m:
        return None
    termine, trad = html.unescape(m.group(1)), html.unescape(m.group(2))
    g = (BASE / "glossario.html").read_text(encoding="utf-8")
    c = re.search(r'<h3[^>]*>%s</h3>\s*<p[^>]*>[^<]*</p>\s*<p[^>]*>([\s\S]*?)</p>' % re.escape(html.escape(termine, quote=False)), g)
    return (termine, trad, testo(c.group(1)) if c else "")


def miniatura(src, w, h):
    """Ritaglio leggero della foto di repertorio, salvato in img/newsletter/ (le email non devono scaricare foto da 1600px)."""
    from PIL import Image
    origine = BASE / src
    nome = "%s-%dx%d.jpg" % (origine.stem, w, h)
    dest = BASE / "img" / "newsletter" / nome
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists() or dest.stat().st_mtime < origine.stat().st_mtime:
        im = Image.open(origine).convert("RGB")
        r = max(w / im.width, h / im.height)
        im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
        x, y = (im.width - w) // 2, max(0, round((im.height - h) * 0.3))
        im.crop((x, y, x + w, y + h)).save(dest, "JPEG", quality=82, optimize=True, progressive=True)
    return "img/newsletter/" + nome


def logo():
    """Il logo come immagine (le email non caricano i font del sito): reso dal browser con gli stessi font e colori della testata."""
    dest = BASE / "img" / "newsletter" / "logo-alma-finanza.png"
    if dest.exists():
        return "img/newsletter/logo-alma-finanza.png"
    from playwright.sync_api import sync_playwright
    pagina = ('<html><head><link href="https://fonts.googleapis.com/css2?family=Lobster&family=Montserrat:wght@900&display=swap" rel="stylesheet">'
              '<style>body{margin:0;background:transparent}#l{display:inline-flex;align-items:center;gap:8px;padding:4px 6px}'
              '.a{font-family:Lobster,cursive;font-size:48px;color:#14b8a6;line-height:1}.t{font-family:Montserrat,sans-serif;font-weight:900;font-size:30px;color:#fff;white-space:nowrap}</style>'
              '</head><body><div id="l"><span class="a">A</span><span class="t">LMA FINANZA</span></div></body></html>')
    dest.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 600, "height": 120}, device_scale_factor=2)
        pg.set_content(pagina, wait_until="networkidle")
        pg.wait_for_timeout(1500)
        pg.locator("#l").screenshot(path=str(dest), omit_background=True)
        b.close()
    return "img/newsletter/logo-alma-finanza.png"


def periodo(lun, ultimo):
    if lun.month == ultimo.month:
        return "%d–%d %s %d" % (lun.day, ultimo.day, MESI[ultimo.month - 1], ultimo.year)
    return "%d %s – %d %s %d" % (lun.day, MESI[lun.month - 1], ultimo.day, MESI[ultimo.month - 1], ultimo.year)


def componi(a, giorni, righe, par, lun, ultimo, campagna):
    tutte = [s for g in giorni.values() for s in g]
    per_slug = {s["href"]: s for s in tutte}
    if a.evidenza:
        scelte = []
        for x in a.evidenza.split(","):
            trovati = [h for h in per_slug if x.strip() in h]
            assert len(trovati) == 1, "--evidenza: «%s» corrisponde a %d articoli" % (x, len(trovati))
            scelte.append(per_slug[trovati[0]])
    else:
        scelte = [g[0] for g in giorni.values()][:5]
    link = lambda s: SITO + s["href"] + "?utm_source=newsletter&utm_medium=email&utm_campaign=" + campagna
    titolo_sez = lambda t: ('<tr><td style="padding:28px 28px 10px"><div style="font:800 12px %s;letter-spacing:.12em;text-transform:uppercase;color:%s">%s</div>'
                            '<div style="height:3px;width:36px;background:%s;margin-top:8px;font-size:0;line-height:0">&nbsp;</div></td></tr>' % (FONT_T, BLU, t, TEAL))
    pill = lambda s: '<span style="font:700 10px %s;letter-spacing:.1em;text-transform:uppercase;color:%s">%s</span>' % (FONT, COLORI.get(s["cat"], BLU), e(s["etichetta"]))
    R, T = [], []   # html e solo testo

    # --- in evidenza
    R.append(titolo_sez("Da leggere"))
    T.append("DA LEGGERE\n")
    p0 = scelte[0]
    R.append('<tr><td style="padding:6px 28px 4px"><a href="%s" style="text-decoration:none;color:%s">'
             '<img src="{{BASE}}%s" width="544" alt="%s" style="display:block;width:100%%;max-width:544px;height:auto;border:0;border-radius:10px">'
             '<div style="padding-top:14px">%s</div><div style="font:800 23px/1.25 %s;color:%s;padding-top:6px">%s</div></a>'
             '<div style="font:400 15px/1.55 %s;color:%s;padding-top:8px"><b style="color:%s">Perché conta:</b> %s</div>'
             '<div style="padding-top:10px"><a href="%s" style="font:700 14px %s;color:%s;text-decoration:none">Leggi l\'articolo &rarr;</a></div></td></tr>'
             % (link(p0), INK, miniatura(p0["img"], 1088, 612), e(p0["alt"]), pill(p0), FONT_T, INK, e(p0["titolo"]), FONT, INK2, INK, e(p0["perche"]), link(p0), FONT, TEAL))
    T.append("%s\n%s\n%s\n" % (p0["titolo"], p0["perche"], link(p0)))
    for s in scelte[1:]:
        R.append('<tr><td style="padding:16px 28px 0"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0" style="border-top:1px solid %s"><tr>'
                 '<td width="132" valign="top" style="padding:16px 14px 0 0"><a href="%s"><img src="{{BASE}}%s" width="118" height="88" alt="%s" style="display:block;border:0;border-radius:8px"></a></td>'
                 '<td valign="top" style="padding-top:14px">%s<div style="padding-top:4px"><a href="%s" style="font:800 16px/1.3 %s;color:%s;text-decoration:none">%s</a></div>'
                 '<div style="font:400 13.5px/1.5 %s;color:%s;padding-top:5px">%s</div></td></tr></table></td></tr>'
                 % (RIGA, link(s), miniatura(s["img"], 236, 176), e(s["alt"]), pill(s), link(s), FONT_T, INK, e(s["titolo"]), FONT, INK2, e(s["perche"])))
        T.append("%s\n%s\n%s\n" % (s["titolo"], s["perche"], link(s)))

    # --- numeri
    if righe:
        gg = datetime.date.fromisoformat(righe[0][3])
        R.append(titolo_sez("I numeri della settimana"))
        tab = ""
        for nome, chius, sett, _ in righe:
            col = "#059669" if sett >= 0 else "#dc2626"
            tab += ('<tr><td style="padding:11px 0;border-bottom:1px solid %s;font:600 15px %s;color:%s">%s</td>'
                    '<td align="right" style="padding:11px 0;border-bottom:1px solid %s;font:400 15px %s;color:%s">%s</td>'
                    '<td align="right" width="96" style="padding:11px 0;border-bottom:1px solid %s;font:700 15px %s;color:%s">%s%s%%</td></tr>'
                    % (RIGA, FONT, INK, e(nome), RIGA, FONT, INK2, it(chius), RIGA, FONT, col, "+" if sett >= 0 else "−", it(sett)))
        R.append('<tr><td style="padding:2px 28px 0"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0">'
                 '<tr><td style="font:700 11px %s;letter-spacing:.08em;text-transform:uppercase;color:#94a3b8;padding-bottom:4px">Indice</td>'
                 '<td align="right" style="font:700 11px %s;letter-spacing:.08em;text-transform:uppercase;color:#94a3b8;padding-bottom:4px">Chiusura %d %s</td>'
                 '<td align="right" style="font:700 11px %s;letter-spacing:.08em;text-transform:uppercase;color:#94a3b8;padding-bottom:4px">Settimana</td></tr>%s</table></td></tr>'
                 % (FONT, FONT, gg.day, MESI[gg.month - 1][:3], FONT, tab))
        T.append("\nI NUMERI DELLA SETTIMANA\n" + "\n".join("%s: %s (%s%s%% nella settimana)" % (n, it(c), "+" if s >= 0 else "−", it(s)) for n, c, s, _ in righe) + "\n")

    # --- agenda
    if a.agenda:
        voci = [v.split("|", 1) for v in a.agenda.split(";") if v.strip()]
        R.append(titolo_sez("Cosa guardare ora"))
        R.append('<tr><td style="padding:2px 28px 0"><table role="presentation" width="100%" cellpadding="0" cellspacing="0">' + "".join(
            '<tr><td width="118" valign="top" style="padding:9px 10px 9px 0;font:700 14px %s;color:%s">%s</td><td valign="top" style="padding:9px 0;font:400 14.5px/1.5 %s;color:%s">%s</td></tr>'
            % (FONT, BLU, e(q.strip()), FONT, INK2, e(t.strip())) for q, t in voci) + '</table></td></tr>')
        T.append("\nCOSA GUARDARE ORA\n" + "\n".join("%s: %s" % (q.strip(), t.strip()) for q, t in voci) + "\n")

    # --- parola
    if par and par[2]:
        R.append(titolo_sez("La parola della settimana"))
        R.append('<tr><td style="padding:4px 28px 0"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0" style="background:#f0fdfa;border-left:4px solid %s;border-radius:6px"><tr><td style="padding:16px 18px">'
                 '<div style="font:800 18px %s;color:%s">%s <span style="font:600 14px %s;color:#0f766e">(%s)</span></div>'
                 '<div style="font:400 14.5px/1.55 %s;color:%s;padding-top:6px">%s</div>'
                 '<div style="padding-top:8px"><a href="%sglossario.html?utm_source=newsletter&utm_medium=email&utm_campaign=%s" style="font:700 13px %s;color:#0f766e;text-decoration:none">Tutto il glossario &rarr;</a></div></td></tr></table></td></tr>'
                 % (TEAL, FONT_T, INK, e(par[0]), FONT, e(par[1]), FONT, INK2, e(par[2]), SITO, campagna, FONT))
        T.append("\nLA PAROLA DELLA SETTIMANA\n%s (%s): %s\n" % par)

    # --- tutti gli articoli
    R.append(titolo_sez("Tutti gli articoli della settimana"))
    T.append("\nTUTTI GLI ARTICOLI DELLA SETTIMANA\n")
    for data, g in giorni.items():
        d = datetime.date.fromisoformat(data)
        R.append('<tr><td style="padding:10px 28px 0"><div style="font:700 13px %s;color:%s;padding-bottom:4px">%s %d %s</div>%s</td></tr>' % (
            FONT, INK, GIORNI[d.weekday()], d.day, MESI[d.month - 1],
            "".join('<div style="font:400 14px/1.45 %s;padding:4px 0"><a href="%s" style="color:%s;text-decoration:underline;text-decoration-color:#cbd5e1">%s</a></div>' % (FONT, link(s), INK2, e(s["titolo"])) for s in g)))
        T.append("%s %d %s\n%s\n" % (GIORNI[d.weekday()], d.day, MESI[d.month - 1], "\n".join("- %s\n  %s" % (s["titolo"], link(s)) for s in g)))

    corpo = "\n".join(R)
    pagina = f'''<!DOCTYPE html>
<html lang="it"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light"><title>{e(a.oggetto)}</title>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@700;800&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>body{{margin:0;padding:0;background:#eef2f7}}a{{color:{TEAL}}}@media (max-width:620px){{.w{{width:100%!important}}}}</style></head>
<body style="margin:0;padding:0;background:#eef2f7">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;font-size:1px;line-height:1px;color:#eef2f7">{e(a.anteprima_testo)}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#eef2f7"><tr><td align="center" style="padding:18px 10px 30px">
<table role="presentation" class="w" width="600" cellpadding="0" cellspacing="0" style="width:600px;max-width:600px">
<tr><td align="right" style="padding:0 4px 8px;font:400 12px {FONT};color:#64748b">Non la vedi bene? <a href="{{{{ mirror }}}}" style="color:#64748b">Aprila nel browser</a></td></tr>
<tr><td style="background:{BLU};border-radius:12px 12px 0 0;padding:26px 28px 24px">
<a href="{SITO}?utm_source=newsletter&utm_medium=email&utm_campaign={campagna}"><img src="{{{{BASE}}}}{logo()}" width="196" alt="Alma Finanza" style="display:block;border:0;width:196px;height:auto"></a>
<div style="font:800 26px/1.2 {FONT_T};color:#ffffff;padding-top:20px">La settimana dei mercati</div>
<div style="font:600 14px {FONT};color:#99f6e4;padding-top:6px">{periodo(lun, ultimo)} · n. {a.numero}</div></td></tr>
<tr><td style="background:#ffffff;border-radius:0 0 12px 12px;padding-bottom:30px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0">
<tr><td style="padding:26px 28px 0;font:400 16px/1.6 {FONT};color:{INK}">{e(a.intro)}</td></tr>
{corpo}
<tr><td style="padding:30px 28px 0"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f8fafc;border-radius:10px"><tr><td align="center" style="padding:20px 18px">
<div style="font:800 16px {FONT_T};color:{INK}">Ti è stata utile?</div>
<div style="font:400 14px/1.5 {FONT};color:{INK2};padding-top:6px">Inoltrala a chi vuole capire i mercati senza gergo. Per iscriversi basta andare su <a href="{SITO}newsletter.html?utm_source=newsletter&utm_medium=email&utm_campaign={campagna}" style="color:#0f766e;font-weight:700;text-decoration:none">almafinanza.com/newsletter</a>.</div></td></tr></table></td></tr>
</table></td></tr>
<tr><td style="padding:22px 20px 0;font:400 12px/1.6 {FONT};color:#64748b" align="center">
Alma Finanza pubblica contenuti informativi ed educativi: non sono consigli di investimento né sollecitazione al pubblico risparmio. Ogni decisione di investimento è personale e comporta rischi.<br><br>
Ricevi questa email perché ti sei iscritto alla newsletter su almafinanza.com.<br>
<a href="{{{{ unsubscribe }}}}" style="color:#64748b">Annulla l'iscrizione</a> · <a href="{SITO}privacy.html" style="color:#64748b">Informativa sulla privacy</a><br><br>
© {ultimo.year} Alma Finanza</td></tr>
</table></td></tr></table></body></html>
'''
    piano = ("OGGETTO: %s\nANTEPRIMA: %s\n\n%s\n\nLA SETTIMANA DEI MERCATI — %s — n. %s\n\n%s\n\n%s\n---\nAlma Finanza pubblica contenuti informativi ed educativi: non sono consigli di investimento.\n"
             "Annulla l'iscrizione: {{ unsubscribe }}\n" % (a.oggetto, a.anteprima_testo, "=" * 60, periodo(lun, ultimo), a.numero, a.intro, "\n".join(T)))
    return pagina, piano, scelte, tutte


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--settimana", help="un giorno qualsiasi della settimana (AAAA-MM-GG); predefinito: l'ultima giornata in homepage")
    ap.add_argument("--numero", required=True, help="numero progressivo dell'edizione")
    ap.add_argument("--oggetto", required=True, help="oggetto dell'email")
    ap.add_argument("--anteprima-testo", dest="anteprima_testo", required=True, help="riga che compare accanto all'oggetto nella casella di posta")
    ap.add_argument("--intro", required=True, help="due-quattro frasi di apertura, scritte sui dati degli articoli")
    ap.add_argument("--evidenza", help="parti del nome file degli articoli in evidenza, separate da virgola (il primo ha la foto grande)")
    ap.add_argument("--agenda", help='appuntamenti, nella forma "Quando|che cosa;Quando|che cosa"')
    a = ap.parse_args()

    idx = (BASE / "index.html").read_text(encoding="utf-8")
    rif = datetime.date.fromisoformat(a.settimana or max(m.group(2) for m in BLOCCO.finditer(idx)))
    lun = rif - datetime.timedelta(days=rif.weekday())
    dom = lun + datetime.timedelta(days=6)
    giorni = schede_della_settimana(lun, dom)
    assert giorni, "nessun articolo fra %s e %s" % (lun, dom)
    ultimo = datetime.date.fromisoformat(max(giorni))
    campagna = "settimana-" + ultimo.isoformat()
    pagina, piano, scelte, tutte = componi(a, giorni, numeri(lun, dom), parola(), lun, ultimo, campagna)

    out = BASE / "output" / "newsletter"
    out.mkdir(parents=True, exist_ok=True)
    (out / (ultimo.isoformat() + "-email.html")).write_text(pagina.replace("{{BASE}}", SITO), encoding="utf-8")
    (out / (ultimo.isoformat() + "-anteprima.html")).write_text(pagina.replace("{{BASE}}", BASE.as_uri() + "/"), encoding="utf-8")
    (out / (ultimo.isoformat() + ".txt")).write_text(piano, encoding="utf-8")
    print("settimana %s – %s · %d articoli in %d giornate · in evidenza: %d" % (lun, ultimo, len(tutte), len(giorni), len(scelte)))
    print("oggetto (%d caratteri): %s" % (len(a.oggetto), a.oggetto))
    print("scritti in output/newsletter/: %s-email.html, -anteprima.html, .txt" % ultimo.isoformat())
    print("peso dell'email: %.0f KB (Gmail taglia oltre 102 KB)" % (len(pagina.encode("utf-8")) / 1024))


if __name__ == "__main__":
    sys.exit(main())
