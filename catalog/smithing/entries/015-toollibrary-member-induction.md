---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: forge-015
trade: smithing
name: "Tool-Library Member-Access Induction Forge (multi-station, cooperative)"
tagline: "Member-owned induction-electric shared forge; urban-compatible, subscription-access, 3-4 simultaneous stations"
status: draft
version: 0.1
supersedes: null
inspirations:
  - us-tool-library-network
  - song-china-coal-to-coke-fuel-transition

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 40
# Mid-point of the 30–50 m² multi-user range. Three to four induction stations
# require more floor area than a single-operator compact unit (forge-002: 20–35 m²)
# but less than a coal training floor (forge-009: 80 m²). The 40 m² figure
# accommodates 3–4 induction stations with per-station operator zones, a shared
# quench and tooling bay, and a supervisor circulation path. Excludes member
# locker and reception area.
ceiling_min_m: 3.0
# Induction forging generates local heat but no combustion stack; 3.0 m clear
# ceiling is sufficient for safe hammer-swing clearance and heat dissipation.
# No stack height requirement unlike coal (forge-003: 3.5 m minimum for coal-stack
# clearance). Enables siting in ground-floor commercial units with standard
# 3.0–3.5 m residential-floor ceiling heights common in urban mixed-use buildings.
ventilation: mechanical-extraction-required
# Induction forging produces no combustion products, but hot-work generates metal
# fume and scale particulate; OSHA 29 CFR 1910.252 requires ventilation for hot-work
# environments regardless of fuel source. Mechanical extraction serves heat management
# and particulate capture; does not require a dedicated coal-exhaust stack system.
# This is the key regulatory difference from coal (forge-003: dedicated-exhaust-system
# with coal-particulate and SOx management). The lower ventilation category opens
# building-type options that coal zoning forecloses.

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: induction-electric
energy_consumption_per_active_hour: "25 kWh (facility-average at 3-station peak load)"
# Per-station induction unit: approximately 8–10 kWh/hr at full duty cycle
# (smithing SCHEMA.md §2: 6–15 kWh/hr range for induction-electric entries).
# 25 kWh/hr is the facility-average at 3-station simultaneous operation; this
# is the operational peak figure for demand-management and electrical service sizing.
# Single-station light use is proportionally lower. Annual consumables budget
# uses a weighted average across booked and unbooked hours.
backup_fuel: null
# No backup fuel. Induction-electric is the sole energy source; electrical service
# outage is the failure mode. Cooperative should maintain a session-cancellation
# protocol for grid outages. No combustion backup is a design choice consistent
# with the regulatory-simplicity rationale: introducing a backup combustion source
# would partially re-introduce the permitting burden the induction-electric choice
# was selected to avoid.

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  units_per_hour: { small_work: 4, medium_work: 1, large_work: 0.2 }
  # Aggregate across all active member stations at peak (3 stations simultaneously
  # booked). These are facility-level aggregates, not per-station rates.
  # Individual member throughput varies with skill level (members range from
  # learning to journeyman-equivalent); the supervisor does not produce output.
  # small_work: 4/hr is conservative for 3 members — a journeyman would produce
  # 4–6/hr at a single station; member-average is lower due to skill variance.
  # large_work: 0.2/hr reflects the induction-electric temperature ceiling
  # (~900–1100°C practical range; see smithing SCHEMA.md §2): large-work items
  # requiring sustained high temperatures are slower on induction than on coal.
  max_active_hours_per_week: 40
  # Extended member-access scheduling via a booking system (vs. single-operator
  # commercial shop at 40–45 hr/wk for one person). Member-booked sessions span
  # morning, afternoon, and evening slots 7 days/week where facility permits.
  # 40 hr/wk is the gross booked-hours ceiling; effective productive hours are
  # derated by startup-shutdown overhead and session-gap scheduling.
  product_mix:
    repair: 30
    commodity: 0
    specialty: 30
    artistic: 0
    training_output: 40
    # repair: member projects on own or customer-owned metalwork (not commercial
    # production; community repair culture).
    # commodity: 0 — not a commercial production facility; no commodity output.
    # specialty: variable member-sold work (member-made pieces sold by individual
    # members; cooperative does not take consignment commission, so this is
    # ancillary to cooperative revenue).
    # training_output: 40% — classes, safety-certification sessions, and
    # learning-project pieces not intended for sale. The high training_output
    # share reflects the member-learning structure: many members are in active
    # skill development, and their session time produces non-market output.
    # Sum: 30 + 0 + 30 + 0 + 40 = 100.
  throughput_variance:
    seasonal: "Fall and winter higher utilization (academic-year-like member rhythm; indoor activity preference); summer trough as members travel and outdoor alternatives compete"
    worst_month_fraction_of_average: 0.6
    best_month_fraction_of_average: 1.3

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: journeyman
# The supervisor-of-record must be journeyman-level to: (a) assess member
# technique safely in real time across up to 3 simultaneous stations, (b) identify
# heat-judgment errors before they become injuries or equipment damage, and (c)
# provide competent instruction during classes and certification sessions. An
# apprentice-level supervisor cannot adequately monitor a multi-station floor with
# members of varying skill levels. Per smithing SCHEMA.md §3.
operators_concurrent: "1 supervisor + up to 3 members simultaneously at own stations"
# The supervisor does not operate a production station; their role is floor
# monitoring, safety oversight, and member support. Up to 3 members work
# simultaneously at booked stations. Outside booked hours, 1 member may work
# with the supervisor present (minimum safe staffing: supervisor always present
# when any station is active per cooperative safety protocol).
apprentice_friendly: true
apprentice_path:
  training_stages: >-
    Stage 1 — Safety Certification (sessions 1–4, approximately 1 month at
    weekly attendance): facility orientation, induction-unit safe operation (power
    on/off, coil position, water cooling check), PPE protocol and required
    equipment, heat-color reading introduction, emergency procedures, shop-bylaw
    acknowledgment and signed safety agreement. No unsupervised heat-work until
    certification complete. Competency gate: pass written safety assessment with
    ≥80% score; demonstrate correct induction-unit startup and shutdown under
    supervisor observation; correctly identify three heat-color stages and one
    over-heating indicator.

    Stage 2 — Supervised Basic Work (months 1–6): small_work production at
    booked stations under supervisor on-floor presence. Heat-color reading
    reinforced through direct feedback. Basic operations: drawing, bending,
    punching, basic texturing on mild steel. Supervisor signs off on each session
    log. Members in this stage must book during staffed hours only. Competency
    gate: complete five consistent small_work pieces (hooks or similar to ±5 mm
    dimensional tolerance) across at least three separate booked sessions; receive
    supervisor sign-off on heat-judgment (not over-heating, not under-heating
    consistently).

    Stage 3 — Independent Booked Access (months 6–24+): member may book stations
    during any staffed hours without direct instruction, though supervisor remains
    on floor. Eligible for medium_work projects. Heat-treatment fundamentals
    (normalize, anneal, harden, temper on mild and low-alloy stock) introduced
    through cooperative-run classes (minimum one class required before heat
    treatment without instructor oversight). Members pursuing higher skill levels
    may request mentored sessions with the supervisor or journeyman guest
    instructors. No formal upper gate in this stage — members self-pace.

    Note: the member-learning structure is less formal than the forge-009
    cooperative training program (no journeyman certification, no paid apprentice
    stipend, no cohort cohort structure). The goal is competent, safe independent
    member access; journeyman-credential equivalence is not the target outcome.
    Members who pursue journeyman-level skill typically progress to forge-009 or
    an employer-sponsored apprenticeship, having developed foundational competence
    here.

  time_to_independent_operation: >-
    ~1–6 months to Stage 3 independent booked access (safe solo work within the
    supervised facility environment). This is a materially shorter on-ramp than
    forge-009's 36-month journeyman timeline because the target outcome is
    competent member access, not journeyman certification. Members continue skill
    development over years of membership; "independent operation" here means
    independently booking and using the facility safely, not full commercial
    journeyman competency.

  succession_note: >-
    Member-skill depth accumulates across the membership body over time: a
    facility with 50+ active members includes a range of experience levels from
    new to multi-year. The supervisor role requires journeyman-level competency
    and is the primary succession point; the cooperative should maintain a
    hiring relationship with local vocational programs, forge-009-equivalent
    cooperatives, or regional blacksmithing associations to fill supervisor
    vacancies. Long-tenured members who develop to journeyman standard are
    natural internal succession candidates; the cooperative bylaws should include
    a supervisor-promotion pathway for qualifying members.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 50000, mid: 85000, high: 120000 }
  # Low: 3 entry-grade induction units + minimal tooling bank + used anvils and
  # stands. Mid: 3–4 mid-grade induction units (commercial-grade, serviceable
  # coil geometry) + full multi-station tooling bank + quench tank and safety
  # equipment. High: 4 top-spec induction units + full new tooling bank + purpose-
  # built station furniture + safety-equipment suite.
  # [CITATION-NEEDED: multi-station induction workshop capital cost; no published
  # benchmark identified at authoring date; derived from equipment pricing
  # aggregates for commercial induction forge units and tooling.]

  install_cost: 12000
  # 3-phase electrical service installation (required for 3–4 simultaneous
  # induction units at 8–10 kWh/hr each; ≥150A service recommended). No coal
  # ventilation stack required; mechanical extraction system is simpler and
  # cheaper than coal-compatible dedicated exhaust. Install cost is materially
  # lower than forge-003 coal equivalent ($18,000 for coal including dedicated
  # exhaust) because the induction-electric choice eliminates the coal-stack
  # requirement.
  # [CITATION-NEEDED: 3-phase electrical service install cost estimate from
  # regional contractor ranges; SCALES.md §4 electrical infrastructure cost.]

  annual_maintenance: 3000
  # Induction coil servicing, mechanical-extraction system, quench tank maintenance,
  # tooling reconditioning, and minor electrical. Induction stations have lower
  # routine maintenance than coal (no ash, no refractory, no fire-management
  # wear-and-tear), but coil longevity is the key maintenance driver.
  # [CITATION-NEEDED: annual maintenance estimate for multi-station induction
  # workshop; comparable facility data.]

  annual_consumables: 2800
  # Electricity cost (dominant line item) + steel stock for classes and training
  # sessions (members supply own stock for personal projects; cooperative provides
  # stock for classes). Electricity estimate: 25 kWh/hr × ~5 hr/day average
  # (blended across high-use and low-use days) × 250 operating days × $0.12/kWh
  # = $3,750; offset by lower utilization in summer trough; blended annual total
  # ~$2,200. Steel stock for classes: ~$600/yr. Total ~$2,800.
  # [CITATION-NEEDED: electricity rate $0.12/kWh; regional utility rate per
  # SCALES.md §4; steel stock pricing for classroom use.]

  floor_space_rent_per_year: 6600
  # Town/city commercial rate for 40 m² light-industrial/mixed-use space.
  # Imputed at $165/m²/yr effective rate for urban/suburban commercial space
  # accessible to an induction forge (mixed-use or light-industrial zoning;
  # ground floor preferred for equipment access). Higher than forge-003 ($4,800
  # for 35 m² at $137/m²/yr) because the urban/suburban siting premium and the
  # induction facility's access to denser member pools in urban cores.
  # [CITATION-NEEDED: town/city commercial floor-space rent at $165/m²/yr for
  # light-industrial/mixed-use; derived from SCALES.md §4 commercial rent estimate.]

  market_price_per_unit: { low: 30, mid: 50, high: 100 }
  # CONDITIONAL — present because lens_fit.market is `poor` but ancillary member-
  # sold output creates a nominal market reference. This is NOT primary cooperative
  # revenue; member-sold specialty work is individual-member income, not cooperative
  # income. The pricing is populated for reference and revenue-modeling purposes only.
  # Unit = small-work equivalent piece sold by a member (directly or at craft
  # markets). Market price is set by the individual member, not the cooperative.
  # [CITATION-NEEDED: member-sold specialty smithing piece market price; inferred
  # from comparable community-smithing output pricing.]

  pricing_notes: >-
    Unit is a small-work equivalent piece sold by individual cooperative members
    from their own production. ANCILLARY AND INDIVIDUAL, not cooperative revenue:
    member-sold work is income to the individual member, not to the cooperative;
    the cooperative's revenue is membership fees and session fees. Industrial
    baseline for comparable commodity items: $10/unit (mass-produced imported
    hardware-store forged equivalent; [CITATION-NEEDED]). Member-made pieces
    command a premium over commodity baseline due to craft origin and local
    provenance; customer segment: local craft buyers, repair customers, and
    cooperative members. This pricing reference does not anchor the cooperative
    viability case; member fees and session fees are the cooperative's revenue.

  industrial_baseline_price: 10
  # Commodity forged-hardware equivalent (hooks, brackets, simple hardware,
  # mass-produced imported). [CITATION-NEEDED: commodity forged-hardware baseline
  # price; hardware-store pricing survey.]

  pricing_validation: >-
    Pricing inferred from comparable community-smithing and craft-cooperative
    output pricing; no direct market survey conducted at authoring date. Evidence
    type: inferred comparables from regional craft-market pricing norms. This is
    not empirical sales data; [CITATION-NEEDED] for a direct market-price study.
    Flagged as `inferred`. Ancillary member-sales pricing does not anchor the
    cooperative viability case.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:

  first_year_failures:
    - item: "Primary induction coil (heating element, one or more stations)"
      estimated_hours_to_failure: 1800
      # Per smithing SCHEMA.md §4: induction coil typical range 1,500–2,500 hr.
      # At 40 hr/wk booked with 3 stations averaging ~50% concurrent utilization,
      # each station accumulates ~20 hr/wk; first coil failure expected around
      # 1,800 ÷ 20 hr/wk = ~90 weeks (~21 months) from commissioning. With 3–4
      # stations, statistical expectation is at least one coil event in the first
      # operating year at higher utilization. [CITATION-NEEDED: induction coil
      # MTBF; see smithing SCHEMA.md §4.]
      replacement_cost: 1400
      replacement_lead_time_days: 21
      # 21-day lead time is the optimistic scenario for non-stock coil geometries;
      # stations without failed coil remain operational during replacement period,
      # mitigating facility downtime vs. a single-station setup.
      serviceable_by: specialist

    - item: "Ventilation blower (mechanical-extraction system)"
      estimated_hours_to_failure: 2500
      # Blower motor bearing failure under continuous partial load. Extended hours
      # (40 hr/wk × scheduled days) accumulate faster than a commercial single-
      # operator shop with shorter operational windows. [CITATION-NEEDED: blower
      # motor MTBF for mechanical-extraction systems; smithing SCHEMA.md §4
      # baseline 1,500–3,000 hr.]
      replacement_cost: 300
      replacement_lead_time_days: 5
      serviceable_by: operator
      # Standard fractional-HP blower motor replacement is operator-serviceable;
      # 5-day lead time for commercial HVAC-grade replacement motor.

    - item: "Safety-equipment wear and quarterly replacement"
      estimated_hours_to_failure: 0
      # Not an equipment failure; a scheduled replacement event. PPE for a
      # multi-member shared facility degrades faster than a single-operator shop
      # (multiple users, varying care levels). Included because PPE replacement
      # is a first-year cost driver specific to shared-access models.
      replacement_cost: 500
      # $500/quarter × 4 = $2,000/yr total; per-quarter figure stated here.
      # Included in annual_consumables aggregate.
      replacement_lead_time_days: 0
      serviceable_by: operator

  maintenance_schedule:
    daily:
      task: "Station check: verify induction unit indicator lights, coolant level (if water-cooled units), PPE stock at each station, quench tank level and condition, member sign-in log current, facility safety checklist signed by supervisor on duty"
      performed_by: operator
      # 'Operator' = supervisor on duty. Daily documented check is the baseline
      # risk-management for a shared-access facility where the supervisor cannot
      # know the prior-session condition without explicit verification.
    weekly:
      task: "Coil and station inspection: visual inspection of all induction coil housings for cracks or discoloration, electrical connection check, ventilation airflow measurement at extraction points, anvil and stand stability check, hand-tool inventory and condition, member booking log review for anomalies"
      performed_by: operator
    monthly:
      task: "Calibration and compliance check: induction unit temperature calibration against reference probe (if pyrometer equipped), PPE inventory against active member count, first-aid kit restock, OSHA compliance checklist review, supervisor safety-log review and anomaly escalation to member steward"
      performed_by: journeyman
      # Monthly calibration requires the supervisor's journeyman-level judgment
      # (ability to assess coil condition, temperature accuracy, and compliance
      # posture); not delegable to a member without equivalent skill.
    quarterly:
      task: "Induction coil and power-system service: full coil inspection by specialist or per manufacturer service protocol; blower motor and ductwork inspection and cleaning; quench tank fluid change; full PPE replacement cycle; member safety-certification renewals as needed"
      performed_by: specialist
    annual:
      task: "Full facility safety review: comprehensive equipment assessment, electrical panel inspection and certification, insurance compliance review, cooperative member safety-audit participation, annual supervisor performance review by member steward"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 30
  # 30 min/day: pre-session station check and sign-in verification (10 min),
  # induction unit startup confirmation and ventilation system check (5 min),
  # post-session shutdown, station cleanup, and log completion (15 min). Lower
  # than forge-009 (60 min/day for coal training floor) because induction startup
  # is near-instant (no fire-establishment sequence) and the member-model shifts
  # some cleanup responsibility to members per shop protocol.

  max_active_hours_realism_note: >-
    40 hr/wk is the gross booked-hours ceiling. Net of 30 min/day startup-
    shutdown overhead on a 5-day scheduled week (30 min × 5 = 150 min = 2.5
    hr/wk), effective session hours are approximately 37.5 hr/wk. Downtime
    fraction of 0.12 accounts for coil-failure events (~3%), blower and
    maintenance windows (~2%), seasonal utilization trough (~4%), and booking
    gaps and session cancellations (~3%). Net effective hours/yr:
    37.5 hr/wk × 52 × (1 − 0.12) ≈ 1,716 hr/yr. sim_params uses the derated
    figure. Note: 40 hr/wk reflects the scheduling model (booked slots across
    7-day availability), not a single-operator full-time production ceiling;
    the facility is part-time for each individual member but continuous across
    the member pool.

  interruption_notes: >-
    Member-access model introduces different interruption patterns than a
    commercial single-operator shop. Typical interruptions: member booking
    check-in and orientation for new sessions (~5–10 min/session change),
    supervisor intervention for technique questions or safety concerns (~5–15
    min/session distributed across active stations), station turnover between
    members (equipment re-configuration, brief cleaning, ~10 min/turnover).
    These are folded into the effective utilization rate via the throughput
    aggregates and training_output product-mix share.

  consumables_lead_time_days: { typical: 5, worst: 30 }
  # Typical: steel stock and safety consumables from regional supplier (5 days).
  # Worst: induction coil from specialist supplier with backorder (30 days);
  # steel stock during supply disruption events. Induction coil is the critical
  # long-lead-time item; multiple stations reduce single-coil-failure impact.

  throughput_variance:
    seasonal: "Fall and winter higher member utilization (academic-year-like rhythm; indoor forge activity competes favorably with outdoor alternatives); summer trough as members travel and outdoor activities reduce bookings"
    worst_month_fraction_of_average: 0.6
    best_month_fraction_of_average: 1.3

  operator_impact:
    noise_db: 70
    # Induction forging and manual hammering. Induction units are near-silent
    # (electrical hum, ~50–55 dB); hammering on anvil is the dominant noise
    # source (~70 dB at operator position for manual work). Materially quieter
    # than coal facilities (forge-009: 85 dB; forge-003 comparable). PPE hearing
    # protection should still be available but is not mandatory at 70 dB;
    # extended daily exposure approaching 8 hr at 70 dB would require protection
    # per OSHA standards. Member sessions are typically 2–4 hr.
    # [CITATION-NEEDED: noise level for induction forge facility with manual
    # hammering; measured data from comparable induction workshop preferred.]
    heat_exposure: "Local heat at anvil station during active forging; induction coil directs heat to workpiece rather than ambient environment; facility ambient temperature lower than coal forge; adequate with mechanical extraction; summer management important"
    emissions: "Very low on-site combustion emissions; induction-electric produces no combustion products; metal fume and scale particulate require mechanical extraction per OSHA; upstream grid emissions apply but are off-site; regulatory posture substantially cleaner than coal"
    physical_demand: "Moderate; manual hammering and sustained standing are primary physical demands; lighter than coal forge work (no fire management, no heavy coal handling); accessible to a wider range of members including those with moderate physical fitness"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Light-industrial or mixed-use zoning; induction-electric avoids coal-combustion zoning restrictions, opening urban and suburban sites that are foreclosed to coal (forge-003); confirm local hot-work ordinance applies regardless of fuel source; ≥150A electrical service required"
  emissions: "No combustion emissions requiring air-quality permit at point of use; metal-fume extraction required per OSHA 29 CFR 1910.252; grid-electricity upstream emissions are off-site and do not trigger local air-quality permits; substantially lower regulatory burden than coal"
  other: "OSHA hot-work standards (29 CFR 1910.252) apply to shared-access workshop; shared-use facility liability and insurance substantially higher than single-operator shop; electrical service upgrade permit required; cooperative should carry general liability, property, and workers-compensation coverage; state cooperative-corporation registration required for legal-form protection"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: poor
  # Not a commercial production operation; member-sold output is individual
  # member income, not cooperative revenue. The cooperative generates revenue
  # from membership fees and session fees, not from selling forge output.
  # Market lens is poor: the facility cannot sustain itself on product sales.
  cooperative: good
  # Primary lens. Member-owned cooperative structure with formal bylaws,
  # paid-subscription membership, safety-certification requirement, and
  # Ostrom-compliant governance. See lens_context.cooperative.
  civic: marginal
  # Municipal makerspace partnership is possible: town provides space, cooperative
  # operates. Not municipally owned; civic lens is marginal because governance
  # authority rests with cooperative membership. Workforce-development and tool-
  # access-equity framing supports a marginal civic case.

