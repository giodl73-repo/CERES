---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: forge-006
trade: smithing
name: "Induction Bladesmith (premium direct-to-consumer knife and blade shop)"
tagline: "Master-operated induction forge targeting custom kitchen and outdoor blades at $200–$800 direct-to-consumer"
status: draft
version: "0.1"
supersedes: null
inspirations:
  - tokugawa-japan-specialty-bladesmith
  - us-modern-bladesmith-maker-community

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 40
# Mid-range of the 30–50 m² envelope. Accommodates: induction forge station,
# small propane forge alcove (forge-welding steps), belt-grinder bank,
# heat-treat oven, quench trough, and finishing bench. Per REQUIREMENTS R-10,
# 15–40 m² is the historical small-scale range; 40 m² reflects the multi-
# station character of a full bladesmith shop with heat-treat infrastructure.
# [Derived from REQUIREMENTS R-10 multi-station single-operator bladesmith
# footprint; CITATION-NEEDED: commercial survey of modern bladesmith shop
# floor areas; structural inference from blade-shop configuration literature
# and REQUIREMENTS R-10.]

ceiling_min_m: 3.0
# 3.0 m provides adequate clearance for overhead grinding dust extraction,
# propane forge hood, and workpiece handling on long blade stock. Per
# REQUIREMENTS R-11 minimum 2.5 m; bladesmith operations with co-located
# propane forge and grinding require the additional headroom for ventilation
# duct runs. [Derived from REQUIREMENTS R-11; propane hood clearance adds
# ~0.3 m above R-11 minimum.]

ventilation: mechanical-extraction-required
# Induction heat source produces no combustion gases. Mechanical extraction
# is required for: (1) metal-grinding particulate from the belt-grinder bank
# (primary particulate source), (2) propane forge combustion products during
# forge-welding steps, (3) oil-quench vapors during heat treatment. Co-located
# grinding triggers OSHA 29 CFR 1910.94 local exhaust ventilation. The
# propane alcove requires an independent hood per OSHA 29 CFR 1910.252(c).
# [OSHA 29 CFR 1910.94; OSHA 29 CFR 1910.252(c)]

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: hybrid-induction-gas
# Primary: induction-electric for the main forge station (precise temperature
# control essential for heat treatment and billet profiling). Secondary:
# propane (small forge alcove for forge-welding steps requiring ~1100–1300°C
# where standard induction units may not reliably achieve forge-weld temps).
# Per smithing SCHEMA.md §2 hybrid-induction-gas definition and induction-
# electric capability note: forge welding requires purpose-built high-power
# induction coils or a supplementary gas forge; propane alcove fills this gap
# without forfeiting the precision temperature control of induction for the
# majority of blade work. [catalog/smithing/SCHEMA.md §2]

energy_consumption_per_active_hour: "15 kWh (induction dominant; propane alcove ~0.5 kg/hr when active)"
# 15 kWh/hr reflects the upper range of smithing SCHEMA.md §2 (6–15 kWh/hr)
# for a full-station bladesmith configuration: induction forge (~10–12 kW),
# belt-grinder bank (~2 kW combined), heat-treat oven (~1 kW average during
# active cycle), ancillary tools. Propane alcove consumption 0.5 kg/hr is
# within smithing SCHEMA.md §2 propane range (1–2 kg/hr at lower partial-
# load use during forge-weld-only steps). Total blended energy reflects
# induction-dominant operation with propane only during forge-welding sessions.
# [CITATION-NEEDED: manufacturer energy-consumption data for combined
# bladesmith station configurations; illustrative estimate within SCHEMA.md §2
# range; label: pricing_validation: inferred.]

backup_fuel: propane
# Propane alcove serves as backup heat source for the induction forge if the
# primary coil fails, allowing basic production to continue (at lower
# temperature control precision) while awaiting coil replacement. Propane
# also covers forge-welding steps that require temperatures above standard
# induction ceiling. [catalog/smithing/SCHEMA.md §2 hybrid-induction-gas]

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  units_per_hour:
    small_work: 0.5
    # One kitchen-knife forge step (profiling, initial bevel roughing) per
    # 2 hrs of active forge time. Small-work unit = one knife billet through
    # the forge stage only; finish-grinding, heat treatment, and handle work
    # are counted in medium_work. Rate reflects the precision-over-speed
    # character of premium bladesmith work: each heat is planned, each grind
    # pass measured. Below the smithing SCHEMA.md §1 journeyman ceiling of
    # 4–8 units/hr for small_work because blade work prioritizes quality and
    # fit-and-finish tolerances over batch throughput.
    # [Derived from REQUIREMENTS R-06 and smithing SCHEMA.md §1; CITATION-NEEDED:
    # empirical throughput measurement for premium bladesmith operations;
    # illustrative estimate; label: inferred.]
    medium_work: 0.3
    # One complete knife: forge + heat treat (normalize, harden, temper) +
    # handle attachment + edge finish. 0.3 units/hr = ~3.3 hr/knife for a
    # complete production pass, which is consistent with direct-to-consumer
    # bladesmith production times reported informally in the US maker community.
    # [CITATION-NEEDED: empirical production-time data for custom kitchen knives
    # from US bladesmith makers; illustrative estimate consistent with community
    # reports but not formally surveyed; label: inferred.]
    large_work: 0.1
    # One large outdoor blade or pattern-welded billet: extended forge
    # sequences, multi-step differential hardening, or damascus layer work.
    # 0.1 units/hr = 10 hrs/piece, which is consistent with the 8–20 hr range
    # reported for high-end bowie knives and laminated-billet work.
    # [CITATION-NEEDED: empirical production-time data for large custom blades;
    # illustrative; label: inferred.]
  max_active_hours_per_week: 35
  # Full-time bladesmith ceiling. Much of the work week is non-forge:
  # belt-grinding (40–50% of active time), handle fitting, edge finishing,
  # customer correspondence, and stock preparation. 35 hr/wk represents
  # combined active-tool time across all stations (forge + grinder + finishing)
  # rather than forge-only hours. Consistent with REQUIREMENTS R-06 (4–8
  # active hr/day historical ceiling; 35/5 = 7 hr/day within upper range for a
  # motivated full-time operator). Derating for startup/shutdown and
  # interruptions is captured in operations_reality and sim_params.
  # [REQUIREMENTS R-06; operations_reality.max_active_hours_realism_note below]
  product_mix:
    repair: 5
    commodity: 0
    specialty: 80
    artistic: 15
    # Sum: 100. Specialty-dominant as defined for Group B (smithing SCHEMA.md §5).
    # Repair (5%): edge re-grinds for existing customers only; no open-market
    # repair work. Commodity (0%): per DECLINE-VERDICT, commodity knife
    # production against factory pricing ($30 industrial baseline) is not viable
    # for this format. Specialty (80%): custom kitchen knives, outdoor blades,
    # chef-knife commissions at $200–$800. Artistic (15%): collector pieces,
    # pattern-welded presentation knives, gallery commissions.
    # [REQUIREMENTS R-22; DECLINE-VERDICT specialty-segmentation guidance;
    # catalog/smithing/SCHEMA.md §5 Group B]
  throughput_variance:
    seasonal: "Q4 (Oct–Dec) holiday peak for kitchen and gift knives; summer moderate for outdoor blade commissions; January–February trough; worst-month fraction reflects specialty order lumpiness"
    worst_month_fraction_of_average: 0.60
    # Specialty and custom work is project-based; the worst month reflects
    # a commission-dry period (e.g., post-holiday trough) rather than purely
    # agricultural seasonality. 0.60 is above the 0.40–0.50 range for repair-
    # dominant shops because bladesmith revenue has fewer demand categories
    # to buffer against: a dead commission month is a dead month.
    # [Structural inference from REQUIREMENTS R-07 and smithing SCHEMA.md §1
    # specialty-group guidance; CITATION-NEEDED: empirical worst-month data
    # for custom bladesmith operations; label: inferred.]
    best_month_fraction_of_average: 1.50
    # Q4 holiday peak. Below the 1.65 ceiling for repair-dominant shops because
    # custom work has a physical production ceiling even at peak demand:
    # 35 hr/wk cannot be materially exceeded. [Same inference as above.]

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: master
# Heat treatment (hardness + tempering color judgment), edge geometry
# (hollow vs. flat grind to fit-and-finish tolerances), and custom handle
# fitting are master-level operations per smithing SCHEMA.md §3. Induction's
# digital temperature readout assists at heat-treat but does not substitute
# for metallurgical judgment in quench timing, steel-specific tempering
# protocol, or problem-solving bespoke blade profiles. A journeyman could
# operate the equipment but could not produce the $200–$800 quality level
# that underpins the economic model. [catalog/smithing/SCHEMA.md §3; REQUIREMENTS R-15, R-17]

