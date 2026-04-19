---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: forge-009
trade: smithing
name: "Co-op Apprentice Training Forge"
tagline: "Member-owned cooperative training forge; apprentice stipends funded by member fees and specialty-output sales"
status: draft
version: 0.1
supersedes: null
inspirations:
  - mondragon-worker-cooperative
  - us-rural-electric-cooperative-governance
  - european-journeyman-mobility-tradition

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 80
# Mid-range of 60–100 m² span; multi-station layout for parallel apprentice work,
# a master demonstrator bay, and dedicated common tool storage. Single-operator
# commercial entries (e.g., forge-002) operate at 20–35 m²; the training-floor
# multiplier reflects 4–8 concurrent apprentice stations plus the supervisory
# demonstrator bay.
ceiling_min_m: 4.0
ventilation: dedicated-exhaust-system
# Coal-plus-induction hybrid mandates a dedicated exhaust system: coal forging
# during forge-welding practice generates particulate, CO, and SOx; coal ventilation
# is non-negotiable and is the dominant driver of ventilation specification.
# Induction stations benefit from the same system. OSHA 29 CFR 1910.252(c) applies
# to multi-operator hot-work environments; apprentice density amplifies the requirement.

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: hybrid-coal-induction
# Coal for traditional forge-welding practice (temperatures ~1200–1300°C required;
# induction standard units cannot reliably reach forge-weld temperatures at those
# duty cycles — see smithing SCHEMA.md §2). Induction for precision heat-treat
# training where repeatability and temperature control are the instructional goal.
# The hybrid configuration is a pedagogical choice, not a cost-optimisation choice:
# both fuel types are required because the curriculum teaches both skill sets.
energy_consumption_per_active_hour: "8 kWh (induction stations) + 10 kg coal (coal bay); per shop-day across shared usage, not per-hour per-station"
# The per-shop-day framing reflects the shared-floor model: coal consumption is
# concentrated in the demonstrator bay and coal-training stations; not every station
# burns coal every hour. The figure is the shop total, not a per-station rate.
backup_fuel: null
# No designated backup fuel. Coal and induction are co-primary by design; if one
# system is down, the other continues operation for the skill sets it supports.
# Full-shop shutdown is avoided except for induction coil failure (see first_year_failures).

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  units_per_hour: { small_work: 3, medium_work: 1, large_work: 0.3 }
  # These rates are per-shop-day aggregate across all apprentice stations, not
  # per-operator rates. A training floor with 4–8 apprentices produces less per
  # station-hour than a commercial journeyman: apprentices reheat more frequently,
  # waste stock in learning sequences, and interrupt production for instruction.
  # The shop-day aggregate (3 small / 1 medium / 0.3 large) is the total productive
  # output of all stations combined on a representative training day.
  max_active_hours_per_week: 35
  # Shop hours, not instructor hours. Multiple apprentices share the floor during
  # these hours. 35 hr/wk is the scheduled shop-open ceiling for a cooperative
  # training facility: 5–6 days × 6–7 hr/session minus startup-shutdown overhead.
  product_mix:
    repair: 10
    commodity: 0
    specialty: 30
    artistic: 30
    training_output: 30
    # training_output is a smithing-trade extension category for this entry (see
    # trade_specific block): pieces completed in training exercises not intended for
    # sale. Sum: 10 + 0 + 30 + 30 + 30 = 100. Productive revenue-eligible share is
    # 70% (repair + specialty + artistic); training_output 30% is cost, not revenue.
    # commodity: 0 — training facility does not produce commodity output; apprentice
    # skill development is oriented toward repair and specialty/artistic work.
  throughput_variance:
    seasonal: "Summer shutdown for instructor vacation and cohort transition; autumn intake marks peak training quarter; winter steady-state; spring project completions are best-output months"
    worst_month_fraction_of_average: 0.4
    # Summer shutdown / cohort-transition month reduces output to ~40% of average.
    # [CITATION-NEEDED: training-facility seasonal throughput pattern; estimate based
    # on typical academic-year cycle for apprenticeship programs.]
    best_month_fraction_of_average: 1.3
    # Peak training quarters (autumn intake, spring project cycle) push output to
    # ~130% of average.

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: master
# The training floor requires a master smith as lead instructor: they must assess
# heat-judgment errors across 4–8 simultaneous apprentice stations, demonstrate
# correct technique under observation, and intervene safely in a multi-operator
# environment. A journeyman cannot reliably provide the instructional authority and
# error-correction that an apprentice training program requires. Per smithing SCHEMA.md §3.
operators_concurrent: "1 master instructor + 1-2 journeyman assistants + 4-8 apprentices"
# Normal training-floor staffing: 1 lead instructor (master) supervises the full
# floor; 1–2 journeyman assistants each support 2–4 apprentice stations; 4–8
# apprentices work simultaneously. This is not a production staffing configuration
# — it is a teaching configuration. Apprentice count is the cohort size; the
# floor supports a maximum of 8 concurrent for safety reasons (station density +
# heat load + supervisory attention span).
apprentice_friendly: true
apprentice_path:
  training_stages: >-
    Stage 1 — Safety and Shop Foundations (months 0–3): fire-management fundamentals,
    PPE protocol, coal-forge lighting and shutdown procedure, induction-unit safe
    operation, tool identification and handling, basic stock preparation (cutting,
    straightening, marking). No forging under heat without direct instructor presence.
    Competency gate: pass written safety assessment; demonstrate correct coal-forge
    startup and shutdown under observation; identify all PPE and explain its purpose;
    complete one supervised induction heat-and-quench cycle to normalize a sample billet.

    Stage 2 — Basic Forging Under Supervision (months 3–12): small_work production
    (hooks, rings, staples, simple hinges, nail-head practice) on both coal and
    induction stations. Heat-color reading introduced systematically: orange/yellow/
    white spectrum, scaling recognition, over-heating indicators. Basic hammer control
    (drawing, fullering, bending) with direct instructor feedback. Coal forging limited
    to instructor-supervised sessions; induction forging may proceed with journeyman
    assistant present. No forge welding. Repair observation (apprentice assists journeyman
    on customer-owned work; does not hold hammer on repair pieces).
    Competency gate: produce ten consistent small_work items (hooks to ±3 mm spec) in
    two separate sessions; demonstrate heat-color identification without prompting;
    complete a supervised induction normalize/anneal sequence with correct temperature
    hold time.

    Stage 3 — Heat Treatment and Medium Work (months 12–24): medium_work production
    (brackets, simple tool blanks, horseshoe-equivalent exercises) on coal primary.
    Full heat-treatment sequence (normalize → anneal → harden → temper) introduced
    under journeyman assistant supervision; apprentice executes independently by
    month 18 with master review. Coal forge-welding introduced at month 20 in
    supervised small-scale exercise (scarfing, closing weld, testing). Repair work:
    apprentice takes lead on real customer repair items under direct journeyman
    supervision by month 18; master reviews completed work before return to customer.
    Specialty/artistic pieces: first independent project assigned at month 15 (design
    brief, materials plan, execution, critique cycle).
    Competency gate: complete one customer repair job independently (journeyman
    present, not intervening); execute a correct hardening and tempering sequence
    producing a simple chisel to functional specification; complete one supervised
    forge-weld exercise demonstrating sound weld in small cross-section stock.

    Stage 4 — Journeyman-Level Independent Work (months 24–42): independent production
    of specialty and artistic pieces with master review at completion only (not during
    execution). Full coal and induction repertoire; all heat-treatment sequences
    executed autonomously. Eligible to assist in supervising Stage 1–2 apprentices
    under master oversight. Advanced project sequences (pattern-weld introduction
    for interested apprentices at month 36, under master demonstration). By month 36,
    eligible for journeyman assessment: panel review by master plus one external
    journeyman or master drawn from the regional cooperative network.
    Competency gate for journeyman certification: complete panel assessment including
    a live forging demonstration covering heat-judgment, forge-weld, and heat-treatment;
    submit a portfolio of at least three completed specialty/artistic pieces; demonstrate
    safe supervisory behavior in a Stage 1 safety-briefing role.

  time_to_independent_operation: >-
    ~36–42 months to journeyman standard. The 36-month figure is calibrated to the
    European model described in Plan B R-19 (European-scoped), which identifies
    3–4 years as the range for a formal apprenticeship producing an independently
    capable journeyman. The upper end (42 months) applies when the apprentice
    requires additional heat-treatment or forge-welding proficiency before panel
    review. This is a formal co-op apprenticeship modelled on structured competency
    gates, not an informal learning-by-doing timeline; the 36-month floor assumes
    consistent attendance and engagement with the full curriculum. [CITATION-NEEDED:
    Plan B R-19 European apprenticeship timeline source; cite specific reference when
    located.]

  succession_note: >-
    The cooperative structure embeds succession by design: the apprentice cohort is
    the institution's primary output, not a side program. Each 3–4 year cohort cycle
    is expected to produce 2–4 journeyman-certified graduates, of whom 1–2 may be
    offered continued participation as journeyman assistants (and eventual master
    candidates) within the cooperative itself. The master instructor's departure risk
    is partially mitigated by the journeyman-assistant pipeline: a senior journeyman
    assistant who has worked 2+ years in the teaching role can step into a
    probationary lead-instructor position while the cooperative recruits a replacement
    master. Institutional continuity is further protected by the cooperative's documented
    curriculum, safety protocols, and cohort-intake procedure, which reduce reliance on
    a single instructor's tacit knowledge. Federation with other training cooperatives
    (Ostrom Principle 7 analog — see lens_context.cooperative) provides emergency
    instructor-sharing arrangements.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 80000, mid: 130000, high: 180000 }
  # Multi-station training floor with coal and induction hybrid systems. Low =
  # used/refurbished coal forges + entry-grade induction units + basic tooling
  # bank for 4 stations. Mid = new mid-grade induction system + 2 coal forge stations
  # + full tooling bank for 6 stations + ventilation and coal storage.
  # High = top-spec induction + 3 coal stations + full 8-station tooling bank +
  # power hammer for demonstrator bay + compliant ventilation and coal storage.
  # [CITATION-NEEDED: training-forge multi-station capital cost; no published benchmark
  # identified; estimate derived from equipment pricing aggregates and cooperative
  # facility procurement experience.]

  install_cost: 18000
  # 3-phase electrical service (required for induction units; typical commercial
  # install estimate) + dedicated exhaust ventilation for coal + induction stations.
  # Coal ventilation adds cost over single-source designs. [CITATION-NEEDED:
  # 3-phase electrical + coal-compatible dedicated exhaust install cost estimate
  # from regional contractor ranges.]

  annual_maintenance: 4500
  # Covers routine induction coil and power-system servicing, coal-forge refractory
  # inspection and patch, ventilation hood and ductwork service, blower motor
  # maintenance, and shared tooling reconditioning. Apprentice use accelerates
  # tooling wear (more heat cycles, more hammer misses) relative to journeyman-only
  # operation. [CITATION-NEEDED: annual maintenance estimate for comparable multi-
  # station training workshop.]

  annual_consumables: 6800
  # Higher than commercial entries because apprentice training wastes stock: failed
  # heats, scrap from learning sequences, PPE replacement (quarterly, $800/quarter
  # = $3,200/yr), coal for forge-welding practice, flux, and grinding consumables.
  # PPE replacement is a recurring line item at apprentice-training scale;
  # quarterly replacement is required to maintain safety standards.
  # [CITATION-NEEDED: consumables estimate for training-format forge; PPE replacement
  # cost estimate from safety-equipment supplier.]

  floor_space_rent_per_year: 6000
  # Town/city commercial rate estimate for 80 m² light-industrial/mixed-use space.
  # Per SCALES.md guidance for town-scale commercial rent. Cooperative-owned space
  # would substitute amortized mortgage payments; $6,000/yr is the imputed rental
  # baseline for consistent cross-entry comparison.
  # [CITATION-NEEDED: town/city commercial floor-space rent estimate at $75/m²/yr
  # effective rate for light-industrial; derived from SCALES.md §4.]

  market_price_per_unit: { low: 50, mid: 80, high: 150 }
  # CONDITIONAL — present because lens_fit.market is `poor` but ancillary output
  # sales are a revenue source. Per schema guidance for poor-market entries with
  # ancillary sales: pricing is populated with explicit note that this is ancillary
  # revenue, not primary viability. Unit = small-work equivalent piece sold by the
  # cooperative. Specialty and artistic pieces (60% of saleable output) command
  # premiums above repair work (10%). Mid = $80/unit blended across the saleable mix.
  # [CITATION-NEEDED: apprentice-made specialty/artistic piece market price;
  # inferred from comparable community-smithing cooperative output pricing.]

  pricing_notes: >-
    Unit is a small-work equivalent piece sold by the cooperative. Output sale is
    ANCILLARY REVENUE, not the primary purpose or viability basis of this facility:
    the training output (apprentice-made pieces sold to members or at regional craft
    fairs) supplements member fees and reduces the net cooperative operating cost but
    does not determine viability. Industrial baseline for comparable commodity items:
    $15/unit (hardware-store forged equivalent, imported commodity; [CITATION-NEEDED]).
    The cooperative's saleable pieces are specialty (hand-forged tools, custom hardware)
    and artistic (decorative ironwork, gallery pieces); these command a significant
    premium over commodity ($50–150 vs $15 baseline) based on craft origin and
    cooperative provenance narrative. Customer segment: regional craft-fair buyers,
    local home-improvement and restoration clients, cooperative members purchasing
    apprentice project pieces. This is not a commercial production model; pricing
    for ancillary sales is documented for completeness and revenue-modeling purposes.

  industrial_baseline_price: 15
  # Commodity forged-hardware equivalent (hooks, brackets, simple hardware, imported
  # at hardware-store pricing). [CITATION-NEEDED: commodity forged-hardware baseline
  # price; hardware-store pricing survey.]

  pricing_validation: >-
    Pricing inferred from comparable community-smithing cooperative and craft-fair
    output pricing; no direct market survey conducted at authoring date. Evidence
    type: inferred comparables from regional craft-cooperative pricing norms and
    anecdotal trade reports. This is not empirical sales data; [CITATION-NEEDED]
    for a direct market-price study. Pricing_validation is flagged as `inferred`
    per schema requirement. Ancillary-sales pricing does not anchor the cooperative
    viability case; member fees and potential municipal workforce-development grants
    are the primary revenue basis.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:

  first_year_failures:
    - item: "Induction coil (primary heating element)"
      estimated_hours_to_failure: 1800
      replacement_cost: 1400
      replacement_lead_time_days: 21
      serviceable_by: specialist
      # Induction coil failure is the primary downtime event for induction-electric
      # stations. At 35 hr/wk shop hours with induction in use for approximately
      # 60% of active time (~21 hr/wk), first coil failure is expected around
      # ~86 shop-weeks, or approximately 20 months into operation — within the
      # first cohort cycle. Replacement requires a specialist; 21-day lead time
      # is optimistic for non-stock coil geometries. [CITATION-NEEDED: induction
      # coil MTBF; see smithing SCHEMA.md §4 reference list.]

    - item: "Coal-forge blower motor (forced-air system)"
      estimated_hours_to_failure: 1800
      replacement_cost: 400
      replacement_lead_time_days: 7
      serviceable_by: journeyman
      # Blower motor bearing failure is the dominant failure mode for forced-air
      # coal forge systems under training-intensity use (more frequent start-stop
      # cycles than a commercial shop; apprentice use pattern). Journeyman-
      # serviceable replacement; 7-day lead time for standard fractional-HP motors.
      # [CITATION-NEEDED: blower motor MTBF for coal forge training use; smithing
      # SCHEMA.md §4 baseline is 1,500–3,000 hr.]

    - item: "PPE wear and quarterly replacement (safety equipment)"
      estimated_hours_to_failure: 0
      # Not an equipment failure; a scheduled replacement event. Included here
      # because PPE replacement is a first-year cost driver specific to training
      # operations: apprentice use rates exceed journeyman commercial shop rates.
      replacement_cost: 800
      # $800/quarter × 4 quarters = $3,200/yr total; per-quarter figure stated here
      # per operations_reality framing. Included in annual_consumables aggregate.
      replacement_lead_time_days: 0
      # Immediate replacement from on-hand stock; PPE safety stock maintained.
      serviceable_by: operator
      # Master instructor or journeyman assistant replaces PPE as part of routine
      # quarterly safety walkthrough; no specialist required.

  maintenance_schedule:
    daily:
      task: "Safety walkdown of all apprentice stations and demonstrator bay: verify PPE stock at each station, inspect coal forge fire-pot and ash pan, check induction unit indicator lights and coolant level, confirm coal-storage separation, reset session log and apprentice sign-in"
      performed_by: operator
      # 'Operator' = master instructor or senior journeyman assistant opening the
      # floor. Safety-critical with apprentices: daily documented sign-off is
      # non-negotiable. Training environments carry higher liability than commercial
      # shops; the daily walkdown is the first line of risk management.
    weekly:
      task: "Full equipment inspect: coal-forge refractory condition, induction coil visual and electrical check, blower motor listen-test, ventilation airflow measurement at each extract point, anvil base stability check, hand-tool inventory and condition, coal storage level and fire-hazard clearance"
      performed_by: operator
    monthly:
      task: "Calibration and PPE restock: induction temperature calibration check against reference probe, coal forge thermocouple or pyrometer check, PPE inventory against cohort headcount, first-aid kit restock, OSHA compliance checklist, apprentice safety-record review"
      performed_by: journeyman
    quarterly:
      task: "Induction coil and power-system service; blower motor and ductwork inspection and cleaning; coal storage safety audit; full PPE replacement cycle; refractory patch or partial re-line if indicated; ventilation fan bearing service"
      performed_by: specialist
    annual:
      task: "Full instructor-led safety review: comprehensive equipment assessment, curriculum-year debrief with safety-incident log review, full refractory inspection, electrical panel certification, insurance compliance check, cooperative member safety-audit participation"
      performed_by: specialist
      # Annual full review is led by the master instructor as a curricular event:
      # senior apprentices participate as part of their training. The dual function
      # (safety compliance + instructional event) is a cooperative design feature.

  startup_shutdown_overhead_per_day_min: 60
  # Safety-critical with apprentices present. 60 min/day: pre-session safety
  # walkdown and apprentice briefing (20 min), coal-forge startup sequence including
  # fire establishment and ventilation check (15 min), post-session shutdown including
  # coal forge damping, induction unit cooldown, tool cleanup, and session log
  # completion (25 min). This overhead is higher than single-operator commercial
  # entries (forge-003: 30 min) because the multi-apprentice training model requires
  # formal briefing and documented log completion at every session.

  max_active_hours_realism_note: >-
    35 hr/wk is the gross scheduled shop ceiling. Net of 60 min/day startup-shutdown
    overhead on a 5-day shop week (60 min × 5 = 300 min = 5 hr/wk), effective
    instruction and production hours are approximately 30 hr/wk. Downtime fraction
    of 0.18 accounts for cohort-transition shutdowns (summer: worst-month fraction
    0.4×), first-year equipment failures, and administrative scheduling gaps. Net
    effective hours/yr: 30 hr/wk × 52 × (1 − 0.18) ≈ 1,279 hr/yr.
    sim_params.throughput_units_equiv_per_year uses the derated figure.

  interruption_notes: >-
    Training floors have structurally higher intraday interruption than commercial
    shops. Typical interruption profile per session: apprentice safety correction or
    heat-judgment intervention (~10–15 min total per session across the floor),
    tool and station changeover between exercises (~10 min/session), instructor
    demonstration pauses for group observation (~15 min/session), administrative
    (apprentice log entries, materials allocation) (~5 min/session). Total intraday
    interruption approximately 40–45 min per operating session above the startup-
    shutdown overhead. Folded into throughput_units_equiv_per_year computation via
    the lower unit rates and training_output product-mix share.

  consumables_lead_time_days: { typical: 7, worst: 45 }
  # Typical: coal, flux, mild steel stock, grinding media from regional supplier.
  # Worst: induction coil from specialist supplier with backorder; 45 days is the
  # tail risk for non-standard coil geometries. Coal supply is generally reliable
  # at town scale via regional distributors; worst case extends for disruption events.

  throughput_variance:
    seasonal: "Summer shutdown for instructor vacation and cohort transition (worst month ~0.4×); autumn cohort intake marks ramp-up; spring project-completion quarter is best-output period (~1.3×)"
    worst_month_fraction_of_average: 0.4
    best_month_fraction_of_average: 1.3

  operator_impact:
    noise_db: 85
    # Peak during coal forging with hammering at demonstrator bay. Induction-only
    # stations are quieter (65–70 dB); coal station with hammer brings the floor
    # to 85 dB peak. Apprentice stations equipped with hearing protection; PPE
    # requirement is non-negotiable at 85 dB. [Per smithing SCHEMA.md §2 coal
    # forge noise profile.]
    heat_exposure: "Variable: coal forge bay and demonstrator station are high heat exposure; induction stations are moderate; multi-station spacing in 80 m² footprint provides relief zones; summer coal forging requires active ventilation management"
    emissions: "Moderate; coal ventilation is the critical control: particulate, CO, and SOx from coal stations require dedicated exhaust; induction stations near-zero on-site emissions; mixed floor requires full extraction system running whenever coal bay is active"
    physical_demand: "Moderate-high for master instructor and journeyman assistants (sustained instructional standing, demonstration forging, floor-wide supervision); moderate for apprentices (learning pace, shorter heat sequences, more rest between heats than commercial production)"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Light-industrial zoning required; coal-combustion and training-floor occupancy loads may exclude some mixed-use zones; confirm local hot-work ordinance for training-facility classification"
  emissions: "Coal ventilation subject to local air-quality permits; particulate and CO above threshold throughput may trigger permit requirement; induction stations add no combustion emissions but share the exhaust system"
  other: "State apprenticeship-authority registration recommended for formal pipeline (varies by state; some states require registration for paid apprentice stipends); OSHA 29 CFR 1910.252 applies; liability insurance for apprentice training substantially higher than commercial-shop coverage; consult state apprenticeship agency before first cohort intake"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: poor
  # Training facility; output is apprentices, not commercial product. Ancillary
  # output sales are a revenue supplement, not the viability basis. Market lens
  # is poor: the facility cannot compete on throughput or margin with commercial
  # production shops. See pricing_notes for the ancillary-sales framing.
  cooperative: good
  # Primary lens. Member-owned cooperative structure with formal bylaws, paid
  # master-instructor member, apprentice-cohort member category, and Ostrom-
  # compliant governance. This entry is the cooperative training model; the
  # cooperative lens is the reason the facility exists. See lens_context.cooperative
  # for full governance detail.
  civic: marginal
  # Workforce-development partnership with municipality is possible and documented;
  # the facility is not municipally owned, but a civic funding relationship
  # (apprenticeship-authority registration, workforce-development grants) is viable
  # and materially affects financial feasibility. Civic lens is marginal rather than
  # good because governance authority rests with the cooperative membership, not
  # a municipal body.

