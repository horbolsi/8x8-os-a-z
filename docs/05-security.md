# Security & Privacy
FlashTM8 ⚡️🌎🤖 | ©️8x8

Security is architectural, not bolted on.

## Secrets
- Secrets live **only** in an encrypted vault / environment variables.
- **Never** hardcoded, never committed. Git push-protection blocks history with secrets.
- A credential-resolution protocol searches the vault and DBs before prompting.

## Anonymous by default
- All external communication is anonymous.
- No real names, no faces, no system internals exposed publicly.
- Sensitive media (QR, credentials) is DM-only, never posted to channels.

## Bounded autonomy
Critical actions require explicit gates:
- `RISK_GATE` + `WALLET_GATE` — trading
- `DEPLOY_GATE` — deploys
- `CONTENT_GATE` — public publishing
- `PAID_MODEL_GATE` — paid model escalation
- `RESTART_GATE` — service restarts

## Verification
- Every claim is backed by live API data before it is reported.
- Read-only audits never mutate state or print secrets.

See [quickstart](docs/06-quickstart.md).
