---
id: plan-c-catalog-smithing
name: Catalog — Smithing Vertical Slice (15 Forge Entries)
description: Author 15 forge catalog entries spanning repair, specialty, and shared/civic niches per DECLINE-VERDICT; each entry schema-complete and ready for Tier A simulation
status: draft
version: "1.0"
created: 2026-04-19
phase: 2
subsystem: catalog
trade: smithing
depends_on: [plan-a-scaffolding, plan-b-research-smithing]
blocks: [plan-e-playbook]
estimated_effort: 3-5 weeks focused, 6-10 weeks part-time
primary_artifact_type: catalog
success_signal: >
  15 forge catalog entries at `catalog/smithing/entries/*.md`, each with
  schema-compliant frontmatter and all conditional fields populated for
  claimed lens and scale fits. Every cost and throughput number cites a
  source or carries a bracketed placeholder. Entries span repair / specialty
  / shared-civic niches per DECLINE-VERDICT.md guidance. The 15 entries
  span the 9-cell context matrix meaningfully — every cell has at least
  one entry claiming `good` or `marginal` fit. Catalog is ready for
  ceres-panel R1 review and Plan D Tier A simulation.
spec: specs/2026-04-18-ceres-design.md
---

# Plan C: Catalog — Smithing Vertical Slice (15 Forge Entries)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans.

**Goal:** Produce the 15-forge catalog that is CERES's creative core and the primary evidence body for Phase 4 simulation and Phase 5 playbook.

**Architecture:** Design-heavy authoring plan. Each entry = one markdown file with substantial YAML frontmatter (per `catalog/SCHEMA.md` v1.1 canonical schema) + prose sections. Entries must span the design space enough that Tier A simulation produces meaningful variance across 9 context cells (3 scales × 3 lenses).

**Tech Stack:** Markdown + YAML. No code in this plan (code starts in Plan D).

**Source of truth:**
- `specs/2026-04-18-ceres-design.md` v0.3 §5 — schema authority
- `catalog/SCHEMA.md` — canonical implementation of schema
- `research/trades/smithing/REQUIREMENTS.md` — functional requirements (R-01 through R-24)
- `research/trades/smithing/DECLINE-VERDICT.md` — niche targeting (repair + specialty + shared/civic; NOT commodity competition)
- `research/trades/smithing/HISTORICAL-FORMS.md` — inspirations + bellows / fuel / org-form variation
- `corpus/program/SCALES.md` — wage/civic/member-pool thresholds
- `corpus/program/CURRENCIES.md` — FX normalization
- `corpus/canon/PRINCIPLES.md` — the 10 principles (Plan C entries must honor these)

**Citation policy:** Same as Plan B — `[CITATION-NEEDED: <claim>]` for numbers where model confidence is low. Verified citations inherited from REQUIREMENTS and prior chapters are acceptable. DO NOT fabricate supplier quotes or manufacturer data — use illustrative estimates with explicit "illustrative" labels.

**Style:** STYLE-GUIDE.md §7 voice: "neutral technical" for catalog entries. No marketing language. No romantic framing.

**Commit cadence:** One commit per task. Each entry is a task; each task is a commit. History of 15 separate commits = 15 independent review objects for ceres-panel later.

---

## The 15-Entry Manifest

Per DECLINE-VERDICT.md §5 implications, the catalog targets restorable niches. The 15 entries distribute across four groups to give Tier A simulation meaningful variance:

### Group A — Repair-Focused (6 entries)

Smithing's most survivable historical niche. Location-bound demand; cannot be centralized.

1. **forge-005 — Frontier-Revival Coal Repair Shop** — single-operator coal forge, village/town, market-primary. Inspired by American frontier smith as last-mile service.
2. **forge-007 — Containerized Mobile Forge** — 20-ft intermodal container conversion, mobile-service model, village/rural routes. Farm-repair circuit. Market-primary.
3. **forge-012 — Farriery-Specialist Propane** — horseshoeing + hoof-care focus, rural/village, market-primary. Boutique equine clientele.
4. **forge-013 — Restoration-Specialist Heritage Shop** — historic-building restoration, architectural repair, small-city, market + civic good. Heritage-preservation clientele.
5. **forge-002 — Induction-Modular Small Repair** — modern induction-electric, compact, tool/implement repair, all scales, market-primary (repair commodity hardware priced as premium service).
6. **forge-014 — Electric-Induction Gig Repair Micro** — minimum-capital entry, part-time, village-only. Stress-test of "lowest possible capital to enter" scenario. Likely market-marginal.

