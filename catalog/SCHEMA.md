# Catalog-Entry Schema (Canonical)

**Version:** 1.0
**Date:** 2026-04-18
**Status:** canonical
**Authoritative for:** all catalog entries in `catalog/<trade>/entries/`
**Spec cross-reference:** `specs/2026-04-18-ceres-design.md` Section 5 (v0.2)

---

## 1. Purpose

This file is the single authoritative contract between catalog authors and the simulation
layer. Every catalog entry — regardless of trade — must match the schema defined here.
The YAML frontmatter is machine-ingested by Tier A, B, and C simulations; a missing
required field produces a failed or silently incorrect evaluation cell. The prose sections
are human-evaluated by the panel voice and editorial gate system. If this schema changes,
the version number below must be bumped, all existing entries must be re-validated against
the new version, and a corresponding amendment to `specs/2026-04-18-ceres-design.md`
Section 5 must be filed. The spec is the primary authority on project scope; this file is the primary
authority on field-level schema detail. When they conflict, a spec amendment
is required (see Section 9). Both are kept in lock-step; divergence in either
direction triggers an amendment, not a silent override.

---

## 2. File Layout

Each catalog entry is one Markdown file:

```
catalog/<trade>/entries/{id}-{slug}.md
```

- `<trade>` — trade name, lowercase, hyphen-separated (e.g. `smithing`, `baking`, `weaving`)
- `{id}` — zero-padded three-digit integer scoped to the trade (e.g. `001`, `042`)
- `{slug}` — short human-readable kebab-case label for the design (e.g. `backyard-propane-compact`)

Example: `catalog/smithing/entries/003-shared-toollibrary-coal.md`

The file contains two parts in order:
1. **YAML frontmatter** — delimited by `---` fences; machine-ingested.
2. **Prose sections** — standard Markdown headings; human-authored and human-reviewed.

Trade-level metadata (overview, design-space map) lives in `catalog/<trade>/README.md`.
Trade-specific schema extensions live in `catalog/<trade>/SCHEMA.md` (see Section 8).

---

## 3. Full YAML Frontmatter Schema

The annotated reference block below documents every field. An example entry (forge-003)
follows in Section 3.2.

### 3.1 Annotated Field Reference

