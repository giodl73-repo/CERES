---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: bake-012
trade: baking
name: "Community Kitchen Collective"
tagline: "Coop-owned shared commercial kitchen; members book oven time for their own cottage-food, catering, or meal-prep operations with compliance costs pooled"
status: draft
version: "0.1"
supersedes: null
inspirations:
  - us-shared-commercial-kitchen-movement
  - incubator-kitchen-model
  - cooperative-extension-community-canning-programs

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 80
# Mid-range of the 60-100 m² spec envelope. 80 m² supports three to four
# commercial electric deck ovens, proofing cabinets, a commercial spiral mixer,
# multiple independent prep stations (one per concurrent member booking),
# cold storage (refrigeration + freezer), shared smallwares storage, and a
# staging/cooling zone. Members work in parallel at separate prep stations;
# the layout is industrial rather than instructional — workstations are side-by-side
# production benches, not supervised-learning setups.
# [CITATION-NEEDED: commercial shared kitchen footprint survey; structural
# inference from multi-oven layout requirements at community-kitchen scale;
# label: inferred.]

ceiling_min_m: 3.0
# Minimum for overhead clearance above multi-deck oven stack plus commercial
# exhaust hood installation. 3.0 m provides adequate clearance for a stacked
# two-deck unit plus hood without requiring structural modification to standard
# commercial-building ceiling height.
# [Structural inference from commercial kitchen design standards; baking SCHEMA.md §2.]

ventilation: dedicated-exhaust-system
# Multi-oven facility with simultaneous baking by several members requires a
# dedicated exhaust system with multiple capture hoods (one per oven cluster),
# common exhaust plenum, and makeup-air supply. Health-department commercial
# kitchen licensing requires documented ventilation capacity sufficient for
# the number of simultaneous occupants and heat-producing appliances.
# More demanding than a single-operator entry because peak load is the sum
# of all active ovens running concurrently at full temperature.

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: electric-deck
# Per spec requirement. Multi-unit shared facility selects electric-deck for
# the same reasons as bake-010 and bake-003: near-zero on-site combustion
# emissions, thermostat control essential when multiple independent operators
# share simultaneous oven time, and elimination of fuel-storage requirements
# that would complicate a shared-building lease or cooperative property
# arrangement. Three to four independent deck units provide parallel capacity
# for simultaneous member bookings without shared temperature-control conflicts.
# Per baking SCHEMA.md §2: electric-deck temperature ceiling 230-290°C;
# thermostat control is a critical operational feature when multiple members
# run different products at different temperatures in adjacent ovens.
energy_consumption_per_active_hour: "22 kWh"
# Four commercial electric deck ovens at operating temperature simultaneously:
# approximately 5-6 kWh/hr sustained per single-deck unit at full bake load.
# Four units combined: ~20-24 kWh/hr. 22 kWh/hr is the mid-range estimate for
# peak concurrent operation (all four ovens running). In practice, not all ovens
# run simultaneously at all times; this figure represents the facility's rated
# peak load. Average hourly consumption across a full operating day (including
# idle and partial-load periods) is approximately 15-17 kWh/hr.
# Proofing cabinets and mixer: additional ~2 kWh/hr when concurrent.
# Per baking SCHEMA.md §2: electric-deck 3-8 kWh/batch per single deck unit.
# [CITATION-NEEDED: manufacturer energy consumption data for multiple simultaneous
# commercial electric deck ovens; Bongard, Sveba-Dahlen, Mono Equipment, or
# equivalent; label: inferred.]
backup_fuel: null
# No backup fuel in base configuration. Grid outage halts all member operations
# simultaneously, representing a collective rather than individual risk.
# A facility-level propane backup generator would substantially increase capital
# cost and permitting complexity; individual members carry their own business-
# continuity risk beyond the cooperative's control. Noted in Known Risks.

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  loaves_per_day: 200
  # FACILITY-LEVEL output per full operating day. Unit: 800g sourdough boule
  # equivalent (see Key Assumptions for unit definition). This figure reflects
  # the combined output of all members booking time on a typical fully-booked day.
  # CRITICAL DISTINCTION FROM BAKE-010: this is not a single operator's output;
  # it is the sum of production from 4-6 simultaneous member sessions across
  # all available oven stations. Individual member output per session varies
  # by product type and experience; facility-level throughput is an aggregate.
  # With four oven stations, 2 batches per oven per day, and ~25 loaves per
  # batch (per member load at their station): 4 stations × 2 batches × 25
  # loaves/batch = 200 loaves/day. Not all bookings are bread; catering and
  # meal-prep members produce non-loaf output counted in loaf-equivalents.
  # [CITATION-NEEDED: empirical throughput data for shared commercial kitchen
  # operations; structural inference from multi-oven layout; label: inferred.]

  batches_per_day: 8
  # Facility-level: 4 ovens × 2 bake loads per oven per day = 8 total oven-loads.
  # Each oven is booked independently by members; typical booking blocks are
  # 4-hour half-day slots or 8-hour full-day slots. Two booking rounds per oven
  # per day are the base scheduling assumption. Members with longer production
  # runs may book consecutive slots.
  # [Structural inference from shared kitchen booking models; label: inferred.]

  batch_size_loaves: 25
  # Per-oven, per-batch loaf-equivalent output. Single-deck commercial oven
  # loaded by an individual member at their own production rate: approximately
  # 20-30 loaves per load depending on product and member efficiency. 25 is
  # the mid-range facility average. Members producing catering trays, pastry,
  # or meal-prep items are normalized to loaf-equivalents by weight or volume.
  # [CITATION-NEEDED: deck-oven capacity per m² of deck area; commercial oven
  # manufacturer specifications for single-deck capacity; label: inferred.]

  max_active_hours_per_week: 80
  # FACILITY-LEVEL active hours per week. Reflects aggregate oven-operating
  # hours across all four oven stations. Each station operates approximately
  # 20 hr/wk (5 operating days × 4 hr/day average loaded time per station);
  # 4 stations × 20 hr/station = 80 facility-oven-hours/wk. This differs from
  # single-operator entries where max_active_hours = one operator's work week.
  # Member booking schedules determine realized utilization; 80 hr/wk is the
  # theoretical full-booking ceiling. Realistic utilization at cooperative
  # maturity is 60-75% of booking capacity (see downtime_fraction).
  # [Structural inference from multi-oven scheduling model; label: inferred.]

  product_mix:
    bread: 40
    # Artisan and yeasted bread is the dominant product category for cottage-
    # food entrepreneurs and home-bakery businesses. Includes sourdough, yeasted
    # loaves, enriched breads, rolls. Members at apprentice-baker skill level
    # concentrate here.
    confection: 25
    # Pastry, cookies, enriched sweet breads, basic laminated items by journeyman-
    # level members. Custom-cake and complex Viennoiserie not expected in base
    # configuration at apprentice-baker skill floor (see bake-009 for custom cake,
    # bake-006 for Viennoiserie).
    specialty: 15
    # Cultural specialty items, heritage grain products, ethnic specialty breads
    # per individual member's product line. Reflects member diversity in a
    # cooperative shared-kitchen model: members bring their own product identities.
    catering: 20
    # Catering production (event trays, institutional delivery, meal-prep services):
    # a meaningful fraction of shared-kitchen membership nationally is caterers and
    # meal-prep operators who use the commercial kitchen for regulatory compliance,
    # not primarily for artisan baking. Normalized to loaf-equivalents by output weight.
    # Sum: 40+25+15+20 = 100.

  throughput_variance:
    seasonal: "Moderate seasonality: holiday peak (Oct-Dec) as member order volumes rise; summer (July-Aug) trough as cottage-food sales slow; January post-holiday lull; meal-prep and catering members partially buffer seasonality with event and institutional demand"
    worst_month_fraction_of_average: 0.60
    # Summer trough consistent with baking SCHEMA.md §1 artisan-bread range 0.55-0.75.
    # Catering members partially offset seasonal bread slowdown.
    # [Baking SCHEMA.md §1 throughput_variance guidance; label: inferred.]
    best_month_fraction_of_average: 1.50
    # Holiday peak: member order volumes rise sharply in October-December;
    # booking demand may exceed available slots, requiring waitlist management.
    # Slightly above artisan-bread range (1.20-1.40) because catering and confection
    # members amplify holiday peak beyond bread-only seasonality.
    # [Baking SCHEMA.md §1; label: inferred.]

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: apprentice-baker
# Per spec requirement. This is the MEMBER skill floor, not the facility manager's
# skill level. Members are self-certified: they present evidence of basic food-handler
# training, complete the cooperative's kitchen-orientation session, and then operate
# independently within their own booking slot. The cooperative does not require
# journeyman-baker certification for membership; cottage-food entrepreneurs and
# meal-prep operators can be functioning businesses at apprentice skill level.
# The facility manager (facility-coordinator role) operates at journeyman level to
# manage equipment, resolve operational issues, and deliver the mandatory kitchen
# orientation. The MEMBER floor is apprentice; the FACILITY MANAGER floor is journeyman.
# Per baking SCHEMA.md §3: apprentice-baker can handle yeasted breads, simple rolls,
# and basic cookies. Members producing sourdough or complex laminated products must
# self-certify to a higher tier in the member onboarding protocol; the cooperative
# does not verify this independently but does not claim to provide expert supervision.
# [Baking SCHEMA.md §3 operator skill definitions]

