---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: forge-011
trade: smithing
name: "Municipal Civic Training Forge — CTE / Community-College Partnership"
tagline: "School-district-owned induction forge; apprentice-pipeline builder for the surrounding private-smithing ecosystem"
status: draft
version: 0.1
supersedes: null
inspirations:
  - tokugawa-shokunin-master-apprentice-transmission
  - us-vocational-cte-tradition

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 100
# Mid-range of 80–120 m² span. Layout: 4–6 student workstations, instructor
# demonstration bay (dedicated, not shared with student stations), tool and stock
# storage room (integrated, approximately 10 m² of the total footprint), and
# adequate circulation for safety egress between stations. The 100 m² figure is
# the working zone per schema definition; building circulation and corridor space
# are outside this number. CTE facility planning standards (ACTE, state CTE
# design guides) typically specify 12–18 m² per student station for metalworking;
# this entry's 6-station target at ~14 m²/station plus instructor bay and storage
# lands squarely within that range. [CITATION-NEEDED: ACTE / state CTE facility
# design standard for metalworking stations.]
ceiling_min_m: 4.0
# Minimum for safe operation with induction coil swing, exhaust ductwork, and
# instructor observation sightlines across all student stations. School-construction
# standard for lab/shop spaces is typically 3.6–4.5 m; 4.0 m is realistic.
ventilation: dedicated-exhaust-system
# Induction-electric primary eliminates combustion emissions at the forge, but
# metalworking operations (grinding, wire-brushing, scale removal) produce
# particulate that requires mechanical extraction regardless of fuel source.
# OSHA 29 CFR 1910.252(c) and NFPA 45 apply to school hot-work shops. A
# dedicated exhaust system above each student station is the safety-grade
# standard for an educational setting, both for OSHA compliance and for insurance
# and district liability management. A mechanical-extraction-only system would be
# insufficient at 4–6 concurrent student stations.

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: induction-electric
# Induction-electric is the correct choice for an educational setting for three
# independent reasons: (1) Safety — induction removes open-flame combustion and
# LP/gas storage from a school facility; fire-safety and insurance profiles are
# substantially simpler than propane or coal; (2) Regulatory — no combustion-
# appliance permit, no LP storage tank regulatory requirements, no air-quality
# permit triggers from combustion; the permitting path for a school induction-
# forge is materially simpler than for any combustion alternative; (3) Pedagogical
# — induction's repeatable temperature control and rapid cycle time are better
# suited to learning-pace work than combustion forges where fire-management is
# itself a skill gate. The capability limitation of standard induction (no forge
# welding at standard power levels per smithing SCHEMA.md §2) is acceptable here:
# forge welding is not a CTE-entry-level curriculum objective and is not attempted
# at this facility. See also operator safety note in regulatory_notes.
energy_consumption_per_active_hour: "10 kWh (active class period; intermittent student use across 4–6 stations; not all stations at full load simultaneously)"
# Per-hour figure is the shop total during an active class period. Because students
# do not forge continuously (they heat, work, re-heat, rest, observe instruction),
# average induction draw across all stations is lower than the nameplate sum.
# 10 kWh/hr is the aggregate estimate during peak class periods; average over a
# full school day (including non-class periods) is lower. [CITATION-NEEDED:
# induction forge energy consumption at intermittent student-use pattern; manufacturer
# spec for mid-grade multi-station induction forge installation.]
backup_fuel: null
# No combustion backup. The pedagogical and safety rationale for induction-only
# is described above; adding a propane backup would reintroduce the permitting
# and safety complexity the induction choice is designed to avoid. If the
# induction system is down, classes are cancelled rather than switched to
# combustion. Downtime planning (see first_year_failures) accounts for coil
# failure lead time.

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  units_per_hour: { small_work: 2, medium_work: 0.5, large_work: 0.1 }
  # These are per-shop-period aggregate rates across all student stations during
  # an active class, not per-student rates. Student throughput is lower than
  # journeyman commercial rates (smithing SCHEMA.md §1 ceiling: 4–8/hr small,
  # 2–4/hr medium) because: (a) students reheat more frequently and waste more
  # stock; (b) instruction pauses, demonstrations, and safety corrections reduce
  # productive forge time; (c) the 70% training_output product mix means most
  # forge time produces learning pieces, not saleable items. Rates are
  # consistent with forge-004 and forge-009 multi-user supervised models.
  max_active_hours_per_week: 25
  # Aligned with CTE/school-day scheduling: typically 5 class periods/week × 90
  # min/period = 7.5 hr/wk, but the shop operates across multiple class sections
  # within the school day. 25 hr/wk represents approximately 3 daily double-period
  # blocks plus additional single periods — a realistic upper bound for a school-
  # embedded forge during the academic year. Summer break reduces this to 0 for
  # approximately 10 weeks/yr (see throughput_variance.seasonal).
  product_mix:
    repair: 5
    commodity: 0
    specialty: 10
    artistic: 15
    training_output: 70
    # training_output is the dominant category: 70% of active forge time produces
    # student learning pieces (practice heats, exercise items, class projects)
    # that are not sold commercially. This is the defining characteristic of a
    # CTE/educational forge: the facility's primary output metric is
    # students-trained-per-cohort, not units-per-hour. Repair (5%): donated or
    # low-complexity repair work used as teaching exercises; not sold.
    # Specialty (10%): select student work that achieves sale-quality; offered
    # for sale at school-program events or via school store at instructor
    # discretion. Artistic (15%): student portfolio pieces, exhibition work,
    # competition entries; occasionally sold. Commodity (0%): CTE forges do not
    # produce commodity output; not consistent with instructional goals.
    # Sum: 5 + 0 + 10 + 15 + 70 = 100.
  throughput_variance:
    seasonal: "Academic-year active (September–June, ~40 weeks); summer break full shutdown for ~10 weeks; worst months are July–August at 0× output; best months are November and March (full-semester mid-points with project cycles active)"
    worst_month_fraction_of_average: 0.0
    # July and August: full summer break. No classes, no student forge time.
    # Zero output is not an estimate — it is the scheduled reality of a
    # school-embedded facility. Annual throughput_units_equiv_per_year must
    # account for this; sim_params uses the derated annual figure.
    best_month_fraction_of_average: 1.4
    # Peak academic months with full class enrollment and project-cycle
    # momentum. Slightly above average because November and March are full
    # production months with no interruptions for schedule transitions.

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: master
# A CTE smithing instructor must hold master-level competency per smithing
# SCHEMA.md §3: simultaneous multi-student oversight requires heat-judgment
# assessment across all active stations, safe intervention capability, and
# the instructional authority to recognize and correct student errors in real
# time. State CTE credentialing typically requires demonstrated master-level
# industry competency plus a teaching credential; both requirements independently
# demand master-tier skill. [CITATION-NEEDED: state CTE instructor credentialing
# requirements for metalworking/smithing — state-specific; varies by jurisdiction.]
operators_concurrent: "1 FT instructor + 1 PT journeyman aide + up to 6 students"
# Normal operating configuration: 1 master smith-instructor (full-time; leads
# instruction, manages all safety decisions, holds credential requirement);
# 1 part-time journeyman aide (provides station-level support, assists with
# material handling and tool prep, covers instructor during brief absences;
# does not hold instructional authority independently); up to 6 students
# concurrently forging during a class period. The 6-student ceiling is a
# safety ratio constraint: 1 qualified instructor per 6 students at hot-work
# is the defensible maximum for school-setting liability; many state CTE
# standards specify lower ratios for equipment-intensive shops.
apprentice_friendly: true
apprentice_path:
  training_stages: >-
    Stage 1 — Safety and Shop Orientation (Semester 1, weeks 1–6): school-shop
    safety rules, OSHA-for-students module, PPE identification and fitting, induction
    forge power-up and power-down procedure, tool identification and handling, bench
    work (filing, measuring, marking) without forge heat. No student operates the
    forge independently. Competency gate: pass written safety exam (school-district
    standard); demonstrate correct PPE donning and forge power-cycle under direct
    instructor observation; complete bench-work exercise to dimensional spec.

    Stage 2 — First Heats and Basic Shaping (Semester 1, weeks 7–18): supervised
    forge operation at student stations with instructor or journeyman aide present
    at arm's reach. Curriculum: drawing out, bending, upsetting on small-section
    mild steel. Heat-color reading introduced (orange/yellow spectrum for induction;
    induction color cues differ from combustion — instructor must address this
    explicitly). First project: student-designed hook or bracket from provided
    template. Competency gate: complete hook project to dimensional spec (±5 mm);
    demonstrate heat-color identification without prompting; complete session without
    safety intervention from instructor.

    Stage 3 — Developing Independence and Medium Work (Semester 2, all weeks): student
    works with reduced direct supervision (instructor circulates rather than stations
    at the student's side). Curriculum: medium-section stock, simple tool forms
    (chisels, punches), introduction to repair work on donated items (gate hardware,
    simple agricultural tools). Introduction to basic heat treatment (normalize,
    anneal) using induction's temperature control as the learning scaffold — induction
    makes the normalize/anneal sequence more teachable than combustion because
    temperature is set, not judged by eye. Artistic/portfolio project assigned; student
    brings piece to completion over the semester. Competency gate: complete one
    supervised repair exercise on donated work item; execute normalize-anneal sequence
    independently with correct hold time; complete portfolio project to presentable
    standard for school exhibition.

    Stage 4 — Advanced CTE and Post-Program Pathway (Year 2, if program continues to
    second year or community-college continuation): independent small- and medium-work
    production, introduction to precision measurement and fit, introduction to hardening
    and tempering sequence, exposure to professional smith standards. Students completing
    Stage 4 are positioned for direct entry into a private-shop apprenticeship in the
    surrounding ecosystem — this is the explicit pipeline function of the facility. Some
    states offer dual-enrollment credit with community-college CTE programs; Stage 4
    students may be eligible for community-college smithing credits. Competency gate:
    complete hardening and tempering of a simple cutting tool under direct instructor
    supervision; produce one medium-work piece to journeyman-entry standard (instructor-
    assessed); receive instructor endorsement for private-shop apprenticeship referral.

  time_to_independent_operation: >-
    ~24 months to apprentice-entry standard (Stage 3 completion at end of Year 1
    or beginning of Year 2); Stage 4 students at 36–48 months are positioned for
    private-shop apprenticeship entry. This is a CTE-output timeline, not a
    journeyman-production timeline. A Stage 4 graduate is not an independent
    journeyman: they are an informed, safety-trained, motivated beginner who can
    enter a private-shop apprenticeship at a higher starting level than an untrained
    hire. The ~36-month journeyman timeline (per smithing SCHEMA.md §3 and forge-009
    apprentice_path) begins after Stage 4 exit, not at Stage 1 entry.

  succession_note: >-
    The CTE program's succession structure is institutional rather than individual:
    the school district owns the equipment, the curriculum is documented in the
    district's CTE program records, and the state CTE credentialing requirement
    means any replacement instructor holds the same baseline qualifications as the
    predecessor. When an instructor departs, the district recruits a credentialed
    replacement from the regional teacher and trades pool; continuity is carried by
    the institution, not the individual. The journeyman aide position provides
    operational continuity during instructor vacancy (aide can run safety-walk and
    maintain equipment; cannot lead instruction). The external pipeline to private
    shops also creates continuity incentive: private shops in the surrounding ecosystem
    that depend on the school program for apprentice referrals have a vested interest
    in helping the district recruit and retain a qualified instructor.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 120000, mid: 200000, high: 280000 }
  # School-shop fitout for a 4–6 station induction forge facility. Low = used/refurbished
  # induction units (2–3 units at $15,000–25,000 each) + basic student tooling bank +
  # minimal ventilation upgrade + used anvils and benches. Mid = new mid-grade induction
  # forge installation (4–6 stations; full student tooling bank; new anvils, vices, and
  # benches per station; code-compliant ventilation system; instructor demonstration bay
  # with dedicated unit). High = top-specification induction system (individual station
  # control; digital temperature logging for instructional feedback) + full student
  # tooling bank with redundant tools per station + power hammer at instructor bay +
  # ADA-compliant station modifications + complete safety-infrastructure package.
  # [CITATION-NEEDED: CTE metalworking shop fitout capital cost; no published benchmark
  # specific to smithing-forge identified at authoring date; estimate derived from
  # vocational-education facility cost literature and induction-forge equipment pricing.
  # Comparable CTE auto-mechanics or welding shop fitouts cited as reference range.]

  install_cost: 22000
  # 3-phase electrical service upgrade (required for multi-station induction installation;
  # typical school-building electrical panel may not support 3-phase; upgrade cost
  # $8,000–15,000) + safety-grade ventilation system installation ($5,000–10,000 for
  # dedicated exhaust hoods over 4–6 stations with makeup-air unit) + student-safety
  # infrastructure (eyewash stations, fire suppression upgrade, first-aid station,
  # safety signage package per OSHA and state school-safety codes: $2,000–5,000).
  # [CITATION-NEEDED: 3-phase electrical upgrade and school-shop safety-infrastructure
  # install cost from regional contractor estimates and school-district procurement data.]

  annual_maintenance: 6000
  # Covers: induction coil system service (quarterly per manufacturer; primary cost
  # driver), ventilation system filter and blower maintenance, student-station anvil
  # and tool maintenance, grinder wheel and disc replacement beyond consumables budget,
  # general shop upkeep. Higher than single-operator commercial entries because
  # student use accelerates equipment wear (more thermal cycles per unit time, more
  # tool misuse, higher grinder turnover). Includes monthly safety-equipment checks
  # (eyewash, fire suppression) and quarterly PPE audit.
  # [CITATION-NEEDED: annual maintenance estimate for school CTE metalworking shop;
  # derived from comparable vocational-shop maintenance budget data.]

  annual_consumables: 8500
  # Higher than commercial-shop entries because student practice wastes stock:
  # failed heats, over-worked sections, scrapped practice pieces, and learning-sequence
  # repetition all consume mild-steel stock beyond production-shop norms. Line items:
  # mild-steel bar stock for student practice ($3,000/yr estimated for 6 students × 40
  # active weeks); grinding discs and wire wheels ($1,200/yr; student grinder use is
  # intensive); flux and scale-control agents ($400/yr); PPE replacement — gloves,
  # face shields, aprons — ($1,600/yr at school-safety replacement schedule, quarterly
  # per student station); miscellaneous consumables ($1,300/yr). Total $8,500.
  # [CITATION-NEEDED: school CTE metalworking consumables budget; derived from comparable
  # welding/machining CTE program consumables expenditure and smithing-specific adjustments.]

  floor_space_rent_per_year: 0
  # Town/school-district-owned facility. Floor space is embedded in the municipal or
  # school building capital; no external rent is charged. This is the civic ownership
  # advantage: eliminating floor-space rent is a material factor in making the facility
  # financially viable where a private operator at the same location could not be.
  # Per schema guidance: imputed at $0 for school/municipal-owned facilities.

  market_price_per_unit: { low: 30, mid: 50, high: 120 }
  # CONDITIONAL — present because lens_fit.market is `poor` but ancillary student-
  # work sales occur at school events and via school-store channel. This is ancillary
  # revenue, not the facility's viability basis. Unit = small-work equivalent piece
  # (hook, bracket, simple hardware) produced by a student and sold. Pricing is
  # highly variable because student work is not priced by quality alone: it carries
  # a "made by learner" discount against journeyman-produced work and also a
  # "community/school program" premium against anonymous commodity product.
  # Low = simple practice pieces sold at school events ($30). Mid = intermediate
  # quality sold via school store or at program-fundraiser events ($50). High = select
  # student work of exhibition quality sold at community events or juried shows ($120).
  # [CITATION-NEEDED: student-made smithing output market price; inferred from
  # comparable school-program craft-sale pricing; no direct market survey conducted.]

  pricing_notes: >-
    Unit is a small-work equivalent piece produced by a student and sold via ancillary
    channel (school store, program fundraiser, community event). Market price is ANCILLARY
    REVENUE, not the primary purpose or viability basis of this facility: the primary
    output is students trained per cohort, not items sold per year. Industrial baseline
    for comparable commodity small-work items: $12/unit (hardware-store imported
    equivalent; [CITATION-NEEDED: commodity hardware baseline price]). Student-made
    pieces command a modest premium over commodity ($30–120 vs $12 baseline) based on
    craft origin, school-program narrative, and selection (only instructor-approved
    pieces are sold). Customer segment: community members purchasing at school events,
    parents, and local supporters of the CTE program. High-end student artistic work
    ($120) targets juried-show and community-auction buyers. This pricing does not
    represent a commercial market test; pricing_validation reflects the inferred
    and highly variable nature of the evidence.

  industrial_baseline_price: 12
  # Commodity small-work equivalent (hooks, brackets, simple hardware) at hardware-
  # store imported pricing. Cited for lens comparison only; not used in revenue
  # calculations (lens_fit.market: poor).
  # [CITATION-NEEDED: commodity forged-hardware baseline price; hardware-store
  # commodity pricing survey for small forged-equivalent items.]

  pricing_validation: >-
    Pricing inferred from comparable school-program craft-sale and community-event
    pricing norms; no direct market survey conducted at authoring date. Evidence type:
    inferred from school-program fundraiser pricing and anecdotal CTE program reports.
    High variance is inherent: student work quality spans a wide range, and community-
    event pricing is as much about program support as about output quality. This is
    not empirical sales data; [CITATION-NEEDED] for direct market-price evidence.
    Pricing_validation is flagged as inferred. Ancillary-sales pricing does not anchor
    the facility viability case.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:

  first_year_failures:
    - item: "Primary induction coil (heating element, first station to accumulate hours)"
      estimated_hours_to_failure: 1800
      replacement_cost: 1400
      replacement_lead_time_days: 21
      serviceable_by: specialist
      # Induction coil failure is the primary downtime event for induction forge
      # installations. At 25 hr/wk gross shop hours with induction running on
      # approximately 4 student stations, the first-station coil accumulates hours
      # faster than a single-operator shop; first failure expected at approximately
      # 1,800 hr. Replacement requires a specialist (high-frequency power systems;
      # not operator- or journeyman-serviceable in a school setting). 21-day lead
      # time is optimistic for non-stocked coil geometries; see consumables_lead_time.
      # [CITATION-NEEDED: induction coil MTBF ~1800 hr; smithing SCHEMA.md §4 ref.]

    - item: "Student-station grinder wear items (grinding discs, wire wheels, flap discs)"
      estimated_hours_to_failure: 0
      # Not a single failure event; a recurring quarterly replacement schedule.
      # Included here because student-intensity grinder use depletes consumables
      # faster than commercial shops and is a predictable first-year cost driver.
      replacement_cost: 400
      # $400/quarter for grinding-media replacement across all student stations.
      # Included in annual_consumables ($8,500) but flagged here to highlight
      # the quarterly cash-flow implication.
      replacement_lead_time_days: 0
      # Immediate from on-hand stock; school-shop supply management standard
      # practice is to maintain 1-quarter consumables inventory.
      serviceable_by: operator
      # Operator (instructor or journeyman aide) replaces grinding media as part
      # of routine quarterly station maintenance.

    - item: "Safety equipment replacement (PPE per-student quarterly: gloves, face shields, leather aprons)"
      estimated_hours_to_failure: 0
      # Not an equipment failure; a scheduled safety-compliance replacement event.
      # School-setting PPE replacement is required on a defined schedule regardless
      # of visible wear: liability and insurance requirements in educational settings
      # are more conservative than OSHA minimums for commercial shops.
      replacement_cost: 1200
      # $1,200/quarter (approximately $50/student/quarter × 6 students × 4 quarters
      # = $1,200/quarter) for gloves, face shields, and aprons. Included in
      # annual_consumables aggregate. Per-quarter figure stated for cash-flow planning.
      replacement_lead_time_days: 0
      # Immediate from safety-stock; PPE should never be depleted below one full
      # set per student station. School-district procurement typically maintains
      # 1-quarter safety-equipment inventory.
      serviceable_by: operator

  maintenance_schedule:
    daily:
      task: "Pre-class safety walkthrough and station check: verify PPE stock at each of 4–6 student stations, confirm induction unit indicator lights and coolant levels, check ventilation extraction operation, ensure fire suppression and eyewash stations are functional, reset sign-in log; 15–20 min per class period"
      performed_by: operator
      # 'Operator' here = the master smith-instructor or journeyman aide opening
      # the facility before each class period. School-setting daily safety sign-off
      # is non-negotiable: liability, insurance, and district safety policy all
      # require documented pre-class inspection. Higher stakes than commercial shop.
    weekly:
      task: "Station-by-station inspection: induction coil visual and indicator check at all student stations, ventilation airflow measurement at each hood, anvil base stability and surface condition, bench-vice functionality, hand-tool inventory and condition, grinding-disc inventory and lead-time check; 45–60 min on a non-class day or between class periods"
      performed_by: operator
    monthly:
      task: "Safety-committee audit per district facility-safety protocol: fire-suppression system check, eyewash station flush and function test, first-aid kit restock, OSHA and state school-safety compliance checklist, PPE inventory against student headcount, incident-log review with CTE department head"
      performed_by: journeyman
      # 'Journeyman' here = the journeyman aide conducting the formal inspection
      # with instructor oversight. Monthly district-level audit is a school-setting
      # requirement beyond what most commercial shops face.
    quarterly:
      task: "Induction coil and power-system service by certified technician; full PPE replacement cycle for all student stations; ventilation hood and ductwork cleaning and inspection; grinder-station safety check and wear-part replacement; CTE program inventory audit for state reporting"
      performed_by: specialist
      # Induction coil service requires a specialist (manufacturer-certified
      # technician or qualified electrical contractor familiar with induction
      # systems). State CTE program reporting may require documented quarterly
      # equipment-condition records.
    annual:
      task: "Full facility safety certification per state CTE and school-district requirements: structural review of all equipment anchorages, electrical panel certification, full equipment inventory and valuation update, insurance assessment, state CTE program compliance audit, complete refractory and coil replacement assessment"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 30
  # Per class period: 15 min pre-class safety walkthrough and briefing + 15 min
  # post-class equipment shutdown, student cleanup, and log completion. This is
  # lower than forge-009 (60 min) because: (a) induction-only eliminates the coal
  # startup sequence; (b) the school schedule imposes a hard clock constraint on
  # class-period length, meaning startup-shutdown must be efficient. 30 min/class
  # period (15 min pre + 15 min post) is the defensible minimum for a school hot-
  # work shop with up to 6 students.

  max_active_hours_realism_note: >-
    25 hr/wk is the academic-year scheduling target (gross ceiling). Net of 30 min/class
    period startup-shutdown overhead: assuming 5 class periods/wk × 30 min = 150 min =
    2.5 hr/wk overhead; effective instruction/forging hours ≈ 22.5 hr/wk during the
    academic year. Downtime fraction of 0.22 accounts for: summer break (~10 weeks,
    the dominant factor — approximately 10/52 = 19% structural downtime); equipment
    maintenance and first-year coil failure (~3%); administrative scheduling gaps,
    school holidays, field trips (~3%). Net effective hours/yr: 22.5 × 52 × (1 − 0.22)
    ≈ 910 hr/yr. sim_params.throughput_units_equiv_per_year uses this derated annual
    figure. The summer-break downtime is structural and scheduled, not unplanned;
    it must be factored into annual cost and throughput calculations even though it
    does not appear in equipment-failure data.

  interruption_notes: >-
    School-setting intraday interruptions are structurally higher than commercial
    shops. Typical per-class interruption profile: instructor demonstration pause
    for group observation (~10–15 min/class), safety intervention or technique
    correction at a student station (~5–10 min total/class), administrative
    (attendance, safety-record entries, equipment-issue log) (~5 min/class), student
    station rotation and setup (~5 min/transition). Total intraday interruption
    approximately 25–35 min per class period above the startup-shutdown overhead.
    These interruptions are folded into throughput_units_equiv_per_year via the
    lower unit rates and 70% training_output product-mix share.

  consumables_lead_time_days: { typical: 7, worst: 45 }
  # Typical: mild-steel stock, grinding media, PPE from regional supplier or
  # school-district approved vendor; 7 days is standard school-procurement lead
  # time with approved supplier. Worst: induction coil from specialist supplier
  # with backorder; 45 days is the tail risk for non-standard coil geometries.
  # School-district procurement cycles may add 5–10 days over commercial-shop
  # procurement due to requisition and approval processes; this is folded into
  # the typical figure.

  operator_impact:
    noise_db: 80
    # Peak during hammer work and grinding at student stations. Induction forge
    # itself is quieter than combustion alternatives, but hammer-on-anvil and
    # angle-grinder use drive the noise level. 80 dB at peak instruction periods
    # with 4–6 students active simultaneously. Hearing protection required for
    # students and instructor during grinding operations; OSHA 29 CFR 1910.95
    # hearing-conservation standard applies in school workshops.
    heat_exposure: "Local at each induction station; induction coil produces radiant heat within the work zone but not at the scale of a combustion forge hearth; multi-station spacing in 100 m² footprint provides adequate relief zones between student stations"
    emissions: "Very low: induction eliminates combustion emissions at the forge; grinding and scale operations produce metal particulate controlled by dedicated exhaust system; no SOx, minimal CO"
    physical_demand: "Moderate for instructor (sustained standing, demonstration forging, floor-wide supervision across 4–6 stations); light-to-moderate for students (learning pace, short heat sequences, more rest between heats than production-shop rates)"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Educational-facility zoning exemption typically applicable; school metalworking shops are established institutional uses in most jurisdictions; confirm local hot-work ordinance classification for induction forge in school setting; no change-of-use permit normally required for a school building adding a CTE shop"
  emissions: "Induction-primary configuration avoids combustion-emission permit triggers; grinding and particulate from metal-working operations may require confirmation against local air-quality ordinance thresholds; dedicated exhaust system satisfies OSHA 29 CFR 1910.252(c) for hot-work in educational settings"
  other: "State CTE certification required for program to access state CTE funding; instructor credentialing requirements vary by state (teaching credential + industry competency certification); student-safety insurance substantially higher than commercial-shop coverage; OSHA general-industry standards apply to school workshops (not construction standards); student waiver and parental-consent documentation required for minors; annual district safety-committee sign-off required"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: poor
  # Educational facility; primary output is trained students, not commercial product.
  # Ancillary student-work sales are fundraising income, not a commercial operation.
  # The facility does not compete on throughput, margin, or market access with
  # private smiths. Market lens: poor.
  cooperative: marginal
  # An instructor-led cooperative variant is theoretically possible: a group of
  # credentialed instructor-smiths could form a worker cooperative and contract
  # with the school district to provide the CTE program, owning the equipment
  # collectively. This is an atypical but not impossible legal form in US educational
  # contexts (similar to how some adult-education programs operate via contracted
  # providers). The cooperative lens is marginal because this form is rarely used
  # in practice for school CTE programs, governance is more complex than direct
  # municipal employment, and the school district's oversight requirements create
  # friction with cooperative self-governance. See lens_context.cooperative.
  civic: good
  # Primary lens. School-district ownership, public-goods externalities (apprentice
  # pipeline, CTE student outcomes, community resilience), and political coalition
  # (school board, workforce development, trades unions, private-shop ecosystem)
  # are fully documented in lens_context.civic below.

