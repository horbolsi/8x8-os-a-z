#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 8x8 OS A-Z documentation in EVERY common format technology knows.
Reads content.py (single source of truth). Outputs to ./formats/.
Signed: FlashTM8 ⚡️🌎🤖 | ©️8x8  — public-safe, zero secrets."""
import os, json, csv, datetime
from content import (SECTIONS, TRANSLATIONS, LIVE, SIGNATURE, PROJECT,
                     VERSION, BUILD_DATE, all_formats)

OUT = os.path.join(os.path.dirname(__file__), "formats")
os.makedirs(OUT, exist_ok=True)

def wrap(text, w):
    out, cur = [], ""
    for word in text.split():
        if len(cur) + len(word) + 1 > w:
            out.append(cur); cur = word
        else:
            cur = (cur + " " + word).strip()
    if cur: out.append(cur)
    return out

# ---------- Markdown ----------
def gen_md():
    L = []
    L.append(f"# {PROJECT} {VERSION} — A→Z Project Documentation\n")
    L.append(f"> {TRANSLATIONS['en']['tagline']}\n")
    L.append(f"**Build:** {BUILD_DATE}  |  **Signed:** {SIGNATURE}\n")
    L.append("---\n")
    L.append("## Live Audit Snapshot (read-only, anonymised)\n")
    for k, v in LIVE.items():
        L.append(f"- **{k.replace('_',' ').title()}**: {v}")
    L.append("\n---\n")
    L.append("## A → Z: The Complete Walkthrough\n")
    for letter, title, body in SECTIONS:
        L.append(f"### {letter}. {title}\n")
        L.append(body + "\n")
    L.append("---\n")
    L.append("## Supported Formats in this Package\n")
    L.append(", ".join(all_formats()))
    L.append("\n")
    L.append(f"_{SIGNATURE}_\n")
    p = os.path.join(OUT, "8x8-os-AZ.md"); open(p, "w", encoding="utf-8").write("\n".join(L))
    return p

# ---------- reStructuredText ----------
def gen_rst():
    L = []
    L.append(f"{PROJECT} {VERSION} — A to Z Documentation")
    L.append("=" * len(f"{PROJECT} {VERSION} — A to Z Documentation") + "\n")
    L.append(f".. note:: {TRANSLATIONS['en']['tagline']}\n")
    L.append(f"   Build: {BUILD_DATE} | Signed: {SIGNATURE}\n")
    L.append("\nLive Audit Snapshot\n------------------\n")
    for k, v in LIVE.items():
        L.append(f"- {k.replace('_',' ').title()}: {v}")
    L.append("\nA to Z Walkthrough\n-----------------\n")
    for letter, title, body in SECTIONS:
        L.append(f"{letter}. {title}\n{'~'* (len(title)+3)}\n")
        L.append(body + "\n")
    L.append("\n" + SIGNATURE + "\n")
    p = os.path.join(OUT, "8x8-os-AZ.rst"); open(p, "w", encoding="utf-8").write("\n".join(L))
    return p

# ---------- HTML ----------
def gen_html():
    rows = "".join(
        f"<tr><td class='ltr'>{l}</td><td><b>{t}</b></td><td>{b}</td></tr>"
        for l, t, b in SECTIONS)
    live = "".join(f"<li><b>{k.replace('_',' ').title()}</b>: {v}</li>" for k, v in LIVE.items())
    langs = "".join(
        f"<tr><td>{d['name']}</td><td>{d['title']}</td><td>{d['tagline']}</td></tr>"
        for code, d in TRANSLATIONS.items())
    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{PROJECT} {VERSION} — A→Z</title>
<style>
 body{{font-family:Segoe UI,DejaVu Sans,Arial,sans-serif;margin:0;background:#0a0a14;color:#e8e8ff}}
 header{{padding:40px;text-align:center;background:linear-gradient(135deg,#1a0a2a,#0a1a2a);border-bottom:2px solid #8a4aff}}
 h1{{font-size:2.4em;margin:0;color:#c08aff;text-shadow:0 0 20px #8a4aff}}
 .tag{{color:#7af;letter-spacing:2px}}
 .wrap{{max-width:1000px;margin:auto;padding:24px}}
 table{{width:100%;border-collapse:collapse;margin:18px 0}}
 th,td{{border:1px solid #33335a;padding:10px;text-align:left;vertical-align:top}}
 th{{background:#1a1a2e;color:#c08aff}}
 .ltr{{font-size:1.6em;color:#ff8a4a;font-weight:bold;width:40px}}
 .live{{background:#10101e;padding:18px;border-radius:10px}}
 footer{{text-align:center;padding:30px;color:#888;border-top:1px solid #333}}
</style></head>
<body><header><h1>{PROJECT} {VERSION}</h1>
<div class="tag">{TRANSLATIONS['en']['tagline']}</div>
<div>Signed: {SIGNATURE}</div></header>
<div class="wrap">
<h2>Live Audit Snapshot</h2><div class="live"><ul>{live}</ul></div>
<h2>A → Z Walkthrough</h2>
<table><tr><th>#</th><th>Topic</th><th>Description</th></tr>{rows}</table>
<h2>Multilingual (9 languages)</h2>
<table><tr><th>Language</th><th>Title</th><th>Tagline</th></tr>{langs}</table>
<p>Formats in this package: {', '.join(all_formats())}</p>
</div><footer>{SIGNATURE}</footer></body></html>"""
    p = os.path.join(OUT, "8x8-os-AZ.html"); open(p, "w", encoding="utf-8").write(html)
    return p

