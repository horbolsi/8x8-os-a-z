# Quick Start
FlashTM8 ⚡️🌎🤖 | ©️8x8

## Prerequisites
- Linux (Termux + Ubuntu proot on Android, or any Linux)
- Python 3.11+
- ffmpeg, git

## 1. Clone
```bash
git clone https://github.com/horbolsi/8x8-os-a-z
cd 8x8-os-a-z
```

## 2. Run the ASCII console
```bash
python3 8x8_console.py --demo     # auto tour
python3 8x8_console.py            # interactive
```
Commands: `status · agents · az · scan · matrix · help · exit`

## 3. Explore the docs
- `formats/` — the full A–Z reference in 9 file formats
- `studio/` — 9-language subtitles + video description
- `docs/` — this product guide

## 4. (Optional) Self-host the fleet
The production runtime uses `runit` for process supervision and `cloudflared`
for public tunnels. See the architecture doc for the service map.

_FlashTM8 ⚡️🌎🤖 | ©️8x8_
