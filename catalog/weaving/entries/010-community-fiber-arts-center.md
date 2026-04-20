---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: weave-010
trade: weaving
name: "Community Fiber Arts Center"
tagline: "Town-owned multi-loom shared workshop with supervised open-studio access, dyeing facilities, and a structured journeyman-weaver training program"
status: draft
version: 0.1
supersedes: null
inspirations:
  - us-public-library-model
  - danish-folkhøjskole-textile-tradition
  - new-england-weaving-guild-cooperative

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 65
# Mid-range of the 50–80 m² span. Accommodates 4–6 floor looms in individual
# bays, a rigid-heddle station row for beginners, a dyeing alcove, warping
# board wall, and a central fiber/storage island. Ceiling height supports
# upright floor-loom castles and natural ventilation over the dye station.
ceiling_min_m: 3.0
ventilation: mechanical-extraction-required
# Dyeing station requires local exhaust over the dye vats (mordant vapors,
# steam). Main weaving hall requires fresh-air circulation for humidity
# management and comfort of multiple concurrent users. A dedicated exhaust
# system for the dye alcove and general mechanical air exchange for the
# weaving floor are both required.

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: electric-lighting-only
# Primary productive equipment (floor looms, rigid heddles) requires no
# powered drive mechanism. Energy consumption is limited to: studio lighting,
# climate control (humidity regulation required for wool/silk work), small
# electric accessories (yarn winder, drum carder), and dye-station hot plate
# or electric wax pot. No three-phase power required.
energy_consumption_per_active_hour: "3–6 kWh (lighting + humidity control at steady state; dye-station burner adds ~1–2 kWh/hr during dye sessions)"
backup_fuel: null

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  meters_per_day: 8.0
  # Per-facility blended daily output across all active looms.
  # Assumes 4 floor looms + 2 rigid-heddle stations, with a member mix of
  # novice through journeyman skill levels. Individual loom yields:
  #   floor-loom journeyman plain/twill: 3–5 m/day per loom
  #   floor-loom novice-supervised: 1–2 m/day
  #   rigid-heddle beginner: 0.5–1.5 m/day
  # Blended across 4 FL + 2 RH stations at ~60% occupancy: ~8 m/day facility-wide.
  # [CITATION-NEEDED: multi-loom facility blended throughput; derived from
  #  weaving SCHEMA.md §1 per-loom ranges and conservative station-occupancy estimate]
  warp_width_cm: 90
  # Representative warp width for the primary floor-loom configuration (4-shaft,
  # 90 cm). Rigid-heddle stations are narrower (45–60 cm) and treated as
  # entry-level instruction equipment rather than primary production looms.
  pattern_complexity: twill
  # Floor looms are set up for plain-weave through twill structures by the
  # supervising journeyman-weaver; advanced pattern work (overshot, M's & O's)
  # is undertaken by experienced members under supervision. Plain weave and
  # twill are the baseline for throughput calculations.
  max_active_hours_per_week: 30
  # Civic scheduling: 5–6 days/wk × ~5 hr/session = 30 hr/wk upper bound.
  # Includes warping-setup sessions (charged to session time, not excluded).
  # Net of startup/shutdown overhead, effective production hours ~27 hr/wk.
  product_mix:
    yardage: 30
    rugs_upholstery: 10
    tapestry_art: 0
    garments_accessories: 10
    instruction_open_studio: 50
    # instruction_open_studio dominates: 50% of active loom-hours are members
    # weaving on their own projects under supervision, with instruction woven
    # into the session. This is the defining feature of the civic model.
    # Yardage, rugs, and accessories are member projects sold or retained;
    # the facility does not produce for commercial sale on its own account.
    # Sum: 30 + 10 + 0 + 10 + 50 = 100.
  throughput_variance:
    seasonal: "Workshop demand is moderately seasonal: autumn/winter uptick (project-focused work, holiday gift weaving); summer uptick from workshop intensives and school programs; January trough."
    worst_month_fraction_of_average: 0.60
    best_month_fraction_of_average: 1.45

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: journeyman-weaver
# The civic multi-loom model requires a journeyman-weaver as the floor
# supervisor: they must simultaneously assess warp-tension problems across
# up to 6 member stations, provide threading and tie-up guidance, and
# manage the dyeing alcove safely. A rigid-heddle-novice cannot supervise
# floor-loom threading or manage dye chemistry; a journeyman-weaver is
# the minimum functional floor for safe and productive supervision.
operators_concurrent: "1 supervisor + up to 5 members"
# Scheduled shift model: 1 journeyman-weaver supervisor present at all
# times; up to 5 community members work simultaneously (mix of floor looms
# and rigid-heddle stations). Concurrent headcount is a safety and quality
# limit enforced by the booking system.
apprentice_friendly: true
apprentice_path:
  training_stages: >-
    Stage 1 — Orientation and Rigid-Heddle Basics (0–3 months): studio orientation,
    loom safety (no pinch points, shuttle handling, beater use), rigid-heddle warp
    winding and dressing, plain-weave production on rigid-heddle loom, yarn selection
    basics, introduction to fiber types (cotton, wool, linen).
    Competency gate: independently warp and weave a 2-meter plain-weave sample on a
    rigid-heddle loom without supervision.

    Stage 2 — Floor Loom Fundamentals (3–12 months): introduction to floor-loom-4shaft
    threading, tie-up, and treadling sequences; warp calculation and sett decisions
    for plain weave and 2/2 twill; shuttle management and selvedge control; warp
    tension monitoring and adjustment.
    Competency gate: independently thread a 4-shaft floor loom from a draft, weave
    a 5-meter twill sample meeting consistent selvedge and sett standards.

    Stage 3 — Supervised Production and Dye Introduction (12–24 months): independent
    production of woven cloth (yardage, scarves, functional textiles) on floor loom
    with weekly journeyman review; introduction to dyeing alcove (mordant preparation,
    basic exhaust dye baths); assisting with member orientation sessions.
    Competency gate: complete a 20-meter yardage commission end-to-end without direct
    supervision; demonstrate safe dye-bath setup and pH management.

    Stage 4 — Journeyman Progression (24–36+ months): advanced pattern structures
    (overshot, M's and O's); full independent dye-bath management; eligible to lead
    beginner instruction sessions under master-weaver oversight; journeyman assessment
    by senior weaver or regional guild examiner.
  time_to_independent_operation: "~24 months to independent floor-loom operation; ~36 months to journeyman-weaver standard with dye competency"
  succession_note: >-
    The community fiber arts center structurally embeds succession: apprentice training
    is the normal operating mode, not a separate program. Stage 2–3 apprentices
    participate in member instruction sessions, transmitting skill while contributing
    to the civic mission. Each training cohort over a 3-year cycle produces 1–3
    candidates for journeyman status, creating a regional pipeline for studio weavers
    and occupational-therapy partnership programs. The institutional curriculum,
    loom-setup documentation, and dye-process records reduce dependence on any
    single supervisor's tacit knowledge.