# ---------- man (groff) ----------
def gen_man():
    L = [".TH \"8X8OS\" \"1\" \"%s\" \"%s\" \"Sovereign AI OS\"" % (BUILD_DATE, PROJECT),
         ".SH NAME", f"{PROJECT.lower()} \\- Sovereign AI Operating System ({VERSION})",
         ".SH SYNOPSIS", f"{PROJECT} is a sovereign, autonomous, multi-agent AI operating system.",
         ".SH DESCRIPTION"]
    for letter, title, body in SECTIONS:
        L.append(f".TP")
        L.append(f"\\fB{letter}. {title}\\fR")
        L.append(body)
    L.append(".SH LIVE STATUS")
    for k, v in LIVE.items():
        L.append(f".TP\n\\fB{k.replace('_',' ').title()}\\fR\n{v}")
    L.append(".SH AUTHOR")
    L.append(SIGNATURE)
    L.append(".SH COPYRIGHT")
    L.append("©️ 8x8 — All rights reserved under the sovereign creator model.")
    p = os.path.join(OUT, "8x8-os-AZ.1"); open(p, "w", encoding="utf-8").write("\n".join(L) + "\n")
    return p

# ---------- JSON ----------
def gen_json():
    doc = {
        "project": PROJECT, "version": VERSION, "tagline": TRANSLATIONS['en']['tagline'],
        "build_date": BUILD_DATE, "signature": SIGNATURE,
        "live_audit": LIVE,
        "az_sections": [{"letter": l, "title": t, "body": b} for l, t, b in SECTIONS],
        "translations": TRANSLATIONS,
        "formats": all_formats(),
        "secret_policy": "zero external secret exposure; anonymous by default",
    }
    p = os.path.join(OUT, "8x8-os-AZ.json"); open(p, "w", encoding="utf-8").write(json.dumps(doc, ensure_ascii=False, indent=2))
    return p

# ---------- YAML ----------
def gen_yaml():
    def esc(s): return '"' + s.replace('"', "'") + '"'
    L = [f"project: {esc(PROJECT)}", f"version: {esc(VERSION)}",
         f"tagline: {esc(TRANSLATIONS['en']['tagline'])}", f"build_date: {esc(BUILD_DATE)}",
         f"signature: {esc(SIGNATURE)}", "live_audit:",]
    for k, v in LIVE.items(): L.append(f"  {k}: {v}")
    L.append("az_sections:")
    for l, t, b in SECTIONS:
        L.append(f"  - letter: {l}")
        L.append(f"    title: {esc(t)}")
        L.append(f"    body: {esc(b)}")
    L.append("translations:")
    for code, d in TRANSLATIONS.items():
        L.append(f"  {code}:")
        L.append(f"    name: {esc(d['name'])}")
        L.append(f"    title: {esc(d['title'])}")
        L.append(f"    tagline: {esc(d['tagline'])}")
        L.append(f"    intro: {esc(d['intro'])}")
    L.append("formats:")
    for f in all_formats(): L.append(f"  - {f}")
    p = os.path.join(OUT, "8x8-os-AZ.yaml"); open(p, "w", encoding="utf-8").write("\n".join(L) + "\n")
    return p

