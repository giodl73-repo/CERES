---
trade: smithing
doc_type: schema-extension
extends: catalog/SCHEMA.md
version: "1.0"
schema_base_version: "1.1"
status: draft
---

Base schema: catalog/SCHEMA.md v1.1

# Smithing Schema Extension

This file extends the canonical catalog schema (`catalog/SCHEMA.md` v1.1) with
smithing-specific field definitions. It does not duplicate base-schema content; consult
`catalog/SCHEMA.md` for all required fields, validation rules, conditional triggers,
and prose-section requirements. This file is authoritative only for (a) the internal
structure of the `throughput:` block for smithing entries, (b) allowed values and
capability notes for `energy_source`, (c) the meaning of each `operator_skill_floor`
tier in a smithing context, (d) a reference list of common `first_year_failures`
items for smithing equipment, and (e) per-niche-group guidance for Wave 2 entry
authors. Any field not mentioned here is governed solely by `catalog/SCHEMA.md`.

---

## 1. Smithing `throughput` Block Structure

The `throughput:` block's internal structure is a smithing-specific extension per
`catalog/SCHEMA.md` §8. The base schema requires `max_active_hours_per_week` and at
minimum one rate measure; the fields below fulfil that requirement for smithing entries.

```yaml
throughput:
  units_per_hour:
    small_work: {integer}
    # Items in the 0.1–0.5 kg range requiring 1–4 heats each.
    # Examples: nails, hooks, simple rings, staples, horseshoe nails, small hinges,
    # shim stock. Throughput ceiling ~4–8 units/hr for a journeyman; apprentice lower.
    # REQUIREMENTS R-06: active forging is 4–8 hr/day; claimed rates above 10/hr
    # require explicit justification and experimental evidence.

    medium_work: {integer}
    # Items in the 0.5–3 kg range requiring multiple heats and some tooling.
    # Examples: horseshoes (fitting), brackets, tool-eye punching, chain links,
    # decorative S-hooks, simple knives, chisels. Throughput ceiling ~2–4 units/hr.

    large_work: {decimal}
    # Items above ~3 kg or requiring sustained multi-heat sequences.
    # Examples: gates, architectural panel sections, axe heads, anvil hardies,
    # laminated (pattern-welded) billets, farriery hind shoes for heavy draught stock.
    # Throughput ceiling ~0.3–1 units/hr; master-level work may be lower.
    # Entries claiming large_work > 1.0 must include explicit justification.

  max_active_hours_per_week: {integer}
  # Net active forging hours per week after startup, shutdown, and non-production
  # overhead. Per REQUIREMENTS R-06, realistic ceiling is 40–45 hr/wk for a
  # full-time single-operator shop; 20–25 hr/wk is more typical when customer
  # interaction, tool maintenance, and reheating time are accounted for.
  # The base schema requires this field; the smithing-specific note here calibrates it.

  product_mix:                    # optional but recommended for all non-trivial entries
    repair: {0-100}               # percentage of active hours on customer-owned work
    commodity: {0-100}            # standard-product output sold on open market
    specialty: {0-100}            # custom/bespoke work at premium price points
    artistic: {0-100}             # decorative/sculptural/collector work
    # Sum must equal 100. REQUIREMENTS R-22 requires product-mix scope be stated.
    # Per DECLINE-VERDICT: repair-dominant and specialty mixes are the historically
    # supported niches; entries with commodity > 40% must document competitive rationale.

  throughput_variance:
    worst_month_fraction_of_average: {decimal}
    # Fraction of the monthly average throughput in the worst calendar month.
    # Per REQUIREMENTS R-07: agricultural seasonality in all four anchor cultures
    # creates demand troughs. Typical range for repair-dominant shops: 0.40–0.60.
    # Gas/induction-electric shops with indoor customer base show less variance.

    best_month_fraction_of_average: {decimal}
    # Typical range for repair-dominant shops: 1.40–1.80 (pre-planting / post-harvest peak).

    seasonal: {string}
    # One-sentence description of the seasonal pattern.
    # Example: "Pre-planting (March–April) and post-harvest (Oct–Nov) peaks; summer trough."
    # For non-agricultural demand (farriery, architectural): describe actual pattern.
```

### `throughput` cross-checks (E-3)

The base schema E-3 rules apply. Smithing-specific guidance:

- `sim_params.throughput_units_equiv_per_year` must be computed from a weighted average
  of `small_work`, `medium_work`, and `large_work` rates using `product_mix` percentages,
  then multiplied by derated active hours. State the weighting explicitly in Key Assumptions.