scale_fit:
  village: poor
  # Member pool too thin at village scale (500–2,000 residents) to sustain ≥50
  # active members needed to cover operating costs including supervisor wage.
  # Induction equipment's higher capital cost relative to coal tool-libraries
  # exacerbates viability at low member counts.
  town: good
  # Target scale: 2,000–15,000 residents. Sufficient population for ≥50 active
  # members and a supervisor wage. Urban/suburban siting compatibility (induction
  # avoids coal zoning) is particularly advantageous at town scale where mixed-use
  # and light-industrial zoning is available without rural acreage.
  small_city: good
  # Per-member cost falls further; scheduling demand supports extended hours
  # and potentially a second shift or second supervisor. Member pool broadens;
  # marketing reach for membership drive is larger.

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:

  cooperative:
    membership_boundary: >-
      Paid annual membership open to residents and workers within the town/city
      and adjacent communities. Annual fee: $600–$1,200/yr (sliding scale
      available; suggested mid-point $900/yr); per-session booking fee in addition
      to annual membership ($15–30/session depending on duration). No craft
      experience prerequisite for membership; safety certification (Stage 1, ~4
      sessions) is required before booking a forge station independently. Members
      who have not yet completed safety certification may attend supervised open-
      house sessions. No demographic restriction; open to adults (18+); supervised
      minors with parental consent may be accommodated by bylaw provision with
      additional supervision ratio requirements. Minimum viable membership:
      ≥50 active fee-paying members to sustain operating costs including supervisor
      wage at town scale. [CITATION-NEEDED: comparable tool-library membership
      pricing; US tool-library network rate-card survey.]

    rules_source: >-
      Registered cooperative bylaws adopted at founding and amendable by member
      vote (see member_amendment_process). Bylaws govern: membership categories
      and fee structure, safety-certification requirement and exemption procedure,
      booking system rules and scheduling priority, supervisor hiring and performance
      review, equipment-damage liability (member responsible for negligent damage),
      output-sales policy (members retain income from own work; cooperative takes
      no consignment commission), and cooperative dissolution procedure. Shop
      safety protocol is a standing exhibit to the bylaws, updatable by the board
      with 14-day member notice without full bylaw amendment.

    monitoring: >-
      Session sign-in log (digital or paper) records every member booking,
      station used, duration, and supervisor on duty. Safety-certification status
      tracked per member; expired or incomplete certifications flag for renewal
      before booking confirmation. Monthly audit by elected member steward:
      reviews session log for anomalies (unapproved bookings, certification gaps,
      equipment-damage incidents), verifies dues current, and reviews supervisor
      daily-check log. Equipment-damage incidents logged and escalated per
      graduated-sanctions track. Annual financial review by member-elected audit
      committee; external audit recommended every 3 years for cooperatives
      receiving public grant funds.

    graduated_sanctions: >-
      Warning (verbal, logged by supervisor in session record) → written notice
      with mandatory corrective action (specific to the violation: e.g., re-take
      safety module, supervised-only booking restriction for 30 days) → 30-day
      suspension from facility access → membership review by 3-member board
      panel with right to appear → membership revocation with pro-rated fee
      refund where applicable. Safety violations (PPE non-compliance, unauthorized
      modifications to equipment, behavior endangering other members) may bypass
      warning steps at supervisor discretion, subject to board review within
      14 days. Equipment-damage (negligent, not accidental): member liable for
      replacement cost; failure to pay within 30 days triggers escalation track.

    conflict_resolution: >-
      Day-to-day facility disputes (scheduling conflicts, station disagreements)
      resolved by supervisor as floor authority with appeal to member steward.
      Member-vs-member disputes and appeals of supervisor decisions: elected
      member steward (informal mediation, target 14-day resolution). Unresolved
      disputes referred to 3-member peer-panel drawn by lot from the full
      membership; panel decision binding subject to annual-meeting appeal.
      Disputes involving the supervisor's employment or conduct: resolved by the
      board. Internal resolution mechanisms are exhausted before external referral.

    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6, 7]
    # Principle 1 (clearly defined boundaries): paid annual membership with
    #   safety-certification requirement; geographic scope (town + adjacent
    #   communities); formal application and fee structure.
    # Principle 2 (congruence): fees and session charges calibrated to actual
    #   operating costs; sliding scale aligns contribution with member means;
    #   supervisor on-floor requirement matched to safety needs.
    # Principle 3 (collective choice): bylaws amendable by member vote with stated
    #   threshold and notice period; shop protocol updatable by board with member
    #   notice; members can propose agenda items at annual meeting.
    # Principle 4 (monitoring): session sign-in log, monthly steward audit,
    #   supervisor daily check, annual financial review.
    # Principle 5 (graduated sanctions): documented six-step track above; safety
    #   bypass with board review preserves due process.
    # Principle 6 (conflict resolution): tiered internal mechanism with peer-panel
    #   as binding arbitrator before external referral.
    # Principle 7 (nested organisations): federation with US tool-library network
    #   (see Historical Lineage) provides the nesting layer — shared governance
    #   resources, insurance pooling, and peer-cooperative mutual aid. Partially
    #   addressed: formal federation depends on network participation, which is
    #   voluntary.
    # Principle 8 (external recognition): satisfied by cooperative-corporation
    #   registration and OSHA compliance documentation.

    member_amendment_process: >-
      2/3 vote at annual general meeting; 30-day advance written notice required
      for proposed amendments (posted to members and on cooperative premises and
      digital member channel). Emergency amendments (safety-critical rule changes)
      may be enacted by the board with 7-day notice and ratified at the next
      general meeting; failure to ratify automatically reverts the emergency
      amendment. Shop safety protocol exhibit may be updated by board vote with
      14-day member notice; no full amendment process required for protocol
      updates.

    legal_form: >-
      State-registered cooperative corporation (consumer-cooperative or
      worker-cooperative variant depending on whether the supervisor is a worker-
      member or an employee; consumer-cooperative is simpler if supervisor is
      hired staff). Legal form provides: limited liability protection for members,
      external recognition satisfying Ostrom Principle 8, access to cooperative-
      specific financing, and institutional continuity to hold assets across
      supervisor transitions. Jurisdiction: state of operation; model articles
      from state cooperative-corporation statute or NCBA CLUSA model articles
      recommended. Alternatively: 501(c)(3) nonprofit if community-benefit framing
      is preferred and commercial-activity thresholds are manageable.
      [CITATION-NEEDED: state cooperative-corporation statute reference; NCBA
      CLUSA model articles; 501(c)(3) qualification criteria for tool-library
      organizations.]

    scale_fit_note: >-
      Governance rules calibrated for town scale (population ≥3,000 to generate
      ≥50 active fee-paying members at realistic participation rates of 1.5–2%
      of adult population). At village scale, the minimum viable membership is
      unachievable without drawing from a multi-village region, which requires a
      federated governance structure out of scope for this entry. At small-city
      scale, rules transfer directly; quorum thresholds may need upward adjustment
      for larger member bodies, and the annual general meeting may need proxy-vote
      provisions. Per-member cost falls at small-city scale, improving viability.

  civic:
    political_coalition: >-
      Municipal economic-development or workforce-development office (tool-access
      equity framing; small-business incubation); parks-and-recreation or community-
      services department if a makerspace-partnership model is used (town provides
      space, cooperative operates facility); library board (tool-library per-capita
      benchmark framing — see benchmark_comparison); small-business alliance
      (potential members and advocates). Secondary: neighborhood associations in
      mixed-use zones where siting is proposed (induction facility is quieter and
      lower-emissions than coal, reducing neighborhood opposition typically faced
      by forge proposals).

    council_vote_estimate: >-
      Not seeking council approval for operating authority (cooperative is
      privately governed). Municipal engagement is limited to: (a) light-industrial
      or mixed-use zoning permit (routine; no council vote typically required for
      by-right use in designated zones); (b) potential space-sharing arrangement
      if town provides a building (requires council approval; estimated 4-2 or
      5-2 favorable in workforce-development-prioritizing councils; opposition
      argument: liability exposure and competing use of municipal space). The
      cooperative does not depend on municipal governance authority; the civic
      lens is marginal precisely because the facility's viability is cooperative-
      member-funded, not municipal-budget-funded.

    competes_with_private: >-
      The cooperative is not structured to compete with private commercial smiths:
      it provides member access to equipment, not commercial production services.
      A private commercial smith producing for market is in a different product
      line (high-volume, consistent output) than the member-access cooperative
      (intermittent individual member projects, repair, and learning). In towns
      where a private smith operates, the cooperative refers commercial work to
      that operator and may develop a referral relationship where the private
      smith directs interested non-commercial clients to the cooperative. No
      displacement of functioning private operators is anticipated.

    governance_form: >-
      Member-owned cooperative corporation. The municipality has no ownership or
      operational authority. The civic relationship is limited to: zoning
      compliance (land-use), potential space-sharing or lease arrangement (funding
      and operations), and light-industrial electrical permit (infrastructure).
      Under a municipal-partnership model, the municipality owns the building
      and the cooperative holds an operating lease; governance of the facility
      remains entirely with the cooperative membership.

    budget_line: >-
      No municipal operating budget line under the standalone cooperative model.
      Under a municipal-partnership model: capital contribution may come from
      municipal economic-development or workforce-development fund (one-time or
      matching grant); operating costs remain cooperative-funded from member fees
      and session fees. Cooperative operating budget estimate: annual maintenance
      $3,000 + consumables $2,800 + rent $6,600 + supervisor wage $52,000 (per
      SCALES.md §3 journeyman rate) = ~$64,400/yr operating cost floor. Revenue:
      50 members × $900/yr avg = $45,000 + session fees ~$10,000 = $55,000/yr
      at minimum viable membership. Gap at minimum: ~$9,400/yr — requires either
      higher membership, higher session fees, or supplemental grant.
      [CITATION-NEEDED: comparable tool-library operating cost and revenue data.]

    benchmark_comparison: >-
      Per-household annual cost at town scale (5,000 households): $64,400/yr
      total operating cost ÷ 5,000 hh = ~$12.88/hh/yr if fully municipally
      funded (not the model; stated for comparison). At small-city scale (25,000
      hh): ~$2.58/hh/yr. US tool-library benchmark for comparison: the Berkeley
      (CA) Tool Lending Library serves ~50,000 residents with an annual operating
      budget of approximately $300,000, implying ~$6/hh/yr for a comprehensive
      civic tool-library [CITATION-NEEDED: Berkeley Tool Lending Library budget
      figures]. Town library per-capita benchmark: ~$42/hh/yr in peer towns (per
      forge-003 established benchmark). The cooperative forge-015 per-household
      cost, even if fully publicly funded, is below the town-library benchmark;
      the cooperative model shifts most cost to member fees, reducing the public
      burden further.

    staffing_model:
      role: "1 journeyman supervisor (contracted floor supervisor; part-time to full-time depending on booked hours)"
      operator_fte: 1.0
      # Full-time at 40 hr/wk booked-hours ceiling; may reduce to 0.6–0.8 FTE
      # if scheduling concentrates sessions on fewer days.
      wage_assumption: 52000
      # Journeyman smith supervisor at $52,000/yr. Per SCALES.md §3 town-scale
      # journeyman skilled-trades median. Lower than forge-009 master instructor
      # ($62,000/yr) because supervisor role is journeyman-level (safety oversight
      # and member support), not master-level instruction with formal curriculum.
      wage_source: "corpus/program/SCALES.md §3 town-scale journeyman skilled-trades median"
      hours: "40 hrs/wk floor supervision, member support, safety oversight, daily maintenance checks, and booking administration"
      hiring_notes: >-
        Journeyman smith with hot-work safety experience and comfort in a
        multi-user teaching environment. Hiring pool is regional (50–100 mile
        radius); more accessible than master-smith hiring pool (forge-009) because
        journeyman-level candidates are more numerous. Cooperative member-supervisor
        model (long-tenured member promoted to supervisor role) is a viable
        internal pipeline after 3–5 years of operation. Part-time framing
        ($26/hr equivalent at 40 hr/wk) may attract skilled-trades workers seeking
        supplemental income or transitioning from production smithing.

    civic_externalities:
      - "Tool-access equity: provides metalworking access to urban and suburban residents who lack the space, capital, or zoning permissions to operate a private forge; reduces barriers to craft skill development across income levels"
      - "Learning infrastructure: safety-certification requirement and structured member-learning stages create a documented pathway from novice to competent independent metalworker; functions as community technical education without formal school enrollment"
      - "Repair culture externality: member repair projects (30% of output) reduce metal-goods throwaway consumption; cooperative provides a community resource for durable-goods repair that market alternatives (commercial smiths) typically decline as economically unviable"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 85000
  # Equals economics.capital_cost.mid per E3-R1.

  cost_sd: 17500
  # (high − low) / 4 = (120,000 − 50,000) / 4 = 17,500.
  # cost_sd / cost_mean = 17,500 / 85,000 ≈ 0.21 — within E3-R5 range (0.15–0.50).

  throughput_units_equiv_per_year: 1440
  # Derivation (per smithing SCHEMA.md §1 E-3 guidance):
  # Gross booked hours: 40 hr/wk.
  # Startup-shutdown: 30 min/day × 5 days = 150 min = 2.5 hr/wk. Net: 37.5 hr/wk.
  # Downtime fraction: 0.12.
  # Effective hours/yr: 37.5 × 52 × (1 − 0.12) = 37.5 × 52 × 0.88 ≈ 1,716 hr/yr.
  # Saleable output share: 60% (repair 30% + specialty 30%; training_output 40% excluded).
  # Revenue-eligible hours: 1,716 × 0.60 ≈ 1,030 hr/yr.
  # Product mix within saleable share (repair 50%, specialty 50% normalized):
  #   repair → small/medium mix blended rate ~2.0 units/hr;
  #   specialty → medium/large mix blended rate ~0.8 units/hr.
  # Blended saleable rate: 0.50 × 2.0 + 0.50 × 0.8 = 1.0 + 0.4 = 1.4 units/hr.
  # Annual throughput equiv: 1,030 hr × 1.4 units/hr ≈ 1,442 ≈ 1,440 units/yr (rounded).
  # Unit = small-work equivalent. Training_output hours excluded from revenue-eligible
  # count; cost folded into lower effective-hour denominator via downtime fraction.

  variable_cost_per_unit: 4.20
  # Annual consumables ($2,800/yr) allocated to revenue-eligible units:
  # $2,800/yr ÷ 1,440 units ≈ $1.94/unit.
  # Electricity cost in consumables already includes session-time energy;
  # no separate energy addition needed (consumables field covers electricity).
  # Additional variable component: incremental steel stock for repair sessions
  # (member supplies own stock for personal specialty work; cooperative provides
  # stock for class/repair sessions) — approximately $0.50/unit additional.
  # Adjusted total: ~$2.44/unit direct materials. Rounded up to $4.20 to include
  # a per-unit allocation of maintenance ($3,000/yr ÷ 1,440 = $2.08/unit).
  # Blended variable cost including maintenance allocation: ~$4.20/unit.
  # [CITATION-NEEDED: per-unit materials and maintenance cost validation.]

  labor_hours_per_unit: 1.19
  # Effective hours/yr (1,716) ÷ throughput_units_equiv_per_year (1,440) ≈ 1.19.
  # Reflects total supervised facility hours per output-equivalent unit, including
  # the training_output overhead share — consistent with E3-R3. The ratio is higher
  # than a commercial single-operator shop because training_output (40%) reduces
  # market-equivalent unit count without reducing supervisor labor hours.

  downtime_fraction: 0.12
  # Sources: seasonal trough (summer, worst-month 0.6×; ~4 weeks partial operation
  # per year ≈ 4%); induction coil failure events (~3% of scheduled hours per year
  # over multi-station facility where one station may be down at a time, with
  # partial facility operation continuing); blower and equipment maintenance (~2%);
  # booking gaps and session-cancellation events (~3%). Total: ~12%. Consistent
  # with operations_reality failure profile: multi-station configuration means
  # single-coil failure is a partial-downtime event, not a full-facility shutdown,
  # keeping effective downtime fraction lower than a single-station entry.

  lifespan_years: 15
  # Induction equipment with periodic coil replacements has a 15–20 year horizon.
  # 15 years is a conservative cooperative-asset planning figure; coil replacements
  # are mid-life maintenance events, not replacements of the full unit. The
  # shorter lifespan horizon vs. coal entries reflects induction power electronics
  # having a shorter MTBF than refractory-and-steel coal forge construction.
  # [CITATION-NEEDED: induction forge system lifespan estimate from manufacturer
  # or comparable facility data.]

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: fail
    primary_metric: 2.1254329747998146
    metric_name: payback_years
    notes: wage_verdict=fail (take_home=37878 vs median=48000)
  village_coop:
    verdict: fail
    primary_metric: 95.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=95, total_annual_cost=18867
  village_civic:
    verdict: fail
    primary_metric: 18.066666666666666
    metric_name: per_household_cost
    notes: per_hh=18.07, threshold=120, hrs/capita=0.000 vs threshold=2.0
  town_market:
    verdict: fail
    primary_metric: 2.1254329747998146
    metric_name: payback_years
    notes: wage_verdict=fail (take_home=37878 vs median=56000)
  town_coop:
    verdict: win
    primary_metric: 95.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=95, total_annual_cost=18867
  town_civic:
    verdict: fail
    primary_metric: 2.6568627450980395
    metric_name: per_household_cost
    notes: per_hh=2.66, threshold=100, hrs/capita=0.000 vs threshold=2.0
  small_city_market:
    verdict: fail
    primary_metric: 2.1254329747998146
    metric_name: payback_years
    notes: wage_verdict=fail (take_home=37878 vs median=62000)
  small_city_coop:
    verdict: win
    primary_metric: 95.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=95, total_annual_cost=18867
  small_city_civic:
    verdict: fail
    primary_metric: 0.5018518518518519
    metric_name: per_household_cost
    notes: per_hh=0.50, threshold=80, hrs/capita=0.000 vs threshold=2.0
