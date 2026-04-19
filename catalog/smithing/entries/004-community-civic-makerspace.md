---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: forge-004
trade: smithing
name: "Community Civic Makerspace — Forge Module"
tagline: "Town-owned supervised multi-user forge; library-model access with structured training program"
status: draft
version: 0.1
supersedes: null
inspirations:
  - japanese-shokunin-training-tradition
  - us-public-library-model
  - jane-jacobs-civic-infrastructure

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 65
# Mid-range of 50–80 m² span (forge module only; makerspace as a whole also houses
# woodworking, textile, and other bays — those are out of scope for this entry).
ceiling_min_m: 4.0
ventilation: dedicated-exhaust-system
# Induction primary reduces combustion emissions substantially; propane backup still
# requires full exhaust. Multi-user model mandates robust extraction (OSHA 29 CFR
# 1910.252(c) applies to public-access hot-work facilities).

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: hybrid-induction-gas
# Induction-electric is the primary working source for daily use: near-zero on-site
# combustion emissions, precise temperature control suited to multi-skill-level users,
# and a cleaner regulatory profile for a public-access facility. Propane provides
# backup and is required for any high-temperature forge-welding operations that exceed
# standard induction ceiling (~1050–1100°C). See smithing SCHEMA.md §2 for capability notes.
energy_consumption_per_active_hour: "8–12 kWh (induction mode); 1.5 kg propane (propane backup mode)"
backup_fuel: propane

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  units_per_hour: { small_work: 2, medium_work: 0.5, large_work: 0.1 }
  # Rates are intentionally lower than single-operator commercial entries. The
  # multi-user supervised model introduces station rotation, supervision pauses,
  # safety briefings, and skill-variation drag. These are lumped averages across
  # all user types (supervisor, experienced members, novice members).
  max_active_hours_per_week: 30
  # Civic scheduling: 5–6 days/wk × ~5 hr/session = 30 hr/wk upper bound.
  # A commercial single-operator shop runs 40–45 hr/wk; the civic model is constrained
  # by scheduled shift slots, community-staffing capacity, and supervision ratios.
  product_mix:
    repair: 30
    commodity: 5
    specialty: 25
    artistic: 0
    training_output: 40
    # training_output extension follows the pattern used in forge-009, forge-011, and
    # forge-015. 40% of active hours are devoted to training-output work (student projects
    # not sold commercially); adding this named field brings the sum to 100.
    # Sum: 30 + 5 + 25 + 0 + 40 = 100. The productive share (repair + commodity +
    # specialty = 60%) drives revenue calculations; training_output hours are reflected
    # in the depressed throughput rates and the product-mix weighting in sim_params.
    # See Key Assumptions for derivation.

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: master
# The civic multi-user model requires a master smith as the floor-supervisor: they
# must simultaneously assess safety across up to 4 member stations, provide real-time
# instruction, and intervene without creating hazard. A journeyman cannot reliably
# maintain instructional authority and floor-wide safety awareness simultaneously
# (see smithing SCHEMA.md §3 for master-tier definition).
operators_concurrent: "1 supervisor + up to 4 members"
# Scheduled shift model: 1 master smith-instructor present at all times; up to 4
# community members work simultaneously under supervision. Shift scheduling enforced
# by sign-up system; concurrent headcount is a safety limit, not a production target.
apprentice_friendly: true
apprentice_path:
  training_stages: >-
    Stage 1 — Orientation and Safety (0–2 months): fire-management fundamentals, PPE
    protocol, tool identification, forging posture, and supervised basic stock prep.
    Competency gate: pass written safety assessment and demonstrate correct use of all
    PPE; complete one supervised session at each of the four workstations.

    Stage 2 — Supervised Small Work (2–8 months): independent small_work production
    (hooks, rings, staples, nails) under weekly review by master smith-instructor.
    Introduction to heat-color reading. Basic tong and hammer selection. No forge welding.
    Competency gate: produce five consistent hooks to dimensional spec within ±3 mm;
    demonstrate heat-color identification (orange/yellow/white) without prompting.

    Stage 3 — Medium Work and Heat Treatment (8–24 months): medium_work production
    (brackets, simple tools, repair operations) with graduated autonomy. Introduction
    to normalize/anneal/harden/temper sequence under supervision. Repair work with
    real customer items begins at 12 months under direct oversight.
    Competency gate: complete a customer repair job independently (with supervisor
    present but not intervening); execute correct hardening and tempering of a simple
    chisel to journeyman-standard finish.

    Stage 4 — Journeyman Progression (24–36+ months): independent production during
    open-shop hours; eligible to assist in training Stage 1–2 members. Demonstrates
    forge-welding awareness (propane mode, supervised). Full independent status granted
    by master smith-instructor after panel review.
  time_to_independent_operation: "~36 months to journeyman standard; structured training integrates with normal supervised shifts"
  succession_note: >-
    The civic model structurally embeds succession: apprentice training is not a
    separate program but the core operating mode of the facility. Each training cohort
    produces 1–3 candidates for journeyman status per 3-year cycle, creating a local
    pipeline that can supply private smiths in the surrounding region. The master
    smith-instructor's departure risk is mitigated by the institutional record
    (curriculum, safety protocols, member log) and by the facility committee's ability
    to recruit a replacement from the journeyman pipeline or the regional trade network.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 80000, mid: 125000, high: 180000 }
  # Forge module only. Low = modest induction unit + used propane backup + basic tooling.
  # Mid = mid-grade induction forge + dedicated propane station + full tooling suite
  #       + ventilation hood and extraction. High = top-spec induction + full propane
  #       redundancy + power-hammer + complete student tooling bank.
  # [CITATION-NEEDED: civic makerspace forge-module capital cost; no published benchmark
  # identified at time of authoring — estimate derived from industrial equipment pricing
  # plus civic-facility overhead multiplier. See Key Assumptions.]

  install_cost: 15000
  # 3-phase electrical service upgrade + dedicated exhaust ventilation system installation.
  # [CITATION-NEEDED: 3-phase electrical + dedicated exhaust install cost estimate;
  # derived from regional contractor estimates per SCALES.md §4 infrastructure ranges.]

  annual_maintenance: 5500
  # Covers routine servicing of induction coil system, propane regulators, ventilation
  # hood, and general workshop equipment. Higher than single-operator entries because
  # multi-user intensity accelerates wear on shared tooling. [CITATION-NEEDED: annual
  # maintenance estimate for comparable civic workshop facilities.]

  annual_consumables: 4200
  # Light relative to commercial entries: civic scheduling is intermittent (~30 hr/wk
  # vs 40–45 hr commercial), induction primary reduces propane consumption to backup
  # only, and the multi-user model shares consumable wear across a member base.
  # Includes: flux, mild-steel stock for training exercises, grinding consumables,
  # PPE replacement, small tooling. [CITATION-NEEDED: consumables estimate.]

  floor_space_rent_per_year: 0
  # Town-owned facility; floor space imputed at $0. Civic ownership eliminates rent
  # as an operating cost. Note: the full facility capital (building) is amortized in
  # the town's broader makerspace budget, not in this forge-module entry. This is a
  # meaningful cost advantage over private or cooperative operators who must pay rent.

  market_price_per_unit: { low: 0, mid: 0, high: 0 }
  # Civic operation; no commercial pricing. The facility does not sell output on
  # the market. Member fees ($50–100/yr) are access/membership charges, not per-unit
  # prices. See pricing_notes for the civic context and industrial_baseline_price
  # for the reference comparator.

  pricing_notes: >-
    This is a civic/training facility, not a commercial producer. market_price_per_unit
    is set to zero because the facility does not sell output at market prices: repair
    work and training-output are provided to members as part of the civic service, not
    priced per item. The industrial baseline price ($10/unit for comparable small-work
    equivalent at industrial-hardware-store pricing [CITATION-NEEDED]) is cited for
    reference only — to document the subsidy level and the value delivered relative to
    commercial alternatives, not as a premium argument. Annual member fees ($50–100/yr)
    are a minimal access charge comparable to a library card, not output pricing.

  industrial_baseline_price: 10
  # Reference baseline for small-work equivalent (hooks, brackets, simple hardware).
  # Cited for lens comparison only; not used in revenue calculations (lens_fit.market: poor).
  # [CITATION-NEEDED: industrial hardware baseline price for small forged-equivalent items.]

  pricing_validation: "N/A — civic operation with no commercial output pricing. Member fees are access charges, not unit prices. Industrial baseline cited for reference comparison only; evidence for baseline is commodity hardware-store pricing [CITATION-NEEDED]."

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:

  first_year_failures:
    - item: "Induction coil (primary heating element)"
      estimated_hours_to_failure: 1800
      replacement_cost: 1400
      replacement_lead_time_days: 21
      serviceable_by: specialist
      # Coil failure is the primary downtime event for induction forges. Replacement
      # requires a specialist familiar with high-frequency power systems; not operator-
      # or journeyman-serviceable in a standard civic workshop setting.

    - item: "Propane regulator (diaphragm wear)"
      estimated_hours_to_failure: 1500
      replacement_cost: 150
      replacement_lead_time_days: 5
      serviceable_by: journeyman
      # Standard regulator wear in the first year under intermittent use. Propane backup
      # is used less frequently than in a propane-primary forge, but regulator integrity
      # is critical when activated; scheduled replacement is prudent.

    - item: "Ventilation hood filter / baffle"
      estimated_hours_to_failure: 1000
      replacement_cost: 200
      replacement_lead_time_days: 5
      serviceable_by: operator
      # Multi-user activity deposits particulate faster than single-operator use.
      # Filter replacement is routine and operator-serviceable; lead time is short.

  maintenance_schedule:
    daily:
      task: "Safety walkdown of all four workstations: clear debris, check PPE stock, verify propane shutoff, inspect induction unit indicator lights, reset sign-in log"
      performed_by: operator
      # 'Operator' here = the master smith-instructor or senior journeyman opening the
      # facility. The multi-user model requires a more thorough daily check than a
      # single-operator shop: four stations, student-use wear, and liability exposure
      # all demand a documented daily safety sign-off before any member enters the forge.
    weekly:
      task: "Full inspection of all workstations: induction coil condition, propane line integrity, ventilation airflow measurement, anvil bases, hand-tool inventory and condition"
      performed_by: operator
    monthly:
      task: "Documented safety walkthrough per town facility-inspection protocol: fire-suppression system check, emergency eyewash station, first-aid kit restock, OSHA compliance checklist"
      performed_by: journeyman
    quarterly:
      task: "Induction coil and power-system service by certified technician; full propane system inspection and pressure-test; ventilation hood and ductwork inspection and cleaning"
      performed_by: specialist
    annual:
      task: "Full facility-wide inspection by town facilities department: structural review, electrical panel certification, insurance assessment, full equipment inventory and valuation update"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 45
  # Safety checks for a shared-user model are substantially longer than for a single-
  # operator shop. 45 min/day accounts for: pre-session safety walkdown (15 min),
  # member check-in and briefing (10 min), post-session equipment shutdown and log
  # completion (20 min). This overhead is non-negotiable given the public-access
  # liability context; see max_active_hours_realism_note.

  max_active_hours_realism_note: >-
    30 hr/wk is the civic scheduling target (gross). Net of 45 min/day startup-shutdown
    overhead on a 5-session week (not necessarily 5 consecutive days; civic scheduling
    varies), effective production/instruction hours are approximately 26.25 hr/wk.
    sim_params.throughput_units_equiv_per_year uses the derated figure of ~26 hr/wk.
    Civic scheduling further reduces effective hours: public holidays, event conflicts,
    and staff absence account for an additional ~10–15% reduction beyond the mechanical
    overhead, folded into the downtime_fraction of 0.15.

  interruption_notes: >-
    In a multi-user supervised setting, intraday interruptions are structurally higher
    than in single-operator production. Typical interruption profile: member skill-check
    pause (~5–10 min per member per session), equipment handoff between station rotations
    (~5 min per rotation), safety intervention or coaching (~10–20 min total/session
    depending on member mix), administrative (sign-in, waiver review, incident log)
    (~5 min/session). Total intraday interruption typically 30–50 min per operating session,
    folded into throughput_units_equiv_per_year computation in sim_params.

  consumables_lead_time_days: { typical: 7, worst: 45 }
  # Typical: standard consumables (flux, stock, grinding media) from regional supplier.
  # Worst: induction coil or specialty propane fittings from specialist supplier with
  # backorder; 45 days is the documented tail risk for non-standard coil geometries
  # (see smithing SCHEMA.md §4 reference list).

  throughput_variance:
    seasonal: "Moderate seasonality: higher autumn/winter demand for repair work; summer trough offset partially by school-program and K-12 partnership demand"
    worst_month_fraction_of_average: 0.55
    # Civic scheduling suppresses deep troughs relative to commercial shops: public
    # programs and K-12 partnerships maintain baseline demand in slow months.
    best_month_fraction_of_average: 1.50

  operator_impact:
    noise_db: 78
    # Mixed-fuel hybrid (induction primary, propane backup): induction forges are
    # substantially quieter than combustion forges. 70–85 dB range per entry parameters;
    # 78 dB mid-range estimate at operator position. Hammering noise dominates over
    # forge noise in this configuration.
    heat_exposure: "Moderate at induction forge station; elevated near propane backup (when in use); multi-workstation spacing reduces cumulative radiant heat exposure vs single-operator layout"
    emissions: "Low: induction primary produces near-zero on-site combustion emissions; propane backup adds CO and combustion products only during backup use; dedicated exhaust system required and present"
    physical_demand: "Variable by station and role: master smith-instructor has moderate physical demand (supervision and demonstration cycles); member operators vary from light (novice, small work) to moderate-heavy (experienced, medium work)"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Town-owned facility typically pre-permitted under municipal institutional zoning; confirm local ordinance re: hot-work in public buildings; no change-of-use permit usually required for existing town facility"
  emissions: "Induction-primary configuration avoids most combustion-emission permit triggers; propane backup subject to LP storage and combustion appliance permit; multi-user public-access adds OSHA 29 CFR 1910.252 hot-work requirements"
  other: "Public-access workshop carries substantial liability and insurance obligations; OSHA general industry standards apply (not just construction); town counsel review of member waiver and access policy required before opening"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: poor
  # Civic operation with zero commercial output pricing. The facility does not compete
  # on market terms, does not produce for sale, and has no revenue stream that would
  # support a market-lens evaluation. Market lens: poor.
  cooperative: good
  # Member-access model layered on civic ownership creates cooperative-analogous
  # governance. Ostrom principles 1–5 are addressed through documented bylaws,
  # sign-in monitoring, and graduated sanctions. The legal form is municipal (not a
  # registered cooperative), but the operating model functions cooperatively.
  civic: good
  # Primary lens. Town ownership, public-goods externalities, and political coalition
  # are fully documented in lens_context.civic below.