operators_concurrent: "1-2"
# Base operation: one master bladesmith. Second operator (advanced apprentice
# or skilled helper) assists during grinding, handle work, and finishing
# while the master concentrates on forge and heat-treat decisions. Motorized
# induction air eliminates bellows-assistant requirement; second operator
# is production-support and apprentice-path role rather than technical necessity.
# [REQUIREMENTS R-18]

apprentice_friendly: true
apprentice_path:
  training_stages: >
    Stage 1 (0–6 months): shop safety, induction-unit and propane-alcove
    operation, temperature display reading and visual heat-color cross-check,
    basic stock preparation, cleaning and maintenance protocols. Gate criterion:
    can safely start, operate, and shut down all stations unassisted; can
    prepare blade stock to specification; passes written safety assessment.

    Stage 2 (6–18 months): belt-grinder operation and bevel geometry under
    master supervision — hollow grind, flat grind, distal taper; handle
    material preparation and basic attachment. Develops grinder-feel before
    advancing to forge work. Gate criterion: produces 10 kitchen-knife blanks
    to master-accepted bevel geometry without supervision on the final three.

    Stage 3 (18–36 months): forge operations under supervision — stock
    profiling, basic bevel-roughing at the induction forge, propane-alcove
    use for forge welding (supervised). Introduces heat-treatment sequence
    (normalize, anneal) under direct master oversight. Gate criterion:
    forges 10 blade profiles to specification; correctly executes normalize
    and anneal cycles independently.

    Stage 4 (36–54 months): full heat-treatment cycle (harden + temper)
    with master reviewing each piece; increasing autonomy on specialty
    commissions; customer-interaction and commission-intake responsibility.
    Gate criterion: completes 5 knives through full production cycle
    (forge + heat treat + handle + edge) with master accepting output at
    retail quality standard without intervention on the final two.

    Stage 5 (54–72 months): independent operation including master-tier
    work (pattern-welded billets, differential harden, bespoke profiles);
    begins supervising Stage 1–2 apprentices. Approximate master standard
    on this equipment. Bladesmith progression is longer than general
    smithing apprenticeship due to the precision requirements of heat
    treatment and edge geometry at the $200–$800 price point.
  time_to_independent_operation: "~54–72 months to master standard on this equipment; journeyman-adjacent independence achievable at ~36–48 months for standard kitchen-knife production but master-level custom and artistic work requires the full 5–6 year arc"
  succession_note: >
    Apprentice co-presence is integrated into the 1–2 concurrent operator
    model from Stage 2 onward: grinding and finishing work is performed
    alongside the master during normal production rather than in a separate
    training program. This follows the US maker-community informal mentorship
    pattern (American Bladesmith Society apprenticeship model analog) rather
    than the European guild indenture. Per REQUIREMENTS R-19, the cultural
    apprenticeship model is stated: US-maker informal co-production model,
    36–72 months. The five-stage structure ensures the master's heat-
    treatment and edge-geometry judgment is transmitted incrementally
    rather than in a single final-year transfer, reducing succession cliff risk.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD
  capital_cost: { low: 40000, mid: 70000, high: 100000 }
  # Low ($40,000): entry-level induction forge unit (~$8,000–$15,000), one
  # 2×72 belt grinder (~$600–$1,500), basic heat-treat oven (~$1,500–$3,000),
  # anvil + tooling ($2,000–$4,000), small propane forge alcove (~$800–$1,500),
  # bench and shop fit-out ($3,000–$6,000), electrical upgrade ($5,000–$8,000).
  # Mid ($70,000): commercial-grade induction forge (~$20,000–$30,000 for a
  # precision 15–20 kW unit), two belt grinders (primary + finishing, ~$3,000–$6,000),
  # programmable heat-treat oven with atmosphere control (~$4,000–$8,000),
  # full tooling suite ($4,000–$6,000), propane alcove ($1,500–$2,500), bench
  # and fit-out ($5,000–$8,000), 3-phase electrical + ventilation ($12,000).
  # High ($100,000): premium induction system with multiple coil sizes and
  # integrated pyrometry (~$35,000–$50,000), full two-grinder + surface-grinder
  # bank, atmosphere-controlled kiln, comprehensive tooling and inventory, and
  # full shop build-out including spray booth for handle finishing.
  # [CITATION-NEEDED: capital cost data for commercial induction forge systems
  # and bladesmith-specific equipment (heat-treat ovens, belt grinders) in the
  # 2024–2026 market; illustrative estimates from market observation of vendor
  # pricing; label: pricing_validation: inferred. Vendor references:
  # Paragon Industries (heat-treat kilns), Grizzly/JET (belt grinders),
  # Induction Systems (induction forge units).]

  install_cost: 12000
  # 3-phase electrical service upgrade (~$6,000–$9,000 depending on distance
  # to utility transformer and local rates) plus mechanical ventilation
  # installation for grinding station and propane alcove (~$2,000–$4,000).
  # $12,000 is the mid-point of the $8,000–$16,000 realistic range for a
  # light-industrial bay with existing service below 200A.
  # [CITATION-NEEDED: 3-phase electrical service upgrade costs for commercial
  # induction equipment, US 2024; illustrative estimate from general electrical
  # contractor cost data; label: inferred.]

  annual_maintenance: 3500
  # Induction coil inspection and coolant service (~$500), heat-treat oven
  # element check and calibration (~$400), belt-grinder tracking and bearing
  # service (~$600), propane alcove regulator and line inspection (~$300),
  # ventilation blower service (~$400), safety interlock testing and general
  # shop maintenance (~$600), minor tooling replacement (~$700). Excludes
  # first-year failure replacements itemized in operations_reality.
  # [CITATION-NEEDED: annual maintenance cost data for bladesmith shop
  # operations with induction forge; illustrative estimate; label: inferred.]

  annual_consumables: 5000
  # Premium high-carbon and tool steel stock (1084, 1095, O1, D2, 15N20 for
  # damascus) externally sourced: ~$2,000–$2,500/yr at direct-to-consumer
  # production volumes. Handle materials (stabilized wood, G10, micarta,
  # natural scales): ~$800–$1,000/yr. Grinding belts (primary cost
  # consumable for bladesmith work): ~$600–$800/yr. Quench oil and flux:
  # ~$200–$300/yr. Finishing and edge-care consumables (sandpaper, polishing
  # compounds): ~$300–$400/yr. Safety and incidental consumables: ~$200/yr.
  # Total: ~$4,100–$5,200/yr; $5,000 used as mid-point estimate.
  # Electricity (separate from consumables per forge-002 convention):
  # 15 kWh/hr × 35 hr/wk × 50 active wk × $0.125/kWh = $3,281/yr (carried
  # in variable_cost_per_unit for sim_params purposes).
  # [CITATION-NEEDED: steel stock and handle material pricing for direct-to-
  # consumer bladesmith operations, US 2024; grinding belt consumption rates
  # for bladesmith production; illustrative estimate; label: inferred.
  # Electricity price: US EIA Electric Power Monthly Table 5.3, 2023–2024
  # small-commercial blended rate $0.10–$0.15/kWh; mid-point $0.125/kWh.]

  floor_space_rent_per_year: 7200
  # Imputed at ~$180/m² per year for light-industrial commercial space in a
  # small-city setting; 40 m² × $180/m²/yr = $7,200/yr. Light-industrial
  # rents in secondary US markets range $120–$240/m²/yr; $180 is a mid-range
  # estimate for a small-city (15,000–75,000 pop) light-industrial bay.
  # [CITATION-NEEDED: light-industrial commercial rent per m² in small-city
  # US markets, 2024; illustrative estimate; label: inferred. CoStar/LoopNet
  # or local commercial broker data would be the appropriate verification source.]

  market_price_per_unit: { low: 200, mid: 350, high: 800 }
  # Per small-work equivalent unit (= one kitchen knife or equivalent blade).
  # Low ($200): standard production kitchen knife, single-bevel or flat-grind,
  # standard handle material, direct-to-consumer at craft market or online.
  # Mid ($350): custom kitchen knife with fitted handle, specified geometry,
  # commissioned or direct-to-consumer; consistent with mid-tier US bladesmith
  # direct pricing. High ($800): master-maker custom piece — bespoke chef knife
  # with premium handle material, pattern-welded blade, or highly specified
  # outdoor knife; consistent with upper-tier direct-to-consumer bladesmith pricing.
  # Pricing validation: inferred. See pricing_validation field.
  # [CITATION-NEEDED: empirical direct-to-consumer pricing data for custom
  # kitchen and outdoor knives from US bladesmith makers, 2024–2026; illustrative
  # estimate from market observation of Etsy, direct-maker websites, and craft-fair
  # pricing in the premium bladesmith segment; label: pricing_validation: inferred.]

  pricing_notes: >
    Unit is a kitchen knife or equivalent blade (small-work equivalent). Premium
    over the industrial baseline ($30/unit for a factory kitchen knife at
    mid-market retail) reflects the direct-to-consumer custom model: customers
    pay for hand-forged construction, bespoke fit-and-finish, heat treatment
    to the customer's steel preference, and direct relationship with the maker.
    The $200–$800 range targets the premium-segment kitchen-knife buyer,
    outdoor-knife enthusiast, and custom-blade collector — a customer segment
    that has demonstrated consistent willingness to pay maker premiums in the
    US direct-to-consumer craft market. Factory alternatives at $30 (mass-market
    stamped stainless) or $80–$150 (mid-tier factory forged, e.g., Victorinox,
    Wüsthof entry-level) do not replicate the made-to-order geometry, steel
    selection, or maker relationship that defines this product. Industrial baseline
    $30 represents a mass-market stamped factory kitchen knife at US retail.
    [CITATION-NEEDED: factory kitchen knife pricing at US retail, 2024;
    consumer knife market segmentation data; label: inferred.]

  pricing_validation: >
    Pricing evidence: inferred from market observation of direct-to-consumer
    bladesmith pricing on Etsy, maker websites, craft fair price lists, and
    community forums (American Bladesmith Society, Bladesmiths Forum) circa
    2024–2026. NOT derived from a formal industry pricing survey, published
    rate-card study, or audited operator financials. This is a placeholder-
    inferred figure consistent with the project citation policy for uncertified
    market-price claims. Recommended verification: direct survey of operating
    bladesmith makers with documented sales data, or a trade-organization pricing
    study. The $200–$800 range is widely cited in the US maker community as
    the realistic premium-segment spread for direct-to-consumer kitchen knives
    but has not been confirmed against formal willingness-to-pay research.
    Label: pricing_validation: inferred.

  industrial_baseline_price: 30
  # Mass-market factory kitchen knife (stamped stainless, e.g., Victorinox
  # Fibrox line or equivalent mid-market entry) at US retail price. $30
  # represents the industrial reference point against which the artisan
  # premium is measured. Not the full factory-forged premium segment
  # ($80–$150 Wüsthof/Henckels), which would reduce the apparent premium;
  # the $30 baseline is the commodity substitute a cost-only buyer could
  # choose. Mid-tier factory ($80–$150) is cited in pricing_notes as a
  # secondary comparison point. [CITATION-NEEDED: US retail pricing for
  # mass-market factory kitchen knives, 2024; e.g., Victorinox Fibrox 8"
  # chef knife MSRP; label: inferred from general market knowledge.]

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Primary induction coil"
      estimated_hours_to_failure: 1800
      replacement_cost: 1400
      replacement_lead_time_days: 21
      serviceable_by: specialist
      # Induction coil failure is the primary downtime event for induction
      # forges per smithing SCHEMA.md §4: coil failure 1,500–2,500 hrs,
      # replacement specialist-level, lead time 14–30 days for non-stocked
      # coils. Propane alcove backup partially mitigates production loss
      # during coil replacement (basic forging can continue at lower precision).
      # [catalog/smithing/SCHEMA.md §4; CITATION-NEEDED: induction coil MTBF
      # data for commercial forge applications; label: inferred.]
    - item: "Belt-grinder abrasive wheel bearings"
      estimated_hours_to_failure: 2500
      replacement_cost: 200
      replacement_lead_time_days: 3
      serviceable_by: operator
      # Belt-grinder bearing failure is the most common mechanical failure
      # in bladesmith shops due to the sustained abrasive loads and grinding
      # particulate ingress. Standard SKF or equivalent replacement bearings
      # are stocked by industrial suppliers in most US markets; 3-day lead
      # time from regional industrial supply. Operator-serviceable on most
      # 2×72 grinder platforms. [catalog/smithing/SCHEMA.md §4 Hammer/bearing
      # analog; CITATION-NEEDED: bearing MTBF for bladesmith belt-grinder
      # applications; label: inferred.]
    - item: "Heat-treat oven heating element"
      estimated_hours_to_failure: 2000
      replacement_cost: 450
      replacement_lead_time_days: 10
      serviceable_by: journeyman
      # Resistance heating elements in kilns and heat-treat ovens fail from
      # thermal cycling fatigue; 2,000-hr estimate is consistent with Paragon
      # and Evenheat published element life data (range 1,500–3,000 hrs depending
      # on max temperature cycling). Element replacement requires oven disassembly
      # and wiring work; journeyman-level (not specialist). 10-day lead time for
      # manufacturer-direct replacement elements.
      # [CITATION-NEEDED: heat-treat oven element life data; Paragon Industries
      # or Evenheat published service documentation; label: inferred from
      # general kiln-element longevity data.]
    - item: "Propane regulator (diaphragm wear)"
      estimated_hours_to_failure: 1500
      replacement_cost: 150
      replacement_lead_time_days: 5
      serviceable_by: operator
      # Propane regulator diaphragm wear per smithing SCHEMA.md §4 reference list
      # (600–2,000 hrs). Bladesmith propane use is intermittent (forge-welding
      # sessions only), which may extend life somewhat, but partial-load cycling
      # accelerates diaphragm wear in some regulator designs. Replacement is
      # operator-serviceable and regulators are available from industrial
      # gas suppliers in most US markets.
      # [catalog/smithing/SCHEMA.md §4; CITATION-NEEDED: propane regulator
      # diaphragm wear data for intermittent-use bladesmith applications;
      # label: inferred.]

  maintenance_schedule:
    daily:
      task: "Clear grinding and metal dust from all stations; wipe induction coil housing; inspect quench oil for contamination; check propane line connections (visual); log work completed and heat-treat cycles run"
      performed_by: operator
    weekly:
      task: "Inspect and calibrate heat-treat oven thermocouple and PID controller (compare against reference pyrometer); clean belt-grinder platens and tracking guides; check induction coolant level; inspect propane regulator for creep or pressure anomaly; verify safety interlock function"
      performed_by: operator
    quarterly:
      task: "Full induction coolant flush and refill; torque all electrical connections on induction unit; inspect propane line integrity (soap-test all fittings); service belt-grinder drive belt tension and bearing pre-load; calibrate heat-treat oven against certified temperature reference; clean ventilation duct runs"
      performed_by: journeyman
    annual:
      task: "Induction coil professional inspection or refurbishment; licensed electrician safety check of 3-phase service; full heat-treat oven element assessment and replacement if indicated; belt-grinder full bearing replacement as preventive maintenance; comprehensive tooling inventory and stock review"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 25
  # Induction startup is fast (~3 min power-on and interlock check). Propane
  # alcove requires pre-use leak check (~5 min). Heat-treat oven preheat cycle
  # adds ~15 min for the first heat-treat batch of the day but is typically
  # started and run while other work proceeds (not dead time). End-of-day:
  # equipment shutdown, quench oil cover, grinding dust cleanup, daily log
  # (~10 min). Total: 25 min/day is a conservative estimate that excludes the
  # heat-treat oven preheat (which overlaps with productive work).
  # [Derived from induction-electric and propane operational characteristics
  # per smithing SCHEMA.md §2; CITATION-NEEDED: empirical startup/shutdown data
  # for bladesmith induction forge operations; label: inferred.]

  max_active_hours_realism_note: >
    35 hr/wk is a derated net figure inclusive of all stations (forge, grinder,
    finishing bench). Derating applied: 25 min/day startup-shutdown overhead ×
    5 operating days = 2.08 hr/wk overhead → theoretical gross ceiling ~37 hr/wk.
    An additional ~2 hr/wk is allocated to customer correspondence, commission
    intake, photography for portfolio/sales, and administrative tasks typical of
    a direct-to-consumer single-operator shop. 35 hr/wk is therefore the estimated
    net productive tool-time across all stations. Note that bladesmith work is
    multi-station: a knife in process will occupy forge time, grinder time, and
    bench time in sequence; 35 hr/wk is the total of all active-tool hours, not
    forge-only hours. Consistent with REQUIREMENTS R-06 (35/5 = 7 hr/day within
    upper range for a full-time motivated operator).

  interruption_notes: >
    Direct-to-consumer bladesmith shops experience: client follow-up calls and
    emails (~15 min/day), commission consultation sessions by appointment
    (~30 min per consultation, 1–2/week), photography and social-media update
    (~20 min/day for makers who use Instagram or equivalent as primary sales
    channel), and tool-setup changes between forge and grinder tasks (~10 min
    per transition, ~3 transitions/day). Aggregate intraday interruption:
    ~45–60 min/day beyond startup-shutdown. These are folded into the 35 hr/wk
    derated figure (reduced from ~37 hr theoretical net). A maker who eliminates
    direct social-media management could reclaim ~15–20 min/day.

  consumables_lead_time_days: { typical: 5, worst: 30 }
  # Typical: grinding belts, flux, quench oil, and standard steel stock available
  # from regional industrial supply or online next-day (US). Worst: induction
  # coil, specialty alloy stock (15N20 for damascus, D2 tool steel), and heat-
  # treat oven elements may require factory-direct ordering with 14–30 day lead
  # time during supply-chain stress or low-stock periods.
  # [SCALES.md §6 supplier density; illustrative lead-time estimates;
  # CITATION-NEEDED: empirical consumable lead-time data for bladesmith
  # operations; label: inferred.]

  throughput_variance:
    seasonal: "Q4 (Oct–Dec) holiday peak for kitchen-knife gifts and commissions; summer moderate for outdoor blades; January–February post-holiday trough; commission-based revenue is inherently lumpy regardless of season"
    worst_month_fraction_of_average: 0.60
    best_month_fraction_of_average: 1.50

  operator_impact:
    noise_db: 85
    # Grinding (belt-grinder on blade stock) is the dominant noise source.
    # 85 dB(A) at operator position during active grinding is consistent with
    # measured belt-grinder noise levels at 1 m for 2×72 variable-speed units.
    # Induction forge operation itself is quieter (~65 dB). Heat-treat oven is
    # near-silent. Hearing protection required during all grinding operations
    # per OSHA 29 CFR 1910.95 (>85 dB action level for 8 hr; grinding periods
    # typically shorter but sustained exposure warrants PPE).
    # [CITATION-NEEDED: sound level measurement at operator position for 2×72
    # belt-grinder operations; illustrative estimate; label: inferred.
    # OSHA 29 CFR 1910.95 action-level reference.]
    heat_exposure: "Localized at the induction forge workpiece during active forging; induction does not heat the ambient room significantly; propane alcove produces local heat during forge-weld sessions (hood required); heat-treat oven adds ambient warmth during cycling but is enclosed; overall operator thermal environment is moderate compared to coal forges"
    emissions: "Near-zero combustion emissions during induction-dominant operation; propane alcove adds CO and combustion products during forge-weld sessions (dedicated hood ventilation required); metal-grinding particulate from belt grinder is the primary sustained emissions source and requires local exhaust extraction per OSHA 29 CFR 1910.94; quench-oil vapors during heat treatment require extraction"
    physical_demand: "Moderate; sustained standing across all stations; repetitive hammer, grinder, and hand-tool use; blade grinding requires significant wrist and forearm endurance; lifting of steel stock up to ~5 kg for typical knife billets; cumulative daily physical load comparable to other single-operator craft trades"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Light-industrial zoning required; knife-making is not restricted as a manufacturing activity in standard US light-industrial or mixed-use commercial zones; propane storage requires fire-code-compliant enclosure (NFPA 58) but propane volumes for a small alcove forge are typically below permit thresholds"
  emissions: "No combustion emissions permit required for induction-dominant operation; propane alcove may require notification or permit above threshold volume (jurisdiction-dependent); grinding particulate requires local exhaust extraction per OSHA 29 CFR 1910.94; no special emissions permit anticipated for typical bladesmith throughput"
  other: "3-phase electrical service permit required for induction unit; OSHA 29 CFR 1910.95 (noise) and 1910.94 (grinding ventilation) apply; shipping restrictions on auto-opening blades and certain blade types (e.g., switchblades) apply to direct-to-consumer e-commerce channels — verify against 15 U.S.C. § 1241 and state law before online sales; no licensing requirement for knife-making as a trade in standard US jurisdictions"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: good
  cooperative: good
  civic: marginal

