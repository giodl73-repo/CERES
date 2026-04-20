---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: bake-009
trade: baking
name: "Custom Celebration Cake Studio (wedding, birthday, corporate events)"
tagline: "Pastry-master-run studio producing high-value custom cakes on lead-time order — premium pricing, low throughput, event-calendar revenue cycle"
status: draft
version: 0.1
supersedes: null
inspirations: [victorian-confectionery-shop, mid-century-american-wedding-cake-tradition, modern-cake-design-competition-circuit]

# ── PHYSICAL ENVELOPE ─────────────────────────────────────────────────────────

footprint_m2: 30
# Midpoint of 20-40 m² range. Covers: baking area (convection oven + 2 mixers),
# cold storage (refrigeration for assembled cakes and buttercream stock),
# decorating bench (fondant work, piping, sugar flowers), drying/staging area
# (gum-paste components, dried sugar work), and a small order-intake/display corner.
# Decorating requires dedicated bench space separate from the baking area;
# a custom-cake studio cannot share its decorating bench with active production.

ceiling_min_m: 2.7
# Standard commercial ceiling acceptable; no unusual height requirement.
# Tiered cake assembly (cakes up to 1 m tall for multi-tier builds) does not
# drive ceiling height; the constraint is horizontal bench space and staging area.

ventilation: mechanical-extraction-required
# Convection oven exhaust and sugar-work heat require mechanical extraction.
# Fondant and sugar work do not require heavy ventilation, but oven heat and
# occasional use of culinary torches (sugar caramelization, Italian meringue)
# mandate commercial-kitchen ventilation per health-department codes in most
# US jurisdictions.

# ── ENERGY ────────────────────────────────────────────────────────────────────

energy_source: convection-electric
# Convection-electric is the industry standard for custom cake baking.
# Temperature precision (165-190°C for layer cakes; 175-200°C for pound cakes)
# and consistency across bake sessions are critical for level, uniform cake
# layers. Wood-fired or gas-fired sources introduce temperature variation that
# is difficult to manage at the precision required for multi-layer stacked cakes.
# A combi-steam oven is an upgrade path (better moisture retention in sponge
# layers) but the base convection-electric is the minimum adequate tool.

energy_consumption_per_active_hour: "3.5 kWh (convection oven during active bake cycle; reduced to ~1 kWh/hr during decorating-only sessions with oven off)"
# Weighted average across a typical operating day: baking ~4 hrs at 3.5 kWh/hr
# + decorating ~4 hrs at 0.5 kWh/hr (refrigeration + lighting) = ~16 kWh/day.
# Refrigeration runs continuously; included in annual_consumables energy cost.
# [CITATION-NEEDED: commercial convection oven kWh/hr at cake-baking temperatures;
# consistent with catalog/baking/SCHEMA.md §2 convection-electric range 2-5 kWh/batch.]

backup_fuel: null
# No backup fuel; electric supply is the only viable energy source for
# precision-temperature custom cake production. Generator backup for power
# outages is a business-continuity option (especially before large weddings)
# but not a primary design element — see Known Risks.

# ── THROUGHPUT ────────────────────────────────────────────────────────────────

throughput:
  loaves_per_day: 2
  # Unit: one custom cake order (one complete baked, filled, frosted, and
  # decorated cake of any tier count, normalized to a single client order).
  # A single-tier birthday cake and a five-tier wedding cake both count as
  # one order unit; labor content differs (see Key Assumptions on unit weighting).
  # Range: 1-4 orders/day depending on complexity and season.
  # Authors must state unit clearly per catalog/baking/SCHEMA.md §1 guidance;
  # see Key Assumptions for the weighting rationale.
  batches_per_day: 1
  # One oven session per operating day: layers for all orders-in-progress
  # baked in a single session (typically morning), then the day shifts to
  # filling, crumb-coating, refrigeration rest, fondant/buttercream application,
  # and decorating. A second bake session occurs only when an exceptionally
  # large wedding-week order fills the oven twice; excluded from baseline.
  batch_size_loaves: 2
  # Two completed cake orders per day at the central estimate. Constrained
  # by decorating-time bottleneck, not oven capacity: the oven can bake
  # layers for 4-6 orders in a single load, but each order requires 2-6 hrs
  # of hands-on decorating; 2 orders/day is the realistic decorated-and-ready
  # ceiling for a solo master baker.
  max_active_hours_per_week: 50
  # Combined operator hours per week for 1-2 operators.
  # Solo master baker: ~40 hrs/wk production. Part-time assistant (for
  # peak-season decorator support or delivery): adds ~10 hrs/wk combined.
  # Net of startup/shutdown overhead: see operations_reality.
  product_mix:
    bread: 0
    confection: 0
    specialty: 100
    catering: 0
  # 100% specialty custom orders. No bread; no standard pastry; no catering
  # trays. This studio is a pure custom-order operation.
  throughput_variance:
    worst_month_fraction_of_average: 0.15
    # January: post-holiday dead period. Wedding inquiry season begins in
    # January but lead times (4-12 weeks) mean baking revenue does not
    # materialize until Q2. Birthday and corporate orders drop sharply.
    # 0.15 = January revenue is ~15% of the monthly average; near shutdown.
    best_month_fraction_of_average: 2.10
    # October-November: wedding season peak + holiday-party corporate orders
    # + birthday season overlap. Some studios report double-booking refusals.
    # 2.10 = peak month is ~210% of average; studio operates at capacity ceiling.
    seasonal: "Q1 (Jan-Feb) near-dead; Q2 (Apr-Jun) and Q4 (Sep-Nov) are twin peaks driven by wedding season and holiday events; Q3 (Jul-Aug) is moderate (summer birthdays, anniversary orders)."