```yaml
---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: <string>
# Globally unique entry identifier. Convention: <trade>-<NNN>.
# Example: forge-003

trade: <string>
# Trade slug matching the enclosing catalog/<trade>/ directory.
# Example: smithing

name: <string>
# Full human-readable name of the equipment design.
# Example: "Shared Tool-Library Coal Forge (medium footprint)"

tagline: <string>
# One-sentence description: ownership model + distinguishing feature.
# Example: "Community-owned coal forge with member-booked shifts"

status: <draft|reviewed|validated|deprecated|superseded>
# Promotion lifecycle. Starts `draft`. Only `validated` entries populate
# playbook recommendations. `superseded` entries remain in the catalog
# linked via the entry that replaces them.

version: <semver-string>
# Entry version. Start at 0.1. Bump on any material change. See Section 9.
# Example: 0.2

supersedes: <string|null>
# ID of the entry this one replaces, or null.
# Example: null    or    forge-001

inspirations: [<string>, ...]
# List of historical or modern precedents that informed the design.
# Each entry must have a matching prose explanation of *functional* (not
# aesthetic) inheritance in the Historical Lineage section.
# Example: [medieval-european-village-forge, edo-blacksmith-cooperative]

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: <number>
# Indoor floor area occupied by the equipment and its immediate working zone
# (operator space, material staging). Square metres. Does not include
# dedicated storage or customer-facing space.

ceiling_min_m: <number>
# Minimum clear ceiling height required for safe operation. Metres.
# Drives zoning and building-selection decisions.

ventilation: <string>
# Ventilation requirement category.
# Accepted values: natural-sufficient | mechanical-extraction-required |
#                  dedicated-exhaust-system | none
# One value only; elaborate in regulatory_notes if needed.

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: <string>
# Primary energy source.
# Common values: coal | propane | natural-gas | electricity | wood | induction
#                hybrid-electric-propane | (trade-specific values permitted)

energy_consumption_per_active_hour: <string>
# Consumption at full operational load. Include unit (kg, kWh, L, m3).
# Example: "8 kg coal"   or   "12 kWh"

backup_fuel: <string|null>
# Secondary fuel available if primary is unavailable. null if none.
# Example: propane

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  # Trade-specific sub-structure. Always nested under the key `throughput`.
  # Contents are defined in catalog/<trade>/SCHEMA.md.
  # Every trade sub-structure MUST include at minimum:
  #   - a units-per-hour or equivalent rate measure
  #   - max_active_hours_per_week (drives E-3 cross-checks)
  # Example (smithing):
  units_per_hour: { small_work: <n>, medium_work: <n>, large_work: <n> }
  max_active_hours_per_week: <number>

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: <string>
# Minimum operator competence required for safe, productive operation.
# Accepted values: novice | apprentice | journeyman | master
# Drives labour-pipeline risk assessment.

operators_concurrent: <string>
# Number of operators required simultaneously for normal operation.
# Use a range string when variable: "1-2". Use integer string for fixed: "1".

apprentice_friendly: <boolean>
# true  = realistic apprentice on-ramp exists; entry should describe it in prose.
# false = no practical apprentice path; succession risk MUST be named in
#         Known Risks section (Principle 9).

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: <ISO-4217 string>
  # Currency for all monetary fields in this block.
  # FX normalisation to project base currency at evaluation time via
  # corpus/program/CURRENCIES.md.
  # Example: USD

  capital_cost: { low: <number>, mid: <number>, high: <number> }
  # All-in equipment purchase cost (hardware only; excludes installation).
  # Three-point range required. mid = central estimate used by sim_params.cost_mean.

  install_cost: <number>
  # One-time installation cost: electrical, plumbing, structural, permitting.
  # Single estimate acceptable; range form { low, mid, high } also valid.

  annual_maintenance: <number>
  # Expected annual maintenance spend under normal operating conditions.
  # Excludes first-year failure replacements (those go in operations_reality).

  annual_consumables: <number>
  # Annual spend on consumables consumed in normal operation (fuel, flux, dies,
  # wear parts replaced on schedule). Excludes unexpected failures.

  floor_space_rent_per_year: <number>
  # Imputed or actual annual rent for the footprint_m2 required.
  # Use local commercial-rate estimate; must be cited or flagged as estimate.

  market_price_per_unit: { low: <number>, mid: <number>, high: <number> }
  # CONDITIONAL — required when lens_fit.market is `good` or `marginal`.
  # Market-clearing price per output unit (in the same currency as this block).
  # Three-point range required. Omit entirely (do not set null) when
  # lens_fit.market is `poor` and the entry is never evaluated on the market lens.
  # Uncited market price is a P1 E-1 finding.

  pricing_notes: <string>
  # CONDITIONAL — required when market_price_per_unit is present.
  # One-to-two sentence explanation of: what the "unit" is, the premium over
  # the relevant industrial-competitor baseline (named and cited), and the
  # customer segment expected to pay the premium. Inconsistency between
  # pricing_notes and sim_params payback is a P1 E-3 finding.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  # CONDITIONAL — required when any lens_fit value is `good` or `marginal`.
  # Captures the tail-risk picture that average-case sim_params miss.
  # Paper designs assume the average case; real operations die in the tail.

  first_year_failures:
    # List of anticipated component failures in the first operating year.
    # Minimum two items required (Principle 3).
    - item: <string>
      # Component name.
      estimated_hours_to_failure: <number>
      # Estimated operating hours before first failure. Drives maintenance
      # scheduling and working-capital buffer calculations.
      replacement_cost: <number>
      # Cost to replace, in the entry's economics.currency.
      replacement_lead_time_days: <number>
      # Calendar days from order to installation-ready replacement.
      # Drives downtime planning and inventory decisions.

  consumables_lead_time_days: { typical: <number>, worst: <number> }
  # Lead time for routine consumable resupply.
  # typical = median order-to-delivery; worst = 95th-percentile or known
  # supply-chain stress scenario. Both values required (Principle 3).

  throughput_variance:
    seasonal: <string>
    # One-sentence description of seasonal demand pattern.
    # Example: "Fall/winter peak for repair work; summer trough"
    worst_month_fraction_of_average: <number>
    # Throughput in the worst month as a fraction of monthly average.
    # Example: 0.45 means worst month is 45% of average. Required (Principle 3).
    best_month_fraction_of_average: <number>
    # Throughput in the best month as a fraction of monthly average.
    # Example: 1.65 means best month is 165% of average.

  operator_impact:
    noise_db: <number>
    # Sound level at operator position during normal operation, in dB(A).
    # Required (Principle 3). Drives HSE assessment and recruitment.
    heat_exposure: <string>
    # Qualitative description of thermal environment at operator position.
    # Required. Example: "High near forge; adequate ventilation required"
    emissions: <string>
    # Exhaust / particulate / chemical emissions profile.
    # Required. Drives regulatory_notes and zoning assessment.
    physical_demand: <string>
    # Physical effort required during normal operation.
    # Example: "Moderate-heavy lifting; sustained standing"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  # Terse three-line flag for showstoppers only. Not a legal treatise.
  # Each field: one sentence maximum. Elaborate in prose Known Risks section.
  zoning: <string>
  # Zoning category required; known restrictions.
  emissions: <string>
  # Emissions permit triggers; known regulatory thresholds.
  other: <string>
  # Any other significant regulatory constraint (fire code, OSHA, licensing).

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: <good|marginal|poor>
  # Fitness for the MARKET lens (private profit motive).
  # good     = likely to produce `win` verdict under at least one scale
  # marginal = possible `marginal` verdict; viable under favourable assumptions
  # poor     = unlikely to be viable under MARKET lens at any scale
  cooperative: <good|marginal|poor>
  civic: <good|marginal|poor>

scale_fit:
  village: <good|marginal|poor>
  # village = 500–2,000 residents (per corpus/program/SCALES.md)
  town: <good|marginal|poor>
  # town = 2,000–15,000 residents
  small_city: <good|marginal|poor>
  # small_city = 15,000–75,000 residents

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:
  # Two conditional sub-blocks. Each is required when the corresponding
  # lens_fit value is `good` or `marginal`. A label without a governance
  # sketch is romantic shorthand; these blocks force the author to earn the label.

  cooperative:
    # CONDITIONAL — required when lens_fit.cooperative is `good` or `marginal`.
    # A `cooperative: good` entry without this block is a P1 E-2 finding.

    membership_boundary: <string>
    # Who may join, on what terms, and at what geographic or demographic scope.
    # Example: "Town residents + surrounding township, paid annual dues"

    rules_source: <string>
    # How the cooperative's operating rules are set and changed.
    # Example: "Bylaws; member vote to amend with 2/3 majority"

    monitoring: <string>
    # How usage and compliance are observed and recorded.
    # Example: "Equipment usage logged per session; monthly audit by elected steward"

    graduated_sanctions: <string>
    # Ordered sequence of consequences for rule violations (Ostrom Principle 5).
    # Example: "Warning → $50 fine → 30-day suspension → membership review"

    conflict_resolution: <string>
    # Mechanism for resolving member disputes (Ostrom Principle 6).
    # Example: "Member-elected steward arbitrates; appeal to full member vote"

    ostrom_principles_addressed: [<integer>, ...]
    # List of Ostrom design-principle numbers (1–8) this governance structure
    # satisfies. Non-addressed principles must be explained in Known Risks.
    # Example: [1, 2, 3, 4, 5, 6]

  civic:
    # CONDITIONAL — required when lens_fit.civic is `good` or `marginal`.
    # A `civic: good` entry without this block is a P1 E-2 finding.

    political_coalition: <string>
    # Named stakeholders whose support is required for approval and funding.
    # Example: "Municipal workforce-development grant + small-business allies"

    council_vote_estimate: <string>
    # Estimated vote margin and main opposition argument.
    # Example: "5-2 favorable; opposition argues tax burden"

    competes_with_private: <string>
    # Relationship to any existing private operators in the same trade.
    # A civic facility that displaces a functioning private operator requires
    # explicit justification. Required (Principle 4).
    # Example: "No existing private smith in target towns; civic facility fills gap"

    governance_form: <string>
    # Ownership and management structure.
    # Example: "Municipally owned; operated by contracted master smith with apprentice program"

    budget_line: <string>
    # How capital and operating costs are funded in the municipal budget.
    # Example: "Capital via 25-year bond; operations under workforce-development or parks-and-rec line"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  # Flat numeric block. All values must be traceable to cited sources or
  # derivable from fields above. E-3 cross-checks these fields against each
  # other and against economics.* and throughput.*.

  cost_mean: <number>
  # Central capital cost estimate. Must equal economics.capital_cost.mid.

  cost_sd: <number>
  # Standard deviation of capital cost for Monte Carlo runs.
  # Derivable from (capital_cost.high - capital_cost.low) / 4 as a default.

  throughput_units_equiv_per_year: <number>
  # Annual throughput in a trade-canonical unit equivalent.
  # E-3 cross-check: approximately equals
  #   max_active_hours_per_week × 52 × (1 - downtime_fraction) × units_per_hour_equiv

  variable_cost_per_unit: <number>
  # Direct cost (materials + energy) per throughput unit equivalent.

  labor_hours_per_unit: <number>
  # Operator hours consumed per throughput unit equivalent.
  # E-3 cross-check: throughput_units_equiv_per_year × labor_hours_per_unit
  #   ≈ max_active_hours_per_week × 52 × (1 - downtime_fraction)

  downtime_fraction: <number>
  # Fraction of scheduled hours lost to maintenance, failure, or setup.
  # Range: 0.0–1.0. Must be consistent with operations_reality failure data.

  lifespan_years: <number>
  # Expected equipment service life in years under normal maintenance.
  # Drives civic-lens amortisation calculation.

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  # 9-cell evaluation matrix. Populated by Tier A simulation; start null.
  # Do not manually edit; values are overwritten by simulation output.
  village_market:    null
  village_coop:      null
  village_civic:     null
  town_market:       null
  town_coop:         null
  town_civic:        null
  small_city_market: null
  small_city_coop:   null
  small_city_civic:  null

# ── SOURCES ──────────────────────────────────────────────────────────────────

sources:
  # List of all cited sources for this entry. Every economic number, every
  # historical claim, every sim_params value must trace to an entry here.
  # Uncited numbers are P1 E-1 findings.
  - ref: <string>
    # Full citation string. Format: "Author YEAR, Journal/Publisher"
    # or URL with access date for online sources.
---
```

