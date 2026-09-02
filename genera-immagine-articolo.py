#!/usr/bin/env python3
"""
Genera l'immagine di apertura di un articolo di Alma Finanza.

Produce un JPG 1200x630 (retina 2x) coerente con l'identità del sito:
la A in Lobster color teal, i titoli in Montserrat, il corpo in Inter.
L'immagine si costruisce dai dati dell'articolo — nessuna foto esterna,
nessun problema di copyright.

Uso tipico (dal Master Prompt di aggiornamento quotidiano):

    python3 genera-immagine-articolo.py \
        --slug articolo-geopolitica-1set-iran-usa-hormuz \
        --categoria "Geopolitica" \
        --colore red \
        --occhiello "Stretto di Hormuz" \
        --titolo "USA colpiscono i Pasdaran: il Brent vola a 92 dollari" \
        --numero "\\$92" --numero-label "Brent" --numero-var "+4,50%" \
        --dato "S&P 500|−0,30%|down" \
        --dato "FTSE MIB|−1,33%|down" \
        --dato "WTI|+4,54%|up"

L'immagine finisce in img/articoli/<slug>.jpg
"""

import argparse
import pathlib
import subprocess
import sys
import tempfile

# Palette per categoria — gli stessi colori dei banner degli articoli
PALETTE = {
    "blue":    ("#1e40af", "#3b82f6", "#dbeafe"),   # Wall Street
    "emerald": ("#047857", "#10b981", "#d1fae5"),   # Piazza Affari
    "red":     ("#b91c1c", "#ef4444", "#fee2e2"),   # Macro / Geopolitica
    "amber":   ("#b45309", "#f59e0b", "#fef3c7"),   # Commodities / Energia
    "purple":  ("#6d28d9", "#8b5cf6", "#ede9fe"),   # Tech / AI
    "sky":     ("#0369a1", "#0ea5e9", "#e0f2fe"),   # Corporate
}

TEMPLATE = """<!DOCTYPE html>
<html lang="it"><head><meta charset="UTF-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800;900&family=Inter:wght@400;500;600;700&family=Lobster&display=swap');
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1200px;height:630px;overflow:hidden;font-family:'Inter',sans-serif;background:#0f172a}}
.card{{width:1200px;height:630px;display:flex;position:relative;background:
   radial-gradient(1100px 520px at 82% 18%, {glow}22 0%, transparent 62%), #0f172a}}
.card:before{{content:"";position:absolute;inset:0;
   background-image:linear-gradient({dark}0e 1px,transparent 1px),linear-gradient(90deg,{dark}0e 1px,transparent 1px);
   background-size:44px 44px}}
.left{{width:{leftw}%;padding:56px 40px 100px 56px;display:flex;flex-direction:column;justify-content:center;position:relative;z-index:2}}
.brand{{position:absolute;left:56px;bottom:44px}}
.top{{display:flex;align-items:center;gap:12px;flex-wrap:wrap}}
.tag{{background:{dark};color:#fff;font-family:'Montserrat',sans-serif;font-weight:800;font-size:13px;
   letter-spacing:1.5px;text-transform:uppercase;padding:7px 15px;border-radius:6px}}
.eyebrow{{color:#94a3b8;font-size:14.5px;font-weight:600;letter-spacing:.4px}}
.title{{font-family:'Montserrat',sans-serif;font-weight:900;font-size:{fsize}px;line-height:1.07;
   color:#f8fafc;margin-top:26px;letter-spacing:-.5px}}
.rule{{width:64px;height:4px;background:{glow};border-radius:2px;margin-top:22px}}
.data{{display:flex;gap:11px;margin-top:24px;flex-wrap:wrap}}
.chip{{background:rgba(255,255,255,.055);border:1px solid {glow}33;border-radius:10px;padding:10px 14px;min-width:112px}}
.chip .k{{color:#94a3b8;font-size:11px;font-weight:600;letter-spacing:.4px;text-transform:uppercase}}
.chip .v{{font-family:'Montserrat',sans-serif;font-weight:800;font-size:19px;margin-top:2px;font-variant-numeric:tabular-nums}}
.up{{color:#34d399}} .down{{color:#f87171}} .flat{{color:#e2e8f0}}
.brand{{display:flex;align-items:center;gap:10px}}
.brand .a{{font-family:'Lobster',cursive;font-size:34px;color:#14B8A6;line-height:1}}
.brand .n{{font-family:'Montserrat',sans-serif;font-weight:800;font-size:20px;color:#f8fafc}}
.brand .n span{{color:#14B8A6}}
.brand .d{{color:#64748b;font-size:13px;font-weight:600;margin-left:4px}}
.right{{width:{rightw}%;display:flex;flex-direction:column;align-items:center;justify-content:center;
   position:relative;z-index:2;padding:40px 44px;border-left:1px solid rgba(255,255,255,.07);
   background:linear-gradient(180deg,{glow}0d,transparent)}}
.big{{font-family:'Montserrat',sans-serif;font-weight:900;font-size:{bsize}px;color:#fff;line-height:.94;
   letter-spacing:-2px;text-align:center;font-variant-numeric:tabular-nums}}
.blabel{{font-family:'Montserrat',sans-serif;font-weight:700;font-size:15px;color:{light};
   letter-spacing:1.4px;text-transform:uppercase;margin-top:14px;text-align:center}}
.bvar{{margin-top:12px;font-family:'Montserrat',sans-serif;font-weight:800;font-size:21px;
   padding:6px 16px;border-radius:999px;background:rgba(255,255,255,.08)}}
</style></head><body>
<div class="card">
  <div class="left">
    <div>
      <div class="top"><span class="tag">{categoria}</span>{eyebrow_html}</div>
      <div class="title">{titolo}</div>
      <div class="rule"></div>
      {chips_html}
    </div>
    <div class="brand"><span class="a">A</span><span class="n">Alma <span>Finanza</span></span><span class="d">almafinanza.com</span></div>
  </div>
  {right_html}
</div></body></html>"""


