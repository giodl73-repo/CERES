---
id: plan-i-catalog-weaving
name: Catalog — Weaving
description: 15 weaving catalog entries per DECLINE-VERDICT guidance
status: draft
version: "1.0"
created: 2026-04-19
phase: 2
subsystem: catalog
trade: weaving
depends_on: [plan-a-scaffolding, plan-h-research-weaving]
blocks: []
estimated_effort: 3-5 weeks focused
primary_artifact_type: catalog
success_signal: >
  15 weaving catalog entries at `catalog/weaving/entries/*.md`, each
  schema-compliant; every entry cites sources or carries bracketed
  placeholders. Cross-entry audit confirms 9-cell matrix coverage.
spec: specs/2026-04-18-ceres-design.md
---

# Plan I: Catalog — Weaving

> **Pattern inherited from Plan C (smithing).** Same structure: manifest + schema extension + 15 entries.
> Follow Plan C (`plans/2026-04-19-plan-c-catalog-smithing.md`) as the template.
> **Simulation already scripted:** after entries are authored, run:
> `python -m simulations.tier_a.cli --catalog catalog/weaving/` (or equivalent) to produce 135 cells.

**Goal:** 15 weaving catalog entries per DECLINE-VERDICT guidance for this trade.

## Task Index
| # | Task | Creates |
|---|---|---|
| 1 | Catalog manifest / README | `catalog/weaving/README.md` |
| 2 | Weaving-specific schema extension | `catalog/weaving/SCHEMA.md` |
| 3-17 | Entries 001-015 | `catalog/weaving/entries/*.md` |
| 18 | Cross-entry audit | `reviews/CATALOG-AUDIT-plan-i.md` |
| 19 | Closeout | TRACKER + plans/README + frontmatter |