### 3.2 Complete Example Entry (forge-003)

The following is the canonical example from spec v0.2 Section 5. It demonstrates every
field in a populated state and is used as the reference implementation for new entries.

```yaml
---
id: forge-003
trade: smithing
name: Shared Tool-Library Coal Forge (medium footprint)
tagline: Community-owned coal forge with member-booked shifts
status: draft
version: 0.2
supersedes: null
inspirations: [medieval-european-village-forge, edo-blacksmith-cooperative]

footprint_m2: 35
ceiling_min_m: 3.5
ventilation: mechanical-extraction-required

energy_source: coal
energy_consumption_per_active_hour: 8 kg coal
backup_fuel: propane

throughput:
  units_per_hour: { small_work: 6, medium_work: 2, large_work: 0.5 }
  max_active_hours_per_week: 45

operator_skill_floor: journeyman
operators_concurrent: 1-2
apprentice_friendly: true

economics:
  currency: USD
  capital_cost: { low: 18000, mid: 28000, high: 45000 }
  install_cost: 6000
  annual_maintenance: 1500
  annual_consumables: 4200
  floor_space_rent_per_year: 4800
  market_price_per_unit: { low: 32, mid: 45, high: 70 }
  pricing_notes: "Per small-work unit equivalent. Premium over industrial baseline (~$12) assumes direct-to-consumer and repair-work mix. Cited."

operations_reality:
  first_year_failures:
    - item: "Primary coil / heating element"
      estimated_hours_to_failure: 1800
      replacement_cost: 1200
      replacement_lead_time_days: 21
    - item: "Refractory lining (partial)"
      estimated_hours_to_failure: 2400
      replacement_cost: 400
      replacement_lead_time_days: 7
  consumables_lead_time_days: { typical: 5, worst: 30 }
  throughput_variance:
    seasonal: "Fall/winter peak for repair work; summer trough"
    worst_month_fraction_of_average: 0.45
    best_month_fraction_of_average: 1.65
  operator_impact:
    noise_db: 85
    heat_exposure: "High near forge; adequate ventilation required"
    emissions: "Particulate, CO, small amounts of SOx with coal; zero with induction"
    physical_demand: "Moderate-heavy lifting; sustained standing"

regulatory_notes:
  zoning: "Light-industrial or mixed-use; coal restricted in many urban cores"
  emissions: "Particulate capture may be required above certain throughput"
  other: "OSHA ventilation standards for hot-work; check local fire code"

lens_fit:      { market: marginal, cooperative: good, civic: good }
scale_fit:     { village: marginal, town: good, small_city: good }

lens_context:
  cooperative:
    membership_boundary: "Town residents + surrounding township, paid annual dues"
    rules_source: "Bylaws; member vote to amend with 2/3 majority"
    monitoring: "Equipment usage logged per session; monthly audit by elected steward"
    graduated_sanctions: "Warning → $50 fine → 30-day suspension → membership review"
    conflict_resolution: "Member-elected steward arbitrates; appeal to full member vote"
    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6]
  civic:
    political_coalition: "Municipal workforce-development grant + small-business allies"
    council_vote_estimate: "5-2 favorable; opposition argues tax burden"
    competes_with_private: "No existing private smith in target towns; civic facility fills gap"
    governance_form: "Municipally owned; operated by contracted master smith with apprentice program"
    budget_line: "Capital via 25-year bond; operations under workforce-development or parks-and-rec line"

sim_params:
  cost_mean: 28000
  cost_sd: 8000
  throughput_units_equiv_per_year: 2400
  variable_cost_per_unit: 3.1
  labor_hours_per_unit: 0.6
  downtime_fraction: 0.12
  lifespan_years: 25

results:
  village_market:    null
  village_coop:      null
  village_civic:     null
  town_market:       null
  town_coop:         null
  town_civic:        null
  small_city_market: null
  small_city_coop:   null
  small_city_civic:  null

sources:
  - ref: "Weisdorf 2018, Economic History Review"
  - ref: "ToolLibrary.org 2024 capex survey"
---
```