# ── OPERATOR PROFILE ──────────────────────────────────────────────────────────

operator_skill_floor: pastry-chef-master
# Custom cake production requires the full pastry-chef-master competence level
# per catalog/baking/SCHEMA.md §3: multi-tier stacked assembly (structural
# engineering of dowels, boards, and supports), fondant application and finishing
# to exhibition standard, buttercream piping at varying pressures and tip sizes,
# sugar-flower construction (gum paste, wafer paper), ganache and mirror-glaze
# finishing, color matching custom palettes from food-grade pigments, and
# client-communication design translation (turning a mood board into a cake
# architecture). This is the highest skill floor in the baking catalog.
# An operator who can bake excellent bread but has not specifically trained in
# cake artistry cannot run this studio; the skill set is distinct.

operators_concurrent: "1-2"
# Solo operation is viable and typical for small-city studios.
# A second operator (part-time assistant, decorator, or delivery driver) is
# economically justified in peak season and for large multi-tier orders.

apprentice_friendly: true
apprentice_path:
  training_stages: "Stage 1 (0-6 mo): foundational baking under supervision — cake layers, standard buttercream, basic leveling and filling, crumb-coating technique, refrigeration staging protocol. Gate: independently produces a consistent two-layer birthday cake meeting client-delivery standard. Stage 2 (6-18 mo): intermediate decoration — fondant application on simple round and square cakes, basic piping (borders, rosettes, writing), simple sugar work (molded fondant decorations, basic flowers). Gate: completes a fondant-covered tiered cake to journeyman-baker standard without rework. Stage 3 (18-36 mo): advanced decoration and structural work — multi-tier assembly with internal support systems, advanced piping (lace, ruffles, brush embroidery), sugar flowers (roses, peonies, succulents in gum paste), mirror glaze and ganache drip technique, custom color matching. Gate: completes a four-tier wedding cake from design brief to delivery with no master-baker intervention. Stage 4 (36-60 mo): client-management and design translation — intake consultations, tasting sessions, design-brief interpretation, pricing custom complexity. Gate: independently manages a client order from first inquiry through delivery."
  time_to_independent_operation: "~36 months to pastry-chef-master standard on basic cake production and decoration; 48-60 months to full design-consultation and complex-sugar-work independence"
  succession_note: "Apprentice co-presence during production integrates skill transfer into normal operations: the apprentice completes foundation tasks (mixing, baking, crumb coating) while the master focuses on high-skill decorating, making peak-season throughput sustainable. An apprentice who reaches Stage 3 can operate the studio independently for standard birthday and simpler wedding orders, providing partial succession coverage and a defined transition path."

# ── ECONOMICS ─────────────────────────────────────────────────────────────────

