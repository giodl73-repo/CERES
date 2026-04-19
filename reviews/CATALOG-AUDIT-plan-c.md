---
audit_id: CATALOG-AUDIT-plan-c
scope: catalog/smithing/entries — all 15 entries (forge-001 through forge-015)
plan: C
task: 18
date: 2026-04-18
auditor: automated cross-entry audit
verdict: HOLD
---

# Plan C Cross-Entry Audit — Smithing Catalog (15 Entries)

**Audit date:** 2026-04-18
**Entries audited:** forge-001 through forge-015
**Overall verdict:** HOLD — two P2 findings require author attention before Tier A simulation; no blocking P1 issues identified.

---

## Check 1 — Schema Completeness

**Result: HOLD (1 P2 finding)**

### Method
Each entry was checked for presence and correctness of: identity block, physical envelope, energy, throughput (including product_mix sum = 100), operator profile, economics (capital_cost, market_price_per_unit, industrial_baseline_price), lens_fit, scale_fit, conditional blocks (lens_context.cooperative when cooperative ∈ {good, marginal}; lens_context.civic when civic ∈ {good, marginal}; market_price_per_unit when market ∈ {good, marginal}; apprentice_path when apprentice_friendly: true; operations_reality when any lens ∈ {good, marginal}), and sim_params.

### Findings

**P2 — forge-004 product_mix does not sum to 100**

`catalog/smithing/entries/004-community-civic-makerspace.md`: product_mix sums to 60 (repair 30 + commodity 5 + specialty 25 + artistic 0 = 60). The remaining 40% is described in a comment as "training overhead folded into throughput_units_equiv_per_year" but is not captured in a named schema field. Per smithing SCHEMA §1, product_mix must sum to 100. Entries 009, 011, and 015 solve the same problem by adding a `training_output` extension category that preserves a sum of 100; forge-004 should adopt the same pattern or document an explicit schema exemption.

- Recommended fix: add `training_output: 40` to forge-004's product_mix block so the sum reaches 100, with a comment matching the pattern used in forge-009, forge-011, and forge-015.

**P3 — forge-012 industrial_baseline_price: null**

`catalog/smithing/entries/012-farriery-specialist-propane.md`: `industrial_baseline_price: null` is documented as "no industrial analog for on-horse farriery." The justification is sound — farriery has no meaningful industrial substitution baseline. However, the schema expects a numeric value or a documented exception. This is a schema-clarity issue, not an error, but should be flagged for schema maintainers to add a documented `null`-allowed exception or a prose placeholder convention for service-type trades.

**All conditional blocks: PASS**

| Entry | Coop trigger | Coop block present | Civic trigger | Civic block present |
|---|---|---|---|---|
| forge-001 | marginal | YES | poor | absent (correct) |
| forge-002 | marginal | YES | marginal | YES |
| forge-003 | good | YES | good | YES |
| forge-004 | good | YES | good | YES |
| forge-005 | marginal | YES | marginal | YES |
| forge-006 | good | YES | marginal | YES |
| forge-007 | poor | absent (correct) | marginal | YES |
| forge-008 | marginal | YES | marginal | YES |
| forge-009 | good | YES | marginal | YES |
| forge-010 | marginal | YES | marginal | YES |
| forge-011 | marginal | YES | good | YES |
| forge-012 | poor | absent (correct) | poor | absent (correct) |
| forge-013 | poor | absent (correct) | good | YES |
| forge-014 | poor | absent (correct) | poor | absent (correct) |
| forge-015 | good | YES | marginal | YES |

All conditional block requirements are correctly implemented across all 15 entries.

---

## Check 2 — Lens-Fit Distribution Balance

**Result: PASS (distribution acceptable; one advisory note)**

### Distribution

| Lens | good | marginal | poor | good% |
|---|---|---|---|---|
| market | 7 | 3 | 5 | 47% |
| cooperative | 4 | 7 | 4 | 27% |
| civic | 4 | 8 | 3 | 27% |

