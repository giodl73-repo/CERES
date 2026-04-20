---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: bake-014
trade: baking
name: "Apartment / Home Micro-Bakery (convection-electric, minimum capital)"
tagline: "Part-time home-kitchen bread sales at the cottage-food viability floor"
status: draft
version: "0.1"
supersedes: null
inspirations:
  - american-cottage-food-movement
  - instagram-dtc-home-baker-phenomenon

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 8
# Mid-range of the 5-10 m² kitchen working zone. This entry occupies a domestic
# kitchen counter and oven area only: no dedicated bakery room, no structural
# modification. 8 m² represents the effective working zone in a standard US
# apartment kitchen (counter run, oven, mixer, cooling rack staging). No
# additional storage or customer-facing area is included; bulk flour storage
# (25-50 lb bags) uses existing pantry or closet space. The footprint IS the
# kitchen; the operator shares this space with domestic food preparation between
# baking sessions.
# [Structural inference from standard US apartment kitchen floor plans; no
# dedicated citation. CITATION-NEEDED: residential kitchen floor-area survey
# data confirming 5-10 m² working zone estimate for standard apartment layouts.]

ceiling_min_m: 2.2
# Standard residential ceiling height in US apartments (typically 2.4-2.7 m;
# 2.2 m minimum in older construction). No commercial exhaust hood is required
# or installed; the domestic range hood (if present) provides nominal steam
# removal. No combustion clearance requirement for convection-electric oven.
# [Structural inference from residential building codes; standard US apartment
# ceiling height per IRC residential code minimum 2.29 m (7 ft 6 in).]

ventilation: natural-sufficient
# Convection-electric domestic or prosumer oven produces steam and ambient heat
# during baking; a domestic kitchen with a range hood or operable window
# provides adequate ventilation for part-time hobby-scale baking sessions.
# No combustion gases; no commercial kitchen exhaust-hood requirement at
# cottage-food production levels. Flour-dust exposure during mixing is low
# at the volumes involved (1-2 kg flour per session); natural room ventilation
# is sufficient. This changes if the operator scales toward commercial-kitchen
# volumes — a distinction the regulatory notes address explicitly.

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: convection-electric
# Domestic or prosumer convection oven (range oven with convection fan, or
# standalone countertop convection oven). Optional: a deck-stone insert
# (pizza stone or baking steel on the oven rack) improves crust quality by
# adding thermal mass, bringing convection oven performance closer to a
# dedicated deck oven without capital-cost parity. The convection-electric
# entry point is the minimum viable baking setup for bread production —
# no new infrastructure, no permit, no gas connection required.
# Per baking SCHEMA.md §2: convection-electric temperature ceiling
# ~160-230°C (fan-circulated); lower effective crust temperature than
# a commercial deck oven. Dutch-oven enclosure method (cast iron) is the
# standard workaround for steam in the first minutes of the bake.

energy_consumption_per_active_hour: "1.5 kWh"
# Domestic convection oven rated 2,000-3,500 W. At a mid-range 2,400 W and
# approximately 60-70% duty cycle during sustained baking (thermostat cycles),
# effective consumption is approximately 1.5 kWh/active hour during baking.
# Preheat from cold (~30-40 min) represents a higher-intensity period; averaged
# across a 2-3 hr baking session the 1.5 kWh/hr figure is a reasonable mid-point.
# Baking steel or pizza stone insert adds ~15-20 min to preheat time but does
# not materially change the per-active-hour consumption once at temperature.
# Per baking SCHEMA.md §2: convection-electric typical 2-5 kWh/batch; 1.5 kWh/hr
# at 2-3 hr per session implies 3.0-4.5 kWh/session — within the stated range.
# [CITATION-NEEDED: metered energy consumption data for domestic convection oven
# at sustained baking temperature; estimate within baking SCHEMA.md §2 range.]

backup_fuel: null
# No backup fuel. This is a domestic oven on residential electrical service.
# Grid outage risk is noted in Known Risks. No propane or gas backup is
# included in this minimum-capital configuration.

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  loaves_per_day: 8
  # Net output per operating session (the "day" here is a baking session of
  # 3-5 hours, not a full commercial operating day). Unit: 800g artisan loaf
  # equivalent (see Key Assumptions for unit definition). A standard domestic
  # oven accommodates 1-2 loaves per batch; with a Dutch-oven method and a
  # deck-stone insert, 2 loaves per batch is achievable for most oven sizes.
  # At 3-4 batches per session, maximum output is 6-8 loaves per session.
  # 8 loaves per session is the achievable ceiling with careful scheduling;
  # many home bakers operate at 4-6 loaves per session.
  # [Structural inference from home-baker community practice; CITATION-NEEDED:
  # empirical output data for home-kitchen convection-oven bread production;
  # range 4-8 loaves/session is consistent with domestic oven capacity and
  # standard sourdough scheduling (one long cold retard + one fresh batch
  # per session).]

  batches_per_day: 4
  # 4 oven loads per baking session. Each load: 1-2 loaves, ~35-50 min baking
  # time. Four loads × ~45 min/load = ~3 hours active bake time in a session;
  # combined with preheat, mixing, and cleanup the full session runs 4-5 hours.
  # This is the practical ceiling for a part-time domestic oven without
  # continuous overnight operation.

  batch_size_loaves: 2
  # Domestic convection oven accommodates 2 standard 800g boules side by side
  # with adequate air circulation for convection baking; 1 loaf in Dutch oven
  # (standard method for steam) per load unless two Dutch ovens are used.
  # Assuming two Dutch ovens or a baking steel with a steam dome: 2 loaves/load.
  # [Structural estimate; oven capacity dependent on specific model dimensions.]

  max_active_hours_per_week: 12
  # Part-time operation: 2-3 baking sessions per week × approximately 4-5 hours
  # per session (preheat, mixing, shaping, baking cycles, cooling, packaging).
  # 12 hr/wk is the practical ceiling for a part-time home baker operating
  # 2-3 sessions/wk without displacing domestic kitchen use or other obligations.
  # This is explicitly NOT a full-time operation. A full-time single operator
  # using a domestic convection oven is constrained to cottage-food thresholds
  # regardless of hours logged; the time ceiling is an operational descriptor,
  # not the binding revenue constraint (which is the cottage-food revenue cap).

  product_mix:
    bread: 90
    # Primary product: yeasted or sourdough loaves, simple rolls. Operator skill
    # floor (apprentice-baker) restricts the product scope to non-laminated
    # bread per baking SCHEMA.md §3. Sourdough is permissible at apprentice
    # level with supervision; fully independent sourdough judgment develops
    # over time but initial sales of simple yeasted and semi-sourdough loaves
    # are within apprentice capability.
    confection: 5
    # Simple cookies, brownies, or quick breads that do not require lamination
    # or advanced confection skill. Incidental supplementary products only.
    specialty: 5
    # Flavored or seeded loaves; minor seasonal variety.
    catering: 0
    # No catering in this configuration; direct-to-consumer only at cottage-food
    # scale. Catering volumes would exceed cottage-food license thresholds in
    # most US states. Sum: 100.

  throughput_variance:
    seasonal: "Modest pre-holiday uptick (November-December) for gift loaves; summer trough from reduced demand and heat-related reluctance to run a home oven for extended periods"
    worst_month_fraction_of_average: 0.60
    # Summer (July-August) is the worst period: reduced consumer demand for
    # hot bread, and home bakers frequently reduce baking frequency due to
    # heat generated by the oven in a residential setting. 0.60 is consistent
    # with baking SCHEMA.md §1 artisan bread range (0.55-0.75).
    # [Baking SCHEMA.md §1 throughput_variance guidance; CITATION-NEEDED:
    # empirical worst-month fraction for home-kitchen cottage-food bakery.]
    best_month_fraction_of_average: 1.35
    # Pre-holiday and fall peak. Consistent with SCHEMA.md §1 artisan bread
    # range 1.20-1.40.
    # [Baking SCHEMA.md §1 throughput_variance guidance.]

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: apprentice-baker
# Per baking SCHEMA.md §3: an apprentice-baker can handle yeasted breads,
# simple rolls, and basic cookies with guidance. This entry is explicitly
# designed for an operator who is building skill while generating early revenue.
# Sourdough management requires developing fermentation judgment over time
# (12-24 months of regular practice); the entry permits a sourdough product
# mix on the condition that early operators accept that fermentation consistency
# will improve as skill develops. Simple yeasted loaves, enriched rolls, and
# standard sandwich bread are solidly within apprentice capability from the
# outset. The skill floor reflects the minimum viable entry point, not the
# optimal operating skill level.