sources:
  - ref: "Ostrom, Elinor. 1990. Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press — design principles 1–8 for commons governance; Principle 7 (nested organisations) cited for tool-library network federation framing"
  - ref: "corpus/program/SCALES.md §3 — town-scale journeyman skilled-trades median wage ($52k/yr supervisor) and town/city commercial rent estimates"
  - ref: "OSHA 29 CFR 1910.252(c) — hot-work and forge safety standards applicable to multi-operator shared-access workshop"
  - ref: "US tool-library network — modern tool-library cooperative movement in the United States; shared-equipment access model funded by membership fees; safety-certification and booking protocols; federation through peer networks (US Tool Library Network and comparable regional organizations). Functional inheritance: membership-fee funding model, booking-based access, safety-certification prerequisite, and peer-cooperative federation as Ostrom Principle 7 analog. [CITATION-NEEDED: US Tool Library Network documentation; specific network directory or governance reference — e.g., localtools.org or comparable network registry; Berkeley Tool Lending Library operating budget data.]"
  - ref: "Song-dynasty China coal-to-coke fuel transition (10th–13th century CE) — the shift from raw-wood charcoal to coal and coke in Chinese metallurgy enabled industrial scale that fuel-constrained charcoal could not support, and opened siting options in coal-adjacent regions that deforestation pressure had closed to charcoal-dependent operations. Cited here as an analog for the CERES 'cleaner-fuel enables different scales' pattern: just as the Song transition was a regulatory-compatibility and resource-availability win (not an aesthetic choice), the induction-electric transition in shared workshops is a zoning-and-permitting win, not a nostalgic craft return. Anti-romantic note: the Song coal transition was not primarily about cleanliness or craft values — it was driven by fuel economics and depletion of coppiced woodland near urban centers. The CERES induction transition is driven by regulatory access to urban sites; both are pragmatic fuel choices with distributional consequences for who can operate and where. [CITATION-NEEDED: academic source on Song-dynasty coal/coke metallurgical transition — e.g., Hartwell, Robert 1962, 'A Revolution in the Chinese Iron and Coal Industries During the Northern Sung, 960-1126 A.D.', Journal of Asian Studies; or Needham, Joseph, Science and Civilisation in China Vol. 5.]"
  - ref: "OSHA 29 CFR 1910.252 — general-industry hot-work safety standards; ventilation requirements for forge environments regardless of fuel source"
  - ref: "[CITATION-NEEDED: multi-station induction workshop capital cost $50,000–$120,000; no published benchmark at authoring date; derived from equipment pricing aggregates for commercial induction forge units and multi-station tooling]"
  - ref: "[CITATION-NEEDED: 3-phase electrical service install cost $12,000; regional contractor estimate ranges; SCALES.md §4 electrical infrastructure cost]"
  - ref: "[CITATION-NEEDED: annual maintenance cost $3,000 for multi-station induction workshop; comparable facility data]"
  - ref: "[CITATION-NEEDED: annual consumables $2,800 including electricity at $0.12/kWh; regional utility rate per SCALES.md §4; steel stock for classroom use]"
  - ref: "[CITATION-NEEDED: town/city commercial floor-space rent $165/m²/yr effective rate; SCALES.md §4 commercial rent estimate for light-industrial/mixed-use]"
  - ref: "[CITATION-NEEDED: member-sold specialty smithing piece market price $30–$100; inferred from comparable community-smithing cooperative output pricing; market survey needed]"
  - ref: "[CITATION-NEEDED: commodity forged-hardware industrial baseline price $10/unit; hardware-store pricing survey]"
  - ref: "[CITATION-NEEDED: comparable tool-library membership pricing $600–$1,200/yr; US tool-library network rate-card survey; localtools.org or comparable source]"
  - ref: "[CITATION-NEEDED: induction coil MTBF ~1,800 hr; manufacturer specification for mid-grade commercial induction forge unit; smithing SCHEMA.md §4 baseline range 1,500–2,500 hr]"
  - ref: "[CITATION-NEEDED: blower motor MTBF ~2,500 hr for mechanical-extraction system; smithing SCHEMA.md §4 baseline 1,500–3,000 hr]"
  - ref: "[CITATION-NEEDED: noise level 70 dB for induction forge with manual hammering; measured data from comparable induction workshop]"
  - ref: "[CITATION-NEEDED: induction forge system lifespan 15 years; manufacturer or comparable facility data]"
  - ref: "[CITATION-NEEDED: Berkeley Tool Lending Library annual operating budget ~$300,000; City of Berkeley Parks, Recreation and Waterfront Department budget records or comparable civic tool-library benchmark data]"
  - ref: "[CITATION-NEEDED: comparable tool-library operating cost and revenue data for cooperative model; US Tool Library Network survey or case-study data]"
  - ref: "[CITATION-NEEDED: state cooperative-corporation statute reference; NCBA CLUSA model articles; 501(c)(3) qualification criteria for tool-library organizations]"
  - ref: "[CITATION-NEEDED: seasonal utilization pattern for shared-access maker/tool facilities; academic-year demand rhythm data]"
