---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: forge-002
trade: smithing
name: "Induction-Modular Small Repair (compact electric forge)"
tagline: "Single-operator induction forge targeting tool and implement repair in town and small-city settings"
status: draft
version: "0.1"
supersedes: null
inspirations:
  - american-frontier-repair-dominant-smith
  - song-china-coal-transition-supply-economics

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 27
# Mid-range of the 20-35 m² envelope; adequate for one operator, staging, and
# quench trough. Per REQUIREMENTS R-10, 15-40 m² is the historical small-scale
# range; 27 m² represents a full-function single-operator bay.
# [CITATION-NEEDED: archaeological or commercial survey of single-operator
# induction-forge shop floor areas; structural inference from REQUIREMENTS R-10
# and American frontier chapter §9 (Wallace 1978 Rockdale one-bay smithy ~15-30 m²)]

ceiling_min_m: 2.8
# Adequate for induction unit, overhead cable management, and operator clearance.
# REQUIREMENTS R-11 minimum 2.5 m; 2.8 m gives modest headroom for a compact
# industrial space. [Derived from REQUIREMENTS R-11; no combustion clearance
# requirement elevates this above structural minimum.]

ventilation: mechanical-extraction-required
# Induction does not produce combustion gases. Mechanical extraction is required
# for metal-scale particulate from grinding and finishing operations typically
# co-located with a repair forge. OSHA 29 CFR 1910.252(c) hot-work ventilation
# standards apply to grinding and cutting operations co-located with forging.
# [OSHA 29 CFR 1910.252(c)]

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: induction-electric
energy_consumption_per_active_hour: "12 kWh"
# Per smithing SCHEMA.md §2 induction-electric range of 6-15 kWh/hr depending
# on unit rating. 12 kWh/hr represents a mid-range commercial induction forge
# unit (~10-15 kW rated power) under sustained operational load.
# [CITATION-NEEDED: manufacturer energy-consumption data for commercial induction
# forge units in the 10-15 kW range; illustrative estimate within SCHEMA.md §2
# range; not directly sourced from industry measurement]

backup_fuel: null
# No backup fuel in the base configuration. Induction is the sole heat source.
# An operator may supplement with a small propane torch for localized heating
# tasks, but this is operator-supplied and not part of the installed design.

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  units_per_hour:
    small_work: 5
    # Repair of small implements, hooks, brackets, horseshoe nails, shim stock.
    # Induction precise temperature control moderately increases repeatability
    # vs. coal but does not increase raw throughput above the journeyman ceiling
    # of ~4-8 units/hr defined in smithing SCHEMA.md §1. [Structural inference
    # from REQUIREMENTS R-06 and smithing SCHEMA.md §1 journeyman ceiling;
    # CITATION-NEEDED: experimental throughput measurement for induction-forge
    # repair operations.]
    medium_work: 1
    # Horseshoe fitting, tool repair (chisels, drawknives, hoe blades), bracket
    # fabrication. 1.5 units/hr is within the smithing SCHEMA.md §1 ceiling of
    # 2-4 units/hr for medium work; 1.5 reflects the repair-dominant mix where
    # each piece requires diagnosis and fitting rather than repetitive production.
    # [Same structural inference as small_work; CITATION-NEEDED.]
    large_work: 0.4
    # Larger repair items: gate hardware, structural brackets, plow shanks.
    # 0.4 units/hr is within the smithing SCHEMA.md §1 ceiling of 0.3-1 units/hr.
    # Large work is a minor fraction of the repair-dominant mix. [Same.]
  max_active_hours_per_week: 35
  # Realistic ceiling for a full-time single operator including customer
  # interaction, setup, and non-production overhead but after startup/shutdown
  # deduction. Per REQUIREMENTS R-06, 4-8 active forging hours/day is the
  # historical baseline; 35 hr/wk ≈ 7 hr/day × 5 days, which is within the
  # upper range for a motivated modern operator with induction's faster startup.
  # See operations_reality.max_active_hours_realism_note for derating detail.
  product_mix:
    repair: 60
    commodity: 10
    specialty: 20
    artistic: 10
    # Sum: 100. Repair-dominant as required for Group A (smithing SCHEMA.md §5).
    # Specialty (20%) includes custom fittings and bespoke agricultural hardware.
    # Artistic (10%) reflects occasional decorative commissions that smooth
    # seasonal demand troughs. Commodity (10%) covers standard replacement
    # hardware items to fill slack capacity. Per REQUIREMENTS R-22 and DECLINE-
    # VERDICT guidance; product-mix scope stated per R-22.
  throughput_variance:
    seasonal: "Pre-planting (March-April) and post-harvest (Oct-Nov) peaks for agricultural implement repair; summer and January troughs; induction-electric indoor setting moderates variance somewhat vs. outdoor coal forges"
    worst_month_fraction_of_average: 0.50
    # Repair-dominant shops show 0.40-0.60 range per smithing SCHEMA.md §1;
    # 0.50 reflects moderate variance given the urban/suburban setting partially
    # decouples from agricultural seasonality. [Structural inference from
    # REQUIREMENTS R-07 seasonal pattern; CITATION-NEEDED: empirical worst-month
    # fraction for modern repair-dominant induction forge operations.]
    best_month_fraction_of_average: 1.60
    # Consistent with repair-dominant smithing SCHEMA.md §1 range of 1.40-1.80.
    # [Same inference as worst_month_fraction_of_average.]

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: journeyman
# Repair work requires formed heat judgment per REQUIREMENTS R-17: "routine
# repair (horseshoe fitting, simple bends, basic tool sharpening): journeyman
# minimum — requires formed judgment, not just procedure." Induction's precise
# temperature readout reduces the cognitive load of heat-color reading, but
# does not eliminate the need for metallurgical judgment in diagnosis and fitting.
# [REQUIREMENTS R-17]

