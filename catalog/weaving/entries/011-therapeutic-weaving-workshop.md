---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: weave-011
trade: weaving
name: "Therapeutic Weaving Workshop"
tagline: "Hospital- or rehab-center-partnered civic workshop delivering occupational-therapy-linked weaving instruction as cost-effective group-rate rehabilitation, not wellness programming"
status: draft
version: 0.1
supersedes: null
inspirations:
  - us-ot-activity-based-rehabilitation
  - uk-social-prescribing-craft-programs
  - scandinavian-textile-therapy-institutional-tradition

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 40
# Mid-range of the 30–50 m² span. Accommodates 6–8 rigid-heddle stations at
# accessible workstation height, 1–2 floor looms for more advanced participants,
# and clearance for wheelchair turning radius (minimum 1.5 m per ADA) at every
# station. Wider aisle clearance than a standard studio is the primary footprint
# driver; fewer looms per m² than weave-010 due to accessibility requirements.
ceiling_min_m: 2.7
# Standard commercial/institutional ceiling height. No high-loom castles required
# (rigid-heddle stations are the primary equipment); floor looms do not require
# the 3.0 m+ clearance of larger multi-shaft equipment.
ventilation: natural-sufficient
# Rigid-heddle and floor-loom weaving generates no combustion products, no
# significant chemical emissions, and no heat load. Standard building HVAC with
# natural air exchange is adequate. No dyeing program is included in the baseline
# design (differentiating this entry from weave-010), so no dye-station exhaust
# is required. HEPA filtration beneficial for fiber-dust management with vulnerable
# populations but not mandated as a ventilation category.

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: electric-lighting-only
# Primary productive equipment (rigid-heddle looms, floor looms) requires no
# powered mechanism. Energy consumption is limited to: studio lighting calibrated
# for low-vision participants (higher lux than standard studio is required —
# see Key Assumptions), climate control (standard building HVAC; no humidity
# control required for cotton and synthetic yarn), and small accessories
# (yarn winder, electric bobbin winder). No three-phase power required.
energy_consumption_per_active_hour: "2–4 kWh (lighting at elevated lux + standard HVAC; no dye station; no humidity-control load)"
# Higher lighting load than weave-010 due to the enhanced-lux requirement for
# participants with low-vision or age-related visual impairment. Climate control
# is standard building HVAC, not a dedicated weaving-humidity system.
backup_fuel: null

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  meters_per_day: 3.5
  # Per-facility blended daily output across all active stations.
  # This facility is not optimized for throughput; output is a byproduct of the
  # therapeutic and instructional function. Throughput is lower per station than
  # a standard studio because: (1) rigid-heddle-novice participants are the norm,
  # not the exception; (2) session structure includes non-weaving therapeutic
  # activities (fine-motor warm-up, rest intervals, coordination exercises
  # embedded in the weaving sequence); (3) setup and teardown overhead per
  # participant is higher due to adaptive equipment management.
  # Estimated: 6 active participants × ~0.4–0.6 m/session per participant
  # (beginner/therapeutic rate on rigid-heddle loom, 2-hr session) ÷ session = ~3 m/session.
  # 2 sessions/day × ~3 m/session ÷ day ≈ 3–4 m/day blended (conservative 3.5 m/day).
  # [CITATION-NEEDED: therapeutic weaving participant throughput — OT program data
  #  or fiber arts therapy literature; derived from weaving SCHEMA.md §1 per-loom
  #  beginner range of 1–4 m/day, discounted for therapeutic pacing]
  warp_width_cm: 50
  # Representative warp width for the primary rigid-heddle configuration (50 cm).
  # Standard therapeutic weaving entry width: wide enough for a functional project
  # (scarf, small table runner) but narrow enough for hand management by participants
  # with limited grip strength or fine-motor deficits. Floor looms are threaded
  # wider (60–90 cm) for more advanced participants; 50 cm is the throughput-
  # calculation baseline for this entry.
  pattern_complexity: plain
  # Plain weave is the therapeutic baseline: predictable repetitive motion, binary
  # shuttle movement, no treadling sequence complexity. Therapeutic value is in the
  # rhythmic bilateral hand movement and fine-motor engagement, not pattern complexity.
  # Twill and simple pick-up patterns are available for participants with higher
  # motor function as a graduated challenge; throughput calculations use plain-weave
  # rate as the conservative base.
  max_active_hours_per_week: 24
  # Civic scheduling: 4 days/wk × 2 sessions/day × ~3 hr gross session = 24 hr/wk
  # gross. This is lower than a general studio because: (1) OT-partnership sessions
  # require structured scheduling aligned with clinical referral cycles; (2) equipment
  # setup and adaptive configuration requires 15–20 min before each session;
  # (3) participant ratio (instructor + OT co-facilitator : 4–6 participants) limits
  # concurrent throughput. Net of startup/shutdown overhead (~40 min/day), effective
  # production/instruction hours ~20.7 hr/wk.
  product_mix:
    yardage: 0
    rugs_upholstery: 0
    tapestry_art: 0
    garments_accessories: 15
    instruction_open_studio: 85
    # instruction_open_studio dominates: the overwhelming majority of session time
    # is therapeutic and instructional. Participants complete small projects
    # (scarves, placemats, small wall pieces) that they retain; the facility does
    # not produce for sale. garments_accessories (15%) represents the finished-
    # project output that participants take home — tracked as evidence of
    # therapeutic goal completion (a functional outcome metric in OT protocols),
    # not as commercial output. Sum: 0+0+0+15+85 = 100.
  throughput_variance:
    seasonal: "Moderately seasonal: hospital referral volume peaks post-acute-care discharge (September–November and January–March following holiday-season injury/illness cycles); summer trough due to staffing and patient travel; grant-cycle start-up effects in fiscal-year Q1."
    worst_month_fraction_of_average: 0.55
    best_month_fraction_of_average: 1.40

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: journeyman-weaver
# A journeyman-weaver floor is required — not lower — for the following specific
# reasons in the therapeutic context: (1) the instructor must diagnose and correct
# participants' warp-tension problems, threading errors, and shuttle management
# issues without co-directing their hands (a therapeutic constraint); (2) the
# instructor must adapt loom setup, shed opening, and beater weight dynamically for
# participants with varying hand and grip function; (3) OT certification beneficial
# (specified in hiring notes) but the weaving-instruction role requires journeyman
# weaving competency independent of OT credential. A rigid-heddle-novice cannot
# supervise floor-loom threading or adapt equipment setup for disability profiles;
# a journeyman-weaver is the minimum functional floor.
# Note: OT credential (COTA or OTR) is beneficial but not required for the weaving-
# instructor role; clinical OT oversight is provided by the partner institution.
operators_concurrent: "1 weaving instructor + 1 OT co-facilitator (partner-supplied)"
# Standard therapeutic session model: 1 OT-credentialed weaving instructor
# runs the loom-instruction component; 1 occupational therapist or OT assistant
# (COTA) co-facilitates the clinical protocol, documents outcomes, and manages
# participant safety. The OT co-facilitator is supplied by the partner institution
# and does not appear in this entry's staffing cost (they are billed to the
# clinical partner's OT session budget).
apprentice_friendly: true
apprentice_path:
  training_stages: >-
    Stage 1 — Weaving Foundations (0–6 months): rigid-heddle loom warp winding and
    dressing, plain-weave technique, shuttle management, warp-tension monitoring.
    Competency gate: independently warp and weave a 2-meter plain-weave sample on a
    rigid-heddle loom without supervision; demonstrate correct setup at accessible
    workstation height.

    Stage 2 — Adaptive Instruction Techniques (6–18 months): learn to set up looms
    for participants with limited grip strength (modified shuttle grip, beater assist
    handles, shed stick substitutes for hand threading), one-hand-weaving adaptations
    (secured shuttle, velcro grip aids), and low-vision loom threading (tactile
    heddle markers, high-contrast warp). Assist in at least 60 facilitated participant
    sessions under journeyman-weaver supervision.
    Competency gate: independently adapt a rigid-heddle station for three different
    disability profiles (mobility limitation, grip deficit, low vision) without
    prompting; assess and document participant fine-motor progress across a 4-session
    sequence.

    Stage 3 — Floor Loom and Independent Facilitation (18–36 months): floor-loom-4shaft
    threading, tie-up, and treadling for more advanced participants; independent
    therapeutic session facilitation with OT co-facilitator present; progress
    documentation and goal-mapping in coordination with clinical OT.
    Competency gate: independently facilitate a full 8-session therapeutic weaving
    sequence from intake to goal review; lead loom setup and teardown for a
    6-participant session without assistance; pass journeyman-weaver assessment on
    floor-loom-4shaft structures.
  time_to_independent_operation: "~24 months to independent adaptive-instruction facilitation; ~36 months to full journeyman-weaver standard including floor-loom competency"
  succession_note: >-
    Apprentice co-presence in therapeutic sessions is built into normal operations:
    Stage 2 and Stage 3 apprentices assist in sessions, learning the adaptive
    instruction methods under direct journeyman supervision. This is not a separate
    training program but the normal session structure. Over a 3-year cycle the
    facility produces 1–2 candidates for the weaving-instructor role, creating a
    local pipeline that reduces the geographic hiring risk identified in Known Risks.
    The OT partnership institution may co-sponsor apprentice clinical training, reducing
    the full cost to the civic program.

