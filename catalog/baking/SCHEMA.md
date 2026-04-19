---
trade: baking
doc_type: schema-extension
extends: catalog/SCHEMA.md
version: "1.0"
schema_base_version: "1.1"
status: draft
---

Base schema: catalog/SCHEMA.md v1.1

# Baking Schema Extension

This file extends the canonical catalog schema (`catalog/SCHEMA.md` v1.1) with
baking-specific field definitions. It does not duplicate base-schema content; consult
`catalog/SCHEMA.md` for all required fields, validation rules, conditional triggers,
and prose-section requirements. This file is authoritative only for (a) the internal
structure of the `throughput:` block for baking entries, (b) allowed values and
capability notes for `energy_source`, (c) the meaning of each `operator_skill_floor`
tier in a baking context, (d) the required `flour_source_declaration` field and its
allowed values, (e) a reference list of common `first_year_failures` items for baking
equipment, and (f) per-niche-group guidance for Wave 2 entry authors. Any field not
mentioned here is governed solely by `catalog/SCHEMA.md`.

---

## 1. Baking `throughput` Block Structure

The `throughput:` block's internal structure is a baking-specific extension per
`catalog/SCHEMA.md` §8. The base schema requires `max_active_hours_per_week` and at
minimum one rate measure; the fields below fulfil that requirement for baking entries.