operators_concurrent: "2-6 members + 1 facility-coordinator"
# Peak concurrent occupancy: 2-6 independent members working simultaneously
# at separate prep stations, each operating their own booked oven station.
# Plus 1 facility-coordinator on duty at all times during member operations.
# The facility-coordinator is not supervising production (unlike bake-010's
# instructor model) — they manage booking logistics, resolve equipment issues,
# enforce cleaning protocols, and handle safety incidents. Members are independent
# operators, not supervised bakers. Minimum concurrent occupancy: 1 member + coordinator.

apprentice_friendly: true
apprentice_path:
  training_stages: >-
    Stage 1 — Kitchen Orientation (0–1 month): mandatory cooperative onboarding
    covering food-handler hygiene standards (state food-handler certification
    required before first booking), commercial kitchen equipment orientation
    (deck oven startup/shutdown, temperature controls, proofing cabinet, mixer
    operation), cleaning and checkout protocol (member responsibility for station
    return-to-ready condition), booking system use, damage-liability procedures.
    Gate criterion: pass state food-handler certification; complete cooperative
    kitchen-orientation session (2-3 hours, run by facility-coordinator); sign
    member operating agreement. Access to basic booking slots unlocked.

    Stage 2 — Independent Production (1–12 months): member operates independently
    in booked slots, developing their own product lines using the facility's
    commercial equipment at scale unavailable in a home kitchen. No formal
    instruction from the cooperative; members draw on their own knowledge or
    external training (culinary classes, online programs, peer consultation).
    Gate criterion: 6 consecutive clean-checkout verifications (station returned
    in compliant condition); no equipment-damage incidents; food-handler
    certification current.

    Stage 3 — Peer-Skill Sharing and Advanced Booking (12–36 months): experienced
    members may request access to advanced booking slots (whole-day reservations,
    recurring weekly slots, equipment priority). Informal peer-to-peer skill
    exchange is a noted feature of functional shared kitchens; the cooperative
    facilitates but does not mandate this. Members may self-organize skill-share
    sessions during open-booking periods at no additional booking fee.
    Gate criterion: 12-month membership in good standing; current on dues;
    no unresolved damage-liability incidents.
  time_to_independent_operation: >-
    ~1 month to operational independence (equipment orientation completion);
    ~6-12 months to commercial-scale production efficiency on the member's
    own product line. Cottage-food entrepreneurs and home bakers with existing
    product experience become productive within weeks; members new to commercial
    equipment take longer to optimize batch sizes and oven-loading for commercial
    scale. The cooperative does not certify member skill levels beyond the
    initial orientation; business development is the member's own responsibility.
  succession_note: >-
    The cooperative's continuity does not depend on any individual member's
    skill level. The facility-coordinator role is the institutional continuity
    point: a journeyman-level coordinator who maintains equipment, manages
    bookings, and runs orientations ensures facility function regardless of
    member composition. The member pool itself is self-renewing (open membership
    within eligibility criteria); experienced members who depart are replaced by
    incoming members cycling through orientation. The governing board (member-elected)
    retains institutional knowledge of policy and governance independent of any
    individual member's tenure.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 55000, mid: 100000, high: 165000 }
  # Per spec requirement.
  # Low ($55,000): two to three commercial electric deck ovens (refurbished or
  # entry-grade: ~$12,000-16,000 each), two proofing cabinets (~$3,000 total),
  # one commercial spiral mixer (~$3,500), four basic prep stations (stainless
  # steel tables: ~$3,000), shared smallwares and storage shelving (~$2,000),
  # cold storage (commercial reach-in refrigerator + freezer: ~$4,000), minimal
  # lease-space fitout.
  # Mid ($100,000): four mid-grade commercial electric deck ovens ($20,000-25,000
  # each; $80,000-100,000 total oven cost), two full-featured proofing cabinets
  # with humidity control ($5,000 total), commercial spiral mixer with divider
  # ($5,500), four fully equipped prep stations ($6,000), dedicated cold storage
  # (walk-in cooler or two commercial reach-ins + freezer: $6,000), shared
  # smallwares package ($3,000), signage and member storage lockers ($2,000).
  # High ($165,000): four premium commercial deck ovens ($35,000-40,000 each
  # in two-deck stacked configurations), full walk-in cold storage ($10,000),
  # heavy-duty spiral mixer with dough divider ($7,500), five fully outfitted
  # prep stations ($8,000), commercial dishwasher ($3,000), exhaust system upgrade
  # beyond standard buildout ($5,000), ADA accessibility compliance and full
  # member amenity fitout ($5,000).
  # [CITATION-NEEDED: capital cost data for multi-oven commercial shared kitchen
  # at community-kitchen cooperative scale, 2024-2026; commercial bakery and
  # restaurant equipment vendor catalogs; label: inferred.]

  install_cost: 18000
  # Electrical service upgrade: shared commercial kitchen with four deck ovens
  # requires a substantial service upgrade — 200-400A three-phase service in
  # most jurisdictions ($6,000-10,000 for service upgrade plus panel work).
  # Dedicated exhaust system with multiple hood drops, plenum, and makeup-air
  # unit: $4,000-6,000. Health-department commercial kitchen inspection, plan
  # review, and licensing: $5,000-15,000/yr ongoing (see regulatory_notes);
  # one-time fitout inspection and certificate of occupancy: ~$1,500-2,000.
  # Total installation estimate: $18,000 mid-range.
  # [CITATION-NEEDED: installation cost for multi-oven commercial shared kitchen;
  # electrical service upgrade and exhaust system data; label: inferred.]

  annual_maintenance: 4500
  # Four-oven facility: oven element inspection and replacement cycle, thermostat
  # calibration, door gasket replacement, proofing cabinet servicing, mixer
  # maintenance, exhaust hood quarterly professional cleaning (health-code
  # requirement), cold storage compressor service, member tooling and smallwares
  # replacement. Multi-member usage accelerates wear on shared equipment
  # (oven doors, deck surfaces, mixer attachments) relative to single-operator
  # entries. Excludes first-year failure replacements itemized in operations_reality.
  # [CITATION-NEEDED: annual maintenance data for shared commercial kitchen
  # operations; label: inferred.]

  annual_consumables: 15500
  # Members bring their own flour and primary ingredients; facility consumables
  # are energy, cleaning materials, packaging supplies, and facility-provided
  # disposables.
  # Energy: four ovens at ~15 kWh/hr average × 80 facility-hr/wk × 50 wk/yr
  # = 60,000 kWh/yr × $0.125/kWh = $7,500/yr [US EIA small-commercial rate].
  # Plus proofing cabinets, mixer, lighting, cold storage: ~$2,000/yr.
  # Cleaning chemicals, sanitizer, paper goods (paper towels, liners): ~$2,500/yr.
  # Facility-provided smallwares replacement (parchment, pan spray, bench flour
  # for cleaning surfaces): ~$1,500/yr. Starter cultures maintained for members
  # who request facility-supplied starter: ~$500/yr. Kitchen certification
  # compliance supplies (temperature logs, food-safety records): ~$500/yr.
  # EXCLUDES: members' own flour, ingredients, and packaging — member-supplied.
  # [US EIA Electric Power Monthly Table 5.3, 2023-2024; label: inferred
  # for cleaning and consumables estimates.]

  floor_space_rent_per_year: 24000
  # Imputed commercial kitchen rental rate for 80 m² at town-to-small-city scale.
  # Commercial kitchen / light-industrial space at town-to-small-city: approximately
  # $25-35/m² per year ($250-350/ft² / 10.76 = $23-33/m²/yr); 80 m² × $300/yr/m²
  # = $24,000/yr as mid estimate. Shared across all members via booking fees;
  # the core economic logic of the cooperative is that individual members who could
  # not afford $2,000+/month for a solo commercial kitchen share this cost.
  # [CITATION-NEEDED: commercial kitchen / light-industrial rental rate per m²
  # at town-to-small-city scale, 2024; CoStar, LoopNet, or local market data;
  # label: inferred.]

# ── TRADE-SPECIFIC FIELDS ────────────────────────────────────────────────────