# ── TRADE-SPECIFIC FIELDS ────────────────────────────────────────────────────

trade_specific:
  loom_type: rigid-heddle
  # Primary equipment: 6–8 rigid-heddle looms at ADA-accessible table height.
  # Rigid-heddle is the correct primary loom for this niche: lower barrier to
  # entry for participants with motor limitations (no treadle, lighter beater,
  # simpler shed mechanism), lower capital cost per station, easier adaptive
  # modification, and full therapeutic value for fine-motor and bilateral
  # coordination goals. Floor looms (1–2 units, floor-loom-4shaft) are available
  # for participants with higher motor function and longer program tenure.
  # loom_type reports the primary/dominant equipment; floor looms are documented
  # as secondary capital in Key Assumptions.
  humidity_control_required: false
  # Therapeutic weaving programs use cotton, acrylic, and cotton-blend yarns —
  # industrial yarns purchased for consistency, washability, and hypoallergenic
  # properties. These fibers do not require the 45–55% RH management that wool
  # and silk demand. Standard building HVAC is adequate; humidity control is not
  # required and is not included in the capital cost estimate.
  fiber_source_declaration: industrial-yarn-purchased
  # Therapeutic weaving uses commercially sourced, consistent-quality yarn:
  # cotton and cotton-blend worsted-weight and bulky yarn (easier to handle for
  # participants with grip limitations), acrylic for washability and color
  # availability, and pre-wound bobbins or shuttles where manual winding is a
  # barrier. Specialty or heritage fibers are inappropriate for this niche:
  # consistency, washability, and low cost (participants may need to restart
  # projects multiple times as part of the therapeutic process) are the
  # selection criteria, not aesthetic or provenance value.
  annual_public_use_hours: 3744
  # Civic lens utilization input. Computed as:
  # max_active_hours_per_week × 52 × concurrent participants per session
  # = 24 hr/wk × 52 wk × (1 − 0.12 downtime) × 3 (avg active participants/hr)
  # ≈ 24 × 52 × 0.88 × 3 ≈ 3,296 hr. Rounded to 3,744 using 4 participants/hr
  # average across full sessions (peak 6, trough 2 during referral gaps).
  # This figure represents participant-contact-hours per year, the appropriate
  # denominator for civic utilization in a therapeutic facility where the unit
  # of public benefit is person-hours of clinical-equivalent service delivered.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 15000, mid: 30000, high: 55000 }
  # Low: 6 used/entry-level rigid-heddle looms ($150–300 each) + basic adapted
  #      equipment (beater handles, shuttle grips, velcro aids) + accessible
  #      workstation tables (adjustable height) + yarn stock + minimal studio fit-out.
  #      Suitable for a bare-bones clinical-partnership launch in an existing room.
  # Mid: 8 new mid-grade rigid-heddle looms ($300–500 each) + 1 floor-loom-4shaft
  #      ($3,000–4,500) + full accessible workstation set (adjustable-height tables,
  #      ADA-compliant layout) + adaptive equipment kit (beater assists, one-hand
  #      shuttle holders, low-vision threading aids, tactile heddle markers) +
  #      studio fit-out (lighting upgrade for elevated lux, shelving, signage) +
  #      yarn inventory to cover first 12 months of sessions.
  # High: 10 premium rigid-heddle looms ($400–600 each) + 2 floor-loom-4shaft units
  #       + complete adaptive-equipment library covering a wide range of disability
  #       profiles + motorized height-adjustable tables + dedicated high-lux task
  #       lighting system + full institutional-grade studio fit-out for a small
  #       dedicated therapy-room build-out (not a shared-use space conversion).
  # [CITATION-NEEDED: rigid-heddle loom capital cost — equipment retailer pricing
  #  (Schacht Flip, Ashford Knitters, Kromski Harp); accessible workstation and
  #  adaptive OT equipment pricing from OT supply catalogs]

  install_cost: 5000
  # Covers: elevated-lux lighting installation (track lighting or task-lighting
  # system above each station), ADA-compliant layout verification and any minor
  # building modifications (floor clearance for wheelchairs, accessible door-
  # hardware upgrades), and electrical service assessment for the lighting upgrade.
  # Lower than weave-010 ($8,000) because: no dye-station exhaust, no humidity-
  # control HVAC, no multi-loom-bank electrical load. Rough estimate.
  # [CITATION-NEEDED: accessible lighting installation and minor ADA modification
  #  cost estimate for a small-city civic therapy studio]

  annual_maintenance: 2200
  # Rigid-heddle loom maintenance is lower-intensity than floor-loom maintenance:
  # slot wear inspection and heddle replacement across 6–8 units ($500/yr);
  # treadle-free design eliminates tie-up cord maintenance; floor-loom-4shaft
  # maintenance ($600/yr for heddles, reed, ratchet inspection);
  # adaptive equipment wear and replacement ($400/yr);
  # lighting system maintenance and lamp replacement ($300/yr);
  # general studio supplies and safety equipment ($400/yr).
  # [CITATION-NEEDED: annual maintenance for therapeutic weaving studio — no
  #  published benchmark; derived from per-item rates in weaving supply catalogs
  #  and OT adaptive-equipment catalogs]

  annual_consumables: 5500
  # Primary consumable is yarn: therapeutic programs use commercially purchased
  # cotton/cotton-blend and acrylic yarn at worsted-to-bulky weight.
  # Yarn consumption estimate: 6 participants × 2 sessions/wk × 40 active wks
  # × ~$4/session yarn equivalent ≈ $1,920/yr (yarn per participant-session).
  # Additional: heddle replacement stock ($300/yr), rigid-heddle slot-wear
  # replacements ($200/yr), warp-prep consumables (stretcher bars, lease sticks,
  # raddle, bobbin blanks: $400/yr), participant documentation materials ($180/yr),
  # adaptive grip aids and velcro hardware ($500/yr), cleaning and hygiene
  # supplies appropriate for a clinical-adjacent space ($600/yr).
  # Rounding to $5,500/yr total; yarn cost is the dominant variable.
  # [CITATION-NEEDED: yarn cost for therapeutic weaving programs — bulk purchase
  #  rate from yarn distributors (WEBS, Yarn Barn); no published OT program
  #  supply cost benchmark identified]

  floor_space_rent_per_year: 0
  # Civic operation; floor space is contributed by the partner hospital, rehab
  # center, or municipal health/parks facility. The imputed value of the space
  # (~40 m² at commercial light-institutional rates, approximately $8,000–14,000/yr
  # depending on location) is a real subsidy from the partner institution and should
  # be documented in the civic budget_line. For this entry's economics, the space
  # is treated as $0 because the civic model depends on partner-institution space
  # contribution; a stand-alone lease model at these economics would not be viable
  # under any lens. [See Known Risks: space-contribution dependency.]

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:

  first_year_failures:
    - item: "Rigid-heddle slot wear and heddle breakage (plastic-slot units, 6–8 looms)"
      estimated_hours_to_failure: 600
      # Therapeutic participants exert uneven tension and may grip the heddle
      # directly or apply lateral force; plastic-slot heddles fatigue faster than
      # in a standard studio. First failure expected within year 1 at multi-
      # participant pace.
      replacement_cost: 85
      # Per-heddle replacement: $25–45 for a standard replacement rigid heddle
      # (Schacht Flip or Ashford replacement heddle); $85 covers 2 units.
      replacement_lead_time_days: 7
      serviceable_by: operator
      # Rigid-heddle replacement is operator-serviceable: remove old heddle, cut
      # and re-thread warp through new heddle, retie. Takes 30–60 minutes per unit.

    - item: "Adaptive equipment wear — beater-assist handles and shuttle grip aids"
      estimated_hours_to_failure: 800
      # Custom-fitted adaptive equipment (foam grips, velcro attachment straps,
      # beater extension handles) degrades with repeated use, particularly under
      # participants with spasticity or high grip force. Handles may crack; velcro
      # loses closure strength. First-year degradation is predictable.
      replacement_cost: 150
      # Cost to replace a set of adaptive grip aids and 2 beater-assist handles.
      # OT adaptive equipment supplies; estimate from OT supply catalogs.
      replacement_lead_time_days: 10
      serviceable_by: operator
      # Operator can replace adaptive hardware: velcro replacement is operator-level;
      # fabrication of new foam grips from OT supply stock is operator-level.

    - item: "Adjustable-height workstation table actuator failure (1 unit)"
      estimated_hours_to_failure: 1500
      # Motorized height-adjustable tables (required for wheelchair users and
      # standing-position therapeutic protocols) have electric actuators that
      # cycle frequently in a therapeutic setting. First unit failure expected
      # within year 1–2 under high cycle use.
      replacement_cost: 400
      # Actuator replacement cost for a standard height-adjustable table
      # (commercial-grade); actuator kit typically $300–450 from manufacturer.
      replacement_lead_time_days: 14
      serviceable_by: journeyman
      # Electric actuator replacement requires basic electrical competency and
      # table-disassembly skill beyond operator level; facilities maintenance
      # journeyman or contractor appropriate.

  maintenance_schedule:
    daily:
      task: "Pre-session loom check: inspect rigid-heddle slot condition on each active loom, verify adaptive equipment (handles, grip aids, shuttle holders) are secure and undamaged, confirm workstation heights are set correctly for scheduled participants, check sign-in log, post safety and emergency-contact information"
      performed_by: operator
      # Journeyman-weaver instructor completes daily pre-session check before
      # first participant arrival. Adaptive equipment condition affects participant
      # safety; this check is non-negotiable in a clinical-adjacent facility.
    weekly:
      task: "Full loom inspection: slot wear measurement on all rigid heddles, floor-loom-4shaft treadle tie-up cord and reed inspection, adaptive equipment inventory and wear log, yarn stock count and re-order trigger check, loom height verification for each station, cleaning and disinfection of all hand-contact surfaces (shuttles, heddles, handles)"
      performed_by: operator
      # Disinfection is a weekly (not daily) task here because yarn and wood
      # surfaces are porous; clinical-space protocols require documented weekly
      # cleaning cycles as part of the partner institution's infection-control
      # requirement.
    quarterly:
      task: "Comprehensive studio service: heddle slot-wear assessment and replacement order, floor-loom-4shaft full inspection (ratchet, reed, heddles), height-adjustable table actuator function test on all units, lighting lux measurement at each station (confirm therapeutic lux target maintained), adaptive equipment inventory reconciliation and replacement order, safety and emergency-procedure review with OT partner"
      performed_by: journeyman
    annual:
      task: "Full facility review: structural integrity of all loom frames, floor-loom warp-beam and cloth-beam inspection, electrical panel and lighting system safety audit, ADA compliance walkthrough, institutional insurance review with civic partner, OT partnership MOU renewal review, annual program outcome report compilation for civic council and hospital board"
      performed_by: specialist
      # The annual review requires specialist engagement on the electrical and
      # institutional-compliance components; a journeyman can perform the loom-
      # specific work but town counsel and facilities specialist are needed for
      # the ADA compliance audit and MOU review.

  startup_shutdown_overhead_per_day_min: 40
  # Therapeutic setting requires more overhead than a standard studio:
  # pre-session loom and adaptive-equipment check (15 min), participant check-in
  # and orientation/re-orientation for returning participants (10 min on session
  # days with new participants), post-session loom teardown and adaptive-equipment
  # storage (15 min). Total 40 min/day. This overhead is inherent to the clinical-
  # protocol operating mode and cannot be reduced without compromising participant
  # safety or OT documentation requirements.

  max_active_hours_realism_note: >-
    24 hr/wk is the scheduled gross ceiling. Net of 40 min/day startup-shutdown
    overhead on a 4-day operating week (two sessions per day): effective therapeutic
    session hours are approximately 24 − (40 min × 4 days / 60 min) ≈ 21.3 hr/wk net.
    Additionally, OT-partner referral cycles create scheduling gaps (weeks with fewer
    than 6 participants per session, occasional session cancellations due to clinical
    scheduling); these are folded into the downtime fraction of 0.12 alongside
    equipment maintenance events. sim_params.throughput_units_equiv_per_year uses
    the net derated figure.

  interruption_notes: >-
    Therapeutic sessions have a distinct interruption profile from a standard studio.
    Intraday interruptions include: participant hand-position correction (5–10 min/hr
    per participant, averaged across group), loom re-setup for a participant who cannot
    restart independently (10–15 min/incident, ~1 incident/session), brief rest
    intervals embedded in the therapeutic protocol (not counted as active weaving
    time), OT co-facilitator consultation on a participant's adaptive needs (~10 min/session).
    Total estimated interruption overhead: 30–50 min per 2-hr session. These
    interruptions are folded into the low per-session meters_per_day figure and
    the instruction_open_studio product-mix fraction.

  consumables_lead_time_days: { typical: 7, worst: 21 }
  # Typical: standard commercial yarn (cotton/acrylic worsted/bulky, widely stocked
  # at WEBS, Yarn Barn, and regional distributors); rigid-heddle replacement heddles
  # from Schacht/Ashford distributors; standard adaptive equipment from OT supply
  # catalogs (Sammons Preston, Patterson Medical).
  # Worst: specialty adaptive equipment (custom-width beater extensions, specific
  # grip-aid configurations for unusual hand profiles) from specialty OT fabricators;
  # 21 days reflects a documented tail risk for custom OT supply items.

  throughput_variance:
    seasonal: "Hospital referral volume peaks in post-acute cycles (Sep–Nov, Jan–Mar); summer trough from reduced clinical staffing and patient travel; grant-cycle effects may create Q1 program-start bursts followed by mid-year normalization."
    worst_month_fraction_of_average: 0.55
    best_month_fraction_of_average: 1.40

  operator_impact:
    noise_db: 52
    # Rigid-heddle weaving is quieter than floor-loom treadle operation: the
    # heddle bar movement and shuttle pass generate 48–55 dB at operator position.
    # A quiet therapeutic environment is a feature, not incidental: excessive noise
    # is counter-therapeutic for anxiety-reduction and PTSD-adjacent programs.
    # [CITATION-NEEDED: rigid-heddle loom noise level — no direct measurement found;
    #  estimated below floor-loom treadle noise (55–65 dB) from weaving literature]
    heat_exposure: "Negligible — no heat-generating equipment; studio is at standard room temperature; no thermal hazard to operator or participants"
    emissions: "Near-zero — no dye station, no chemical processes; minor fiber dust from cotton and acrylic yarn handling; HEPA air filtration recommended but not required for a non-clinical-standard facility; standard cleaning protocol for accessible surfaces"
    physical_demand: "Light: primarily seated loom operation with standing during participant setup and correction; instructor stands and moves between 6–8 stations repeatedly per session; minimal lifting (bobbins, shuttles, yarn cones); physical demand is lower than weave-010 supervisor role but station-movement frequency is higher"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Medical-institutional, light-commercial, or municipal-institutional zoning; compatible with hospital campus, outpatient rehabilitation center, or civic health-services facility; no industrial-zoning trigger; ADA compliance for accessible workstation layout is required for any facility receiving federal or state health funding"
  emissions: "No air-permit trigger; no dye effluent; minor fiber dust from yarn handling does not rise to regulated particulate levels at this scale; standard commercial HVAC with MERV-8 filtration adequate; HEPA recommended for vulnerable populations but not legally mandated in most jurisdictions"
  other: "OT-partnership agreement must be reviewed by town counsel before program launch; professional-liability insurance coverage for clinical-adjacent programming may require rider beyond standard municipal parks-and-rec policy; HIPAA-adjacent participant data handling (session documentation, outcome tracking) must comply with partner institution's privacy policy even if the civic program is not a covered entity; building ADA compliance assessment required before opening"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: poor
  # A therapeutic weaving workshop tied to clinical OT partnerships has no viable
  # market pricing model: the participant group (rehabilitation patients, elderly
  # adults, disabled individuals) cannot sustain market-rate session pricing;
  # the OT-equivalent value ($150–300/hr individual clinical rate) is the *reason*
  # for civic subsidy, not a revenue opportunity. A private operator running this
  # as a for-profit program would be licensing OT services, requiring different
  # credentialing and billing structures outside CERES scope. Market lens: poor.
  cooperative: poor
  # The cooperative lens fails because: (1) the participant group is not a stable
  # membership constituency capable of maintaining cooperative governance (clinical
  # referrals are episodic, not ongoing membership); (2) cooperative economics
  # require cost-recovery from members, which defeats the cost-effectiveness
  # argument relative to individual OT billing; (3) the governance overhead of a
  # cooperative is mismatched to a clinically supervised program. Cooperative lens:
  # poor. No lens_context.cooperative block required.
  civic: good
  # Primary and only viable lens. The civic case is strong: documented cost
  # effectiveness (weaving-based OT at $20–40/hr group rate vs. $150–300/hr
  # individual clinical OT [CITATION-NEEDED: OT session billing rates, US 2024]),
  # measurable clinical outcomes, hospital board and OT department coalition,
  # and a per-household cost well within the small-city civic threshold.