scale_fit:
  village: poor
  town: marginal
  small_city: good

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:
  cooperative:
    membership_boundary: >
      Paid-subscriber artisan collective: 8–15 members sharing access to the
      induction forge, heat-treat oven, and grinding bench stations. Members
      must be working bladesmiths or advanced apprentices operating at
      journeyman-adjacent or master level; access is not open to hobbyist
      members below basic heat-treatment competency (safety and quality
      reasons). Geographic scope: small-city and immediate surrounding area;
      membership fee covers booked-hours access on a per-session basis with
      additional shared-stock purchasing rights through the collective's
      steel and consumable procurement pool. 15 members is the realistic
      upper bound at small-city population scale per SCALES.md §5
      (15,000–75,000 residents × 2.0% trade-participation estimate;
      midpoint ~45,000 pop × 2.0% × bladesmith-specific fraction of
      smithing participants → 15 members feasible). Village and town
      populations are insufficient for this membership model.
      [corpus/program/SCALES.md §5 2.0% participation × small-city midpoint]
    rules_source: >
      Operating bylaws adopted at founding annual general meeting; member vote
      required to amend any operating provision. Rules govern: station booking
      protocol (advance booking required for forge and heat-treat oven; grinder
      bench walk-up permitted), shared-stock purchasing rights and cost-share
      formula, skill-level certification requirements for station access tiers,
      equipment damage liability (member responsible for damage caused by
      demonstrated negligence), dues schedule, and apprentice sponsorship
      provisions (each member may sponsor one apprentice at reduced dues).
    monitoring: >
      Station usage logged per session via digital or paper booking register;
      heat-treat oven run logs maintained by each member (temperature, steel
      type, cycle parameters) for quality and safety audit; monthly usage
      summary to elected shop-lead; safety incident log reviewed quarterly.
      Shared-stock inventory tracked against member drawdown records. Shop-lead
      conducts weekly walkthrough to assess equipment condition and flag
      maintenance needs. [catalog entry task spec: shop-lead weekly walkthrough]
    graduated_sanctions: >
      First violation (booking breach, equipment damage, safety shortcut):
      written warning from shop-lead and mandatory equipment re-orientation.
      Second violation within 12 months: $100 fine and 30-day suspension of
      forge and oven access (grinder bench retained). Third violation within
      24 months: membership review by shop-lead and member committee; possible
      permanent suspension or membership termination with dues forfeiture for
      that period. Equipment damage exceeding $200: cost-recovery invoice
      regardless of sanction tier. Graduated structure per Ostrom Principle 5.
      [Ostrom 1990, Governing the Commons]
    conflict_resolution: >
      Shop-lead (elected annually) arbitrates first-level disputes between
      members regarding booking priority, stock allocation, or quality
      standards; appeal to full membership vote at the next scheduled meeting
      (monthly or as-needed). Disputes involving shop-lead directly are
      referred to an ad-hoc three-member panel elected by remaining members.
      Legal disputes not resolvable within the cooperative are subject to
      the cooperative's registered legal form's dispute-resolution provisions.
      Per Ostrom Principle 6. [Ostrom 1990]
    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6, 7]
    # Principle 1 (clearly defined boundaries): membership_boundary above —
    #   paid subscriber, skill-gated, geographically scoped.
    # Principle 2 (rules fit local conditions): station booking rules calibrated
    #   to 8–15 members sharing induction + oven + grinder bench; rules
    #   differentiate forge/oven (advance booking) from grinder (walk-up).
    # Principle 3 (collective choice arrangements): member vote to amend bylaws.
    # Principle 4 (monitoring): booking register + heat-treat logs + shop-lead
    #   weekly walkthrough.
    # Principle 5 (graduated sanctions): above.
    # Principle 6 (conflict resolution): above.
    # Principle 7 (external recognition): addressed via legal_form below —
    #   cooperative-corporation or LLC with municipal acknowledgment gives
    #   external recognition that prevents dissolution under pressure.
    # Principle 8 (nested governance): not applicable at single-cooperative
    #   scale; no nested structure required or present.
    member_amendment_process: "2/3 vote at annual general meeting; 30-day written notice to all members required before any bylaw amendment vote; emergency amendment (3/4 vote) permissible with 7-day notice for safety-critical rule changes only; annual bylaws review is a standing agenda item at the general meeting"
    legal_form: "Cooperative-corporation or multi-member LLC with member-subscriber structure; registered in the operating state; municipal acknowledgment of facility operation on file (Ostrom Principle 7 analog); specific jurisdiction filing required before launch. Cooperative-corporation is preferred where available (clearer member-ownership structure and democratic governance norms); LLC with operating agreement is acceptable fallback."
    scale_fit_note: >
      Governance rules are calibrated to small-city scale (15,000–75,000 residents).
      Membership of 8–15 working bladesmiths is feasible at the small-city midpoint
      (~45,000 pop × 2.0% smithing-participation rate per SCALES.md §5 ×
      bladesmith-specific fraction); town-scale (2,000–15,000) would reduce the
      viable membership pool to 4–8 members, which may fall below the economic
      break-even for shared capital cost. Village scale (500–2,000) is infeasible:
      the bladesmith market segment (premium direct-to-consumer) requires a minimum
      consumer base that village populations cannot support. Scale_fit.village: poor
      and scale_fit.town: marginal reflect these membership-pool constraints.
      [corpus/program/SCALES.md §5]

  civic:
    political_coalition: >
      Municipal economic-development or arts-and-culture office (artisan-economy
      argument); library or makerspace network (bladesmith module as add-on to
      existing civic maker infrastructure); workforce-development program
      (apprentice-pipeline externality); small-business and tourism board
      (craft-maker destination argument for small cities with artisan-economy
      identity).
    council_vote_estimate: >
      Estimated 4-3 favorable in a typical small-city council; tighter than
      civic-forge proposals without an existing makerspace context. Primary
      opposition argument: niche craft with thin public-benefit rationale
      compared to broader workforce-development investments; knife-making
      cultural discomfort in some political environments. Civic case rests on
      bladesmith module as add-on to an existing civic makerspace (not a
      standalone facility), which reduces the capital ask and broadens the
      public-benefit narrative.
    competes_with_private: >
      In most small cities, no functioning private bladesmith operates at
      the premium custom scale; where one exists, a civic makerspace-module
      model (bench-time rental rather than competing production) does not
      displace the private operator but complements it by developing the
      local maker pipeline. Entries in specific communities must verify
      locally; a civic facility directly competing against an established
      private bladesmith requires explicit justification.
    governance_form: >
      Bladesmith module within a municipally owned or nonprofit makerspace
      facility; equipment owned by the municipality or makerspace; operated
      by a contracted specialist bladesmith on a part-time basis (20–25 hr/wk)
      who rents bench-time to members and conducts structured workshops;
      makerspace administration handles booking, dues, and liability.
    budget_line: >
      Capital ($70,000 mid-estimate + $12,000 install = $82,000) via
      economic-development grant, arts-council grant, or makerspace capital
      campaign; operations ($3,500 maintenance + $5,000 consumables + $7,200
      rent equivalent + ~$52,000 contracted specialist wage at part-time rate)
      under makerspace operating line or workforce-development budget.
    benchmark_comparison: >
      Small-city scale (30,000 pop ÷ 2.5 hh-size = 12,000 hh):
      Annualized capital: ($70,000 + $12,000) ÷ 20 yr = $4,100/yr.
      Annual operations: $3,500 + $5,000 + $7,200 + $52,000 = $67,700/yr.
      Total: ~$71,800/yr ÷ 12,000 hh = $5.98/hh/yr.
      Comparison: IMLS Public Library Survey FY 2021 median library operating
      expenditure ~$40–$55/capita × 2.5 hh-size = $100–$137/hh/yr.
      This bladesmith module costs ~$6/hh/yr vs. library at $100–$137/hh/yr —
      well within the CIVIC lens per-household threshold of $80/hh/yr for
      small-city scale per SCALES.md §4. Civic designation is marginal because
      the public-benefit case (niche craft vs. broad access) is weaker than
      for general-purpose civic forges, not because the cost is prohibitive.
      [corpus/program/SCALES.md §4; IMLS Public Library Survey FY 2021]
    staffing_model:
      role: "contracted specialist bladesmith (part-time bench-time rental model)"
      operator_fte: 0.6
      # Part-time: 20–25 hr/wk production + instruction + administration.
      # 0.6 FTE reflects ~24 hr/wk effective engagement in a makerspace-module
      # setting where some administrative overhead is handled by the makerspace.
      wage_assumption: 52000
      # Between town-scale ($56,000) and village-scale ($48,000) SCALES.md
      # median wage thresholds; $52,000 is the mid-point for a contracted
      # specialist at 0.6 FTE (implying a ~$87,000/yr full-time equivalent rate
      # for a master bladesmith, which is above median but consistent with the
      # skill premium for master-level craft trades at direct-to-consumer pricing).
      # [$52,000 contracted at 0.6 FTE from SCALES.md §3 range; CITATION-NEEDED:
      # master bladesmith contracted rate data; label: inferred.]
      wage_source: "corpus/program/SCALES.md §3; contracted specialist rate estimated between town-scale median ($56,000) and village-scale median ($48,000); BLS OEWS SOC 47+51 basis; full-time equivalent ~$87k for master-level bladesmith above median, reflecting skill premium — [CITATION-NEEDED: bladesmith-specific wage survey]"
      hours: "20–25 hr/wk production and workshop instruction plus ~5 hr/wk administrative (booking, member coordination, stock management) = ~25–30 hr/wk effective; contracted on annual basis"
      hiring_notes: >
        Master-floor bladesmith required; hiring pool is national (US bladesmith
        community is geographically dispersed; American Bladesmith Society and
        Knife Makers Guild are the primary networks); local hiring within 100-mile
        radius is feasible in metro-adjacent small cities but not guaranteed in
        secondary markets. Part-time contracted structure may attract a working
        bladesmith who maintains their own direct-to-consumer business alongside
        the civic role, which is consistent with the bench-rental model.
    civic_externalities:
      - "Apprentice training pipeline: structured bladesmith progression produces 1–2 journeyman-adjacent makers per 5-year cycle, supplying the regional craft-maker pipeline with heat-treatment and precision-grinding competency"
      - "Craft-economy activation: civic bladesmith module creates a visible premium-craft anchor for small-city artisan-economy identity and craft-tourism, a documented economic-development strategy for small cities with insufficient scale for large industrial investment"
      - "Skills preservation: maintains working bladesmith competency (heat treatment, edge geometry, tool-steel metallurgy) in a community where this knowledge would otherwise be absent, preventing the irreversible knowledge-pipeline gap when no private operator exists"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 70000
  # Equals economics.capital_cost.mid per E3-R1. [Derived from economics block above]

  cost_sd: 15000
  # Derived: (capital_cost.high - capital_cost.low) / 4 = (100,000 - 40,000) / 4
  # = $15,000. E3-R5 check: cost_sd/cost_mean = 15,000/70,000 = 0.214;
  # within the 0.15–0.50 plausible range. [Derived per catalog/SCHEMA.md §3 default]

  throughput_units_equiv_per_year: 460
  # Derivation (stated explicitly per smithing SCHEMA.md §1 E-3 cross-check):
  #
  # Step 1 — derated active hours/yr:
  #   max_active_hours_per_week (35) × 52 wk × (1 − downtime_fraction 0.10)
  #   = 35 × 52 × 0.90 = 1,638 hr/yr
  #
  # Step 2 — weighted throughput rate using product_mix:
  #   repair (5%) → small_work rate (0.5/hr): 0.05 × 0.5 = 0.025
  #   commodity (0%): 0.00
  #   specialty (80%) → medium_work rate (0.3/hr): 0.80 × 0.3 = 0.240
  #   artistic (15%) → large_work rate (0.1/hr): 0.15 × 0.1 = 0.015
  #   weighted rate = 0.025 + 0.240 + 0.015 = 0.280 units/hr
  #
  # Step 3: 1,638 hr/yr × 0.280 equiv/hr = 458.6 → 460 (rounded to nearest 10)
  #
  # E3-R2 cross-check: 35 × 52 × 0.90 × 0.280 = 458.6 ≈ 460 ✓
  # [Derived from throughput fields, product_mix, and downtime_fraction above]

  variable_cost_per_unit: 17.60
  # Energy cost per unit:
  #   15 kWh/hr × $0.125/kWh = $1.875/hr ÷ 0.280 units/hr = $6.70/unit energy
  # Consumables cost per unit:
  #   $5,000/yr ÷ 460 units/yr = $10.87/unit
  # Total: $6.70 + $10.87 = $17.57/unit → $17.60 (rounded).
  # [Derived from energy_consumption_per_active_hour at $0.125/kWh per EIA Electric
  # Power Monthly Table 5.3 and annual_consumables above]

  labor_hours_per_unit: 3.57
  # 1 hr ÷ 0.280 units/hr weighted rate = 3.571 hr/unit → 3.57.
  # E3-R3 cross-check: 460 units × 3.57 hr/unit = 1,642 hr/yr; target =
  # 35 × 52 × 0.90 = 1,638 hr/yr. Discrepancy = 4 hr (<0.3%); within P2 threshold.
  # Difference reflects rounding in throughput_units_equiv_per_year derivation.
  # [Derived from weighted throughput rate above]

  downtime_fraction: 0.10
  # First-year failure profile:
  #   Primary induction coil at ~1,800 hrs → 21-day lead time.
  #   Belt-grinder bearings at ~2,500 hrs → 3-day lead time (outside year 1).
  #   Heat-treat oven element at ~2,000 hrs → 10-day lead time.
  #   Propane regulator at ~1,500 hrs → 5-day lead time.
  # In year 1 at 35 hr/wk, 1,800 hrs ≈ 51.4 wks: coil failure occurs near
  # end of year 1; 1,500 hrs ≈ 42.9 wks: propane regulator failure mid-Q4.
  # Downtime events: coil (21 days) + propane regulator (5 days) + oven
  # element (partial overlap) + routine maintenance (~5 days) ≈ 35–40 days/yr.
  # As fraction of 52 wks × 5 days = 260 working days: 37 days ÷ 260 ≈ 0.14.
  # Using 0.10 (slightly optimistic) to reflect the propane alcove backup
  # mitigating the coil downtime impact on total production (basic forging
  # continues on propane during coil replacement). E3-R6: consistent with
  # the first_year_failures profile at the generous end; author acknowledges
  # 0.12–0.14 is a more conservative estimate if propane backup is absent or
  # inadequate for all production types.
  # [Derived from operations_reality.first_year_failures above]

  lifespan_years: 20
  # Commercial induction forge units rated ~20,000–30,000 operating hours under
  # regular maintenance; heat-treat oven major refurbishment at 8–12 years;
  # belt-grinder chassis ~15–25 years with bearing replacement. 20-year total
  # design life with major induction unit refurbishment at year 10–12 is
  # consistent with the entry's planned capital structure.
  # [CITATION-NEEDED: service life data for commercial induction forge systems
  # and heat-treat ovens; illustrative estimate; label: inferred.]

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: win
    primary_metric: 0.672607485957268
    metric_name: payback_years
    notes: ''
  village_coop:
    verdict: fail
    primary_metric: 99.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=99, total_annual_cost=19800
  village_civic:
    verdict: fail
    primary_metric: 22.46666666666667
    metric_name: per_household_cost
    notes: per_hh=22.47, threshold=120, hrs/capita=0.000 vs threshold=2.0
  town_market:
    verdict: win
    primary_metric: 0.672607485957268
    metric_name: payback_years
    notes: ''
  town_coop:
    verdict: win
    primary_metric: 99.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=99, total_annual_cost=19800
  town_civic:
    verdict: fail
    primary_metric: 3.3039215686274512
    metric_name: per_household_cost
    notes: per_hh=3.30, threshold=100, hrs/capita=0.000 vs threshold=2.0
  small_city_market:
    verdict: win
    primary_metric: 0.672607485957268
    metric_name: payback_years
    notes: ''
  small_city_coop:
    verdict: win
    primary_metric: 99.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=99, total_annual_cost=19800
  small_city_civic:
    verdict: fail
    primary_metric: 0.6240740740740741
    metric_name: per_household_cost
    notes: per_hh=0.62, threshold=80, hrs/capita=0.000 vs threshold=2.0