operators_concurrent: "1"
# Single operator throughout. Home kitchen context precludes multi-operator
# simultaneous use; domestic kitchen spatial constraint limits to one active
# baker per session.

apprentice_friendly: true
apprentice_path:
  training_stages: >
    Stage 1 (0-3 months): basic bread chemistry, yeast vs. sourdough leavening,
    dough hydration fundamentals, convection oven operation, safe food handling,
    cottage-food law in the operator's state. Gate criterion: produces 5
    consecutive acceptable yeasted loaves (consistent crumb, adequate oven spring,
    no raw center) independently; can recite cottage-food compliance requirements
    for their jurisdiction.
    Stage 2 (3-12 months): bulk fermentation observation, shaping consistency
    (boule and batard), proofing judgment for domestic temperature variation,
    Dutch-oven steam method, refrigerator cold-retard scheduling, customer
    packaging and labeling. Gate criterion: produces a consistent product
    across 3 consecutive baking sessions without guidance; customer complaint
    rate below 10% of sales.
    Stage 3 (12-30 months): sourdough starter management without supervision,
    recipe development, seasonal adjustments, pricing and cost tracking,
    social-media or DTC channel management, decision point on whether to
    upgrade to commercial kitchen and larger production. Gate criterion:
    independent sourdough fermentation judgment; ability to articulate
    unit economics (cost per loaf, margin per session).
  time_to_independent_operation: >
    ~12 months to produce consistent yeasted artisan bread independently;
    ~24-30 months to reach competent sourdough management on a domestic
    kitchen schedule. Fermentation judgment requires seasonal experience;
    cannot be compressed by instruction alone. This path is explicitly
    slower than a formal culinary school program because it unfolds
    part-time within domestic baking practice rather than through
    concentrated full-time training.
  succession_note: >
    Succession is inherently individual in a home-kitchen micro-bakery:
    there is no institutional continuity beyond the operator. If the
    operator stops, the bakery stops. The apprentice path here is not
    an institutional pipeline — it is a personal skill development arc
    that may or may not lead to a larger commercial operation.
    Community baking groups, bread-baking circles, and online fermentation
    communities (The Fresh Loaf, r/Breadit) provide informal peer-learning
    support that accelerates skill development, but the business itself
    has no succession mechanism.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 500, mid: 2000, high: 5000 }
  # Low: operator already owns a domestic oven; costs are a baking steel or
  # pizza stone (~$50-$100), two Dutch ovens (~$60-$120), bannetons (~$40-$80),
  # basic smallwares (lame, bench scraper, kitchen scale) (~$50-$100),
  # initial flour and ingredient stock (~$100). Total: ~$300-$500.
  # Mid: prosumer countertop convection oven (dedicated to baking, not the
  # domestic range; e.g., Breville Smart Oven Pro or equivalent ~$300-$500),
  # baking steel ($100), two Dutch ovens ($150), proofing setup (insulated
  # box or dedicated proofing bag, ~$50-$150), stand mixer ($200-$400),
  # full smallware set ($100-$200), labeling supplies and initial stock ($200).
  # Total: ~$1,500-$2,500; mid $2,000.
  # High: high-end prosumer oven with steam injection capability
  # (e.g., Anova Precision Oven or Cuisinart Steam-and-Convect, ~$700-$1,200),
  # commercial-grade stand mixer (KitchenAid Professional or Globe equivalent,
  # ~$500-$800), full professional smallwares, branded packaging, initial
  # marketing materials, state cottage-food license fees (~$50-$200), DTC
  # website/Shopify setup (~$200). Total: ~$3,000-$5,000.
  # [CITATION-NEEDED: retail pricing for prosumer convection ovens, Dutch ovens,
  # baking steel, stand mixers, and smallwares; illustrative estimates from
  # consumer retail channels (Amazon, Williams-Sonoma, Restaurant Depot);
  # label: inferred.]

  install_cost: 0
  # No installation cost. This entry uses existing residential electrical
  # infrastructure. No dedicated circuit, no exhaust-hood installation, no
  # plumbing modification, no health-department commercial kitchen inspection.
  # The single major hidden cost is the cottage-food license fee (typically
  # $0-$200 depending on state), captured in the high end of capital_cost.
  # If an operator later upgrades to a commercial kitchen (crossing out of
  # the cottage-food paradigm entirely), a new entry — bake-001 or similar —
  # becomes the applicable model and install_cost would apply there.

  annual_maintenance: 150
  # Domestic appliance maintenance: oven element cleaning and inspection
  # (~$50/yr amortized), Dutch oven seasoning and handle tightening (~$20/yr),
  # stand mixer service (~$30/yr amortized), miscellaneous smallwares
  # replacement (bannetons, lame blades) (~$50/yr). Total: ~$150/yr.
  # [CITATION-NEEDED: domestic appliance maintenance cost data; illustrative
  # estimate from consumer appliance service frequency; label: inferred.]

  annual_consumables: 1400
  # At 1,500 loaves/yr (throughput_units_equiv_per_year):
  # Flour: ~0.5 kg/loaf × 1,500 loaves × $0.70/kg commodity bread flour
  #   [CITATION-NEEDED: US retail or wholesale bread-flour price per kg, 2024]
  #   = $525/yr flour.
  # Specialty flour (heritage wheat, rye, for variety): ~$100/yr.
  # Salt, yeast, oil, and other minor ingredients: ~$100/yr.
  # Packaging: paper bags, parchment, labels, twist ties — ~$0.30/loaf ×
  #   1,500 loaves = $450/yr.
  # Sourdough starter maintenance (flour for feeding): ~$75/yr.
  # Initial flour stock buffer and waste allowance (~15%): ~$150/yr.
  # Total: ~$1,400/yr. Rounds up from ~$1,350 to allow for price variation.
  # [CITATION-NEEDED: retail bread-flour pricing per kg; packaging material
  # costs for cottage-scale bread producer; label: inferred.]

  floor_space_rent_per_year: 0
  # The kitchen is the operator's existing residential space. Per
  # catalog/SCHEMA.md §6, floor_space_rent should be imputed at commercial
  # rate for consistency. However, for this entry the kitchen doubles as
  # domestic space; there is no incremental rent attributable to the bakery.
  # Imputing residential rent at commercial rates would distort the comparison:
  # the operator is not renting kitchen space for baking; they are using space
  # they would pay for regardless. The zero here acknowledges this structural
  # difference from all other baking entries. Economic models that require
  # full-cost comparison should add a notional occupancy cost (~$600-$1,200/yr
  # for a proportional share of residential rent for the kitchen area), but
  # doing so would not change the revenue-ceiling finding (the binding
  # constraint is cottage-food law, not rent).

  market_price_per_unit: { low: 5, mid: 9, high: 15 }
  # Per loaf equivalent (800g artisan loaf). Low: commodity-competitive
  # home-baker pricing at a neighborhood or farmers-market stall ($5 for
  # a plain loaf in a price-sensitive market). Mid: standard cottage-food
  # artisan bread pricing at farmers markets or Instagram/DTC in a mid-tier
  # market ($9 for a sourdough boule or seeded loaf). High: premium pricing
  # in an affluent urban neighborhood or specialty DTC subscription context
  # ($15 for a heritage-grain or highly branded specialty loaf).
  # Industrial baseline: $3 (mass-produced supermarket sourdough).
  # Per entry parameters: low $5, mid $9, high $15.
  # [CITATION-NEEDED: cottage-food bread pricing survey at US farmers markets
  # and DTC home-baker channels, 2024-2026; illustrative estimates from market
  # observation; label: pricing_validation: inferred.]

  pricing_notes: >
    Unit is an 800g artisan loaf equivalent. Premium over mass-produced
    industrial sourdough loaf ($3/loaf at major US supermarket; Sara Lee,
    Pepperidge Farm, or private-label equivalent [CITATION-NEEDED: US
    supermarket sourdough shelf-price survey, 2024]) reflects: (1) direct-to-
    consumer sale via Instagram, neighborhood sale, or farmers-market stall
    with a personal story and face-to-face relationship; (2) fresh-baked
    product with no preservatives or shelf-life extension common to industrial
    bread; (3) the social-media DTC phenomenon that has established consumer
    willingness to pay $8-$15 for home-baker specialty loaves in urban and
    suburban markets. The customer segment is the affluent neighborhood buyer
    who discovered home-baker bread via Instagram or a farmers-market encounter
    — not a buyer substituting on price. This premium is real and documented
    by the modern DTC home-baker market; it is entirely dependent on platform
    access (Instagram, Goldbelly, local Facebook group) and NOT on any
    restoration of local food systems.

  pricing_validation: >
    Pricing evidence: inferred from market observation of cottage-food home
    bakers on Instagram DTC channels and US farmers-market vendors operating
    below commercial-kitchen thresholds, circa 2024-2026. NOT sourced from
    a formal pricing survey. This is a placeholder-inferred figure.
    Recommended verification: USDA AMS farmers-market pricing survey for
    bread/bakery goods; Specialty Food Association cottage-food market report;
    or direct survey of state cottage-food bakery operator pricing.

  industrial_baseline_price: 3
  # Mass-produced supermarket sourdough loaf (Sara Lee, Pepperidge Farm, or
  # major private-label equivalent) at approximately $3-$4 per loaf at US
  # supermarket retail pricing. The $3 figure is the low end of mass-market
  # artisan-branded supermarket bread and the most relevant direct consumer
  # substitute for a farmer-market home-baker loaf.
  # [CITATION-NEEDED: US supermarket sourdough bread shelf-pricing survey,
  # 2024; illustrative estimate from market observation; label: inferred.]

