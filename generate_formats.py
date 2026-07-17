#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the full A-Z (micro->macro) project documentation in 9 formats.
Public-safe. Signed. From content.py (single source)."""
import os, json, csv, html
from content import PROJECT, VERSION, SIGNATURE, BUILD_DATE, CHAPTERS, GUIDANCE, ROADMAP, TRANSLATIONS, GLOBAL_VISION, FINGERPRINT

BASE = os.path.dirname(__file__)
OUT  = os.path.join(BASE, "formats"); os.makedirs(OUT, exist_ok=True)

def az_block_md():
    s = [f"# {PROJECT} {VERSION} — From Micro to Macro (A→Z)\n*{SIGNATURE}*\n"]
    s.append("A complete walkthrough of the system, from its smallest unit to the whole civilisation.\n")
    for n,t,b in CHAPTERS:
        s.append(f"## {n}. {t}\n{b}\n")
    s.append("## Guidance\n" + "\n".join(f"- **{h}**: {b}" for h,b in GUIDANCE))
    s.append("\n## Roadmap\n" + "\n".join(f"- **{h}**: {b}" for h,b in ROADMAP))
    s.append("\n## Global Vision — Every Sector, Every Topic, No Exception\nOn Earth and beyond:")
    s.append("\n".join(f"- **{h}**: {b}" for h,b in GLOBAL_VISION))
    s.append(f"\n\n## Artifact Fingerprint\n- Project ID: `{FINGERPRINT['project_id']}`\n- Edition: {FINGERPRINT['edition']}\n- Unique titles: " + "; ".join(FINGERPRINT['unique_titles']) + f"\n- {FINGERPRINT['fingerprint_note']}")
    s.append(f"\n\n---\n*{SIGNATURE}*")
    return "\n".join(s)

BODY = az_block_md()

# 1 MD
open(os.path.join(OUT,"8x8-os-AZ.md"),"w",encoding="utf-8").write(BODY)

# 2 RST
rst = ["="*60,"8x8 OS — From Micro to Macro (A→Z)","="*60,"",f"**{SIGNATURE}**","",
       "A complete walkthrough of the system, from its smallest unit to the whole civilisation.","",
       ".. contents::","",""]
for n,t,b in CHAPTERS:
    rst += [f"{n}. {t}","-"*40, b, ""]
rst += ["Guidance","-"*40]
rst += [f"{h}\n    {b}" for h,b in GUIDANCE] + [""]
rst += ["Roadmap","-"*40] + [f"{h}\n    {b}" for h,b in ROADMAP] + [""]
rst += ["Global Vision — Every Sector, Every Topic, No Exception","-"*40]
rst += ["On Earth and beyond:"] + [f"{h}\n    {b}" for h,b in GLOBAL_VISION] + [""]
rst += ["Artifact Fingerprint","-"*40]
rst += [f"Project ID: {FINGERPRINT['project_id']}", f"Edition: {FINGERPRINT['edition']}",
        "Unique titles: " + "; ".join(FINGERPRINT['unique_titles']), FINGERPRINT['fingerprint_note']]
rst += ["", SIGNATURE]
open(os.path.join(OUT,"8x8-os-AZ.rst"),"w",encoding="utf-8").write("\n".join(rst))

# 3 HTML
rows = "".join(f"<section class='ch'><h2>{n}. {html.escape(t)}</h2><p>{html.escape(b)}</p></section>" for n,t,b in CHAPTERS)
grows= "".join(f"<li><b>{html.escape(h)}</b> — {html.escape(b)}</li>" for h,b in GUIDANCE)
rrows= "".join(f"<li><b>{html.escape(h)}</b> — {html.escape(b)}</li>" for h,b in ROADMAP)
vrows= "".join(f"<li><b>{html.escape(h)}</b> — {html.escape(b)}</li>" for h,b in GLOBAL_VISION)
html_doc=f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>{PROJECT} {VERSION} — A→Z</title>
<style>body{{background:#0a0a14;color:#e8e8f0;font-family:system-ui;max-width:900px;margin:auto;padding:40px}}
h1{{color:#c08aff}} .ch{{border-left:3px solid #ff8a4a;padding:8px 18px;margin:14px 0}}
h2{{color:#b388ff}} a{{color:#4a90ff}} .sign{{color:#ffb450;text-align:center;margin-top:30px}}
.fp{{background:#12122a;border:1px solid #ff8a4a;padding:14px 18px;border-radius:8px;margin-top:20px}}</style></head>
<body><h1>{PROJECT} {VERSION} — From Micro to Macro (A→Z)</h1>
<p class="sign">{SIGNATURE}</p>{rows}
<h2>Guidance</h2><ul>{grows}</ul><h2>Roadmap</h2><ul>{rrows}</ul>
<h2>Global Vision — Every Sector, Every Topic, No Exception (on Earth &amp; beyond)</h2><ul>{vrows}</ul>
<div class="fp"><b>Artifact Fingerprint</b><br>Project ID: {FINGERPRINT['project_id']}<br>Edition: {FINGERPRINT['edition']}<br>
Unique titles: {html.escape('; '.join(FINGERPRINT['unique_titles']))}<br>{html.escape(FINGERPRINT['fingerprint_note'])}</div>
<p class="sign">{SIGNATURE}</p></body></html>"""
open(os.path.join(OUT,"8x8-os-AZ.html"),"w",encoding="utf-8").write(html_doc)

