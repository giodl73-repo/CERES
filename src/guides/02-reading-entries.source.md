# Reading a Catalog Entry

A catalog entry is a single Markdown file with YAML frontmatter followed by
prose sections. The YAML is machine-readable; the prose is human-readable.
Both are required. The simulation engine ingests the YAML; reviewers read
the prose.

---

## File location and naming

```
catalog/<trade>/entries/<NNN>-<slug>.md
```

Examples: `catalog/baking/entries/001-sourdough-artisan-micro.md`,
`catalog/smithing/entries/003-community-forge-town.md`.

The three-digit prefix preserves ordering without encoding meaning. Slugs
should be descriptive, not redundant with the trade prefix.

---

## YAML frontmatter structure

The canonical field list lives in `catalog/SCHEMA.md`. Trade-specific
extensions live in `catalog/<trade>/SCHEMA.md`. The sections below summarize
each block.

### Identity

```yaml
id: bake-001
trade: baking
name: "Sourdough Artisan Micro-bakery (electric deck, village/town scale)"
tagline: "Single-operator naturally-leavened bread bakery with premium DTC pricing"
status: draft
version: "0.1"
supersedes: null
```

`id` is `<trade-prefix>-<NNN>`. `status` follows the lifecycle below.
`supersedes` links to the id of the entry this one replaces.

### Physical envelope

```yaml
footprint_m2: 25
ceiling_min_m: 2.5
ventilation: kitchen-exhaust-hood-required
```

Physical constraints that determine whether the design fits a specific site.
Every field must carry an inline comment explaining the derivation and a
`[CITATION-NEEDED: ...]` tag if the value is inferred rather than sourced.

### Energy

```yaml
energy_source: electric-deck
energy_consumption_per_active_hour: "5.5 kWh"
backup_fuel: null
```

Primary energy source and consumption. Trade-specific schemas define allowed
`energy_source` values. Do not invent new values without amending the schema.

### Throughput

```yaml
throughput:
  loaves_per_day: 115
  batches_per_day: 2
  max_active_hours_per_week: 35
  throughput_variance:
    worst_month_fraction_of_average: 0.65
    best_month_fraction_of_average: 1.30
```

The throughput block drives `sim_params.throughput_units_equiv_per_year`.
The derivation must be written explicitly in the `sim_params` comments and
cross-checked by E-3.

### Operator profile

```yaml
operator_skill_floor: journeyman-baker
operators_concurrent: "1"
apprentice_friendly: true
apprentice_path:
  time_to_independent_operation: "~36-42 months"
```

Skill floor must match the operations the entry actually requires. See
`catalog/<trade>/SCHEMA.md §3` for allowed skill-level values and their
definitions. The apprentice path documents how skill transmission works,
which is part of the viability claim.

### Economics

```yaml
economics:
  currency: USD
  capital_cost: { low: 18000, mid: 32000, high: 55000 }
  install_cost: 4000
  annual_maintenance: 1200
  annual_consumables: 8500
  floor_space_rent_per_year: 3000
  market_price_per_unit: { low: 5, mid: 8, high: 12 }
  industrial_baseline_price: 3
```

All monetary values use the declared `currency`. Low/mid/high triples represent
the range; simulations default to `mid`. `install_cost` is a single estimate.
Every dollar figure carries a comment explaining the derivation.

```proof:callout kind=warning label="Citation policy"
Every cost figure must carry a [CITATION-NEEDED: ...] tag until it is
sourced. Unsourced figures block promotion to `validated`. The tag should
name the specific data source that would verify the figure (e.g., a vendor
category, a BLS survey, a trade association report).
```

### Simulation parameters

```yaml
sim_params:
  cost_mean: 32000
  cost_sd: 9250
  throughput_units_equiv_per_year: 29500
  variable_cost_per_unit: 0.33
  labor_hours_per_unit: 0.056
  downtime_fraction: 0.10
  lifespan_years: 15
```

These are the inputs the simulation engine consumes directly. Every value must
be derivable from the fields above it; the derivation is written as an inline
comment. E-3 cross-checks `throughput_units_equiv_per_year` against
`max_active_hours_per_week` and `labor_hours_per_unit` against total annual
hours.

**Standard derivations:**