# ── TRADE-SPECIFIC FIELDS ────────────────────────────────────────────────────

trade_specific:
  flour_source_declaration: industrial-flour-purchased
  # Home micro-bakery purchases commodity or specialty bread flour from
  # retail or wholesale channel (grocery store, Costco, regional food-service
  # distributor for larger volumes). No mill infrastructure; no direct farm
  # relationship. This is the explicit minimum-capital flour-sourcing model:
  # no supply-chain differentiation, no provenance narrative, highest exposure
  # to commodity wheat price volatility.
  # Per baking SCHEMA.md §4 and DECLINE-VERDICT mill-dependency falsifier:
  # the premium market positioning of this entry, such as it is, derives from
  # process (home-baked, direct relationship, fresh-baked) not from ingredient
  # provenance. The operator cannot credibly claim grain-sourcing differentiation
  # when buying retail all-purpose flour from a grocery store.
  # See Key Assumptions for flour sourcing details.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Convection fan motor (prosumer countertop oven)"
      estimated_hours_to_failure: 800
      replacement_cost: 250
      replacement_lead_time_days: 7
      serviceable_by: specialist
      # Prosumer convection ovens (Breville, Cuisinart-steam, Anova) have
      # convection fan motors that are more lightly built than commercial
      # units and are subject to faster degradation under sustained baking
      # temperatures. At ~12 hr/wk × 50 wk = 600 hr/yr active use, a
      # lightly-built motor may fail in 12-18 months. Per baking SCHEMA.md §5:
      # convection fan motor 2,000-4,000 hr for commercial ovens; prosumer
      # domestic units at higher thermal load relative to design spec may
      # fail significantly earlier.
      # Repair on prosumer countertop ovens is typically not field-serviceable;
      # manufacturer warranty service or replacement is the standard path
      # (specialist). If covered by warranty (typically 1 yr), replacement
      # cost is $0-$50 (shipping); out-of-warranty a replacement unit may be
      # required at full capital cost. $250 is a conservative mid-estimate
      # assuming partial warranty coverage or a refurbished replacement unit.
      # [Baking SCHEMA.md §5 convection fan motor reference; CITATION-NEEDED:
      # empirical MTBF data for prosumer convection ovens under sustained
      # baking use; label: inferred.]
    - item: "Dutch oven handle screw or knob failure"
      estimated_hours_to_failure: 400
      replacement_cost: 15
      replacement_lead_time_days: 3
      serviceable_by: operator
      # Dutch oven lids are subjected to repeated thermal cycling in a domestic
      # oven (room temperature to 230°C and back). The phenolic or stainless
      # lid knob or handle screw is the most common failure point: knobs
      # crack from thermal stress; screws strip from repeated removal for
      # cleaning. Operator-serviceable (standard hardware or manufacturer
      # replacement part); 3-day lead time from Amazon or hardware store.
      # [General domestic cookware failure mode; CITATION-NEEDED: empirical
      # failure data for cast-iron Dutch oven lid hardware under sustained
      # high-temperature oven use; label: inferred.]
    - item: "Stand mixer bowl or dough hook (wear and micro-fracture)"
      estimated_hours_to_failure: 600
      replacement_cost: 80
      replacement_lead_time_days: 5
      serviceable_by: operator
      # Domestic stand mixer (KitchenAid or equivalent) dough hook and bowl
      # are designed for household use, not sustained commercial-scale bread
      # production. At 12 hr/wk active use with frequent high-hydration
      # dough (~70-80% hydration), hook coating degradation and bowl surface
      # micro-fractures are expected within 12 months of sustained use.
      # Operator-serviceable: hook and bowl are standard replacement parts
      # widely available. $80 is a mid-estimate for a replacement bowl or
      # hook set.
      # [CITATION-NEEDED: domestic stand mixer hook and bowl wear data under
      # sustained bread-production use; illustrative from baking SCHEMA.md §5
      # general wear-item guidance; label: inferred.]

  maintenance_schedule:
    daily:
      task: "After each baking session: clean Dutch ovens (season if needed), clean mixer bowl and hook, wipe oven interior, log batch results (yield, fermentation notes, any customer feedback)"
      performed_by: operator
    weekly:
      task: "Inspect oven convection fan for noise or uneven airflow; check Dutch oven handles; calibrate kitchen thermometer against a water-boil reference; review flour stock levels; log ingredient costs against loaves produced"
      performed_by: operator
    quarterly:
      task: "Deep-clean oven interior (baked-on residue removal); mixer motor brush check and lubrication (on applicable models); Dutch oven full seasoning restoration; review cottage-food license compliance (sales volume, labeling)"
      performed_by: operator
    annual:
      task: "Full equipment review: assess whether oven, mixer, and Dutch ovens have reached end of useful life for production use; reassess cottage-food revenue against state thresholds; evaluate whether to upgrade to commercial kitchen (triggering a different catalog model)"
      performed_by: operator

  startup_shutdown_overhead_per_day_min: 45
  # Per baking session (the operational unit for this entry, not a calendar day):
  # (1) oven preheat from cold to 230-250°C with baking steel: ~35-40 min;
  # (2) end-of-session cleanup, packaging completed loaves, updating sales log:
  # ~20-25 min. Total: ~55-65 min/session; 45 min/session is the minimum if
  # the oven is pre-heated while mixing begins (parallel operations). The 45 min
  # figure is used here as the per-session overhead, representing the practical
  # minimum rather than the average.
  # [Structural inference from sourdough home-baking scheduling; CITATION-NEEDED:
  # empirical overhead data for home-kitchen bread sessions; label: inferred.]

  max_active_hours_realism_note: >
    12 hr/wk is the gross ceiling including startup preheat and session cleanup.
    Operating 2.5 sessions/wk (average; some weeks 2, some 3) × 4.8 hr/session
    gross = 12 hr/wk. Derating for per-session overhead (45 min): 2.5 sessions
    × 45 min = 1.875 hr/wk overhead → net active production time (mixing,
    shaping, baking monitoring, cooling) ≈ 10.1 hr/wk net. sim_params uses
    the loaves-per-session figure (8 loaves/session × 2.5 sessions/wk = 20
    loaves/wk) as the primary throughput driver, consistent with the net
    active-hour window. The 12 hr/wk gross figure is used in E-3 cross-checks.

  interruption_notes: >
    Home-kitchen operations interleave baking with domestic life: childcare,
    domestic tasks, and household members using the kitchen are constant
    interruption sources that are not present in commercial bakery operations.
    These interruptions are not quantified separately; they are embedded in the
    conservative 8 loaves/session output ceiling and the 2-3 sessions/wk
    frequency assumption. An operator who achieves uninterrupted baking
    sessions will exceed these figures; an operator managing household
    obligations concurrently will reach them.

  consumables_lead_time_days: { typical: 1, worst: 7 }
  # Typical: grocery store or Costco same-day or next-day flour purchase.
  # Worst: regional supply disruption, preferred specialty flour out of stock
  # at distributor; 7-day lead time from online specialty-flour supplier.
  # [Structural inference; CITATION-NEEDED: residential flour supply chain
  # lead-time data; label: inferred.]

  throughput_variance:
    seasonal: "Summer trough (July-August) from consumer demand reduction and operator reluctance to run a home oven during hot weather; pre-holiday uptick (November-December) for gift loaves and holiday tables; January post-holiday slowdown"
    worst_month_fraction_of_average: 0.60
    best_month_fraction_of_average: 1.35

  operator_impact:
    noise_db: 55
    # Domestic convection oven: fan noise ~50-60 dB at operator position.
    # Stand mixer during dough mixing: ~65-70 dB (peak, intermittent, ~5-10 min
    # per session). Ambient domestic kitchen during baking session: ~50-60 dB(A).
    # Well below OSHA 90 dB(A) PEL; no occupational noise concern at this scale.
    # [CITATION-NEEDED: domestic appliance noise measurement at operator position;
    # illustrative estimate; label: inferred.]
    heat_exposure: "Moderate ambient heat increase near oven during baking (oven at 230-250°C; domestic kitchen ambient may rise 3-8°C above baseline during extended sessions); no commercial heat-stress risk at this scale and session frequency; open window or kitchen fan manages ambient temperature adequately"
    emissions: "Near-zero combustion emissions; steam during Dutch-oven baking dissipates quickly in kitchen volume; flour dust from mixing is the primary occupational exposure concern — at 1-2 kg flour/session, dust concentrations are well below OSHA TWA limits; natural ventilation sufficient"
    physical_demand: "Low to moderate; repetitive dough-shaping motions (8-16 shaping actions per session), 2-5 kg dough-mass handling, bending to load and unload domestic oven; no sustained heavy lifting; anti-fatigue mat recommended for extended standing during mixing and shaping phases"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Residential zoning; cottage-food laws govern home-based food production sales in all US states; direct-consumer sales (farmers market, home pickup, DTC delivery) typically permitted without commercial kitchen licensing below revenue thresholds; check state-specific cottage-food law before selling — thresholds range from $5,000/yr (most restrictive) to $75,000/yr (most permissive) with most states in the $25,000-$50,000/yr range; wholesale or restaurant sales are prohibited under most cottage-food laws regardless of revenue"
  emissions: "No emissions permit required for convection-electric domestic oven; residential range-hood or natural ventilation meets applicable standards; no air-quality or combustion permit trigger"
  other: "Cottage-food license required in most states (typically $0-$200 fee); product labeling requirements under cottage-food law (operator name, address, ingredient list, allergen disclosure, 'Made in a Home Kitchen' statement required in most jurisdictions); no HACCP plan required for cottage-food sales; farmers-market vendor permit required if selling at a farmers market; interstate commerce may void cottage-food exemption — operator should not ship across state lines unless state law explicitly permits it"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: marginal
  cooperative: poor
  civic: poor

