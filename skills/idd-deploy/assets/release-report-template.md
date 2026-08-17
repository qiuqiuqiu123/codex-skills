# IDD Release Bundle

## `plan.md`

```markdown
# Release Plan: <release-id>

- Environment: <environment>
- Strategy: dry-run | standard | rolling | blue-green | canary | rollback
- Source revision: <immutable revision>
- Services: <list>
- Rollback target: <revision or artifact>
- Automatic rollback authorized: yes | no

## Related IDD Changes
## Preflight Commands
## Migration Compatibility
## Deployment Steps
## Health and Smoke Signals
## Promotion and Failure Thresholds
## Rollback Procedure
## Approval
```

## `report.md`

```markdown
# Release Report: <release-id>

- Environment: <environment>
- Source revision: <revision>
- Live revision: <verified revision>
- Result: verified | partial | failed | rolled-back

## Preflight Results
## Deployment Events
## Live Version Evidence
## Readiness and Smoke Results
## Metrics and Observation
## Rollback Evidence
## State Documents Updated
## Residual Risks
```