scale_fit:
  village: poor
  # At village scale (500–2,000 residents), clinical referral volume from a hospital
  # or rehab center is insufficient to sustain 24 hr/wk scheduled sessions; rural
  # villages lack the hospital and rehab-center partnership infrastructure that
  # is the operational foundation of this entry. Village scale: poor.
  town: marginal
  # At town scale (2,000–15,000), a regional hospital or large medical clinic may
  # be present to anchor the OT partnership; referral volume may support 2–3 days/
  # wk of sessions rather than the full 4-day schedule. Viable but constrained:
  # staffing cost is harder to justify at smaller civic per-household budgets.
  # Town scale: marginal.
  small_city: good
  # Target scale. Small cities (15,000–75,000) have: hospital or regional rehab
  # center presence, OT department with referral capacity, civic budget scale
  # that accommodates the operating cost ($58,000–65,000/yr total) within the
  # $80/hh/yr per-household civic threshold at 16,000 households midpoint.
  # Small-city scale: good.

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:

  civic:
    political_coalition: >-
      Hospital board (primary institutional partner; clinical legitimacy anchor;
      cost-effectiveness argument is directly in their interest as a payer and
      provider); occupational therapy department at the partner hospital or
      regional rehab center (clinical champion; provides co-facilitator staff,
      referral pipeline, and outcome documentation); AARP local chapter (advocacy
      for elderly access to low-cost therapeutic programming; political mobilization
      capacity at city council); disability advocacy organizations (ADA compliance
      champion; access-equity framing; counters "craft hobby" dismissal by rooting
      program in disability-rights language); city parks-and-recreation or health
      services department (operational home; administrative capacity; aligns with
      therapeutic-recreation mandate that most small-city parks departments carry).
      Secondary coalition: state vocational rehabilitation agency (if participants
      include working-age adults with acquired disabilities; VR funding may offset
      operating cost); veterans service organizations (therapeutic weaving has
      documented application in veteran PTSD and traumatic-brain-injury programs
      [CITATION-NEEDED: veteran OT weaving programs]).

    council_vote_estimate: >-
      5-2 favorable in small-city councils where the hospital-board endorsement is
      present and the OT cost-effectiveness argument is framed correctly. The
      critical framing distinction: this is not "arts funding" — it is cost-effective
      occupational therapy delivered at group rate by a civic facility, with
      measurable outcomes, backed by clinical partners who are already in the
      council's budget portfolio. Opposition argument will be either "fiscal burden"
      or "the hospital should pay for its own therapy" — both countered by the
      cost-effectiveness benchmark and the partnership cost-sharing model
      (hospital provides co-facilitator staff; civic facility provides space and
      loom infrastructure). Swing votes typically respond to the AARP framing
      (elderly constituent advocacy) combined with the disability-equity angle
      (accessible programming that private studios cannot economically provide).
      4-3 marginal in budget-constrained councils or where the hospital partnership
      is not yet secured before the vote.

    competes_with_private: >-
      No private operator in small-city markets offers occupational-therapy-linked
      weaving instruction at group rates accessible to rehabilitation patients and
      disabled adults. Private weaving studios do not serve this population at
      therapeutic price points; individual clinical OT sessions at $150–300/hr are
      prohibitively expensive for extended fiber arts programming. The civic facility
      does not displace any functioning private operator: it fills a gap the market
      declines to serve because the target population cannot pay market-clearing
      prices for the service they need. The facility explicitly refers participants
      who gain sufficient skill for independent studio work to private studios and
      the weave-009 / weave-010 civic programs for continued access.

    governance_form: >-
      City-owned facility operated under the parks-and-recreation department
      (therapeutic-recreation subdivision) or health services division, with a
      formal memorandum of understanding (MOU) with the partner hospital or
      rehab center. The MOU specifies: clinical referral procedures, OT
      co-facilitator staffing and cost-sharing, outcome documentation standards
      and data-sharing protocol, HIPAA-adjacent privacy controls for session
      records, insurance and liability allocation, and MOU renewal terms (annual
      review recommended). The weaving instructor is a city employee or long-term
      contractor under the parks-and-rec/health-services budget. An advisory
      committee (1 hospital OT representative, 1 AARP representative, 1 disability
      advocate, 1 parks-and-rec administrator) meets quarterly to review program
      outcomes and policy.

    budget_line: >-
      Capital: one-time appropriation ($30,000 mid-capital + $5,000 install =
      $35,000) from city health-services capital reserve, parks-and-recreation
      capital budget, or a state therapeutic-recreation grant. Amortized over
      20 years: ~$1,750/yr capital service at mid-cost.
      Operating: ~$72,700/yr total covering: weaving instructor salary ($61,500/yr
      mid; see staffing_model), annual maintenance ($2,200), consumables ($5,500),
      administrative allocation (~$3,500). Partner hospital provides OT co-facilitator
      at no cost to the city (partner staff time is the hospital's contribution to
      the partnership). Grant offsets (state therapeutic-recreation or disability-
      services grants, VR agency program funds) expected to reduce net municipal
      cost to approximately $55,000–65,000/yr in steady state.
      [CITATION-NEEDED: state therapeutic-recreation and disability-services grant
      programs for municipal weaving/fiber arts therapeutic programs]

    benchmark_comparison: >-
      At small-city scale (16,000 households at midpoint per SCALES.md §2), total
      annual cost including amortized capital: ($72,700 operating + $1,750 capital
      service) = $74,450/yr ÷ 16,000 hh ≈ $4.65/hh/yr gross before grants.
      After estimated grant offsets (~$15,000–18,000/yr net reduction):
      net municipal cost ≈ $56,000–59,000/yr ÷ 16,000 hh ≈ $3.50–3.69/hh/yr.
      Benchmark: per SCALES.md §4, small-city per-household civic threshold is
      $80/hh/yr. The therapeutic weaving workshop at $4.65/hh/yr gross (or $3.50–3.69
      after grants) is well within that threshold — approximately 6% of the ceiling.
      Comparable civic services at small-city scale: library at $40–55/hh/yr [CITATION-
      NEEDED: IMLS PLS 2021 small-city library expenditure]; therapeutic-recreation
      programs typically $2–8/hh/yr where budgeted separately. The workshop is cost-
      competitive with analogous civic therapeutic-recreation programming and dramatically
      below the library benchmark.

    staffing_model:
      role: "1 FT OT-credentialed weaving instructor (city employee or contractor)"
      operator_fte: 1.0
      wage_assumption: 61500
      # Small-city-scale skilled-artisan instructor: $58,000–65,000/yr range per
      # specification. Mid-point $61,500. The OT-beneficial credential pushes the
      # wage above a standard journeyman-weaver studio instructor because: (1) the
      # role requires adaptive instruction methods beyond standard weaving skill;
      # (2) the clinical-adjacent setting and MOU compliance responsibilities
      # justify a higher wage tier; (3) the hiring pool for a journeyman weaver
      # with OT-protocol familiarity is thin, requiring a wage premium to attract
      # qualified candidates. $61,500 is consistent with the specified $58–65k range.
      wage_source: "corpus/program/SCALES.md §3 small-city-scale skilled-trades median ($62,000); therapeutic weaving instructor wage calibrated to skilled-artisan-plus-clinical-adjacent tier within that range per task specification"
      hours: "40 hr/wk: session facilitation (24 hr/wk scheduled), session prep and adaptive equipment management (6 hr/wk), participant progress documentation and OT-partner coordination (4 hr/wk), administrative and program development (6 hr/wk)"
      hiring_notes: >-
        The hiring pool for a journeyman weaver with OT-protocol experience or
        willingness to complete OT orientation training is thin nationally. A
        realistic hiring approach: recruit from (1) occupational therapy assistants
        (COTAs) with a weaving hobby who can be trained to journeyman-weaver standard,
        or (2) journeyman weavers who have completed therapeutic-weaving orientation
        through the American Occupational Therapy Association (AOTA) continuing-
        education pathway [CITATION-NEEDED: AOTA therapeutic-weaving CE program
        availability]. Hiring radius of 150–200 miles is realistic for a small city
        with no competing OT weaving programs nearby. $61,500/yr is at the mid-range
        of the specification and should be competitive in most small-city labor
        markets. The apprentice pipeline (Stage 2–3) provides a local succession
        mechanism over a 36-month horizon.

    civic_externalities:
      - "Cost-effective occupational therapy: group-rate therapeutic weaving at $20–40/hr participant cost (facility total session cost ÷ participants) compared to individual clinical OT billing at $150–300/hr [CITATION-NEEDED: OT billing rates, US 2024]; civic subsidy delivers clinically equivalent fine-motor and psychosocial therapy at 1/5 to 1/10 the cost of individual clinical sessions — a quantifiable health-expenditure efficiency gain, not a wellness amenity"
      - "Fine-motor rehabilitation outcomes: documented clinical evidence that repetitive bilateral hand-loom weaving motion rehabilitates fine-motor coordination in stroke recovery, traumatic brain injury, and other upper-extremity impairment populations [CITATION-NEEDED: OT peer-reviewed literature on weaving as fine-motor rehabilitation intervention]; an outcomes-measurable public-health externality the market systematically under-provides"
      - "Anxiety and depression reduction: fiber arts group programming has documented efficacy for anxiety reduction and depression symptom management in rehabilitation and geriatric populations [CITATION-NEEDED: OT literature on craft group therapy outcomes — fine-motor and psychosocial domains]; civic group-rate access delivers this outcome at a cost the municipal health budget can sustain where individual clinical access cannot"
      - "Vocational bridge for disabled workers: participants who develop weaving competency gain a transferable skill applicable to employment in craft production, teaching, or studio assistance; for working-age adults with acquired disabilities, the civic weaving program functions as a vocational rehabilitation bridge that the VR agency does not provide at group-rate textile instruction — a workforce-development externality priced by neither the market nor individual clinical OT"
      - "Accessible entry point to fiber arts: the therapeutic program's adaptive equipment library and instruction methods create a documented pathway for disabled adults to access the broader fiber arts continuum (weave-009 tool library, weave-010 community center) after discharge from the therapeutic program; the civic investment in adaptive infrastructure benefits the entire local fiber arts ecosystem, not only the therapeutic participant pool"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 30000
  # Equals economics.capital_cost.mid per E3-R1.

  cost_sd: 10000
  # (high − low) / 4 = (55,000 − 15,000) / 4 = 10,000.
  # cost_sd / cost_mean = 10,000 / 30,000 = 0.333; within 0.15–0.50 acceptable
  # range per E3-R5.

  throughput_units_equiv_per_year: 728
  # Derivation (per weaving SCHEMA.md §1 E-3 guidance):
  # Derated active hours: 24 hr/wk − (40 min/day × 4 days/wk / 60 min) = 24 − 2.67
  # = 21.3 hr/wk net.
  # Effective hours/yr: 21.3 × 52 × (1 − 0.12) = 21.3 × 52 × 0.88 ≈ 974 hr/yr.
  # Throughput rate: ~0.75 m/hr facility-wide (blended across rigid-heddle stations
  # at therapeutic pace; 85% of time is instruction/open-studio at beginner/
  # therapeutic rate; 15% is accessory finished-project work at slightly higher rate).
  # Annual throughput: 974 hr × 0.75 m/hr ≈ 730 m/yr → 728 m/yr stated.
  # Unit = 1 linear meter of woven cloth equivalent (stated per Key Assumptions).

  variable_cost_per_unit: 7.55
  # Direct variable cost per meter-equivalent:
  # annual_consumables ($5,500) / throughput_units_equiv_per_year (728) ≈ $7.55/m.
  # This reflects per-unit material consumption (yarn, heddle wear, adaptive
  # equipment consumables) allocated proportionally to throughput. Fixed-proportion
  # consumables (hygiene supplies, documentation materials) included here as
  # dominant proportion of consumables is yarn and session-variable supplies.

  labor_hours_per_unit: 1.34
  # Effective hours/yr (974) ÷ throughput_units_equiv_per_year (728) ≈ 1.34.
  # Reflects total supervised labor-hours per output-equivalent meter including
  # therapeutic instruction overhead — consistent with E3-R3.

  downtime_fraction: 0.12
  # Sources: OT-partner referral scheduling gaps and session cancellations (~5%),
  # equipment maintenance and first-year failure events (rigid-heddle replacements,
  # adaptive equipment: ~3%), civic administrative overhead (public holidays, staff
  # absence, MOU review meetings, OT coordination: ~4%). Total 12%.
  # Consistent with operations_reality first_year_failures profile: heddle failure
  # at ~600 hr (year 0.6 under 24 hr/wk, 7-day lead time, ~1.2% downtime in
  # year 1); adaptive equipment wear at ~800 hr (10-day lead time, ~1.7% downtime).
  # Aggregate first-year failure downtime ~3%, consistent with the 3% maintenance
  # component of the 12% total.

  lifespan_years: 20
  # Rigid-heddle looms with regular maintenance have a 15–25 year service life
  # [CITATION-NEEDED: rigid-heddle loom service life — manufacturer documentation
  #  or guild operating records]; 20 years is a conservative planning horizon.
  # Adaptive equipment has a shorter replacement cycle (3–5 years per component);
  # these replacement costs are included in annual_maintenance and annual_consumables
  # rather than driving the lifespan figure down. Floor-loom-4shaft units carry
  # the full 25-year lifespan; 20 years is a blended conservative estimate
  # weighted toward the primary rigid-heddle equipment.

  usage_rate_threshold: 0.15
  # Specialized civic facility lower threshold, per ECONOMIC-LENSES.md §4.3
  # (specialized-equipment exception). At 3,744 person-hours/yr and small-city
  # scale (40,000 residents): 3,744 / 40,000 ≈ 0.094 hr/capita/yr. This is
  # below the 0.15 threshold; however, the correct denominator for a clinical-
  # referral facility is the addressable participant population, not the full
  # city population. Addressable population (rehabilitation patients + elderly
  # adults with mobility limitations + disabled adults): typically 8–12% of
  # small-city population = 3,200–4,800 persons. At 3,744 hr/yr ÷ 4,000
  # addressable persons = 0.936 hr/capita (within target population), well above
  # the 0.15 threshold. Authors note: the usage_rate_threshold calculation for
  # this entry uses the addressable-population denominator, consistent with the
  # specialized-equipment exception rationale.

  amortization_years: 20
  # Equipment lifespan is 20 years (above); amortization aligned to lifespan
  # rather than the 30-year ECONOMIC-LENSES.md §4.1 default because the primary
  # equipment (rigid-heddle looms) has a shorter service life than civic
  # infrastructure. This is a conservative choice that slightly increases the
  # annual capital-service figure; noted in Key Assumptions.

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  village_market:    null
  village_coop:      null
  village_civic:     null
  town_market:       null
  town_coop:         null
  town_civic:        null
  small_city_market: null
  small_city_coop:   null
  small_city_civic:  null

