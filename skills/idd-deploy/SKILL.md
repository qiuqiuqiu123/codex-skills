---
name: idd-deploy
description: Deploy or roll back an IDD project to a specified local, development, staging, production, or custom environment. Use when a revision needs dry-run, standard, rolling, blue-green, canary, or rollback execution with repository-defined preflight checks, explicit production authorization, live revision verification, and an auditable release report.
---

# IDD Deploy

Read [references/idd-core.md](references/idd-core.md) and [assets/release-report-template.md](assets/release-report-template.md). Prefer repository-owned release automation; never invent deployment commands when the project defines them.

## Resolve

Inspect release instructions, CI/CD, manifests, environments, migrations, health checks, observability, and current state. Resolve and restate:

- environment: `local`, `dev`, `staging`, `production`, or named custom target;
- strategy: `dry-run`, `standard`, `rolling`, `blue-green`, `canary`, or `rollback`;
- immutable source revision, affected services, and related IDD changes;
- rollback target and whether automatic rollback is authorized;
- live version, health, smoke, promotion, and failure signals.

Ask when external target or rollback behavior remains ambiguous.

## Preflight

1. Confirm the working tree and revision; do not silently deploy uncommitted state.
2. Reject unresolved critical IDD drift.
3. Run required tests, lint or type checks, and builds. Stop on failure; do not weaken gates.
4. Validate configuration without printing secret values.
5. Verify migrations remain compatible with old and new application revisions.
6. Define promotion, observation, failure, and rollback criteria.
7. Write `.idd/releases/<release-id>/plan.md`.

`dry-run` stops after non-mutating validation. Before production, destructive migration, public traffic change, or rollback, present the exact target, revision, services, actions, downtime, rollback, and risks. Require authorization for that exact mutation unless the current request already supplies it; never broaden staging authorization to production or deploy authorization to rollback.

## Deploy and verify

1. Execute the approved path and capture the platform revision.
2. Observe each progressive rollout step and stop on threshold failure.
3. Prove the new revision is serving traffic.
4. Run deep readiness and business smoke checks, then observe defined logs and metrics without exposing sensitive data.
5. On failure, follow only the approved rollback policy; otherwise preserve evidence and stop.
6. After successful live verification, write `report.md` and update a repository-owned deployment state document when one exists.

A zero exit status is not live verification. Never say deployed, healthy, shipped, or rolled back until the target confirms the exact revision and required behavior.
