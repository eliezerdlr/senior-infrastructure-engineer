#!/usr/bin/env python3
"""Dependency-free repository security and governance audit."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

TEXT_SUFFIXES = {".md", ".json", ".yml", ".yaml", ".py", ".ps1", ".sh", ".txt"}
EXCLUDED_PARTS = {".git", "__pycache__", "node_modules", ".venv"}
SECRET_PATTERNS = {
    "private key material": re.compile(
        r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----\s*\n"
        r"[A-Za-z0-9+/=]{20,}"
    ),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "generic bearer token": re.compile(r"Authorization:\s*Bearer\s+[A-Za-z0-9._~-]{20,}", re.I),
}
PRIVATE_PATTERNS = {
    "local user path": re.compile(r"/" + r"Users/[^/\s]+/|/" + r"home/[^/\s]+/"),
}
RISK_PATTERNS = {
    "passwordless sudo": re.compile(r"NOPASSWD\s*:\s*ALL", re.I),
    "disabled SSH host checking": re.compile(r"StrictHostKeyChecking\s*=\s*no", re.I),
    "remote script piped to shell": re.compile(r"(?:curl|wget)[^\n|]{0,240}\|\s*(?:ba)?sh\b", re.I),
    "destructive filesystem command": re.compile(r"\brm\s+-rf\s+/(?:\s|$)"),
}

# Exact vendored fixtures remain byte-identical to their pinned manifests. Only
# these visibly synthetic values are allowed; another matching value in the
# same file remains a finding.
ALLOWED_SYNTHETIC_MATCHES = {
    (
        Path("skills/api-design-reviewer/references/api_antipatterns.md"),
        "generic bearer token",
    ): {"Authorization: " + "Bearer jwt-token-with-context"},
    (
        Path("skills/api-design-reviewer/references/rest_design_rules.md"),
        "generic bearer token",
    ): {"Authorization: " + "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."},
    **{
        (Path(f"skills/code-reviewer/expected_outputs/{name}"), "local user path"): {
            "/home/" + "user/"
        }
        for name in [
            "sample_c_clean_quality.json",
            "sample_c_smells_quality.json",
            "sample_csharp_clean_quality.json",
            "sample_csharp_smells_quality.json",
            "sample_java_clean_quality.json",
            "sample_java_smells_quality.json",
        ]
    },
}


def text_files(root: Path):
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            if not any(part in EXCLUDED_PARTS for part in path.parts):
                yield path


def repository_policy_findings(root: Path):
    findings = []

    kubernetes_skill = (root / "skills/kubernetes-ops/SKILL.md").read_text(encoding="utf-8")
    kubernetes_practices = (root / "skills/kubernetes-ops/references/best-practices.md").read_text(encoding="utf-8")
    windows_skill = (root / "skills/windows-server/SKILL.md").read_text(encoding="utf-8")
    cleanup = (root / "skills/kubernetes-ops/scripts/namespace-cleanup.sh").read_text(encoding="utf-8")

    forbidden = {
        "embedded Kubernetes example secret": "secret-" + "key-value",
        "embedded database password": "secret" + "123",
        "command-line registry password": "--docker-" + "password=",
        "PowerShell plaintext secure-string conversion": "-AsPlain" + "Text -Force",
    }
    combined = "\n".join((kubernetes_skill, kubernetes_practices, windows_skill))
    for label, marker in forbidden.items():
        if marker in combined:
            findings.append((Path("skills"), label))

    if 'MODE="${2:---dry-run}"' not in cleanup or '"$MODE" = "--execute"' not in cleanup:
        findings.append((Path("skills/kubernetes-ops/scripts/namespace-cleanup.sh"), "cleanup is not dry-run by default with explicit execution opt-in"))

    return findings


def audit(root: Path):
    critical = repository_policy_findings(root)
    warnings = []
    scanned = 0
    for path in text_files(root):
        scanned += 1
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            warnings.append((path, "non-UTF-8 text file"))
            continue
        rel = path.relative_to(root)
        for label, pattern in SECRET_PATTERNS.items():
            matches = {match.group(0) for match in pattern.finditer(content)}
            allowed = ALLOWED_SYNTHETIC_MATCHES.get((rel, label), set())
            if matches - allowed:
                critical.append((rel, label))
        for label, pattern in PRIVATE_PATTERNS.items():
            matches = {match.group(0) for match in pattern.finditer(content)}
            allowed = ALLOWED_SYNTHETIC_MATCHES.get((rel, label), set())
            if matches - allowed:
                critical.append((rel, label))
        for label, pattern in RISK_PATTERNS.items():
            if pattern.search(content):
                warnings.append((rel, label))
    return scanned, critical, warnings


def write_report(path: Path, scanned: int, critical, warnings):
    verdict = "PASS" if not critical else "FAIL"
    lines = [
        "# Security Audit",
        "",
        f"- Verdict: **{verdict}**",
        f"- Text files scanned: **{scanned}**",
        f"- Critical findings: **{len(critical)}**",
        f"- Review warnings: **{len(warnings)}**",
        "",
        "This is a dependency-free static review. It is not a security certification, live penetration test, model-behavior guarantee, or authorization to operate infrastructure.",
        "",
        "## Critical findings",
        "",
    ]
    lines += [f"- `{p}`: {label}" for p, label in critical] or ["None."]
    lines += ["", "## Review warnings", ""]
    lines += [f"- `{p}`: {label}" for p, label in warnings] or ["None."]
    lines += [
        "",
        "Warnings identify operationally sensitive examples that require contextual review; they are not automatically vulnerabilities.",
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--report", default="docs/SECURITY-AUDIT.md")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    scanned, critical, warnings = audit(root)
    write_report(root / args.report, scanned, critical, warnings)
    print(f"verdict={'PASS' if not critical else 'FAIL'} files={scanned} critical={len(critical)} warnings={len(warnings)}")
    raise SystemExit(1 if critical else 0)


if __name__ == "__main__":
    main()