# 4 MAN
man = [".TH \"8X8-OS-AZ\" \"1\" \"\" \"{PROJECT} {VERSION}\"",".SH NAME",
       "8x8-os-az \\- from micro to macro reference",".SH DESCRIPTION",
       f"{PROJECT} {VERSION} — a sovereign, autonomous, multi-agent AI operating system.",
       "This page walks the system from its smallest unit to the whole civilisation.",""]
for n,t,b in CHAPTERS:
    man += [f".SH {n}. {t}", b, ""]
man += [".SH GUIDANCE"] + [f"{h}: {b}" for h,b in GUIDANCE] + [".SH ROADMAP"] + [f"{h}: {b}" for h,b in ROADMAP]
man += [".SH GLOBAL VISION","Every sector, every topic, no exception — on Earth and beyond:"]
man += [f"{h}: {b}" for h,b in GLOBAL_VISION]
man += [".SH ARTIFACT FINGERPRINT", f"Project ID: {FINGERPRINT['project_id']}",
        f"Edition: {FINGERPRINT['edition']}", "Unique titles: " + "; ".join(FINGERPRINT['unique_titles']),
        FINGERPRINT['fingerprint_note']]
man += ["",".SH SIGNATURE", SIGNATURE]
open(os.path.join(OUT,"8x8-os-AZ.1"),"w",encoding="utf-8").write("\n".join(man))

# 5 JSON
data={"project":PROJECT,"version":VERSION,"signature":SIGNATURE,"build":BUILD_DATE,
      "chapters":[{"n":n,"title":t,"body":b} for n,t,b in CHAPTERS],
      "guidance":[{"head":h,"body":b} for h,b in GUIDANCE],
      "roadmap":[{"phase":h,"body":b} for h,b in ROADMAP],
      "global_vision":[{"sector":h,"body":b} for h,b in GLOBAL_VISION],
      "fingerprint":FINGERPRINT,
      "languages":list(TRANSLATIONS.keys())}
open(os.path.join(OUT,"8x8-os-AZ.json"),"w",encoding="utf-8").write(json.dumps(data,ensure_ascii=False,indent=2))

# 6 YAML
yaml=[f"project: {PROJECT}","version: {VERSION}","signature: \"{SIGNATURE}\"","build: {BUILD_DATE}","chapters:"]
for n,t,b in CHAPTERS:
    yaml += [f"  - n: {n}","    title: \"{t}\"",f"    body: \"{b.replace(chr(34),'')}\""]
yaml += ["guidance:"] + [f"  - head: \"{h}\"\n    body: \"{b.replace(chr(34),'')}\"" for h,b in GUIDANCE]
yaml += ["roadmap:"] + [f"  - phase: \"{h}\"\n    body: \"{b.replace(chr(34),'')}\"" for h,b in ROADMAP]
yaml += ["global_vision:"] + [f"  - sector: \"{h}\"\n    body: \"{b.replace(chr(34),'')}\"" for h,b in GLOBAL_VISION]
yaml += ["fingerprint:","  project_id: \""+FINGERPRINT['project_id']+"\"","  edition: \""+FINGERPRINT['edition']+"\"",
         "  unique_titles:","  - "+"\n  - ".join(FINGERPRINT['unique_titles']),"  note: \""+FINGERPRINT['fingerprint_note'].replace(chr(34),'')+"\""]
open(os.path.join(OUT,"8x8-os-AZ.yaml"),"w",encoding="utf-8").write("\n".join(yaml))

