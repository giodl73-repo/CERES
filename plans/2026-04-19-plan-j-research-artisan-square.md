---
id: plan-j-research-artisan-square
name: Research Corpus — Artisan Square Facility Model
description: Establish Artisan Square as a CERES-compatible "building-operator trade"; define facility functional requirements, schema extension, real-world benchmarking, and market-viability foundation for Plan K catalog
status: completed
version: "1.1"
created: 2026-04-19
completed: 2026-04-19
last_modified: 2026-04-19
phase: 1
subsystem: research-corpus
trade: artisan-square
depends_on: [plan-a-scaffolding]
blocks: [plan-k-catalog-artisan-square]
estimated_effort: 2-3 weeks focused
primary_artifact_type: research
success_signal: >
  Artisan Square established as a CERES trade with a schema extension,
  functional requirements document, real-world benchmark analysis (3-5
  comparable facilities), market context per facility type (Type A/B/combined),
  a DECLINE-VERDICT analog (when does the building-operator model work vs.
  fail?), and SOURCES.md with placeholder audit. Plan K catalog authoring
  can begin.
spec: specs/2026-04-19-artisan-square-design.md
---

# Plan J: Research Corpus — Artisan Square Facility Model

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Establish Artisan Square as a researchable "trade" within the CERES framework — the trade being building and operating a multi-trade artisan production facility — so that Plan K can author 15 facility catalog entries the same way Plans C/G/I authored craft entries.

**Architecture:** Research-heavy authoring, like Plans B/F/H. The "practitioner" is the building developer/operator (not a craftsperson). The "equipment" is the building itself plus its shared infrastructure. The functional requirements describe what a facility MUST do to serve artisan tenants — a new category within CERES.

**Tech Stack:** Markdown only. No code until Plan L.

**Source of truth:** `specs/2026-04-19-artisan-square-design.md` — especially Sections 4, 5, 6 (physical design, tenant model, economics). Everything in this plan elaborates those sections into research-grade documents.

**Citation policy:** `[CITATION-NEEDED: <claim>]` over fabrication. Real-world comparable facilities (Artisans Asylum, La Cocina, Manchester Craft Centre, East End Maker Hub, The Artisan Factory) are the primary benchmarks — cite them properly.

**Key difference from craft-trade research (Plans B/F/H):** There is no four-culture historical analysis. The "history" of multi-trade artisan buildings is contemporary — the Sola Salons model (2004 to present), makerspace movement (2008+), food incubator movement (2010+). The cultural analysis is replaced by market analysis: where does this model work and what makes it fail?

---

## Trade Definition

**The trade being researched:** Building and operating a shared-infrastructure artisan production facility (Artisan Square). The "practitioner" is the building developer/operator.

**Why this is a CERES trade:** The Artisan Square operator faces the same market/coop/civic viability questions as a smith or baker. They need capital (building), operating costs (staff, insurance, maintenance), a customer base (tenants), and a viable revenue model. The Tier A simulation can evaluate whether an Artisan Square pencils out under each economic lens the same way it evaluates a forge or bakery — by modeling the building as an entry in the catalog.

---

## New Directory Structure

```
research/
├── trades/
│   └── artisan-square/
│       ├── REQUIREMENTS.md          (Task 5 — facility functional requirements)
│       ├── FACILITY-TYPES.md        (Task 6 — comparable to HISTORICAL-FORMS.md)
│       ├── MARKET-VERDICT.md        (Task 7 — comparable to DECLINE-VERDICT.md)
│       └── SOURCES.md               (Task 8)
│
catalog/
└── artisan-square/
    ├── README.md                    (stub — populated by Plan K)
    ├── SCHEMA.md                    (Task 2 — artisan-square schema extension)
    └── entries/
        └── .gitkeep                 (Plan K will populate)
```

---

## Task Index

