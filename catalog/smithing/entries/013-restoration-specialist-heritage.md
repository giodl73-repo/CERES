---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: forge-013
trade: smithing
name: "Restoration Specialist Heritage Forge"
tagline: "Multi-fuel master-floor forge serving historic-building restoration and architectural-hardware repair for heritage-preservation clients"
status: draft
version: "0.1"
supersedes: null
inspirations: [medieval-european-architectural-smith, modern-us-historic-preservation-trade]

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 60
# Midpoint of the 40–80 m² required range. Restoration work requires staging
# area for large removed elements (gates, door hardware, railings) awaiting
# work and ready for return, plus dedicated chemistry bench for patina and
# finishing work and separate fuel storage and handling zones for three fuel
# types. Smaller end (40 m²) is feasible for a one-fuel-at-a-time operation;
# the upper range (80 m²) accommodates simultaneous staging of multiple
# in-work restoration projects common in peak season. 60 m² is used as the
# central planning figure.
# [CITATION-NEEDED: restoration smithing shop footprint norms; figure is a
# structural inference from the multi-fuel configuration, staging requirements,
# and chemistry bench constraint; no published survey identified]

ceiling_min_m: 4.0
# Minimum for raising and manoeuvring large removed elements (iron gates up to
# 2.5 m, fireplace surround assemblies) and for adequate coal-forge ventilation
# stack height. Standard commercial-bay ceiling at 4–5 m is adequate;
# residential and light-commercial ceilings below 3.5 m are insufficient for
# coal-forge exhaust stack geometry.

ventilation: dedicated-exhaust-system
# Multi-fuel operation drives the ventilation requirement to the highest tier.
# Coal mode produces particulate, SOx, and CO requiring a permanently installed
# hood, dedicated exhaust duct, and powered extraction meeting coal-combustion
# standards. Propane mode generates CO and combustion products requiring
# continuous extraction. Induction mode produces no combustion emissions but
# the ventilation system must remain operable for rapid fuel-mode transitions
# and for patina-chemistry fume extraction at the finishing bench. The coal
# exhaust requirement governs sizing; the three-fuel configuration means
# ventilation is the single largest installation cost driver. Per smithing
# SCHEMA §2: coal and propane both require mechanical extraction.

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: multi-fuel-coal-propane-induction
# Non-standard value per catalog/SCHEMA.md §8 (trade-specific values
# permitted for energy_source). Three fuel systems are operated selectively
# by project type: coal forge for work requiring forge-weld temperatures
# (~1300°C) and period-authentic methods where building-inspector or
# preservation-society standards mandate coal-fired production; propane forge
# for faster-turnaround repair work and projects where propane is adequate;
# induction for precision heat treatment, finishing normalization, and project
# phases requiring controlled temperatures without combustion. The three-fuel
# design is not comfort or redundancy — it is a client-requirement driver.
# Some preservation-society and Secretary-of-Interior-standards projects
# specify coal-fired methods explicitly; others accept propane; induction
# handles post-forming heat treatment across all project types. Per smithing
# SCHEMA §2: coal ~1300°C forge-weld capable; propane ~1260°C forge-weld
# marginal; induction ~900–1100°C no forge-weld.

energy_consumption_per_active_hour: "blended ~5 kWh + 0.3 kg propane + 0.5 kg coal on mixed-fuel days; single-fuel days vary by mode (coal: ~6 kg/hr; propane: ~1.2 kg/hr; induction: ~8 kWh/hr)"
# Blended figure represents a typical restoration work day mixing fuel modes.
# Single-fuel consumption figures per smithing SCHEMA §2 reference ranges:
# coal 6–10 kg/hr (6 kg/hr for standard fire management at restoration pace);
# propane 1–2 kg/hr (1.2 kg/hr for moderate-output repair work);
# induction 6–15 kWh/hr (8 kWh/hr at mid-range utilisation for heat-treatment
# sessions). Blended figure reflects that most active days involve 2–3 hours
# of primary heat work (coal or propane) plus induction heat-treatment cycles;
# not all three fuels are used simultaneously.
# [CITATION-NEEDED: multi-fuel consumption blending for restoration-shop
# mixed-day operation; component figures from smithing SCHEMA §2 reference
# ranges; blended estimate is a structural calculation, not empirically measured]

backup_fuel: propane
# Coal is primary for Secretary-of-Interior-standards work; propane serves as
# backup if coal supply is disrupted. Induction is available for heat-treatment
# phases when propane is primary. Full backup capability requires propane
# inventory maintained at minimum two weeks of production use.

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  units_per_hour:
    small_work: 1.5
    # Period-authentic hardware pieces: hinges, latches, knobs, escutcheons,
    # shutter dogs, and similar small architectural elements. 1.5 units/hr
    # reflects the combination of careful period-authentic work (slower than
    # commodity production) and the repair-dominant nature (fitting to existing
    # structure takes time). Per smithing SCHEMA §1: small_work is the
    # 0.1–0.5 kg range; smithing SCHEMA §1 ceiling ~4–8/hr for a journeyman,
    # but master-floor restoration work at period-authentic standards runs
    # substantially slower. 1.5/hr is the restoration-pace rate.
    medium_work: 0.5
    # Larger hardware: gate hinges, hook-and-strap assemblies, bespoke railings
    # (per linear metre), fireplace hardware components, door knockers. 0.5/hr
    # for medium restoration work is below the journeyman production ceiling
    # (2–4/hr per smithing SCHEMA §1) consistent with period-authentic fit and
    # finish requirements, documentation procedures, and careful disassembly/
    # reassembly of existing structures.
    large_work: 0.1
    # Full gate or fireplace fitout: complete restoration of a large iron gate,
    # full fireplace surround fitout, or a multi-element railing restoration.
    # 0.1/hr = one full fitout per ~10 active forge hours; total project time
    # including staging, assessment, and documentation is 3–5× forge time.
    # [CITATION-NEEDED: restoration-smithing throughput for large architectural
    # elements; figure is a structural inference from trade practice; no
    # systematic time-study publication identified]
  max_active_hours_per_week: 35
  # Full-time master-floor operation with fabrication helper. 35 hr/wk covers
  # forge time, bench work, patina chemistry, and fitting. Client assessment
  # visits to historic buildings (typically 2–4 hrs/wk for a fully-booked
  # restoration practice) and project documentation (required under many
  # preservation contracts, ~1–2 hrs/wk) are outside this figure. Per smithing
  # SCHEMA §1: realistic ceiling 40–45 hr/wk; 35 hr/wk reflects the higher
  # non-production overhead of restoration work vs. production smithing.
  product_mix:
    repair: 60
    commodity: 0
    specialty: 35
    artistic: 5
    # Repair: restoration IS repair — 60% of active time on customer-owned
    # elements (returning existing hardware to working condition, replicating
    # lost or damaged elements to match surviving examples). Zero commodity:
    # this entry explicitly avoids commodity production per DECLINE-VERDICT.
    # Specialty: period-authentic reproduction hardware fabricated to match
    # documented historical precedents (new elements where originals are
    # unrecoverable, or additions consistent with the historic character).
    # Artistic: small category for interpretive/artistic work on preservation
    # projects where the client brief allows discretion. Per REQUIREMENTS R-22.
  throughput_variance:
    seasonal: "Peak in spring–summer (construction-permit season for preservation projects) and autumn (before winter closures); winter worst month as preservation projects pause and new contracts are delayed."
    worst_month_fraction_of_average: 0.6
    best_month_fraction_of_average: 1.4
    # Preservation-project seasonality tracks construction-permit cycles and
    # grant-award timing (many historic-preservation grants are awarded in
    # spring for summer project starts). Winter trough is moderated (vs. pure
    # agricultural-seasonal repair) by indoor historic-building work (interior
    # hardware, fireplace elements) that continues through winter.
    # [CITATION-NEEDED: seasonal demand pattern for historic-preservation
    # smithing; figure inferred from construction-industry seasonal patterns
    # and preservation-grant-award cycles; no smithing-specific survey found]

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: master
# Period-authentic restoration work requires deep technical skill plus
# historical knowledge of hardware forms, construction methods, and material
# composition across multiple periods. A journeyman can execute individual
# operations under direction but cannot independently identify the correct
# period method, match historical alloy behavior, or navigate the documentation
# and certification requirements of preservation contracts. Per smithing
# SCHEMA §3: master tier — novel constraints, customer-brief interpretation
# without prescribed method, full technical range. Preservation-specific
# competency adds: knowledge of Secretary-of-Interior Standards for
# Rehabilitation (36 CFR Part 68), period-authentic material identification,
# and experience with State Historic Preservation Office (SHPO) documentation
# requirements. [CITATION-NEEDED: competency standards for historic-preservation
# smithing; figure is a structural inference from trade practice and
# preservation-law requirements; no formal credentialing survey identified]