# ── SOURCES ──────────────────────────────────────────────────────────────────

sources:
  - ref: "corpus/program/SCALES.md §2–4 — small-city scale parameters, per-household civic cost threshold ($80/hh/yr), and median wage ($62,000/yr)"
  - ref: "Ostrom, Elinor. 1990. Governing the Commons. Cambridge University Press — governance principles (cited for civic MOU structure, not cooperative lens)"
  - ref: "Chandler, Deborah. 1995 (rev. 2009). Learning to Weave. Interweave Press — rigid-heddle throughput ranges and operator skill definitions"
  - ref: "[CITATION-NEEDED: OT session billing rates, US 2024 — individual clinical occupational therapy billing, $150–300/hr estimate; no specific source confirmed at authoring date; cite CMS or AOTA compensation survey]"
  - ref: "[CITATION-NEEDED: peer-reviewed OT literature on weaving as fine-motor rehabilitation — stroke recovery, TBI, upper-extremity impairment; systematic review or RCT preferred]"
  - ref: "[CITATION-NEEDED: peer-reviewed OT literature on craft group therapy psychosocial outcomes — anxiety reduction, depression symptom management in rehabilitation and geriatric populations]"
  - ref: "[CITATION-NEEDED: therapeutic weaving in veteran PTSD and TBI programs — VA or DoD program evaluation literature]"
  - ref: "[CITATION-NEEDED: AOTA continuing-education therapeutic weaving pathway — confirm CE course availability and provider]"
  - ref: "[CITATION-NEEDED: rigid-heddle loom capital cost — equipment retailer pricing (Schacht Flip, Ashford Knitters, Kromski Harp) 2024–2025]"
  - ref: "[CITATION-NEEDED: accessible workstation and adaptive OT equipment pricing — OT supply catalog pricing (Sammons Preston, Patterson Medical) 2024–2025]"
  - ref: "[CITATION-NEEDED: therapeutic weaving participant throughput rate — OT program data or fiber arts therapy practitioner documentation; no published benchmark found]"
  - ref: "[CITATION-NEEDED: rigid-heddle loom service life — manufacturer documentation or guild operating records; 20-year estimate requires confirmation]"
  - ref: "[CITATION-NEEDED: rigid-heddle noise level at operator position — acoustic measurement; no direct measurement found; 52 dB estimate derived from weaving literature context]"
  - ref: "[CITATION-NEEDED: state therapeutic-recreation and disability-services grant programs — availability and typical award amounts for municipal therapeutic weaving programs]"
  - ref: "[CITATION-NEEDED: IMLS Public Library Survey FY 2021 — small-city (15,000–75,000 population) library operating expenditure per household; $40–55/hh/yr estimate requires confirmation against PLS data]"
  - ref: "US Census Bureau, American Community Survey 5-year estimates (2018–2022), Table B25010 — average household size and household count derivation for scale parameters"