scale_fit:
  village: poor
  # Capital requirement ($125,000 mid) is disproportionate at village scale (500–2,000
  # residents); per-household cost would exceed political tolerance (~$60–125/hh/yr
  # vs the $125/hh benchmark at town scale). Insufficient scheduling demand to justify
  # a FT master smith-instructor. Village-scale civic forges are feasible only as
  # shared regional facilities (out of scope for this entry).
  town: good
  # Target scale: 2,000–15,000 residents. Sufficient population base to spread
  # per-household cost to ~$125/hh/yr range, generate enough shift demand to sustain
  # 30 hr/wk scheduling, and support the staffing model. Political coalition is
  # viable at town scale.
  small_city: good
  # Per-household cost falls further (favorable). Scheduling demand may support
  # extended hours. Multiple staff positions may become viable. Minor governance
  # adjustments needed for larger member base; core model transfers directly.

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:

  cooperative:
    membership_boundary: >-
      Town residents and immediate township equivalents; access granted via library-card
      equivalent credential (town residency verification). Non-residents may join at a
      higher annual fee tier ($100–150/yr vs $50–100/yr resident rate) subject to
      capacity. No demographic restriction; open to all ages with minor waiver adjustments
      (under-18 requires parental consent and additional supervision ratio).

    rules_source: >-
      Posted workshop bylaws adopted by the facility committee (a standing subcommittee
      of the town library board or parks-and-rec department). Bylaws govern: station
      booking, skill-tier certification, PPE requirements, prohibited materials,
      visitor policy, and access suspension procedures. Rules displayed in the facility
      and published on the town website.

    monitoring: >-
      Mandatory sign-in log for every session (member ID, date, station, hours);
      supervisor observation during all operating hours (master smith-instructor present
      at all times by policy); monthly facility-committee review of usage logs;
      incident log maintained separately and reviewed quarterly by the facility committee
      and town counsel.

    graduated_sanctions: >-
      Warning (verbal, logged) → written notice + 30-day suspended booking privileges →
      revoked access pending facility-committee review → permanent access revocation
      with opportunity for appeal to town board. Safety violations (PPE non-compliance,
      unauthorized modifications) may skip directly to revocation at supervisor discretion.

    conflict_resolution: >-
      Day-to-day disputes resolved by master smith-instructor as floor authority.
      Member-vs-member disputes and appeals of supervisor decisions escalated to
      facility committee (3–5 members drawn from library board or parks-and-rec);
      facility-committee decisions are final subject to town board appeal. Conflict
      resolution meeting required within 14 days of formal complaint.

    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6]
    # Principle 1 (clear boundaries): residency-based membership with documented
    #   eligibility. Principle 2 (congruence): rules calibrated to civic-facility
    #   context (supervised use, not autonomous member-managed commons).
    # Principle 3 (collective choice): bylaw amendment process below allows member input.
    # Principle 4 (monitoring): sign-in logs + supervisor observation.
    # Principle 5 (graduated sanctions): documented above.
    # Principle 6 (conflict resolution): facility-committee mechanism above.
    # Principles 7–8 (nested/external recognition): municipal ownership provides
    #   external recognition (Principle 8); nesting into town governance satisfies
    #   Principle 7 at the institutional level. Not addressed via member self-governance
    #   but via civic umbrella — acceptable for a municipally-owned commons.

    member_amendment_process: >-
      2/3 vote of active members at annual facility-review meeting (held concurrently
      with town library board annual meeting); 30-day advance notice required for
      bylaw amendments. Emergency safety-related rule changes may be enacted by
      facility committee with 7-day notice and ratified at next member meeting.
      Town board retains override authority on budget-related rules.

    legal_form: >-
      Municipal operation under town government authority (not a registered cooperative
      entity). The member-user model is layered on civic ownership: the town holds title
      and operational authority; the facility committee provides member governance.
      Ostrom Principle 7 analog is satisfied by municipal recognition and budget-line
      accountability rather than by cooperative registration.

    scale_fit_note: >-
      Governance rules calibrated for town scale (2,000–15,000 residents). Minimum
      viable population approximately 2,000 to generate sufficient scheduling demand
      (≥15 active member-users needed to fill 30 hr/wk shift slots across 4 stations).
      At village scale, quorum for annual member meeting and scheduling demand both
      become problematic. At small-city scale, rules transfer directly; staff complement
      may expand.

  civic:
    political_coalition: >-
      Library board (operational home; aligns with library-model access philosophy);
      workforce-development board (training pipeline for skilled trades; grant-funding
      alignment); small-business alliance (complementary to private smiths; repair
      referral network); trade-union allies (IBEW for electrical work; UA for propane/gas;
      potential endorsement from regional blacksmithing guild as training-quality signal).
      Secondary coalition partners: K-12 school district (curriculum partnership
      potential); emergency-management office (resilience argument for civic infrastructure).

    council_vote_estimate: >-
      6-1 favorable in pro-library, workforce-development-minded town councils;
      4-3 marginal in conservative budget climates where the capital ask (~$125,000 +
      $15,000 installation) triggers fiscal-responsibility opposition. Primary opposition
      argument: "government competing with private enterprise" — addressed in
      competes_with_private below. Secondary opposition: insurance and liability exposure.
      Swing vote typically held by a fiscal-moderate council member; benchmark_comparison
      data ($125/hh/yr, within library-expenditure range) is the most effective counter-argument.

    competes_with_private: >-
      The civic makerspace forge is structurally complementary to, not competitive
      with, private smiths. The facility does not sell output commercially, does not
      accept production contracts, and explicitly refers commercial work to private
      operators. Its apprenticeship pipeline actively supplies journeyman labor to
      the surrounding private-smith market. In towns where no private smith operates,
      the civic forge fills an access gap the market has declined to fill (consistent
      with the library model: public libraries do not displace bookstores competing
      on the same titles). In towns where a private smith does operate, the civic
      facility trains the private smith's future employees and handles low-value repair
      work the private operator has no incentive to take.

    governance_form: >-
      Town-owned; operated under town parks-and-recreation department or library system
      (whichever has existing facility-management capacity). Master smith-instructor is
      a town employee or long-term contractor. Facility committee (3–5 members, appointed
      by library board or parks-and-rec director) sets operating policy within
      town-approved bylaws. Annual budget line reviewed by town council.

    budget_line: >-
      Capital: one-time appropriation or 20–25 year general-obligation bond (~$4,700–6,250/yr
      amortized at mid-capital + install cost of $140,000 over 25 yr). Operating:
      ~$35,000/yr covering staffing ($58,000 FT master + $20,000 PT journeyman assistant =
      $78,000 total labor, offset by ~$50,000 in grants and member fees leaving ~$28,000 net)
      plus maintenance ($5,500), consumables ($4,200), and administration (~$3,000);
      gross operating ~$47,700/yr. Member fee revenue (~$5,000–10,000/yr at 100–200 active
      members) and workforce-development grants (~$10,000–20,000/yr) reduce net municipal
      cost. Budget line: workforce-development or parks-and-rec capital and operating accounts.
      [CITATION-NEEDED: grant availability and typical award amounts for civic makerspace
      workforce programs.]

    benchmark_comparison: >-
      At town scale (5,000 households as representative mid-point), gross operating cost
      of ~$47,700/yr ÷ 5,000 hh = ~$9.54/hh/yr; net municipal cost after member fees and
      grants (~$30,000–35,000/yr) ≈ $6–7/hh/yr. Amortized capital adds ~$1.25–1.56/hh/yr
      (25-yr bond). All-in municipal cost: ~$7–9/hh/yr.
      Benchmark: SCALES.md §3 notes town library operating cost typically $35–65/hh/yr;
      town recreation center $45–80/hh/yr [CITATION-NEEDED: SCALES.md library/rec-center
      benchmark data]. The civic forge at $7–9/hh/yr is well within the established range
      for civic cultural and skills infrastructure — approximately one-fifth of library cost.

    staffing_model:
      role: "1 FT master smith-instructor (town employee or contractor) + 1 PT journeyman assistant (20 hr/wk)"
      operator_fte: 1.5
      # 1.0 FT master + 0.5 FTE journeyman assistant (20 hr/wk)
      wage_assumption: 58000
      # Master smith-instructor: $58,000/yr. Journeyman assistant: $20/hr × 20 hr/wk × 50 wk
      # = $20,000/yr. Total annual labor: $78,000. wage_assumption reflects master position
      # as primary cost driver.
      wage_source: "corpus/program/SCALES.md §3 town-scale skilled-trades median"
      hours: "40 hr/wk (master: production supervision + instruction + admin); 20 hr/wk (journeyman assistant: shift coverage + maintenance support)"
      hiring_notes: >-
        Master smith-instructor requires journeyman-to-master competency and demonstrable
        teaching ability; hiring pool is regional (100–150 mile radius). Competition from
        private shops and vocational schools creates salary pressure; $58,000 is at the
        lower bound of what a qualified master smith-instructor will accept in most US
        regions [CITATION-NEEDED: regional skilled-trades wage survey]. Apprentice pipeline
        from the facility itself is the long-run succession source, but requires ~5–8 years
        of operation to produce a qualified internal candidate. Part-time journeyman assistant
        hire pool is broader; local workforce-development program graduates are a viable source.

    civic_externalities:
      - "Apprentice training pipeline: structured 36-month program produces 1–3 journeyman smiths per cycle, directly supplying regional private smiths, farriers, and metal-trade employers who cannot afford to run their own apprenticeship programs"
      - "Emergency and resilience production capacity: a functioning forge can fabricate or repair critical metal components (hinges, brackets, fasteners, agricultural tools) during supply-chain disruptions — a documented resilience argument for post-disaster and infrastructure-stress scenarios"
      - "Repair culture externality: accessible civic repair service extends the useful life of metal goods (tools, hardware, structural fasteners) that would otherwise be discarded, reducing waste and supporting a local circular-economy norm the market systematically under-provides"
      - "K-12 and workforce-development pipeline: co-curricular metalworking exposure at the civic forge reduces the soft-skills and safety-culture gap that vocational programs and employers consistently cite as a hiring barrier; produces students with workshop-readiness that has downstream labor-market value"
      - "Private-operator complement: the facility trains the future employees of private smiths, farriers, and metal-trade shops in the surrounding region, functioning as a workforce subsidy to those private operators who would otherwise bear full apprentice-training costs"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 125000
  # Equals economics.capital_cost.mid per E3-R1.

  cost_sd: 25000
  # (high - low) / 4 = (180,000 - 80,000) / 4 = 25,000. Consistent with E3-R5
  # ratio: 25,000 / 125,000 = 0.20 (within 0.15–0.50 acceptable range).

  throughput_units_equiv_per_year: 960
  # Derivation (stated per smithing SCHEMA.md §1 E-3 guidance):
  # Derated active hours: 30 hr/wk gross − (45 min/day × 5 days / 60) = 26.25 hr/wk net.
  # Downtime fraction: 0.15 (multi-user overhead, scheduling gaps, maintenance).
  # Effective hours/yr: 26.25 × 52 × (1 − 0.15) = 26.25 × 52 × 0.85 ≈ 1,160 hr/yr.
  # Product mix weighting (productive share only, 60% of hours):
  #   Productive hours: 1,160 × 0.60 = 696 hr/yr (repair 30%, commodity 5%, specialty 25%).
  #   Remaining 40% (464 hr/yr) = training-output hours; produce ~0 market-equivalent units.
  # Weighted unit rate over productive hours:
  #   Within productive mix (normalized): repair 50%, commodity 8.3%, specialty 41.7%.
  #   small_work: 2/hr; medium_work: 0.5/hr; large_work: 0.1/hr.
  #   Approx blended rate: 0.50×2 + 0.083×2 + 0.417×0.5 = 1.00 + 0.17 + 0.21 ≈ 1.38 units/hr.
  # Annual productive output: 696 hr × 1.38 units/hr ≈ 960 units/yr.
  # Note: "unit" = small-work equivalent. Training-output hours are not zeroed in
  # throughput but are reflected in the lower productive-share fraction above.

  variable_cost_per_unit: 5.9
  # Consumables ($4,200/yr) + energy cost (induction: ~8 kWh/hr × $0.12/kWh ×
  # 1,160 hr/yr ≈ $1,114; propane backup minimal at ~5% of hours: 1.5 kg/hr ×
  # $1.50/kg × 58 hr ≈ $131) = total variable ~$5,445/yr ÷ 960 units ≈ $5.67/unit.
  # Rounded to $5.9 to include minor per-unit consumable variation.
  # [CITATION-NEEDED: electricity rate $0.12/kWh; propane rate $1.50/kg — regional
  # utility estimates per SCALES.md §4 energy cost ranges.]

  labor_hours_per_unit: 1.21
  # Effective hours/yr (1,160) ÷ throughput_units_equiv_per_year (960) ≈ 1.21.
  # This reflects total supervised labor hours per output-equivalent unit including
  # training overhead — consistent with E3-R3.

  downtime_fraction: 0.15
  # Sources: multi-user scheduling gaps (~5%), equipment maintenance and first-year
  # failure events (~5%), civic administrative overhead (public holidays, staff
  # absence, facility inspections) (~5%). Total 15%. Consistent with operations_reality
  # first_year_failures profile (induction coil 21-day lead time is the dominant
  # tail risk; at 1,800 hrs to failure and 30 hr/wk schedule, first failure occurs
  # ~year 1.15 — within first operating year range; contributes ~4–5% downtime).

  lifespan_years: 25
  # Standard civic infrastructure amortization horizon. Induction forge equipment
  # manufacturer warranties typically 5–10 years; civic maintenance standard extends
  # effective life with periodic coil replacement. 25-year horizon aligns with
  # municipal general-obligation bond term.

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
  - ref: "corpus/program/SCALES.md §3 — town-scale skilled-trades median wage and civic facility per-household cost benchmarks"
  - ref: "OSHA 29 CFR 1910.252(c) — hot-work and forge safety standards for public-access facilities"
  - ref: "Ostrom, Elinor. 1990. Governing the Commons. Cambridge University Press — design principles for commons governance"
  - ref: "[CITATION-NEEDED: civic makerspace forge-module capital cost — no published benchmark at authoring date; estimate from industrial equipment pricing plus civic overhead multiplier]"
  - ref: "[CITATION-NEEDED: 3-phase electrical + dedicated exhaust installation cost — regional contractor estimate ranges per SCALES.md §4]"
  - ref: "[CITATION-NEEDED: induction forge energy consumption rates — manufacturer spec for mid-grade induction forge unit]"
  - ref: "[CITATION-NEEDED: propane forge consumption (backup mode) — modern experimental measurement; see smithing SCHEMA.md §2]"
  - ref: "[CITATION-NEEDED: regional skilled-trades master-smith wage survey — confirm $58,000/yr town-scale estimate]"
  - ref: "[CITATION-NEEDED: town library per-household annual operating cost benchmark — $35-65/hh/yr range cited from SCALES.md pending confirmation]"
  - ref: "[CITATION-NEEDED: workforce-development grant availability and typical award amounts for civic makerspace programs]"
  - ref: "[CITATION-NEEDED: industrial hardware baseline price for small forged-equivalent items — hardware-store commodity pricing survey]"
  - ref: "Jacobs, Jane. 1961. The Death and Life of Great American Cities. Random House — civic infrastructure as neighborhood resilience anchor; public-goods framing for non-commercial community services"
  - ref: "[CITATION-NEEDED: Japanese shokunin apprenticeship tradition — functional training structure, state licensing history; primary academic source needed for historical lineage claims]"