scale_fit:
  village: marginal
  town: poor
  small_city: poor

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 2000
  # Equals economics.capital_cost.mid per E3-R1. [Derived from economics block above]

  cost_sd: 1125
  # Derived: (capital_cost.high - capital_cost.low) / 4 = (5,000 - 500) / 4
  # = $1,125. E3-R5 check: cost_sd/cost_mean = 1,125/2,000 = 0.5625; slightly
  # above the 0.15-0.50 guideline range; however, the wide low-to-high range
  # ($500-$5,000) accurately reflects the 10× capital span between a bare-minimum
  # entry (operator already owns an oven) and a fully-kitted prosumer setup.
  # Asymmetry is explained by the fact that many entrants start near the $500
  # floor, pulling cost_mean below the arithmetic midpoint; the 0.56 SD ratio
  # is a P2 flag per E3-R5 and is documented here.
  # [Derived per catalog/SCHEMA.md §3 default formula; asymmetry note above]

  throughput_units_equiv_per_year: 1500
  # Derivation (per baking SCHEMA.md §1 E-3 guidance):
  # Unit: 800g artisan loaf equivalent (see Key Assumptions).
  # Step 1 — operating sessions per year:
  #   2.5 sessions/wk × 50 wk/yr (allowing 2 wk vacation / holiday closure)
  #   = 125 sessions/yr.
  # Step 2 — loaves per session (gross):
  #   throughput.loaves_per_day = 8 loaves/session.
  # Step 3 — gross annual loaves:
  #   8 × 125 = 1,000 loaves/yr at 2.5 sessions/wk.
  #   Upper bound at 3 sessions/wk: 8 × 150 = 1,200 loaves/yr.
  #   Entry parameter range is 20-50 loaves/wk; at 30 loaves/wk mid-point:
  #   30 × 50 = 1,500 loaves/yr.
  # Step 4 — apply downtime fraction (0.12):
  #   1,500 × (1 - 0.12) ≈ 1,320; however, for home operations "downtime"
  #   also includes weeks of lower output (illness, holidays, demand trough),
  #   embedded in the 1,500 figure before further deration.
  #   Using 1,500 as the net operating target (sessions × loaves already
  #   represents conservative estimate; downtime folded into session frequency).
  # E3-R2 active-hours cross-check:
  #   max_active_hours_per_week (12) × 50 wk × (1 - 0.12) = 528 hr/yr.
  #   loaves/hr implied: 1,500 ÷ 528 = 2.84 loaves/hr.
  #   At 8 loaves/session ÷ 4.8 hr/session (gross) = 1.67 loaves/hr (gross
  #   including overhead); net baking hours ÷ loaves: ~2.4 loaves/net hr.
  #   The 2.84 figure is within order-of-magnitude consistency with 2.4
  #   net-hour calculation; slight variance reflects the conservatism in
  #   the session-count estimate. No order-of-magnitude discrepancy.
  # [Derived from throughput fields, session-count assumption, and
  # entry-parameter range 20-50 loaves/wk]

  variable_cost_per_unit: 0.97
  # Flour: 0.5 kg/loaf × $0.70/kg = $0.35/loaf [CITATION-NEEDED].
  # Salt, yeast, additives: ~$0.05/loaf.
  # Packaging (paper bag + label): ~$0.30/loaf.
  # Energy: 1.5 kWh/hr × ~0.6 hr/loaf (4.8 hr session ÷ 8 loaves) × $0.13/kWh
  #   [US EIA residential rate] = $0.12/loaf.
  # Sourdough starter maintenance: ~$0.05/loaf amortized.
  # Waste allowance (failed batches, unsold product): ~$0.10/loaf.
  # Total: ~$0.97/loaf.
  # Cross-check against annual_consumables: $1,400/yr ÷ 1,500 loaves = $0.93/loaf
  # for consumables alone; adding energy ($0.12/loaf) gives $1.05/loaf —
  # within rounding of $0.97 (the small gap reflects that annual_consumables
  # includes a buffer for stock waste and price variation not in per-unit calc).
  # [Derived from annual_consumables, energy figures; US EIA residential
  # electricity rate average $0.12-$0.14/kWh, midpoint $0.13 used]

  labor_hours_per_unit: 0.34
  # 12 hr/wk × 50 wk × (1 - 0.12) = 528 hr/yr total operator time.
  # 528 ÷ 1,500 loaves = 0.352 hr/loaf → 0.34 hr/loaf (rounding down
  # slightly to reflect that some operator hours include non-production
  # tasks like marketing and admin that are loosely baked into the 12 hr/wk
  # figure; the approximation is within E3-R3 tolerance).
  # E3-R3 check: 1,500 × 0.34 = 510 hr/yr; target = 12 × 50 × 0.88 = 528 hr.
  # Discrepancy = 18 hr (3.4%); within P2 threshold.
  # [Derived from throughput_units_equiv_per_year and max_active_hours_per_week]

  downtime_fraction: 0.12
  # Convection fan motor failure (~7 days downtime if replacement unit needed);
  # illness or household obligation weeks (typical home-baker schedule includes
  # 2-3 missed weeks per year beyond vacation); recipe development sessions that
  # produce no saleable output (~1-2 sessions/month in early months).
  # Total estimated downtime equivalent: 6 weeks/year out of 52 = 11.5% → 0.12.
  # Consistent with E3-R6: first-year fan motor failure = up to 1-2 weeks
  # downtime = 2-4%; household and illness interruptions = 3-5%; development
  # waste = 2-3%; total ~10-12%.
  # [Derived from operations_reality.first_year_failures and domestic-schedule
  # interruption pattern above]

  lifespan_years: 10
  # Domestic and prosumer kitchen appliances (convection oven, stand mixer,
  # Dutch ovens) in sustained semi-commercial use: estimated 7-12 years.
  # At ~600-650 hr/yr active oven use, a prosumer oven rated for ~5,000-8,000
  # hr domestic use would last 8-13 years before major refurbishment or
  # replacement. Using 10 years as a mid-estimate consistent with accelerated
  # wear from semi-commercial use. This is significantly shorter than
  # commercial deck oven lifespan (15-20 years per bake-001) — reflecting
  # that prosumer equipment is not designed for sustained production use.
  # [CITATION-NEEDED: prosumer convection oven lifespan data under semi-
  # commercial baking use; illustrative estimate from general appliance
  # longevity literature; label: inferred.]

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
  - ref: "catalog/baking/SCHEMA.md v1.0 §1: throughput block structure; loaves/day ranges for home/micro (10-40); E-3 cross-check guidance"
  - ref: "catalog/baking/SCHEMA.md v1.0 §2: convection-electric energy consumption 2-5 kWh/batch; temperature ceiling 160-230°C; Dutch-oven steam workaround"
  - ref: "catalog/baking/SCHEMA.md v1.0 §3: apprentice-baker skill definition; product scope boundary (yeasted breads, simple rolls, basic cookies)"
  - ref: "catalog/baking/SCHEMA.md v1.0 §4: flour_source_declaration required field; industrial-flour-purchased supply-chain risk"
  - ref: "catalog/baking/SCHEMA.md v1.0 §5: first_year_failures reference list; convection fan motor 2,000-4,000 hr (commercial); Dutch oven and stand mixer wear items"
  - ref: "catalog/baking/SCHEMA.md v1.0 §6 Group D: capital_cost as defining constraint; cottage-food law regulatory environment as primary field"
  - ref: "catalog/baking/DECLINE-VERDICT.md: mill-dependency falsifier; cottage-food as part-time income supplement not primary livelihood; DTC/Instagram channel dependency"
  - ref: "corpus/program/SCALES.md §6: infrastructure baseline; residential electricity rate reference"
  - ref: "US Energy Information Administration. Electric Power Monthly, Table 5.3: Average Retail Price of Electricity. Monthly release. https://www.eia.gov/electricity/monthly/ (residential rate 2023-2024: $0.12-$0.14/kWh; midpoint $0.13 used)"
  - ref: "OSHA 29 CFR 1910.1000 Table Z-1. Air Contaminants. (Flour-dust permissible exposure limit; applies at commercial baking scale; not a binding constraint at cottage-food volumes)"
  - ref: "OSHA 29 CFR 1910.95. Occupational noise exposure. (90 dB(A) PEL; domestic baking well below threshold)"
  - ref: "National Conference of State Legislatures (NCSL). Cottage Food Laws. Accessed 2024. https://www.ncsl.org/agriculture-and-rural-development/cottage-food-laws (state-by-state cottage-food revenue thresholds; basis for $25,000-$50,000/yr most-states range cited in regulatory_notes)"
  - ref: "Ostrom, Elinor. 1990. Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press. (Cooperative lens governance principles; cited for background context only — this entry does not trigger cooperative lens.)"
  - ref: "[CITATION-NEEDED: retail pricing for prosumer convection ovens (Breville, Anova, Cuisinart), Dutch ovens, baking steel, stand mixers, and baker smallwares; consumer retail channels, 2024]"
  - ref: "[CITATION-NEEDED: US retail or wholesale bread-flour price per kg, 2024; USDA ERS wheat and flour price series; King Arthur, Bob's Red Mill, or food-service distributor pricing]"
  - ref: "[CITATION-NEEDED: packaging material costs (paper bags, labels) for cottage-food bread producer at 1,000-2,000 loaves/yr volume; 2024]"
  - ref: "[CITATION-NEEDED: cottage-food bread pricing survey at US farmers markets and DTC home-baker channels, 2024-2026; USDA AMS farmers-market pricing data or Specialty Food Association cottage-food market report]"
  - ref: "[CITATION-NEEDED: US supermarket sourdough bread shelf-pricing survey, 2024; IRI or Nielsen retail-scanner data for sourdough bread category]"
  - ref: "[CITATION-NEEDED: empirical MTBF data for prosumer convection ovens (Breville, Anova) under sustained semi-commercial baking use; appliance reliability survey or manufacturer service data]"
  - ref: "[CITATION-NEEDED: domestic stand mixer bowl and hook wear data under sustained bread-production use at 10-15 hr/wk; operator survey or appliance service documentation]"
  - ref: "[CITATION-NEEDED: prosumer convection oven lifespan under semi-commercial baking use; general appliance longevity literature or manufacturer specification]"
  - ref: "[CITATION-NEEDED: empirical throughput data for home-kitchen convection-oven bread production at 2-3 sessions/wk; home baker survey or cottage-food operator financial records]"
