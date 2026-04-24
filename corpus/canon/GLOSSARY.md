---
title: CERES Canonical Glossary
version: "1.0"
created: 2026-04-18
spec: specs/2026-04-18-ceres-design.md
---

# CERES Canonical Glossary

This glossary is authoritative. When a term defined here appears in any CERES
artifact — catalog entries, research documents, playbook files, pitch narrative,
role files, simulation code, or review outputs — it carries precisely the meaning
given here, no more and no less. Contributors must add new terms to this file
before using them with a novel meaning in any artifact. A term used in a document
that conflicts with its definition here is a scope finding (E-2, P1 or P2
depending on severity).

Terms are listed alphabetically. Each entry is 1–3 sentences.

---

## A

**Applies_to** — a YAML frontmatter field in every role file (`.roles/**/*.md`)
listing the artifact types that role is eligible to review: one or more of `spec`,
`plan`, `catalog-entry`, `playbook-file`, `pitch-narrative`. The `ceres-check` skill
reads this field to filter roles by artifact type before running its checklist.

**Anchor culture** — one of the 4–6 historical cultures (medieval Northern Europe,
Song-era China, Tokugawa Japan, Islamic Golden Age, Andean ayllu, American frontier)
whose documented production forms serve as the primary research basis for extracting
functional requirements. Anchor cultures supply the requirements specification;
modern catalog designs are not required to replicate them directly.

**Apprentice-friendly** (added beyond plan task list) — a catalog-entry frontmatter
flag (`apprentice_friendly: true/false`) indicating whether the equipment and workflow
support training an operator from journeyman level or below. An entry marked
apprentice-friendly must describe, in the `operations_reality` block or prose, what
the learning curve actually requires; the flag without that support is a P-4 critique
target.

## B

**Board** (added beyond plan task list) — the per-trade tier of domain experts
assembled on demand when a catalog entry, playbook file, or pitch narrative makes a
specific technical claim beyond the panel's generalist expertise (e.g., exact forge
temperatures, fermentation chemistry, textile-fiber degradation). Unlike the panel,
the board is not permanent; it is assembled per artifact, not per trade wholesale.
Board composition spans three specialist types: domain-history, modern-practitioner,
and adjacent-engineering.

**Break-even (cooperative)** — the minimum number of cooperative members at which
combined dues and shared labor cover the total annualized cost of the equipment,
including capital amortization, maintenance, consumables, and floor space. The
cooperative lens pass condition requires this count to be achievable within the
feasible member pool at the target settlement scale.

## C

**Catalog entry** — a single markdown file under `catalog/<trade>/entries/` describing
one equipment design according to the canonical schema, including structured YAML
frontmatter (economics, throughput, operator profile, operations reality, lens fit,
lens context, simulation parameters, evaluation results) and required prose sections
(summary, design rationale, historical lineage, key assumptions, known risks, iteration
log). Each file is its own evaluation record; there is no separate results database.

**Civic lens** — viability evaluation of a catalog entry under the municipal /
public-goods model, analogous to a library or fire department: capital amortized over
a 25–40-year municipal lifespan, operations funded by the tax base or a dedicated
budget line. The primary metrics are per-household annual cost and hours-of-use per
capita; the pass condition requires both to meet thresholds defined per scale in
`corpus/program/SCALES.md`.

**Consumables lead-time** (added beyond plan task list) — the number of days between
ordering a consumable (refractory lining, replacement coil, raw materials) and its
arrival at the operator's facility, as captured in `operations_reality.consumables_lead_time_days`.
Lead time is a practical failure mode: an operator who cannot source a consumable
within a reasonable window cannot sustain throughput, and the worst-case figure
(`worst: N days`) is the operationally relevant number, not the typical case.

**Cooperative lens** — viability evaluation of a catalog entry under the member-
ownership / commons model, where capital is split across member contributions, tools
are shared, and governance is structured according to documented rules. A cooperative
label requires a `lens_context.cooperative` block specifying membership boundary,
rules source, monitoring mechanism, graduated sanctions, conflict resolution, and
Ostrom principles addressed; the label without this governance sketch is a P-2
Commons Theorist critique and an editorial hold.

## D

**Domain_signals** — a YAML frontmatter field in every role file listing
keyword strings that indicate an artifact is in that role's domain of expertise
(e.g., `["market", "payback", "ROI", "wage"]` for P-1 Market Economist). The
`ceres-check` skill counts how many domain signals appear in the artifact's content
to compute a relevance score used to prioritize which roles are most applicable.