operators_concurrent: "1-2"
# Base operation: single journeyman operator. Second operator (apprentice or
# skilled helper) is beneficial during peak periods and for apprentice-path
# integration. Motorized induction air eliminates bellows-assistant requirement
# per REQUIREMENTS R-18. [REQUIREMENTS R-18]

apprentice_friendly: true
apprentice_path:
  training_stages: >
    Stage 1 (0-3 months): equipment safety, induction-unit operation,
    temperature reading from digital display and visual cue cross-check,
    basic stock prep, and cleaning protocols. Gate criterion: can safely
    start, operate, and shut down the induction unit unassisted; can prepare
    stock to specification.
    Stage 2 (3-12 months): small-work repair operations under journeyman
    supervision — hooks, brackets, simple tool sharpening and re-tempering.
    Develops heat-judgment via induction's direct temperature feedback before
    transitioning to visual-only judgment. Gate criterion: completes 20
    small-work repair items to journeyman-accepted quality standard without
    supervision on the final five.
    Stage 3 (12-30 months): medium-work repair and specialty output; customer
    interaction; diagnosis of unfamiliar repair requests. Gate criterion:
    operates the shop independently for a full day with journeyman review of
    all output at end of day.
    Stage 4 (30-48 months): full independent operation including heat treatment
    (quench and temper); quality responsibility for own work; capable of
    supervising a Stage 1-2 apprentice. Approximate journeyman standard on
    this equipment.
  time_to_independent_operation: "~36-48 months to journeyman standard on this equipment; induction's digital temperature feedback compresses Stage 1-2 vs. coal or propane but does not eliminate the judgment-formation time required at Stage 3-4"
  succession_note: >
    Apprentice co-presence during production is built into the 1-2 concurrent
    operator model; Stage 2-3 apprentices participate in customer repair work
    under journeyman oversight, integrating skill transfer into normal revenue-
    generating operations rather than a separate training program. This follows
    the American frontier informal-apprenticeship pattern (shorter and variable
    duration) rather than the European guild indenture model (3-7 years formal
    indenture). Per REQUIREMENTS R-19, the cultural apprenticeship model is
    stated: informal co-production model, duration 36-48 months.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD
  capital_cost: { low: 25000, mid: 42000, high: 60000 }
  # Low: minimal induction unit (~$8,000-$12,000), basic anvil and tooling,
  # secondhand or fabricated stands, minimal HVAC upgrade.
  # Mid: mid-range commercial induction forge (~$18,000-$25,000), full tooling
  # set, adequate ventilation, basic surface grinder for repair finishing.
  # High: premium induction system with integrated temperature control and
  # coil inventory, full tooling suite, grinder/polisher, shop fit-out.
  # [CITATION-NEEDED: capital cost data for commercial induction forge systems
  # in the 10-20 kW range; illustrative estimate based on market observation of
  # induction forge pricing circa 2024-2026; not sourced from formal industry
  # survey. Label: pricing_validation: inferred.]

  install_cost: 8000
  # Electrical service upgrade often required: 100A single-phase minimum,
  # 3-phase preferred for larger units. Upgrade from standard residential service
  # ($4,000-$8,000 depending on distance to utility transformer) plus mechanical
  # ventilation installation. Mid-point estimate.
  # [CITATION-NEEDED: electrical service upgrade costs for commercial induction
  # equipment; illustrative estimate from general electrical contractor cost
  # ranges; not sourced from specific job data. Label: inferred.]

  annual_maintenance: 1800
  # Induction coil inspection and cleaning, coolant system maintenance, safety
  # interlock testing, ventilation blower service. Excludes first-year failure
  # replacements itemized in operations_reality. Lower than coal forge (~$2,500-
  # $4,000/yr for refractory and coal-related maintenance) due to absence of
  # consumable refractory and ash management.
  # [CITATION-NEEDED: annual maintenance cost data for commercial induction forge
  # operations; illustrative estimate; label: inferred.]

  annual_consumables: 2400
  # Bar stock (steel) assumed externally procured and charged to customer job cost
  # rather than carried as shop consumable inventory. This figure covers: flux
  # and cleaning compounds ($200), grinding and cutting wheels ($600), fire bricks
  # and insulation for quench area ($200), safety consumables ($200), minor
  # tooling replacement ($400), and electricity overage beyond base operational
  # budget (~$800 at 12 kWh/hr × 35 hr/wk × 50 active wk × $0.125/kWh =
  # $2,625/yr actual electricity cost — carried separately in variable_cost_per_unit
  # for sim_params purposes; consumables figure here excludes electricity).
  # Note: electricity = 12 kWh/hr × 35 hr/wk × 50 wk × $0.125/kWh = $2,625/yr
  # is the primary variable energy cost; annual_consumables captures non-energy
  # consumables only. [CITATION-NEEDED: consumable cost breakdown for induction
  # forge repair operations; illustrative estimate; label: inferred.
  # Electricity price: US EIA Electric Power Monthly, Table 5.3, 2023-2024
  # blended small-commercial rate $0.10-$0.15/kWh; mid-point $0.125/kWh used.]

  floor_space_rent_per_year: 3600
  # Imputed at ~$130/m² per year for light-industrial or mixed-use commercial
  # space in a town or small-city setting; 27 m² × $133/m²/yr ≈ $3,600.
  # Light-industrial rents vary substantially by region; this is a mid-range
  # illustrative estimate for a non-metro or secondary market. Owner-operator
  # scenarios should impute this cost for consistent cross-entry comparison per
  # catalog/SCHEMA.md §6 semantics.
  # [CITATION-NEEDED: light-industrial commercial rent per m² in town and small-
  # city US markets; illustrative estimate; label: inferred. CoStar/LoopNet
  # commercial real-estate data would be the appropriate verification source.]

  market_price_per_unit: { low: 40, mid: 55, high: 90 }
  # Per small-work equivalent unit. Reflects the repair-service market where
  # customers pay for labor applied to their own material. Low: commodity repair
  # pricing floor (~$40 for a simple hook repair, weld, or sharpening). Mid:
  # standard repair job including diagnosis and fitting ($55). High: specialty
  # or precision repair requiring heat treatment and quality verification ($90).
  # Pricing validation: inferred. See pricing_validation field below.
  # [CITATION-NEEDED: empirical repair-market pricing data for small-metalwork
  # repair services in US town and small-city markets circa 2024-2026;
  # illustrative estimate from market observation; label: pricing_validation: inferred.]

  pricing_notes: >
    Unit is a small-work equivalent repair item. Premium over industrial baseline
    ($10/unit for commodity hardware at hardware-store/industrial-supplier pricing)
    reflects the labor-of-repair model: customers pay for skilled diagnosis,
    access to the forge, and workmanship on their own implement, not for a
    factory-produced commodity substitute. The repair customer base is inelastic
    on attachment (customers prefer to repair a known tool rather than replace it)
    and price-tolerant relative to the industrial-hardware alternative, which
    often does not address the specific repair need. The $40-$90 range targets the
    direct-to-consumer and small-business market segment, not industrial bulk
    purchasers. Industrial baseline of $10 reflects commodity hardware-store
    pricing for equivalent new small fasteners/fittings [CITATION-NEEDED:
    commodity hardware pricing survey, hardware-store or wholesale, US 2024].

  pricing_validation: >
    Pricing evidence: inferred from market observation of small-metalwork repair
    pricing at craft fairs, maker-community forums, and informal operator surveys
    circa 2024-2026. NOT directly sourced from a formal industry pricing survey
    or published rate-card study. This is a placeholder-inferred figure.
    Recommended verification: direct survey of operating repair smiths or a
    trade-organization rate-card publication. This field carries a citation-needed
    flag per the project citation policy.

  industrial_baseline_price: 10
  # Commodity hardware pricing for small metal fittings at industrial/hardware-
  # store distribution: nails, hooks, brackets, standard fasteners in the
  # small-work category. The $10 figure represents the median unit price for
  # equivalent new hardware at US hardware-store or wholesale pricing.
  # [CITATION-NEEDED: commodity hardware pricing per unit at US hardware retail
  # or wholesale, 2024; e.g., Grainger or Fastenal catalog pricing for equivalent
  # small metal hardware items; illustrative estimate; label: inferred.]

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Primary induction coil"
      estimated_hours_to_failure: 1800
      replacement_cost: 1400
      replacement_lead_time_days: 21
      serviceable_by: specialist
      # Induction coil failure is the primary downtime event for induction forges.
      # Per smithing SCHEMA.md §4 reference list: coil failure 1,500-2,500 hrs;
      # replacement specialist-level; lead time 14-30 days for non-stocked coils.
      # [CITATION-NEEDED: induction coil mean-time-to-failure data for commercial
      # forge applications; illustrative from smithing SCHEMA.md §4 reference
      # range; label: inferred.]
    - item: "Ventilation blower (motor bearing failure)"
      estimated_hours_to_failure: 2000
      replacement_cost: 300
      replacement_lead_time_days: 5
      serviceable_by: operator
      # Blower motor bearing failure is the most common ventilation failure mode.
      # Per smithing SCHEMA.md §4: 1,500-3,000 hrs; operator- or journeyman-level
      # for standard replaceable-type motors; 5-day lead time from regional
      # electrical supply.
      # [CITATION-NEEDED: ventilation blower bearing MTBF data for light-
      # industrial applications; illustrative from smithing SCHEMA.md §4;
      # label: inferred.]

  maintenance_schedule:
    daily:
      task: "Wipe induction coil housing and water-cooling connections; clear metal debris from work area; inspect quench trough for contamination; check safety interlocks"
      performed_by: operator
    weekly:
      task: "Inspect coil lead connections and power cable insulation for wear; check coolant level and flow rate; clean ventilation intake filter; inspect anvil base for loosening"
      performed_by: operator
    quarterly:
      task: "Full coolant flush and refill (induction cooling circuit); inspect and torque all electrical connections; calibrate temperature sensor or pyrometer; check ventilation ductwork seals"
      performed_by: journeyman
    annual:
      task: "Coil replacement or professional refurbishment inspection; full electrical safety check by licensed electrician; ventilation blower motor service; comprehensive tooling inventory and replacement"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 20
  # Induction startup is substantially faster than coal (no fire-building, no
  # warm-up period for refractory). 20 min/day covers: equipment power-on and
  # safety interlock check (~5 min), end-of-day cleanup and coolant system
  # shutdown (~10 min), and daily inspection log (~5 min). Significantly below
  # the 30-60 min/day overhead for coal forges. [Derived from induction-electric
  # operational characteristics per smithing SCHEMA.md §2; CITATION-NEEDED:
  # empirical startup/shutdown data for commercial induction forge operations.]

  max_active_hours_realism_note: >
    35 hr/wk is a derated net figure. Derating applied: 20 min/day startup-
    shutdown overhead × 5 operating days = 1.67 hr/wk overhead deducted, leaving
    a theoretical ceiling of ~38 hr/wk forging time, from which 3 hr/wk is
    further allocated to customer intake, quote preparation, and administrative
    tasks typical of a single-operator repair shop. The 35 hr/wk figure used in
    sim_params is therefore the estimated net productive forging time, not the
    theoretical ceiling. Consistent with REQUIREMENTS R-06 (4-8 active forging
    hr/day historical baseline; 35/5 = 7 hr/day at the upper-mid range).

  interruption_notes: >
    Single-operator repair shops typically experience customer walk-ins 2-4 times
    per workday (~10-15 min each); phone inquiries (~5 min each, 3-4/day); and
    tool-change or workpiece-setup time (~5 min per repair job transition).
    Aggregate intraday interruption estimated at 45-60 min/day beyond the
    startup/shutdown overhead. This is folded into the 35 hr/wk net figure
    (reduced from ~38 hr theoretical net) rather than modeled as a separate
    downtime fraction. Authors of downstream entries who modify the product mix
    toward production (lower repair %) should reconsider the interruption load.

  consumables_lead_time_days: { typical: 3, worst: 21 }
  # Typical: grinding wheels, flux, and cleaning compounds available from
  # regional industrial supply (town/small-city: moderate supplier density per
  # SCALES.md §6). Worst: induction coil and specialty refractory items may
  # require factory-direct ordering with 14-21 day lead time during supply-chain
  # stress. [SCALES.md §6 supplier density; illustrative lead-time estimates;
  # CITATION-NEEDED: empirical consumable lead-time data for induction forge
  # repair operations.]

  throughput_variance:
    seasonal: "Pre-planting (March-April) and post-harvest (Oct-Nov) peaks for agricultural implement repair; summer and January troughs; indoor setting and urban/suburban clientele moderately reduce agricultural seasonality vs. outdoor rural forges"
    worst_month_fraction_of_average: 0.50
    best_month_fraction_of_average: 1.60

  operator_impact:
    noise_db: 70
    # Induction forges are substantially quieter than coal forges (no bellows,
    # no coal combustion noise). 70 dB(A) at operator position during normal
    # operation reflects induction hum, anvil strike noise, and ventilation.
    # Grinding operations (co-located for repair finishing) may peak higher
    # (85-95 dB); PPE required for grinding periods.
    # [CITATION-NEEDED: sound level measurement at operator position for
    # commercial induction forge operations; illustrative estimate; label: inferred.
    # OSHA permissible exposure limit: 90 dB(A) for 8-hour shift — 29 CFR 1910.95.]
    heat_exposure: "Localized near the workpiece during active forging; induction heats the workpiece not the ambient environment, significantly reducing whole-room heat load vs. coal forge; operator thermal exposure is moderate at the anvil, low at distance"
    emissions: "Near-zero combustion emissions at point of use; no CO, SOx, or particulate from the heat source; metal-grinding particulate from finishing operations requires local extraction per OSHA 29 CFR 1910.94"
    physical_demand: "Moderate; sustained standing; repetitive hammer and hand-tool use; lower sustained heat stress than coal forge; lifting of workpieces up to ~15 kg for repair items in the medium-work category"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Light-industrial or mixed-use zoning adequate; no combustion permit required; induction-electric qualifies for cleaner regulatory path than coal or propane in most jurisdictions"
  emissions: "No combustion emissions permit required; grinding/cutting particulate may trigger local air-quality notification thresholds at sustained production volumes; verify with local authority"
  other: "Electrical service upgrade (≥100A single-phase, 3-phase preferred) may require permit and utility coordination; OSHA 29 CFR 1910.95 (noise) and 1910.94 (grinding ventilation) apply to co-located finishing operations"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: good
  cooperative: marginal
  civic: marginal

