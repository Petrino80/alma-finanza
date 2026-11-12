# -*- coding: utf-8 -*-
"""
Impagina gli articoli di Alma Finanza con il layout "D" (dal 12 novembre 2026, SOLO per gli articoli nuovi).

Gli articoli si scrivono come sempre (modello in uso, foto e firma con applica-foto-articolo.py).
Questo script li trasforma nel layout D: testata blu scuro con le sezioni del sito, titolo in Manrope,
colonna destra con "In sintesi", indice e riquadro "Impara", schede dei numeri, articoli della stessa giornata.
Gli articoli già pubblicati NON vanno convertiti. Stile in articolo-d.css, comportamenti in articolo-d.js.

USO
    python3 impagina-articolo.py a.html b.html c.html            # prova: mostra cosa troverebbe, non scrive
    python3 impagina-articolo.py a.html b.html c.html --applica  # scrive i file

Eseguirlo UNA volta sola, su TUTTI gli articoli della giornata insieme (le schede "Dalla stessa giornata"
si costruiscono fra gli articoli passati nello stesso comando). Un file già in layout D viene saltato.

BLOCCHI DA METTERE NEL TESTO DELL'ARTICOLO, DOPO il paragrafo <p class="lead"> (commenti HTML, invisibili nel vecchio formato)
  Chiusura di un indice (solo articoli Wall Street / Piazza Affari): tre schede con valore, variazione e andamento reale della seduta
      <!-- INDICI | 2026-11-12 | ^GSPC|S&P 500|7592.40|-27.98 ; ^IXIC|Nasdaq Composite|25366.09|-100.10 ; ^DJI|Dow Jones|52297.09|-189.40 -->
      campi per indice: simbolo Yahoo | nome | chiusura ufficiale | variazione in punti (con segno) — Piazza Affari: FTSEMIB.MI
  Scheda numeri di un'azienda (nel punto in cui compare il commento):
      <!-- SCHEDA | CoreWeave | Dati del trimestre | Ricavi trimestrali|3,661 mld $|+168% su base annua ; Contratti in portafoglio|132,5 mld $ -->
  Sintesi (facoltativo): <!-- SINTESI --><ul><li>...</li></ul><!-- /SINTESI -->
      Se manca, l'"In sintesi" si ricava dal riquadro finale "Da ricordare" (voci separate da " · ").
      Se mancano entrambi lo script si ferma: non inventa nulla.
"""
import re, sys, os, json, html, subprocess, datetime

B = os.path.dirname(os.path.abspath(__file__)) + '/'
CSS_V = '1'
MARK = '<!-- LAYOUT-D v1 -->'

CATEGORIE = {  # nome nel banner -> (data-cat, pagina categoria)
    'wall street': ('wall', 'categoria-wall-street.html'),
    'piazza affari': ('milano', 'categoria-borsa-milano.html'),
    'borsa milano': ('milano', 'categoria-borsa-milano.html'),
    'commodities': ('commod', 'categoria-commodities.html'),
    'crypto': ('commod', 'categoria-crypto.html'),
    'macro': ('macro', None), 'geopolitica': ('macro', None),
    'tech': ('tech', None), 'ai': ('tech', None),
    'corporate': ('corp', None),
}
COLORE_BANNER = {'blue': 'wall', 'emerald': 'milano', 'red': 'macro', 'amber': 'commod', 'purple': 'tech', 'sky': 'corp'}
MESI = ['gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre']
NAV = [('Home', 'index.html'), ('Wall Street', 'categoria-wall-street.html'), ('Borsa Milano', 'categoria-borsa-milano.html'),
       ('Crypto', 'categoria-crypto.html'), ('Commodities', 'categoria-commodities.html'),
       ('Impara la Finanza', 'impara-finanza.html'), ('Glossario', 'glossario.html')]