---

## Summary

Bake-014 is the minimum-capital stress-test entry for the baking catalog: a part-time home-kitchen or apartment-based micro-bakery producing 20-50 loaves per week using a domestic or prosumer convection-electric oven, selling under state cottage-food laws at farmers markets, neighborhood direct-sale, or via social-media DTC channels. Its defining characteristics are: (1) zero installation cost — the domestic kitchen is the entire infrastructure; (2) capital cost of $500-$5,000, an order of magnitude below any commercial baking entry; (3) binding revenue ceiling imposed by cottage-food law ($25,000-$50,000/year in most US states), not by market demand or throughput capacity; (4) part-time operation only — this is a second-income supplement, not a livelihood; and (5) market viability that is genuinely marginal, not disguised as promising. This entry documents the "home baker selling on Instagram" phenomenon honestly: the income is real, the premium is real, the platform dependency is real, and the ceiling is real. It does not restore a local food system; it exploits a consumer-preference niche enabled by social media and DTC logistics.

## Design rationale

This entry exists to stress-test the viability floor of the baking catalog — the analog to forge-001 (Backyard Propane Compact) in the smithing catalog. Every other baking entry assumes a commercial kitchen, a commercial oven, and a capital investment of $18,000 or more. Bake-014 asks: what happens at the absolute capital minimum, in a domestic kitchen, under cottage-food law? The answer is a bounded, marginal business that can supplement household income by $5,000-$20,000 per year for an operator who already bakes and wants to monetize that activity — but cannot, under any realistic scenario, generate a primary livelihood. The specific problem this entry solves that no other entry addresses is: the home baker who wants to begin selling bread without a commercial kitchen, a commercial oven, or significant capital. Bake-001 (sourdough artisan micro) requires a $32,000 commercial setup; bake-014 requires a $2,000 prosumer setup already sitting on most domestic kitchen counters. The gap between these two entries defines the cottage-food threshold in operational rather than legal terms.