scale_fit:
  village: marginal
  town: good
  small_city: good

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:
  cooperative:
    membership_boundary: >
      Town or small-city residents and nearby businesses within a 15-mile
      radius; paid annual dues ($150-$300/yr estimated) entitle members to
      booked shift access to the induction forge for their own repair work
      under their own skill level; specialist repair jobs above member skill
      are referred to the contracted journeyman operator. Village members
      may join but reduced repair demand at village scale makes individual
      membership economics marginal.
    rules_source: >
      Operating bylaws adopted at founding; member vote required to amend
      any provision; annual meeting reviews dues schedule and access rules.
      Rules specify: shift booking protocol, skill-level self-certification
      for access tier, required safety orientation completion, equipment
      damage liability, and dues schedule.
    monitoring: >
      Equipment usage logged per session via booking system (digital or
      paper sign-in sheet); monthly usage report to elected steward;
      safety incident log maintained and reviewed quarterly; annual
      financial report to membership. Damage or misuse reported by any
      member to the steward triggers review.
    graduated_sanctions: >
      First incident: written warning and mandatory safety re-briefing.
      Second incident within 12 months: $75 fine and 30-day access
      suspension. Third incident within 24 months: membership review by
      steward and member committee; possible permanent suspension.
      Equipment damage: cost-recovery invoice plus warning. Graduated
      structure per Ostrom Principle 5. [Ostrom 1990, Governing the Commons]
    conflict_resolution: >
      Member-elected steward handles first-level disputes; appeal to full
      membership vote at the next scheduled meeting (monthly or quarterly);
      unresolved legal disputes referred to the cooperative's registered
      legal form's dispute-resolution provisions. Per Ostrom Principle 6.
      [Ostrom 1990]
    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6]
    # Principle 1 (clearly defined boundaries): membership_boundary above.
    # Principle 2 (rules fit local conditions): small-footprint induction forge
    # rules calibrated to single-shift, single-operator-at-a-time access.
    # Principle 3 (collective choice arrangements): member vote to amend bylaws.
    # Principle 4 (monitoring): usage log + steward audit.
    # Principle 5 (graduated sanctions): above.
    # Principle 6 (conflict resolution): above.
    # Principle 7 (external recognition): addressed via legal_form below.
    # Principle 8 (nested governance): not applicable at single-cooperative scale;
    # no nested governance structure is required or present.
    # Non-addressed: Principle 7 is addressed at lens_fit.cooperative: marginal
    # (not `good`) — legal_form is recommended but not strictly required by
    # schema at marginal rating. Included here as best practice.
    member_amendment_process: >
      2/3 vote at scheduled annual meeting; 30-day notice to all members
      required before any bylaw amendment vote; emergency amendment (3/4 vote
      threshold) permissible with 7-day notice for safety-related rule changes only.
    legal_form: >
      LLC (single-member or multi-member depending on founding structure) or
      state-registered unincorporated cooperative association, depending on
      jurisdiction. Legal registration recommended even at marginal scale to
      provide external recognition (Ostrom Principle 7 analog) and member
      liability protection. Specific jurisdiction filing required before launch.
    scale_fit_note: >
      Cooperative form is marginal at village scale (repair demand too thin
      to sustain member pool above break-even; 500-2,000 residents × 2.5%
      participation rate = 13-50 members, with break-even requiring
      substantive dues volume to offset $42,000 capital + operating costs).
      Town scale (2,000-15,000) provides an adequate member pool of ~50-375
      members at 2.5% participation, with break-even reachable.
      [SCALES.md §5 member-pool formula; Ostrom 1990]

  civic:
    political_coalition: >
      Municipal economic-development office (repair-capacity argument);
      library-adjacent siting allies (tool-library model); small-business
      alliance (supporting local repair economy reduces commercial hardware
      imports); workforce-development program (apprentice-pipeline externality).
    council_vote_estimate: >
      Estimated 4-3 or 5-2 favorable in typical town or small-city context;
      primary opposition argument is the availability of private repair operators
      and the question of whether a civic facility displaces them. Civic case
      rests on apprentice-pipeline and repair-culture externalities not priced
      by the market.
    competes_with_private: >
      Where a functioning private repair smith exists in the target town or
      small-city, a civic facility requires explicit justification (per schema
      requirements and Principle 4). In the majority of target towns and small
      cities, no functioning private forge-based repair operator exists as of
      2024-2026; the civic facility fills a gap rather than displacing a
      functioning private operator. Entries in specific communities must verify
      this assessment locally.
    governance_form: >
      Municipally owned equipment; operated by contracted journeyman smith under
      annual renewable contract; booking managed by library or parks-and-rec
      department using existing scheduling infrastructure (tool-library model).
    budget_line: >
      Capital ($42,000 mid-estimate) via economic-development grant, workforce-
      development grant, or municipal equipment reserve fund; installation
      ($8,000) under capital budget; operations ($1,800 maintenance + $2,400
      consumables + $3,600 rent + $52,000 contracted journeyman wage) under
      workforce-development or parks-and-rec operating line.
    benchmark_comparison: >
      Town scale (3,000 households): annualized capital ($42,000 + $8,000
      install ÷ 20-year amortization = $2,500/yr) + annual operations
      ($59,800/yr) = ~$62,300/yr ÷ 3,000 hh = $20.77/hh/yr.
      Small-city scale (16,000 hh): same $62,300/yr ÷ 16,000 hh = $3.89/hh/yr.
      Comparison: IMLS Public Library Survey FY 2021 median library operating
      expenditure ~$40-$55/capita × 2.5 hh-size = $100-$137/hh/yr for library
      service. This facility costs $3.89-$20.77/hh/yr vs. library at $100-$137/hh/yr.
      Per-household cost is well within the CIVIC lens pass thresholds of $100/hh
      (town) and $80/hh (small-city) defined in SCALES.md §4.
      [SCALES.md §4; IMLS Public Library Survey FY 2021]
    staffing_model:
      role: "contracted journeyman smith"
      operator_fte: 1.0
      wage_assumption: 52000
      # Between town-scale ($56,000) and village-scale ($48,000) SCALES.md
      # median wage thresholds; $52,000 reflects contracted (not FTE-benefited)
      # journeyman rate for a part-time or contract-basis engagement.
      # Prompt specification: "~$52k/yr per SCALES".
      wage_source: "corpus/program/SCALES.md §3; journeyman contracted rate estimated between town-scale median ($56,000) and village-scale median ($48,000); SCALES.md §3 BLS OEWS SOC 47+51 basis"
      hours: "35 productive forging hours/wk plus ~5 hr/wk administrative, customer intake, and booking management = ~40 hr/wk effective; contracted on annual basis"
      hiring_notes: >
        Journeyman-floor operator required; hiring pool regional (50-100 mile
        radius for town/small-city settings); induction-forge experience preferred
        but not required — journeyman coal or propane smith can be trained on
        induction in 2-4 weeks; apprentice pipeline sourced from local workforce-
        development program or community college.
    civic_externalities:
      - "Apprentice training pipeline: integrates 1-2 apprentices per 3-year cycle into normal operations, producing journeyman-level repair capacity for the regional market"
      - "Repair culture: accessible civic forge reduces throwaway consumption of metal implements, tools, and hardware — a measurable public goods externality where market-rate repair pricing deters individual investment in repair"
      - "Supply-chain resilience: a locally operated forge provides emergency fabrication and repair capacity for municipal and agricultural equipment during commercial supply-chain disruptions"
      - "Skills preservation: maintains working forge competency in the community; where all local smithing capacity has already been lost, the civic forge reestablishes the baseline from which apprentice training can resume"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 42000
  # Equals economics.capital_cost.mid per E3-R1. [Derived from economics block above]

  cost_sd: 8750
  # Derived: (capital_cost.high - capital_cost.low) / 4 = (60,000 - 25,000) / 4
  # = $8,750. Within the E3-R5 plausible range (cost_sd/cost_mean = 8,750/42,000
  # = 0.208; within 0.15-0.50 range). [Derived per catalog/SCHEMA.md §3 default]

  throughput_units_equiv_per_year: 5900
  # Derivation (stated explicitly per smithing SCHEMA.md §1 E-3 cross-check):
  # Step 1 — derated active hours/yr:
  #   max_active_hours_per_week (35) × 52 wk × (1 - downtime_fraction 0.10)
  #   = 35 × 52 × 0.90 = 1,638 hr/yr
  # Step 2 — weighted throughput rate using product_mix:
  #   repair (60%) + commodity (10%) → use small_work rate (5/hr): 70% × 5 = 3.50
  #   specialty (20%) → use medium_work rate (1.5/hr × weight factor):
  #     specialty produces ~1.5 units/hr but each is valued as ~2 small-work equiv;
  #     for throughput counting, use direct rate contribution: 20% × 1.5 = 0.30
  #   artistic (10%) → use large_work rate (0.4/hr): 10% × 0.4 = 0.04
  #   weighted rate = 3.50 + 0.30 + 0.04 = 3.84 small-work equiv/hr
  # Step 3: 1,638 hr/yr × 3.84 equiv/hr = 6,290 raw units/yr
  # Step 4 — intraday interruption derating: max_active_hours_realism_note states
  #   35 hr/wk already incorporates ~1.67 hr/wk of direct overhead derating,
  #   but interruption_notes estimates an additional ~45-60 min/day beyond
  #   startup/shutdown that is partially already folded in; applying a modest
  #   5% further derating for unplanned interruptions:
  #   6,290 × 0.94 ≈ 5,913 → 5,900 (rounded to nearest 100).
  # Cross-check with E3-R2: 35 × 52 × 0.90 × 3.84 = 6,290 (within-order of 5,900;
  # ~6% discrepancy from interruption derating; acceptable for P2 threshold).
  # [Derived from throughput fields, product_mix, and downtime_fraction above]

  variable_cost_per_unit: 0.80
  # Energy: 12 kWh/hr × $0.125/kWh = $1.50/hr ÷ 3.84 units/hr = $0.39/unit.
  # Non-energy consumables: $2,400/yr ÷ 5,900 units/yr = $0.41/unit.
  # Total: $0.39 + $0.41 = $0.80/unit.
  # [Derived from energy_consumption_per_active_hour, EIA electricity price
  # $0.125/kWh per SCALES.md §6 footnote and annual_consumables above;
  # electricity price: US EIA Electric Power Monthly Table 5.3]

  labor_hours_per_unit: 0.26
  # 1 hr ÷ 3.84 units/hr weighted rate = 0.260 hr/unit.
  # E3-R3 cross-check: 5,900 units × 0.26 hr/unit = 1,534 hr/yr; target =
  # 35 × 52 × 0.90 = 1,638 hr/yr. Discrepancy = 104 hr (6.3%); within P2
  # threshold. Difference reflects rounding in interruption derating applied
  # in throughput_units_equiv_per_year.
  # [Derived from weighted throughput rate above]

  downtime_fraction: 0.10
  # Primary induction coil failure at ~1,800 hrs → 21-day lead time = 3 weeks
  # downtime in the first year. Ventilation blower at ~2,000 hrs → 5-day lead
  # time. Plus routine maintenance shutdowns (~1 week/yr). Total estimated
  # downtime: ~4-5 weeks/yr out of 52 = 8-10%. Midpoint 0.10 used.
  # Consistent with E3-R6 (downtime_fraction consistent with first_year_failures
  # profile: coil replacement alone = 3 weeks ≈ 5.8% downtime; consistent with
  # 10% when routine maintenance is added).
  # [Derived from operations_reality.first_year_failures above]

  lifespan_years: 20
  # Commercial induction forge units are rated for ~20,000-30,000 operating
  # hours under regular maintenance; at 35 hr/wk × 50 active wk/yr = 1,750 hr/yr,
  # 20,000 hr service life = ~11 years to first major overhaul; full design life
  # with major refurbishment at year 11-15 supports a 20-year total lifespan.
  # Lower than the 25 years used for coal forges (refractory and structural
  # components age differently from electronic systems).
  # [CITATION-NEEDED: service life data for commercial induction forge systems;
  # illustrative estimate from general industrial electronics longevity;
  # label: inferred.]

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: win
    primary_metric: 0.17857015307033522
    metric_name: payback_years
    notes: ''
  village_coop:
    verdict: fail
    primary_metric: 52.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=52, total_annual_cost=10300
  village_civic:
    verdict: fail
    primary_metric: 11.733333333333334
    metric_name: per_household_cost
    notes: per_hh=11.73, threshold=120, hrs/capita=0.000 vs threshold=2.0
  town_market:
    verdict: win
    primary_metric: 0.17857015307033522
    metric_name: payback_years
    notes: ''
  town_coop:
    verdict: win
    primary_metric: 52.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=52, total_annual_cost=10300
  town_civic:
    verdict: fail
    primary_metric: 1.7254901960784315
    metric_name: per_household_cost
    notes: per_hh=1.73, threshold=100, hrs/capita=0.000 vs threshold=2.0
  small_city_market:
    verdict: win
    primary_metric: 0.17857015307033522
    metric_name: payback_years
    notes: ''
  small_city_coop:
    verdict: win
    primary_metric: 52.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=52, total_annual_cost=10300
  small_city_civic:
    verdict: fail
    primary_metric: 0.32592592592592595
    metric_name: per_household_cost
    notes: per_hh=0.33, threshold=80, hrs/capita=0.000 vs threshold=2.0
