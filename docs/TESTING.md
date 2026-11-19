# Testing and Security Evidence

The default validation is offline and dependency-free:

```bash
npm run validate
```

It checks:

- the 46-specialist inventory and supervisor;
- SHA-256 integrity of every file declared by the vendored `agents-skills` manifests;
- unique names and required frontmatter;
- package registration;
- routing coverage;
- local licence/provenance presence without runtime catalogue dependencies;
- common secret patterns and forbidden private artifacts;
- risky operational language that requires review.

A passing static audit is not a security certification. It does not establish model obedience, live compatibility, vulnerability absence, production readiness, or authorization to operate infrastructure.