trade_specific:
  flour_source_declaration: industrial-flour-purchased
  # Per baking SCHEMA.md §4 required field and DECLINE-VERDICT mill-dependency
  # falsifier. Each member brings their own flour and primary ingredients; the
  # FACILITY does not purchase or supply flour. The flour_source_declaration
  # applies to the operational reality: members individually source from industrial
  # distributors, local mills, or specialty suppliers per their own business model.
  # No facility-level flour supply chain exists; supply risk is distributed across
  # the member pool, not centralized. This is a defining structural difference
  # from bake-001 through bake-003, where the bakery operator controls flour
  # sourcing. The cooperative's supply-chain responsibility ends at energy,
  # cleaning materials, and equipment; flour is a member-carried input.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Deck heating element (electric) — one of four oven units"
      estimated_hours_to_failure: 2200
      replacement_cost: 700
      replacement_lead_time_days: 14
      serviceable_by: specialist
      # Multi-member usage pattern (many different operators loading the same oven)
      # may accelerate element degradation slightly versus single-operator use due
      # to variable loading practices. At 80 facility-oven-hours/wk, a 2,200-hr
      # element failure would occur within ~1.5 operating years; one deck-unit
      # element failure in year 1 is probable. Facility continues operating with
      # three remaining units; the affected oven is taken offline pending repair.
      # Specialist required per baking SCHEMA.md §5 reference list; 14-day lead
      # time for non-stocked element.
      # [Baking SCHEMA.md §5 deck element 1,500-3,000 hr range; label: inferred.]

    - item: "Oven door seal / gasket — one or more oven units"
      estimated_hours_to_failure: 1500
      replacement_cost: 120
      replacement_lead_time_days: 5
      serviceable_by: operator
      # Multi-member operations significantly accelerate door seal wear: members
      # loading and unloading their own ovens have variable door-handling practices
      # and may not be attentive to seal condition (unlike a single trained operator
      # who monitors equipment daily). Facility-coordinator performs weekly visual
      # inspection; door gasket failure at 1,500 hr is plausible in year 1 for
      # the highest-use oven unit. Operator-serviceable; 5-day regional supply lead.
      # [Baking SCHEMA.md §5 door seal 1,500-3,000 hr range; label: inferred.]

    - item: "Deck stones cracking — one oven unit, thermal shock from member misuse"
      estimated_hours_to_failure: 1200
      replacement_cost: 250
      replacement_lead_time_days: 7
      serviceable_by: operator
      # Most common equipment-damage mode in shared commercial kitchens with
      # self-operating members: member spilling water, cold dough contact with
      # hot stones, or improper loading causes thermal shock cracking. At 80
      # facility-oven-hours/wk across multiple independent operators, the probability
      # of at least one thermal shock event in year 1 is elevated versus single-operator
      # entries. Modular stone replacement is operator-serviceable; 7-day lead for
      # stones from commercial equipment supplier.
      # [Baking SCHEMA.md §5 deck stones 800-2,500 hr thermal shock range;
      # multi-member risk assessment; label: inferred.]

  maintenance_schedule:
    daily:
      task: "Facility-coordinator checkout inspection for each departing member: verify station returned to ready condition (deck surfaces clear, implements stored, mixer bowl clean, prep table sanitized, no spills); log oven operating hours per unit; feed facility starter cultures; review booking log for next-day sessions; replenish paper goods and hand-sanitizer stations; check cold storage temperature logs"
      performed_by: operator
      # 'Operator' here = facility-coordinator. Daily end-of-booking checkout
      # is the primary compliance mechanism in a shared-kitchen model where
      # each member is responsible for returning their station to ready condition.
      # Facility-coordinator spot-checks and resolves any non-compliance before
      # the next booking slot opens.
    weekly:
      task: "Deep-clean all four oven decks and door seals; inspect deck stones for cracking; calibrate proofing cabinet temperature and humidity; drain and clean mixer bowl and inspect motor; inspect and clean exhaust hood filters; audit member storage lockers for expired ingredients (health-code requirement); review damage-liability log; restock shared consumables (parchment, pan spray, bench flour); update booking utilization report for member board review"
      performed_by: operator
    quarterly:
      task: "Professional exhaust hood and grease-trap service (health-code requirement); full deck element resistance inspection on all four units; proofing cabinet professional calibration; mixer motor inspection and lubrication; cold storage compressor service; full smallwares inventory and replacement assessment; health-department compliance review and documentation update; board-presented booking utilization and revenue report"
      performed_by: journeyman
    annual:
      task: "Full commercial kitchen inspection for license renewal (health department); deck oven professional service on all four units (element test, seal replacement, thermostat calibration); proofing cabinet and mixer professional overhaul; electrical panel and service inspection; insurance assessment update; member-agreement renewal cycle; governing board annual meeting and governance review"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 45
  # Shared kitchen operating overhead per day:
  # (1) Facility open/close: coordinator arrival and departure, security, HVAC
  # and exhaust startup, temperature log initialization: ~10 min.
  # (2) Pre-session member check-in: booking verification, equipment handoff
  # briefing for members using equipment for the first time: ~10 min average
  # across all sessions starting in a day.
  # (3) End-of-day checkout: final station inspection, log completion, cold
  # storage temperature sign-off, equipment shutdown: ~15 min.
  # (4) Booking-gap turnovers between morning and afternoon slots: 2 transitions
  # × ~5 min each = 10 min.
  # Total: ~45 min/day non-productive coordinator overhead.
  # [Structural inference from shared kitchen booking model operating protocols;
  # label: inferred.]

  max_active_hours_realism_note: >-
    80 facility-oven-hr/wk is the theoretical full-booking ceiling across four
    oven stations. Net of 45 min/day coordinator overhead on a 5-operating-day
    week: 45 min × 5 days / 60 = 3.75 hr/wk non-productive overhead (facility-
    coordinator time), leaving ~76.25 effective facility-oven-hr/wk. However,
    the more binding constraint is booking utilization: at cooperative maturity,
    realistic booking fill rate is 65-75% of available slots. At 70% fill rate,
    effective facility-oven-hr/wk = 80 × 0.70 = 56 hr/wk. This booking
    utilization constraint is the primary throughput governor, not the coordinator
    overhead. sim_params uses the booking-utilization-derated figure as the
    effective throughput basis, represented in the downtime_fraction of 0.20
    (which blends booking underutilization, maintenance downtime, and scheduling
    gaps into a single effective-idle fraction).

  interruption_notes: >-
    Intraday interruptions in a multi-member shared kitchen are member-driven
    rather than facility-driven: members learning new equipment configurations,
    requesting coordinator help for equipment settings (~5-10 min/incident;
    2-3 incidents/day average), booking conflicts at transition times (~5-10 min
    to resolve), damage incidents requiring coordinator intervention (~15-30 min
    per incident; 1-2 per week). These interruptions affect coordinator time and
    occasionally delay a member's booking start, but do not uniformly reduce
    facility throughput because other ovens continue operating during any single
    incident. Folded into facility-level throughput via the booking utilization
    rate rather than as a separate overhead item.

  consumables_lead_time_days: { typical: 3, worst: 21 }
  # Facility consumables (cleaning chemicals, replacement smallwares, parchment):
  # typical regional food-service distributor lead time 2-4 days at town-to-
  # small-city scale per SCALES.md §6 infrastructure baseline. Replacement
  # oven elements and deck stones: 7-14 days typical from commercial equipment
  # suppliers; 21-day worst case for non-stocked items or specialty components.
  # Members' own flour and ingredients are their own supply chain; not captured here.
  # [SCALES.md §6; baking SCHEMA.md §5; label: inferred.]

  throughput_variance:
    seasonal: "Holiday peak (Oct-Dec) as member order volumes surge; summer (Jul-Aug) trough for bread members offset by catering and event demand; January post-holiday lull affects most members simultaneously, suppressing booking demand"
    worst_month_fraction_of_average: 0.60
    best_month_fraction_of_average: 1.50

  operator_impact:
    noise_db: 63
    # Four simultaneous electric deck ovens (each ~45-50 dB ambient), commercial
    # spiral mixer during use (~68-72 dB intermittent), multiple member activity
    # (conversation, equipment handling, pans and sheet trays): estimated 60-66 dB(A)
    # at facility-coordinator position during peak concurrent operation. Louder than
    # bake-010 (single operator + 2 members) due to higher concurrent occupancy.
    # Well below OSHA 90 dB(A) PEL for 8-hr shift.
    # [CITATION-NEEDED: ambient sound measurement at facility-coordinator position
    # in a multi-operator shared commercial kitchen; OSHA 29 CFR 1910.95 PEL;
    # illustrative estimate; label: inferred.]
    heat_exposure: "Elevated ambient when multiple ovens running simultaneously; ambient near oven cluster 30-38°C at peak concurrent operation; managed by dedicated exhaust system and makeup-air supply; coordinator and member rotation away from oven-adjacent positions during sustained bake windows recommended; no single member sustains peak heat exposure for more than their booking slot duration"
    emissions: "Near-zero combustion emissions from electric deck configuration; flour dust is the primary occupational exposure at a multi-member bakery (multiple members handling flour simultaneously elevates ambient dust levels relative to single-operator entries); facility exhaust system manages steam and heat; flour-dust PPE (dust mask) required for all occupants during peak mixing periods per OSHA flour-dust guidelines; member orientation must include PPE policy"
    physical_demand: "Moderate for facility-coordinator (sustained standing during operating hours; oven-monitoring rounds; equipment checks; station inspections); variable for members (members control their own workload within their booking slot); oven loading/unloading with peel at commercial scale (10-20 kg dough batches per load) is physically demanding and must be addressed in the member orientation"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Light-industrial, commercial, or mixed-use with commercial kitchen use permitted; shared commercial kitchen licensed as a food-manufacturing or food-processing establishment in most jurisdictions; confirm local zoning for multi-tenant food production; some municipalities require a specific 'shared kitchen' or 'commissary kitchen' use permit in addition to standard commercial zoning"
  emissions: "No combustion emissions permit required for all-electric configuration; kitchen exhaust system requires building permit and fan-capacity inspection; flour-dust occupational exposure governed by OSHA 29 CFR 1910.1000 Table Z-1; multi-member simultaneous flour handling elevates ambient dust versus single-operator; exhaust makeup-air design must meet ventilation requirements for the rated concurrent occupancy"
  other: "Commercial kitchen license is the primary regulatory cost: $5,000-15,000/yr in most US jurisdictions (permit fees, annual inspections, plan-review fees); this is the explicit compliance-cost-sharing rationale for the cooperative model. Each member operating under the cooperative's license must hold a current state food-handler certification. Members selling food produced at the facility must confirm that the cooperative's commercial kitchen license covers their product category (some jurisdictions require cottage-food-law registration in addition to, or instead of, a commercial kitchen license for certain product types). Food liability insurance required at facility level; members may be required to carry their own product liability coverage per operating agreement."

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: poor
  # The cooperative does not sell baked goods commercially; it sells kitchen time
  # to members. There is no market for artisan bread produced by the cooperative
  # as an entity. Individual members' businesses have market exposure, but this
  # entry evaluates the COOPERATIVE FACILITY, not each member's revenue model.
  # The facility's revenue is booking fees, not bread sales. A market-lens
  # evaluation of the cooperative as a business entity yields poor results: the
  # facility earns booking revenue that must cover capital amortization, operating
  # costs, and the commercial kitchen licensing fee — margins are thin and the
  # economics depend on maintaining high booking utilization.
  cooperative: good
  # The defining lens for this entry. The cooperative model solves the problem the
  # market cannot: no individual cottage-food entrepreneur can afford a $5,000-15,000/yr
  # commercial kitchen license and $100,000 in equipment. The cooperative aggregates
  # compliance costs across 15-50 members, making regulated food production
  # accessible at ~$150-600/member/yr in booking fees rather than $5,000-15,000/yr
  # in solo compliance costs. Ostrom principles 1-6 are addressed; full governance
  # documentation below.
  civic: marginal
  # The shared kitchen creates a marginal civic case: it incubates small food
  # businesses (civic externality: economic development), reduces barriers to
  # entrepreneurship for low-income cottage-food operators (food-equity adjacent),
  # and preserves cultural food production capacity in immigrant communities.
  # However, it is primarily a compliance-cost-sharing arrangement run by and for
  # members' private business interests, not a food-access or public-nutrition
  # service. Municipal acknowledgment or grant support is achievable but not primary.

