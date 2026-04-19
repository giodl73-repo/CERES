---
trade: weaving
doc_type: schema-extension
extends: catalog/SCHEMA.md
version: "1.0"
schema_base_version: "1.1"
status: draft
---

Base schema: catalog/SCHEMA.md v1.1

# Weaving Schema Extension

This file extends the canonical catalog schema (`catalog/SCHEMA.md` v1.1) with
weaving-specific field definitions. It does not duplicate base-schema content; consult
`catalog/SCHEMA.md` for all required fields, validation rules, conditional triggers,
and prose-section requirements. This file is authoritative only for (a) the internal
structure of the `throughput:` block for weaving entries, (b) allowed values and
capability notes for `energy_source`, (c) the required `loom_type` field and its
allowed values, (d) the meaning of each `operator_skill_floor` tier in a weaving
context, (e) the required `fiber_source_declaration` field and its allowed values,
(f) the `humidity_control_required` field, (g) a reference list of common
`first_year_failures` items for weaving equipment, and (h) per-niche-group guidance
for Wave 2 entry authors. Any field not mentioned here is governed solely by
`catalog/SCHEMA.md`.

---

## 1. Weaving `throughput` Block Structure

The `throughput:` block's internal structure is a weaving-specific extension per
`catalog/SCHEMA.md` §8. The base schema requires `max_active_hours_per_week` and at
minimum one rate measure; the fields below fulfil that requirement for weaving entries.

**Unit definition note:** `meters_per_day` is a linear measure; its area equivalent
depends on `warp_width_cm`. Authors must state the cloth type and warp width clearly.
For tapestry entries, `meters_per_day` may be replaced by `m2_per_day` with explicit
justification. `sim_params.throughput_units_equiv_per_year` must use a consistent unit
stated in Key Assumptions.

```yaml
throughput:
  meters_per_day: {decimal}
  # Net woven length per full operating day.
  # Dependent on warp width, pattern complexity, and operator skill.
  # Typical ranges by pattern_complexity:
  #   plain weave: 4-10 m/day (floor loom, journeyman); 1-4 m/day (rigid heddle)
  #   twill: 2-6 m/day (floor loom, journeyman)
  #   pattern/overshot: 1-3 m/day (floor loom, journeyman-to-master)
  #   tapestry: 0.1-0.5 m²/day (master-weaver; state as area for tapestry)
  # [CITATION-NEEDED: measured throughput rates by loom type and pattern]

  warp_width_cm: {integer}
  # Usable weaving width at the reed, in centimeters.
  # Typical ranges:
  #   backstrap: 30-60 cm
  #   rigid-heddle: 30-90 cm
  #   floor-loom-4shaft: 60-150 cm
  #   floor-loom-8shaft: 90-200 cm
  #   drawloom: 60-150 cm (pattern width may be narrower than loom width)
  #   power-loom: 100-250 cm

  pattern_complexity: plain | twill | pattern | tapestry
  # plain: plain weave, tabby, simple basket weave
  # twill: 2/2 twill, herringbone, satin derivatives
  # pattern: overshot, M's & O's, networked twill, supplementary weft; requires 4+ shafts
  # tapestry: weft-faced discontinuous-weft tapestry; requires master-weaver floor

  max_active_hours_per_week: {integer}
  # Net active weaving hours per week after warping, dressing the loom,
  # threading/sleying overhead, and finishing work.
  # Warping and loom-dressing time is significant: a new warp may require
  # 4-8 hours of setup for a floor loom before the first pick is woven.
  # Realistic ceiling for full-time weaver: 30-40 hr/wk at loom;
  # total shop time including setup may reach 50-55 hr/wk.

  product_mix:                        # optional but recommended
    yardage: {0-100}                  # woven cloth sold by the meter/yard
    rugs_upholstery: {0-100}          # rugs, floor coverings, upholstery-weight cloth
    tapestry_art: {0-100}             # tapestry and wall-hanging work
    garments_accessories: {0-100}     # finished garments, scarves, accessories
    instruction_open_studio: {0-100}  # teaching time and shared-studio facilitation
    # Sum must equal 100. For cooperative/civic entries, instruction_open_studio
    # may dominate; for market-primary entries, yardage or tapestry_art dominates.

  throughput_variance:
    worst_month_fraction_of_average: {decimal}
    # Weaving demand is relatively non-seasonal for commissions and production coops.
    # Instruction-based entries show summer uptick (workshops) and January trough.
    # Typical range for commission/market entries: 0.60-0.80.

    best_month_fraction_of_average: {decimal}
    # Holiday gift season (Oct-Dec) provides a peak for retail-oriented entries.
    # Typical range: 1.20-1.50 for retail; 1.0-1.1 for commission-only.

    seasonal: {string}
    # One-sentence description of the seasonal pattern.
    # Example: "Commission work is non-seasonal; retail yardage peaks Oct-Dec."
```