---

## 4. Required vs Optional Fields

The table below is the authoritative gate reference for E-1, E-2, and E-3. "Conditional"
means the field is as binding as Required when its trigger condition is met; absence under
that condition is a P1 E-2 finding.

| Field | Level | Trigger (for conditional) |
|---|---|---|
| `id` | Required | — |
| `trade` | Required | — |
| `name` | Required | — |
| `tagline` | Required | — |
| `status` | Required | — |
| `version` | Required | — |
| `supersedes` | Required | — (null is a valid value) |
| `inspirations` | Required | — (empty list `[]` permitted if no precedents) |
| `footprint_m2` | Required | — |
| `ceiling_min_m` | Required | — |
| `ventilation` | Required | — |
| `energy_source` | Required | — |
| `energy_consumption_per_active_hour` | Required | — |
| `backup_fuel` | Required | — (null is a valid value) |
| `throughput` | Required | — (contents defined in trade SCHEMA.md) |
| `throughput.max_active_hours_per_week` | Required | — (always present in trade sub-structure) |
| `operator_skill_floor` | Required | — |
| `operators_concurrent` | Required | — |
| `apprentice_friendly` | Required | — |
| `economics` | Required | — |
| `economics.currency` | Required | — |
| `economics.capital_cost` | Required | — |
| `economics.install_cost` | Required | — |
| `economics.annual_maintenance` | Required | — |
| `economics.annual_consumables` | Required | — |
| `economics.floor_space_rent_per_year` | Required | — |
| `economics.market_price_per_unit` | Conditional | `lens_fit.market` is `good` or `marginal` |
| `economics.pricing_notes` | Conditional | `economics.market_price_per_unit` is present |
| `operations_reality` | Conditional | Any `lens_fit` value is `good` or `marginal` |
| `operations_reality.first_year_failures` | Conditional | `operations_reality` is required; minimum two items |
| `operations_reality.consumables_lead_time_days` | Conditional | `operations_reality` is required |
| `operations_reality.consumables_lead_time_days.worst` | Conditional | `operations_reality` is required |
| `operations_reality.throughput_variance` | Conditional | `operations_reality` is required |
| `operations_reality.throughput_variance.worst_month_fraction_of_average` | Conditional | `operations_reality` is required |
| `operations_reality.throughput_variance.best_month_fraction_of_average` | Conditional | `operations_reality` is required |
| `operations_reality.operator_impact` | Conditional | `operations_reality` is required |
| `operations_reality.operator_impact.noise_db` | Conditional | `operations_reality` is required |
| `operations_reality.operator_impact.heat_exposure` | Conditional | `operations_reality` is required |
| `operations_reality.operator_impact.emissions` | Conditional | `operations_reality` is required |
| `operations_reality.operator_impact.physical_demand` | Conditional | `operations_reality` is required |
| `regulatory_notes` | Required | — |
| `regulatory_notes.zoning` | Required | — |
| `regulatory_notes.emissions` | Required | — |
| `regulatory_notes.other` | Required | — |
| `lens_fit` | Required | — |
| `lens_fit.market` | Required | — |
| `lens_fit.cooperative` | Required | — |
| `lens_fit.civic` | Required | — |
| `scale_fit` | Required | — |
| `scale_fit.village` | Required | — |
| `scale_fit.town` | Required | — |
| `scale_fit.small_city` | Required | — |
| `lens_context.cooperative` | Conditional | `lens_fit.cooperative` is `good` or `marginal` |
| `lens_context.cooperative.membership_boundary` | Conditional | `lens_context.cooperative` is required |
| `lens_context.cooperative.rules_source` | Conditional | `lens_context.cooperative` is required |
| `lens_context.cooperative.monitoring` | Conditional | `lens_context.cooperative` is required |
| `lens_context.cooperative.graduated_sanctions` | Conditional | `lens_context.cooperative` is required |
| `lens_context.cooperative.conflict_resolution` | Conditional | `lens_context.cooperative` is required |
| `lens_context.cooperative.ostrom_principles_addressed` | Conditional | `lens_context.cooperative` is required |
| `lens_context.civic` | Conditional | `lens_fit.civic` is `good` or `marginal` |
| `lens_context.civic.political_coalition` | Conditional | `lens_context.civic` is required |
| `lens_context.civic.council_vote_estimate` | Conditional | `lens_context.civic` is required |
| `lens_context.civic.competes_with_private` | Conditional | `lens_context.civic` is required |
| `lens_context.civic.governance_form` | Conditional | `lens_context.civic` is required |
| `lens_context.civic.budget_line` | Conditional | `lens_context.civic` is required |
| `sim_params` | Required | — |
| `sim_params.cost_mean` | Required | — |
| `sim_params.cost_sd` | Required | — |
| `sim_params.throughput_units_equiv_per_year` | Required | — |
| `sim_params.variable_cost_per_unit` | Required | — |
| `sim_params.labor_hours_per_unit` | Required | — |
| `sim_params.downtime_fraction` | Required | — |
| `sim_params.lifespan_years` | Required | — |
| `results` (block, all 9 cells) | Required | — (cells start null; populated by Tier A sim) |
| `sources` | Required | — (at minimum one entry per cited number) |