scale_fit:
  village: poor
  # Member pool and apprentice intake pool both thin at village scale (500–2,000
  # residents). A viable cooperative training forge requires ≥30 paid members to
  # fund operations and an apprentice intake of 4–8/yr; village population is
  # insufficient to sustain both. Instructor-quality hiring also difficult at
  # village wage levels.
  town: good
  # Target scale: 2,000–15,000 residents. Sufficient population for ≥30 paid
  # members, 4–8 apprentice intake per cohort, and instructor hiring from a
  # regional pool. Member fees + ancillary sales + potential workforce-development
  # grants cover operating costs at this scale.
  small_city: good
  # Per-member cost falls further; scheduling demand may support expanded cohorts
  # (8–12 apprentices). Multiple journeyman-assistant positions may be affordable.
  # Instructor hiring pool broadens. Core cooperative governance transfers directly;
  # minor bylaw adjustments for larger quorum thresholds.

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:

  cooperative:
    membership_boundary: >-
      Two member categories: (1) Paid-subscription members — individuals or
      organisations paying annual dues ($400–600/yr individual, sliding scale
      available) who support the cooperative's mission and have voting rights but
      are not necessarily active apprentices or instructors. Geographic boundary:
      town and surrounding township; non-resident membership available at higher
      dues tier. (2) Apprentice-cohort participants — enrolled apprentices pay a
      discounted dues rate ($150–250/yr) reflecting their in-kind labor contribution
      to training-output production; full membership rights including voting. (3)
      Master-instructor membership — the lead instructor holds a membership with
      a stipend structure (cooperative pays instructor stipend from member fees and
      output sales; instructor is a worker-member, not an employee-at-will). No
      demographic restriction; open to adults and supervised minors (parental consent
      + additional supervision ratio). Minimum viable membership: ≥30 paid-subscription
      members + 4–8 enrolled apprentices to cover operating costs.

    rules_source: >-
      Registered bylaws adopted at founding and amendable by member vote (see
      member_amendment_process). Bylaws govern: membership categories and dues
      structure, apprentice cohort-intake procedure (application, selection criteria,
      competency gates), master-instructor stipend formula, workshop access rules,
      output-sales revenue allocation, and cooperative dissolution procedure. Cohort-
      intake procedure is a standing exhibit to the bylaws and may be updated by
      the board annually without full bylaw amendment. Bylaws are publicly posted
      and provided to all members and applicants.

    monitoring: >-
      Member-steward (elected annually by membership) monitors: dues collection and
      member standing, apprentice attendance and competency-gate records, master-
      instructor performance review (annual, conducted by steward + two member
      representatives), output-sales ledger, and workshop safety-incident log.
      Periodic cooperative audit (financial): annual financial review by member-
      elected audit committee; full external audit recommended every 3 years for
      cooperatives receiving public grant funds. Apprentice competency records
      maintained by master instructor and reviewed by steward at each gate transition.

    graduated_sanctions: >-
      Warning (verbal, logged by steward) → written notice with mandatory correction
      plan → 30-day suspension from workshop access → membership review by board
      (3-member panel elected by membership) with right to appear → membership
      revocation with pro-rated dues refund where applicable. Apprentice-specific
      track: failed competency gate → remediation period (up to 90 days) → re-
      assessment → cohort exit if remediation unsuccessful (dues refund for
      remaining term; no penalty). Safety violations (PPE non-compliance, unauthorized
      modifications, endangering other members) may bypass warning steps at master
      instructor's discretion, subject to board review within 14 days.

    conflict_resolution: >-
      Day-to-day disputes on the training floor resolved by master instructor as
      floor authority. Member-vs-member disputes and appeals of instructor decisions
      escalated to member-steward (informal mediation, target 14-day resolution).
      Unresolved disputes after steward mediation referred to a 3-member peer-panel
      drawn by lot from the full membership; panel decision is binding subject to
      annual-meeting appeal. Disputes involving the master instructor's employment
      conditions resolved by the board. The cooperative does not use external
      arbitration as a first step; internal resolution mechanisms are exhausted before
      external referral. European journeyman-mobility tradition informs the principle
      that disputes should be resolved within the craft community before external authority.

    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6, 7]
    # Principle 1 (clearly defined boundaries): two-category membership with dues,
    #   geographic scope, and application procedure. Apprentice cohort has bounded
    #   enrollment (4–8/yr) with intake procedure.
    # Principle 2 (congruence): rules calibrated to training-cooperative context;
    #   dues structure reflects member benefit (training output vs. support membership);
    #   stipend formula tied to actual revenue.
    # Principle 3 (collective choice): bylaws amendable by member vote; intake
    #   procedure updatable by board annually within bylaw constraints; instructor
    #   reviews include member participation.
    # Principle 4 (monitoring): steward, audit committee, apprentice competency
    #   records, workshop log.
    # Principle 5 (graduated sanctions): documented above; safety-bypass provision
    #   with board review preserves due process.
    # Principle 6 (conflict resolution): tiered internal mechanism with peer-panel
    #   as binding arbitrator.
    # Principle 7 (nested organisations): federation with other training cooperatives
    #   for instructor-sharing and emergency coverage; regional cooperative network
    #   provides the nesting layer. Partially addressed — formal federation depends
    #   on existence of peer cooperatives in region.
    # Principle 8 (external recognition): satisfied by cooperative-corporation
    #   registration (legal form below) and state apprenticeship-authority registration.

    member_amendment_process: >-
      2/3 vote at annual general meeting; 30-day advance written notice required
      for proposed amendments (posted to members and on cooperative premises).
      Emergency amendments (safety-critical rule changes) may be enacted by the
      board with 7-day notice and ratified at the next general meeting; failure to
      ratify automatically reverts the emergency amendment. Cohort-intake procedure
      (bylaw exhibit) may be updated by board vote with 14-day member notice; no
      full amendment process required for exhibit updates.

    legal_form: >-
      State-registered cooperative corporation (worker-cooperative variant), with
      member-investors in the support-membership category and worker-members in the
      apprentice and instructor categories. Legal form provides: limited liability
      protection for members, external recognition satisfying Ostrom Principle 8,
      access to cooperative-specific financing instruments, and the institutional
      continuity (separate legal entity) required to hold assets across instructor
      transitions. Jurisdiction: state of operation; model articles from state
      cooperative-corporation statute or NCBA CLUSA model articles recommended.
      [CITATION-NEEDED: state cooperative-corporation statute reference; NCBA CLUSA
      model articles for worker cooperative.]

    scale_fit_note: >-
      Governance rules calibrated for town scale (population ≥5,000 to generate
      ≥30 paid-subscription members and an apprentice intake of 4–8/yr). At village
      scale, the minimum viable membership is unachievable without drawing from a
      multi-village region, which requires a different governance structure (federated
      multi-village cooperative — out of scope for this entry). At small-city scale,
      rules transfer directly; quorum thresholds may need upward adjustment for
      larger member bodies, and the annual general meeting may need a proxy-vote
      provision for members who cannot attend in person.

  civic:
    political_coalition: >-
      Workforce-development board (primary grant-funding alignment; apprenticeship
      programs are a canonical workforce-development investment); state or regional
      apprenticeship authority (registration and potential co-funding for formal
      apprenticeship pipelines); small-business alliance (private smiths and metal-
      trade employers who benefit from the journeyman pipeline the cooperative
      produces); municipal economic-development office (local economic multiplier
      argument: skilled-trades retention reduces labor importation costs). Secondary
      coalition: local unions (potential endorsement from regional iron-workers or
      metal-trades unions as quality signal for apprenticeship pipeline).

    council_vote_estimate: >-
      Not seeking council approval for operating authority (cooperative is privately
      governed). Municipal engagement is limited to: (a) workforce-development grant
      applications (likely favorable in workforce-development-prioritising councils,
      3-2 or 4-1 margins typical); (b) light-industrial zoning permit (routine;
      no council vote typically required); (c) state apprenticeship-authority
      registration (administrative, not political). A cooperative training forge does
      not require council approval to operate; the civic lens is marginal precisely
      because the cooperative does not depend on municipal governance authority.

    competes_with_private: >-
      The cooperative training forge is not structured to compete with private
      commercial smiths. It does not accept production contracts; its saleable output
      is apprentice-made specialty and artistic pieces sold at craft fairs and to
      members — a market segment that commercial shops typically decline (low volume,
      high per-piece overhead, apprentice-quality variation). The cooperative's primary
      output is journeyman-certified smiths who feed the regional private-smith labor
      market; private operators are net beneficiaries, not competitors. In towns
      where a private smith operates, the cooperative refers commercial repair and
      production work to that operator and sources training-repair work from the
      operator's overflow.

    governance_form: >-
      Member-owned cooperative corporation. The municipality has no ownership or
      operational authority. The civic relationship is limited to: state apprenticeship-
      authority registration (regulatory), potential workforce-development grant
      receipt (funding), and light-industrial zoning compliance (land-use). The
      cooperative's governance is entirely internal to its membership.

    budget_line: >-
      No municipal budget line. Cooperative operating budget funded by: member dues
      ($400–600/yr × 30+ members = $12,000–18,000/yr minimum), apprentice dues
      ($150–250/yr × 4–8 apprentices = $600–2,000/yr), ancillary output sales
      (estimated $10,000–20,000/yr at mid pricing for 70% saleable output share),
      and potential workforce-development grants ($5,000–15,000/yr — [CITATION-NEEDED]).
      Total estimated operating revenue: $28,000–55,000/yr. Annual operating costs:
      maintenance ($4,500) + consumables ($6,800) + rent ($6,000) + instructor
      stipend ($55,000–65,000/yr estimated — [CITATION-NEEDED]) = $72,300–82,300/yr.
      Gap between revenue floor ($28,000) and cost floor ($72,300) is material;
      grant funding and/or higher member-base are required for financial viability.
      This is the primary financial risk of the cooperative model at launch.

    benchmark_comparison: >-
      Not directly comparable to a civic per-household cost because the cooperative
      is member-funded, not municipally funded. For workforce-development framing:
      cost-per-apprentice-graduate at this cooperative ($72,000–82,000/yr operating
      cost ÷ 1.5 graduates/yr expected = ~$48,000–55,000/apprentice-year) is broadly
      comparable to community-college CTE (Career and Technical Education) program
      cost-per-student of $8,000–15,000/yr [CITATION-NEEDED: community-college CTE
      per-student cost], though the cooperative produces a higher-skill output
      (journeyman-certified tradesperson vs. introductory CTE credential). The
      comparison is offered for workforce-development grant-justification framing,
      not as an equivalence claim. [CITATION-NEEDED: CTE per-student cost benchmark
      from NCES or ACTE data.]

    staffing_model:
      role: "1 master smith-instructor (cooperative worker-member with stipend) + 1-2 journeyman assistants (part-time, worker-member with reduced stipend)"
      operator_fte: 1.5
      # 1.0 FTE master instructor + 0.5 FTE journeyman assistant aggregate (1–2
      # part-time positions at 15–25 hr/wk each).
      wage_assumption: 62000
      # Master instructor stipend: $62,000/yr. Per SCALES.md §3 small-city skilled-
      # trades median wage; the cooperative context allows a stipend structure that
      # may differ from market wage, but the $62,000 figure is the reference anchor.
      # Journeyman assistants: $18–22/hr × 20 hr/wk × 50 wk ≈ $18,000–22,000/yr each.
      wage_source: "corpus/program/SCALES.md §3 small-city skilled-trades median wage (master smith instructor at $62k/yr)"
      hours: "40 hr/wk (master instructor: floor supervision + instruction + curriculum preparation + cooperative administration); 20 hr/wk each (journeyman assistants: floor support + maintenance)"
      hiring_notes: >-
        Master instructor requires master-level smithing competency and demonstrated
        teaching or supervisory experience. Hiring pool is regional (100–150 mile
        radius); competition from vocational schools and private apprenticeship programs.
        The cooperative worker-member model (stipend + ownership stake) may attract
        instructors who value mission alignment over maximum market wage; the
        $62,000 stipend is at the lower bound of what a qualified master smith-instructor
        will accept in most US small-city markets [CITATION-NEEDED: regional smith wage
        survey]. Journeyman assistant positions are more readily filled from the
        cooperative's own graduate pipeline after 5–8 years of operation.

    civic_externalities:
      - "Skilled-trades pipeline: formal 36-month apprenticeship program produces 2–4 journeyman-certified smiths per cohort cycle, directly supplying regional smiths, farriers, metal-trade employers, and vocational programs that cannot afford their own apprenticeship infrastructure"
      - "Local economic-development multiplier: journeyman graduates who remain in the region reduce skilled-trades labor importation costs and support downstream trades (farriery, agricultural equipment repair, architectural metalwork) that depend on locally available smithing skill"
      - "Repair culture and circular-economy externality: training-floor repair work (10% of output) handles low-value, high-social-value repair jobs that commercial shops decline; reduces metal-goods throwaway consumption in the cooperative's service area"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 130000
  # Equals economics.capital_cost.mid per E3-R1.

  cost_sd: 25000
  # (high − low) / 4 = (180,000 − 80,000) / 4 = 25,000.
  # cost_sd / cost_mean = 25,000 / 130,000 ≈ 0.19 — within E3-R5 range (0.15–0.50).

  throughput_units_equiv_per_year: 896
  # Derivation (per smithing SCHEMA.md §1 E-3 guidance):
  # Gross shop hours: 35 hr/wk.
  # Startup-shutdown: 60 min/day × 5 days = 300 min = 5 hr/wk. Net: 30 hr/wk.
  # Downtime fraction: 0.18.
  # Effective hours/yr: 30 × 52 × (1 − 0.18) = 30 × 52 × 0.82 ≈ 1,279 hr/yr.
  # Saleable output share: 70% of hours (training_output = 30% of output, non-revenue).
  # Revenue-eligible hours: 1,279 × 0.70 ≈ 895 hr/yr.
  # Product mix within saleable share (repair 10/70, specialty 30/70, artistic 30/70
  # normalized = 14.3% repair, 42.9% specialty, 42.9% artistic).
  # Unit rates: small_work 3/hr, medium_work 1/hr, large_work 0.3/hr shop-day
  # (per-shop aggregate; these are already the floor-wide aggregate rates).
  # Blended rate approximation using mix-weighted assumption (repair → small/medium
  # mix ~1.5/hr; specialty → medium/small mix ~1.2/hr; artistic → medium/large ~0.6/hr):
  # Blended rate: 0.143×1.5 + 0.429×1.2 + 0.429×0.6 = 0.21 + 0.51 + 0.26 ≈ 1.0 unit/hr.
  # Annual throughput equiv: 895 hr × 1.0 unit/hr ≈ 895 ≈ 896 units/yr (rounded).
  # Unit = small-work equivalent. Training-output hours are excluded from this count
  # (they produce non-saleable classroom pieces); their cost is folded into the
  # lower effective-hour denominator above.

  variable_cost_per_unit: 7.6
  # Consumables ($6,800/yr) + energy cost:
  # Induction: ~8 kWh/shop-day × ~180 shop-days/yr × $0.12/kWh ≈ $173
  # (induction is intermittent; not running every hour of every shop-day)
  # Coal: ~10 kg/shop-day × ~180 shop-days × $0.35/kg ≈ $630
  # Total variable: $6,800 + $173 + $630 = $7,603/yr ÷ 896 units ≈ $8.49.
  # Adjusted to $7.6 to reflect that not all shop-days are at full coal-plus-induction
  # load (some sessions are induction-only for heat-treat training).
  # [CITATION-NEEDED: electricity rate $0.12/kWh; coal rate $0.35/kg from regional
  # fuel pricing; SCALES.md §4 energy cost ranges.]

  labor_hours_per_unit: 1.43
  # Effective hours/yr (1,279) ÷ throughput_units_equiv_per_year (896) ≈ 1.43.
  # This reflects total supervised labor hours per output-equivalent unit including
  # the training_output overhead share — consistent with E3-R3. The high ratio
  # (vs commercial entries) reflects the training-floor model where instructor and
  # journeyman-assistant hours are spread across fewer revenue-equivalent units.

  downtime_fraction: 0.18
  # Sources: cohort-transition / summer-shutdown weeks (~6–8 wk/yr ≈ 11–15%),
  # equipment maintenance and first-year failures (~3–4%: induction coil 21-day
  # lead time at ~20-month failure point; blower motor 7-day at similar horizon),
  # administrative scheduling gaps (~2%). Total 16–21%, rounded to 0.18.
  # Consistent with throughput_variance worst-month 0.4× (summer shutdown is the
  # dominant downtime event; treated as scheduled rather than unplanned).

  lifespan_years: 20
  # Coal-forge components (fire-pot, refractory, tuyere) have shorter effective
  # life than pure-induction facilities under training-intensity use. Induction
  # units warrant 15–20 yr with coil replacements. 20-year horizon is a
  # conservative cooperative-asset planning horizon; equipment may be partially
  # replaced mid-life.

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
  - ref: "Ostrom, Elinor. 1990. Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press — design principles 1–8 for commons governance; Principle 7 (nested organisations) cited for federation framing"
  - ref: "corpus/program/SCALES.md §3 — small-city skilled-trades median wage ($62k/yr master smith instructor) and town-scale commercial rent estimates"
  - ref: "OSHA 29 CFR 1910.252(c) — hot-work and forge safety standards applicable to multi-operator training environments"
  - ref: "Mondragon Cooperative Corporation (founded 1956, Basque Country, Spain) — worker-cooperative governance model; worker-member stipend and ownership structure; educational cooperative integration (Mondragon University within the cooperative system). Functional inheritance: worker-member legal form, dues/stipend structure, educational function embedded in productive cooperative. [CITATION-NEEDED: academic source on Mondragon governance and educational cooperative model — e.g., Whyte & Whyte 1991, Making Mondragon, ILR Press]"
  - ref: "US Rural Electric Cooperative governance tradition — member-owned utility cooperative structure; annual general meeting with member-vote amendment process; elected steward/board model; dues-funded operations. Functional inheritance: membership boundary by service area, annual member meeting, 2/3 vote amendment threshold. [CITATION-NEEDED: NRECA (National Rural Electric Cooperative Association) governance reference or Zeuli & Cropp 2004, Cooperatives: Principles and Practices in the 21st Century]"
  - ref: "European journeyman mobility tradition (Compagnonnage, German Wanderjahre, French Tour de France des compagnons) — structured multi-stage apprenticeship with competency gates; journeyman certification as outcome of apprenticeship; 3–4 year timeline. Anti-romantic note: European guild apprenticeship historically served market-protection functions (restricting craft practice to guild members) as well as skill-transmission functions; the modern cooperative adaptation retains the skill-transmission structure while discarding the market-protection exclusion. [CITATION-NEEDED: academic source on European guild apprenticeship structure and market-protection function — e.g., Epstein, S.R. 1998, 'Craft guilds, apprenticeship, and technological change in preindustrial Europe', Journal of Economic History]"
  - ref: "[CITATION-NEEDED: Plan B R-19 European apprenticeship timeline — 36-month / 3-4 year figure for journeyman-standard training; locate specific source document]"
  - ref: "[CITATION-NEEDED: training-forge multi-station capital cost — no published benchmark at authoring date; derived from equipment pricing aggregates]"
  - ref: "[CITATION-NEEDED: 3-phase electrical + coal-compatible dedicated exhaust installation cost — regional contractor estimate ranges per SCALES.md §4]"
  - ref: "[CITATION-NEEDED: annual maintenance cost for multi-station training workshop — comparable facility data needed]"
  - ref: "[CITATION-NEEDED: PPE replacement cost for apprentice training operations — safety equipment supplier pricing]"
  - ref: "[CITATION-NEEDED: coal rate $0.35/kg — regional fuel pricing; electricity rate $0.12/kWh — regional utility estimate per SCALES.md §4]"
  - ref: "[CITATION-NEEDED: induction coil MTBF ~1800 hr — manufacturer specification for mid-grade training induction forge unit]"
  - ref: "[CITATION-NEEDED: blower motor MTBF ~1800 hr for coal forge training use — smithing SCHEMA.md §4 baseline range 1500-3000 hr]"
  - ref: "[CITATION-NEEDED: apprentice-made specialty/artistic piece market price $50-150 — inferred from community-smithing cooperative pricing; market survey needed]"
  - ref: "[CITATION-NEEDED: commodity forged-hardware industrial baseline price $15/unit — hardware-store pricing survey]"
  - ref: "[CITATION-NEEDED: workforce-development grant availability for cooperative apprenticeship programs — DOL or state workforce agency data]"
  - ref: "[CITATION-NEEDED: community-college CTE per-student cost $8,000-15,000/yr — NCES or ACTE benchmark data for cost-per-apprentice comparison]"
  - ref: "[CITATION-NEEDED: regional master smith wage survey — confirm $62,000/yr small-city estimate; BLS or regional trade data]"
  - ref: "[CITATION-NEEDED: state cooperative-corporation statute reference; NCBA CLUSA model worker-cooperative articles]"
  - ref: "[CITATION-NEEDED: seasonal throughput pattern for training-facility apprenticeship programs — academic-year cycle data]"