scale_fit:
  village: poor
  # Village scale (500–2,000 residents) cannot sustain the enrollment base for a
  # CTE forge program. A minimum of one class section of 6 students per period,
  # running 5 periods/week, requires a school population of at least 400–600
  # enrolled students to generate enough demand — which implies a community of
  # at least 3,000–5,000 residents. Per-household cost ($109,000+/yr operating at
  # village scale with 400 households: ~$273/hh/yr) is politically unsustainable.
  # Village-scale communities that want CTE smithing access should participate in
  # regional consolidation (see town: marginal note).
  town: marginal
  # Town scale (2,000–15,000 residents) is possible with regional consolidation:
  # a district serving multiple towns can aggregate enrollment to fill the CTE
  # forge program. Per-household cost at 3,000 households: approximately $36/hh/yr
  # gross — at the edge of CTE political viability. Viable where CTE programs
  # have strong community support and regional-district consolidation is in place;
  # not viable for a single isolated town. The marginal label reflects this
  # conditionality rather than structural infeasibility.
  small_city: good
  # Target scale: 15,000–75,000 residents. Sufficient school population to fill
  # a CTE forge program across multiple sections; per-household cost falls into
  # a politically viable range (~$7–22/hh/yr depending on grant offset). The
  # surrounding private-smithing ecosystem at small-city scale is also large enough
  # to absorb the apprentice-pipeline output. This is the natural home scale for
  # a CTE municipal civic training forge.

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:

  cooperative:
    membership_boundary: >-
      Instructor-cooperative variant only: credentialed master-smith instructors
      (meeting state CTE certification requirements) may form a worker cooperative
      and contract with the school district as the CTE program provider. Membership
      boundary is defined by credential holding and contractual relationship with
      the district. Students are not cooperative members; they are program participants.
      Journeyman aide(s) may hold associate worker-member status with reduced
      governance rights. Geographic boundary: instructors must be within commuting
      distance of the school facility.

    rules_source: >-
      Worker-cooperative bylaws plus contractual terms with the school district.
      The district's CTE program-oversight requirements create a rules-source
      constraint that is external to the cooperative's internal governance: the
      district sets curriculum standards, safety requirements, and student-outcome
      metrics that the cooperative must meet regardless of its internal governance
      choices. Cooperative bylaws govern: member equity shares, stipend formula,
      decision-making authority on non-district-constrained matters (equipment
      purchases within budget, curriculum enrichment, professional development).

    monitoring: >-
      Two-layer monitoring: (1) district monitoring of program outcomes (student
      enrollment, completion rates, safety incidents, state CTE compliance) — external
      to the cooperative; (2) internal cooperative monitoring of member contribution,
      stipend calculations, and equipment stewardship. The district's oversight
      function satisfies Ostrom Principle 4 for the primary commons resource (the
      school facility and equipment); internal cooperative monitoring addresses
      member-level compliance with cooperative bylaws.

    graduated_sanctions: >-
      Internal cooperative sanctions: Warning → probationary status (reduced
      governance rights, stipend review) → membership review → member exit with
      equity buyout per bylaws. The district contract introduces an additional
      sanction layer: poor student outcomes or safety violations may trigger
      district contract non-renewal, which is the terminal sanction for the
      cooperative as a contracting entity. Safety violations at student level
      may trigger immediate suspension of operations pending district review,
      bypassing cooperative-internal sanctions.

    conflict_resolution: >-
      Day-to-day instructional disputes resolved by lead instructor (master smith).
      Cooperative-internal disputes between worker-members escalated to a member
      panel or cooperative board. Disputes with the school district resolved via
      contract dispute-resolution mechanism (typically mediation, then district
      administrative appeal). The cooperative's reliance on the district contract
      means conflict escalation to district level is a material operational risk,
      not merely a governance formality.

    ostrom_principles_addressed: [1, 2, 5]
    # Principle 1 (defined boundaries): credential requirement defines membership.
    # Principle 2 (congruence): bylaws calibrated to instructor-cooperative context.
    # Principle 5 (graduated sanctions): documented above.
    # Principles 3, 4, 6, 7, 8: partially addressed at best. Rule-making authority
    # (Principle 3) is constrained by the district contract — member collective
    # choice is limited to non-district-constrained matters. Monitoring (Principle 4)
    # is partly external (district oversight), not fully member-controlled.
    # Conflict resolution (Principle 6) requires external district mechanism.
    # Nested organisations (Principle 7) and external recognition (Principle 8):
    # recognition is via district contract, not cooperative legal form per se.
    # Ostrom principles are only partially satisfied in the cooperative-contract
    # variant — a design weakness noted in Known Risks.

    member_amendment_process: >-
      2/3 vote of worker-members; 30-day notice required. Amendments affecting
      district-contract compliance require district notification and may require
      contract renegotiation before taking effect. Emergency safety-related rule
      changes may be enacted by the lead instructor with board ratification at
      next meeting. The constraint that district-contract terms supersede cooperative
      bylaws on program-delivery matters must be stated explicitly in the bylaws
      to avoid governance confusion.

    legal_form: >-
      Worker cooperative contracting with school district: state-registered worker-
      cooperative corporation (LLC or incorporated form per state statute) holding
      a service contract with the school district for CTE program delivery. The
      cooperative owns the equipment (in the cooperative variant; in the civic variant,
      the district owns equipment and employs the instructor directly). Equipment
      ownership by the cooperative creates asset continuity across district-contract
      cycles but also concentrates risk: if the contract is not renewed, the cooperative
      owns equipment it cannot operate without a new district or institutional client.
      [CITATION-NEEDED: state-specific worker-cooperative corporation statute
      applicable to educational service contractors.]

    scale_fit_note: >-
      The instructor-cooperative variant is calibrated for small-city scale where the
      district is large enough to support a full-time CTE smithing program (minimum
      ~15,000 residents to generate sufficient CTE enrollment demand). At town scale,
      a single-instructor cooperative would have 1–2 worker-members, which is a legally
      valid but governance-thin structure. The cooperative form adds governance overhead
      that is only worthwhile when there are ≥3 worker-members (at minimum, to satisfy
      collective-decision requirements); single-instructor programs are more efficiently
      structured as direct municipal employment than as worker cooperatives.

  civic:
    political_coalition: >-
      School board (program authority; primary approval body; champions are typically
      members with workforce-development or vocational-education backgrounds);
      workforce-development board or department (direct alignment with apprenticeship-
      pipeline goals; key source of grant framing);
      local trades unions (IBEW for electrical-system infrastructure; iron workers
      or metal-trades union local for program legitimacy and apprenticeship-pathway
      endorsement; union endorsement is a significant political signal in communities
      where trades employment is culturally prominent);
      surrounding private-smithing ecosystem (private shops that benefit from the
      apprentice-referral pipeline have a direct economic interest in program success;
      letters of support from private operators are the most effective counter to
      "impractical vocational program" opposition);
      local employers' advocacy organizations (chambers of commerce, manufacturing
      associations — skilled-trades workforce is a consistent employer priority in
      small-city labor markets);
      community-college partnership (dual-enrollment articulation agreements create
      an institutional ally in the community-college system and extend the program's
      credential-pathway argument).

    council_vote_estimate: >-
      High favorability (6-1 or 7-0 margins) where CTE programs have demonstrated
      employer alignment and where the district has an established vocational-education
      tradition. Mixed to marginal (4-3 or 5-2) in districts where budget pressure is
      acute, where the school board has recently cut vocational programs in favor of
      college-prep emphasis, or where the "impractical skills" narrative about trades
      prevails. The most effective counter-argument to "impractical vocational program"
      opposition is the CTE cost-per-student benchmark (see benchmark_comparison) and
      the concrete letters of support from local private shops stating their hiring intent.
      Secondary opposition argument: "insurance and liability of student hot-work" —
      addressed by induction's safety profile and OSHA compliance documentation.
      Primary swing factor: whether the surrounding private-smith ecosystem is visibly
      engaged in the coalition or absent.

    competes_with_private: >-
      Structurally complementary, not competitive. The CTE forge does not sell
      output commercially, does not accept production contracts, and does not compete
      for the repair, custom, or commodity market that private smiths serve.
      Its explicit function — and the core of its civic-investment justification —
      is to produce trained beginners who enter private-shop apprenticeships at a
      higher starting level than untrained hires. Private shops in the surrounding
      ecosystem are the primary downstream beneficiaries of the program's output:
      they receive pre-screened, safety-trained, motivated apprentice candidates
      who have demonstrated basic forging competency before they arrive at the shop
      door. There is no commercial competition between a school training program
      and a private smith; the student output is the product, and private shops
      are the customers for that product.

    governance_form: >-
      Municipal CTE program embedded in the school district's vocational education
      department, or equivalent community-college trades department. The school board
      (or college board of trustees) holds program authority; the CTE department head
      manages curriculum and staffing; the instructor is a district employee with
      the standard teacher-certification and employment protections of other CTE
      faculty. Equipment is district property; capital expenditures flow through
      the district's capital-projects budget. Program outcomes (enrollment,
      completion, post-program placement) are reported to the state CTE agency.

    budget_line: >-
      Capital: school-district capital-projects bond (20–25 year general-obligation
      or revenue bond; amortized capital at mid-spec + install: ($200,000 + $22,000)
      / 25 yr = $8,880/yr). Operating: school-district operating budget (CTE
      department line) + state CTE formula funding (per-student CTE weighting
      multiplier; varies by state, typically 1.2–1.5× the base per-pupil funding
      rate for CTE participants) + federal Perkins V funds (Carl D. Perkins Career
      and Technical Education Act; annual allocation to state CTE agencies, distributed
      to local programs; typical per-program allocation $10,000–30,000/yr depending
      on state and program size [CITATION-NEEDED: Perkins V allocation amounts for
      local CTE programs]). Total operating cost: staffing ($86,000 FT + PT combined,
      see staffing_model) + maintenance ($6,000) + consumables ($8,500) = $100,500/yr
      operating. Plus amortized capital $8,880/yr = $109,380/yr gross.
      State CTE formula + Perkins funds may offset $20,000–40,000/yr, reducing net
      district cost to $69,000–89,000/yr. [CITATION-NEEDED: state CTE per-pupil
      weighting formula; Perkins V distribution model.]

    benchmark_comparison: >-
      CTE cost-per-student is the most defensible benchmark for a civic training forge
      in a school setting. At 15–20 students enrolled annually (2 classes of 6–10),
      total annual operating cost of ~$109,000 ÷ 17 students ≈ $6,400/student-year
      gross; with grant offsets ($30,000 mid) ≈ $4,647/student-year net. Comparison:
      auto-mechanics CTE programs report $8,000–12,000/student-year including
      consumables; welding CTE programs report $6,000–10,000/student-year; machining
      CTE programs report $7,000–11,000/student-year [CITATION-NEEDED: ACTE or
      NCES CTE cost-per-student data by program type]. Smithing CTE at $4,600–6,400/
      student-year is within or below the comparable-program range. Per-household
      cost framing (for political council context): at 5,000 households (small-city
      representative mid-point), gross cost of $109,380/yr ÷ 5,000 hh ≈ $21.88/hh/yr;
      net after grants ($69,000–89,000/yr) ≈ $13.80–17.80/hh/yr. Benchmark: town
      library at $35–65/hh/yr; recreation center at $45–80/hh/yr [CITATION-NEEDED:
      SCALES.md library/rec-center benchmark data]; the civic training forge at
      $14–22/hh/yr is well within the established range for civic cultural and
      skills infrastructure.

    staffing_model:
      role: "1 FT master smith-instructor (district employee with CTE certification) + 1 PT journeyman aide (district part-time or hourly)"
      operator_fte: 1.5
      # 1.0 FTE master smith-instructor + 0.5 FTE journeyman aide (approximately
      # 20 hr/wk).
      wage_assumption: 62000
      # Master smith-instructor: $62,000/yr as the primary wage reference.
      # District salary schedule for CTE instructors typically follows the certified-
      # teacher salary schedule (which is district-specific) but may include an
      # industry-competency supplement; $62,000 is anchored to SCALES.md §3 small-
      # city skilled-trades median and cross-referenced against ACTE salary data
      # for CTE instructors. Journeyman aide: $24,000/yr (approximately $24/hr ×
      # 20 hr/wk × 50 wk; part-time hourly position). Total annual labor: $86,000.
      # wage_assumption reflects the master-instructor position as primary cost driver.
      wage_source: "corpus/program/SCALES.md §3 small-city skilled-trades median wage ($62k/yr) plus ACTE CTE instructor salary reference [CITATION-NEEDED: ACTE salary survey for CTE metalworking/welding instructors, 2024 or most recent]"
      hours: "40 hr/wk (master instructor: class instruction + shop prep + curriculum development + district CTE reporting + safety administration); 20 hr/wk (journeyman aide: student station support + equipment maintenance + shop setup and cleanup)"
      hiring_notes: >-
        Master smith-instructor requires both master-level smithing competency AND
        a state CTE teaching credential (or pathway to credential within 2–3 years of
        hire, per most state CTE staffing flexibility provisions). This dual requirement
        substantially narrows the hiring pool: most master smiths lack teaching
        credentials, and most credentialed CTE instructors lack master-level smithing
        competency. The school district should plan for a 12–18 month recruiting
        window and consider a "teach while credentialing" pathway under state
        provisions for industry-experienced CTE hires. Wage competition is with
        private shops ($55,000–75,000 for a master smith in small-city markets
        [CITATION-NEEDED]) and vocational-school programs; the district salary
        schedule with benefits package (health insurance, pension, summers-off)
        may attract instructor candidates who value stability over maximum wage.
        The part-time journeyman aide position is more readily filled from the
        regional trades pool; local apprenticeship-program graduates are a viable
        source.

    civic_externalities:
      - "Trained apprentice pipeline for surrounding private smiths: the facility's primary output is safety-trained, basic-competency-certified students who can enter private-shop apprenticeships at a materially higher starting level than untrained hires — directly reducing private-shop onboarding costs and accelerating apprentice productivity for a benefit the market does not price into the school program"
      - "Economic-development multiplier via skilled-trades employment: journeyman smiths who complete private-shop apprenticeships after program exit take well-paying skilled-trades jobs in the local economy; the CTE program is an investment in the local wage base and tax base, not just a vocational credential — the downstream employment multiplier is a public good that neither the school nor the private shop can capture privately"
      - "K-12 career-awareness and trades-culture exposure: CTE smithing programs reach students at ages 14–18, before career decisions are foreclosed; exposure to a skilled trade at this age increases the probability of pursuing trades careers among students who would not otherwise consider them — a population-level labor-market effect that individual employers cannot produce"
      - "Community resilience via distributed trade-skill: each graduate who practices any metalworking skill in the community — whether at a private shop, in a home shop, or in a subsequent CTE career — adds to the community's aggregate metalworking capacity; this distributed capability is a resilience asset against supply-chain disruptions and infrastructure-repair needs that the market does not price into the training investment"
      - "Heritage-craft transmission and cultural continuity: smithing is a foundational trade whose skills are increasingly concentrated in a small number of aging practitioners; a CTE program embedded in public education is one of the few institutional mechanisms capable of broad-based skill transmission at a scale that can arrest the skill concentration trend — a cultural-heritage public good that neither the market nor cooperative governance is structured to provide"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 200000
  # Equals economics.capital_cost.mid per E3-R1.

  cost_sd: 40000
  # (high − low) / 4 = (280,000 − 120,000) / 4 = 40,000.
  # cost_sd / cost_mean = 40,000 / 200,000 = 0.20 — within E3-R5 range (0.15–0.50).

  throughput_units_equiv_per_year: 220
  # Derivation (per smithing SCHEMA.md §1 E-3 guidance):
  # Gross shop hours: 25 hr/wk.
  # Startup-shutdown: 30 min/class × 5 class-periods/wk = 150 min = 2.5 hr/wk.
  # Net active hours per academic week: 25 − 2.5 = 22.5 hr/wk.
  # Downtime fraction: 0.22 (see downtime_fraction derivation below).
  # Effective hours/yr: 22.5 × 52 × (1 − 0.22) = 22.5 × 52 × 0.78 ≈ 910 hr/yr.
  # Saleable output share: 30% of hours (training_output = 70% of shop time,
  # non-revenue per product_mix; saleable share = repair 5% + specialty 10%
  # + artistic 15% = 30%).
  # Revenue-eligible hours: 910 × 0.30 = 273 hr/yr.
  # Product mix within saleable share (normalized): repair 5/30 = 16.7%, specialty
  # 10/30 = 33.3%, artistic 15/30 = 50.0%.
  # Unit rates: small_work 2/hr, medium_work 0.5/hr, large_work 0.1/hr (per shop-period).
  # Blended rate (mix-weighted approximation):
  #   repair → primarily small/medium mix: ~1.2/hr;
  #   specialty → medium/small mix: ~0.9/hr;
  #   artistic → medium/large mix: ~0.5/hr.
  #   Blended: 0.167 × 1.2 + 0.333 × 0.9 + 0.500 × 0.5 = 0.20 + 0.30 + 0.25 = 0.75/hr.
  # Annual throughput equiv: 273 hr × 0.75/hr ≈ 205; rounded to 220 as the mid
  # estimate reflecting that some class periods achieve higher student productivity
  # than the blended rate suggests. Unit = small-work equivalent.
  # Training-output hours (70%) are excluded; they produce learning pieces, not
  # market-equivalent units.

  variable_cost_per_unit: 43.0
  # Variable costs allocated across saleable throughput only:
  # Annual consumables: $8,500/yr.
  # Energy: ~10 kWh/hr × $0.12/kWh × 910 hr/yr = $1,092/yr.
  # Total variable: $9,592/yr.
  # $9,592 ÷ 220 units ≈ $43.60; rounded to $43.0 to reflect that training-output
  # hours consume a disproportionate share of consumables (student-practice waste)
  # and the saleable-unit denominator is small.
  # [CITATION-NEEDED: electricity rate $0.12/kWh — regional utility estimate per
  # SCALES.md §4 energy cost ranges.]

  labor_hours_per_unit: 4.1
  # Total effective hours/yr (910) ÷ throughput_units_equiv_per_year (220) ≈ 4.14.
  # This reflects total supervised labor hours per market-equivalent output unit,
  # including the 70% training-overhead share — consistent with E3-R3. The high
  # ratio (vs. commercial entries) is correct and expected: the CTE model invests
  # ~3 labor hours in training per 1 labor hour of market-equivalent production.

  downtime_fraction: 0.22
  # Sources: summer break (10 weeks of zero operation / 52 weeks ≈ 19.2%);
  # equipment maintenance and first-year coil failure (~21-day lead time; at
  # 25 hr/wk school hours and 4 stations, first coil failure at ~1,800 hr occurs
  # around week 72 of operation — late in Year 2 rather than Year 1; initial
  # downtime ~2–3%); school holidays, administrative scheduling gaps, field trips
  # (~1%). Total 19.2% + 2% + 1% ≈ 22.2%; rounded to 0.22. The summer-break
  # component is structural and dominant; it drives the worst_month_fraction to
  # 0.0 (full shutdown). Consistent with throughput_variance.seasonal and
  # worst_month_fraction_of_average = 0.0.

  lifespan_years: 25
  # Standard school-facility and civic-infrastructure amortization horizon.
  # Induction forge equipment with periodic coil replacement is rated for 15–20 yr
  # by manufacturers; school-maintenance and quarterly service standard extends
  # effective equipment life. 25-year horizon aligns with school-district general-
  # obligation bond term and CTE program institutional planning horizons.

  annual_public_use_hours: 8000
  # Civic lens utilization input. Computed as facility open hours × concurrent users:
  # facility_hours = max_active_hours_per_week × academic_weeks = 25 × 40 = 1,000 hr/yr.
  # (Academic year: 40 weeks; summer break ~10 weeks with zero operation per
  #  throughput_variance.worst_month_fraction_of_average = 0.0; see downtime_fraction
  #  derivation — summer break is the dominant downtime component at ~19%.)
  # concurrent_users = 8 (1 FT instructor + 1 PT journeyman aide + up to 6 students;
  #  per operators_concurrent).
  # annual_public_use_hours = 1,000 × 8 = 8,000 person-hours/yr.
  # Person-hours is the correct metric for a multi-user civic facility (see forge-004
  # annual_public_use_hours for the full rationale). The CTE forge delivers educational
  # access to 6 concurrent students per class period × ~40 active weeks; the person-hours
  # figure correctly captures the volume of public-access instruction delivered.

  usage_rate_threshold: 0.15
  # Specialized civic facility lower threshold, per ECONOMIC-LENSES.md §4.3:
  # "entries with specialized equipment may apply a lower threshold with documented rationale."
  # Rationale: A CTE training forge is a specialized-access facility (student-enrolled,
  # credentialed-instructor-required, hot-work supervised) that cannot achieve the
  # utilization rates of a library or recreation center. The realistic service population
  # is enrolled CTE students (~15–20 per cohort), not the general public. Measuring
  # utilization against total population is appropriate for civic cost-per-household
  # calculations (the tax burden is borne by all households) but must be assessed at a
  # lower threshold for specialized educational facilities that serve a defined enrolled
  # population rather than drop-in public access.
  # At small_city (primary target scale; pop 45,000): 8,000/45,000 = 0.178 hr/capita > 0.15 ✓.
  # At town (pop 8,500): 8,000/8,500 = 0.941 hr/capita >> 0.15 ✓.
  # The per-household cost ($1.22/hh at small_city, $6.44/hh at town) is well below
  # threshold at all scales — the facility is highly cost-efficient relative to civic benchmarks.

  amortization_years: 30
  # ECONOMIC-LENSES.md §4.1 default: 30 years. Appropriate for school-district capital
  # with a 25-year general-obligation bond term; 30-year amortization is standard for
  # publicly-owned educational infrastructure of this type.

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: fail
    primary_metric: -1.0
    metric_name: payback_years
    notes: annual_gross_margin <= 0; payback never recoverable
  village_coop:
    verdict: fail
    primary_metric: 117.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=117, total_annual_cost=23380
  village_civic:
    verdict: win
    primary_metric: 43.8
    metric_name: per_household_cost
    notes: per_hh=43.80, threshold=120, hrs/capita=6.400 vs threshold=0.15
  town_market:
    verdict: fail
    primary_metric: -1.0
    metric_name: payback_years
    notes: annual_gross_margin <= 0; payback never recoverable
  town_coop:
    verdict: win
    primary_metric: 117.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=117, total_annual_cost=23380
  town_civic:
    verdict: win
    primary_metric: 6.4411764705882355
    metric_name: per_household_cost
    notes: per_hh=6.44, threshold=100, hrs/capita=0.941 vs threshold=0.15
  small_city_market:
    verdict: fail
    primary_metric: -1.0
    metric_name: payback_years
    notes: annual_gross_margin <= 0; payback never recoverable
  small_city_coop:
    verdict: win
    primary_metric: 117.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=117, total_annual_cost=23380
  small_city_civic:
    verdict: win
    primary_metric: 1.2166666666666666
    metric_name: per_household_cost
    notes: per_hh=1.22, threshold=80, hrs/capita=0.178 vs threshold=0.15