---

## 5. Prose Sections

Every entry must contain the following six prose sections in this order. One paragraph is
the target length for each; longer is acceptable when substance demands it, but prose
sections must not substitute for frontmatter fields. Simulation code does not read prose.

### Summary
Who this equipment design is, who it is for, and why it exists as a distinct entry in the
catalog. Not a recapitulation of frontmatter fields — a human-facing orientation.

### Design rationale
The specific problem this entry solves that no other entry in the same trade's catalog
solves. Justifies the entry's existence as distinct rather than a variant of an existing
one. Generic rationale ("this entry explores a coal-fired forge") is insufficient and
constitutes a P2 E-2 finding. Required by Principle 7.

### Historical lineage
Historical forms and modern precedents that informed the design. Must explain *functional*
inheritance (what the modern design carries forward in terms of capability, economics, or
operational form), not aesthetic similarity. Labor regimes, supply-chain conditions, and
property structures that made the historical form viable must be named; those that cannot
be reproduced in modern form must be acknowledged. Required by Principle 6.

### Key assumptions
Where the economic numbers come from. Which estimates are solid (derived from published
data), which are rough (order-of-magnitude), and which rest on contested premises.
Connects frontmatter fields to the `sources:` block.

### Known risks / failure modes
Explicitly names at least one failure mode in each of three categories: (1) regulatory
(zoning, emissions, licensing), (2) labour pipeline (succession, skill scarcity, apprentice
path), (3) supply chain (input availability, lead time, single-supplier dependencies). An
entry with `apprentice_friendly: false` must name the succession risk here. Required by
Principle 8.