# ── TRADE-SPECIFIC FIELDS ────────────────────────────────────────────────────

trade_specific:
  loom_type: floor-loom-4shaft
  # Primary production equipment. Four floor-loom-4shaft units are the
  # core capital item; rigid-heddle stations (2–3 units) are supplementary
  # beginner and instruction equipment. If spinning wheels are present
  # (optional integrated-spinning module), they occupy the fiber-prep corner
  # and are documented separately in the civic-externalities block.
  humidity_control_required: true
  # Wool and silk work is conducted at these looms; heritage-fiber projects
  # and therapeutic weaving programs use natural fiber. Target RH 45–55%
  # for warp-tension stability. Climate-control system is a required capital
  # item; see Key Assumptions for HVAC cost disaggregation.
  fiber_source_declaration: industrial-yarn-purchased
  # The civic open-studio model uses commercially sourced yarn: members
  # bring their own yarn or purchase from a small studio yarn stock. The
  # facility does not operate a fiber sourcing or spinning program as a
  # default; an integrated-spinning module is an optional upgrade (see
  # civic_externalities for spinning-wheel integration note).
  annual_public_use_hours: 7800
  # Civic lens utilization input. Computed as facility open hours × concurrent users:
  # facility_hours = max_active_hours_per_week × 52 = 30 × 52 = 1,560 hr/yr.
  # concurrent_users = 5 (1 supervisor + up to 4 active members at any time;
  # conservative figure given 5-member booking ceiling and variable occupancy).
  # annual_public_use_hours = 1,560 × 5 = 7,800 person-hours/yr.
  # This metric captures the total public-access person-hours delivered per year;
  # it is the correct denominator for civic utilization assessment at a multi-user
  # supervised facility. See forge-004 sim_params for the usage-rate formula precedent.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 30000, mid: 65000, high: 110000 }
  # Low: 2 second-hand floor looms + 2 rigid-heddle stations + basic dyeing
  #      equipment + residential humidity control + used warping equipment.
  # Mid: 4 new floor-loom-4shaft units ($2,500–$4,500 each) + 2–3 rigid-heddle
  #      stations + warping boards/mills + dyeing alcove equipment (stainless vats,
  #      electric hot plates, mordant stock) + commercial humidity-control system
  #      + yarn winder + drum carder + storage and studio fit-out.
  # High: 6 floor looms (some 8-shaft) + full rigid-heddle bank + jacquard-capable
  #       upgrade option + full dye kitchen (professional vats, exhaust hood) +
  #       commercial HVAC with humidity management + spinning-wheel complement.
  # [CITATION-NEEDED: floor-loom-4shaft capital cost — estimated from equipment
  #  retailer pricing (Schacht, AVL, Leclerc); see Key Assumptions]

  install_cost: 8000
  # Covers: humidity-control HVAC installation, dye-station local exhaust ventilation,
  # electrical service upgrade for climate-control load, and studio fit-out (loom
  # bay markings, storage shelving, signage). Rough estimate; actual cost varies
  # with building condition. [CITATION-NEEDED: HVAC + exhaust install cost estimate]

  annual_maintenance: 3500
  # Multi-loom facility: heddle replacement, reed maintenance, treadle tie-up cord
  # renewal, warp-beam ratchet service across 4–6 looms; HVAC filter replacements
  # quarterly; dye-vat and mordant equipment cleaning and annual inspection. Higher
  # per-loom maintenance rate than single-studio entries due to multi-user wear intensity.
  # [CITATION-NEEDED: annual maintenance estimate for comparable civic fiber arts facility]

  annual_consumables: 4800
  # Workshop yarn sample stock (foundation warps for beginner instruction: ~$1,200/yr);
  # heddle replacements across all looms (~$400/yr); reed replacement cycle (~$300/yr);
  # treadle tie-up cord stock (~$150/yr); dyeing consumables (mordants, dye materials,
  # pH testing supplies: ~$1,800/yr); general studio supplies (scissors, tapestry needles,
  # shuttle replacement, labels: ~$600/yr); cleaning and safety supplies (~$350/yr).
  # [CITATION-NEEDED: weaving facility consumables estimate; derived from per-item
  #  pricing in weaving supply catalogs; see Key Assumptions]

  floor_space_rent_per_year: 0
  # Town-owned facility; floor space imputed at $0. Civic ownership eliminates rent
  # as an operating cost line. The full facility capital (building) is amortized in
  # the town's broader community-space budget, not in this equipment-module entry.
  # This cost advantage over cooperative or private studio operators is significant:
  # a comparable rented commercial studio would carry $8,000–$15,000/yr in floor
  # space rent at typical light-commercial rates for 65 m².

  market_price_per_unit: { low: 0, mid: 0, high: 0 }
  # Civic operation; no commercial output pricing. The facility does not sell
  # woven cloth on the market. Member access fees ($40–80/yr) are library-model
  # access charges, not per-unit or per-session prices. Workshop instruction fees
  # (if charged) are cost-recovery, not market pricing. See pricing_notes.

  pricing_notes: >-
    This is a civic open-studio facility, not a commercial weaving producer.
    market_price_per_unit is set to zero because the facility does not sell woven
    output at market prices: member projects are owned by members; the facility's
    production function is access, instruction, and community use, not commercial
    output. The industrial baseline price ($8/m for comparable plain-weave cotton
    cloth from domestic commercial textile importers [CITATION-NEEDED]) is cited
    for reference only — to document the replacement-cost framing of the subsidy,
    not as a premium calculation. Annual member fees ($40–80/yr) are comparable
    to a library card or recreation-center day-use pass; they do not represent
    per-unit pricing.

  industrial_baseline_price: 8
  # Reference baseline for plain-weave cloth equivalent (cotton, commodity
  # commercial grade). Cited for civic-lens comparison only; not used in
  # revenue calculations (lens_fit.market: poor). [CITATION-NEEDED: commercial
  # plain-weave cotton cloth wholesale price per meter, US market 2024-2025]

  pricing_validation: >-
    N/A — civic operation with no commercial output pricing. Member fees are
    access charges, not unit prices. Industrial baseline cited for civic-subsidy
    reference comparison only; evidence for baseline is commercial textile importer
    pricing from domestic fabric distributors [CITATION-NEEDED]. No market-price
    premium claim is being made.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:

  first_year_failures:
    - item: "Heddle breakage (wire heddles, floor-loom-4shaft × 4 units)"
      estimated_hours_to_failure: 800
      # Multi-user multi-loom facility: novice users apply uneven tension,
      # drop shuttles into heddle eyes, and misthread — all accelerating
      # wire heddle fatigue relative to single-operator studio use. First
      # failure expected within the first operating year across the loom bank.
      replacement_cost: 120
      # Per-loom heddle set replacement (wire heddles for 4-shaft loom, ~$25–35
      # per shaft × 4 shafts = $100–140 per loom; spot replacement ~$25–40).
      replacement_lead_time_days: 5
      serviceable_by: operator
      # Heddle replacement is operator-serviceable (re-thread after replacing
      # heddles in the affected shaft); takes 30–90 minutes per shaft.

    - item: "Warp beam ratchet / pawl wear (floor-loom-4shaft, first unit)"
      estimated_hours_to_failure: 2000
      replacement_cost: 200
      replacement_lead_time_days: 10
      serviceable_by: journeyman
      # Ratchet-and-pawl beam tensioning wears under continuous multi-user
      # use; tension slippage mid-weave is a quality and safety concern.
      # Journeyman-level diagnosis and pawl spring or full ratchet replacement.

    - item: "Climate-control humidifier unit failure"
      estimated_hours_to_failure: 2500
      # Residential-to-commercial humidifier under continuous load in a
      # 65 m² workshop; first-year failure probability is significant.
      replacement_cost: 750
      replacement_lead_time_days: 7
      serviceable_by: specialist
      # HVAC humidifier component failure requires specialist diagnosis if
      # integrated into the central system; standalone portable unit is
      # operator-replaceable but commercial/central unit requires specialist.

  maintenance_schedule:
    daily:
      task: "Safety walkdown of all loom stations: check warp tension and heddle condition on active warps, inspect shuttle stocks, verify dye-station is powered down and secure, sign-in log reset, humidity and temperature log entry"
      performed_by: operator
      # Journeyman-weaver supervisor completes the daily walkdown before the
      # first member session. Multi-user wear requires a more thorough daily
      # check than a single-operator studio; documented sign-off before opening.
    weekly:
      task: "Full loom inspection: treadle tie-up cord condition on all looms, reed alignment and bent-dent check, warp-beam ratchet function test, rigid-heddle slot wear inspection; dye-station cleaning and mordant inventory; humidity-control filter check"
      performed_by: operator
    quarterly:
      task: "Comprehensive loom service: ratchet/pawl inspection and lubrication on all floor looms, bulk heddle inventory assessment and replacement order, professional HVAC filter replacement, dye-vat deep clean and safety inspection, fire-suppression system check"
      performed_by: journeyman
    annual:
      task: "Full facility inspection: structural loom frames assessed for joint fatigue, all warp and cloth beams inspected for warping, HVAC system annual service contract call, electrical panel review, insurance and compliance walkthrough with town facilities department"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 35
  # Multi-user shared facility requires more extensive startup/shutdown than
  # a single-operator studio. 35 min/day: pre-session safety and loom-readiness
  # check (10 min), member check-in and orientation briefing for new users
  # (10 min on session-open days), post-session loom and dye-station shutdown
  # and log completion (15 min). This overhead is non-negotiable for a supervised
  # public-access facility.

  max_active_hours_realism_note: >-
    30 hr/wk is the civic scheduling gross target. Net of 35 min/day startup-shutdown
    overhead on a 5-day operating week: effective production/instruction hours are
    approximately 30 − (35 min × 5 days / 60 min) ≈ 27.1 hr/wk net.
    sim_params.throughput_units_equiv_per_year uses the derated figure of ~27 hr/wk.
    Civic scheduling additionally reduces effective hours via public holidays, member
    no-shows, and occasional facility conflicts; these are folded into the downtime
    fraction of 0.13 alongside equipment maintenance events.

  interruption_notes: >-
    In a multi-user supervised studio, intraday interruptions substantially exceed
    a single-operator shop. Typical interruption profile per session: beginner loom
    setup assistance (15–25 min total per session for 1–2 novice members), warp
    threading help on floor looms (10–20 min per threading question), shuttle or
    tension problem diagnosis (5–10 min per incident, 2–3 incidents/session typical),
    dye-station supervision if a dye session is in progress (intermittent monitoring,
    ~15 min total). Total intraday interruption approximately 45–75 min per operating
    session. These interruptions are folded into the instruction_open_studio product-mix
    fraction (50%) and the derated throughput figure in sim_params.

  consumables_lead_time_days: { typical: 7, worst: 30 }
  # Typical: standard weaving supplies (heddles, reeds, tie-up cord, basic mordants)
  # from regional weaving suppliers or online distributors.
  # Worst: specialty reeds (non-standard sett), specific floor-loom parts (warp-beam
  # hardware for older or uncommon models), or commercial HVAC components with
  # backorder; 30 days is the documented tail risk for specialty loom hardware.

  throughput_variance:
    seasonal: "Workshop demand is moderately seasonal: autumn/winter uptick from project-focused members and holiday gift weaving; summer spike from workshop intensives and school programs; January trough as members recover from holiday projects."
    worst_month_fraction_of_average: 0.60
    best_month_fraction_of_average: 1.45

  operator_impact:
    noise_db: 58
    # Floor-loom weaving: rhythmic beater and treadle sound; 55–65 dB at operator
    # position in a multi-loom studio. Below OSHA action level (85 dB) by a wide
    # margin; compatible with conversation and therapeutic use. [CITATION-NEEDED:
    # floor-loom noise level measurement — practitioner or acoustic survey]
    heat_exposure: "Low during weaving; moderate over dye vats during active dye sessions (steam, 60–90°C baths); adequate exhaust ventilation required over dyeing alcove; weaving hall comfortable year-round with humidity management"
    emissions: "Natural mordant vapors (alum, tannin, iron sulfate, vinegar) during dye sessions; no synthetic dye VOCs at standard civic program scale; local exhaust over dye alcove required; effluent pH management required for drain disposal of mordant baths"
    physical_demand: "Light-moderate: sustained seated treadling, repetitive upper-body shuttle and beater motion; standing during warping and loom dressing; supervisor role adds floor-walking and demonstration cycles throughout session"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Municipal institutional, light-commercial, or arts-district zoning; standard studio/assembly occupancy; no industrial-zoning trigger from floor looms or small-scale dye work; confirm local ordinance re: dye effluent for sewer permit"
  emissions: "Natural mordant effluent (tannin, iron sulfate, alum, vinegar) requires pH neutralization before drain discharge in most municipal sewer jurisdictions; check local POTW pretreatment rules; no air-permit trigger at this throughput; local exhaust over dye alcove satisfies typical OSHA non-industrial ventilation requirements"
  other: "Humidity-control HVAC requires standard commercial mechanical permit; public-access facility carries liability and insurance obligations beyond a private studio; town counsel review of member waiver, minor-access policy, and occupational-therapy partnership agreement required before operating"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: poor
  # Civic operation with zero commercial output pricing. The facility does not
  # compete on market terms, does not produce for sale, and has no revenue stream
  # that would support a market-lens evaluation. Market lens: poor.
  cooperative: good
  # Member-access model with documented bylaws, booking system, graduated sanctions,
  # and Ostrom-compliant governance. The legal form is municipal (not a registered
  # cooperative), but the operating model functions cooperatively with full
  # member-governance documentation.
  civic: good
  # Primary lens. Town ownership, public-goods externalities (textile education,
  # therapeutic weaving, cultural preservation, apprenticeship), and political
  # coalition are fully documented in lens_context.civic below.

