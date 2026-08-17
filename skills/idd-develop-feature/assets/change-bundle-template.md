# IDD Feature Change Bundle

Create these files under `.idd/changes/<slug>/`. They are transaction records, not canonical business sources.

## `request.md`

```markdown
# Feature Request: <title>

- Slug: <slug>
- Mode: plan | build
- Profile: lightweight | enterprise
- Status: clarifying | awaiting-intent-approval | awaiting-contract-approval | ready-to-build | implementing | verified

## Outcome
## Users and Roles
## Current Behavior
## Desired Behavior
## Acceptance Scenarios
## Non-goals
## Constraints
## Open Questions
## Approval Log
```

## `intent-proposal.md`

```markdown
# Intent Proposal: <title>

## Canonical Files Affected
## Business Rule and Workflow Diffs
## Permission or Persona Impact
## Assumptions
## Gate 1 Decision
```

## `contract-impact.md`

```markdown
# Contract Impact: <title>

## Structure Contracts
## Behavior Contracts
## Compatibility and Migration
## Consumers and Failure Modes
## Gate 2 Decision
```

## `design.md`

```markdown
# Technical Design: <title>

## Context
## Chosen Design
## Verified Visual
## Data and State Flow
## Security and Operations
## Alternatives and Trade-offs
## Risks
```

## `tasks.md`

Use ordered checkboxes with a concrete file or artifact for every task. Include implementation, tests, anchors, migration, observability, deployment, and reconciliation when applicable.

## `verification.md`

Record acceptance evidence, commands and exit results, reconciliation findings, skipped checks with reasons, residual risks, and the exact revision when one exists.
