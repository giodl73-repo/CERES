---
trade: artisan-square
doc_type: functional-requirements
version: "1.0"
status: draft
review_status: {panel: pending, editorial: pending}
derived_from:
  - research/trades/artisan-square/type-a-heavy.md
  - research/trades/artisan-square/type-b-light.md
  - research/trades/artisan-square/combined-campus.md
sources_count: 37
---

# Artisan Square: Cross-Facility Functional Requirements

## 1. Purpose

This document specifies what an Artisan Square facility MUST provide to serve its
artisan tenants. It is written from the operator's perspective: the entity that builds,
licenses, staffs, and maintains the building. It does not prescribe craft practice —
that belongs to trade-specific REQUIREMENTS documents. It abstracts the physical,
regulatory, and operational commitments the operator must meet regardless of which
wing or trade is under discussion. Plan K catalog authors use this document as the
input specification: every Artisan Square catalog entry must satisfy each applicable
requirement listed here, or explicitly state which requirements are inapplicable and
why. Requirements apply at the facility level, not the tenant level; the operator
delivers them, the tenant depends on them.

---

## 2. Electrical Requirements

Artisan Square's two-wing design carries fundamentally different power density
profiles. These are not preferences — they are driven by the process loads of the
trades served.

### Type A Wing (Forge, Metalwork, Kiln)

**Power density:** 150–200 W/sq ft across the studio floor. This reflects concurrent
induction forge, kiln, studio lighting, and auxiliary equipment operation. The
density assumption must be met at the sub-panel level, not merely at the main service.

**Per-studio service:** 200A 3-phase sub-panel, individually metered. A 10 kW
induction forge on 208V 3-phase draws approximately 28A per leg. A production
electric kiln (7–10 cubic feet) draws 50–60A at 240V. A single-phase 200A panel
cannot serve these loads concurrently without leg-balancing problems; 3-phase
eliminates that constraint. Individual metering is operationally required: metalwork
power bills are high and highly variable. Unmetered Type A studios produce cost
disputes that cannot be fairly resolved through allocation.

**Wing-level service:** 800A 3-phase minimum for a wing of 6–8 Type A studios.
This is a floor, not a target. The main service over-build is cheaper at construction
than a post-occupancy upgrade; large commercial service upgrades (above 400A) carry
utility coordination lead times of 6–18 months in suburban markets.

**3-phase requirement:** 3-phase is required at the building level even if individual
studios run single-phase draws. Single-phase panels cannot serve 3-phase equipment;
the reverse is always true. The Type A wing design must not foreclose 3-phase
equipment installation by any tenant.

### Type B Wing (Baking, Fiber Arts, Light Trades)

**Power density:** 40–60 W/sq ft. Baking studios drive the upper bound: one commercial
convection oven (4.5–7.5 kW), a stand mixer (2–3 kW), refrigeration, and lighting
simultaneously. Fiber arts studios are lower-density users — a 240V 30A circuit is
the spec standard for hand-loom and powered-loom operations. Non-food studios (leather,
soap-candle, light ceramics) are at the low end of this range.

**Per-studio service — baking:** 60A 240V single-phase sub-panel, individually metered.
This is a minimum. Studios that add a proofing cabinet, dough sheeter, or commercial
refrigerator will approach or reach this ceiling; the operator should not over-promise
panel headroom beyond the spec rating.

**Per-studio service — fiber arts:** 240V 30A single-phase sub-panel, individually
metered. This accommodates both hand-loom operation (lighting-only draw) and a
powered Jacquard or dobby mechanism (30–40A draw) without a sub-panel replacement.

**Wing-level service:** 400A 3-phase minimum for 15–20 Type B studios. 3-phase at
the wing-level distribution panel enables single-phase draws to be balanced across
legs without asymmetric loading on the building's main service.

### Combined Campus

**Main service:** 1,000–1,200A 3-phase total building service. For a 24-studio
combined campus (8 Type A at 200A 3-phase plus 16 Type B at 60A 240V single-phase),
the pre-headroom minimum is approximately 800A; the 1,000A service provides the 20%
headroom required as a planning standard. The 1,200A upper bound accommodates a
location with a larger studio mix or a planned expansion bay.

**Sub-panel configuration:** Separate distribution panels per wing, fed from the
main service. Wing-level sub-panels allow the operator to isolate a wing for
maintenance without interrupting the other. Type A and Type B panels must be
labeled and documented separately for inspection and emergency-shutdown purposes.

**Individual metering:** Every studio in both wings must carry individual metering.
Electrical consumption variance between a forge studio and a weaving studio is large
enough that unmetered combined-campus operation produces unrecoverable operator cost.
Metering infrastructure must be installed at build-out, not added later; retro-fit
metering in an occupied multi-tenant building is disruptive and expensive.

