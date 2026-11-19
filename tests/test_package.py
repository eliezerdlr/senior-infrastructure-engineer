import hashlib
import importlib.util
import json
import re
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
ADAPTED = {
    "terraform-engineer", "vmware-engineer", "hyper-v", "pure-storage",
    "storage-spaces-direct", "disaster-recovery", "prompt-orchestrator",
}

EXPECTED = {
    "senior-devops", "aws-solution-architect", "azure-cloud-architect",
    "gcp-cloud-architect", "network-interface-health",
    "network-config-validation", "incident-response", "dsh-error-handling",
    "observability-designer", "runbook-generator", "linux-administration",
    "windows-server", "kubernetes-ops", "ansible", "disaster-recovery",
    "terraform-engineer", "vmware-engineer", "hyper-v", "pure-storage",
    "storage-spaces-direct", "cloud-security", "senior-secops",
    "senior-security", "security-audit", "env-secrets-manager",
    "dependency-auditor", "red-team", "security-pen-testing",
    "prompt-orchestrator", "agent-identity-governance",
    "agent-workflow-designer", "ai-security", "api-design-reviewer",
    "automation-governance", "code-reviewer", "controlled-technical-english",
    "database-designer", "database-reliability", "doc-maintenance",
    "email-lifecycle-strategy", "finops-operating-model",
    "release-announcement", "senior-architect", "slo-architect",
    "spec-driven-workflow", "tdd-guide",
}


def frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return {}
    data = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"')
    return data