---

## Summary

The Co-op Apprentice Training Forge (forge-009) is a member-owned cooperative training facility whose primary output is journeyman-certified smiths, not commercial product. The cooperative is funded through paid-subscription member dues, discounted apprentice dues, and ancillary sales of apprentice-made specialty and artistic pieces; the master instructor is a worker-member receiving a cooperative stipend. The facility operates a coal-plus-induction hybrid floor — coal for forge-welding practice requiring temperatures not reliably achieved by standard induction units, induction for precision heat-treatment training — across 60–100 m² of multi-station space serving 4–8 concurrent apprentices under a master instructor and 1–2 journeyman assistants. This entry is distinct from forge-003 (shared tool-library) and forge-004 (civic makerspace) because it models the cooperative as employer and trainer simultaneously: the apprentice is a dues-paying worker-member, the instructor holds a stipend-funded ownership stake, and the governance structure is formally calibrated to Ostrom's design principles for a worker cooperative rather than a civic facility with cooperative-analogous access rules.

## Design rationale

The problem this entry solves is the absence of a formal apprenticeship pipeline in the cooperative-ownership catalog. Forge-003 embeds an apprentice path as a secondary feature of a tool-library cooperative; forge-004 places training in a civic facility. Neither models the cooperative as the explicit institutional vehicle for a formal, multi-year, stipend-funded apprenticeship with competency gates, journeyman certification, and governance structures drawn from cooperative-corporation law. The distinction matters because the economic structure is fundamentally different: this cooperative's operating budget must cover instructor stipends and apprentice stipend subsidies from member fees, making the member-dues-to-cost ratio the central financial parameter rather than the commercial throughput of a production shop. The coal-induction hybrid is a pedagogical specification, not a cost optimization — coal is kept because forge-welding is a journeyman-required skill that cannot be taught on standard induction equipment, and removing it from the curriculum would produce a credential gap. This entry also provides the cooperative primary lens with the depth that the catalog has not yet documented: the Mondragon worker-cooperative structure, the US rural electric cooperative's governance traditions, and the anti-romantic treatment of the European guild apprenticeship model are all functional (not aesthetic) inheritances that require named treatment in this entry's niche.

