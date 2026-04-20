---
id: plan-i-catalog-weaving
name: Catalog — Weaving (15 Entries)
description: 15 weaving catalog entries per DECLINE-VERDICT niche guidance; each schema-complete and ready for Tier A sim
status: completed
completed: 2026-04-19
last_modified: 2026-04-19
version: "1.1"
created: 2026-04-19
phase: 2
subsystem: catalog
trade: weaving
depends_on: [plan-a-scaffolding, plan-h-research-weaving]
blocks: []
estimated_effort: 2-4 weeks focused
primary_artifact_type: catalog
success_signal: >
  15 weaving catalog entries at catalog/weaving/entries/*.md, schema-compliant.
  All conditional fields populated. Entries target luxury-specialty / heritage /
  therapeutic-educational niches per DECLINE-VERDICT (commodity cloth not targeted).
  Fiber-sourcing pathway declared for every entry. 9-cell matrix coverage confirmed.
spec: specs/2026-04-18-ceres-design.md
---

# Plan I: Catalog — Weaving (15 Entries)

> **Pattern inherited from Plan C (smithing).** Same structure: manifest + schema extension + 15 entries + cross-entry audit + closeout.
> **Simulation already scripted** — run Tier A CLI on catalog/weaving/ after entries authored:
> `cd simulations/tier-a-comparator && python -c "import sys; sys.path.insert(0,'src'); from tier_a.cli import main; main(['--catalog','../../catalog/weaving/','--results-dir','./results/weaving'])"`

**Decline-verdict guidance (per `research/trades/weaving/DECLINE-VERDICT.md`):**
- Target niches: luxury/specialty handwoven textiles, heritage/natural-dye, therapeutic/educational, custom/commission, repair-alteration
- Do NOT target commodity cloth production
- Key falsifier: **fiber-sourcing** — every entry must declare whether it uses purchased industrial yarn or integrates spinning

**Key weaving-specific schema differences:**
- `throughput` block: `meters_per_day`, `warp_width_cm`, `pattern_complexity` (plain/twill/pattern/tapestry)
- `fiber_source_declaration` (required): industrial-yarn-purchased / local-fiber-spun / integrated-spinning / heritage-fiber
- `loom_type` (required): backstrap / rigid-heddle / floor-loom-4shaft / floor-loom-8shaft / drawloom / power-loom
- `humidity_control_required`: boolean (wool/silk = true; cotton = false typically)
- `energy_source` weaving enum: no-power / electric-lighting-only / electric-power-loom / hybrid
- `operator_skill_floor`: rigid-heddle-novice / journeyman-weaver / master-weaver

---

## The 15-Entry Manifest

Per DECLINE-VERDICT.md guidance, the catalog targets restorable niches. The 15 entries distribute across four groups:

### Group A — Luxury / Specialty (5 entries)

High-margin, low-volume handwoven textiles that industrial production cannot replicate at equivalent aesthetic quality. This group tests the premium-market hypothesis for handwoven goods.

1. **weave-001 — Handwoven Tapestry Studio** — floor loom, market-primary, small-city, custom and gallery-market tapestry commissions.
2. **weave-002 — Heritage Wool / Natural-Dye Workshop** — floor loom, market + civic, town, natural-dye and heritage-breed wool focus with cultural-preservation angle.
3. **weave-003 — Architectural Textile Studio** — large floor loom, market-primary, small-city, large-format commissions for interior and architectural installations.
4. **weave-004 — Natural Fiber Fashion Atelier** — floor loom + warping, market-primary, small-city, luxury slow-fashion yardage and finished garments.
5. **weave-005 — Custom Rug & Upholstery Studio** — frame loom + floor loom, market-primary, town/city, custom furnishing textiles for residential and commercial interiors.

### Group B — Heritage / Cultural (3 entries)

Heritage and cultural-revival weaving traditions where the product itself is inseparable from the cultural knowledge; industrial substitution is structurally difficult.

6. **weave-006 — Traditional / Ethnic Weaving Revival** — backstrap + frame, market + civic, town, community-specific cultural-textile revival with civic-preservation argument.
7. **weave-007 — Coverlet & Americana Revival** — 4-shaft floor loom, market-primary, village/town, American frontier double-weave coverlet tradition from Plan B research.
8. **weave-008 — Japanese-style Textile Studio** — drawloom / dobby adapted, specialty market, small-city, complex Japanese pattern-weave tradition (kasuri, nishiki).

### Group C — Community / Coop / Educational (5 entries)

Shared, institutional, and therapeutic weaving models that justify coop and civic lens viability where market-primary operations cannot sustain themselves alone.

9. **weave-009 — Rigid Heddle Tool-Library** — rigid-heddle looms shared, coop-primary, town, low-capital shared-access model for beginning weavers.
10. **weave-010 — Community Fiber Arts Center** — floor loom coop, coop + civic, town/city, multi-member shared studio with instruction.
11. **weave-011 — Therapeutic Weaving Workshop** — floor loom, civic-primary, small-city, hospital or rehabilitation-center partnership.
12. **weave-012 — Apprentice Training Loom Studio** — floor loom multi-station, coop + civic, town/city, vocational weaving program.
13. **weave-013 — Production Weaving Cooperative** — floor loom × 6, coop-primary, small-city, B2B specialty cloth supply to fashion and interior-design clients.

### Group D — Minimum-viable / Stress-test (2 entries)

14. **weave-014 — Backstrap Home Studio** — backstrap loom, village-only, minimum capital, stress-test of viability floor.
15. **weave-015 — Artist-Designer Collaboration Studio** — floor loom shared, market + coop, small-city, studio pairing model where weaver and textile designer share resources.

### Context-Matrix Coverage

The 15 entries collectively span the 9-cell matrix (3 scales × 3 lenses). Every cell has at least 2 entries claiming `good` or `marginal`. Variance enables Tier A simulation to produce meaningful results per cell.

---

## Task Index (same as Plan C)

| # | Task | Creates |
|---|---|---|
| 1 | Catalog manifest / README | `catalog/weaving/README.md` (expand stub) |
| 2 | Weaving schema extension | `catalog/weaving/SCHEMA.md` (expand stub) |
| 3 | Entry weave-001 Handwoven Tapestry Studio | `catalog/weaving/entries/001-handwoven-tapestry-studio.md` |
| 4 | Entry weave-002 Heritage Wool / Natural-Dye Workshop | `catalog/weaving/entries/002-heritage-wool-natural-dye.md` |
| 5 | Entry weave-003 Architectural Textile Studio | `catalog/weaving/entries/003-architectural-textile-studio.md` |
| 6 | Entry weave-004 Natural Fiber Fashion Atelier | `catalog/weaving/entries/004-natural-fiber-fashion-atelier.md` |
| 7 | Entry weave-005 Custom Rug & Upholstery Studio | `catalog/weaving/entries/005-custom-rug-upholstery-studio.md` |
| 8 | Entry weave-006 Traditional / Ethnic Weaving Revival | `catalog/weaving/entries/006-traditional-ethnic-weaving-revival.md` |
| 9 | Entry weave-007 Coverlet & Americana Revival | `catalog/weaving/entries/007-coverlet-americana-revival.md` |
| 10 | Entry weave-008 Japanese-style Textile Studio | `catalog/weaving/entries/008-japanese-textile-studio.md` |
| 11 | Entry weave-009 Rigid Heddle Tool-Library | `catalog/weaving/entries/009-rigid-heddle-tool-library.md` |
| 12 | Entry weave-010 Community Fiber Arts Center | `catalog/weaving/entries/010-community-fiber-arts-center.md` |
| 13 | Entry weave-011 Therapeutic Weaving Workshop | `catalog/weaving/entries/011-therapeutic-weaving-workshop.md` |
| 14 | Entry weave-012 Apprentice Training Loom Studio | `catalog/weaving/entries/012-apprentice-training-loom-studio.md` |
| 15 | Entry weave-013 Production Weaving Cooperative | `catalog/weaving/entries/013-production-weaving-cooperative.md` |
| 16 | Entry weave-014 Backstrap Home Studio | `catalog/weaving/entries/014-backstrap-home-studio.md` |
| 17 | Entry weave-015 Artist-Designer Collaboration Studio | `catalog/weaving/entries/015-artist-designer-collaboration-studio.md` |
| 18 | Cross-entry audit | `reviews/CATALOG-AUDIT-plan-i.md` |
| 19 | Closeout | TRACKER + plans/README + frontmatter |

19 tasks total. Execution is naturally parallelizable in waves:
- Wave 0 (sequential): Tasks 1 + 2 (manifest + schema extension — everything downstream depends on these)
- Wave 2 (parallel × 3 batches): 5 entries per batch (Tasks 3-7, Tasks 8-12, Tasks 13-17)
- Wave 3 (sequential): Task 18 audit, then Task 19 closeout

---

## Task 1: Catalog Manifest / README

**Files:**
- Expand: `catalog/weaving/README.md` (stub exists; this expands it)

**Required content:**

1. **Frontmatter:** trade: weaving, doc_type: catalog-overview, version: "1.0", status: draft, entry_count: 15
2. **Purpose** (~100 words)
3. **The 15-entry manifest** (Groups A/B/C/D with entry IDs + names + one-line descriptions)
4. **Design-space coverage note** — fiber-sourcing falsifier + DECLINE-VERDICT niche targeting
5. **Lens-fit and scale-fit distribution** — 15-row summary table
6. **Entry status tracking** — entry-id | status | last-modified
7. **Sources** pointers

**Commit:** `Plan I task 1: weaving catalog manifest (15-entry overview)`

---

## Task 2: Weaving-Specific Schema Extension

**Files:**
- Expand: `catalog/weaving/SCHEMA.md` (stub exists; this replaces with full content)

**Required content:**

1. **Frontmatter:** trade: weaving, doc_type: schema-extension, extends: catalog/SCHEMA.md, version: "1.0", schema_base_version: "1.1"
2. **Purpose** — one paragraph
3. **Weaving `throughput` block** with `meters_per_day`, `warp_width_cm`, `pattern_complexity`
4. **`energy_source` weaving enum** with capability notes
5. **`loom_type` enumeration** with capability notes
6. **`operator_skill_floor` weaving definitions**
7. **`fiber_source_declaration` field definition** (required for all entries)
8. **`humidity_control_required` field definition**
9. **`first_year_failures` reference list**
10. **Per-niche-group notes** for Wave 2 authors

**Commit:** `Plan I task 2: weaving-specific schema extension`

---

## Tasks 3-17: Per-Entry Authoring (15 entries)

### Shared Structure Across All Entry Tasks

Each entry follows `catalog/SCHEMA.md` v1.1 plus the weaving extension in `catalog/weaving/SCHEMA.md`. Full frontmatter schema as per Plan C, with weaving-specific additions:

```yaml
fiber_source_declaration: industrial-yarn-purchased | local-fiber-spun | integrated-spinning | heritage-fiber
loom_type: backstrap | rigid-heddle | floor-loom-4shaft | floor-loom-8shaft | drawloom | power-loom
humidity_control_required: {boolean}
throughput:
  meters_per_day: {decimal}
  warp_width_cm: {integer}
  pattern_complexity: plain | twill | pattern | tapestry
energy_source: no-power | electric-lighting-only | electric-power-loom | hybrid
operator_skill_floor: rigid-heddle-novice | journeyman-weaver | master-weaver
```

**Required prose sections:** Summary, Design rationale, Historical lineage, Key assumptions, Known risks / failure modes, Target niche(s) and competitive positioning, Iteration log.

### Per-Entry Self-Review Checklist

- [ ] All required frontmatter fields populated
- [ ] `fiber_source_declaration` present and consistent with Key Assumptions
- [ ] `loom_type` specified and consistent with `energy_source` and throughput
- [ ] `humidity_control_required` populated (true for wool/silk; false for cotton typical; justify if non-standard)
- [ ] Conditional fields populated iff their trigger condition holds
- [ ] Every numeric field cited or carries `[CITATION-NEEDED: ...]`
- [ ] `sim_params` cross-checks against throughput (meters_per_day × warp_width as area equivalent)
- [ ] `first_year_failures` 2-4 items with `serviceable_by` per item
- [ ] Pricing validation explicit
- [ ] Regulatory notes terse (3 lines max)
- [ ] Prose sections all present and non-trivial
- [ ] No `docs/superpowers/...` paths
- [ ] No marketing language (STYLE-GUIDE §7)
- [ ] No romanticism (STYLE-GUIDE §4)
- [ ] Historical lineage cites a specific chapter passage

### Per-Entry Commit

```bash
git add catalog/weaving/entries/{NNN}-{slug}.md
git commit -m "Plan I task {N}: weave-{NNN} {short-name}"
```

---

### Task 3-specific — weave-001 Handwoven Tapestry Studio

**Target niche:** High-end tapestry for gallery, collector, and interior-design commissions.

**Key parameters:**
- `loom_type`: floor-loom-8shaft or high-warp tapestry frame. Footprint: 30-50 m². Capital: $15,000-$50,000.
- `fiber_source_declaration: industrial-yarn-purchased` (specialty dyed wool and linen) or `local-fiber-spun`.
- `humidity_control_required: true` (wool warp tension sensitive to humidity change).
- Operator: master-weaver. 1-2 operators.
- Small-city: market-good. Throughput: 0.3-1.5 m²/day (tapestry weave is slow; state the unit clearly).

**Commit:** `Plan I task 3: weave-001 Handwoven Tapestry Studio`

---

### Task 4-specific — weave-002 Heritage Wool / Natural-Dye Workshop

**Target niche:** Heritage-breed wool + natural dye; cultural-preservation civic angle available.

**Key parameters:**
- `loom_type`: floor-loom-4shaft or floor-loom-8shaft. Footprint: 40-70 m². Capital: $20,000-$60,000.
- `fiber_source_declaration: local-fiber-spun` or `heritage-fiber`.
- `humidity_control_required: true`.
- Operator: journeyman-weaver. 1-3 operators.
- Town: market-marginal + civic-marginal. Civic argument: heritage-preservation; benchmark vs. living-history program cost.

**Commit:** `Plan I task 4: weave-002 Heritage Wool / Natural-Dye Workshop`

---

### Task 5-specific — weave-003 Architectural Textile Studio

**Target niche:** Large-format architectural and interior textiles for commissions.

**Key parameters:**
- `loom_type`: floor-loom-8shaft (wide-format, 180-250 cm warp). Footprint: 60-100 m². Capital: $40,000-$120,000.
- `fiber_source_declaration: industrial-yarn-purchased` (structural-grade synthetic and natural yarns).
- `humidity_control_required: false` (synthetic or cotton-primary construction).
- Operator: master-weaver. 1-3 operators.
- Small-city: market-good. Project-based revenue; `throughput_variance` high (large projects).

**Commit:** `Plan I task 5: weave-003 Architectural Textile Studio`

---

### Task 6-specific — weave-004 Natural Fiber Fashion Atelier

**Target niche:** Luxury slow-fashion handwoven yardage and finished garments.

**Key parameters:**
- `loom_type`: floor-loom-8shaft + warping mill. Footprint: 40-80 m². Capital: $30,000-$90,000.
- `fiber_source_declaration: local-fiber-spun` or `industrial-yarn-purchased` (luxury natural fiber — silk, cashmere, fine merino).
- `humidity_control_required: true` (silk and fine wool tension sensitive).
- Operator: master-weaver. 1-3 operators.
- Small-city: market-good. Fashion-cycle demand dependency is a key risk; must document in Known Risks.

**Commit:** `Plan I task 6: weave-004 Natural Fiber Fashion Atelier`

---

### Task 7-specific — weave-005 Custom Rug & Upholstery Studio

**Target niche:** Custom furnishing textiles for residential and commercial interior clients.

**Key parameters:**
- `loom_type`: frame loom + floor-loom-4shaft. Footprint: 40-80 m². Capital: $20,000-$70,000.
- `fiber_source_declaration: industrial-yarn-purchased` (durable upholstery-grade and rug-weight yarn).
- `humidity_control_required: false` (wool rugs: note if true for specific construction).
- Operator: journeyman-weaver. 1-3 operators.
- Town/small-city: market-good. B2B channel to interior designers is a demand anchor; concentration risk must be noted.

**Commit:** `Plan I task 7: weave-005 Custom Rug & Upholstery Studio`

---

### Task 8-specific — weave-006 Traditional / Ethnic Weaving Revival

**Target niche:** Community-specific cultural textile revival with civic-preservation framing.

**Key parameters:**
- `loom_type`: backstrap + frame (tradition-specific). Footprint: 20-40 m². Capital: $5,000-$25,000.
- `fiber_source_declaration: heritage-fiber` or `local-fiber-spun`.
- `humidity_control_required: variable` (document per tradition; note if humid-climate origin).
- Operator: master-weaver for tradition-holder; journeyman-weaver for trained community practitioners.
- Town: market-marginal + civic-marginal. Cultural-preservation civic argument required; must name the specific tradition and community, not generic "ethnic weaving."

**Commit:** `Plan I task 8: weave-006 Traditional / Ethnic Weaving Revival`

---

### Task 9-specific — weave-007 Coverlet & Americana Revival

**Target niche:** American frontier double-weave coverlet and overshot pattern tradition. Market-primary.

**Key parameters:**
- `loom_type`: floor-loom-4shaft (overshot, M's & O's, or double-weave profile). Footprint: 25-45 m². Capital: $10,000-$35,000.
- `fiber_source_declaration: industrial-yarn-purchased` (cotton warp, wool weft typical of frontier coverlets).
- `humidity_control_required: true` (wool weft dimensional stability).
- Operator: journeyman-weaver. 1-2 operators.
- Village/town: market-marginal (collector and heritage-market niche). Historical lineage must cite Plan B American frontier chapter passage specifically.

**Commit:** `Plan I task 9: weave-007 Coverlet & Americana Revival`

---

### Task 10-specific — weave-008 Japanese-style Textile Studio

**Target niche:** Complex Japanese pattern-weave tradition (kasuri ikat, nishiki brocade, or dobby-woven patterns).

**Key parameters:**
- `loom_type`: drawloom or dobby-adapted floor loom. Footprint: 40-70 m². Capital: $25,000-$80,000.
- `fiber_source_declaration: industrial-yarn-purchased` (silk, fine cotton) or `heritage-fiber`.
- `humidity_control_required: true` (silk dimensional stability; critical for kasuri register).
- Operator: master-weaver. 1-2 operators.
- Small-city: market-marginal (specialist collector market). Cultural-preservation civic angle may be claimed; must benchmark vs. cultural-center programming.

**Commit:** `Plan I task 10: weave-008 Japanese-style Textile Studio`

---

### Task 11-specific — weave-009 Rigid Heddle Tool-Library

**Target niche:** Low-capital shared access; tool-library model for beginning weavers. Canonical low-barrier cooperative entry.

**Key parameters:**
- `loom_type`: rigid-heddle (multiple units, 6-12 looms). Footprint: 25-40 m². Capital: $5,000-$20,000.
- `fiber_source_declaration: industrial-yarn-purchased` (per-member supply; studio may stock starter yarn).
- `humidity_control_required: false`.
- Operator: rigid-heddle-novice for members; journeyman-weaver for supervision/instruction.
- Town: coop-good. Ostrom principles critical; scheduling and booking rules must be substantive.

**Commit:** `Plan I task 11: weave-009 Rigid Heddle Tool-Library`

---

### Task 12-specific — weave-010 Community Fiber Arts Center

**Target niche:** Multi-member shared studio with classes, floor looms, and open studio time.

**Key parameters:**
- `loom_type`: floor-loom-4shaft × 4-8 units. Footprint: 80-150 m². Capital: $40,000-$120,000.
- `fiber_source_declaration: industrial-yarn-purchased` (per-member; studio may stock common yarns).
- `humidity_control_required: true` (climate control for wool-primary studio).
- Operator: journeyman-weaver for instruction; rigid-heddle-novice for open-studio members.
- Town/small-city: coop-good + civic-marginal. Benchmark vs. municipal recreation-center arts program.

**Commit:** `Plan I task 12: weave-010 Community Fiber Arts Center`

---

### Task 13-specific — weave-011 Therapeutic Weaving Workshop

**Target niche:** Hospital or rehabilitation-center partnership. Civic-primary. Rhythm and tactile engagement of weaving as occupational therapy.

**Key parameters:**
- `loom_type`: floor-loom-4shaft (simple, accessible for motor therapy) + rigid-heddle. Footprint: 30-60 m². Capital: $15,000-$50,000.
- `fiber_source_declaration: industrial-yarn-purchased`.
- `humidity_control_required: false` (clinical environment has its own climate systems).
- Operator: journeyman-weaver with occupational-therapy or therapeutic-arts training.
- Small-city: civic-good. Lens_context.civic must include clinical partnership structure, staffing model, and therapeutic-outcome benchmark (not just a cost comparison).

**Commit:** `Plan I task 13: weave-011 Therapeutic Weaving Workshop`

---

### Task 14-specific — weave-012 Apprentice Training Loom Studio

**Target niche:** Vocational weaving training program linked to textile and fashion programs. Coop + civic.

**Key parameters:**
- `loom_type`: floor-loom-4shaft × 4-6 (multi-station teaching configuration). Footprint: 60-100 m². Capital: $30,000-$90,000.
- `fiber_source_declaration: industrial-yarn-purchased`.
- `humidity_control_required: true` (climate control for fiber quality in teaching context).
- Operator: master-weaver for instruction; journeyman-weaver trainees.
- Town/small-city: coop-good + civic-marginal. `apprentice_path` is the defining block; must specify stages, time-to-independent-operation, and succession-note.

**Commit:** `Plan I task 14: weave-012 Apprentice Training Loom Studio`

---

### Task 15-specific — weave-013 Production Weaving Cooperative

**Target niche:** Multi-loom production coop supplying B2B specialty cloth. Walks the closest line to the DECLINE-VERDICT commodity-cloth exclusion; must explicitly document specialty positioning.

**Key parameters:**
- `loom_type`: floor-loom-8shaft × 6. Footprint: 120-200 m². Capital: $80,000-$200,000.
- `fiber_source_declaration: industrial-yarn-purchased` (volume supply required) or `local-fiber-spun` (premium specialty positioning).
- `humidity_control_required: true` (production-quality climate control for consistent warp behavior).
- Operator: journeyman-weaver × 6 concurrent. Coop-primary.
- Small-city: coop-good. Market: marginal (B2B price competition from industrial cloth is the primary risk). Entry MUST state specialty-cloth positioning explicitly and document price premium over industrial-cloth baseline.

**Commit:** `Plan I task 15: weave-013 Production Weaving Cooperative`

---

### Task 16-specific — weave-014 Backstrap Home Studio

**Target niche:** Minimum-capital home-based entry. Stress-test of viability floor.

**Key parameters:**
- `loom_type`: backstrap (minimal capital; no fixed structure). Footprint: 5-10 m². Capital: $200-$1,500.
- `fiber_source_declaration: industrial-yarn-purchased` or `local-fiber-spun`.
- `humidity_control_required: false` (home environment; note if specific fiber requires control).
- Operator: journeyman-weaver minimum (backstrap requires body-tension skill and postural practice; not appropriate for rigid-heddle-novice without instruction).
- Village-only: market-marginal. Regulatory burden minimal; throughput very low (0.5-2 m/day at narrow warp). Expected verdict: marginal-to-fail at market and coop; possible marginal at civic-cultural cells.

**Commit:** `Plan I task 16: weave-014 Backstrap Home Studio`

---

### Task 17-specific — weave-015 Artist-Designer Collaboration Studio

**Target niche:** Shared loom studio pairing weaver-practitioners with textile designers for joint production.

**Key parameters:**
- `loom_type`: floor-loom-8shaft shared (2-3 units). Footprint: 40-70 m². Capital: $25,000-$70,000.
- `fiber_source_declaration: industrial-yarn-purchased` (designer-specified materials; designers may specify unusual fibers).
- `humidity_control_required: true` (mixed fiber; climate control recommended).
- Operator: master-weaver + designer collaborator (roles distinct; IP/attribution rules must be named).
- Small-city: market-good + coop-marginal. Designer partnership is a demand anchor. Entry must name the IP and attribution model as a risk item.

**Commit:** `Plan I task 17: weave-015 Artist-Designer Collaboration Studio`

---

## Task 18: Cross-Entry Audit

**Files:**
- Create: `reviews/CATALOG-AUDIT-plan-i.md`

**Audit checklist:**

1. Schema completeness — every entry passes per-entry self-review checklist
2. `fiber_source_declaration` present and consistent in all 15 entries
3. `loom_type` and `humidity_control_required` present in all 15 entries
4. Lens-fit distribution — balance across market / coop / civic
5. Scale-fit distribution — balance across village / town / small-city
6. Context-matrix coverage — every one of 9 cells has ≥ 2 entries at `good` or `marginal`
7. Entry-ID uniqueness (weave-001 through weave-015)
8. DECLINE-VERDICT compliance — no commodity cloth entries; weave-013 specialty-cloth positioning verified
9. Anti-romanticism hold
10. Citation density and consolidated `[CITATION-NEEDED]` placeholder audit

**Commit:** `Plan I task 18: weaving catalog cross-entry audit`

---

## Task 19: Closeout

**Files touched:**
- Update: `TRACKER.md` (Plan I status → completed)
- Update: `plans/README.md` (Plan I status → completed)
- Update: `plans/2026-04-19-plan-i-catalog-weaving.md` frontmatter (status: completed, completed: date)
- Update: `catalog/weaving/README.md` (entry-status-tracking table populated)

**Commit:** `Plan I task 19: closeout`

---

## Retrospective: Risks and Assumptions

### Risks and Objections

- **Fiber-sourcing falsifier.** Every entry must declare `fiber_source_declaration`. Entries claiming `integrated-spinning` or `local-fiber-spun` must document the spinning supply chain; this is a significant additional capital and skill dependency beyond the loom itself.
- **Throughput unit definition.** `meters_per_day` varies widely by cloth type (tapestry ~0.3 m²/day vs. plain weave ~5 m/day at 60 cm width). Each entry must define the cloth type, warp width, and any area-to-unit conversion used in `sim_params`.
- **Humidity control operating cost.** Entries with `humidity_control_required: true` face significantly higher operating costs if located in non-climate-controlled buildings. Must reflect in `annual_maintenance` and `floor_space_rent_per_year`.
- **Commodity-cloth boundary.** weave-013 (Production Weaving Cooperative) walks closest to the commodity-cloth boundary per DECLINE-VERDICT. This entry must explicitly document specialty-cloth positioning and price premium over industrial baseline.
- **Capital range.** Capital range across entries (backstrap $200 vs. multi-loom coop $200,000) is extremely wide. Tier A simulation should be checked for numerical stability across this range.

### Failure Modes (contingency paths)

- **If schema proves insufficient:** spec-amendment to SCHEMA.md (not silent field addition). Pause authoring; unblock when amendment lands.
- **If weave-013 cannot document specialty positioning:** reclassify to `status: deprecated`; author a replacement entry targeting the same coop + small-city + production cell without commodity-cloth risk.
- **If cross-entry audit shows matrix cells empty:** author replacement entries targeting empty cells; bump Plan I scope.

### Assumptions Now Made Explicit

- DECLINE-VERDICT.md commodity-cloth guidance is binding; plain-weave fabric for commodity textile markets is excluded.
- `fiber_source_declaration`, `loom_type`, and `humidity_control_required` are required fields for all weaving entries.
- `catalog/SCHEMA.md` v1.1 is the canonical schema; `catalog/weaving/SCHEMA.md` extends without contradiction.
- Citation policy continues: `[CITATION-NEEDED: ...]` over fabrication.
- Plan D Tier A simulation CLI handles weaving entries via `--catalog` flag (same Python entry point as smithing and baking).

## Handoff

When Plan I completes:

1. TRACKER updated. Plan I frontmatter `status: completed`.
2. 15 entries exist at `catalog/weaving/entries/*.md`, all schema-complete.
3. Cross-entry audit committed at `reviews/CATALOG-AUDIT-plan-i.md`.
4. Tier A simulation can be run immediately:
   `cd simulations/tier-a-comparator && python -c "import sys; sys.path.insert(0,'src'); from tier_a.cli import main; main(['--catalog','../../catalog/weaving/','--results-dir','./results/weaving'])"`