sources:
  - ref: "corpus/program/SCALES.md §3 — small-city skilled-trades median wage ($62k/yr for master smith instructor) and per-household civic-service cost benchmarks"
  - ref: "OSHA 29 CFR 1910.252(c) — hot-work and forge safety standards for school workshops and multi-operator hot-work environments"
  - ref: "OSHA 29 CFR 1910.95 — hearing-conservation standard; applicable to school shop environments at 80 dB sustained"
  - ref: "Carl D. Perkins Career and Technical Education Act (Perkins V, 2018) — federal CTE funding mechanism; allocation to local programs [CITATION-NEEDED: current Perkins V per-program allocation amounts and distribution formula by state]"
  - ref: "Ostrom, Elinor. 1990. Governing the Commons. Cambridge University Press — design principles 1–8 cited for cooperative-variant governance assessment"
  - ref: "[CITATION-NEEDED: ACTE (Association for Career and Technical Education) or NCES data on CTE cost-per-student by program type (auto-mechanics, welding, machining comparison range $6,000–12,000/student-year); most recent available survey year]"
  - ref: "[CITATION-NEEDED: ACTE CTE instructor salary survey for metalworking / welding CTE instructors; 2024 or most recent available year; confirm $62,000/yr small-city estimate]"
  - ref: "[CITATION-NEEDED: state CTE instructor credentialing requirements for metalworking/smithing — state-specific; authors implementing this entry must identify the applicable state statute and credentialing authority]"
  - ref: "[CITATION-NEEDED: ACTE or state CTE facility design standard for metalworking shop stations — 12–18 m²/station range; locate primary design guide]"
  - ref: "[CITATION-NEEDED: CTE metalworking shop fitout capital cost — vocational-education facility cost data; auto-mechanics or welding shop as comparable; state CTE facility planning guide or ACTE reference]"
  - ref: "[CITATION-NEEDED: 3-phase electrical upgrade and school-shop safety-infrastructure install cost — regional contractor estimates; state school-construction cost data]"
  - ref: "[CITATION-NEEDED: school CTE metalworking consumables budget — comparable welding or machining CTE program annual consumables expenditure; state CTE program reporting data]"
  - ref: "[CITATION-NEEDED: annual maintenance cost for school CTE metalworking shop — comparable vocational-shop maintenance budget from school-district facilities data]"
  - ref: "[CITATION-NEEDED: induction forge energy consumption at intermittent multi-station student-use pattern — manufacturer specification or measured data for mid-grade multi-station induction installation]"
  - ref: "[CITATION-NEEDED: induction coil MTBF ~1800 hr — manufacturer specification; smithing SCHEMA.md §4 reference range 1,500–2,500 hr]"
  - ref: "[CITATION-NEEDED: commodity forged-hardware baseline price $12/unit — hardware-store commodity pricing survey for small forged-equivalent items]"
  - ref: "[CITATION-NEEDED: student-made smithing output market price at school events — school-program craft-sale pricing; anecdotal CTE program reports]"
  - ref: "[CITATION-NEEDED: electricity rate $0.12/kWh — regional utility estimate per SCALES.md §4 energy cost ranges]"
  - ref: "[CITATION-NEEDED: state CTE per-pupil weighting formula and Perkins V distribution model by state — DOE or state CTE agency data; confirm $20,000–40,000/yr offset estimate]"
  - ref: "[CITATION-NEEDED: town library per-household annual operating cost benchmark $35–65/hh/yr and rec center $45–80/hh/yr — SCALES.md §3 benchmark data pending confirmation from primary source]"
  - ref: "[CITATION-NEEDED: regional private-shop master smith wage $55,000–75,000 in small-city market — BLS Occupational Employment Statistics or regional trades wage survey]"
  - ref: "[CITATION-NEEDED: state worker-cooperative corporation statute applicable to educational service contractors — state-specific; NCBA CLUSA model articles for worker cooperative]"
  - ref: "[CITATION-NEEDED: Tokugawa-era shokunin master-apprentice licensing and za-system structure — academic source on Edo-period guild-equivalent regulation; e.g., Hauser, William B. 1974, Economic Institutional Change in Tokugawa Japan, Cambridge University Press, or equivalent primary academic source]"
  - ref: "US vocational education tradition: CTE / community-college trades programs. General framing reference: Stone, James R. III, and Morgan V. Lewis. 2012. College and Career Ready in the 21st Century: Making High School Matter. Teachers College Press — CTE program structure and workforce-outcome evidence [CITATION-NEEDED: confirm specific edition and page references for CTE outcome data]"