---

## Summary

The Community Civic Makerspace Forge Module (forge-004) is a town-owned supervised multi-user forge designed on the library-model of public access: residents book shifts, work under qualified supervision, and pay a modest annual access fee rather than per-session commercial rates. This entry covers the forge portion of a broader multi-craft makerspace; the overall facility would also house woodworking, textile, and other bays (out of scope here). The forge operates on an induction-electric primary system with propane backup, supports up to four simultaneous member-users under a master smith-instructor, and embeds a structured 36-month apprenticeship program as its core operating mode. It exists as a distinct catalog entry because no existing entry models the civic-public-goods case for a forge: the subsidy logic, staffing economics, political coalition, and Ostrom governance layer are not variants of a private or cooperative forge design — they require a purpose-built analysis.

## Design rationale

The problem this entry solves is the access gap that neither the market nor small cooperatives reliably fill in towns of 2,000–15,000 residents: the market will not place a commercially viable forge where throughput is insufficient to cover rent and a master smith's wage; small cooperatives struggle with governance fragility, liability exposure, and the capital hurdle for a training-grade facility. The civic model resolves all three constraints simultaneously: zero rent (town ownership), institutional governance (municipal authority backstops bylaw enforcement), and public-goods justification (apprentice pipeline, repair culture, emergency resilience) that justifies the subsidy independently of commercial viability. The induction-electric primary choice is deliberately civic rather than commercially optimal: it produces a cleaner, quieter, more accessible environment for novice users and reduces the regulatory friction of operating a combustion forge in a public building. The propane backup is retained not for primary production economics but for capability completeness — forge welding and high-temperature work that a fully equipped civic forge should be able to offer for advanced apprentice training. This hybrid configuration is not cost-optimal for a commercial operator; it is policy-optimal for a public-access facility.

