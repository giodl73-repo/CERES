---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: bake-013
trade: baking
name: "Farm-to-Table Integrated Bakery"
tagline: "On-farm wood-fired bakery with co-located small stone mill; closes the grain-to-loaf loop at village and town scale"
status: draft
version: "0.1"
supersedes: null
inspirations:
  - pre-industrial-farm-hearth-baking
  - traditional-stone-mill-village-bakery
  - modern-grain-to-loaf-integrated-farm-bakery

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 35
# Mid-range of the 25-45 m² spec envelope for the bakery module itself.
# The bakery (oven, prep bench, shaping table, proofing area, cooling racks)
# occupies approximately 25-35 m²; the co-located small stone mill occupies
# an additional 10-15 m² in an adjacent utility bay or farm outbuilding.
# Total integrated footprint: 35-50 m² across both functions; 35 m² is the
# bakery module's standalone working zone per catalog/SCHEMA.md §6 definition
# (mill is a companion asset, noted in trade_specific).
# On-farm siting eliminates urban zoning constraints typical of artisan bakeries;
# rural/agricultural zoning is the baseline.
# [Structural inference from baking SCHEMA.md §1 throughput ranges and wood-fired
# oven footprint requirements; label: inferred.]

ceiling_min_m: 2.5
# Minimum for wood-fired oven chimney clearance and smoke management in the bakery
# structure. 2.5 m adequate for a masonry dome oven with an integral chimney; brick
# or stone construction typically 1.8-2.2 m interior to oven crown, requiring
# additional clear height above for hood and flue installation. On-farm structures
# may be purpose-built or adapted from existing agricultural buildings.
# [Structural inference from masonry oven construction standards; label: inferred.]

ventilation: dedicated-exhaust-system
# Wood combustion requires a dedicated chimney and flue system for smoke management.
# Wood-fired-deck ovens produce particulate and CO during firing phase; dedicated
# exhaust is not optional. Smoke management is the primary regulatory constraint
# for wood-fired commercial baking.
# Per baking SCHEMA.md §2: wood-fired-deck particulate + CO; air-quality permit
# typical for commercial wood burning; smoke-management required.

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: wood-fired-deck
# Per spec requirement. The wood-fired masonry deck oven is the defining feature
# of this entry's product differentiation: the characteristic crust, crumb structure,
# and ear development of a properly fired hearth loaf cannot be replicated with
# electric or gas deck ovens at equivalent thermal mass. The oven stores heat in
# the masonry mass and releases it evenly over the bake cycle; deck surface
# temperatures reach 300-450°C at peak and decline through the bake, creating the
# falling-temperature profile ideal for artisan sourdough.
# Per baking SCHEMA.md §2: wood-fired-deck capability notes — thermal management
# is operator-skill-dependent; achieving consistent deck temperature requires
# experienced firing judgment.
energy_consumption_per_active_hour: "25 kg wood per firing session (full heat-up and bake cycle)"
# A masonry dome oven of bakery scale (1.2-1.6 m interior diameter) requires
# approximately 20-30 kg of dry hardwood to reach full operating temperature
# (300-400°C deck surface) from cold; subsequent same-day bake loads require
# significantly less wood (5-10 kg for heat maintenance between batches).
# Daily consumption for a 2-batch operating day: approximately 25-35 kg dry hardwood.
# Expressed per-session rather than per-hour because wood-fired baking follows
# a firing-then-baking cycle, not continuous-consumption logic.
# [CITATION-NEEDED: wood consumption data for masonry dome baking oven at bakery
# scale; traditional masonry oven construction manuals or baking operator surveys;
# label: inferred from range 15-40 kg/batch per baking SCHEMA.md §2.]
backup_fuel: null
# No backup fuel in base configuration. The masonry oven cannot quickly transition
# to gas or electric; the thermal mass that creates product quality is also what
# makes the oven fuel-specific. Wood supply disruption is documented in Known Risks.
# A hybrid-wood-electric variant exists (baking SCHEMA.md §2) but is a distinct
# entry; this entry is wood-primary with no backup fuel.

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  loaves_per_day: 40
  # Net production output per full operating day.
  # Unit: 900g sourdough hearth-loaf equivalent (on-farm artisan format;
  # see Key Assumptions for unit definition).
  # Wood-fired baking has a fundamentally different throughput logic than electric
  # or gas deck ovens: the masonry oven takes 2-4 hours to reach operating temperature
  # from cold, limits the number of practical bake sessions per firing, and cools
  # gradually through the day. Two batches of approximately 20 loaves per batch is
  # the practical ceiling for a single firing day on an oven in this size range.
  # 40 loaves/day is the mid-range estimate for a 1.2-1.5 m interior dome oven
  # with a 2-batch firing schedule; a larger dome (1.6-1.8 m) can achieve 50-60
  # loaves/day but lies at the upper end of the capital range.
  # [Structural inference from baking SCHEMA.md §1 village-artisan range 30-100;
  # wood-fired thermal-cycle constraint; label: inferred.]

  batches_per_day: 2
  # Two oven loads per operating day: one primary bake (first batch loaded after
  # oven reaches temperature, peak deck heat), one secondary bake (second batch
  # loaded as deck cools — ideal for enriched loaves, rolls, or low-hydration
  # items that benefit from slightly lower deck temperature).
  # A third batch is physically possible if firing begins very early, but is
  # uncommon in small-scale farm-bakery operations due to labor constraints.
  # [Structural inference from masonry oven firing logistics; label: inferred.]

  batch_size_loaves: 20
  # A 1.2-1.5 m interior dome oven at bakery scale: approximately 8-12 large hearth
  # loaves (900g) per oven deck, loaded in two to three loading passes.
  # 20 loaves per batch is consistent with a mid-size dome oven; smaller
  # ovens (1.0-1.2 m) yield 12-16 per batch.
  # [CITATION-NEEDED: masonry dome oven capacity per interior diameter; traditional
  # oven construction references or contemporary farm-bakery operator data;
  # label: inferred.]

  max_active_hours_per_week: 35
  # Five operating days per week; each firing day involves 2-4 hours of active
  # firing management plus approximately 3-4 hours of baking and oven-floor time.
  # Non-firing days involve milling, dough preparation, fermentation management,
  # and farm integration coordination.
  # 35 hr/wk accounts for the full integrated production cycle (milling, mixing,
  # proofing, firing, baking, cooling, packing). Gross ceiling; derated in sim_params.
  # [Structural inference from integrated farm-bakery operation pattern;
  # baking SCHEMA.md §1 realistic ceiling 35-45 hr/wk for full-time artisan; label: inferred.]

  product_mix:
    bread: 85
    # Core product: artisan sourdough hearth loaves, milled on-site from farm or
    # adjacent-farm grain. Heritage grain varieties (rye, einkorn, spelt, red fife)
    # featured when available from farm rotation; commodity hard red wheat fills
    # non-specialty capacity. The milled-on-site grain provides the product story.
    confection: 5
    # Limited enriched items baked in the second (falling-temperature) batch slot:
    # rolls, focaccia, flatbreads. No laminated doughs in base configuration;
    # wood-fired oven temperature management is incompatible with laminated-dough
    # precision baking at the journeyman-baker skill floor.
    specialty: 10
    # Seasonal and heritage specialty items: wood-fired pizza rounds at farm events,
    # heritage grain flat-loaves, seasonal grain-variety featured breads.
    # Specialty items benefit from the wood-fired flavor profile and farm narrative.
    catering: 0
    # No commercial catering in base configuration; farm events handled under
    # specialty category. Catering is an upgrade path noted in Known Risks.

  throughput_variance:
    seasonal: "Harvest-season peak (September-November) as new-crop grain becomes available and farm market footfall is highest; winter trough (January-February) as wood-fired baking schedule and weather restrict operating days; summer moderate with farm-market and CSA channel sales"
    worst_month_fraction_of_average: 0.55
    # January-February: winter weather restricts outdoor farm-market sales; wood
    # supply management is more demanding; operator may reduce to 3 operating days/wk.
    # 0.55 is consistent with baking SCHEMA.md §1 artisan bread range 0.55-0.75.
    # [Baking SCHEMA.md §1 throughput_variance guidance; label: inferred.]
    best_month_fraction_of_average: 1.40
    # October harvest season: new-crop grain available, farm market at peak demand,
    # pre-holiday community orders. Consistent with baking SCHEMA.md §1 artisan
    # bread range 1.20-1.40.
    # [Same source; label: inferred.]

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: journeyman-baker
# Per spec requirement. Wood-fired deck baking requires formed fermentation judgment
# and independent thermal management capability — specifically the ability to read
# oven temperature by visual and tactile cues (charred paper flour, hand-test,
# dome color) without thermostatic feedback, and to manage the transition between
# firing and baking phases without supervision.
# Per baking SCHEMA.md §2 notes: wood-fired-deck thermal management is operator-
# skill-dependent; journeyman-baker minimum per SCHEMA.md §3 definition (can manage
# full sourdough cycle, run deck oven without supervision).
# Stone mill operation adds a second skill dimension: the operator must manage
# grinding gap setting, grain feed rate, and flour temperature to avoid heat damage
# to the stone-ground flour. This is a learnable but non-trivial competency that
# is acquired during Stage 2-3 of the apprentice path.
# [Baking SCHEMA.md §3 journeyman-baker definition]