scale_fit:
  village: poor
  # Capital requirement ($65,000 mid) is disproportionate at village scale
  # (500–2,000 residents): per-household cost would likely exceed political
  # tolerance, and insufficient scheduling demand to sustain a FT journeyman
  # supervisor. Village-scale fiber arts programs are feasible as informal
  # guild meetings (out of scope for this entry).
  town: good
  # Target scale: 2,000–15,000 residents. Sufficient population to spread
  # per-household cost to ~$10–13/hh/yr, generate scheduling demand to sustain
  # 30 hr/wk open-studio hours, and support the staffing model. Political
  # coalition (arts council + library board) is viable at town scale.
  small_city: good
  # Per-household cost falls further (favorable). Scheduling demand supports
  # extended hours and potentially a second shift. Multiple staff positions
  # may become viable. Core governance model transfers directly.

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:

  cooperative:
    membership_boundary: >-
      Town residents and immediate township equivalents; access granted via a
      library-card equivalent credential (town residency verification). Non-residents
      may join at a higher annual fee tier ($80–120/yr vs $40–80/yr resident rate)
      subject to capacity. No demographic restriction; open to all ages with minor
      waiver adjustments (under-18 requires parental consent and adjusted supervision
      ratio). Occupational-therapy program participants access the facility under a
      separate partnership agreement with defined session slots.

    rules_source: >-
      Posted workshop bylaws adopted by the facility committee (a standing subcommittee
      of the town library board, arts council, or parks-and-recreation department).
      Bylaws govern: loom booking and session limits, skill-tier certification for
      floor-loom access, dye-alcove use policy (trained members only), guest and
      observer policy, loom-damage liability, and access suspension procedures.
      Rules displayed in the facility and published on the town website.

    monitoring: >-
      Mandatory sign-in log for every session (member ID, date, loom or station used,
      hours, warp project record); supervisor observation during all operating hours
      (journeyman-weaver supervisor present at all times by policy); monthly
      facility-committee review of usage logs; incident and loom-damage log maintained
      separately, reviewed quarterly by the facility committee and town counsel.

    graduated_sanctions: >-
      Warning (verbal, logged) → written notice + 30-day suspended booking privileges →
      revoked access pending facility-committee review → permanent access revocation with
      opportunity for appeal to town board. Loom-damage incidents (unrepaired broken
      heddles left for next user, dye-station left uncleaned) carry immediate written
      notice plus cost-recovery charge for remediation. Safety violations (unauthorized
      dye-alcove use, unescorted minor access) may skip directly to suspension at
      supervisor discretion.

    conflict_resolution: >-
      Day-to-day disputes (scheduling conflicts, loom-damage attribution, dye-alcove
      use disputes) resolved by journeyman-weaver supervisor as floor authority.
      Member-vs-member disputes and appeals of supervisor decisions escalated to the
      facility committee (3–5 members drawn from library board, arts council, or
      parks-and-rec); facility-committee decisions are final subject to town board
      appeal. Conflict resolution meeting required within 14 days of formal written
      complaint.

    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6, 7, 8]
    # Principle 1 (clear boundaries): residency-based membership with documented
    #   eligibility criteria; skill-tier certification for floor-loom access.
    # Principle 2 (congruence): rules calibrated to multi-user civic-studio context;
    #   dye-alcove policy congruent with chemical-safety requirements.
    # Principle 3 (collective choice): bylaw amendment process (below) allows member
    #   input via annual meeting.
    # Principle 4 (monitoring): mandatory session sign-in + supervisor observation.
    # Principle 5 (graduated sanctions): documented above.
    # Principle 6 (conflict resolution): facility-committee mechanism above.
    # Principle 7 (nested enterprises): facility committee nested within town
    #   arts-council or library board governance structure.
    # Principle 8 (external recognition): municipal ownership + town-budget line
    #   provides external recognition and institutional legitimacy.

    member_amendment_process: >-
      2/3 vote of active members at the annual facility-review meeting (held
      concurrently with the town arts council or library board annual meeting);
      30-day advance notice required for bylaw amendments. Emergency safety-related
      rule changes may be enacted by the facility committee with 7-day notice and
      ratified at the next member meeting. Town board retains override authority
      on budget-related rules.

    legal_form: >-
      Municipal operation under town government authority (not a separately registered
      cooperative entity). The member-access model is layered on civic ownership: the
      town holds title and operational authority; the facility committee provides
      member-facing governance. Ostrom Principle 7 is satisfied by nesting into
      municipal governance; Principle 8 is satisfied by the town-budget line and
      public-record accountability.

    scale_fit_note: >-
      Governance rules calibrated for town scale (2,000–15,000 residents). Minimum
      viable membership approximately 20–30 active users to fill 30 hr/wk shift
      slots across 4–6 looms. At village scale, scheduling demand and quorum for the
      annual member meeting both become problematic. At small-city scale, rules
      transfer directly; additional staff or a second shift may be added without
      governance restructuring.

  civic:
    political_coalition: >-
      Library board (operational home; aligns with library-model open-access
      philosophy); arts council (cultural programming mandate; grant-application
      capacity); workforce-development board (textile-skills training pipeline;
      grant alignment); occupational therapy programs and regional hospital
      rehabilitation departments (therapeutic weaving partnership; health-system
      endorsement is a strong civic legitimacy signal). Secondary coalition partners:
      K-12 school district (textile arts curriculum partnership); heritage and cultural
      preservation groups (traditional weaving practices). Anti-opposition signal:
      endorsement from local or regional weaving guild as quality-and-curriculum validator.

    council_vote_estimate: >-
      5-2 favorable in arts-supportive, workforce-development-minded town councils
      where library-model civic services have established precedent. 4-3 marginal in
      conservative budget climates where the capital ask ($65,000 mid + $8,000 install)
      triggers fiscal-responsibility opposition. Primary opposition argument: "this is
      a hobby subsidy, not essential infrastructure" — countered by the therapeutic
      weaving partnership (health system endorsement), apprenticeship pipeline
      (workforce development), and per-household cost benchmark (well within arts
      and recreation civic service range). Swing vote typically responds to the
      OT-partnership framing, which reframes fiber arts as a health-outcomes investment.

    competes_with_private: >-
      The community fiber arts center is structurally complementary to, not competitive
      with, private weaving studios and yarn shops. The facility does not sell woven
      cloth commercially, does not compete for commission work, and explicitly refers
      commercial weaving clients to private studio operators. Its apprenticeship and
      instruction pipeline directly supplies potential customers and students to
      private yarn retailers and studio operators. In towns where no private studio
      exists (the more common case at town scale), the civic center fills an access
      gap the market has declined to provide. In towns where a private studio does
      operate, the civic center trains that studio's future students and handles
      beginner instruction that a boutique studio cannot economically offer at low cost.

    governance_form: >-
      Town-owned; operated under the town arts council, library system, or
      parks-and-recreation department (whichever has existing facility-management
      capacity and strongest alignment with the cultural-programming mandate).
      Journeyman-weaver supervisor is a town employee or long-term contractor with
      a defined instruction and community-programming mandate. Facility committee
      (3–5 members, appointed by the parent department head) sets operating policy
      within town-approved bylaws. Annual budget reviewed by town council. OT
      partnership formalized via a memorandum of understanding with the health
      system or regional hospital.

    budget_line: >-
      Capital: one-time appropriation or 20–25 year general-obligation bond (~$2,600–3,250/yr
      amortized at mid-capital + install cost of $73,000 over 25 yr). Operating:
      ~$75,800/yr covering staffing ($52,000 FT journeyman-weaver supervisor + $13,000 PT
      assistant-instructor at 20 hr/wk = $65,000 total labor), maintenance ($3,500),
      consumables ($4,800), administration (~$2,500). Member fee revenue (~$4,000–8,000/yr
      at 80–150 active members) and arts-council/workforce-development grants
      (~$8,000–15,000/yr) reduce net municipal cost to approximately $55,000–63,000/yr.
      Budget line: arts-and-culture programming or parks-and-recreation capital and
      operating accounts. [CITATION-NEEDED: arts and workforce-development grant
      availability and typical award amounts for civic fiber arts programs]

    benchmark_comparison: >-
      At town scale (5,000 households as representative mid-point), gross operating cost
      of ~$75,800/yr ÷ 5,000 hh ≈ $15.16/hh/yr; net municipal cost after member fees
      and grants (~$55,000–63,000/yr) ≈ $11–12.60/hh/yr. Amortized capital adds
      ~$0.52/hh/yr (25-yr bond on $73,000 mid-capital + install). All-in municipal
      cost: ~$11.50–13.10/hh/yr.
      Benchmark: per SCALES.md §3, town library operating cost typically $35–65/hh/yr;
      town recreation center $45–80/hh/yr [CITATION-NEEDED: SCALES.md library/rec-center
      benchmark data]; typical town arts-programming line $5–20/hh/yr. The community
      fiber arts center at ~$11.50–13.10/hh/yr is consistent with the upper bound of
      arts programming and well below library and rec-center benchmarks — politically
      defensible on the existing civic service cost continuum.

    staffing_model:
      role: "1 FT journeyman-weaver supervisor (town employee or contractor) + 1 PT assistant-instructor (20 hr/wk)"
      operator_fte: 1.5
      # 1.0 FT journeyman-weaver + 0.5 FTE assistant-instructor (20 hr/wk).
      # The assistant-instructor role can be filled by an advanced member on a
      # paid part-time basis or a senior apprentice in the Stage 3–4 cohort.
      wage_assumption: 52000
      # Journeyman-weaver supervisor: $52,000/yr. Assistant-instructor:
      # $15–16/hr × 20 hr/wk × 50 wk = ~$15,500/yr; aggregate labor $67,500/yr.
      # wage_assumption reflects the primary supervisory role.
      wage_source: "corpus/program/SCALES.md §3 town-scale skilled-trades median; journeyman-weaver wage calibrated to skilled-artisan tier below master-weaver ceiling"
      hours: "40 hr/wk (supervisor: open-studio supervision, instruction, curriculum planning, administrative); 20 hr/wk (assistant: session coverage, beginner instruction, loom maintenance support)"
      hiring_notes: >-
        Journeyman-weaver supervisor requires full floor-loom competency, dye-chemistry
        knowledge, and demonstrable adult-education ability; hiring radius likely 150–200
        miles. The pool is larger than master-weaver entries but still thin nationally.
        $52,000/yr is at the lower bound of what a qualified journeyman-weaver with
        instruction experience will accept in most US regions [CITATION-NEEDED: regional
        textile-arts instructor wage survey]. OT partnership sessions require basic
        familiarity with therapeutic-weaving protocols; initial training for the supervisor
        can be provided by the partner OT program at low cost. Part-time assistant hire
        pool is broader; Stage 3–4 apprentices and community college textile graduates
        are viable sources.

    civic_externalities:
      - "Textile education pipeline: structured 36-month apprenticeship program produces journeyman-level weavers who can operate independent studios, teach community workshops, or supply regional occupational-therapy programs with qualified fiber arts instructors — an intergenerational knowledge-preservation externality the market systematically under-provides at town scale"
      - "Therapeutic weaving access: occupational-therapy partnership enables fine-motor rehabilitation, anxiety reduction, and social engagement programming for stroke recovery patients, veterans, and neurodiverse adults; a documented clinical modality [CITATION-NEEDED: OT therapeutic weaving outcomes literature] that is cost-prohibitive in private clinical settings but feasible as a civic facility add-on"
      - "Community gathering and social cohesion: multi-loom open-studio model creates a structured creative gathering space that reduces social isolation — a public-health externality that is well-documented for community craft programs but not priced by market studios charging per-session fees"
      - "Cultural preservation: the facility maintains active knowledge of traditional weaving structures (overshot, M's and O's, coverlet patterns, regional fiber traditions) that would otherwise erode as master practitioners age without successors; civic institutional continuity is the only reliable preservation mechanism at town scale"
      - "Apprenticeship to skilled trades: the training pipeline supplies journeyman weavers to the surrounding region, including potential instructors for other civic programs, private studio operators, and textile-arts educators; functions as a workforce-development subsidy to institutions that cannot afford internal apprentice programs"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 65000
  # Equals economics.capital_cost.mid per E3-R1.

  cost_sd: 20000
  # (high − low) / 4 = (110,000 − 30,000) / 4 = 20,000.
  # cost_sd / cost_mean = 20,000 / 65,000 = 0.308; within 0.15–0.50 acceptable
  # range per E3-R5.

  throughput_units_equiv_per_year: 1200
  # Derivation (stated per weaving SCHEMA.md §1 E-3 guidance):
  # Derated active hours: 30 hr/wk − (35 min/day × 5 days / 60) = 27.1 hr/wk net.
  # Effective hours/yr: 27.1 × 52 × (1 − 0.13) = 27.1 × 52 × 0.87 ≈ 1,224 hr/yr.
  # Throughput rate: ~1.0 m/hr facility-wide (blended across floor looms and
  # rigid-heddle stations at mixed skill levels; 50% of hours are instruction/
  # open-studio where weaving rate is lower than pure production).
  # Annual throughput: 1,224 hr × ~0.98 m/hr ≈ 1,200 m/yr.
  # Unit = 1 linear meter of woven cloth equivalent (stated per Key Assumptions).

  variable_cost_per_unit: 4.00
  # Direct variable cost per meter-equivalent:
  # annual_consumables ($4,800) / throughput_units_equiv_per_year (1,200) = $4.00/m.
  # This reflects per-unit material consumption (heddle wear, dye material, yarn
  # samples) allocated proportionally to throughput. Fixed-proportion consumables
  # (HVAC filters, safety supplies) are included in annual_maintenance, not here.

  labor_hours_per_unit: 1.02
  # Effective hours/yr (1,224) ÷ throughput_units_equiv_per_year (1,200) ≈ 1.02.
  # Reflects total supervised labor-hours per output-equivalent meter including
  # instruction and supervision overhead — consistent with E3-R3.

  downtime_fraction: 0.13
  # Sources: multi-user scheduling gaps and no-shows (~4%), equipment maintenance
  # and first-year failure events (~5%), civic administrative overhead (public
  # holidays, staff absence, facility inspections, OT-program setup sessions) (~4%).
  # Total 13%. Consistent with operations_reality first_year_failures profile:
  # humidifier failure (7-day lead time at ~2,500 hr to failure = year 1.6 under
  # 30 hr/wk; contributes ~2% downtime in first operating year).

  lifespan_years: 25
  # Standard civic infrastructure amortization horizon. Floor-loom-4shaft units
  # with regular maintenance have a 20–40 year service life [CITATION-NEEDED:
  # floor-loom manufacturer expected lifespan]; 25 years is the conservative
  # planning horizon and aligns with a municipal general-obligation bond term.

  usage_rate_threshold: 0.15
  # Specialized civic facility lower threshold, per ECONOMIC-LENSES.md §4.3
  # (specialized-equipment exception): a supervised fiber-arts studio cannot
  # achieve open-access utilization rates of a library or recreation center.
  # The concurrent-user ceiling is ~5 (1 supervisor + 4 members); the facility
  # cannot simultaneously serve more users regardless of scheduling pressure.
  # At 7,800 person-hours/yr and town scale (8,500 residents, ~3,400 hh):
  # 7,800 / 8,500 ≈ 0.918 hr/capita/yr — meaningful civic access above the
  # 0.15 hr/capita/yr specialized-facility threshold. Per-household cost (~$13/hh
  # gross at town scale) is well below the $100 threshold. Same threshold
  # rationale as forge-004 civic precedent.

  amortization_years: 30
  # ECONOMIC-LENSES.md §4.1 default: 30 years. Appropriate for civic infrastructure
  # with a 25-year municipal bond term; standard for town-owned facilities.

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: fail
    primary_metric: -1.0
    metric_name: payback_years
    notes: market_price_per_unit absent or zero; entry not designed for market lens
  village_coop:
    verdict: fail
    primary_metric: 57.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=57, total_annual_cost=11220
  village_civic:
    verdict: fail
    primary_metric: 21.46666666666667
    metric_name: per_household_cost
    notes: per_hh=21.47, threshold=120, hrs/capita=0.000 vs threshold=0.15
  town_market:
    verdict: fail
    primary_metric: -1.0
    metric_name: payback_years
    notes: market_price_per_unit absent or zero; entry not designed for market lens
  town_coop:
    verdict: win
    primary_metric: 57.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=57, total_annual_cost=11220
  town_civic:
    verdict: fail
    primary_metric: 3.1568627450980395
    metric_name: per_household_cost
    notes: per_hh=3.16, threshold=100, hrs/capita=0.000 vs threshold=0.15
  small_city_market:
    verdict: fail
    primary_metric: -1.0
    metric_name: payback_years
    notes: market_price_per_unit absent or zero; entry not designed for market lens
  small_city_coop:
    verdict: win
    primary_metric: 57.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=57, total_annual_cost=11220
  small_city_civic:
    verdict: fail
    primary_metric: 0.5962962962962963
    metric_name: per_household_cost
    notes: per_hh=0.60, threshold=80, hrs/capita=0.000 vs threshold=0.15
