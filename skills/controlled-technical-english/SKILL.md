---
name: controlled-technical-english
description: Rewrite technical instructions and user-facing engineering content into concise, consistent, unambiguous English using a local controlled-language profile. Use for runbooks, procedures, plans, warnings, and support text; not for formal ASD-STE100 compliance certification.
license: MIT
---

# Controlled Technical English

Use this local writing profile to make technical content easier to translate, review, and follow. It borrows general controlled-language principles but is **not** the official ASD-STE100 specification, does not include its complete dictionary, and must not be used to claim ASD-STE100 compliance.

## Core rules

1. Write one action or idea per sentence.
2. Prefer active voice and present tense.
3. Name the actor when responsibility could be unclear.
4. Use one preferred term for each concept. Do not alternate synonyms.
5. Put conditions before actions: “If the check fails, stop the deployment.”
6. Use numbered steps for ordered procedures.
7. Keep procedure sentences near 20 words and descriptive sentences near 25 words when clarity permits.
8. Define necessary acronyms and domain terms at first use.
9. Use exact values, units, paths, commands, states, and expected results.
10. Separate warnings, prerequisites, actions, verification, and recovery.
11. Avoid vague qualifiers such as “usually,” “simple,” “quick,” and “as needed” unless quantified.
12. Avoid idioms, humor, metaphors, and culture-specific references in operational text.

## Preferred local vocabulary

Use the project term when it is already established. Otherwise prefer:

| Prefer | Avoid when the simple term is accurate |
|---|---|
| start / stop | initiate / terminate |
| use | utilize / leverage |
| make / create | facilitate / instantiate |
| before / after | prior to / subsequent to |
| about | regarding / in relation to |
| check | ascertain / verify visually |
| change | modify / alter, when they mean the same thing |
| remove | eliminate / purge, unless technically distinct |
| help | facilitate |
| required / optional | mandatory-ish / nice to have |

A technical verb is acceptable when the simpler word changes the meaning, for example “encrypt,” “mount,” “serialize,” or “revoke.”

## Procedure structure

```md
## Purpose
<One sentence.>

## Prerequisites
- <Required state, permission, tool, or backup.>

## Steps
1. <Action.>
   Expected result: <observable result>.
2. <Action.>
   Expected result: <observable result>.

## Verification
- <Check and pass condition.>

## Recovery
- <Safe rollback or escalation step.>
```

## Rewrite pass

1. Identify the audience, task, and consequence of error.
2. Preserve technical meaning, commands, identifiers, thresholds, warnings, and contractual keywords.
3. Build a small term list for repeated concepts.
4. Split compound steps and ambiguous pronouns.
5. Replace vague words with observable conditions.
6. Check that “it,” “this,” and “they” have one clear referent.
7. Check each step for actor, action, object, condition, and result.
8. Compare the rewrite with the source to detect lost requirements.
9. Mark unresolved ambiguity instead of guessing.

## Output

Return:

- the rewritten text;
- a short terminology list when the document is long;
- ambiguities or source defects that need author confirmation;
- a statement that the output follows the local profile and is not a formal standards-compliance result.

## Boundaries

This skill does not provide the official ASD-STE100 dictionary, certification, legal interpretation, translation certification, or automated compliance validation. It does not alter source files or publish text without separate authorization.