| # | Task | Creates |
|---|---|---|
| 1 | Schema extension for artisan-square trade | `catalog/artisan-square/SCHEMA.md` |
| 2 | Catalog stub | `catalog/artisan-square/README.md` |
| 3 | Research: Type A facility (heavy trades) | `research/trades/artisan-square/type-a-heavy.md` |
| 4 | Research: Type B facility (light trades) | `research/trades/artisan-square/type-b-light.md` |
| 5 | Research: Combined campus model | `research/trades/artisan-square/combined-campus.md` |
| 6 | Cross-facility functional requirements | `research/trades/artisan-square/REQUIREMENTS.md` |
| 7 | Facility type comparison | `research/trades/artisan-square/FACILITY-TYPES.md` |
| 8 | Market viability verdict | `research/trades/artisan-square/MARKET-VERDICT.md` |
| 9 | Consolidated bibliography | `research/trades/artisan-square/SOURCES.md` |
| 10 | Closeout | TRACKER + plans/README + frontmatter |

---

## Task 1 — Schema Extension for Artisan-Square Trade

**Files:**
- Create: `catalog/artisan-square/SCHEMA.md`

The artisan-square schema extends `catalog/SCHEMA.md` v1.1. The "entry" being described is a **facility configuration** — a specific Artisan Square building design. The fields describe the building, not the tenants.

**Required schema additions:**

```yaml
# Artisan-square-specific fields (in trade_specific: block)

trade_specific:
  # Facility composition
  facility_type: Type-A-only | Type-B-only | combined-campus | small-town-lite
  total_studios: {integer}
  type_a_studios: {integer}   # forge/metalwork/kiln
  type_b_studios: {integer}   # baking/weaving/fiber/leather
  anchor_training_studios: {integer}  # below-market, pipeline function

  # Infrastructure ratings
  main_electrical_service_amps: {integer}   # 600-1200A typical
  has_3phase: {boolean}
  has_industrial_exhaust_stack: {boolean}
  has_food_grade_exhaust_stack: {boolean}
  has_commissary_umbrella_license: {boolean}

  # Occupancy/zoning
  ibc_occupancy_classification: "F-2/B mixed" | "F-2 only" | "B only"
  zoning_required: light-industrial | mixed-use | retail-commercial

  # Tenant economics (operator perspective)
  avg_monthly_rent_per_studio: {integer}    # USD
  target_occupancy_rate: {decimal}          # 0.85 typical
  anchor_studio_subsidy_per_month: {integer}

  # Build model
  build_approach: adaptive-reuse | purpose-built-new | purpose-built-shell
  location_prototype: location-1-proof | chain-prototype | small-town-variant
```

**throughput reinterpretation for artisan-square:**

For the CERES Tier A simulation, "throughput" for a facility entry represents studios rented per year (occupancy × 12 months × studio count). The economics flow from occupancy, not production output.

```yaml
throughput:
  target_occupancy_rate: 0.85
  studios_rented_per_month: {integer}  # total_studios × occupancy_rate
  annual_tenant_months: {integer}      # studios × occupancy × 12
  graduation_rate_per_year: {decimal}  # typical 20-30% of tenants graduate annually
```

**market_price reinterpretation:**

`market_price_per_unit` = average monthly rent per studio. `throughput_units_equiv_per_year` = studio-months rented per year. This maps cleanly to the existing Tier A lens formulas.

**Commit:**
```bash
git -C /c/src/artisan add catalog/artisan-square/
git -C /c/src/artisan commit -m "Plan J task 1: artisan-square schema extension"
```

---

## Task 2 — Catalog Stub

**Files:**
- Create: `catalog/artisan-square/README.md`
- Create: `catalog/artisan-square/entries/.gitkeep`

Stub README: one paragraph explaining the artisan-square catalog is forthcoming in Plan K. Lists the 15 anticipated facility configurations (by facility_type and location_prototype) as placeholders. Pattern: `catalog/smithing/README.md`.

**Commit:**
```bash
git -C /c/src/artisan add catalog/artisan-square/
git -C /c/src/artisan commit -m "Plan J task 2: artisan-square catalog stub"
```

---

## Task 3 — Research: Type A Facility (Heavy Trades)

**Files:**
- Create: `research/trades/artisan-square/type-a-heavy.md`

**Frontmatter:**
```yaml
---
facility_type: Type-A-heavy
trade: artisan-square
trades_served: [smithing, metalwork, pottery-kiln]
status: draft
version: "1.0"
review_status: {panel: pending, editorial: pending}
sources_count: {count}
---
```