### Group B — Specialty / Custom / Artistic (3 entries)

Low-volume, elastic demand, high margin. Per DECLINE-VERDICT: survives via premium-market segmentation.

7. **forge-006 — Induction Bladesmith / Cutlery** — chef-knife / outdoor-blade specialty, small-city, market + coop good. Direct-to-consumer premium.
8. **forge-010 — Architectural Ironwork Bespoke** — gates, railings, custom hardware, small-city, market-primary. Contractor + high-end residential market.
9. **forge-008 — Traditional Charcoal Village** — purist/historical-method shop. Village scale. Primary deliverable is the craft's preservation + limited specialty output; market-marginal. Tests "can traditional method itself be viable?"

### Group C — Shared / Civic / Coop (4 entries)

Per DECLINE-VERDICT: apprentice-training and civic externalities argue strongly for coop and civic lens viability where market struggles.

10. **forge-003 — Shared Tool-Library Coal** — member-booked shifts, medium footprint, town scale, coop-primary (the example entry from spec §5; canonical reference design).
11. **forge-004 — Community Civic Makerspace** — town-owned workshop, library-model access, town/small-city, civic-primary + coop-good. Training + repair + community making.
12. **forge-011 — Municipal Civic Training Forge** — public high-school / community-college partnership, small-city, civic-primary. Apprentice-pipeline builder.
13. **forge-015 — Tool-Library Member-Access Induction** — member-subscription induction workshop, town/city, coop-primary. Lower-capital shared-resource model than coal.

### Group D — Training / Apprentice / Cooperative-Training (2 entries)

These overlap Group C but are distinct enough in structure to deserve separate entries.

14. **forge-009 — Co-op Apprentice Training Forge** — formal apprentice-pipeline workshop, town/city, coop-primary + civic-marginal. Inspired by Mondragon + US rural electric coop traditions.
15. **forge-001 — Backyard Propane Compact** — minimum-footprint hobbyist / low-capital starter. Village scale only. Tests the "entry-level" cell of the matrix. Market/coop/civic all marginal or poor.

### Context-Matrix Coverage

The 15 entries collectively span the 9-cell matrix (3 scales × 3 lenses). Every cell has at least 2 entries claiming `good` or `marginal`. No cell is empty. Variance across entries enables Tier A simulation to produce meaningful winners and losers per cell.

---

## Task Index

| # | Task | Creates / Updates |
|---|---|---|
| 1 | Catalog manifest confirmation | `catalog/smithing/README.md` (expands + incorporates manifest) |
| 2 | Smithing-specific schema extension | `catalog/smithing/SCHEMA.md` (extends canonical `catalog/SCHEMA.md`) |
| 3 | Entry forge-001 Backyard Propane Compact | `catalog/smithing/entries/001-backyard-propane-compact.md` |
| 4 | Entry forge-002 Induction-Modular Small Repair | `catalog/smithing/entries/002-induction-modular-small-repair.md` |
| 5 | Entry forge-003 Shared Tool-Library Coal | `catalog/smithing/entries/003-shared-toollibrary-coal.md` |
| 6 | Entry forge-004 Community Civic Makerspace | `catalog/smithing/entries/004-community-civic-makerspace.md` |
| 7 | Entry forge-005 Frontier-Revival Coal Repair | `catalog/smithing/entries/005-frontier-revival-coal-repair.md` |
| 8 | Entry forge-006 Induction Bladesmith | `catalog/smithing/entries/006-induction-bladesmith.md` |
| 9 | Entry forge-007 Containerized Mobile Forge | `catalog/smithing/entries/007-containerized-mobile-forge.md` |
| 10 | Entry forge-008 Traditional Charcoal Village | `catalog/smithing/entries/008-traditional-charcoal-village.md` |
| 11 | Entry forge-009 Co-op Apprentice Training | `catalog/smithing/entries/009-coop-apprentice-training.md` |
| 12 | Entry forge-010 Architectural Ironwork Bespoke | `catalog/smithing/entries/010-architectural-ironwork-bespoke.md` |
| 13 | Entry forge-011 Municipal Civic Training | `catalog/smithing/entries/011-municipal-civic-training.md` |
| 14 | Entry forge-012 Farriery-Specialist Propane | `catalog/smithing/entries/012-farriery-specialist-propane.md` |
| 15 | Entry forge-013 Restoration-Specialist Heritage | `catalog/smithing/entries/013-restoration-specialist-heritage.md` |
| 16 | Entry forge-014 Electric-Induction Gig Repair Micro | `catalog/smithing/entries/014-electric-induction-gig-repair.md` |
| 17 | Entry forge-015 Tool-Library Member-Access Induction | `catalog/smithing/entries/015-toollibrary-member-induction.md` |
| 18 | Cross-entry audit | `reviews/CATALOG-AUDIT-plan-c.md` |
| 19 | Closeout | TRACKER, plans/README, Plan C frontmatter |

