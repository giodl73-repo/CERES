---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: forge-003
trade: smithing
name: "Shared Tool-Library Coal Forge (medium footprint)"
tagline: "Community-owned coal forge with member-booked shifts"
status: draft
version: "0.1"
supersedes: null
inspirations:
  - medieval-european-village-forge
  - edo-blacksmith-cooperative

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 35
ceiling_min_m: 3.5
ventilation: mechanical-extraction-required

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: coal
energy_consumption_per_active_hour: "8 kg coal"
backup_fuel: propane

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  units_per_hour:
    small_work: 6
    medium_work: 2
    large_work: 0.5
  max_active_hours_per_week: 45
  product_mix:
    repair: 50
    commodity: 10
    specialty: 30
    artistic: 10
  throughput_variance:
    seasonal: "Fall/winter peak for repair work; summer trough"
    worst_month_fraction_of_average: 0.45
    best_month_fraction_of_average: 1.65

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: journeyman
operators_concurrent: "1-2"
apprentice_friendly: true
apprentice_path:
  training_stages: >-
    Stage 1 (0–6 mo): safety orientation, coal fire management, ash cleanup protocol,
    basic stock prep (cutting, straightening, stock selection). Gate criterion: can
    build and maintain a forge fire independently and identify unsafe conditions.
    Stage 2 (6–18 mo): small-work production (hooks, simple hardware, nails, staples),
    tool maintenance and dressing, bellows and blower operation, session log completion.
    Gate criterion: independent small-work output at ≥4 units/hr with journeyman quality
    assessment.
    Stage 3 (18–36 mo): medium-work production (brackets, horseshoes, chain, chisels),
    heat-treatment fundamentals (normalize, anneal), supervised customer repair intake.
    Gate criterion: independent medium-work output at journeyman standard; forge-weld
    demonstration under supervision.
  time_to_independent_operation: "~36 months to journeyman standard on this equipment"
  succession_note: >-
    Apprentice co-presence during production shifts is the primary transmission mechanism;
    skill transfer is embedded in normal operations rather than segregated into a training
    program. The cooperative's mandatory apprentice-slot policy (at least one registered
    apprentice active whenever the forge operates ≥20 hr/wk) institutionalizes succession
    continuity beyond any single journeyman's career.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD
  capital_cost:
    low: 18000
    mid: 28000
    high: 45000
  install_cost: 6000
  annual_maintenance: 1500
  annual_consumables: 4200
  floor_space_rent_per_year: 4800
  market_price_per_unit:
    low: 32
    mid: 45
    high: 70
  pricing_notes: >-
    "Unit" is one small-work unit equivalent (0.1–0.5 kg finished piece or its
    labor equivalent in repair). The mid price of $45 represents a 3.75× premium
    over the industrial hardware-store baseline of $12/unit (imported commodity
    hardware). The premium is sustained by direct-to-consumer repair work and
    specialty mix; customers are local residents and small tradespeople who value
    proximity, customization, and repair capability unavailable industrially.
    [CITATION-NEEDED: market price survey for small-forge repair and custom-work
    pricing, comparable regional smith rate cards, 2023-2025]
  pricing_validation: >-
    Pricing evidence type: inferred from analogous operator financials and tool-library
    membership rate structures rather than a direct sales-data survey. Comparable
    small-forge operators in the US Midwest and Northeast report repair-work billing
    of $40–$75/hr for journeyman labor, yielding $35–$65 per small-work equivalent
    at typical cycle times. This is not a cost-plus residual. A direct market-rate
    survey (ToolLibrary.org or comparable trade association data) would strengthen
    this to sourced. [CITATION-NEEDED: ToolLibrary.org 2024 rate-card survey or
    equivalent; comparable operator billing data for journeyman coal forge repair work]
  industrial_baseline_price: 12

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Bellows blower motor (bearing failure)"
      estimated_hours_to_failure: 1800
      replacement_cost: 400
      replacement_lead_time_days: 7
      serviceable_by: journeyman
      # Coal forges using an electric blower (as opposed to traditional hand bellows)
      # experience blower motor bearing failure as the primary first-year downtime event.
      # Bearing replacement is journeyman-serviceable with standard motor-shop tools.
      # [CITATION-NEEDED: blower motor MTBF data for forge-duty centrifugal blowers;
      # smithing equipment service manuals or operator survey]

    - item: "Refractory lining (partial spalling)"
      estimated_hours_to_failure: 2400
      replacement_cost: 400
      replacement_lead_time_days: 7
      serviceable_by: operator
      # Partial spalling of fire-brick or castable refractory in the firebox is normal
      # in the first year of a coal forge under variable thermal cycling (member-booked
      # intermittent use accelerates thermal stress vs. continuous operation). Castable
      # refractory patching is operator-serviceable; materials are typically stocked.
      # [CITATION-NEEDED: refractory lining MTBF for intermittently-operated coal forges;
      # refractory product data sheets or comparable operator experience logs]

    - item: "Coal storage bin corrosion (base weld failure)"
      estimated_hours_to_failure: 4000
      replacement_cost: 200
      replacement_lead_time_days: 14
      serviceable_by: operator
      # Coal's moisture and sulfur content accelerate corrosion in mild-steel storage bins.
      # Base weld failure is the typical first-failure mode; repair or bin replacement is
      # operator-serviceable with basic welding skills (journeyman or above). Lead time
      # reflects fabrication or sourcing of replacement bin.
      # [CITATION-NEEDED: coal storage bin corrosion data; typical bin service life
      # under indoor storage conditions with bituminous coal]

  maintenance_schedule:
    daily:
      task: >-
        Remove ash and clinker from firepot; clean ash dump and ash pit; inspect
        bellows blower intake for obstruction; wipe down anvil and tool surfaces;
        clear coal spillage from work zone. Check flue damper operation.
      performed_by: operator
    weekly:
      task: >-
        Inspect bellows blower belt or coupling; check refractory lining for new
        cracks or spalling; inspect anvil base fasteners for loosening; test emergency
        shutdown procedure; review session log for anomalies; inspect propane backup
        connection and regulator.
      performed_by: operator
    quarterly:
      task: >-
        Full refractory inspection; patch spalled areas with castable refractory;
        replace blower motor brushes or bearings if wear indicators present; clean
        chimney and flue of soot accumulation; inspect structural anchors of forge
        stand; lubricate forge tuyere (if adjustable); review session-log metrics
        for throughput variance trends.
      performed_by: journeyman
    annual:
      task: >-
        Deep cleanout of firebox and flue system; full refractory assessment with
        partial or full replacement if indicated; blower motor full inspection and
        service; anvil stand inspection for settling or crack propagation; review
        and update member safety documentation; full audit of coal and propane
        stock levels and storage condition.
      performed_by: journeyman

  startup_shutdown_overhead_per_day_min: 45
  # Coal forge startup (fire-building, reaching working temperature ~900°C) takes
  # approximately 25–30 min; shutdown (banking or extinguishing fire, ash management,
  # safe-temperature verification before leaving) takes approximately 15 min. Total
  # per operating day: ~45 min. This is materially longer than propane or induction
  # forges and is the primary operational penalty of coal over alternative fuels.
  # [CITATION-NEEDED: coal forge startup/shutdown time data; operator experience
  # surveys or smithing guild documentation]

  max_active_hours_realism_note: >-
    45 hr/wk is the theoretical scheduling ceiling for a 6-day operating week. Net of
    45 min/day startup-shutdown overhead (6-day week: 270 min = 4.5 hr), effective
    production time is approximately 40.5 hr/wk gross. sim_params uses 2400
    throughput_units_equiv_per_year, which is substantially below the theoretical
    ceiling of ~3432 units (40.5 hr × 52 wk × [1 − 0.12] / 0.6 labor-hr/unit ≈ 3432).
    The gap reflects: (1) seasonal variance — worst month at 0.45× average; (2)
    intraday interruptions not captured in startup_shutdown_overhead (member check-in,
    tool changes, apprentice instruction); (3) realistic member-booking utilization
    (not all 45 schedulable hours fill at a new cooperative). The 2400 figure is the
    variance-adjusted realistic annual throughput, not the mathematical ceiling.

  interruption_notes: >-
    Typical intraday interruptions in a member-booked cooperative setting: member
    check-in and orientation (5–10 min/session start); tool setup and handoff between
    members (~10 min/changeover); apprentice instruction and correction (~20 min/day
    when apprentice is present); coal resupply from storage bin (~10 min/shift when
    needed). Aggregate: 45–60 min/operating day above and beyond startup-shutdown
    overhead. These are folded into the throughput_units_equiv_per_year figure of 2400
    rather than modeled separately.

  consumables_lead_time_days:
    typical: 5
    worst: 30
    # Typical lead time reflects regional coal distribution (most US and European towns
    # within delivery range of a coal yard or fuel merchant). Worst-case of 30 days
    # reflects supply-chain stress (regional coal distributor disruption, seasonal
    # stockout at supplier) or transition to alternative supplier. Propane backup
    # mitigates worst-case operational impact but does not fully substitute for coal
    # in a coal-optimized forge at full throughput.
    # [CITATION-NEEDED: coal supply chain lead times for small industrial/artisan
    # purchasers; regional fuel merchant delivery schedules]

  throughput_variance:
    seasonal: "Fall/winter peak for repair work (pre-winter equipment prep, post-harvest repair); summer trough (reduced farm and outdoor equipment demand)"
    worst_month_fraction_of_average: 0.45
    best_month_fraction_of_average: 1.65

  operator_impact:
    noise_db: 85
    # Forge hammering on anvil at operator position. OSHA PEL for 85 dB: 8 hr/day
    # continuous exposure limit; hearing protection required for extended shifts.
    # [CITATION-NEEDED: noise level measurements at coal forge operator position;
    # OSHA 1910.95 threshold documentation]
    heat_exposure: >-
      High at forge face and anvil (radiant heat from coal fire and hot stock);
      operator position 0.5–1 m from firebox during active work. Adequate mechanical
      ventilation is required to prevent heat accumulation in enclosed space. Summer
      operating conditions may require supplemental cooling or reduced shift length.
    emissions: >-
      Coal combustion produces particulate (PM2.5 and PM10), carbon monoxide (CO),
      and sulfur oxides (SOx) in proportion to coal sulfur content. Mechanical
      extraction to exterior is mandatory; dedicated chimney with adequate draft
      required. Urban core operation may be prohibited by local air-quality ordinance
      regardless of extraction. Operator exposure to CO is the primary acute risk;
      CO monitor required at operator position.
    physical_demand: >-
      Moderate-heavy: sustained standing on concrete or compacted earth; repeated
      hammer strikes (0.5–2 kg hammer) with arm and shoulder engagement; lifting
      of stock and finished work (typically 1–10 kg per piece); bending and reaching
      to manage fire and position work. Full-shift forging is physically demanding;
      member booking limits should account for operator fatigue if shift length
      exceeds 4 hours continuous.

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: >-
    Light-industrial or mixed-use zoning required; coal forges are restricted or
    prohibited in many urban cores and residential zones due to emissions and fire
    risk; verify local air-quality district rules before site selection.
  emissions: >-
    Particulate capture (baghouse or equivalent) may be required above certain
    throughput thresholds depending on jurisdiction; SOx limits apply in some
    air-quality attainment areas; check EPA and state/local AQD permit triggers.
  other: >-
    OSHA 29 CFR 1910.252(c) hot-work ventilation standards apply; local fire code
    governs coal storage quantity and separation from structure; check whether
    cooperative legal form requires occupancy permit amendment for multi-member access.

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: marginal
  cooperative: good
  civic: good