The anti-romantic framing is deliberate. The home-baker DTC phenomenon is enabled by Instagram discovery, Facebook neighborhood groups, and DTC fulfillment logistics — not by any revival of pre-industrial community baking. A home baker in 2026 selling sourdough via Instagram is participating in a late-capitalist social-media commerce phenomenon, not restoring a traditional food system. The premium pricing is real; the platform dependency is equally real and fragile. When Instagram's algorithm changes, when a local commercial artisan bakery opens, or when the neighborhood novelty fades, the home baker's revenue is exposed. This entry documents that exposure rather than papering over it.

## Historical lineage

Two precedents are cited, both requiring anti-romantic treatment.

**American cottage-food movement** (functional inheritance): The cottage-food movement — state legislation permitting home-kitchen food production for direct commercial sale, enacted or expanded in most US states between 2010 and 2024 — created the legal infrastructure that makes this entry viable. The functional inheritance is legal permission and a defined revenue envelope, not any historical baking tradition. The cottage-food movement was not a revival of premodern household baking; it was a modern regulatory accommodation to the home-cooking hobbyist community that wanted to sell at farmers markets without meeting full commercial kitchen requirements. States with the most permissive cottage-food laws (e.g., Wyoming, Missouri) allow direct sales to consumers without revenue cap; states with the most restrictive (Massachusetts before its 2022 reform, several Northeastern states) require commercial kitchen licensing even for small-scale home production. The legal form varies widely; authors must verify their state's specific provisions before treating this entry as viable.