economics:
  currency: USD
  capital_cost: { low: 15000, mid: 28000, high: 55000 }
  # Low ($15,000): used commercial convection oven ($3,000-5,000), two
  # refurbished stand mixers ($400-800 each), basic refrigeration unit
  # ($800-1,500), decorating bench and tools ($500-1,000), leased space
  # fit-out minimal. Viable for a home-to-studio transition.
  # Mid ($28,000): new mid-tier commercial convection oven ($6,000-9,000),
  # two commercial stand mixers ($1,200-1,800 each), walk-in-style reach-in
  # refrigeration ($2,000-3,500), dedicated decorating bench with built-in
  # lighting ($800-1,500), display refrigerator for tastings/pickup ($1,000-2,000),
  # initial fondant/gum-paste tooling set ($500-1,000), turntables and cake
  # boards ($300-600), initial branding and packaging materials ($500-1,000).
  # High ($55,000): commercial combi or double-stack convection oven ($12,000-18,000),
  # three professional KitchenAid-or-equivalent stand mixers, walk-in refrigeration
  # ($6,000-10,000), full decorator's bench with airbrush station, professional
  # photography backdrop for portfolio, initial sugar-flower tooling, branded
  # premium packaging, point-of-sale and booking software, full first-year
  # marketing spend.
  install_cost: 4500
  # Electrical service upgrade for commercial convection oven (240V, 30-50A
  # dedicated circuit): $1,500-2,500. Mechanical extraction (ventilation hood
  # and exhaust fan): $800-1,500. Health-department commercial-kitchen inspection
  # and permit: $300-600. Plumbing (sink for pastry work): $400-800.
  # Mid estimate: $4,500. [CITATION-NEEDED: commercial kitchen ventilation and
  # electrical installation cost ranges for small commercial kitchens.]
  annual_maintenance: 1800
  # Convection oven service ($600/yr), stand mixer maintenance and bowl/attachment
  # replacement ($400/yr for two mixers), refrigeration service ($400/yr),
  # decorating tools replacement (tips, turntables, boards, piping bags) ($400/yr).
  # Estimated from comparable small-commercial-kitchen operating cost data.
  # [CITATION-NEEDED: small commercial bakery/pastry studio maintenance cost survey.]
  annual_consumables: 18000
  # Ingredient costs for 400 cake orders/yr × $40 variable_cost/order = $16,000
  # in direct ingredients (flour, sugar, butter, eggs, fondant, gum paste,
  # food-grade pigments, specialty fillings). Plus: packaging ($0.50-$2/order
  # depending on box size) × 400 = $800-$1,600. Electricity (16 kWh/day × 260
  # operating days × $0.12/kWh) = $499. Rounded consumables total: $18,000.
  # [CITATION-NEEDED: commercial fondant and gum-paste ingredient pricing;
  # consistent with boutique pastry-supply trade estimates circa 2024-2025.]
  floor_space_rent_per_year: 9600
  # 30 m² commercial kitchen/studio space in a small-city commercial zone.
  # Estimated at $320/m²/yr ($8.00-$12.00/sq ft US commercial-kitchen rate
  # for secondary market cities; small cities outside coastal metros).
  # = 30 m² × $320 = $9,600/yr. This is the imputed rate even for owner-
  # occupied space, for cross-entry comparability per schema semantics.
  # [CITATION-NEEDED: small-city commercial kitchen lease rates; consistent with
  # secondary-market US commercial real estate reports circa 2024-2025 but
  # not confirmed against a formal survey for this entry.]
  market_price_per_unit: { low: 150, mid: 350, high: 900 }
  # Per custom cake order. Low ($150): simple single-tier birthday cake,
  # minimal decoration, sheet-cake format, mass-market palette.
  # Mid ($350): two-to-three tier celebration cake (birthday, anniversary,
  # small wedding), fondant-covered or buttercream with moderate decoration.
  # High ($900): multi-tier wedding cake (4-6 tiers), elaborate sugar-flower
  # decoration, custom design, delivery and setup included.
  # Range reflects market segmentation across order types; the revenue mix
  # for a viable studio skews toward mid and high (wedding-centric revenue).
  # [CITATION-NEEDED: custom wedding cake price surveys; The Knot 2023 Real
  # Weddings Study reported median US wedding cake cost ~$500-800; trade
  # practitioner pricing forums and IBISWorld bakery industry reports consistent
  # with this range. Citation-level evidence required before promotion.]
  industrial_baseline_price: 35
  # Nearest industrial equivalent: a sheet cake or two-layer frosted birthday
  # cake from a major grocery retailer (Walmart, Costco, regional supermarket).
  # Walmart custom sheet cake: $18-$28; Costco half-sheet: $19.99; decorated
  # two-layer grocery cake: $25-$45. Mid-range estimate: $35.
  # Walmart makes approximately 20% of US wedding cakes by volume; the grocery-
  # store entry-level custom cake is the true industrial baseline, not the
  # boutique competitor. [CITATION-NEEDED: Walmart and Costco custom cake pricing
  # confirmed against current retail pricing; industry market-share data for
  # grocery-chain custom cakes from IBISWorld or comparable industry report.]
  pricing_notes: "Unit is one custom celebration cake order. Industrial baseline ($35) is a decorated grocery-store two-layer cake (Walmart/Costco equivalent); the artisan studio premium (4-25×) reflects custom design, master-level decoration (fondant, sugar work, multi-tier structural engineering), client consultation, and the event-specific irreplaceability premium that grocery chains cannot provide. Customer segment: couples planning weddings ($400-$900 budget), affluent birthday-party clients ($150-$400), and corporate event coordinators ($200-$600 for branded or themed cakes). The premium is supported by event-irreplaceability: a wedding cake cannot be substituted at the last minute; the client has paid a deposit 4-12 weeks in advance and the studio captures the full commitment value. Industrial baseline named and cited per schema requirement."
  pricing_validation: "Market price evidence: The Knot 2023 Real Weddings Study (median US wedding cake cost) and WeddingWire practitioner-survey data provide the primary pricing evidence for the high end of the range ($500-$900). Mid-range birthday and celebration cake pricing is inferred from small-business practitioner forums (Cake Central, Sugar Geek Show pricing guides) and secondary-market studio pricing observed in trade directories. Evidence type: industry consumer survey (The Knot) + practitioner-reported pricing from trade community sources; not a cost-plus residual. Direct competitor-pricing audit of small-city studios in target markets would strengthen the claim before promotion to reviewed. [CITATION-NEEDED: The Knot 2023 Real Weddings Study cake-cost data as primary citation.]"