**Unit definition note:** "loaves" is not a uniform unit. Authors must state the
specific product unit used (e.g., "800g sourdough boule equivalent" or "baguette
pair") in the Key Assumptions prose section. `sim_params.throughput_units_equiv_per_year`
must use the same stated unit.

```yaml
throughput:
  loaves_per_day: {integer}
  # Net production output per full operating day.
  # Includes all product categories converted to the stated loaf-equivalent unit.
  # Authors must define the unit in Key Assumptions.
  # Typical ranges: home/micro (10-40), village artisan (30-100),
  # town artisan (80-250), wholesale/deck (150-600).
  # Per REQUIREMENTS: claimed rates above 400 loaves/day for a single-operator
  # shop require explicit justification (oven capacity, bake time, labor hours).

  batches_per_day: {integer}
  # Number of oven loads per operating day.
  # One batch = one full oven load. For deck ovens, one batch per deck per load.
  # Typical: 2-4 batches/day for artisan micro-bakery; 6-12 for wholesale operation.

  batch_size_loaves: {integer}
  # Number of loaf-equivalents per batch.
  # Dependent on oven deck area and loaf spacing.
  # [CITATION-NEEDED: typical deck-oven capacity per m² of deck area]

  max_active_hours_per_week: {integer}
  # Net active production hours per week after startup, mixing, proofing overhead,
  # and cleanup. Realistic ceiling for a full-time single-operator artisan bakery:
  # 35-45 hr/wk. Wholesale operations with multiple operators may exceed 60 hr/wk.

  product_mix:                    # optional but recommended for all non-trivial entries
    bread: {0-100}                # percentage of active hours on bread (sourdough, yeasted loaves)
    confection: {0-100}           # pastry, laminated doughs, sweet enriched products
    specialty: {0-100}            # custom orders, cultural specialty items
    catering: {0-100}             # event catering, wholesale trays, institutional supply
    # Sum must equal 100. Per DECLINE-VERDICT: artisan-bread-dominant and
    # specialty mixes are the historically supported niches; entries with
    # high industrial-commodity mix must document competitive rationale.

  throughput_variance:
    worst_month_fraction_of_average: {decimal}
    # Fraction of the monthly average throughput in the worst calendar month.
    # Baking demand shows moderate seasonality: summer (July-August) slowdown
    # for artisan retail; post-holiday (January) slowdown for confection.
    # Typical range for artisan bread: 0.55-0.75; confection: 0.35-0.55.

    best_month_fraction_of_average: {decimal}
    # Pre-holiday (November-December) peaks dominate for confection and custom cake.
    # Typical range: 1.30-1.80 for confection; 1.20-1.40 for artisan bread.

    seasonal: {string}
    # One-sentence description of the seasonal pattern.
    # Example: "Holiday peak (Nov-Dec) for confection; moderate summer trough for bread."
```

### `throughput` cross-checks (E-3)

The base schema E-3 rules apply. Baking-specific guidance:

- `sim_params.throughput_units_equiv_per_year` must be computed from `loaves_per_day`
  × `batches_per_day` logic, derated by `max_active_hours_per_week` and
  `throughput_variance`. State the annual operating days assumption explicitly
  (typically 260-310 days/year for a full-time artisan bakery).
- An entry with `operator_skill_floor: apprentice-baker` should have `loaves_per_day`
  values constrained to simpler bread and basic confection; laminated doughs, complex
  pastry, and custom-cake require at minimum `journeyman-baker`.
- `throughput_variance.worst_month_fraction_of_average` must be consistent with
  `sim_params.downtime_fraction`; seasonal trough weeks count toward effective downtime.

---

## 2. Baking-Specific `energy_source` Enumeration

The base schema permits trade-specific `energy_source` values (see `catalog/SCHEMA.md` §8).
The following values are the allowed set for baking entries. Each value carries
capability implications per REQUIREMENTS (baking temperature and steam requirements).

| Value | Temp. ceiling | Steam-injection capable | Emissions posture | Regulatory notes | Typical consumption/batch |
|---|---|---|---|---|---|
| `wood-fired-deck` | ~300-450°C deck surface (declining from peak during bake) | No (steam from misting or Dutch-oven equivalent) | Particulate + CO; air-quality permit typical for commercial wood burning | Rural/farm zoning typical; urban restrictions common; fuel-storage and smoke-management required | 15-40 kg/batch wood [CITATION-NEEDED] |
| `electric-deck` | ~230-290°C (thermostat-controlled) | Requires separate steam injector or water-tray add-on | Near-zero on-site combustion emissions | Cleanest permit path; requires 30-60A dedicated circuit per deck unit | 3-8 kWh/batch depending on deck size and load [CITATION-NEEDED] |
| `convection-electric` | ~160-230°C (fan-circulated; lower effective temp than deck for bread crust) | Via combi attachment or separate steam tray | Near-zero on-site | Standard single-phase or three-phase; van-mount generator feasible for mobile | 2-5 kWh/batch [CITATION-NEEDED] |
| `deck-gas` | ~230-290°C (gas-fired deck; more consistent mass heat than electric) | Requires steam-injection system | CO + combustion products; no particulate; venting required | Gas line or propane supply; commercial-combustion appliance permit; simpler than solid-fuel | 0.5-1.5 m³ gas/batch [CITATION-NEEDED] |
| `combi-steam` | ~100-250°C (combi mode); full steam mode for proofing/steaming | Yes — integral steam-injection system | Near-zero on-site (electric combi) or CO if gas-fired combi | Electrical service upgrade for electric combi; gas line for gas combi; health-department approval for steam systems | 4-10 kWh/batch (electric combi) [CITATION-NEEDED] |
| `hybrid-wood-electric` | ~300-400°C peak (wood) + ~230-260°C sustained (electric backup) | Misting for wood mode; steam injector for electric mode | Wood mode: particulate + CO; electric mode: near-zero | Dual permit path: solid-fuel + electrical; most complex regulatory posture | Wood or electric per mode |

**Notes on `wood-fired-deck` capability.** A properly fired masonry deck oven retains
heat across multiple bakes and produces the characteristic ear and crust development
of traditional sourdough. However, thermal management is operator-skill-dependent:
achieving consistent deck temperature requires experienced firing judgment that cannot
be delegated to apprentice-baker floor operators reliably. Entries claiming
`wood-fired-deck` with `operator_skill_floor: apprentice-baker` must explain the
temperature management protocol. See REQUIREMENTS (wood-firing judgment requirement).

**Notes on `combi-steam` for laminated doughs.** French-style laminated pastry
(croissant, pain au chocolat) requires precise steam injection in the first minutes
of the bake to gelatinize the surface starch before the butter layers melt. A
`combi-steam` oven is the standard tool for this. Entries claiming Viennoiserie
output without `combi-steam` energy source must explain the steam management alternative.

---

## 3. Baking-Specific `operator_skill_floor` Definitions

The base schema defines `operator_skill_floor` as "the minimum competence at which a
real operator can run the equipment safely and productively without direct supervision."
The following values apply to baking entries per REQUIREMENTS (operator skill R-series).

| Value | Baking meaning | Capability boundary | Product scope |
|---|---|---|---|
| `apprentice-baker` | Entry-level operator with basic dough mixing, shaping, and bake-monitoring capability under supervision. Has not internalized fermentation judgment or oven-heat management independently. | Cannot manage sourdough fermentation schedule without supervision. Cannot execute laminated doughs, complex pastry, or custom sugar work. Cannot troubleshoot oven temperature variation independently. Can handle yeasted breads, simple rolls, and basic cookies with guidance. | Simple yeasted breads, basic rolls, cookies; NOT sourdough management, laminated doughs, or custom confection. |
| `journeyman-baker` | Independently capable baker with formed fermentation judgment. Can manage full sourdough cycle, run a deck oven without supervision, execute standard enriched doughs (brioche, challah), and produce consistent commercial-scale output. | Can manage sourdough starter maintenance, bulk fermentation timing, and proofing schedules without oversight. Can execute standard pastry (tarts, simple laminated). Cannot reliably execute high-complexity sugar work, multi-tier cake assembly, or competition-level Viennoiserie. Can supervise an apprentice. | Full sourdough program, most yeasted breads, standard pastry; NOT complex lamination, custom sugar art, or competition-level confection. |
| `pastry-chef-master` | Senior practitioner with full technical range across bread, pastry, and confection. Can execute complex laminated doughs, multi-technique sugar work, custom cake design, and cultural specialty confection with professional-grade consistency. | Full laminated dough program (croissant, Danish, puff). Precision sugar and chocolate work. Multi-tier custom cake assembly and structural engineering. Cultural specialty confection requiring tradition-specific knowledge (wagashi, ethnic specialty). Can train and assess journeyman and apprentice operators. | All baking and confection categories; required for bake-006 (Viennoiserie), bake-007 (Wagashi), bake-009 (Custom Cake). |

**Note on succession risk.** An entry with `operator_skill_floor: pastry-chef-master`
and `apprentice_friendly: false` must name succession risk explicitly in Known Risks.
Master-floor entries with no apprentice path represent the shortest viable operating
horizon.

---

## 4. Required Field: `flour_source_declaration`

**This field is required for all baking entries** per DECLINE-VERDICT mill-dependency
falsifier. It must be present in every entry's frontmatter and must be consistent with
the Key Assumptions prose section.

```yaml
flour_source_declaration: industrial-flour-purchased | local-mill-partnership | integrated-milling | on-site-milling
```

| Value | Meaning | Supply-chain risk | Capital implication |
|---|---|---|---|
| `industrial-flour-purchased` | Baker purchases commodity or specialty flour from industrial mill or distributor. No mill infrastructure or direct farm relationship. | Supply-chain disruption; price volatility; no premium sourcing narrative. | Lowest (no mill capital). |
| `local-mill-partnership` | Baker sources flour from a named local or regional mill with a direct relationship. Mill is independent; baker does not own or operate milling equipment. | Mill-partner dependency; single-source risk unless multiple mills named. | Low (contract or relationship management cost only). |
| `integrated-milling` | Baker has a formal operational integration with a mill: may be the same cooperative, same farm, or a formal revenue-sharing arrangement. The mill is not owned by the bakery but operates in coordination. | Coordination complexity; requires mill-side capacity commitment. | Moderate (integration and coordination overhead; may include shared infrastructure). |
| `on-site-milling` | Baker owns and operates milling equipment on-site or at a directly attached facility. Flour is produced from grain at point of baking. | Grain sourcing (upstream), mill maintenance (equipment), and milling expertise (skill). Highest single-operator dependency. | Highest (stone mill or hammer mill capital, grain storage, milling skill requirement). |

Authors must explain the specific flour sourcing in Key Assumptions: name the flour
type(s), specify whether specialty grains are involved, and assess supply continuity.

---

## 5. Baking `first_year_failures` Reference List

The base schema requires 2-4 `first_year_failures` items per entry. The following
reference list reflects common baking-equipment failure modes in the first operating
year; authors select 2-4 items appropriate to the specific energy source and equipment
of their entry.

This list is descriptive and not exhaustive. Numbers are illustrative starting points;
entries must carry a citation or explicit `[CITATION-NEEDED]` per E-1 rules.

| Component | Applicable oven types | Typical hours-to-failure | Notes |
|---|---|---|---|
| Deck heating element (electric) | `electric-deck` | 1,500-3,000 hr | Electric deck heating elements degrade under repeated thermal cycling; replacement is journeyman- or specialist-level; lead time 7-21 days for non-stocked elements [CITATION-NEEDED] |
| Oven thermostat / controller | `electric-deck`, `convection-electric`, `combi-steam` | 2,000-4,000 hr | Thermostat drift is the most common non-structural failure in deck ovens; calibration is operator-level; replacement is journeyman or specialist; lead time 5-14 days |
| Proofer heating element or thermostat | All entries with dedicated proofing cabinet | 1,000-2,500 hr | Proofer elements fail similarly to oven elements; shorter cycle time may accelerate degradation; replacement is operator- or journeyman-level |
| Deck stones cracking | `electric-deck`, `deck-gas`, `wood-fired-deck` (stone surface variant) | 800-2,500 hr (thermal shock dependent) | Deck stones crack from thermal shock (water spills, cold dough contact); replacement is operator-level for modular stones; full deck resurfacing is specialist; lead time 3-10 days for stones [CITATION-NEEDED] |
| Oven door seal / gasket | `electric-deck`, `convection-electric`, `combi-steam`, `deck-gas` | 1,500-3,000 hr | Door gasket degradation causes heat loss and inconsistent bake; replacement is operator-serviceable for standard commercial ovens; lead time 3-7 days |
| Steam injector nozzle or valve | `combi-steam`, `electric-deck` (with steam injector) | 1,200-2,500 hr | Limescale buildup in hard-water areas accelerates nozzle failure; descaling is operator-level; nozzle replacement is journeyman-level; lead time 3-14 days |
| Wood-fired dome refractory (spalling or crack) | `wood-fired-deck`, `hybrid-wood-electric` | 2,000-5,000 hr | Partial spalling is normal; operator-serviceable with high-temperature refractory mortar; full dome repair is specialist; lead time depends on mason availability |
| Convection fan motor | `convection-electric`, `combi-steam` | 2,000-4,000 hr | Fan bearing failure is the most common convection-oven failure; replacement is journeyman-level; lead time 5-14 days |

Authors selecting items from this list must populate all five sub-fields required
by the base schema: `item`, `estimated_hours_to_failure`, `replacement_cost`,
`replacement_lead_time_days`, and `serviceable_by`.

---

## 6. Per-Niche-Group Guidance for Wave 2 Authors

The 15-entry manifest (Plan G) distributes entries across four niche groups. The
following notes identify which schema fields tend to be most load-bearing for
each group. "Load-bearing" means: (a) incorrect or missing values most likely
produce a failed or misleading E-3 cross-check, or (b) the field is the primary
evidence for the lens-fit claim.

### Group A — Artisan Bread / Premium (bake-001 through bake-005)

`flour_source_declaration` is the defining falsifier for this group. Entries claiming
`local-mill-partnership` or `integrated-milling` must document the supply relationship
in Key Assumptions; entries claiming `industrial-flour-purchased` must explain why
premium positioning is defensible without grain-sourcing differentiation.

`product_mix.bread` dominates (70-90% typical). `throughput_variance.seasonal` matters:
summer slowdowns and holiday peaks shape annual revenue. `loaves_per_day` is the primary
throughput signal; authors must state the unit clearly and be consistent with
`sim_params.throughput_units_equiv_per_year`.

For bake-005 (Mobile Pop-up), `regulatory_notes.zoning` is critical: mobile food
service permitting varies widely by jurisdiction and is a primary early-failure risk.

### Group B — Specialty Confection / Pastry (bake-006 through bake-009)

`operator_skill_floor: pastry-chef-master` is required for bake-006, bake-007, and
bake-009; `journeyman-baker` minimum for bake-008. The critical field pair is
`market_price_per_unit` + `economics.industrial_baseline_price`: the specialty premium
over supermarket-confection baseline is the core economic claim, and it must be cited
or flagged `[CITATION-NEEDED]`.

`throughput_variance` is high for event-driven entries (bake-009): custom cakes are
project-based; revenue is lumpy. `sim_params.throughput_units_equiv_per_year` must
use a unit that accounts for the diversity of confection products; authors should
state the weighting explicitly.

`product_mix.confection` or `product_mix.specialty` dominates. For bake-007 (Wagashi),
the civic-lens claim must be substantive: cultural-preservation externalities must be
named specifically, not described generically.

### Group C — Community / Civic / Cooperative (bake-010 through bake-013)

`lens_context.cooperative` or `lens_context.civic` (or both) are the primary
load-bearing blocks for this group. All Ostrom-principle sub-fields must be substantive
for bake-012 (Community Kitchen Collective); a coop entry without substantive
scheduling/booking rules is unverifiable per E-2.

For bake-010 (Civic Neighborhood Bakery): `lens_context.civic.benchmark_comparison`
must name a comparable food-access program (food bank, community meal program) and
provide a cost-per-meal or cost-per-household comparison. `staffing_model` must cite
public-sector or nonprofit wages from SCALES.md or a named source.

For bake-011 (Apprentice Training Bakery): `apprentice_path` is the defining block;
`training_stages`, `time_to_independent_operation`, and `succession_note` must be
specific to the culinary program referenced.

For bake-013 (Farm-to-Table Integrated Bakery): `flour_source_declaration: integrated-milling`
is the entry's core claim; Key Assumptions must describe the farm-mill integration
mechanism (ownership, partnership terms, grain supply quantities).

### Group D — Minimum-viable / Stress-test (bake-014, bake-015)

`economics.capital_cost` is the defining constraint for both entries. bake-014 must
document the cottage-food-law regulatory environment explicitly: which jurisdictions
permit home-based commercial baking, and what the licensing threshold is.

bake-015 (Wood-fired Community Oven) should have `lens_fit.market: poor` (shared-access
model is not market-primary) and `lens_fit.civic: good` + `lens_fit.coop: good`. The
civic and coop claims must reference the specific medieval or early-modern communal
oven model from Plan B HISTORICAL-FORMS.md chapter passage. `throughput` will be
low by design; authors should not attempt to optimize bake-015 throughput — its role
is to test the civic/coop viability of the traditional shared-oven model.

---

## 7. Sources

The following documents are the primary sources for the baking-specific parameter
ranges and definitions in this extension:

- `research/trades/baking/REQUIREMENTS.md` — functional requirements; primary authority
  for temperature envelopes, throughput ranges, fuel regime options, footprint,
  operator skill definitions, and product-category matrix.
- `research/trades/baking/HISTORICAL-FORMS.md` — physical oven characteristics by
  culture; fuel configurations that inform `throughput.loaves_per_day` ceiling estimates
  and `throughput_variance.seasonal` patterns.
- `research/trades/baking/DECLINE-VERDICT.md` — niche targeting; mill-dependency
  falsifier; binding guidance on `flour_source_declaration` requirement.
- `catalog/SCHEMA.md` v1.1 — base schema; all fields, validation rules, and conditional
  triggers not covered by this extension are governed there.

---

*Schema extension iteration log:*

- 2026-04-19: v1.0 — initial creation per Plan G Wave 0 (Task 2).