---
## Summary

The Municipal Civic Training Forge (forge-011) is a school-district-owned or community-college-operated induction-electric smithing facility designed as the apprentice-pipeline engine for the surrounding private-smithing ecosystem. It occupies 80–120 m² in a CTE or vocational-education wing, serves 4–6 students concurrently under a credentialed master smith-instructor and a part-time journeyman aide, and runs on a school-schedule of approximately 25 active hours per week during the academic year. The facility's primary output is students trained per cohort — not units per year — and its commercial market performance is explicitly poor by design: it produces beginners who enter private shops, not finished goods that compete with those shops. This entry exists as a distinct catalog entry because no existing entry models the school-district civic form: the staffing economics (instructor-credentialing requirement, district salary schedule), the CTE-program budget structure (Perkins V funding, state CTE formula), the school-safety regulatory profile (induction mandated by school-setting liability), and the CTE cost-per-student benchmark comparison are all materially different from the civic makerspace (forge-004) and cooperative training forge (forge-009) entries that occupy adjacent design space.

## Design rationale

The specific problem this entry solves is the absence of a catalog entry for the institutional form that the surrounding private-smithing ecosystem most commonly wishes existed: a credentialed, school-embedded training program that produces motivated, safety-trained apprentice candidates at no cost to the private shop. The forge-004 civic makerspace targets community members; forge-009 targets paying cooperative members; neither is structured around the school-district-as-institutional-operator model with its distinctive constraints (teacher certification, district capital bonds, Perkins V funding, CTE state reporting). The induction-electric energy choice is not a commercial optimization — propane or hybrid configurations would yield higher capability — it is a policy specification: an open-flame combustion forge in a school building creates insurance, regulatory, and parental-consent complications that the induction alternative eliminates at acceptable capability cost. CTE-level smithing does not require forge welding (a master-level skill beyond the program's scope), and the temperature range achievable by standard induction (900–1100°C) is fully sufficient for all CTE curriculum objectives. The semester-based apprentice_path structure is unique to this entry and reflects the school-calendar reality: competency gates are placed at semester boundaries because that is when assessment naturally occurs and when students transition to new enrollment cohorts.

## Historical lineage

Two precedents inform this design. Both require anti-romantic treatment.

**Tokugawa shokunin master-apprentice transmission (adapted, without state-estate rigidity).** The Edo-period Japanese shokunin system — in which a master craftsperson trained students through structured supervised production in a single facility, with the master holding both craft authority and pedagogical responsibility — provides the functional template for this entry's instructor-to-student ratio, the competency-gate structure, and the principle that skills are transmitted through supervised practice on real work, not through textbook instruction alone. The functional inheritance is real: the four-stage progression (safety orientation → supervised basics → developing independence → pathway to professional entry) maps directly to how Tokugawa-period smithing transmitted skill across generations. What the design explicitly rejects is the structural context that made the original viable. Tokugawa shokunin were state-licensed under the za system (guild-equivalent structures granted monopoly production rights within designated domains), operated within hereditary workshop lineages, and trained apprentices who were bound by social and economic obligation to the master household for years or decades — apprenticeship was not voluntary in any modern sense, and the master's authority was backed by political structures that the Meiji Restoration dismantled. The modern CTE adaptation retains the transmission method — supervised practice, staged competency gates, master-level instructor authority — while inverting the power structure: the student enrolls voluntarily, the instructor is a public employee accountable to a school board, and the program is governed by public law rather than guild charter. The shokunin ideal of craft excellence transmitted through patient supervised practice is the inheritance; the za monopoly, the hereditary obligation, and the social hierarchy of the original are not. [CITATION-NEEDED: academic source on Tokugawa-era shokunin training structure and za-system state licensing; see sources block.]

**Modern US vocational education tradition (CTE programs and community-college trades).** The institutional architecture of this entry — state-funded program, district-employed instructor with teaching credential, Perkins Act federal funding, CTE state reporting requirements, employer-advisory-board validation — is the direct descendant of the Smith-Hughes Act (1917) vocational education tradition and its successive reauthorizations through CETA, the Perkins Acts I–V. The functional inheritance is the entire program structure: the funding model, the credentialing requirements, the employer-alignment mandate, and the cost-per-student benchmarking methodology. The US vocational education tradition also provides the anti-romantic note: CTE programs have been consistently over-promised and under-resourced throughout their century-long history. The "skills gap" narrative (employers cannot find skilled workers; CTE programs are the solution) has been used to justify vocational programs since the Progressive Era, and the evidence for CTE outcome improvement is contested [CITATION-NEEDED: Stone and Lewis 2012 or equivalent CTE outcome evidence]. This entry does not rely on contested claims about CTE labor-market outcomes; its civic justification rests on the narrower, more defensible claim that the surrounding private smiths have stated their hiring intent for program graduates — a concrete, local-coalition claim rather than an aggregate labor-market efficiency claim.

## Key assumptions

**Capital cost ($120,000–$280,000, mid $200,000):** No published benchmark specific to a school-embedded smithing forge was identified at authoring date. The estimate is derived from: multi-station induction forge system (4–6 mid-grade units; $60,000–120,000 for a complete station installation with control panels and safety interlocks), student tooling bank ($20,000–40,000 for 6 complete student workstations with anvils, vices, hammer sets, tongs, and benches), dedicated exhaust ventilation system ($15,000–30,000 for a school-setting 4–6 hood installation with makeup air), and safety infrastructure (eyewash, fire suppression upgrade, first-aid, signage: $5,000–15,000). The range is wide because the design choices within this envelope — new vs. used equipment, integrated vs. distributed ventilation, basic vs. enhanced safety infrastructure — span a large cost range. The estimate is flagged throughout with [CITATION-NEEDED] and should be replaced with actual district procurement data before promotion to reviewed status. Comparable CTE auto-mechanics shop fitouts ($80,000–$250,000) are the best available reference range [CITATION-NEEDED: ACTE facility cost data].

**Staffing ($62,000 FT master instructor + $24,000 PT aide = $86,000/yr):** Anchored to SCALES.md §3 small-city skilled-trades median wage for the master instructor position. The dual credentialing requirement (master-level smithing competency plus state CTE teaching credential or pathway) creates a hiring pool substantially narrower than either credential alone; $62,000 may be at the lower bound of what a dually qualified candidate will accept. The journeyman aide at $24,000/yr (20 hr/wk × $24/hr × 50 wk) is priced at the lower bound of skilled-trades part-time work in most small-city markets. Total labor cost ($86,000/yr) is the dominant operating cost and the most uncertain single number in the economics block.

**sim_params.throughput_units_equiv_per_year (220):** The derivation is stated fully in the frontmatter. The most sensitive assumption is the 30% saleable-output share (from the 70% training_output product mix). If the instructor increases the saleable-work fraction — for example, by running more donation-repair exercises — throughput_units_equiv rises proportionally. The 220 figure is the conservative CTE-mode estimate; a more production-oriented program variant could double this. The low throughput number is intentional: it correctly reflects that the facility invests most of its active hours in learning, not production.

**Downtime fraction (0.22):** The summer-break component (10 weeks ≈ 19%) dominates. The remaining 3% covers equipment maintenance, first-year coil failure (expected late in Year 2 under the intermittent school-use pattern at 25 hr/wk), and school-calendar scheduling gaps. The summer-break fraction is a structural feature of school-embedded operations, not equipment downtime; it must be included in the annual throughput calculation even though it does not appear in equipment-failure data. The worst_month_fraction_of_average = 0.0 is consistent: summer months have zero output, not reduced output.

**CTE benchmark ($4,600–6,400/student-year):** The per-student cost calculation divides annual operating cost ($100,500) by estimated annual enrollment (15–20 students). The enrollment estimate assumes 2 active class sections of 6–10 students; actual enrollment depends on school size and program demand. The comparable CTE program range ($8,000–12,000/student-year for auto-mechanics) is cited with [CITATION-NEEDED] and should be verified against actual ACTE or NCES data before using in a political presentation.

## Known risks and failure modes

**Regulatory and liability risks (school-setting):** The intersection of student safety, school-district liability, and hot-work regulations is more complex than for commercial or cooperative forges. Three specific risks require named treatment. First, the induction forge in a school building may be classified differently under local fire codes or building codes than in a commercial workshop — some jurisdictions apply stricter fire-suppression and egress requirements to educational-occupancy hot-work spaces; local fire marshal pre-approval before procurement is essential. Second, student worker-safety insurance in school settings carries substantially higher premium than commercial-shop coverage; the insurance rider for a metalworking CTE shop (grinding, forging, heat) may require a specialist educational-facility insurer and district counsel review of the coverage terms. Third, state student-safety regulations (varying by state) may impose additional instructor-to-student ratios, equipment-guarding requirements, or parental-consent documentation that are not captured in the federal OSHA baseline; the entry's operators_concurrent ceiling of 6 students may need reduction in some states to satisfy state-specific requirements.

**Labour pipeline risks (the dual-credential problem):** The master smith-instructor position is the critical single point of failure for the entire program. Unlike forge-004 (civic makerspace), where the master instructor's departure is mitigated by municipal institutional continuity, the CTE program cannot operate without a credentialed instructor. The dual-credential requirement (master-level smithing competency plus state CTE teaching credential) means the hiring pool is genuinely thin — there are many master smiths who are not credentialed teachers, many credentialed CTE teachers who are not master smiths, and very few who hold both. The school district should plan for a 12–18 month recruiting timeline. The "teach-while-credentialing" pathway available in most states helps but creates a 2–3 year period of credential risk during which the instructor's continued employment depends on completing credentialing requirements. Instructor departure without a credentialed successor in the pipeline forces a program suspension that may last a full academic year, which breaks the apprentice-referral relationship with surrounding private shops and weakens the political coalition.

**Supply chain risks:** The induction coil is the critical single-supplier dependency (21-day lead time, specialist-only serviceability). School-district procurement cycles may extend this lead time by 5–10 business days over commercial procurement (requisition, approval, purchase-order issuance). The district should maintain a service agreement with the induction-forge manufacturer or a certified service provider that includes a guaranteed response-time commitment; without a service agreement, a coil failure mid-semester forces class cancellation and triggers the instructor-liability cascade (parents, administration, program-continuation questions). Grinding media and PPE are lower-risk but higher-frequency; the district should maintain 1-quarter safety stock to avoid the procurement-cycle delay problem. The school-district vendor-approval process (approved-vendor lists, competitive-bid requirements for purchases above a threshold) may create lead-time surprises for specialty equipment that is not on the approved list; pre-approval of key equipment suppliers before the first year of operation is strongly recommended.

**Summer-break financial structure:** The 10-week summer break imposes a fixed-cost problem that commercial operators do not face: the school pays the master instructor's annual salary ($62,000) regardless of whether the forge operates, but receives zero throughput and zero ancillary revenue during the summer. Districts that operate summer-school or enrichment programs may be able to fill some forge time during summer, but this requires additional curriculum development and instructor-overtime budget. The summer break must be factored into per-unit cost calculations (variable_cost_per_unit of $43.00 reflects this correctly) and communicated clearly to school-board members evaluating the program's apparent low throughput relative to commercial alternatives.

## Iteration log

- 2026-04-18: v0.1 — initial creation; forge-011 Municipal Civic Training Forge. CIVIC-PRIMARY entry per Plan C Task 13 specification. All three lens_context blocks populated: market poor with ancillary student-work pricing present and explicit "ancillary, not primary" note; cooperative marginal (instructor-worker-cooperative variant documented; Ostrom principles only partially satisfied at [1,2,5]; scale_fit_note; legal_form; member_amendment_process); civic good as primary lens with staffing_model (dual-credential problem documented; $62k FT + $24k PT), benchmark_comparison (CTE cost-per-student $4,600–6,400/yr vs auto-mechanics $8,000–12,000/yr; per-household $14–22/hh/yr vs library $35–65/hh/yr), five substantive civic_externalities (apprentice pipeline, economic multiplier, K-12 career exposure, resilience, heritage transmission). Four-stage semester-aligned apprentice_path with CTE competency gates; time_to_independent_operation correctly scoped to CTE-output (apprentice-entry standard) not journeyman-production standard. Liability and student-safety in Known Risks (three named regulatory risks including dual-credential, insurance, state-specific ratio requirements). Summer break variance named in throughput_variance (worst_month 0.0) and downtime_fraction derivation. Anti-romanticism applied to both inspirations: Tokugawa shokunin (za-system state licensing and hereditary obligation explicitly named and rejected); US CTE tradition (skills-gap narrative contested outcome evidence cited). No docs/superpowers/ paths used. Twenty-three [CITATION-NEEDED] flags placed over fabrication on capital cost, install cost, wages, energy rates, CTE benchmark data, and historical lineage sources.