# 7 CSV
with open(os.path.join(OUT,"8x8-os-AZ.csv"),"w",encoding="utf-8",newline="") as f:
    w=csv.writer(f); w.writerow(["type","key","title","body"])
    for n,t,b in CHAPTERS: w.writerow(["chapter",n,t,b])
    for h,b in GUIDANCE: w.writerow(["guidance","",h,b])
    for h,b in ROADMAP: w.writerow(["roadmap",h,"",b])
    for h,b in GLOBAL_VISION: w.writerow(["global_vision",h,"",b])
    w.writerow(["fingerprint","project_id","",FINGERPRINT['project_id']])
    w.writerow(["fingerprint","edition","",FINGERPRINT['edition']])
    w.writerow(["fingerprint","unique_titles","","; ".join(FINGERPRINT['unique_titles'])])

# 8 TXT (plain, signed)
open(os.path.join(OUT,"8x8-os-AZ.txt"),"w",encoding="utf-8").write(BODY)

# 9 PDF (fpdf2, latin-1 safe)
try:
    from fpdf import FPDF
    def safe(s):
        s=s.replace("\u2014","-").replace("\u2013","-").replace("\u2019","'").replace("\u201c",'"').replace("\u201d",'"')
        return s.encode("latin-1","replace").decode("latin-1")
    class P(FPDF):
        def header(self):
            self.set_font("Helvetica","B",9); self.set_text_color(160,120,255)
            self.cell(0,6,safe(f"{PROJECT} {VERSION} — A to Z"),0,0,"R"); self.ln(8)
        def footer(self):
            self.set_y(-12); self.set_font("Helvetica","I",8); self.set_text_color(255,180,80)
            self.cell(0,6,safe(SIGNATURE),0,0,"C")
    p=P(); p.set_margins(15,15,15); p.set_auto_page_break(True,18); p.add_page(); p.set_text_color(20,20,30)
    p.set_font("Helvetica","B",16); p.set_text_color(160,120,255)
    p.set_x(15); p.multi_cell(0,8,safe(f"{PROJECT} {VERSION} — From Micro to Macro (A to Z)")); p.ln(2)
    p.set_text_color(40,40,60)
    for n,t,b in CHAPTERS:
        if p.get_y()>255: p.add_page()
        p.set_x(15); p.set_font("Helvetica","B",12); p.set_text_color(140,90,255); p.multi_cell(0,6,safe(f"{n}. {t}"))
        p.set_x(15); p.set_font("Helvetica","",10); p.set_text_color(40,40,60); p.multi_cell(0,5,safe(b)); p.ln(1)
    p.add_page(); p.set_x(15); p.set_font("Helvetica","B",13); p.set_text_color(255,138,74)
    p.multi_cell(0,6,"Roadmap"); p.set_font("Helvetica","",10)
    for h,b in ROADMAP:
        if p.get_y()>255: p.add_page()
        p.set_x(15); p.multi_cell(0,5,safe(f"- {h}: {b}"))
    p.ln(1); p.set_x(15); p.set_font("Helvetica","B",13); p.set_text_color(255,138,74)
    p.multi_cell(0,6,"Global Vision - Every Sector, Every Topic, No Exception (on Earth & beyond)")
    p.set_font("Helvetica","",10)
    for h,b in GLOBAL_VISION:
        if p.get_y()>255: p.add_page()
        p.set_x(15); p.multi_cell(0,5,safe(f"- {h}: {b}"))
    p.ln(1); p.set_x(15); p.set_font("Helvetica","B",13); p.set_text_color(255,138,74)
    p.multi_cell(0,6,"Artifact Fingerprint")
    p.set_font("Helvetica","",10); p.set_x(15)
    p.multi_cell(0,5,safe(f"Project ID: {FINGERPRINT['project_id']}"))
    p.set_x(15); p.multi_cell(0,5,safe(f"Edition: {FINGERPRINT['edition']}"))
    p.set_x(15); p.multi_cell(0,5,safe("Unique titles: " + "; ".join(FINGERPRINT['unique_titles'])))
    p.set_x(15); p.multi_cell(0,5,safe(FINGERPRINT['fingerprint_note']))
    p.ln(1); p.set_x(15); p.set_font("Helvetica","B",13); p.set_text_color(255,138,74)
    p.multi_cell(0,6,"Roadmap"); p.set_font("Helvetica","",10)
    for h,b in ROADMAP:
        if p.get_y()>255: p.add_page()
        p.set_x(15); p.multi_cell(0,5,safe(f"- {h}: {b}"))
    p.output(os.path.join(OUT,"8x8-os-AZ.pdf"))
    print("PDF_OK")
except Exception as e:
    print("PDF skip:",repr(e))

print("FORMATS_DONE:", sorted(os.listdir(OUT)))