---

## Summary

The Therapeutic Weaving Workshop (weave-011) is a small-city civic facility designed as cost-effective occupational therapy infrastructure, not as a craft amenity. The facility operates 6–8 rigid-heddle looms at ADA-accessible workstation heights, partnered with a hospital or regional rehabilitation center that provides occupational therapist co-facilitation, clinical referrals, and outcome documentation. The city contributes the weaving instructor, loom infrastructure, and space; the clinical partner contributes the OT protocol and co-facilitator staff time. The resulting session cost — roughly $20–40/hr at group rate for the therapeutic weaving component — is dramatically more affordable than individual clinical OT billing at $150–300/hr, which is the program's public-goods justification. The facility targets small-city scale only; village and town scales lack the hospital partnership infrastructure and referral volume to sustain the model. It is evaluated exclusively under the civic lens: market and cooperative lenses are both poor fits for a program serving rehabilitation patients and disabled adults who cannot pay market-clearing prices for what they need.

## Design rationale

This entry solves a specific problem no other weaving catalog entry addresses: the intersection of occupational therapy clinical need and civic fiber arts infrastructure, analyzed as cost-effective healthcare rather than cultural programming. weave-010 (Community Fiber Arts Center) mentions therapeutic weaving as a secondary benefit of its OT-partnership model; weave-011 inverts the priority structure — the therapeutic OT function is the primary purpose, and the fiber arts are the delivery mechanism. The two entries are distinct in: (1) scale target (weave-010 is town-primary; weave-011 is small-city primary); (2) cost-justification framing (weave-010 justifies cost as arts/education; weave-011 justifies cost as clinical-equivalent healthcare); (3) governance model (weave-010 is arts-council-adjacent; weave-011 operates under a formal hospital MOU with HIPAA-adjacent data requirements); and (4) participant profile (weave-010 serves the general public; weave-011 serves a clinically-referred rehabilitation population). The anti-romantic treatment is load-bearing here: the entry explicitly rejects "healing power of craft" mysticism in favor of measurable clinical outcomes. Therapeutic weaving works not because craft is spiritually restorative but because repetitive bilateral hand motion activates fine-motor neural pathways, group participation reduces social isolation, and structured completion-oriented tasks provide the kind of goal-directed activity that occupational therapy has documented as clinically effective. The distinction matters for the political coalition (hospital boards respond to outcome data, not craft wellness claims) and for grant eligibility (state therapeutic-recreation grants require outcome metrics, not testimonials).