scale_fit:
  village: marginal
  town: good
  small_city: good

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:
  cooperative:
    membership_boundary: >-
      Town residents and surrounding township (within ~15 km radius), paying annual
      dues of approximately $300/yr [CITATION-NEEDED: comparable tool-library membership
      dues; ToolLibrary.org or US tool-lending library fee survey]. Membership open to
      adults 18+; no trade credential required for membership, but unsupervised forge
      access requires completion of safety orientation and demonstrated competency at
      journeyman-minimum standard (or supervised session with a journeyman member).
    rules_source: >-
      Cooperative bylaws; rules amended by member vote with 2/3 majority at annual
      general meeting. Session booking, equipment-use protocols, and safety rules are
      standing-committee policy (adjustable by 2/3 board vote between annual meetings
      with 30-day member notice).
    monitoring: >-
      Session log maintained per booking (member ID, session start/end, equipment used,
      incidents if any); monthly audit by elected steward against session log and physical
      equipment inspection; quarterly financials distributed to all members; annual
      meeting reviews steward audit reports.
    graduated_sanctions: >-
      Warning (first rule violation, documented in session log) → $50 fine (second
      violation or first safety-rule breach) → 30-day suspension from forge access
      (third violation or any serious safety incident) → membership review and potential
      termination (pattern of violations or single severe incident). Steward has
      discretion to escalate directly to suspension for safety-critical violations.
    conflict_resolution: >-
      Member-elected steward arbitrates disputes between members (scheduling conflicts,
      equipment-damage attribution, dues disputes); steward decision is final for
      disputes below $500 in value. Appeals above $500 or involving membership status
      go to full member vote at next regular meeting (or special meeting within 30 days
      if requested by 10% of members).
    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6]
    # Principle 1 (clearly defined boundaries): membership boundary defined by geography
    # and dues payment. Principle 2 (congruence with local conditions): rules calibrated
    # for town-scale participation and coal-forge operational realities. Principle 3
    # (collective choice): member vote to amend bylaws; see member_amendment_process.
    # Principle 4 (monitoring): session log + steward audit. Principle 5 (graduated
    # sanctions): see graduated_sanctions above. Principle 6 (conflict resolution): see
    # conflict_resolution above. Principles 7 (nested organisations) and 8 (external
    # recognition) are partially applicable — see scale_fit_note and legal_form.
    member_amendment_process: >-
      2/3 vote at annual general meeting; 30-day written notice to all members required
      before vote; emergency amendments (safety-critical changes) by 3/4 vote with 7-day
      notice. Any member may propose an amendment; proposals must be circulated with the
      meeting agenda.
    legal_form: >-
      State-registered cooperative corporation or 501(c)(3) nonprofit (jurisdiction-
      dependent); municipal acknowledgment on file. An unregistered informal cooperative
      is not an acceptable form for this entry: absence of legal registration creates the
      commons-failure mode identified by Ostrom principle 7 analog (external recognition
      prevents dissolution under pressure from non-members or municipal authorities).
      [CITATION-NEEDED: state cooperative corporation statutes; applicable jurisdiction
      for target town; IRS 501(c)(3) qualification criteria for member-service organizations]
    scale_fit_note: >-
      Governance rules calibrated for town-scale (2,000–15,000 residents). Minimum viable
      member pool is approximately 25 active members to sustain 45 schedulable forge-hours
      per week with realistic booking utilization [CITATION-NEEDED: tool-library membership
      utilization data; SCALES §5.5 or comparable]. At village scale (500–2,000 residents),
      the member pool is likely insufficient to reach this floor, making the cooperative
      unviable at that scale (consistent with scale_fit.village: marginal). Quorum for
      annual meeting decisions is infeasible at village scale.

  civic:
    political_coalition: >-
      Municipal workforce-development grant program + small-business development allies +
      local trades union or apprenticeship council (if present). Primary funding argument:
      gap-filling public infrastructure where no private operator exists.
    council_vote_estimate: >-
      5-2 favorable in a typical small-town council; principal opposition argues tax
      burden and questions whether a forge is an appropriate municipal service. Favorable
      votes rely on workforce-development and repair-culture framing rather than economic-
      development subsidy argument.
    competes_with_private: >-
      No existing private smith in the majority of target towns (2,000–15,000 residents);
      civic facility fills a genuine service gap rather than displacing a functioning
      private operator. If a private smith exists within 20 km, civic justification shifts
      to training-pipeline and emergency-capacity arguments rather than primary service
      provision. [CITATION-NEEDED: survey of private smith density in US/EU towns
      2,000–15,000 population; DECLINE-VERDICT §3 or comparable]
    governance_form: >-
      Municipally owned facility; operated by contracted master smith (or journeyman with
      master-level supervisory oversight) with one registered apprentice. Master smith
      reports to a workforce-development or parks-and-recreation department director;
      apprentice hired through local workforce-development pipeline.
    budget_line: >-
      Capital via 25-year municipal bond (or equivalent long-term financing instrument);
      annual operations funded under workforce-development or parks-and-recreation budget
      line. Operating costs include contracted smith wage (~$68,000/yr), annual maintenance
      ($1,500), consumables ($4,200), and floor space (~$4,800/yr imputed or actual).
    benchmark_comparison: >-
      Approximately $95–$120 per household per year in a town of 3,000–5,000 households
      [CITATION-NEEDED: per-household civic cost calculation; town population assumptions
      and bonded debt amortization rate; SCALES §5 or comparable]. For comparison:
      public library operating cost in peer towns is approximately $100/hh/yr; municipal
      recreation center is $150–$250/hh/yr [CITATION-NEEDED: library and rec-center
      per-household cost benchmarks; ALA or IMLS data for small-town libraries]. The
      forge sits within the library cost band, making the civic case politically
      tractable once the comparison is named explicitly.
    staffing_model:
      role: "Contracted master smith + registered apprentice (part-time to full-time)"
      operator_fte: 1.0
      wage_assumption: 68000
      wage_source: "corpus/program/SCALES.md §3 town-scale skilled-trades median [CITATION-NEEDED: verify SCALES.md §3 current figure for skilled-trades median at town scale]"
      hours: "40 hrs/wk production + administration (scheduling, member coordination, safety oversight)"
      hiring_notes: >-
        Journeyman-or-master smith required; hiring pool is regional (100-mile radius
        is typical for rural/small-town smithing vacancies). Retention risk is moderate:
        smithing-qualified labor is scarce and may be recruited away by larger urban
        operations or higher-paying specialty shops. Apprentice hired locally through
        workforce-development pipeline; pipeline must exist or be created as part of
        program launch. [CITATION-NEEDED: smithing labor market data; regional journeyman
        smith vacancy rates and typical retention period]
    civic_externalities:
      - >-
        Apprentice training pipeline: produces 1–2 journeyman smiths per 3-year cycle,
        supplying regional repair capacity that would otherwise be absent. Externality is
        not priced by the market (private smith cannot recover training costs in repair
        pricing without losing price-sensitive customers).
      - >-
        Emergency production capacity: civic forge can produce or repair critical metal
        components (agricultural equipment, utility hardware, structural fasteners) during
        supply-chain disruptions when commercial hardware supply is constrained.
      - >-
        Repair culture: accessible civic forge reduces throwaway consumption of metal
        goods; economic and environmental externality not captured in market pricing.
      - >-
        Resilience anchor: operational forge sustains downstream trades requiring custom
        or repaired metal components (carpentry, masonry, farriery, small-scale
        manufacturing) that would otherwise face service gaps.

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 28000
  # Must equal economics.capital_cost.mid = 28000. E3-R1 satisfied.
  cost_sd: 8000
  # Derivation: (capital_cost.high − capital_cost.low) / (2 × 1.65) ≈ (45000 − 18000) / 3.375 ≈ 8000.
  # Alternatively by convention: (high − low) / 4 = 27000 / 4 = 6750 (rounds to 7000);
  # 8000 reflects slightly wider tail given coal-forge installation variance.
  # [CITATION-NEEDED: capital cost distribution for coal forge with installation;
  # vendor quotes or comparable installer survey data]
  throughput_units_equiv_per_year: 2400
  # Derivation note (E3-R2 cross-check): Theoretical ceiling =
  #   45 hr/wk × 52 wk × (1 − 0.12) / 0.6 labor-hr/unit ≈ 3,432 units/yr
  # The sim_params figure of 2,400 represents the variance-adjusted realistic annual
  # throughput, incorporating:
  #   (a) Seasonal variance: worst month at 0.45× average means annual yield is
  #       reduced relative to flat-demand assumption; rough seasonal adjustment ≈ −10–15%.
  #   (b) Member-booking utilization: a new cooperative will not immediately fill all
  #       45 schedulable hr/wk; Year 1 utilization assumed ~60–70% of ceiling.
  #   (c) Intraday interruptions (member check-in, tool changes, apprentice instruction)
  #       folded in beyond startup-shutdown overhead.
  #   Combined effect: 3,432 × ~0.70 ≈ 2,402, rounded to 2,400.
  # This is intentionally conservative for a first-year/ramp-up estimate. A mature
  # cooperative at full utilization could approach 2,800–3,000 units/yr.
  variable_cost_per_unit: 3.1
  # Coal consumption: 8 kg/hr × $0.20/kg [CITATION-NEEDED: coal price per kg, small
  # industrial/artisan quantity, current US market] = $1.60/hr; at 0.6 hr/unit = $0.96
  # coal cost/unit. Consumables (flux, tooling wear, propane backup pro-rata, refractory
  # patch materials): estimated $2.14/unit. Total: ~$3.10/unit. [CITATION-NEEDED: flux
  # and consumable cost data for coal forge operations; smithing supply vendor pricing]
  labor_hours_per_unit: 0.6
  # 0.6 hr/unit = 36 min per small-work equivalent. Consistent with 6 small_work
  # units/hr throughput ceiling for journeyman operator on coal forge.
  # E3-R3 cross-check: 2400 units × 0.6 hr/unit = 1440 labor-hr/yr.
  # 45 hr/wk × 52 wk × (1 − 0.12) = 2059 hr/yr theoretical maximum.
  # 1440 / 2059 = 0.70 utilization — consistent with 70% booking utilization
  # assumption used in throughput_units_equiv_per_year derivation above.
  downtime_fraction: 0.12
  # 12% of scheduled hours lost to maintenance, failure, and setup interruptions.
  # Consistent with 3 first-year failures with aggregate lead time of ~28 days
  # (7 + 7 + 14 days), spread across operating year. Includes quarterly refractory
  # patching downtime (~0.5 day/quarter) and annual deep-cleanout (~1 day). At
  # 45 hr/wk, 12% ≈ 5.4 hr/wk average downtime — plausible for coal forge.
  # [CITATION-NEEDED: downtime fraction data for coal forges; operator survey or
  # comparable equipment reliability data]
  lifespan_years: 25
  # Conservative estimate for a masonry/steel coal forge under normal maintenance;
  # refractory is replaced on schedule, anvil and tooling maintained. 25-year
  # lifespan drives 25-year bond amortization for civic-lens calculation.
  # [CITATION-NEEDED: coal forge structural lifespan data; insurance or depreciation
  # schedules for comparable equipment]

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: win
    primary_metric: 0.43593767629832497
    metric_name: payback_years
    notes: ''
  village_coop:
    verdict: fail
    primary_metric: 60.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=60, total_annual_cost=11860
  village_civic:
    verdict: fail
    primary_metric: 13.666666666666666
    metric_name: per_household_cost
    notes: per_hh=13.67, threshold=120, hrs/capita=0.000 vs threshold=2.0
  town_market:
    verdict: win
    primary_metric: 0.43593767629832497
    metric_name: payback_years
    notes: ''
  town_coop:
    verdict: win
    primary_metric: 60.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=60, total_annual_cost=11860
  town_civic:
    verdict: fail
    primary_metric: 2.0098039215686274
    metric_name: per_household_cost
    notes: per_hh=2.01, threshold=100, hrs/capita=0.000 vs threshold=2.0
  small_city_market:
    verdict: win
    primary_metric: 0.43593767629832497
    metric_name: payback_years
    notes: ''
  small_city_coop:
    verdict: win
    primary_metric: 60.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=60, total_annual_cost=11860
  small_city_civic:
    verdict: fail
    primary_metric: 0.3796296296296296
    metric_name: per_household_cost
    notes: per_hh=0.38, threshold=80, hrs/capita=0.000 vs threshold=2.0
