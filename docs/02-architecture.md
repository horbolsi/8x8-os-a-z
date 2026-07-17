# Architecture
FlashTM8 ⚡️🌎🤖 | ©️8x8

Layered, independently replaceable, self-healing.

| Layer | Role |
|-------|------|
| Core OS | API + agent runtime |
| Agent Brain | Shared memory + knowledge graph |
| Trading | Futures + multi-exchange screening (bounded risk) |
| Bot Fleet | External bodies (Telegram, Discord) |
| Orchestration | Dispatch, watchdog, self-improve |
| Gateway | Unified model + API surface |
| Storage | Internal vault |
| Mesh | Device + cloud nodes |

## Failure model
- Watchdog restarts dead services automatically.
- Multi-provider model fallback guarantees a response.
- State is checkpointed; recovery is automatic.

See [agents](docs/03-agents.md).
