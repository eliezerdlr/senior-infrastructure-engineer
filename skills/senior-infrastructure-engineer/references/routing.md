# Specialist Routing

Select the minimum specialists that directly contribute to the request.

| Intent | Primary specialist | Add when needed |
|---|---|---|
| Prompt creation or enhancement, reusable prompt template, prompt evaluation, or rough notes requiring a structured brief | `prompt-orchestrator` | domain specialist only when subject-matter validation is required |
| Agent identity, authorization boundaries, delegated authority, and audit controls | `agent-identity-governance` | `ai-security`, `automation-governance` |
| Multi-agent workflow design, handoffs, review gates, and orchestration patterns | `agent-workflow-designer` | `agent-identity-governance`, `prompt-orchestrator` |
| AI system threat modeling, prompt injection, model abuse, and AI control review | `ai-security` | `senior-security`, `agent-identity-governance` |
| API contract design, compatibility, versioning, and breaking-change review | `api-design-reviewer` | `senior-architect`, `code-reviewer` |
| Automation ownership, control gates, exception handling, and governance | `automation-governance` | `agent-workflow-designer`, affected platform specialist |
| Source-code quality or pull-request review | `code-reviewer` | `tdd-guide`, `security-audit` |
| Clear, unambiguous, controlled technical instructions | `controlled-technical-english` | `doc-maintenance`, domain specialist |
| Data model, schema, indexing, migration, or database technology design | `database-designer` | `database-reliability`, `senior-architect` |
| Database availability, backup, replication, incident, and operational reliability | `database-reliability` | `database-designer`, `disaster-recovery`, `observability-designer` |
| Documentation consistency, lifecycle, drift, and maintenance | `doc-maintenance` | `controlled-technical-english`, domain specialist |
| Email lifecycle, segmentation, deliverability, retention, and campaign operations | `email-lifecycle-strategy` | `automation-governance`, `controlled-technical-english` |
| FinOps governance, allocation, forecasting, optimization, and cloud cost accountability | `finops-operating-model` | cloud specialist, `observability-designer` |
| Release notes, stakeholder announcement, rollout communication, and change summary | `release-announcement` | `doc-maintenance`, `controlled-technical-english` |
| Cross-system architecture, trade-offs, quality attributes, and architectural decisions | `senior-architect` | affected platform specialist, `api-design-reviewer` |
| SLI/SLO design, error budgets, reliability targets, and service review | `slo-architect` | `observability-designer`, `incident-response` |
| Requirements, acceptance criteria, bounded autonomy, and implementation specification | `spec-driven-workflow` | `prompt-orchestrator`, domain specialist |
| Test-driven development, test strategy, fixtures, and coverage workflow | `tdd-guide` | `code-reviewer`, affected engineering specialist |
| Broad DevOps, CI/CD, containers | `senior-devops` | `terraform-engineer`, `kubernetes-ops`, cloud specialist |
| AWS architecture | `aws-solution-architect` | `terraform-engineer`, `observability-designer`, `disaster-recovery` |
| Azure architecture | `azure-cloud-architect` | `terraform-engineer`, `hyper-v`, `storage-spaces-direct` |
| GCP architecture | `gcp-cloud-architect` | `terraform-engineer`, `kubernetes-ops` |
| Terraform | `terraform-engineer` | target cloud specialist |
| Linux administration | `linux-administration` | `ansible`, `network-interface-health` |
| Windows Server / AD / IIS | `windows-server` | `hyper-v`, `storage-spaces-direct` |
| Kubernetes operations | `kubernetes-ops` | `senior-devops`, cloud specialist |
| Ansible automation | `ansible` | OS/platform specialist |
| Interface errors and link health | `network-interface-health` | `network-config-validation` |
| Network configuration review | `network-config-validation` | `network-interface-health` |
| Security incident | `incident-response` | `senior-secops`, affected platform specialist, `disaster-recovery` |
| Cloud security posture, IAM, public exposure | `cloud-security` | cloud specialist, `security-audit` |
| Security operations, CVE triage, hardening | `senior-secops` | affected platform specialist, `dependency-auditor` |
| Threat modeling and security request routing | `senior-security` | specialist selected from identified threat lane |
| Focused source or release security review | `security-audit` | `dependency-auditor`, platform specialist |
| Environment variables and secret hygiene | `env-secrets-manager` | `senior-secops`, affected platform specialist |
| Dependency, license, or upgrade risk | `dependency-auditor` | `security-audit`, `senior-devops` |
| Authorized penetration test or vulnerability exploitation validation | `security-pen-testing` | `security-audit`, affected platform specialist |
| Authorized adversary simulation or attack-path exercise | `red-team` | `senior-security`, `incident-response`, affected platform specialist |
| Structured failure and recovery ownership | `dsh-error-handling` | relevant platform specialist |
| Metrics, logs, traces, alerts | `observability-designer` | service/platform specialist |
| Operational runbooks | `runbook-generator` | relevant platform specialist |
| Business/service recovery | `disaster-recovery` | storage, virtualization, cloud, OS specialists |
| VMware | `vmware-engineer` | storage, network, DR |
| Hyper-V | `hyper-v` | Windows, S2D, DR |
| Pure Storage | `pure-storage` | virtualization, Kubernetes, DR |
| Storage Spaces Direct | `storage-spaces-direct` | Windows, Hyper-V, DR |

For cross-domain incidents, use at most one lead specialist per affected layer and one coordinating recovery or incident specialist. Expand only when evidence reveals another dependency.

Security requests must remain lane-specific: use `senior-security` to threat-model or route ambiguous requests, then load only the security specialist that owns the evidenced need. Route active vulnerability testing to `security-pen-testing` and adversary simulation to `red-team` only after written authorization, targets, rules of engagement, exclusions, test window, stop conditions, and evidence-handling requirements are established.