sources:
  - ref: "Ostrom, Elinor. 1990. Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press."
    # Supports cooperative governance structure; Ostrom design principles 1–8 applied in lens_context.cooperative.
  - ref: "Weisdorf, Jacob. 2006. 'From Foraging to Farming: Explaining the Neolithic Revolution.' Journal of Economic Surveys 20(4):561–586."
    # [CITATION-NEEDED: verify this supports medieval village forge framing in Historical Lineage; may need replacement with more directly applicable forge history source]
  - ref: "CITATION-NEEDED: ToolLibrary.org or equivalent tool-lending library membership dues survey, 2023-2025. Supports: economics.market_price_per_unit, lens_context.cooperative.membership_boundary annual dues figure."
  - ref: "CITATION-NEEDED: US coal price per kg for small industrial/artisan purchasers, 2023-2025 (EIA or comparable). Supports: sim_params.variable_cost_per_unit coal cost component."
  - ref: "CITATION-NEEDED: Per-household cost benchmarks for small-town public libraries (ALA or IMLS data) and municipal recreation centers. Supports: lens_context.civic.benchmark_comparison."
  - ref: "CITATION-NEEDED: corpus/program/SCALES.md §3 town-scale skilled-trades median wage. Supports: lens_context.civic.staffing_model.wage_assumption = $68,000."
  - ref: "CITATION-NEEDED: Blower motor MTBF data for forge-duty centrifugal blowers. Supports: operations_reality.first_year_failures[0] (bellows blower motor)."
  - ref: "CITATION-NEEDED: Refractory lining service life data for intermittently-operated coal forges. Supports: operations_reality.first_year_failures[1] (refractory lining partial spalling)."
  - ref: "CITATION-NEEDED: Coal forge startup and shutdown time; operator survey or guild documentation. Supports: operations_reality.startup_shutdown_overhead_per_day_min = 45."
  - ref: "CITATION-NEEDED: Survey of private smith density in US/EU towns 2,000–15,000 population. Supports: lens_context.civic.competes_with_private claim of gap-filling."
