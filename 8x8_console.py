#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""©️8x8 by FlashTM8 ⚡️🌎🤖 — public product terminal demo.

This file is intentionally PUBLIC-SAFE. It demonstrates the user-facing idea
of an 8x8 Terminal without exposing or reproducing the private One-Fabric
runtime, agent roster, service topology, repositories, credentials, private
paths, owner controls or operational telemetry.

Everything shown here is a product/demo fixture unless it is explicitly bound
to a public API receipt by a future public client.
"""
from __future__ import annotations

import os
import shutil
import sys
import time

BRAND = "©️8x8 by FlashTM8 ⚡️🌎🤖"
VERSION = "Public Product Demo"

PRODUCTS = [
    ("Home / World", "Unified discovery, activity, search and evidence."),
    ("AI / Agents", "Use approved AI and agent services through your own 8x8 account."),
    ("Studio", "Research, write, create, edit and publish supported media."),
    ("Social", "Profiles, communities, messaging, feeds and creator channels."),
    ("Live / TV / Radio", "Public streaming, channels, radio and live experiences."),
    ("Build", "Project workspace, developer tools, terminal and supported integrations."),
    ("Connectors", "Link supported third-party services with scoped user permission."),
    ("8x8 ID / Wallet", "Identity, profile and approved wallet/product experiences."),
    ("8x8 Network", "Public network, explorer and interoperability products as released."),
    ("Economy", "8x8 and approved token/economic information with evidence-bound state."),
    ("NFT Vaults / Market", "Public Vault discovery and marketplace functions as released."),
    ("Markets / Gaming", "Approved analytics, games and participation experiences."),
    ("Governance", "Public proposals, voting and contribution workflows as released."),
    ("Transparency", "Public receipts, treasury/economic evidence and benchmark context."),
]

HELP = """Commands:
  help          show this help
  products      list public product families
  status        show public-demo truth boundary
  build         explain the user project-building workspace
  connect       explain connector permission model
  transparency  explain public receipt/economic transparency model
  clear         clear the screen
  exit          leave the demo

This terminal is a public product demonstration. It is not the private OWNER_ROOT
shell and does not contain private One-Fabric implementation or authority.
"""


def _clear() -> None:
    if sys.stdout.isatty() and os.environ.get("TERM", "") != "dumb":
        sys.stdout.write("\033[2J\033[H")
    else:
        print("\n" * 8)


def _width() -> int:
    return max(60, min(100, shutil.get_terminal_size((84, 24)).columns))


def _rule(char: str = "─") -> str:
    return char * _width()


def _header() -> None:
    print(_rule("═"))
    print("8x8 TERMINAL · PUBLIC PRODUCT SURFACE")
    print(BRAND)
    print(VERSION)
    print(_rule("═"))
    print("PUBLIC PRODUCT ≠ PRIVATE ONE-FABRIC IMPLEMENTATION")
    print("Demo fixtures ≠ live telemetry. OWNER_ROOT controls are not included here.")
    print()


def _products() -> None:
    print("\nPUBLIC PRODUCT FAMILIES\n" + _rule())
    for name, description in PRODUCTS:
        print(f"• {name:<22} {description}")
    print(_rule())
    print("Availability is release/evidence dependent; this list is a product map, not a live-state claim.\n")


def _status() -> None:
    rows = [
        ("Product shell", "DEMO / PUBLIC-SAFE"),
        ("Private topology", "NOT INCLUDED"),
        ("Owner controls", "NOT INCLUDED"),
        ("Credentials / secrets", "NOT INCLUDED"),
        ("Live balances / telemetry", "NOT FABRICATED"),
        ("Public API data", "ONLY WHEN A FUTURE CLIENT BINDS TO A VERIFIED PUBLIC ENDPOINT"),
    ]
    print("\nPUBLIC TRUTH BOUNDARY\n" + _rule())
    for key, value in rows:
        print(f"{key:<28} {value}")
    print(_rule() + "\n")


def _build() -> None:
    print("""
BUILD WORKSPACE — PRODUCT VISION
An authenticated user can have an isolated project workspace that combines an
8x8 Terminal, editor/IDE surfaces, AI/agent assistance, approved connectors,
artifact storage, previews, testing and deployment integrations. User projects
are tenant-isolated and never inherit OWNER_ROOT authority or private 8x8 code.
""")


def _connect() -> None:
    print("""
CONNECTORS — PRODUCT VISION
Users connect their own supported accounts through scoped OAuth/API permission.
The product should show what a connector can read or change, let the user revoke
it, and keep credentials behind a server-side secret boundary. Connector access
does not expose the private 8x8 orchestration implementation.
""")


def _transparency() -> None:
    print("""
TRANSPARENCY — PRODUCT VISION
Public economic dashboards may show cryptographically/verifiably sourced fee,
subscription, treasury, liquidity and reward receipts. Public transparency can
include public wallet/address roles, asset/network, amount, timestamp, policy
version and transaction/receipt proof. Private signer material, custody secrets,
internal treasury controls and OWNER_ROOT operations are never part of the feed.
""")


def main() -> None:
    demo = "--demo" in sys.argv
    _clear()
    _header()
    if demo:
        _products()
        _status()
        _build()
        _transparency()
        print("Demo complete.")
        return

    print("Type 'help' for commands.\n")
    while True:
        try:
            command = input("8x8-public> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if command in {"exit", "quit", "q"}:
            break
        if command in {"", "help"}:
            print(HELP)
        elif command == "products":
            _products()
        elif command == "status":
            _status()
        elif command == "build":
            _build()
        elif command == "connect":
            _connect()
        elif command == "transparency":
            _transparency()
        elif command == "clear":
            _clear(); _header()
        else:
            print("Unknown public-demo command. Type 'help'.")
        time.sleep(0.02)


if __name__ == "__main__":
    main()