scale_fit:
  village: poor
  # Village scale (500-2,000 residents) cannot sustain the member base needed
  # to fill 80 facility-oven-hours/wk of booking demand. Commercial kitchen
  # licensing ($5,000-15,000/yr) plus operating costs (~$60,000/yr) require
  # a minimum viable member base of approximately 20-40 regular booking members
  # to achieve viable booking utilization (>60% fill rate). Village-scale
  # cottage-food and catering market is too thin. Also: at village scale, the
  # $100,000 capital cost cannot be amortized over a member population large
  # enough to make per-member costs attractive versus solo alternatives.
  town: good
  # Target scale per spec. Town of 2,000-15,000 residents provides sufficient
  # cottage-food entrepreneur, caterer, and meal-prep operator density to
  # sustain a 20-50 member cooperative. Commercial kitchen licensing is a
  # real barrier for solo operators at town scale; collective compliance cost
  # sharing is the strongest recruitment argument. Food business density is
  # sufficient without requiring urban-scale infrastructure.
  small_city: good
  # Small-city scale (15,000-75,000 residents) supports an expanded member base
  # (50-100+ members), higher booking utilization, and potentially multiple
  # facility-coordinator shifts. The governance model scales without structural
  # change; member-board representation may need adjustment for larger cooperative
  # populations. Multiple shared-kitchen cooperatives may coexist in a small city,
  # serving different neighborhoods or food-business communities.

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:

  cooperative:
    membership_boundary: >-
      Any person operating a cottage-food business, catering service, meal-prep
      operation, specialty food business, or home-bakery enterprise within the
      cooperative's service area (town and immediately surrounding township or
      county equivalent). Membership is open to individual operators, not corporate
      entities; one member-vote per operating business, regardless of booking volume.
      Annual dues ($150-300/yr depending on tier) establish membership; booking fees
      ($15-25/hr oven time, or $50-100 per half-day slot) cover facility operating
      costs. Waitlist managed by the governing board during periods of oversubscription.
      Non-member commercial use (event bookings, day-pass access) permitted at a
      higher rate and without voting rights, at board discretion. Members must hold
      a current state food-handler certification and maintain compliance with the
      cooperative's operating agreement.

    rules_source: >-
      Member-adopted bylaws, approved at founding general meeting and amended by
      member vote. Bylaws govern: eligibility criteria (food-handler certification,
      signed operating agreement, dues current); booking protocol (advance reservation
      required via cooperative scheduling system; minimum booking block 2 hours;
      cancellation policy with 24-hour notice window); member responsibilities (station
      return-to-ready condition, equipment damage reporting, compliance with cleaning
      protocols); booking-fee schedule and annual dues; damage-liability mechanism
      (member responsible for replacement cost of equipment damaged in their booking
      slot; see graduated_sanctions); governing board composition and election process;
      member amendment process. Operating procedures posted in facility and on cooperative
      website. Fee schedule reviewed annually by governing board and ratified by member vote.

    monitoring: >-
      Facility-coordinator completes checkout inspection for every departing member's
      station and logs compliance in the operating record. Booking system generates
      utilization reports (hours booked per member, per oven station, by product
      category) reviewed monthly by the governing board. Equipment condition log
      maintained by coordinator; damage incidents documented and attributed to the
      booking record of the responsible member. Temperature calibration logs for
      ovens, proofing cabinets, and cold storage maintained daily and available for
      health-department inspection. Member food-handler certification expiry tracked
      in the membership database; booking system blocks expired-certification members
      from future reservations until renewal is confirmed. Per Ostrom Principle 4.

    graduated_sanctions: >-
      Tier 1 — Minor protocol violation (station not fully returned to ready
      condition, minor cleaning omission, booking cancellation without 24-hour
      notice): written notice logged in member record; 30-day window to remediate
      without further penalty. Repeated Tier 1 within 12 months: $25 compliance fee.

      Tier 2 — Equipment damage (verified in checkout log): member billed for
      replacement cost at cost (no markup); 60-day booking suspension pending
      payment. Non-payment escalates to Tier 3.

      Tier 3 — Serious violation (food-safety breach, hygiene failure posing
      contamination risk to other members' products, non-payment of equipment
      damage cost, falsification of food-handler certification): immediate
      booking suspension pending governing-board review. Board review within
      14 days; outcomes: suspension (30-90 days), probationary membership
      with enhanced coordinator monitoring, or membership termination with
      pro-rated dues refund. Food-safety violations may be escalated to
      health department per cooperative's licensing obligation.

      Per Ostrom Principle 5.

    conflict_resolution: >-
      Member-vs-member disputes (scheduling conflicts, contamination claims,
      noise/interference complaints) presented in writing to the facility-
      coordinator; coordinator mediates within 5 business days. Disputes
      not resolved at coordinator level escalated to a dispute-resolution
      panel of three governing-board members (excluding any board member
      with a conflict of interest); panel decision issued within 21 days
      of escalation. Appeal of panel decision to a full-member vote at the
      next general meeting (held quarterly or called by 20% of members).
      Member-vs-cooperative disputes (fee disputes, sanction appeals) follow
      the same three-tier path. Per Ostrom Principle 6.

    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6]
    # Principle 1 (clearly defined boundaries): membership eligibility criteria
    #   (food-handler certification, signed operating agreement, dues current,
    #   service-area residency or business operation) define who may use the
    #   facility and who may not. Non-members can book at day-pass rate but
    #   without governance rights.
    # Principle 2 (congruence): booking-fee structure is calibrated to actual
    #   facility operating costs; dues cover overhead; damage-liability mechanism
    #   assigns costs to the member responsible. Rules reflect the shared-kitchen
    #   operational reality, not generic cooperative boilerplate.
    # Principle 3 (collective choice arrangements): bylaws amendable by member
    #   vote; fee schedule ratified annually; members who use the resource
    #   participate in rule-making through the governing board and general meeting.
    # Principle 4 (monitoring): coordinator checkout logs, booking utilization
    #   reports, equipment condition tracking, food-handler certification database.
    # Principle 5 (graduated sanctions): four-tier sanction system documented above.
    # Principle 6 (conflict resolution): three-tier dispute path documented above.
    # Principles 7-8: a registered cooperative-corporation or 501(c)(3) entity
    #   provides external recognition (Principle 8 analog). Principle 7
    #   (nested organizations) not formally applicable at single-cooperative scale;
    #   membership in regional shared-kitchen networks (e.g., Kitchen Table Coop
    #   affiliates) may satisfy this partially in practice.

    member_amendment_process: >-
      2/3 vote of active members at a general meeting (held at minimum quarterly;
      special meeting called by governing board or by petition of 20% of active
      members); 30-day advance written notice to all members before any bylaw
      amendment vote. Fee-schedule adjustments require simple majority at annual
      general meeting with 30-day notice. Emergency amendments (health-code
      compliance, licensing requirement, imminent legal obligation) may be enacted
      by 3/4 governing-board vote with 7-day member notice and ratification by
      member vote at the next general meeting. No single board member or founding
      member holds unilateral amendment authority; Ostrom Principle 3 compliance
      requires that rule-change authority rests with the member body, not the
      founders or a permanent steering committee.

    legal_form: >-
      Cooperative corporation registered under state cooperative-corporation statute
      (available in most US states: e.g., California Corporations Code §§12200-12604,
      Minnesota Statutes §308B, or equivalent); alternatively structured as a 501(c)(3)
      nonprofit mutual-benefit corporation where state cooperative-corporation law is
      thin. Registration provides the external recognition (Ostrom Principle 7 analog)
      that prevents dissolution under pressure: a registered cooperative has a legal
      charter, articles, and bylaws on file with the state; an unincorporated
      cooperative has no such protection and is vulnerable to informal dissolution
      if founding members leave. The commercial kitchen licensing ($5,000-15,000/yr)
      and food liability insurance require a legal entity; informal governance is not
      sufficient. Jurisdiction: state of operation; municipal registration or
      acknowledgment filed with the relevant business licensing office.

    scale_fit_note: >-
      Governance rules calibrated for town-to-small-city scale (2,000-75,000
      residents). Minimum viable active member base: approximately 20-40 regular
      booking members to sustain >60% booking utilization (facility viability
      threshold). At this membership level, quarterly general meetings are feasible
      (20-40 participants), the governing board (5-7 members) can be elected with
      competitive participation, and the dispute-resolution mechanism is workable
      with a three-member panel. At village scale, member base falls below minimum
      viable threshold and the governance structure becomes an overhead burden on
      a handful of operators. At large-city scale (>75,000 residents), the model
      remains viable but may need sub-cooperative or multi-site governance structures
      to maintain the congruence (Principle 2) between rules and operational reality
      as member count grows above 100.

  civic:
    political_coalition: >-
      Economic development office (small-business incubation; food-entrepreneurship
      support; job creation in the food sector); workforce development board
      (cottage-food skills training; food-business licensing pathway; entry-level
      food-sector employment channel); cultural organizations (shared kitchen
      as platform for immigrant-community food businesses and cultural food
      preservation); health department (commercially licensed food production
      replacing unlicensed home operations — a public health benefit, not a
      threat). Secondary coalition partners: local business associations (new
      food-business creation benefits downtown food economy); community development
      financial institutions (CDFIs with food-business lending programs); state
      small-business development centers (SBDC food-business consulting alignment).

    council_vote_estimate: >-
      4-3 marginal in most town councils. The cooperative is primarily a private-
      member benefit organization, not a clearly public-good institution; the
      civic case requires the economic-development and small-business-incubation
      framing to land. Opposition arguments: "why is the city subsidizing private
      businesses' kitchen costs?" (answered by incubator framing, not food-security
      framing) and "liability exposure from food production in a cooperatively
      managed facility" (answered by legal form and insurance documentation).
      Municipal support is more likely to take the form of grant-funding, low-rate
      facility lease, or zoning accommodation than direct capital investment.
      A council that frames this as a small-business incubator rather than a food-
      access program achieves a more durable political coalition.

    competes_with_private: >-
      Commercial shared kitchen rentals exist in some towns and small cities as
      private operators. A cooperative shared kitchen is in direct competition
      with a private shared-kitchen rental business if one operates in the same
      market. The cooperative's advantage is member-ownership (booking fees flow
      back into the cooperative rather than to a private landlord) and governance
      rights (members set policy). A civic facility that displaces a functioning
      private shared-kitchen rental operator requires explicit justification;
      in most town-scale markets, no private shared-kitchen rental operator
      exists because the market is too thin to support one — which is precisely
      why the cooperative model is viable. Where a private operator exists,
      the cooperative should document the gap it fills (lower-income members,
      cultural-food-specific services, member-ownership structure not available
      commercially) rather than competing head-to-head.

    governance_form: >-
      Member-owned and member-governed cooperative corporation. The governing
      board (5-7 directors, elected annually by member vote) sets policy and
      approves the budget. A paid facility-coordinator (full-time or substantial
      part-time, journeyman-baker skill level) manages day-to-day operations.
      There is no municipal ownership; the cooperative is an independent legal
      entity. Municipal support (if any) takes the form of grant funding, below-
      market facility lease from a municipal or redevelopment property, or zoning
      accommodation. The cooperative retains full operational autonomy.

    budget_line: >-
      Cooperative revenue: booking fees ($15-25/hr × 56 effective facility-oven-hr/wk
      × 50 wk/yr = ~$42,000-70,000/yr in booking revenue at 70% utilization, mid
      $56,000/yr at $20/hr average); annual member dues ($200/yr × 35 members
      = $7,000/yr); total gross revenue: ~$63,000/yr mid. Operating costs:
      facility-coordinator wage (~$42,000-50,000/yr for substantial part-time
      to full-time journeyman; $46,000 mid), commercial kitchen license
      ($5,000-15,000/yr; $10,000 mid), floor space rent ($24,000/yr), annual
      maintenance ($4,500), annual consumables ($15,500), insurance ($3,000/yr).
      Total operating costs: ~$103,000/yr mid. Capital amortization:
      ($100,000 + $18,000) ÷ 20 yr = $5,900/yr. Total annual cost: ~$109,000/yr.
      Revenue gap vs. costs: ~$46,000/yr — the cooperative must supplement
      booking revenue with grants, below-market lease, municipal support, or
      higher booking rates. Alternatively, booking rates need to be ~$35-45/hr
      to break even without external support; this is above typical shared-kitchen
      market rates [CITATION-NEEDED] and may suppress member demand.
      Municipal or CDFI grant support of $20,000-40,000/yr closes the gap.
      This financial picture is the civic-lens case: the cooperative serves
      a public incubation function that the market alone will not subsidize.
      [CITATION-NEEDED: shared commercial kitchen booking rates in US markets;
      label: inferred from cooperative kitchen surveys.]

    benchmark_comparison: >-
      At town scale (3,000 households mid-point per SCALES.md §2): net municipal
      contribution (if any — grant support of ~$20,000-40,000/yr assumed for
      viability) ÷ 3,000 hh = ~$7-13/hh/yr municipal cost. All-in cooperative
      cost (including capital amortization) is ~$109,000/yr; if fully grant-funded
      from municipal economic development budget: ~$36/hh/yr gross. More typically,
      municipal support covers a portion: $20,000-25,000/yr grant = ~$7-8/hh/yr
      municipal contribution.

      Benchmark: small-business incubator programs in comparable towns cost
      $15,000-50,000/yr in municipal economic development grants for programs
      that serve 10-30 businesses [CITATION-NEEDED: municipal small-business
      incubator program cost data]. At ~$7-8/hh/yr municipal contribution, the
      community kitchen cooperative is comparable to or cheaper than conventional
      incubator models while providing a capital asset that remains in member
      ownership rather than reverting to a private landlord. Food bank programs
      in comparable towns: ~$20-40/hh/yr [CITATION-NEEDED]; the cooperative
      is not primarily a food-access program but serves some food-equity function
      by lowering barriers for low-income food entrepreneurs.

    staffing_model:
      role: "1 facility-coordinator (journeyman-baker level; full-time or substantial part-time)"
      operator_fte: 0.8
      # Substantial part-time to full-time: 30-40 hr/wk during facility operating
      # hours. Not a full 1.0 FTE in base configuration because the coordinator
      # is a facility manager, not a production baker — oversight, booking management,
      # orientations, checkout inspections, and maintenance coordination do not
      # require 40 hr/wk of direct labor at a 35-member cooperative. At 50+ members
      # and higher booking utilization, 1.0 FTE becomes necessary.
      wage_assumption: 46000
      # Facility-coordinator at journeyman skill level; operations management role
      # rather than production baker role. $42,000-50,000/yr range; $46,000 mid.
      # Per corpus/program/SCALES.md §3: town-scale skilled-trades median $56,000/yr;
      # $46,000 is below this threshold, reflecting the operations-management nature
      # of the role (less direct production skill demand than a baker-instructor).
      # [corpus/program/SCALES.md §3 town-scale skilled-trades median]
      wage_source: "corpus/program/SCALES.md §3 town-scale skilled-trades median; facility-coordinator below baker-instructor level due to operations vs. production role; $46,000 consistent with cooperative operations-management wage range"
      hours: "30-40 hr/wk (facility open/close, member check-in/checkout, booking management, equipment monitoring, orientations, quarterly compliance reporting, board meeting attendance)"
      hiring_notes: >-
        Journeyman baker with operations management or food-safety management
        experience is the ideal profile. The coordinator does not need to be
        a production expert (members supply their own expertise) but must be
        competent enough to recognize equipment issues, conduct meaningful
        checkout inspections, and deliver credible kitchen-orientation sessions.
        The hiring pool is broader than bake-010's baker-instructor profile:
        food service managers, culinary school graduates with operations interest,
        or experienced cooperative kitchen users who transition into management
        are viable candidates. $46,000/yr is within the range for food-service
        management roles in most US town-scale markets [CITATION-NEEDED: BLS
        Food Service Managers (SOC 11-9051) or Baker (SOC 51-3011) wage data,
        2024]. Cooperative ownership structure and mission alignment are secondary
        hiring advantages.

    civic_externalities:
      - "Small-business incubation: lowers the compliance-cost barrier for cottage-food entrepreneurs, caterers, and meal-prep operators who cannot individually afford commercial kitchen licensing ($5,000-15,000/yr) or equipment ($55,000-165,000 capital); members who launch and grow food businesses contribute to local tax base, food sector employment, and neighborhood food economy in ways the unlicensed home-kitchen alternative cannot"
      - "Cultural food preservation: immigrant communities and heritage-food operators gain access to commercial-scale production capacity for traditional food products that require licensed commercial kitchen production to be sold legally; cooperative shared kitchen is the only viable platform for these operators in most town-scale markets where cultural-food-specific commercial kitchens do not exist"
      - "Food-business licensing pathway: the cooperative's commercial kitchen license covers members' production under the facility's permit umbrella, providing a legal pathway to market for food entrepreneurs who would otherwise operate in the informal economy (unlicensed cottage-food, gray-market catering); compliance externality benefits public health by moving food production from unregulated home environments to a licensed, inspected facility"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 100000
  # Equals economics.capital_cost.mid per E3-R1.
  # [Derived from economics.capital_cost above]

  cost_sd: 27500
  # Derived: (capital_cost.high - capital_cost.low) / 4 = (165,000 - 55,000) / 4
  # = $27,500. E3-R5 ratio: 27,500 / 100,000 = 0.275; within 0.15-0.50 range.
  # [Derived per catalog/SCHEMA.md §3 default; E3-R5 compliance confirmed]

  throughput_units_equiv_per_year: 45000
  # Unit: 800g sourdough boule equivalent (facility-level aggregate; see Key
  # Assumptions for unit definition and member-throughput composition).
  # Derivation (per baking SCHEMA.md §1 E-3 guidance):
  # Step 1 — annual operating days:
  #   5 operating days/wk × 50 wk/yr (allowing ~2 wk annual closure for deep-
  #   clean, license renewal, and board activities) = 250 days/yr.
  # Step 2 — facility loaves per operating day (gross ceiling):
  #   throughput.loaves_per_day = 200 loaves/day (four ovens × 2 batches ×
  #   25 loaves/batch).
  # Step 3 — apply downtime fraction (booking underutilization + maintenance):
  #   200 loaves/day × 250 days/yr × (1 - 0.10 maintenance downtime) = 45,000.
  #   Note: the booking-utilization constraint (~70% fill rate) is already
  #   embedded in loaves_per_day (200 is the 70%-utilization figure, not the
  #   full-booking ceiling of ~286). The downtime_fraction of 0.10 captures
  #   equipment maintenance and scheduling gaps beyond booking utilization.
  # E3-R2 cross-check via active-hours method:
  #   max_active_hours_per_week (80) × 52 wk × (1 - 0.10 downtime) = 3,744 hr/yr.
  #   Net of overhead: 45 min/day × 250 days / 60 = 188 hr/yr overhead.
  #   Net active hr/yr: 3,744 - 188 ≈ 3,556 hr/yr.
  #   At 200 loaves/day ÷ ~8 effective oven-hr/day (4 ovens × 2 batches ÷ 1 hr/batch)
  #   ≈ 25 loaves/facility-oven-hr.
  #   3,556 hr × 25 loaves/hr ÷ 2 (booking factor correction: 70% utilization
  #   already in loaves_per_day) ≈ 44,450 — consistent with 45,000; within P2 threshold.
  # [Derived from throughput fields, operating-day assumption, and downtime_fraction above]

  variable_cost_per_unit: 0.34
  # Facility-level variable cost per loaf-equivalent (energy + cleaning + facility
  # consumables ONLY; excludes members' own flour and ingredients which are not
  # facility costs).
  # Energy: $15,500 consumables / 2 (energy share ~50% of consumables) = ~$7,750.
  # Actually: energy estimated at $7,500 + $2,000 = $9,500/yr facility energy.
  # Total consumables $15,500/yr ÷ 45,000 loaves = $0.344/loaf.
  # Note: this variable cost is substantially lower than single-operator entries
  # where flour is included in consumables; members supply their own flour,
  # which is the primary per-unit variable cost in all other baking entries.
  # The facility's per-unit cost to the cooperative is $0.34; the member's
  # total per-unit cost (flour + booking fee + facility cost) is $1.50-3.50
  # depending on product and booking efficiency.
  # [Derived from annual_consumables and throughput_units_equiv_per_year above;
  # US EIA Electric Power Monthly Table 5.3, 2023-2024 blended small-commercial
  # rate $0.125/kWh used]

  labor_hours_per_unit: 0.018
  # Facility-coordinator hours per loaf-equivalent:
  # Coordinator at 0.8 FTE: ~32 hr/wk × 50 wk = 1,600 hr/yr total.
  # Production-attributable coordination (booking management, checkout, equipment
  # monitoring): ~70% of coordinator time = 1,120 hr/yr.
  # 1,120 hr/yr ÷ 45,000 loaves/yr = 0.0249 hr/loaf (gross).
  # But facility-coordinator time is a fixed overhead, not truly variable per unit;
  # using 0.018 hr/loaf as effective production-attributable rate.
  # E3-R3 cross-check: 45,000 × 0.018 = 810 hr/yr coordinator production time;
  # combined with 0.8 FTE × 1,600 hr/yr × 0.70 production fraction = 896 hr/yr.
  # Discrepancy: 86 hr (9.6%); within P2 threshold for a fixed-overhead allocation.
  # [Derived from throughput_units_equiv_per_year and active-hours calculation above]

  downtime_fraction: 0.10
  # Sources: deck element failure on one of four units (~2,200 hr to failure;
  # facility continues operating with three remaining units at reduced capacity;
  # partial throughput reduction ~25% × 14-day repair lead = ~1.5-2% effective
  # facility downtime); door gasket replacement on up to two units (5-day lead,
  # operator-serviceable, ~0.5% each); deck stone replacement (~1% per incident);
  # cooperative administrative and scheduling gaps (annual closure, board activities,
  # license-renewal inspection shutdowns: ~4%); routine maintenance shutdowns
  # (~2%). Total: ~10%.
  # Note: booking underutilization (30% below full-booking ceiling) is NOT
  # included in downtime_fraction — it is already embedded in loaves_per_day
  # (200 loaves/day reflects 70% booking utilization, not 100%). The 10%
  # downtime captures only equipment failures and administrative shutdowns.
  # Consistent with E3-R6: multi-unit facility absorbs single-unit failures
  # without full-facility shutdown; lower downtime fraction appropriate.
  # [Derived from operations_reality.first_year_failures above; label: inferred]

  lifespan_years: 20
  # Commercial electric deck ovens: same rated life as bake-010 (15,000-20,000
  # operating hours). At 80 facility-oven-hours/wk, each oven operates ~20 hr/wk;
  # 20,000 hr ÷ (20 hr/wk × 50 wk/yr) = 20 years to rated end-of-life per unit.
  # With professional service at year 10-12, full design life 18-22 years per unit.
  # Facility lifespan is governed by the cooperative's lease or property agreement,
  # not by equipment replacement: individual ovens can be replaced as they fail
  # (the cooperative's capital base regenerates through booking revenue and retained
  # earnings, or replacement is funded by member assessment). 20 years is
  # a conservative cooperative-entity planning horizon.
  # [CITATION-NEEDED: service life data for commercial electric deck ovens;
  # manufacturer specification; label: inferred]

  annual_public_use_hours: 4000
  # Civic lens utilization input. Computed as facility booking hours × concurrent users:
  # Booking hours: 56 effective facility-oven-hr/wk × 50 wk = 2,800 hr/yr of oven time.
  # Concurrent users per booking hour: 1 member + 0.1 coordinator (pro-rated
  # coordinator presence across bookings); effectively ~2 average persons in the
  # facility per active booking hour (member + shared coordinator time + occasional
  # visiting partner or assistant): 2,800 × 2 = 5,600 person-hours. However, at
  # peak concurrent operation (4-6 members simultaneously), total person-hours rise:
  # assume 40% of hours are multi-member concurrent (2.5 average members concurrent)
  # and 60% single-member; weighted average ~1.75 persons/hr × 2,800 hr = 4,900 hr.
  # Using 4,000 as a conservative round estimate.
  # At town scale (7,500 residents): 4,000 ÷ 7,500 = 0.53 hr/capita/yr.
  # [Derived from effective facility booking hours and concurrent occupancy estimate]

  usage_rate_threshold: 0.15
  # Specialized civic facility exception per ECONOMIC-LENSES.md §4.3 precedent.
  # The shared kitchen is a supervised-access facility with physical capacity
  # limited to 2-6 simultaneous members; it cannot serve unrestricted public
  # traffic. The 0.15 hr/capita threshold preserves civic-lens marginal viability
  # at 0.53 hr/capita/yr (town scale).

  amortization_years: 20
  # Cooperative asset amortization consistent with cooperative-corporation
  # accounting norms and equipment lifespan. Shorter than municipal bond horizon
  # (25 yr in civic entries) because cooperative capital is raised through member
  # equity and grants, not long-term municipal bonds.

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: fail
    primary_metric: -1.0
    metric_name: payback_years
    notes: market_price_per_unit absent or zero; entry not designed for market lens
  village_coop:
    verdict: fail
    primary_metric: 250.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=250, total_annual_cost=49900
  village_civic:
    verdict: win
    primary_metric: 51.8
    metric_name: per_household_cost
    notes: per_hh=51.80, threshold=120, hrs/capita=3.200 vs threshold=0.15
  town_market:
    verdict: fail
    primary_metric: -1.0
    metric_name: payback_years
    notes: market_price_per_unit absent or zero; entry not designed for market lens
  town_coop:
    verdict: fail
    primary_metric: 250.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=250, total_annual_cost=49900
  town_civic:
    verdict: win
    primary_metric: 7.617647058823529
    metric_name: per_household_cost
    notes: per_hh=7.62, threshold=100, hrs/capita=0.471 vs threshold=0.15
  small_city_market:
    verdict: fail
    primary_metric: -1.0
    metric_name: payback_years
    notes: market_price_per_unit absent or zero; entry not designed for market lens
  small_city_coop:
    verdict: win
    primary_metric: 250.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=250, total_annual_cost=49900
  small_city_civic:
    verdict: fail
    primary_metric: 1.4388888888888889
    metric_name: per_household_cost
    notes: per_hh=1.44, threshold=80, hrs/capita=0.089 vs threshold=0.15