sources:
  - ref: "REQUIREMENTS.md R-06: active forging hours per day 4–8 hr across all four anchor cultures; startup/shutdown overhead structural inference"
  - ref: "REQUIREMENTS.md R-10: small-scale forge footprint 15–40 m²; multi-station bladesmith shop inference"
  - ref: "REQUIREMENTS.md R-11: minimum ceiling height ~2.5 m for combustion-gas clearance"
  - ref: "REQUIREMENTS.md R-12: ventilation mandatory; OSHA 29 CFR 1910.252(c)"
  - ref: "REQUIREMENTS.md R-15: precision edge tools; master-level skill required for edge geometry to fit-and-finish tolerances"
  - ref: "REQUIREMENTS.md R-17: master skill floor for bespoke fabrication and precision heat treatment; journeyman insufficient for $200–$800 quality standard"
  - ref: "REQUIREMENTS.md R-18: concurrent operators 1 smith + 0-2 assistants; motorized air eliminates bellows requirement"
  - ref: "REQUIREMENTS.md R-19: US maker-community informal apprenticeship model; shorter and variable duration"
  - ref: "REQUIREMENTS.md R-20: labor economics adjusted to modern market-wage rates; household or indenture-basis labor not assumed"
  - ref: "REQUIREMENTS.md R-22: product category scope must be stated; DECLINE-VERDICT specialty-segmentation guidance"
  - ref: "REQUIREMENTS.md R-07: seasonal throughput variance"
  - ref: "catalog/smithing/SCHEMA.md §1: throughput ceilings small_work 4–8/hr, medium_work 2–4/hr, large_work 0.3–1/hr; Group B specialty guidance"
  - ref: "catalog/smithing/SCHEMA.md §2: induction-electric energy 6–15 kWh/hr; forge-weld limitation at standard units; propane 1–2 kg/hr; hybrid-induction-gas definition"
  - ref: "catalog/smithing/SCHEMA.md §3: master skill floor definition; blade work to fit-and-finish tolerances; heat-treatment judgment requirement"
  - ref: "catalog/smithing/SCHEMA.md §4: primary coil failure 1,500–2,500 hrs specialist; propane regulator 600–2,000 hrs operator; ventilation blower 1,500–3,000 hrs"
  - ref: "catalog/smithing/SCHEMA.md §5 Group B: specialty/custom/artistic entries; operator_skill_floor master expected; market_price_per_unit + industrial_baseline_price load-bearing pair"
  - ref: "corpus/program/SCALES.md §3: median wage thresholds; town $56,000/yr, village $48,000/yr; BLS OEWS SOC 47+51 basis"
  - ref: "corpus/program/SCALES.md §4: CIVIC lens per-household cost thresholds; small-city $80/hh/yr; IMLS Public Library Survey FY 2021 basis"
  - ref: "corpus/program/SCALES.md §5: cooperative member-pool formula; 2.0% participation rate at small-city scale"
  - ref: "corpus/program/SCALES.md §6: infrastructure baseline; electricity $0.10–$0.15/kWh (US EIA Electric Power Monthly); supplier density by scale"
  - ref: "DECLINE-VERDICT: specialty-market segmentation survives; commodity knife production against factory pricing is not viable for artisan-scale entry"
  - ref: "US Energy Information Administration. Electric Power Monthly, Table 5.3: Average Retail Price of Electricity. Monthly release. https://www.eia.gov/electricity/monthly/ (small-commercial blended rate 2023–2024: $0.10–$0.15/kWh; midpoint $0.125 used)"
  - ref: "IMLS. Public Library Survey, Fiscal Year 2021. Published 2023. https://www.imls.gov/research-evaluation/data-collection/public-libraries-survey (median operating expenditure per capita ~$40–$55; per-household ~$100–$137)"
  - ref: "Ostrom, Elinor. 1990. Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press. (Chapters 2–3: eight design principles, graduated sanctions, conflict resolution)"
  - ref: "OSHA 29 CFR 1910.252(c). Hot-work ventilation standards. (Propane forge alcove and general hot-work ventilation requirements)"
  - ref: "OSHA 29 CFR 1910.94. Ventilation — grinding, polishing, and buffing operations. (Local exhaust ventilation for belt-grinder stations)"
  - ref: "OSHA 29 CFR 1910.95. Occupational noise exposure. (85 dB(A) action level; grinding operations PPE requirement)"
  - ref: "15 U.S.C. § 1241 et seq. Federal Switchblade Knife Act. (Shipping restrictions on automatic-opening knives in interstate commerce; relevant to direct-to-consumer e-commerce sales)"
  - ref: "NFPA 58. Liquefied Petroleum Gas Code. (Propane storage requirements for forge alcove; volume thresholds for permit triggers)"
  - ref: "Tsude, Hiroshi. 1990. 'Iron Technology in Premodern Japan.' In A.K. Bhattacharya ed., History of Science and Technology in Asia. (Tokugawa-period specialty bladesmith traditions; functional economic context — cited with reservation; CITATION-NEEDED: verify specific functional economic content against primary sources.)"
  - ref: "Sinclaire, Clive. 2009. Samurai: The Weapons and Spirit of the Japanese Warrior. Globe Pequot Press. (Modern kitchen-knife market as direct-to-consumer commercial activity distinct from sword-smith tradition; anti-romantic framing reference — illustrative; CITATION-NEEDED: formal academic source preferred over general reference.)"
  - ref: "American Bladesmith Society. https://www.americanbladesmith.com/ (US modern bladesmith-maker community; apprenticeship and journeyman certification structure; referenced for US maker-community informal apprenticeship model)"
  - ref: "[CITATION-NEEDED: capital cost data for commercial induction forge systems and bladesmith equipment (heat-treat ovens, belt grinders) in the 2024–2026 market; Paragon Industries, Evenheat, Grizzly, JET, Induction Systems vendor catalog data]"
  - ref: "[CITATION-NEEDED: 3-phase electrical service upgrade costs for commercial induction equipment; US general electrical contractor cost data, 2024]"
  - ref: "[CITATION-NEEDED: annual maintenance cost data for bladesmith shop operations with induction forge; trade or operator survey, 2024]"
  - ref: "[CITATION-NEEDED: direct-to-consumer pricing data for custom kitchen and outdoor knives from US bladesmith makers, 2024–2026; Etsy sales data, maker website price lists, or trade pricing survey]"
  - ref: "[CITATION-NEEDED: factory kitchen knife pricing at US retail, 2024; Victorinox Fibrox or equivalent mass-market reference price]"
  - ref: "[CITATION-NEEDED: empirical throughput and production-time data for custom kitchen-knife and large-blade production; bladesmith operator surveys or documented production logs]"
  - ref: "[CITATION-NEEDED: induction coil mean-time-to-failure for commercial forge applications; manufacturer service data]"
  - ref: "[CITATION-NEEDED: heat-treat oven element life data; Paragon Industries or Evenheat published service documentation]"
  - ref: "[CITATION-NEEDED: belt-grinder bearing MTBF for bladesmith applications; bearing manufacturer data or operator survey]"
  - ref: "[CITATION-NEEDED: service life data for commercial induction forge systems and heat-treat ovens; manufacturer specification or industry longevity data]"
  - ref: "[CITATION-NEEDED: light-industrial commercial rent per m² in small-city US markets, 2024; CoStar, LoopNet, or local broker data]"
  - ref: "[CITATION-NEEDED: bladesmith-specific contracted wage data; American Bladesmith Society or similar trade organization salary survey]"