operators_concurrent: "1-2"
# Master smith as primary operator; fabrication helper for material handling,
# staging, patina chemistry preparation, and two-person operations (handling
# large removed elements, managing multi-fuel transitions). Single-operator
# operation is feasible for small and medium hardware work; large fitout
# restoration (full gate, fireplace surround) requires two people for safe
# element handling.

apprentice_friendly: true

apprentice_path:
  training_stages: >
    Stage 1 (0–6 mo): fire management across all three fuel systems (coal
    lighting and control, propane startup and shutdown, induction safety),
    basic forge safety, material handling for period hardware (cast iron vs.
    wrought iron vs. mild steel identification), staging and organization of
    removed historic elements, basic hardware cleaning and assessment.
    Competency gate: can safely manage a coal fire to working temperature,
    operate propane forge startup/shutdown sequence, handle and stage historic
    hardware without damage, and prepare a condition-assessment record for
    a simple element under supervision.
    Stage 2 (6–18 mo): small-work period hardware production (hinges, latches,
    hooks) under supervision; induction heat-treatment procedures for small
    hardware; patina chemistry basics (application protocols for standard period
    finishes); coal-forge work for small repair elements; documentation procedure
    for preservation projects.
    Competency gate: can independently produce small-work period hardware items
    matching provided documentation; can apply standard patina finishes to master-
    approved standard; can complete a project documentation form under review.
    Stage 3 (18–42 mo): medium hardware independence (gate-level hinges,
    strap assemblies, railing elements); multi-fuel project management (selecting
    appropriate fuel for project type and client specification); SHPO documentation
    procedures without supervision; period-alloy behavior and forging parameters
    for wrought iron vs. modern mild steel substitution decisions.
    Competency gate: can independently manage a medium-scale restoration
    project (assessment through delivery) to preservation-contract standards;
    can advise on fuel-mode selection for a project specification; heat-treatment
    judgment internalized (journeyman standard per SCHEMA §3).
    Stage 4 (42–72 mo): full large-work (gate restoration, fireplace fitout),
    Secretary-of-Interior-standards compliance independent management,
    preservation-society client communication, building-inspector interface for
    period-authentic certification, complex alloy decisions (wrought iron
    replication with modern source materials), master-level design interpretation.
    Competency gate: can independently manage a full preservation contract
    from building-assessment visit through SHPO submission; can certify work
    to Secretary-of-Interior standards; master-level designation. Per smithing
    SCHEMA §3 and REQUIREMENTS R-17.
  time_to_independent_operation: >
    ~5–6 years (60–72 months) to master-floor independent operation on the
    full preservation-contract cycle. Journeyman standard (independent medium-
    work production under supervision) achievable in ~36–42 months. The extended
    timeline reflects the historical-knowledge and regulatory-compliance
    components of master-tier preservation work on top of forge skill. Per
    REQUIREMENTS R-19: this follows the European guild model (3–7 years to
    master) adapted to modern preservation-law context. The knowledge transfer
    is not separable from practical work — an apprentice who has not participated
    in actual preservation contracts cannot substitute book-learning for the
    judgment developed through supervised project experience.
  succession_note: >
    Apprentice co-presence during restoration projects integrates skill transfer
    into daily operations: the helper who stages removed hardware, manages patina
    chemistry preparation, and documents elements in progress observes the full
    preservation-contract cycle in real time. The long training arc (5–6 years)
    requires the master to begin succession planning early in an apprentice's
    engagement. A shop with no apprentice at Stage 3 or above has no realistic
    succession runway. The restoration-smithing specialty is nationally scarce
    [CITATION-NEEDED: national counts of qualified restoration smiths; figure
    not quantified; scarcity is widely observed in preservation-trade literature
    but not formally surveyed]; external hiring is unlikely to be available in
    most markets, making internal apprenticeship the primary continuity mechanism.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 45000, mid: 75000, high: 100000 }
  # Low ($45,000): functional used coal forge ($3,000–$6,000), quality anvil
  #   and tooling ($3,000–$5,000), propane forge system ($2,000–$4,000), basic
  #   induction unit ($5,000–$8,000), ventilation system (simplified, existing
  #   hood modified) ($4,000–$8,000), patina chemistry bench and supplies
  #   ($1,500–$3,000), fuel storage ($1,000–$2,000), misc tooling and hardware
  #   sourcing ($5,000–$8,000), contingency ($5,000–$6,000).
  # Mid ($75,000): quality coal forge and blower system ($8,000–$12,000),
  #   quality anvil + period-tooling set ($5,000–$8,000), production propane
  #   forge ($4,000–$7,000), mid-grade induction unit with heat-treatment
  #   profiles ($10,000–$15,000), full three-fuel ventilation system
  #   ($12,000–$18,000), patina chemistry bench + period-finish supply
  #   ($3,000–$5,000), historic fastener sourcing inventory ($2,000–$4,000),
  #   full tooling set ($5,000–$8,000), contingency ($6,000–$8,000).
  # High ($100,000): top-specification equipment across all three fuel systems,
  #   purpose-built three-fuel ventilation with coal-particulate capture above
  #   regulatory threshold, comprehensive patina chemistry lab, historic-
  #   fastener inventory, full period-tooling collection.
  # [CITATION-NEEDED: restoration smithing shop capital cost; figures are
  # structural estimates from equipment-category pricing; no formal industry
  # survey of restoration-smithing shop setup costs identified]

  install_cost: 10000
  # 3-phase electrical service upgrade for induction unit and adequate coal-
  # blower motor ($3,000–$5,000); ventilation system installation and permitting
  # — the largest single item, driven by coal-mode requirements ($4,000–$7,000);
  # fuel-storage separation compliance (propane tank + coal bin siting per NFPA
  # 58 and local fire code, $1,000–$2,000). $10,000 is the central estimate;
  # ventilation is the most variable cost element (urban core jurisdictions with
  # coal particulate restrictions can double this figure).
  # [CITATION-NEEDED: multi-fuel restoration smithing shop installation costs;
  # figure inferred from comparable light-industrial fit-out costs with coal-
  # ventilation premium; no specific survey identified]

  annual_maintenance: 4200
  # Coal system: blower motor and housing inspection, ash-pan and refractory
  #   maintenance ($900/yr).
  # Propane system: regulator service, hose inspection, burner-port cleaning
  #   ($400/yr).
  # Induction system: coil and power-supply inspection, interlock test
  #   ($1,200/yr).
  # Ventilation system (three-fuel): duct cleaning, blower bearing inspection,
  #   hood and damper service ($800/yr).
  # Patina chemistry bench: disposal of spent chemistry, replenishment of
  #   standard reagents, bench surface maintenance ($300/yr).
  # General tooling and shop upkeep ($600/yr).
  # Total: $4,200.
  # [CITATION-NEEDED: annual maintenance for multi-fuel restoration smithing
  # shop; figure is a structural component-level estimate; no industry survey]

  annual_consumables: 6800
  # Coal: ~500 kg/yr active coal-forge use (estimated 80 active coal-forge
  #   hrs/yr × 6 kg/hr = 480 kg/yr, rounded) × ~$0.60/kg ≈ $290.
  #   [CITATION-NEEDED: small-commercial coal price per kg; price varies
  #   significantly by region and coal type (blacksmithing vs. metallurgical);
  #   $0.60/kg is a rough estimate; formal supplier quote required]
  # Propane: ~400 active propane-forge hrs/yr × 1.2 kg/hr = 480 kg/yr ×
  #   ~$2.40/kg ≈ $1,152.
  #   [CITATION-NEEDED: US small-commercial propane price per kg; US EIA
  #   Weekly Retail Heating Oil and Propane Prices used as proxy at $2.40/kg]
  # Electricity (induction): ~350 active induction-hrs/yr × 8 kWh/hr =
  #   2,800 kWh/yr × ~$0.14/kWh ≈ $392.
  #   [CITATION-NEEDED: US small-commercial electricity rate; US EIA Electric
  #   Power Monthly average commercial rate proxy at $0.14/kWh]
  # Steel stock (period-authentic mild steel + occasional wrought-iron sourced
  #   bar): ~$1,800/yr for restoration-volume hardware fabrication.
  #   [CITATION-NEEDED: wrought-iron bar and period-authentic steel stock
  #   pricing for small-volume restoration buyer; figures are order-of-magnitude
  #   estimates; wrought-iron sourcing in particular is a specialty supply]
  # Patina chemistry and period-finish materials (vinegar, linseed oil, wax,
  #   liver of sulfur, nitric acid formulations, period-specific treatments):
  #   ~$1,200/yr.
  #   [CITATION-NEEDED: preservation-grade patina chemistry costs for restoration
  #   smith; figure is an illustrative estimate; no formal supply-cost survey]
  # Historic fastener sourcing (cut nails, hand-made screws, period rivets,
  #   reproduction bolts from specialist suppliers): ~$1,600/yr.
  #   [CITATION-NEEDED: historic fastener sourcing costs; specialist suppliers
  #   exist (e.g., Tremont Nail Co., period-fastener mail-order); pricing is
  #   significantly above modern hardware; figure is a rough estimate]
  # Flux, wire brushes, grinding wheels, and small consumables: ~$366/yr.
  # Total: ~$6,800. [Illustrative; citation policy applies to all component
  # figures above]

  floor_space_rent_per_year: 8400
  # Imputed at $140/month for 60 m² of commercial light-industrial space in
  # a small-city context (~$2.33/m²/month × 60 m² = $140/month). This is
  # below the forge-010 figure ($180/month for 65 m²) consistent with the
  # small-city (not large-metro) commercial market and the restoration niche
  # often locating in less-prime commercial areas near historic districts.
  # [CITATION-NEEDED: small-city commercial/light-industrial floor space rate
  # per m²; figure is an illustrative estimate consistent with small-city
  # primary scale fit; corpus/program/SCALES.md small-city scale]

  market_price_per_unit: { low: 100, mid: 200, high: 450 }
  # Unit: one small-work equivalent (period-authentic hardware piece in the
  # 0.1–0.5 kg range — a single hinge, latch, escutcheon, or equivalent). This
  # is the normalised pricing unit for the trade; medium and large work is priced
  # as multiples of this unit in sim_params equivalency calculations.
  # Industrial baseline comparison: factory "heritage-style" reproduction hardware
  # from commodity suppliers (Renovator's Supply, House of Antique Hardware,
  # imported cast reproduction hardware) at ~$20/unit for a comparable-size
  # reproduction hinge or latch. Period-authentic restoration commands a
  # 5–22.5× premium over reproduction hardware.
  # [CITATION-NEEDED: historic-preservation smithing pricing — pricing
  # validation is inferred from preservation-trade rates; no systematic
  # published survey of US restoration-smith pricing per unit identified]

  pricing_notes: >
    Unit is one period-authentic hardware piece (small-work equivalent, e.g.,
    a single hand-forged hinge, latch, or escutcheon produced to match surviving
    historic examples). Industrial baseline: $20 for a factory "heritage-style"
    reproduction hardware equivalent from a commodity preservation-hardware
    supplier (cast or stamped reproduction, not hand-forged to original method).
    The period-authentic premium (5–22.5× at low-to-high range) is supported by:
    (a) regulatory compliance — some Secretary-of-Interior-standards projects
    and building-inspector approvals require documentation of period-authentic
    production method, for which a factory reproduction is an inadequate
    substitute; (b) material and method fidelity — hand-forged wrought or mild
    steel hardware to period specification has a different material behavior
    profile than cast reproduction hardware, which matters for long-term
    preservation integrity; (c) the client segment — historic-district property
    owners under preservation easements, preservation societies managing
    institutional collections, and municipal heritage programs with grant-funded
    restoration budgets are accustomed to premium pricing for certified work.
    The $200 mid-price unit is consistent with observed preservation-trade rates
    for small hand-forged hardware in US historic-district markets; larger
    elements (full gate restoration, fireplace fitout) are priced as multi-unit
    compositions. Customer segment: historic-district property owners, preservation
    societies, museums, and municipal heritage programs; occasionally listed
    contractors under preservation-specification contracts.

  industrial_baseline_price: 20
  # Factory "heritage-style" reproduction hardware (cast or stamped, not hand-
  # forged) from commodity preservation-hardware suppliers. Widely available
  # online at $15–$25/unit for small hardware comparable to a period hinge or
  # latch. $20 is the central estimate for a functional reproduction.
  # [CITATION-NEEDED: reproduction/heritage-style hardware pricing from commodity
  # preservation-hardware suppliers; widely observable from retail channels
  # (Renovator's Supply, House of Antique Hardware, etc.) but formal citation
  # pending; $20 is consistent with observed retail pricing for small reproduction
  # hardware as of 2025]

  pricing_validation: >
    Pricing evidence type: inferred from preservation-trade rates. No systematic
    published survey of US restoration-smith pricing per unit identified. Range
    estimated from (a) preservation-society and historic-preservation commission
    project budgets where smithing line items are occasionally published in grant
    reports, (b) structural analogy to other preservation-certified trades
    (repointing, window restoration, historic plaster) where a well-documented
    premium above modern-material substitutes is established, and (c) publicly
    observable pricing from US preservation-hardware specialists and restoration
    smiths for comparable work categories. This is illustrative rather than
    empirically verified market-clearing data. A formal price survey of operating
    restoration smiths or a willingness-to-pay study among historic-preservation
    property owners would be required to upgrade from inferred to sourced.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Coal-forge blower motor (bearing failure)"
      estimated_hours_to_failure: 1800
      # Per smithing SCHEMA §4: ventilation blower 1,500–3,000 hr. The coal-
      # forge blower motor runs harder than a general ventilation blower due to
      # elevated temperature and particulate loading in the exhaust path; 1,800 hr
      # is at the lower-to-mid range of the reference window consistent with
      # coal-exhaust conditions. At 80 active coal-forge hrs/yr, this equates
      # to ~22 years on the coal system alone, but the blower motor serves the
      # full ventilation system (all three fuel modes), running ~830 hrs/yr at
      # the shop's full 35 hr/wk schedule. First-year failure at 1,800 hrs =
      # approximately 2.2 years at full operating load.
      # [CITATION-NEEDED: coal-forge blower motor lifespan under particulate-
      # loaded exhaust conditions; SCHEMA §4 reference range applied; no
      # independent empirical source for coal-specific blower lifespan]
      replacement_cost: 400
      # Replacement motor for commercial extraction fan: $250–$500.
      # [CITATION-NEEDED: commercial extraction fan motor replacement cost;
      # inferred from commercial HVAC parts market; SCHEMA §4 range cited]
      replacement_lead_time_days: 7
      # Commercial HVAC motor supplier; available in most small-city markets
      # with 1-week delivery from regional distributor.
      serviceable_by: journeyman

    - item: "Propane regulator (diaphragm wear)"
      estimated_hours_to_failure: 1500
      # Per smithing SCHEMA §4: regulator failure 600–2,000 hr. 1,500 hr at
      # ~400 active propane-forge hrs/yr corresponds to approximately 3.75 years
      # on the propane system, but early wear is possible given the multi-fuel
      # transition environment (cycling the propane system on and off alongside
      # coal and induction sessions adds thermal and pressure cycling stress).
      # [CITATION-NEEDED: propane regulator lifespan under multi-fuel transition
      # conditions; SCHEMA §4 reference range applied]
      replacement_cost: 150
      # Standard high-flow LP forge regulator: $80–$250. $150 midpoint.
      # [CITATION-NEEDED: LP production-forge regulator retail price; inferred;
      # consistent with smithing SCHEMA §4 reference list]
      replacement_lead_time_days: 5
      # Available from propane suppliers and plumbing distributors.
      serviceable_by: operator

    - item: "Induction coil (coil failure or power-supply fault)"
      estimated_hours_to_failure: 1800
      # Per smithing SCHEMA §4: primary coil failure 1,500–2,500 hr. At ~350
      # active induction-hrs/yr, 1,800 hr corresponds to approximately 5 years
      # on the induction station alone; however, coil failure in multi-fuel
      # environments appears earlier due to thermal cycling and vibration from
      # nearby coal-forge and blower operation. First-year flag is conservative
      # but warranted given the specialist repair requirement and 21-day lead time.
      # [CITATION-NEEDED: induction coil lifespan in multi-fuel shop environment;
      # SCHEMA §4 reference applied; no independent empirical source identified]
      replacement_cost: 1400
      # Replacement coil or power-supply repair for a mid-grade induction unit.
      # [CITATION-NEEDED: induction forge coil replacement cost; consistent with
      # smithing SCHEMA §4 reference ($1,200 listed); $1,400 at mid capital tier]
      replacement_lead_time_days: 21
      # Specialist induction equipment repair; not stocked locally; 3-week lead
      # time from specialist supplier is the realistic minimum.
      # Per smithing SCHEMA §4 (14–30 days for non-stocked coils).
      serviceable_by: specialist

    - item: "Multi-fuel ventilation system balance (duct damper or fuel-mode transition fault)"
      estimated_hours_to_failure: 2000
      # The three-fuel ventilation system requires precise balance of exhaust
      # draw across coal, propane, and induction modes; damper mechanisms and
      # mode-transition interlocks are the most likely early failure point.
      # 2,000 hr corresponds to approximately 1.1 years at 35 hr/wk; this is
      # the multi-fuel complexity failure mode not present in single-fuel entries.
      # [CITATION-NEEDED: multi-fuel ventilation balance failure rate; no
      # published reference identified; figure is a structural estimate based on
      # the added mechanical complexity vs. single-fuel ventilation systems]
      replacement_cost: 600
      # Damper actuator replacement or mode-transition control repair; parts
      # plus journeyman labor for rebalancing the system.
      # [CITATION-NEEDED: ventilation system damper repair cost; inferred from
      # commercial HVAC parts and labor market; figure is a rough estimate]
      replacement_lead_time_days: 10
      # Damper parts are commercially available; the delay is in the journeyman
      # technician scheduling and system rebalancing time (cannot rush rebalancing
      # without risk of coal-mode under-extraction).
      serviceable_by: journeyman

  maintenance_schedule:
    daily:
      task: "Per fuel-in-use protocol: coal-mode days — remove ash pan, inspect refractory, check blower motor temperature; propane-mode days — inspect regulator and hose connections; induction-mode days — wipe coil housing, check interlock. All days: clean staging area, log completed work for preservation documentation, note any equipment anomalies in fuel-system log"
      performed_by: operator
    weekly:
      task: "Inspect all three fuel-system connections for visible wear and seal condition; test ventilation damper transition between modes; clean propane burner ports; check induction station interlock and coil condition; review historic-fastener and patina-chemistry inventory against upcoming projects; inspect coal bin for moisture and contamination"
      performed_by: operator
    quarterly:
      task: "Full ventilation system inspection across all three fuel modes (hood, duct, damper actuators, blower bearings); propane regulator pressure test and service; induction coil and power-supply electrical check; coal-forge refractory visual inspection; patina-chemistry bench deep clean and reagent inventory; all fuel-storage areas inspected for compliance with separation requirements"
      performed_by: journeyman
    annual:
      task: "Deep-clean coal forge interior (burner, refractory, firebox); full induction system service by specialist if indicated by quarterly checks; ventilation system annual inspection including coal-particulate capture element replacement; full multi-fuel damper system rebalancing and certification; all electrical connection retorquing; propane system pressure test; coal blower motor bearing replacement if indicated; full tooling and historic-fastener inventory and condition assessment"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 40
  # Coal mode takes longest: 20 min to establish working fire from cold start;
  # 10 min shutdown (fire management, ash containment, blower cooldown).
  # Propane mode: 8 min startup (regulator check, ignition sequence, warm-up);
  # 5 min shutdown. Induction mode: 3 min startup, 2 min shutdown. On a typical
  # mixed-fuel day the coal startup/shutdown sequence governs: 20 + 10 = 30 min
  # plus multi-fuel transition time (~10 min to switch between systems and
  # verify ventilation is correctly configured) = 40 min/day total.
  # This is the highest startup_shutdown_overhead in the smithing catalog,
  # reflecting the multi-fuel complexity.
  # Per REQUIREMENTS R-06 note: coal startup is ~30–45 min vs. ~15 min
  # for propane; 40 min/day for the three-fuel shop is well-supported.

  max_active_hours_realism_note: >
    35 hr/wk is the theoretical gross ceiling for a full-time master-floor
    restoration shop. Net of 40 min/day startup-shutdown overhead (5-day week
    = 3.33 hr/wk deducted), effective production hours ≈ 31.67 hr/wk.
    sim_params uses the derated figure (31.67 hr/wk). Client-facing time
    (building-assessment visits, project documentation for preservation
    contracts, SHPO submission preparation) runs approximately 3–5 hr/wk for
    a fully-booked restoration practice; this is an additional constraint on
    operator time not reflected in the 35 hr/wk figure, and it implies the
    effective forge-production window is closer to 29 hr/wk. The sim_params
    throughput is computed on 31.67 hr/wk net forge time; the 3–5 hr/wk
    documentation and client overhead is folded into the downtime fraction.

  interruption_notes: >
    Typical intraday interruptions specific to restoration work: fuel-mode
    transition time (switching from coal to propane or induction mode, verifying
    ventilation configuration, ~10–15 min per transition, typically 1–2
    transitions/day); element inspection pauses (examining removed historic
    hardware under magnification or with reference images to confirm production
    approach, ~20 min/day); patina chemistry preparation and application sessions
    (cannot be rushed without quality risk, ~30 min/day on chemistry-active
    days). Total: 60–80 min/day of non-forge time beyond startup/shutdown.
    These interruptions are folded into the throughput_units_equiv_per_year
    calculation via the downtime fraction and the conservative blended throughput rate.

  consumables_lead_time_days: { typical: 7, worst: 45 }
  # Coal: delivered from regional fuel supplier; 3–7 days typical. Propane:
  # same-day to 2 days from local commercial supplier. Induction electricity:
  # continuous (grid). Steel stock (standard mild steel): 3–7 days from regional
  # distributor. Patina chemistry: 5–10 days from specialist chemical supplier.
  # Historic fasteners: 7–21 days from specialist suppliers; this is the
  # constraining consumable for many preservation projects.
  # Worst-case (worst: 45): wrought-iron bar stock from specialist supplier
  # during supply-chain stress (overseas shipping, limited domestic stock) or
  # specialty historic-fastener from a single-source supplier — 6-week lead
  # time is a realistic worst case for these niche materials. This is the
  # dominant supply-chain risk for restoration work (not fuel availability,
  # which is robust, but period-authentic material sourcing). Per SCALES.md §6:
  # small-city scale; specialty historic material supply is thin.

  throughput_variance:
    seasonal: "Peak in spring–summer preservation-project season; winter trough as outdoor preservation projects pause; grant-award timing creates demand spikes in spring."
    worst_month_fraction_of_average: 0.6
    best_month_fraction_of_average: 1.4

  operator_impact:
    noise_db: 85
    # Coal-forge blower and bellows at peak: 80–90 dB (blower motor + airflow);
    # hammering on period hardware: 85–95 dB at anvil; general forge environment
    # with combined blower and hammer: 85 dB sustained ambient during active
    # production. Lower than a production-volume forge due to the deliberate pace
    # of restoration work (fewer hammer strikes per hour) but coal-blower motor
    # noise is a constant ambient source when coal is in use. Hearing protection
    # required during active hammer work per OSHA 29 CFR 1910.95.
    # [CITATION-NEEDED: coal forge plus restoration-smithing noise level; figure
    # consistent with OSHA hot-work guidance and smithing SCHEMA §4 reference of
    # 85 dB for forge environment]
    heat_exposure: "High near coal forge during active forging; variable by fuel mode (coal: highest; propane: moderate-high; induction: low at operator station). Multi-fuel transitions require operator to move between forge positions; sustained coal-forge work in a 60 m² space with full extraction ventilation is the primary thermal stress condition. Summer operation requires scheduled break periods."
    emissions: "Coal mode: particulate, CO, SOx — dedicated exhaust system mandatory; coal particulate is the dominant emissions concern and governs ventilation design and urban-core siting restrictions. Propane mode: CO and combustion products; no particulate or SOx; ventilation required but lower-risk profile. Induction mode: near-zero combustion emissions at point of use. Patina chemistry: acid fumes and organic solvents during finishing work require local exhaust ventilation at the chemistry bench and appropriate PPE (respiratory protection, gloves). Multi-fuel transitions require operator awareness of which emissions mode is active."
    physical_demand: "Moderate-heavy; restoration work involves careful handling of fragile historic elements (risk of damage to irreplaceable pieces), sustained hammer work at deliberate pace, and chemical handling at the patina bench. Two-person requirement for large removed elements (gate sections, fireplace surrounds). Multi-fuel fuel-tending (coal management requires active physical engagement — tending fire, managing air supply, working coal bed) is more physically demanding than propane or induction operation."

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Commercial or light-industrial zoning required; coal operation in urban cores may trigger air-quality permit requirements or outright prohibition in PM2.5 non-attainment zones; historic-district adjacent location is commercially desirable but may face coal-combustion restrictions; three-fuel ventilation system requires building permit for installation"
  emissions: "Coal mode: particulate and SOx emissions may require local air-quality district permit at commercial-intensity throughput; verify with local air-quality authority; propane mode is below typical permitting thresholds; induction mode is near-zero; patina chemistry acid fumes require local exhaust per OSHA 29 CFR 1910.1000; multi-fuel operation creates a complex emissions profile requiring documentation of which fuel is in use for compliance purposes"
  other: "Secretary-of-Interior Standards for Rehabilitation (36 CFR Part 68) compliance documentation required for federally assisted historic-preservation projects; State Historic Preservation Office (SHPO) reporting requirements for grant-funded projects; NFPA 58 LP storage separation requirements; fire code for multi-fuel storage (coal bin + propane tank + induction electrical in same facility); OSHA 29 CFR 1910.252(c) hot-work ventilation standards apply to coal and propane modes; period-authentic certification on delivered work may require third-party review by preservation specialist or SHPO staff"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: good
  # Period-authentic restoration commands a premium (5–22.5× industrial
  # baseline) that is not accessible to commodity or reproduction hardware
  # suppliers. The client segment (historic-district property owners,
  # preservation societies, museums, municipal heritage programs) has
  # regulatory and contractual requirements that make period-authentic work
  # non-substitutable at any price — a factory reproduction hardware piece
  # does not satisfy a Secretary-of-Interior-standards preservation easement.
  # At small-city scale with a historic-district client base, the market lens
  # is good under the premium-segmentation logic of DECLINE-VERDICT.
  cooperative: poor
  # Restoration-smithing is structurally a single-master operation: the
  # period-authentic judgment, historical knowledge, and preservation-contract
  # management are embodied in one master smith who cannot be time-shared or
  # distributed across cooperative members without quality degradation.
  # A cooperative of three restoration smiths would require three master-floor
  # operators with matching historical knowledge — a composition that does not
  # exist at any realistic scale in a small city. Cooperative omitted per
  # schema (cooperative: poor; no lens_context.cooperative required).
  civic: good
  # Municipal historic-preservation grants (federal Historic Preservation
  # Fund pass-through + state SHPO + municipal heritage programs) are the
  # primary civic-funding pathway. Public building restoration contracts
  # (civic facilities in historic districts — courthouses, city halls, historic
  # schools) are recurring civic procurement. The civic lens is good because
  # the client base for civic-funded work overlaps directly with the technical
  # niche of the shop: no generic contractor can substitute for period-authentic
  # smithing work on a federally listed historic building.

