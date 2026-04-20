---
trade: artisan-square
doc_type: facility-type-comparison
version: "1.0"
status: draft
derived_from:
  - research/trades/artisan-square/type-a-heavy.md
  - research/trades/artisan-square/type-b-light.md
  - research/trades/artisan-square/combined-campus.md
sources_count: 37
---

# Artisan Square — Facility Type Comparison

## 1. Purpose

This document is a comparative record of how different Artisan Square facility
configurations differ on physical infrastructure, operator economics, and regulatory
complexity. Its relationship to `REQUIREMENTS.md` is complementary: REQUIREMENTS.md
states what any Artisan Square facility must do regardless of type — the non-negotiable
functional floor. This document states how the five catalog facility types compare on
the dimensions that vary by type. Catalog authors should read both: REQUIREMENTS.md
constrains the design; this document supplies the comparative framing that informs which
type is appropriate for a given site, market, and operator context.

---

## 2. Physical Infrastructure Comparison

Five facility types are recognized in the Artisan Square catalog schema:

- **Type-A-only** — Heavy-trades wing only (forge, metalwork, kiln); no food production.
- **Type-B-only** — Light-trades wing only (baking, weaving, leather, soap/candle); commissary umbrella; no combustion forging.
- **combined-campus-adaptive** — Both wings in adaptive-reuse building (Location 1 prototype).
- **combined-campus-purpose-built** — Both wings in purpose-built new construction (Location 2+ prototype).
- **small-town-lite** — Scaled-down combined or single-wing format for towns of 2,000–15,000 population; typically 12–18 studios.

### Table 1: Physical Infrastructure by Facility Type

| Feature | Type-A-only | Type-B-only | combined-campus-adaptive | combined-campus-purpose-built | small-town-lite |
|---|---|---|---|---|---|
| **Main electrical service** | 400–600A 3-phase (sized for wing only) | 200–400A single-phase or 3-phase depending on studio count | 1,000A 3-phase (shared main, over-built intentionally) [design spec §4.5] | 1,000A 3-phase (purpose-built to spec) [design spec §4.5] | 400–600A 3-phase (12–18 studios; smaller aggregate load) |
| **3-phase required?** | Yes — forge/kiln loads require 3-phase sub-panels per studio [type-a-heavy.md §2] | No — baking and fiber arts studios operate on 240V single-phase 60A or 30A sub-panels [type-b-light.md §2] | Yes — Type A wing drives the 3-phase main service requirement [combined-campus.md §3] | Yes — same as adaptive | Conditional — required if any Type A studios included; not required for Type-B-only small-town variant |
| **Type A exhaust stack?** | Yes — ≥2,000 CFM per station, industrial-grade, 2-hour fire-rated vertical chase [type-a-heavy.md §4; design spec §4.3] | No | Yes — dedicated industrial stack, separate from food-grade stack [combined-campus.md §3] | Yes — purpose-built dual-stack configuration [combined-campus.md §3] | Conditional — required if Type A studios present; omitted in Type-B-only small-town variant |
| **Type B food-grade exhaust stack?** | No | Yes — 300–600 CFM per food studio; grease interceptor at riser base; UL 710 compliant [type-b-light.md §4] | Yes — entirely separate from Type A stack; no shared ductwork [combined-campus.md §3] | Yes — purpose-built dual-stack [combined-campus.md §3] | Conditional — required if food-producing studios present |
| **Floor load rating** | 150 lb/sq ft minimum (general); reinforced kiln pad at kiln location for point-load spec [type-a-heavy.md §3; design spec §4.3] | Standard commercial floor (40–80 lb/sq ft for baking studios); no industrial floor rating required | 150 lb/sq ft in Type A wing; standard commercial in Type B wing [type-a-heavy.md §2] | 150 lb/sq ft in Type A wing; standard commercial in Type B wing | 150 lb/sq ft if any Type A; standard commercial for Type-B-only |
| **Ceiling height** | 14 ft minimum (16 ft preferred in purpose-built) [type-a-heavy.md §2; design spec §4.1] | 10 ft standard [design spec §4.4] | 14 ft in Type A wing; 10 ft in Type B wing | 14 ft in Type A wing; 10 ft in Type B wing | Matches wing type; 14 ft if Type A present; 10 ft for Type-B-only |
| **Zoning classification** | Light-industrial or industrial (IBC F-2 requires industrial or mixed-use zoning) [type-a-heavy.md §6] | Mixed-use or retail-commercial acceptable; most permissive of the five types for zoning [type-b-light.md §1] | Light-industrial or mixed-use with IBC F-2 + Group B dual occupancy [design spec §4.1] | Light-industrial or mixed-use purpose-built to dual-occupancy spec | Light-industrial or mixed-use; civic co-investment often unlocks below-market land in these zones [design spec §3] |
| **IBC occupancy group** | Group F-2 (light manufacturing) [type-a-heavy.md §1] | Group F-2 (food studios, conservative baseline) + Group B (fiber arts, non-food) [type-b-light.md §4] | F-2 (Type A wing) + F-2/Group B (Type B wing); IBC §508.4 Mixed Use Protected applies [combined-campus.md §2] | Same as adaptive; purpose-built for §508.4 compliance from ground up | Same as applicable wing types; §508.4 applies if both wings present |
| **Commissary license?** | No | Yes — operator-held Type A commercial kitchen license covering all food-producing Type B studios [type-b-light.md §2] | Yes — covers Type B wing only; commissary scope explicitly excludes Type A wing [combined-campus.md §3] | Yes — same scope as adaptive | Conditional — required if food studios present |
| **Build approach typical** | Adaptive reuse of existing light-industrial building; concrete floor, 3-phase service, industrial zoning often already present | Adaptive reuse or new construction; lighter infrastructure requirements expand site options | Adaptive reuse of factory, warehouse, or light-industrial building (Location 1) [design spec §4.1] | New construction, single-story, purpose-built two-wing plan (Locations 2+) [design spec §4.1] | Adaptive reuse preferred; smaller footprint than medium-format; civic land contribution possible |

