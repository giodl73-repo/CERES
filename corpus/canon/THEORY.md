---
title: CERES Local-Production Framework
version: "1.0"
created: 2026-04-18
spec: specs/2026-04-18-ceres-design.md
---

# CERES Local-Production Framework

This document is the canonical in-repository statement of the theoretical framework
that CERES applies to all catalog, simulation, and playbook work. It restates the
working hypothesis from the design specification, explains the rationale for the
equipment-redesign frame, defines the three economic lenses and three scales as
parallel evaluation dimensions, describes the role of the catalog as a living
evidentiary artifact, characterizes the relationship between historical precedent and
modern design, and pre-registers the criteria for success, null result, and failure.

Every claim here traces to a section of `specs/2026-04-18-ceres-design.md` (v0.2).
No concept is introduced that does not appear in the spec or in `corpus/canon/GLOSSARY.md`.

---

## 1. Working Hypothesis

*(Spec Section 2)*

CERES's working hypothesis — to be tested, not assumed:

> Local artisan production in industrialized economies declined primarily because the
> equipment, scale, and organizational forms inherited from pre-industrial times no
> longer penciled out against industrial competition. Redesign the equipment for
> modern contexts (energy sources, regulations, labor costs, shareability patterns),
> pair it with the right organizational form (market / cooperative / civic), match it
> to the right settlement scale, and a meaningful share of these trades becomes viable
> again.

### Falsifiers

If the historical research (Phase 1) reveals that the binding constraint was not
equipment economics but one of the following, CERES must acknowledge it and adapt:

- **Demand collapse** — consumers genuinely prefer industrial goods for reasons
  durable to price reduction (consistency, safety perception, brand trust). Equipment
  redesign cannot restore what was never lost.
- **Regulatory capture** — trades were displaced by zoning, licensing, food-safety,
  or tax regimes that equipment redesign cannot navigate.
- **Labor-regime dependency** — historical viability rested on household labor,
  apprentice servitude, or customary obligations that cannot be reproduced ethically.
- **Supply-chain disappearance** — the upstream inputs (local grain mills, tanneries,
  regional steel) vanished and cannot be reconstituted at equipment scale alone.

### Pivot Criteria

If any falsifier holds strongly for a given trade, CERES's analysis for that trade
pivots from "here is equipment that restores viability" to "here is what would
actually be required, and whether equipment is part of the answer or not." A trade
where equipment is shown to be *not* the binding constraint is a finding, not a
failure.

CERES tests the hypothesis by building a catalog of equipment designs and evaluating
each design against a matrix of contexts. The pattern of verdicts — across trades,
across scales, across lenses — is the evidence for or against the hypothesis.

---

## 2. Why the Equipment-Redesign Frame

*(Spec Section 2, Section 3)*

Among the levers available to restore local artisan production, equipment economics
is selected as the primary focus because it is the most directly addressable,
estimable, and fundable variable at project scope. Demand-side interventions (consumer
preference campaigns, provenance labeling, local-first procurement mandates) require
sustained behavioral change across many actors and operate on decade-scale timelines
without clear, bounded scope. Regulatory interventions (zoning reform, food-safety
variance, licensing liberalization) require political coalition-building that is
jurisdiction-specific and fragile. Labor-regime interventions (apprenticeship pipeline
restoration, guild reconstitution, wage subsidy programs) require institutional
infrastructure that presupposes a functioning production base to recruit into. Equipment
economics, by contrast, is bounded and testable: given a realistic capital cost,
throughput, energy source, and organizational form, does the unit math close under
modern wages and at modern price points? That question can be answered with
research-paper-level estimates, and the answer — positive or negative — is a
fundable and publishable result. This is why the working hypothesis centers on
equipment redesign, and why the four falsifiers are explicitly pre-registered: if the
binding constraint is elsewhere, the project says so.

---

## 3. Three Economic Lenses as Parallel Viability Frames

*(Spec Section 6)*

Every catalog entry is evaluated under three parallel economic lenses — market,
cooperative, and civic — reflecting the three plausible organizational forms under
which local production might be restored. No single lens is privileged; the same
equipment design may be viable under one lens and not another, and the pattern of
those verdicts is informative.

The **market lens** evaluates viability as a private business, measuring payback
years and operator annual take-home after wage against thresholds defined per scale.

The **cooperative lens** evaluates viability under the member-ownership / commons
model, measuring the minimum member count required for the economics to close against
the feasible member pool at the target scale.

The **civic lens** evaluates viability as a municipal public good, measuring
per-household annual cost and hours-of-use per capita against thresholds defined per
scale.

Each lens produces a `win | marginal | fail` verdict and a primary numeric metric.
Formal definitions, formulas, and scale-specific thresholds are in
`corpus/program/ECONOMIC-LENSES.md` and `corpus/program/SCALES.md`. This section
states the conceptual frame; the math is not duplicated here.

---

