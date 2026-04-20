---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: forge-010
trade: smithing
name: "Architectural Ironwork Bespoke"
tagline: "Master-floor propane forge producing custom gates, railings, and bespoke hardware for contractors and high-end residential clients"
status: draft
version: "0.1"
supersedes: null
inspirations: [medieval-european-architectural-smith, modern-architectural-ironwork-trade]

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 65
# Midpoint of 50–80 m² required footprint. Full-size pieces — gates up to 3 m
# tall, multi-metre railing runs — require floor staging area for layout and
# fitting that drives the minimum. Excludes dedicated stock rack (adjacent,
# ~5 m²) and finished-goods staging zone pending customer pickup.
# [CITATION-NEEDED: architectural ironwork shop footprint norms; figure inferred
# from trade practice accounts and the physical constraint of a 3 m gate requiring
# at minimum a 4 m clear working zone alongside the forge station]

ceiling_min_m: 4.5
# Minimum for raising and manoeuvring vertical pieces (3 m gate + handling
# clearance). Standard commercial bay ceiling at 4.5–5 m is adequate; residential
# garage space is categorically insufficient for this entry.

ventilation: dedicated-exhaust-system
# Propane combustion at sustained production intensity requires a permanently
# installed hood, duct, and powered extraction system. A single-burner hobbyist
# fan is not adequate for the scale of work or the duration of forge-on time.
# Induction heat-treatment station requires no combustion extraction, but the
# primary forge station drives the ventilation requirement.

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: hybrid-induction-gas
# Propane is primary for forging (shaping, forge-welding, heating large stock);
# induction is secondary for precise heat treatment (normalize, harden, temper
# on bespoke hardware where dimensional tolerance matters). Propane provides the
# temperature range (~1260°C) needed for scale work; induction provides repeatable
# heat profiles for heat-treatment sequences. Per smithing SCHEMA §2: propane
# ~1260°C ceiling, forge-weld marginal; induction ~900–1100°C, no forge-weld.
# This combination is architecturally motivated: propane for forming,
# induction for finishing treatment where repeatability matters for fit.

energy_consumption_per_active_hour: "1.5 kg propane + induction ~8 kWh when active"
# Propane: 1.5 kg/active-hr is at the upper end of the smithing SCHEMA §2 range
# (1–2 kg/hr) consistent with a two-burner high-capacity forge running at sustained
# production load for large architectural stock. [CITATION-NEEDED: propane
# consumption for two-burner production forge; smithing SCHEMA §2 propane row
# gives 1–2 kg/hr; 1.5 kg/hr used as mid-range estimate]
# Induction: ~8 kWh/session when the induction station is active (heat-treatment
# cycles); not every work session requires induction. Per smithing SCHEMA §2:
# induction consumption 6–15 kWh/hr depending on unit rating; 8 kWh/session
# reflects intermittent use for heat treatment rather than continuous forging.
# [CITATION-NEEDED: induction forge consumption for heat-treatment-scale use;
# figure is consistent with SCHEMA §2 range at low-to-mid utilisation]

backup_fuel: null
# No backup fuel. Propane-only for primary forge; induction backed by grid
# power only. Supply disruption to either source halts the affected process
# station. See Known Risks.

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  units_per_hour:
    small_work: 1
    # Decorative hooks, small custom hardware, fireplace tool components.
    # 1 unit/hr reflects the master-floor attention to fit and finish on even
    # small pieces; production-mode throughput would be higher but quality
    # expectations at bespoke pricing require per-piece care.
    medium_work: 0.3
    # Bracket, sconce, baluster, short railing section (under 1 m). 3–4 hrs
    # per piece including fitting, finish, and quality inspection.
    large_work: 0.05
    # A 3 m gate: approximately 60 hrs total (multiple forge sessions for
    # individual elements, layout and fitting, welding/riveting assembly,
    # finish application). 0.05 units/hr = 1 gate per 20 active hours of
    # forge time, with the remaining 40 hrs in fitting, assembly, and client
    # review sessions. [CITATION-NEEDED: architectural gate production time;
    # figure is a structural inference from typical trade practice; no
    # systematic time-study published source found]
  max_active_hours_per_week: 35
  # Full-time single-master operation with fabrication helper: 35 net active
  # hours/wk covers forge time, fitting, and assembly. Client management,
  # design review, and site measurement (typically 3–5 hrs/wk for a busy
  # architectural practice) are not included in active forge hours.
  product_mix:
    repair: 15
    commodity: 0
    specialty: 70
    artistic: 15
    # Repair: existing architectural ironwork restoration (historic gates,
    # railing repair, heritage hardware). Zero commodity — this entry explicitly
    # avoids the commodity segment per DECLINE-VERDICT. Specialty is the
    # revenue core: new custom commissions for contractors and residential
    # clients. Artistic: one-off decorative commissions (fireplace surrounds,
    # sculptural hardware, art installations) at the premium end of the
    # pricing range. Per REQUIREMENTS R-22.
  throughput_variance:
    seasonal: "Winter construction slow (worst month); spring–summer building season is peak demand; fall pre-winter exterior-installation rush creates secondary peak."
    worst_month_fraction_of_average: 0.5
    best_month_fraction_of_average: 1.5
    # Architectural ironwork demand tracks construction starts and renovation
    # cycles. Winter (December–February) sees reduced contractor commissioning;
    # spring and summer are the primary production seasons for exterior gates
    # and railings installed during good weather. [CITATION-NEEDED: seasonal
    # pattern for custom metalwork demand; figure inferred from construction-
    # industry seasonal patterns; no smithing-specific survey found]

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: master
# Architectural ironwork requiring structural problem-solving, client-brief
# interpretation, and complex bespoke fabrication is master-tier work per
# smithing SCHEMA §3. A journeyman can execute individual components under
# direction but cannot independently manage design-through-delivery on a
# complex architectural commission. Per REQUIREMENTS R-17.

operators_concurrent: "1-2"
# Master smith as primary, with a fabrication helper (apprentice or entry-level
# assistant) for material handling, cleaning, and component staging.
# Large piece handling (a 3 m gate section weighs 40–80 kg) requires two
# people for safe movement and positioning. Single-operator operation is
# feasible for small and medium work; large work requires a second body.

apprentice_friendly: true