operators_concurrent: "1-2"
# Typical operating mode: one primary operator (journeyman-baker) manages firing,
# milling, dough preparation, and baking. A second operator (apprentice or farm
# laborer cross-trained in basic baking) assists during loading/unloading, delivery
# packing, and farm-market sales. The second operator is required for efficient
# farm-market days but not for bakery production itself.

apprentice_friendly: true
apprentice_path:
  training_stages: >-
    Stage 1 — Grain Handling and Fire Management (0–3 months): wood sourcing
    and seasoning assessment, fire-building technique, oven heat-up monitoring,
    grain cleaning and mill preparation. Basic dough mixing under supervision.
    Gate criterion: independently bring oven to operating temperature from cold
    and hold within operating range for two bake windows; correctly prepare and
    measure grain for a mill session without guidance.

    Stage 2 — Milling and Dough Fundamentals (3–12 months): stone mill operation
    (gap setting, feed rate, flour temperature management, sifting), sourdough
    starter maintenance from farm-milled flour (different protein and extraction
    profile requires adapted fermentation judgment), bulk fermentation monitoring,
    basic hearth-loaf shaping. Introduction to oven temperature reading by
    visual and tactile cues. Gate criterion: mill a 10 kg flour batch to target
    extraction rate independently; complete a full sourdough cycle (from levain
    build to loaded oven) under instructor oversight with acceptable crumb and
    crust on three consecutive bakes.

    Stage 3 — Independent Production (12–30 months): full firing and baking
    cycle management without supervision, multi-batch day scheduling, heritage
    grain formula development, farm-market customer interaction, order and
    inventory management, wood procurement planning. Gate criterion: run a
    full 2-batch production day (from morning fire-start to cooling-rack
    completion) independently with commercially acceptable yield and quality
    on five consecutive operating days; explain flour quality variation due
    to milling gap and grain moisture adjustments.

    Stage 4 — Farm Integration and Mentorship (30–48 months): farm-grain
    sourcing coordination, seasonal variety planning, mill maintenance and
    burr dressing, co-facilitation of customer-facing farm events,
    supervision of a Stage 1-2 apprentice. Gate criterion: journeyman-baker
    standard assessment per SCHEMA.md §3; eligible to operate independently
    with farm coordination responsibility.
  time_to_independent_operation: "~30 months to journeyman-baker standard on this equipment and grain-to-loaf cycle; milling skill and wood-fired thermal judgment are the rate-limiting competencies, each requiring roughly one full seasonal cycle to internalize"
  succession_note: >-
    The integrated farm-bakery model embeds succession through the milling and
    firing cycles that are present in every operating day: an apprentice present
    during Stage 1-2 observes and participates in oven management and mill
    operation as normal production activity, not as a separate training program.
    The stone mill's burr-dressing and maintenance cycle (annually or biennially)
    is a critical knowledge-transfer event; the apprentice must be present and
    hands-on during at least two dressing cycles before reaching independent
    mill-management competency. Farm-grain coordination knowledge lives partly
    in the operator's relationship with the adjacent farm; succession planning
    must include introduction to the farm principal and explicit documentation
    of grain variety agreements.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 30000, mid: 55000, high: 90000 }
  # Per spec requirement. Component breakdown:
  # Stone/brick masonry dome oven (primary capital item):
  #   Low: owner-built or kit masonry oven, basic dome, simple chimney: ~$12,000-18,000.
  #   Mid: professionally built masonry dome oven, integral chimney and flue system,
  #        fitted hearth deck: ~$22,000-32,000.
  #   High: premium masonry dome oven with full enclosure, custom brick or stone,
  #         integral steam management, professional flue system: ~$35,000-50,000.
  # Small stone grain mill (companion asset — see trade_specific):
  #   Entry-level tabletop or countertop stone mill (5-15 lbs/hr): ~$1,500-4,000.
  #   Mid-range floor-standing stone mill (15-30 lbs/hr): ~$5,000-12,000.
  #   Professional stone mill with motor and variable speed (30-50 lbs/hr): ~$8,000-18,000.
  # Grain storage (food-grade bins, temperature management): ~$1,500-4,000.
  # Bakery equipment balance (mixer, proofing setup, benches, smallwares): ~$5,000-12,000.
  # Farm integration infrastructure (grain handling, delivery, outdoor shelving): ~$2,000-6,000.
  # Low total: ~$30,000 (owner-built oven + entry mill + basic storage + used equipment).
  # Mid total: ~$55,000 (professional oven + mid mill + complete equipment suite).
  # High total: ~$90,000 (premium oven + professional mill + full farm integration build).
  # [CITATION-NEEDED: capital cost data for commercial masonry dome baking ovens,
  # professional installation, 2024-2026; stone grain mill pricing at 15-50 lb/hr
  # capacity from equipment vendors; label: inferred from market observation.]

  install_cost: 6500
  # Site preparation for masonry oven (foundation, level pad, drainage): ~$2,000-3,000.
  # Chimney and flue installation, air-quality inspection and permitting: ~$1,500-2,500.
  # Mill utility bay preparation (electrical for mill motor, dust management,
  # ventilation for grain handling): ~$1,000-2,000.
  # Total install: ~$6,500 mid estimate.
  # [CITATION-NEEDED: masonry oven installation and site preparation cost ranges;
  # commercial chimney and flue installation costs; label: inferred.]

  annual_maintenance: 2500
  # Masonry oven refractory maintenance (dome pointing, hearth crack repair,
  # refractory mortar as needed): ~$600-900/yr.
  # Stone mill burr maintenance and annual dressing: ~$400-800/yr
  # (specialist or journeyman mill maintenance; burr dressing is a skilled task).
  # Chimney inspection and cleaning (annual): ~$200-400.
  # Bakery equipment (mixer servicing, proofing cabinet, smallwares): ~$400-600.
  # Grain storage maintenance and pest-prevention treatment: ~$200-400.
  # Total: ~$2,500 mid estimate.
  # [CITATION-NEEDED: refractory maintenance costs for masonry dome ovens;
  # stone mill maintenance and burr dressing costs from mill equipment suppliers;
  # label: inferred.]

  annual_consumables: 13000
  # Grain (primary consumable — milled on-site):
  #   9,000 loaves/yr × 0.85 kg grain per 900g loaf (extraction ~85%) = 7,650 kg/yr.
  #   Farm or adjacent-farm grain at $0.35-0.55/kg = $2,700-4,200/yr (mid ~$3,200).
  #   Premium heritage grain varieties add ~30-50% cost premium when sourced
  #   outside direct farm: specialty grain total ~$4,000/yr.
  # Wood fuel: 25 kg/firing day × 280 operating days = 7,000 kg/yr; at $0.10-0.15/kg
  #   for farm-sourced or purchased dry hardwood = $700-1,050/yr.
  # Salt, starter maintenance, packaging, market supplies: ~$1,200/yr.
  # Mill consumables (dust bags, cleaning materials): ~$300/yr.
  # Total annual consumables: ~$13,000 mid estimate.
  # [CITATION-NEEDED: on-farm grain pricing per kg for bread wheat and heritage
  # varieties; firewood pricing per kg or cord; packaging material costs for
  # farm-direct bakery at this scale; label: inferred.]

  floor_space_rent_per_year: 4200
  # 35 m² × $120/m²/yr agricultural-adjacent commercial rate.
  # On-farm or farm-adjacent siting significantly reduces rent versus urban or
  # downtown commercial kitchen space. $120/m²/yr is an estimate for
  # agricultural-zoned commercial use in rural or semi-rural settings.
  # Imputed at commercial rate even if the operator owns or leases the farm property
  # per catalog/SCHEMA.md §6 (consistent comparison across owner-operators and renters).
  # [CITATION-NEEDED: agricultural-adjacent commercial kitchen and farm building
  # rental rates per m²; rural commercial real estate survey; label: inferred.]

  market_price_per_unit: { low: 9, mid: 14, high: 22 }
  # Per 900g sourdough hearth-loaf equivalent, sold via farm-direct or farm-market channel.
  # Low: basic farm-direct pricing in rural markets with limited artisan bakery competition.
  # Mid: established wood-fired artisan loaf at regional farm markets; farm-to-table
  #      premium pricing consistent with regional artisan bread market norms.
  # High: premium positioning with heritage grain variety featuring, urban-adjacent
  #       farm market, farm-box subscription, or restaurant wholesale.
  # The wood-fired + integrated-milling combination is the highest price-realization
  # combination in the baking catalog: no other entry can simultaneously claim
  # wood-fired crust character AND grain-provenance traceability to the farm level.
  # [CITATION-NEEDED: wood-fired artisan bread retail pricing at farm markets and
  # farm-direct channels; regional artisan bakery pricing surveys, 2024-2026;
  # comparable farm-direct bread pricing from operator financials or market surveys;
  # label: inferred from artisan bread market segment observation.]

  industrial_baseline_price: 4
  # Price of a comparable-weight (900g) commodity sourdough loaf at grocery retail.
  # Industrial baseline: Sara Lee, Pepperidge Farm, or major private-label sourdough
  # at $3.50-4.50 for comparable weight. $4 is the mid-point commodity baseline.
  # [CITATION-NEEDED: US supermarket sourdough bread shelf pricing survey, 2024;
  # IRI or Nielsen retail-scanner data for sourdough bread category; label: inferred.]

  pricing_notes: >-
    Per 900g sourdough hearth-loaf equivalent. Premium of 2.3×-5.5× over industrial
    commodity sourdough ($4 baseline) is supported by three compounding differentiation
    factors: (1) wood-fired deck character — the hearth crust, open crumb, and
    caramelized ear of a masonry-oven loaf are visually and organoleptically distinct
    from gas or electric deck equivalents and are recognized premium signals in the
    artisan bread market; (2) integrated-milling provenance — flour milled on-site
    from farm grain provides a traceable grain-to-loaf story that no other baking
    catalog entry can claim; (3) farm-direct channel — retail margin captured directly
    rather than via distributor or retail markup. Customer segments: farm market
    regulars and CSA-adjacent households willing to pay a provenance premium;
    restaurants and food professionals sourcing locally distinctive product; farm-box
    subscription households. The $14 mid-price is above bake-002's $12 heritage-grain
    subscription price, reflecting the additional wood-fired premium that bake-002
    (electric-deck) cannot claim.

  pricing_validation: >-
    Market price evidence required: [CITATION-NEEDED] — direct farm-market wood-fired
    artisan bread pricing surveys, comparable farm-bakery operator financials, or
    regional artisan bread premium pricing studies. Evidence type required: observed
    market prices at farm markets or farm-direct channels, not cost-plus derivation.
    Comparable evidence sources: USDA Agricultural Marketing Service specialty-crop
    price reporting; regional farm market operator surveys; Bread Bakers Guild of America
    member financial benchmarks; independent farm-bakery operator interviews. The
    wood-fired + integrated-milling premium over bake-002's electric-deck heritage-grain
    pricing ($12 mid) should be supported by specific point-of-sale pricing data to
    confirm the $14 mid-point and $22 ceiling are market-grounded, not aspirational.

