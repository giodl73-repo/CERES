# Adding a New Trade

Adding a trade to the CERES catalog is a five-phase process that mirrors the
main pipeline. Each phase has a plan document and defined completion criteria.
The three existing trades (smithing, baking, weaving) are the templates; follow
their structure exactly.

---

## Before starting

Check the spec (`specs/2026-04-18-ceres-design.md`) to confirm the trade is in
scope. The current scope covers **artisan-production trades** for which:

1. A meaningful historical form exists across multiple anchor cultures.
2. The binding constraint for decline is plausibly equipment-related or
   economics-related (not purely regulatory capture or demand collapse with no
   equipment-viable path).
3. The equipment can be realistically designed and costed at the three scales
   (village, town, small city) within the developed-economy context.

If the trade does not meet these criteria, the research phase will generate a
null result — which is valid, but should be anticipated before committing to the
full five-phase pipeline.

---

## Step 1 — Research (Plan pattern: Plans B, F, H)

### Create the research directory

```
research/trades/<new-trade>/
  REQUIREMENTS.md
  HISTORICAL-FORMS.md
  DECLINE-VERDICT.md
  SOURCES.md
```

And culture chapters:

```
research/cultures/medieval-northern-europe/<new-trade>.md
research/cultures/song-china/<new-trade>.md
research/cultures/tokugawa-japan/<new-trade>.md
research/cultures/american-frontier/<new-trade>.md
```

### Write REQUIREMENTS.md

This is the anchor document. It extracts functional requirements from the
historical forms across cultures:

```proof:tree kind=org
REQUIREMENTS.md sections
- §1 Overview: what this equipment does; scope within the trade
- §2 Functional requirements: temperature, throughput, precision, mobility, fuel
- §3 Operator requirements: skill floor, training path, concurrent operators
- §4 Space requirements: footprint, ceiling, ventilation, utility connections
- §5 Falsifier tests: which requirements, if not met, falsify the viability claim
- §6 Cross-cultural synthesis: where cultures agree and where they diverge
```

Each requirement must be cited. The falsifier tests are the most important
section — they define what a rigorous catalog entry must address.

### Write DECLINE-VERDICT.md

Diagnose why this trade declined. Name the binding constraint(s):

- Was it equipment economics? (capital cost above viable threshold)
- Was it labor regime? (the economics required unpaid family labor or guild labor
  conditions that no longer exist)
- Was it demand collapse? (the product became uncompetitive with industrial
  substitutes)
- Was it regulatory? (zoning, licensing, or environmental rules blocked the
  trade)
- Was it supply chain? (key inputs became unavailable or unaffordable)

A trade may have multiple binding constraints. Rank them. The catalog entries
must address the top constraint explicitly.

```proof:callout kind=note label="A null result is valid"
If the decline verdict shows that the binding constraint is not equipment
economics and cannot be addressed by equipment redesign, the analysis pivots
to document what would actually be required. Write the null result clearly.
A rigorous null result is a genuine contribution; silent scope expansion to
rescue a failing hypothesis is not.
```

### Submit for panel review

Run `/ceres-panel` on `REQUIREMENTS.md`. Address P1 findings before proceeding
to Phase 2.

---

## Step 2 — Trade schema (Part of catalog plan, e.g., Plan C, G, I)

Before authoring any entries, define the trade-specific schema extensions.

### Create catalog/<new-trade>/SCHEMA.md

The trade schema extends `catalog/SCHEMA.md` with fields specific to this
trade's physics, economics, and operations. Structure it as sections:

```proof:tree kind=org
catalog/<trade>/SCHEMA.md sections
- §1 Throughput: allowed throughput units, ranges by scale, E-3 cross-check guidance
- §2 Energy: allowed energy sources and consumption ranges
- §3 Operator skills: skill-level taxonomy (apprentice / journeyman / master)
- §4 Trade-specific required fields: fields that must be present in every entry
- §5 First-year failures reference: common failure modes and MTBF ranges
- §6 Design groups: categorize entries (e.g., Group A: micro-scale; Group B: shared community)
```

**Do not add fields that are already in `catalog/SCHEMA.md`.** Trade-specific
means specific to this trade's equipment and economics. If you find yourself
adding a field that would apply to all trades, propose it for `catalog/SCHEMA.md`
instead.

### Create catalog/<new-trade>/entries/.gitkeep

Placeholder until first entries are authored.

### Create catalog/<new-trade>/README.md

Short description of the trade, the catalog's scope within it, and how to read
the entries.

---

## Step 3 — Catalog entries (Plans C, G, I pattern)

### Target: 15 entries spanning the design-tradeoff space

Fifteen entries is the minimum for a meaningful catalog. It provides enough
variety to surface the tradeoff structure without stalling the pipeline.

Design the 15 entries before writing any of them. Lay out the coverage:

| # | Design group | Energy | Scale affinity | Ownership affinity |
|---|-------------|--------|---------------|-------------------|
| 001 | Micro / private | electric | village/town | market |
| 002 | Micro / private | gas | village/town | market |
| 003 | Community shared | electric | town | coop |
| ... | | | | |

Ensure:
- At least one entry in each energy source category the trade supports.
- At least one entry per scale (village-primary, town-primary, small-city-primary).
- At least one entry designed for each lens affinity (market, cooperative, civic).
- At least one entry derived from each anchor culture.
- At least one high-capital-cost design and one low-capital-cost design.