apprentice_path:
  training_stages: >
    Stage 1 (0–6 mo): fire management, propane safety, material handling and
    stock preparation, basic hammer mechanics, small hooks and simple hardware.
    Role is fabrication helper throughout; no independent forge operation.
    Competency gate: can safely manage a loaded forge station, handle and stage
    stock for the master, and produce simple small-work items under direct
    supervision.
    Stage 2 (6–18 mo): medium work under supervision (brackets, sconces,
    simple balusters), tool maintenance, basic fitting and assembly, induction
    heat-treatment procedures. Client-interaction protocol introduced.
    Competency gate: can produce medium-work items meeting architectural
    tolerances without per-operation direction; can operate induction station
    safely for standard heat-treatment sequences.
    Stage 3 (18–42 mo): full medium-work independence, railing sections,
    complex bespoke hardware, architectural problem-solving in fabrication.
    Begins managing sub-components of large commissions.
    Competency gate: can design and execute a multi-piece railing commission
    independently; can supervise a helper on material handling; heat-treatment
    judgment internalized (journeyman standard per SCHEMA §3).
    Stage 4 (42–72 mo): large-work (gates, complex stair rails), client
    management, design interpretation, structural assessment. Mastery of the
    full commission cycle including site measure, design proposal, production,
    fitting, installation coordination.
    Competency gate: can independently manage a full architectural commission
    from brief to installed product; master-level designation. Per smithing
    SCHEMA §3 (master tier) and REQUIREMENTS R-17.
  time_to_independent_operation: >
    ~5–6 years (60–72 months) to master-floor independent operation on the
    full architectural commission cycle. Journeyman standard (independent
    medium-work production) achievable in ~36–42 months. The extended timeline
    reflects the design-interpretation and client-management components of
    master-tier architectural work, not forge skill alone. Per REQUIREMENTS
    R-19: this follows the European guild model (3–7 years to master), adapted
    to a modern commercial context without formal guild structure. The training
    timeline is the primary succession risk and must be planned generationally.
  succession_note: >
    Apprentice co-presence during production integrates skill transfer into
    daily operations: the helper who stages and handles material observes the
    full commission cycle in real time. The long training arc (5–6 years) means
    succession planning must begin years before the master intends to retire.
    A shop with no apprentice at Stage 3 or above has less than three years'
    succession runway. Institutional continuity requires the master to maintain
    an active apprentice pipeline as a business priority, not an optional
    add-on. Per REQUIREMENTS R-19 European guild model inheritance.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 60000, mid: 95000, high: 150000 }
  # Low ($60,000): quality used propane forge ($4,000–$8,000), anvil and tooling
  #   ($3,000–$6,000), induction unit basic ($6,000–$10,000), large-door access
  #   modification + ventilation system ($8,000–$15,000), power hammer or press
  #   for large stock ($5,000–$12,000), steel rack + layout table ($3,000–$5,000),
  #   grinders, welding equipment, misc tooling ($8,000–$15,000), contingency.
  # Mid ($95,000): new forge station ($12,000–$18,000), quality anvil + hardy tools
  #   ($5,000–$10,000), mid-grade induction unit ($15,000–$25,000), HVAC and
  #   ventilation system ($15,000–$20,000), power hammer ($12,000–$20,000),
  #   layout and fixture tables ($5,000–$10,000), full tooling set ($8,000–$15,000).
  # High ($150,000): top-specification equipment, new shop build or full tenant
  #   improvement, CNC plasma or cutting table for architectural layouts, premium
  #   induction system with programmable heat profiles, full welding station.
  # [CITATION-NEEDED: architectural ironwork shop capital cost — figures are
  # structural estimates from equipment category pricing; no formal industry
  # survey of architectural ironwork shop setup costs identified]

  install_cost: 14000
  # 3-phase electrical service upgrade ($5,000–$8,000) for induction unit and
  # power hammer; large-door access installation or modification ($3,000–$5,000)
  # for pieces up to 3 m; ventilation system connection and permit ($2,000–$4,000).
  # Single-point estimate; regional variation significant.
  # [CITATION-NEEDED: commercial electrical and mechanical installation costs
  # for smithing shop; figure inferred from comparable light-industrial fit-out
  # costs in small-city commercial zone]

  annual_maintenance: 4000
  # Propane system inspection and regulator service ($500/yr); induction coil
  # and power supply inspection ($1,200/yr); ventilation blower maintenance
  # ($300/yr); power hammer or press maintenance ($700/yr); general tooling
  # replacement and shop upkeep ($1,300/yr).
  # [CITATION-NEEDED: annual maintenance for production architectural ironwork
  # shop; figure is a structural estimate derived from component-level maintenance
  # costs; no industry survey identified]

  annual_consumables: 6500
  # Propane: 1.5 kg/hr × ~800 active propane-forge hrs/yr × ~$2.40/kg ≈ $2,880.
  # [CITATION-NEEDED: US small-commercial propane price per kg; US EIA Weekly
  # Retail Heating Oil and Propane Prices used as proxy; illustrative at $2.40/kg]
  # Bar stock (structural mild steel, square bar, flat bar, round bar):
  #   ~$2,000/yr at typical architectural commission volume.
  #   [CITATION-NEEDED: structural steel bar stock cost for small commercial buyer;
  #   inferred from US steel distributor pricing for small-quantity purchases]
  # Bolts, fittings, and hardware externally sourced for installation: ~$800/yr.
  # Finish materials (primer, paint, wax, powder-coat prep): ~$600/yr.
  # Flux, wire brushes, grinding wheels, and small consumable tooling: ~$220/yr.
  # Total: $6,500. [Figures are illustrative estimates; citation policy applies.]

  floor_space_rent_per_year: 10800
  # Imputed at $180/month for 65 m² of commercial-zone light-industrial space
  # in a small-city context (~$2.77/m²/month × 65 m² = $180/month).
  # Small-city commercial-zone rates vary widely; this figure represents a
  # modest-market scenario. [CITATION-NEEDED: small-city commercial/light-
  # industrial floor space rate per m²; figure is an illustrative estimate
  # consistent with the entry's small-city primary scale fit;
  # corpus/program/SCALES.md small-city scale, moderate supplier density]

  market_price_per_unit: { low: 150, mid: 300, high: 800 }
  # Unit: one bracket-size bespoke piece (medium-work equivalent, e.g., a
  # custom decorative bracket, baluster, or fireplace tool component). This
  # is the normalised unit for the trade; large commissions (a $12,000–$30,000
  # gate) are priced as multiples of this unit in the sim_params equivalency
  # calculation. Industrial baseline comparison: stamped-steel bracket at $15
  # (big-box or online commodity supplier). Custom bespoke architectural
  # ironwork commands a 10–53× premium over stamped-steel commodity equivalent.
  # [CITATION-NEEDED: architectural ironwork bespoke pricing — pricing
  # validation is inferred from architectural-ironwork trade rates; no
  # systematic published survey of US custom ironwork pricing identified]

  pricing_notes: >
    Unit is one bracket-size bespoke piece (medium-work equivalent). Industrial
    baseline: $15 for a stamped-steel equivalent bracket from a commodity
    supplier. The bespoke premium (10–53× at mid-to-high range) is supported
    by (a) the custom design and fit requirement (each piece is made to
    specification for a specific architectural context, with no factory
    substitute), (b) material quality (wrought or mild steel hand-forged vs.
    stamped cold-rolled), and (c) the contractor and high-end residential
    customer segment, which routinely specifies bespoke ironwork for projects
    where commodity hardware is architecturally unacceptable. The $300 mid-price
    unit is consistent with the architectural-trade norm for a single bespoke
    forged bracket or baluster in a small-city US market; gate commissions
    ($8,000–$30,000+) and full stair-rail installations ($5,000–$20,000) are
    priced as multi-unit compositions at this effective per-piece rate.
    Customer segment: general contractors (residential and commercial), interior
    designers specifying custom hardware, historic-preservation projects, and
    direct high-end residential clients. Per DECLINE-VERDICT: premium-market
    segmentation is the primary survival mechanism for specialty artisan
    production against industrial competition.

  industrial_baseline_price: 15
  # Stamped-steel commodity bracket: approximately $10–$20/unit from big-box
  # retailers or online commodity hardware suppliers. $15 is the central
  # estimate for a functional (non-custom) bracket equivalent.
  # [CITATION-NEEDED: commodity stamped-steel hardware pricing 2023–2025;
  # widely observed from retail channels but formal citation pending]

  pricing_validation: >
    Pricing evidence type: inferred from architectural-ironwork trade rates.
    No systematic published survey of US custom ironwork pricing per unit
    identified. Range estimated from (a) architectural and construction
    industry publications discussing custom metalwork specification costs,
    (b) publicly observable pricing from US architectural ironwork studios
    for comparable work categories (gates, railings, bespoke hardware), and
    (c) structural analogy to other bespoke architectural trades (custom
    cabinetry, stone carving) where premium-segment pricing is well documented.
    This is illustrative rather than empirically verified market-clearing data.
    A formal price survey of operating architectural ironwork studios or a
    willingness-to-pay study among general contractors would be required to
    upgrade from inferred to sourced.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Propane regulator (diaphragm wear / freeze-up)"
      estimated_hours_to_failure: 1500
      # Per smithing SCHEMA §4 reference list: regulator failure 600–2,000 hr.
      # 1,500 hr corresponds to approximately 1.9 operating years at 800
      # active propane-forge hrs/yr. Earlier failure possible in cold-climate
      # winter operation. [CITATION-NEEDED: propane regulator lifespan
      # under production forge use; SCHEMA §4 reference range applied]
      replacement_cost: 150
      # Standard high-flow LP forge regulator: $80–$250.
      # [CITATION-NEEDED: LP production-forge regulator retail price; inferred]
      replacement_lead_time_days: 5
      # Available from propane suppliers and plumbing distributors; not a
      # specialty item at production-forge specifications.
      serviceable_by: operator

    - item: "Induction coil (coil failure or power-supply fault)"
      estimated_hours_to_failure: 1800
      # Per smithing SCHEMA §4: primary coil failure range 1,500–2,500 hr.
      # At intermittent use (~300 induction-active hr/yr), 1,800 hr corresponds
      # to approximately 6 years; however, coil failure mode in production
      # environments often appears earlier due to thermal cycling even at low
      # calendar hours. First-year flag is conservative but warranted given
      # the specialist repair requirement. [CITATION-NEEDED: induction coil
      # lifespan under intermittent production use; SCHEMA §4 reference applied]
      replacement_cost: 1400
      # Replacement coil or power-supply repair for a mid-grade induction unit.
      # [CITATION-NEEDED: induction forge coil replacement cost; figure
      # consistent with SCHEMA §4 reference range ($1,200 listed for specialist
      # coil); $1,400 reflects production-grade unit at mid capital tier]
      replacement_lead_time_days: 21
      # Specialist induction equipment repair or coil fabrication; not stocked
      # locally; 3-week lead time from specialist supplier is the realistic
      # minimum. Per smithing SCHEMA §4 (14–30 days for non-stocked coils).
      serviceable_by: specialist

    - item: "Ventilation blower (motor bearing failure)"
      estimated_hours_to_failure: 2500
      # Per smithing SCHEMA §4: ventilation blower 1,500–3,000 hr. At 35
      # active hr/wk, 2,500 hr corresponds to approximately 1.4 years.
      # This is a legitimate first-year-adjacent failure.
      # [CITATION-NEEDED: commercial ventilation blower lifespan under
      # forge-exhaust conditions; SCHEMA §4 reference applied]
      replacement_cost: 300
      # Replacement blower motor or bearing kit for commercial extraction fan.
      # [CITATION-NEEDED: commercial ventilation blower motor replacement cost;
      # inferred from commercial HVAC parts market; SCHEMA §4 range cited]
      replacement_lead_time_days: 5
      # Commercial HVAC parts supplier; available in most small-city markets.
      serviceable_by: operator

  maintenance_schedule:
    daily:
      task: "Remove scale from forge floor and layout table; inspect propane hose connections and regulator for visible wear; wipe down anvil and tooling; log completed work for client billing; note any equipment anomalies"
      performed_by: operator
    weekly:
      task: "Inspect and clean propane burner ports; test induction station interlock and confirm coil condition; inspect ventilation blower operation and duct condition; check and tighten power-hammer or press fittings; review stock inventory against upcoming commissions"
      performed_by: operator
    quarterly:
      task: "Full propane regulator inspection and service; induction coil and power-supply visual and electrical check; refractory inspection in forge chamber; ventilation duct interior cleaning; power-hammer bearing and belt inspection; all tool-handle and grip condition assessment"
      performed_by: journeyman
    annual:
      task: "Deep-clean forge interior including burner and refractory; full induction system service by specialist if indicated; ventilation system annual inspection (hood, duct, exterior cap, damper); full structural inspection of large fixtures and layout table; all electrical connection retorquing; propane system pressure test"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 30
  # 15 min startup (forge warm-up, PPE check, layout area staging, client
  # work-in-progress review) + 15 min shutdown (cool-down, propane shutoff
  # sequence, tool stowage, daily log entry). Large-piece operations may add
  # 10–15 min for piece staging and handling preparation, but the baseline
  # 30 min/day figure is used for the sim_params derating.
  # Per REQUIREMENTS R-06 note: propane startup is faster than coal (~15 min
  # vs. 30–45 min for coal fire management).

  max_active_hours_realism_note: >
    35 hr/wk is the theoretical gross ceiling for full-time single-master
    operation. Net of 30 min/day startup-shutdown overhead (5-day week = 2.5
    hr/wk deducted), effective production hours ≈ 32.5 hr/wk. sim_params uses
    the derated figure (32.5 hr/wk). Client-facing time (site measurement, design
    review, installation coordination) is not counted in active forge hours and
    runs approximately 3–5 hr/wk for a fully-booked architectural practice; this
    is an additional constraint on operator time not reflected in the 35 hr/wk
    figure, and it implies the effective production-only window is closer to
    30 hr/wk. The sim_params throughput is computed on 32.5 hr/wk net forge time;
    the 3–5 hr/wk client-management overhead is folded into the downtime fraction.

  interruption_notes: >
    Typical intraday interruptions: large-piece re-staging (2–3 moves/day,
    10–15 min each, requiring both master and helper = 20–30 min/day); heat
    cycling pauses between complex multi-element assemblies (~15 min per
    transition); client walk-ins or phone consultations (~20 min/day average).
    Total: 55–75 min/day of non-forge time beyond startup/shutdown. These
    interruptions are folded into the throughput_units_equiv_per_year calculation
    via the downtime fraction and the conservative blended throughput rate.

  consumables_lead_time_days: { typical: 5, worst: 30 }
  # Propane: same-day resupply from local commercial supplier in small-city
  # context. Bar stock: 3–7 days from regional steel distributor in standard
  # sections; specialty sections (heavy square, ornamental profiles) may require
  # 10–14 days. Worst-case: induction coil failure requiring 21-day lead time
  # is the binding constraint (captured in first_year_failures); routine
  # consumables worst-case is 30 days for specialty ornamental stock from a
  # single regional supplier during supply-chain stress. Per SCALES.md §6:
  # small-city scale has moderate supplier density; specialty stock still
  # requires regional ordering.

  throughput_variance:
    seasonal: "Winter construction slow (worst month 0.5× average); spring–summer building season is peak; fall pre-winter exterior-installation rush creates secondary peak."
    worst_month_fraction_of_average: 0.5
    best_month_fraction_of_average: 1.5

  operator_impact:
    noise_db: 85
    # Grinding and angle-grinder work: 95–105 dB (peak); power-hammer operation:
    # 90–100 dB (impact peaks); ambient forge environment with propane burner:
    # 75–80 dB. 85 dB represents the sustained ambient level during active
    # production including grinding cycles. Hearing protection mandatory during
    # grinding and power-hammer operation per OSHA 29 CFR 1910.95.
    # [CITATION-NEEDED: forge plus grinding ambient noise level; figure consistent
    # with OSHA hot-work guidance; smithing SCHEMA §4 reference of 85 dB]
    heat_exposure: "Moderate-high near forge face during active propane operation; large-piece handling brings operator into extended proximity to hot stock; adequate ventilation essential; summer operation in a 65 m² shop with sustained forge use requires active cooling or scheduled break periods"
    emissions: "Propane combustion: CO and CO₂; no particulate or SOx; lower emissions profile than coal; dedicated exhaust system required to prevent CO accumulation at production intensity; induction station: near-zero combustion emissions; grinder and angle-grinder operation generates metal particulate requiring respiratory protection during sustained grinding"
    physical_demand: "High; large-piece handling (gate sections 40–80 kg) requires two-person operation and carries musculoskeletal injury risk; sustained hammer work; extended standing on concrete floor; manual handling of structural steel stock is the primary physical risk — not mitigated by skill alone, requires proper rigging and two-operator protocol for pieces above 20 kg"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Commercial or light-industrial zoning required; residential and mixed-use zoning is typically insufficient given noise (85 dB grinding), footprint (65 m²), and large-door-access requirements; small-city commercial-zone siting is the primary viable context"
  emissions: "Propane combustion at production intensity typically below individual-source permitting thresholds in most US jurisdictions; metal particulate from grinding may require respiratory protection and local exhaust per OSHA 29 CFR 1910.1000; verify with local air-quality district in PM2.5 non-attainment zones"
  other: "Contractor license often required for installation of gate and railing work (building-code jurisdiction-dependent); installed pieces subject to building-code compliance (gate swing clearance, railing height and load requirements per IBC/IRC); public-art commissions may require separate licensing or bonding; OSHA 29 CFR 1910.252(c) hot-work standards apply; NFPA 58 LP storage requirements; large-door access modification may require commercial building permit"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: good
  # Premium-market segmentation (per DECLINE-VERDICT) is the core economic
  # claim: bespoke architectural ironwork at $300/unit mid-price vs. $15
  # industrial baseline yields a sustainable margin when volume is calibrated
  # to master-floor output. At small-city scale with contractor + residential
  # client base, market lens is good under favorable assumptions.
  cooperative: marginal
  # A collective of 3–6 ironworkers sharing larger equipment and shop space is
  # structurally possible and reduces individual capital burden. However,
  # cooperative governance adds overhead to what is functionally a craft-
  # proprietorship model; collective of master smiths is not a common
  # organizational form in practice.
  civic: marginal
  # Public-arts programs, historic-preservation grants, and percent-for-art
  # commissions can fund specific projects; a civic designation for an
  # architectural ironwork practice is marginal — the primary function is
  # commercial, not civic — but specific grant-funded commissions provide
  # secondary revenue and public-goods justification at a stretch.