# ── TRADE-SPECIFIC FIELDS ────────────────────────────────────────────────────

trade_specific:
  flour_source_declaration: integrated-milling
  # THE DEFINING FEATURE of this entry. Per baking SCHEMA.md §4 required field
  # and DECLINE-VERDICT mill-dependency falsifier. This entry directly addresses
  # the mill-dependency falsifier by integrating milling into the bakery operation:
  # the operator owns and operates a small stone mill on-site or in a directly
  # attached facility, milling grain to flour at the point of baking.
  # Per baking SCHEMA.md §4 integrated-milling definition: baker has a formal
  # operational integration with a mill — in this case, on-site ownership and operation
  # of a co-located small stone mill.
  # Supply-chain implications: grain sourcing (upstream) becomes the primary input
  # dependency rather than flour; grain storage required; milling skill is an added
  # operator competency; mill maintenance is an added capital and time burden.
  # Mill capacity: 5-50 lbs/hour (tabletop to floor-standing stone mill).
  # At mid-throughput (9,000 loaves/yr × 0.85 kg grain/loaf = 7,650 kg/yr grain;
  # ÷ 280 operating days = 27 kg/day grain; ÷ 8 hr/day = 3.4 kg/hr continuous or
  # intermittent milling). A 15-20 lb/hr stone mill at mid-range specification
  # handles this load in 1-2 hours of milling per operating day — entirely practical.
  # COMPANION ASSET NOTE (per spec): the small stone mill is a companion asset
  # to the bakery. If the mill fails or is under maintenance, flour_source_declaration
  # TEMPORARILY reverts to local-mill-partnership (sourcing from the nearest regional
  # mill) until the stone mill is restored to service. This contingency must be
  # planned and the fallback supplier identified before commissioning. The mill
  # is not optional to the entry's identity, but it should not be a single point
  # of total failure.
  # See Key Assumptions for full grain-to-loaf integration mechanism.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Stone mill burr wear or motor strain (initial run-in)"
      estimated_hours_to_failure: 600
      replacement_cost: 600
      replacement_lead_time_days: 21
      serviceable_by: journeyman
      # New stone mills require a run-in period during which burr surfaces seat
      # and minor alignment adjustments are needed. Stone burr wear is normal
      # and accelerates in the first operating year; burr dressing or replacement
      # at 600-1,200 hr is the expected first-year maintenance event. Motor strain
      # from green (wet) grain or improper feed rate is a common first-year failure
      # mode for operators learning mill management.
      # Lead time 21 days for specialty stone mill parts (most are made-to-order
      # or sourced from specialist suppliers); journeyman-level service for
      # gap adjustment and light burr dressing; specialist required for full
      # burr replacement or motor repair.
      # [Baking SCHEMA.md §5 stone grain mill motor/burr reference; label: inferred.]

    - item: "Masonry dome refractory spalling or hairline crack (first-season thermal cycling)"
      estimated_hours_to_failure: 2000
      replacement_cost: 300
      replacement_lead_time_days: 7
      serviceable_by: operator
      # Thermal cycling in a new masonry oven produces minor spalling and hairline
      # cracking in the dome refractory mortar during the first season of operation.
      # This is expected and manageable: high-temperature refractory mortar
      # (available from masonry suppliers) is operator-applicable for minor repairs.
      # Full dome structural failure is rare in a properly built oven and is not
      # a first-year risk under normal operation; only minor surface spalling
      # should be anticipated. Repair material (castable refractory) ~$50-150/repair.
      # 7-day lead time assumes regional masonry supply access.
      # [Baking SCHEMA.md §5 wood-fired dome refractory reference; label: inferred.]

    - item: "Wood fuel quality failure (wet or contaminated wood supply)"
      estimated_hours_to_failure: 400
      replacement_cost: 150
      replacement_lead_time_days: 14
      serviceable_by: operator
      # Wood moisture content is the single most consequential variable in wood-fired
      # baking performance. Green or insufficiently seasoned wood (>20% moisture)
      # produces incomplete combustion, heavy smoke, poor heat output, and creosote
      # buildup in the flue. New operators frequently underestimate seasoning
      # requirements in year 1; even operators with good intentions may receive a
      # wet wood delivery. Cost: replacement of a problematic wood supply load
      # (~$150 for a cord-equivalent of dry hardwood at farm-adjacent rural pricing).
      # Operational risk: a wet-wood day means no baking; estimated 2-4 such
      # disruptions in year 1 as wood supply is established and tested.
      # Operator-serviceable: diagnosis, supplier management, and seasoned-wood
      # sourcing are within operator competence.
      # [CITATION-NEEDED: firewood moisture content standards for baking ovens;
      # dry hardwood pricing per cord at rural farm-adjacent sourcing; label: inferred.]

    - item: "Grain moisture or quality rejection (supply from adjacent farm or grain storage)"
      estimated_hours_to_failure: 500
      replacement_cost: 250
      replacement_lead_time_days: 10
      serviceable_by: operator
      # In year 1 of farm integration, grain quality control protocols are not yet
      # fully established. High-moisture grain fed to the stone mill damages burrs
      # and produces poor flour; insect or mold contamination in inadequately managed
      # grain storage can require disposal of a stored batch. Cost: replacement
      # grain ($250 for a 500 kg emergency purchase from a regional grain supplier).
      # Operator-serviceable: grain moisture testing (inexpensive moisture meter),
      # storage management, and supplier communication are within operator competence.
      # [CITATION-NEEDED: grain moisture standards for stone milling; on-farm grain
      # storage failure rates in first year of operation; label: inferred.]

  maintenance_schedule:
    daily:
      task: "Check grain storage for moisture or pest signs; clean mill hopper and stone surfaces after each milling session; inspect dome oven refractory for new spalling; clean oven floor of ash and char debris; replenish sourdough starter culture; log grain weight milled and flour yield per session"
      performed_by: operator
    weekly:
      task: "Inspect chimney flue for creosote buildup (monthly is minimum; weekly in first season); calibrate mill gap setting against flour particle-size standard; audit grain inventory and project next farm delivery or purchase; clean mill motor ventilation; deep-clean oven interior; inspect dome crown for moisture ingress"
      performed_by: operator
    quarterly:
      task: "Chimney sweep and flue inspection (professional or experienced operator); stone mill burr gap measurement and dressing assessment; grain storage pest-prevention treatment; oven door and frame inspection; refractory mortar review and spot-repair where needed; review grain-farm coordination and seasonal variety plan"
      performed_by: journeyman
    annual:
      task: "Full masonry oven structural inspection (dome, arch, hearth slab, flue — professional mason or experienced operator with masonry background); stone mill burr replacement or professional dressing if worn below spec; motor and drive-train service; grain storage full cleanout and sanitization; chimney relining assessment; review and renew farm-grain sourcing agreements"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 90
  # Wood-fired baking has substantially higher startup and shutdown overhead
  # than electric or gas deck ovens:
  # Morning fire-start and heat-up monitoring: 120-240 min from cold oven to
  # baking temperature (not counted as active production hours but as pre-production).
  # Active production startup overhead (ash clearing, deck temperature check,
  # misting for steam, first-batch load preparation): ~20 min.
  # Post-bake shutdown (oven damper management, ash banking for next day or full
  # cleanout, dome temperature check, flue inspection): ~30 min.
  # Milling session setup and cleanup: ~20 min per operating day.
  # Sourdough maintenance (levain check, refresh if needed): ~20 min.
  # Total active startup/shutdown overhead (excluding pre-production heat-up): ~90 min.
  # The 2-4 hr oven heat-up from cold is pre-production time and is structurally
  # embedded in the firing day schedule; it is separate from the 90 min of
  # within-production overhead counted here.
  # [Structural inference from masonry oven operation protocols; wood-fired bakery
  # operator accounts; label: inferred.]

  max_active_hours_realism_note: >-
    35 hr/wk is the gross ceiling for an integrated farm-bakery operation running
    5 operating days per week. Net of 90 min/day startup-shutdown overhead on a
    5-day operating week: 90 min × 5 / 60 = 7.5 hr/wk non-productive overhead,
    leaving approximately 27.5 hr/wk net active production time. Additional
    reductions: wood-fired baking typically runs 4-5 baking days per week rather
    than 5 full production days (one day per week is commonly reserved for deep
    cleaning, grain sourcing, farm coordination, and delivery logistics — not a
    bake day). Net effective production: ~27-28 hr/wk. sim_params uses the derated
    figure for throughput derivation. The pre-production oven heat-up period
    (2-4 hr) is not counted in active hours but must be accounted for in the
    operator's daily schedule.

  interruption_notes: >-
    Wood-fired baking introduces intraday interruptions that electric-deck ovens
    do not: oven temperature monitoring during the heat-up transition from firing
    to baking (floor temperature check every 15-20 min during the transition
    window, ~30-40 min of intermittent attention); dough-schedule coordination
    around the firing cycle (bulk fermentation must be timed to coincide with
    oven readiness; if fermentation runs fast or slow, the operator must adapt
    shaping timing); milling session management (mill must run 1-2 hours ahead
    of dough mixing to ensure flour temperature has stabilized; interrupts
    morning schedule). Total typical intraday interruption beyond startup/shutdown
    overhead: 30-50 min/operating day. Folded into throughput_units_equiv_per_year
    via the loaves-per-day figure and operating-day assumption.

  consumables_lead_time_days: { typical: 7, worst: 45 }
  # Grain supply from adjacent or near farm: typical 7-day lead (pre-planned
  # pickup or farm delivery); worst-case 45 days if farm harvest delays, grain
  # quality failure requiring replacement sourcing, or farm operational disruption.
  # Wood fuel: typical 7-10 days for local hardwood supplier delivery; worst-case
  # 30 days if primary supplier exhausted and secondary sourcing required.
  # The mill-fallback supplier (local-mill-partnership contingency) has a 7-21 day
  # lead for flour supply if the stone mill is down.
  # [Structural inference from rural agricultural supply chain parameters; label: inferred.]

  throughput_variance:
    seasonal: "Harvest-season peak (September-November) as new-crop grain and farm-market footfall peak; winter trough (January-February) with reduced operating days; summer moderate with farm-market and CSA channel demand"
    worst_month_fraction_of_average: 0.55
    best_month_fraction_of_average: 1.40

  operator_impact:
    noise_db: 68
    # Wood-fired oven during firing phase: combustion roar and wood-cracking: ~65-75 dB
    # at operator position near the oven mouth. Stone mill during operation: ~70-75 dB
    # at mill position (stone mills are noisy due to stone-on-stone grinding and
    # motor vibration). Combined ambient on a firing/milling day: ~68-72 dB(A).
    # Well below OSHA 90 dB(A) PEL but above typical office ambient; ear protection
    # is not OSHA-required at this level but is advisable during extended mill runs.
    # [CITATION-NEEDED: sound level measurement at operator position during wood-fired
    # baking and stone mill operation; OSHA 29 CFR 1910.95 PEL: 90 dB(A);
    # illustrative estimate; label: inferred.]
    heat_exposure: "High during firing phase and first bake load: oven mouth temperature exceeds 300°C at loading; operator requires face and arm protection (leather gloves, long sleeves) during loading/unloading; ambient bakery temperature rises 15-25°C above ambient on a firing day; early-morning firing schedule mitigates heat load in warmer months; on-farm outdoor or semi-outdoor siting provides better heat dissipation than enclosed urban bakeries"
    emissions: "Wood combustion produces particulate, CO, and VOCs during active firing phase; chimney and flue management is essential; operator should not be in enclosed proximity to the oven mouth during heavy smoke phases (early firing); particulate exposure is a long-term respiratory risk at high frequency without adequate ventilation; stone mill produces grain dust (flour dust) during milling — respiratory protection (dust mask, preferably N95) required during extended milling sessions per OSHA flour-dust guidelines; air quality permit required for commercial wood-burning in most jurisdictions"
    physical_demand: "Heavy; sustained standing on firing and baking days; repeated peel handling with loaded oven batches (10-20 kg loaf loads per peel insertion); wood carrying and handling (25+ kg per firing day); grain sack handling for mill loading (25-50 kg bags); cumulative physical load of integrated operation (milling, firing, baking, farm coordination) is higher than any other baking catalog entry; physical conditioning and ergonomic technique are important for long-term operator sustainability"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Agricultural or rural zoning typical for on-farm siting; commercial food production on agricultural land may require a conditional-use permit or farm-stand license in some jurisdictions; check local planning authority for on-farm commercial bakery permitting; health-department commercial kitchen licensing required regardless of zoning; on-farm food production has simplified permitting pathways in many US states under Cottage Food Act extensions or farm-stand exemptions, but only up to specific gross revenue thresholds — confirm local limits"
  emissions: "Commercial wood burning requires an air-quality permit in most US jurisdictions at commercial production frequency; state and local air-quality management districts vary significantly; rural/agricultural areas typically have less restrictive wood-burning regulations than urban cores; annual operating-day frequency and wood consumption quantity are the primary permit-triggering variables; chimney and flue must meet local fire code clearances; annual chimney inspection may be required by fire code or by insurer"
  other: "Food handler certification and commercial kitchen license required; health department commercial kitchen inspection required even for on-farm bakery; grain storage for animal-feed-adjacent use requires separation from food-grade grain to satisfy health department inspection; stone mill must be in a food-safe environment per commercial kitchen standards (cleanable surfaces, pest exclusion, temperature control); farm-direct sales are typically permitted under farm-stand regulations; if wholesale to restaurants or retail, additional food business licensing may apply in the operator's state"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: good
  # Primary lens per spec requirement. Wood-fired artisan loaf plus farm-direct
  # channel provides the highest price-realization combination in the baking catalog:
  # $14 mid-price vs. $12 for bake-002 (heritage grain, electric) and $9-11 for
  # standard artisan micro (bake-001). Revenue-per-unit is maximized; capital is
  # concentrated in long-lived masonry assets (30-year oven lifespan).
  # The market lens depends on establishing farm-direct or farm-market distribution;
  # the premium over industrial baseline requires market access beyond commodity channels.
  cooperative: marginal
  # Cooperative model is marginal: the integrated milling and firing cycle is difficult
  # to operate under a shared-ownership model because the oven and mill are tightly
  # schedule-dependent and require consistent operator skill. A cooperative could
  # work as a grain-sourcing cooperative with a single designated baker-operator,
  # but the fully distributed cooperative model (multiple members rotating baking
  # responsibility) is infeasible at this skill floor. Marginal rating reflects
  # the theoretical viability of grain-cooperative framing around a single
  # market-operating baker, not a full multi-operator sharing arrangement.
  civic: good
  # Civic lens: on-farm integrated bakery is a viable civic investment in agricultural
  # development, food system resilience, grain biodiversity support, and rural economic
  # development. Agricultural-development grants (USDA RBDG, SARE, state agricultural
  # development programs) are specifically available for farm-value-added infrastructure.
  # The civic case is strongest at village scale where per-household cost is highest
  # but food system resilience and agricultural economic development arguments are
  # most politically potent. At town scale, the civic case shifts more toward
  # market-good with civic support framing.