---## Summary

The Shared Tool-Library Coal Forge (forge-003) is a medium-footprint, member-booked
cooperative forge operating on coal with propane backup. It is designed for a town-scale
community (2,000–15,000 residents) where no private smith exists and where the capital
cost of a forge ($28,000 mid estimate, installed $34,000) is too high for a single
household but tractable for a membership cooperative of 25 or more. The cooperative
structure distributes capex across members, makes per-use costs accessible, and embeds
skill transmission (apprenticeship) into normal operations. This entry exists as the
canonical cooperative example in the CERES catalog — it is the reference design for
the shared-resource model and is used in spec v0.3 §5 as the schema example. Market
viability is marginal (coal forge output cannot compete on price with industrial
commodity hardware), but cooperative and civic viability are good: the cooperative
shares cost burden, and the civic case rests on apprentice training, emergency
production capacity, and repair-culture externalities that the market does not price.

## Design rationale

The forge-003 design addresses a specific gap that no other entry in the smithing
catalog addresses: the cooperative ownership structure applied to a full-production
coal forge at town scale. Other entries in the catalog are either single-operator
(forge-005, forge-002) or civic-primary without the member-governance layer (forge-011).
The cooperative model here is substantive, not decorative: member dues fund capital
amortization, Ostrom-compliant governance rules prevent free-riding, and the mandatory
apprentice-slot policy embeds succession into operational routine. Coal rather than
induction is the design choice because coal is the historically appropriate and lower-
capital energy source for a general-purpose repair and specialty forge; the ventilation
and emissions burden is the primary cost of that choice, and the 35 m² medium footprint
is sized to accommodate extraction infrastructure. The design specifically does not
optimize for market lens viability — the market lens is marginal by design, and the
cooperative and civic lenses carry the case.