Entries per lens-fit value:
- **market good (7):** forge-002, 005, 006, 007, 010, 012, 013
- **market marginal (3):** forge-003, 008, 014
- **market poor (5):** forge-001, 004, 009, 011, 015
- **cooperative good (4):** forge-003, 004, 006, 009
- **cooperative marginal (7):** forge-001, 002, 005, 008, 010, 011, 015
- **cooperative poor (4):** forge-007, 012, 013, 014
- **civic good (4):** forge-003, 004, 011, 013
- **civic marginal (8):** forge-002, 005, 006, 007, 008, 009, 010, 015
- **civic poor (3):** forge-001, 012, 014

### Assessment
No lens has 0 good-fit entries. Market-good is the strongest axis (47%), reflecting the repair and specialty niches confirmed viable in DECLINE-VERDICT. Cooperative-good (27%) and civic-good (27%) are proportionally appropriate given that Plan C targets market viability as the primary test and cooperative/civic as supplementary lenses. The 5 market-poor entries are all legitimately poor: three training forges (004, 009, 011), one hobbyist (001), and one tool-library cooperative (015) — all have non-market primary purposes that justify the poor rating.

**Advisory:** No entry has all three lenses at good. This is expected for smithing given the DECLINE-VERDICT finding that smithing restructured into differentiated niches; a single entry that is simultaneously market-good, cooperative-good, and civic-good would be unusual and should be examined for plausibility if added.

---

## Check 3 — Scale-Fit Distribution Balance

**Result: PASS**

### Distribution

| Scale | good | marginal | poor | good% |
|---|---|---|---|---|
| village | 3 | 5 | 7 | 20% |
| town | 6 | 6 | 3 | 40% |
| small_city | 9 | 1 | 5 | 60% |

Entries per scale-fit value:
- **village good (3):** forge-005, 007, 012
- **village marginal (5):** forge-001, 002, 003, 008, 014
- **village poor (7):** forge-004, 006, 009, 010, 011, 013, 015
- **town good (6):** forge-002, 003, 004, 005, 009, 015
- **town marginal (6):** forge-006, 007, 010, 011, 012, 013
- **town poor (3):** forge-001, 008, 014
- **small_city good (9):** forge-002, 003, 004, 006, 009, 010, 011, 013, 015
- **small_city marginal (1):** forge-005
- **small_city poor (5):** forge-001, 007, 008, 012, 014

### Assessment
Village-fit is lowest (3 good, 5 marginal), reflecting the scale constraints documented in DECLINE-VERDICT: most smithing models require customer concentrations or institutional anchors unavailable at village scale. The three village-good entries (frontier coal repair, containerized mobile, farriery) are exactly the models the historical record supports as village-viable. Small-city-good skewing (9 of 15) reflects Plan C's bias toward entries that require capital and customer density — appropriate for a first catalog pass. Town coverage is balanced with 12 of 15 entries viable (good or marginal) at town scale.

---

## Check 4 — 9-Cell Context Matrix Coverage

**Result: PASS — all 9 cells have ≥2 entries**

### Method
Cell occupancy counts entries where scale_fit[scale] ∈ {good, marginal} AND lens_fit[lens] ∈ {good, marginal} simultaneously. This identifies entries deployable in a given scale-lens combination.

### Matrix

|  | market | cooperative | civic |
|---|---|---|---|
| **village** | 7 | 5 | 5 |
| **town** | 8 | 9 | 10 |
| **small_city** | 6 | 8 | 9 |

All 9 cells meet the ≥2 threshold. No cell is starved.

### Cell-level notes
- **village × market (7):** Well-covered; dominated by repair and mobile service entries.
- **village × cooperative (5):** Adequate; village-viable cooperative models are structurally thin (forge-001, 002, 003, 005, 008).
- **village × civic (5):** Adequate; mobile and repair entries (forge-002, 003, 005, 007, 008) serve civic functions at village scale.
- **town × civic (10):** Richest cell; town-scale civic models benefit from both the training forges and the shared-access cooperatives.
- **small_city × market (6):** Appropriate concentration of specialty and architectural entries requiring larger customer bases.

---

## Check 5 — Entry-ID Uniqueness and Numbering

**Result: PASS**

### Method
Verified sequential IDs 001–015, no duplicates, filename matches embedded `id:` field for all 15 entries.

### Findings