---

## 3. Operator Economics Comparison

Rent ranges per design spec §5.3. Build-out and operating costs per design spec §6.

### Table 2: Operator Economics by Facility Type

| Feature | Type-A-only | Type-B-only | combined-campus-adaptive | combined-campus-purpose-built | small-town-lite |
|---|---|---|---|---|---|
| **Total studios (range)** | 6–8 Type A studios [design spec §4.2] | 14–20 Type B studios [design spec §4.2] | 20–28 combined (6–8 Type A + 14–20 Type B) [design spec §3] | 20–40 combined (same wing ratio) [design spec §3] | 12–18 studios (typically 4–6 Type A + 8–12 Type B, or Type B-only variant) [design spec §3] |
| **Monthly gross rent potential (range)** | $9,000–19,200 (6–8 studios at $1,300–2,400/studio) [design spec §5.3] | $12,250–35,000 (14–20 studios at $875–1,750/studio) [design spec §5.3] | $25,000–42,000 (24 studios at full range) [design spec §5.3] | $30,000–56,000 (40 studios at full range; larger format) | $10,500–21,600 (12–18 studios; blended mix) [CITATION-NEEDED: small-town-lite unit economics not separately modeled in design spec] |
| **Build-out cost estimate (range)** | $350k–700k (Type A wing only: electrical, exhaust, floor, fire suppression; land excluded) [CITATION-NEEDED: Type-A-only build-out not separately itemized in design spec §6.1; derived by subtracting Type B line items] | $200k–450k (Type B wing only: electrical, plumbing, food-grade exhaust, commissary permitting; land excluded) [CITATION-NEEDED: Type-B-only build-out not separately itemized in design spec §6.1] | $760k–1.45M (full two-wing adaptive reuse including land/building) [design spec §6.1] | $1M–2M (purpose-built full campus) [design spec §8] | $500k–900k (small-town prototype) [design spec §8] |
| **Annual operating cost (range)** | $140k–230k (reduced staff, no commissary compliance overhead; estimated) [CITATION-NEEDED: Type-A-only operating cost not separately modeled] | $120k–210k (no 3-phase maintenance, no forge suppression; commissary compliance adds staff burden; estimated) [CITATION-NEEDED: Type-B-only operating cost not separately modeled] | $245k–405k [design spec §6.2] | $280k–450k (larger campus; proportionally more staff and maintenance) [CITATION-NEEDED: purpose-built operating cost increment not modeled separately] | $160k–280k (smaller campus; 1 FT manager; reduced utility and maintenance load) [CITATION-NEEDED: small-town-lite operating cost not separately modeled] |
| **Target occupancy rate** | 85% (6.8 studios of 8 occupied) — thinner tenant pool than Type B; graduation path less mature in Type A [type-a-heavy.md §5] | 85% [design spec §6.3] | 85% [design spec §6.3] | 85% (established brand; waitlist dynamics at Locations 2+) [design spec §6.4] | 85% with civic co-investment; 75% without (smaller pool in small-town markets) [design spec §3] |
| **Payback at target occupancy (years)** | 14–20 yr (estimated; narrower revenue base, similar capital intensity) [CITATION-NEEDED: Type-A-only payback not separately modeled] | 10–16 yr (estimated; lower capital, wider tenant pool, but lower gross rents) [CITATION-NEEDED: Type-B-only payback not separately modeled] | 12–15 yr (85% occupancy) [design spec §6.3] | 10–14 yr (larger studio count amortizes fixed costs; established brand) [CITATION-NEEDED: purpose-built payback not separately modeled] | 14–20 yr without civic subsidy; 10–14 yr with civic anchor subsidy [design spec §3; design spec §6.4] |