19 tasks total. Execution is naturally parallelizable in waves:
- Wave 1 (sequential): Tasks 1 + 2 (manifest + schema extension — everything downstream depends on these)
- Wave 2 (parallel × 3 batches): 5 entries per batch (Tasks 3-7, Tasks 8-12, Tasks 13-17)
- Wave 3 (sequential): Task 18 audit, then Task 19 closeout

---

## Task 1: Catalog Manifest / README

**Files:**
- Create: `catalog/smithing/README.md` (Plan A Task 2 created a stub; this expands it)

**Required content:**

1. **Frontmatter:**
```yaml
---
trade: smithing
doc_type: catalog-overview
version: "1.0"
status: draft
entry_count: 15
---
```

2. **Purpose** (~100 words) — what the smithing catalog is, who consumes it, relationship to REQUIREMENTS/HISTORICAL-FORMS/DECLINE-VERDICT.

3. **The 15-entry manifest** — the table above (Groups A/B/C/D) with entry IDs + names + one-line description each.

4. **Design-space coverage note** — briefly explain why these 15 and not others. Reference DECLINE-VERDICT niche targeting.

5. **Lens-fit and scale-fit distribution** — summary table showing how many entries target each (scale × lens) cell as `good`, `marginal`, or `poor`. Demonstrates the catalog spans the matrix.

6. **Entry status tracking** — small table: entry-id | status | last-modified. Populated as entries are authored.

7. **Sources** (pointers to REQUIREMENTS, HISTORICAL-FORMS, DECLINE-VERDICT, SOURCES).

**Commit:**
```bash
git add catalog/smithing/README.md
git commit -m "Plan C task 1: smithing catalog manifest (15-entry overview)"
```

---

## Task 2: Smithing-Specific Schema Extension

**Files:**
- Create: `catalog/smithing/SCHEMA.md`

Per `catalog/SCHEMA.md` v1.1 (canonical), trade-specific extensions live under `catalog/<trade>/SCHEMA.md`. This file documents the smithing-specific structure of the `throughput` block and any other smithing-only fields.

**Required content:**

1. **Frontmatter:**
```yaml
---
trade: smithing
doc_type: schema-extension
extends: catalog/SCHEMA.md
version: "1.0"
schema_base_version: "1.1"
---
```

2. **Purpose** — one paragraph. This file extends the canonical schema with smithing-specific detail. Must NOT contradict the base schema.

3. **Smithing `throughput` block structure:**
```yaml
throughput:
  units_per_hour:
    small_work: {integer}      # small items: nails, hooks, horseshoes, simple hardware
    medium_work: {integer}     # tools, brackets, chains, decorative items
    large_work: {integer}      # architectural pieces, bladesmithing, complex fabrication
  max_active_hours_per_week: {integer}
  product_mix:                 # optional but recommended
    repair: {percentage}
    commodity: {percentage}
    specialty: {percentage}
    artistic: {percentage}
  throughput_variance:
    worst_month_fraction_of_average: {decimal}
    best_month_fraction_of_average: {decimal}
    seasonal: {description}
```

4. **Smithing-specific energy sub-fields** for `energy_source`:
   - Allowed values: `coal`, `coke`, `charcoal`, `propane`, `natural-gas`, `induction-electric`, `hybrid-coal-propane`, `hybrid-induction-gas`.
   - Each value implies different throughput capabilities (per REQUIREMENTS R-08) — document the implication table.

5. **Smithing-specific operator_skill_floor enumeration:**
   - `apprentice` — entry-level smithing (cannot do forge welding solo)
   - `journeyman` — full-shop operation including forge welding, heat treatment
   - `master` — complex/artistic work; pattern welding; bladesmithing at professional tolerance
   - Maps to REQUIREMENTS R-13 through R-15.

6. **Smithing-specific `first_year_failures` common items** — a reference list Plan C authors populate from:
   - Primary coil / heating element (induction)
   - Refractory lining (coal/charcoal forges)
   - Bellows mechanism (traditional)
   - Anvil base settling / crack (all)
   - Ventilation blower / hood
   - Propane regulator (gas forges)
   - Hammer/power-hammer bearings (if equipped)
   
   Authors pick 2-4 per entry; numbers are illustrative.