class PackageTests(unittest.TestCase):
    def test_package_manifest(self):
        package = json.loads((ROOT / "package.json").read_text())
        self.assertEqual(package["name"], "senior-infrastructure-engineer")
        self.assertIn("./skills/**/SKILL.md", package["pi"]["skills"])
        self.assertIn("./agents/senior-infrastructure-engineer.md", package["pi"]["prompts"])

    def test_exact_specialist_inventory(self):
        found = {
            path.parent.name
            for path in SKILLS.glob("*/SKILL.md")
            if path.parent.name != "senior-infrastructure-engineer"
        }
        self.assertEqual(found, EXPECTED)

    def test_readme_links_every_specialist_to_its_local_skill(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for name in EXPECTED:
            self.assertIn(
                f"[{name}](skills/{name}/SKILL.md)",
                readme,
                name,
            )

    def test_skill_names_are_unique_and_match_directories(self):
        seen = set()
        for path in SKILLS.rglob("SKILL.md"):
            metadata = frontmatter(path)
            self.assertIn("name", metadata, str(path))
            self.assertIn("description", metadata, str(path))
            name = metadata["name"]
            self.assertEqual(name, path.parent.name)
            self.assertNotIn(name, seen)
            seen.add(name)

    def test_routing_covers_every_specialist(self):
        routing = (SKILLS / "senior-infrastructure-engineer" / "references" / "routing.md").read_text()
        for name in EXPECTED:
            self.assertIn(f"`{name}`", routing)

    def test_supervisor_has_safety_contract(self):
        text = (SKILLS / "senior-infrastructure-engineer" / "SKILL.md").read_text()
        for phrase in [
            "Do **not** execute every specialist",
            "Start with read-only discovery",
            "Before any mutation",
            "Never request or expose",
            "Stop and ask for approval",
        ]:
            self.assertIn(phrase, text)

    def test_release_documents_exist(self):
        for name in [
            "README.md", "LICENSE", "THIRD_PARTY_NOTICES.md", "SECURITY.md",
            "CONTRIBUTING.md", "docs/ARCHITECTURE.md", "docs/TESTING.md",
            "licenses/engineering-skills-MIT.txt", "licenses/bagelhole-MIT.txt",
            "licenses/openfang-APACHE-2.0.txt",
            "licenses/devops-skills-MIT.txt",
            "licenses/agency-agents-MIT.txt",
            "licenses/agency-agents-adaptations-MIT.txt",
            "provenance/agents-skills/skills.json",
            "provenance/agents-skills/authored-skills.json",
            "provenance/agents-skills/devops-skills-THIRD_PARTY_NOTICES.md",
            "provenance/agents-skills/agency-agents-adaptations-UPSTREAM.json",
        ]:
            self.assertTrue((ROOT / name).is_file(), name)

    def test_adapted_skill_licence_and_provenance(self):
        notices = (ROOT / "THIRD_PARTY_NOTICES.md").read_text(encoding="utf-8")
        for name in ADAPTED:
            directory = SKILLS / name
            self.assertTrue((directory / "LICENSE").is_file(), name)
            self.assertTrue((directory / "PROVENANCE.md").is_file(), name)
            self.assertIn(f"`{name}`", notices)

    def test_agents_skills_are_complete_local_copies(self):
        provenance = ROOT / "provenance" / "agents-skills"
        manifests = [
            json.loads((provenance / "skills.json").read_text(encoding="utf-8")),
            json.loads((provenance / "authored-skills.json").read_text(encoding="utf-8")),
        ]
        for manifest in manifests:
            for skill in manifest["skills"]:
                directory = SKILLS / skill["name"]
                self.assertTrue(directory.is_dir(), skill["name"])
                for item in skill["files"]:
                    path = directory / item["path"]
                    self.assertTrue(path.is_file(), str(path.relative_to(ROOT)))
                    digest = hashlib.sha256(path.read_bytes()).hexdigest()
                    self.assertEqual(digest, item["sha256"], str(path.relative_to(ROOT)))

    def test_security_audit_is_self_contained_without_duplicate_skill(self):
        directory = SKILLS / "security-audit"
        for name in ["LICENSE", "UPSTREAM.json", "SHA256SUMS", "references/focused-review.md", "references/full-audit.md", "upstream/security-audit/WORKFLOW.md"]:
            self.assertTrue((directory / name).is_file(), name)
        nested = list((directory / "upstream").rglob("SKILL.md"))
        self.assertEqual(nested, [])

    def test_mutating_cleanup_requires_explicit_execution(self):
        script = (SKILLS / "kubernetes-ops" / "scripts" / "namespace-cleanup.sh").read_text(encoding="utf-8")
        self.assertIn('MODE="${2:---dry-run}"', script)
        self.assertIn('"$MODE" = "--execute"', script)

    def test_no_embedded_secret_examples(self):
        targets = [
            SKILLS / "kubernetes-ops" / "SKILL.md",
            SKILLS / "kubernetes-ops" / "references" / "best-practices.md",
            SKILLS / "windows-server" / "SKILL.md",
        ]
        forbidden = [
            "secret-" + "key-value", "secret" + "123",
            "--docker-" + "password=", "-AsPlain" + "Text -Force",
        ]
        content = "\n".join(path.read_text(encoding="utf-8") for path in targets)
        for marker in forbidden:
            self.assertNotIn(marker, content)

    def test_security_audit_allows_only_exact_synthetic_fixture_values(self):
        audit_path = ROOT / "scripts" / "security_audit.py"
        spec = importlib.util.spec_from_file_location("security_audit", audit_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.repository_policy_findings = lambda _root: []

        relative = Path("skills/api-design-reviewer/references/rest_design_rules.md")
        known = "Authorization: " + "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
        unexpected = "Authorization: " + "Bearer " + "A" * 32
        with tempfile.TemporaryDirectory() as temporary:
            fixture = Path(temporary) / relative
            fixture.parent.mkdir(parents=True)
            fixture.write_text(known, encoding="utf-8")
            _, critical, _ = module.audit(Path(temporary))
            self.assertEqual(critical, [])

            fixture.write_text(f"{known}\n{unexpected}\n", encoding="utf-8")
            _, critical, _ = module.audit(Path(temporary))
            self.assertIn((relative, "generic bearer token"), critical)

    def test_no_private_workspace_paths_or_key_material(self):
        private_patterns = ["/" + "Users/", "ero" + "drigues"]
        key_material = re.compile(
            r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----\s*\n"
            r"[A-Za-z0-9+/=]{20,}"
        )
        for path in ROOT.rglob("*"):
            if path.is_file() and ".git" not in path.parts:
                try:
                    text = path.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    continue
                for pattern in private_patterns:
                    self.assertNotIn(pattern, text, f"{pattern} in {path.relative_to(ROOT)}")
                self.assertIsNone(
                    key_material.search(text),
                    f"private key material in {path.relative_to(ROOT)}",
                )


if __name__ == "__main__":
    unittest.main()