---

## 4. Regulatory Complexity Comparison

### Table 3: Regulatory Complexity by Facility Type

| Feature | Type-A-only | Type-B-only | combined-campus-adaptive | combined-campus-purpose-built | small-town-lite |
|---|---|---|---|---|---|
| **Permitting timeline estimate** | 6–12 months (F-2 occupancy; fire marshal review for forge/kiln; industrial zoning confirmation; no health dept involvement) [type-a-heavy.md §6; CITATION-NEEDED: Type-A-only permitting timeline from contractor or jurisdiction experience] | 4–8 months (commissary licensing adds health dept review cycle; building code lighter than Type A; zoning often pre-compatible) [type-b-light.md §2; CITATION-NEEDED: Type-B-only permitting timeline] | 10–18 months at Location 1 (dual occupancy analysis; IBC §508.4 fire-separation review; health dept commissary application; fire marshal review for both wings; first-ever in many jurisdictions) [combined-campus.md §2; design spec §7.2] | 6–10 months (purpose-built; AHJ already familiar with the design from Location 1 playbook; permit drawings pre-engineered) [design spec §6.4] | 6–12 months (smaller scope; same permit categories but lower complexity; civic relationships may accelerate) [design spec §3] |
| **Health dept involvement** | None — no food production; no commissary; health dept has no jurisdiction over metalwork or pottery studios | Heavy — commissary license application; initial inspection; annual inspection calendar; individual tenant registrations; sanitation log oversight [type-b-light.md §4] | Heavy — full commissary licensing for Type B wing; health dept scope explicitly bounded at the fire-rated wall; no health dept involvement in Type A wing [combined-campus.md §3] | Heavy (same as adaptive; established template reduces rework) | Moderate to heavy — if food studios present, commissary applies; if Type-B-only, same as Type-B-only; civic partners may provide local health dept relationships |
| **Fire code variance required?** | Likely — most AHJs have limited experience with forge/kiln operations in leased multi-tenant buildings; fire marshal may require engineering analysis for Class D metals risk, kiln suppression head specs, and damper systems [type-a-heavy.md §4; CITATION-NEEDED: fire code variance frequency for F-2 forge occupancy in multi-tenant context] | Unlikely — commercial kitchen exhaust and suppression systems are well-understood by AHJs; no combustion or Class D risk [type-b-light.md §4] | Likely in Type A wing; unlikely in Type B wing — the 2-hour fire-rated separation is itself a code mechanism, not a variance [combined-campus.md §2] | No — purpose-built design is pre-engineered for compliance; fire code variance risk is resolved at Location 1 and absorbed into the playbook [design spec §7.2] | Conditional — same logic as the wing type included |
| **Zoning variance typical?** | Possible — F-2 in mixed-use zones may require a conditional use permit or variance in some jurisdictions; urban adaptive reuse sites carry more risk than suburban industrial [type-a-heavy.md §6] | Unlikely — Type B uses are compatible with mixed-use and commercial zoning in most jurisdictions without variance [type-b-light.md §1] | Possible for the Type A component in a mixed-use zone; unlikely for Type B component [combined-campus.md §2] | Low — site selection for purpose-built specifically targets industrial or mixed-use zoned parcels; design spec §4.1 | Low to moderate — small towns often have more flexible zoning with fewer formal variance processes; civic sponsorship further reduces exposure |
| **Commissary inspection schedule** | N/A | Annual (health dept); plus follow-up inspections if deficiencies noted; grease interceptor requires operator-managed pumping every 30–90 days [type-b-light.md §4] | Annual for Type B wing; no schedule for Type A wing [combined-campus.md §3] | Annual for Type B wing (same) | Annual if food studios present; same grease interceptor obligation |

---

## 5. Cross-Facility Observations

### Universal to All Facility Types

