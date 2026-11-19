# Agent identity governance control matrix

Use this matrix to record evidence. Mark unknown controls as gaps; do not infer deployment from policy text.

| Domain | Required evidence | Failure signal |
|---|---|---|
| Ownership | Accountable owner, technical custodian, recovery contact | Orphaned identity or shared mailbox as owner |
| Inventory | Stable identity ID, tenant, environment, workload and resources | Identity exists only in a secret or deployment script |
| Authentication | Managed identity, constrained federation or approved certificate | Human account, embedded secret or unbounded federation subject |
| Authorization | Task-to-permission matrix and approval for privileged scopes | Tenant-wide role without a resource/task justification |
| Separation | Distinct dev/test/prod identities and admin vs invocation roles | One principal crosses teams or trust zones |
| Credentials | Store, expiry, rotation owner and last rotation evidence | Non-expiring secret or no rotation owner |
| Access review | Reviewer, cadence, last result and remediation tracking | Dormant grants remain because the workload still exists |
| Monitoring | Sign-in/token, admin, consent, role and resource events | Logs absent, inaccessible or without an alert owner |
| Incident response | Containment, revocation, evidence preservation and recovery steps | Deletion is the only documented response |
| Decommissioning | Dependency check, disable window, grant removal and deletion evidence | Identity disabled but active credentials/roles remain |
| Exceptions | Risk owner, reason, compensating control and expiry | Permanent exception without review date |

## Review priorities

Treat these as high risk until verified:

- directory-wide or tenant-wide application permissions;
- role-management, consent, secret-management or policy-management access;
- cross-tenant trust or wildcard federation subjects;
- agent access to production deployment, finance, identity or security controls;
- one identity shared by several teams, agents or environments;
- credentials with unknown age, storage or consumer;
- an identity with no recent use but active privileged grants.

## Change record

For each remediation, capture:

1. current and proposed control;
2. affected identities, resources and teams;
3. evidence and reason;
4. approver and implementation owner;
5. pre-change backup/export where supported;
6. validation queries or expected events;
7. rollback trigger and recovery action;
8. residual risk and next review date.
