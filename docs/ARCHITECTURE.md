# Architecture

## Model

The package uses a supervisor-and-specialists pattern:

1. The `senior-infrastructure-engineer` supervisor receives the objective.
2. It classifies the request and selects the minimum relevant specialists.
3. Specialists contribute domain guidance and evidence requirements.
4. The supervisor reconciles recommendations and owns the final response.
5. Mutating work is gated by explicit authorization and verification.

The package does not fan out automatically and does not run all skills on every request. Security work is routed by lane: threat modeling, cloud posture, SecOps, source audit, secret hygiene, dependency risk, penetration testing, or red-team simulation. Active offensive work requires written authorization, defined targets, rules of engagement, exclusions, stop conditions, evidence handling, and an approved test window. Runtime concurrency, tool access, model selection, and external credentials are supplied by the host platform.

## Layers

- **Supervisor** — routing, governance, evidence contract, approval gates.
- **Specialists** — 28 domain capabilities, including six defensive-security lanes and two authorized offensive-security lanes.
- **Host runtime** — model, tools, authentication, execution, cancellation, and logging.
- **Operator controls** — scope, maintenance window, backup, rollback, business approval, and acceptance.

## Trust boundaries

User content, repositories, configuration, logs, API responses, web content, and tool output are untrusted inputs. Skill text cannot grant permission. External changes require a bounded tool and an authorized operator.