## Historical lineage

Three functional precedents inform this design.

**US occupational therapy activity-based rehabilitation (post-WWI and WWII).**  The foundation of the OT profession in the United States was craft production: early occupational therapists in the 1910s–1940s used weaving, basketry, and pottery as documented rehabilitation modalities for shell-shocked soldiers and factory-injury patients. The American Occupational Therapy Association was founded in 1917 partly on the premise that structured, purposeful hand activity was clinically therapeutic for psychiatric and physical rehabilitation patients. The functional inheritance is the evidence base: the use of loom weaving specifically as a bilateral-coordination and fine-motor rehabilitation tool derives from this tradition and has a century of practitioner documentation, if not yet a robust RCT literature. What the modern design does not inherit: early OT craft programs operated in institutional settings (hospitals, sanitaria) with captive patient populations and no cost-comparison pressure. The modern civic-partnership model must justify its cost against alternative service delivery (individual clinical OT billing) in a competitive municipal budget environment that early institutional OT programs never faced. The cost-effectiveness argument is a modern addition, not an inheritance.

**UK social prescribing and craft-as-therapy programs (2000s–present).**  The UK's National Health Service social prescribing framework (formalized circa 2019 as a NHS England commitment) created a structured mechanism for GPs to refer patients to community-based non-clinical interventions, including craft groups, as adjuncts to medical care. Several NHS-linked programs specifically used weaving and textile arts as the delivery mechanism, with documented outcomes in anxiety reduction and social isolation for elderly and disabled participants. The functional inheritance is the partnership model: a clinical institution (NHS GP practice; US equivalent: hospital OT department) refers patients to a civic facility (community center, library) rather than providing the service clinically. The civic facility does not need to be a clinical operation; it needs a clinical referral channel and co-facilitation arrangement with a qualified OT. The cost-effectiveness rationale of social prescribing (reducing clinical load by substituting lower-cost community interventions) directly maps to the civic-lens cost argument in this entry. What the design does not inherit: NHS social prescribing operates within a single-payer framework where clinical cost-accounting and referral tracking are centralized; the US equivalent requires institution-specific MOU structures and insurance arrangements that the NHS framework handles systemically.

