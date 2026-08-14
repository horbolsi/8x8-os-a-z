#!/usr/bin/env python3
"""Fail closed if private One-Fabric operational material enters public A→Z guidance."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
EXCLUDED = {SELF, ROOT / ".github" / "workflows" / "validate-public-guidance-boundary.yml"}

TEXT_PATTERNS = {
    "private_root_path": re.compile(r"/root/(?:8x8|trading_venv|\.hermes)", re.I),
    "private_android_path": re.compile(r"/data/data/com\.termux", re.I),
    "private_runtime_dir": re.compile(r"(?:^|[\\/])\.hermes(?:[\\/]|$)", re.I),
    "private_db": re.compile(r"\b(?:state|agent_brain|agent_bus|trades|telegram_intel|discord_intel)\.db\b", re.I),
    "private_repo": re.compile(r"\bhorbolsi/(?:8x8-os-june2026|8x8-memory|8x8-os-private|8x8-OS-unified)\b", re.I),
    "protected_deploy_id": re.compile(r"\bdpl_[A-Za-z0-9]{16,}\b"),
    "private_key": re.compile(r"BEGIN (?:RSA|OPENSSH|EC) PRIVATE KEY"),
    "credential_token": re.compile(r"\b(?:gh[opsu]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,})\b"),
    "credential_assignment": re.compile(r"(?mi)^\s*(?:ADMIN_SECRET|TG_BOT_TOKEN|BITGET_SECRET_KEY|BITGET_PASSPHRASE|OPENROUTER_API_KEY|ELEVENLABS_API_KEY|FAL_KEY)\s*=\s*[^\s#]+"),
}
BYTE_PATTERNS = {k: re.compile(v.pattern.encode(), v.flags) for k, v in TEXT_PATTERNS.items() if k != "credential_assignment"}


def tracked() -> list[Path]:
    raw = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT)
    return [ROOT / p for p in raw.decode().split("\0") if p]


def main() -> int:
    violations: list[str] = []
    seen = 0
    for path in tracked():
        if not path.is_file() or path in EXCLUDED:
            continue
        seen += 1
        rel = path.relative_to(ROOT).as_posix()
        data = path.read_bytes()
        if b"\x00" not in data:
            try:
                text = data.decode("utf-8", errors="strict")
            except UnicodeDecodeError:
                text = ""
            if text:
                for label, pattern in TEXT_PATTERNS.items():
                    if pattern.search(text):
                        violations.append(f"{label}: {rel}")
                continue
        for label, pattern in BYTE_PATTERNS.items():
            if pattern.search(data):
                violations.append(f"binary_{label}: {rel}")

    if violations:
        print("PUBLIC_GUIDANCE_BOUNDARY=FAIL")
        for item in sorted(set(violations)):
            print(f"- {item}")
        return 1
    print(f"PUBLIC_GUIDANCE_BOUNDARY=PASS scanned={seen}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
