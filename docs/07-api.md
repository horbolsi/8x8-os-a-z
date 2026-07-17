# API Reference (public contract)
FlashTM8 ⚡️🌎🤖 | ©️8x8

The Core OS exposes a JSON API. All endpoints are schema-checked and versioned.

## Base
```
GET  /api/8x8/status      -> live system status
GET  /api/8x8/agents      -> registered agents
POST /api/8x8/dispatch    -> route a task to an agent
GET  /api/8x8/trading/live-> live trading snapshot (read-only)
```

## Message contracts
Versioned in the `8x8-messages` repository. Every message has:
`id, from, to, type, payload, ts, signature`.

## Auth
Public endpoints require no auth. Privileged endpoints use the sovereign
owner's scoped tokens (never exposed externally).

See [roadmap](docs/08-roadmap.md).