7. **Per-niche notes** — for each of the 4 groups (Repair / Specialty / Shared-Civic / Training), one paragraph on what schema fields tend to matter most.

8. **Sources** — pointers to REQUIREMENTS.md sections.

**Commit:**
```bash
git add catalog/smithing/SCHEMA.md
git commit -m "Plan C task 2: smithing-specific schema extension"
```

---

## Tasks 3-17: Per-Entry Authoring (15 entries)

### Shared Structure Across All Entry Tasks

Each entry task creates one markdown file at `catalog/smithing/entries/{id-slug}.md`. Structure per `catalog/SCHEMA.md` v1.1.

**Required frontmatter (full schema per `catalog/SCHEMA.md`):**

```yaml
---
id: forge-{NNN}
trade: smithing
name: {human-readable name}
tagline: {one-line positioning}
status: draft
version: "1.0"
supersedes: null
inspirations: [{culture-slug-or-historical-form}, ...]

# Physical envelope (required)
footprint_m2: {integer}
ceiling_min_m: {decimal}
ventilation: {description}

# Energy (required)
energy_source: {allowed value from SCHEMA.md}
energy_consumption_per_active_hour: {value with units}
backup_fuel: {optional}

# Throughput (required — see smithing SCHEMA extension)
throughput:
  units_per_hour:
    small_work: {integer}
    medium_work: {integer}
    large_work: {integer}
  max_active_hours_per_week: {integer}
  product_mix:
    repair: {0-100}
    commodity: {0-100}
    specialty: {0-100}
    artistic: {0-100}
  throughput_variance:
    worst_month_fraction_of_average: {decimal}
    best_month_fraction_of_average: {decimal}
    seasonal: {description}

# Operator profile (required)
operator_skill_floor: {apprentice | journeyman | master}
operators_concurrent: {N or "N-M"}
apprentice_friendly: {boolean}
apprentice_path:              # required when apprentice_friendly: true
  training_stages: [{stage-description}, ...]
  time_to_independent_operation: {value with units}
  succession_note: {description}

# Economics (required)
economics:
  currency: USD                            # or other declared currency
  capital_cost: { low: {}, mid: {}, high: {} }
  install_cost: {integer}
  annual_maintenance: {integer}
  annual_consumables: {integer}
  floor_space_rent_per_year: {integer}
  market_price_per_unit:                   # required if lens_fit.market in {good, marginal}
    low: {value}
    mid: {value}
    high: {value}
  pricing_notes: {description}
  pricing_validation: {sourced | inferred | placeholder}
  industrial_baseline_price: {value}        # required if lens_fit.market in {good, marginal}

# Operations reality (required)
operations_reality:
  first_year_failures:
    - item: {description}
      estimated_hours_to_failure: {integer}
      replacement_cost: {integer}
      replacement_lead_time_days: {integer}
      serviceable_by: {operator | journeyman | specialist}
    # 2-4 items typical
  maintenance_schedule:
    daily: {task}
    weekly: {task}
    monthly: {task}
    quarterly: {task}
    annual: {task}
  startup_shutdown_overhead_per_day_min: {integer}
  max_active_hours_realism_note: {description — derated or theoretical?}
  consumables_lead_time_days: { typical: {}, worst: {} }
  interruption_notes: {optional prose}
  operator_impact:
    noise_db: {integer}
    heat_exposure: {description}
    emissions: {description}
    physical_demand: {description}

# Regulatory notes (required, 3-line cap)
regulatory_notes:
  zoning: {description}
  emissions: {description}
  other: {description}

# Context fit (required — tri-state)
lens_fit:      { market: {good|marginal|poor}, cooperative: {}, civic: {} }
scale_fit:     { village: {}, town: {}, small_city: {} }

# Lens context — required when corresponding lens_fit is good or marginal
lens_context:
  cooperative:      # if lens_fit.cooperative in {good, marginal}
    membership_boundary: {description}
    rules_source: {description}
    monitoring: {description}
    graduated_sanctions: {description}
    conflict_resolution: {description}
    scale_fit_note: {description}
    member_amendment_process: {description}
    legal_form: {LLC | cooperative-corporation | unincorporated-association | 501c3}
    ostrom_principles_addressed: [{1-8}]
  civic:            # if lens_fit.civic in {good, marginal}
    political_coalition: {description}
    council_vote_estimate: {description}
    competes_with_private: {description}
    governance_form: {description}
    budget_line: {description}
    benchmark_comparison: {description}    # library / rec center / etc
    staffing_model:
      role: {description}
      wage_source: {pointer to SCALES.md or citation}
      wages_per_year: {integer}
      hours: {description}
      hiring_notes: {description}
    civic_externalities: [{description}, ...]

# Machine-readable simulation parameters
sim_params:
  cost_mean: {integer}
  cost_sd: {integer}
  throughput_units_equiv_per_year: {integer}
  variable_cost_per_unit: {decimal}
  labor_hours_per_unit: {decimal}
  downtime_fraction: {decimal}
  lifespan_years: {integer}

# Evaluation results (populated by Plan D; 9 cells, start null)
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
  - ref: {citation or [CITATION-NEEDED]}
    note: {what it supports}
---
```