## Historical lineage

Three precedents inform this design. Each requires anti-romantic treatment.

**Mondragon worker-cooperative structure.** The Mondragon Cooperative Corporation (Basque Country, Spain, founded 1956 under Father José María Arizmendiarrieta) is the canonical modern reference for worker-cooperative governance at scale: worker-members hold ownership stakes, receive stipends rather than wages (in the Mondragon formulation), vote on governance decisions, and are represented in a tiered structure of local cooperatives, group cooperatives, and a congress. Mondragon also embedded education within the cooperative system — the Escuela Politécnica Profesional preceded the productive cooperatives, and Mondragon University (now Mondragon Unibertsitatea) remains structurally integrated with the industrial cooperatives. The functional inheritance from Mondragon is: the worker-member legal form, the stipend-versus-wage distinction, the integration of educational function within a productive cooperative, and the annual general meeting with 2/3-vote amendment threshold. What this entry does not inherit from Mondragon is the scale, the industrial scope, or the specific Basque cultural and political context that made Mondragon's founding viable; Mondragon's success was partially contingent on Franco-era restrictions on alternative labor organization that created demand for cooperative alternatives — a condition that does not reproduce in modern US contexts. The governance model is inherited; the historical conditions are not. [CITATION-NEEDED: academic source on Mondragon structure and educational integration.]