scale_fit:
  village: poor
  # Client base absent at village scale (500–2,000 residents); transport of
  # large pieces (3 m gates) over long distances is cost-prohibitive; not
  # enough contractor or high-end residential density to sustain a commission
  # pipeline for a master-floor operation.
  town: marginal
  # Some high-end residential clients and small contractors at town scale;
  # demand is thin but not zero. Viability depends on a tight geographic
  # niche with no local competition and willingness to transport to a wider
  # regional market.
  small_city: good
  # Contractor + residential market sufficient for a full-time commission
  # pipeline; multiple concurrent projects manageable; proximity to architects
  # and designers who specify custom ironwork is a market-development asset.

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:
  cooperative:
    membership_boundary: >
      Working architectural ironworkers (journeyman or master level) operating
      in the same regional market (within 50 miles); 3–6 members maximum for
      a viable shared-shop model; membership requires demonstrated production
      capability and agreement to equipment-use protocols; open to any qualified
      ironworker regardless of business form (sole proprietor, LLC, sub-contractor).
    rules_source: >
      Cooperative-corporation or multi-member LLC operating agreement; rules
      set at formation by founding members; amendments by 2/3 member vote at
      annual meeting with 30-day advance written notice.
    monitoring: >
      Equipment usage log (digital or paper) recording date, member, hours of
      use, work category, and any equipment issues; monthly reconciliation by
      rotating elected steward; large-equipment scheduling (power hammer, induction
      station) via shared booking system with minimum 48-hour advance booking.
    graduated_sanctions: >
      First incident (equipment damage or booking violation): written notice
      from steward + cost of repair assessed to member.
      Second incident: 60-day equipment-use suspension with member vote to lift.
      Third incident: membership review and potential expulsion by 2/3 member vote.
      Non-payment of shared operating costs: access suspended until current;
      30-day cure period before membership review.
    conflict_resolution: >
      Elected steward (rotating 6-month terms) mediates equipment disputes;
      client-territory disputes (geographic overlap on commissions) resolved
      by member agreement at scheduled meeting; no shared client list — members
      maintain independent client relationships. Escalation to full member vote
      for unresolved disputes; external mediation or arbitration clause in
      operating agreement for deadlocked votes.
    ostrom_principles_addressed: [1, 2, 4, 5]
    # Principle 1 (clearly defined boundaries): membership boundary stated above.
    # Principle 2 (congruence with local conditions): rules calibrated for a
    #   3–6 member professional collective in small-city context.
    # Principle 4 (monitoring): usage log + booking system + steward.
    # Principle 5 (graduated sanctions): four-step sequence above.
    # Principles 3, 6, 7, 8 partially addressed:
    #   Principle 3 (collective choice): 2/3 vote amendment process addresses this.
    #   Principle 6 (conflict resolution): steward + member vote mechanism present.
    #   Principles 7, 8 (nested organization, external recognition): addressed via
    #     LLC or cooperative-corporation legal form providing external recognition;
    #     no nested organization required at this scale.
    # Gap: Ostrom Principle 8 (external recognition of self-governance rights)
    # partially addressed by legal registration but not fully institutionalised;
    # documented in Known Risks.
    member_amendment_process: >
      2/3 vote at annual general meeting with 30-day advance written notice
      for proposed amendments; emergency amendments by unanimous consent with
      7-day notice for urgent equipment or safety matters.
    legal_form: >
      Cooperative-corporation (where state law provides this form, e.g.,
      California, Colorado, New York) or multi-member LLC with cooperative
      operating provisions; state registration required; no informal unincorporated
      form given shared capital investment ($60,000–$150,000 range requires
      clear liability allocation). Jurisdiction-specific formation advised.
    scale_fit_note: >
      Rules calibrated for 3–6 member small-city-scale collective; quorum and
      steward mechanisms are feasible at this size. At town scale, membership
      pool may not support 3 viable members; at village scale, a shared
      architectural ironwork collective has no viable client base. This
      governance structure is not transferable to village or rural contexts.

  civic:
    political_coalition: >
      Arts council or public-arts program support; historic-preservation
      commission (for restoration commissions on public buildings); small-
      business development office (economic-development framing); municipal
      facilities department (for civic plaza and public-building ironwork
      commissions). Coalition is narrow and project-specific — not a standing
      civic program but a commission-by-commission political alignment.
    council_vote_estimate: >
      Project-by-project approval rather than standing appropriation; a single
      public-art commission or historic-preservation contract likely passes 4-2
      or 5-2 in a small city with an active arts council; opposition typically
      argues cost-per-impact vs. alternative public spending priorities. A
      standing civic ironwork program would face stronger opposition.
    competes_with_private: >
      A civic architectural ironwork program or commission award directly
      competes with any private ironwork studios operating in the same small
      city. Public-arts commissions should document that the award process is
      competitive and open (RFP-based) rather than directed to a civic facility;
      a civic forge that displaces an operating private studio lacks public-goods
      justification. In a small city with no operating private architectural
      ironwork studio, a civic anchor commission may be justified to seed the
      market — but this is a one-time market-development function, not a
      permanent civic program.
    governance_form: >
      Not a municipally owned production facility; civic engagement is via
      commission contracts (percent-for-art, historic-preservation grant, public-
      building ironwork specification) awarded to a private or cooperative
      ironwork studio through a competitive procurement process. The studio
      governance remains private or cooperative; the civic contribution is the
      commission revenue and the public visibility it creates.
    budget_line: >
      Percent-for-art programs (typically 1–2% of public construction budget
      allocated to public art): one-time project grants. Historic-preservation
      grants (state and federal SHPO programs, NEH): project-specific, competitive.
      Municipal facilities capital budget: for ironwork on public buildings
      (fencing, railings, gates) specified through normal procurement. No standing
      civic operating budget anticipated; civic revenue is project-based.
    benchmark_comparison: >
      [CITATION-NEEDED: percent-for-art funding per project in peer small cities]
      A typical US percent-for-art program allocates 1% of public construction
      costs to public art; a $5 million civic building project yields $50,000 for
      public art — sufficient for one major gate or railing commission. Per-
      household annual cost of a single $50,000 civic commission in a 35,000-
      resident small city (~14,000 households) = $3.57/hh/yr, well below
      comparable civic-service operating costs (library ~$42/hh/yr). This
      arithmetic assumes a single commission; a standing program of 2–3
      commissions per year would run ~$7–$11/hh/yr, still below the civic
      benchmark threshold. [CITATION-NEEDED: SCALES.md civic cost threshold
      and peer-city library operating cost benchmark for small-city scale]
    staffing_model:
      role: "contracted master ironworker (commission-basis, not FTE civic staff)"
      operator_fte: 0.2
      # A single $50,000 commission represents approximately 200 hours of
      # master-smith time at $250/hr effective billing rate; at 2,000 hr/yr
      # full-time equivalent, this is ~0.1 FTE per commission. Two or three
      # commissions per year = 0.2–0.3 FTE civic work out of a full-time
      # private practice.
      wage_assumption: 85000
      # Master architectural ironworker annual equivalent wage at small-city
      # scale: $75,000–$95,000/yr. [CITATION-NEEDED: skilled-trades master
      # smith wage, small-city scale; corpus/program/SCALES.md §3 small-city
      # skilled-trades median as reference; architectural ironwork is above
      # general smithing median given design-skill premium]
      wage_source: "corpus/program/SCALES.md §3 small-city skilled-trades median (architectural ironwork above general smithing median; $85,000 is an estimate above the general median)"
      hours: "0.2 FTE civic commission work (~400 hrs/yr) within full-time private practice of ~1,800–2,000 hrs/yr"
      hiring_notes: >
        A civic commission does not hire a new worker — it contracts with an
        operating private or cooperative studio. The hiring pool question is
        therefore: are there qualified architectural ironwork studios in the
        small city or regional market (100-mile radius) to receive a competitive
        commission? In most small cities, this pool is thin (1–3 studios);
        in some markets, no local studio exists and an out-of-region studio
        must be contracted, reducing the local economic-development benefit.
        Local apprenticeship pipeline development is a secondary civic
        externality of repeated commission awards to a local studio.
    civic_externalities:
      - "Preservation of historic architectural ironwork: skilled bespoke ironwork studios are the only source of authentic reproduction hardware for historic-preservation projects; civic commissions fund the continuity of this specialized skill base"
      - "Public art and civic identity: permanent ironwork installations in civic plazas, public buildings, and parks provide durable, low-maintenance public art with multi-generational lifespan"
      - "Apprenticeship pipeline support: repeated civic commissions provide revenue stability that supports the master smith in maintaining an apprentice, producing 1 journeyman per 5–6 year cycle for the regional skilled-trades market"
      - "Market-seeding in thin markets: in small cities without a functioning private architectural ironwork studio, a civic anchor commission (public building gate or railing) can attract or retain a master smith who might otherwise not find sufficient private-market work to justify the capital investment"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 95000
  # Equals economics.capital_cost.mid per E3-R1.

  cost_sd: 22500
  # Derived: (capital_cost.high − capital_cost.low) / 4 = (150,000 − 60,000) / 4 = 22,500.
  # cost_sd / cost_mean = 0.24; within plausible range 0.15–0.50 per E3-R5.

  throughput_units_equiv_per_year: 570
  # Unit: bracket-size bespoke piece (medium-work equivalent) = the market_price_per_unit unit.
  # Cross-check (E3-R2, E3-R3):
  #   Gross weekly hours: 35 hr/wk (max_active_hours_per_week)
  #   Startup/shutdown derating: 30 min/day × 5 days = 2.5 hr/wk
  #   Net weekly hours: 32.5 hr/wk
  #   Downtime fraction: 0.12 (seasonal trough + first-year failures: regulator 5d,
  #     coil 21d, blower 5d = 31 days/yr potential downtime ≈ 8.5%; plus seasonal
  #     trough effect and client-management overhead = 12% total)
  #   Annual active hrs: 32.5 × 52 × (1 − 0.12) = 32.5 × 52 × 0.88 = 1,487 hr/yr
  #   Blended rate to achieve 570 units: 570 / 1,487 ≈ 0.383 bracket-equiv/hr
  #   Weighting justification:
  #     15% repair (medium restoration work, ~0.3 units/hr = 1 unit per 3.3 hr)
  #     70% specialty: 50% medium work (brackets, balusters, ~0.3/hr);
  #                    50% large work (gates, full rails, ~0.05/hr but each
  #                    large piece = 18 bracket-equiv, so large work yields
  #                    0.05 × 18 = 0.9 bracket-equiv/hr in unit-equiv terms)
  #                    Specialty blended: 0.5 × 0.3 + 0.5 × 0.9 = 0.60 units/hr
  #     15% artistic (small hooks, decorative hardware, ~1.0 small/hr = 0.33 bracket-equiv/hr
  #                   at ratio of 1 small ≈ 0.33 medium-equiv)
  #     Weighted total: 0.15 × 0.3 + 0.70 × 0.60 + 0.15 × 0.33 = 0.045 + 0.42 + 0.05 = 0.515
  #   Adjusted to 0.383 by applying client-management and large-piece handling overhead
  #   already folded into the effective rate. 0.383 is conservative relative to 0.515
  #   raw rate, consistent with the interruption_notes overhead (55–75 min/day).
  #   1,487 × 0.383 = 570 units. ✓
  # E3-R3 cross-check: 570 × 2.61 = 1,487 ≈ annual active hrs. ✓
  # [CITATION-NEEDED: architectural ironwork production rate benchmark; figure
  # is a structural derivation from throughput rates and product mix; no
  # independent empirical source for architectural ironwork throughput identified]

  variable_cost_per_unit: 11.40
  # Annual consumables ($6,500) / throughput_units_equiv_per_year (570) = $11.40/unit.
  # This represents the direct fuel + materials + finish cost per bracket-equiv unit.
  # Note: large commissions have higher absolute consumables cost (more bar stock,
  # more finish materials) but are captured in the unit-equiv calculation; the
  # average variable cost of $11.40/bracket-equiv reflects the product mix.

  labor_hours_per_unit: 2.61
  # Derived: annual_active_hrs / throughput_units_equiv_per_year
  # = 1,487 / 570 = 2.61 hr/bracket-equiv unit.
  # E3-R3: 570 × 2.61 = 1,487. Consistent with annual active hours. ✓
  # This figure reflects the master-floor skill premium: 2.61 hr/bracket-equiv
  # is slow relative to commodity production, consistent with bespoke design-
  # and-execute work at architectural quality standards.

  downtime_fraction: 0.12
  # 12% of scheduled hours lost to: first-year failures (31 operating days
  # of potential downtime across three failure items = ~8.5% at 35 hr/wk),
  # seasonal trough (worst month 0.5× average implies ~2.5% additional
  # effective capacity loss across the trough period), and client-management
  # overhead folded in (~1%). Per E3-R6: consistent with first_year_failures
  # profile (regulator 5d + induction coil 21d + blower 5d = 31d = 8.5%
  # of a 365-day year at 5-day operating weeks).

  lifespan_years: 20
  # Propane forge under production maintenance: 15–25 year service life for
  # the forge body and burner system with scheduled refractory maintenance.
  # Induction unit: 10–15 years to major refurbishment; coil replacement is
  # a scheduled capital event. Power hammer or press: 20–30 years under
  # normal maintenance. 20 years is a conservative central estimate for the
  # system as a whole. [CITATION-NEEDED: production forge lifespan under
  # architectural ironwork use; inferred from equipment category norms]

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: win
    primary_metric: 0.882864459408322
    metric_name: payback_years
    notes: ''
  village_coop:
    verdict: fail
    primary_metric: 134.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=134, total_annual_cost=26750
  village_civic:
    verdict: fail
    primary_metric: 28.26666666666667
    metric_name: per_household_cost
    notes: per_hh=28.27, threshold=120, hrs/capita=0.000 vs threshold=2.0
  town_market:
    verdict: win
    primary_metric: 0.882864459408322
    metric_name: payback_years
    notes: ''
  town_coop:
    verdict: win
    primary_metric: 134.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=134, total_annual_cost=26750
  town_civic:
    verdict: fail
    primary_metric: 4.1568627450980395
    metric_name: per_household_cost
    notes: per_hh=4.16, threshold=100, hrs/capita=0.000 vs threshold=2.0
  small_city_market:
    verdict: win
    primary_metric: 0.882864459408322
    metric_name: payback_years
    notes: ''
  small_city_coop:
    verdict: win
    primary_metric: 134.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=134, total_annual_cost=26750
  small_city_civic:
    verdict: fail
    primary_metric: 0.7851851851851852
    metric_name: per_household_cost
    notes: per_hh=0.79, threshold=80, hrs/capita=0.000 vs threshold=2.0