## Historical lineage

Two inspirational precedents inform forge-003, with a required anti-romanticism note on each.

**Medieval European village forge** — the functional inheritance is the shared-resource
model and repair-dominant work mix. Medieval village forges operated as communal assets
(often guild-regulated or lord-licensed) serving the agricultural and craft repair needs
of the surrounding population; the smith was often the sole metalworker within a
multi-village catchment area, and the forge was a de facto public utility. The modern
cooperative design carries forward the shared-access structure and repair-dominant product
mix. What it does not carry forward: the coercive guild-licensing system, the smith's
semi-captive labor relationship with the manorial lord, and the monopoly enforcement that
prevented competition. [CITATION-NEEDED: primary or secondary source on medieval village
forge ownership and governance structures; Pounds 1994 or comparable economic history
of medieval craft organization]

**Edo-period blacksmith cooperative (shokunin estate)** — this inspiration requires
explicit anti-romanticism. The Edo-period shokunin (artisan) estate system in Japan is
sometimes cited as a precedent for cooperative craft organization, but this framing is
historically inaccurate. Edo shokunin were organized into hierarchical za (guilds) that
were state-licensed by the Tokugawa bakufu, not voluntary cooperatives; membership was
hereditary or controlled by guild masters with bakufu sanction; and the system was
explicitly designed to capture tax revenue and control urban labor. The functional
inheritance for forge-003 is limited to the multi-operator shared-forge model (several
smiths working at a common forge under a head smith's oversight) and the apprenticeship
transmission structure. The cooperative governance layer in forge-003 is not derived from
Edo precedent — it is derived from Ostrom commons governance principles applied to the
modern tool-library movement. [CITATION-NEEDED: Hauser 1974 or comparable on Edo
shokunin za structure; Penelope Francks on Tokugawa craft organization and state licensing]

## Key assumptions

**Capital costs:** The $18,000–$45,000 capital range is an illustrative estimate for
a medium-footprint coal forge including: firebox/hearth (custom masonry or pre-fabricated
steel), blower system, chimney and extraction hood, anvil (100–150 kg), basic tooling
set, and coal storage. The $6,000 installation cost covers concrete work, chimney
installation, electrical for blower, and permitting. These figures are not sourced to
a single vendor quote; they are illustrative order-of-magnitude estimates consistent
with comparable facility descriptions in the maker/smithing community.
[CITATION-NEEDED: vendor quotes or market survey for new coal forge installation
at 35 m² medium-footprint scale]

**Market price:** $45/unit (mid) is inferred from journeyman billing rates for repair
work ($40–$75/hr) and typical small-work cycle times, not from a direct price survey.
Pricing validation type is "inferred." The industrial baseline of $12/unit is an estimate
for commodity hardware-store imported equivalents; this is also not precisely cited.

**Sim_params cross-check:** 45 hr/wk × 52 × 0.88 / 0.6 ≈ 3,432 theoretical ceiling;
2,400 variance-adjusted figure assumes 70% utilization (Year 1 cooperative ramp-up +
seasonal trough). This is explicitly conservative. The 0.12 downtime_fraction is
consistent with 3 first-year failures with total lead-time days of ~28 days and
routine quarterly maintenance.

**Edo anti-romanticism:** The "edo-blacksmith-cooperative" inspiration label is retained
because it is used in the spec §5 example, but the Historical Lineage section explicitly
addresses the state-licensing reality. The inspiration is functional (multi-operator
shared-forge model; apprenticeship structure), not governance.

## Known risks / failure modes

**Regulatory (primary):** Coal use is restricted or prohibited in many urban cores and
air-quality non-attainment areas. Site selection is constrained to light-industrial or
mixed-use zones with adequate chimney height and setback from residential. Particulate
capture requirements above throughput thresholds could add $5,000–$20,000 to installation
cost. This is the entry's largest regulatory exposure. [CITATION-NEEDED: EPA/state AQD
permit thresholds for small-forge coal combustion; local air-quality district variance data]