- An entry with `operator_skill_floor: apprentice` must have `small_work` and `medium_work`
  values lower than the journeyman ceiling rates above; `large_work` should be 0 or flagged.
- `throughput_variance.worst_month_fraction_of_average` must be consistent with
  `sim_params.downtime_fraction`; seasonal trough weeks count toward effective downtime.

---

## 2. Smithing-Specific `energy_source` Enumeration

The base schema permits trade-specific `energy_source` values (see `catalog/SCHEMA.md` §8).
The following values are the allowed set for smithing entries. Each value carries
capability implications per REQUIREMENTS R-08 (fuel regime options).

| Value | Temp. ceiling | Forge-weld capable | Emissions posture | Regulatory notes | Typical consumption/active hr |
|---|---|---|---|---|---|
| `coal` | ~1300°C with forced air | Yes | Particulate + SOx + CO; venting mandatory | Light-industrial or rural zoning typical; urban core restrictions common; sulfur-management required (REQUIREMENTS §4) | 6–10 kg/hr coal |
| `coke` | ~1300°C with forced air | Yes | Lower SOx than raw coal; particulate still present | Similar to coal; coke supply chain is a dependency | 5–8 kg/hr coke |
| `charcoal` | ~1300°C with forced air | Yes | Particulate + CO; lower SOx than coal | Supply-chain dependency (coppiced wood or purchased charcoal); urban restrictions on open-fire forges | 4–7 kg/hr charcoal |
| `propane` | ~1260°C (standard forge burner) | Marginal; requires high-capacity burner | CO + combustion products; no particulate or SOx; venting required | LP storage tank regulatory requirements; simpler permit path than coal in most jurisdictions | 1–2 kg/hr propane (≈1.4–2.8 L/hr) [CITATION-NEEDED: propane forge consumption, modern experimental measurement; see REQUIREMENTS R-08 placeholder] |
| `natural-gas` | ~1260°C | Marginal; same as propane | CO + combustion products; lower carbon intensity than propane | Gas line infrastructure required; permit for commercial combustion appliance; simpler than coal | Equivalent BTU to propane; roughly 1.0–1.8 m³/hr |
| `induction-electric` | Limited by coil geometry; typically 900–1100°C practical ceiling for standard induction forges; higher with purpose-built units | No — induction does not produce forge-weld temperatures in standard configurations | Near-zero combustion emissions at point of use; upstream grid emissions apply | Electrical service upgrade often required (50–100A, 240V typical); no combustion permit; cleanest regulatory path | 6–15 kWh/hr depending on unit rating |
| `hybrid-coal-propane` | ~1300°C (coal mode); ~1260°C (propane mode) | Yes (coal mode); marginal (propane mode) | Switchable; coal mode carries full coal emissions profile | Requires permits for both fuel types; storage for both | Coal or propane per mode |
| `hybrid-induction-gas` | ~1100°C (induction); ~1260°C (gas mode) | No (induction); marginal (gas mode) | Gas mode: CO + combustion; induction mode: near-zero on-site | Dual permit path; induction for precision; gas for bulk heating | Induction or gas per mode |

**Notes on `induction-electric` capability.** Standard commercial induction forges (e.g.,
Anvilfire-style units, Induction Systems designs) typically top out at ~1050–1100°C in
practice under sustained load for a billet of medium cross-section. Forge-welding
requires ~1100–1300°C and precise timing; this is achievable with purpose-built high-power
induction coils but is not a standard capability of compact entry-level units. Catalog
entries claiming forge-weld capability with induction-electric must specify the unit
configuration. See REQUIREMENTS R-02.

**Notes on `charcoal` sustainability.** Per REQUIREMENTS §4 (DIV-01 and forest-pressure
finding): charcoal must not be presented as inherently sustainable without documenting
the specific supply context. Entries using `charcoal` must state the supply chain in
`regulatory_notes` or Key Assumptions.

---

## 3. Smithing-Specific `operator_skill_floor` Definitions

The base schema defines `operator_skill_floor` as "the minimum competence at which a
real operator can run the equipment safely and productively without direct supervision."
The following values apply to smithing entries per REQUIREMENTS §6 (R-17).