# ---------- CSV ----------
def gen_csv():
    p = os.path.join(OUT, "8x8-os-AZ.csv")
    with open(p, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh); w.writerow(["Letter", "Topic", "Description"])
        for l, t, b in SECTIONS: w.writerow([l, t, b])
    return p

# ---------- TXT ----------
def gen_txt():
    L = [f"{PROJECT} {VERSION} — A TO Z", "="*40,
         f"Tagline: {TRANSLATIONS['en']['tagline']}",
         f"Build: {BUILD_DATE}  Signed: {SIGNATURE}", ""]
    L.append("LIVE AUDIT SNAPSHOT"); L.append("-"*40)
    for k, v in LIVE.items(): L.append(f"  {k.replace('_',' ').title()}: {v}")
    L.append(""); L.append("A TO Z WALKTHROUGH"); L.append("-"*40)
    for l, t, b in SECTIONS:
        L.append(f"[{l}] {t}"); L.extend("  "+x for x in wrap(b, 72)); L.append("")
    L.append(SIGNATURE)
    p = os.path.join(OUT, "8x8-os-AZ.txt"); open(p, "w", encoding="utf-8").write("\n".join(L))
    return p

# ---------- PDF ----------
def _pdf_safe(t):
    # core PDF fonts are latin-1; replace fancy unicode + emoji with ASCII-safe
    repl = {"—": "-", "→": "->", "⚡": "*", "🌎": "", "🤖": "", "©️": "(c)", "█": "#",
            "░": ".", "│": "|", "─": "-", "┌": "+", "┐": "+", "└": "+", "┘": "+",
            "├": "+", "┤": "+", "⠋": "", "⠙": "", "⠹": "", "⠸": "", "⠼": "", "⠴": "",
            "⠦": "", "⠧": "", "⠇": "", "⠏": ""}
    for k, v in repl.items(): t = t.replace(k, v)
    return t.encode("latin-1", "replace").decode("latin-1")

def gen_pdf():
    from fpdf import FPDF
    p = os.path.join(OUT, "8x8-os-AZ.pdf")
    pdf = FPDF(format="A4"); pdf.set_auto_page_break(True, margin=15)
    pdf.set_margins(12, 12, 12)
    def mc(h, text, style="", size=10, r=30, g=30, b=40):
        pdf.set_x(12); pdf.set_font("Helvetica", style, size)
        pdf.set_text_color(r, g, b); pdf.multi_cell(0, h, _pdf_safe(text))
    pdf.add_page()
    mc(10, f"{PROJECT} {VERSION} - A to Z", "B", 20, 120, 60, 200)
    mc(6, TRANSLATIONS['en']['tagline'], "", 11, 40, 40, 60)
    mc(6, f"Build: {BUILD_DATE}    Signed: {SIGNATURE}", "", 11, 40, 40, 60)
    pdf.ln(2)
    mc(8, "Live Audit Snapshot", "B", 13, 80, 40, 150)
    for k, v in LIVE.items():
        mc(5, f"- {k.replace('_',' ').title()}: {v}")
    pdf.ln(2)
    for l, t, b in SECTIONS:
        if pdf.get_y() > 250: pdf.add_page()
        mc(7, f"{l}. {t}", "B", 12, 200, 80, 40)
        mc(5, b); pdf.ln(1)
    pdf.output(p); return p

if __name__ == "__main__":
    files = [gen_md(), gen_rst(), gen_html(), gen_man(), gen_json(),
             gen_yaml(), gen_csv(), gen_txt(), gen_pdf()]
    print("GENERATED:")
    for f in files: print("  ", os.path.relpath(f, OUT))
    print("FORMAT COUNT:", len(files))