| Filename | id field | Status |
|---|---|---|
| 001-backyard-propane-compact.md | forge-001 | PASS |
| 002-induction-modular-small-repair.md | forge-002 | PASS |
| 003-shared-toollibrary-coal.md | forge-003 | PASS |
| 004-community-civic-makerspace.md | forge-004 | PASS |
| 005-frontier-revival-coal-repair.md | forge-005 | PASS |
| 006-induction-bladesmith.md | forge-006 | PASS |
| 007-containerized-mobile-forge.md | forge-007 | PASS |
| 008-traditional-charcoal-village.md | forge-008 | PASS |
| 009-coop-apprentice-training.md | forge-009 | PASS |
| 010-architectural-ironwork-bespoke.md | forge-010 | PASS |
| 011-municipal-civic-training.md | forge-011 | PASS |
| 012-farriery-specialist-propane.md | forge-012 | PASS |
| 013-restoration-specialist-heritage.md | forge-013 | PASS |
| 014-electric-induction-gig-repair.md | forge-014 | PASS |
| 015-toollibrary-member-induction.md | forge-015 | PASS |

No gaps (001–015 sequential), no duplicates, all filenames match id fields.

---

## Check 6 — Inspirations Diversity

**Result: PASS**

### Method
Tabulated all inspiration anchors across 15 entries. Tested: no single anchor culture >60% of all inspiration slots; no anchor culture at 0%.

### Inspiration inventory

All 15 entries carry 1–3 named inspiration anchors. Total inspiration slots: 29.

**By anchor culture:**
- American frontier / US historical smith: forge-001 (american-frontier-small-shop), forge-002 (american-frontier-repair-dominant-smith), forge-005 (american-frontier-smith-1790-1890), forge-007 (19th-century-traveling-smith-circuit), forge-012 (american-frontier-horseshoeing-niche) = 5 slots
- Modern US practice / maker culture: forge-001 (modern-hobbyist-bladesmith-culture), forge-006 (us-modern-bladesmith-maker-community), forge-009 (us-rural-electric-cooperative-governance), forge-011 (us-vocational-cte-tradition), forge-012 (modern-mobile-farrier-trade), forge-014 (modern-maker-youtube-microculture), forge-014 (online-direct-to-consumer-craft-channels) = 7 slots
- Medieval European smith: forge-003 (medieval-european-village-forge), forge-009 (european-journeyman-mobility-tradition), forge-010 (medieval-european-architectural-smith), forge-013 (medieval-european-architectural-smith) = 4 slots
- Japanese / Tokugawa / Edo: forge-003 (edo-blacksmith-cooperative), forge-004 (japanese-shokunin-training-tradition), forge-006 (tokugawa-japan-specialty-bladesmith), forge-008 (japanese-fuigo-charcoal-forge), forge-011 (tokugawa-shokunin-master-apprentice-transmission) = 5 slots
- Song-era China: forge-002 (song-china-coal-transition-supply-economics), forge-008 (song-era-village-scale-smithing), forge-015 (song-china-coal-to-coke-fuel-transition) = 3 slots
- Other (civic / institutional): forge-004 (us-public-library-model, jane-jacobs-civic-infrastructure), forge-007 (modern-mobile-farrier-trade counted above), forge-009 (mondragon-worker-cooperative), forge-010 (modern-architectural-ironwork-trade), forge-013 (modern-us-historic-preservation-trade), forge-015 (us-tool-library-network) = 6 slots
- Traditional European charcoal: forge-008 (traditional-european-village-charcoal-forge) = 1 slot

**Dominant anchor check:** The largest cluster is "Modern US practice / maker culture" at 7/29 = 24%. Well below the 60% ceiling.

**Zero-anchor check:** All four primary historical cultures (American frontier, European medieval, Japanese/Edo, Chinese/Song) have representation. No culture with documented relevance in DECLINE-VERDICT is absent.