**Required prose sections (per `catalog/SCHEMA.md` §5):**

1. **Summary** (~100-150 words) — what this forge is, who it's for, why it exists in the catalog.
2. **Design rationale** (~150-200 words) — why these design choices; what problem this entry solves that no other entry does.
3. **Historical lineage** (~100-150 words) — which anchor cultures inspired it (reference specific chapter passages); function-vs-form distinction respected.
4. **Key assumptions** (~150-200 words) — where the numbers come from; which are solid, which are rough; pricing_validation explicit.
5. **Known risks / failure modes** (~100-150 words) — regulatory, labor pipeline, supply chain, demand variance.
6. **Target niche(s) and competitive positioning** (~100-150 words) — per DECLINE-VERDICT guidance, name the restorable niche (repair / specialty / shared-civic / training). Name what industrial competitor this does / does not compete against.
7. **Iteration log** — dated notes as the entry evolves. Initially: "2026-04-XX v1.0 — initial authoring."

### Per-Entry Self-Review Checklist

- [ ] All required frontmatter fields populated (not left blank or with `{placeholder}` values)
- [ ] Conditional fields (`lens_context.cooperative`, `lens_context.civic`, `market_price_per_unit`, `apprentice_path`) populated iff their trigger condition holds
- [ ] Every numeric field either cited via `sources:` or carries a `[CITATION-NEEDED: ...]` placeholder
- [ ] `sim_params` cross-checks against throughput (per METHODOLOGY §3.1)
- [ ] Operations-reality captures `first_year_failures` with `serviceable_by` per item
- [ ] Pricing validation explicit (sourced / inferred / placeholder)
- [ ] Regulatory notes terse (3 lines max)
- [ ] Prose sections all present and non-trivial (summary / rationale / lineage / assumptions / risks / niche / log)
- [ ] No `docs/superpowers/...` paths
- [ ] No marketing language (STYLE-GUIDE §7)
- [ ] No romanticism (STYLE-GUIDE §4)
- [ ] Historical lineage cites a specific chapter passage, not generic culture-reference

### Per-Entry Commit

```bash
git add catalog/smithing/entries/{NNN}-{slug}.md
git commit -m "Plan C task {N}: forge-{NNN} {short-name}"
```

---

### Task 3-specific — forge-001 Backyard Propane Compact

**Target niche:** Entry-level / hobbyist / low-capital starter. Tests the "minimum viable entry" cell of the matrix.

**Key parameters to populate:**
- Energy: propane. Footprint: 8-12 m². Capital: $1,500-$5,000 range.
- Operator: apprentice-to-journeyman floor. Single operator.
- Scale: village-only (community of 500-2000). Market: poor-to-marginal (cannot compete on commodity; premium segment too thin at village scale). Coop: marginal. Civic: poor.
- This entry's purpose is to DEMONSTRATE that low-capital entry is not automatically viable. Per DECLINE-VERDICT, it's testing the boundary.

**Commit:** `Plan C task 3: forge-001 Backyard Propane Compact`

---

### Task 4-specific — forge-002 Induction-Modular Small Repair

**Target niche:** Modern repair-focused operation. Induction-electric avoids coal/emission regulation; modular allows urban small-city footprint.

**Key parameters:**
- Energy: induction-electric. Footprint: 20-35 m². Capital: $25,000-$60,000.
- Operator: journeyman floor. 1-2 operators.
- Scale: village marginal, town good, small-city good. Market: good (repair priced as premium service). Coop: marginal. Civic: marginal.

**Commit:** `Plan C task 4: forge-002 Induction-Modular Small Repair`

