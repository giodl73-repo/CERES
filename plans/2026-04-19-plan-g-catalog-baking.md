---
id: plan-g-catalog-baking
name: Catalog — Baking
description: 15 baking catalog entries per DECLINE-VERDICT guidance
status: draft
version: "1.0"
created: 2026-04-19
phase: 2
subsystem: catalog
trade: baking
depends_on: [plan-a-scaffolding, plan-f-research-baking]
blocks: []
estimated_effort: 3-5 weeks focused
primary_artifact_type: catalog
success_signal: >
  15 baking catalog entries at `catalog/baking/entries/*.md`, each
  schema-compliant; every entry cites sources or carries bracketed
  placeholders. Cross-entry audit confirms 9-cell matrix coverage.
spec: specs/2026-04-18-ceres-design.md
---

# Plan G: Catalog — Baking

> **Pattern inherited from Plan C (smithing).** Same structure: manifest + schema extension + 15 entries.
> Follow Plan C (`plans/2026-04-19-plan-c-catalog-smithing.md`) as the template.
> **Simulation already scripted:** after entries are authored, run:
> `python -m simulations.tier_a.cli --catalog catalog/baking/` (or equivalent) to produce 135 cells.

**Goal:** 15 baking catalog entries per DECLINE-VERDICT guidance for this trade.

## Task Index
| # | Task | Creates |
|---|---|---|
| 1 | Catalog manifest / README | `catalog/baking/README.md` |
| 2 | Baking-specific schema extension | `catalog/baking/SCHEMA.md` |
| 3-17 | Entries 001-015 | `catalog/baking/entries/*.md` |
| 18 | Cross-entry audit | `reviews/CATALOG-AUDIT-plan-g.md` |
| 19 | Closeout | TRACKER + plans/README + frontmatter |