### `throughput` cross-checks (E-3)

The base schema E-3 rules apply. Weaving-specific guidance:

- `sim_params.throughput_units_equiv_per_year` must be computed from `meters_per_day`
  × annual operating days, derated by `max_active_hours_per_week` fraction and
  `throughput_variance`. For area-sold entries, convert using `warp_width_cm`.
  State the annual operating days assumption (typically 220-260 days/year
  for a studio weaver accounting for warping setup days).
- An entry with `operator_skill_floor: rigid-heddle-novice` cannot claim
  `pattern_complexity: pattern` or `tapestry`; these require journeyman-weaver or
  master-weaver floor respectively.
- Entries with `loom_type: backstrap` must cap `warp_width_cm` at 60 cm maximum
  unless an explicit justification is provided.
- `throughput_variance.worst_month_fraction_of_average` must be consistent with
  `sim_params.downtime_fraction`; loom-setup days (warping) count toward
  non-production overhead and should be reflected in `max_active_hours_per_week`.

---

## 2. Weaving-Specific `energy_source` Enumeration

The base schema permits trade-specific `energy_source` values. The following values
are the allowed set for weaving entries. Weaving is unusual in the CERES catalog:
the primary productive equipment (the loom) requires no energy in most forms; energy
consumption relates to lighting, climate control, and occasional power-loom operation.

| Value | Use case | Emissions posture | Regulatory notes | Typical consumption |
|---|---|---|---|---|
| `no-power` | Hand-operated and treadle looms; backstrap, rigid-heddle, floor looms with treadle mechanism. No electrical power required for weaving. | Near-zero | No electrical permit for weaving operations; lighting must comply with building code | Essentially zero for weaving; workshop lighting only (if natural light sufficient) |
| `electric-lighting-only` | Floor and frame looms in a studio requiring artificial lighting; no powered weaving mechanism. The dominant mode for most non-power-loom entries. | Near-zero (grid-source) | Standard commercial electrical permit; no special weaving-related permit | 1-5 kWh/day depending on studio size and natural light availability |
| `electric-power-loom` | Power-assisted or fully automated loom mechanisms; rapier, projectile, or air-jet power looms. Not standard for artisan/handwoven entries. | Near-zero on-site (grid) | Three-phase supply typical for production looms; may trigger industrial-zoning requirements | 5-25 kWh/hr per power-loom unit [CITATION-NEEDED] |
| `hybrid` | Studio combining hand looms (no-power) with power-assisted auxiliary equipment (warping mill motor, electric yarn winder, power bobbin winder, climate-control system). | Near-zero | Standard commercial electrical; no weaving-specific permit | 2-8 kWh/day for auxiliary equipment; climate control adds 10-25 kWh/day if applicable |

**Note on climate control.** For entries with `humidity_control_required: true`, the
energy demand of climate control (HVAC, humidifier or dehumidifier) typically exceeds
the energy demand of weaving itself. Authors should account for climate-control energy
in `energy_consumption_per_active_hour` or document it separately in Key Assumptions.
Climate control is an operating cost, not a capital cost, but it materially affects
`annual_maintenance` and `economics.floor_space_rent_per_year` if leased space lacks
existing systems.

