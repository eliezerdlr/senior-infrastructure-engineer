# Recovery Exercises and Evidence

## Exercise progression

1. **Document review** — confirm scope, owners, dependencies, access, and recovery sources.
2. **Tabletop** — walk through a defined scenario, decisions, communications, and blocked dependencies.
3. **Isolated restore** — restore representative data or systems without production cutover.
4. **Component test** — recover a bounded dependency and validate integrity.
5. **Service test** — recover the service and integrations in an isolated or alternate environment.
6. **Failover/failback test** — perform an approved controlled transition and reconciliation.
7. **Full scenario** — exercise people, technology, communications, and business validation under representative constraints.

Advancing a level requires evidence from the prior level and explicit authorization.

## Safety controls

- named test controller and stop authority;
- exact target and environment confirmation;
- protected production boundaries;
- backups and rollback/recovery verified before changes;
- isolation, fencing, and split-brain controls;
- monitoring and communication active;
- no unapproved destructive or production-impacting actions;
- immediate stop on data-integrity, security, containment, or rollback uncertainty.

## Evidence checklist

- start/end timestamps and decision log;
- recovery source and recovery point;
- command/change records without secrets;
- integrity and consistency results;
- dependency and application health;
- measured RTO/RPO;
- user/business acceptance;
- deviations, failed steps, and workarounds;
- residual risk, owner, and due date.

## Readiness labels

- **Designed** — architecture and runbook exist.
- **Configured** — required controls are configured but not restored.
- **Restore-tested** — representative restore completed and validated.
- **Component-tested** — bounded technical recovery completed.
- **Service-tested** — end-to-end service recovery completed.
- **Full-scenario-tested** — technology, people, communications, and business validation exercised.

Never assign a higher label than the available evidence supports.