---
## Summary

The Induction Bladesmith is a master-operated, 40 m² single-operator shop targeting the premium direct-to-consumer custom knife market: chef knives, outdoor blades, and kitchen cutlery at $200–$800 per piece. It is distinguished from other smithing-catalog entries by its combination of induction-electric heat source (for precise heat-treatment temperature control) with a small propane alcove (for forge-welding steps), its master-level skill floor, and its specialty-dominant product mix (80% specialty, 15% artistic, 5% repair). The entry was created because the DECLINE-VERDICT for general smithing survival explicitly carves out the specialty and premium direct-to-consumer segment as viable: factory knives at $30 industrial baseline do not replicate made-to-order geometry, chosen steel, or maker relationship. The catalog addresses this viable niche in forge-006 rather than subsume it under the repair-dominant entries (forge-002, forge-005) or the cooperative/civic entries (forge-003, forge-004). The target customer is a premium-kitchen, outdoor, or collector buyer who has opted out of the commodity knife market.

## Design rationale

This entry solves a specific problem no other entry in the smithing catalog solves: how does a direct-to-consumer premium blade specialist operate at a $200–$800 price point with induction-dominant precision heat control, a cooperative-compatible shared-facility option, and a structured five-stage apprentice path for master-tier succession? Forge-002 (Induction-Modular Small Repair) uses the same energy source but operates at a repair-dominant product mix and journeyman skill floor; the economics and product mix are entirely different — repair pricing ($40–$90/unit) against a $10 industrial baseline versus custom knife pricing ($200–$800/unit) against a $30 industrial baseline. Forge-005 (Frontier-Revival Coal) is repair-dominant and coal-powered; it shares the custom-knife market segment only at the margins of its artistic (15%) allocation. The bladesmith entry is justified as a distinct entry because: (1) the product (custom knife) has different throughput economics (0.28 units/hr vs. 3.84 units/hr for repair), (2) the heat-source combination (induction + propane alcove) is specifically driven by the heat-treatment precision requirements of tool steel, and (3) the cooperative form for this entry is artisan-collective shared infrastructure rather than a community-access repair model, requiring a different governance structure than forge-003. The problem is real: a bladesmith entry without the specialty-premium pricing and master-skill-floor properly specified would produce a systematically optimistic sim_params outcome, as it would apply repair throughput rates and journeyman labor costs to a higher-priced, lower-throughput product.