---

## 3. Required Field: `loom_type`

**This field is required for all weaving entries.** It must be present in every entry's
frontmatter and must be consistent with `throughput.warp_width_cm`,
`throughput.pattern_complexity`, `operator_skill_floor`, and the Key Assumptions prose.

```yaml
loom_type: backstrap | rigid-heddle | floor-loom-4shaft | floor-loom-8shaft | drawloom | power-loom
```

| Value | Typical warp width | Pattern range | Operator floor | Capital range | Notes |
|---|---|---|---|---|---|
| `backstrap` | 30-60 cm | plain to simple pattern | journeyman-weaver (body-tension technique requires practice) | $200-$1,500 | Portable; no floor space required; traditional in many Mesoamerican, Andean, SE Asian traditions |
| `rigid-heddle` | 30-90 cm | plain weave to simple pick-up patterns | rigid-heddle-novice | $150-$600/unit | Lowest barrier loom; suitable for tool-library and workshop models; limited pattern complexity |
| `floor-loom-4shaft` | 60-150 cm | plain, twill, overshot, most 4-shaft patterns | journeyman-weaver | $1,500-$6,000 | Standard studio loom; workhorse for most artisan weaving catalog entries |
| `floor-loom-8shaft` | 90-200 cm | all patterns including networked twills and 8-shaft structures | journeyman-weaver (master for complex networked work) | $4,000-$15,000 | Wider pattern range; wider cloth; higher capital; suits fashion atelier, architectural textile, tapestry entries |
| `drawloom` | 60-150 cm | unlimited pattern complexity including brocade and compound weaves | master-weaver | $8,000-$30,000 | Historical loom for complex figured weaves (Jacquard antecedent); requires pattern-shaft setup time; low throughput |
| `power-loom` | 100-250 cm | plain to basic patterns (pick-up and dobby attachments extend range) | journeyman-weaver with mechanical aptitude | $15,000-$80,000 | High throughput but approaches commodity-cloth territory; entries must document specialty positioning; see DECLINE-VERDICT |

---

## 4. Required Field: `humidity_control_required`

**This field is required for all weaving entries.**

```yaml
humidity_control_required: {boolean}
```

| Value | When applicable | Operating implications |
|---|---|---|
| `true` | Wool warp or weft; silk; fine linen; any fiber that changes dimension with humidity | Warp tension changes with relative humidity; dimensional stability of finished cloth affected; climate-controlled studio recommended (45-55% RH); heating/cooling and humidification/dehumidification equipment needed |
| `false` | Cotton; synthetic fiber; coarse linen; most upholstery-weight materials in non-extreme climates | Standard building environment acceptable; no dedicated humidity management required |

Authors working with mixed-fiber entries (e.g., cotton warp + wool weft) should set
`humidity_control_required: true` if the more humidity-sensitive fiber dominates the
structural or aesthetic properties of the cloth.

---

## 5. Weaving-Specific `operator_skill_floor` Definitions

The base schema defines `operator_skill_floor` as "the minimum competence at which a
real operator can run the equipment safely and productively without direct supervision."
The following values apply to weaving entries.

