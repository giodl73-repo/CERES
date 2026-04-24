# CERES Skills

Reusable pipeline stages for CERES. Each skill lives in its own directory
as `SKILL.md`. Skills operationalize the review tiers defined in
`.roles/`.

## Review Skills

| Skill | Tier | Purpose |
|-------|------|---------|
| [ceres-panel](ceres-panel/SKILL.md) | Panel (6 voices) | Run 6-voice panel review on any CERES artifact — spec, plan, catalog entry, playbook file, pitch |
| [ceres-editorial](ceres-editorial/SKILL.md) | Editorial (3 lenses) | Run citation / scope / numeracy cleanup pass before promoting an artifact to `validated` |
| [ceres-board](ceres-board/SKILL.md) | Board (per-trade) | Assemble a trade-specific domain board and run expert review on a contested claim |
| [ceres-check](ceres-check/SKILL.md) | All tiers (dynamic) | Fast filtered audit: dynamically selects applicable roles by artifact type and content signals, then evaluates each role's verify checklist and produces a severity-coded findings table |

## Authoring Skills (future)

Planned for Phase 2 when the vertical slice is running:

- `ceres-catalog-entry` — author a new catalog entry against the schema
- `ceres-sim-tier-a` — run the Tier A scenario-comparator across catalog entries
- `ceres-playbook` — compile winning-designs playbook files from populated catalog results
- `ceres-pitch` — author the pitch narrative from validated playbook evidence

## Orchestration Skills (future)

- `ceres-promote` — orchestrate panel → editorial → validated promotion in sequence
- `ceres-e2e` — full pipeline for a catalog entry from draft through validated
