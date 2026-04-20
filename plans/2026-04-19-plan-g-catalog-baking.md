---
id: plan-g-catalog-baking
name: Catalog — Baking (15 Entries)
description: 15 baking catalog entries per DECLINE-VERDICT niche guidance; each schema-complete and ready for Tier A sim
status: completed
completed: 2026-04-19
last_modified: 2026-04-19
version: "1.1"
created: 2026-04-19
phase: 2
subsystem: catalog
trade: baking
depends_on: [plan-a-scaffolding, plan-f-research-baking]
blocks: []
estimated_effort: 2-4 weeks focused
primary_artifact_type: catalog
success_signal: >
  15 baking catalog entries at catalog/baking/entries/*.md, schema-compliant
  per catalog/SCHEMA.md v1.1. All conditional fields populated. Every cost
  and throughput number cited or placeholdered. Entries span artisan-bread /
  confection-specialty / community-bakery / training niches per
  DECLINE-VERDICT. 9-cell matrix coverage confirmed by cross-entry audit.
spec: specs/2026-04-18-ceres-design.md
---

# Plan G: Catalog — Baking (15 Entries)

> **Pattern inherited from Plan C (smithing).** Same structure: manifest + schema extension + 15 entries + cross-entry audit + closeout.
> **Simulation already scripted:** after entries are authored, run the existing Tier A CLI:
> `cd simulations/tier-a-comparator && python -c "import sys; sys.path.insert(0,'src'); from tier_a.cli import main; main(['--catalog','../../catalog/baking/','--results-dir','./results/baking'])"`

**Decline-verdict guidance (per `research/trades/baking/DECLINE-VERDICT.md`):**
- Target niches: artisan/premium bread, community-bakery (coop/civic), specialty confection, training/apprenticeship
- Key falsifier: **mill dependency** — every entry must declare its flour-sourcing assumption
- Do NOT attempt commodity factory-bread competition

**Key baking-specific schema differences:**
- `throughput` block: `loaves_per_day`, `batches_per_day`, `batch_size_loaves`
- `energy_source` enum extends to: wood-fired, electric-deck, convection-electric, deck-gas, combi-steam, hybrid
- `operator_skill_floor` baking-specific: apprentice-baker / journeyman-baker / pastry-chef-master

---

## The 15-Entry Manifest

Per DECLINE-VERDICT.md guidance, the catalog targets restorable niches. The 15 entries distribute across four groups to give Tier A simulation meaningful variance:

### Group A — Artisan Bread / Premium (5 entries)

The most durable historical baking niche. Premium differentiation resists industrial displacement where commodity bread does not. Location-bound customer relationships and sensory quality are the competitive moat.

1. **bake-001 — Sourdough Artisan Micro-bakery** — wood-fired or electric deck, market-primary, village/town, minimum-capital entry. Direct-to-consumer premium sourdough; tests lowest-viable artisan bread operation.
2. **bake-002 — Heritage Grain Subscription Bakery** — electric-deck, market + coop, town/city, premium CSA subscription model with heritage-grain sourcing.
3. **bake-003 — Community Grain-Share Bakery** — electric, coop-primary, town, mill-integrated test case addressing the flour-sourcing falsifier directly.
4. **bake-004 — Wholesale Artisan Loaf Bakery** — electric-deck, market-primary, small-city, B2B channel to restaurants and specialty grocery.
5. **bake-005 — Mobile Pop-up Bakery** — convection van, market-primary, village/rural, farmers-market and event-driven model.

### Group B — Specialty Confection / Pastry (4 entries)

Low-volume, elastic-demand, high-margin work. Per DECLINE-VERDICT: survives via premium-market and event-driven segmentation where commodity confection is industrial-dominated.

6. **bake-006 — French-style Pastry / Viennoiserie** — electric-combi, market-primary, small-city, premium laminated-dough pastry retail.
7. **bake-007 — Japanese-style Wagashi Confection** — combi-steam + low-bake, market + civic, town/city, cultural specialty with heritage-preservation civic angle.
8. **bake-008 — Ethnic / Cultural Specialty Bakery** — variable fuel, market-primary, any scale, serves an underserved ethnic community niche.
9. **bake-009 — Wedding / Custom Cake Studio** — electric, market-primary, small-city, event-driven custom-order model.

### Group C — Community / Civic / Coop (4 entries)

Per DECLINE-VERDICT: community-serving bakeries and training externalities support coop and civic lens viability where market-primary models are marginal.

10. **bake-010 — Civic Neighborhood Bakery** — electric-deck, civic-primary, town, community food-access mandate.
11. **bake-011 — Apprentice Training Bakery** — electric-combi, coop + civic, town/city, linked to food-service and culinary programs.
12. **bake-012 — Community Kitchen Collective** — shared-facility model, coop-primary, town, commercial-kitchen-sharing reduces capital per member.
13. **bake-013 — Farm-to-Table Integrated Bakery** — wood-fired, market + civic, village/town, addresses mill-dependency falsifier via direct farm-mill-bakery integration.

### Group D — Minimum-viable / Stress-test (2 entries)

These entries test the viability floor. Both are expected to perform poorly across most matrix cells; their inclusion provides the low-end variance required for meaningful simulation.

14. **bake-014 — Apartment/Home Micro-bakery** — electric home oven + optional deck stone upgrade, village-only, stress-test of viability floor. Tests whether cottage-food-law entry is economically viable.
15. **bake-015 — Wood-fired Community Oven** — civic/coop, village/town, traditional shared-oven model from Plan B medieval chapter.

### Context-Matrix Coverage

The 15 entries collectively span the 9-cell matrix (3 scales × 3 lenses). Every cell has at least 2 entries claiming `good` or `marginal`. No cell is empty. Variance across entries enables Tier A simulation to produce meaningful winners and losers per cell.

---

## Task Index (same as Plan C)

| # | Task | Creates |
|---|---|---|
| 1 | Catalog manifest / README | `catalog/baking/README.md` (expand stub) |
| 2 | Baking schema extension | `catalog/baking/SCHEMA.md` (expand stub) |
| 3 | Entry bake-001 Sourdough Artisan Micro-bakery | `catalog/baking/entries/001-sourdough-artisan-micro-bakery.md` |
| 4 | Entry bake-002 Heritage Grain Subscription Bakery | `catalog/baking/entries/002-heritage-grain-subscription-bakery.md` |
| 5 | Entry bake-003 Community Grain-Share Bakery | `catalog/baking/entries/003-community-grain-share-bakery.md` |
| 6 | Entry bake-004 Wholesale Artisan Loaf Bakery | `catalog/baking/entries/004-wholesale-artisan-loaf-bakery.md` |
| 7 | Entry bake-005 Mobile Pop-up Bakery | `catalog/baking/entries/005-mobile-popup-bakery.md` |
| 8 | Entry bake-006 French-style Pastry / Viennoiserie | `catalog/baking/entries/006-french-pastry-viennoiserie.md` |
| 9 | Entry bake-007 Japanese-style Wagashi Confection | `catalog/baking/entries/007-wagashi-confection.md` |
| 10 | Entry bake-008 Ethnic / Cultural Specialty Bakery | `catalog/baking/entries/008-ethnic-cultural-specialty-bakery.md` |
| 11 | Entry bake-009 Wedding / Custom Cake Studio | `catalog/baking/entries/009-wedding-custom-cake-studio.md` |
| 12 | Entry bake-010 Civic Neighborhood Bakery | `catalog/baking/entries/010-civic-neighborhood-bakery.md` |
| 13 | Entry bake-011 Apprentice Training Bakery | `catalog/baking/entries/011-apprentice-training-bakery.md` |
| 14 | Entry bake-012 Community Kitchen Collective | `catalog/baking/entries/012-community-kitchen-collective.md` |
| 15 | Entry bake-013 Farm-to-Table Integrated Bakery | `catalog/baking/entries/013-farm-to-table-integrated-bakery.md` |
| 16 | Entry bake-014 Apartment/Home Micro-bakery | `catalog/baking/entries/014-apartment-home-micro-bakery.md` |
| 17 | Entry bake-015 Wood-fired Community Oven | `catalog/baking/entries/015-wood-fired-community-oven.md` |
| 18 | Cross-entry audit | `reviews/CATALOG-AUDIT-plan-g.md` |
| 19 | Closeout | TRACKER + plans/README + frontmatter |

19 tasks total. Execution is naturally parallelizable in waves:
- Wave 0 (sequential): Tasks 1 + 2 (manifest + schema extension — everything downstream depends on these)
- Wave 2 (parallel × 3 batches): 5 entries per batch (Tasks 3-7, Tasks 8-12, Tasks 13-17)
- Wave 3 (sequential): Task 18 audit, then Task 19 closeout

---

## Task 1: Catalog Manifest / README

**Files:**
- Expand: `catalog/baking/README.md` (Plan A Task 2 created a stub; this expands it)

**Required content:**

1. **Frontmatter:** trade: baking, doc_type: catalog-overview, version: "1.0", status: draft, entry_count: 15
2. **Purpose** (~100 words) — what the baking catalog is, relationship to REQUIREMENTS/HISTORICAL-FORMS/DECLINE-VERDICT.
3. **The 15-entry manifest** (Groups A/B/C/D with entry IDs + names + one-line descriptions)
4. **Design-space coverage note** — mill-dependency falsifier + DECLINE-VERDICT niche targeting
5. **Lens-fit and scale-fit distribution** — 15-row summary table
6. **Entry status tracking** — entry-id | status | last-modified
7. **Sources** pointers

**Commit:** `Plan G task 1: baking catalog manifest (15-entry overview)`

---

## Task 2: Baking-Specific Schema Extension

**Files:**
- Expand: `catalog/baking/SCHEMA.md` (stub exists; this replaces with full content)

**Required content:**

1. **Frontmatter:** trade: baking, doc_type: schema-extension, extends: catalog/SCHEMA.md, version: "1.0", schema_base_version: "1.1"
2. **Purpose** — one paragraph
3. **Baking `throughput` block structure** with `loaves_per_day`, `batches_per_day`, `batch_size_loaves`, `product_mix`
4. **`energy_source` baking enum** with capability notes
5. **`operator_skill_floor` baking definitions**
6. **`flour_source_declaration` field definition** (required for all entries)
7. **`first_year_failures` reference list**
8. **Per-niche-group notes** for Wave 2 authors

**Commit:** `Plan G task 2: baking-specific schema extension`

---

## Tasks 3-17: Per-Entry Authoring (15 entries)

### Shared Structure Across All Entry Tasks

Each entry follows `catalog/SCHEMA.md` v1.1 plus the baking extension in `catalog/baking/SCHEMA.md`. Full frontmatter schema as per Plan C, with baking-specific additions:

```yaml
flour_source_declaration: industrial-flour-purchased | local-mill-partnership | integrated-milling | on-site-milling
throughput:
  loaves_per_day: {integer}
  batches_per_day: {integer}
  batch_size_loaves: {integer}
  product_mix:
    bread: {percentage}
    confection: {percentage}
    specialty: {percentage}
    catering: {percentage}
energy_source: wood-fired-deck | electric-deck | convection-electric | deck-gas | combi-steam | hybrid-wood-electric
operator_skill_floor: apprentice-baker | journeyman-baker | pastry-chef-master
```

**Required prose sections:** Summary, Design rationale, Historical lineage, Key assumptions, Known risks / failure modes, Target niche(s) and competitive positioning, Iteration log.

### Per-Entry Self-Review Checklist

- [ ] All required frontmatter fields populated (not left blank)
- [ ] `flour_source_declaration` present and consistent with Key Assumptions
- [ ] Conditional fields populated iff their trigger condition holds
- [ ] Every numeric field cited or carries `[CITATION-NEEDED: ...]`
- [ ] `sim_params` cross-checks against throughput
- [ ] `first_year_failures` 2-4 items with `serviceable_by` per item
- [ ] Pricing validation explicit (sourced / inferred / placeholder)
- [ ] Regulatory notes terse (3 lines max)
- [ ] Prose sections all present and non-trivial
- [ ] No `docs/superpowers/...` paths
- [ ] No marketing language (STYLE-GUIDE §7)
- [ ] No romanticism (STYLE-GUIDE §4)
- [ ] Historical lineage cites a specific chapter passage

### Per-Entry Commit

```bash
git add catalog/baking/entries/{NNN}-{slug}.md
git commit -m "Plan G task {N}: bake-{NNN} {short-name}"
```

---

### Task 3-specific — bake-001 Sourdough Artisan Micro-bakery

**Target niche:** Minimum-capital artisan-bread entry. Tests the low-capital artisan bread cell of the matrix.

**Key parameters:**
- Energy: wood-fired-deck or electric-deck. Footprint: 15-25 m². Capital: $8,000-$25,000.
- `flour_source_declaration: local-mill-partnership` (preferred) or `industrial-flour-purchased`.
- Operator: journeyman-baker floor. 1-2 operators.
- Village/town: market-primary. Loaves: 30-80/day. Throughput unit = 800g boule equivalent.

**Commit:** `Plan G task 3: bake-001 Sourdough Artisan Micro-bakery`

---

### Task 4-specific — bake-002 Heritage Grain Subscription Bakery

**Target niche:** Premium CSA/subscription model using heritage grains. High margin, loyal customer base resists price comparison.

**Key parameters:**
- Energy: electric-deck. Footprint: 30-50 m². Capital: $35,000-$80,000.
- `flour_source_declaration: local-mill-partnership` or `integrated-milling`.
- Operator: journeyman-baker floor. 1-3 operators.
- Town/small-city: market-good + coop-good. Heritage-grain supply chain is a key dependency; must state supplier or `[CITATION-NEEDED]`.

**Commit:** `Plan G task 4: bake-002 Heritage Grain Subscription Bakery`

---

### Task 5-specific — bake-003 Community Grain-Share Bakery

**Target niche:** Coop model integrating grain-share/CSA with baking. Tests mill-dependency falsifier directly — this is the catalog's canonical mill-integration entry.

**Key parameters:**
- Energy: electric-deck. Footprint: 40-70 m². Capital: $50,000-$120,000.
- `flour_source_declaration: integrated-milling` — this entry's defining feature; the entry must describe the mill integration in Key Assumptions.
- Operator: journeyman-baker. Multi-member coop.
- Town: coop-primary. Coop lens-context must address member grain-share mechanics and Ostrom 8.

**Commit:** `Plan G task 5: bake-003 Community Grain-Share Bakery`

---

### Task 6-specific — bake-004 Wholesale Artisan Loaf Bakery

**Target niche:** B2B artisan-bread wholesale to restaurants and specialty retail. Market-primary.

**Key parameters:**
- Energy: electric-deck (multiple deck ovens). Footprint: 60-100 m². Capital: $80,000-$200,000.
- `flour_source_declaration: industrial-flour-purchased` or `local-mill-partnership`.
- Operator: journeyman-baker floor. 2-4 operators.
- Small-city: market-good. B2B channel dependency (restaurant closures, retail buyer concentration) is a key risk.

**Commit:** `Plan G task 6: bake-004 Wholesale Artisan Loaf Bakery`

---

### Task 7-specific — bake-005 Mobile Pop-up Bakery

**Target niche:** Vehicle-based mobile bakery serving farmers-markets and rural routes.

**Key parameters:**
- Energy: convection-electric (van-mounted generator or shore power). Footprint: vehicle (8-12 m² equivalent). Capital: $20,000-$55,000.
- `flour_source_declaration: industrial-flour-purchased` (supply chain must be mobile-compatible).
- Operator: journeyman-baker. 1-2 operators.
- Village/rural: market-good. Town: market-marginal. Permitting for mobile food is the primary regulatory risk.

**Commit:** `Plan G task 7: bake-005 Mobile Pop-up Bakery`

---

### Task 8-specific — bake-006 French-style Pastry / Viennoiserie

**Target niche:** Premium pastry retail. High skill floor, high margin, low throughput.

**Key parameters:**
- Energy: combi-steam (laminated dough requires precise steam injection). Footprint: 40-60 m². Capital: $60,000-$150,000.
- `flour_source_declaration: industrial-flour-purchased` (specialty flour grades, Type 45/55 equivalent required).
- Operator: pastry-chef-master floor. 1-3 operators.
- Small-city: market-good. Town: market-marginal. Skill succession is the primary long-run risk.

**Commit:** `Plan G task 8: bake-006 French-style Pastry / Viennoiserie`

---

### Task 9-specific — bake-007 Japanese-style Wagashi Confection

**Target niche:** Cultural specialty confection. Civic-preservation angle supports coop + civic lens.

**Key parameters:**
- Energy: combi-steam + low-bake electric (separate steam and dry-heat units). Footprint: 25-40 m². Capital: $30,000-$70,000.
- `flour_source_declaration: industrial-flour-purchased` (specialty rice flour, azuki bean paste supply chain).
- Operator: pastry-chef-master preferred. 1-2 operators.
- Town/city: market-marginal + civic-marginal. Cultural-preservation civic argument available; benchmark vs. cultural-center programming.

**Commit:** `Plan G task 9: bake-007 Japanese-style Wagashi Confection`

---

### Task 10-specific — bake-008 Ethnic / Cultural Specialty Bakery

**Target niche:** Underserved ethnic-community bakery serving a captive cultural niche.

**Key parameters:**
- Energy: deck-gas or variable (tradition-specific; document per cultural referent). Footprint: 25-50 m². Capital: $25,000-$70,000.
- `flour_source_declaration: industrial-flour-purchased` (specialty grain sourcing noted per cultural tradition).
- Operator: journeyman-baker floor. Any community scale.
- Market: good (captive underserved community demand). Coop: marginal-to-good (community collective option available).

**Commit:** `Plan G task 10: bake-008 Ethnic / Cultural Specialty Bakery`

---

### Task 11-specific — bake-009 Wedding / Custom Cake Studio

**Target niche:** Event-driven custom cake and confection studio. Market-primary.

**Key parameters:**
- Energy: electric (precision temperature control required for sugar work and fondant). Footprint: 30-50 m². Capital: $25,000-$80,000.
- `flour_source_declaration: industrial-flour-purchased`.
- Operator: pastry-chef-master floor. 1-2 operators.
- Small-city: market-good. Town: market-marginal. Revenue lumpy (event-driven); `throughput_variance` must reflect seasonal event peaks.

**Commit:** `Plan G task 11: bake-009 Wedding / Custom Cake Studio`

---

### Task 12-specific — bake-010 Civic Neighborhood Bakery

**Target niche:** Community food-access mandate, civic-primary. The baking equivalent of a civic library.

**Key parameters:**
- Energy: electric-deck. Footprint: 40-70 m². Capital: $50,000-$130,000.
- `flour_source_declaration: industrial-flour-purchased` or `local-mill-partnership`.
- Operator: journeyman-baker. 2-4 staff.
- Town: civic-good. Lens_context.civic must include food-access mandate framing, benchmark vs. food-bank cost per meal, and staffing model with public-sector wage source.

**Commit:** `Plan G task 12: bake-010 Civic Neighborhood Bakery`

---

### Task 13-specific — bake-011 Apprentice Training Bakery

**Target niche:** Formal apprentice-pipeline bakery linked to culinary and food-service programs.

**Key parameters:**
- Energy: electric-combi (teaching requires demonstrable, controllable heat). Footprint: 60-100 m². Capital: $80,000-$200,000.
- `flour_source_declaration: industrial-flour-purchased`.
- Operator: pastry-chef-master for supervision; apprentice-baker trainees.
- Town/small-city: coop-good + civic-marginal. `apprentice_path` is the defining block; must specify training stages, time-to-independent-operation, and succession-note.

**Commit:** `Plan G task 13: bake-011 Apprentice Training Bakery`

---

### Task 14-specific — bake-012 Community Kitchen Collective

**Target niche:** Shared commercial kitchen; multiple small bakers share a licensed facility and infrastructure cost.

**Key parameters:**
- Energy: electric-deck (shared ovens, scheduled booking). Footprint: 60-120 m². Capital: $60,000-$150,000.
- `flour_source_declaration: industrial-flour-purchased` (per-member; facility may stock shared staples).
- Operator: journeyman-baker floor per member. Multi-member coop model.
- Town: coop-primary. Ostrom principles critical; booking and scheduling rules must be substantive, not boilerplate.

**Commit:** `Plan G task 14: bake-012 Community Kitchen Collective`

---

### Task 15-specific — bake-013 Farm-to-Table Integrated Bakery

**Target niche:** Vertically integrated farm-to-table model; directly addresses mill-dependency falsifier.

**Key parameters:**
- Energy: wood-fired-deck (farm setting; wood fuel is on-site or local). Footprint: 30-60 m². Capital: $35,000-$90,000.
- `flour_source_declaration: integrated-milling` (on-farm or adjacent farm-mill partnership; entry must describe the integration).
- Operator: journeyman-baker. 1-3 operators.
- Village/town: market-good + civic-marginal. Supply chain advantage is the core economic claim; must document versus industrial-flour baseline.

**Commit:** `Plan G task 15: bake-013 Farm-to-Table Integrated Bakery`

---

### Task 16-specific — bake-014 Apartment/Home Micro-bakery

**Target niche:** Minimum-capital home-based entry. Stress-test of the viability floor.

**Key parameters:**
- Energy: electric (standard domestic oven; deck stone or baking steel optional upgrade). Footprint: 5-10 m². Capital: $500-$3,000.
- `flour_source_declaration: industrial-flour-purchased`.
- Operator: apprentice-baker to journeyman-baker. Part-time / cottage-industry model.
- Village-only: market-marginal. Regulatory burden (cottage-food laws, commercial-kitchen requirements) is a primary risk. Expected verdict: marginal-to-fail across most cells.

**Commit:** `Plan G task 16: bake-014 Apartment/Home Micro-bakery`

---

### Task 17-specific — bake-015 Wood-fired Community Oven

**Target niche:** Traditional shared community oven. Civic/coop primary; village/town. Inspired by medieval and early-modern communal oven tradition from Plan B research.

**Key parameters:**
- Energy: wood-fired (traditional masonry dome or barrel oven). Footprint: 15-25 m² (oven structure + firing area + queuing space). Capital: $5,000-$20,000.
- `flour_source_declaration: industrial-flour-purchased` or `local-mill-partnership`.
- Operator: apprentice-baker sufficient for routine firing; journeyman-baker for oven maintenance and repair.
- Village/town: civic-good + coop-good. Market: poor (shared-access model; not market-primary). Low throughput by design; entry is testing civic/coop model viability, not market profitability.

**Commit:** `Plan G task 17: bake-015 Wood-fired Community Oven`

---

## Task 18: Cross-Entry Audit

**Files:**
- Create: `reviews/CATALOG-AUDIT-plan-g.md`

**Audit checklist:**

1. Schema completeness — every entry passes per-entry self-review checklist
2. `flour_source_declaration` present and consistent in all 15 entries
3. Lens-fit distribution — balance check across market / coop / civic
4. Scale-fit distribution — balance check across village / town / small-city
5. Context-matrix coverage — every one of 9 cells has ≥ 2 entries at `good` or `marginal`
6. Entry-ID uniqueness (bake-001 through bake-015)
7. DECLINE-VERDICT compliance — no commodity factory-bread entries
8. Anti-romanticism hold — no entry drifts into marketing-speak
9. Citation density — every numeric field cited or placeholdered; no blank fields
10. Placeholder audit — consolidated `[CITATION-NEEDED]` list across 15 entries

**Commit:** `Plan G task 18: baking catalog cross-entry audit`

---

## Task 19: Closeout

**Files touched:**
- Update: `TRACKER.md` (Plan G status → completed)
- Update: `plans/README.md` (Plan G status → completed)
- Update: `plans/2026-04-19-plan-g-catalog-baking.md` frontmatter (status: completed, completed: date)
- Update: `catalog/baking/README.md` (entry-status-tracking table populated)

**Commit:** `Plan G task 19: closeout`

---

## Retrospective: Risks and Assumptions

### Risks and Objections

- **Mill-dependency falsifier.** Every entry must declare `flour_source_declaration`. Entries claiming `integrated-milling` or `local-mill-partnership` must document the supply-chain specifics; these are significant additional dependencies.
- **Design-space gaps.** 15 entries may not span the 9-cell matrix uniformly. Mitigation: Task 18 audit catches this; reauthor 1-2 entries if a cell has no coverage.
- **Regulatory complexity for food service.** Baking entries face food-safety licensing (commercial kitchen certification, health-department inspection, cottage-food laws) in addition to zoning. Entries must address this in `regulatory_notes`.
- **Throughput unit definition.** "Loaves" is not a uniform unit (baguette vs. sandwich loaf vs. sourdough boule). Each entry must define the specific unit used in its throughput block and the `sim_params` weighting.
- **Wood-fired entries.** Entries bake-001, bake-013, and bake-015 use wood fuel. These face fuel-supply and air-quality regulatory burdens not present for electric entries. Entries must address this in `regulatory_notes`.

### Failure Modes (contingency paths)

- **If schema proves insufficient:** spec-amendment to SCHEMA.md (not silent field addition). Pause authoring; unblock when amendment lands.
- **If an entry repeatedly fails self-review:** simplify to 10-12 entries + document dropped entries as `status: deprecated`.
- **If cross-entry audit shows matrix cells empty:** author replacement entries targeting empty cells; bump Plan G scope.

### Assumptions Now Made Explicit

- DECLINE-VERDICT.md commodity-bread guidance is binding; commodity sandwich-loaf factory entries are explicitly excluded.
- `flour_source_declaration` is a required field for all baking entries per DECLINE-VERDICT mill-dependency falsifier.
- `catalog/SCHEMA.md` v1.1 is the canonical schema; `catalog/baking/SCHEMA.md` extends without contradiction.
- Citation policy from Plan B continues: `[CITATION-NEEDED: ...]` over fabrication.
- Plan D Tier A simulation CLI already handles baking entries via `--catalog` flag (same Python entry point as smithing).

## Handoff

When Plan G completes:

1. TRACKER updated. Plan G frontmatter `status: completed`.
2. 15 entries exist at `catalog/baking/entries/*.md`, all schema-complete.
3. Cross-entry audit committed at `reviews/CATALOG-AUDIT-plan-g.md`.
4. Tier A simulation can be run immediately:
   `cd simulations/tier-a-comparator && python -c "import sys; sys.path.insert(0,'src'); from tier_a.cli import main; main(['--catalog','../../catalog/baking/','--results-dir','./results/baking'])"`