**Critical note:** 3-phase service is required at the building level in all
configurations — including buildings that begin with Type B studios only — if any
Type A wing is contemplated at any future date. Retrofitting 3-phase service after
single-phase occupancy has begun is a major disruption; the conduit runs must be
sized for 3-phase at initial construction regardless of Day 1 tenant mix.

---

## 3. Ventilation Requirements

The two-wing model requires two entirely separate exhaust systems. This is not a
preference or a best-practice recommendation: it is a commissary-licensing
requirement. Forge and metalwork exhaust contains combustion byproducts and metal
particulates that cannot share ductwork with food-production spaces under any
commissary standards interpretation. Any single-stack or shared-plenum configuration
that mingles Type A and Type B exhaust will be rejected by the health department
during commissary license inspection.

### Type A Industrial Exhaust

**Capacity:** 2,000 CFM minimum per forge or kiln station. Combustion forges and gas
kilns consume oxygen and produce CO, nitrogen oxides, and combustion particulates.
Induction forges produce metal oxide fumes during flux-welding operations. Both load
profiles require capture-at-source exhaust at or above this CFM floor.

**Stack construction:** Dedicated fire-rated vertical chase, 2-hour fire-resistance
rating, continuous from studio connection to roofline. Any duct penetrating a
fire-rated assembly in F-2 occupancy requires 2-hour-rated chase construction per
IBC Section 717 (or current equivalent in the adopted edition). Each studio
connection must include a motorized fire damper that closes automatically when the
studio is unoccupied, preventing backdraft from an active main riser into an empty
studio.

**CO monitoring:** Carbon monoxide detection required per studio or per 1,000 sq ft
of studio area, whichever produces more monitoring points. Combustion forge operation
in an enclosed studio can accumulate CO to OSHA's 50 ppm TWA ceiling within minutes
if exhaust capture fails. CO alarms must be wired to the building management system,
not battery-only standalone units.

**Kiln exhaust sub-circuit:** Pottery studios require a separate exhaust circuit for
clay-preparation areas (silica-dust capture at low velocity) in addition to the
high-temperature kiln-top flue connection. A single duct cannot serve both functions
well; the clay-work capture operates at low velocity to prevent respirable silica
dispersion while the kiln exhaust must handle high-temperature flue gases. The two
circuits may share the main Type A stack above the studio level but must originate
from separate in-studio stub connections.

**Annual inspection:** Motorized dampers on the Type A stack require annual inspection
and functional testing. This is an operator maintenance obligation, not a tenant
responsibility.

### Type B Food-Grade Exhaust

**Capacity:** 500 CFM minimum per baking studio. The Type B food-grade exhaust
handles grease-laden vapor from commercial ovens and cooking surfaces. 300–600 CFM
per food studio is the operating range; 500 CFM is the required minimum for a
baking studio with one commercial convection oven. The aggregate for a wing of 10–15
food studios is 2,000–4,000 CFM at the stack base; the stack and fan must be sized
for the aggregate, not per-studio.

**Grease interceptor:** A mechanical or hydromechanical grease interceptor is required
at the base of the food-grade exhaust riser before connection to the municipal drain.
The interceptor handles fat, oil, and grease (FOG) discharged from food studio cooking
and cleaning operations. Interceptor pumping is required every 30–90 days depending
on tenant cooking activity; this is an operator-managed maintenance obligation. Failure
to maintain the interceptor is a commissary compliance deficiency — health department
inspectors will flag an unmaintained interceptor as a facility-level violation.

**UL 710 compliance:** All food studio exhaust connection points must meet UL 710
(commercial kitchen ventilation) at the hood-to-duct interface. Tenant-installed
exhaust hoods must be verified for UL 710 compliance before studio occupancy; the
operator holds this verification obligation as the commissary licensee.

**Separation from Type A:** The food-grade stack must have no shared duct sections,
plenums, or discharge points with the Type A industrial stack. The stacks may share
structural chase space in the mechanical spine but are separate systems from the
studio connection to atmosphere.

### Makeup Air

**Volume:** Replace 80% or more of exhausted volume with tempered outdoor air.
Combustion forges and gas kilns consume oxygen from the studio environment; without
adequate makeup air, ambient O2 in a sealed Type A studio will fall below OSHA's
19.5% oxygen-deficiency threshold during sustained combustion operation. The makeup
air unit must be designed for combustion tenants regardless of whether Day 1 tenants
run induction forges only — retro-fitting combustion-ready makeup air into an occupied
building is a major disruption.

**Tempering:** Makeup air must be conditioned (heated or cooled) before delivery —
not raw outdoor air in winter or summer. Raw outside air at sub-freezing temperatures
delivered at 80% of exhaust volume will destabilize kiln-firing temperature control
in Type A studios and create tenant comfort problems in Type B studios. A direct-fired
or indirect makeup air unit with a building management system-controlled setpoint is
the standard solution.