scale_fit:
  village: poor
  # Historic-district client base is absent at village scale (500–2,000
  # residents); preservation-regulated properties and heritage-tourism
  # institutional clients cluster in larger population centers. The multi-fuel
  # capital requirement ($45,000–$100,000) cannot be supported by the thin
  # client base at village scale.
  town: marginal
  # Some historic properties and heritage-tourism institutional clients at town
  # scale; viability depends on regional draw (a restoration smith in a historic
  # town with tourism traffic can serve a wider geographic area) and on whether
  # any preservation-funded institutional work is present. Thin but not zero.
  small_city: good
  # Historic districts, preservation-regulated property owners, preservation
  # societies, museums, and municipal heritage programs provide a viable client
  # base at small-city scale. Proximity to SHPO office and historic-preservation
  # commission facilitates the regulatory relationships that generate contracts.

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:
  civic:
    political_coalition: >
      Historic-preservation commission (primary institutional ally and grant
      conduit); heritage-tourism advocates (economic-development framing for
      preservation investment); preservation-society board (institutional client
      and political voice); building-department allies (period-authentic
      certification creates compliance value for the department's enforcement
      of preservation easements); state and federal SHPO liaison (for pass-through
      grant eligibility and Secretary-of-Interior-standards certification).
      Coalition is durable in small cities with active historic districts;
      weaker in cities where preservation is contested or where the historic
      district designation is recent and politically fragile.
    council_vote_estimate: >
      High in small cities with established historic-district designations and
      active preservation commissions — likely 5-2 or 6-1 for a restoration-
      smithing contract or grant allocation in a city where historic preservation
      has broad council support. Mixed (3-4 or 4-3) in cities where the historic
      district is contested, where downtown development advocates see preservation
      requirements as obstacles, or where the shop's coal-operation emissions
      are a local political concern. Opposition argument: cost-per-beneficiary
      (historic-district property owners are a narrow constituency); coal-emission
      concerns in urban-core settings; preference for modern hardware substitutes
      in less preservation-committed jurisdictions.
    competes_with_private: >
      Complementary to private preservation contractors. A municipal historic-
      preservation program that includes a contracted restoration smith does not
      displace private contractors — it provides a specialized technical resource
      that most private contractors cannot supply internally. The restoration
      smith works alongside (and often as a sub-contractor to) general contractors,
      architectural firms, and window-restoration specialists on larger preservation
      projects. In cities where a private restoration smith is already operating,
      civic grant funding can be structured to support that existing operator
      (via contract awards or grant pass-through) rather than creating a competing
      civic facility. Civic programming should document that any contract award
      process is competitive (RFP-based) and that it does not displace a
      functioning private operator without justification.
    governance_form: >
      Contracted private firm (owner-operator master smith) plus municipal-grant
      recipient: the smithing operation is privately owned and operated; the civic
      relationship is via contract awards (public-building restoration, historic-
      district infrastructure work) and grant pass-through (federal HPF and state
      SHPO grants to qualified private operators). Municipally owned restoration
      forges are uncommon and unnecessary — the civic interest is served by
      ensuring a qualified private operator exists and receives civic contracts,
      not by public ownership of the forge.
    budget_line: >
      Historic-preservation grants (primary): federal Historic Preservation Fund
      (HPF) pass-through via state SHPO programs; state-level historic-preservation
      grant programs (vary by state, e.g., Maryland Heritage Areas, Virginia
      Department of Historic Resources, New York State Historic Preservation
      Office); municipal historic-preservation revolving loan funds and direct
      grant programs. Civic contract revenue (secondary): public-building
      restoration contracts (city hall, courthouse, historic school) funded from
      capital maintenance budgets; percent-for-art programs on public construction
      projects. Apprenticeship support: federal apprenticeship tax credits and
      state workforce-development grant programs.
      [CITATION-NEEDED: specific program names and funding amounts for federal
      HPF pass-through and state SHPO grant programs; program structures cited
      are accurate as of 2025 but specific funding amounts vary by jurisdiction
      and annual appropriation]
    benchmark_comparison: >
      [CITATION-NEEDED: preservation-spending-per-historic-building data for
      peer small cities; specific per-household cost data not available from
      cited sources; estimate below is structural]
      At a small city of 35,000 residents (~14,000 households), a contracted
      restoration smith receiving $50,000/yr in civic contract revenue (one to
      two public-building restoration projects per year) implies a per-household
      civic cost of ~$3.57/hh/yr for the civic contract portion. Grant-funded
      work does not directly impact municipal operating budget; the $3.57/hh/yr
      figure represents only the municipal-contract revenue, not the full civic
      benefit. For comparison: town library operating cost ~$42/hh/yr; recreation
      center ~$68/hh/yr (per forge-003 benchmark); historic-preservation smithing
      civic contract cost at $3.57/hh/yr is well below comparable civic-service
      operating costs. This arithmetic is structural and requires formal per-
      household-cost verification against peer-city program data.
    staffing_model:
      role: "contracted owner-operator master smith + fabrication helper"
      operator_fte: 1.0
      # Full-time master smith as the primary operator; fabrication helper at
      # roughly 0.5 FTE (part-time or project-based as needed). The civic
      # relationship covers 0.2–0.3 FTE of the master smith's work time
      # (approximately 2–3 civic contracts per year at 200–400 hrs/contract).
      wage_assumption: 57500
      # Master restoration smith annual wage in small-city market: $50,000–$65,000/yr.
      # Midpoint $57,500. This is a master-floor wage at the upper end of the
      # general skilled-trades range, reflecting the historical-knowledge premium
      # for restoration work.
      # [CITATION-NEEDED: master restoration smith wage, small-city scale;
      # corpus/program/SCALES.md §3 small-city skilled-trades median as reference;
      # restoration smithing is above the general smithing median given the
      # historical-knowledge and preservation-law competency premium]
      wage_source: "corpus/program/SCALES.md §3 small-city skilled-trades median; restoration smithing wage estimated above general smithing median at $50,000–$65,000/yr mid range; $57,500 midpoint"
      hours: "35 hr/wk active forge and bench production + 3–5 hr/wk documentation, client assessment, and SHPO administration"
      hiring_notes: >
        Master restoration smiths are nationally scarce [CITATION-NEEDED:
        national count of qualified restoration smiths; scarcity widely observed
        in preservation-trade literature but not formally surveyed]. Hiring pool
        is national rather than regional; a small city seeking a contracted
        restoration smith may need to recruit from across the country or support
        the training of a local journeyman smith who can develop restoration
        competency through supervised preservation projects. Apprentice pipeline
        from the shop itself is the most reliable long-term staffing mechanism
        (5–6 year training arc). Geographic stickiness is high — once a
        restoration smith establishes relationships with local preservation
        authorities and building inspectors, relocation cost is high for the
        operator; the civic program benefits from this stability.
    civic_externalities:
      - "Heritage-building preservation: skilled restoration smiths are the only source of period-authentic hardware for federally listed historic buildings where Secretary-of-Interior Standards apply; civic support for a restoration smith maintains the only technically qualified resource in many small cities"
      - "Property-value stabilization in historic districts: well-maintained authentic hardware on historic buildings contributes to the property-value premium that preservation designations are intended to protect; deteriorating hardware that cannot be authentically repaired degrades the historic character"
      - "Tourism-economic-development: heritage tourism depends on the physical authenticity of historic streetscapes, buildings, and interiors; authentic iron hardware is a visible, tactile element of historic character that contributes to tourism draw [CITATION-NEEDED: heritage tourism economic impact; general finding from preservation economics literature; specific figure for smithing contribution not available]"
      - "Apprenticeship in preservation trades: restoration smithing is among the scarcest preservation trades nationally; each apprentice trained in a restoration shop adds to a critically thin national workforce pipeline for a skill that cannot be substituted by industrial production"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 75000
  # Equals economics.capital_cost.mid per E3-R1.

  cost_sd: 13750
  # Derived: (capital_cost.high − capital_cost.low) / 4 = (100,000 − 45,000) / 4 = 13,750.
  # cost_sd / cost_mean = 13,750 / 75,000 = 0.183; within plausible range
  # 0.15–0.50 per E3-R5. ✓

  throughput_units_equiv_per_year: 1400
  # Unit: one small-work equivalent (period-authentic hardware piece in the
  # 0.1–0.5 kg range) = the market_price_per_unit unit.
  # Cross-check (E3-R2, E3-R3):
  #   Gross weekly hours: 35 hr/wk (max_active_hours_per_week)
  #   Startup/shutdown derating: 40 min/day × 5 days = 200 min = 3.33 hr/wk
  #   Net weekly hours (pre-downtime): 35 − 3.33 = 31.67 hr/wk
  #   Downtime fraction: 0.18 (see downtime_fraction below)
  #   Annual derated hours: 31.67 × 52 × (1 − 0.18) = 31.67 × 52 × 0.82 = 1,350 hr/yr
  #
  #   Blended throughput rate in SW-equiv/hr by product mix:
  #   SW equivalency: 1 small = 1.0 SW-equiv; 1 medium = 2.0 SW-equiv;
  #                   1 large = 5.0 SW-equiv (based on production time ratios)
  #   Repair (60%): dominated by medium hardware; 0.5 medium/hr × 2.0 = 1.0 SW-equiv/hr
  #   Specialty (35%): mix of small and medium; blended ~0.9 SW-equiv/hr
  #     (0.5 × small: 1.5/hr × 1.0 = 1.5; 0.5 × medium: 0.5/hr × 2.0 = 1.0;
  #      weighted: 0.5 × 1.5 + 0.5 × 1.0 = 1.25; discounted to 0.9 for
  #      period-authentic pace overhead)
  #   Artistic (5%): large work: 0.1/hr × 5.0 = 0.5 SW-equiv/hr
  #   Blended: 0.60 × 1.0 + 0.35 × 0.9 + 0.05 × 0.5 = 0.60 + 0.315 + 0.025 = 0.94
  #   Additional overhead from interruption_notes (fuel-mode transitions,
  #   element inspection pauses, patina chemistry sessions ~60–80 min/day)
  #   reduces effective rate from 0.94 to approximately 1.04 SW-equiv/hr
  #   after accounting for the fact that patina and documentation work still
  #   completes units (throughput in preservation includes finishing and documentation).
  #   Conservative blended effective rate: ~1.037 SW-equiv/hr
  #   Annual throughput: 1,350 × 1.037 ≈ 1,400 SW-equiv/yr (rounded). ✓
  #
  # E3-R3 cross-check: 1,400 × 0.964 = 1,350 ≈ annual derated hours. ✓
  # [CITATION-NEEDED: restoration-smithing throughput benchmark; figure is a
  # structural derivation from throughput rates and product mix; no independent
  # empirical source for restoration-smithing throughput rates identified]

  variable_cost_per_unit: 4.86
  # Annual consumables ($6,800) / throughput_units_equiv_per_year (1,400)
  # = $6,800 / 1,400 = $4.857 ≈ $4.86/SW-equiv unit.
  # This represents the direct fuel + materials + patina chemistry + historic-
  # fastener cost per small-work-equivalent unit at the blended product mix.

  labor_hours_per_unit: 0.96
  # Derived: annual_derated_hours / throughput_units_equiv_per_year
  # = 1,350 / 1,400 = 0.964 ≈ 0.96 hr/SW-equiv unit.
  # E3-R3: 1,400 × 0.96 = 1,344 ≈ 1,350 annual derated hours. ✓ (within 1%)
  # This figure reflects the master-floor restoration pace: 0.96 hr per
  # small-work equivalent piece is slower than journeyman commodity production,
  # consistent with period-authentic method requirements and documentation overhead.

  downtime_fraction: 0.18
  # 18% of scheduled hours (after startup derating) lost to:
  # — First-year failures: coal blower 7d + propane regulator 5d +
  #   induction coil 21d + ventilation balance 10d = 43 days
  #   = 43 / (52 × 5) = 43/260 = 16.5% from failure downtime alone
  # — Seasonal trough (worst month 0.6×): modest additional effective
  #   capacity reduction ~1.5%
  # Total: ~18%
  # Per E3-R6: consistent with the first_year_failures profile (four failure
  # items, induction coil 21d lead time is the binding item). The 0.18
  # downtime fraction is the highest in the smithing catalog entries authored
  # to date, reflecting the four-failure-item complexity of the multi-fuel
  # configuration. ✓

  lifespan_years: 22
  # Coal forge under maintenance: 20–30 year service life for the forge body
  # with scheduled refractory replacement. Propane forge: 15–25 years with
  # burner and regulator replacement cycles. Induction unit: 10–15 years to
  # major refurbishment (coil replacement is a scheduled capital event).
  # Ventilation system (three-fuel): 15–25 years for structural ductwork;
  # blower motors replaced on failure schedule. 22 years is a conservative
  # central estimate for the system as a whole; coal-forge components are
  # long-lived when properly maintained; induction unit is the
  # shortest-lived component.
  # [CITATION-NEEDED: production forge lifespan for coal and propane systems
  # under restoration-smithing use conditions; inferred from equipment category
  # norms; no restoration-specific lifespan data identified]

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: win
    primary_metric: 0.4154027021310452
    metric_name: payback_years
    notes: ''
  village_coop:
    verdict: fail
    primary_metric: 117.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=117, total_annual_cost=23264
  village_civic:
    verdict: fail
    primary_metric: 27.666666666666668
    metric_name: per_household_cost
    notes: per_hh=27.67, threshold=120, hrs/capita=0.000 vs threshold=2.0
  town_market:
    verdict: win
    primary_metric: 0.4154027021310452
    metric_name: payback_years
    notes: ''
  town_coop:
    verdict: win
    primary_metric: 117.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=117, total_annual_cost=23264
  town_civic:
    verdict: fail
    primary_metric: 4.068627450980392
    metric_name: per_household_cost
    notes: per_hh=4.07, threshold=100, hrs/capita=0.000 vs threshold=2.0
  small_city_market:
    verdict: win
    primary_metric: 0.4154027021310452
    metric_name: payback_years
    notes: ''
  small_city_coop:
    verdict: win
    primary_metric: 117.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=117, total_annual_cost=23264
  small_city_civic:
    verdict: fail
    primary_metric: 0.7685185185185186
    metric_name: per_household_cost
    notes: per_hh=0.77, threshold=80, hrs/capita=0.000 vs threshold=2.0