| Value | Weaving meaning | Capability boundary | Equipment scope |
|---|---|---|---|
| `rigid-heddle-novice` | Entry-level operator who has completed basic rigid-heddle instruction. Can wind a warp, dress a rigid-heddle loom, and weave a plain-weave cloth. | Cannot manage floor-loom threading or tie-up. Cannot execute pattern weaves. Cannot diagnose and correct warp tension problems independently. Can produce plain-weave scarves, wraps, and simple utility cloth on a rigid-heddle loom. | Rigid-heddle loom only. NOT floor loom, backstrap loom, or drawloom. |
| `journeyman-weaver` | Independently capable studio weaver. Can thread a multi-shaft floor loom, manage warp tension, execute standard pattern structures (twill, overshot, M's & O's), and produce consistent yardage. | Can manage floor-loom-4shaft and floor-loom-8shaft setup and operation without supervision. Can execute most pattern structures within the loom's shaft capacity. Cannot reliably execute master-tier work (complex drawloom figures, large-scale tapestry with shading gradients, kasuri ikat registration). Can supervise a rigid-heddle-novice. | Floor-loom-4shaft, floor-loom-8shaft, rigid-heddle; NOT drawloom for complex figured work; NOT high-warp tapestry at master level. |
| `master-weaver` | Senior practitioner with full technical range across loom types and pattern traditions. Can execute drawloom figured weaves, large-format tapestry, complex ikat registration, and tradition-specific heritage weave structures. | Drawloom figured weave (brocade, compound twill). High-warp tapestry with tonal shading and complex compositional structure. Kasuri ikat with tight registration. Backstrap loom at traditional precision. Can design and set up complex threading sequences. Can train and assess journeyman weavers. | All loom types. Required for weave-001 (Tapestry), weave-003 (Architectural), weave-004 (Fashion Atelier), weave-006 (Traditional Revival), weave-008 (Japanese Textile). |

**Note on backstrap loom and operator skill.** Backstrap weaving requires internalized
body-tension control that is not achievable by a rigid-heddle-novice. The entry
`weave-014` (Backstrap Home Studio) requires `journeyman-weaver` minimum because
the backstrap technique demands physical practice and body-tension judgment that
goes beyond basic rigid-heddle instruction. Do not set `operator_skill_floor:
rigid-heddle-novice` for any backstrap loom entry.

---

## 6. Required Field: `fiber_source_declaration`

**This field is required for all weaving entries** per DECLINE-VERDICT fiber-sourcing
falsifier. It must be present in every entry's frontmatter and must be consistent with
the Key Assumptions prose section.

```yaml
fiber_source_declaration: industrial-yarn-purchased | local-fiber-spun | integrated-spinning | heritage-fiber
```

| Value | Meaning | Supply-chain dependency | Capital implication |
|---|---|---|---|
| `industrial-yarn-purchased` | Weaver purchases commercially spun yarn from a distributor or wholesaler. No spinning infrastructure or direct fiber relationship. | Yarn price volatility; quality consistency from commercial sources is reliable; specialty/luxury yarn may have long lead times. | Lowest (yarn procurement only; working-capital inventory). |
| `local-fiber-spun` | Weaver sources yarn from a local or regional hand-spinner or small-scale spinning operation, typically with a direct relationship. Spinning is done by a separate entity. | Spinner dependency; single-source risk; quality and quantity may be less consistent than industrial yarn; scheduling coordination required. | Low-moderate (relationship management; may involve premium pricing for local-spun yarn). |
| `integrated-spinning` | Weaver has a formal operational integration with a spinning operation: may be the same cooperative, same workshop, or a formal yarn-production arrangement within the studio. The spinning is done at the weaving site or in direct operational coordination. | Spinning equipment maintenance; spinner skill requirement in addition to weaver skill; fiber sourcing (upstream from spinning). | High (spinning wheel or spindle inventory, fiber stock, spinning skill; doubles the equipment and skill requirement of the operation). |
| `heritage-fiber` | Weaver uses heritage-breed or heritage-variety fiber (rare-breed wool, heritage cotton, natural plant fiber) as a defining feature of the product. The fiber source is part of the product's identity and value proposition. | Heritage-breed or heritage-variety sourcing is a specialty supply chain with limited suppliers; disruption risk is higher than industrial yarn. | Moderate (premium sourcing cost; may involve direct farm relationship or long-term supply contracts). |

Authors must explain the specific fiber sourcing in Key Assumptions: name the fiber
type(s) used, specify the typical yarn counts or weights, and assess supply continuity.
Entries claiming `integrated-spinning` must document the spinning equipment and
spinning-skill requirement as a separate capital and operator item.

---

## 7. Weaving `first_year_failures` Reference List

The base schema requires 2-4 `first_year_failures` items per entry. The following
reference list reflects common weaving-equipment failure modes in the first operating
year; authors select 2-4 items appropriate to the specific loom type and configuration.