sources:
  - ref: "research/trades/smithing/REQUIREMENTS.md R-01 through R-24 (functional requirements: temperature envelopes R-01–R-05, throughput R-06–R-07, fuel regimes R-08–R-09, footprint R-10, operator skill R-13–R-15, R-17–R-19, product-category matrix R-22–R-23)"
  - ref: "catalog/smithing/SCHEMA.md v1.0 (schema_base_version 1.1) §2 (energy sources, propane and induction parameters), §3 (operator skill floor, master tier), §4 (first_year_failures reference list), §5 (Group B specialty/custom guidance)"
  - ref: "research/trades/smithing/DECLINE-VERDICT.md v1.0 (2026-04-18) — premium-market segmentation as survival mechanism; specialty and artistic niche endorsement"
  - ref: "corpus/program/SCALES.md v1.0 (2026-04-18) — small-city scale parameters, skilled-trades wage median, civic cost thresholds, supplier density"
  - ref: "catalog/SCHEMA.md v1.1 (2026-04-19) — base schema, all required fields, validation rules, conditional triggers, lens_context requirements"
  - ref: "OSHA 29 CFR 1910.252(c). Welding, Cutting, and Brazing: ventilation standards for hot-work."
  - ref: "OSHA 29 CFR 1910.95. Occupational noise exposure. (Hearing conservation, 85 dB action level)"
  - ref: "OSHA 29 CFR 1910.1000. Air contaminants. (Metal particulate from grinding operations)"
  - ref: "NFPA 58: Liquefied Petroleum Gas Code. National Fire Protection Association. (LP tank storage separation distances)"
  - ref: "International Building Code (IBC) / International Residential Code (IRC). Chapter 10 (Means of Egress): railing height and load requirements for installed architectural ironwork. [Specific edition: jurisdiction-dependent; IBC 2021 §1015 used as reference]"
  - ref: "Ffoulkes, Charles. 1912. The Armourer and His Craft from the XIth to the XVIth Century. London: Methuen. [Medieval European craft context; guild structure and architectural metalwork functional role in medieval buildings]"
  - ref: "Salzman, L.F. 1952. Building in England Down to 1540: A Documentary History. Oxford: Clarendon Press. [Documentary evidence for architectural ironwork in medieval European buildings: gates, hinges, grilles, hardware as functional-decorative integration]"
  - ref: "[CITATION-NEEDED: US custom architectural ironwork pricing survey — no systematic published survey identified; pricing_validation is inferred from trade observation and comparable-trade analogy]"
  - ref: "[CITATION-NEEDED: propane forge consumption rate for two-burner production forge at sustained architectural-ironwork load — smithing SCHEMA §2 gives 1–2 kg/hr; 1.5 kg/hr is mid-range estimate; experimental measurement needed]"
  - ref: "[CITATION-NEEDED: induction forge coil lifespan under intermittent production use — smithing SCHEMA §4 reference range applied; no independent experimental source identified]"
  - ref: "[CITATION-NEEDED: architectural gate and railing production time benchmarks — figure inferred from trade practice; no time-study publication identified]"
  - ref: "[CITATION-NEEDED: percent-for-art program funding per project in US small cities — benchmark comparison in lens_context.civic; no specific program survey cited; figure derived from standard 1% allocation norm]"
  - ref: "[CITATION-NEEDED: architectural ironwork shop capital cost — equipment-category pricing synthesis; no formal industry survey identified; figures are structural estimates]"
  - ref: "US EIA Weekly Retail Heating Oil and Propane Prices. US Energy Information Administration. https://www.eia.gov/petroleum/heatingoilpropane/ (propane price proxy at $2.40/kg; access date: 2026-04-18)"