# ── OPERATIONS REALITY ────────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Convection fan motor (bearing failure under repeated daily thermal cycling at cake-baking temperatures)"
      estimated_hours_to_failure: 2200
      replacement_cost: 380
      replacement_lead_time_days: 7
      serviceable_by: journeyman
      # From catalog/baking/SCHEMA.md §5: convection fan motor typical 2,000-4,000 hr.
      # Custom-cake studio cycles the oven daily; thermal cycling at 165-200°C
      # stresses the motor more than intermittent use; conservative end of range used.
      # [CITATION-NEEDED: commercial convection oven fan motor MTTF under daily use.]
    - item: "Stand mixer planetary gear or bowl-lift mechanism (overuse failure under frequent large-batch buttercream and fondant kneading)"
      estimated_hours_to_failure: 1800
      replacement_cost: 450
      replacement_lead_time_days: 10
      serviceable_by: journeyman
      # Stand mixers under commercial-intensity use (kneading fondant, whipping
      # large buttercream batches) fail faster than home-use ratings suggest.
      # Planetary gear wear is the most common failure mode; replacement parts
      # are available for KitchenAid Pro and Hobart N50 equivalents but require
      # a journeyman appliance tech. [CITATION-NEEDED: commercial stand mixer
      # MTTF under daily use; food-equipment repair service data.]
    - item: "Refrigeration compressor or thermostat (assembled-cake refrigeration running continuously)"
      estimated_hours_to_failure: 3000
      replacement_cost: 600
      replacement_lead_time_days: 14
      serviceable_by: specialist
      # Reach-in cake refrigerator runs 24/7 to hold assembled cakes at 4°C.
      # Continuous-duty refrigeration compressors fail more predictably than
      # intermittent-use units; thermostat drift is the earliest failure mode.
      # A specialist refrigeration tech is required; lead time for replacement
      # compressor in a non-standard commercial unit can reach 2-3 weeks.
      # [CITATION-NEEDED: commercial reach-in refrigerator compressor MTTF;
      # consistent with food-equipment trade service data but not entry-specific.]

  maintenance_schedule:
    daily:
      task: "Clean oven interior and remove residual baking debris; wipe decorating bench and sanitize surfaces; check refrigeration temperature log for assembled cakes in-hold; inspect cake boards and turntables for damage; review order schedule for next day"
      performed_by: operator
    weekly:
      task: "Deep-clean oven (degrease interior, inspect door seal and hinge); check stand mixer attachments and tighten bowl-lift mechanism; calibrate oven thermostat with external probe; restock consumables (fondant, gum paste, packaging, piping bags); refrigeration coil inspection"
      performed_by: operator
    quarterly:
      task: "Stand mixer planetary inspection and lubrication; oven heating element visual inspection; refrigeration condenser coil cleaning; decorating tool audit (replace worn tips, cracked turntables, damaged smoothers); health-permit inspection readiness check"
      performed_by: journeyman
    annual:
      task: "Full oven service (element test, thermostat calibration by specialist, door gasket replacement if indicated); refrigeration compressor inspection and refrigerant check by licensed specialist; stand mixer full rebuild if indicated; annual health-department commercial-kitchen inspection; insurance and liability policy review"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 45
  # Per operating day: 15 min oven preheat (oven requires full preheat before
  # baking layers; not productive time) + 15 min morning prep (mixer setup,
  # ingredient staging, order-board review) + 15 min end-of-day cleanup (bench
  # sanitization, oven shutdown, refrigeration check, order log update) = 45 min.

  max_active_hours_realism_note: "50 hr/wk is the combined ceiling for 1-2 operators across a 5-day operating week. Solo operation: 40 hrs/wk gross minus 45 min/day × 5 days = 3.75 hrs/wk startup-shutdown overhead, yielding ~36.25 hrs/wk net production time. Two-operator peak: 50 hrs combined. sim_params uses 50 combined hrs/wk as the ceiling for throughput derivation, acknowledging that solo operation constrains to ~36 hrs effective. The 400 cakes/yr throughput figure uses the blended (1-2 operator) scenario; solo-operation throughput is approximately 280-320 cakes/yr. Seasonal dead periods (Q1, mid-Q3) are folded into downtime_fraction rather than modeled as separate capacity reductions."

  interruption_notes: "Custom cake studio interruptions include: client inquiry calls and consultation scheduling (30-60 min/day during peak season); tasting appointments (1-2 hrs each, 2-4/week in Q2/Q4); design-revision discussions for current orders (15-30 min/order, not captured in standard decorating time); delivery and setup for destination weddings (half-day or full-day events, removing the operator from production entirely). Delivery days are excluded from throughput calculation but consume capacity disproportionately during peak wedding season. These interruptions are folded into downtime_fraction."

  consumables_lead_time_days: { typical: 3, worst: 21 }
  # Fondant, gum paste, and specialty food-grade pigments: typical 3-day
  # reorder from specialty baking supply (online or regional distributor).
  # Worst case (21 days): imported specialty ingredients (Belgian couverture
  # chocolate, specialty metallic dust, licensed-character decal wafer paper
  # for branded corporate cakes) with single international supplier; supply-
  # chain disruption can extend lead time to 3+ weeks.
  # [CITATION-NEEDED: specialty cake-supply distributor lead times; consistent
  # with practitioner-reported supply chain experience but not formally cited.]

  throughput_variance:
    seasonal: "Q1 (Jan-Feb) near-dead; Q2 (Apr-Jun) and Q4 (Sep-Nov) are twin peaks for weddings and holiday-party cakes; Q3 (Jul-Aug) moderate (birthdays, summer events)."
    worst_month_fraction_of_average: 0.15
    # January: inquiries arrive but deposits are thin and lead-time orders have
    # not converted to active production yet. Revenue from December orders may
    # still be collecting but new orders are scarce. Near-shutdown conditions.
    best_month_fraction_of_average: 2.10
    # October: peak wedding season overlap with Halloween specialty orders +
    # early holiday-party bookings. Studios routinely decline inquiries in
    # October due to booking saturation weeks in advance.

  operator_impact:
    noise_db: 58
    # Convection oven fan (~55 dB(A)) + stand mixer at bowl-speed (~60-65 dB(A))
    # during active use; decorating work is near-silent. Average across an
    # operating day: ~55-65 dB(A); well below hearing-damage threshold.
    # No industrial noise hazard in this studio environment.
    heat_exposure: "Moderate during oven-active sessions: convection oven exhaust raises kitchen ambient temperature by 3-7°C; adequate mechanical ventilation (required) mitigates sustained heat exposure. Decorating sessions are at ambient room temperature. No radiant heat exposure; substantially lower heat burden than any forge or deck-oven environment."
    emissions: "Near-zero combustion emissions (convection-electric oven). Minor aerosol from airbrush food coloring during decorating (food-grade pigment particles); operator should wear an N95 mask during airbrush work. Sugar caramelization with culinary torch produces minimal CO; adequate ventilation is sufficient. No particulate or chemical emission permitting trigger expected."
    physical_demand: "Moderate: sustained standing during decorating (4-6 hrs/day on hard floors); precision hand and wrist work (piping, fondant smoothing, sugar-flower assembly); lifting assembled tiered cakes (a 5-tier wedding cake can weigh 12-18 kg) during transport and delivery; repetitive mixing and bowl scraping. Ergonomic mat and anti-fatigue flooring are standard investments. Lower physical demand than bread-production or forge operations but repetitive fine-motor work creates wrist and hand strain risk over long careers."