Every Artisan Square configuration — regardless of type — requires the following
infrastructure and operational elements. These are non-negotiable across the catalog:

- **3-phase main electrical service.** Even a Type-B-only facility sized for baking
  and fiber arts studios benefits from a 3-phase main service for headroom and
  flexibility. A single-phase service upgrade to an occupied building carries a
  utility lead time of 6–18 months in suburban markets [combined-campus.md §3;
  CITATION-NEEDED: utility upgrade lead-time data]. Building correctly once is
  cheaper than upgrading under tenancy.

- **Individual tenant metering.** Power consumption variance across Artisan Square
  tenant types — a forge studio versus a weaving studio, or a baking studio versus a
  leather studio — is large enough that unmetered tenancy creates unrecoverable cost
  conflict. Individual sub-panel metering is required in all five facility types.
  [type-a-heavy.md §2; type-b-light.md §2; combined-campus.md §5]

- **Loading dock.** All trades require bulk delivery: bar stock and propane for
  metalwork, flour and ingredient pallets for bakers, loom parts and fiber bales for
  weavers. A commercial dock with shared pallet jack is required in every Artisan
  Square format; without it, tenant businesses cannot operate at production scale.
  [design spec §4.5]

- **Locked individual materials storage cages.** Studio footprints (100–450 sq ft)
  are production spaces, not warehouses. Material storage — steel stock, flour bags,
  yarn cones, leather hides — requires dedicated external caged storage per tenant.
  [design spec §4.5]

- **Management office and compliance records.** The Artisan Square operator function
  is infrastructure management and compliance, not craft. A 300–400 sq ft management
  office housing the location manager, lease files, and commissary compliance records
  (where applicable) is required in all formats. [design spec §4.5]

### Type-Contingent Features

These elements vary across facility types and represent the primary decision points
for catalog authors selecting a facility type for a given context:

- **Commissary license.** Required in Type-B-only, both combined-campus variants, and
  small-town-lite formats that include food studios. Absent in Type-A-only. This is
  the single most significant regulatory differentiator: it adds a continuous operational
  compliance burden (annual health dept inspections, grease interceptor maintenance,
  individual tenant registration, sanitation log oversight) that Type-A-only facilities
  do not carry. [type-b-light.md §4; combined-campus.md §3]

- **Industrial exhaust stack.** Required in Type-A-only, both combined-campus variants,
  and small-town-lite formats with Type A studios. Absent in Type-B-only. The industrial
  stack is a 2-hour fire-rated vertical chase from studio connections to roofline with
  motorized fire dampers per studio — a material construction cost element and a fire
  marshal review trigger. [type-a-heavy.md §4; design spec §4.3]

- **Zoning classification.** Type-A-only and combined-campus formats require
  light-industrial or mixed-use zoning with F-2 occupancy eligibility. Type-B-only
  can operate in commercial or mixed-use zones that are inaccessible to F-2 forging
  operations — a meaningful site-selection advantage for food-only configurations.
  [type-a-heavy.md §6; type-b-light.md §1]

- **Floor load specification.** The 150 lb/sq ft floor rating and reinforced kiln pad
  are required only where Type A studios are present. Type B studios operate on
  standard commercial floor construction, substantially reducing structural costs and
  adaptive-reuse site eligibility. [type-a-heavy.md §2; type-b-light.md §2]

### Combined-Campus Specific Features

These elements exist only in the combined-campus-adaptive and combined-campus-purpose-built
facility types. They represent the regulatory price of operating both wings under one roof:

- **IBC §508.4 fire-rated occupancy separation.** A 2-hour fire-rated assembly must
  continuously separate the Type A and Type B wings from foundation to roofline.
  This is a non-negotiable IBC requirement enabling dual occupancy; it is the
  structural mechanism that permits a forge operation and a commissary kitchen to
  coexist in a single building envelope. [combined-campus.md §2; design spec §4.1]
  [CITATION-NEEDED: IBC 2021 §508.4 continuity requirements for fire separation
  assemblies in mixed-occupancy buildings]

- **Dual exhaust stacks with no cross-contamination.** The industrial (Type A) and
  food-grade (Type B) exhaust stacks must not share duct sections, plenums, or
  discharge points. Forge exhaust in food-production space is a health code violation
  independent of building code requirements. They may share structural chase space in
  the mechanical spine but are completely separate systems from studio connection to
  atmosphere. This dual-stack design adds to both construction cost and complexity
  relative to either single-wing format. [combined-campus.md §3; type-a-heavy.md §4;
  type-b-light.md §4]

