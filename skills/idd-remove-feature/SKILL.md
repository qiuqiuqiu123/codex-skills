---
name: idd-remove-feature
description: Disable, deprecate, or permanently delete an IDD-managed feature. Use when retiring a capability, endpoint, workflow, flag, schema, or UI requires an evidence-backed reverse-impact map, intent and contract Gates, migration safety, synchronized document and code removal, negative verification, anchor cleanup, and an audit record.
---

# IDD Remove Feature

Read [references/idd-core.md](references/idd-core.md) and [assets/removal-record-template.md](assets/removal-record-template.md). Use a unique `.idd/changes/<slug>/` bundle.

## Resolve and map

Start from canonical intent and contracts, then follow anchors and repository references. Confirm:

- `disable`: close entry points but preserve reversible implementation;
- `deprecate`: retain compatibility for an agreed migration window;
- `delete`: physically remove implementation and obsolete authority.

Inventory intent, contracts, code, routes, UI, APIs, events, jobs, consumers, flags, configuration, schemas, stored data, migrations, tests, docs, SDKs, telemetry, dashboards, runbooks, infrastructure, and anchors. Resolve retention, compatibility, rollout, and rollback obligations.

Invoke `$show-me` when available for the smallest evidence-backed dependency tree and removal order; otherwise use a compact tree or Mermaid. Mark uncertain edges.

## Gate 1: intent

Draft the exact canonical intent diff: reason, mode, user-visible remaining behavior, dates, alternatives, data handling, and non-goals. Present it and **stop for Gate 1**. Before approval, do not modify contracts or implementation. Apply only the approved diff.

## Gate 2: contracts

Draft API, event, schema, behavior, error, consumer, migration, compatibility, and rollout changes. Destructive data changes require a verified staged migration while old revisions or consumers still depend on the schema.

Present exact contract diffs, dependency visual, ordered implementation, rollback limits, and irreversible effects. **Stop for Gate 2.** Apply only approved contract changes.

## Execute

1. Reconfirm exact destructive targets when Gate 2 did not enumerate them.
2. Disable ingress and new writes before dependent removals when required.
3. Migrate, export, anonymize, or retain data as approved.
4. Remove implementation, generated output, config, infrastructure, and operations in dependency order.
5. Remove obsolete tests and add negative tests proving the capability is inaccessible.
6. Remove obsolete active rules while preserving compatibility records.
7. Refresh anchors and run `$idd-reconcile` when available.
8. Write `.idd/history/<slug>/removal.md` with approvals, exact removals, data disposition, verification, revision, and residual obligations.

Never claim full deletion while consumers, data, flags, routes, contracts, anchors, or operational assets remain unexplained. Preserve audit history.