This list is descriptive and not exhaustive. Numbers are illustrative starting points;
entries must carry a citation or explicit `[CITATION-NEEDED]` per E-1 rules.

| Component | Applicable loom types | Typical hours-to-failure | Notes |
|---|---|---|---|
| Heddle breakage (wire or texsolv) | floor-loom-4shaft, floor-loom-8shaft, drawloom | 500-2,000 hr | Wire heddles fatigue and snap at the eye; texsolv heddles stretch and lose registry. Both are operator-replaceable; heddle sets are low-cost but require re-threading when replaced in bulk. Lead time: 1-7 days for stocked heddles. |
| Warp beam ratchet / pawl wear | floor-loom-4shaft, floor-loom-8shaft | 1,500-3,500 hr | Ratchet-and-pawl beam tensioning wears under constant use; slippage causes warp-tension loss mid-weave. Operator-serviceable with replacement pawl springs; journeyman for full ratchet replacement. Lead time: 5-14 days. |
| Treadle tie-up cord wear or breakage | floor-loom-4shaft, floor-loom-8shaft | 800-2,500 hr | Texsolv or cord tie-ups connecting treadles to shaft lamms wear and break; replacement is operator-serviceable (re-tie); takes 30-90 min per shaft. Lead time: immediate (keep spare cord stock). |
| Reed damage (bent dents) | floor-loom-4shaft, floor-loom-8shaft, rigid-heddle, drawloom | 1,000-3,000 hr | Reed dents bend or break from dropped objects, excess beating force, or improper storage. A bent dent creates a streak in the cloth. Operator-diagnosis; journeyman-level reed replacement or specialist repair. Lead time: 3-14 days for replacement reed. |
| Rigid heddle slot wear | rigid-heddle | 500-2,000 hr | Slots and holes in rigid heddles wear from repeated yarn abrasion; metal-slotted heddles are more durable than plastic but not immune. Replacement is operator-level (full heddle swap). Lead time: 1-7 days. |
| Backstrap strap or loom-bar wear | backstrap | 200-1,000 hr | Leather or woven backstrap fatigue and crack; front and back bars may split along grain. Operator-level replacement (traditional materials easy to source locally); see REQUIREMENTS for traditional material specifications. Lead time: 0-3 days locally. |
| Dobby mechanism malfunction | floor-loom-8shaft (dobby-equipped), drawloom | 2,000-4,000 hr | Mechanical dobby (peg-and-lever) mechanisms develop stick-and-release failures from accumulated lint and wear. Journeyman-level cleaning and adjustment; specialist for mechanism replacement. Lead time: 5-21 days for parts. |
| Climate-control system failure (humidity) | All entries with humidity_control_required: true | 1,500-3,500 hr | Humidifier or dehumidifier failure causes warp-tension instability and potential cloth defect. Not loom-specific; building-system maintenance. Journeyman-level diagnosis; specialist for HVAC repair. Lead time: 1-7 days for residential-scale units; 5-21 days for commercial systems. |

Authors selecting items from this list must populate all five sub-fields required
by the base schema: `item`, `estimated_hours_to_failure`, `replacement_cost`,
`replacement_lead_time_days`, and `serviceable_by`.

---

## 8. Per-Niche-Group Guidance for Wave 2 Authors

The 15-entry manifest (Plan I) distributes entries across four niche groups. The
following notes identify which schema fields tend to be most load-bearing for each group.

### Group A — Luxury / Specialty (weave-001 through weave-005)

`market_price_per_unit` + `economics.industrial_baseline_price` are the critical field
pair for this group: the premium over industrial-woven cloth is the core economic claim,
and it must be cited (sourced / inferred / placeholder) per E-1 requirements. The
premium is typically based on provenance, pattern complexity, and material quality —
all of which must be named explicitly.

`operator_skill_floor: master-weaver` is required for weave-001, weave-003, weave-004.
`fiber_source_declaration` is a market-differentiation signal: `local-fiber-spun` or
`heritage-fiber` supports the luxury-positioning claim; `industrial-yarn-purchased`
requires a stronger case for premium pricing.