**Labor pipeline:** Journeyman smith labor is scarce in rural and small-town markets. A
cooperative that cannot hire or retain a qualified journeyman cannot operate the forge
safely; the mandatory apprentice-slot policy is the long-term mitigation, but it takes
3 years to produce a journeyman from zero. Short-term succession gap is the highest
operational risk of this design. [CITATION-NEEDED: smithing labor market data; journeyman
smith vacancy rates by region]

**Supply chain:** Coal availability is declining in many regions as coal yards close and
distribution networks contract. Propane backup mitigates operational interruption but
does not fully substitute (coal forge geometry is not optimized for propane burners).
A cooperative that cannot source coal within its consumables_lead_time_days budget faces
either fuel conversion (capital cost) or operational shutdown. [CITATION-NEEDED: coal
distribution network density data for US/EU small-town markets; trend data on coal yard
closures]

**Demand variance:** Worst-month throughput at 0.45× average means that in a typical
summer trough, the cooperative may operate at less than half its average capacity. Member
satisfaction during trough months (paying dues but having little repair work to bring)
requires the cooperative to provide value through other means (tool access, social
function, specialty classes) or risk membership attrition. [CITATION-NEEDED: tool-library
member retention data; seasonal utilization patterns for comparable shared-workshop
facilities]

**Ostrom principles 7 and 8:** At single-cooperative scale, nested organizations (P7)
and external recognition by governmental authorities (P8) are partially but not fully
addressed. Legal registration (cooperative corporation or 501(c)(3)) provides the minimum
external recognition; absence of a regional cooperative network means P7 is not
applicable. This is a known governance gap for single-coop designs at this scale.