sources:
  - ref: "REQUIREMENTS.md R-06: active forging hours per day 4-8 hr across all four anchor cultures; startup/shutdown overhead 1-2 hr/day structural inference"
  - ref: "REQUIREMENTS.md R-10: small-scale forge footprint 15-40 m²; American frontier one-bay smithy (Wallace 1978 Rockdale, 15-30 m²)"
  - ref: "REQUIREMENTS.md R-11: minimum ceiling height ~2.5 m for combustion-gas clearance"
  - ref: "REQUIREMENTS.md R-12: ventilation mandatory; OSHA 29 CFR 1910.252(c)"
  - ref: "REQUIREMENTS.md R-17: repair work journeyman minimum skill floor; formed judgment required"
  - ref: "REQUIREMENTS.md R-18: concurrent operators 1 smith + 0-2 assistants; motorized air eliminates bellows requirement"
  - ref: "REQUIREMENTS.md R-19: American frontier informal apprenticeship model; shorter and variable duration"
  - ref: "REQUIREMENTS.md R-22: product category scope must be stated"
  - ref: "REQUIREMENTS.md R-07: seasonal throughput variance; agricultural seasonality in all four cultures"
  - ref: "catalog/smithing/SCHEMA.md §1: throughput ceilings small_work 4-8/hr, medium_work 2-4/hr, large_work 0.3-1/hr"
  - ref: "catalog/smithing/SCHEMA.md §2: induction-electric energy consumption 6-15 kWh/hr; temperature ceiling ~1050-1100°C practical"
  - ref: "catalog/smithing/SCHEMA.md §4: primary coil failure 1,500-2,500 hrs, replacement specialist; ventilation blower 1,500-3,000 hrs, operator-level"
  - ref: "catalog/smithing/SCHEMA.md §5 Group A: repair-dominant entries guidance; product_mix.repair defining field"
  - ref: "corpus/program/SCALES.md §3: median wage thresholds; town $56,000/yr, village $48,000/yr; BLS OEWS SOC 47+51 basis"
  - ref: "corpus/program/SCALES.md §4: CIVIC lens per-household cost thresholds; town $100/hh/yr, small-city $80/hh/yr; IMLS Public Library Survey FY 2021 basis"
  - ref: "corpus/program/SCALES.md §5: cooperative member-pool formula; 2.5% participation rate at village and town scale"
  - ref: "corpus/program/SCALES.md §6: infrastructure baseline; electricity $0.10-$0.15/kWh (US EIA Electric Power Monthly); supplier density by scale"
  - ref: "US Energy Information Administration. Electric Power Monthly, Table 5.3: Average Retail Price of Electricity. Monthly release. https://www.eia.gov/electricity/monthly/ (small-commercial blended rate 2023-2024: $0.10-$0.15/kWh; midpoint $0.125 used)"
  - ref: "IMLS. Public Library Survey, Fiscal Year 2021. Published 2023. https://www.imls.gov/research-evaluation/data-collection/public-libraries-survey (median operating expenditure per capita ~$40-$55; per-household ~$100-$137)"
  - ref: "Ostrom, Elinor. 1990. Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press. (Chapters 2-3: eight design principles, graduated sanctions, minimum viable group size)"
  - ref: "OSHA 29 CFR 1910.252(c). Hot-work ventilation standards. (Ventilation and respiratory-protection requirements for forging and hot-work operations)"
  - ref: "OSHA 29 CFR 1910.94. Ventilation — grinding, polishing, and buffing operations. (Local exhaust ventilation requirements for co-located finishing)"
  - ref: "OSHA 29 CFR 1910.95. Occupational noise exposure. (90 dB(A) PEL for 8-hour shift)"
  - ref: "Wallace, Anthony F.C. 1978. Rockdale. Knopf. (American frontier one-bay smithy footprint ~15-30 m²; cited in REQUIREMENTS R-10)"
  - ref: "Hartwell, Robert. 1962. A Revolution in the Chinese Iron and Coal Industries During the Northern Sung, 960-1126 A.D. Journal of Asian Studies 21(2): 153-162. (Song China coal transition as demand-driven supply-economics precedent; functional analog to modern induction-electric transition)"
  - ref: "Atack, Jeremy, and Peter Passell. 1994. A New Economic View of American History. 2nd ed. Norton. (American frontier coal transition driven by railroad freight economics; analog for supply-driven fuel-choice reasoning)"
  - ref: "[CITATION-NEEDED: capital cost data for commercial induction forge systems 10-20 kW range, 2024-2026; Anvilfire, Induction Systems, or equivalent vendor catalog data]"
  - ref: "[CITATION-NEEDED: electrical service upgrade costs for commercial induction equipment; general electrical contractor cost data, 2024]"
  - ref: "[CITATION-NEEDED: annual maintenance cost data for commercial induction forge operations; trade or operator survey, 2024]"
  - ref: "[CITATION-NEEDED: repair-market pricing data for small-metalwork repair services in US town and small-city markets, 2024-2026; trade survey or operator financials]"
  - ref: "[CITATION-NEEDED: commodity hardware pricing per unit at US hardware retail or wholesale, 2024; Grainger, Fastenal, or equivalent distributor catalog]"
  - ref: "[CITATION-NEEDED: induction coil mean-time-to-failure data for commercial forge applications; manufacturer service data or experimental measurement]"
  - ref: "[CITATION-NEEDED: throughput measurement for induction-forge repair operations; experimental or operator-reported data]"
  - ref: "[CITATION-NEEDED: service life data for commercial induction forge systems; manufacturer specification or industry longevity data]"