**Required sections (~1500-2500 words):**

1. **Facility context** — Who operates Type A? What tenant profile fills these studios? What distinguishes Type A from a generic makerspace (individual dedicated studios vs. shared floor time)?

2. **The forge/metalwork studio** — Physical requirements: concrete floor (150 lb/sq ft), 14 ft clearance, 200A 3-phase sub-panel, industrial exhaust connection (≥2,000 CFM per station). Sound isolation (STC 55+). Eye-wash station. What a tenant builds in this space vs. what they'd need standalone.

3. **The pottery/kiln studio** — Physical requirements: kiln pad (1,000+ lb floor load locally), dedicated kiln ventilation, 240V 50A minimum for electric kiln or gas line for gas kiln. Comparison: electric vs. gas kiln implications for building design.

4. **Type A shared infrastructure** — Industrial exhaust stack spec (2-hr fire-rated chase from studio to roofline; makeup air unit; dampers). The case for 3-phase over single-phase at the building level. Fire suppression upgrade (NFPA 13, Class D requirements for metalwork). IBC Group F-2 light manufacturing occupancy implications.

5. **Tenant economics from operator's perspective** — What does a Type A studio rent for? What occupancy rate is achievable given the thin tenant pool for heavy-trade practitioners? Real-world benchmark: East End Maker Hub heavy-fab rates; Artisans Asylum shared metalwork shop fees vs. dedicated studio rates.

6. **Operator risks specific to Type A** — Zoning (light-industrial required; harder to find in mixed-use districts). Environmental review (combustion byproducts, noise). Tenant skill-floor enforcement (a forge is dangerous; operator needs minimum competency verification — not employment, but a safety certification requirement in the lease).

7. **Functional requirements learned** — What must a Type A facility DO in trade-agnostic terms: power density (kW/sq ft), exhaust capacity (CFM/studio), floor load rating, sound attenuation, occupancy classification. Feed `REQUIREMENTS.md`.

8. **Sources.**

**Anti-romanticism:** The CERES STYLE-GUIDE §4 anti-romanticism rules apply. Artisan Square is not "restoring the village forge" — it is an infrastructure investment that reduces the capital barrier for market-path artisan operators. The "community" framing is secondary to the business-viability framing.

**Commit:**
```bash
git -C /c/src/artisan add research/trades/artisan-square/type-a-heavy.md
git -C /c/src/artisan commit -m "Plan J task 3: Type A heavy-trades facility research"
```

---

## Task 4 — Research: Type B Facility (Light Trades)

**Files:**
- Create: `research/trades/artisan-square/type-b-light.md`

**Frontmatter:**
```yaml
---
facility_type: Type-B-light
trade: artisan-square
trades_served: [baking, weaving, leather, ceramics-light, soap-candle]
status: draft
version: "1.0"
review_status: {panel: pending, editorial: pending}
sources_count: {count}
---
```

**Required sections (~1500-2500 words):**

1. **Facility context** — The commissary licensing umbrella: how La Cocina SF structured it; how it maps to Type B; what a Type A commercial kitchen license actually covers (multiple operators producing different products); what the health department inspection regime looks like for an umbrella operation.

2. **The baking studio** — Physical requirements: 240V 60A, floor drain, NSF-rated hot-water line, food-grade exhaust connection (grease interceptor), NSF flooring. How cottage-food licensing interacts with the commissary umbrella (some states allow cottage-food-scale producers to operate under commissary vs. needing standalone inspection). Real-world benchmark: La Cocina SF per-studio economics.

3. **The fiber arts/weaving studio** — Physical requirements: 240V lighting-only is sufficient for hand looms; 30-40A for electric floor looms; humidity control (65-75% RH for wool, 65-70% for silk); no exhaust required (vs. baking). The dye studio variant (if included): requires floor drain, hot water, ventilation, separate from food spaces.

4. **Type B shared infrastructure** — Food-grade exhaust stack (grease interceptor, separate from Type A). Commissary umbrella license: tenant registration process, health dept inspection calendar, shared sanitation records. IBC Group B (business) or F-2 (light manufacturing) designation — Type B often qualifies for mixed-use/retail zoning, which opens up more desirable sites than light-industrial.