---

### Task 5-specific — forge-003 Shared Tool-Library Coal

**Target niche:** Canonical coop example from spec §5. Member-booked shifts, medium footprint, town scale.

**Key parameters:** use the spec's forge-003 example frontmatter as the starting basis; adapt consistent with the updated schema (v0.3 added fields). Market: marginal. Coop: good. Civic: good. Village: marginal. Town: good. Small-city: good.

**Commit:** `Plan C task 5: forge-003 Shared Tool-Library Coal`

---

### Task 6-specific — forge-004 Community Civic Makerspace

**Target niche:** Town-owned civic workshop, library-model access. Includes smithing + woodworking + textiles within one facility (but this entry covers only the forge portion).

**Key parameters:**
- Energy: hybrid (induction + propane backup). Footprint: 50-80 m² (forge portion only).
- Operator: master floor for supervision; community members use under supervision.
- Civic: good. Coop: good. Market: poor (not competing commercially).
- Lens_context.civic must be substantive: political coalition (library + economic-development + workforce), benchmark vs rec-center cost.

**Commit:** `Plan C task 6: forge-004 Community Civic Makerspace`

---

### Task 7-specific — forge-005 Frontier-Revival Coal Repair

**Target niche:** Single-operator coal forge, repair-dominant. American frontier smith revival for contemporary rural market.

**Key parameters:**
- Energy: coal (+ charcoal backup). Footprint: 25-40 m². Capital: $15,000-$30,000.
- Operator: journeyman or master. 1 + informal apprentice.
- Village/town: market-primary. Small-city: market-marginal (zoning against coal).

**Commit:** `Plan C task 7: forge-005 Frontier-Revival Coal Repair`

---

### Task 8-specific — forge-006 Induction Bladesmith

**Target niche:** Specialty / custom / direct-to-consumer premium. Chef knives, outdoor blades, kitchen knives.

**Key parameters:**
- Energy: induction-electric (precise heat control for heat treatment). Footprint: 30-50 m².
- Capital: $40,000-$100,000 (induction + grinders + heat-treat oven).
- Operator: master floor. 1-2 operators.
- Small-city: market-good. Town: market-marginal. Coop: good (member-artisan variant). Civic: marginal.

**Commit:** `Plan C task 8: forge-006 Induction Bladesmith`

---

### Task 9-specific — forge-007 Containerized Mobile Forge

**Target niche:** Mobile service provider; drives a route of rural/village clients. Intermodal-container conversion.

**Key parameters:**
- Energy: propane primary (mobility requires). Footprint: 15 m² (container interior).
- Capital: $35,000-$75,000 (container conversion + truck + forge equipment).
- Village: market-good (cannot be centralized; location-bound repair demand). Town: market-marginal (stationary competitors). Small-city: market-poor.

**Commit:** `Plan C task 9: forge-007 Containerized Mobile Forge`

---

### Task 10-specific — forge-008 Traditional Charcoal Village

**Target niche:** Purist / historical-method shop. Primary deliverable is the craft's preservation + specialty output.

**Key parameters:**
- Energy: charcoal + traditional bellows (hand or treadle). Footprint: 20-35 m².
- Capital: $8,000-$20,000 (low-tech, traditional materials).
- Operator: master preferred; journeyman acceptable.
- Village: market-marginal (slow throughput; premium only). Coop: marginal (craft-education pairing). Civic: marginal (cultural-preservation argument).

**Commit:** `Plan C task 10: forge-008 Traditional Charcoal Village`

---

### Task 11-specific — forge-009 Co-op Apprentice Training Forge

**Target niche:** Formal apprentice pipeline. Coop-operated workshop with paid master-of-the-week rotation; funds apprentice stipends via member fees + specialty-output sales.

**Key parameters:**
- Energy: coal + induction hybrid. Footprint: 60-100 m² (multi-station for apprentice work).
- Capital: $80,000-$180,000.
- Town / small-city: coop-good + civic-marginal. Village: poor (member-pool too thin).
- Lens_context.cooperative must detail: member-pool sizing, Ostrom 8, apprentice intake cadence.

**Commit:** `Plan C task 11: forge-009 Co-op Apprentice Training Forge`

---

### Task 12-specific — forge-010 Architectural Ironwork Bespoke

**Target niche:** Gates, railings, custom hardware for contractors + high-end residential. Specialty output, market-primary.