## Target niche and competitive positioning

Forge-003 targets the shared-resource civic-cooperative niche in towns of 2,000–15,000
residents where: (a) no private smith operates within reasonable distance, (b) the
community has sufficient social capital and organizational capacity to sustain a
member-governed cooperative, and (c) the repair and specialty work mix justifies
collective capital investment. Per DECLINE-VERDICT, this is not a commodity-hardware
competitor: the $45/unit price point requires a premium justified by repair work, local
customization, and the absence of substitutes — not by volume production. The civic
lens is equally viable: municipal ownership with contracted operations is an alternative
governance form that removes the member-recruitment risk while retaining the public-goods
justification. The market lens is marginal: a privately-owned coal forge at this scale
cannot generate sufficient margin on repair work alone to recover capital within a
reasonable payback horizon, which is why the cooperative and civic structures are the
primary lenses for this entry.

## Iteration log

- 2026-04-18: v0.1 — Initial authoring per Plan C Task 5. Entry is the canonical cooperative
  example from spec v0.3 §5; all v1.1 schema fields populated including new fields
  (operations_reality with serviceable_by, maintenance_schedule, startup_shutdown_overhead,
  max_active_hours_realism_note, apprentice_path, industrial_baseline_price, pricing_validation,
  lens_context.cooperative with member_amendment_process / legal_form / scale_fit_note,
  lens_context.civic with benchmark_comparison / staffing_model / civic_externalities).
  All three lens_context blocks present (market is marginal — lens_context.market is not
  a schema block; market parameters captured in economics fields per schema §3.1).
  Anti-romanticism note on Edo inspiration added per Plan B requirement.
  First-year failures corrected from spec example (which erroneously listed "primary coil"
  for a coal forge — coal forges have no induction coil); replaced with bellows blower
  motor, refractory lining, and coal storage bin corrosion per smithing SCHEMA.md §4
  reference list. Heavy [CITATION-NEEDED] load on pricing, capital costs, civic benchmarks,
  and labor market data — all flagged for post-authoring verification.