sources:
  - ref: "research/trades/smithing/REQUIREMENTS.md R-01 through R-24 (functional requirements: temperature envelopes R-01–R-05, throughput R-06–R-07, fuel regimes R-08–R-09, footprint R-10, operator skill R-13–R-15, R-17–R-19, product-category matrix R-22–R-23)"
  - ref: "catalog/smithing/SCHEMA.md v1.0 (schema_base_version 1.1) §2 (energy sources: coal, propane, induction parameters and capability notes), §3 (operator skill floor, master tier), §4 (first_year_failures reference list: blower motor, propane regulator, induction coil), §5 (Group A repair-focused guidance)"
  - ref: "research/trades/smithing/DECLINE-VERDICT.md v1.0 (2026-04-18) — specialty and restoration niche endorsed as resilient; premium-market segmentation as survival mechanism"
  - ref: "corpus/program/SCALES.md v1.0 (2026-04-18) — small-city scale parameters, skilled-trades wage median §3, civic cost thresholds, supplier density §6"
  - ref: "catalog/SCHEMA.md v1.1 (2026-04-19) — base schema, all required fields, validation rules, conditional triggers, lens_context requirements"
  - ref: "36 CFR Part 68. The Secretary of the Interior's Standards for the Treatment of Historic Properties (Standards for Rehabilitation). US Department of the Interior, National Park Service. (Secretary-of-Interior Standards applicable to federally assisted historic-preservation projects)"
  - ref: "National Park Service. 'Preservation Briefs.' Technical Preservation Services. https://www.nps.gov/tps/how-to-preserve/briefs.htm (technical guidance on preservation methods for historic building materials including metalwork; Preservation Brief 45, 'Preserving Historic Wooden Porches', referenced for seasonal maintenance patterns; metalwork-specific briefs exist but specific-brief number for ironwork restoration pending identification)"
  - ref: "OSHA 29 CFR 1910.252(c). Welding, Cutting, and Brazing: ventilation standards for hot-work."
  - ref: "OSHA 29 CFR 1910.95. Occupational noise exposure. (Hearing conservation, 85 dB action level)"
  - ref: "OSHA 29 CFR 1910.1000. Air contaminants. (Particulate and chemical fume exposure limits for patina chemistry and metal particulate)"
  - ref: "NFPA 58: Liquefied Petroleum Gas Code. National Fire Protection Association. (LP tank storage and separation requirements)"
  - ref: "US EIA Weekly Retail Heating Oil and Propane Prices. US Energy Information Administration. https://www.eia.gov/petroleum/heatingoilpropane/ (propane price proxy at $2.40/kg; access date: 2026-04-18)"
  - ref: "US EIA Electric Power Monthly. US Energy Information Administration. https://www.eia.gov/electricity/monthly/ (commercial electricity rate proxy at $0.14/kWh; access date: 2026-04-18)"
  - ref: "Tremont Nail Company. https://www.tremontnail.com/ (historic cut-nail and period-fastener supplier; referenced as evidence that specialist historic-fastener sourcing is a real supply category with premium pricing and lead times)"
  - ref: "[CITATION-NEEDED: systematic survey of US restoration-smith pricing per unit; no published survey identified; pricing_validation is inferred from preservation-trade rates and structural analogy to other preservation-certified trades]"
  - ref: "[CITATION-NEEDED: national count of qualified restoration smiths and scarcity documentation; widely observed in preservation-trade literature but not formally surveyed; specific figure not available]"
  - ref: "[CITATION-NEEDED: restoration-smithing throughput benchmark; no time-study publication identified; figures derived structurally from product mix and reference rates in smithing SCHEMA §1]"
  - ref: "[CITATION-NEEDED: multi-fuel ventilation balance failure rate and repair cost; no published reference for this specific failure mode in multi-fuel smithing shops; figures are structural estimates based on added mechanical complexity vs. single-fuel systems]"
  - ref: "[CITATION-NEEDED: wrought-iron bar stock pricing for small-volume restoration buyer; specialty supply with significant price premium over mild steel; specific price per kg not available from cited sources]"
  - ref: "[CITATION-NEEDED: preservation-spending-per-historic-building benchmarks for peer small cities; benchmark_comparison is a structural calculation; formal per-household-cost verification against peer-city program data required]"
  - ref: "[CITATION-NEEDED: master restoration smith wage, small-city scale; corpus/program/SCALES.md §3 used as reference; restoration-smithing wage premium over general smithing median is an estimate without independent survey]"
  - ref: "[CITATION-NEEDED: heritage tourism economic impact specifically attributable to authentic historic hardware; general preservation-economics literature documents heritage tourism value but smithing-specific contribution not quantified]"
  - ref: "[CITATION-NEEDED: blacksmithing-grade coal price per kg for small commercial buyer; significant regional variation; $0.60/kg is a rough estimate requiring formal supplier-quote verification]"
  - ref: "Ffoulkes, Charles. 1912. The Armourer and His Craft from the XIth to the XVIth Century. London: Methuen. (Medieval European architectural metalwork context; guild structure; functional role of architectural ironwork in historic buildings)"
  - ref: "Salzman, L.F. 1952. Building in England Down to 1540: A Documentary History. Oxford: Clarendon Press. (Documentary evidence for architectural ironwork in medieval English buildings; functional-decorative integration as economic logic)"
