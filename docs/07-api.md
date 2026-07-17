# API (public contract)
FlashTM8 ⚡️🌎🤖 | ©️8x8

```
GET  /api/8x8/status       -> live system status
GET  /api/8x8/agents       -> registered agents
POST /api/8x8/dispatch     -> route a task to an agent
```
All messages are schema-versioned and signed. Privileged endpoints use scoped
owner tokens (never exposed externally).

See [roadmap](docs/08-roadmap.md).
