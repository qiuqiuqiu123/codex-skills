---
name: idd-init-project
description: Initialize Intent-Driven Development in a new or existing project. Use when starting a Greenfield foundation or first vertical slice, or adopting Brownfield incrementally by discovering real project rules, protecting existing instructions, distilling one high-value module, and establishing steering, intent, contracts, anchors, validation, and transaction records.
---

# IDD Init Project

Read [references/idd-core.md](references/idd-core.md). The offline template is `assets/idd-template.tar.gz`; inspect before extraction and merge rather than overwrite target files.

## Resolve

Inspect the target, then confirm `lightweight` or `enterprise` and one mode:

- `greenfield/foundation-only`: IDD and application foundation, no business slice;
- `greenfield/starter-slice`: foundation followed by one gated vertical feature;
- `brownfield`: incremental adoption around one selected module.

For Greenfield, resolve product boundary, stack, package manager, storage, environments, and verification. For Brownfield, derive these from tracked evidence before asking.

## Greenfield

1. Clarify outcome, users, non-goals, quality constraints, environments, and profile.
2. Draft `.steering/constitution.md`, `tech-stack.md`, and `conventions.md`. Unimplemented commands remain explicit TODOs, not guessed facts.
3. Show the full steering draft and wait for approval before writing.
4. Extract the template to a temporary directory, inspect it, and merge the agreed shape into the target without replacing existing files.
5. Initialize glossary, permissions, empty indexes, validator config, and `.idd/` directories.
6. Scaffold only confirmed application infrastructure and run real verification commands.

`foundation-only` ends with structure, verified commands, and open decisions. `starter-slice` hands one minimal vertical slice to `$idd-develop-feature`, which still enforces Gate 1 and Gate 2.

## Brownfield

Never default to full-repository distillation.

1. Read instructions, manifests, CI, scripts, source boundaries, tests, docs, schemas, deployment config, and targeted history.
2. Create a ledger for existing instructions: `retain`, `rewrite`, `relocate`, `automate`, or `delete`, including evidence and risk.
3. Derive candidate steering rules from evidence. Ask only about governance, domain meaning, frozen areas, or recurring mistakes the repository cannot reveal.
4. Present the steering proposal and ledger before writing. Deletion or weakening requires approval.
5. Select one supplied or user-approved high-value module.
6. Draft inferred intent and contracts, clearly label uncertain business meaning, and use normal Gates.
7. After approval, add anchors and establish a reconciliation baseline.
8. Leave other modules undistilled and record the next candidate only.

Finish only after required files exist, existing content is preserved, JSON indexes parse, commands are evidence-backed, verification ran or has a recorded blocker, and Brownfield scope is explicit.