**US rural electric cooperative governance.** The rural electric cooperative movement (REA Act 1936; NRECA as the governing association) developed the specific governance forms that this entry borrows: the member-elected board, the annual general meeting with member-vote amendment, the dues-funded operations model calibrated to a service-area membership boundary, and the elected steward (in the rural electric context: an elected board of directors with a specific geographic mandate). The functional inheritance is the governance architecture — not the electricity distribution business. Rural electric cooperatives demonstrated that member-owned utilities with heterogeneous member-bases (farmers, small businesses, households) could maintain stable governance over decades through the annual-meeting mechanism, clear bylaw amendment thresholds, and boundary rules tied to service geography. This entry adapts that architecture to a craft-training context. What it does not inherit is the monopoly-utility context: a craft cooperative operates in a voluntary-membership market, not a territorial franchise — governance rules must account for member exit being cheaper than in a utility cooperative. [CITATION-NEEDED: NRECA governance reference or Zeuli and Cropp 2004.]

**European journeyman mobility tradition (anti-romantic note required).** The Compagnonnage (France), the Wanderjahre (Germany), and related European journeyman-mobility traditions provide the functional template for the 3–4 year structured apprenticeship: competency-gate progression from novice to journeyman, a panel assessment for journeyman certification, and the expectation of post-journeyman travel to broaden craft exposure. The functional inheritance is the training structure, the gate-based progression, and the 36-month timeline cited in Plan B R-19 [CITATION-NEEDED]. What this entry explicitly rejects is the market-protection function that was inseparable from European guild apprenticeship: the historical guild apprenticeship was not merely a skill-transmission vehicle. It was a labor-market cartel — guild membership was required to practice the trade in most jurisdictions, and the seven-year apprenticeship timeline was partly set to restrict labor supply and protect incumbent masters' pricing power. The Compagnonnage and guild systems enforced geographic monopolies, excluded women and certain religious minorities, and were legally abolished in France (Le Chapelier Law, 1791) and Germany precisely because they functioned as market-restricting institutions. The modern cooperative apprenticeship retains the pedagogical architecture (stages, gates, journeyman panel review) while discarding the market exclusion: anyone can practice smithing without guild membership, and the cooperative's journeyman certification is a credential, not a license to trade. This is a genuinely different institutional structure, not a romantic recreation of a guild. Authors and evaluators should resist framing the cooperative training forge as a "guild revival." [CITATION-NEEDED: Epstein 1998 on guild apprenticeship and market protection.]