`humidity_control_required: true` for most Group A entries (fine wool, silk, or mixed
natural fiber). Climate-control cost must be reflected in `economics.annual_maintenance`
or `floor_space_rent_per_year`.

For weave-005 (Custom Rug & Upholstery), the B2B-channel dependency (interior designers
and commercial specifiers) is a key risk that must be addressed in Known Risks and
`lens_fit` values.

### Group B — Heritage / Cultural (weave-006 through weave-008)

`fiber_source_declaration: heritage-fiber` or `local-fiber-spun` is the defining
signal for this group. Entries that cannot source tradition-specific fiber must explain
the substitution and assess whether it undermines the heritage-positioning claim.

`operator_skill_floor: master-weaver` is required for weave-006 and weave-008
(tradition-holder knowledge is not reducible to journeyman weaving skill).
weave-007 (Coverlet) is a journeyman-accessible tradition if the entry uses
standard 4-shaft floor-loom structures; the historical lineage must cite the Plan B
American frontier chapter passage specifically.

For weave-006, the civic claim must name the specific community and tradition — not
generic "ethnic weaving." Lens_context.civic must include a named community group,
cultural organization, or heritage-preservation body as the political coalition.

### Group C — Community / Coop / Educational (weave-009 through weave-013)

`lens_context.cooperative` is the primary load-bearing block for weave-009 through
weave-013. All Ostrom-principle sub-fields must be substantive; scheduling/booking
rules for shared-loom access (weave-009, weave-010) must name the specific mechanism
(time-slot booking, member-priority rules, guest weaving policy).

For weave-011 (Therapeutic Weaving), the civic claim must include clinical-partnership
terms and therapeutic-outcome benchmarks — not just cost comparison. A civic entry
that justifies itself solely on cost cannot claim `lens_fit.civic: good`.

For weave-012 (Apprentice Training), `apprentice_path` is the defining block; all
three sub-fields must be specific to the vocational program named.

For weave-013 (Production Weaving Cooperative), `fiber_source_declaration` and the
specialty-cloth positioning argument are critical: this entry must explicitly document
why its output is not commodity cloth (per DECLINE-VERDICT). Without a credible
specialty argument, this entry should be classified `status: deprecated` and
replaced with a less production-intensive cooperative model.

### Group D — Minimum-viable / Stress-test (weave-014, weave-015)

weave-014 (Backstrap Home Studio) tests the absolute capital floor. `economics.capital_cost`
is the primary data point: this entry is testing whether a $200-$1,500 capital entry
is economically viable at village scale. Expected verdict is marginal-to-fail at
market and coop; the question is whether any civic-cultural cell produces a positive
result. `operator_skill_floor: journeyman-weaver` must be justified: backstrap weaving
is not a novice technique.

weave-015 (Artist-Designer Collaboration) tests a hybrid market + coop model. The
IP/attribution and revenue-sharing rules between weaver and designer must be named
in the Key Assumptions — this is a primary failure mode for collaboration studios
that the entry must address directly.

---

## 9. Sources

The following documents are the primary sources for the weaving-specific parameter
ranges and definitions in this extension:

- `research/trades/weaving/REQUIREMENTS.md` — functional requirements; primary authority
  for throughput ranges, loom type capability, fiber regime options, footprint,
  operator skill definitions, and product-category matrix.
- `research/trades/weaving/HISTORICAL-FORMS.md` — physical loom characteristics by
  culture; fiber traditions and weave structures that inform `throughput.meters_per_day`
  ceiling estimates and `throughput_variance.seasonal` patterns.
- `research/trades/weaving/DECLINE-VERDICT.md` — niche targeting; fiber-sourcing
  falsifier; binding guidance on `fiber_source_declaration` requirement; commodity-cloth
  exclusion.
- `catalog/SCHEMA.md` v1.1 — base schema; all fields, validation rules, and conditional
  triggers not covered by this extension are governed there.

---

*Schema extension iteration log:*

- 2026-04-19: v1.0 — initial creation per Plan I Wave 0 (Task 2).