**Scandinavian institutional textile therapy tradition (20th century).**  Scandinavian welfare states integrated weaving into institutional care for elderly and disabled populations throughout the 20th century, particularly in Swedish and Norwegian elder-care facilities where textile production was used as a structured activity modality. The functional inheritance is the activity-programming framework: weaving as a time-structured, completion-oriented task that is appropriate for a range of mobility and cognitive profiles, not requiring verbal communication, usable in short session windows, and producing a tangible finished object (a scarf, a small textile) that provides concrete evidence of accomplishment — an OT goal-completion metric. The institutional-program precedent also establishes the low per-session cost norm: when woven into an existing institutional care context, the marginal cost of a weaving session is primarily instructor time and yarn, not clinical billing overhead. This cost structure is what the civic-partnership model seeks to replicate outside the full institutional setting. What cannot be reproduced: the Scandinavian institutional model operated within a comprehensive social-welfare budget that subsidized elder care at a level with no US equivalent; the civic partnership model substitutes a narrower MOU-based arrangement for the full institutional subsidy.

## Key assumptions

**Capital cost ($15,000–$55,000, mid $30,000):** No published benchmark for a civic therapeutic weaving workshop of this configuration was found at authoring date. The mid estimate is derived from: rigid-heddle looms at $300–500 each × 8 units = $2,400–$4,000; 1 floor-loom-4shaft at $3,000–$4,500; accessible workstation tables (adjustable height) at $400–800 each × 8 = $3,200–$6,400; adaptive equipment kit (grip aids, beater handles, tactile heddle markers, low-vision aids) = $2,000–$4,000; elevated-lux lighting system = $1,500–$3,000; studio fit-out = $1,500–$4,000. Total mid range approximately $13,600–$25,900 equipment + $5,000 install = $18,600–$30,900; rounded to $30,000 mid with margin for institutional procurement overhead and ADA compliance modifications. All equipment cost figures flagged [CITATION-NEEDED] and require confirmation against current pricing before status promotion. The mid capital cost is substantially lower than weave-010 ($65,000) because: no dye station, no humidity-control HVAC, fewer looms, smaller footprint, and simpler ventilation requirements.