**Cross-contamination dampers:** In a combined campus, a dampered supply-air system
must maintain positive pressure in Type B food spaces relative to Type A industrial
spaces. Positive pressure in food spaces blocks particulate migration from the
industrial wing. Type B studios must not draw replacement air through Type A zones;
the makeup air zoning must be documented in the mechanical drawings submitted for
health department review.

---

## 4. Floor Load and Ceiling Requirements

### Type A Wing

**General floor load:** 150 lb/sq ft minimum across the entire studio floor. This
is the practical minimum for anvil stands, leg-vise anchor bolts, forge equipment,
and kiln placement. It is not aspirational — anvil stands and equipment dolly loads
exceed wood-frame floor capacity in standard commercial construction. Type A studios
require a concrete slab rated to this specification. Wood-frame subfloor systems are
categorically inadequate.

**Kiln pad:** Local structural reinforcement is required at each kiln pad location.
An electric kiln in the 7–10 cubic foot range weighs 400–600 lb loaded; a gas-fired
car kiln or catenary arch kiln can exceed 1,000 lb. The 150 lb/sq ft general rating
addresses distributed loads but does not address point loads from kiln feet on a small
contact area. A reinforced concrete pad poured on the slab (typically 4–6 inches over
the base slab) is required at each kiln position to distribute point load and provide
a fire-rated surface. Kiln pad locations must be specified in the studio lease plan
before permit submission; adding them post-occupancy requires vacating the studio.

**Ceiling height:** 14 ft minimum clearance in all Type A studios. Long-stock
manipulation (bar stock, billet, tube rotation) requires head clearance above 10 ft
for the swing arc of long stock at horizontal. Equipment dolly clearance and the
ability to operate a floor-standing power hammer with vibration buffer also require
headroom that standard 10–12 ft commercial ceilings do not provide. 16 ft is
preferred in purpose-built configurations.

### Type B Wing

**General floor load:** 80 lb/sq ft minimum. Commercial baking equipment — deck
ovens (400–800 lb), commercial refrigerators (300–400 lb), stand mixers (150–300 lb)
— is substantially lighter than Type A metalwork and kiln equipment but still exceeds
the 50 lb/sq ft rating of some light commercial framing systems. The 80 lb/sq ft
floor must be confirmed before permitting, not assumed.

**Ceiling height:** 10 ft minimum. Standard commercial construction at 10–12 ft
satisfies this requirement. The minimum ensures clearance for deck oven hoods and
exhaust connections without custom ductwork routing.

**Flooring — food studios:** Quarry tile, sealed concrete, or other NSF/ANSI 2-
compliant flooring is required in all food-producing studios. No carpet, no unsealed
concrete, no porous surface. Minimum 2% slope to the floor drain. This requirement
extends to the grout lines and substrate, not merely the surface material; the health
department inspector will check grout condition and verify there are no standing-water
zones.

### Loading Dock

**Floor rating:** 20,000 lb minimum for pallet and forklift use. The loading dock
serves both wings: ceramic equipment, kiln delivery, raw materials for metalwork
studios, and bulk food-production ingredients all move through this point. A floor
rating below 20,000 lb is a forklift-incident liability and will be flagged in an
insurance underwriting review for an F-2 occupancy building.

---

## 5. Plumbing Requirements

### Type A Studios

**Eye-wash stations:** One eye-wash station per studio, or one per 1,000 sq ft of
studio area in studios larger than 1,000 sq ft, whichever results in more stations.
OSHA 29 CFR 1910.151 requires eye-wash facilities where corrosive materials are
present; relevant hazards in Type A studios include flying scale, quench splash, and
flux spattering. Eye-wash stations must be within 10 seconds of travel from the primary
work zone per ANSI Z358.1 (Emergency Eyewash and Shower Equipment). They must be
plumbed to tepid water (60–100°F), not cold-tap.

**Quench tank supply:** Where quench tank or slack tub infrastructure is provided by
the operator (rather than tenant-owned), a cold water supply line stub must be present
in the studio. Tenant-owned quench buckets and slack tubs do not require a plumbing
connection but the studio must have a utility sink capable of filling them. A floor
drain in Type A studios is recommended but not universally required; the operator
should specify it as a build-out option.

### Type B Studios — Food-Producing

**Floor drain per studio:** NSF-rated floor drain is required in every food-producing
Type B studio. Commercial food safety code requires a floor drain in any space where
water is used for cleaning. The drain must connect to the building's grease interceptor
system — not directly to the municipal sewer, which would bypass the required FOG
treatment.

**Hot water temperature:** NSF-rated hot water at a minimum of 110°F at the tap for
equipment and surface sanitation per state health code. The type-b-light.md source
cites 120°F at tap; 110°F is the commonly applied state health department minimum for
food equipment sanitizing; the operator should specify 120°F as the design setpoint
to maintain margin against the line-loss that reduces tap temperature below the
building hot-water system temperature. This is a dedicated hot-water line from the
building system, not shared with restroom circuits.