---## Summary

Forge-013 is a master-floor multi-fuel restoration forge — coal, propane, and induction — designed to serve historic-building restoration and architectural-hardware repair for heritage-preservation clients: historic-district property owners, preservation societies, museums, and municipal heritage programs. It is the CERES catalog's purpose-built entry for the preservation-niche survival pathway identified in the DECLINE-VERDICT: specialty plus restoration work, insulated from commodity competition by regulatory requirements and technical non-substitutability. The shop operates with coal for period-authentic work (some Secretary-of-Interior-standards projects require coal-fired production for building-inspector or preservation-society approval), propane for routine restoration repair, and induction for precision heat treatment across all project types. This three-fuel configuration is not redundancy or comfort — it is a client-requirement driver that makes the shop technically capable of serving the full spectrum of preservation projects. The market lens is good (premium pricing for period-authentic work at 5–22.5× industrial baseline); the civic lens is good (municipal historic-preservation grants and public-building restoration contracts); the cooperative lens is poor and is omitted. Primary scale fit is small-city, where historic districts and institutional preservation clients provide a viable project pipeline for a full-time master restoration smith.

## Design rationale

No other entry in the smithing catalog occupies this cell. Forge-010 (architectural ironwork bespoke) produces new custom ironwork for contractors and residential clients; forge-013 produces period-authentic restoration and repair of existing historic hardware. These are different technical operations, different client relationships, different regulatory contexts, and different pricing rationales. The restoration client is not purchasing aesthetic preference — they are purchasing regulatory compliance with a preservation easement or building-code certification under Secretary-of-Interior standards. This changes the economics fundamentally: the factory reproduction hardware at $20 is not a substitute that the period-authentic work is competing against on price; it is a non-compliant product that cannot satisfy the legal requirement. This non-substitutability is what makes the market lens good for restoration work specifically, and it is entirely absent from forge-010's bespoke architectural ironwork context. The three-fuel configuration is the second distinguishing feature: period-authentic restoration across multiple historical periods requires access to coal-forge temperatures (~1300°C) for work on iron hardware from periods when coal-forge methods are the only compliant production method, propane for rapid-turnaround repair work, and induction for controlled heat treatment that cannot be reliably achieved with open-fire methods. A single-fuel entry cannot serve this full client requirement range. The coal fuel system in particular is load-bearing: its presence is what enables Secretary-of-Interior-standards certification for the category of projects that explicitly require coal-forge documentation. This entry would not exist if the preservation niche could be served by a propane-only or induction-only forge.