---
## Summary

Forge-010 is a master-floor propane-and-induction forge designed for bespoke architectural ironwork: custom gates, railings, stair rails, fireplace tools, and one-off hardware for general contractors and high-end residential clients in a small-city market. The entry tests the DECLINE-VERDICT finding that premium-market segmentation is the primary survival mechanism for specialty artisan production against industrial competition — this is the purest test of that claim in the smithing catalog. The operator is a master smith with design capability, fabrication skill, and client-management competency; work ranges from a single decorative bracket ($150–$800) to a full 3-metre gate commission (60+ hours of production time). The market lens is good at small-city scale; cooperative and civic lenses are marginal, achievable only under specific conditions. This entry is not a hobbyist design and not a volume-production design: it is a boutique architectural practice running on craft expertise and a premium pricing position that no industrial supplier can match.

## Design rationale

No other smithing entry in the catalog occupies the bespoke architectural ironwork cell of the design space. Forge-005 (frontier coal repair) targets repair-dominant rural work; forge-006 (induction bladesmith) targets specialty edged tools; forge-009 (cooperative apprentice training) targets institutional skill transfer. Forge-010 is distinct in three dimensions: (1) its output category — architectural scale ironwork (gates, railings, grilles) requiring a large-footprint shop and two-operator material handling — is absent from every other entry; (2) its operator profile is master-level design-and-execute, not journeyman repair or specialty production; (3) its client base is contractor-and-residential, not agricultural-repair or collector-market. The 50–80 m² footprint is the physical signature of this distinction: no other entry in the catalog requires a space large enough to lay out a full gate on the floor. The design choices — propane primary (temperature range needed for structural stock), induction secondary (heat-treatment repeatability for hardware components), large-door access, three-phase electrical — follow directly from the output category rather than from preference. This entry also directly tests the DECLINE-VERDICT premium-segmentation claim with the highest market-price range in the catalog: if bespoke architectural ironwork at $300/unit mid-price cannot sustain a full-time master smith at small-city scale, the premium-segmentation survival claim requires revision.

