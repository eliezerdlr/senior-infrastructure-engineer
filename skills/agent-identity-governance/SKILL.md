---
name: agent-identity-governance
description: "Govern AI agent and other non-human identities across their lifecycle: ownership, Entra ID/AD integration, least privilege, credential choice, access reviews, monitoring, incident response and decommissioning. Use for agent service principals, managed identities, workload identities and multi-team RBAC. Not for human user administration or for executing tenant changes."
---

# Agent Identity Governance

Design and review lifecycle controls for AI agents and other non-human identities (NHIs). This skill is instruction-only: it does not connect to a directory, handle credentials or change a tenant.

Use it when an agent, automation or service needs an identity, especially in a shared multi-team platform. For general agent architecture use `agent-designer`; for workflow topology use `agent-workflow-designer`; for human Microsoft 365 administration use `ms365-tenant-manager`; for prompt/tool abuse use `ai-security`.

## Required inputs

Before recommending controls, establish:

- agent purpose, environment, owner and accountable business team;
- resources, tenants and data classifications it must access;
- execution platform and supported identity mechanisms;
- human users, groups or services allowed to invoke or administer it;
- regulatory, retention, incident and recovery requirements;
- current identity, permissions, credentials, logs and expiry state.

If evidence is missing, label the result as a proposed control design rather than a verified deployment.

## Workflow

### 1. Inventory and classify

Create one record per identity with a stable ID, display name, agent/workload type, owner, technical custodian, environment, tenant, application, data class, creation source, last use, review date and planned retirement date.

Reject anonymous shared identities and identities without an accountable owner. Separate development, test and production identities. Do not reuse one identity across unrelated teams or trust zones merely for convenience.

### 2. Select the identity pattern

Prefer, in order:

1. platform-managed identity when the runtime and target support it;
2. workload identity federation with exact issuer, subject and audience constraints;
3. certificate credential held in an approved secret store;
4. short-lived secret only when stronger mechanisms are unavailable.

Avoid long-lived client secrets, embedded credentials and human accounts used by agents. Record the reason when a weaker mechanism is unavoidable, plus expiry, rotation owner and migration date.

For Microsoft environments, distinguish on-premises AD authentication from Microsoft Entra ID application/workload identity. AD or Entra can authenticate users and map groups to application roles; it does not update application code or grant agent permissions without an explicit authorization design. See [Entra and AD integration](references/entra-integration.md).

### 3. Define authorization

Build a permission matrix from verified tasks and resources. Grant only the actions and scopes needed for those tasks. Prefer application roles, resource-specific permissions and policy conditions over broad directory roles.

Separate:

- who may invoke the agent;
- who may change prompts, tools, policies or deployments;
- which workload identity the agent uses;
- which downstream resources that identity may access;
- who may approve privileged or high-impact operations.

Use group-to-role mapping for teams, but keep privileged administration separate from ordinary invocation. Treat agent delegation and downstream impersonation as distinct trust decisions. Require explicit approval for tenant-wide permissions, cross-tenant access, destructive actions, financial actions or access to highly sensitive data.

### 4. Apply lifecycle controls

At creation, require owner approval, purpose, environment, permission evidence, expiry/review dates and a recovery contact. At change time, review permission deltas and affected resources before rollout. At least periodically—and after ownership, scope or incident changes—confirm that the identity is still used, correctly owned and minimally privileged.

Disable before deleting when recovery may be needed. Decommission by revoking credentials/federation, removing role assignments and consent, disabling the identity, preserving required audit evidence, validating dependent workflows, then deleting after the approved recovery window.

### 5. Monitor and respond

Collect sign-in/token events, authorization failures, administrative changes, consent and role changes, credential changes, unusual resource access and dormant-identity signals. Define alert ownership and retention before claiming observability is complete.

For a suspected compromise:

1. contain the identity without destroying evidence;
2. revoke or rotate credentials and invalidate trust where supported;
3. identify affected resources, tokens, jobs and downstream identities;
4. restore the minimum required access through a reviewed identity path;
5. document root cause, permission changes and recurrence controls.

Do not prescribe a destructive response without confirming impact, dependencies and recovery.

### 6. Produce a reviewable decision

Deliver:

- identity inventory and ownership gaps;
- identity mechanism decision and rejected alternatives;
- permission matrix with high-risk grants highlighted;
- lifecycle and access-review schedule;
- logging/alert coverage and evidence gaps;
- incident containment and recovery procedure;
- phased remediation plan with owner, approval gate and rollback for each change.

Use [control matrix](references/control-matrix.md) as the completion checklist.

## Acceptance criteria

A design is ready for implementation only when every production identity has:

- a named accountable owner and separate technical custodian where practical;
- one documented purpose, environment and trust boundary;
- a non-human authentication method with no embedded secret;
- task-linked least-privilege permissions and explicit high-risk approvals;
- expiry/review, rotation, monitoring, incident and decommission procedures;
- a tested rollback or recovery path for permission and identity changes.

These checks establish a governance design, not proof that directory or cloud controls are deployed. Actual tenant changes require current vendor documentation, scoped tooling, authorized credentials, change approval and post-change verification.