## Historical lineage

Two traditions inform this design, and both require anti-romantic treatment.

**Japanese shokunin training tradition (adapted, without estate rigidity).** The shokunin model — a master craftsperson who trains students through structured, supervised production within a single facility — provides the functional blueprint for the apprentice_path structure and the operator-to-member ratio. The inheritance is real: the multi-stage competency gate system (orientation → supervised small work → medium work → graduated autonomy) maps directly to how Japanese metalworking apprenticeships structured skill transmission across centuries. What the design explicitly rejects is the economic and social structure that made the original viable: Japanese shokunin smithing was state-licensed under the Edo period's strict guild-like regulation (za system), operated within hereditary workshop lineages, and relied on a captive apprentice labor supply that was not voluntary in any modern sense. The civic makerspace reverses all three: access is voluntary, membership is open, and the town (not a craft family) holds institutional continuity. The training sequence is the inheritance; the power structure is not. [CITATION-NEEDED: academic source on Japanese shokunin metalworking apprenticeship structure and Edo-period licensing; see sources block.]

**US public library and recreation-center model (Jane Jacobs civic-infrastructure framing).** The library-card access model, the zero-rent civic ownership, and the benchmark comparison against library per-household costs are all inherited from the US public library tradition. Jane Jacobs's argument in *The Death and Life of Great American Cities* (1961) — that civic infrastructure generates neighborhood resilience and social capital that the market systematically under-provides — supplies the theoretical frame for the civic_externalities block. The functional inheritance is the pricing model (access fee, not unit price), the governance form (municipal ownership + member-facing facility committee), and the public-goods justification structure. What this design does not inherit from the library model is any assumption that the facility can be unstaffed or self-service: a forge is not a book, and the liability and safety profile requires qualified supervision at all times. The analogy is to the library as institution, not the library as unstaffed resource room.