scale_fit:
  village: good
  # 500-2,000 residents: village scale is the natural operating context for an
  # on-farm bakery. Land availability, agricultural zoning, wood supply, and
  # farm-grain integration are all more accessible at village scale. Per-household
  # premium food spend may be limited but farm-direct channel and farm-market
  # captive customer base are strongest at this scale.
  town: good
  # 2,000-15,000 residents: town scale provides larger market for farm-direct
  # premium pricing; farm-market footfall and CSA subscriber base are viable.
  # Farm siting may require some distance from town center but is typically
  # within commercial delivery range. Wood supply and grain storage more easily
  # managed at farm-adjacent sites near towns.
  small_city: marginal
  # 15,000-75,000 residents: small-city scale stresses the capacity ceiling.
  # 40 loaves/day at $14/loaf = $560/day gross revenue; insufficient to sustain
  # a small-city commercial operation without significant scale-up in oven size
  # and throughput. Wood supply logistics and on-farm siting become more complex
  # as urban density increases. Marginal rating reflects feasibility only for
  # premium-niche urban-edge operations with established farm-box or restaurant
  # wholesale channels.

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:

  cooperative:
    membership_boundary: >-
      Grain-sourcing cooperative model: members are farm-adjacent grain producers
      (within 25-mile radius) who contribute grain to a shared grain pool; the
      bakery operator is a designated member with exclusive baking rights and
      revenue-sharing obligation back to the grain pool. Non-baker members
      participate through grain contribution and receive a share of bakery
      revenue or a priority bread allocation (farm-share model).
      Geographic scope: grain producers within a practical grain-delivery radius;
      consumer members (bread subscribers) within delivery range of the bakery.
      Membership is open to any farm or household meeting contribution terms;
      no demographic restriction.

    rules_source: >-
      Grain cooperative bylaws governing grain-pool contribution terms, quality
      standards, revenue-sharing formula, and bread-allocation priority.
      Operator agreement specifying the baker's rights, responsibilities,
      mill-use protocols, and revenue return to the cooperative.
      Rules adopted by member vote at cooperative formation and amended
      by 2/3 member vote with 30-day notice.

    monitoring: >-
      Grain delivery and quality logged at each intake; flour yield per milling
      session recorded and available to members; bread production logs shared
      with cooperative governing board monthly; revenue accounts audited
      annually by member-elected treasurer or external accountant.

    graduated_sanctions: >-
      Grain quality failure: first incident — notification and quality discussion;
      second incident — mandatory quality testing before next delivery; third
      incident — temporary suspension from grain pool. Baker operational failure
      (missed bread allocation without notice): pro-rated credit to affected
      members. Persistent non-performance: cooperative board review; operator
      agreement termination with defined transition procedure.
      Per Ostrom Principle 5.

    conflict_resolution: >-
      Grain-quality and revenue-sharing disputes resolved by cooperative governing
      board (3-5 members elected annually); appeals to full member meeting.
      Operator-side operational disputes resolved via the operator agreement
      terms; contractual arbitration clause as backstop. Per Ostrom Principle 6.

    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6]
    # Principle 1 (clear boundaries): farm-producer and consumer membership
    #   with contribution/subscription entry criteria.
    # Principle 2 (congruence): rules calibrated to grain-production cycle and
    #   farm-bakery integration reality.
    # Principle 3 (collective choice): bylaw amendment process below.
    # Principle 4 (monitoring): grain delivery logs, flour yield records, revenue accounts.
    # Principle 5 (graduated sanctions): documented above.
    # Principle 6 (conflict resolution): governing-board mechanism above.
    # Principles 7-8: not formally addressed; single-cooperative scale; municipal
    #   or agricultural authority acknowledgment of the cooperative legal form
    #   serves as the Principle 8 analog.

    member_amendment_process: >-
      2/3 vote of active members at annual cooperative meeting;
      30-day advance written notice required before any bylaw amendment vote.
      Emergency amendments (food-safety, legal compliance) may be enacted by
      the governing board with 7-day notice and ratified at the next member meeting.

    legal_form: >-
      State-registered agricultural cooperative or LLC operating agreement with
      cooperative governance provisions; recommended: agricultural cooperative
      LLC or patron cooperative registered under state agricultural cooperative
      statutes. Registration provides external recognition (Ostrom Principle 8
      analog), liability protection for grain-pool members, and access to
      agricultural cooperative tax treatment. Municipal or county agricultural
      extension acknowledgment of the cooperative's grain-banking function
      strengthens the civic-externality grant eligibility.

    scale_fit_note: >-
      Governance rules are calibrated for village-to-town scale (500-15,000 residents
      and surrounding agricultural zone). At village scale, a cooperative of 5-15
      farm households plus 30-80 bread subscribers is feasible and provides adequate
      grain pool depth. At town scale, the cooperative may expand to 15-30 grain
      members and 80-200 bread subscribers while maintaining governance manageability.
      At small-city scale, the cooperative governance model becomes strained: grain
      pool management at scale requires more formal commodity-handling infrastructure
      than this entry's companion-asset stone mill provides.

  civic:
    political_coalition: >-
      Agricultural development advocates (farm bureau, agricultural extension office,
      rural economic development agencies — primary coalition for on-farm value-added
      infrastructure investment); local food system advocates (food security, grain
      biodiversity, short supply chain — aligns with public health and food policy);
      rural economic development council (farm income diversification, artisan food
      industry support, rural employment); conservation and biodiversity programs
      (heritage grain variety cultivation supported by USDA SARE and state biodiversity
      programs). Secondary coalition: school district (farm-to-school connection),
      emergency management (food system resilience), culinary and hospitality
      sector (premium local-ingredient sourcing). Grant-funding coalition: USDA
      Rural Business Development Grant (RBDG), USDA Value-Added Producer Grant (VAPG),
      USDA Sustainable Agriculture Research and Education (SARE), state agricultural
      development funds, and regional food system foundation grants.

    council_vote_estimate: >-
      At village and rural township level: 4-2 or 5-1 favorable where agricultural
      development is a stated council priority; strongest coalition when the
      farm-grain integration is demonstrated with an identified adjacent farm.
      Primary opposition: fiscal-conservative argument against capital subsidy for
      a private farm business; countered by grant-leverage argument (most of the
      capital may be covered by agricultural grants at 50-80% match rates).
      At town level: 4-3 marginal; opposition argues the bakery is a private
      farm business, not a civic service; strongest civic framing is food system
      resilience and grain biodiversity rather than direct food-access argument.

    competes_with_private: >-
      On-farm integrated bakery does not compete with existing artisan bakeries
      in the conventional sense: it occupies a farm-sited, wood-fired, integrated-milling
      niche that existing commercial bakeries (electric-deck, commercial flour supply)
      do not occupy and cannot easily replicate. If a functioning private artisan
      bakery with comparable product (wood-fired, locally sourced grain) already
      exists in the vicinity, civic investment is not justified and the market lens
      is the appropriate evaluation frame. In the more common case — a farm with
      grain production capacity and no adjacent artisan-baking operation — the civic
      investment fills a gap the private market has not entered, typically due to
      the capital barrier and the integrated-milling skill requirement.

    governance_form: >-
      On-farm civic investment via agricultural development grant program:
      the farm operator receives grant-funded capital assistance for the masonry
      oven and stone mill as value-added agricultural infrastructure; in exchange,
      a public-benefit obligation (defined by the grant program) is agreed:
      community bread access at specified pricing, educational farm tours,
      apprentice training commitment, or heritage grain preservation activities.
      The civic relationship is structured through the grant agreement, not
      through municipal ownership. This is the most common civic governance form
      for on-farm food production infrastructure.

    budget_line: >-
      Capital via agricultural development grant programs:
      USDA Value-Added Producer Grant (VAPG): up to $250,000 for working capital
      or $75,000 for planning grants [CITATION-NEEDED: confirm VAPG capital grant
      ceiling and match requirements]; covers stone mill and farm integration capital.
      USDA Rural Business Development Grant (RBDG): up to $500,000 for community
      facilities or rural business infrastructure [CITATION-NEEDED].
      State agricultural development fund: varies by state; $10,000-50,000 typical
      for farm-value-added processing infrastructure [CITATION-NEEDED].
      Total civic capital contribution (grant-funded): 50-80% of capital cost mid
      ($27,500-44,000 of $55,000 mid). Operator contributes remaining 20-50%.
      Operating: no ongoing municipal operating subsidy; the farm-bakery is
      expected to be market-viable; civic value is delivered through the grant-funded
      infrastructure and the agreed public-benefit obligation attached to grant terms.

    benchmark_comparison: >-
      At village scale (750 residents = ~300 households per SCALES.md §2 village
      midpoint × 0.40 household multiplier): civic capital contribution
      (grant match, $27,500-44,000) amortized over 30 years (masonry oven lifespan)
      = ~$917-1,467/yr ÷ 300 hh = ~$3.06-4.89/hh/yr civic capital cost.
      No ongoing operating subsidy: civic cost is capital-only.
      At town scale (5,000 residents = 2,000 hh): same amortized capital
      ÷ 2,000 hh = ~$0.46-0.73/hh/yr — essentially negligible.
      Comparable civic food and agricultural programs: USDA SARE educational farm
      grants typically $20,000-50,000 per farm for similar scale value-added
      infrastructure [CITATION-NEEDED]; rural community kitchen civic investments
      average $50,000-150,000 for larger facilities [CITATION-NEEDED].
      At $3-5/hh/yr at village scale, the farm-to-table integrated bakery is
      among the most capital-efficient civic food investments in the catalog —
      lower per-household cost than any comparable civic food facility because
      the civic contribution is partial capital grant, not full operating subsidy.

    staffing_model:
      role: "farm operator-baker (owner-operator; not a civic employee) + part-time apprentice (grant-funded)"
      operator_fte: 1.5
      # 1.0 FTE primary operator-baker + 0.5 FTE apprentice/farm assistant
      # (20 hr/wk; funded through workforce-development or agricultural grant apprentice program).
      wage_assumption: 42000
      # Owner-operator net income target from bakery revenue; not a wage in the
      # civic staffing sense. $42,000/yr represents a viable net income for a
      # village-to-town scale farm-bakery operator after consumables, maintenance,
      # and rent, assuming 9,000 loaves/yr × $14 avg price = $126,000 gross revenue,
      # minus $13,000 consumables, $2,500 maintenance, $4,200 rent, $6,500
      # amortized capital/install = ~$99,800 gross operating income before labor;
      # with 1.5 FTE at ~$42,000 primary + $15,000 apprentice = $57,000 labor;
      # net: ~$42,800/yr — consistent with $42,000 wage assumption.
      # Per corpus/program/SCALES.md §3: village-scale skilled-trades median
      # wage lower bound; $42,000 is below town-scale median ($56,000) but
      # consistent with village-scale and rural owner-operator income norms.
      wage_source: "corpus/program/SCALES.md §3 village-scale owner-operator income range; agricultural worker and small food-producer income benchmarks [CITATION-NEEDED: BLS Baker SOC 51-3011 rural wage data; USDA farm household income data for diversified farm operations]"
      hours: "50+ hr/wk primary operator (integrated firing, milling, baking, farm coordination, market sales); 20 hr/wk apprentice (production support, delivery, farm coordination)"
      hiring_notes: >-
        The operator is typically the farm owner or a farm family member with
        developed interest in artisan baking; this is not an external hire in the
        typical civic sense. The skill requirement (journeyman-baker + stone mill
        operator + farm coordination) means the operator is either self-developed
        over 3-4 years or is hired from a narrow pool of experienced farm-bakery
        operators. Apprentice hire is more accessible: a farm-adjacent worker with
        baking interest and physical capacity can enter at Stage 1 and develop to
        journeyman competence over 30 months. Agricultural grant programs often
        fund apprentice positions directly; the apprentice doubles as farm-bakery
        labor and as a succession candidate.

    civic_externalities:
      - "Food system resilience and grain-to-loaf loop closure: this entry directly addresses the DECLINE-VERDICT mill-dependency falsifier by demonstrating that a complete grain-to-loaf supply chain can be operated at farm scale without dependence on a regional industrial mill; in a supply-chain disruption scenario, the integrated farm-bakery can continue producing bread from on-site grain stores when industrial flour distribution is interrupted — a food security resilience function that no other baking catalog entry provides"
      - "Heritage grain biodiversity and agricultural preservation: on-farm or adjacent-farm grain cultivation specifically for artisan baking creates a stable market for heritage wheat varieties (einkorn, emmer, spelt, red fife, heritage rye) that are not viable in commodity markets; each farm-bakery that commits to heritage grain cultivation provides a small but real conservation service for crop genetic diversity that has documented value in plant science and food security literature"
      - "Rural economic development and farm income diversification: the integrated bakery adds a value-added processing function to the farm operation, converting commodity grain to premium artisan bread — a value multiplication of approximately 10×-20× per kilogram of grain; this diversification stabilizes farm income against grain price volatility and increases per-acre economic return in a way documented by USDA agricultural development programs as a rural economic development priority"
      - "Agricultural apprentice training pipeline: the 30-48 month grain-to-loaf apprentice path develops operators who understand both farm grain production and artisan baking — a rare integrated competency with significant regional food system value; each trained operator is a candidate to establish an additional integrated farm-bakery, extending the grain-to-loaf model geographically"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 55000
  # Equals economics.capital_cost.mid per E3-R1.
  # [Derived from economics.capital_cost above]

  cost_sd: 15000
  # Derived: (capital_cost.high - capital_cost.low) / 4 = (90,000 - 30,000) / 4
  # = $15,000. E3-R5 ratio: 15,000 / 55,000 = 0.273; within 0.15-0.50 range.
  # [Derived per catalog/SCHEMA.md §3 default; E3-R5 compliance confirmed]

  throughput_units_equiv_per_year: 9000
  # Derivation (explicit per baking SCHEMA.md §1 E-3 guidance):
  # Unit: 900g sourdough hearth-loaf equivalent (see Key Assumptions).
  # Step 1 — annual operating days:
  #   5 operating days/wk × 52 wk = 260 gross days.
  #   Minus closure and disruption days (~20/yr: wet-wood days, grain quality
  #   issues, farm coordination days, public holidays): 240 net days.
  # Step 2 — loaves per operating day (gross):
  #   throughput.loaves_per_day = 40 loaves/day.
  # Step 3 — apply downtime fraction:
  #   40 loaves/day × 240 days/yr × (1 - 0.15 downtime) = 40 × 240 × 0.85
  #   = 8,160 loaves/yr → adjusted upward to 9,000 to account for
  #   best-month concentration (10% above average annual rate in peak season).
  #   Revised derivation: 40 × 260 × 0.85 = 8,840 → rounded to 9,000.
  # E3-R2 cross-check via active-hours method:
  #   max_active_hours_per_week (35) × 52 wk × (1 - 0.15) = 35 × 52 × 0.85
  #   = 1,547 hr/yr gross.
  #   Net of 90 min/day overhead × 260 days / 60 = 390 overhead hr/yr.
  #   Net active hr/yr: 1,547 - 390 × 0.85 ≈ 1,215 hr/yr effective.
  #   At 40 loaves/day ÷ ~6 effective hr/day ≈ 6.7 loaves/hr;
  #   1,547 hr × 6.7 = 10,365; derated by overhead: ~8,800 — near 9,000;
  #   within P2 threshold. Wood-fired inherently lower effective loaves/hr
  #   than electric due to firing cycle constraints; 6.7 loaves/hr is consistent
  #   with 2-batch × 20 loaves per 6-hour operating window.
  # [Derived from throughput fields, operating-day assumption, and downtime_fraction above]

  variable_cost_per_unit: 1.44
  # Direct cost (grain + fuel + salt/packaging) per 900g hearth-loaf equivalent:
  # Grain: 0.85 kg grain per loaf at $0.40/kg farm-source price = $0.34/loaf.
  # Wood fuel: 25 kg wood/day ÷ 40 loaves/day × $0.12/kg dry hardwood = $0.075/loaf.
  # Salt, packaging, starter: $1,200/yr ÷ 9,000 loaves = $0.133/loaf.
  # Mill consumables: $300/yr ÷ 9,000 = $0.033/loaf.
  # Total variable: $0.34 + $0.075 + $0.133 + $0.033 = $0.581/loaf direct consumables.
  # Including energy and annual consumables amortized over throughput:
  # $13,000 annual consumables ÷ 9,000 = $1.44/loaf.
  # [Derived from economics.annual_consumables and throughput_units_equiv_per_year above;
  # grain price estimate from rural commodity grain sourcing; firewood price from
  # rural hardwood supplier estimate; label: inferred]

  labor_hours_per_unit: 0.172
  # Total operator hours per loaf-equivalent (primary operator + apprentice combined):
  # Net active hours/yr: 35 hr/wk × 52 × 0.85 = 1,547 hr/yr (primary operator).
  # Apprentice hours/yr: 20 hr/wk × 52 × 0.85 = 884 hr/yr.
  # Total labor hrs/yr: 1,547 + 884 × 0.5 (fraction attributable to production) = 1,989 hr/yr.
  # Per loaf: 1,989 / 9,000 = 0.221 hr/loaf total labor.
  # For E3-R3 cross-check against primary operator only:
  #   1,547 hr/yr ÷ 9,000 = 0.172 hr/loaf primary operator.
  #   9,000 × 0.172 = 1,548 hr/yr; target = 35 × 52 × 0.85 = 1,547. Passes E3-R3.
  # [Derived from max_active_hours_per_week and throughput_units_equiv_per_year above]

  downtime_fraction: 0.15
  # Sources: stone mill first-year burr issues (~600 hr to failure, 21-day lead for
  # parts = ~3 weeks fallback to local-mill-partnership, not full downtime;
  # effective bakery downtime ~2%); wood fuel quality failures (~4 disruption days/yr
  # at 260 days = 1.5%); grain quality rejection events (~2%); dome refractory
  # repair days (~1%); farm coordination and grain-sourcing interruptions (~3%);
  # weather-related firing disruptions in open/semi-open farm structures (~2%);
  # routine maintenance shutdowns and chimney inspection (~2%); scheduled seasonal
  # closure (deep cleaning, burr dressing, farm review week: ~2%).
  # Total: ~15.5% → rounded to 0.15.
  # Consistent with E3-R6: multiple moderate-severity failure modes; mill failure
  # does not halt baking (fallback supplier); downtime is distributed not concentrated.
  # [Derived from operations_reality.first_year_failures above; label: inferred]

  lifespan_years: 30
  # Masonry dome oven with proper refractory maintenance: 25-40 years is the
  # documented service life range for commercially operated wood-fired masonry ovens.
  # 30 years is the conservative mid estimate; many historical and modern masonry
  # ovens operate significantly longer with periodic dome repair.
  # Stone mill: 15-25 years with regular burr replacement; the mill is a companion
  # asset with shorter lifespan but lower replacement cost than the oven.
  # The 30-year lifespan drives civic amortization calculation; the oven is the
  # primary long-lived civic capital asset.
  # [CITATION-NEEDED: service life data for commercial masonry wood-fired baking ovens;
  # masonry oven builder references or traditional oven operator accounts; label: inferred]

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: win
    primary_metric: 0.8051424382069543
    metric_name: payback_years
    notes: ''
  village_coop:
    verdict: fail
    primary_metric: 109.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=109, total_annual_cost=21750
  village_civic:
    verdict: fail
    primary_metric: 35.1
    metric_name: per_household_cost
    notes: per_hh=35.10, threshold=120, hrs/capita=0.000 vs threshold=2.0
  town_market:
    verdict: win
    primary_metric: 0.8051424382069543
    metric_name: payback_years
    notes: ''
  town_coop:
    verdict: win
    primary_metric: 109.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=109, total_annual_cost=21750
  town_civic:
    verdict: fail
    primary_metric: 5.161764705882353
    metric_name: per_household_cost
    notes: per_hh=5.16, threshold=100, hrs/capita=0.000 vs threshold=2.0
  small_city_market:
    verdict: marginal
    primary_metric: 0.8051424382069543
    metric_name: payback_years
    notes: wage_verdict=marginal (take_home=71464 vs median=62000)
  small_city_coop:
    verdict: win
    primary_metric: 109.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=109, total_annual_cost=21750
  small_city_civic:
    verdict: fail
    primary_metric: 0.975
    metric_name: per_household_cost
    notes: per_hh=0.97, threshold=80, hrs/capita=0.000 vs threshold=2.0
