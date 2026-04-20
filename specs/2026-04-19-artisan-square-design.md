# Artisan Square — Design Specification

## Design Specification

**Date:** 2026-04-19
**Version:** 0.1
**Author:** Giovanni Della-Libera + Claude Sonnet 4.6
**Status:** Draft — pending author review before implementation planning

---

## 1. Project Identity

- **Codename:** Artisan Square
- **Mission:** A private, operator-owned chain of multi-trade artisan production buildings — shared infrastructure, individually rented studios — enabling solo artisan practitioners to build their business without absorbing the full capital and compliance burden of a standalone commercial space. The Sola Salons model applied to smithing, baking, weaving, and adjacent trades.
- **Relationship to CERES:** Artisan Square is Plan J in the CERES pipeline. The CERES Tier A simulation across 3 trades and 405 evaluation cells demonstrated that artisan production is economically viable in repair/specialty/premium niches, but that the binding constraint is not equipment economics — it is operator pipeline and shared infrastructure. Artisan Square is the physical instantiation of the shared-infrastructure finding. It completes the CERES vertical slice by providing the real-world context in which catalog entries would operate.
- **Repository:** `C:\src\artisan` (Artisan Square spec lives alongside the CERES research that generated it)

---

## 2. The Gap This Fills

No existing building type fully combines:
- Heavy-trade infrastructure (3-phase power, industrial-grade ventilation) for smithing/metalwork
- Food-grade commissary licensing for baking/fermentation/food-craft
- Individual rentable production studios (not shared open-floor-plan access)
- Multi-trade adjacency (a baker next to a weaver next to a smith)
- Month-to-month terms with no employment relationship

Artisans Asylum (Boston) comes closest on the heavy-trade side but explicitly excludes food production. La Cocina SF is the gold standard for food-incubator buildings but is food-only by regulatory design. No facility combines them at the individual studio-rental level.

The gap is structural and regulatory — food safety code and combustion/forge fire code are incompatible occupancies under current IBC without deliberate two-wing design. Artisan Square solves this by design: two wings, one fire-rated spine, each wing with its own occupancy permit.

---

## 3. Operator Model

**Operator type:** Private, operator-owned chain.

The Artisan Square operator is a real estate and infrastructure company that serves artisans — not an artisan business itself. The operator provides space, infrastructure, and compliance umbrella. Tenant craft decisions, customer relationships, pricing, and brand belong entirely to the tenant.

**Civic involvement:** Not structured into the model, but anticipated to emerge. CERES data shows towns can justify civic investment at <$15/household/year. When towns see the workforce development, food security, and local economic multiplier outputs, they find ways to participate — typically by subsidizing the anchor training studio rent, providing below-market land, or contributing economic development grants. The operator does not depend on this but welcomes it.

**Growth sequence:**
1. **Location 1 — Medium (adaptive reuse):** 20-28 studios, 15,000-20,000 sq ft, adaptive reuse of existing industrial building. Prove the model and operations. Build the permitting playbook from real experience.
2. **Locations 2-5 — Medium/Large (purpose-built):** 20-40 studios, purpose-built single-building design using lessons from Location 1. Destination assets in regional markets.
3. **Location 6+ — Small (small-town prototype):** 12-18 studios, scaled-down version of the single-building design for towns of 2,000-15,000 population. This is the CERES sweet spot. May carry civic co-investment more reliably.

---

## 4. Physical Design

### 4.1 Site

15,000-20,000 sq ft (medium location). Light-industrial or mixed-use zone with IBC Group F-2 (light manufacturing) + Group B (business) dual occupancy classification. Single-story preferred (loading dock, forklift access, high ceiling clear). Existing 3-phase electrical service or capacity for service upgrade highly preferred.

**Adaptive reuse target (Location 1):** Former factory, warehouse, or light-industrial building. Desired features: concrete floors, 12-16 ft ceilings, loading dock, 3-phase service or heavy electrical infrastructure, industrial zoning already in place.

**Purpose-built prototype (Locations 2+):** New construction optimized from Location 1 learnings. Single building, two wings separated by 2-hour fire-rated wall (IBC Section 508 Mixed Use Protected).