- **Commissary scope exclusion boundary.** The commissary umbrella license covers Type B
  only. The exclusion must appear explicitly in the commissary license application,
  health department records, and every Type A tenant lease. A boundary failure —
  any commissary use extending into the Type A wing — risks the commissary license
  for all Type B tenants. The 2-hour fire-rated wall is the physical correlate of
  this boundary. [combined-campus.md §3]

---

## 6. Benchmark Comparison: Five Real-World Comps vs. Artisan Square

The following five facilities are the closest real-world comparators to the Artisan
Square concept as of the research period. None fully replicates the Artisan Square
combination; the table documents where each facility is a partial match and where
the Artisan Square concept fills a gap.

### Table 4: Real-World Benchmark Facilities vs. Artisan Square

| Facility | Type A trades? | Type B trades? | Individual studios? | Commissary? | Heavy infra? | Notes |
|---|---|---|---|---|---|---|
| **Artisans Asylum** (Somerville, MA) | Yes (shared floor-time, not dedicated studios) | No — food explicitly excluded | Yes (approx. 160 dedicated studios at various scales) [CITATION-NEEDED: Artisans Asylum studio count — confirm from artisansasylum.com] | No | Yes — 3-phase, forge bay, metal shop; industrial-grade exhaust | Closest existing facility on heavy infrastructure and studio-tenancy model. Critical gap: no dedicated individual forge studios with exclusive tenancy; the code and liability complexity of individually metered F-2 forge studios in a multi-tenant building has not been resolved at this scale. Artisan Square addresses this gap by design. [type-a-heavy.md §2] |
| **La Cocina** (San Francisco, CA) | No | Yes — food only by regulatory design | No — shared kitchen access, hourly rotation (approx. $20–40/hr) [CITATION-NEEDED: La Cocina current rate schedule] | Yes — gold-standard commissary umbrella model; operator holds license, tenants register under it | No | Gold standard for food-incubator commissary structure. The Artisan Square Type B commissary model is derived directly from the La Cocina umbrella mechanism. Critical gap: dedicated individual studio tenancy absent; shared rotation model does not support production-scale businesses exceeding 10–15 hrs/week without paying more than a dedicated studio. [type-b-light.md §2] |
| **The Artisan Factory** (Northampton, PA) | Partial — some light fabrication tenants | Partial — some food-related tenants reported | Yes — mixed studio sizes, variable infrastructure per unit | Partial — unclear whether operator holds commissary license or individual tenants self-license [CITATION-NEEDED: The Artisan Factory PA — commissary licensing structure, studio types, current rates; confirm from direct contact or current facility documentation] | Partial — industrial electrical present; no confirmed forge-grade exhaust or Class D suppression | Incidentally multi-trade rather than designed multi-trade. Does not appear to operate under a unified commissary umbrella or a purpose-built dual-wing plan. Represents the category of facilities that combine trades by leasing to whoever arrives rather than by infrastructure design. |
| **Manchester Craft and Design Centre** (Manchester, UK) | No — light bench crafts only; no forge or kiln at industrial grade | No — no food production | Yes — approximately 20 individual studios at bench scale [CITATION-NEEDED: Manchester Craft and Design Centre current studio count — confirm from current facility documentation] | No | No — standard commercial building infrastructure | Most closely documented example of the cross-trade destination effect. Tenants in unrelated trades report higher retail foot traffic when adjacent studios in different trades are occupied. Critical gap: no heavy infrastructure, no food production — restricted to light bench trades. Scale is small relative to the Artisan Square medium format. [combined-campus.md §1; CITATION-NEEDED: Manchester Craft and Design Centre cross-trade foot-traffic documentation] |
| **East End Maker Hub** (Houston, TX) | Yes — heavy fabrication at large scale (welding bays, CNC, industrial equipment) | No | Yes — large-format studios, not artisan-scale | No | Yes — industrial electrical, ventilation at manufacturing scale [CITATION-NEEDED: East End Maker Hub current studio rates and infrastructure specs — confirm from eastendmakerhub.com or direct contact] | Industrial scale, not artisan scale. Heavy fabrication studios designed for small manufacturing businesses, not sole-proprietor craft practitioners. Rent at $18–28/sq ft/year for raw space without metered 3-phase, exhaust, and compliance overhead — below Artisan Square Type A rates but without the compliance and infrastructure stack. Too large for the artisan tenant profile; represents the upper end of the heavy-trade building category. [type-a-heavy.md §5] |
| **Artisan Square (proposed)** | Yes — dedicated individual Type A studios (forge, metalwork, pottery/kiln) with exclusive tenancy, metered 3-phase, industrial exhaust | Yes — dedicated individual Type B studios (baking, weaving, leather, soap/candle) under commissary umbrella | Yes — all studios individually tenanted with exclusive occupancy | Yes — operator-held commissary covering all food-producing Type B studios | Yes — 1,000A 3-phase main; dual exhaust stacks; 150 lb/sq ft Type A floor; 2-hour fire-rated separation | The combination all five comparators partially represent but none achieves. Specifically fills the gap of: individual dedicated studio tenancy + heavy-trade infrastructure + food commissary umbrella + multi-trade adjacency in a single building. |