## Key assumptions

**Capital cost ($80,000–$180,000, mid $130,000):** No published benchmark for a multi-station cooperative training forge was identified at authoring date. The estimate is derived from: coal forge stations (2–3 stations at $3,000–8,000 each), induction units (1–2 mid-grade units at $20,000–40,000 each), multi-station tooling bank ($15,000–25,000 for 6–8 stations), ventilation and exhaust system ($12,000–20,000 for coal-compatible dedicated extraction), and coal storage enclosure ($3,000–8,000). The range reflects the wide variability between refurbished/used equipment (low end) and new purpose-built training-grade equipment (high end). Flagged throughout with [CITATION-NEEDED]; should be replaced with actual procurement data before promotion to `reviewed` status. The mid-high capital skew (mid $130k vs arithmetic midpoint $130k) reflects that training-grade multi-station equipment tends to cluster toward the upper quartile of commercial equipment pricing.

**Throughput (small_work: 3/hr, medium_work: 1/hr, large_work: 0.3/hr):** These are per-shop-day aggregate rates across all apprentice stations, intentionally lower than single-operator journeyman ceiling rates in smithing SCHEMA.md §1 (4–8/hr small, 2–4/hr medium for a journeyman). The depression reflects: apprentice skill-level variance, higher reheat rates, stock waste in learning sequences, and the 30% training_output share that produces no market-equivalent units. The rates are a rough authorial estimate; experimental measurement at comparable training facilities would be required for validation.

