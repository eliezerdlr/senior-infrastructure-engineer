---
name: doc-maintenance
description: Keep project documentation aligned with verified behavior changes. Use for release documentation, changed CLI/API/configuration behavior, stale examples, and behavior-anchored documentation drift. Avoid cosmetic rewrites that are unrelated to a verified change.
license: MIT
---

# Documentation Maintenance

Keep documentation accurate with the smallest reviewable change. Documentation follows verified behavior; it does not promise behavior that is not implemented.

## Inputs

Collect:

- the commit, pull request, ticket, release, or observed behavior that anchors the pass;
- the user-visible change and affected audience;
- relevant source, tests, generated schemas, help output, and existing docs;
- release status and compatibility or migration constraints.

If the behavior cannot be verified, label the claim as unverified and stop before publishing it as fact.

## Workflow

1. **Establish the baseline.** Name the change range or artifact being documented.
2. **List user-visible differences.** Include flags, defaults, configuration keys, API shapes, endpoints, environment variables, supported versions, errors, and workflows.
3. **Build a change-to-document map.** Search README, guides, references, examples, migration notes, FAQ, and release notes for each changed concept.
4. **Update precisely.** Change only affected lines and nearby context. Avoid unrelated reformatting.
5. **Update every contract surface.** A new flag belongs in the CLI reference; a new key belongs in configuration docs; a breaking API change needs migration guidance.
6. **Verify examples.** Run examples when safe and available. Otherwise perform a static consistency check and state the limitation.
7. **Search for stale wording.** Look for old names, defaults, paths, examples, and “coming soon” text.
8. **Prepare release notes.** Summarize user impact under Added, Changed, Fixed, Deprecated, Removed, or Breaking.
9. **Report evidence.** List behavior sources, files changed, checks run, unresolved gaps, and any claims that remain unverified.

## Drift signals

A page is drifting when it:

- documents an identifier or behavior that no longer exists;
- shows an example that does not match the current interface;
- states a default or supported version that differs from code or tests;
- omits required migration steps;
- describes a shipped or cancelled feature as future work;
- conflicts with another authoritative page.

## Writing rules

- Lead with user impact.
- Use present tense for shipped behavior.
- Mark experimental or unreleased behavior explicitly.
- Keep code blocks language-tagged and internally consistent.
- Link the first useful mention, not every occurrence.
- Never convert assumptions into facts.
- Do not claim that a command was executed when only inspected.

## Release-note template

```md
## <version> — <date>

### Added
- <capability> — <user benefit>. <evidence/link>

### Changed
- <behavior> — <impact and action, if any>.

### Fixed
- <user-visible symptom> — <result>.

### Deprecated
- <old behavior>. Use <replacement>. Removal: <version/date or unknown>.

### Breaking
- **Breaking:** <change>. **Migration:** <steps or guide>.
```

## Completion checklist

- [ ] Every change is anchored to verified behavior.
- [ ] All affected documentation surfaces were searched.
- [ ] Examples were executed or explicitly marked as statically checked.
- [ ] Old terminology and contradictory defaults were searched.
- [ ] Breaking changes include migration guidance.
- [ ] The diff contains no unrelated stylistic rewrite.
- [ ] The report separates verified facts from remaining gaps.

## Boundaries

This skill provides an instruction workflow only. It does not install tools, modify documentation without authorization, call external services, publish content, or certify correctness.