5. **Tenant economics from operator's perspective** — Type B rent ranges. Occupancy outlook: bakers, weavers, and fiber artists represent a larger practitioner pool than forge operators. Real-world comps: shared commercial kitchen rent rates ($20-40/hr or $800-1,500/month dedicated). The commissary umbrella value: saves tenants $5-10k/year in individual licensing fees.

6. **Operator risks specific to Type B** — Health department compliance burden (the operator is the commissary licensee; if one tenant fails an inspection, it can affect the whole umbrella). How to structure tenant compliance obligations in the lease. Humidity system maintenance (failure causes mold in fiber studios; HVAC monitoring required).

7. **Functional requirements learned** — What must a Type B facility DO: commissary licensing coverage, food-grade exhaust capacity, humidity-control envelope, electrical density, plumbing requirements. Feed `REQUIREMENTS.md`.

8. **Sources.**

**Commit:**
```bash
git -C /c/src/artisan add research/trades/artisan-square/type-b-light.md
git -C /c/src/artisan commit -m "Plan J task 4: Type B light-trades facility research"
```

---

## Task 5 — Research: Combined Campus Model

**Files:**
- Create: `research/trades/artisan-square/combined-campus.md`

**Required sections (~1000-1500 words):**

1. **The IBC Section 508 strategy** — How Mixed Use Protected occupancy works: 2-hour fire-rated separation, separate exits, compliance requirements. Single building vs. two adjacent structures — the regulatory and practical tradeoffs.

2. **The mechanical spine** — Shared loading dock, materials storage, management office. The electrical backbone: single 1,000A 3-phase service to the building, sub-panels to each wing. Why over-building at construction is cheap; retrofitting is expensive.

3. **Cross-traffic dynamics** — The value of adjacency: baker customers discover the weaver next door. Smith's hammer draws curious visitors. Mixed-trade co-location creates a destination that no single trade could create alone. Real-world analog: Manchester Craft and Design Centre's observation that cross-trade foot traffic benefits all tenants.

4. **The anchor training studio** — How to size it, how to price it, how to structure the civic partnership (who pays what). The right-of-first-offer clause. How the training studio feeds the tenant pipeline.

5. **Functional requirements specific to combined campus** — Fire-rated separation spec, makeup air unit sizing for combined exhaust loads, single commissary license covering Type B only (Type A specifically excluded from food-adjacent spaces).

6. **Sources.**

**Commit:**
```bash
git -C /c/src/artisan add research/trades/artisan-square/combined-campus.md
git -C /c/src/artisan commit -m "Plan J task 5: combined campus model research"
```

---

## Task 6 — Cross-Facility Functional Requirements

**Files:**
- Create: `research/trades/artisan-square/REQUIREMENTS.md`

Pattern: exactly `research/trades/smithing/REQUIREMENTS.md` but for the facility operator.

**Required sections:**

1. **Purpose** — What this document is; how Plan K uses it.

2. **Electrical requirements** — Power density by facility type (Type A: 150W/sq ft; Type B: 40W/sq ft; combined: blended 80-100W/sq ft). 3-phase requirement (all facility types). Individual sub-panel and metering requirement.

3. **Ventilation requirements** — Type A industrial exhaust (CFM/studio, stack sizing). Type B food-grade exhaust (CFM/studio, grease interceptor sizing). Combined campus (two stacks, separation specification). Makeup air unit sizing (% of exhaust volume). Humidity control for Type B fiber studios.

4. **Floor load and ceiling requirements** — Type A: 150 lb/sq ft, 14 ft clearance. Type B: 80 lb/sq ft, 10 ft clearance. Concrete vs. wood framing by zone.

5. **Plumbing requirements** — Type A: eye-wash stations (OSHA), general. Type B: floor drain per studio, NSF hot-water line, grease trap at exhaust stack base. Combined: separate drain systems.

6. **Zoning and occupancy requirements** — IBC occupancy classification by facility type. Minimum zoning designation. Special permits required (commissary, dual-occupancy).

7. **Tenant-management requirements** — Studios per management FTE (25-30 studios per manager). Commissary compliance monitoring. Safety certification requirement for Type A tenants. Utility metering per studio.