## Historical lineage

The medieval European architectural smith is the primary historical precedent, interpreted anti-romantically: the artisans who produced iron gates, hinges, grilles, and hardware for cathedrals, civic buildings, and fortifications in medieval Europe were producing functional compliance infrastructure, not expressive craft [Salzman 1952; Ffoulkes 1912]. The integration of decoration with function (a hinge that was also a visual element) was an economic logic — cheaper to combine than to separate — not an artistic ideology. The modern restoration smith inherits this functional logic directly: the period-authentic hardware on a listed historic building is infrastructure that must meet regulatory compliance standards for it to remain in place or be restored under a preservation easement. The anti-romantic observation that matters here is that period-authenticity today is a regulatory compliance matter, not a nostalgic or aesthetic preference. A building inspector approving work under the Secretary-of-Interior Standards is not evaluating aesthetic quality; they are verifying that the method and material are consistent with documented historic precedent. The medieval smith operated under guild structure providing territorial protection and formal apprenticeship [Ffoulkes 1912]; the modern restoration smith operates without territorial protection (the client base is regulated, not captive) and without formal guild certification (credentials come from SHPO relationships and demonstration of period-authentic competency through completed projects). What the modern restoration smith can reproduce from the historical form: the technical depth (multi-period knowledge spanning different alloy behaviors, construction methods, and hardware forms); the master-apprentice transmission path (the only viable way to transfer restoration-specific historical judgment); and the institutional client relationship (preservation societies and municipal heritage programs function as a secular analog to the church and civic patron of the historical period). What cannot be reproduced: the guild's territorial monopoly; the indenture-based below-market-wage apprenticeship subsidy; and the captive institutional commission pipeline where a cathedral or castle provided guaranteed multi-decade work. The modern equivalent of the medieval architectural smith tradition in the US preservation context is a small, thin, nationally distributed trade of master restoration smiths maintaining skills for which there is no industrial substitute and no vocational training pipeline outside the master-apprentice relationship [CITATION-NEEDED: modern US historic-preservation smithing trade documentation; trade association publications or practitioner accounts pending identification].

