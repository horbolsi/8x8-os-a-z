# Architecture
FlashTM8 ⚡️🌎🤖 | ©️8x8

8x8 OS is built in layers. Each layer is independently replaceable and
self-healing.

## Layers
| Layer | Role | Tech |
|-------|------|------|
| Core OS | API + agent runtime | FastAPI (port 8086) |
| Agent Brain | Shared memory + knowledge graph | SQLite + graph store |
| Trading | Futures + multi-exchange screening | BitGet API + CCXT-free direct client |
| Bot Fleet | External bodies | Telegram (6) + Discord (1) via runit |
| Orchestration | Dispatch, watchdog, self-improve | cron + Python services |
| Gateway | Unified model + API surface | FastAPI (port 9119) |
| Storage | Internal vault | 08-partition namespace |
| Mesh | Device + cloud nodes | Termux, proot, iPhone iSH, Render, Vercel, Neon, GitHub |

## Data flow
1. A message arrives at a bot (Telegram/Discord).
2. The gateway routes it to the mapped agent via the orchestrator.
3. The agent reads/writes the shared brain, may spawn sub-agents, and acts.
4. Results are published back to the channel and recorded in the brain.

## Failure model
- Watchdog restarts any dead service every 2 minutes.
- 14-tier model fallback guarantees a response even if providers rate-limit.
- State is checkpointed; recovery is automatic.

See [agents](docs/03-agents.md).