**Demand collapse** — one of the four pre-registered falsifiers for CERES's working
hypothesis. Demand collapse holds when consumers prefer industrial goods for reasons
durable to price reduction — consistency, safety perception, or brand trust —
meaning equipment redesign cannot restore a market that was not lost due to equipment
economics.

**Deprecated** (added beyond plan task list) — a catalog-entry status value indicating
the design has been superseded or found non-viable and is no longer recommended. A
deprecated entry remains in the catalog and is linked by `supersedes:` to whatever
replaced it; entries are not deleted. The deprecated status is a finding, not a
failure, and is part of the project's commitment to honest null results.

## E

**Editorial** (added beyond plan task list) — the three-reviewer tier (E-1 Citation
Auditor, E-2 Scope Keeper, E-3 Numeracy Checker) that runs a final pass on artifacts
at the promotion gate from `reviewed` to `validated`. Editorial reviewers enforce
form, not substance: citation completeness, scope adherence, and unit-economics
sanity. All three editorial reviewers run on every artifact that reaches the
promotion stage; the pass is automatic, not a conversation.

**Evaluation matrix** — the 3 scales × 3 economic lenses = 9 contexts applied to
every catalog entry. Each context produces a `win | marginal | fail` verdict and a
primary numeric metric (payback years for market, break-even member count for
cooperative, per-household annual cost for civic). The 9-cell `results:` block in
each catalog entry's frontmatter holds the simulation output for the full matrix.

**Everyday trade** — a trade producing essential goods at inelastic demand, where
consumers will pay for the good regardless of price variation within a reasonable
range (bread, meat, cloth, leather, metalwork, ceramics, wood). Everyday trades form
the primary scope tier of the CERES catalog, with approximately 12 trades targeted.
Economic modeling for everyday trades assumes stable baseline demand, unlike
specialty trades.

## F

**Falsifier** — a specific, pre-registered condition under which CERES's working
hypothesis (Section 2 of the spec) is invalidated for a given trade. Four falsifiers
are pre-registered: demand collapse, regulatory capture, labor-regime dependency, and
supply-chain disappearance. A trade for which a falsifier holds strongly produces a
pivot finding rather than a viability verdict; this outcome is a scientific
contribution, not a project failure.

**Functional requirement** — a trade-specific capability that any equipment design for
that trade must achieve, derived from documented historical production forms rather
than from modern design preferences. Examples: "forge must reach 1,100 °C sustained
for forge-welding"; "bread oven must hold 230–260 °C for 45 minutes without
reloading fuel." Functional requirements are the output of Phase 1 research and live
in `research/trades/<trade>/REQUIREMENTS.md`.

## L

**Labor-regime dependency** — one of the four pre-registered falsifiers for CERES's
working hypothesis. This falsifier holds when historical viability rested on household
labor, apprentice servitude, or customary obligations that cannot be reproduced
ethically, making per-unit economics incomparable to a modern wage-based operation.

**Lens** — one of three economic evaluation frames (market, cooperative, civic)
applied to every catalog entry. Each lens scores viability using a different rule,
different inputs, and different pass conditions, reflecting the distinct organizational
logic of private profit, member-owned commons, and municipal public goods respectively.
The lens framework is formalized in `corpus/program/ECONOMIC-LENSES.md`.

**Lens context** (added beyond plan task list) — the required supporting-detail block
in catalog entry frontmatter (`lens_context.cooperative` and/or `lens_context.civic`)
that provides the governance, political, or structural information needed to justify a
`good` or `marginal` lens-fit label. A lens-fit label without the corresponding
lens-context block is incomplete and cannot be promoted past `draft`.

**Lens fit** (added beyond plan task list) — the per-lens, per-catalog-entry
tri-state signal (`good | marginal | fail`) recorded in the `lens_fit:` frontmatter
field, summarizing the entry's suitability under each economic lens before simulation.
Lens fit is a design-level annotation; the simulation's 9-cell `results:` block
provides the computed verdicts. When the two diverge materially, the discrepancy
should be documented in `## Key assumptions`.

**Local production** — production of goods for local consumption by operators living
in the same town or region as their customers, using equipment scaled and organized
for that settlement rather than for national or global distribution. CERES does not
claim local production is superior to industrial supply; it tests whether it is
economically viable as an option alongside industrial supply.

## M