**sim_params.throughput_units_equiv_per_year (896):** Fully derived in the frontmatter derivation note. The unit is small-work equivalent; the weighting is stated explicitly per smithing SCHEMA.md §1 E-3 guidance. The 70% saleable-output share is the key assumption: if training_output fraction rises (e.g., the cooperative runs a more intensive first-year cohort), throughput_units_equiv falls and variable_cost_per_unit rises. The 70/30 split is an authorial estimate calibrated to the product_mix specification.

**Downtime fraction (0.18):** The summer-shutdown / cohort-transition weeks are the dominant downtime driver (~11–15% of shop-weeks per year if 6–8 weeks of reduced operation are assumed). Equipment failures (induction coil at ~20 months, blower motor at similar horizon) add ~3–4%. Administrative scheduling gaps add ~2%. Total 16–21%; 0.18 is the central estimate. The worst-month fraction (0.4×) is consistent: a 4-week summer shutdown at 40% capacity is approximately 3 weeks of effective lost output, consistent with ~6% seasonal downtime contribution.

**Instructor stipend ($62,000/yr):** Anchored to SCALES.md §3 small-city skilled-trades median. The cooperative worker-member stipend structure may allow a modest discount below market wage in exchange for ownership stake and mission alignment; $62,000 is nonetheless at the lower bound of what a qualified master smith-instructor will accept. The cooperative faces a structural financial challenge: the instructor stipend alone ($62,000) exceeds the member-dues floor revenue ($12,000–20,000/yr from 30–40 members). Grant funding and ancillary sales are required to close the gap; the entry treats this as a known financial risk rather than a design flaw.