---## Summary

The Tool-Library Member-Access Induction Forge (forge-015) is a member-owned cooperative providing subscription-based shared access to 3–4 induction-electric forge stations in a 30–50 m² facility within urban or suburban commercial space. Members pay annual dues and per-session booking fees; a journeyman supervisor is on-floor whenever stations are active; members work under shop protocol at their own stations. The cooperative is the primary ownership and governance vehicle. The design is the induction-electric counterpart to the coal-based shared tool-library (forge-003) and is distinguishable from the civic makerspace (forge-004) and the apprentice training cooperative (forge-009) by its consumer-cooperative structure, its lower regulatory footprint, and its target niche of urban and suburban populations where coal-forge zoning and emissions requirements would block siting entirely.

## Design rationale

The problem this entry solves is the absence of a cooperative-primary, induction-electric, multi-station shared-access design calibrated for urban and suburban settings. Forge-003 models the coal-based shared tool-library with comparable governance but a heavier regulatory footprint; forge-004 is civic-primary; forge-009 is a formal training cooperative with a journeyman-certification curriculum and master-instructor requirement. Forge-015 occupies a distinct niche: it is the design choice for cooperative groups in locations where coal is regulatory-foreclosed (urban zoning, emissions ordinances, building codes that exclude combustion stacks) but where a member population of 50–100 households can sustain a shared induction facility. The induction-electric choice is a regulatory-compatibility decision, not a preference statement about fuel types: coal forges can achieve higher temperatures and forge-weld capability that induction cannot reliably match at standard commercial configurations, but those capabilities are not the target output of a member-access learning-and-repair facility. The capital cost is higher than a coal tool-library at the same footprint; the trade is regulatory access to urban-density member pools large enough to amortize the higher capital cost across a viable membership.

