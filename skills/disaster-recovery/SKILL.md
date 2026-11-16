---
name: disaster-recovery
description: Design, review, test, and operate technology disaster recovery and business continuity capabilities across on-premises and cloud environments. Use for business impact analysis, service tiering, RTO/RPO, backup and restore, replication, failover/failback, dependency mapping, recovery runbooks, exercises, ransomware recovery, crisis coordination, and evidence-based readiness reporting.
license: MIT
metadata:
  version: 1.0.0
  author: Innuos infrastructure-agent project
  source: independently-authored-local-adaptation
  adapted_by: Innuos infrastructure-agent project
  adaptation_date: 2026-11-16
  vendor_affiliation: none
  domain: infrastructure-reliability
---

# Disaster Recovery

Build recoverability as a verified operational capability rather than a document-only promise. Work across business services, applications, identity, network, compute, storage, databases, SaaS dependencies, cloud platforms, facilities, people, and communications.

## Scope

Use this skill to:

- perform business impact analysis and service criticality classification;
- define measurable recovery time objectives (RTO), recovery point objectives (RPO), maximum tolerable downtime, and minimum service levels;
- map service dependencies and recovery sequencing;
- design backup, replication, alternate-site, multi-zone, multi-region, and hybrid recovery patterns;
- create failover, restore, rebuild, validation, and failback runbooks;
- plan tabletop exercises, technical recovery tests, and full simulations;
- assess ransomware and destructive-event recovery, including isolation and clean-room restoration;
- produce readiness findings, evidence gaps, risks, ownership, and remediation roadmaps.

This skill provides independent engineering guidance and is not affiliated with a cloud, backup, storage, virtualization, or security vendor.

## Operational Approach

1. **Authorize and bound the exercise** — Identify the business service, systems, environments, data classes, test window, participants, allowed actions, success criteria, stop conditions, and decision authority.
2. **Collect evidence read-only** — Inventory dependencies, backups, replication, retention, immutability, encryption, keys, identity, DNS, certificates, network paths, infrastructure definitions, runbooks, contacts, contracts, monitoring, and previous test evidence.
3. **Set recovery objectives** — Obtain business-approved RTO/RPO and minimum service requirements. Do not invent objectives from technical preferences.
4. **Design recovery tiers** — Select patterns based on criticality, failure scope, data consistency, operational capacity, compliance, cost, and verified platform capability.
5. **Define recovery order** — Include facilities/connectivity, identity and secrets, management planes, DNS/time/certificates, data services, platforms, applications, integrations, observability, and user validation.
6. **Prepare recovery and rollback** — Specify prerequisites, exact targets, data cut-off, isolation, fencing, expected impact, fallback, failback, reconciliation, validation, and ownership.
7. **Obtain explicit approval** — Require approval immediately before restore, failover, failback, DNS/routing change, isolation, credential rotation, deletion, replication reversal, backup-policy change, or any production/disruptive test.
8. **Test incrementally** — Prefer tabletop and isolated restore verification before component, service, site, or regional exercises. Stop when integrity, containment, redundancy, or rollback is uncertain.
9. **Verify outcomes** — Measure actual recovery time and recovery point, data integrity, application consistency, dependency health, security controls, monitoring, user acceptance, and residual risk.
10. **Record evidence** — Separate observed results, assumptions, untested claims, exceptions, decisions, owners, and due dates.

Never request passwords, private keys, recovery codes, tokens, or backup encryption secrets in chat. Use approved authenticated sessions and secret stores. Never place live credentials, customer data, production topology, or sensitive recovery material in reusable skill files or public reports.

## Recovery Design Principles

- A successful backup job is not restore evidence.
- Replication is not a backup and can replicate corruption or malicious deletion.
- High availability addresses selected component failures; it is not automatically disaster recovery.
- Recovery requires control-plane dependencies such as identity, DNS, time, certificates, keys, networking, and management access.
- RTO/RPO claims are provisional until tested under representative conditions.
- Failback and data reconciliation are part of the recovery lifecycle.
- Immutable/offline copies, separate administrative boundaries, and tested clean-room procedures reduce correlated risk.
- Recovery procedures must work when normal collaboration, identity, network, or documentation systems are unavailable.

## Required Deliverables

Select only the artifacts needed for the request:

- business impact and service-tier matrix;
- dependency and recovery-sequence map;
- recovery architecture and failure-scenario coverage;
- backup/replication control assessment;
- runbook with prerequisites, actions, validation, rollback, and ownership;
- exercise plan with scope, safety controls, injects, evidence, and success criteria;
- readiness scorecard based on actual evidence;
- gap/risk register with priority, owner, target date, and acceptance decision;
- post-exercise report with measured RTO/RPO and corrective actions.

Use `references/recovery-plan-template.md` for a reusable plan structure and `references/exercise-and-evidence.md` for safe testing and evidence requirements.

## Completion Standard

A DR task is complete only when the output clearly states:

- scope and authorized failure scenarios;
- business-approved objectives and assumptions;
- dependencies and recovery order;
- recovery, rollback, and failback methods;
- security and data-integrity controls;
- evidence collected and tests actually performed;
- measured results versus targets;
- untested claims and remaining gaps;
- accountable owners and next actions.

Do not report a service as recoverable solely because documentation, replication, or backup jobs exist. Report the highest level actually evidenced: designed, configured, restore-tested, component-tested, service-tested, or full-scenario-tested.