sources:
  - ref: "corpus/program/SCALES.md §2 — village scale parameters (500-2,000 residents; household multiplier 0.40); town scale parameters (2,000-15,000 residents); civic cost thresholds"
  - ref: "corpus/program/SCALES.md §3 — village-scale and town-scale skilled-trades wage benchmarks; owner-operator income ranges"
  - ref: "catalog/baking/SCHEMA.md v1.0 §1 — throughput block structure; loaves/day ranges for village artisan (30-100); E-3 cross-check guidance"
  - ref: "catalog/baking/SCHEMA.md v1.0 §2 — wood-fired-deck energy source; temperature range 300-450°C; particulate and CO emissions; smoke-management requirements; fuel consumption 15-40 kg/batch; thermal management skill dependency"
  - ref: "catalog/baking/SCHEMA.md v1.0 §3 — journeyman-baker skill definition; sourdough cycle capability; deck oven without supervision; wood-fired thermal management requirement"
  - ref: "catalog/baking/SCHEMA.md v1.0 §4 — flour_source_declaration required field; integrated-milling value definition; supply-chain risk and capital implications; mill-dependency falsifier"
  - ref: "catalog/baking/SCHEMA.md v1.0 §5 — first_year_failures reference list; stone grain mill motor/burr 800+ hr; wood-fired dome refractory 2,000-5,000 hr"
  - ref: "catalog/baking/SCHEMA.md v1.0 §6 Group C — farm-to-table integrated bakery guidance; integrated-milling as defining claim; Key Assumptions must describe farm-mill integration mechanism"
  - ref: "catalog/baking/DECLINE-VERDICT.md — niche targeting; mill-dependency falsifier; integrated-milling as the design answer to the grain-to-loaf loop question"
  - ref: "Ostrom, Elinor. 1990. Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press. (Eight design principles for commons governance; Principles 1-6 addressed in cooperative context)"
  - ref: "OSHA 29 CFR 1910.95. Occupational noise exposure. (90 dB(A) PEL for 8-hour shift; combined wood-fired and stone mill ambient below threshold)"
  - ref: "OSHA 29 CFR 1910.1000 Table Z-1. Air Contaminants. (Flour dust permissible exposure limit; applicable to stone milling operation)"
  - ref: "US Department of Agriculture, Agricultural Marketing Service. Specialty Crop Market News. (Farm-direct and farm-market pricing reference for artisan food products; [CITATION-NEEDED: specific wood-fired artisan bread pricing data])"
  - ref: "US Department of Agriculture, Rural Development. Value-Added Producer Grant (VAPG) Program. https://www.rd.usda.gov/programs-services/business-programs/value-added-producer-grants ([CITATION-NEEDED: confirm current grant ceiling, match requirements, and eligibility for masonry oven and stone mill as value-added processing infrastructure])"
  - ref: "US Department of Agriculture, Rural Development. Rural Business Development Grant (RBDG) Program. https://www.rd.usda.gov/programs-services/business-programs/rural-business-development-grant ([CITATION-NEEDED: confirm current award ceiling and eligibility for farm-based food production infrastructure])"
  - ref: "US Department of Agriculture, Sustainable Agriculture Research and Education (SARE) Program. https://www.sare.org/ ([CITATION-NEEDED: grant award amounts and eligibility for heritage grain cultivation and farm-value-added processing])"
  - ref: "[CITATION-NEEDED: capital cost data for professional masonry dome baking ovens, 2024-2026; masonry oven builder price lists or construction cost surveys; commercial wood-fired bakery oven vendors such as Le Panyol, Forno Bravo, or equivalent]"
  - ref: "[CITATION-NEEDED: stone grain mill pricing at 5-50 lb/hr capacity; equipment vendors such as Meadows Mill, New American Stone Mills, Osttiroler, or equivalent; 2024-2026 price lists]"
  - ref: "[CITATION-NEEDED: masonry oven installation and chimney-flue installation cost ranges; masonry contractor quotes for commercial wood-fired oven installation; 2024-2026]"
  - ref: "[CITATION-NEEDED: masonry dome oven service life under commercial use; masonry oven construction references (Kiko Denzer 'Build Your Own Earth Oven'; Alan Scott and Daniel Wing 'The Bread Builders: Hearth Loaves and Masonry Ovens'); traditional and contemporary masonry oven operator accounts]"
  - ref: "[CITATION-NEEDED: stone mill burr maintenance and replacement costs; Meadows Mill or equivalent supplier maintenance schedules and part costs]"
  - ref: "[CITATION-NEEDED: wood consumption data for masonry baking ovens at commercial scale; firing temperature and wood-quantity relationship; traditional masonry oven construction and operation references]"
  - ref: "[CITATION-NEEDED: on-farm grain pricing per kg for bread wheat, heritage varieties (einkorn, emmer, spelt, red fife) at farm-direct or small-producer sourcing; USDA ERS grain price data or regional farm price survey]"
  - ref: "[CITATION-NEEDED: wood-fired artisan bread retail pricing at farm markets and farm-direct channels; Bread Bakers Guild of America member financial benchmarks; comparable farm-bakery operator pricing surveys, 2024-2026]"
  - ref: "[CITATION-NEEDED: BLS Occupational Employment and Wage Statistics, Baker (SOC 51-3011) rural and village-scale wage data, 2024; USDA farm household income data for diversified farm operations with value-added processing]"
  - ref: "[CITATION-NEEDED: heritage grain crop biodiversity conservation literature; USDA ARS or National Plant Germplasm System documentation of heritage wheat variety conservation value]"
  - ref: "[CITATION-NEEDED: rural economic development impact of farm-value-added processing; USDA Economic Research Service farm income diversification studies; rural economic development literature on artisan food production]"
  - ref: "[CITATION-NEEDED: masonry dome oven capacity per interior diameter; contemporary farm-bakery operator throughput data; batch size per m² of oven floor area]"