## Historical lineage

Two precedents inform this design, both requiring anti-romantic treatment.

**Modern US tool-library movement.** The US tool-library movement — catalyzed by public library-model institutions such as the Berkeley Tool Lending Library (1979) and amplified through municipal makerspace programs and cooperative tool-sharing networks in the 2000s–2020s — provides the direct institutional template: a membership-fee-funded cooperative or civic facility providing access to capital equipment that individuals cannot economically own individually. The functional inheritance is the booking-based access model, the safety-certification prerequisite, the membership-boundary tied to a geographic service area, and the per-capita cost benchmark that justifies the civic-institutional comparison (forge-015 borrowing the "tool-library per-capita vs library per-capita" framing from this tradition). What this entry does not inherit from the tool-library movement is the tool-library's typically non-hazardous equipment profile: a forge, unlike most tool-library equipment, involves hot-work hazards that require a credentialed supervisor present at all times, substantially raising the labor cost compared to a library where trained volunteers can check out a drill press. The supervisor requirement differentiates the forge tool-library from an open-access tool-library economically; it is not a design flaw but a safety reality. [CITATION-NEEDED: US Tool Library Network documentation; Berkeley Tool Lending Library history and operating model.]

**Song-dynasty China coal-to-coke fuel transition as CERES analog.** The transition from charcoal to coal and coke in Song-dynasty China (10th–13th century CE) is cited not as a cultural precedent for cooperative governance but as the canonical CERES example of a fuel-transition pattern that changed what scales and sites were viable for metal production. Hartwell's analysis of the Northern Song iron and coal industries identifies a step-change: when coal (and later coke) became the primary forge fuel, production could site near coal deposits rather than near managed woodland, and the scale of output became constrained by capital and labor rather than by fuel-supply radius. The analog for forge-015 is structural, not historical: just as the Song coal transition opened siting options foreclosed by charcoal-woodland proximity requirements, the induction-electric transition opens urban siting options foreclosed by coal-combustion regulations. The anti-romantic framing is essential here: the CERES pattern is not "electric is better" — it is "different fuels impose different site-selection constraints, and operators who match their fuel choice to their siting context outperform operators who apply the wrong fuel to the wrong site." An urban cooperative that attempts coal-based operation faces emissions permits, dedicated-exhaust requirements, and potential zoning variances that an induction facility avoids entirely; the cost of that regulatory friction is the practical argument for induction in this niche, not an aesthetic preference for clean technology. Forge-015 would not be recommended for a rural setting where coal-zoning is unproblematic and induction's capital premium buys no siting advantage. [CITATION-NEEDED: Hartwell 1962 on Song-dynasty coal/coke transition; Needham Vol. 5 on Chinese metallurgy.]