sources:
  - ref: "corpus/program/SCALES.md §3 — town-scale skilled-trades median wage and civic facility per-household cost benchmarks"
  - ref: "Ostrom, Elinor. 1990. Governing the Commons. Cambridge University Press — design principles for cooperative and commons governance"
  - ref: "Chandler, Deborah. 1995 (rev. 2009). Learning to Weave. Interweave Press — floor-loom throughput ranges, warping overhead time estimates, and loom operation fundamentals"
  - ref: "Ostergaard, Jens. 1990. Rigid Heddle Weaving. Interweave Press — rigid-heddle loom throughput and beginner-instruction parameters"
  - ref: "[CITATION-NEEDED: floor-loom-4shaft capital cost — equipment retailer pricing (Schacht Spindle Co., AVL Looms, Leclerc Industries) for mid-grade 4-shaft studio looms, 2024–2025]"
  - ref: "[CITATION-NEEDED: multi-loom civic facility consumables estimate — no published benchmark identified; derived from per-item pricing in weaving supply catalogs (Yarn Barn, WEBS, The Woolery)]"
  - ref: "[CITATION-NEEDED: commercial plain-weave cotton cloth wholesale price per meter, US domestic market 2024–2025 — industrial baseline for civic-subsidy reference]"
  - ref: "[CITATION-NEEDED: floor-loom noise level measurement at operator position — acoustic survey or practitioner measurement; range estimated from weaving literature]"
  - ref: "[CITATION-NEEDED: floor-loom expected service life — manufacturer documentation or fiber arts center operating records; 25-year conservative estimate used]"
  - ref: "[CITATION-NEEDED: town library and rec-center per-household annual operating cost — SCALES.md §3 benchmark data; $35-65/hh/yr library and $45-80/hh/yr rec-center ranges require confirmation]"
  - ref: "[CITATION-NEEDED: arts-council and workforce-development grant availability for civic fiber arts programs — typical award amounts; no published survey identified at authoring date]"
  - ref: "[CITATION-NEEDED: occupational therapy therapeutic weaving clinical outcomes — peer-reviewed OT literature on fine-motor and psychosocial outcomes of fiber arts programs in rehabilitation settings]"
  - ref: "[CITATION-NEEDED: journeyman-weaver instructor wage survey — regional textile-arts instructor compensation data; $52,000/yr town-scale estimate requires confirmation]"
  - ref: "Jacobs, Jane. 1961. The Death and Life of Great American Cities. Random House — civic infrastructure as neighborhood social-capital anchor; public-goods framing for non-commercial community services"
  - ref: "Danish Folk High School Movement (Grundtvig tradition) — functional precedent for community skills education in civic institutional form; see Historical Lineage for anti-romantic treatment [CITATION-NEEDED: primary academic source on folkhøjskole textile tradition]"