def build_html(args):
    dark, glow, light = PALETTE.get(args.colore, PALETTE["blue"])

    eyebrow_html = f'<span class="eyebrow">{args.occhiello}</span>' if args.occhiello else ""

    chips = []
    for d in args.dato or []:
        parts = [p.strip() for p in d.split("|")]
        if len(parts) < 2:
            continue
        k, v = parts[0], parts[1]
        cls = parts[2] if len(parts) > 2 else "flat"
        if cls not in ("up", "down", "flat"):
            cls = "flat"
        chips.append(f'<div class="chip"><div class="k">{k}</div><div class="v {cls}">{v}</div></div>')
    chips_html = f'<div class="data">{"".join(chips)}</div>' if chips else ""

    if args.numero:
        var_html = f'<div class="bvar {args.numero_dir}">{args.numero_var}</div>' if args.numero_var else ""
        right_html = (
            f'<div class="right"><div class="big">{args.numero}</div>'
            f'<div class="blabel">{args.numero_label or ""}</div>{var_html}</div>'
        )
        leftw, rightw = 63, 37
    else:
        right_html = ""
        leftw, rightw = 100, 0

    n = len(args.titolo)
    fsize = 50 if n <= 58 else (44 if n <= 82 else (39 if n <= 108 else 34))
    bn = len(args.numero or "")
    bsize = 92 if bn <= 5 else (76 if bn <= 7 else 62)

    return TEMPLATE.format(
        dark=dark, glow=glow, light=light,
        categoria=args.categoria.upper(), eyebrow_html=eyebrow_html,
        titolo=args.titolo, chips_html=chips_html, right_html=right_html,
        leftw=leftw, rightw=rightw, fsize=fsize, bsize=bsize,
    )


def main():
    ap = argparse.ArgumentParser(description="Genera l'immagine di apertura di un articolo Alma Finanza")
    ap.add_argument("--slug", required=True, help="nome del file senza estensione")
    ap.add_argument("--categoria", required=True, help="es. Wall Street, Piazza Affari, Macro")
    ap.add_argument("--colore", default="blue", choices=sorted(PALETTE), help="palette della categoria")
    ap.add_argument("--titolo", required=True, help="titolo breve, 40-110 caratteri")
    ap.add_argument("--occhiello", default="", help="testo piccolo accanto alla categoria")
    ap.add_argument("--numero", default="", help="dato principale, es. $92 o −1,33%%")
    ap.add_argument("--numero-label", dest="numero_label", default="", help="didascalia del dato principale")
    ap.add_argument("--numero-var", dest="numero_var", default="", help="variazione, es. +4,50%%")
    ap.add_argument("--numero-dir", dest="numero_dir", default="flat", choices=["up", "down", "flat"])
    ap.add_argument("--dato", action="append", help='riquadro "Etichetta|Valore|up|down|flat" (ripetibile)')
    ap.add_argument("--outdir", default="img/articoli")
    args = ap.parse_args()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("Manca Playwright. Installalo con:  pip install playwright && playwright install chromium")

    outdir = pathlib.Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    out = outdir / f"{args.slug}.jpg"

    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as fh:
        fh.write(build_html(args))
        tmp = fh.name

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
        page.goto(pathlib.Path(tmp).resolve().as_uri())
        page.wait_for_timeout(1400)
        page.screenshot(path=str(out), type="jpeg", quality=92,
                        clip={"x": 0, "y": 0, "width": 1200, "height": 630})
        browser.close()

    pathlib.Path(tmp).unlink(missing_ok=True)
    print(f"✅ {out}")


if __name__ == "__main__":
    main()