## Key assumptions

**Capital cost ($80,000–$180,000 mid $125,000):** No published benchmark for a civic forge-module within a multi-craft makerspace was identified at authoring date. The estimate is derived from industrial induction-forge equipment pricing (mid-grade unit: approximately $40,000–60,000), propane backup station ($5,000–10,000), tooling suite for four stations ($10,000–20,000), ventilation system ($10,000–20,000), and a civic-overhead multiplier for permitting, accessibility compliance, and institutional procurement. The range is wide (low–high spread of $100,000) because the design choices within this envelope vary substantially. This is a rough estimate flagged with [CITATION-NEEDED] throughout; it should be replaced with actual procurement data before promotion to `reviewed` status.

**Staffing ($58,000 master + $20,000 PT journeyman):** Derived from corpus/program/SCALES.md §3 town-scale skilled-trades median wage. The $58,000 figure is at the lower bound of what a qualified master smith-instructor will accept; the assumption is contested. See hiring_notes in staffing_model for the regional-market caveat.

**Throughput rates (small_work: 2/hr, medium_work: 0.5/hr, large_work: 0.1/hr):** These are intentionally below the single-operator journeyman ceiling rates in smithing SCHEMA.md §1 (ceiling 4–8/hr small, 2–4/hr medium). The depression reflects the multi-user supervised model: station-rotation overhead, skill-variation drag, and the 40% training-hour share. The rates are a rough authorial estimate; experimental measurement at comparable civic facilities would be needed for validation.

