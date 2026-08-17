---
name: idd-reconcile
description: Audit or repair drift across IDD steering, intent, contracts, implementation, generated code, tests, and anchors. Use when checking whether documents still drive code, validating anchors after a change, producing a severity-ranked drift report, or applying authority-ordered repairs that stop for human Gates whenever canonical business meaning changes.
---

# IDD Reconcile

Read [references/idd-core.md](references/idd-core.md) and [assets/drift-report-template.md](assets/drift-report-template.md). Resolve scope and mode:

- `audit`: no source, canonical doc, generated output, test, or index changes; only a requested report may be written.
- `repair`: audit first, then propose authority-ordered fixes. Repair is not Gate approval.

Run the deterministic scanner before semantic checks:

```bash
python3 <skill-root>/scripts/scan_anchors.pyz <project-root> --format markdown
```

## Audit

Inspect `.steering/`, `intent/`, `contracts/`, implementation, tests, `.anchors/`, `.validator/`, and scoped `.idd/` records. Check:

1. steering violations and valid ADR overrides;
2. missing or contradictory intent-to-contract propagation;
3. schema versus human tables and generated output;
4. every scoped EARS/GWT rule against implementation and independent test evidence;
5. forward targets, headings, reverse entries, deleted paths, duplicates, and stale transaction references.

Do not require business anchors on pure implementation details. State confidence for semantic findings and distinguish missing behavior from missing test evidence.

Classify `critical` for proven authority violations, `warning` for likely drift needing judgment, and `suggestion` for non-drift improvements. Each finding includes evidence, authority, files, confidence, consequence, preferred resolution, and Gate requirement.

In audit mode, return or write `.validator/drift-report.md` and stop. Do not refresh indexes because that would alter the audit snapshot.

## Repair

1. Order fixes: steering decision, intent, contracts, generated code, ordinary implementation, tests, anchors.
2. Stop for Gate 1 when business meaning, permissions, workflow, or canonical intent changes.
3. Stop for Gate 2 when structure or behavior contracts change.
4. Apply the smallest verified change for implementation-only drift.
5. Regenerate output only through repository-owned generators.
6. Refresh indexes after canonical and source changes settle.
7. Re-run deterministic and semantic checks; preserve before-and-after evidence.

If evidence cannot identify the correct authority, stop and ask rather than inventing a rule.