| Value | Smithing meaning | Capability boundary | Mapped requirement |
|---|---|---|---|
| `apprentice` | Entry-level operator with basic fire management, stock preparation, and simple bending/shaping under supervision. Has not yet developed independent heat-judgment. | Cannot perform forge welding solo (REQUIREMENTS §6: forge welding requires temperature *judgment*, not just temperature achievement). Cannot make independent heat-treatment decisions (quench timing, tempering color reading). Cannot perform precision edge-tool work. Can handle small_work with oversight; medium_work rates are depressed and quality variable. | REQUIREMENTS R-17; see also R-13 (anvil base — apprentice may not recognize inadequate base mass effect) |
| `journeyman` | Fully independent operator. Has internalized heat judgment. Can run any standard forge operation without supervision. | Can perform forge welding in standard configurations. Can execute basic heat treatment (normalize, anneal, harden, temper) with formed judgment. Can handle most repair work including horseshoe fitting, tool repair, hardware fabrication. Can supervise an apprentice safely. Cannot reliably produce master-tier work (pattern welding, differential harden to tight tolerances, complex bespoke fabrication). | REQUIREMENTS R-17, R-14 (formed heat-treatment judgment required for quench decisions) |
| `master` | Senior practitioner with full technical range and problem-solving capability under novel constraints. | Pattern welding (lamination and manipulation of dissimilar alloys). Differential hardening (hamon formation, clay-coat techniques). Bladesmithing to professional fit-and-finish tolerances. Complex architectural ironwork requiring structural problem-solving. Customer-brief interpretation without prescribed method. Can train and assess apprentice and journeyman operators. | REQUIREMENTS R-15 (precision edge tools); R-17 (bespoke fabrication category) |

**Mapping to REQUIREMENTS R-13 through R-15:**

- R-13 (anvil base mass) maps to all three tiers: apprentice operators are unlikely to
  recognize the performance degradation from an undersized base; journeyman and master
  operators should be able to diagnose and address it.
- R-14 (quench infrastructure) maps primarily to `journeyman` and `master`: heat
  treatment requiring a quench is not appropriate for `apprentice` solo operation.
- R-15 (fuel and stock storage) is a facility requirement, not operator-tier-dependent;
  all tiers must follow storage separation rules per OSHA 29 CFR 1910.252(c).

**Note on succession risk.** An entry with `operator_skill_floor: master` and
`apprentice_friendly: false` must name succession risk explicitly in Known Risks
(base schema §5, Principle 9). Master-floor entries with no apprentice path represent
the shortest viable operating horizon.

---

## 4. Smithing `first_year_failures` Reference List

The base schema requires 2–4 `first_year_failures` items per entry when `operations_reality`
is required. The following reference list reflects common smithing-equipment failure
modes in the first operating year; authors select 2–4 items appropriate to the
specific energy source and equipment configuration of their entry.

This list is descriptive and not exhaustive. Numbers are illustrative starting points;
entries must carry a citation or explicit `[CITATION-NEEDED]` per E-1 rules.

| Component | Applicable forge types | Typical hours-to-failure | Notes |
|---|---|---|---|
| Primary coil / heating element | `induction-electric`, `hybrid-induction-gas` | 1,500–2,500 hr | Coil failure is the primary induction-forge downtime event; replacement is specialist-level; lead time 14–30 days for non-stocked coils |
| Refractory lining (partial spalling) | `coal`, `charcoal`, `coke`, `hybrid-coal-propane` | 1,800–3,000 hr | Partial re-lining is operator-serviceable with castable refractory; full replacement is journeyman or specialist; lead time 3–7 days for materials |
| Bellows mechanism (leather, valve, or treadle failure) | Traditional `charcoal`, `coal` (hand or foot bellows) | 800–2,000 hr | Leather degradation with heat cycling; valve replacement is operator-serviceable; full bellows replacement is specialist or custom fabrication |
| Anvil base settling / crack | All forge types (universal) | 500–2,000 hr (settling); crack timing variable | Wood-stump bases settle or split; masonry bases crack from thermal cycling; steel stands may develop weld fatigue. Operator-serviceable for wood-stump replacement; journeyman for masonry |
| Ventilation blower / hood (motor or ductwork failure) | All forge types requiring `mechanical-extraction-required` or `dedicated-exhaust-system` | 1,500–3,000 hr | Blower motor bearing failure is the most common mode; replacement is operator- or journeyman-level; hood ductwork seals degrade from heat and soot |
| Propane regulator (diaphragm wear, freeze-up, ice blockage) | `propane`, `natural-gas`, `hybrid-coal-propane`, `hybrid-induction-gas` | 600–2,000 hr (wear); seasonal (freeze-up) | Regulator replacement is operator-serviceable; winter freeze-up is operational rather than mechanical, but counts as interruption event |
| Hammer / power-hammer bearings (if equipped) | Entries with power hammer or mechanical striker | 1,000–3,000 hr | Bearing failure in power hammers is journeyman-serviceable for standard replaceable types; custom-built hammers may require specialist; lead time varies widely |

Authors selecting items from this list should populate all five sub-fields required
by the base schema: `item`, `estimated_hours_to_failure`, `replacement_cost`,
`replacement_lead_time_days`, and `serviceable_by`.