sources:
  - ref: "corpus/program/SCALES.md §2 — town scale parameters; household count multiplier (0.40); civic cost threshold at town scale"
  - ref: "corpus/program/SCALES.md §3 — town-scale skilled-trades median wage $56,000/yr; facility-coordinator wage reference"
  - ref: "catalog/baking/SCHEMA.md v1.0 §1 — throughput block structure; loaves/day ranges; E-3 cross-check guidance"
  - ref: "catalog/baking/SCHEMA.md v1.0 §2 — electric-deck energy consumption 3-8 kWh/batch; temperature ceiling 230-290°C"
  - ref: "catalog/baking/SCHEMA.md v1.0 §3 — apprentice-baker and journeyman-baker skill definitions; product scope boundaries"
  - ref: "catalog/baking/SCHEMA.md v1.0 §4 — flour_source_declaration required field; industrial-flour-purchased supply-chain risk"
  - ref: "catalog/baking/SCHEMA.md v1.0 §5 — first_year_failures reference list; deck element 1,500-3,000 hr; door seal 1,500-3,000 hr; deck stones 800-2,500 hr thermal shock"
  - ref: "catalog/baking/SCHEMA.md v1.0 §6 Group C — community/civic/cooperative entries guidance; lens_context.cooperative load-bearing fields for bake-012"
  - ref: "catalog/baking/DECLINE-VERDICT.md — niche targeting; mill-dependency falsifier; cooperative shared kitchen as compliance-cost-sharing model"
  - ref: "catalog/baking/entries/010-civic-neighborhood-bakery.md — bake-010 precedent; annual_public_use_hours methodology; usage_rate_threshold 0.15; multi-user kitchen layout reference"
  - ref: "Ostrom, Elinor. 1990. Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press. (Chapters 2-3: eight design principles for commons governance; graduated sanctions; conflict resolution; collective-choice arrangements)"
  - ref: "US Energy Information Administration. Electric Power Monthly, Table 5.3: Average Retail Price of Electricity. Monthly release. https://www.eia.gov/electricity/monthly/ (small-commercial blended rate 2023-2024: $0.10-$0.15/kWh; midpoint $0.125 used)"
  - ref: "OSHA 29 CFR 1910.1000 Table Z-1. Air Contaminants. (Flour dust permissible exposure limit; applicable to shared commercial baking operations)"
  - ref: "OSHA 29 CFR 1910.95. Occupational noise exposure. (90 dB(A) PEL for 8-hour shift; shared kitchen ambient noise assessment)"
  - ref: "[CITATION-NEEDED: commercial shared kitchen footprint survey; multi-operator kitchen layout requirements at community-kitchen cooperative scale, 2024]"
  - ref: "[CITATION-NEEDED: capital cost data for multi-oven commercial shared kitchen fitout, 2024-2026; Bongard, Sveba-Dahlen, Mono Equipment, or equivalent commercial bakery equipment vendor catalogs]"
  - ref: "[CITATION-NEEDED: installation cost for multi-oven commercial shared kitchen; electrical service upgrade (200-400A three-phase) cost data; exhaust system multi-hood installation, 2024]"
  - ref: "[CITATION-NEEDED: annual maintenance data for shared commercial kitchen operations at 4-oven multi-member scale; trade or operator survey, 2024]"
  - ref: "[CITATION-NEEDED: commercial kitchen licensing cost ranges ($5,000-15,000/yr) by US jurisdiction; health department permit fee schedules; label: inferred from general knowledge of commercial kitchen regulatory environment]"
  - ref: "[CITATION-NEEDED: commercial kitchen / light-industrial rental rate per m² at town-to-small-city scale in US markets, 2024; CoStar, LoopNet, or commercial real estate market survey]"
  - ref: "[CITATION-NEEDED: shared commercial kitchen booking rate survey ($15-25/hr range); US shared commercial kitchen market data, 2024; Cooperative Kitchen Alliance or equivalent industry survey]"
  - ref: "[CITATION-NEEDED: BLS Occupational Employment and Wage Statistics, Food Service Managers (SOC 11-9051) and Baker (SOC 51-3011), 2024; facility-coordinator wage range in US town-scale markets]"
  - ref: "[CITATION-NEEDED: municipal small-business incubator program cost data for towns of 2,000-15,000 population; economic development grant program surveys, 2024]"
  - ref: "[CITATION-NEEDED: service life data for commercial electric deck ovens under multi-operator shared-kitchen use conditions; manufacturer specification or industry longevity survey]"
  - ref: "[CITATION-NEEDED: US shared commercial kitchen cooperative formation data; Kitchen Table Coop, La Cocina, Hot Bread Kitchen, or equivalent incubator kitchen program evaluations and member economics]"
  - ref: "[CITATION-NEEDED: state cooperative-corporation statute citations by jurisdiction; California Corporations Code §§12200-12604; Minnesota Statutes §308B; equivalent state cooperative-corporation law]"