---## Summary

The Induction-Modular Small Repair forge is a single-operator, electric-induction shop
designed for the tool and implement repair segment in town and small-city settings. Its
distinguishing characteristics are: (1) induction-electric heat source, which eliminates
combustion emissions, reduces regulatory friction, and allows placement in light-industrial
or mixed-use urban zones; (2) compact 20-35 m² footprint accessible to a single journeyman
operator; and (3) a repair-dominant product mix (60% repair, 10% commodity, 20% specialty,
10% artistic) targeting the niche that has demonstrated the strongest survival across all
four anchor cultures in the REQUIREMENTS research. This entry targets a market that prices
repair services as a premium labor product ($40-$90 per small-work equivalent) rather than
competing against commodity hardware pricing ($10 industrial baseline). The design is
apprentice-friendly: induction's digital temperature feedback makes the heat-judgment
learning curve more gradual for apprentices than coal or propane, while the fundamentals of
repair diagnosis and fitting remain journeyman-level skills.

## Design rationale

This entry addresses a specific gap in the catalog: a modern, regulation-minimizing repair
forge that can operate in urban or near-urban settings where coal combustion is either
prohibited or impractical. Forge-005 (Frontier-Revival Coal) covers the rural coal repair
niche; forge-002 covers the urban induction-electric equivalent. The two entries share the
repair-dominant orientation and market-primary lens fit but diverge sharply on energy source,
regulatory posture, and physical placement. Induction-electric eliminates: the combustion
permit pathway, the coal supply-chain dependency, and the particulate-emission management
requirement. In exchange it introduces: higher capital cost per kWh of heat, electrical
service infrastructure requirements, and coil-failure downtime risk. The specific problem
this entry solves is: how does a modern repair smith operate in a town or small city where
zoning or landlord restrictions preclude coal or propane combustion? The answer is a fully
electric forge whose regulatory path is straightforwardly an electrical service permit,
available in any light-industrial or mixed-use commercial zone.