---
## Summary

The Community Fiber Arts Center (weave-010) is a town-owned supervised multi-loom workshop designed on the library model of civic access: residents book sessions, work under qualified supervision on their own projects or through structured instruction, and pay a modest annual fee rather than per-session commercial rates. The facility houses four floor-loom-4shaft units as its primary production equipment, supplemented by rigid-heddle stations for beginners, a dyeing alcove, and warping infrastructure. It is staffed by a journeyman-weaver supervisor with an optional part-time assistant-instructor. The facility targets town and small-city scale and is viable under both cooperative and civic lenses; market lens is poor because the facility does not produce for commercial sale. The primary civic justification is fourfold: textile education and apprenticeship, therapeutic weaving access (occupational-therapy partnership), community gathering as a documented social-cohesion mechanism, and cultural preservation of traditional weaving knowledge. weave-010 is the fiber arts analog of forge-004 (Community Civic Makerspace), purpose-built to model the civic public-goods case for a fiber arts facility that no cooperative or market-lens entry addresses.

## Design rationale

This entry solves a problem that no other entry in the weaving catalog solves: it models the civic investment case for a supervised multi-loom open-studio in terms of staffing economics, Ostrom governance, political coalition, and public-goods externalities, rather than as a commercial or cooperative production analysis. The existing catalog covers luxury/specialty studios (weave-001 through weave-005) and heritage/cultural entries (weave-006 through weave-008); none models the civic-commons form where the facility exists to produce public access and skill transmission, not commercial output. The therapeutic-weaving partnership angle is the design's distinctive element: it reframes the facility as health infrastructure rather than purely a cultural amenity, which changes the political coalition (adds the health system as a stakeholder) and the civic-externality argument (adds documented clinical outcomes to the public-goods case). This is not decorative — it is the mechanism by which a fiber arts center can credibly argue for civic investment in towns where "arts subsidy" arguments alone face opposition. The multi-loom shared configuration (floor looms + rigid heddles together in one supervised space) is also a deliberate design choice: it creates a skill continuum that serves beginners (rigid-heddle, low barrier) through advanced practitioners (floor loom, overshot patterns) in a single civic footprint, maximizing access breadth per square meter and per dollar of staffing cost. A facility housing only floor looms would serve fewer residents; a facility housing only rigid-heddle stations would not serve the skilled end of the demand curve that makes the apprenticeship pipeline viable.