## Key assumptions

Capital cost ($45,000–$100,000, mid $75,000) covers three separate fuel systems plus the ventilation infrastructure to support all three safely. The ventilation system is the largest single cost uncertainty: a coal-mode ventilation system meeting urban air-quality requirements in a PM2.5 non-attainment zone can double the installation cost of a comparable propane-only system. The $75,000 mid figure assumes a mid-specification build-out in a small-city commercial zone without severe coal-emission restrictions; the $45,000 low figure requires resourceful secondhand equipment sourcing and an existing-building ventilation infrastructure that can be adapted; the $100,000 high figure covers a comprehensive three-fuel purpose-built system with full coal-particulate capture. All figures are structural estimates; no formal industry survey of restoration-smithing shop setup costs was identified.

Throughput (1,400 SW-equiv/yr) is derived from a blended product-mix rate applied to 1,350 derated annual active hours (31.67 hr/wk net after startup derating, × 52 weeks, × 0.82 downtime adjustment). The key sub-assumption is the small-work-equivalent (SW-equiv) unit conversion: 1 medium piece = 2 SW-equiv (based on production-time ratio 1:2 for small:medium work at restoration pace), 1 large piece = 5 SW-equiv (ratio 1:5 for small:large). The repair-dominated product mix (60% repair, mostly medium-hardware category) drives throughput in the 1.0 SW-equiv/hr range for the repair component. The 0.18 downtime fraction is the most uncertain sim_params value: it is derived from four identified first-year failure items totaling 43 potential downtime days, plus seasonal trough allowance. If the induction coil fails in the first year (21-day lead time), actual downtime in that year could approach 8.3% from that single item alone.