### Iteration log
Dated entries recording design decisions and revisions. At least one entry required. Add
entries on revision; never overwrite prior entries. Required by Principle 10. Format:

```
- YYYY-MM-DD: [Summary of change or initial creation note]
```

---

## 6. Field Semantics

Definitions for fields whose meaning is not fully self-evident from their name.

| Field | Definition |
|---|---|
| `status: superseded` | Entry has been replaced by a newer design. The entry remains in the catalog, marked superseded, with `supersedes` pointing to it from the replacement. Superseded entries are excluded from playbook recommendations but remain in the evaluation record. |
| `inspirations` | Functional precedents, not aesthetic references. Each entry must map to a prose explanation in Historical Lineage. An inspiration with no functional explanation is a P3 E-1 finding. |
| `footprint_m2` | Working zone only. Excludes storage, customer space, and shared circulation. The number that drives lease-size and zoning analysis. |
| `energy_consumption_per_active_hour` | At full operational load. Does not include idle consumption or warm-up. Drives annual_consumables calculation for fuel-source entries. |
| `operator_skill_floor` | The minimum competence at which a real operator can run the equipment safely and productively without direct supervision. Not the ideal skill level — the floor. |
| `economics.capital_cost.mid` | The central estimate used in `sim_params.cost_mean`. If mid is not the arithmetic mean of low and high, the asymmetry should be explained in Key Assumptions. |
| `economics.floor_space_rent_per_year` | Imputed at local commercial rate even if the space is owned. This keeps cost comparisons between owner-operators and renters consistent across the evaluation matrix. |
| `economics.market_price_per_unit` | The price at which the output sells in the market — not a cost-plus derivation, not a break-even price. It is a claim about what real customers will pay, and it must be argued with evidence. |
| `economics.pricing_notes` | Must name the industrial-competitor baseline price and the customer segment that pays the premium. A pricing note that does not name the baseline is insufficient (Principle 5). |
| `operations_reality.first_year_failures` | Components expected to fail or need partial replacement within the first 12 months of operation under normal use. Not every conceivable failure — the two or three most predictable ones based on cited service data. |
| `operations_reality.consumables_lead_time_days.worst` | Not theoretical maximum — the 95th-percentile scenario or a documented supply-chain stress case (e.g., single supplier, overseas shipping). |
| `operations_reality.throughput_variance.worst_month_fraction_of_average` | Fraction relative to the monthly average implied by `throughput_units_equiv_per_year / 12`. A value of 0.45 means the worst month yields 45% of that average. |
| `lens_fit` | Author's prospective assessment of fitness before simulation runs. Not a simulation output. The simulation may confirm, contradict, or refine the author's label; discrepancies should be logged in the Iteration Log. |
| `scale_fit` | Same prospective nature as `lens_fit`. The Tier A simulation may assign `marginal` where the author claimed `good`; that is a finding, not a schema error. |
| `lens_context.cooperative.ostrom_principles_addressed` | Ostrom's eight design principles (Governing the Commons, 1990). Non-addressed principles signal governance gaps. Principles 7 (nested organisations) and 8 (external recognition) are often not applicable at single-cooperative scale; NA at that scale is acceptable and should be noted. |
| `lens_context.civic.competes_with_private` | Analyzes whether a civic facility displaces an existing functioning private operator. "No existing private operator" and "existing private operator; civic fills a gap they cannot" are both acceptable answers; silence is not. |
| `sim_params.cost_mean` | Must equal `economics.capital_cost.mid`. Discrepancy is a P1 E-3 finding. |
| `sim_params.downtime_fraction` | Must be consistent with the `operations_reality` failure profile. A `downtime_fraction` of 0.05 with two first-year failures totaling 4+ weeks of lead time is internally inconsistent. |
| `results` | All nine cells start null. Values written by Tier A simulation only. An entry with `status: validated` must have all nine cells populated. An entry with `status: reviewed` may have some or all cells as null (simulation has not yet run). |
| `sources` | Each `ref` entry should include enough information to locate the source: Author, Year, Publisher/Journal for formal works; URL + access date for online resources. Sources are not annotated in this block — annotation belongs in the prose. |