# ── REGULATORY NOTES ──────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Commercial kitchen or mixed-use commercial zoning required; a home-based studio may qualify under home-occupation permits with kitchen inspection in some jurisdictions, but delivery, client visits, and commercial refrigeration typically require a commercial-zone address; verify local zoning before signing a lease."
  emissions: "Near-zero emissions profile; no air-quality permit trigger expected; culinary torch use (minor CO) does not reach commercial-combustion permit thresholds in any known US jurisdiction; airbrush aerosol (food-grade) does not trigger industrial emissions regulation."
  other: "Commercial kitchen health permit required (annual inspection by county/city health department); food handler certification required for all operators; state cottage-food laws typically do not cover custom wedding cakes at this revenue scale — full commercial licensing required; liability insurance for event delivery (wedding venue damage, product liability) is a contractual requirement for most wedding venues and strongly advised."

# ── CONTEXT FIT ───────────────────────────────────────────────────────────────

lens_fit:
  market: good
  cooperative: poor
  civic: poor

scale_fit:
  village: poor
  town: marginal
  small_city: good

# ── LENS CONTEXT ──────────────────────────────────────────────────────────────

# lens_context.cooperative and lens_context.civic are omitted: both are `poor`
# and no conditional block is triggered per catalog/SCHEMA.md §4 trigger rules.
# Rationale: custom cake is an artisan-market product driven by individual
# client relationships and premium brand identity. A cooperative ownership model
# is incompatible with the single-master-baker brand that sustains premium pricing;
# a civic facility has no civic-goods justification for subsidizing a premium luxury
# product. The market lens is the only viable frame for this entry.

# ── BAKING TRADE-SPECIFIC FIELDS ──────────────────────────────────────────────

flour_source_declaration: industrial-flour-purchased
# Custom cake studios purchase commodity or specialty cake flour from industrial
# distributors or restaurant-supply warehouses. At 400 orders/yr, flour volume
# (~180 kg/yr for cake flour; custom cakes use less flour per unit than bread)
# is far below the threshold that would attract a local-mill partnership.
# The premium positioning of this studio rests entirely on craft skill and
# design distinctiveness, not on grain provenance. Flour sourcing is not a
# customer-visible value claim in the custom cake market; fondant, fillings,
# and decoration execution are the visible differentiators.

# ── SIMULATION PARAMETERS ─────────────────────────────────────────────────────

sim_params:
  cost_mean: 28000
  # Equals economics.capital_cost.mid per E3-R1 requirement.
  cost_sd: 10000
  # (55,000 - 15,000) / 4 = 10,000. Ratio: 10,000 / 28,000 = 0.357.
  # Within 0.15-0.50 plausible range (E3-R5) ✓
  throughput_units_equiv_per_year: 400
  # 2 cake orders/day × 5 days/wk × 52 wk × (1 - 0.22 downtime) = 405,
  # rounded to 400. See Key Assumptions for unit definition and seasonal
  # derating rationale. This figure represents blended 1-2 operator scenario.
  # E-3 cross-check: 50 hr/wk × 52 × 0.78 / 5 hr/unit = 2028 / 5 = 406 ≈ 400 ✓
  variable_cost_per_unit: 40
  # Per cake order: specialty cake flour (~$2-4), sugar/butter/eggs (~$8-12),
  # fondant or premium buttercream ($8-15), specialty fillings/ganache ($4-8),
  # gum-paste/sugar-flower materials ($3-6), food-grade pigments ($1-2),
  # board, box, ribbon, packaging ($2-4). Central estimate: $40/order.
  # [CITATION-NEEDED: specialty cake ingredient cost breakdown; consistent with
  # trade practitioner cost-of-goods estimates but formal citation required.]
  labor_hours_per_unit: 5.0
  # Combined operator hours per cake order (1-2 operators, blended).
  # Simple birthday cake: ~2-3 hrs. Standard wedding tier: ~6-8 hrs.
  # Average across order mix: ~5 hrs. E-3 R3 cross-check:
  # 400 × 5.0 = 2,000 labor hrs ≈ 50 hr/wk × 52 × 0.78 = 2,028 hrs ✓
  downtime_fraction: 0.22
  # Components: seasonal dead weeks (Q1 January-February: ~8 weeks at near-
  # zero production = ~8/52 = 0.154 effective); equipment failures and
  # maintenance (~0.03); delivery days removing operator from production
  # (~0.02); miscellaneous illness/admin (~0.016). Total: ~0.22.
  # Consistent with worst_month_fraction of 0.15 (E3-R6 ✓).
  lifespan_years: 15
  # Commercial convection oven: 12-18 years under moderate daily use.
  # Stand mixers: 10-20 years (varies by brand; Hobart commercial mixers
  # exceed 25 years with maintenance). Refrigeration: 12-15 years.
  # Binding asset is the oven; 15 years is the central estimate.
  # [CITATION-NEEDED: commercial convection oven service-life data.]