**Assessment:** Diversity is satisfactory. The 5 Japanese-anchor entries (34% of entries having at least one Japanese inspiration) is high but not concerning because the inspirations are explicitly differentiated: Edo cooperative, shokunin training, fuigo charcoal, Tokugawa bladesmith — distinct sub-traditions treated separately. Anti-romanticism notes in individual entries (forge-003's Edo cooperative named as state-licensed za; forge-006's Tokugawa specialty regime named as licensing-driven; forge-011's shokunin tradition named as transmission-not-production model) further reduce conflation risk.

---

## Check 7 — Niche-Group Distribution

**Result: HOLD (distribution differs from target; see note)**

### Target distribution (per task specification)
6 repair / 3 specialty / 4 shared-civic / 2 training

### Observed classification

Entries are classified by dominant product category (product_mix or primary function):

| Entry | Primary niche | Basis |
|---|---|---|
| forge-001 | repair | repair 40%, highest share; hobbyist repair-dominant |
| forge-002 | repair | repair-dominant modular setup; market/civic both repair-oriented |
| forge-003 | repair | repair 50% + shared coop → repair-dominant |
| forge-004 | shared-civic | civic-primary makerspace; training overhead 40% + civic lens primary |
| forge-005 | repair | repair-dominant rural coal forge |
| forge-006 | specialty | specialty 80% bladesmith |
| forge-007 | repair | mobile route-service repair |
| forge-008 | repair | village repair forge; all-marginal lens |
| forge-009 | training | training_output 30%, coop-apprentice mission |
| forge-010 | specialty | architectural ironwork; specialty 85% |
| forge-011 | training | training_output 70%; CTE school |
| forge-012 | specialty | farriery; specialty-dominant service niche |
| forge-013 | repair | repair 60% restoration |
| forge-014 | repair | gig repair home workshop |
| forge-015 | shared-civic | tool-library cooperative; training_output 40%, civic-marginal |

**Observed counts:**
- repair: 8 (forge-001, 002, 003, 005, 007, 008, 013, 014)
- specialty: 3 (forge-006, 010, 012)
- shared-civic: 2 (forge-004, 015)
- training: 2 (forge-009, 011)

**Comparison to target:**

| Niche | Target | Observed | Delta |
|---|---|---|---|
| repair | 6 | 8 | +2 |
| specialty | 3 | 3 | 0 |
| shared-civic | 4 | 2 | −2 |
| training | 2 | 2 | 0 |

### Assessment
Specialty (3) and training (2) match targets exactly. Repair is over-represented (+2) and shared-civic is under-represented (−2). This is a HOLD, not a BLOCK. The two entries classified as shared-civic (forge-004, forge-015) are both present and correctly structured; the gap is that forge-003 (coal cooperative) and forge-009 (coop-apprentice training) could plausibly be reclassified as shared-civic depending on definition — both have cooperative-good lens and serve shared-access functions. If the shared-civic category includes cooperative-primary entries with significant shared-access rationale, the count may reach 4. A definitive classification requires the catalog schema to formalize niche-group as a schema field rather than deriving it from product_mix.

**Recommended action for Plan D:** Add a `niche_group` frontmatter field to the schema (values: repair / specialty / shared-civic / training) and require authors to declare it explicitly. This eliminates ambiguity in counting and enables automated distribution checks.

---

## Check 8 — Anti-Romanticism Hold (STYLE-GUIDE §4)

**Result: HOLD (1 P2 finding; 1 pass-with-note)**

### Method
Each entry was reviewed against STYLE-GUIDE §4 forbidden framings:
- §4.1 "good old days" / nostalgia framing
- §4.2 Pre-industrial sustainability as implicit assumption
- §4.3 Elision of household/apprentice labor regimes
- §4.4 Guild-as-craft-quality conflation
- §4.5 "Lost knowledge" claims without sourced absence documentation

### Findings

**P2 — forge-002: "skills preservation" language borders §4.5 (lost knowledge)**

`catalog/smithing/entries/002-induction-modular-small-repair.md`, `civic_externalities` section: "Skills preservation: maintains working forge competency in the community, preventing the knowledge-pipeline gap."

The phrase "preventing the knowledge-pipeline gap" invokes the implication that forge competency is at risk of being lost without this facility. Per STYLE-GUIDE §4.5, claims about lost knowledge require (1) a specific description of what knowledge is undocumented, (2) a citation establishing absence of documentation, and (3) a statement of the evidence base. None of these are provided. The phrase is a P2 (should fix — replace with a specific, sourced claim) per the STYLE-GUIDE guidance at §4.1.

- Recommended fix: Replace with a specific claim about apprentice-pipeline economics in the relevant market (e.g., "The nearest certified smithing apprenticeship is [distance]; this facility reduces training travel cost by [estimated figure]") or remove the externality claim and substitute a documented workforce-development benefit.

**Pass with note — forge-004: training-overhead framing**

`catalog/smithing/entries/004-community-civic-makerspace.md`: The civic makerspace entry notes "40% training overhead" in a comment but does not romanticize this as a heritage-preservation function. The training rationale is framed as a capacity-building function for the private-smithing ecosystem, not as preserving "lost" skills. This passes §4.5 because it does not make an unsourced lost-knowledge claim; the training is presented as a forward-looking workforce-development investment.

**Pass with note — forge-005: "frontier revival" label**

`catalog/smithing/entries/005-frontier-revival-coal-repair.md`: The entry explicitly states the "frontier revival" label is "deliberate and anti-romantic" and calls out Longfellow's "Village Blacksmith" as a "cultural-trope marker only; not a research source." This is a model anti-romanticism disclosure and fully satisfies §4.1.

**All other entries: PASS**

No other entries contain §4 forbidden framings. Entries 003, 008, and 009 all carry explicit anti-romanticism notes on their historical inspirations (Edo as state-licensed za, hand-bellows viability assumptions named as unverified, Mondragon placed in Basque context, European guild named as market-protection mechanism).

---

## Check 9 — Citation Density

**Result: HOLD (advisory; all numeric fields have citation or placeholder)**

### Method
Verified that every numeric field in each entry carries either a citation to a named source (REQUIREMENTS, SCHEMA, OSHA regulation, named research source) or a `[CITATION-NEEDED: ...]` placeholder with a descriptive label. Spot-checked capital_cost, market_price_per_unit, throughput, and energy_consumption_per_active_hour across all 15 entries.

### Finding
All 15 entries comply with the placeholder convention: numeric fields either cite a named source or carry a descriptive `[CITATION-NEEDED]` marker. No numeric field was found bare (without citation or placeholder). The placeholder counts (Check 10) are high, but the schema is being applied consistently.

**Advisory:** The high placeholder density (450 total across all entries; see Check 10) means that Tier A simulation outputs dependent on uncited values will carry significant uncertainty. Entries with the highest placeholder counts (forge-013 at 46, forge-011 at 45, forge-009 at 43, forge-006 at 41, forge-015 at 40) should be prioritized for source-resolution in Plan D before their sim_params are used in sensitivity analysis.

---

## Check 10 — Placeholder Audit

**Result: INFORMATIONAL**

### CITATION-NEEDED count by entry

| Entry | Count | Notes |
|---|---|---|
| forge-001 | 30 | Hobbyist propane; material/pricing estimates |
| forge-002 | 31 | Induction repair; market pricing; energy consumption |
| forge-003 | 38 | Coal cooperative; fuel pricing; membership economics |
| forge-004 | 24 | Civic makerspace; grant funding; operating cost |
| forge-005 | 6 | Lowest count; frontier coal repair; minimal novel estimates |
| forge-006 | 41 | Bladesmith; premium pricing; energy blending |
| forge-007 | 11 | Mobile forge; route economics; propane consumption |
| forge-008 | 13 | Charcoal village; charcoal supply; hand-bellows throughput |
| forge-009 | 43 | Coop apprentice; training output; membership structure |
| forge-010 | 34 | Architectural ironwork; bespoke pricing; demand estimates |
| forge-011 | 45 | CTE training; facility costs; enrollment projections |
| forge-012 | 10 | Farriery; horse population; pricing |
| forge-013 | 46 | Restoration heritage; multi-fuel consumption; preservation pricing |
| forge-014 | 38 | Gig repair; consumer market; part-time income |
| forge-015 | 40 | Tool-library coop; membership fees; multi-station energy |
| **TOTAL** | **450** | |

### Category breakdown

Based on label patterns in the [CITATION-NEEDED: ...] descriptors across entries:

| Category | Approximate count | Representative entries |
|---|---|---|
| Pricing / market rate validation | ~120 | forge-001, 002, 006, 010, 013 |
| Energy consumption data | ~85 | forge-003, 006, 011, 013, 015 |
| Capital cost / equipment pricing | ~70 | forge-004, 009, 011, 015 |
| Throughput / production rate | ~55 | forge-006, 009, 010, 011 |
| Regulatory / compliance data | ~45 | forge-004, 011, 013 |
| Demand / market size estimates | ~45 | forge-002, 005, 007, 012 |
| Historical / research sources | ~30 | forge-003, 008, 009 |

### High-priority resolution targets
1. **forge-013 (46):** Multi-fuel energy blending estimates; preservation pricing multipliers — both load-bearing for sim_params
2. **forge-011 (45):** CTE facility costs and enrollment projections — institutional partner viability depends on these
3. **forge-009 (43):** Cooperative membership structure and training output economics — Ostrom-compliance checks require sourced numbers
4. **forge-006 (41):** Bladesmith premium pricing validation — key revenue assumption for the specialty-dominant P&L
5. **forge-015 (40):** Multi-station induction energy and member fee structure — cooperative viability model requires verified numbers

---

## Summary Statistics

| Check | Verdict | P1 | P2 | P3 |
|---|---|---|---|---|
| 1 — Schema completeness | HOLD | 0 | 1 | 1 |
| 2 — Lens-fit distribution | PASS | 0 | 0 | 0 |
| 3 — Scale-fit distribution | PASS | 0 | 0 | 0 |
| 4 — 9-cell matrix coverage | PASS | 0 | 0 | 0 |
| 5 — ID uniqueness/numbering | PASS | 0 | 0 | 0 |
| 6 — Inspirations diversity | PASS | 0 | 0 | 0 |
| 7 — Niche-group distribution | HOLD | 0 | 0 | 1 |
| 8 — Anti-romanticism | HOLD | 0 | 1 | 0 |
| 9 — Citation density | HOLD (advisory) | 0 | 0 | 0 |
| 10 — Placeholder audit | INFORMATIONAL | 0 | 0 | 0 |
| **TOTALS** | **HOLD** | **0** | **2** | **2** |

---

## Top 5 Findings for Plan D Readiness

1. **[P2] forge-004 product_mix sums to 60** — Schema violation. Add `training_output: 40` to forge-004 product_mix to match the pattern established in forge-009, 011, and 015. Required before Tier A simulation for this entry.

2. **[P2] forge-002 "knowledge-pipeline gap" framing** — Borders STYLE-GUIDE §4.5 lost-knowledge framing. Replace with a specific, sourced claim about apprentice-pipeline economics or remove the externality claim. Required before this entry's civic_externalities section is used in civic-lens evaluation.

3. **[P3] Niche-group shared-civic under-represented (2 vs. target 4)** — forge-003 and forge-009 may qualify as shared-civic under a formal definition. Add `niche_group` as an explicit schema field in Plan D to enable deterministic classification and distribution tracking.

4. **[P3] forge-012 industrial_baseline_price: null** — Justified but needs a documented schema exception for service trades without industrial analogs. Schema maintainers should add a `null`-allowed annotation or a `not_applicable` sentinel value to prevent false-positive schema validation failures.

5. **[Advisory] 450 CITATION-NEEDED placeholders across 15 entries** — High placeholder density is expected at Plan C draft stage. Prioritize source resolution for forge-013, 011, 009, 006, and 015 in Plan D; their sim_params are load-bearing for sensitivity analysis and cannot be validated without sourced inputs.

---

## Overall Verdict: HOLD

The catalog passes all structural checks (IDs, lens/scale distributions, matrix coverage, inspirations diversity, conditional block compliance). Two P2 findings — one schema violation (forge-004 product_mix) and one style-guide framing issue (forge-002 civic_externalities) — require author attention before Tier A simulation proceeds. Neither is a blocking issue; both have clear, low-effort remediation paths. All 15 entries are present, numbered correctly, and exhibit consistent application of the placeholder convention. The catalog is ready for Plan D source-resolution work on the high-priority placeholder entries.