8. **Functional Requirements Summary Table** — 15-25 rows; columns: requirement, Type A value, Type B value, combined campus value, source.

9. **Divergence Log** — Where Type A and Type B requirements fundamentally differ (fire code, health code, zoning, electrical density). These divergences drive the two-wing design.

**Commit:**
```bash
git -C /c/src/artisan add research/trades/artisan-square/REQUIREMENTS.md
git -C /c/src/artisan commit -m "Plan J task 6: Artisan Square cross-facility functional requirements"
```

---

## Task 7 — Facility Type Comparison (FACILITY-TYPES.md)

**Files:**
- Create: `research/trades/artisan-square/FACILITY-TYPES.md`

Pattern: `research/trades/smithing/HISTORICAL-FORMS.md` — comparative tables.

**Required sections:**

1. **Purpose** — What this document is; relationship to REQUIREMENTS.md.

2. **Physical comparison table** — Rows: electrical service, exhaust system, floor load, ceiling height, plumbing, zoning, occupancy classification, build approach. Columns: Type A only, Type B only, combined (adaptive reuse), combined (purpose-built), small-town lite.

3. **Operator economics comparison** — Rows: total studios, gross monthly rent potential, operating cost range, target occupancy, payback at target occupancy. By facility type.

4. **Regulatory complexity comparison** — Rows: permits required, health dept involvement, fire code variance, zoning variance typical. By facility type.

5. **Cross-facility observations** — What's universal (all facility types need 3-phase, individual metering, loading dock); what's type-specific (commissary only for Type B; industrial exhaust only for Type A).

6. **Benchmark: real-world comps** — Table of the 5 closest existing examples (Artisans Asylum, La Cocina SF, The Artisan Factory, Manchester Craft Centre, East End Maker Hub) vs. Artisan Square by key dimensions.

7. **Sources.**

**Commit:**
```bash
git -C /c/src/artisan add research/trades/artisan-square/FACILITY-TYPES.md
git -C /c/src/artisan commit -m "Plan J task 7: Artisan Square facility type comparison"
```

---

## Task 8 — Market Viability Verdict (MARKET-VERDICT.md)

**Files:**
- Create: `research/trades/artisan-square/MARKET-VERDICT.md`

Pattern: `research/trades/smithing/DECLINE-VERDICT.md` — explicit verdict with CERES vocabulary.

**The central question:** Does the Artisan Square building-operator model pencil out in the market, and under what conditions?

**Required sections:**

1. **The Question** — Does an operator building and running an Artisan Square generate a viable private return? If not, can the coop or civic lens make it viable?

2. **Evidence: Market comparables** — What do we know about Sola Salons unit economics? What do existing maker spaces charge and what is their occupancy history? What does La Cocina charge and what do they earn? Use these as anchors for the Plan J/K model.

3. **The payback analysis** — Using the spec Section 6.3 economics table as the baseline. At 85% occupancy, target payback is 12-15 years. At 95%, 8-10 years. What does it take to achieve 95% occupancy?

4. **Market-path verdict** — Private market viability: MARGINAL for location 1 (long payback, execution risk); GOOD for chain at locations 3-5 (brand-driven occupancy, amortized compliance playbook).

5. **Coop-path verdict** — Can a tenant cooperative own the building? Member-pool constraints: 25 studios × $1,500/month = $37,500 gross; capital recovery requires member equity contributions or bond financing. Tentative: MARGINAL for single building; GOOD for tenant-owned chain with anchor tenant guarantees.

6. **Civic-path verdict** — Town subsidy via below-market land or training-studio subsidy. CERES data: <$15/household/year for comparable civic infrastructure. At 10,000 households, $150,000/year civic contribution flips location 1 to GOOD. Verdict: GOOD for civic when population ≥5,000 with economic-development mandate.

7. **Binding constraints** — What actually makes or breaks Artisan Square viability: (a) occupancy — requires tenant pipeline (anchor training studio + craft school partnerships); (b) permitting — dual-occupancy takes 12-24 months without civic partnership; (c) operator expertise — nobody has built this before; the first build IS the learning.