## Historical lineage

Three precedents inform this design.

**Danish folkhøjskole textile tradition.** The Danish folk high school movement (founded by N.F.S. Grundtvig, 1844) developed a civic model of non-credentialed adult skills education housed in purpose-built community facilities. Textile weaving was a core subject in many rural folkhøjskole programs throughout the late 19th and early 20th centuries, taught in shared workshop spaces with instructor-led open-studio sessions that combined technical instruction with community gathering. The functional inheritance is real: the open-studio model, the instructor-as-facilitator role (not a producer), and the civic-subsidy-for-skills-education framing all derive from this tradition. What the design cannot reproduce: the folkhøjskole operated within a strong state-subsidy framework (Danish Folk High School Act provides ~65% public funding for operating costs [CITATION-NEEDED: Danish Folk High School Act funding provisions]) and a high-trust social fabric specific to Danish cooperative culture. The governance form and subsidy level must be adapted to US municipal institutional capacity, not imported wholesale. The training model and civic-access philosophy are the inheritance; the funding structure is not.

**US public library model (library-card access, Jane Jacobs civic-infrastructure framing).** The library-model access structure — annual membership fee, scheduled sessions, publicly funded capital and operations — is directly inherited from the US public library tradition. Jane Jacobs's argument (*The Death and Life of Great American Cities*, 1961) that civic infrastructure generates social capital and neighborhood resilience that the market systematically under-provides supplies the theoretical frame for the civic_externalities block. The functional inheritance is: zero-per-session pricing, civic ownership, public-goods justification, and political legitimacy via institutional precedent. What the fiber arts center does not inherit from the library model is the possibility of unstaffed or self-service operation: a loom studio requires qualified supervision for safety, quality, and skill transmission in ways that a book collection does not.