## Historical lineage

Two precedents inform this design. First, the American frontier repair-dominant smith
[American frontier chapter §5, §9; Gordon 1996; Atack and Passell 1994]: the frontier
smith's functional inheritance to this entry is the repair-primary revenue model — labor
applied to customer-owned implements, with demand that is location-bound and not replicable
by industrial substitutes. The frontier smith used coal and later coke as those fuels became
economical via railroad freight; this entry follows the same supply-economics logic by using
electricity as the most economical and regulatorily accessible heat source in a modern urban
setting. Second, Song-dynasty China's coal transition [Hartwell 1962; REQUIREMENTS §4
DIV-01]: the transition from charcoal to coal in northern Song China was not technically
forced but demand-driven — coal was simply cheaper to transport given the geography of
co-located coal and iron ore deposits. REQUIREMENTS §4 draws the explicit modern analog:
"modern propane forges and induction forges represent equally valid supply-driven fuel
choices, not deviations from 'authentic' practice." This entry inherits that logic: the
choice of induction-electric is not a departure from historical precedent but the continuation
of a consistent pattern of forge operators using the most economical and accessible fuel in
their supply context. Labor regimes: the American frontier model relied on informal
apprenticeship and household-adjacent assistance without coercive indenture [REQUIREMENTS
R-19; REQUIREMENTS §6 labor-regime adjustment note]. The modern equivalent is a contracted
journeyman with a voluntary apprentice arrangement at market-adjacent wages — consistent
with REQUIREMENTS §6's mandate to adjust historical economics upward for modern labor
conditions [REQUIREMENTS R-20].