# ── RESULTS ───────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: win
    primary_metric: 0.4827688651218063
    metric_name: payback_years
    notes: ''
  village_coop:
    verdict: fail
    primary_metric: 158.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=158, total_annual_cost=31567
  village_civic:
    verdict: fail
    primary_metric: 41.766666666666666
    metric_name: per_household_cost
    notes: per_hh=41.77, threshold=120, hrs/capita=0.000 vs threshold=2.0
  town_market:
    verdict: marginal
    primary_metric: 0.4827688651218063
    metric_name: payback_years
    notes: wage_verdict=marginal (take_home=64720 vs median=56000)
  town_coop:
    verdict: win
    primary_metric: 158.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=158, total_annual_cost=31567
  town_civic:
    verdict: fail
    primary_metric: 6.1421568627450975
    metric_name: per_household_cost
    notes: per_hh=6.14, threshold=100, hrs/capita=0.000 vs threshold=2.0
  small_city_market:
    verdict: marginal
    primary_metric: 0.4827688651218063
    metric_name: payback_years
    notes: wage_verdict=marginal (take_home=64720 vs median=62000)
  small_city_coop:
    verdict: win
    primary_metric: 158.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=158, total_annual_cost=31567
  small_city_civic:
    verdict: fail
    primary_metric: 1.1601851851851852
    metric_name: per_household_cost
    notes: per_hh=1.16, threshold=80, hrs/capita=0.000 vs threshold=2.0
sources:
  - ref: "catalog/baking/SCHEMA.md v1.0 (schema_base_version 1.1, 2026-04-19). Baking throughput block, convection-electric energy-source definition, pastry-chef-master skill-floor definition, Group B author guidance for bake-009."
  - ref: "catalog/SCHEMA.md v1.1 (2026-04-19). Base schema: all required fields, conditional triggers, validation rules, sim_params cross-check conventions."
  - ref: "catalog/baking/entries/005-mobile-popup-bakery.md (bake-005). Structural reference: solo-operator succession risk framing, convection-electric energy use figures, consumables cost methodology."
  - ref: "[CITATION-NEEDED: The Knot 2023 Real Weddings Study — primary citation for wedding cake pricing range ($400-$900 median). Required before promotion to reviewed. Published annually by The Knot; 2023 edition surveys ~10,000 US couples.]"
  - ref: "[CITATION-NEEDED: IBISWorld US Bakeries Industry Report (2023-2025) — market-size data, grocery-chain share of wedding cakes (~20% Walmart estimate), industry revenue benchmarks. IBISWorld industry code 31181 or 722515.]"
  - ref: "[CITATION-NEEDED: Walmart and Costco custom cake retail pricing — confirmation of $35 industrial baseline price. Publicly available from retail websites; snapshot citation with access date required before promotion.]"
  - ref: "[CITATION-NEEDED: commercial convection oven kWh/hr consumption — confirmation of 3.5 kWh/hr at cake-baking temperatures. Manufacturer specification sheets or energy-audit data for commercial bakery equipment.]"
  - ref: "[CITATION-NEEDED: commercial stand mixer MTTF under daily food-service use — first_year_failures item for planetary gear failure. Food-equipment service industry data or manufacturer commercial-use ratings.]"
  - ref: "[CITATION-NEEDED: commercial reach-in refrigeration compressor MTTF — first_year_failures item. Food-service equipment service data; commercial refrigeration trade sources.]"
  - ref: "[CITATION-NEEDED: small-city commercial kitchen lease rates ($/m²/yr) — floor_space_rent_per_year $9,600 estimate. US commercial real estate reports for secondary-market cities; CoStar or LoopNet data circa 2024-2025.]"
  - ref: "[CITATION-NEEDED: specialty cake-supply distributor pricing (fondant, gum paste, food pigments) — variable_cost_per_unit $40 estimate. Specialty baking supply trade pricing from sources such as Global Sugar Art, Satin Ice, Tomric, or equivalent distributor price lists.]"
  - ref: "Mintz, Sidney W. 1985. Sweetness and Power: The Place of Sugar in Modern History. Viking. — historical grounding for sugar-confectionery as elite cultural form; Victorian wedding cake origins."
  - ref: "Freeman, June. 2004. The Making of the Modern Kitchen. Berg Publishers. — background on Victorian confectionery trade and celebration-cake commercial emergence."
---
## Summary

Bake-009 is a custom celebration cake studio operated by one to two practitioners at the pastry-chef-master skill level. The studio produces bespoke cakes for weddings, milestone birthdays, and corporate events on a lead-time order model: clients book 4-12 weeks in advance, pay a deposit at consultation, and receive a one-of-a-kind product that cannot be substituted from any industrial source on short notice. The defining economic characteristic is high per-unit value ($150-$900 per order) and low throughput (5-20 orders per week at peak, near zero in the Q1 dead period), generating revenue that is lumpy, seasonal, and dependent on sustained client-relationship management. The studio targets a small-city market, where the resident population and its event calendar (weddings, corporate milestones, affluent birthday clients) are large enough to sustain 400 orders per year at premium pricing without a population density that brings in large national competitors. This is not an accessible or community-oriented entry: it occupies the premium custom market that survived industrial consolidation precisely because industrial producers cannot replicate the design-consultation and cake-artistry experience at affordable scale.