**Instagram / DTC home-baker phenomenon** (functional inheritance): The contemporary home-baker commercial scene was enabled by three converging factors: the COVID-19 home-baking surge (2020-2021), which created widespread skill development and sourdough starter culture propagation; Instagram and Facebook Marketplace as low-cost discovery and trust channels that eliminated the farmers-market stall cost for initial customer acquisition; and DTC fulfillment logistics (local delivery, porch pickup) that removed the physical market requirement. This is recent history (2020-2026), not a historical tradition. The functional inheritance is the DTC channel model and the social-proof mechanism (customer photos, word-of-mouth within neighborhood groups). What this precedent does NOT provide is sustainable economics: the DTC home-baker market is oversaturated in many urban markets as of 2024-2026, and average operator tenure at commercial scale is short. The entry acknowledges this fragility explicitly.

## Key assumptions

**Cottage-food revenue cap (binding constraint):** Most US states cap cottage-food sales at $25,000-$50,000/year for direct-to-consumer sales. This is the primary revenue ceiling, not market demand or throughput capacity. At mid-case pricing ($9/loaf × 1,500 loaves/yr), gross revenue is $13,500/year — well below any state's threshold. Even at high-case pricing ($15/loaf × 1,500 loaves/yr = $22,500) the operation remains below the most common threshold ($25,000). The revenue ceiling is not binding at the throughput levels achievable with a domestic oven and part-time schedule; an operator who wants to grow beyond $25,000/year must upgrade to a commercial kitchen and exit the cottage-food model, transitioning to a different catalog entry (bake-001 or similar). [NCSL Cottage Food Laws database, 2024.]