Gaps in the coverage grid are valid if the spec does not authorize that design
point — document the gap in `catalog/<trade>/README.md`.

### Author each entry

Follow the process in guide `04-authoring-entries`. The key steps:

1. Read `catalog/SCHEMA.md` and `catalog/<trade>/SCHEMA.md`.
2. Fill all YAML fields with inline derivation comments.
3. Apply `[CITATION-NEEDED: ...]` tags to every inferred value.
4. Address the trade's decline-verdict falsifiers explicitly.
5. Write all prose sections.
6. Run E-3 cross-checks manually.
7. Submit for panel review via `/ceres-panel`.

### After panel — advance to reviewed

Address panel P1 findings. Increment the version. If changes are substantive,
run R2 panel review. Advance `status: reviewed`.

---

## Step 4 — Simulation (Plan D pattern)

Once entries reach `reviewed`, run Tier A evaluation to populate the
`results:` blocks.

The Tier A simulation code is in `simulations/tier-a-comparator/`. The model
is trade-agnostic: it consumes `sim_params` fields and applies the lens formulas
from `corpus/program/ECONOMIC-LENSES.md`. No trade-specific code changes are
needed for standard entries.

### Before running

Verify:
- All 15 entries have complete `sim_params` blocks.
- `throughput_units_equiv_per_year` derivations are documented.
- `currency: USD` is declared in `economics:` (or the entry uses a currency
  listed in `corpus/program/CURRENCIES.md`).

### Run Tier A

Run all 15 entries through the Tier A comparator. The output for each entry is
15 × 9 = 135 cells. Results are written back to the `results:` block.

### Run VALIDATION.md sanity checks

`corpus/program/VALIDATION.md` defines cross-entry sanity rules. For example:
payback years for a `win` verdict must be ≤ 6.4; a `fail` in `cooperative` at
village scale should not coexist with break-even members < 10 (check the
floor-constraint logic).

### Submit Tier A output for review

Run `/ceres-panel` on the Tier A results documentation. E-3 cross-checks the
output before any result is cited in a playbook.

### Tier B (after ≥2 trades complete Tier A)

With smithing, baking, and weaving all at Tier A complete, the new trade adds
to the inter-trade system dynamics model. Identify trade dependencies:

- Does this trade's equipment require maintenance from another trade (e.g.,
  a kiln requires forge work for metal components)?
- Does this trade's output feed another trade (e.g., a tannery supplies
  leather to a cobbler)?

Document these dependencies in `simulations/tier-b-system-dynamics/` and
add the new trade to the system dynamics model.

---

## Step 5 — Playbook (Plan E pattern)

Write three playbook files — one per scale:

```
playbook/<new-trade>/village.md
playbook/<new-trade>/town.md
playbook/<new-trade>/small-city.md
```

Each file:
1. Identifies the top 3–5 winning designs from the Tier A results (catalog ids).
2. Explains why these designs win at this scale — cite specific cell verdicts.
3. Provides an implementation sketch (not a BOM): who operates it, how it
   integrates with existing local economy, what the first year looks like.
4. States the top risks and what would flip the verdict.

The playbook is directive (not analytical). It answers: "If a town wanted to
restore this trade, which design should they build, and how?"

```proof:callout kind=warning label="Playbook is evidence-based, not prescriptive"
The playbook identifies winners from the catalog. It does not recommend
designs that are not validated. If no design achieves a `win` at a given
scale, the playbook documents the marginal options and the open risks honestly.
A playbook file that overstates the evidence will fail panel review at P-6.
```

After authoring, run `/ceres-panel` and `/ceres-editorial` on each file.
Editorial clearance is required before citing playbook files in the pitch
narrative.

---

## Automation

A Python script in `scripts/new-trade.py` scaffolds the directory structure
for a new trade. It creates the research and catalog directory trees with
`.gitkeep` placeholders and README stubs.

```bash
python scripts/new-trade.py <trade-slug>
# e.g.: python scripts/new-trade.py ceramics
```

The script creates directories and stubs; it does not write content. You still
need to author `REQUIREMENTS.md`, `catalog/<trade>/SCHEMA.md`, and all entries
manually.

---

## Checklist

Before declaring a new trade complete:

```proof:bullets depth=2
Research phase
  REQUIREMENTS.md — written, cited, panel R1 cleared
  HISTORICAL-FORMS.md — four anchor cultures documented
  DECLINE-VERDICT.md — binding constraints identified and ranked
  SOURCES.md — bibliography complete
Catalog phase
  catalog/<trade>/SCHEMA.md — finalized
  15 entries — all at reviewed or validated
  Design space coverage documented in catalog/<trade>/README.md
Simulation phase
  Tier A — all 135 cells evaluated (15 entries × 9 cells)
  VALIDATION.md sanity checks — passing
  E-3 gate — cleared
  Tier B — trade added to system dynamics model
Playbook phase
  playbook/<trade>/village.md — authored, panel and editorial cleared
  playbook/<trade>/town.md — authored, panel and editorial cleared
  playbook/<trade>/small-city.md — authored, panel and editorial cleared
  TRACKER.md — updated with new trade status
```