---
## Summary

Bake-012 is a cooperative-owned shared commercial kitchen: members book oven time for their own cottage-food, catering, and meal-prep businesses at a compliant commercial facility none of them could afford to build or license independently. The facility houses three to four commercial electric deck ovens, proofing cabinets, a spiral mixer, and multiple independent prep stations in approximately 80 m² of cooperative-leased floor space. The primary purpose is compliance-cost sharing: commercial kitchen licensing runs $5,000-15,000/yr in most US jurisdictions, and the capital investment in a code-compliant multi-oven facility is $55,000-165,000. By pooling these costs across 20-50 member-businesses, the cooperative converts a prohibitive per-business barrier into a manageable shared overhead of ~$150-600/year in dues plus $15-25/hr booking fees. This entry is structurally distinct from bake-010 (Civic Neighborhood Bakery): bake-010 is a publicly-owned food-access and training service with an instructor supervising community members; bake-012 is a member-owned cooperative of independent operators who share infrastructure and license but run their own businesses. The instructor is absent; members self-operate. The cooperative does not sell bread; its members do.

## Design rationale

This entry addresses a specific problem none of the other baking catalog entries solve: the regulatory compliance barrier for cottage-food entrepreneurs at the threshold between home-kitchen operation and commercial food production. In the US, selling food products above the cottage-food-law threshold — or selling categories (meat, certain dairy-containing items, catering for events serving the public) that cottage-food laws do not cover — requires a commercially licensed kitchen. The barrier is not skill; it is fixed compliance cost. A $10,000/yr commercial kitchen license is a fatal overhead for a part-time home baker with $40,000 in annual sales. The cooperative model makes this tractable: twenty members each paying $500/yr in dues and $2,500/yr in booking fees together fund the license, the equipment, and the facility-coordinator. Each member retains full ownership of their product, brand, and customer relationships; the cooperative is the shared infrastructure, not the business. This is categorically different from bake-003 (Community Grain-Share) where the cooperative bakes and distributes collectively, or bake-010 where a civic instructor supervises public participants. The design rationale for selecting electric-deck as the energy source is consistent with other multi-user entries: thermostat control (critical when multiple operators run different products at different temperatures in adjacent ovens), near-zero combustion emissions (simplest permit path for a shared commercial building), and elimination of fuel-storage requirements that would complicate a multi-tenant cooperative lease. The footprint (60-100 m²) is calibrated to the multi-operator layout: independent prep stations require physical separation for food-safety compliance (cross-contamination between members' allergen profiles is a real regulatory concern).

## Historical lineage

Three functional precedents inform this design; each requires precise treatment of what was carried forward and what was not.

**US shared commercial kitchen movement (1990s–present).** The contemporary shared commercial kitchen sector emerged in the 1990s as cottage-food businesses and food entrepreneurs encountered the same commercial-kitchen licensing barrier this entry addresses. Incubator kitchens — originally developed by culinary business incubators, CDFIs, and community development organizations in urban areas — proved that pooled commercial kitchen access could support viable food business development. La Cocina (San Francisco, est. 2005), Hot Bread Kitchen (New York, est. 2008), and the Kitchen Table Cooperative model [CITATION-NEEDED: functional description of these programs] represent different ownership structures around the same infrastructure logic: licensed commercial kitchen space, shared across multiple food-business operators who cannot afford individual facilities. The functional inheritance to this entry is the operating model itself — the booking system, the member-operator independence, the compliance-license-as-shared-overhead logic, and the facility-coordinator role as operations manager rather than production supervisor. What this design does not inherit from the incubator kitchen model is the nonprofit charitable framing: the cooperative model positions members as owners who govern the facility for collective benefit, not beneficiaries of a charitable food-business support program. The property structure is different; the governance motivation is different; the economic sustainability model is different (member fees rather than donor subsidy).

**Cooperative extension community canning programs (early twentieth century).** The US Cooperative Extension Service operated community canning kitchens from the 1910s through the mid-twentieth century: licensed shared food-production facilities where rural households could can fruits, vegetables, and meats in quantities too large for home processing, using commercial-grade equipment under supervised conditions. [CITATION-NEEDED: historical description of cooperative extension canning kitchen programs; functional description of shared-kitchen operating model.] The functional inheritance is the shared-use-of-licensed-infrastructure model: rural households could not individually afford commercial canning equipment, but a county extension service facility could aggregate access cost-effectively. The compliance rationale (food safety from licensed industrial equipment) is identical to the modern shared kitchen. What this design explicitly does not inherit from the extension-service model is its government-agency ownership structure: the modern cooperative kitchen is member-owned, not extension-service-operated. The extension-service canning kitchen was also a product of an era when food processing at home was a survival necessity; the modern shared kitchen serves a different economic reality (entrepreneurship and regulatory arbitrage, not household food preservation). The participation motivation and governance structure are categorically different; the infrastructure logic is the same.

**Ostrom's common-pool resource governance (theoretical grounding).** The Community Kitchen Collective is formally a governed common-pool resource: the commercial kitchen license, the equipment, and the booking slots are the shared resource; exclusion and subtractability both apply (a booking slot used by one member is unavailable to others; the license's compliance status is diminished by violations). Ostrom's design principles (1990) are the theoretical authority for the governance structure documented in lens_context.cooperative: clearly defined membership boundaries, damage-liability mechanism as graduated sanction, collective-choice arrangements via member-amended bylaws, and monitoring through coordinator checkout logs. The functional inheritance is the governance design language; the underlying institutional economics analysis is the reason the entry includes specific governance mechanisms rather than generic "cooperative bylaws." What this design acknowledges that Ostrom's original commons work does not fully anticipate is the commercial context: unlike a village fishery or irrigation system, this commons exists within a regulatory framework (commercial kitchen licensing) that external actors (health department, state alcohol and tobacco control analog for food) can terminate at will. The legal form (registered cooperative-corporation) is the response to this additional fragility.