**Grease trap on drain lines:** All food studio drain lines must connect through the
building's grease interceptor before reaching the municipal sewer. A food studio
connected directly to the municipal drain without a grease interceptor will trigger
a pretreatment violation from the municipal utility, which is a commissary compliance
deficiency independent of the health department.

### Combined Campus Drainage

**Separate drain systems:** Type A and Type B drain lines must not share a grease
interceptor or a common sump that mixes metalwork drainage with food-production
drainage. Metalwork drainage (quench water, floor-washing water with metal particulates)
is not food-safe and must route separately. This is not merely a best practice: a
health department inspector who identifies cross-connection between metalwork drainage
and food-studio drainage will suspend the commissary license.

**No cross-connection:** Any drain line serving both a Type A studio and a Type B
studio (for example, a shared floor drain in a corridor between wings) is a code
violation in the commissary context. The mechanical drawings must show complete
drainage separation; the commissary license application must certify it.

---

## 6. Zoning and Occupancy Requirements

### Type A Only

**Zoning classification:** Light-industrial (IBC Group F-2) zoning is required for
any facility that includes Type A studios with forge, metalwork, or kiln operations.
Group F-2 (light manufacturing, low-hazard industrial) is the IBC classification that
covers these operations. Mixed-use or retail-commercial zoning is not sufficient for
Type A without a conditional use permit or a zoning variance — and both add permitting
time, cost, and risk. A site selected for a Type A-only or combined campus facility
must be confirmed as F-2-eligible before land acquisition, not after.

**Noise ordinance exposure:** Type A operations (power hammer, forge work) produce
impulse noise in the 95–110 dB range at the operator position. STC 55+ demising walls
protect adjacent tenants; they do not protect the exterior property line. A Type A
facility must commission an exterior noise analysis before permit submission for any
building configuration where power-hammer operations are anticipated. The tenant lease
must restrict high-impulse operations to daytime hours (7 AM–8 PM) without a specific
noise variance.

### Type B Only

**Occupancy classification:** Food-producing studios classify as IBC Group F-2 (light
manufacturing — food and beverage products) under the conservative assumption adopted
by the CERES spec. Group B (business) applies to non-food studios (fiber arts,
leather, soap-candle) and to the management office. If the local building official
reads baking studios as Group B rather than F-2, the Type B facility design is
over-specified — the preferred direction. Group M (mercantile) may apply to
street-facing retail studios; this triggers higher parking and egress requirements
in some jurisdictions and should be anticipated in the site plan.

**Commissary license:** The operator must hold a state-issued Type A commercial
kitchen license (the highest-grade food facility license) covering all
food-producing Type B studios as a multi-operator commissary. This license is held
by the building entity, not by individual tenants. Tenants register with the health
department as commissary users under the operator's license. The commissary license
application must describe the multi-tenant structure and identify all food-producing
studio spaces; the operator should not attempt to obtain the license before the studio
count and layout are finalized.

### Combined Campus — IBC §508.4 Mixed Use Protected

**Fire-rated separation:** IBC §508.4 (Mixed Use Protected, IBC 2021) requires a
2-hour fire-resistance-rated separation assembly between occupancy groups in a mixed-
use building. For the Artisan Square combined campus, this is the demising assembly
between the Type A F-2 zone and the Type B F-2/B zone. The assembly must be continuous
from foundation to roofline — no gaps, no penetrations without rated fire-stopping.
The specific assembly (CMU wall, fire-rated gypsum board per UL design listing, or
other) must be specified by a licensed structural engineer and reviewed by the local
authority having jurisdiction (AHJ) before permit submission.

**Commissary scope exclusion:** The commissary umbrella license covers Type B only.
No Type A space with metal grinding, torch use, forge operation, or kiln firing falls
under the commissary in any circumstances. The exclusion must appear in the commissary
license application, in the health department's inspection records, and in each Type
A tenant lease. A boundary failure — any Type A space inadvertently included in the
commissary scope — risks the commissary license for all Type B tenants.

**Independent fire suppression zones:** NFPA 13 wet-pipe suppression is required
throughout. The Type A zone requires high-temperature-rated sprinkler heads in kiln
proximity (212°F+ activation temperature; standard 155°F heads will activate at kiln
surface temperatures during high-fire operation). The Type A and Type B zones must
be independently controllable zones on the suppression system so that a Type A zone
isolation does not suppress the Type B wing.

---

## 7. Operator Capacity Requirements

### Location Manager

**Ratio:** 1.0 FTE location manager per 25–30 studios (both wings combined). For a
small Artisan Square location (18–22 studios), the location manager is the sole
management staff member. For a large location (30+ studios), an assistant manager or
part-time administrative support is required. The location manager's duties include:
tenant onboarding, lease management, walk-through inspections, health department
liaison, and first-response coordination for facilities issues. This role cannot be
performed remotely or part-time at a location with food-producing tenants; the
commissary compliance obligations require physical presence.