## Key assumptions

**Capital cost ($50,000–$120,000, mid $85,000):** No published benchmark for a multi-station cooperative induction forge was identified at authoring date. The estimate is derived from commercial induction forge unit pricing (mid-grade units: $15,000–$25,000 each × 3–4 stations), multi-station tooling bank ($8,000–$15,000), safety equipment and quench infrastructure ($3,000–$6,000), ventilation system ($5,000–$10,000), and miscellaneous fit-out. The range reflects used/refurbished (low) versus purpose-built new (high). Flagged with [CITATION-NEEDED] throughout; should be replaced with procurement data before promotion to `reviewed`. The mid-capital skew ($85,000 vs arithmetic midpoint $85,000) is symmetric; the range is wide because equipment sourcing variance is high at this scale.

**Throughput (aggregate 4 small/1 medium/0.2 large per hour at 3-station peak):** These are facility-aggregate rates at peak simultaneous booking, not per-operator rates. A journeyman at a single station could produce 4–6 small_work/hr; member-average across 3 stations is lower due to skill variance and higher reheat frequency among learning members. The 4/hr facility aggregate is a rough estimate; experimental measurement at a comparable induction-forge facility would be required for validation. The induction temperature ceiling (~900–1100°C practical) limits large-work rates relative to coal.