**Market lens** — viability evaluation of a catalog entry under the private-profit
model: a single operator or small business funding capital from their own resources,
earning revenue by selling goods at market-clearing prices. The primary metrics are
payback years and operator annual take-home after wage; the pass condition requires
payback ≤ 8 years and operator earnings ≥ the scale-appropriate median wage threshold
defined in `corpus/program/SCALES.md`.

## O

**Operations reality** — the frontmatter block (`operations_reality:`) in a catalog
entry capturing the practical failure modes and variance that the average-case
`sim_params` miss: first-year equipment failures (item, estimated hours to failure,
replacement cost, replacement lead time), consumables lead time (typical and worst
case), throughput variance (seasonal pattern, worst-month and best-month fractions of
average), and operator impact (noise, heat, emissions, physical demand). This block
satisfies the P-4 Craft Practitioner's core review requirement and is mandatory for
any entry aspiring to `reviewed` status.

**Operator skill floor** (added beyond plan task list) — the minimum skill level an
operator must have to run the equipment safely and achieve the stated throughput, as
captured in the `operator_skill_floor:` frontmatter field (e.g., `journeyman`,
`master`, `trained-novice`). The skill floor has direct implications for the
labor-regime falsifier: a design that requires a master smith implicitly requires a
functioning apprenticeship pipeline, which may not exist at target scales.

**Ostrom principles** (added beyond plan task list) — the eight design principles for
sustainable governance of common-pool resources identified by Elinor Ostrom, used in
CERES's `lens_context.cooperative` block to assess whether a proposed cooperative
governance structure is institutionally robust. The `ostrom_principles_addressed:`
field lists which of the eight principles the governance sketch satisfies; Principles
7 and 8 (recognition by external authorities; nested enterprises) are noted as
non-applicable at single-cooperative scale.

## P

**Panel** (added beyond plan task list) — the six permanent reviewers (P-1 through
P-6) who review every CERES artifact. The panel represents six productive intellectual
tensions: private profit (P-1) vs. commons (P-2), voluntary association (P-2) vs.
municipal stewardship (P-3), library model (P-3) vs. competitive market (P-1),
practitioner reality (P-4) vs. funder rigor (P-6), historical realism (P-5) vs.
narrative compression (P-6), and modern adaptation (P-4) vs. historical accuracy
(P-5). Panel review produces qualitative findings; numeric scoring is a separate step
against `scoring/RUBRIC.md`.

**Payback** (added beyond plan task list) — the number of years required to recover
the capital cost of a catalog entry from annual net income under the market lens,
calculated as `capital_cost.mid / annual_net`. The market lens pass condition requires
payback ≤ 8 years; an entry claiming `market: win` with an implied payback above this
threshold is a P1 internal contradiction (E-3).

**Pitch narrative** — the single white-paper-style document (`playbook/pitch/PITCH-NARRATIVE.md`)
framing the CERES project for funders: the problem (what changed when local
production declined), the approach (catalog-driven design, evaluation matrix,
simulation), the findings (winning patterns, failure modes, structural insights), and
the ask (pilot program outline, funding envelope, milestones). The pitch cites the
catalog and playbook as evidence and does not generate claims independently.

**Pivot finding** (added beyond plan task list) — the output for a trade where one or
more falsifiers hold strongly, replacing the standard viability verdict. A pivot
finding documents what the binding constraint actually is (not equipment economics)
and what would genuinely be required to restore production in that trade. A pivot
finding is a scientific contribution, not a project failure, and is treated as a
first-class deliverable.

**Playbook** — a per-trade, per-scale markdown file (`playbook/<trade>/<scale>.md`)
naming the 3–5 winning catalog entries for that trade at that settlement scale, with
a one-line explanation of why each wins, an implementation sketch (pilot, staffing,
capex timeline, revenue ramp), a capital ask, and explicitly named open risks. There
are three playbook files per trade (one per scale) and one additional cross-trade
pitch narrative.

**Promotion gate** (added beyond plan task list) — the checkpoint at which a catalog
entry advances from `status: reviewed` to `status: validated`, requiring all three
editorial reviewers (E-1, E-2, E-3) to pass the entry with no blocking (P1) findings
open. The panel review of the entry as a draft is a separate earlier step; the
promotion gate is editorial-only. Three or more open P1 findings from any single
editorial reviewer hold the entry.

## R

