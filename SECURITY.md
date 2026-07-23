# Security Policy

## Public repository boundary

This repository is the public narrative, documentation, and demonstration surface for 8x8 OS. It must not contain private operational state or reusable authority.

Never commit:

- API keys, tokens, passwords, cookies, session files, private keys, seed phrases, or wallet private material;
- owner email, phone, private account identifiers, private chat IDs, or authentication allowlists;
- private messages, private memory, SOUL files, hidden reasoning, or cross-session context;
- raw logs, process listings, command lines, internal host paths, service inventories, ports, tunnels, or exploitable topology;
- private repository contents, private database rows, internal provider routing, or production deployment credentials;
- unrestricted remote-shell instructions or reusable privileged device access.

Public examples must use placeholders and simulated data. Claims must distinguish `CLAIMED`, `DESIGNED`, `IMPLEMENTED`, `TESTED`, `RECEIPT_VERIFIED`, `RUNNING`, `DEPLOYED`, `PUBLICLY_RELEASED`, and `ADOPTED`.

## Reporting

Report suspected exposure privately to the repository owner. Do not open a public issue containing a credential value, personal identifier, exploit path, or private-system topology.

## Transfer gate

A repository transfer requires:

1. current-tree public-safety scan;
2. historical reachability review without reproducing secret values;
3. exact-head CI;
4. backup and restore-test receipt;
5. public/private boundary review;
6. post-transfer verification of redirects, Actions, Pages, packages, webhooks, deploy keys, environments, permissions, and branch protections.

Removing a value from the current branch does not revoke a credential or erase Git history.