**sim_params.throughput_units_equiv_per_year (960):** Fully derived in the frontmatter derivation note; the calculation is internally consistent with derated active hours, downtime fraction, and the product-mix weighting. The unit is small-work equivalent; the weighting is stated explicitly per smithing SCHEMA.md §1 E-3 guidance.

**Downtime fraction (0.15):** Conservatively estimated for the multi-user civic context. The induction coil failure at ~1,800 hours (year 1 under 30 hr/wk schedule) is the dominant downtime driver. 21-day lead time for specialist replacement during first-year operation contributes approximately 4–5% downtime; scheduling and administrative gaps contribute the remainder.

**Per-household cost (~$7–9/hh/yr net):** The benchmark_comparison calculation uses 5,000 households as a representative mid-town figure. The net figure is sensitive to grant-funding assumptions ([CITATION-NEEDED]); without grants, gross cost rises to ~$9.54/hh/yr before amortization — still well within library-benchmark range. The calculation is transparent in the civic block and should be updated with actual town demographic data at implementation.

## Known risks and failure modes

**Regulatory risks:** The most significant regulatory risk is the intersection of public-access, hot-work, and OSHA general-industry standards (29 CFR 1910.252). A town that classifies the forge module as a "public building" may face stricter fire-suppression requirements than a private workshop; local fire marshal approval is required and may impose significant retrofit costs. The propane backup adds LP storage and combustion-appliance permit requirements that vary widely by jurisdiction. Liability and insurance: a public-access forge with community members (including minors under parental consent) creates an insurance exposure that may exceed parks-and-rec standard coverage; town counsel review and specialist insurance rider are required before opening.