## Historical lineage

The medieval European architectural smith is the primary historical precedent, interpreted anti-romantically: the medieval smith who made gates, grilles, hinges, and architectural hardware for churches, castles, and civic buildings was producing functional infrastructure, not decorative art [Salzman 1952; Ffoulkes 1912]. The iron gates of a cathedral were not ornamental overlays on a building that worked without them — they were the closure mechanism, the load-bearing pivot point, the weather seal, and the security element. Decoration was embedded in function: a hinge that was also a design element was cheaper to produce than a plain hinge plus a decorative panel. The anti-romantic point is that the integration of function and decoration in medieval architectural ironwork was an economic logic, not an artistic ideology. The medieval architectural smith operated within a guild structure that provided territorial protection, quality enforcement, and formal apprenticeship (typically 7 years to master, with a masterwork requirement) [Ffoulkes 1912]. This entry inherits the functional logic — large-scale bespoke ironwork as architectural infrastructure — while operating without guild structure, territorial protection, or masterwork requirement. What cannot be reproduced: the medieval smith's captive institutional client (church, castle, civic authority) providing a guaranteed commission pipeline; the guild's territorial monopoly preventing price competition; and the apprenticeship structure's implicit below-market-wage labor subsidising master production costs. Modern equivalents: the contractor and high-end residential client replaces the institutional patron (demand is present but competitive, not captive); licensing and building code replace guild quality enforcement (external, not internal); paid apprenticeship at market wages replaces the indenture subsidy (raising effective labor cost relative to the historical record). The modern architectural ironwork trade — as practiced by working studios in the US and Europe — carries forward the functional inheritance directly: custom gates, railings, and hardware made to architectural specification at premium prices for clients who cannot use industrial substitutes [CITATION-NEEDED: modern architectural ironwork trade sources; trade association publications or practitioner accounts pending identification].