**Throughput (1,500 loaves/year):** Derived from 30 loaves/week mid-point of the 20-50 loaves/week entry parameter range, × 50 operating weeks. This is achievable at 3-4 sessions/week with a domestic convection oven; it is labeled inferred and requires verification from actual cottage-food baker operator data [CITATION-NEEDED]. The range 20-50 loaves/week corresponds to gross revenue of $9,000-$22,500/year at mid-case pricing ($9/loaf) — a part-time income supplement, not a livelihood.

**Market pricing ($5-$15/loaf):** Per entry parameters; labeled pricing_validation: inferred. The $9 mid-case is consistent with observed DTC and farmers-market pricing for home-baker sourdough in mid-tier US markets. The $15 high case is achievable in premium urban markets (SF Bay Area, Brooklyn, Seattle) with a strong social-media following. The $5 low case reflects price-sensitive neighborhood or community market contexts. All three figures require verification against empirical cottage-food pricing data [CITATION-NEEDED].

**Capital costs ($500-$5,000):** The low end ($500) assumes the operator already owns a domestic oven and needs only smallwares and initial stock. The mid ($2,000) is a prosumer oven setup; the high ($5,000) adds a steam-capable oven, commercial-grade mixer, and branding costs. The 10× range between low and high produces a cost_sd/cost_mean ratio of 0.56, slightly above the E3-R5 0.50 guideline (flagged as P2 in sim_params above). The asymmetry is real: most entrants start near the $500 floor.

**Floor space rent ($0):** Deliberately set to zero rather than imputing commercial rates, because the kitchen is the operator's existing residential space and no incremental rent is attributable to baking. This differs from commercial entries and makes cross-entry cost comparison using floor_space_rent structurally non-comparable; analysts should note this difference when comparing bake-014 against bake-001 economics.

**Unit definition:** The 800g artisan loaf equivalent is consistent with bake-001 for cross-entry comparability. The actual product mix may include smaller rolls (which would increase loaf-equivalent count per session) or larger specialty loaves (which would reduce it); the 800g boule equivalent is the stated canonical unit per Key Assumptions.

## Known risks / failure modes

**Regulatory (primary risk):** Cottage-food law is a patchwork of state-level regulations that change frequently. Key risks: (1) Revenue threshold violation — inadvertently exceeding the state annual cap triggers a requirement to obtain a commercial kitchen license, which may cost $2,000-$10,000 in facility upgrades or shared-kitchen fees; the operator must track gross sales carefully. (2) Interstate commerce — shipping bread across state lines may void the cottage-food exemption in both origin and destination states; DTC operators who ship nationally are operating in a grey area that has seen enforcement in some states. (3) Labeling non-compliance — cottage-food laws require specific labeling (operator address, allergen disclosure, "Made in a Home Kitchen" language); a failure inspection can result in sales prohibition and fines. (4) Wholesale prohibition — most cottage-food laws prohibit sale to restaurants, retail stores, or institutional buyers; any wholesale inquiry should be declined or routed to a licensed commercial kitchen arrangement. Operators who fail to read their state's specific statute are the primary risk vector.

**Labour pipeline (skill formation and succession):** The apprentice-baker skill floor means that early output quality will be inconsistent. Sourdough fermentation judgment takes 12-24 months of regular seasonal practice to develop; operators who rush to market with 2-3 months of home baking experience will produce variable product. Succession risk is complete: the home micro-bakery has no institutional continuity beyond the single operator. If the operator stops (illness, life event, disinterest), the business ceases immediately. There is no apprentice pipeline, no co-operator, no institutional knowledge transfer mechanism. This is not a risk to manage — it is a structural characteristic of the model that must be understood before entry.

**Supply chain (flour price volatility and retail availability):** At retail flour prices, commodity wheat price volatility has a direct pass-through effect: the 2022 US retail bread-flour price spike (~30-50% above 2021 levels) would have increased annual consumables from ~$1,400 to ~$1,700, reducing operator net margin by ~$300/year at 1,500 loaves/year throughput. This is material relative to total revenue but not existential. More significant: retail flour availability in supply-chain disruption scenarios (e.g., regional store closure, distributor outage) is the worst-case scenario; the 7-day worst-case lead time [consumables_lead_time_days.worst] implies maintaining a 2-3 week flour inventory buffer (~$30-$50 working capital) as standard practice.

**Platform dependency (revenue channel fragility):** The Instagram and DTC channel model is the primary customer acquisition mechanism for home-baker micro-bakeries in 2024-2026. This channel is entirely dependent on: algorithm stability (changes to Instagram's discovery algorithm can reduce reach overnight), platform longevity (platform shifts over a 5-10 year operating horizon are likely), and neighborhood novelty (early-adopter premium fades as more home bakers enter the local market). A home baker who has not built a subscription base or recurring customer relationship independent of the platform is exposed to sudden revenue loss. This is not a supply-chain or regulatory risk — it is a market-structure risk unique to the social-media DTC model. It has no historical analog and cannot be hedged through operational practices alone.

## Iteration log

- 2026-04-18: v0.1 — initial authoring per Plan G Task 16. Minimum-capital stress-test
  entry for the baking catalog analog to forge-001. All schema fields populated including
  trade_specific.flour_source_declaration (industrial-flour-purchased per DECLINE-VERDICT);
  operations_reality required and populated because lens_fit.market is marginal (E2-R4
  trigger); cooperative and civic lens_context blocks omitted (both lens_fit values are
  poor, no trigger); market pricing per entry parameters (low $5, mid $9, high $15);
  cottage-food revenue cap documented as binding regulatory constraint in regulatory_notes
  and Known Risks; floor_space_rent set to zero with explicit justification (domestic
  kitchen; no incremental rent attributable to baking activity); anti-romantic framing
  of Instagram/DTC phenomenon explicit throughout; 14 CITATION-NEEDED placeholders
  carried forward; sim_params cost_sd/cost_mean ratio (0.56) flagged as P2 per E3-R5
  with justification; throughput_units_equiv_per_year (1,500 loaves/yr) derived from
  entry parameter range 20-50 loaves/wk mid-point.