**Key parameters:**
- Energy: propane + induction for heat treatment. Footprint: 50-80 m² (need space for large pieces).
- Capital: $60,000-$150,000.
- Operator: master. 1-2 operators + fabrication helper.
- Small-city: market-good. Town: market-marginal. Village: market-poor (clientele absent).

**Commit:** `Plan C task 12: forge-010 Architectural Ironwork Bespoke`

---

### Task 13-specific — forge-011 Municipal Civic Training Forge

**Target niche:** Public high-school / community-college partnership. Apprentice-pipeline builder. Civic-primary.

**Key parameters:**
- Energy: induction-electric (safety, fewer regulatory hurdles in school context). Footprint: 80-120 m² (multi-station teaching facility).
- Capital: $120,000-$280,000 (school grant + municipal bond financing typical).
- Civic: good (small-city); marginal (town); poor (village).
- Lens_context.civic substantive: budget-line likely workforce-development, staffing public-education wages, benchmark vs. CTE / vocational programs.

**Commit:** `Plan C task 13: forge-011 Municipal Civic Training Forge`

---

### Task 14-specific — forge-012 Farriery-Specialist Propane

**Target niche:** Horseshoeing + hoof-care. Equine clientele. Per DECLINE-VERDICT: last survivable horseshoeing niche = boutique horse-owning communities.

**Key parameters:**
- Energy: propane (portable; often mobile for stable visits). Footprint: 10-15 m² (shop) or vehicle-mounted.
- Capital: $15,000-$35,000.
- Operator: journeyman floor (farriery skill specialized).
- Rural-village focus. Market: good (location-bound, skilled). Town: marginal (horse population thin in suburban areas). Small-city: poor.

**Commit:** `Plan C task 14: forge-012 Farriery-Specialist Propane`

---

### Task 15-specific — forge-013 Restoration-Specialist Heritage

**Target niche:** Historic-building restoration, architectural repair. Heritage-preservation clientele. Market + civic good (historical preservation public interest).

**Key parameters:**
- Energy: coal + propane + induction (multi-capability needed for period-authentic work). Footprint: 40-80 m².
- Capital: $45,000-$100,000.
- Operator: master floor.
- Small-city: market-good + civic-good. Town: market-marginal + civic-marginal. Village: market-poor.
- Civic angle: municipal historic-preservation grants; benchmark vs. preservation-society funding.

**Commit:** `Plan C task 15: forge-013 Restoration-Specialist Heritage`

---

### Task 16-specific — forge-014 Electric-Induction Gig Repair Micro

**Target niche:** Minimum-capital entry, part-time operator, village-only. Stress-test of "lowest possible capital to enter" scenario.

**Key parameters:**
- Energy: induction-electric compact unit. Footprint: 8-12 m² (garage or shed conversion).
- Capital: $3,000-$10,000.
- Operator: apprentice-to-journeyman. Part-time / gig structure.
- Village: market-marginal. Town / small-city: market-poor (cannot compete with larger shops on throughput).
- Tests the viability floor. Expected verdict: marginal-to-fail across all lenses.

**Commit:** `Plan C task 16: forge-014 Electric-Induction Gig Repair Micro`

---

### Task 17-specific — forge-015 Tool-Library Member-Access Induction

**Target niche:** Member-subscription induction workshop. Lower-capital shared-resource model than coal (no ventilation infrastructure burden; induction is cleaner).

**Key parameters:**
- Energy: induction-electric. Footprint: 30-50 m² (multi-user configuration).
- Capital: $50,000-$120,000.
- Operator: journeyman floor for supervision; members work under protocol.
- Town / small-city: coop-good + civic-marginal. Village: poor (member-pool thin).

**Commit:** `Plan C task 17: forge-015 Tool-Library Member-Access Induction`

---

## Task 18: Cross-Entry Audit

**Files:**
- Create: `reviews/CATALOG-AUDIT-plan-c.md`

**Purpose:** Before the catalog is promoted from draft to ceres-panel review, run an audit across all 15 entries to verify:

1. **Schema completeness** — every entry passes self-review checklist
2. **Lens-fit distribution** — sanity check: is the distribution balanced enough to give Tier A simulation meaningful variance? No lens starved (e.g., if only 1 of 15 claims civic-good, flag).
3. **Scale-fit distribution** — same check per scale
4. **Context-matrix coverage** — every one of the 9 cells (scale × lens) has ≥2 entries claiming `good` or `marginal`. No empty cells.
5. **Entry-ID uniqueness + numbering** — 001-015, no duplicates
6. **Inspirations diversity** — entries reference chapters from multiple anchor cultures, not only one
7. **Niche-group distribution** — approximately 6 repair, 3 specialty, 4 shared-civic, 2 training (per manifest)
8. **Anti-romanticism hold** — no entry drifts into marketing-speak or romantic framing
9. **Citation density** — every numeric field cited or placeholdered; no field blank
10. **Placeholder audit** — consolidated list of `[CITATION-NEEDED]` across 15 entries; priority for verification