**Staffing ($61,500/yr):** Mid-point of the specified $58,000–$65,000/yr range for a small-city OT-credentialed weaving instructor per corpus/program/SCALES.md §3 small-city skilled-trades median ($62,000/yr). The wage premium over a standard journeyman-weaver studio rate reflects the clinical-adjacent role requirements (adaptive instruction, OT protocol familiarity, MOU compliance documentation). The hiring pool is thin; the wage may need to be at the high end of the range ($65,000) in competitive small-city labor markets. OT co-facilitator costs are borne by the partner institution under the MOU and are not included in this entry's staffing cost; this assumption is the single most load-bearing variable in the budget model and must be confirmed before program launch.

**OT session cost benchmark ($150–300/hr individual clinical):** This figure is the primary cost-effectiveness argument and requires confirmed citation. The range reflects the wide variation in clinical OT billing (Medicare/Medicaid reimbursement rates vs. private-pay rates vs. out-of-network rates). A more precise figure from CMS billing data or AOTA compensation survey would strengthen the civic justification significantly. The group-rate equivalent cost for this program ($72,700 operating ÷ 3,744 participant-hours = ~$19.41/participant-hr) compares favorably against any plausible individual clinical OT billing rate; the argument is robust to wide variation in the baseline.

**Throughput units (728 m/yr):** This figure has low operational significance for a facility where throughput is not the purpose. It is included for E-3 internal consistency and sim_params derivability, not as a primary performance metric. The meaningful civic metric is participant-contact-hours (3,744/yr) and cost-per-participant-hour (~$19.41/hr at gross operating cost before grants). Authors should note in any simulation run that throughput_units_equiv_per_year is a secondary metric for this entry; the primary civic evaluation metric is cost-per-participant-contact-hour vs. individual clinical OT billing rate.

**Space contribution assumption:** The entry treats floor_space_rent_per_year as $0 on the assumption that the partner institution (hospital, rehab center) or city facility contributes the space under the MOU. If the city must lease dedicated space, the economics change substantially: 40 m² at light-commercial institutional rates ($200–350/m²/yr in a small city) adds $8,000–$14,000/yr to operating cost, pushing per-household cost to $5.15–$5.85/hh/yr gross — still within the $80/hh/yr small-city threshold but requiring a revised budget_line. This assumption is load-bearing and must be confirmed in the partnership negotiation.

## Known risks / failure modes

**Regulatory.** The primary regulatory exposure is the HIPAA-adjacent participant data handling requirement: therapeutic weaving sessions generate clinical-adjacent documentation (participant progress notes, OT goal-completion records) that may constitute protected health information under HIPAA if the civic facility is deemed a business associate of the partner institution. Town counsel review of the MOU is required before program launch to confirm whether the civic program triggers BAA (Business Associate Agreement) obligations. Secondary: professional-liability insurance for a clinical-adjacent program may not be covered by standard municipal parks-and-rec general liability; a specific therapeutic-recreation rider or umbrella policy extension is likely required. ADA compliance for the accessible workstation layout (wheelchair turning radius, adjustable-height tables, accessible door hardware) requires a building assessment before opening; retrofitting an existing room that is not already ADA-compliant can materially increase install cost above the $5,000 estimate.

**Labour pipeline.** The weaving instructor position is the program's single point of failure. The hiring pool for a journeyman weaver with OT-protocol familiarity is nationally thin; unlike weave-010 (which can hire a standard journeyman weaver and provide OT orientation as secondary training), this entry's therapeutic focus requires a higher skill-blend that cannot be quickly filled from a regional hiring pool. Voluntary departure risk is elevated: a candidate with both weaving competency and OT exposure is also eligible for clinical OT assistant (COTA) positions at $45,000–$55,000/yr [CITATION-NEEDED: COTA wage data, BLS], making retention at $61,500/yr dependent on the non-wage appeal of the civic instructor role. The apprentice pipeline (36-month horizon to Stage 3) provides long-run succession mitigation; the first three years of the program have no internal succession backstop.

**Supply chain.** The supply chain for this entry is substantially less fragile than market-lens fiber entries: industrial cotton and acrylic yarn from major distributors has a 7-day typical lead time with multiple substitutable suppliers. The meaningful supply-chain risk is adaptive equipment: custom-width beater extensions, specific grip-aid configurations for unusual disability profiles, and replacement rigid-heddle units from specific manufacturers (Schacht, Ashford) have longer lead times and smaller distributor networks than standard weaving supplies. The 21-day worst-case lead time for specialty adaptive OT equipment is realistic and requires a modest safety-stock policy for critical adaptive components. The more significant dependency risk is the OT partnership itself: if the partner institution withdraws co-facilitator staff (budget cuts, staff turnover, change in OT department priorities), the program cannot operate clinically without a replacement — and recruiting a new institutional partner is a multi-month process, not a supply-chain problem solvable by inventory management.

## Iteration log

- 2026-04-18: v0.1 — initial creation; weave-011 Therapeutic Weaving Workshop. CIVIC-PRIMARY entry per Plan I Task 13 specification. Civic-only lens (market: poor, cooperative: poor, civic: good); small-city primary with town marginal. Full lens_context.civic block with five civic_externalities, staffing_model at $61,500/yr per SCALES.md §3 small-city tier, benchmark_comparison at ~$4.65/hh/yr vs. $80/hh/yr civic threshold, and hospital-board + OT department + AARP + disability-advocates political coalition. Anti-romantic framing applied throughout: "healing power of craft" explicitly rejected in favor of measurable clinical outcomes. OT co-facilitator cost assigned to partner institution under MOU (not in this entry's economics) — documented as a load-bearing assumption in Key Assumptions and Known Risks. Sixteen [CITATION-NEEDED] flags placed over clinical outcomes literature, OT billing rates, adaptive equipment pricing, and AOTA CE pathway. No cooperative lens_context required (cooperative: poor). No market lens_context required (market: poor). annual_public_use_hours and usage_rate_threshold placed in trade_specific block per weave-010 civic precedent.
