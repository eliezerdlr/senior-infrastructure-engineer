# Third-party notices

This repository combines independently authored project material with selected and adapted skills from public sources. Inclusion does not imply affiliation, endorsement, certification, or vendor support. Preserve the licence and provenance files included with each specialist.

## Engineering skills

Selected skills are included as complete local copies and include MIT-licensed material originating from `alirezarezvani/claude-skills`, ECC, and DeepSeek Harness.

- Engineering skill family: MIT; preserved at `licenses/engineering-skills-MIT.txt`.
- ECC network skills: MIT; nested licence files are retained.
- `dsh-error-handling`: MIT; nested licence retained.

The selected paths are: `senior-devops`, `aws-solution-architect`, `azure-cloud-architect`, `gcp-cloud-architect`, `incident-response`, `observability-designer`, `runbook-generator`, `network-interface-health`, `network-config-validation`, `dsh-error-handling`, `cloud-security`, `senior-secops`, `senior-security`, `env-secrets-manager`, `dependency-auditor`, `red-team`, and `security-pen-testing`.

## Vendored agents-skills collection

Collection source: https://github.com/eliezerdlr/agents-skills. The 22 selected upstream skills are byte-pinned by `provenance/agents-skills/skills.json` to their original `devops-skills` source commit `d59835fec2b1b85224c639f4ff1ef2e05586d1c5`. The repository-authored `prompt-orchestrator` is synchronized from `agents-skills` commit `0e56ff1e3a591948ddeff68433a1646a262010bb`.

All 23 selected skills and every supporting file declared by their manifests are stored locally. Runtime operation does not read or fetch the source repository. The collection contains:

- `agent-identity-governance`, `agent-workflow-designer`, `ai-security`, `api-design-reviewer`, `automation-governance`
- `cloud-security`, `code-reviewer`, `controlled-technical-english`, `database-designer`, `database-reliability`
- `dependency-auditor`, `doc-maintenance`, `email-lifecycle-strategy`, `env-secrets-manager`, `finops-operating-model`
- `observability-designer`, `prompt-orchestrator`, `release-announcement`, `senior-architect`, `senior-security`
- `slo-architect`, `spec-driven-workflow`, `tdd-guide`

The 22 upstream-selected skills remain byte-verifiable against `provenance/agents-skills/skills.json`. The repository-authored `prompt-orchestrator` remains byte-verifiable against `provenance/agents-skills/authored-skills.json`. Local tests verify every declared SHA-256 digest.

Applicable MIT licence texts are preserved at `licenses/devops-skills-MIT.txt`, `licenses/agency-agents-MIT.txt`, and `licenses/agency-agents-adaptations-MIT.txt`. Upstream notices and adaptation records are preserved under `provenance/agents-skills/`. `skills/prompt-orchestrator/LICENSE` and `skills/prompt-orchestrator/PROVENANCE.md` additionally record its project-level origin.

## Cloudflare security-audit adaptation

Upstream source: [Cloudflare security-audit-skill](https://github.com/cloudflare/security-audit-skill), with a local Pi-compatible adaptation included directly in this repository.

Selected skill: `security-audit`, including its focused-review guidance, upstream audit corpus, schemas, validators, provenance manifest, and MIT licence. Its upstream workflow entrypoint is stored as `WORKFLOW.md` inside the package to prevent duplicate Pi skill discovery.

## BagelHole DevOps Security Agent Skills

Source: https://github.com/BagelHole/DevOps-Security-Agent-Skills

Selected skills: `linux-administration`, `windows-server`, and `kubernetes-ops`.

Licence: MIT; preserved at `licenses/bagelhole-MIT.txt`.

## OpenFang

Source: https://github.com/RightNow-AI/openfang

Selected skill: `ansible`.

Licence: Apache License 2.0; preserved at `licenses/openfang-APACHE-2.0.txt`.

## Adapted infrastructure specialists

The following locally adapted copies preserve a `LICENSE` and `PROVENANCE.md` in their own directories:

- `terraform-engineer` — adapted from https://github.com/jeffallan/claude-skills
- `vmware-engineer` — adapted from https://github.com/theneoai/awesome-skills
- `hyper-v`, `pure-storage`, and `storage-spaces-direct` — adapted from https://github.com/chrishuffman5/domain-expert

Local adaptations add vendor-neutral identity, explicit authorization gates, secret-safe handling, provenance, and safer operational boundaries. Consult each directory for exact terms.

## Disaster recovery

`disaster-recovery` is independently authored local material under MIT. Its `PROVENANCE.md` records why an earlier unlicensed/internal candidate was not redistributed.

## Trademarks

AWS, Microsoft Azure, Google Cloud, Kubernetes, Ansible, Terraform, VMware, Hyper-V, Pure Storage, Windows, Linux, and other product names are trademarks of their respective owners. Nominative references do not imply affiliation or endorsement.