## Key assumptions

Capital costs ($25,000-$60,000) are illustrative estimates inferred from market observation
of commercial induction forge systems in the 10-20 kW range as of 2024-2026; no formal
industry survey or vendor BOM underlies these figures [CITATION-NEEDED]. The mid-point
($42,000) is weighted toward the cost of a capable commercial system plus tooling and
ventilation rather than the minimum-viable unit (which would be ~$8,000-$15,000 for equipment
alone). Installation cost ($8,000) reflects the electrical service upgrade typically required
for a commercial induction forge; regional variation is substantial. Market pricing
($40-$90 per small-work equivalent) is inferred from informal market observation of repair-
smith pricing at craft and maker channels; it is explicitly labeled as placeholder-inferred
and requires verification against a trade pricing survey [CITATION-NEEDED]. Throughput
(5,900 units/yr) is derived from the smithing SCHEMA.md §1 journeyman ceiling rates weighted
by product mix, derated for downtime (10%) and intraday interruptions; the underlying
throughput rates for induction-forge repair operations are not empirically verified
[CITATION-NEEDED]. Electricity cost uses $0.125/kWh (mid-range of the $0.10-$0.15/kWh
small-commercial blended rate per US EIA Electric Power Monthly, SCALES.md §6). The
downtime fraction (0.10) is derived from the first_year_failures profile: coil replacement
at ~1,800 hrs with 21-day lead time ≈ 3-4 weeks downtime in year one, plus routine
maintenance, totaling approximately 10% of scheduled hours lost. All economic figures assume
market-wage labor throughout; no household or indenture-basis labor is assumed [REQUIREMENTS R-20].