8. **Overall verdict** — `mixed`: market path marginal at location 1, good at scale; coop path marginal; civic path good where applicable. The model works — but requires either the chain scale or a civic partner to be fully viable from day one.

9. **Implications for Plan K catalog** — Which Artisan Square configurations pencil out under which lenses. The combined-campus purpose-built model (highest capital, highest potential) requires civic co-investment or 3+ location chain. The adaptive-reuse Type B only (lowest capital, fastest to market) is the strongest location-1 candidate.

**Commit:**
```bash
git -C /c/src/artisan add research/trades/artisan-square/MARKET-VERDICT.md
git -C /c/src/artisan commit -m "Plan J task 8: Artisan Square market viability verdict"
```

---

## Task 9 — Consolidated Bibliography (SOURCES.md)

**Files:**
- Create: `research/trades/artisan-square/SOURCES.md`

Pattern: `research/trades/smithing/SOURCES.md`.

Consolidate all citations from Tasks 3-8. Group by: building code/zoning, electrical engineering, food safety/commissary licensing, real-world comparable facilities, financial modeling comps.

**Critical verification items for Plan K:**
1. Sola Salons unit economics — exact revenue per location (publicly disclosed in franchise disclosures)
2. East End Maker Hub rental rates for heavy-fab studios
3. La Cocina SF per-kitchen revenue and occupancy
4. IBC Section 508 dual-occupancy requirements — cite current edition (IBC 2021 or local jurisdiction adoption)
5. NFPA 13 fire suppression requirements for metalwork (Class D fire risk)
6. State-by-state commissary license portability (does an umbrella license cover tenants in each state?)

**Commit:**
```bash
git -C /c/src/artisan add research/trades/artisan-square/SOURCES.md
git -C /c/src/artisan commit -m "Plan J task 9: Artisan Square consolidated bibliography"
```

---

## Task 10 — Closeout

- [ ] Update `plans/2026-04-19-plan-j-research-artisan-square.md` frontmatter: `status: completed`, `completed: YYYY-MM-DD`, `last_modified: YYYY-MM-DD`, bump version to `"1.1"`
- [ ] Update `TRACKER.md`: Plan J row → completed; note Plan K (catalog) unblocked
- [ ] Update `plans/README.md`: Plan J row → completed
- [ ] Add Plans K, L, M as `not-yet-authored` stubs in `plans/README.md`

**Commit:**
```bash
git -C /c/src/artisan add plans/ TRACKER.md
git -C /c/src/artisan commit -m "Plan J task 10: closeout"
```

---

## Retrospective: Risks (upfront)

- **Citation-hallucination risk:** Artisan Square research cites CONTEMPORARY sources (building codes, franchise disclosures, real facility rates) — these are more verifiable than medieval economic history but model-knowledge may not have current IBC/NFPA editions or specific La Cocina financials. Apply citation policy strictly: `[CITATION-NEEDED]` over fabrication, especially for financial benchmarks.
- **Schema novelty risk:** The artisan-square schema extension inverts CERES's trade-oriented field semantics (throughput = studio-months not production units; market_price = rent not product price). The Tier A sim should handle this via the same lens formulas, but the `io_catalog.py` reader will need to handle the new field names. Flag for Plan L.
- **Regulatory currency risk:** IBC, NFPA, and commissary licensing rules vary by jurisdiction and edition year. Functional requirements should describe what is needed, not the specific code section, and note that local jurisdictional review is required before any build.

## Failure Modes

- **If dual-occupancy research reveals fundamental regulatory incompatibility in a target jurisdiction:** Document as Plan K guidance — certain locations may only support Type A or Type B, not combined. The catalog must have entries for each.
- **If market comparable research reveals Sola Salons economics don't translate to longer-payback artisan trades:** Document the gap honestly in MARKET-VERDICT.md; adjust Plan K catalog entry parameters accordingly. An honest verdict of "chain-dependent, not standalone-viable" is a real finding.

## Handoff

When Plan J completes, Plan K (Artisan Square Catalog — 15 facility configurations) is unblocked. Plan K authors should read REQUIREMENTS.md, FACILITY-TYPES.md, and MARKET-VERDICT.md before authoring any catalog entry.