**Labour pipeline risks:** The master smith-instructor position is the single point of failure for the entire facility. If the position is vacant for more than a few weeks, the facility cannot operate (supervision requirement is absolute). At $58,000/yr, the wage may not attract or retain a qualified master smith in regions where private shops pay market rates; the risk of under-hiring (journeyman misrepresented as master) is non-trivial. The apprentice pipeline mitigates this over a 5–8 year horizon but provides no short-term succession protection. The entry's civic externality argument depends on the apprentice pipeline actually producing journeyman graduates; if the facility runs with low member engagement, the pipeline thins and the public-goods case weakens.

**Supply chain risks:** The induction coil is the critical single-supplier dependency. Non-standard coil geometries for mid-grade civic-use induction forges may have a single manufacturer or a limited distributor network; the 21-day lead time estimate is optimistic for bespoke or uncommon coil geometries. The worst-case consumables lead time of 45 days (see operations_reality) is the primary supply-chain tail risk; the facility should maintain a safety stock of propane regulator spares and ventilation filters to avoid extended downtime on parts that are cheap but slow to arrive.

## Target niche and competitive positioning

The civic argument for forge-004 rests on three claims that must be made explicitly rather than assumed.

**Why public investment is warranted.** The market systematically declines to place a commercially viable forge in towns of 2,000–15,000 residents: throughput is insufficient to cover rent and a master smith's wage at market pricing, and the apprentice-training function generates benefits (journeyman labor supply, repair culture, emergency resilience) that accrue to the community but cannot be captured by the private operator. This is a classic public-goods argument: the externalities of a well-run civic forge — the apprentice pipeline, the repair culture, the resilience capacity — are non-excludable and non-rival in ways that a private operator cannot monetize. The civic model prices access at the library level ($7–9/hh/yr net municipal cost) rather than at market rates, making the service accessible to residents who could not afford commercial smithing services.

**Why the facility complements, not competes with, private operators.** The forge-004 design is explicitly non-commercial: it does not accept production contracts, does not sell output, and does not compete for the repair or custom-fabrication market that a private smith serves. It is a training facility that happens to produce useful work as a byproduct of training. In towns where a private smith operates, the civic forge trains that smith's future employees and handles the low-value, high-volume repair work (re-hanging a gate, replacing a hook) that the private operator declines because the margin is insufficient. In towns where no private smith operates (the more common case at town scale), the civic forge is the only metalworking resource available; there is no displacement to assess. The "competes with private enterprise" council-opposition argument fails on the facts: a library does not displace a bookstore because libraries are not selling books, and a civic forge does not displace a private smith because civic forges are not accepting production contracts.

**Why the Jacobs framing matters.** Jane Jacobs's argument that civic infrastructure generates neighborhood resilience that the market under-provides is not decorative here — it is the functional justification for the subsidy. The K-12 partnership potential, the emergency production capacity, and the repair-culture externality are all Jacobs-class public goods: they are real, they are valuable, and they are not priced into any private operator's business model. The civic makerspace forge is the institutional form that captures those externalities while remaining politically viable at the per-household cost level that towns have already demonstrated willingness to support for libraries and recreation centers.

## Iteration log

- 2026-04-18: v0.1 — initial creation; forge-004 Community Civic Makerspace. CIVIC-PRIMARY entry per Plan C Task 6 specification. All three lens_context blocks populated (market poor with industrial_baseline cited for reference; cooperative good with Ostrom 1–6; civic good as primary lens with staffing_model, benchmark_comparison, five civic_externalities, and apprentice_path). Thirteen [CITATION-NEEDED] flags placed over fabrication on capital cost, install cost, wages, energy rates, and historical lineage sources. Anti-romanticism applied to both Japanese shokunin and library-model precedents.
