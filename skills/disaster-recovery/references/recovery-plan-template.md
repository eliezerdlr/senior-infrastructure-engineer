# Disaster Recovery Plan Template

## 1. Scope and authority

- Business service:
- Service owner:
- Technical recovery lead:
- Incident decision authority:
- Environments and locations:
- Included failure scenarios:
- Excluded scenarios:
- Allowed actions:
- Stop conditions:

## 2. Objectives

| Service/component | Tier | RTO | RPO | Minimum service | Approval owner |
|---|---:|---:|---:|---|---|

Record whether objectives are approved, proposed, or unverified.

## 3. Dependencies and recovery order

| Order | Dependency/component | Recovery source | Owner | Validation | Blocking dependencies |
|---:|---|---|---|---|---|

Include identity, secrets/keys, DNS, time, certificates, network, management planes, data services, integrations, observability, and user access.

## 4. Recovery method

For each component document:

- prerequisites and required access;
- backup/replica/artifact source and timestamp;
- isolation and fencing;
- exact recovery steps;
- expected impact and duration;
- data consistency and reconciliation;
- rollback or alternate recovery;
- failback method;
- technical and business validation.

## 5. Communications

- primary and out-of-band channels;
- contact roster and alternates;
- internal/customer/regulatory decision points;
- status cadence and approved message owner.

## 6. Evidence

- backup and replication evidence;
- restore evidence;
- configuration exports and infrastructure definitions;
- integrity checks;
- measured recovery times and data-loss window;
- application and user acceptance;
- exceptions and unresolved gaps.

## 7. Approval and maintenance

- plan owner:
- last review:
- last test:
- next test:
- approved exceptions:
- revision history:
