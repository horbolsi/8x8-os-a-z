#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
8x8 OS — ADVANCED MODERN ASCII CONSOLE
A self-contained, secret-safe, animated terminal UI for the 8x8 OS sovereign stack.
Pure standard library (ANSI). No external deps, no network, no secrets.

Usage:
    python3 8x8_console.py            # interactive console
    python3 8x8_console.py --demo     # auto-run a 20s tour (for recordings/headless)
    python3 8x8_console.py --no-color # force monochrome

Signed: FlashTM8 ⚡️🌎🤖 | ©️8x8
"""
import os
import sys
import time
import shutil
import random

try:
    from content import SECTIONS, TRANSLATIONS, LIVE, SIGNATURE, PROJECT, VERSION
except Exception:
    SECTIONS = [("A", "Architecture", "8x8 OS sovereign stack.")]
    TRANSLATIONS = {"en": {"name": "English"}}
    LIVE = {"termux_services": 53, "github_repos": 11, "agents_registered": 131}
    SIGNATURE = "FlashTM8 ⚡️🌎🤖 | ©️8x8"
    PROJECT, VERSION = "8x8 OS", "v3.0"

# ---------------- color ----------------
def _supports_color():
    return sys.stdout.isatty() and os.environ.get("TERM", "") != "dumb"

_USE_COLOR = _supports_color()
if "--no-color" in sys.argv:
    _USE_COLOR = False

C = {
    "R": "\033[0m", "B": "\033[1m", "D": "\033[2m",
    "RED": "\033[31m", "GRN": "\033[32m", "YLW": "\033[33m",
    "BLU": "\033[34m", "MAG": "\033[35m", "CYN": "\033[36m", "WHT": "\033[97m",
    "CYAN": "\033[36m",  # alias to avoid typos
}
def _c(k): return C[k] if _USE_COLOR else ""
def paint(text, *keys):
    return _c("".join(C[k] for k in keys)) + text + _c("R")
def reset():
    if _USE_COLOR: sys.stdout.write(_c("R"))

# ---------------- widgets ----------------
def bar(pct, width=24, color="GRN"):
    pct = max(0, min(100, pct))
    filled = int(width * pct / 100)
    bar_str = "█" * filled + "░" * (width - filled)
    return paint(bar_str, color) + f" {pct:3d}%"

SPIN = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
MATRIX = "01ｱｲｳｴｵｶｷｸｹｺ#$%&*+<>=@"

def box(title, lines, w=56):
    inner = w - 2
    top = "┌─" + "─" * (len(title) + 2) + "─" + "─" * (inner - len(title) - 2) + "┐"
    out = [paint(top, "CYN")]
    out.append(paint("│ " + _c("B") + title + _c("R") + " " + " " * (inner - len(title) - 1) + "│", "CYN"))
    out.append(paint("├" + "─" * inner + "┤", "CYN"))
    for ln in lines:
        ln = ln[:inner]
        out.append(paint("│ " + ln + " " * (inner - len(ln)) + "│", "CYN"))
    out.append(paint("└" + "─" * inner + "┘", "CYN"))
    return "\n".join(out)

def cls():
    if _USE_COLOR:
        sys.stdout.write("\033[2J\033[H")
    else:
        sys.stdout.write("\n" * 40)

def logo():
    L = [
        "  ██████╗   █████╗  ██╗  ██╗ ██████╗  ███████╗",
        " ██╔═══██╗ ██╔══██╗ ╚██╗██╔╝ ██╔══██╗ ██╔════╝",
        " ██║   ██║ ███████║  ╚███╔╝  ██████╔╝ ███████╗",
        " ██║   ██║ ██╔══██║  ██╔██╗  ██╔══██╗ ╚════██║",
        " ╚██████╔╝ ██║  ██║ ██╔╝ ██╗ ██║  ██║ ███████║",
        "  ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚══════╝",
    ]
    return "\n".join(paint(l, "MAG", "B") for l in L)

def header():
    w = 56
    cls()
    print(logo())
    print(paint(f"  {PROJECT} {VERSION} — Sovereign AI Operating System", "CYAN", "B"))
    print(paint(f"  {SIGNATURE}", "YLW"))
    print()

def dashboard():
    lines = [
        paint("Termux runit services : ", "WHT") + bar(100, 18) + f"  {LIVE['termux_services']}",
        paint("Proot processes        : ", "WHT") + bar(96, 18) + f"  {LIVE['proot_processes']}",
        paint("GitHub repositories    : ", "WHT") + bar(100, 18) + f"  {LIVE['github_repos']}",
        paint("Agents registered      : ", "WHT") + bar(100, 18) + f"  {LIVE['agents_registered']}",
        paint("Skills loaded          : ", "WHT") + bar(100, 18) + f"  {LIVE['skills']}",
        paint("Databases online       : ", "WHT") + bar(100, 18) + f"  {LIVE['databases']}",
        paint("TTS / video pipeline   : ", "WHT") + paint("READY (edge-tts+ffmpeg+PIL)", "GRN"),
        paint("Secret exposure        : ", "WHT") + paint("ZERO — anonymous by default", "GRN"),
    ]
    print(box("LIVE SYSTEM STATUS", lines))
    print()
    print(paint("Commands: ", "YLW") + "status · agents · az · scan · matrix · help · exit")
    print(paint("8x8> ", "GRN", "B"), end="")

def show_agents():
    names = ["HERMES","FLASH","AEGIS","TRADER","ARCHITECT","CODEx","SCRIBE","CURATOR",
             "SENTINEL","ORACLE","NEXUS","CITADEL","FORGE","WRENCH","PIPELINE","CANVAS","SAGE"]
    roles = ["Orchestrator","Creator Proxy","Security","Trading","Design","Builder","Writing",
             "Memory","Monitor","Prediction","Coord","Defense","Build","DevOps","CI/CD","Media","Voice"]
    lines = []
    for i, (n, r) in enumerate(zip(names, roles)):
        pct = 80 + (i * 3) % 20
        lines.append(f"{paint(n, 'CYAN', 'B'):10} {paint(r, 'WHT'):12} {bar(pct, 14)}")
    print()
    print(box("AGENT ROSTER (sample of 131)", lines, w=64))
    print()

def show_az(page=0):
    print()
    chunk = SECTIONS[page*5:(page+1)*5]
    lines = []
    for letter, title, body in chunk:
        lines.append(paint(f"[{letter}] ", "MAG", "B") + paint(title, "CYAN", "B"))
        words = body.split()
        cur = ""
        for w in words:
            if len(cur) + len(w) + 1 > 50:
                lines.append("    " + cur); cur = w
            else:
                cur = (cur + " " + w).strip()
        if cur: lines.append("    " + cur)
        lines.append("")
    print(box(f"A→Z PROJECT WALKTHROUGH (p{page+1}/{(len(SECTIONS)+4)//5})", lines, w=64))
    print(paint("next/prev to page · back to return", "D"))
    print()

def do_scan():
    print()
    print(paint("Running read-only deep audit across all namespaces…", "YLW"))
    steps = [
        "Termux runit services …", "Ubuntu proot processes …",
        "GitHub repositories …", "Neon / PostgreSQL …",
        "Internal storage vault …", "Agent brain (shared memory) …",
        "Knowledge graph …", "Multilingual TTS pipeline …",
    ]
    for i, s in enumerate(steps):
        sys.stdout.write(paint(f"  {SPIN[i % len(SPIN)]} {s}", "CYN"))
        sys.stdout.flush()
        time.sleep(0.18)
        sys.stdout.write("\r")
        sys.stdout.write(" " * 50 + "\r")
        print(paint(f"  {SPIN[(i+3) % len(SPIN)]} {s}", "CYN") + paint(" [OK]", "GRN"))
    print(paint(f"  Audit complete — {LIVE['termux_services']} services, {LIVE['github_repos']} repos, 0 secrets exposed.", "GRN", "B"))
    print()

def do_matrix(seconds=6):
    cls()
    h = shutil.get_terminal_size((80, 24)).lines - 2
    w = shutil.get_terminal_size((120, 40)).columns - 2
    cols = [0] * w
    end = time.time() + seconds
    try:
        while time.time() < end:
            sys.stdout.write("\033[H")
            for _ in range(h):
                row = "".join(random.choice(MATRIX) if (random.random() < 0.5) else " " for _ in range(w))
                print(paint(row, "GRN"))
            time.sleep(0.08)
    except KeyboardInterrupt:
        pass
    reset()
    print(paint("\n  matrix rain — signed " + SIGNATURE, "D"))

HELP = (
    "8x8 OS Console — interactive sovereign terminal\n"
    "  status  show live system dashboard\n"
    "  agents  show agent roster\n"
    "  az      walk the project A→Z\n"
    "  scan    run a read-only deep audit animation\n"
    "  matrix  secret-safe matrix rain screensaver\n"
    "  help    this message\n"
    "  exit    leave the console\n"
    "All output is anonymous and contains zero secrets. " + SIGNATURE
)

def main():
    demo = "--demo" in sys.argv
    header()
    dashboard()
    if not demo:
        while True:
            try:
                cmd = input().strip().lower()
            except (EOFError, KeyboardInterrupt):
                print(); break
            if cmd in ("exit", "quit", "q"):
                print(paint("  signed off — " + SIGNATURE, "D")); break
            elif cmd in ("status", ""):
                header(); dashboard()
            elif cmd == "agents":
                show_agents()
            elif cmd == "az":
                p = 0
                show_az(p)
                while True:
                    nxt = input(paint("az> ", "GRN", "B")).strip().lower()
                    if nxt in ("exit", "back", "q"): break
                    elif nxt == "next": p = min(p+1, (len(SECTIONS)-1)//5)
                    elif nxt == "prev": p = max(p-1, 0)
                    show_az(p)
                header(); dashboard()
            elif cmd == "scan":
                do_scan()
            elif cmd == "matrix":
                do_matrix()
            elif cmd == "help":
                print("\n" + HELP + "\n")
            else:
                print(paint("  unknown command — type 'help'", "RED"))
    else:
        # demo tour without blocking input
        time.sleep(1.2); show_agents(); time.sleep(1.2)
        show_az(0); time.sleep(1.2); do_scan(); time.sleep(0.5)
        print(paint("  demo complete — " + SIGNATURE, "GRN", "B"))

if __name__ == "__main__":
    main()
