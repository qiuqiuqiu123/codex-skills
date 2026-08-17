---
name: idd-develop-feature
description: Develop or plan a feature through Intent-Driven Development. Use when a user asks for a new capability in an IDD project, wants intent and contracts kept authoritative, or needs an explicit lightweight-versus-enterprise solution choice. Draft intent and stop for Gate 1, then draft contracts and a visual design and stop for Gate 2 before changing implementation code.
---

# IDD Develop Feature

Read [references/idd-core.md](references/idd-core.md) and [assets/change-bundle-template.md](assets/change-bundle-template.md). Use a unique `.idd/changes/<slug>/` bundle; never overwrite an unrelated active change.

## Resolve

Inspect `.steering/`, relevant intent, contracts, code, tests, and active changes before asking questions. Resolve:

- `plan` or `build` mode;
- `lightweight` or `enterprise`, explicitly confirmed after an evidence-based recommendation;
- outcome, users, actual and desired behavior, acceptance scenarios, non-goals, and material constraints.

Ask only for facts that cannot be found in the repository and would alter the design.

## Stage 1: intent

Write `request.md` and `intent-proposal.md`. Name canonical `intent/` targets and show exact proposed diffs. Do not edit canonical intent until approved.

Present the intent, assumptions, profile, and open questions. **Stop for Gate 1.** Ambiguous encouragement is not approval. Before approval, do not create or modify contracts, technical design, implementation, generated code, migrations, or feature tests.

After approval, apply only the approved intent diff and record the decision.

## Stage 2: contracts and design

Derive structure contracts, EARS/GWT behavior contracts, affected code and consumers, migrations, tests, anchors, operations, and ordered tasks. Enterprise work also covers security, auditability, compatibility, failure modes, capacity, observability, rollback, and ADR needs.

Write `contract-impact.md`, `design.md`, and `tasks.md`. Invoke `$show-me` when available for the smallest repository-grounded architecture, state, control, or data-flow visual; otherwise use compact verified Mermaid.

Present contract diffs, the visual, impact, risks, migration, verification, and tasks. **Stop for Gate 2.** Before approval, do not modify implementation, generated code, migrations, or tests. Recompute downstream artifacts whenever approved upstream content changes.

After approval, apply only the approved contract changes.

## Stage 3: build

`plan` ends with an approved, ready implementation package. For `build`:

1. Implement ordered tasks without unrelated refactors.
2. Generate code only from approved schemas; add independent acceptance and failure-path tests.
3. Add `@intent:` and `@contract:` anchors and refresh indexes.
4. Run focused and required broader checks.
5. Run `$idd-reconcile` in audit mode when available.
6. Write `verification.md` with commands, evidence, skipped checks, and residual risk.

Never claim completion while a Gate, acceptance scenario, task, or required verification is outstanding.