### Facilities and Mechanical

**Ratio:** 0.5 FTE for mechanical and electrical maintenance per location. This may
be structured as a half-time staff position or as a contracted facilities technician
with a minimum response SLA (4 hours for HVAC and ventilation failures; 24 hours for
non-critical items). The facilities role covers: exhaust damper inspection, grease
interceptor service coordination, humidity system monitoring in fiber arts studios,
CO monitor testing, and electrical sub-panel inspection. A location without dedicated
facilities coverage will accumulate deferred maintenance that produces commissary
compliance deficiencies and tenant disputes.

### Commissary Compliance Monitoring

The operator's commissary obligations do not end at license issuance. Ongoing
compliance monitoring includes:

- **Health department inspection preparation:** The operator must prepare for annual
  health department inspections of the entire commissary (not individual tenant
  inspections). Preparation includes verifying that all tenant commissary user
  agreements are current, that sanitation logs are being maintained by tenants, and
  that the physical facility (drains, hot water, exhaust, flooring) is in passing
  condition. The location manager should run a full pre-inspection checklist at least
  60 days before the anticipated annual inspection date.

- **Tenant food-safety record oversight:** Each food-producing tenant must maintain
  sanitation logs and make them available to the operator on 24-hour notice. The
  location manager must conduct quarterly walk-throughs of all food studios using a
  checklist that mirrors the health department's inspection criteria. One non-compliant
  tenant can trigger a conditions notice against the entire commissary license.

- **Product scope monitoring:** Tenants must not produce food categories outside their
  registered commissary use without operator notification and health department
  registration amendment. The operator must have a documented process for reviewing
  and approving tenant product-scope changes before they occur, not after discovery
  during inspection.

### Type A Safety Oversight

**Minimum competency verification:** Before studio key delivery, each Type A tenant
must provide documented evidence of safety training covering forge or kiln operation,
as applicable. For metalwork tenants: completion of an ABANA-affiliated forge safety
course or equivalent documented training. For pottery tenants: documented kiln
operation certification. The operator is not certifying craft skill; it is
documenting that the tenant can operate exhaust systems, fire suppression, CO monitors,
and emergency shutoff systems — a liability and insurance prerequisite. This
verification must be recorded in the tenant file and renewed if the tenant's primary
operator changes.

---

## 8. Functional Requirements Summary Table

