# Testing and Security Evidence

The default validation is offline and dependency-free:

```bash
npm run validate
```

It checks:

- the 28-specialist inventory and supervisor;
- unique names and required frontmatter;
- package registration;
- routing coverage;
- licence/provenance presence;
- common secret patterns and forbidden private artifacts;
- risky operational language that requires review.

A passing static audit is not a security certification. It does not establish model obedience, live compatibility, vulnerability absence, production readiness, or authorization to operate infrastructure.
