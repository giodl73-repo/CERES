# CERES — Project Overview

CERES is the **Local Production Atlas**: a catalog-driven design and evaluation
project for artisan-production equipment — forges, ovens, looms, kilns, and
related trades. The mission is to design equipment that hits price and
operational points enabling towns and small cities to restore meaningful local
production, evaluated under realistic economic conditions.

---

## The Working Hypothesis

Local production of craft goods (bread, metalwork, textiles) declined in the
twentieth century primarily because the economics stopped working — not because
the knowledge disappeared or the demand vanished. The research hypothesis is that
**redesigned equipment and ownership structures can restore viability** at village,
town, and small-city scale.

The hypothesis is testable. If Phase 1 research reveals that the binding
constraint for a trade is not equipment economics but something else — demand
collapse, regulatory capture, labor-regime dependency, supply-chain disappearance
— that trade's analysis pivots to document what is actually required. A rigorous
null result is success.

---

## Three Trades and a Facility

The current catalog covers three trades and one shared-facility type:

| Trade | Catalog directory | Entries |
|-------|-------------------|---------|
| Smithing (forges) | `catalog/smithing/` | 15 entries |
| Baking (ovens, bakeries) | `catalog/baking/` | 15 entries |
| Weaving (looms, fiber) | `catalog/weaving/` | 15 entries |
| Artisan Square (co-location) | `catalog/artisan-square/` | planned |

Each trade is evaluated across four anchor cultures — medieval Northern Europe,
Song-era China, Tokugawa Japan, American frontier — to extract requirements from
historical forms rather than modern assumptions.

---

## Three Scales

Every catalog entry is evaluated at three settlement sizes. Scale is a
**first-class variable**, not a post-hoc filter.

```proof:tree kind=org
Scales
- Village: 500–2,000 residents
- Town: 2,000–15,000 residents
- Small city: 15,000–75,000 residents
```

Scale-specific thresholds (wages, cost ceilings, member-pool sizes) live in
`corpus/program/SCALES.md`. Every entry produces a 3 × 3 grid of verdicts —
one per (scale × lens) combination.

---

## Three Economic Lenses

The same catalog entry is evaluated three times, each asking a different
ownership question:

| Lens | Ownership model | Primary metric |
|------|-----------------|----------------|
| **MARKET** | Private operator | Payback years (ceiling: 8) |
| **COOPERATIVE** | Worker/member co-op | Break-even members vs. feasible pool |
| **CIVIC** | Municipal / public | Per-household annual cost (ceiling: scale threshold) |

A design that fails all three lenses at all three scales is not viable under
any realistic model. A design that passes `win` under MARKET at town scale but
fails under COOPERATIVE and CIVIC is viable only as a private business. The
combination of verdicts tells the story.

Full lens definitions and formulas: `corpus/program/ECONOMIC-LENSES.md`.

---

## Project Structure

```proof:tree kind=org
CERES directories
- specs/: Design specifications and amendments
- plans/: Implementation plans (Plans A–J complete)
- research/: Phase 1 — functional requirements from historical forms
  - cultures/: Four anchor cultures × three trades
  - trades/: Requirements, forms, decline verdicts, sources
- catalog/: Phase 2 — THE STAR. One file per equipment design
  - SCHEMA.md: Canonical field definitions
  - smithing/ baking/ weaving/ artisan-square/: Per-trade schemas and entries
- corpus/: Reference framework
  - canon/: Theory, glossary, principles
  - program/: Lens formulas, scales, currencies, validation rules
- simulations/: Phase 4 — Tier A (deterministic), Tier B (system dynamics), Tier C (agent-based)
- playbook/: Phase 5 — winning designs by trade and scale, pitch narrative
- docs/: Pipeline, style guide, methodology, compiled guides
- skills/: Review and authoring skill definitions
- .roles/: Panel, editorial, and board role definitions
- reviews/: All review outputs
- scoring/: Quality rubric
```

---

## The Five Phases

```proof:callout kind=note label="Pipeline summary"
Phase 1 — Research: extract functional requirements from historical forms
Phase 2 — Catalog: design equipment variants spanning the tradeoff space
Phase 3 — Evaluation: run every entry through 9 cells (3 scales × 3 lenses)
Phase 4 — Simulation: Tier A deterministic, Tier B system dynamics, Tier C agent-based
Phase 5 — Playbook + Pitch: identify winners, write implementation plans and funder narrative
```

Full pipeline: `docs/PIPELINE.md`.

---

## Quality Bar

```proof:callout kind=warning label="Non-negotiables"
Every number must be cited. An uncited number in a catalog entry blocks promotion
to `validated`. No supplier BOMs, no real vendor quotes. No hand-waving on
economics — if a lens result is `marginal` or `fail`, say so and explain why.
```

Research-paper-level estimates with cited sources. Order-of-magnitude unit
economics, not due-diligence-grade procurement plans.

---

## Sibling Projects

CERES borrows structural patterns from sibling projects but operates under its
own rules:

| Project | Path | Relationship |
|---------|------|--------------|
| LUCIA | `chronicle` | Structural pattern source: "many instances, consistent schema" catalog model |
| FELICE/RMM | `rmm` | `corpus/` framework structure and simulation-design discipline |
| MAXIM | `reference` | Primary citation source for domain material |

Cite MAXIM for domain material; do not duplicate it in CERES. If MAXIM has a
relevant entry, reference it. If no MAXIM entry exists, add the citation to
`sources/` and note the gap.

---

## Where to Start

- **Understand the evaluation framework:** `corpus/program/ECONOMIC-LENSES.md`
- **Understand scale parameters:** `corpus/program/SCALES.md`
- **Read a catalog entry:** any file in `catalog/smithing/entries/` or `catalog/baking/entries/`
- **Understand the schema:** `catalog/SCHEMA.md` + `catalog/<trade>/SCHEMA.md`
- **Run a review:** `skills/ceres-panel/SKILL.md`
- **Track project status:** `TRACKER.md`