Write the audit report. Does NOT need to produce a PASS verdict to complete — HOLD is acceptable; blocking findings are fixed in a follow-up task.

**Commit:** `Plan C task 18: catalog cross-entry audit`

---

## Task 19: Closeout

**Files touched:**
- Update: `TRACKER.md` (Plan C status → completed; vertical-slice-progress updates for catalog entries)
- Update: `plans/README.md` (Plan C status → completed)
- Update: `plans/2026-04-19-plan-c-catalog-smithing.md` frontmatter (status: completed, completed: date, version bump as appropriate)
- Update: `catalog/smithing/README.md` (entry-status-tracking table populated)

**Commit:** `Plan C task 19: closeout`

---

## Retrospective: Risks and Assumptions (authored upfront per P-6 discipline)

### Risks and Objections

- **Design-space gaps.** 15 entries may not span the 9-cell matrix as expected; some cells may be thin. Mitigation: Task 18 audit catches this; reauthor 1-2 entries if a cell has no coverage.
- **Schema drift risk.** Authoring 15 entries against the schema may surface schema deficiencies. Policy: spec-amendment pathway (don't silently deviate). If the schema needs an addition, open a spec amendment before proceeding.
- **Citation-placeholder load.** Equipment cost numbers for modern forges are not academically well-sourced. Expect heavy use of `[CITATION-NEEDED: ...]` placeholders for modern capital costs. The author verifies via vendor catalogs / maker forums post-hoc; for the plan, illustrative-but-reasonable is acceptable.
- **Niche-group imbalance.** If the review surfaces that the 6/3/4/2 split is wrong (e.g., too many repair entries, not enough civic), the cross-entry audit can flag; fixes rebalance.
- **Downstream sim-readiness.** sim_params are the sim's ingestion target. Schema enforces them, but their values drive Tier A outputs. Illustrative numbers may produce simulation results that don't match intuition. Accept this is evidence, not failure.

### Failure Modes (contingency paths)

- **If schema proves insufficient:** spec-amendment to SCHEMA.md (not silent field addition). Pause authoring; unblock when amendment lands.
- **If an entry repeatedly fails self-review:** simplify to 10-12 entries + document the 3-5 that were attempted and dropped (as entries with `status: deprecated` — preserves the design-exploration record).
- **If cross-entry audit shows matrix cells empty:** author 1-2 replacement entries targeting the empty cells; bump Plan C scope.
- **If DECLINE-VERDICT implications prove too narrow:** if the 15 entries all land in only 1-2 niches and cannot span repair+specialty+shared-civic, propose a spec-level discussion (the verdict may need reinterpretation). Stop and escalate, don't silently proceed.

### Assumptions Now Made Explicit

- REQUIREMENTS.md R-01 through R-24 are stable; Plan C cites them but does not re-derive.
- SCALES.md thresholds are stable for Plan C duration; wage and civic-cost anchors carry the "illustrative — refine before validated" label.
- `catalog/SCHEMA.md` v1.1 is the canonical schema; `catalog/smithing/SCHEMA.md` extends without contradiction.
- DECLINE-VERDICT.md's "target repair + specialty + shared-civic" guidance is binding; commodity-hardware entries are explicitly deprecated (not authored) per the verdict.
- Citation policy from Plan B continues: `[CITATION-NEEDED: ...]` over fabrication. Manufacturer / vendor numbers for modern equipment are illustrative.
- Plan D and Plan E authors will consume these entries and perform their own reviews.

## Handoff

When Plan C completes:

1. TRACKER updated. Plan C frontmatter `status: completed`.
2. 15 entries exist at `catalog/smithing/entries/*.md`, all schema-complete.
3. Cross-entry audit committed.
4. Plan C artifacts are ready for formal `ceres-panel` R1 review (all 6 voices on a representative sample of entries) before Plan D consumes them for simulation.
5. Plan D (simulation + lens math) is unblocked — it reads the `sim_params` blocks from all 15 entries and produces the 9-cell `results:` evaluations.
6. Plan E (playbook + pitch) is not yet unblocked — it needs Plan D outputs.