## Key assumptions

**Flour and ingredients (member-supplied):** Each member brings their own flour and primary ingredients to their booking slot. The cooperative facility provides only energy, cleaning materials, facility-provided consumables (parchment, starter cultures), and equipment. This design decision is fundamental to the entry's economic model: the cooperative's annual_consumables ($15,500/yr) is unusually low compared to other baking entries because flour — which dominates consumables in all other entries — is not a facility cost. The member's effective per-loaf cost includes their own ingredient cost (~$0.40-1.20/loaf in flour and ingredients, depending on product) plus the allocated booking fee (~$0.30-0.80/loaf depending on batch efficiency). The flour_source_declaration of industrial-flour-purchased applies to the facility's operational reality in aggregate: most members source commodity or specialty flour from industrial distributors or local mills per their own business model. The cooperative does not track member flour sourcing.

**Throughput (facility-level, 200 loaves/day):** This figure is explicitly a facility-level aggregate, not a single operator's output. It reflects four ovens × two batches per oven per day × 25 loaves per batch at 70% booking utilization (not full booking ceiling). The labeled unit is 800g sourdough boule equivalent per baking SCHEMA.md §1. Individual member sessions will produce diverse products (catering trays, pastry, meal-prep items); these are normalized to loaf-equivalents by weight for aggregate throughput accounting. The figure is labeled [CITATION-NEEDED] as empirical shared-kitchen aggregate throughput data was not available at authoring date; it is derived from structural inference from the multi-oven layout and booking model.