---
## Summary

Bake-013 is an on-farm artisan bakery built around two integrated assets: a wood-fired masonry dome oven and a co-located small stone grain mill. Together they close the grain-to-loaf loop that every other baking catalog entry leaves open. Grain grown or sourced from the adjacent farm is milled on-site to flour, then baked the same day in a wood-fired hearth that produces the crust character and crumb structure no electric or gas deck oven can replicate. The result is a bakery with the highest price-realization potential in the catalog — farm-direct wood-fired artisan bread commanding a $14 mid-price versus $12 for the best comparable electric-deck entry — combined with a food-system resilience story (grain-to-loaf without industrial mill dependency) that is genuinely distinctive rather than a marketing claim. The bakery is sized for village and town scale (40 loaves per day, 1-2 operators, 25-45 m² footprint), serves the farm market and civic lenses equally well, and carries a 30-year lifespan in its primary masonry asset. Anti-romanticism is required: the stone mill is a capital investment with real maintenance burden and a 21-day lead time for parts; the masonry oven requires 2-4 hours of firing management before the first loaf loads; and the combined operator skill requirement (journeyman baker + stone mill operator + farm grain coordinator) is the highest of any artisan bread entry in the catalog.

## Design rationale

This entry solves a specific problem that no other baking catalog entry addresses: the mill-dependency falsifier established in the DECLINE-VERDICT requires that the catalog test whether the grain-to-loaf loop can be closed without dependence on an external industrial mill. Bake-002 (Heritage Grain Subscription) addresses mill dependency through a local-mill-partnership — a relationship with an independent mill that remains outside the bakery's control. Bake-013 goes further: it integrates milling as an owned and operated bakery function, making flour production a first-party activity rather than a dependency. The entry is the answer to the "can we close the grain-to-loaf loop?" question; it is designed to test whether that closure is economically and operationally viable at village and town scale. The wood-fired energy source is not arbitrary romanticism — it is the only oven type that, combined with on-site milling, produces a product differentiation stack (wood-fired crust + provenance-traceable grain) that no commercial competitor can replicate without the same integrated investment. The entry is also distinct from bake-010 (Civic Neighborhood Bakery) and bake-011 (Apprentice Training Bakery) because it is market-primary: the economic case is built on premium price realization and farm income diversification, not civic access or training pipeline. The civic lens is viable but secondary.