| Req ID | Requirement | Type A Value | Type B Value | Combined Value | Source |
|--------|-------------|--------------|--------------|----------------|--------|
| FAC-01 | Power density (W/sq ft) | 150–200 W/sq ft | 40–60 W/sq ft | Both apply per wing | type-a-heavy §2; type-b-light §2 |
| FAC-02 | Per-studio electrical service | 200A 3-phase sub-panel | 60A 240V single-phase (baking); 30A 240V (fiber) | Both apply per wing | type-a-heavy §2; type-b-light §2, §7 |
| FAC-03 | Individual tenant metering | Required per studio | Required per studio | Required all studios | type-a-heavy §4; combined-campus §3 |
| FAC-04 | Wing-level electrical service | 800A 3-phase (6–8 studios) | 400A 3-phase dist. panel (15–20 studios) | 1,000–1,200A 3-phase total | combined-campus §3, §5 |
| FAC-05 | 3-phase at building level | Required | Required at distribution | Required; future-proofs both wings | type-a-heavy §4; combined-campus §3 |
| FAC-06 | Industrial exhaust capacity | ≥2,000 CFM per forge/kiln station | N/A | Per Type A spec; separate from food stack | type-a-heavy §2, §4 |
| FAC-07 | Food-grade exhaust capacity | N/A | ≥500 CFM per baking studio | Per Type B spec; separate from industrial | type-b-light §2, §4 |
| FAC-08 | Exhaust stack fire rating | 2-hour rated vertical chase | UL 710 compliant connections | Two separate stacks; no shared ductwork | type-a-heavy §4; type-b-light §4 |
| FAC-09 | Grease interceptor | N/A | Required at food-grade stack base; pump every 30–90 days | Operator-managed; Type B only | type-b-light §4, §7 |
| FAC-10 | CO monitoring | Required per studio or per 1,000 sq ft | N/A | Wired to BMS; Type A only | type-a-heavy §2 |
| FAC-11 | Makeup air volume | ≥80% of exhausted volume, tempered | ≥80% of exhausted volume, tempered | Dampered zones; positive pressure in food spaces | type-a-heavy §4; combined-campus §3 |
| FAC-12 | General floor load rating | 150 lb/sq ft (concrete slab) | 80 lb/sq ft | Both apply per wing | type-a-heavy §2, §3 |
| FAC-13 | Kiln pad point load | 1,000+ lb point load; reinforced pad required | N/A | Type A only; specified pre-permit | type-a-heavy §3 |
| FAC-14 | Loading dock floor rating | 20,000 lb for pallet/forklift | 20,000 lb for pallet/forklift | Shared; 20,000 lb minimum | combined-campus §3 |
| FAC-15 | Ceiling height minimum | 14 ft (16 ft preferred) | 10 ft | Both apply per wing | type-a-heavy §2; type-b-light §2 |
| FAC-16 | Food studio flooring | N/A | NSF/ANSI 2-compliant; 2% slope to drain | Type B food studios only | type-b-light §2, §7 |
| FAC-17 | Eye-wash stations | 1 per studio or per 1,000 sq ft; tepid water | N/A | OSHA 29 CFR 1910.151; ANSI Z358.1 | type-a-heavy §2 |
| FAC-18 | Floor drain — food studios | Recommended | 1 NSF-rated drain per food studio | Required; connects to grease interceptor | type-b-light §2, §7 |
| FAC-19 | Hot water — food studios | N/A | ≥110°F (120°F design setpoint) at tap; NSF-rated | Type B food studios; separate from restroom | type-b-light §2, §7 |
| FAC-20 | Drain separation | Metalwork drainage separate from food drainage | Food drainage to grease interceptor only | No cross-connection permitted | combined-campus §3; type-b-light §4 |
| FAC-21 | Zoning classification | IBC F-2 light-industrial required | IBC F-2 (food) or Group B; mixed-use compatible | IBC §508.4 Mixed Use Protected; 2-hr fire-rated separation | type-a-heavy §1; type-b-light §4; combined-campus §2 |
| FAC-22 | Commissary license | N/A | Operator-held Type A commercial kitchen license | Covers Type B only; explicitly excludes Type A | type-b-light §2, §4; combined-campus §3 |
| FAC-23 | Fire-rated wing separation | 2-hr between F-2 zones where applicable | 2-hr where adjacent to Type A | Foundation-to-roofline continuity; AHJ review required | combined-campus §2 |
| FAC-24 | Location manager staffing | 1.0 FTE per 25–30 studios | 1.0 FTE per 25–30 studios | Shared; cannot be remote/part-time with food tenants | type-b-light §6; combined-campus §4 |
| FAC-25 | Facilities maintenance staffing | 0.5 FTE per location | 0.5 FTE per location | Shared; 4-hr SLA for HVAC/exhaust failures | type-a-heavy §6; type-b-light §6 |

---

## 9. Divergence Log

This section documents where Type A and Type B requirements differ fundamentally,
with implications for combined-campus design.

**DIV-01: Exhaust chemistry and stack separation.**

Type A exhausts combustion byproducts (CO, NOx, metal oxide fumes) and high-
temperature kiln flue gases. Type B exhausts grease-laden vapor and steam from food
cooking and cleaning. The chemical profiles are incompatible in both directions: forge
exhaust in food-production ductwork is a health code violation; food-grade grease
vapor in an industrial stack creates fire hazard and cross-contamination of the
industrial capture system. The combined campus must build and maintain two entirely
separate exhaust systems — not a shared main stack with branch separators. Any
architectural or cost-reduction proposal that merges the stacks above a split-point
must be rejected at design review: health departments have not accepted split-stack
designs for commissary facilities in US markets. *Combined-campus implication:*
Mechanical drawings require explicit stack separation from studio connection to
atmosphere, verified during commissary license inspection. Two stack risers must
penetrate the roofline separately. The structural cost of the second chase is not
avoidable.

**DIV-02: Zoning classification and site selection.**

Type A requires industrial or mixed-use zoning with F-2 light-manufacturing
eligibility. Type B can occupy retail-commercial corridors on ground floors under
mixed-use zoning — this is a strategic advantage, not a detail, because it places
Type B studios where artisan customers already shop and live. A combined campus must
be sited on a parcel that satisfies the more restrictive requirement (Type A /
F-2), which constrains the operator's site selection away from the main-street
retail corridors where Type B generates maximum foot traffic. The divergence is not
resolvable through design: F-2 zoning is a parcel-level designation. *Combined-campus
implication:* The combined campus accepts a site-selection constraint (industrial or
mixed-use parcels only) in exchange for the destination and cross-traffic benefits of
co-location. Locations where F-2-eligible parcels adjoin retail corridors — industrial
adaptive-reuse on a main street in a transitional district — are the site-selection
target. Greenfield suburban industrial parks are lower-cost but sacrifice the Type B
foot-traffic advantage.

**DIV-03: Health code involvement and compliance burden.**