---

## 7. Decline-Pattern Mapping for Facility Types

Using the CERES canonical vocabulary (`viable`, `marginal`, `decline`, `restructuring`,
`demand-collapse`, `regulatory-dissolution`, `civic-lens`), the following maps the
economic conditions that favor or disfavor each facility type.

### Type-A-only

**Favorable conditions:** Urban manufacturing districts with active journeyman-level
metalwork or ceramics practitioner communities; communities with vocational programs
producing forge or ceramics graduates; markets where light-industrial zoning is
accessible and relatively inexpensive. The Artisan Square graduation path functions
most reliably in Type-A-only when an anchor training studio feeds the Type A tenant
pipeline — without it, the tenant pool is thin.

**Disfavorable conditions:** Suburban or small-town markets with no pre-existing
journeyman metalwork or pottery practitioner base; sites where F-2 zoning is
unavailable without a variance; markets where heavy-trades practitioners have been
priced out entirely (urban land costs can make F-2 zoning inaccessible). Type-A-only
without an active training pipeline faces `marginal` viability in most suburban markets
and `demand-collapse` risk in markets where the practitioner pool is absent.

**CERES verdict:** `viable` in urban manufacturing districts with established practitioner
communities; `marginal` without training pipeline; `demand-collapse` risk in thin markets.

### Type-B-only

**Favorable conditions:** Mixed-use or retail-commercial zones near higher-income
customer bases (farmers market culture, food-artisan markets, specialty retail
corridors); markets with active startup food business communities; sites where
light-industrial zoning is unavailable but commercial zoning is. Type B-only is the
simplest facility type to permit and the broadest on site selection. The commissary
umbrella creates a self-selecting tenant marketing channel — bakers who need commissary
access find the facility.

**Disfavorable conditions:** Low-income markets where the addressable customer base
for specialty artisan food products is thin; markets saturated with existing shared
commissary kitchen access (hourly rotation facilities); markets where the sole-proprietor
food business startup rate is low.

**Smallest moat:** Type B-only is the easiest Artisan Square configuration for a
competitor to replicate. A standalone commercial kitchen incubator with individual
studios is a simpler regulatory and construction project than any format including
Type A. The competitive moat is operational excellence and commissary compliance
management, not the hardware.

**CERES verdict:** `viable` in mixed-use zones near higher-income markets; `marginal`
in low-demand food startup markets; `restructuring` risk where hourly-rotation commissary
competitors dominate.

### Combined Campus (adaptive and purpose-built)

**Favorable conditions:** Markets that support both a metalwork/ceramics practitioner
pool and a food-startup community simultaneously; medium-format suburban markets
(populations 15,000–150,000) where the combined destination effect produces occupancy
that neither wing alone could sustain. Multi-trade adjacency is a retention mechanism:
tenants forgo lower per-square-foot alternatives because the network and cross-traffic
value exceeds the rent savings. [combined-campus.md §4]

**Most resilient format:** The combined campus cross-subsidizes occupancy risk: a
soft year in the Type A tenant pool does not threaten the commissary license; a
difficult commissary inspection cycle does not undermine the Type A rent base. The
two wings are operationally independent under one roof, creating a diversification
benefit unavailable to either single-wing format.

**Highest capital and highest permitting complexity:** The 2-hour fire-rated separation,
dual exhaust stacks, dual-occupancy permitting, and commissary licensing combine to
produce the most complex permit package of any facility type. This is the format that
builds the permitting playbook. Location 1 combined-campus cost ($80–150k in
permitting and engineering) amortizes to $8–15k per location by Location 10
[design spec §7.2] — the capital barrier is a one-time investment in catalog IP, not
a recurring per-location burden.

**CERES verdict:** `viable` and most resilient in medium suburban markets with dual
practitioner/food-startup communities; `marginal` where only one tenant population
exists; strongest multi-lens (market + civic) viability case.

