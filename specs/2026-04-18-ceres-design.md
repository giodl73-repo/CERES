# CERES — Local Production Atlas

## Design Specification

**Date:** 2026-04-18
**Version:** 0.3 (revised 2026-04-19 after ceres-check on v0.2)
**Author:** Giovanni Della-Libera + Claude Opus 4.7
**Status:** Draft — revised twice; v0.3 addresses 12 P2 + 5 P3 findings from ceres-check; pending author review before implementation planning

---

## 1. Project Identity

- **Codename:** CERES (after CeCe, Giovanni's chicken; CERES = Roman goddess of grain, harvest, and nourishment of settlements)
- **Mission:** Design and evaluate a catalog of modern artisan-production equipment — forges, ovens, looms, kilns, and the rest — that hits price and operational points enabling towns and cities to restore meaningful local production. Anchor the designs in historical functional requirements; evaluate them under realistic economic conditions; produce a fundable-quality plan.
- **Sibling projects:** LUCIA (C:\src\chronicle — narrative encyclopedia of human cultures), FELICE/RMM (C:\src\rmm — theoretical framework + simulation), MAXIM (C:\src\reference — encyclopedic knowledge base).
- **Relationship:** Fully independent. Own CLAUDE.md, schema, playbook, simulation code. Borrows patterns from siblings: Chronicle's "many instances, consistent schema" model for the catalog; RMM's canon/program/simulations structure for the theoretical framework. References MAXIM for domain citations (archaeology, ceramics, architecture-history, chemical-eng, agriculture, etc.).
- **Repository:** https://github.com/giodl73-repo/CERES.git
- **Quality bar:** Research-paper-level estimates. Order-of-magnitude unit economics with citations. Conceptual design specs, not real supplier BOMs.

---

## 2. Working Hypothesis

CERES's working hypothesis — to be tested, not assumed:

> Local artisan production in industrialized economies declined primarily because the equipment, scale, and organizational forms inherited from pre-industrial times no longer penciled out against industrial competition. Redesign the equipment for modern contexts (energy sources, regulations, labor costs, shareability patterns), pair it with the right organizational form (market / cooperative / civic), match it to the right settlement scale, and a meaningful share of these trades becomes viable again.

**Falsifier.** If the historical research (Phase 1) reveals that the binding constraint was not equipment economics but one of the following, CERES must acknowledge it and adapt:

- **Demand collapse** — consumers genuinely prefer industrial goods for reasons durable to price reduction (consistency, safety perception, brand trust). Equipment redesign cannot restore what was never lost.
- **Regulatory capture** — trades were displaced by zoning, licensing, food-safety, or tax regimes that equipment redesign cannot navigate.
- **Labor-regime dependency** — historical viability rested on household labor, apprentice servitude, or customary obligations that cannot be reproduced ethically.
- **Supply-chain disappearance** — the upstream inputs (local grain mills, tanneries, regional steel) vanished and cannot be reconstituted at equipment scale alone.

**Pivot criteria.** If any falsifier holds strongly for a given trade, CERES's analysis for that trade pivots from "here is equipment that restores viability" to "here is what would actually be required, and whether equipment is part of the answer or not." A trade where equipment is shown to be *not* the binding constraint is a finding, not a failure.

CERES tests the hypothesis by building a catalog of equipment designs and evaluating each design against a matrix of contexts. The pattern of verdicts — across trades, across scales, across lenses — is the evidence for or against the hypothesis.

---

## 3. Scope Decisions (Locked)

| Decision | Value |
|---|---|
| Primary output | All three artifacts, sequenced: research corpus → framework → playbook/pitch |
| Trade scope | Two-tier. **Everyday trades** (bread, meat, cloth, leather, metalwork, ceramics, wood — ~12 trades) + **specialty trades** (armory-grade metalwork, tapestries, fine ceramics, bespoke garments). Different economic models per tier. |
| Historical scope | 4–6 representative cultures as research anchors (medieval Northern Europe, Song-era China, Tokugawa Japan, Islamic Golden Age, Andean ayllu, American frontier). Corpus structured so additional cultures slot in without re-architecture. |
| Modern unit | Three scales: **village** (500–2,000), **town** (2,000–15,000), **small city / district** (15,000–75,000). Scale is a first-class simulation variable. |
| Economic lenses | Three parallel evaluation frames: **market** (private profit), **cooperative / commons** (member-funded), **civic** (municipal, library-model). Same catalog entry evaluated three ways. |
| Simulation approach | Layered. **Tier A** — scenario comparator (runs every cell). **Tier B** — system dynamics (town-as-system, inter-trade dependencies). **Tier C** — agent-based (targeted questions only). |
| Execution approach | **Vertical slice.** Drive smithing/forge end-to-end first (research → catalog → sim → playbook). Prove the pipeline. Then replicate pattern for other trades. |
| Smithing as template | Smithing was selected as the first-slice trade because it is an equipment-tractable, regulatory-light trade with strong historical precedent — a deliberately accessible first case. Whether the pipeline pattern generalises to harder trades (weaving with fibre-supply complexity, pottery with kiln permitting, baking and food trades with health-code and licensing overhead) is **itself a finding of the project**, not an assumption. The vertical slice proves the pipeline exists; a second-trade attempt is required to test its generalisability. |

---

## 4. Architecture

### 4.1 The Pipeline

```
Research  →  Design Catalog ★  →  Evaluation Matrix  →  Simulation  →  Playbook + Pitch
   ↑                                                                          │
   └──────────── feedback loop: failed designs revised and re-evaluated ──────┘
```

- **Research (Phase 1)** — extract *functional requirements* from historical forms. What must a forge do? Temperature range, throughput, fuel options, mobility, operator skill floor. History gives the requirements spec, not the design. Each trade's `research/trades/<trade>/REQUIREMENTS.md` must explicitly adjudicate a **decline-or-restructuring verdict** — one of `decline | restructuring | displacement | ambiguous` — with a one-paragraph justification. This step prevents the research from defaulting to a "decline" framing when the historical record may show restructuring (local production moved form, not disappeared). The verdict is required before a trade's catalog entries can move to `reviewed` status.
- **Design Catalog (Phase 2) — the star.** Per trade, 20–40 equipment variants spanning different design tradeoffs (size, capital cost, energy source, throughput, specialization, shareability, skill floor). Each entry = one markdown file with structured frontmatter.
- **Evaluation Matrix (Phase 3)** — every catalog entry evaluated under 9 contexts (3 scales × 3 lenses).
- **Simulation (Phase 4)** — the engine that runs the evaluation matrix. Tier A produces the 9 results per entry. Tier B answers systemic questions Tier A cannot. Tier C is reserved for specific targeted questions.
- **Playbook + Pitch (Phase 5)** — per-trade, per-context playbook files identifying winning designs + implementation sketch; a single pitch-narrative document frames the whole project for funders.

### 4.2 Repository Structure

```
CERES/
├── README.md
├── CLAUDE.md                          # project conventions
├── specs/                             # design specs (top-level, first-class)
├── plans/                             # implementation plans (top-level)
├── docs/
│   ├── PIPELINE.md                    # 5-phase workflow guide
│   ├── STYLE-GUIDE.md                 # citation & writing conventions
│   └── METHODOLOGY.md                 # how estimates are made and defended
│
├── corpus/                            # RMM-pattern: canon + program
│   ├── canon/
│   │   ├── THEORY.md                  # local-production framework
│   │   ├── GLOSSARY.md
│   │   └── PRINCIPLES.md              # what makes a "good" catalog entry
│   └── program/
│       ├── ECONOMIC-LENSES.md         # market / coop / civic definitions + formulas
│       ├── SCALES.md                  # village / town / small-city parameters
│       ├── CURRENCIES.md              # multi-currency FX conversion table
│       └── VALIDATION.md              # how sim output is sanity-checked
│
├── research/                          # Phase 1: functional requirements from history
│   ├── cultures/                      # 4–6 anchor cultures, Chronicle-pattern
│   │   ├── medieval-northern-europe/
│   │   ├── song-china/
│   │   ├── tokugawa-japan/
│   │   ├── islamic-golden-age/
│   │   ├── andean-ayllu/
│   │   └── american-frontier/
│   └── trades/                        # functional requirements per trade
│       ├── smithing/
│       │   ├── REQUIREMENTS.md
│       │   ├── HISTORICAL-FORMS.md
│       │   └── SOURCES.md
│       ├── baking/                    # stubbed now, populated later
│       ├── weaving/
│       └── ...
│
├── catalog/                           # Phase 2: THE STAR
│   ├── smithing/                      # vertical slice target
│   │   ├── README.md                  # overview of forge catalog
│   │   ├── SCHEMA.md                  # canonical catalog-entry schema
│   │   └── entries/
│   │       ├── 001-backyard-propane-compact.md
│   │       ├── 002-induction-modular-250a.md
│   │       ├── 003-shared-toollibrary-coal.md
│   │       └── ...                    # 15 in vertical slice; 20–40 long term
│   ├── baking/                        # stubbed; populated phase 2+
│   ├── weaving/
│   └── ...
│
├── simulations/                       # Phase 4: layered A → B → C
│   ├── tier-a-comparator/
│   │   ├── README.md
│   │   ├── model.py                   # or .ipynb
│   │   ├── VALIDATION.md
│   │   └── results/
│   ├── tier-b-system-dynamics/
│   │   └── ...
│   └── tier-c-agent-based/
│       └── ...
│
├── playbook/                          # Phase 5
│   ├── smithing/
│   │   ├── village.md                 # winning designs @ 500–2k
│   │   ├── town.md                    # @ 2k–15k
│   │   └── small-city.md              # @ 15k–75k
│   └── pitch/
│       └── PITCH-NARRATIVE.md
│
├── agents/                            # Chronicle-pattern
│   └── ...
├── .roles/
│   └── roles/                         # panel reviewer roles
├── reviews/                           # panel outputs
├── scoring/
│   └── RUBRIC.md                      # catalog-entry quality scoring
└── sources/                           # raw citations, images
```

**Scaling properties:**
- Every trade directory is parallel (`research/trades/<trade>/`, `catalog/<trade>/`, `playbook/<trade>/`). Adding a trade = duplicate-and-fill, no re-architecture.
- Catalog entries are individual markdown files. Adding design #41 does not touch the first 40.
- Framework material (corpus/canon, corpus/program) is trade-agnostic, defined once.
- Simulation tiers are independent. Tier A can ship without Tier B or C existing.

---

## 5. Catalog-Entry Schema (Canonical)

Every catalog entry is one markdown file with YAML frontmatter. Frontmatter is structured; simulation code ingests it directly. Prose sections follow.

```markdown
---
id: forge-003
trade: smithing
name: Shared Tool-Library Coal Forge (medium footprint)
tagline: Community-owned coal forge with member-booked shifts
status: draft              # draft | reviewed | validated | deprecated | superseded
version: 0.2
supersedes: null
inspirations: [medieval-european-village-forge, edo-blacksmith-cooperative]

# Physical envelope
footprint_m2: 35
ceiling_min_m: 3.5
ventilation: mechanical-extraction-required

# Energy
energy_source: coal
energy_consumption_per_active_hour: 8 kg coal
backup_fuel: propane

# Throughput (per-trade sub-structure but always named "throughput")
throughput:
  units_per_hour: { small_work: 6, medium_work: 2, large_work: 0.5 }
  max_active_hours_per_week: 45

# Operator profile
operator_skill_floor: journeyman
operators_concurrent: 1-2
apprentice_friendly: true
apprentice_path:                    # Required prose sub-fields when apprentice_friendly: true
  training_stages: "Stage 1 (0–6 mo): safety, fire management, basic stock prep. Stage 2 (6–18 mo): small work, tool maintenance. Stage 3 (18–36 mo): medium work, independent production. Competency gates at each stage."
  time_to_independent_operation: "~36 months to journeyman standard on this equipment"
  succession_note: "Forge is designed for apprentice co-presence during production; skill transfer is built into normal operations, not a separate program"

# Economics (order-of-magnitude, cited; multi-currency aware)
economics:
  currency: USD
  capital_cost: { low: 18000, mid: 28000, high: 45000 }
  install_cost: 6000
  annual_maintenance: 1500
  annual_consumables: 4200
  floor_space_rent_per_year: 4800
  # Market-clearing output pricing — required for MARKET lens evaluation
  market_price_per_unit: { low: 32, mid: 45, high: 70 }
  industrial_baseline_price: 12   # USD/unit; named industrial-alternative price. Required when lens_fit.market is good or marginal. Must be cited.
  pricing_notes: "Per small-work unit equivalent. Premium over industrial baseline ($12/unit, e.g. imported hardware-store equivalent) assumes direct-to-consumer and repair-work mix. Cited."
  pricing_validation: "Market price evidence: comparable community-forge rate cards (ToolLibrary.org 2024 survey) + direct-to-consumer repair pricing from three regional smiths; willingness-to-pay supported by cited survey data, not cost-plus residual."

# Operations reality — what actually breaks and what an operator's worst month looks like
# Required for P-4 (Craft Practitioner) lens; separate from regulatory compliance.
operations_reality:
  first_year_failures:
    - item: "Primary coil / heating element"
      estimated_hours_to_failure: 1800
      replacement_cost: 1200
      replacement_lead_time_days: 21
      serviceable_by: specialist   # operator | journeyman | specialist
    - item: "Refractory lining (partial)"
      estimated_hours_to_failure: 2400
      replacement_cost: 400
      replacement_lead_time_days: 7
      serviceable_by: operator     # refractory patching is operator-trainable
  maintenance_schedule:
    daily:
      task: "Clean ash pan, inspect seals, check fuel line"
      performed_by: operator
    weekly:
      task: "Inspect refractory lining, lubricate moving parts, calibrate temp sensor"
      performed_by: operator
    quarterly:
      task: "Full refractory inspection; replace worn seals; check electrical connections"
      performed_by: journeyman
    annual:
      task: "Full refurbishment: replace lining if indicated, inspect structural components"
      performed_by: specialist
  startup_shutdown_overhead_per_day_min: 30  # minutes/day of non-productive operator time
  max_active_hours_realism_note: "45 hr/wk is the theoretical shift-hours ceiling; net of 30 min/day startup-shutdown overhead across a 5-day week, effective active production hours are approximately 41.5 hr/wk. sim_params.throughput_units_equiv_per_year uses the derated figure."
  consumables_lead_time_days: { typical: 5, worst: 30 }
  interruption_notes: "Optional. Typical intraday interruptions: customer walk-ins (~2–3 per day, 10 min avg), tool-change setup (~15 min per major work-type switch), apprentice instruction (~20 min/day when apprentice is present). These micro-interruptions are separate from startup_shutdown_overhead and should be folded into throughput_units_equiv_per_year estimates per METHODOLOGY.md guidance."
  throughput_variance:
    seasonal: "Fall/winter peak for repair work; summer trough"
    worst_month_fraction_of_average: 0.45
    best_month_fraction_of_average: 1.65
  operator_impact:
    noise_db: 85
    heat_exposure: "High near forge; adequate ventilation required"
    emissions: "Particulate, CO, small amounts of SOx with coal; zero with induction"
    physical_demand: "Moderate-heavy lifting; sustained standing"

# Regulatory notes (kept terse — flag showstoppers only)
regulatory_notes:
  zoning: "Light-industrial or mixed-use; coal restricted in many urban cores"
  emissions: "Particulate capture may be required above certain throughput"
  other: "OSHA ventilation standards for hot-work; check local fire code"

# Context fit (tri-state per axis)
lens_fit:      { market: marginal, cooperative: good, civic: good }
scale_fit:     { village: marginal, town: good, small_city: good }

# Lens context — required supporting detail for any entry whose lens_fit is
# `good` or `marginal` in the corresponding lens. Governance / political /
# competitive structures that determine whether the label is earned.
lens_context:
  # Required when lens_fit.cooperative is good or marginal
  cooperative:
    membership_boundary: "Town residents + surrounding township, paid annual dues"
    rules_source: "Bylaws; member vote to amend with 2/3 majority"
    monitoring: "Equipment usage logged per session; monthly audit by elected steward"
    graduated_sanctions: "Warning → $50 fine → 30-day suspension → membership review"
    conflict_resolution: "Member-elected steward arbitrates; appeal to full member vote"
    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6]  # 7 and 8 NA at single-coop scale
    member_amendment_process: "2/3 vote at annual general meeting; 30-day notice required for agenda items; emergency amendments by 3/4 vote with 7-day notice"
    legal_form: "State-registered worker cooperative, LLC; municipal acknowledgment on file"
    scale_fit_note: "Rules calibrated for town-scale (2,000–15,000); participation quorum of 20 members is achievable at this scale but would be infeasible at village scale — see scale_fit.village: marginal"
  # Required when lens_fit.civic is good or marginal
  civic:
    political_coalition: "Municipal workforce-development grant + small-business allies"
    council_vote_estimate: "5-2 favorable; opposition argues tax burden"
    competes_with_private: "No existing private smith in target towns; civic facility fills gap"
    governance_form: "Municipally owned; operated by contracted master smith with apprentice program"
    budget_line: "Capital via 25-year bond; operations under workforce-development or parks-and-rec line"
    benchmark_comparison: "$2.28/hh/yr vs town library at $42/hh/yr and rec center at $68/hh/yr — well below comparable civic services; cost-per-beneficiary comparable when adjusted for specialized-user fraction"
    staffing_model:
      role: "contracted master smith + apprentice (part-time)"
      operator_fte: 1.0
      wage_assumption: 68000   # USD/yr; references SCALES.md scale-appropriate median skilled-trades wage
      wage_source: "corpus/program/SCALES.md §3 town-scale skilled-trades median"
      hours: "40 hrs/wk production + administration"
      hiring_notes: "Journeyman-or-master smith required; hiring pool is regional (100-mile radius typical); apprentice hired locally from workforce-development pipeline"
    civic_externalities:
      - "Apprentice training pipeline: produces 1–2 journeyman smiths per 3-year cycle, supplying regional repair capacity"
      - "Emergency production capacity: forge can produce or repair critical metal components (brackets, fittings, tools) during supply-chain disruptions"
      - "Repair culture: accessible civic forge reduces throwaway consumption of metal goods; repair-economy externality unpriced by market"
      - "Resilience anchor: operational forge sustains downstream trades (leatherwork needs rivets, carpentry needs hardware, masonry needs metal anchors)"

# Machine-readable simulation parameters
sim_params:
  cost_mean: 28000
  cost_sd: 8000
  throughput_units_equiv_per_year: 2400
  variable_cost_per_unit: 3.1
  labor_hours_per_unit: 0.6
  downtime_fraction: 0.12
  lifespan_years: 25

# Evaluation results (populated by simulation; 9 cells)
results:
  village_market: null
  village_coop: null
  village_civic: null
  town_market: null
  town_coop: null
  town_civic: null
  small_city_market: null
  small_city_coop: null
  small_city_civic: null

sources:
  - ref: "Weisdorf 2018, Economic History Review"
  - ref: "ToolLibrary.org 2024 capex survey"
---

## Summary
Prose description: what this forge is, who it's for, why it exists in the catalog.

## Design rationale
Why these choices. What problem this entry solves that others don't.

## Historical lineage
Historical forms that informed the design; modern precedents.

## Key assumptions
Where the economic numbers come from; which are solid, which are rough.

## Known risks / failure modes
Regulatory, labor pipeline, supply-chain dependencies.

## Iteration log
Dated notes as the design evolves.
```

**Rationale for this shape:**
- Trade-agnostic fields (footprint, economics, operator, lens_fit, scale_fit, operations_reality, lens_context) are consistent across all trades. Simulation code is written once and works for any trade.
- Trade-specific fields (contents of `throughput`) are namespaced under consistent top-level keys.
- `results:` block starts null and is populated by Tier A simulation output. The catalog file is its own evaluation record; no separate results database.
- `status` + `version` + `supersedes` track iteration. Failed designs remain in the catalog marked `deprecated`, linked to what replaced them.
- Multi-currency support: each entry declares its currency; FX conversion table (`corpus/program/CURRENCIES.md`) normalizes to a project base currency at evaluation time.
- Regulatory notes are deliberately terse: three short lines to flag showstoppers, not a legal treatise.
- **`market_price_per_unit`** is required for any entry with `lens_fit.market` set to `good` or `marginal` — the MARKET lens cannot evaluate without it. Uncited pricing is a P1 editorial finding. `pricing_notes` must name the industrial-competitor baseline price (see `economics.industrial_baseline_price` when `lens_fit.market` is `good` or `marginal`).
- **`operations_reality`** captures what the panel's Craft Practitioner (P-4) asks for and what the average-case sim_params miss: first-year failures (each with a `serviceable_by` value — `operator | journeyman | specialist`), a `maintenance_schedule` object with `performed_by` per cadence, `startup_shutdown_overhead_per_day_min` (non-productive operator minutes deducted when calculating throughput realism), `max_active_hours_realism_note` (declares whether the claimed `max_active_hours_per_week` is gross or derated), consumables lead time, variance / worst-month throughput, and operator impact. Paper designs assume the average case; real shops die in the tail.
- **`lens_context.cooperative`** is required for any entry with `lens_fit.cooperative` set to `good` or `marginal`. A coop label without a governance sketch is a romantic shorthand; this block forces the author to state membership, rules, monitoring, sanctions, conflict resolution, Ostrom-principle alignment, `member_amendment_process` (how rules can be changed), `legal_form` (registered entity status), and `scale_fit_note` (whether the governance rules are calibrated to the population size where this entry is viable).
- **`lens_context.civic`** is required for any entry with `lens_fit.civic` set to `good` or `marginal`. Names the political coalition, council-vote estimate, relationship to existing private operators, governance form, municipal budget line, `benchmark_comparison` (per-household annual cost vs. a named analogous civic service such as library or rec center), `staffing_model` (named role, wage referencing `corpus/program/SCALES.md`, FTE, hours, and hiring-pool realism), and `civic_externalities` (list of public-goods externalities the facility generates that the market does not price). A civic label without a political path and a cost benchmark is a wish; without an externalities list it cannot justify civic investment over alternatives.

---

## 6. Economic Lens Math

Each lens scores the same catalog entry with a different viability rule. Formulas live in `corpus/program/ECONOMIC-LENSES.md` and are applied uniformly.

**MARKET lens** (private business, profit motive)
- Inputs: capital, annual costs, throughput, market price, cost of capital
- Outputs: payback years, ROI, operator annual take-home after wage
- Pass condition: payback ≤ 8 years AND operator earns ≥ scale-appropriate median wage (thresholds per scale defined in `corpus/program/SCALES.md`)

**COOPERATIVE lens** (worker/member co-op)
- Inputs: capital split across N members, member dues, shared labor and tools
- Outputs: break-even member count, per-member annual contribution, utilization
- Pass condition: break-even member count ≤ feasible member pool at that scale

**CIVIC lens** (municipal, library / fire-department model)
- Inputs: capital amortized over municipal lifespan (25–40 years), tax cost per resident, public use hours; `lens_context.civic.staffing_model` (staffing cost incorporated in annual_operating_cost when civic facility employs an operator); `lens_context.civic.benchmark_comparison` (referenced when evaluating whether the per-household cost is politically defensible relative to peer services)
- Outputs: per-household annual cost, hours-of-use per capita
- Pass condition: per-household cost ≤ threshold AND usage rate ≥ threshold

Thresholds are defined in `corpus/program/SCALES.md` per scale (village/town/small-city). Each lens produces a `win | marginal | fail` verdict plus a primary numeric metric (payback years, break-even members, per-household cost).

---

## 7. Simulation Tiers

**Tier A — Scenario Comparator.** Deterministic math. For every (entry × scale × lens) cell, runs the appropriate lens rule and produces a verdict plus primary metric. Populates the 9-cell `results:` block in every catalog entry. Goal: every catalog entry has all 9 cells filled.

**Tier B — System Dynamics.** Models the town as a system: demand flows, production capacity, inter-trade dependencies (miller → baker, tanner → cobbler, forge repairs everyone). Answers systemic questions Tier A cannot — cascade risk, resilience under shocks, collapse dynamics. Output: dependency maps and resilience scores per scenario.

**Tier C — Agent-Based.** Reserved for high-value targeted questions: labor pipeline failures (smith retires, no apprentice), regulatory shocks, energy-price shocks, generational succession. Not run on every cell; only where Tier A/B flag a need.

---

## 8. Validation Strategy

- Every `sim_params` number in a catalog entry cites a source (historical cost data, modern equipment listing, trade-journal estimate). Uncited numbers block `status: validated`.
- Tier A outputs are sanity-checked against known real-world parallels (existing microbakeries, community forges, small textile operations) documented in `simulations/tier-a-comparator/VALIDATION.md`.
- A quality rubric (`scoring/RUBRIC.md`) scores catalog entries. `status: draft` → `reviewed` → `validated` gates require rubric score thresholds.
- Chronicle/Panel-style review pattern: reviewer roles in `.roles/` score catalog entries and flag issues.

---

## 9. Playbook + Pitch Output

**Per-context playbook files** (`playbook/<trade>/<scale>.md` — 3 files per trade).
For each file: top 3–5 winning designs, one-line "why it wins here," implementation sketch (pilot → staffing → capex timeline → revenue ramp), capital ask, open risks.

**Pitch narrative** (`playbook/pitch/PITCH-NARRATIVE.md`).
Single white-paper-style document: the problem (what changed when local production declined, what it costs communities); the approach (catalog-driven design + evaluation matrix + simulation); what we learned (winning patterns, failure modes, structural insights); the ask (pilot program outline, funding envelope, measurable milestones). Pitch cites the catalog and playbook as evidence.

**Competitive response prompt (required section in pitch narrative, Phase 5).** The pitch must address the most plausible incumbent counter-move: if a local smithing cooperative or civic forge demonstrates viability, what is the most likely response from existing industrial or regional supply chains? (Price undercutting? Supply-chain lock-in of consumables? Regulatory lobbying?) Authors are not required to resolve this question in the design spec, but Phase 5 pitch authors must address it explicitly as a stress-test of the pitch narrative's durability.

---

## 10. Phase-1 Vertical Slice — Definition of Done

The vertical slice is complete when all of the following exist for smithing:

| Deliverable | Target |
|---|---|
| `research/trades/smithing/REQUIREMENTS.md` | written, cited |
| `research/cultures/*/smithing.md` | 4–6 cultures, short chapters each |
| `catalog/smithing/SCHEMA.md` | finalized |
| `catalog/smithing/entries/*.md` | ~15 forge designs, all schema-complete |
| `corpus/program/ECONOMIC-LENSES.md` | three lens rules formalized |
| `simulations/tier-a-comparator/` | all 15 × 9 = 135 cells evaluated; `results:` populated in each entry |
| `simulations/tier-b-system-dynamics/` | scaffolded only (directory + README describing intended model). Tier B runs require at least two trades populated; deferred to after trade #2. |
| `playbook/smithing/{village,town,small-city}.md` | three files written |
| `playbook/pitch/PITCH-NARRATIVE.md` | first draft, smithing-only evidence |

15 entries is a deliberate floor for the first slice — enough variety to make the catalog meaningful, few enough that the vertical slice does not stall. Entry count grows after the pipeline is proven.

After the slice completes, subsequent trades (baking, weaving, pottery, leatherwork, etc.) replicate the same structure. The slice is the template.

---

## 11. Project Success Criteria

Distinct from Section 10's artifact-level definition of done, this section defines what counts as project-level success, failure, or scientific null — and commits to these criteria before Phase 1 begins, not after Phase 4 evidence arrives.

### 11.1 Success — Validated Hypothesis

The working hypothesis (Section 2) is validated if, across the 15 smithing catalog entries, **at least one design achieves `win` under at least one lens at at least one scale**, with all supporting fields (market_price_per_unit, operations_reality, lens_context) defensible under editorial review. A validated hypothesis produces a publishable playbook and a fundable pitch.

### 11.2 Success — Scientific Null Result

If the 15 entries span the realistic design space (electric / propane / coal / induction / hybrid × single-owner / shared / civic × small / medium / large footprint) and **none achieves `win` under any lens at any scale**, this is a **scientific null**, not a project failure. The project deliverable in this case is a revised pitch: "modern smithing cannot be restored by equipment redesign alone in the three-scale developed-economy context; here is what the research reveals is actually required." This outcome is publishable and valuable. CERES pre-registers acceptance of null results.

**Second-trade generalisability finding.** If smithing validates CERES's method but a second-trade attempt exposes a systemic issue — for example, food-safety regulation makes a Plan-C viability path for baking unworkable across all scales and organizational forms — that outcome is a **finding worth publishing**, not a project failure. The project should name that finding explicitly ("the CERES pipeline works for equipment-tractable trades; food-code trades require a regulatory-reform precondition outside the scope of equipment redesign"), update the working hypothesis accordingly, and continue. A finding that delimits the method's scope is a contribution. See Section 3 Smithing-as-template row for the related scope decision.

### 11.3 Failure

The project is a failure only if:

- Fewer than 15 entries are authored, or the authored entries do not span the realistic design space; OR
- Editorial review finds systemic citation or numeracy failures that invalidate the results; OR
- **Systematic editorial review failure:** 3 or more P1 findings per entry across more than half the catalog triggers a methodology-halt review before continuing. Continuing to produce entries without resolving a systemic methodological weakness is itself a failure mode; OR
- The research corpus is too thin to evaluate the hypothesis one way or the other.

Failure is a process outcome, not an evidence outcome. A rigorous null is success; a shoddy validation is failure.

### 11.4 Timeline

Indicative — not contractual, but committed to honestly for planning purposes:

| Phase | Duration target |
|---|---|
| Phase 1 Research (4–6 cultures × smithing) | 4–6 weeks |
| Phase 2 Catalog (15 forge entries, schema-complete) | 6–10 weeks |
| Phase 3 Economic lens formalization + Tier A sim | 3–4 weeks |
| Phase 4 Playbook + pitch first draft | 2–3 weeks |
| **Vertical slice total** | **~4 months of focused work, ~6 months part-time** |

### 11.5 Funder Archetype for the Pitch

The pitch narrative (Section 9) is authored for a specific archetype and pre-registers that archetype here:

- **Primary target:** civic-economic-development foundation or family office with an interest in rural / small-town economic resilience (program-related investment or grant, $250k–$2M range).
- **Secondary target:** municipal economic-development department considering a pilot (single-town, $50k–$500k budget line).
- **Not the target:** venture capital (CERES is not a scalable software company), retail consumer campaigns (too broad, too thin), or political campaigns (Section 13 non-goal).

If the evidence points to viability only under the cooperative or civic lens, the funder archetype shifts toward foundation / municipal and away from individual philanthropy.

### 11.6 World-Level Outcome

Beyond the artifacts, CERES is accountable for a contribution to the question: **"What would it actually take to restore meaningful local artisan production in a town of N residents?"** A project that materially advances public and funder understanding of that question — including by decisively ruling out the equipment-centered hypothesis — has produced value. A project that produces artifacts nobody reads and nobody can act on has not.

---

## 12. Reuse From Sister Projects

- **Chronicle (LUCIA)** — directory pattern for "many instances, consistent schema." Catalog entries mirror Chronicle's "peoples" — individual files, uniform structure. Reuse review/panel/scoring patterns.
- **RMM (FELICE)** — `corpus/canon` + `corpus/program` framework structure. Simulation-design discipline from `corpus/program/SIMULATIONS.md`. Predictions/validation mindset.
- **Reference (MAXIM)** — primary citation source for domain material (archaeology, ceramics, architecture-history, chemical-eng, agriculture, botany, etc.). Cite, do not duplicate.

---

## 13. Non-Goals

- **Not** real supplier BOMs, real vendor quotes, or due-diligence-grade procurement plans. Research-paper estimates only.
- **Not** an argument that industrial production is bad. The project's claim is about restoring *optionality* and *local capacity*, not displacing industrial supply.
- **Not** a political manifesto. Analytical rigor first, narrative framing second.
- **Not** a global-reach simulation. Target context is developed-economy settlements; other contexts can be added later.
- **Not** exhaustive historical coverage. 4–6 anchor cultures; more added only when the framework demands it.