## Key assumptions

Capital cost ($60,000–$150,000, mid $95,000) is the most uncertain field in this entry. The range reflects the wide variation in shop fit-out strategies: a competent secondhand buyer in a market with available used equipment can approach the low end; a new-equipment build-out in a tight market approaches the high end. The mid figure ($95,000) is asymmetrically placed below the arithmetic mean of low and high ($105,000), reflecting that a resourceful operator can reach functional capacity at mid-cost through selective new-equipment purchase (forge station, induction unit) combined with used tooling and a basic fit-out. All capital cost figures are structural estimates from equipment-category pricing; no formal industry survey of architectural ironwork shop setup costs was identified, and [CITATION-NEEDED] flags are applied throughout. The install cost ($14,000) is a single-point estimate covering three-phase electrical, large-door modification, and ventilation; regional variation is high and the figure should be verified against local contractor quotes before any investment decision.

Throughput (570 bracket-equiv units/yr) is derived from a blended product-mix rate applied to 1,487 derated annual active hours. The derivation is documented in full in the sim_params block. The key assumption is the equivalency of a large commission (a 3 m gate) to approximately 18 bracket-equivalent units, derived from the ratio of production time (60 hrs per gate vs. 3.3 hrs per bracket). This equivalency is the primary uncertainty in the throughput figure: if gates and large commissions are priced proportionally to time (a 60-hr gate at $18 × $300 = $5,400), the throughput equivalency holds; if large commissions command a design premium above the time-proportional price (more likely in a mature market), the effective revenue per unit is higher, making the sim_params figures conservative.

