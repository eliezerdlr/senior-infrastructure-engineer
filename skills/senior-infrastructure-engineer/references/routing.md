# Specialist Routing

Select the minimum specialists that directly contribute to the request.

| Intent | Primary specialist | Add when needed |
|---|---|---|
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