### Small-Town Lite

**Favorable conditions:** Towns of 2,000–15,000 population where civic co-investment
is available — economic development agencies, vocational school partnerships, community
colleges with culinary or trades programs. The anchor training studio at below-market
rent is the critical economic unlock: civic funding converts the below-market slot into
a fully-underwritten pipeline asset, and the training output aligns directly with civic
economic development metrics (workforce development, food security, local economic
multiplier). [design spec §3; design spec §6.4]

**Market-path marginal without civic co-investment:** In a small-town market without
civic subsidy, the monthly gross rent potential (est. $10,500–21,600) against estimated
operating costs ($160k–280k/year) produces a payback period that requires 14–20 years
at target occupancy. This is viable as an investment but not quickly self-sustaining.
The CERES civic lens makes the case more clearly than the market lens: the social return
(workforce development, food security, local practitioner employment) justifies civic
investment at cost-per-household levels well below alternative economic development
programs [design spec §3].

**Strongest civic-lens case:** Of the five facility types, small-town-lite is the format
where the civic-lens CERES analysis produces the most compelling case for co-investment.
The market-path analysis is weaker than for combined-campus medium format; the civic-path
analysis is stronger.

**CERES verdict:** `viable` with civic co-investment; `marginal` on market-path alone;
strongest `civic-lens` case of any facility type; `restructuring` risk in towns too
small to sustain a practitioner base of any kind.

---

## 8. Divergence Log

The following are the three sharpest divergences across facility types and their
implications for catalog authoring.

**Divergence 1: Commissary license presence or absence.** The commissary license is
the most operationally consequential split in the facility type catalog. A Type-A-only
facility is a real estate and infrastructure business. A facility with any food-producing
Type B studios is a real estate, infrastructure, and continuous health-department
compliance business. The operator profile, staff skills, and risk tolerance required
are materially different. A Type-A-only operator with no food background can manage
the building without a commissary; any facility type including Type B studios requires
an operator with either food-business compliance experience or a contracted compliance
management relationship. Catalog authors must not treat the commissary as a background
feature — it is an operational capability requirement that the operator must match to
the facility type.

**Divergence 2: Zoning class and site selection range.** Type-B-only operates in
commercial and mixed-use zones that are categorically unavailable to facility types
including Type A studios. This divergence matters most in urban markets and older
suburban retail corridors where light-industrial zoning is scarce or prohibitively
expensive. A catalog author selecting a facility type for an urban Main Street context
faces a zoning constraint that eliminates all Type-A-including formats before any
other analysis is performed. Conversely, a site with abundant and inexpensive
light-industrial zoning in a suburban setting that could support either wing type
should be analyzed as a combined-campus candidate rather than defaulting to Type B
for simplicity. The zoning divergence is a hard filter, not a preference input.

**Divergence 3: Permitting timeline and operator playbook maturity.** The combined-campus-
adaptive format carries a 10–18 month permitting timeline at Location 1 precisely
because it is the first execution of the dual-occupancy strategy in most jurisdictions.
By combined-campus-purpose-built at Locations 2+, the engineering drawings are pre-
stamped, the AHJ relationships are established, and the permitting timeline compresses
to 6–10 months. The payback analysis for the combined-campus format is therefore
chain-dependent: single-location combined-campus economics are marginal; chain
economics at 3+ locations are substantially stronger because Location 1's permitting
cost is the capital investment in the catalog. Catalog authors evaluating the combined-
campus format for a single-location context must apply the Location 1 cost structure,
not the chain-amortized cost. Treating the playbook as already built when it is not
is the most common error in comparative facility-type analysis.

---

## 9. Sources

Sources inherited from derived research chapters and design specification. Additional
facility-type-comparison-specific citations listed below.

1. Artisan Square Design Specification, v0.1 (2026-04-19). `specs/2026-04-19-artisan-square-design.md`.
   Primary source for physical design (§4), tenant model (§5), economic model (§6),
   operations and chain playbook (§7), and rollout sequence (§8). All design-spec-
   derived figures throughout this document reference this source.

2. Artisan Square — Type A Heavy-Trades Facility Research. `research/trades/artisan-square/type-a-heavy.md`.
   Physical requirements (§2–§3), shared Type A infrastructure (§4), tenant economics (§5),
   operator risks (§6), and functional requirements (§7). Primary source for all Type A
   specifications in this document.