def testo(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', s))).strip()


def it(v, dec=2, segno=False):
    s = '{:,.{d}f}'.format(abs(v), d=dec).replace(',', 'X').replace('.', ',').replace('X', '.')
    return ('+' if v > 0 else '−' if v < 0 else '') + s if segno else ('−' if v < 0 else '') + s


# ---------------------------------------------------------------- grafici reali della seduta
def serie(simbolo, chiusura, giorno, tol_rel=0.001):
    """Punti a 5 minuti del giorno (Yahoo Finance). L'ultimo punto deve stare entro 0,1% dalla chiusura ufficiale e viene allineato ad essa."""
    try:
        raw = subprocess.run(['curl', '-s', '-m', '25', '-A', 'Mozilla/5.0',
                              'https://query1.finance.yahoo.com/v8/finance/chart/%s?interval=5m&range=5d' % simbolo.replace('^', '%5E')],
                             capture_output=True, text=True).stdout
        d = json.loads(raw)['chart']['result'][0]
        pts = [c for t, c in zip(d['timestamp'], d['indicators']['quote'][0]['close'])
               if c is not None and datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime('%Y-%m-%d') == giorno]
    except Exception as e:
        print('   grafico non disponibile per', simbolo, '(' + str(e)[:50] + ')')
        return None
    if len(pts) < 40 or abs(pts[-1] - chiusura) > chiusura * tol_rel:
        print('   grafico SCARTATO per', simbolo, '- punti:', len(pts), 'ultimo:', pts[-1] if pts else None, 'chiusura indicata:', chiusura)
        return None
    pts[-1] = chiusura
    return pts


def svg(pts, prec, w=130, h=46):
    pad = 4
    lo, hi = min(min(pts), prec), max(max(pts), prec)
    sx = lambda i: i * w / (len(pts) - 1)
    sy = lambda v: pad + (hi - v) * (h - 2 * pad) / (hi - lo)
    linea = ' '.join('%s%.1f,%.1f' % ('M' if i == 0 else 'L', sx(i), sy(v)) for i, v in enumerate(pts))
    area = linea + ' L%.1f,%d L0,%d Z' % (w, h, h)
    col = '#22c55e' if pts[-1] >= prec else '#ef4444'
    gid = 'g%d' % (abs(hash(linea)) % 99999)
    return ('<svg class="spk" viewBox="0 0 %d %d" preserveAspectRatio="none" role="img" aria-label="Andamento della seduta">'
            '<defs><linearGradient id="%s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="%s" stop-opacity=".25"/><stop offset="1" stop-color="%s" stop-opacity="0"/></linearGradient></defs>'
            '<path d="%s" fill="url(#%s)"/><line x1="0" x2="%d" y1="%.1f" y2="%.1f" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3" vector-effect="non-scaling-stroke"/>'
            '<path d="%s" fill="none" stroke="%s" stroke-width="2" vector-effect="non-scaling-stroke" stroke-linejoin="round"/></svg>') % (
        w, h, gid, col, col, area, gid, w, sy(prec), sy(prec), linea, col)


# ---------------------------------------------------------------- lettura articolo
def leggi(path):
    s = open(path, encoding='utf-8').read()
    d = {'path': path, 'src': s}
    if MARK in s:
        return d  # già convertito
    m = re.search(r'<article[^>]*>(.*)</article>', s, re.S)
    if not m or '<p class="lead">' not in m.group(1):
        raise ValueError('formato articolo non riconosciuto (manca <article> o <p class="lead">)')
    art = m.group(1)
    # banner
    bn = re.search(r'<div class="bg-([a-z]+)-\d+[^"]*text-white">(.*?)</h1>(.*?)</div>\s*</div>', s, re.S)
    if not bn:
        raise ValueError('banner di categoria non trovato')
    kick = re.search(r'<span class="[^"]*uppercase[^"]*">(.*?)</span>', bn.group(2), re.S)
    kt = testo(kick.group(1)) if kick else ''
    kt = re.sub(r'[^\w\s·&\'’./+−-]', '', kt, flags=re.U).strip()
    parti = [p.strip() for p in kt.split('·') if p.strip()]
    d['cat_nome'] = parti[0] if parti else 'Alma Finanza'
    d['cat_sotto'] = parti[1] if len(parti) > 2 else ''
    d['cat'] = CATEGORIE.get(d['cat_nome'].lower(), (COLORE_BANNER.get(bn.group(1), 'wall'), None))
    d['h1'] = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S).group(1).strip()
    dk = re.search(r'</h1>\s*<p[^>]*>(.*?)</p>', s, re.S)
    d['deck'] = dk.group(1).strip() if dk else ''
    tm = re.search(r'<time datetime="([^"]+)"', art)
    if not tm:
        raise ValueError('manca <time datetime=...> (esegui prima applica-foto-articolo.py)')
    d['dt'] = tm.group(1)
    lm = re.search(r'Lettura\s+(\d+)\s+min', art)
    d['min'] = lm.group(1) if lm else str(max(2, round(len(testo(art).split()) / 200)))
    fg = re.search(r'<figure.*?<img src="([^"]+)"[^>]*alt="([^"]*)".*?<figcaption[^>]*>(.*?)</figcaption>', art, re.S)
    d['img'], d['alt'], d['cap'] = (fg.group(1), fg.group(2), testo(fg.group(3))) if fg else (None, '', '')
    d['body'] = art[art.index('<p class="lead">'):]
    d['canon'] = re.search(r'<link rel="canonical" href="([^"]+)"', s).group(1)
    ft = re.search(r'<footer.*?<p[^>]*>(.*?)</p>', s, re.S)
    d['disclaimer'] = ft.group(1).strip() if ft else ''
    return d