## Design rationale

No other entry in the baking catalog addresses the custom-order celebration market. Bake-001 through bake-005 are production-focused bread and artisan-loaf entries where throughput is maximized per operating hour and per-unit value is low to moderate. Bake-006 (Viennoiserie) and bake-007 (Wagashi) are specialty product studios, but they operate on a retail-display or direct-sale model rather than a commission-order model: the product is made and displayed, and customers choose from what is available. Custom cake is structurally different: every unit is client-specified, no unit exists before the order is placed, and the operator's calendar is sold in advance rather than post-production. This event-calendar model is the defining feature that places bake-009 in its own design-space cell. The high per-unit value relative to input cost creates the market lens viability; the low throughput ceiling creates the scale constraint that limits viability to small cities and above. The distinction from a grocery-chain bakery department is also categorical: grocery-chain custom cakes (bake-and-decorate from a standard template) require journeyman-baker skill at most; this studio requires pastry-chef-master level for the full design-to-delivery cycle. Bake-009 is the premium custom-market survivor, not a generic bakery with a cake menu.

## Historical lineage

Three functional precedents inform this entry. The first is the Victorian and Edwardian confectionery shop, which introduced the tiered and decorated celebration cake as a commercial product for elite urban markets from roughly the 1840s onward. Prior to this period, elaborate multi-tiered cakes were the province of aristocratic households with dedicated pastry staff; the confectionery shop made the form available to the merchant and professional classes at a price. What this entry carries forward: the commission-order model (client consults with a skilled confectioner, specifies design elements, pays a premium for craft execution), the event-irreplaceability premium, and the high skill floor. What it does not carry forward: the Victorian confectionery shop's product range (including marzipan, sugar sculpture, and confection categories no longer commercially mainstream), the workshop-apprentice labor structure of the period, and the absence of health-department regulation. The second precedent is the mid-century American wedding-cake tradition that consolidated around the 1950s-1970s: the emergence of a recognizable professional wedding-cake industry serving the postwar mass-wedding market, with regional bakeries building reputation through wedding-show demonstrations and bridal-fair presence. This tradition established the consumer expectation of a custom wedding cake as a standard wedding expenditure rather than a luxury; it is the commercial form this studio inherits and occupies. The third precedent is the modern cake-design competition circuit (television competition shows from the 2000s onward: Ace of Cakes, Cake Boss, Sugar Rush, and analogues), which expanded consumer awareness of high-end custom cake design and created a market signal that master-level cake artistry commands a significant premium. What this entry carries forward from the competition circuit: the consumer vocabulary for articulating custom-design preferences (sugar flowers, fondant finishing, geode cakes, watercolor buttercream, etc.) and the customer willingness to pay $500-$900 for a competition-adjacent aesthetic. What it does not carry forward: the television-show scale (multi-person specialist teams), the marketing infrastructure of celebrity cake studios, or the viewer-facing entertainment framing.

A note on anti-romanticism: the wedding cake as a cultural institution is a Victorian invention for elite markets, approximately 150 years old. It was rapidly industrialized through the 20th century; Walmart and Costco together serve a substantial share of the US wedding-cake market at price points ($18-$45) that a custom studio cannot compete on. The custom-studio market that this entry targets is the premium segment that survived industrialization specifically because it offers something the industrial channel cannot: client-specified design, master execution, and the event-irreplaceability premium. This is not a timeless tradition — it is a market niche defined by what industrial consolidation left behind.

## Key assumptions

**Capital cost.** The $15,000-$55,000 range reflects three equipment scenarios described in the economics block. The central estimate ($28,000) represents a purpose-built studio with new mid-tier equipment — not the minimum viable configuration (used equipment, $15,000) and not the fully-fitted premium studio ($55,000). cost_sd = $10,000 (ratio 0.357, within the 0.15-0.50 plausible range). The asymmetry in the range (low at $15,000 vs. mid at $28,000 and high at $55,000) reflects that the high-end scenario includes marketing and fit-out costs that scale disproportionately; the arithmetic mean ($35,000) is above the mid, and cost_mean ($28,000) is set at the modal cost for a competent studio fit-out rather than the arithmetic mean. This asymmetry is documented here per schema guidance.

**Throughput unit definition.** One "custom cake order" is the unit, regardless of tier count or complexity. This choice creates internal variance in labor content (a single-tier birthday cake requires ~2-3 hrs; a five-tier wedding cake requires ~8-12 hrs), which is acknowledged in labor_hours_per_unit as an average (5 hrs/order blended). For simulation purposes, the average holds if the revenue mix is approximately 60% mid-complexity (2-3 tier, $200-$500) and 40% simple-to-elaborate, which is consistent with the market distribution of a viable small-city custom studio. An operator running predominantly $900 wedding orders would have higher revenue per unit but lower unit throughput; the mid-range assumption is used here and should be noted as a key sensitivity.