**sim_params.throughput_units_equiv_per_year (1,440):** Fully derived in the frontmatter derivation note. The 60% saleable-output share (training_output 40% excluded) is the key assumption; if the member mix skews more heavily toward learning and less toward production, saleable share falls and per-unit cost rises. The 1.4-unit/hr blended saleable rate uses a simplified repair/specialty mix weighting; the explicit weighting is stated in the derivation.

**Supervisor wage ($52,000/yr):** Anchored to SCALES.md §3 town-scale journeyman rate. At minimum viable membership (50 members × $900 avg = $45,000 dues + $10,000 session fees = $55,000 revenue), the supervisor wage alone ($52,000) consumes nearly all revenue, leaving ~$3,000 for maintenance, consumables, and rent ($12,400 combined). The cooperative is not financially self-sustaining at minimum viable membership on dues and session fees alone without either higher membership, higher fees, or supplemental revenue (grants, classes). This is the primary financial risk and is named explicitly in Known Risks.

**Downtime fraction (0.12):** Multi-station configuration is the key moderating factor: when one induction coil fails (21-day lead time), two remaining stations continue operation. This reduces effective downtime per failure event compared to a single-station entry. Seasonal trough (summer, worst-month 0.6×) is the dominant downtime contributor; equipment failures add approximately 5% on top of seasonal losses. Total 0.12 is the central estimate; should be validated against actual tool-library or makerspace booking-utilization data.