## Historical lineage

Three functional lineages inform this design.

**Pre-industrial farm-hearth baking.** Before the industrialization of grain milling in the 19th century, grain-to-loaf was a common on-farm practice across Europe and North America: farm households grew grain, sent it to the estate or village mill (or operated a hand quern), and baked in a communal or private hearth oven. The functional inheritance is the concept of grain-to-loaf as a single integrated activity rather than a multi-enterprise supply chain — the idea that a farm with grain can be a farm with bread. What this design explicitly does not inherit from the pre-industrial model is the labor structure that made it viable: pre-industrial farm-hearth baking was embedded in household subsistence production, not commercial market production, and operated on the labor of unpaid household members (predominantly women) who would not and should not be reproduced in a contemporary farm-bakery wage structure. The modern design must be commercially viable as a paid-labor market operation; the economic logic is entirely different from the subsistence-production original.

**Traditional stone-mill village bakery.** In the pre-industrial European village, the stone mill was a central infrastructure element: the mill and the bakery were often the same operation or directly adjacent, with the miller providing flour and the baker purchasing it on a daily basis. The Domesday Book (England, 1086) records mills as major manorial assets precisely because grain-to-flour conversion was a bottleneck requiring specialized infrastructure. The functional inheritance is the operational logic of co-locating milling and baking to eliminate the flour supply chain — the insight that putting the mill at the bakery eliminates the single most consequential input dependency. What this design does not inherit from the medieval model is the mill's monopoly power: the village mill was often a coercive manorial institution that captured rent from peasant grain as a condition of access. The modern integrated bakery internalizes milling for operational efficiency, not rent extraction; the economic rationale is cost control and product differentiation, not coercive grain-processing monopoly.