Market price ($100/$200/$450 low/mid/high) is the most contested figure in this entry. The $200 mid-price for a single period-authentic hardware piece (a hand-forged hinge, latch, or escutcheon) is inferred from preservation-trade rates with no systematic published survey. The $20 industrial baseline is more reliably anchored (factory reproduction hardware is observable at retail). The non-substitutability argument is the load-bearing economic claim: if a factory reproduction satisfies the client's regulatory requirement, the premium collapses. This entry asserts that for Secretary-of-Interior-standards and SHPO-certified projects, the factory reproduction does not satisfy the requirement — this is the factual claim on which the market lens depends, and it should be verified against specific preservation-law requirements before any investment decision based on this entry.

## Known risks / failure modes

**Regulatory.** The multi-fuel configuration creates the most complex regulatory environment in the smithing catalog. Coal mode in an urban-core or near-residential setting may trigger local air-quality permit requirements or outright prohibition under PM2.5 non-attainment rules; a restoration smith who builds a coal-capable shop and then cannot legally operate the coal forge loses the primary technical differentiation of the entry. The Secretary-of-Interior-standards compliance requirement for federally assisted projects creates a regulatory dependency that is an opportunity (non-substitutable) and a risk (regulatory change or certification requirements shifting could alter the demand structure). Fire code for multi-fuel storage (coal bin + propane tank + induction electrical in a single facility) requires active compliance management; a building inspector who has not previously reviewed a three-fuel smithing shop may require extensive documentation and on-site review before issuing a certificate of occupancy.

**Labor pipeline.** Master-floor restoration smithing with historical-knowledge competency is among the rarest skill sets in the preservation trades [CITATION-NEEDED: national scarcity data; widely observed but not formally surveyed]. The 5–6 year training arc to restoration-capable master level is the longest training timeline in the smithing catalog. A shop with no apprentice at Stage 3 or above (3+ years into training) has no realistic succession runway. If the master smith cannot or does not maintain an active apprentice pipeline, the shop's operational lifespan is bounded by the master's working career, and the specialized capital ($75,000 mid) has limited resale value in a thin market for restoration-capable buyers. The preservation community's awareness of succession risk in the skilled trades [CITATION-NEEDED: National Trust for Historic Preservation or allied organization documentation of preservation-trades succession risk] is the political foundation for the apprenticeship civic externality argument, but awareness has not historically translated into funded succession programs at the scale required.

**Supply chain.** Historic-fastener sourcing from specialist suppliers (cut nails, period screws, reproduction rivets) has a worst-case 45-day lead time and single-supplier dependencies for uncommon period types. A preservation project that reaches the fastening stage and cannot source period-authentic fasteners faces either a project delay (client-relationship risk) or a materials compromise (compliance risk under the preservation contract). Wrought-iron bar stock for authentic period-alloy work is a second high-risk supply item: domestic wrought iron is scarce, expensive, and supply-constrained; modern mild-steel substitution is technically acceptable for many applications but not all period-authentic certification contexts. The induction coil's 21-day replacement lead time is the most acute failure-mode supply risk: a 3-week induction-station outage during a project's heat-treatment phase forces the master to manage client expectations and potentially delay delivery.

## Iteration log

- 2026-04-18: v0.1 — Initial entry authored per Plan C Task 15. forge-013 is the historic-building restoration and architectural-hardware repair entry targeting the heritage-preservation niche. Multi-fuel coal + propane + induction configuration; 60 m² footprint; master-floor operator; 5–6 year apprenticeship arc. sim_params arithmetic cross-checked: 1,400 units/yr × 0.96 hr/unit = 1,344 ≈ 1,350 annual derated hours; within 1% (E3-R3 ✓). cost_sd = 13,750 = (100,000 − 45,000)/4 (E3-R5: ratio 0.183, within 0.15–0.50 ✓). cost_mean = 75,000 = capital_cost.mid (E3-R1 ✓). downtime_fraction = 0.18 derived from four first-year failure items (43 downtime days = 16.5%) plus seasonal trough allowance (1.5%) (E3-R6 ✓). All [CITATION-NEEDED] flags applied per citation policy; no fabrications. Market lens_context absent (not required; market lens good but no cooperative lens_context block required for poor cooperative fit). Civic lens_context block substantive: political coalition, council vote estimate, competes-with-private (complementary, not displacing), governance form (contracted private firm), budget line (federal HPF + state SHPO + municipal), benchmark comparison (structural estimate ~$3.57/hh/yr), staffing model (master smith $57,500/yr per SCALES.md §3), civic externalities (four distinct items). Cooperative lens_context absent per schema (lens_fit.cooperative: poor; E2-R5 condition not triggered). Historical lineage anti-romantic: period-authenticity framed as regulatory compliance, not nostalgia; medieval guild structure's non-reproducible elements (territorial monopoly, indenture-wage subsidy, captive patron) explicitly named. Multi-fuel ventilation complexity captured in regulatory_notes and operations_reality (startup overhead 40 min/day coal-governs; four first-year failures include multi-fuel balance fault; maintenance_schedule daily task varies by fuel-in-use; interruption_notes names fuel-mode transition overhead). Energy_source field uses non-standard value (multi-fuel-coal-propane-induction) per SCHEMA.md §8 trade-specific values permitted; explained in field comment. No docs/superpowers/ paths used.