3. Artisan Square — Type B Light-Trades Facility. `research/trades/artisan-square/type-b-light.md`.
   Baking studio requirements (§2), fiber arts studio requirements (§3), Type B shared
   infrastructure including commissary umbrella structure (§4), tenant economics (§5),
   operator risks (§6), and functional requirements (§7). Primary source for all Type B
   specifications in this document.

4. Artisan Square — Combined Campus Model. `research/trades/artisan-square/combined-campus.md`.
   IBC Section 508 strategy (§2), mechanical spine design (§3), cross-traffic dynamics (§4),
   combined-campus functional requirements (§5). Primary source for combined-campus
   specifications in this document.

5. International Building Code, §508.4 Mixed Use Protected (IBC 2021).
   [CITATION-NEEDED: confirm §508.4 as the controlling section in IBC 2021 for mixed-
   occupancy fire separation; verify 2-hour assembly requirement for F-2/B separation;
   confirm edition adopted by target jurisdiction]

6. NFPA 13: Standard for the Installation of Sprinkler Systems (2022 edition).
   [CITATION-NEEDED: sections governing suppression zoning across occupancy separations;
   Class D applicability to metalwork studios in multi-tenant buildings]

7. Artisans Asylum, Somerville MA. Studio count, membership structure, metalwork shop
   access model. [CITATION-NEEDED: current studio count (~160), membership tier pricing,
   and explicit food-exclusion policy — confirm from artisansasylum.com or direct contact]

8. La Cocina SF. Commissary licensing structure, shared kitchen rate schedule, dedicated
   studio pricing. [CITATION-NEEDED: La Cocina published program guides and current rate
   schedule; shared kitchen access $20–40/hr cited from publicly available 2020s-era
   program documentation; requires confirmation of current rates]

9. The Artisan Factory, Northampton PA. Studio types, commissary licensing status,
   facility infrastructure. [CITATION-NEEDED: direct contact or current facility
   documentation — current public web presence does not confirm commissary or forge
   infrastructure details with sufficient specificity for catalog use]

10. Manchester Craft and Design Centre, Manchester UK. Studio count, cross-trade foot-
    traffic data, tenant survey. [CITATION-NEEDED: operator report or third-party
    evaluation documenting cross-trade foot-traffic benefit; current studio count;
    facility-published or third-party source preferred]

11. East End Maker Hub, Houston TX. Heavy-fabrication studio rates, infrastructure
    specifications, studio size range. [CITATION-NEEDED: current rates ($18–28/sq ft/yr
    cited from type-a-heavy.md §5) and infrastructure specs — confirm from
    eastendmakerhub.com or direct contact]

12. NSF International. NSF/ANSI 2 — Food Equipment; NSF/ANSI 61 — Drinking Water
    System Components. [Standards referenced for Type B food studio flooring, plumbing,
    and hot-water specifications throughout this document]

13. UL 710 — Standard for Exhaust Hoods for Commercial Cooking Equipment.
    [Referenced for food-grade exhaust stack compliance standard in Type B and combined-
    campus facility types]

14. OSHA 29 CFR 1910.151. Eye-wash station requirement for corrosive-material
    exposure. [CITATION-NEEDED: confirm applicability to commercial lease (non-employer-
    employee) context for metalwork tenants]

15. OSHA 29 CFR 1910.1053. Respirable Crystalline Silica PEL (50 μg/m³ 8-hr TWA).
    [Referenced for pottery studio clay-preparation ventilation requirement in Type A]

16. International Building Code, Group F-2 (Light Manufacturing) occupancy
    classification. [CITATION-NEEDED: IBC F-2 definition and requirements — confirm
    edition and section number; F-2 classification applies to both Type A forge/kiln
    studios and Type B food-production studios under conservative reading]

17. [CITATION-NEEDED: utility service upgrade lead times for large commercial electrical
    services above 400A in suburban US markets; 6–18 month range cited from
    combined-campus.md §3 requires primary industry or utility source]

18. [CITATION-NEEDED: multi-tenant commissary license suspension when individual tenant
    violates conditions — state health department administrative law; California, New York,
    Texas as most-documented jurisdictions; cited in type-b-light.md §4 and relevant to
    combined-campus commissary scope exclusion analysis in this document]

19. [CITATION-NEEDED: small-town-lite unit economics (monthly gross rent potential,
    annual operating cost, payback at target occupancy without and with civic subsidy)
    are estimated in this document from design spec §8 rollout table and §3 civic
    co-investment text; no standalone small-town-lite financial model exists in the
    current research set; a dedicated small-town-lite economics analysis is required
    before these figures can be treated as confirmed catalog entries]