## Known risks / failure modes

**Regulatory:** The primary regulatory risk is the electrical service upgrade cost and
lead time. An electrical service upgrade from residential to 100A commercial service requires
utility coordination and may take 4-12 weeks, delaying launch. In jurisdictions with
aggressive building codes, the light-industrial or mixed-use zoning requirement may exclude
some potential locations. Grinding and cutting co-located with the forge may trigger local
air-quality notification thresholds even without combustion. **Labor pipeline:** Journeyman
induction-forge operators are a thin labor pool as of 2024-2026; the induction-forge as a
production tool for repair work is not yet a well-established trade pattern. An operator with
coal or propane experience can be transitioned, but this adds 2-4 weeks of onboarding time.
The apprentice pipeline is the primary succession mitigation; a shop that fails to establish
an active apprentice relationship within the first three years will face succession risk if
the founding journeyman departs. **Supply chain:** Induction coil replacement is a
specialist-serviceable, 21-day lead-time event. A single-coil shop cannot operate during
coil replacement; a spare coil inventory ($1,400 per unit) significantly reduces downtime
risk but adds working-capital burden. The coil supply chain is concentrated in a small
number of specialist fabricators; a single-supplier dependency is a documented risk.
**Demand variance:** Repair demand is bursty and seasonally variable; the worst month is
estimated at 50% of average. A single-operator shop without a secondary revenue source
(specialty or artistic work) faces cash-flow strain during demand troughs.

## Target niche and competitive positioning

This entry targets the repair and maintenance segment — the historically most survivable
smithing niche per REQUIREMENTS §8 — in urban-accessible settings where traditional
combustion forges face zoning or landlord restrictions. The competitive positioning is not
against industrial hardware production ($10 commodity baseline) but against the absence of
accessible local repair capacity. The customer segment is: small-business operators who need
rapid repair of specific implements (agricultural, contractor, restaurant, marine), hobbyists
and collectors who value repair over replacement for quality tools, and institutions seeking
local fabrication capacity for maintenance items. This segment accepts $40-$90 for a repair
job that would otherwise require a $15-$30 shipping cost plus turnaround time to a distant
repair service, or a $20-$80 replacement cost for a new (often lower-quality) substitute.
Per REQUIREMENTS §8 on the repair category: "repair is inherently location-bound, requires
on-site judgment, not replicable by factory product." The market-good rating reflects this
position. The cooperative and civic marginal ratings reflect that while both governance forms
are feasible, the market-primary operation is the more straightforward path for this
entry's footprint and capital level.

## Iteration log

- 2026-04-18: v0.1 — initial authoring per Plan C Task 4. All schema fields populated;
  conditional blocks for cooperative (marginal) and civic (marginal) fully populated per
  E2-R5 and E2-R6 requirements; market pricing flagged as placeholder-inferred per
  citation policy; sim_params derivation stated explicitly in field comments; 12
  CITATION-NEEDED placeholders carried forward for post-authoring verification.