### 4.2 Floor Plan — Two Wings, One Spine

```
            [ LOADING DOCK ]
                    │
        [ MECHANICAL SPINE ]
          ← Electrical bus, ventilation mains, plumbing trunk →
         /                                    \
TYPE A WING                              TYPE B WING
6,000-7,000 sq ft                        10,000-12,000 sq ft
6-8 studios (250-450 sq ft each)         14-20 studios (150-300 sq ft each)
Heavy: forge, metalwork, pottery kilns   Light: baking, weaving, leather, ceramics
─────────────────── 2-HOUR FIRE-RATED WALL ───────────────────

         [ MANAGEMENT OFFICE + SHARED BATHROOMS + KITCHENETTE ]
         [ ANCHOR TRAINING STUDIO — 150-200 sq ft, below-market ]
         [ SHARED MATERIALS STORAGE CAGES ]
         [ RETAIL GALLERY CORRIDOR — Type B street-facing studios ]
```

### 4.3 Type A Studio Infrastructure (per studio)

- 200A 3-phase sub-panel with individual metering
- Connection stub to shared industrial exhaust riser (forge-grade, ≥2,000 CFM rated per station)
- Concrete floor, 150 lb/sq ft rated
- 14 ft ceiling clearance minimum
- Sound-isolating demising walls (STC 55+)
- Eye-wash station
- Fire suppression (wet pipe, Class D rated)

### 4.4 Type B Studio Infrastructure (per studio)

- 60A 240V single-phase sub-panel with individual metering
- Floor drain + NSF-rated hot-water line (food safety compliant)
- Connection to shared food-grade exhaust riser (separate stack from Type A, grease interceptor on food-producing studios)
- Humidity-controlled HVAC (65-75% RH for fiber arts studios; standard for baking)
- Standard 10 ft ceiling
- Retail window option (street-facing studios)

### 4.5 Shared Infrastructure

| System | Specification | Note |
|---|---|---|
| Main electrical service | 1,000A 3-phase | Deliberately over-built; cheap now, impossible later |
| Exhaust stack — Type A | Industrial-grade, dedicated stack | Combustion byproducts; cannot share with food |
| Exhaust stack — Type B | Food-grade, grease interceptor | Health dept compliant |
| Commissary license | Single Type A commercial kitchen license covering all Type B food tenants | Tenants register under umbrella |
| Loading dock | One commercial dock, shared pallet jack | All trades need bulk delivery |
| Materials storage | Locked individual cages per tenant | Steel, flour, yarn — none fits in studios |
| Management office | 300-400 sq ft | Manager, compliance records, lease files |
| Anchor training studio | 150-200 sq ft, below-market rent | Occupancy pipeline; civic partnership slot |

---

## 5. Tenant Model

### 5.1 Who Rents

| Studio Type | Tenant Profile |
|---|---|
| Type A — forge/metalwork | Journeyman smith, bladesmith, metalwork artist, farrier |
| Type A — pottery/kiln | Potter, ceramic artist, production ceramicist |
| Type B — baking | Cottage baker scaling up, specialty/ethnic bakery startup, artisan bread |
| Type B — fiber arts | Handweaver, natural dye studio, rigid-heddle instructor |
| Type B — leather/other | Leatherworker, bookbinder, candlemaker, soap-maker |
| Anchor training | Pre-commercial artisan, apprentice graduate, vocational partnership |

### 5.2 Lease Terms

- Month-to-month or 6-month minimum
- All-inclusive: space + infrastructure access + commissary umbrella + loading dock + shared storage
- Utilities metered per studio — tenant pays own power (Artisan Square pays common area only)
- No non-compete; tenant owns customer relationships entirely
- Commissary compliance clause: Type B food tenants must maintain health department registration under commissary and comply with inspection requirements

### 5.3 Rent Ranges (medium location, suburban market)