**Seasonal derating.** The downtime_fraction of 0.22 incorporates heavy Q1 dead-period: January and February combined account for roughly 8 of 52 weeks at near-zero production (worst_month_fraction = 0.15 of average, implying those weeks produce ~6% of the monthly average cake order rate). Folding these into downtime_fraction rather than modeling them separately is a deliberate simplification; the sim_params throughput figure of 400 orders/year already reflects this derating via the 0.78 productive-fraction multiplier. An alternative model would cap weekly throughput at 15 orders/week (5-day, 2 cakes/day, 1.5 operators equivalent) and then multiply by an effective-weeks count (~46 weeks after removing dead-period weeks), yielding 15 × (52 × 0.78)/5 × 5 ≈ similar figure. Both approaches converge at approximately 400 orders/year.

**E-3 cross-check.** throughput_units_equiv_per_year (400) × labor_hours_per_unit (5.0) = 2,000 labor hrs. max_active_hours_per_week (50) × 52 × (1 - 0.22) = 2,028 hrs. Discrepancy of 28 hrs (1.4%) is within rounding; E-3 R3 is satisfied.

**Flour source.** industrial-flour-purchased is declared. Custom cake production uses relatively little flour per order (compared to artisan bread), and the flour cost is a minor component of variable cost (roughly $2-4/order). No local-mill partnership or provenance story is plausible or economically meaningful at this volume and product type. Premium positioning is built on design skill, not ingredient sourcing.

**Industrial baseline.** The $35 grocery-store custom cake is the honest industrial baseline, not a boutique bakery competitor. Walmart's market share in custom cakes (estimated ~20% of US wedding cake volume; [CITATION-NEEDED: IBISWorld or comparable industry source]) establishes that the industrial channel is the actual competition, not other artisan studios. The custom studio serves a segment that has already self-selected out of the grocery-store option; the pricing premium is not defended against other artisan studios but against the grocery alternative.

## Known risks / failure modes

**Regulatory.** The primary regulatory risk is commercial kitchen licensing. Home-based custom cake studios under cottage-food laws face revenue caps (commonly $25,000-$50,000/yr in states that permit them; some states exclude custom cakes requiring refrigeration from cottage-food exemption entirely) that may be breached before the studio reaches financial viability. A studio at 400 orders/year × $350 average = $140,000 in revenue far exceeds cottage-food thresholds; full commercial kitchen licensing is required. Health-department commercial kitchen inspections are annual events that can temporarily suspend operations; a failed inspection during peak wedding season is a catastrophic revenue event if in-progress orders must be transferred or refunded. Liability for event delivery is a secondary regulatory exposure: a wedding-cake delivery accident (dropped cake, vehicle incident en route to venue) creates a product-liability claim against the studio that inadequate insurance may not cover. Wedding-venue contracts commonly require $1-2 million in product liability coverage.

**Labour pipeline.** The pastry-chef-master skill floor is the highest in the baking catalog and represents a genuine succession challenge. Unlike journeyman-baker entries, where the skill pool is broader, master-level cake artists who are both technically excellent and business-competent are rare. A studio operator who is injured, becomes ill, or exits the business without a trained successor loses not only revenue but the customer relationships and booking calendar that constitute the studio's primary asset. The apprentice path described in this entry (36-60 months to full independence) represents the best-case succession scenario; it requires consistent investment in apprentice training during normal operations, and the economic model of a solo or two-person studio provides limited capacity for formal training time. The `apprentice_friendly: true` designation reflects that an apprentice path exists and is described; it does not guarantee that any given studio will execute it. Studios that operate without an apprentice in development should explicitly note succession risk in their operating plan.

**Supply chain.** The most critical supply-chain risk is the availability of specialty decorating materials: imported fondant brands, specific gum-paste formulations, licensed-character wafer paper for branded corporate cakes, and specialist food-grade pigments (metallic gold/silver, specific Pantone-matched colors). These materials have single or dual suppliers in many markets, and a supply disruption 2-3 weeks before a booked wedding order cannot be resolved by substitution — color-matching or alternative sourcing may not produce an acceptable result on short notice. The 21-day worst-case lead time for specialty materials is a planning constraint: the studio must carry 4-6 weeks of specialty inventory for booked orders during peak season. A secondary supply risk is electricity: a power outage during a critical decorating session (assembled cake with buttercream melting, refrigeration failure) can destroy hours of work. Generator backup for pre-delivery holding refrigeration is a justified investment for any studio with a significant revenue event the following day.

**Event-calendar revenue lumpiness.** The core business risk of this model is cashflow volatility that is intrinsic to the event-calendar revenue cycle. A slow Q1 followed by a booked Q2 peak requires working-capital discipline: the studio may have 20 confirmed orders with deposits in hand for April-May while generating near-zero revenue in January-February. If the studio is paying commercial rent in Q1 ($800/month) against near-zero revenue, the working-capital requirement is 2-3 months of expenses covered by prior-season savings or deposit float. This is not a failure mode that can be engineered away; it is a structural feature of the event-driven model that operators must plan for explicitly.

## Iteration log

- 2026-04-18: v0.1 — initial entry authored per Plan G Task 11. Custom celebration cake studio; convection-electric, market-primary, small-city primary, pastry-chef-master skill floor, 1-2 operators, industrial-flour-purchased, apprentice_friendly: true. Throughput unit defined as "custom cake order" with blended labor-hours rationale. Seasonal dead-period (Q1) folded into downtime_fraction. Anti-romanticism section on Victorian wedding-cake origins and Walmart market-share included in Historical Lineage. Cooperative and civic lenses omitted (both poor) with explicit rationale. No docs/superpowers/ paths used.
