---
name: release-announcement
description: Create channel-specific release announcements that lead with user impact, identify the affected audience, explain required action, and include migration and verification details without unsupported claims.
license: MIT
---

# Release Announcement

Create a reviewable release communication from verified release evidence. A changelog, engineering release note, in-product message, email, and social post require different levels of detail.

## Required inputs

- release name/version and actual or planned date;
- shipped changes and supporting evidence;
- affected audiences and channels;
- compatibility, migration, rollback, and known-issue information;
- approved links, measurements, screenshots, and acknowledgements;
- publication status: draft, approved, or shipped.

Do not announce an incomplete release as shipped. Do not invent metrics, dates, testimonials, compatibility, or links.

## Workflow

1. **Verify the release state.** Distinguish merged, released, generally available, deprecated, and removed.
2. **Segment the audience.** Existing operators, API adopters, end users, prospects, or internal teams may need different messages.
3. **Choose one channel per artifact.** Do not blend a terse changelog with marketing prose.
4. **Lead with three facts:** what changed, who it affects, and what they must do.
5. **Describe impact.** State benefits and risks in user language.
6. **Add action details.** Include upgrade, migration, opt-in, compatibility, rollback, or “no action required.”
7. **Mark breaking changes prominently.**
8. **Cite evidence.** Link approved release notes, migration docs, tags, issues, or measurement methods.
9. **Review claims and confidentiality.** Remove unsupported, internal, embargoed, or security-sensitive detail.
10. **Return a draft for approval.** Publication is a separate authorized action.

## Channel templates

### Changelog

```md
## <version> — <date>

### Added
- <capability> — <user benefit>. <link>

### Changed
- <change> — <impact and action>.

### Fixed
- <symptom> — <result>.

### Deprecated
- <old behavior>. Use <replacement>. Removal: <date/version or unknown>.

### Breaking
- **Breaking:** <change>. **Migration:** <steps/link>. **Rollback:** <path>.
```

### Engineering release notes

Include:

- summary and affected users;
- upgrade command or procedure;
- before/after examples;
- compatibility matrix;
- migration and rollback;
- known issues and workarounds;
- evidence and acknowledgements.

### In-product message

Use one short outcome sentence, one action, and one approved link. State whether dismissal is permanent.

### Email or internal post

Use: audience-specific subject, three-line summary, action deadline if real, owner/contact, migration link, and known risks.

### Social post

Use one verifiable outcome, one audience cue, and one approved link. Do not compress a breaking migration into a social-only message.

## Claim checks

- Replace adjectives with measured facts when an approved method exists.
- If a metric is unavailable, describe the behavior without a number.
- Use the actual ship date.
- Do not promise future dates without approved commitment.
- Repeat breaking-change and security-critical action across all relevant channels.
- Avoid disclosure that increases exploitability before users can mitigate.

## Delivery package

Return:

1. audience and chosen channel;
2. draft copy;
3. source/evidence list;
4. migration and rollback status;
5. known issues and unresolved claims;
6. reviewer/approval needed before publication.

## Boundaries

This instruction-only skill writes drafts. It does not call release systems, create tickets, use credentials, publish, email, post to social networks, or modify source control.