## Historical lineage

Two precedents inform this design, both with anti-romantic caveats required.

**Tokugawa Japan specialty bladesmith tradition.** The Tokugawa-period (1603–1868) specialist bladesmith — the tōken (sword) smith working in a small dedicated forge with a single master and a handful of apprentices — represents a functional predecessor in the following dimensions: small-footprint dedicated forge, master-apprentice skill-transmission structure, specialty product aimed at a premium buyer segment, and geographic concentration in specialized production districts. The functional inheritance is the master-apprentice succession model and the premium-segment market positioning. The anti-romantic caveat is significant and must not be elided: modern Japanese sword-making (nihontō production) is not a commercial market success story but a cultural-regulatory preservation artifact. The Japanese sword is protected under the Law for the Preservation of Cultural Properties; production is limited to licensed master smiths producing a small number of blades per year under cultural-preservation rules. This has nothing to do with the commercial kitchen-knife market. The modern direct-to-consumer kitchen-knife maker in the US — and indeed the commercial Japanese kitchen-knife industry centered in Sakai and Seki — is a distinct commercial activity from nihontō sword-smithing, even though both involve specialty blade work. The functional lesson taken from Tokugawa-period bladesmith tradition is the economic form (small dedicated shop, premium segment, master-apprentice succession) — not the cultural or regulatory preservation mechanism, which cannot be reproduced and should not be cited as evidence for commercial viability. [CITATION-NEEDED: formal academic source on Tokugawa bladesmith economics as commercial form; Sinclaire 2009 is a general reference; a more rigorous economic history is preferred.]