**Ancillary sales pricing ($50–80–150/unit):** Flagged as `inferred` in pricing_validation. No direct market survey was conducted. The $80/unit mid-price is a rough comparables estimate from community-smithing cooperative output pricing; the $15 industrial baseline is cited for the commodity-comparison framing. Ancillary sales are not the viability anchor; the entry's financial case rests on member dues plus grant funding.

## Known risks and failure modes

**Regulatory risks:** Coal combustion in a multi-apprentice training setting creates the intersection of OSHA general-industry hot-work standards (29 CFR 1910.252), local air-quality permit requirements for coal-burning facilities, and state apprenticeship-authority oversight that varies substantially by jurisdiction. Some states require registered apprenticeship programs (with Department of Labor oversight) before paid apprentice stipends can be legally offered; failure to register before paying stipends creates employment-law exposure. Liability and insurance: a cooperative with apprentices (some potentially under 18 with parental consent) requires substantially higher general-liability and workers'-compensation coverage than a commercial shop; insurance cost is a material line item not captured in the annual_maintenance or consumables fields and should be budgeted separately before first cohort intake. The liability exposure for an apprentice injury during training is the single largest unquantified risk in this entry.

**Labour pipeline risks:** The master instructor is the cooperative's critical single point of failure. Unlike a civic facility (forge-004) where the municipality backstops continuity, this cooperative's institutional survival depends on the instructor relationship remaining intact. The journeyman-assistant pipeline mitigates this after the first cohort cycle but provides no short-term succession. The Ostrom Principle 7 federation (instructor-sharing with peer cooperatives) is the structural mitigation — but it is only partially addressed (marked as [1,2,3,4,5,6,7] with the caveat that formal federation depends on peer-cooperative existence in the region). A cooperative that launches without a regional peer network has weaker succession protection than the frontmatter suggests. The European journeyman tradition's instructor-mobility norm is a cultural mitigation, not a contractual one; it requires a dense regional network of cooperatives that may not exist at launch.

**Supply chain risks:** The induction coil is the critical single-supplier dependency (21-day lead time at specialist-only serviceability). The coal supply chain is generally more resilient at town/small-city scale (regional distributors; multiple suppliers), but coal quality variability (sulfur content, lump size) affects forge-welding success rates and apprentice training outcomes — a supply disruption that forces low-quality coal use degrades the training program. The worst-case consumables lead time of 45 days is the primary tail risk; the cooperative should maintain safety stock of induction coil spares (difficult given cost) or a service agreement with a specialist to reduce lead time. Coal storage must comply with OSHA fire-separation requirements and local fire code; failure to maintain compliant storage is both a regulatory risk and a practical supply-continuity risk.

**Financial viability risk:** The structural gap between member-dues revenue floor (~$12,000–20,000/yr) and instructor-stipend cost alone ($62,000/yr) means the cooperative cannot survive on dues alone. This is the entry's primary financial weakness and should be named explicitly. The design assumes grant funding and ancillary sales close the gap; both are uncertain. Workforce-development grants are competitive and non-recurring; a cooperative that structures its budget around grant revenue without a credible path to dues-and-sales sustainability is fragile. The cooperative should plan for a 3-year grant-dependent launch phase transitioning to a dues-dominant steady state as the member base grows; failure to execute this transition is the most likely first-year financial failure mode after instructor departure.

## Iteration log

- 2026-04-18: v0.1 — initial creation; forge-009 Co-op Apprentice Training Forge. COOP-PRIMARY entry per Plan C Task 11 specification. All three lens_context blocks populated (market poor with ancillary-sales pricing present and explicit "ancillary, not primary" note; cooperative good as primary lens with Ostrom 1–7, worker-member legal form, dues structure, graduated sanctions, conflict resolution, member_amendment_process, scale_fit_note; civic marginal with workforce-development framing, staffing_model, benchmark_comparison vs CTE cost-per-student, three civic_externalities). Anti-romanticism applied to all three inspirations: Mondragon (Basque political context not reproduced), US rural electric (monopoly-utility context not inherited), European guild apprenticeship (market-protection function explicitly named and discarded). Liability/insurance risk named in Known Risks. Four-stage apprentice_path with competency gates; time_to_independent_operation anchored to Plan B R-19 European figure with [CITATION-NEEDED]. Financial viability gap named explicitly. Twenty-one [CITATION-NEEDED] flags placed over fabrication.