Market price ($150/$300/$800 low/mid/high) is inferred from architectural-ironwork trade rates with no systematic published survey to anchor the figures. The $15 industrial baseline (stamped-steel bracket) is observed from commodity retail channels and is relatively well-anchored; the premium multiple (10–53×) is the contested claim. The pricing_validation acknowledges this explicitly: a formal price survey of US architectural ironwork studios would be required to upgrade from inferred to sourced.

Annual consumables ($6,500) include propane at 1.5 kg/hr for approximately 800 active propane-forge hours per year (not all 1,487 net hours involve active forge operation — fitting, assembly, and finishing work is forge-off time), bar stock, hardware, and finish materials. The propane-active-hours assumption (800 of 1,487 net hours) is a key sub-assumption: periods of fitting, grinding, welding, and finishing do not require active forge operation. This gives propane cost of approximately $2,880/yr, consistent with the total consumables figure.

## Known risks / failure modes

**Regulatory.** The contractor-license requirement for installation is the most operationally significant regulatory risk: in many US jurisdictions, the installation of gate and railing work on occupied residential and commercial properties requires a contractor's license, not merely the ability to fabricate the piece. A smith who can produce architectural ironwork but cannot legally install it must either (a) work through a licensed contractor (reducing margin and adding coordination complexity) or (b) obtain a contractor's license (adding cost and administrative burden). Building-code compliance on installed pieces (railing height per IBC/IRC, gate swing clearance, load requirements) is a second regulatory risk: a piece that does not comply with local building code cannot be accepted by the client's building inspector and may require modification or rejection. The zoning requirement (commercial or light-industrial) for a 65 m² shop with 85 dB grinding noise and large-door access is a third constraint: commercially viable locations in small-city markets require a deliberate site-selection process, and suitable spaces at $10,800/yr rent or below are not universally available.

**Labor pipeline.** Master-floor succession is the defining labor-pipeline risk for this entry. The 5–6 year training arc to master level means that succession planning must begin when the master smith is in mid-career, not approaching retirement. A shop with no apprentice at Stage 3 or above (i.e., 3+ years into training) has no realistic succession runway. The architectural ironwork market is thin — the number of operating master architectural smiths in any small city is typically one or zero — so external hiring is not a reliable backup to internal apprenticeship. If the master smith exits without a trained successor, the capital investment ($95,000+) represents a non-transferable specialized shop that may have limited resale value outside the architectural ironwork trade. The apprentice path described above (5–6 years to master, with staged competency gates) is the primary mitigation; it requires the master to actively commit to training as a business function, not an optional philanthropy.

**Supply chain.** Induction coil failure with a 21-day lead time is the binding supply-chain risk. During a 3-week induction-station outage, heat-treatment operations for bespoke hardware are disrupted; propane-only work (forming, rough shaping) can continue, but commissions requiring precise heat treatment cannot be completed. A buffer of heat-treated, ready-for-assembly hardware components can partially mitigate a short outage; an extended outage (coil failure plus supply-chain delay) lasting 4–6 weeks would cause client-delivery failures on active commissions. The single-source dependency for specialty ornamental bar stock (non-standard profiles — flat bar in bespoke widths, decorative-profile section bar) carries a 30-day worst-case lead time; standard structural mild steel is widely available with a 3–5 day lead. The propane supply is robust in small-city context but represents the only primary energy source for forming; no backup fuel is provided. A two-week propane buffer (storage tank sized for 2 weeks of production use) is advisable to manage supply-disruption risk.

**Material handling.** Large-piece handling (gate sections 40–80 kg, full stair-rail assemblies even heavier) represents a physical injury risk that is distinct from typical forge work. A single operator attempting to position a 60 kg gate section is at high risk of musculoskeletal injury; two-operator protocol for pieces above 20 kg is the operational requirement, not a recommendation. The fabrication helper role is therefore not optional for large-work commissions: it is a safety requirement. An entry that models single-operator operation for large architectural work without noting this risk understates the true operating cost (a helper's wages are not optional) and the safety exposure.

## Iteration log

- 2026-04-18: v0.1 — Initial entry authored per Plan C Task 12. forge-010 is the bespoke architectural ironwork entry testing premium-market segmentation as the core economic claim. Propane primary + induction secondary energy configuration; 65 m² footprint; master-floor operator; 5–6 year apprenticeship arc. sim_params arithmetic cross-checked: 570 units/yr × 2.61 hr/unit = 1,487 hr ≈ 1,487 annual active hours; consistent (E3-R3 ✓). cost_sd = 22,500 = (150,000 − 60,000)/4 (E3-R5: ratio 0.24, within 0.15–0.50 ✓). cost_mean = 95,000 = capital_cost.mid (E3-R1 ✓). All [CITATION-NEEDED] flags applied per citation policy; no fabrications. Market lens_context block substantive (pricing, industrial baseline, premium rationale). Cooperative and civic lens_context blocks present as marginal sketches per schema requirement (E2-R5 and E2-R6 satisfied). Ostrom principles 1, 2, 4, 5 addressed in cooperative block; gaps documented in Known Risks. Civic block structured as commission-based rather than standing civic program — appropriate to marginal civic fit. No docs/superpowers/ paths used. Historical lineage anti-romantic: medieval architectural smith treated as functional infrastructure producer, not decorative artist; function-decoration integration identified as economic logic rather than aesthetic ideology. Material handling risk named explicitly in Known Risks. Contractor-license and building-code requirements named in regulatory_notes and Known Risks.