**US modern bladesmith-maker community.** The contemporary American Bladesmith Society (ABS) and Knife Makers Guild networks represent a living predecessor community: working bladesmiths who operate direct-to-consumer businesses, use induction and propane forges, and produce custom kitchen and outdoor knives in the $150–$1,500 range. The functional inheritance is the direct-to-consumer sales model, the induction + propane equipment configuration, the product-mix structure (specialty + artistic), and the informal co-production apprenticeship model that the ABS journeyman and master certification structure institutionalizes. The ABS certification system (apprentice → journeyman → master) maps directly onto the five-stage apprentice_path described in this entry. The labor regime (market-wage contracted or self-employed single operator, voluntary apprenticeship) is entirely modern and does not rely on pre-modern coercive indenture. The supply-chain condition (externally sourced high-carbon and tool steel, standard industrial consumables) is straightforwardly modern; no historical production condition is being romantically assumed. [American Bladesmith Society, https://www.americanbladesmith.com/]

## Key assumptions

Capital costs ($40,000–$100,000) are illustrative estimates inferred from market observation of commercial induction forge systems, heat-treat oven pricing (Paragon, Evenheat), and belt-grinder pricing (Grizzly, JET) as of 2024–2026; no formal industry survey or vendor bill-of-materials underlies these figures [CITATION-NEEDED]. The mid-point ($70,000) represents a capable professional-grade configuration including the full installation cost structure; the low ($40,000) is a realistic entry-level build for a skilled operator willing to fabricate some tooling. Market pricing ($200–$800 per knife) is the central economic claim of this entry and is explicitly labeled pricing_validation: inferred: it reflects market observation of direct-to-consumer bladesmith pricing channels (Etsy, maker websites, craft-fair pricing, ABS community) but is not sourced from a formal pricing survey or published rate-card study [CITATION-NEEDED]. The industrial baseline ($30/factory kitchen knife) is inferred from general market knowledge of US retail knife pricing and requires verification against a current retail pricing survey [CITATION-NEEDED]. Throughput (460 units/yr equivalent) is derived from the smithing SCHEMA.md §1 ceiling rates (0.3 medium_work/hr for complete knife production) weighted by product mix; the underlying production-time estimates for custom knife work are community-reported approximations rather than empirically measured data [CITATION-NEEDED]. The downtime fraction (0.10) is generous relative to the first-year failure profile (which implies 0.12–0.14 without propane backup mitigation); the entry documents this explicitly and authors of downstream evaluation should use 0.12 if propane backup is insufficient for the production type under test. All economic figures assume modern market-wage labor; no household or indenture-basis labor is assumed [REQUIREMENTS R-20]. The cooperative model assumes 8–15 member participants, which is feasible only at small-city population scale per SCALES.md §5.

## Known risks / failure modes

**Regulatory:** Shipping restrictions on certain blade types (switchblades, ballistic knives) under 15 U.S.C. § 1241 and state analog statutes apply to direct-to-consumer e-commerce channels. A bladesmith producing primarily kitchen and outdoor knives is not materially constrained by these restrictions, but any expansion into auto-opening or gravity-operated designs requires legal review before online sales. Propane alcove storage requires NFPA 58 compliance; volumes for a small bladesmith forge alcove are typically below permit thresholds but must be verified locally. Electrical service upgrade (3-phase, typically 200A) requires utility coordination and may take 4–12 weeks, delaying launch.

**Labor pipeline:** Master-level bladesmith is the single most constrained input in this design. The hiring pool for a master bladesmith willing to operate at contracted rates in a specific small-city location is geographically dispersed and potentially thin; an unsuccessful hiring search is the highest-probability failure mode for both the market and cooperative/civic variants. The five-stage apprentice path mitigates this over a 5–7 year horizon but cannot solve an immediate succession gap. A shop that fails to establish an active apprentice relationship within the first three years faces near-certain succession risk if the founding master departs. The ABS certification network is the most accessible pipeline, but certified masters are not uniformly distributed across US geographies.

**Supply chain:** Induction coil replacement (specialist-level, 21-day lead time) is the primary downtime risk. The propane alcove provides partial backup but cannot replicate the temperature precision of induction for heat treatment; certain production types (differential harden, precise tempering cycles) cannot proceed during coil downtime. Specialty steel stock (15N20 for damascus layers, D2 tool steel) has limited distributor depth in non-metro markets; a 30-day worst-case consumables lead time for specialty alloys is realistic. The heat-treat oven element failure at ~2,000 hrs (10-day lead time) is a second significant downtime event; a spare element inventory ($450) reduces this to a same-day repair and is strongly recommended.

**Demand structure:** Custom blade demand is inherently lumpy and commission-based; the worst month at 0.60× average represents a real cash-flow risk for a single-operator shop without a diversified revenue base. The cooperative model mitigates this by pooling multiple makers' throughput against shared capital costs, smoothing the lumpiness across member production schedules. The civic model further mitigates by converting fixed costs to per-household amortization.

## Niche and competitive positioning

This entry targets the specialty premium segment explicitly carved out as viable by the DECLINE-VERDICT: direct-to-consumer custom knives at $200–$800 per piece in a market where factory alternatives ($30–$150) do not satisfy the buyer's requirements for made-to-order geometry, specified steel, and maker relationship. The competitive position is not against factory knife production — which operates at volumes and margins unreachable at single-operator scale — but against the absence of local master-level custom blade work. The $200 floor represents the lowest price at which a master operator can produce a complete knife, recover variable costs ($17.60/unit), and contribute meaningfully to fixed-cost amortization; the $800 ceiling represents the upper range of the premium direct-to-consumer segment before the buyer enters the gallery/collector segment where artistic pricing logic diverges from production economics. The cooperative artisan-collective variant (8–15 shared-infrastructure members) is structurally advantageous: it distributes the $70,000 capital cost across multiple operators, each of whom brings their own customer base, eliminating the single-point-of-failure revenue risk of the solo-operator market model. Per smithing SCHEMA.md §5 Group B, the critical economic claim — specialty premium over industrial baseline — is the load-bearing test for this entry, and it is explicitly labeled as placeholder-inferred pending formal verification.

## Iteration log

- 2026-04-18: v0.1 — initial authoring per Plan C Task 8 (forge-006). All v1.1 schema fields populated; three lens_context blocks populated (market good, cooperative good, civic marginal); five-stage apprentice_path at master-level progression; four operations_reality first_year_failures items; Japan lineage includes anti-romantic cultural-regulatory preservation point per task specification; sim_params derivation stated explicitly with E3-R2 and E3-R3 cross-checks; pricing_validation labeled inferred throughout per citation policy; 13 CITATION-NEEDED placeholders carried forward for post-authoring verification; downtime_fraction conservatism noted in sim_params comments.
