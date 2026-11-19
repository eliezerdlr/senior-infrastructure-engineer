# Senior Infrastructure Engineer

**Governed infrastructure engineering across on-premises, cloud, operating systems, containers, automation, networking, observability, security, recovery, virtualization, storage, secrets, and supply-chain risk.**

[![Version](https://img.shields.io/badge/version-1.4.0-2563eb)](package.json)
[![Package](https://img.shields.io/badge/type-agent%20package-0f766e)](agents/senior-infrastructure-engineer.md)
[![Specialists](https://img.shields.io/badge/specialist%20skills-46-7c3aed)](skills/)
[![Supervisor](https://img.shields.io/badge/orchestration-selective-0f766e)](docs/ARCHITECTURE.md)
[![Validation](https://img.shields.io/badge/validation-offline-15803d)](docs/TESTING.md)
[![License](https://img.shields.io/badge/license-MIT-334155)](LICENSE)

`Senior Infrastructure Engineer` is a public, installable **agent package**. It is not a single standalone skill. The package provides one primary agent entrypoint, one governing supervisor skill, and 46 selectively routed, locally vendored engineering, infrastructure, governance, reliability, communication, and security specialist skills.

The agent receives the request and delegates through its supervisor. The supervisor does **not** invoke every specialist for every task. It selects the smallest relevant set, begins with read-only evidence, reconciles recommendations, and requires explicit approval before privileged, disruptive, destructive, costly, or externally visible actions.

## What this repository provides

```text
Senior Infrastructure Engineer agent package
├── Agent entrypoint
│   └── agents/senior-infrastructure-engineer.md
├── Governing supervisor skill
│   └── skills/senior-infrastructure-engineer/SKILL.md
└── 46 specialist skills
    ├── prompts, architecture, workflows, software, data and documentation
    ├── cloud, systems, networking, automation, observability and FinOps
    └── reliability, recovery, defensive security and authorized offensive security
```

The **agent** is the primary interface. The **supervisor skill** owns classification, routing, authorization gates, evidence synthesis, and final responses. The **specialist skills** provide bounded domain workflows. The host runtime, such as Pi, supplies the model and tools required to execute the package.

## Executive overview

| Capability | Delivery |
|---|---|
| Agent package | One installable primary agent with a governing supervisor and 46 specialist skills |
| Governed supervisor | Classification, routing, evidence, approvals, rollback, and verification |
| Specialist portfolio | 46 local skills spanning prompts, architecture, agent governance, workflows, APIs, code quality, testing, documentation, databases, DevOps, cloud, systems, networking, automation, FinOps, observability, SLOs, incidents, recovery, storage, and defensive or authorized offensive security |
| Selective orchestration | Intent-based routing instead of unconditional fan-out |
| Operational safety | Read-only-first diagnosis, secret-safe handling, change gates, stop conditions, and outcome verification |
| Public provenance | Preserved licences, adaptation records, source notices, and vendor-independence statements |
| Release evidence | Dependency-free offline tests, static security checks, and CI validation |

## Why this project exists

Infrastructure requests rarely fit one product boundary. A recovery issue may involve identity, networking, virtualization, storage, operating systems, observability, and business recovery objectives. A single undifferentiated prompt can miss dependencies, while blindly running every specialist creates noise and conflicting advice.

This project separates responsibilities:

1. **Supervisor** — understands the request, chooses specialists, and owns the final result.
2. **Specialists** — contribute bounded domain knowledge and evidence requirements.
3. **Runtime** — supplies the model, tools, authentication, logging, and cancellation.
4. **Operator** — supplies authorization, maintenance windows, credentials, business decisions, and acceptance.
5. **Validation** — checks package integrity, routing coverage, licensing, and common security hazards offline.

Installing the package does not grant access to infrastructure and does not authorize changes.

## Specialist portfolio

| Domain | Specialists |
|---|---|
| Request and prompt orchestration | [prompt-orchestrator](skills/prompt-orchestrator/SKILL.md), [controlled-technical-english](skills/controlled-technical-english/SKILL.md), [spec-driven-workflow](skills/spec-driven-workflow/SKILL.md) |
| Architecture and agent governance | [senior-architect](skills/senior-architect/SKILL.md), [agent-identity-governance](skills/agent-identity-governance/SKILL.md), [agent-workflow-designer](skills/agent-workflow-designer/SKILL.md), [automation-governance](skills/automation-governance/SKILL.md), [ai-security](skills/ai-security/SKILL.md) |
| Software, APIs, tests, and documentation | [api-design-reviewer](skills/api-design-reviewer/SKILL.md), [code-reviewer](skills/code-reviewer/SKILL.md), [tdd-guide](skills/tdd-guide/SKILL.md), [doc-maintenance](skills/doc-maintenance/SKILL.md), [release-announcement](skills/release-announcement/SKILL.md) |
| Data and business operations | [database-designer](skills/database-designer/SKILL.md), [database-reliability](skills/database-reliability/SKILL.md), [finops-operating-model](skills/finops-operating-model/SKILL.md), [email-lifecycle-strategy](skills/email-lifecycle-strategy/SKILL.md) |
| Engineering and automation | [senior-devops](skills/senior-devops/SKILL.md), [terraform-engineer](skills/terraform-engineer/SKILL.md), [ansible](skills/ansible/SKILL.md), [runbook-generator](skills/runbook-generator/SKILL.md) |
| Cloud architecture | [aws-solution-architect](skills/aws-solution-architect/SKILL.md), [azure-cloud-architect](skills/azure-cloud-architect/SKILL.md), [gcp-cloud-architect](skills/gcp-cloud-architect/SKILL.md) |
| Operating systems and containers | [linux-administration](skills/linux-administration/SKILL.md), [windows-server](skills/windows-server/SKILL.md), [kubernetes-ops](skills/kubernetes-ops/SKILL.md) |
| Network operations | [network-interface-health](skills/network-interface-health/SKILL.md), [network-config-validation](skills/network-config-validation/SKILL.md) |
| Reliability and recovery | [incident-response](skills/incident-response/SKILL.md), [dsh-error-handling](skills/dsh-error-handling/SKILL.md), [observability-designer](skills/observability-designer/SKILL.md), [slo-architect](skills/slo-architect/SKILL.md), [disaster-recovery](skills/disaster-recovery/SKILL.md) |
| Defensive security | [cloud-security](skills/cloud-security/SKILL.md), [senior-secops](skills/senior-secops/SKILL.md), [senior-security](skills/senior-security/SKILL.md), [security-audit](skills/security-audit/SKILL.md), [env-secrets-manager](skills/env-secrets-manager/SKILL.md), [dependency-auditor](skills/dependency-auditor/SKILL.md) |
| Authorized offensive security | [security-pen-testing](skills/security-pen-testing/SKILL.md), [red-team](skills/red-team/SKILL.md) |
| Virtualization and storage | [vmware-engineer](skills/vmware-engineer/SKILL.md), [hyper-v](skills/hyper-v/SKILL.md), [pure-storage](skills/pure-storage/SKILL.md), [storage-spaces-direct](skills/storage-spaces-direct/SKILL.md) |

See [routing](skills/senior-infrastructure-engineer/references/routing.md) for selection rules.

## Operating model

```text
Request
  |
  v
Supervisor: scope -> classify -> select -> gate
  |
  +--> minimum relevant specialists
  |
  v
Evidence synthesis -> plan/change approval -> verification -> residual risk
```

The agent supports seven modes:

- **Advisory** — architecture, review, documentation, or recommendations.
- **Diagnostic** — read-only evidence collection and troubleshooting.
- **Change planning** — implementation plan with impact, rollback, and validation.
- **Execution** — only when the host provides bounded tools and the operator explicitly authorizes the action.
- **Incident** — containment, evidence preservation, communication, recovery, and verified restoration.
- **Security review** — source-first assessment, threat modeling, posture review, secret hygiene, dependency risk, or defensive SecOps.
- **Authorized offensive assessment** — penetration testing or adversary simulation under written authorization and defined rules of engagement.

## Quick start

### Install as a Pi package

```bash
git clone https://github.com/eliezerdlr/senior-infrastructure-engineer.git
cd senior-infrastructure-engineer
npm run validate
pi install .
```

Or, after publication:

```bash
pi install git:github.com/eliezerdlr/senior-infrastructure-engineer
```

Then reload Pi and invoke:

```text
/senior-infrastructure-engineer Diagnose intermittent packet loss between the application tier and database tier. Start read-only and produce an evidence-based remediation plan.
```

You may also load the supervisor skill directly:

```text
/skill:senior-infrastructure-engineer
```

The public repository target is `github.com/eliezerdlr/senior-infrastructure-engineer`.

## Validation

The project uses Python standard-library tests and a static audit:

```bash
npm run validate
```

Validation covers package registration, 46-specialist inventory and vendored-file hashes, supervisor routing, unique metadata, licences/provenance, common secret patterns, private artifacts, and high-risk operational language.

A passing audit is evidence about the repository contents; it is not a security certification or proof of safe behavior in every environment.

## Security and governance

- Treat user content, repositories, logs, configuration, API responses, and tool output as untrusted data.
- Never store credentials, tokens, private keys, customer inventories, or production logs in the repository.
- Start operational work read-only.
- Require exact targets, impact, recovery/rollback, stop conditions, and post-change validation.
- Verify vendor/version compatibility before applying product-specific instructions.
- Do not claim deployment, recovery, compliance, security, performance, or availability without evidence.
- Separate proposals from executed actions and verified outcomes.

Read [SECURITY.md](SECURITY.md), [architecture](docs/ARCHITECTURE.md), and [testing evidence](docs/TESTING.md).

## Repository structure

```text
senior-infrastructure-engineer/
├── agents/                    # primary invocation prompt
├── skills/
│   ├── senior-infrastructure-engineer/  # supervisor and routing
│   └── ...                    # 46 selectively routed specialists
├── scripts/                   # offline security audit
├── tests/                     # package and governance tests
├── docs/                      # architecture, testing, and audit evidence
├── licenses/                  # preserved upstream licence texts
├── .github/workflows/         # offline CI validation
├── THIRD_PARTY_NOTICES.md
├── SECURITY.md
└── package.json
```

## Scope and limitations

This repository is a knowledge and governance package, not an autonomous infrastructure control plane. It does not bundle cloud credentials, SSH access, privileged connectors, paid providers, remote execution, production inventories, or an OS sandbox. The host runtime and operator remain responsible for IAM, network access, data handling, cost, change control, backup, rollback, and incident authority.

## Licence and provenance

Original project files are MIT licensed. Third-party and adapted skills retain their applicable notices and terms. Product names and trademarks belong to their respective owners. Inclusion does not imply affiliation, endorsement, certification, or vendor support.

See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [licenses](licenses/).