**Rubric_contribution** — a YAML frontmatter field in every role file (v1.1+) with
two sub-fields: `primary` (a list of dimension IDs, e.g. `[D4]`) and `secondary`
(a list of dimension IDs, e.g. `[D2, D6]`). Primary dimensions are weighted at
1.0x when aggregating role findings into a rubric dimension score; secondary
dimensions are weighted at 0.5x. The `ceres-check` skill uses this field to
build the Dimension Aggregate table. The authoritative mapping is in
`scoring/RUBRIC.md` Section 6, but the role files are the canonical source;
the RUBRIC table is derived from them.

**Regulatory capture** — one of the four pre-registered falsifiers for CERES's working
hypothesis. This falsifier holds when trades were displaced primarily by zoning,
licensing, food-safety, or tax regimes that equipment redesign alone cannot navigate,
meaning the binding constraint is regulatory, not economic.

**Research corpus** (added beyond plan task list) — the body of Phase 1 artifacts
produced for each trade: functional requirements documents
(`research/trades/<trade>/REQUIREMENTS.md`), historical-forms documents
(`research/trades/<trade>/HISTORICAL-FORMS.md`), source bibliographies
(`research/trades/<trade>/SOURCES.md`), and the per-trade chapters within each anchor
culture's directory. The research corpus is the evidentiary foundation for catalog
design choices; a catalog entry whose `## Historical lineage` cites no research-corpus
document is unsupported.

## S

**Scale** — one of three settlement sizes used as the primary scope variable for
viability evaluation: village (500–2,000 residents), town (2,000–15,000 residents),
or small-city / district (15,000–75,000 residents). Scale determines demand pool,
labor availability, capital access, and the feasibility thresholds for all three
economic lenses; parameters per scale are defined in `corpus/program/SCALES.md`.

**Scientific null** (added beyond plan task list) — the outcome if the 15 smithing
catalog entries span the realistic design space and none achieves `win` under any
lens at any scale. A scientific null is a pre-registered acceptable project outcome
(not a failure); it produces a revised pitch documenting that equipment redesign is
not the binding constraint for this trade in the three-scale developed-economy
context, which is itself a fundable and publishable finding.

**Specialty trade** — a trade producing low-volume, elastic-demand goods where
consumers' willingness to pay varies significantly with quality, brand, and
provenance (armory-grade metalwork, tapestries, fine ceramics, bespoke garments).
Specialty trades form the secondary scope tier of the CERES catalog and require
different economic modeling than everyday trades because demand is not guaranteed by
household necessity.

**Supply-chain disappearance** — one of the four pre-registered falsifiers for CERES's
working hypothesis. This falsifier holds when upstream inputs required for a trade
(local grain mills, regional tanneries, accessible steel supply) have vanished and
cannot be reconstituted at the scale of equipment redesign alone.

## T

**Tier A / B / C simulation** — the three-tier layered simulation approach. Tier A
(scenario comparator) runs deterministic lens math on every (entry × scale × lens)
cell and populates the 9-cell `results:` block in each catalog entry; it runs on every
entry. Tier B (system dynamics) models the town as a system, capturing inter-trade
dependencies, cascade risk, and resilience under shocks; it requires at least two
trades to be meaningful and is deferred until after the vertical slice. Tier C
(agent-based) is reserved for specific high-value targeted questions (labor pipeline
failures, regulatory shocks, generational succession) and is not run on every cell.

## V

**Validated** — the catalog-entry promotion status (`status: validated`) reached after
the entry has passed full panel review as a draft, all P1 findings have been resolved,
and all three editorial reviewers (E-1, E-2, E-3) have issued a pass verdict with no
blocking findings open. A validated entry has defensible, cited economics and is
eligible to be cited in playbook files and the pitch narrative.

**Vertical slice** — the first full pass of the CERES pipeline on one trade
(smithing/forge), producing all five phase artifacts: research documents (REQUIREMENTS,
HISTORICAL-FORMS, SOURCES, per-culture chapters), catalog entries (~15 forge designs,
all schema-complete), Tier A simulation results (all 15 × 9 = 135 evaluation cells
populated), playbook files (village, town, small-city), and a first-draft pitch
narrative. The vertical slice proves the pipeline and serves as the template for all
subsequent trades.

## W

**Working hypothesis** — the claim CERES is testing (spec Section 2): local artisan
production in industrialized economies declined primarily because the equipment, scale,
and organizational forms inherited from pre-industrial times no longer penciled out
against industrial competition; redesigning the equipment for modern contexts, pairing
it with the right organizational form, and matching it to the right settlement scale
will make a meaningful share of these trades viable again. The working hypothesis is
tested, not assumed; the pattern of `win | marginal | fail` verdicts across the
evaluation matrix is the evidence for or against it.