| Studio | Size | Monthly rent |
|---|---|---|
| Type A — forge (350 sq ft) | 350 sq ft | $1,500–2,400 |
| Type A — pottery (300 sq ft) | 300 sq ft | $1,300–2,000 |
| Type B — baking (200 sq ft) | 200 sq ft | $1,100–1,750 |
| Type B — fiber arts (250 sq ft) | 250 sq ft | $875–1,500 |
| Anchor training (200 sq ft) | 200 sq ft | $325–650 (subsidized) |

**Gross monthly potential (24 studios, full occupancy):** $25,000–$42,000
**Gross annual potential:** $300k–$500k

### 5.4 The Graduation Path (the occupancy engine)

Tenants build their customer base, reputation, and revenue in their studio over 2-4 years. When they can afford a standalone commercial lease, they leave. Before leaving, they refer their apprentice or protégé to the vacancy. The social network of practitioners IS the occupancy guarantee — the same dynamic Sola Salons relies on. The anchor training studio deliberately produces the next cohort of tenants.

---

## 6. Economic Model

### 6.1 Build-Out Costs (medium location, adaptive reuse)

| Item | Range |
|---|---|
| Building acquisition / lease | $400k–800k |
| Electrical main service + sub-panels + metering | $80k–150k |
| Ventilation stacks (2 separate systems) | $90k–180k |
| Plumbing (floor drains, NSF lines, grease trap) | $40k–70k |
| Studio demising walls + sound isolation | $60k–100k |
| Fire suppression upgrade | $30k–50k |
| Loading dock + materials storage | $20k–35k |
| Management office + common areas | $25k–40k |
| Commissary licensing + permitting | $15k–30k |
| **Total** | **$760k–1.45M** |

### 6.2 Annual Operating Costs

| Item | Range |
|---|---|
| Property (mortgage or lease) | $80k–160k |
| Staff (1 FT manager + 0.5 FT facilities) | $90k–120k |
| Utilities (common areas, shared systems) | $30k–50k |
| Insurance (commercial + commissary liability) | $25k–40k |
| Maintenance + reserves | $20k–35k |
| **Total** | **$245k–405k/year** |

### 6.3 Unit Economics (24 studios)

| Scenario | Annual gross rent | Operating costs | NOI | Payback |
|---|---|---|---|---|
| Conservative (75% occupancy) | $270k–375k | $325k | Breakeven | — |
| Target (85% occupancy) | $306k–425k | $325k | $0–100k | 12–15 yr |
| Strong (95% occupancy) | $342k–475k | $325k | $17k–150k | 8–10 yr |

### 6.4 Why This Works as a Chain

Single-location economics are marginal. Chain economics compound sharply:
- Brand reduces tenant acquisition cost to near-zero by locations 3-5 (waitlists form)
- Corporate compliance playbook amortizes across locations — Location 1 costs $80-150k in permitting/engineering; Location 10 costs $8-12k (same drawings, local adjustments)
- Bulk purchasing of infrastructure components
- Management team runs multiple locations per person

**The civic unlock:** When a town subsidizes land or the anchor training studio, Location 1 unit economics flip strongly positive. Not a structural dependency but a repeatable accelerant.

---

## 7. Operations and Chain Playbook

### 7.1 Day-to-Day Operations

- 1 FT Location Manager: tenant relations, commissary compliance, maintenance coordination
- 0.5 FT Facilities: HVAC, exhaust system, electrical maintenance
- Software platform: studio billing + maintenance requests (Mindbody / Square or proprietary)
- Tenant onboarding: safety certification, health dept registration under commissary umbrella, fire safety training

### 7.2 The Compliance Playbook (the real IP)

Artisan Square corporate owns and maintains the following as proprietary documents, updated from each location's experience:

| Document | Content |
|---|---|
| **Permitting playbook** | IBC Section 508 mixed-use analysis; fire code variance strategy; dual-occupancy approach by jurisdiction type |
| **Commissary license template** | State-adaptable health dept application package; tenant registration process; inspection prep |
| **Electrical specification** | Stamped engineering drawings for 1,000A 3-phase spine + studio sub-panels; adaptable to any building footprint |
| **Ventilation specification** | Two-stack design with CFM calculations per studio count; industrial + food-grade stacks |
| **Tenant lease agreement** | Month-to-month; all-inclusive; metered utilities; no non-compete; commissary compliance clause |
| **Studio fit-out standard** | What ships with every studio; what tenant adds; what stays at lease-end |