---

## 7. Validation Rules

The following rules are enforced by the editorial gate system. Errors listed below are
P1 findings unless noted; P1 findings block promotion.

### E-1 Citation Auditor checks (citation completeness)

| Rule ID | Rule | Severity |
|---|---|---|
| E1-R1 | Every field in `economics.*` (including `market_price_per_unit` when present) traces to a `sources:` entry. | P1 |
| E1-R2 | Every field in `sim_params.*` traces to a `sources:` entry or is derivable from cited fields above with the derivation stated in Key Assumptions. | P1 |
| E1-R3 | Every historical claim in prose traces to a `sources:` entry. | P1 |
| E1-R4 | `market_price_per_unit`, when present, must be explicitly cited (not a residual from sim_params arithmetic). Uncited market price is a P1 finding regardless of other citations. | P1 |
| E1-R5 | `sources:` entries must be real, findable, and appropriate to the claim made. A source that does not exist or does not support the specific claim is worse than no source. | P1 |
| E1-R6 | `inspirations` entries used in prose must each have a traceable source. | P2 |

### E-2 Scope Keeper checks (schema compliance and scope)

| Rule ID | Rule | Severity |
|---|---|---|
| E2-R1 | All Required fields in Section 4 are present and non-null (except `supersedes` and `backup_fuel`, which accept null as a valid value). | P1 |
| E2-R2 | All Conditional fields are present when their trigger condition is met. | P1 |
| E2-R3 | No fields are invented outside this schema. Trade-specific extensions must be documented in `catalog/<trade>/SCHEMA.md` under the `trade_specific:` namespace. | P1 |
| E2-R4 | `operations_reality` is present whenever any `lens_fit` value is `good` or `marginal`. | P1 |
| E2-R5 | `lens_context.cooperative` is present whenever `lens_fit.cooperative` is `good` or `marginal`. | P1 |
| E2-R6 | `lens_context.civic` is present whenever `lens_fit.civic` is `good` or `marginal`. | P1 |
| E2-R7 | `status: validated` is not claimed while any Required or triggered Conditional field is absent or contains a placeholder (`TBD`, `todo`, etc.). | P1 |
| E2-R8 | `version` is greater than `0.1` only if the Iteration Log records at least one revision beyond the initial creation entry. | P2 |
| E2-R9 | `supersedes` is non-null only if the Iteration Log records the reason for superseding the predecessor. | P2 |
| E2-R10 | Prose sections do not substitute for frontmatter fields. Economic data in prose that is absent from frontmatter is a scope violation. | P2 |