**New England weaving guild cooperative (20th-century revival).** New England weaving guilds (Connecticut Guild of Craftsmen, Weavers Guild of Greater Boston, etc.) demonstrated in the mid-to-late 20th century that shared-loom studio facilities could be operated on a membership-dues model in community spaces, with member-volunteers providing instruction and equipment maintenance. The functional inheritance is the scheduling model (sign-up for loom time), the skill-tier access policy (beginner must complete orientation before floor-loom booking), and the instruction-integrated-with-production operating mode. What the design does not inherit from the guild model is voluntary-labor dependence: the civic center employs a paid journeyman-weaver supervisor rather than relying on volunteer instructors, because the civic model must be institutionally reliable rather than dependent on volunteer continuity.

## Key assumptions

**Capital cost ($30,000–$110,000, mid $65,000):** No published benchmark for a civic fiber arts center of this configuration was identified at authoring date. The estimate is derived from equipment pricing: floor-loom-4shaft units at $2,500–$4,500 each (mid-grade new; Schacht Wolf Loom or equivalent) × 4 looms = $10,000–$18,000; rigid-heddle stations at $200–$400 each × 3 = $600–$1,200; dyeing alcove equipment (stainless vats, electric burners, mordant stock) = $1,500–$4,000; humidity-control system (residential/commercial humidifier-dehumidifier) = $1,500–$8,000; studio fit-out (lighting, shelving, warping boards, yarn winder, drum carder, signage) = $3,000–$10,000; plus a civic-facility overhead multiplier for accessibility compliance, permitting, and institutional procurement. The mid estimate ($65,000) reflects a four-loom studio with commercial humidity management and a complete dye setup. The range is wide because loom quality and humidity-control scope vary substantially. All equipment cost figures flagged [CITATION-NEEDED] and should be replaced with actual procurement quotes before status promotion.