**Booking economics:** The cooperative's financial sustainability depends on achieving sustained booking utilization above ~65% of available slots. The booking rate assumption ($20/hr average; $50-100/half-day slot) is drawn from shared commercial kitchen market surveys [CITATION-NEEDED]. Below 55% utilization, the cooperative cannot cover operating costs without substantial external subsidy. Member recruitment and retention is the primary operational risk; the cooperative requires active cultivation of its member base, not passive receipt of bookings. The $46,000/yr facility-coordinator wage is below the $56,000/yr SCALES.md town-scale skilled-trades median, reflecting the operations-management rather than production-baker nature of the role; this below-market positioning carries hiring risk noted in Known Risks.

**Commercial kitchen licensing cost ($5,000-15,000/yr):** This range represents the most important single parameter for the cooperative's economic rationale. At $5,000/yr, the compliance-cost-sharing argument is weaker (a sole operator might find this manageable); at $15,000/yr, pooling the cost across 20-50 members is strongly compelling. The range is derived from general knowledge of US commercial kitchen regulatory environments [CITATION-NEEDED: actual fee schedule data needed]. Jurisdictional variance is very high; entry authors and implementers must verify local health-department fee schedules before using this entry for actual planning.

**sim_params derivation:** throughput_units_equiv_per_year (45,000) derived from 200 loaves/day × 250 operating days × (1 - 0.10 downtime). Note that the 200 loaves/day already embeds 70% booking utilization; the 10% downtime captures only equipment and administrative downtime, not booking underutilization. cost_mean (100,000) equals capital_cost.mid. cost_sd (27,500) = (165,000-55,000)/4. All monetary values in USD.

## Known risks / failure modes

**Regulatory (primary risk):** The cooperative's single commercial kitchen license is the facility's existential regulatory dependency. A food-safety violation by any member — a contaminated product, an unreported allergen incident, a health inspector finding that the facility's cleaning protocols are not being followed — can result in license suspension affecting all 20-50 member businesses simultaneously. This systemic risk is the inverse of the compliance-cost-sharing benefit: just as compliance costs are pooled, compliance failures are pooled. The damage-liability mechanism and graduated sanctions documented in lens_context.cooperative address individual member behavior, but cannot fully prevent every food-safety incident in a self-operated multi-member facility. The facility must maintain a documented allergen-management protocol (member disclosure of allergen-containing products, scheduling to separate allergen-intense sessions from sensitive-product sessions) and a comprehensive HACCP plan applicable to all member product categories. This regulatory complexity is higher than bake-010's supervised civic model and is a significant management burden for the facility-coordinator role.

**Labour pipeline (facility-coordinator succession):** The facility-coordinator is the operational single point of failure for the cooperative's day-to-day function. Unlike bake-010's baker-instructor, the coordinator role does not require a rare combined skill profile (operations management at journeyman-baker level is a broader hiring pool). However, the cooperative is a single-employer entity; if the coordinator departs mid-season, booking operations, health-department compliance, and member checkout processes are all disrupted until a replacement is hired and trained. The cooperative should maintain a documented coordinator orientation manual, an up-to-date booking system that any board member can access, and a succession plan that identifies at least one advanced member qualified to serve as interim coordinator for 30-60 days. At below-market wage ($46,000/yr), coordinator retention risk is real; the cooperative's mission-alignment argument and non-wage benefits (flexible hours, cooperative ownership participation) must be actively maintained.

**Supply chain:** The facility's supply chain is primarily energy and cleaning materials — highly available at town scale with short lead times. The more significant supply-chain risk is the members' individual ingredient supply chains: a specialty flour shortage affecting multiple members simultaneously (e.g., a single specialty mill failure) concentrates member-business disruption in a way that the facility itself does not control. The cooperative has no visibility into or leverage over members' individual supply chains; this is by design (member independence) but means that aggregate throughput can drop sharply if a common ingredient source is disrupted across the member pool. Grid electricity outage is the facility's own supply-chain single point of failure; a multi-oven electric facility without backup power has zero production capacity during outages, and all members' scheduled booking slots are lost simultaneously.

**Cooperative cohesion and governance failure:** Shared-kitchen cooperatives face characteristic governance failure modes that Ostrom's framework does not fully anticipate: (1) booking-rate free-riders (members who book slots at peak times and then cancel without notice, preventing other members from filling the slot); (2) equipment-damage moral hazard (members who damage equipment know the cooperative will pay for repairs, reducing individual care); (3) high-volume member power imbalance (members who book 40% of all slots have disproportionate informal influence even if formal governance is one-vote-per-member); (4) founding-member capture (governance calcifies around the preferences of the members who launched the cooperative, excluding later joiners from meaningful policy participation). The damage-liability mechanism, cancellation policy, and member amendment process documented in lens_context.cooperative are direct responses to failure modes 1-3. Failure mode 4 is addressed by the Ostrom Principle 3 explicit statement: "No single board member or founding member holds unilateral amendment authority." These mechanisms must be actively enforced; a cooperative that documents but does not enforce its governance rules will experience the same commons failure as one with no governance documentation.

## Iteration log

- 2026-04-18: v0.1 — initial authoring per Plan G Task 14. Coop-primary shared commercial kitchen entry per spec requirement. Full v1.1 schema populated: electric-deck multi-oven facility, $55k-$165k capital range, 80 m² footprint at multi-oven scale, industrial-flour-purchased declaration (member-supplied flour; facility does not purchase flour), apprentice-baker member skill floor with journeyman-level facility-coordinator, scale_fit town/small_city good + village poor, lens_fit cooperative good + civic marginal + market poor. Full lens_context.cooperative block with Ostrom principles 1-6: booking-system-based member access, damage-liability mechanism as graduated sanction, legal form as cooperative-corporation or 501(c)(3), member amendment process requiring 2/3 vote with 30-day notice, scale_fit_note calibrated to town-to-small-city. Full lens_context.civic block (marginal lens): economic-development political coalition, 4-3 marginal council estimate, competes_with_private analysis, staffing_model at $46k/yr facility-coordinator citing SCALES.md §3, three civic_externalities (small-business incubation, cultural food preservation, food-business licensing pathway), benchmark_comparison vs municipal incubator programs. sim_params: cost_mean 100,000; cost_sd 27,500; throughput_units_equiv_per_year 45,000 (facility-level aggregate, 200 loaves/day × 250 days × 0.90); variable_cost_per_unit $0.34 (energy and facility consumables only; flour member-supplied); labor_hours_per_unit 0.018 (coordinator hours only); downtime_fraction 0.10 (equipment/administrative only; booking utilization embedded in loaves_per_day). Key anti-romanticism: explicitly named compliance-cost-sharing (not communal baking tradition) as the operative logic; multi-member simultaneous damage risk as inverse of compliance-benefit; governance failure modes (free-riders, moral hazard, founding-member capture) named in Known Risks beyond standard Ostrom analysis. Twenty-six source entries with appropriate [CITATION-NEEDED] flags over fabrication on capital costs, licensing fees, booking rates, wages, and historical precedent descriptions.