Each new location pays $8-15k in engineering adaptation costs against $80-150k at Location 1. The playbook IS the franchise value even in a non-franchise model.

### 7.3 The Tenant Pipeline (apprentice-to-tenant funnel)

The anchor training studio hosts:
- 6-month subsidized residencies for pre-commercial artisans
- Partnerships with vocational schools, culinary programs, community colleges
- Resident builds practice; Artisan Square holds right-of-first-offer on next available studio

This solves the occupancy risk: you grow your own tenant base rather than recruiting cold from a thin practitioner pool.

---

## 8. Rollout Sequence

| Phase | Location type | Studios | Build-out | Primary goal |
|---|---|---|---|---|
| 1 | Adaptive reuse, suburban | 20-28 | $760k–1.45M | Prove model; build playbook from real experience |
| 2-5 | Purpose-built, suburban/urban | 20-40 | $1-2M each | Scale operations; destination assets; brand established |
| 6+ | Small-town prototype | 12-18 | $500k–900k | CERES sweet spot; civic co-investment likely; rural economic development story |

---

## 9. How Artisan Square Changes the CERES Findings

The CERES simulation showed artisan production is economically viable in repair/specialty/premium niches but identified three binding constraints:
1. **Operator pipeline** — journeyman practitioners don't exist in thin talent markets
2. **Shared infrastructure** — individual operators can't absorb 3-phase power, commissary licensing, industrial ventilation
3. **Capital barrier** — standalone commercial space costs $60-200k to outfit before serving first customer

Artisan Square directly dissolves constraints 2 and 3. Constraint 1 is addressed via the anchor training studio. The CERES catalog entries map directly to Artisan Square tenants:

| CERES entry | Artisan Square studio |
|---|---|
| forge-003 (Shared Tool-Library Coal) | Type A studio in Artisan Square |
| bake-001 (Sourdough Artisan Micro) | Type B baking studio |
| weave-009 (Rigid Heddle Tool-Library) | Type B fiber arts studio |
| bake-011 (Apprentice Training Bakery) | Anchor training studio (below-market) |
| Any market-path winner | Direct commercial tenant |
| Any coop-path winner | Studios collectively rented by a group |

---

## 10. Non-Goals

- Artisan Square does not manage tenant businesses, price their products, or employ practitioners
- Not a retail market or food hall — production-first; retail is secondary and only in street-facing Type B studios
- Not a civic program — civic co-investment is welcomed but not required
- Not targeting commodity production — per DECLINE-VERDICT findings, commodity trades do not benefit from shared infrastructure; specialty/repair/premium niches do
- Not a makerspace (drop-in equipment access model) — individual dedicated studios only; tenants have exclusive use of their space

---

## 11. Success Criteria

**Location 1 validated when:**
- 85%+ occupancy sustained for 12+ months
- At least 1 tenant has graduated to standalone space (the graduation path works)
- At least 1 civic entity has approached operator about training studio partnership (civic interest is organic)
- Permitting playbook is documented and transferable
- Unit economics demonstrate path to 8-10 year payback at 95% occupancy

**Chain validated when:**
- 3 locations operating with positive NOI
- Tenant waitlists at existing locations filling vacancies within 30 days
- Location 4+ opens using the playbook at <15% of Location 1 permitting cost

---

## 12. Next Step: Plan J

Plan J will implement the Artisan Square spec as a CERES research + catalog + simulation cycle:
- Research: What does the Artisan Square operator's unit economics look like as a *catalog entry* within the CERES schema? (The building itself can be modeled as a new "trade" — the trade of building artisan infrastructure)
- Catalog: 10-15 Artisan Square facility designs spanning small/medium/large formats, rural/suburban/urban contexts
- Simulation: Run Tier A on the building-operator lens (market/coop/civic) to find which Artisan Square configurations pencil out where
- Playbook: Per-context guidance for building or funding an Artisan Square
