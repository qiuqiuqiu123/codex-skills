# IDD Issue Bundle

## `analysis.md`

```markdown
# Bug Analysis: <title>

- Slug: <slug>
- Mode: analyze | fix
- Verdict: confirmed | likely | unconfirmed | not-a-bug
- Severity: critical | high | medium | low
- Root-cause confidence: high | medium | low
- IDD layer: intent | contract | implementation | environment | unknown

## Actual and Expected Behavior
## Reproduction and Environment
## Evidence
## Affected Code and Anchors
## Root Cause
## Rejected Hypotheses
## Preferred Remediation
## Tests and Verification Plan
## Risks and Open Questions
```

## `fix.md`

```markdown
# Bug Fix: <title>

- Analysis: ./analysis.md
- Status: applied | partial | not-applied

## Root-cause Fix
## Files Changed
## Regression Test
## Deviations from Analysis
## Anchor or Contract Impact
```

## `verification.md`

Record the original reproduction after the fix, new and existing test commands with results, broader regression evidence, skipped checks and reasons, residual risk, and verdict `verified | partial | failed`.