def pulisci_classi(b):
    """Toglie le classi Tailwind dal corpo, tiene solo quelle dello stile D."""
    ok = {'positive', 'negative', 'lead', 'info-box', 'highlight-box', 'data-table', 'note'}
    def f(m):
        keep = [c for c in m.group(1).split() if c in ok]
        return ' class="%s"' % ' '.join(keep) if keep else ''
    return re.sub(r' class="([^"]*)"', f, b)


def trasforma(d, correlati):
    ev = []  # avvisi
    b = re.sub(r'<p class="text-xs[^"]*">', '<p class="note">', d['body'])
    b = pulisci_classi(b)
    # --- blocchi dati
    indici = None
    mi = re.search(r'<!--\s*INDICI\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|(.*?)-->', b, re.S)
    if mi:
        indici = (mi.group(1), [[x.strip() for x in r.split('|')] for r in mi.group(2).strip().split(';') if r.strip()])
        b = b.replace(mi.group(0), '')
    # --- sintesi
    sint = None
    ms = re.search(r'<!--\s*SINTESI\s*-->(.*?)<!--\s*/SINTESI\s*-->', b, re.S)
    if ms:
        sint = re.findall(r'<li>(.*?)</li>', ms.group(1), re.S)
        b = b.replace(ms.group(0), '')
    mr = re.search(r'<div class="info-box">\s*<h3>[^<]*Da ricordare[^<]*</h3>\s*<p>(.*?)</p>\s*</div>', b, re.S)
    if mr and sint:
        b = b.replace(mr.group(0), '')  # il riepilogo finale ripete l'"In sintesi": si toglie
    if not ms:
        if mr:
            sint = [x.strip() for x in mr.group(1).split(' · ') if x.strip()]
            if len(sint) > 6:
                raise ValueError('il riquadro "Da ricordare" ha %d voci: troppe per l\'"In sintesi". Scrivi il blocco <!-- SINTESI --> con 4-5 punti' % len(sint))
            b = b.replace(mr.group(0), '')
    if not sint:
        raise ValueError('manca la sintesi: aggiungi il blocco <!-- SINTESI --> oppure il riquadro finale "Da ricordare"')
    # --- Perché conta
    def why(m):
        t = m.group(1).strip()
        return '<aside class="why"><span class="why-l">Perché conta</span><p>%s</p></aside>' % (t[:1].upper() + t[1:])
    b, n = re.subn(r'<p[^>]*>\s*<strong[^>]*>\s*Perché conta:?\s*</strong>(.*?)</p>', why, b, count=1, flags=re.S)
    if not n:
        ev.append('manca il "Perché conta"')
    # --- scheda azienda (posizione = posizione del commento)
    for m in re.finditer(r'<!--\s*SCHEDA\s*\|(.*?)-->', b, re.S):
        parti = [x.strip() for x in m.group(1).split('|', 2)]
        voci = [[y.strip() for y in v.split('|')] for v in parti[2].split(';') if v.strip()]
        h = '<div class="co"><div class="co-n">%s<small>%s</small></div>' % (parti[0], parti[1])
        for v in voci:
            h += '<div class="co-i"><span>%s</span><b>%s</b>%s</div>' % (v[0], v[1], '<em>%s</em>' % v[2] if len(v) > 2 else '')
        b = b.replace(m.group(0), h + '</div>')
    # --- Impara: copia nella colonna (nel testo resta, visibile solo su telefono)
    imp = re.search(r'<div class="info-box">\s*<h3>💡\s*Impara:\s*(.*?)</h3>\s*<p>(.*?)</p>\s*</div>', b, re.S)
    impara = None
    if imp:
        impara = (imp.group(1), imp.group(2))
        b = b.replace(imp.group(0), imp.group(0).replace('<div class="info-box">', '<div class="info-box impara-body">', 1), 1)
    # --- titoli di sezione con id, tabelle, nota
    n = [0]
    def h2(m):
        n[0] += 1
        return '<h2 id="s%d">%s</h2>' % (n[0], m.group(1))
    b = re.sub(r'<h2[^>]*>(.*?)</h2>', h2, b, flags=re.S)
    sez = re.findall(r'<h2 id="(s\d+)">(.*?)</h2>', b, re.S)
    b = re.sub(r'<table class="data-table">(.*?)</table>', r'<div class="tw"><table class="data-table">\1</table></div>', b, flags=re.S)
    # --- controlli di struttura (regole del Master Prompt)
    if len(sez) < 5: ev.append('meno di 5 sezioni (%d)' % len(sez))
    if b.count('class="tw"') < 2: ev.append('meno di 2 tabelle')
    if b.count('class="info-box') < 2: ev.append('meno di 2 riquadri educativi')
    # --- pagina
    cat, pag = d['cat']
    dt = datetime.datetime.fromisoformat(d['dt'])
    data_lunga = '%d %s %d' % (dt.day, MESI[dt.month - 1], dt.year)
    # schede indici
    kp, tick, marker = '', '', ''
    if indici:
        marker = mi.group(0)  # resta nella pagina: la homepage legge da qui i dati della striscia Mercati
        giorno, righe = indici
        gd = datetime.date.fromisoformat(giorno)
        if gd != dt.date():
            ev.append('INDICI: la data %s non coincide con la data dell\'articolo %s' % (giorno, dt.date()))
        for sim, nome, chius, var in righe:
            chius, var = float(chius), float(var)
            prec = chius - var
            pct = var / prec * 100
            pts = serie(sim, chius, giorno)
            cl = 'pos' if var >= 0 else 'neg'
            fr = '▲' if var >= 0 else '▼'
            kp += ('<div class="kc2"><div class="kt"><b>%s</b><span class="kv2">%s</span><span class="%s">%s %s%%</span><small>Chiusura precedente %s</small></div>%s</div>'
                   % (nome, it(chius), cl, fr, it(pct, 2, True), it(prec), svg(pts, prec) if pts else ''))
            tick += '<span class="s"><b>%s</b>%s <span class="%s">%s %s%%</span></span>' % (nome, it(chius), cl, fr, it(pct, 2, True))
        tick = '<div class="tick"><div><span class="lv">%s <small>(chiusura %d %s)</small></span>%s</div></div>' % (
            d['cat_nome'], dt.day, MESI[dt.month - 1][:3], tick)
        kp = '<div class="kp">%s</div>' % kp
    # condivisione
    from urllib.parse import quote
    u, t = quote(d['canon'], safe=''), quote(testo(d['h1']), safe='')
    share = ('<span class="ic"><a href="https://www.linkedin.com/sharing/share-offsite/?url=%s" target="_blank" rel="noopener">LinkedIn</a>'
             '<a href="https://twitter.com/intent/tweet?url=%s&amp;text=%s" target="_blank" rel="noopener">X</a><button type="button" id="copia">Copia link</button></span>') % (u, u, t)
    sint_li = ''.join('<li>%s</li>' % x for x in sint)
    sint_card = '<div class="card"><h5>In sintesi</h5><ul>%s</ul></div>' % sint_li
    toc = '<div class="card toc"><h5>Indice dell\'articolo</h5>%s</div>' % ''.join('<a href="#%s">%s</a>' % (i, tt) for i, tt in sez)
    imp_card = ('<section class="imp"><span class="ico">🎓</span><h5>Impara: %s</h5><p>%s</p></section>' % impara) if impara else ''
    figura = ('<figure class="hero"><img src="%s" alt="%s" width="1200" height="560" loading="eager"><figcaption>%s</figcaption></figure>'
              % (d['img'], html.escape(d['alt']), html.escape(d['cap']))) if d['img'] else ''
    crumb = 'Home › ' if False else '<a href="index.html">Home</a> &nbsp;›&nbsp; '
    crumb += ('<a href="%s">%s</a>' % (pag, d['cat_nome']) if pag else d['cat_nome'])
    catl = ('<a href="%s">%s</a>' % (pag, d['cat_nome']) if pag else d['cat_nome'])
    sotto = '<span>%s</span>' % (d['cat_sotto'] + ' · ' + data_lunga if d['cat_sotto'] else data_lunga)
    nav = ''.join('<a href="%s">%s</a>' % (h, n_) for n_, h in NAV)
    corr = ''
    if correlati:
        corr = '<section class="more"><h3>Dalla stessa giornata</h3><div class="corr">%s</div></section>' % ''.join(
            '<a href="%s"><img src="%s" alt="" loading="lazy"><div class="c"><small>%s</small><h4>%s</h4></div></a>' % (f, im, c, t_) for f, c, t_, im in correlati)
    pagina = (
        MARK + '\n<div class="bar"></div>\n'
        '<header class="top"><div class="top-in"><a class="logo" href="index.html"><span class="a">A</span><span class="t">LMA FINANZA</span></a>'
        '<nav class="nv">%s</nav><div class="tools"><button class="tgl" onclick="toggleTheme()" title="Cambia tema" aria-label="Cambia tema">☀️</button></div></div></header>\n%s\n'
        '<div class="wrap"><div class="crumb">%s</div><div class="grid"><main>\n'
        '<div class="cat">%s%s</div><h1>%s</h1><p class="deck">%s</p>\n'
        '<div class="by"><span class="av">A</span><b>Redazione Alma Finanza</b><span>·</span><time datetime="%s">%s, %s</time><span>·</span><span>Lettura %s min</span><span class="sp"></span>%s</div>\n'
        '%s\n%s\n%s\n<div class="sint-m">%s</div>\n<div class="prose">\n%s\n</div></main>\n'
        '<aside class="rail">%s%s%s</aside></div>\n%s</div>\n'
        '<footer><a class="logo" href="index.html"><span class="a">A</span><span class="t">LMA FINANZA</span></a><p>%s</p></footer>\n'
        '<script src="articolo-d.js?v=%s"></script>\n') % (
        nav, tick, crumb, catl, sotto, d['h1'], d['deck'], d['dt'], data_lunga, dt.strftime('%H:%M'), d['min'], share,
        figura, kp, marker, sint_card, b, sint_card, toc, imp_card, corr, d['disclaimer'], CSS_V)
    # head: via Tailwind e stile inline, dentro il foglio condiviso e i font nuovi
    s = d['src']
    head = s[:s.index('</head>')]
    head = re.sub(r'<script src="https://cdn\.tailwindcss\.com"></script>\s*', '', head)
    head = re.sub(r'<script>tailwind\.config=.*?</script>\s*', '', head)
    head = re.sub(r'<style>.*?</style>\s*', '', head, flags=re.S)
    head = re.sub(r'<link href="https://fonts\.googleapis\.com/css2[^>]*>',
                  '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
                  '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Lobster&family=Manrope:wght@600;700;800&family=Montserrat:wght@900&display=swap" rel="stylesheet">'
                  '<link rel="stylesheet" href="articolo-d.css?v=%s">' % CSS_V, head, count=1)
    if 'articolo-d.css' not in head:
        raise ValueError('link dei font non trovato nell\'head')
    out = head + '</head>\n<body data-cat="%s">\n' % cat + pagina + '</body>\n</html>\n'
    info = {'sezioni': len(sez), 'sintesi': len(sint), 'indici': bool(indici), 'impara': bool(impara), 'foto': bool(d['img']), 'correlati': len(correlati), 'avvisi': ev}
    return out, info