Type A operations carry no health department involvement. No food is produced; no
commissary license is required; no health department inspection occurs. The Type A
operator's compliance calendar is building code (IBC F-2), NFPA 13, and OSHA — all
of which are inspected at fixed intervals (occupancy permit, annual fire marshal,
periodic OSHA audit). Type B operations under a commissary umbrella are subject to
continuous health department jurisdiction: the operator holds the license, every
food tenant is a registrant, the license is inspected annually at a minimum, and
any tenant's non-compliance can trigger conditions on the entire license. One tenant
failing to maintain sanitation logs can produce a conditions notice that affects every
other food tenant in the building. *Combined-campus implication:* The operator must
staff and manage the commissary compliance function as an ongoing operational
obligation — not a one-time permitting event. The location manager must have health
department compliance as a primary job function, not a secondary one. The combined
campus operator cannot hire a general-purpose property manager and expect commissary
compliance to run itself.

**DIV-04: Noise profile and neighbor impact.**

Type A forge operations produce impulse noise at 100+ dB at the operator position
(hammer-on-anvil); power-hammer operations produce 95–110 dB at operator level. These
levels require STC 55+ demising walls to protect adjacent tenants and an exterior
noise analysis to establish municipal compliance at the property line. Type B baking
studios produce 70–80 dB from commercial mixer and oven fan operation — well within
standard commercial-occupancy noise tolerances. A Type B-only facility faces no
special noise compliance obligations beyond standard commercial construction.
*Combined-campus implication:* The noise compliance design for a combined campus must
address both the tenant-to-tenant isolation (STC 55+ for Type A demising walls) and
the exterior-property-line analysis for power-hammer operations. The 2-hour
fire-rated separation wall between Type A and Type B wings serves double duty as the
primary acoustic barrier, but it must be designed explicitly for STC 55+ performance,
not just fire-resistance. CMU walls achieve both; light-frame fire-rated assemblies
may meet the fire-rating without achieving STC 55+. The structural engineer must
specify for both.

**DIV-05: Humidity control requirements.**

Type A studios have no humidity control requirement. Metal and ceramic production is
insensitive to ambient relative humidity within normal commercial HVAC operating
ranges (40–60% RH). Type B fiber arts studios for wool and silk weaving require
65–75% RH — a range that standard commercial HVAC cannot maintain in dry climates or
dry winters without supplemental humidification. The HVAC system serving fiber arts
studios requires RH sensors with building management system integration, automated
alerts below 45% RH or above 80% RH, and a 4-hour response SLA for humidification
system failures. Over-humidification above 80% RH creates mold risk in stored fiber
materials, a health and property liability. *Combined-campus implication:* The
mechanical design must treat the fiber arts zone as a separately controlled humidity
zone — it cannot share an HVAC air-handler or setpoint with either the Type A wing or
the non-fiber Type B studios without compromising the humidity envelope.

---

## 10. Sources

Sources inherited from the three facility research chapters. Full citation detail,
including all CITATION-NEEDED placeholders, is carried in each source chapter.

1. Artisan Square Design Specification, v0.1 (2026-04-19). `specs/2026-04-19-artisan-square-design.md`. Sections 4 and 5 (infrastructure specifications and rent ranges). Primary design-intent reference for all facility specifications. [type-a-heavy §2; type-b-light §2; combined-campus §3]

2. International Building Code (IBC) 2021. §508.4: Mixed Use Protected occupancy separation requirements. 2-hour assembly requirement for F-2/B separation. [combined-campus §2; type-a-heavy §1; type-b-light §4]

3. International Building Code (IBC). Group F-2 (Light Industrial Manufacturing) occupancy classification. IBC Table 307.1(2). [type-a-heavy §1; type-b-light §4]

4. International Building Code (IBC). Section 717 (or current equivalent): Fire-rated duct and chase construction requirements for F-2 occupancy. [type-a-heavy §4]

5. NFPA 13: Standard for the Installation of Sprinkler Systems. Wet-pipe requirements, high-temperature head specifications, suppression zoning across occupancy separations. [type-a-heavy §4; combined-campus §2]

6. OSHA 29 CFR 1910.151: First Aid. Eye-wash station requirement for corrosive-material exposure environments. [type-a-heavy §2]

7. OSHA 29 CFR 1910.1053: Respirable Crystalline Silica standard. PEL 50 micrograms/m³ 8-hr TWA. Applicable to pottery studio clay-preparation areas. [type-a-heavy §3]

8. OSHA oxygen deficiency guidance: 19.5% O2 deficiency threshold for combustion-equipment contexts. [type-a-heavy §4]

9. ANSI Z358.1: Emergency Eyewash and Shower Equipment. 10-second travel-distance requirement; tepid water specification. [type-a-heavy §2]

10. NSF International. NSF/ANSI 61 — Drinking Water System Components. NSF-rated hot-water line specification. [type-b-light §2, §7]

11. NSF International. NSF/ANSI 2 — Food Equipment. NSF-rated flooring and food contact surface requirements. [type-b-light §2, §7]