**Staffing ($52,000 journeyman-weaver + ~$15,500 PT assistant):** Derived from corpus/program/SCALES.md §3 town-scale skilled-trades median wage for the skilled-artisan tier. The $52,000 figure is at the lower bound of what a qualified journeyman-weaver with instruction experience will accept; the assumption is contested. The pool for a town-scale instructor with floor-loom, dye, and adult-education competency is thin nationally; hiring radius of 150–200 miles is realistic.

**Throughput units equivalent (1,200 m/yr):** Derived from derated active hours (1,224 hr/yr) at a blended 1.0 m/hr facility-wide rate. The 1.0 m/hr figure is conservative: it reflects the fact that 50% of session time is instruction/open-studio at reduced throughput (novice members, loom setup assistance, beginning-of-session orientation). The 1.0 m/hr blended rate is an authorial estimate; measured throughput data from comparable civic fiber arts facilities would be needed for validation. The "unit" is stated as 1 linear meter of woven cloth equivalent throughout; sim_params is internally consistent with this definition.

**Downtime fraction (0.13):** Estimated for the multi-user civic context. The humidifier failure at ~2,500 hours (year 1.6 at 30 hr/wk) is the dominant first-year downtime risk at 7 days lead time. Scheduling gaps, administrative overhead, and public holidays contribute the remainder. A 13% downtime is slightly lower than the forge-004 civic precedent (15%) because fiber arts looms have fewer high-consequence failure modes than induction forge equipment and the safety-gating overhead is lighter.

**Per-household cost (~$13/hh/yr gross):** The benchmark_comparison calculation uses 5,000 households as a representative mid-town figure. The net figure is sensitive to grant-funding assumptions [CITATION-NEEDED]; without grants, gross cost rises to ~$15.16/hh/yr — still within the arts-programming civic service range. The calculation is transparent in the civic block and should be updated with actual town demographic data at implementation.

## Known risks / failure modes

**Regulatory.** The primary regulatory exposure is the dyeing alcove: natural mordant effluent (iron sulfate, tannin, alum, vinegar) must be pH-adjusted before drain discharge in most municipal sewer jurisdictions; some jurisdictions require hauled disposal regardless of concentration. Failure to obtain prior clearance from the local publicly owned treatment works (POTW) can shut down the dye program post-opening with significant remediation cost. A secondary regulatory risk is the OT-partnership agreement: occupational-therapy sessions involving clinical outcomes may require the facility to carry professional-liability coverage beyond standard municipal parks-and-rec insurance; town counsel review is required before the OT program launches. Building mechanical permits for the humidity-control HVAC system are routine but require advance coordination if the selected building lacks an existing adequate mechanical system.

**Labour pipeline.** The journeyman-weaver supervisor position is the single point of failure for the facility's quality, instruction, and safety function. At $52,000/yr, the position competes with community-college textile instructor salaries and private studio income; voluntary departure risk is non-trivial. The apprentice pipeline provides long-run mitigation (36-month horizon to produce a Stage 4 candidate) but no short-term succession protection. The OT-partnership sessions create an additional skill dependency: if the supervisor lacks therapeutic-weaving orientation, the OT program cannot operate. Initial OT training for the supervisor should be formalized in the launch plan rather than treated as an assumption.

**Supply chain.** The facility's supply chains are substantially less fragile than market-lens fiber entries because it uses industrial-yarn-purchased fiber: standard commercial yarn from regional distributors has short lead times and multiple substitutable suppliers. The meaningful supply-chain risk is specialized loom parts: warp-beam hardware for older or non-standard floor-loom models may have limited US distributor networks; a 30-day worst-case lead time for specialty parts is realistic and requires a modest safety stock policy for critical components (ratchet springs, heddle sets, replacement reeds). The humidity-control system is a secondary supply-chain concern: commercial HVAC components with 7-day residential lead times can stretch to 21+ days for commercial equipment or uncommon system configurations; a documented backup plan (portable humidifier as temporary measure) should be part of the facility's operational continuity plan.

## Iteration log

- 2026-04-18: v0.1 — initial creation; weave-010 Community Fiber Arts Center. CIVIC-PRIMARY / COOPERATIVE-GOOD entry per Plan I Task 12 specification. All three lens_context blocks populated (market poor with industrial_baseline cited for reference; cooperative good with all Ostrom principles 1–8 addressed; civic good as co-primary lens with staffing_model, benchmark_comparison, five civic_externalities, therapeutic-weaving partnership, and apprentice_path). `annual_public_use_hours` and `usage_rate_threshold` placed in `trade_specific` block per forge-004 civic precedent. Fifteen [CITATION-NEEDED] flags placed over fabricated estimates for capital cost, consumables, wages, energy rates, OT outcomes literature, and historical lineage sources. Anti-romantic treatment applied to Danish folkhøjskole and New England guild-cooperative precedents.