## 4. Three Scales as First-Class Variable

*(Spec Section 3)*

Settlement scale is a first-class variable in every evaluation. The three scales are:

- **Village** — 500–2,000 residents
- **Town** — 2,000–15,000 residents
- **Small city / district** — 15,000–75,000 residents

Scale is not a tie-breaker or a filter applied after the primary evaluation; it is one
of the two primary axes of the evaluation matrix (the other being lens). Every catalog
entry is evaluated at all three scales under all three lenses, producing a 3 × 3 = 9
cell results block. An equipment design that wins only at town scale under the
cooperative lens and fails elsewhere is a meaningful, specific finding. Scale
determines demand pool, labor availability, capital access, and the feasibility
thresholds for all three lenses. Parameter values per scale are defined in
`corpus/program/SCALES.md`. This section states the conceptual role of scale; the
parameters are not duplicated here.

---

## 5. Catalog as Living Artifact

*(Spec Sections 4, 5, 8)*

The catalog is the primary evidentiary artifact of the CERES project. It is not a
recommendation list; it is the evidence base against which the working hypothesis is
tested. This distinction has structural consequences.

Designs iterate. A catalog entry begins at `status: draft`, advances through panel
review to `status: reviewed`, and — after all three editorial reviewers pass it with
no blocking findings — reaches `status: validated`. An entry can also be `deprecated`
or `superseded` when a later design replaces it or when analysis finds the design
non-viable.

Deprecated entries are not deleted. They remain in the catalog, linked by the
`supersedes:` field in the entry that replaced them. A deprecated entry is a finding:
it documents what was tried, why it did not work, and what was learned. Removing it
would destroy part of the evidentiary record. The same logic applies to entries that
produce `fail` verdicts across the full evaluation matrix: a consistently failing
design, if it spans a realistic region of the design space, is evidence toward the
scientific null, not a gap to be hidden.

The catalog is the only place where simulation results live. The 9-cell `results:`
block in each entry's frontmatter is populated by Tier A simulation output; there is
no separate results database. The catalog file is its own evaluation record.

---

## 6. Relationship to Historical Precedent

*(Spec Section 4.1, Section 12; MAXIM citation pattern)*

Historical production forms — medieval European forges, Edo-era Japanese smithing
cooperatives, Song-dynasty ceramics workshops — enter the CERES framework as
requirements specifications, not as design templates. Phase 1 research asks: what
did each historical form *do*, at what throughput, with what energy input, at what
operator skill level, under what organizational form? The answers become functional
requirements. Phase 2 design then asks: what modern equipment design meets those
functional requirements under current conditions?

This distinction — function versus form — is central to the method. A modern forge
design is not required to look like a medieval forge, use coal because medieval
forges used coal, or be organized as a guild because guilds were the historical
organizational form. It must reach the temperatures, sustain the throughput, and
operate at the capital and labor cost that make it viable in a contemporary settlement.
The historical form informs the requirements spec; it does not constrain the answer
to the requirements spec.

Anchor cultures (the 4–6 documented historical contexts in `research/cultures/`)
supply the primary research basis. Domain citations for archaeological, engineering,
and economic evidence are sourced from MAXIM (`reference`), not generated
independently. The research corpus documents which historical forms informed which
functional requirements, providing a traceable chain from historical precedent to
catalog design choice. A catalog entry whose `## Historical lineage` section cites no
research-corpus document is unsupported and cannot advance past `draft`.

---

## 7. Success, Null Result, and Failure

*(Spec Section 11.1–11.3)*

CERES pre-registers its acceptance criteria before Phase 1 begins, not after the
evidence arrives.

### 7.1 Success — Validated Hypothesis

The working hypothesis is validated if, across the 15 smithing catalog entries,
**at least one design achieves `win` under at least one lens at at least one scale**,
with all supporting fields (`market_price_per_unit`, `operations_reality`,
`lens_context`) defensible under editorial review. A validated hypothesis produces a
publishable playbook and a fundable pitch.

### 7.2 Success — Scientific Null Result

If the 15 entries span the realistic design space (electric / propane / coal /
induction / hybrid × single-owner / shared / civic × small / medium / large
footprint) and **none achieves `win` under any lens at any scale**, this is a
**scientific null**, not a project failure. The project deliverable in this case is
a revised pitch: "modern smithing cannot be restored by equipment redesign alone in
the three-scale developed-economy context; here is what the research reveals is
actually required." This outcome is publishable and valuable. CERES pre-registers
acceptance of null results.

### 7.3 Failure

The project is a failure only if:

- Fewer than 15 entries are authored, or the authored entries do not span the
  realistic design space; OR
- Editorial review finds systemic citation or numeracy failures that invalidate the
  results; OR
- The research corpus is too thin to evaluate the hypothesis one way or the other.

Failure is a process outcome, not an evidence outcome. A rigorous null is success;
a shoddy validation is failure.