def scheda_correlato(path):
    s = open(path, encoding='utf-8').read()
    h1 = testo(re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S).group(1))
    sec = re.search(r'article:section" content="([^"]+)"', s)
    im = re.search(r'src="(img/repertorio/[^"]+)"', s)
    return os.path.basename(path), html.unescape(sec.group(1)) if sec else '', h1, im.group(1) if im else ''


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    applica = '--applica' in sys.argv
    if not args:
        print(__doc__); sys.exit(1)
    letti, errori = [], 0
    for a in args:
        p = a if os.path.isabs(a) else os.path.abspath(a)
        try:
            d = leggi(p)
        except Exception as e:
            print('ERRORE', os.path.basename(p), '-', e); errori += 1; continue
        letti.append(d)
    schede = {}
    for d in letti:
        try:
            schede[d['path']] = scheda_correlato(d['path'])
        except Exception:
            pass
    for d in letti:
        nome = os.path.basename(d['path'])
        if MARK in d['src']:
            print('salto', nome, '(già in layout D)'); continue
        altri = [schede[x['path']] for x in letti if x['path'] != d['path'] and x['path'] in schede][:3]
        try:
            out, info = trasforma(d, [(f, c, t, im) for f, c, t, im in altri])
        except Exception as e:
            print('ERRORE', nome, '-', e); errori += 1; continue
        print('%s %s: %s | sezioni %d, sintesi %d, grafici indici %s, impara %s, foto %s, correlati %d' % (
            'scritto' if applica else 'ok   ', nome, d['cat_nome'], info['sezioni'], info['sintesi'], 'sì' if info['indici'] else 'no',
            'sì' if info['impara'] else 'no', 'sì' if info['foto'] else 'NO', info['correlati']))
        for av in info['avvisi']:
            print('   ATTENZIONE:', av)
        if applica:
            open(d['path'], 'w', encoding='utf-8').write(out)
    if errori:
        print('\n%d file con errori: non scritti.' % errori); sys.exit(2)
    if not applica:
        print('\nProva completata: nessun file scritto. Aggiungi --applica per scrivere.')


if __name__ == '__main__':
    main()