## Known risks and failure modes

**Regulatory risks:** Induction-electric avoids coal-combustion air-quality permits and dedicated-exhaust requirements, but does not eliminate regulatory exposure. OSHA 29 CFR 1910.252 applies to hot-work environments regardless of fuel source; the multi-member shared-access model creates higher OSHA liability than a single-operator shop. The electrical service upgrade (≥150A 3-phase) requires a commercial electrical permit; cost and timeline can surprise cooperative founders who budget only for equipment. Shared-use facility liability insurance is substantially higher than single-operator shop coverage — the cooperative carries general liability for member activities, and an injury during a booked session is a first-party liability event. The cooperative should obtain insurance quotes before committing to a lease, as the insurance cost is a material line item not fully captured in the annual_maintenance and consumables fields. In urban mixed-use buildings, the landlord's building insurance and hot-work policies may impose additional requirements (sprinkler systems, fire separation) that add to install cost.

**Labour pipeline risks:** The journeyman supervisor is the facility's critical operational dependency. Unlike forge-003's coal tool-library (where the skill floor is similar but the role is better-defined by the forge-003 cooperative's broader operational history), forge-015's induction-forge supervisor role is relatively novel: there is no established labor market for "induction forge cooperative supervisors" from which to hire. The cooperative must either hire a journeyman smith willing to learn the induction-specific equipment profile, or hire from the small pool of induction-forge practitioners (primarily bladesmith shops, industrial operations, or equivalent forge-002-type small repair facilities). The member-promotion pathway (long-tenured member rising to supervisor) is the long-run mitigation but takes 3–5 years to mature. A cooperative that launches without a credible supervisor-succession plan has a short viable operating horizon.

**Supply chain risks:** The induction coil is the critical single-supplier dependency (21-day lead time at specialist-only serviceability). The multi-station configuration partially mitigates single-coil failure, but a facility with all coils from the same supplier facing a supply disruption (manufacturer delay, distributor stockout) could face extended multi-station downtime. The cooperative should establish supplier diversity where coil geometries permit, or negotiate a stocked-spare arrangement with a specialist to reduce lead time. Electrical service infrastructure is the facility's other supply dependency: a grid outage suspends all operations with no combustion backup. The cooperative should include a session-cancellation protocol and member communication plan for grid-outage events in its operating procedures.

**Financial viability risk:** The structural challenge is the supervisor wage ($52,000/yr) relative to dues-and-session-fee revenue at minimum viable membership ($55,000/yr). At minimum viable scale, the facility has effectively no operating margin for maintenance ($3,000), consumables ($2,800), rent ($6,600), or capital amortization. The cooperative requires either a member base materially above the minimum (75–100 active members) or higher session fees, or supplemental revenue (grant funding, class fees, tool-storage rentals) to be financially stable. New cooperatives should plan for a 2–3 year membership-building phase and secure bridge funding (grants, founding-member pledges, or municipal space subsidy) to cover the operating gap while the membership base grows.

## Iteration log

- 2026-04-18: v0.1 — initial creation; forge-015 Tool-Library Member-Access Induction Forge. COOP-PRIMARY entry per Plan C Task 17 specification. Full v1.1 schema completed. Market lens poor (populated with ancillary member-sales pricing and explicit "not cooperative revenue" note; industrial baseline $10; pricing_validation flagged inferred). Cooperative lens good as primary substantive: Ostrom 1–7 addressed with substantive notes on each principle; Principle 7 via US tool-library network federation; legal_form (cooperative corporation or 501(c)(3)); member_amendment_process (2/3 vote, 30-day notice, emergency bypass with ratification); scale_fit_note (≥3,000 population for ≥50 members); graduated_sanctions with safety-bypass provision; conflict_resolution tiered mechanism; three-stage member-learning apprentice_path (less formal than forge-009; targets competent member access, not journeyman certification). Civic lens marginal: municipal-partnership sketch (town provides space, coop operates); staffing_model with SCALES.md §3 journeyman wage ($52k/yr); benchmark_comparison (tool-library per-capita vs library per-capita per-hh/yr); three civic_externalities. Induction-vs-coal framing cast as regulatory-compatibility (not fuel-quality advocacy); Song-dynasty coal-to-coke analog used as CERES pattern illustration with explicit anti-romantic framing. Two inspirations cited: us-tool-library-network and song-china-coal-to-coke-fuel-transition. No docs/superpowers/ paths. Twenty-two [CITATION-NEEDED] flags placed over fabrication.
