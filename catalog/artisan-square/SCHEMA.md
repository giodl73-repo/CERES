---
trade: artisan-square
doc_type: schema-extension
extends: catalog/SCHEMA.md
version: "1.0"
schema_base_version: "1.1"
status: draft
---

Base schema: catalog/SCHEMA.md v1.1

# Artisan Square Schema Extension

This file extends the canonical catalog schema (`catalog/SCHEMA.md` v1.1) with
artisan-square-specific field definitions. It does not duplicate base-schema content;
consult `catalog/SCHEMA.md` for all required fields, validation rules, conditional
triggers, and prose-section requirements. This file is authoritative only for (a) the
internal structure of the `throughput:` block for artisan-square entries, (b) the
`trade_specific:` fields unique to artisan-square facility configurations, (c) the
meaning of each `operator_skill_floor` tier in a building-operator context, (d) a
reference list of common `first_year_failures` items for facility operations, and (e)
per-configuration-type guidance for entry authors. Any field not mentioned here is
governed solely by `catalog/SCHEMA.md`.

---

## 1. Purpose

This schema extension covers the artisan-square trade. An artisan-square catalog
**entry** is a facility configuration — a specific building design operated as a
multi-trade artisan production building — not an artisan practitioner. The "operator"
is a building developer/operator; the "equipment" is the building itself. Standard
CERES economic fields are reinterpreted for this context: `throughput` measures
studio-months rented rather than production units per hour; `market_price_per_unit`
is the average monthly rent per studio (the operator's unit of revenue); and the
operator identity shifts from a craft practitioner to a real estate and infrastructure
company serving artisan tenants. The Tier A simulation evaluates whether operating an
Artisan Square facility pencils out under the same market/cooperative/civic lenses used
for a forge or bakery, applying the same payback and viability formulas with the
reinterpreted fields defined below.

---

## 2. Artisan Square `trade_specific` Block Structure

Fields under `trade_specific:` capture artisan-square-specific characteristics that
have no analogue in the base schema and must not shadow any base-schema field name.

```yaml
trade_specific:

  # ── FACILITY COMPOSITION ──────────────────────────────────────────────────

  facility_type: Type-A-only | Type-B-only | combined-campus | small-town-lite
  # Configuration class for the facility.
  #   Type-A-only      = heavy-trade studios only (forge/metalwork/kiln); no food production
  #   Type-B-only      = light-trade studios only (baking/weaving/fiber/leather); no combustion
  #   combined-campus  = two-wing design with both Type A and Type B studios (the canonical model)
  #   small-town-lite  = scaled-down combined-campus, 12-18 studios, for town-scale deployment

  total_studios: {integer}
  # Total count of rentable studios including anchor training studios.

  type_a_studios: {integer}
  # Count of Type A studios: forge, metalwork, pottery kiln, and other heavy-trade occupancies.
  # Type A studios require 3-phase sub-panels, industrial exhaust, and F-2 occupancy classification.
  # Set to 0 for Type-B-only facility_type.

  type_b_studios: {integer}
  # Count of Type B studios: baking, weaving, fiber arts, leather, and other light-trade occupancies.
  # Type B studios require food-grade exhaust, humidity control, and NSF plumbing where applicable.
  # Set to 0 for Type-A-only facility_type.

  anchor_training_studios: {integer}
  # Count of anchor training studios, rented at below-market rates.
  # These serve an apprentice-pipeline and civic-partnership function.
  # Include in total_studios. Below-market subsidy is captured in anchor_studio_subsidy_per_month.
  # Typical: 1. Set to 0 if no anchor studio in this configuration.

  # ── INFRASTRUCTURE RATINGS ────────────────────────────────────────────────

  main_electrical_service_amps: {integer}
  # Amperage of the building main electrical service. Typical range: 600-1200A.
  # Drives infrastructure capital cost and tenant capacity ceiling.

  has_3phase: {boolean}
  # true  = building is served by 3-phase electrical service.
  # false = single-phase only; limits Type A studio capability (no heavy induction equipment).

  has_industrial_exhaust_stack: {boolean}
  # true  = building has a dedicated forge-grade exhaust stack (Type A wing).
  # false = no industrial exhaust; Type A studios not supportable.
  # Required true for facility_type: Type-A-only or combined-campus.

  has_food_grade_exhaust_stack: {boolean}
  # true  = building has a dedicated food-grade exhaust stack with grease interceptor (Type B wing).
  # false = no food-grade exhaust; commissary tenants not supportable.
  # Required true for facility_type: Type-B-only or combined-campus.

  has_commissary_umbrella_license: {boolean}
  # true  = facility holds a commercial kitchen / commissary umbrella license.
  # false = no commissary umbrella; Type B food tenants must obtain individual commercial kitchen
  #         permits, significantly increasing tenant burden and reducing occupancy.
  # Required true whenever type_b_studios > 0 and facility serves baking / food-craft tenants.

  # ── OCCUPANCY / ZONING ────────────────────────────────────────────────────

  ibc_occupancy_classification: "F-2/B mixed" | "F-2 only" | "B only"
  # IBC occupancy group classification.
  #   F-2/B mixed = combined-campus or combined light-industrial + business; requires IBC §508
  #                 Mixed Use Protected analysis and 2-hour fire-rated separation wall.
  #   F-2 only    = light manufacturing only; Type A wing or Type-A-only facility.
  #   B only      = business occupancy; Type B wing or Type-B-only facility with no forge/kiln.

  zoning_required: light-industrial | mixed-use | retail-commercial
  # Minimum zoning category required for this facility configuration.
  #   light-industrial  = required for Type A or combined-campus (combustion / exhaust stack)
  #   mixed-use         = acceptable for combined-campus or small-town-lite in many jurisdictions
  #   retail-commercial = viable only for Type-B-only; Type A combustion prohibits retail-commercial

  # ── BUILD MODEL ───────────────────────────────────────────────────────────

  build_approach: adaptive-reuse | purpose-built-new | purpose-built-shell
  # Physical construction strategy.
  #   adaptive-reuse     = conversion of existing industrial/warehouse building
  #   purpose-built-new  = new construction from ground up
  #   purpose-built-shell = new shell construction with tenant-fitted interiors

  location_prototype: location-1-proof | chain-prototype | small-town-variant
  # Where this configuration fits in the rollout sequence.
  #   location-1-proof   = proof-of-concept first location; adaptive reuse; builds playbook
  #   chain-prototype    = optimized design for locations 2-5; purpose-built; brand established
  #   small-town-variant = 12-18 studio scaled-down design for town-scale markets (2,000-15,000 pop.)

  # ── TENANT ECONOMICS (OPERATOR PERSPECTIVE) ──────────────────────────────

  avg_monthly_rent_per_studio: {integer}
  # Blended average monthly rent per studio across all studio types, in USD.
  # This value is the basis for market_price_per_unit.
  # Compute as: weighted average of Type A, Type B, and anchor studio rents weighted by studio counts.
  # Anchor studio subsidy is already reflected in this blended average.
  # Range per spec §5.3: $875-$2,400/studio/month for medium suburban location.

  target_occupancy_rate: {decimal}
  # Target occupancy fraction. Range: 0.0-1.0.
  # Typical: 0.85. Conservative underwrite: 0.75. Strong: 0.95.
  # Drives throughput_units_equiv_per_year and NOI projections.
  # The Tier A market lens depends on this value; must be consistent with sim_params.

  anchor_studio_subsidy_per_month: {integer}
  # Monthly rent reduction per anchor training studio versus market-rate Type B equivalent.
  # USD. Represents the operator's investment in the tenant pipeline and civic function.
  # Example: if comparable Type B studio rents at $1,200 and anchor studio rents at $450,
  # anchor_studio_subsidy_per_month = 750.
  # This cost is implicit in avg_monthly_rent_per_studio when anchor studios are included
  # in the blend; authors should document whether avg_monthly_rent is pre- or post-subsidy.
```

---

## 3. Artisan Square `throughput` Block Structure

The `throughput:` block's internal structure is an artisan-square-specific extension per
`catalog/SCHEMA.md` §8. For artisan-square entries, throughput is measured in
**studio-months rented** — not production units per hour. The facility is not a
production trade; it is an infrastructure-rental business. The base schema fields
`units_per_hour` and `max_active_hours_per_week` are not applicable and must be set to
null explicitly so that E-3 cross-checks are not misfired against production-trade
formulas.

```yaml
throughput:
  # For artisan-square, throughput = studio-months rented.
  # This is not a production trade; unit-per-hour measures do not apply.
  units_per_hour: null          # not applicable (not a production trade)
  max_active_hours_per_week: null  # not applicable (throughput is studio-months, not hours)

  # Use these artisan-square-specific fields instead:
  studios_rented_per_month: {integer}
  # Expected studios occupied in a typical month.
  # Derivation: total_studios × target_occupancy_rate (rounded to nearest integer).
  # This is the operating throughput figure — how many tenants are paying rent in a given month.

  annual_studio_months: {integer}
  # Total studio-months rented in a year.
  # This is throughput_units_equiv_per_year for artisan-square entries.
  # Derivation: total_studios × target_occupancy_rate × 12
  # Must equal sim_params.throughput_units_equiv_per_year.

  graduation_rate_per_year: {decimal}
  # Fraction of tenants who graduate to standalone commercial space per year (0.0-1.0).
  # Typical range: 0.20-0.30 (20-30% of tenants graduate annually).
  # This is the natural vacancy-creation rate; it must be matched by the tenant pipeline
  # to sustain occupancy. If graduation_rate_per_year > 0.30, authors should document
  # the fill-rate assumption in Key Assumptions.
```

### `throughput` cross-checks (E-3) for artisan-square

The base schema E-3 rules apply with artisan-square-specific substitutions:

- `sim_params.throughput_units_equiv_per_year` = `total_studios × target_occupancy_rate × 12`.
  Authors must state this derivation explicitly in Key Assumptions.
- `throughput.annual_studio_months` must equal `sim_params.throughput_units_equiv_per_year`.
  A discrepancy between these two fields is a P1 E-3 finding.
- `throughput.studios_rented_per_month` must equal `annual_studio_months / 12` (rounded).
- Because `units_per_hour` and `max_active_hours_per_week` are null, the standard E-3-R2
  and E-3-R3 cross-checks (production-rate formula) are suspended for artisan-square entries.
  The E-3-R2 analogue for artisan-square is the studio-months formula above.
- `sim_params.labor_hours_per_unit` for artisan-square represents property management
  hours per studio-month (not craft production hours). Typical: 3-6 hours per studio-month
  for a blended location manager + facilities role. Authors must state this definition in
  Key Assumptions.
- `sim_params.downtime_fraction` for artisan-square represents the vacancy fraction
  = `1 - target_occupancy_rate`. Example: 0.85 occupancy → downtime_fraction = 0.15.
  Authors must state this interpretation explicitly.

---

## 4. Economics Field Reinterpretation for Artisan Square

The base `economics:` block fields carry different meaning for a building operator than
for a craft practitioner. The following table documents the artisan-square-specific
interpretation of each base field. Fields not listed here retain their standard
base-schema meaning.

| Base Field | Artisan Square Interpretation |
|---|---|
| `economics.capital_cost` | Building acquisition + all renovation / build-out costs. Three-point range. Low = adaptive reuse conservative; high = purpose-built aggressive. Per spec §6.1: typical range $760k–$1.45M for 20-28 studios. |
| `economics.install_cost` | Permitting + commissary licensing + initial fit-out costs that are one-time and non-structural. Per spec §6.1: commissary licensing + permitting = $15k–$30k. |
| `economics.annual_maintenance` | Ongoing maintenance of building systems: HVAC, electrical panels, structural, exhaust stacks, plumbing. Excludes insurance and compliance (those go in annual_consumables). Per spec §6.2: $20k–$35k/yr. |
| `economics.annual_consumables` | Insurance (commercial + commissary liability) + annual compliance costs (health dept, fire inspection, license renewal). These recur annually and are not maintenance events. Per spec §6.2: $25k–$40k/yr for insurance. |
| `economics.floor_space_rent_per_year` | Property taxes or mortgage interest on the building (if owned), or base building lease cost (if leased). Represents the cost of holding the real estate independent of fit-out. Per spec §6.2: $80k–$160k/yr. |
| `economics.market_price_per_unit` | **Required for market lens.** Average monthly rent per studio (`trade_specific.avg_monthly_rent_per_studio`). The unit of revenue for the building operator. Must be consistent with `trade_specific.avg_monthly_rent_per_studio`. Three-point range: low = anchor-studio-weighted or low-market scenario; mid = target blended average; high = full-occupancy premium-rate scenario. |
| `economics.industrial_baseline_price` | Comparable commercial lease rate per month per studio-equivalent (sq ft × local commercial $/sq ft / avg studio count). The baseline the artisan-square operator must beat to attract tenants. |
| `economics.pricing_notes` | Must name the comparable standalone commercial space rate and the tenant segment that pays a premium for all-inclusive infrastructure + commissary umbrella. |
| `sim_params.throughput_units_equiv_per_year` | Total annual studio-months rented = `total_studios × target_occupancy_rate × 12`. This is the single most important sim_params field for artisan-square entries; all revenue and payback projections derive from it. |

### Staffing cost note

For artisan-square entries with `lens_fit.civic: good` or `lens_fit.cooperative: good`,
`lens_context.civic.staffing_model` should reflect the building-management staffing
structure: typically 1.0 FT location manager + 0.5 FT facilities coordinator (per spec §6.2:
$90k–$120k/yr combined). The `role` field should name the building-management function,
not an artisan skill. `labor_hours_per_unit` in sim_params represents management hours
per studio-month, not craft production hours; this reinterpretation must be documented
in Key Assumptions.

---

## 5. Artisan Square `operator_skill_floor` Definitions

The base schema defines `operator_skill_floor` as "the minimum competence at which a
real operator can run the equipment safely and productively without direct supervision."
For artisan-square, "the equipment" is the building itself. The following values replace
the standard trade-craft tiers for artisan-square entries.

| Value | Artisan Square Meaning | Capability Boundary |
|---|---|---|
| `property-manager` | Day-to-day building operations: tenant relations, maintenance scheduling, billing, lease administration. No artisan-craft knowledge required. | Can manage routine occupancy, coordinate vendor maintenance calls, collect rent, handle lease renewals, respond to tenant requests. Cannot manage commissary compliance or Type A safety systems independently. |
| `artisan-building-operator` | All of property-manager, plus: commissary compliance management (Type B food tenants), Type A exhaust stack safety certifications, health department inspection preparation, fire code compliance for combustion studios. | Can manage full dual-occupancy facility without external compliance consultants for routine inspections. Can supervise tenant onboarding for both Type A and Type B studios. Cannot manage multi-location playbook deployment. |
| `chain-operator` | All of artisan-building-operator, plus: multi-location management, playbook deployment and adaptation, corporate-level commissary license structures, bulk purchasing coordination, location manager hiring and training. | Can open and operate new locations using the established playbook. Can manage multiple location managers. Can adapt permitting playbook to new jurisdictions. |

**Note on succession risk.** An entry with `operator_skill_floor: artisan-building-operator`
and `apprentice_friendly: false` must name succession risk in Known Risks — the compliance
knowledge is not transferable without deliberate documentation (the playbook).
`chain-operator`-floor entries without a documented playbook represent an institutional
single-point-of-failure; this should be named explicitly.

**Note on `apprentice_path` for artisan-square.** The `apprentice_path` block, when
present, describes the path from `property-manager` to `artisan-building-operator`. The
training stages map to: (1) standard property management, (2) commissary compliance
certification, (3) Type A safety certifications, (4) independent dual-occupancy facility
operation. `time_to_independent_operation` is typically "12-18 months to artisan-building-operator
standard."

---

## 6. Artisan Square `first_year_failures` Reference List

The base schema requires 2-4 `first_year_failures` items when `operations_reality` is
required. The following reference list reflects common facility-operation failure modes
in the first operating year. Authors select 2-4 items appropriate to the specific
facility configuration.

This list is descriptive and not exhaustive. Cost figures are illustrative starting
points; entries must carry a citation or explicit `[CITATION-NEEDED]` per E-1 rules.

| Component | Applicable facility types | Notes |
|---|---|---|
| HVAC / humidity control malfunction | combined-campus, Type-B-only (fiber arts studios) | Humidity control failure damages fiber arts inventory and violates fiber/textile tenant conditions. First-year commissioning failures are common in dual-occupancy HVAC systems. Specialist-serviceable; lead time 5-15 days for parts. |
| Exhaust stack damper failure — Type A wing | Type-A-only, combined-campus | Forge-grade stack damper failures in the first year from thermal cycling and commissioning calibration errors. Each wing's damper system should be treated as a separate failure item. Journeyman-serviceable for damper; specialist for stack resealing. |
| Exhaust stack damper failure — Type B wing | Type-B-only, combined-campus | Food-grade grease interceptor stack dampers fail independently from Type A. Grease accumulation in first 6 months is typically higher than design spec during commissioning period. |
| Commissary health inspection violation (first inspection) | Type-B-only, combined-campus (any with commissary umbrella) | First health department inspection under a new commissary umbrella license commonly finds procedural and documentation gaps even when physical infrastructure is compliant. Operator-serviceable but requires process correction and re-inspection scheduling (21-45 day cycle). |
| High vacancy in months 1-6 (occupancy < 60%) | All facility types | Not a mechanical failure, but the most common first-year operational failure. Pre-leasing targets often slip; tenant onboarding takes longer than modeled; anchor studio pipeline not yet producing referrals. Treat as a revenue-shortfall event. Estimated revenue impact: (target_occupancy_rate - 0.60) × avg_monthly_rent_per_studio × total_studios × 6 months. |
| Permitting surprise — zoning variance delay | All facility types (adaptive reuse especially) | Zoning variance approvals for F-2/B mixed occupancy in jurisdictions without precedent take 60-120 days longer than projected. Delays construction completion and pre-leasing start date. No direct replacement cost but significant carrying-cost impact. |
| Sub-panel metering system failure | All facility types | Individual studio sub-panel metering systems (required for utility pass-through billing) frequently have calibration or communication failures in the first year. Journeyman-electrician serviceable; low per-unit cost but affects multiple studios simultaneously. |

Authors populating `first_year_failures` for artisan-square entries should adapt the
`estimated_hours_to_failure` field to represent months-of-operation-to-failure (rather than
equipment-hours), and document this reinterpretation in Key Assumptions. The
`replacement_cost` field should reflect the full remediation cost including any re-inspection
fees, lost rent during downtime, or emergency contractor rates.

---

## 7. Per-Configuration-Type Field Guidance

The following notes identify which schema fields are most load-bearing for each
`facility_type` value. "Load-bearing" means the field (a) most directly determines
the E-3 cross-check result, or (b) is the primary evidence for the lens-fit claim.

### Type-A-only

Primary load-bearing fields: `type_a_studios`, `main_electrical_service_amps`,
`has_3phase`, `has_industrial_exhaust_stack`. The market lens depends entirely on
Type A rent rates; `avg_monthly_rent_per_studio` and `market_price_per_unit` must
reflect Type A rates only (no Type B blending). `ibc_occupancy_classification` must
be `F-2 only`. `zoning_required` must be `light-industrial`. The tenant pool for
Type A is narrower than combined-campus (smiths, metalworkers, kiln artists only);
`target_occupancy_rate` above 0.85 requires documented tenant demand evidence.
`has_commissary_umbrella_license` must be false; `type_b_studios` must be 0.

### Type-B-only

Primary load-bearing fields: `type_b_studios`, `has_food_grade_exhaust_stack`,
`has_commissary_umbrella_license`. The commissary umbrella is the core value
proposition for Type B food tenants; an entry with `has_commissary_umbrella_license:
false` and Type B food studios must document how food tenants obtain individual
commercial kitchen permits (and the associated tenant burden this creates).
`avg_monthly_rent_per_studio` reflects Type B rates only ($875-$1,750/month per
spec §5.3). `ibc_occupancy_classification` must be `B only`. `zoning_required` may
be `retail-commercial` if no combustion equipment is present.

### combined-campus

The canonical two-wing Artisan Square model. All `trade_specific` fields are active.
The primary load-bearing analytical requirement is the blended `avg_monthly_rent_per_studio`
calculation — authors must document the studio-type weights used to compute the blend
(e.g., "8 Type A at $1,800 avg + 14 Type B at $1,200 avg + 2 anchor at $450 = blended
$1,325 across 24 studios"). `ibc_occupancy_classification` must be `F-2/B mixed`.
The 2-hour fire-rated separation wall (IBC §508) is a non-negotiable structural cost
that must appear in `economics.capital_cost` or `economics.install_cost`. The civic
lens is strongest for combined-campus entries because the multi-trade workforce
development externality spans both studio types; `lens_context.civic.civic_externalities`
should name both Type A and Type B trade pipelines.

### small-town-lite

The scaled-down variant for town-scale markets (2,000-15,000 population). Key constraint:
total_studios ≤ 18. The economics are thinner than combined-campus (fewer studios to
spread fixed costs); `target_occupancy_rate` carries more sensitivity here — a 10-point
occupancy drop has larger percentage impact on NOI. The civic lens is strongest for
small-town-lite entries because civic co-investment (subsidized land, anchor studio
partnership) is most likely to appear at this scale. `lens_context.civic.benchmark_comparison`
should reference town-scale civic services (library, rec center) rather than regional
economic development comps. `build_approach` for small-town-lite entries is typically
`purpose-built-shell` or `adaptive-reuse` (lower capital than full purpose-built-new).
`location_prototype` should be `small-town-variant`.

---

## 8. Sources

- `specs/2026-04-19-artisan-square-design.md` Sections 4-6 — physical design, tenant
  model, and economic model for Artisan Square; primary source for infrastructure
  specifications, studio counts, rent ranges, and build-out cost ranges used in this
  extension.
- `catalog/SCHEMA.md` v1.1 — base schema; all fields, validation rules, conditional
  triggers, and prose-section requirements not covered by this extension are governed
  there.
- `catalog/artisan-square/REQUIREMENTS.md` (upcoming) — functional requirements for
  artisan-square entries; will be the primary source for occupancy rate benchmarks,
  throughput cross-check calibration, and zoning analysis guidance once created.

---

*Schema extension iteration log:*

- 2026-04-18: v1.0 — initial creation per Plan J Task 1.