12. UL 710: Commercial kitchen ventilation standard. Hood-to-duct interface compliance for food studio exhaust connections. [type-b-light §4]

13. La Cocina SF. Program documentation and commissary licensing structure. San Francisco, CA. Multi-tenant commissary umbrella model. [CITATION-NEEDED: La Cocina published program guides] [type-b-light §2]

14. Artisans Asylum, Somerville MA. Studio membership tiers; absence of dedicated F-2 forge studio tenancy. [CITATION-NEEDED: current artisansasylum.com rates] [type-a-heavy §2]

15. East End Maker Hub, Houston TX. Heavy-fabrication studio rental rates ($18–28/sq ft/year cited). [CITATION-NEEDED: current rates from eastendmakerhub.com] [type-a-heavy §5]

16. ABANA (Artist Blacksmiths Association of North America). Forge safety course structure and affiliate network. [CITATION-NEEDED: artisanblacksmith.org or direct contact] [type-a-heavy §6]

17. Manchester Craft and Design Centre, Manchester UK. Cross-trade foot-traffic documentation. [CITATION-NEEDED: operator report or tenant survey] [combined-campus §1, §4]

18. CommonWealth Kitchen, Boston MA. Commissary kitchen rates and dedicated studio pricing. [CITATION-NEEDED: published program documentation] [type-b-light §5]

19. CERES Baking Trade REQUIREMENTS.md. `research/trades/baking/REQUIREMENTS.md`. Commissary licensing as capital-barrier constraint. [type-b-light §2]

20. CERES Weaving Trade REQUIREMENTS.md. `research/trades/weaving/REQUIREMENTS.md`. Humidity envelope requirements R-01 through R-03. [type-b-light §3]

21. [CITATION-NEEDED: Multi-tenant commissary license suspension when individual tenant violates conditions — state health department administrative law; California, New York, and Texas provide the most documented case patterns.] [type-b-light §4]

22. [CITATION-NEEDED: State health department commercial kitchen permit cost schedules — $1,500–$6,000 initial; $300–$1,500 annual renewal; aggregated from public state health department fee schedules.] [type-b-light §2]

23. [CITATION-NEEDED: RH requirements for wool weaving — textile engineering or conservation science source confirming 65–75% range.] [type-b-light §3, §7]

24. [CITATION-NEEDED: Utility industry or construction industry data on large commercial electrical service upgrade lead times (>400A) in suburban US markets; 6–18 months range cited.] [combined-campus §3]

25. [CITATION-NEEDED: ASHRAE or equivalent guidance on makeup air unit design for mixed-occupancy buildings with separated exhaust systems; damper zoning for positive-pressure food production spaces.] [combined-campus §3]

26. [CITATION-NEEDED: IBC 2021 §508.4 continuity requirements for fire separation assemblies in mixed-occupancy buildings — foundation-to-roofline specification.] [combined-campus §5]

27. [CITATION-NEEDED: IBC 2021 §508.4 — confirm 2-hour assembly requirement for F-2/B separation; verify edition adopted by target jurisdiction.] [combined-campus §2]

28. [CITATION-NEEDED: NFPA 13 sections governing suppression zoning across occupancy separations; Class D metal fire applicability to metalwork studios.] [combined-campus §2]

29. [CITATION-NEEDED: Kiln surface temperature during cone 10 firing — exterior surface of standard 7–10 cu ft electric kiln; manufacturer spec or safety data.] [type-a-heavy §4]

30. [CITATION-NEEDED: Municipal noise ordinance daytime dBA limits for light-industrial zones — representative jurisdiction; Houston, Austin, or comparable suburban US market.] [type-a-heavy §6]

31. [CITATION-NEEDED: Measured SPL for power hammer and hand hammer in commercial metalwork studio at operator position — NIOSH or occupational-health source.] [type-a-heavy §6]

32. [CITATION-NEEDED: Structural engineering reference for kiln pad design — point load distribution requirements for electric kiln on concrete slab.] [type-a-heavy §3]

33. [CITATION-NEEDED: Permitting timeline difference for gas vs. electric kiln in US commercial building — fire code source or contractor experience; 4–8 weeks cited.] [type-a-heavy §3]

34. [CITATION-NEEDED: Artisans Asylum Boston — confirm absence of dedicated F-2 forge studio tenancy option; confirm current membership tiers from artisansasylum.com.] [type-a-heavy §2]

35. [CITATION-NEEDED: Legal treatment of multi-tenant commissary license suspension — administrative law; California, New York, Texas preferred.] [type-b-light §4]

36. [CITATION-NEEDED: WeWork or comparable shared-office/creative-space monthly rates for 150–200 sq ft private studios — published rate data; 2022–2024 US suburban markets.] [type-b-light §5]

37. [CITATION-NEEDED: Handweavers Guild of America membership or equivalent national fiber arts practitioner count — organizational membership data or market survey.] [type-b-light §5]