### E-3 Numeracy Checker checks (internal arithmetic consistency)

| Rule ID | Rule | Severity |
|---|---|---|
| E3-R1 | `sim_params.cost_mean` equals `economics.capital_cost.mid`. | P1 |
| E3-R2 | `sim_params.throughput_units_equiv_per_year` is approximately consistent with `throughput.max_active_hours_per_week × 52 × (1 − downtime_fraction) × units_per_hour_equiv`. Order-of-magnitude discrepancy is P1; within-order discrepancy is P2. | P1/P2 |
| E3-R3 | `throughput_units_equiv_per_year × labor_hours_per_unit` approximately equals `max_active_hours_per_week × 52 × (1 − downtime_fraction)`. | P2 |
| E3-R4 | The payback period implied by `(cost_mean + install_cost) / annual_net_revenue` is consistent with what `pricing_notes` implies. Inconsistency between stated market price and sim_params-implied payback is P1. | P1 |
| E3-R5 | `sim_params.cost_sd` is within plausible range relative to `cost_mean` (typically `cost_sd / cost_mean` between 0.15 and 0.50 for uncertain capital estimates). | P2 |
| E3-R6 | `sim_params.downtime_fraction` is consistent with the `operations_reality.first_year_failures` profile. A low downtime fraction with high-severity first-year failures is internally inconsistent. | P2 |
| E3-R7 | If the entry has `results:` cells populated, cells must be internally consistent across scales and lenses (e.g., if `village_market: fail` and `small_city_market: win`, `town_market` should not be `fail` without explanation). | P2 |
| E3-R8 | All monetary values in the same entry use the same currency (the one declared in `economics.currency`). Cross-currency mixing is P1. | P1 |

---

## 8. Extending per Trade

Trade-specific fields that do not generalise across trades go under the `trade_specific:`
top-level key in the YAML frontmatter. They are documented in `catalog/<trade>/SCHEMA.md`,
which inherits the full base schema (this file) and adds the trade extension.

**Conventions:**

- The `throughput:` block's internal structure is the primary per-trade extension point.
  Contents of `throughput:` (beyond the required `max_active_hours_per_week` sub-field) are
  defined in `catalog/<trade>/SCHEMA.md`.
- Any additional fields added in `catalog/<trade>/SCHEMA.md` must be under `trade_specific:`
  and must not shadow or redefine any base-schema field name.
- Trade SCHEMA.md files must open with a line declaring their base:
  `Base schema: catalog/SCHEMA.md v<version>`
- A field added in a trade schema that proves useful across multiple trades is a candidate
  for promotion to this base schema via a formal amendment (bump this schema's version;
  update spec Section 5; re-validate affected entries).

**Example trade extension (smithing):**

```yaml
# In frontmatter of a smithing entry:
throughput:
  units_per_hour: { small_work: 6, medium_work: 2, large_work: 0.5 }
  max_active_hours_per_week: 45

trade_specific:
  heat_range_celsius: { min: 800, max: 1300 }
  anvil_weight_kg: 150
```

See `catalog/smithing/SCHEMA.md` for the full smithing extension. *(Not yet created;
created in Plan C when the smithing vertical slice reaches catalog-entry authoring.)*

---

## 9. Versioning

**This schema is versioned.** The current version is **1.0** (declared at the top of this
file).

**When this schema changes:**

1. Bump the version number at the top of this file.
2. File a corresponding amendment to `specs/2026-04-18-ceres-design.md` Section 5. The
   spec and this schema are kept in lock-step; divergence is a P1 E-2 finding against
   the schema itself.
3. Update `catalog/<trade>/SCHEMA.md` files that inherit this base schema to declare the
   new version in their `Base schema:` line.
4. Re-validate every existing entry against the new schema. An entry valid under the prior
   version may fail under the new one; failed entries must be updated or explicitly
   grandfathered with a dated note in their Iteration Log.
5. Record the schema change in the Iteration Log of this file:

**Schema iteration log:**

- 2026-04-18: v1.0 — initial canonical schema created, matching spec v0.2 Section 5.
  Includes v0.2 additions: `economics.market_price_per_unit`, `economics.pricing_notes`,
  `operations_reality` block, `lens_context.cooperative` block, `lens_context.civic` block.