```
throughput_units_equiv_per_year =
  loaves_per_day × operating_days_per_year × (1 − downtime_fraction)

cost_sd = (capital_cost.high − capital_cost.low) ÷ 4
```

### Results block

```yaml
results:
  village_market:
    verdict: win
    primary_metric: 0.19
    metric_name: payback_years
    notes: ''
  village_coop:
    verdict: fail
    primary_metric: 76.0
    metric_name: break_even_members
    notes: "feasible_pool=31.2, break_even=76, total_annual_cost=15100"
  town_market:
    verdict: win
    ...
```

Nine cells: three scales × three lenses. Each cell has a `verdict`, a
`primary_metric`, a `metric_name`, and optional `notes`. The results block is
populated by the Tier A simulation run; authors do not fill it manually.

---

## The nine-cell grid

```proof:tree kind=org
Results grid (3 × 3)
- village_market: payback_years ≤ 8 AND operator take-home ≥ $48k/yr
- village_coop: break_even_members ≤ feasible pool (25 at village midpoint)
- village_civic: per_household_cost ≤ $120/hh/yr AND usage rate ≥ 2 hr/capita
- town_market: payback_years ≤ 8 AND operator take-home ≥ $56k/yr
- town_coop: break_even_members ≤ feasible pool (188 at town midpoint)
- town_civic: per_household_cost ≤ $100/hh/yr AND usage rate ≥ 2 hr/capita
- small_city_market: payback_years ≤ 8 AND operator take-home ≥ $62k/yr
- small_city_coop: break_even_members ≤ feasible pool (800 at small-city midpoint)
- small_city_civic: per_household_cost ≤ $80/hh/yr AND usage rate ≥ 2 hr/capita
```

Verdicts: `win` (passes with ≥20% margin), `marginal` (passes narrowly or under
optimistic inputs), `fail` (does not pass under any reasonable scenario).

---

## Interpreting verdicts

A `win` in `town_market` means a private operator can recover capital in under
6.4 years and clear the $56,000 median wage threshold at town scale. That is the
most favorable ownership form for this design at this scale.

A `fail` in `village_coop` does not mean the design is bad; it means the
cooperative form does not close at village scale. The design may still `win` in
`town_market`.

Read the `notes` field on `fail` cells: it records the actual numbers (e.g.,
`break_even=76, feasible_pool=31.2`) so the reader understands how far the design
falls short, and whether a modest design change could flip the verdict.

---

## Status lifecycle

| Status | Meaning |
|--------|---------|
| `draft` | Author-submitted; panel review has not cleared it |
| `reviewed` | Panel R1 findings addressed; structurally sound; editorial not yet run |
| `validated` | Editorial all-3-pass cleared; results block populated |
| `held` | Editorial found P1 issues; blocked pending fix |
| `deprecated` | Superseded or falsified; retained in catalog for record |

Movement is earned, not assumed. An entry does not advance to `reviewed` just
because time has passed.

---

## Prose sections

After the YAML closing `---`, every entry has these prose sections:

| Section | Purpose |
|---------|---------|
| `## Summary` | Two-paragraph narrative: what this design is, what the economics show |
| `## Design rationale` | Why this specific design point exists in the catalog |
| `## Historical lineage` | Which historical forms informed this design — with anti-romantic treatment |
| `## Key assumptions` | Explicit statement of the biggest load-bearing assumptions, especially those labeled `inferred` |
| `## Operations reality` | What running this looks like day-to-day; maintenance schedule |
| `## Known risks / failure modes` | What can go wrong and why |
| `## Target niche` | Who this design serves and under what conditions |
| `## Iteration log` | Version history with dates |

The historical lineage section must not romanticize. Historical forms supply
functional requirements; they do not supply economic instruction. A frontier
bakery was household subsistence production on unpaid family labor — not a model
for a modern artisan business.

---

## Trade-specific fields

Each trade extends the base schema with trade-specific fields under
`trade_specific:`. For baking, this includes `flour_source_declaration`. For
smithing, it includes fuel type and bellows configuration. Read
`catalog/<trade>/SCHEMA.md` before authoring to know which fields are required
and what values are allowed.

Do not invent new `trade_specific` fields without amending `catalog/<trade>/SCHEMA.md`.
Silent additions break the simulation ingestion pipeline.