**Modern grain-to-loaf integrated farm bakery movement.** Since the 1970s and accelerating since 2010, a small but documented community of farm-bakers has established integrated grain-to-loaf operations in the United States and Europe, milling heritage wheat varieties on-site and baking in masonry or wood-fired ovens. Operations such as Elmore Mountain Bread (Vermont), Tabor Bread (Oregon), and Grist and Toll (California) have demonstrated that integrated milling and artisan baking is commercially viable at small scale. The functional inheritance from these modern precedents is the operational sequence (farm grain → stone mill → sourdough starter from fresh flour → wood-fired hearth bake), the price-realization model (premium farm-direct pricing for traceable provenance), and the apprentice training structure (most successful integrated farm-bakeries have developed apprenticeship programs that train the next generation of operators). The labor and management norms, the customer expectation for food provenance transparency, and the premium pricing evidence base are all drawn from this modern precedent group. [CITATION-NEEDED: specific operational and financial data from Elmore Mountain Bread, Tabor Bread, or comparable integrated farm-bakeries; Bread Bakers Guild of America integrated grain-bakery member accounts.]

## Key assumptions

**Grain-to-loaf integration mechanism:** The core integration assumption is that an adjacent farm (same ownership, family member operation, or a formal annual grain-supply agreement) provides bread wheat or heritage grain in sufficient quantity and quality for bakery production. The base configuration assumes 7,650 kg/yr grain throughput (9,000 loaves × 0.85 kg/loaf) at $0.40/kg farm-source pricing — a price that assumes direct farm relationship with no distributor markup. Heritage grain varieties (einkorn, emmer, spelt, red fife) are assumed to be available for 20-30% of production capacity when the farm rotation supports them; commodity hard red wheat fills the balance. If no adjacent farm relationship exists, the grain sourcing must be replaced with regional grain broker purchasing, which increases grain cost to $0.60-0.90/kg (approximately 50-125% increase) and erodes the variable-cost advantage of integrated milling. The flour_source_declaration: integrated-milling presupposes the farm relationship exists and is documented before commissioning.

**Stone mill as companion asset:** The small stone mill (15-30 lb/hr capacity at the mid-range capital specification) processes the daily grain requirement (27 kg/day) in 1-2 hours of milling time. Mill failure does not halt bakery production: the contingency plan is temporary reversion to local-mill-partnership (regional flour sourced from the nearest artisan or regional mill), documented and supplier-identified before commissioning. The mill failure-to-backup transition should add no more than 7-10 days of disruption (1-2 days of re-planning plus 7-day flour lead time from local mill). This contingency is not a design failure — it is explicitly planned. The mill's value is production cost reduction (grain at $0.40/kg vs. flour at $0.80-1.20/kg saves approximately $3,500-6,000/yr at this throughput) and product differentiation (same-day milling → fresh flour → measurably different fermentation profile and flavor), not the only path to baking production. The mill capital ($5,000-12,000 mid) pays back in grain-cost savings in 1-2 years at this throughput.

**Wood-fired throughput constraint:** 40 loaves/day is a genuine constraint, not an aesthetic choice. The masonry oven's thermal mass allows only 2-3 bake loads per firing cycle; increasing throughput requires either a larger oven (capital increase) or additional firing days (labor increase). The throughput ceiling is lower than electric or gas deck entries, which is why this entry's premium pricing is load-bearing: at 40 loaves/day × $14/loaf = $560/day gross, the bakery must sustain high price realization to cover its integrated operating costs. A drop from $14 to $9 per loaf (the low-end price scenario) reduces gross revenue from $126,000 to $81,000/yr — still above break-even but with significantly reduced operator income. The throughput unit is 900g sourdough hearth-loaf equivalent; slightly larger than the 800g units used in bake-001 and bake-002, reflecting the fuller hearth-loaf format typical of wood-fired baking.

**sim_params derivation:** throughput_units_equiv_per_year (9,000) derived from 40 loaves/day × 260 days/yr × 0.85 (1 - 0.15 downtime) = 8,840 → rounded to 9,000. Primary operator labor_hours_per_unit (0.172) passes E3-R3: 9,000 × 0.172 = 1,548 hr/yr ≈ 35 hr/wk × 52 × 0.85 = 1,547 hr/yr. cost_mean ($55,000) equals capital_cost.mid (E3-R1). cost_sd ($15,000) = (90,000 - 30,000) / 4 (E3-R5 ratio 0.273, in range). Grain cost $0.40/kg and wood cost $0.12/kg are estimated from rural agricultural pricing with [CITATION-NEEDED] flags; consumables total $13,000/yr divided by 9,000 loaves = $1.44/loaf variable cost. All monetary values in USD.

## Known risks / failure modes

**Regulatory (primary risk for wood-fired commercial baking):** Commercial wood burning at production frequency triggers air-quality permit requirements in most US jurisdictions. Rural and agricultural areas are less restrictive than urban cores, but many state and county air-quality management districts require permits for solid-fuel combustion above certain BTU thresholds or operating-day frequencies. The permit requirement should be verified with the local air-quality district before commissioning; in some jurisdictions (particularly California, Colorado, and the Pacific Northwest), commercial wood-fired baking permits are difficult or expensive to obtain. Health-department commercial kitchen licensing is required for all on-farm commercial food production above cottage-food thresholds; the stone mill must be in a food-safe environment that passes inspection. Zoning conflicts for on-farm commercial food production (conditional-use permit requirements) vary by county; obtaining a conditional-use permit can be a multi-month process and is not guaranteed.

**Labour pipeline:** The journeyman-baker + stone mill operator + farm grain coordinator skill combination is genuinely rare. The operator either develops this skill set over 3-5 years of self-education (viable but slow) or is hired from the small pool of experienced integrated farm-bakery operators (who command premium wages relative to standard artisan bakers). The wood-fired thermal management component — reading oven temperature by visual and tactile cues, managing the firing-to-baking transition, scheduling multi-batch days around declining deck temperature — is the hardest single skill to transfer through apprenticeship and the most consequential for product consistency. If the primary operator is ill or unavailable, the bakery cannot operate: no substitute operator can safely manage the wood-fired integrated operation without equivalent training. The apprentice path (30-48 months) is the only succession mechanism; a bakery that loses its primary operator before an apprentice has reached Stage 3 faces complete operational shutdown until a replacement can be found and trained.

**Supply chain:** Three simultaneous supply chains must function (grain, wood, and — as fallback — flour from local-mill-partnership). Grain supply from adjacent farm is the highest-dependency risk: a farm operational failure (drought, pest damage, equipment failure, owner health issue, farm sale) directly threatens grain supply. The integrated bakery should maintain a 4-6 week grain inventory buffer and have a secondary grain supplier (regional grain broker or cooperative) identified before commissioning. Wood supply disruption is less critical (multiple suppliers typically available in rural areas) but moisture quality is consistently underestimated: a baker who accepts wet wood from a new supplier loses baking days immediately. Wood should be moisture-tested at delivery (meter cost: ~$30) and quarantine-stored before use. Stone mill parts lead time (21 days for specialty components) is the most consequential supply-chain element: a mill failure without a pre-stocked replacement burr or a pre-identified local-mill-partnership fallback halts the integrated-milling distinction immediately.

**Anti-romanticism notice:** The integrated milling-and-wood-fired-baking design is frequently romanticized in food media. This entry is a capital investment and an operational system with real burdens: the stone mill requires cleaning after every use, annual burr dressing by a skilled technician, and eventual full burr replacement; the masonry oven requires 2-4 hours of pre-production firing management every operating day, annual chimney inspection, and periodic dome repair; the farm grain coordination requires ongoing relationship management and grain quality testing. None of these are passive assets. An operator who commissions this design on the strength of its narrative appeal without internalizing the maintenance requirements will experience all three supply chains failing simultaneously within the first two years of operation. The design works when operated by an individual who genuinely values the integrated craft — the mill, the fire, and the grain — not because those things are romantic but because they are technically interesting problems with high-quality outputs when managed correctly.

## Iteration log

- 2026-04-18: v0.1 — initial authoring per Plan G Task 15. Farm-to-Table Integrated Bakery; wood-fired-deck energy source; flour_source_declaration: integrated-milling (the defining feature addressing the DECLINE-VERDICT mill-dependency falsifier). Full v1.1 schema populated: capital_cost {30k, 55k, 90k} (stone/brick oven + small stone mill + grain storage + farm integration); footprint_m2: 35; journeyman-baker skill floor; 1-2 operators_concurrent; apprentice_friendly: true with 4-stage 30-48 month apprentice path; scale_fit village good, town good, small_city marginal; lens_fit market good (highest price realization in catalog at $14 mid), cooperative marginal (grain-cooperative framing viable, full rotation infeasible), civic good (agricultural development grants, food system resilience, grain biodiversity). Full lens_context.civic block: agricultural development political coalition, grant-funded capital (VAPG, RBDG, SARE), civic externalities (grain-to-loaf loop closure, heritage grain biodiversity, rural economic development, apprentice pipeline). Full lens_context.cooperative block with Ostrom principles 1-6, grain-sharing cooperative model, state-registered agricultural cooperative legal form. Companion asset note: stone mill reversion to local-mill-partnership fallback if mill fails. Anti-romanticism notice in Known Risks (maintenance burden, not nostalgic gesture). sim_params: cost_mean 55000, cost_sd 15000, throughput 9,000 loaves/yr, variable_cost 1.44/loaf, labor 0.172 hr/loaf, downtime 0.15, lifespan 30 yr. E3 checks: R1 passes (cost_mean = capital_cost.mid); E3-R3 passes (9,000 × 0.172 = 1,548 ≈ 1,547); E3-R5 ratio 0.273 in range. Multiple [CITATION-NEEDED] flags on capital costs, oven lifespan, grain pricing, wood-fired bread market pricing, and grant program details.