---

## 5. Per-Niche-Group Guidance for Wave 2 Authors

The 15-entry manifest (Plan C) distributes entries across four niche groups. The
following notes identify which schema fields tend to be most load-bearing for
each group. "Load-bearing" means: (a) incorrect or missing values most likely
produce a failed or misleading E-3 cross-check, or (b) the field is the primary
evidence for the lens-fit claim.

### Group A — Repair-Focused (entries forge-005, 007, 012, 013, 002, 014)

`product_mix.repair` is the defining field for this group; it should dominate (50–80%
typical) and must be consistent with `lens_fit.market: good` or `marginal` via a
`market_price_per_unit` that prices repair labor (not commodity output) as the unit.
`throughput_variance.seasonal` and `worst_month_fraction_of_average` carry significant
weight: repair demand is bursty and agricultural-seasonal per REQUIREMENTS R-07.
`operator_skill_floor: journeyman` is the historically supported baseline for repair-
dominant entries; entries dropping to `apprentice` must document which repair operations
are excluded. `apprentice_path` matters more for long-term viability than for short-term
economics; repair entries with `apprentice_friendly: false` are high succession-risk.

### Group B — Specialty / Custom / Artistic (entries forge-006, 010, 008)

`product_mix.specialty` or `product_mix.artistic` dominates; `operator_skill_floor:
master` is expected for bladesmithing and architectural ironwork. The critical field
pair is `market_price_per_unit` + `economics.industrial_baseline_price`: the
specialty premium over industrial baseline is the core economic claim, and it must
be cited (E-1-R4). `throughput_variance` tends to be high (custom work is project-
based; revenue is lumpy). `sim_params.throughput_units_equiv_per_year` must use a
unit equivalent that accounts for the mix of small/medium/large work; authors should
state the weighting explicitly. `energy_source: induction-electric` is common in
this group (heat-treatment precision); see Section 2 notes on forge-weld limitations.

### Group C — Shared / Civic / Cooperative (entries forge-003, 004, 011, 015)

`lens_context.cooperative` or `lens_context.civic` (or both) are the primary load-
bearing blocks for this group. All Ostrom-principle sub-fields must be substantive,
not boilerplate. `lens_context.civic.benchmark_comparison` and `staffing_model` carry
the political-viability argument; a civic entry that does not name a benchmark is
unverifiable per E-2-R6a. `product_mix` in this group often has high `repair` and
`commodity` at subsidized or below-market pricing; `market_price_per_unit` may be
absent or low (requiring `lens_fit.market: poor` or `marginal`). `operators_concurrent`
reflects a supervised multi-member model rather than single-operator production;
`apprentice_path` and `civic_externalities` together carry the succession and
public-goods arguments that justify the lens-fit claim.

### Group D — Training / Apprentice / Cooperative-Training (entries forge-009, 001)

`apprentice_path` is the defining block; all three sub-fields (`training_stages`,
`time_to_independent_operation`, `succession_note`) must be substantive and specify
which cultural apprenticeship model is being followed (per REQUIREMENTS R-19). For
the training-forge subtype, `operators_concurrent` typically reflects a teaching
configuration (master + multiple apprentices) rather than production staffing.
`throughput_units_equiv_per_year` will be lower than a production-equivalent entry
at the same scale; the delta is the cost of training and must be made explicit in
Key Assumptions. Entries in this group often have `lens_fit.market: poor`; the
civic or cooperative lens must carry the viability case. For forge-001 (entry-level
hobbyist), this is inverted: the training function is incidental; the test is whether
minimal capital entry is economically viable at all.

---

## 6. Sources

The following documents are the primary sources for the smithing-specific parameter
ranges and definitions in this extension:

- `research/trades/smithing/REQUIREMENTS.md` — functional requirements R-01 through R-24;
  primary authority for temperature envelopes (R-01 through R-05), throughput ranges
  (R-06, R-07), fuel regime options (R-08, R-09), footprint (R-10), operator skill
  definitions (R-13 through R-15, R-17 through R-19), and product-category matrix (R-22, R-23).
- `research/trades/smithing/HISTORICAL-FORMS.md` — physical forge characteristics by
  culture (Table 1); bellows mechanisms, hearth forms, and fuel configurations that inform
  `throughput.units_per_hour` ceiling estimates and `throughput_variance.seasonal` patterns.
- `catalog/SCHEMA.md` v1.1 — base schema; all fields, validation rules, and conditional
  triggers not covered by this extension are governed there.

---

*Schema extension iteration log:*

- 2026-04-18: v1.0 — initial creation per Plan C Task 2.
