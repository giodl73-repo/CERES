---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: bake-001
trade: baking
name: "Sourdough Artisan Micro-bakery (electric deck, village/town scale)"
tagline: "Single-operator naturally-leavened bread bakery with premium direct-to-consumer pricing"
status: draft
version: "0.1"
supersedes: null
inspirations:
  - american-frontier-home-baking-tradition
  - modern-sourdough-revival-dtc

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 25
# Mid-range of the 20-30 m² envelope; adequate for one operator, deck oven,
# proofing cabinet, mixer, and staging. Excludes customer-facing space or
# retail area. Per REQUIREMENTS Group A guidance; 25 m² represents a
# full-function single-operator micro-bakery bay.
# [CITATION-NEEDED: commercial survey of single-operator artisan bakery floor
# areas; structural inference from baking SCHEMA.md §6 Group A guidance and
# common commercial kitchen footprints.]

ceiling_min_m: 2.5
# Minimum required for overhead clearance with deck oven stack and exhaust
# hood installation. No combustion clearance above this is required for
# electric deck; 2.5 m is the functional minimum for kitchen-exhaust-hood
# installation per commercial kitchen design standards.
# [CITATION-NEEDED: commercial kitchen design ceiling height minimums;
# derived from ventilation requirement and standard hood installation clearances.]

ventilation: kitchen-exhaust-hood-required
# Electric deck oven produces heat and steam; a commercial kitchen exhaust hood
# is required for operator comfort and local code compliance in any commercial
# food-production space. No combustion gases; no air-quality permit trigger
# from the oven source. Steam and heat from baking operations necessitate
# mechanical extraction to maintain habitable ambient temperatures during
# multi-hour baking sessions. [Commercial kitchen code requirements; local
# jurisdiction may require hood inspection and certification.]

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: electric-deck
energy_consumption_per_active_hour: "5.5 kWh"
# Per baking SCHEMA.md §2 electric-deck range of 3-8 kWh/batch; 5.5 kWh/batch
# at 2 batches/day and approximately 2-3 active oven-hours per batch represents
# a mid-range consumption figure for a single-deck commercial unit (approx.
# 8-12 kW rated power). Active-hour consumption during sustained baking at
# operating temperature is estimated at 5.5 kWh/hr.
# [CITATION-NEEDED: manufacturer energy consumption data for commercial electric
# deck ovens in the 8-12 kW range; illustrative estimate within baking SCHEMA.md
# §2 electric-deck range; not directly sourced from metered measurement.
# Label: pricing_validation: inferred.]

backup_fuel: null
# No backup fuel in the base configuration. Electric deck is the sole heat
# source. Grid outage risk is noted in Known Risks but no backup fuel system
# is included in this design; a backup arrangement (propane combi) would
# elevate capital cost substantially and is a candidate for a variant entry.

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  loaves_per_day: 115
  # Net production output per full operating day. Unit: 800g sourdough boule
  # equivalent (see Key Assumptions for unit definition). Mid-range of the
  # 80-150 loaves/day parameter; 115 represents a realistic full-day output
  # for a single operator running 2 batches on a standard single-deck commercial
  # oven with 8-15 loaves per batch per oven load (8-15 × 2 batches × 2 loads
  # per batch window = up to ~60 loaves/batch cycle; with proofing schedule
  # staggering, 115/day is achievable across the 7-hour active production window).
  # [CITATION-NEEDED: empirical throughput measurement for single-operator
  # sourdough micro-bakery with electric deck oven; illustrative estimate from
  # baking SCHEMA.md §1 village artisan range 30-100 loaves/day, noting that
  # 115 is at the high end of the town-artisan lower bound; label: inferred.]

  batches_per_day: 2
  # Two oven loads per operating day, consistent with standard artisan sourdough
  # scheduling: overnight cold retard + morning bake (batch 1), midday proof +
  # afternoon bake (batch 2). Each batch occupies approximately 45-60 minutes
  # oven time; total bake time per day ~90-120 minutes, leaving operator time
  # for mixing, shaping, packaging, and farmers-market prep within the 35 hr/wk
  # ceiling. [Structural inference from standard sourdough production scheduling;
  # CITATION-NEEDED: empirical scheduling data for two-batch micro-bakery operation.]

  batch_size_loaves: 12
  # Mid-range of 8-15 loaves per batch as stated in entry parameters. A standard
  # single-deck commercial oven (0.5-0.8 m² deck area) accommodates approximately
  # 8-16 loaves of 800g boule size depending on oven model and spacing.
  # [CITATION-NEEDED: deck-oven capacity per m² of deck area; typical commercial
  # deck oven manufacturer specifications, e.g., Bongard, Sveba-Dahlen, or
  # equivalent; illustrative estimate; label: inferred.]

  max_active_hours_per_week: 35
  # Total operator active time per week including prep, mix, shape, proof
  # monitoring, bake, cool, package, and market/delivery overhead. This is the
  # gross ceiling including the 60 min/day startup-shutdown overhead. Net active
  # bake production time is approximately 30 hr/wk after overhead deduction.
  # Per entry parameters; consistent with baking SCHEMA.md §1 realistic ceiling
  # of 35-45 hr/wk for full-time single-operator artisan bakery.

  product_mix:
    bread: 70
    # Artisan sourdough and naturally-leavened loaves; the core revenue product.
    # Includes: country boules, batards, rye blends, seeded loaves.
    confection: 10
    # Simple pastry: scones, soda bread, laminated-free enriched rolls (no
    # laminated doughs without pastry-chef-master skill floor per SCHEMA.md §3).
    specialty: 20
    # Specialty loaves: whole-grain heritage wheat, rye-dominant loaves,
    # seasonal and flavored sourdoughs (olive, walnut, herb).
    catering: 0
    # No catering in the base configuration; farmers-market and DTC only.
    # Sum: 100.

  throughput_variance:
    seasonal: "Moderate winter uptick (holiday gifting, soup-season bread demand); summer trough at farmers markets; July-August slowdown typical for artisan bread retail"
    worst_month_fraction_of_average: 0.65
    # Artisan bread shows moderate seasonality; typical range 0.55-0.75 per
    # baking SCHEMA.md §1. 0.65 reflects a mid-range summer trough for a
    # farmers-market-primary operation that loses some weekend traffic to
    # outdoor-activity competition. [Baking SCHEMA.md §1 throughput_variance
    # guidance; CITATION-NEEDED: empirical worst-month fraction for artisan
    # bread micro-bakery retail.]
    best_month_fraction_of_average: 1.30
    # Consistent with baking SCHEMA.md §1 artisan bread range 1.20-1.40.
    # Pre-holiday and fall peak for bread-gift and holiday-table demand.
    # [Same source as worst_month_fraction_of_average.]

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: journeyman-baker
# Sourdough management requires formed fermentation judgment: the operator must
# independently manage starter health, bulk fermentation timing, and proofing
# schedules without supervision. Per baking SCHEMA.md §3: journeyman-baker can
# manage full sourdough cycle, run a deck oven without supervision, and produce
# consistent commercial-scale output. Apprentice-baker level is insufficient for
# sourdough management per SCHEMA.md §3 explicit boundary.
# [Baking SCHEMA.md §3 operator skill definitions]

operators_concurrent: "1"
# Single operator throughout. Apprentice presence is beneficial during production
# peaks but is not required for normal operation. The sourdough cycle timing
# and deck oven management are manageable by one journeyman baker.

apprentice_friendly: true
apprentice_path:
  training_stages: >
    Stage 1 (0-3 months): bakery safety, sanitation, equipment operation (mixer,
    proofer, deck oven startup and shutdown), sourdough starter feeding and
    observation. Gate criterion: can safely operate and clean all equipment
    unassisted; can maintain a starter on schedule without prompting.
    Stage 2 (3-9 months): dough mixing ratios, bulk fermentation monitoring
    under supervision, basic shaping (round boule). Gate criterion: completes
    10 consecutive standard boules to journeyman-accepted shape and crumb
    standard without guidance on the final three.
    Stage 3 (9-24 months): full bulk fermentation judgment, proofing-schedule
    reading, oven-load timing, packaging and market preparation. Gate criterion:
    operates full production day independently with journeyman review of output
    at end of day for five consecutive days.
    Stage 4 (24-42 months): specialty loaf recipes, product-mix adjustments,
    customer relationship management, starter troubleshooting. Approximate
    journeyman standard on this equipment configuration.
  time_to_independent_operation: "~36-42 months to journeyman-baker standard on sourdough production at this scale; fermentation judgment formation is the rate-limiting step and cannot be accelerated beyond the lived experience of seasonal variation cycles"
  succession_note: >
    Apprentice co-presence during production — Stage 2 onward — is integrated
    into normal operations at no separate cost: the apprentice assists with
    shaping, packaging, and market load-out while acquiring hands-on fermentation
    observation under journeyman instruction. The bakery does not require a
    formal apprenticeship program; the co-production model follows the American
    craft-bakery tradition of informal skill transmission through daily
    participation in the production cycle.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 18000, mid: 32000, high: 55000 }
  # Low: entry-level commercial electric deck oven (~$10,000-$12,000 secondhand
  # or budget new), basic proofing cabinet (~$2,000), commercial spiral mixer
  # (~$2,500), bannetons, lames, misc smallwares (~$1,500). Minimal fitout.
  # Mid: mid-range commercial deck oven ($14,000-$18,000 new), full proofing
  # cabinet with humidity control ($4,500), commercial spiral mixer ($4,000),
  # full smallware set, bakery display shelving, point-of-sale tablet setup.
  # High: premium multi-deck commercial oven ($22,000-$28,000), full humidity
  # proofing cabinet, heavy-duty spiral mixer with dough divider, walk-in
  # proofer upgrade, full commercial kitchen fitout and exhaust hood installation.
  # [CITATION-NEEDED: capital cost data for commercial electric deck ovens,
  # proofing cabinets, and commercial spiral mixers, 2024-2026; illustrative
  # estimates from market observation of bakery equipment vendors (Bongard,
  # Sveba-Dahlen, Globe, Hobart, etc.); not sourced from formal industry survey.
  # Label: pricing_validation: inferred.]

  install_cost: 4000
  # Electrical service upgrade if required (30-60A dedicated circuit per deck
  # unit), exhaust hood installation and ductwork, health-department inspection
  # and commercial kitchen certification, initial deep-clean and setup.
  # Single-estimate; regional variation substantial.
  # [CITATION-NEEDED: installation cost data for commercial bakery kitchen
  # fitout; illustrative estimate from general commercial kitchen contractor
  # cost ranges; label: inferred.]

  annual_maintenance: 1200
  # Deck element inspection and cleaning, proofing cabinet calibration,
  # mixer bowl and hook inspection, exhaust hood cleaning (quarterly), small
  # appliance maintenance. Excludes first-year failure replacements itemized
  # in operations_reality.
  # [CITATION-NEEDED: annual maintenance cost data for commercial electric
  # deck bakery operations; illustrative estimate; label: inferred.]

  annual_consumables: 8500
  # Primary: flour (commodity bread flour or specialty flour purchased from
  # industrial distributor — see flour_source_declaration). Flour dominates
  # consumables cost (~$5,500-$6,000/yr at 115 loaves/day × 285 days ×
  # ~0.7 kg flour/loaf × ~$0.60/kg commodity bread flour [CITATION-NEEDED:
  # commodity bread flour price per kg, US wholesale 2024]).
  # Remaining: salt (~$200/yr), water/utility overage (~$300/yr), packaging
  # materials — paper bags, labels, twist-ties (~$1,200/yr), sourdough starter
  # maintenance consumables (~$300/yr). Mid-point estimate.
  # [CITATION-NEEDED: commodity bread flour pricing per kg at US wholesale
  # distributor level, 2024; packaging materials costs for small-batch artisan
  # bakery; label: inferred.]

  floor_space_rent_per_year: 3000
  # Imputed at ~$120/m² per year for commercial kitchen or light-commercial
  # space in a village or town setting; 25 m² × $120/m²/yr = $3,000.
  # Commercial kitchen rental (shared-kitchen model available as an alternative
  # to lease) may reduce this cost; standalone lease in smaller markets may
  # be lower than metro rates. Owner-operator scenarios should impute this
  # cost for consistent cross-entry comparison per catalog/SCHEMA.md §6.
  # [CITATION-NEEDED: commercial kitchen or light-commercial rental rate per
  # m² in US village and town markets; illustrative estimate; label: inferred.
  # CoStar or shared-kitchen aggregator data (e.g., Kitchen United, The Food
  # Corridor) would be the appropriate verification source.]

  market_price_per_unit: { low: 5, mid: 8, high: 12 }
  # Per loaf equivalent (800g sourdough boule equivalent). Low: commodity-
  # adjacent entry-level artisan pricing ($5 for plain sourdough at a
  # farmers market in a cost-sensitive region). Mid: standard premium artisan
  # sourdough retail price in a mid-tier market ($8 for a standard country
  # boule). High: premium specialty or heritage-grain loaf pricing in a higher-
  # income DTC or farmers-market context ($12 for whole-grain or seeded loaf).
  # Industrial baseline: $3 (mass-produced supermarket sliced sourdough loaf
  # equivalent). See pricing_notes.
  # [CITATION-NEEDED: empirical artisan sourdough retail pricing survey in
  # US farmers-market and DTC bakery channels, 2024-2026; illustrative estimate
  # from market observation; label: pricing_validation: inferred.]

  pricing_notes: >
    Unit is an 800g sourdough boule equivalent. Premium over mass-produced
    industrial sourdough loaf ($3/loaf at major US supermarket; Sara Lee,
    Pepperidge Farm or private-label equivalents [CITATION-NEEDED: US
    supermarket sourdough shelf price survey, 2024]) reflects: (1) naturally-
    leavened fermentation process (longer proof cycle, distinct flavor and
    crust development not achievable at industrial scale without process
    additives); (2) direct-to-consumer sale eliminating the distributor and
    retailer markup chain; (3) premium customer segment willing to pay for
    local sourcing story and fresh-baked product. The $5-$12 range targets
    farmers-market and DTC subscription customers, not supermarket or food-
    service bulk buyers. Customers choosing artisan sourdough at $8 over
    supermarket sourdough at $3 are not substituting on price; the artisan
    segment is partially price-inelastic within the premium-bread customer base.

  pricing_validation: >
    Pricing evidence: inferred from market observation of artisan bakery
    pricing at US farmers markets and DTC bakery websites and subscription
    box services circa 2024-2026. NOT directly sourced from a formal industry
    pricing survey or published rate-card study. This is a placeholder-inferred
    figure. Recommended verification: USDA Agricultural Marketing Service
    farmers-market pricing surveys, Specialty Food Association market reports,
    or direct survey of operating artisan micro-bakeries in comparable markets.
    This field carries a citation-needed flag per the project citation policy.

  industrial_baseline_price: 3
  # Mass-produced supermarket sourdough loaf (Sara Lee, Pepperidge Farm, or
  # major private-label equivalent): approximately $3-$4 per loaf at US
  # supermarket retail pricing. The $3 figure represents the low end of mass-
  # market artisan-branded supermarket bread, not commodity white bread ($1.50-
  # $2.50). Using $3 as the competitive baseline anchors the premium analysis
  # to the most relevant direct substitute a consumer might choose instead of
  # a farmers-market sourdough.
  # [CITATION-NEEDED: US supermarket sourdough bread shelf pricing survey,
  # 2024; illustrative estimate from market observation; label: inferred.]

# ── TRADE-SPECIFIC FIELDS ────────────────────────────────────────────────────

trade_specific:
  flour_source_declaration: industrial-flour-purchased
  # Mill dependency declared explicitly per DECLINE-VERDICT mill-dependency
  # falsifier and baking SCHEMA.md §4. This bakery purchases commodity or
  # specialty bread flour from an industrial mill or regional distributor.
  # No mill infrastructure is owned or operated. No direct farm relationship
  # is assumed in the base configuration.
  # Supply-chain risk: price volatility of commodity wheat flour (driven by
  # global wheat market conditions); availability disruption in supply-chain
  # stress scenarios. The premium market positioning of this entry does NOT
  # depend on grain-sourcing differentiation in the base configuration;
  # the artisan premium is derived from process (natural leavening, deck baking)
  # and direct-to-consumer relationship rather than ingredient provenance.
  # Authors of entries claiming local-mill-partnership or integrated-milling
  # should create variant entries (bake-002 or later) per baking SCHEMA.md §4.
  # See Key Assumptions for specific flour sourcing discussion.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Deck heating element (electric)"
      estimated_hours_to_failure: 2000
      replacement_cost: 600
      replacement_lead_time_days: 14
      serviceable_by: specialist
      # Electric deck heating elements degrade under repeated thermal cycling.
      # Per baking SCHEMA.md §5 reference list: 1,500-3,000 hr typical range;
      # 2,000 hr is within that range for a unit running ~5 hr/day × 285 days
      # ≈ 1,425 hr/yr — likely to hit first-element failure in year one or early
      # year two. Replacement requires a specialist or factory-trained technician
      # and factory-ordered element; 14-day lead time is optimistic (may be
      # longer for less common deck oven models).
      # [Baking SCHEMA.md §5 first_year_failures reference; CITATION-NEEDED:
      # empirical MTBF data for commercial electric deck oven elements; label: inferred.]
    - item: "Proofing cabinet heating element or thermostat"
      estimated_hours_to_failure: 3000
      replacement_cost: 200
      replacement_lead_time_days: 5
      serviceable_by: journeyman
      # Proofer elements fail similarly to oven elements but with shorter
      # thermal cycling amplitude (proofing temperatures 24-32°C vs. oven 230-260°C).
      # Per baking SCHEMA.md §5: proofer elements 1,000-2,500 hr typical; 3,000 hr
      # is within range for a dedicated proofing cabinet (lower duty cycle than oven).
      # Journeyman-level replacement (simple element or thermostat swap on most
      # commercial proofing cabinet models); 5-day regional supply lead time.
      # [Baking SCHEMA.md §5 reference; CITATION-NEEDED: proofing cabinet element
      # MTBF data; label: inferred.]
    - item: "Mixer bowl and dough hook (wear replacement)"
      estimated_hours_to_failure: 2500
      replacement_cost: 150
      replacement_lead_time_days: 3
      serviceable_by: operator
      # Mixer bowl and dough hook are wear items subject to fatigue and surface
      # degradation from repeated contact with high-hydration dough and cleaning
      # chemicals. Operator-serviceable (no technical skill required beyond
      # removing and reinstalling the bowl and hook); parts available from
      # regional restaurant-equipment supply within 3 days.
      # [CITATION-NEEDED: commercial spiral mixer bowl and hook wear replacement
      # cycle data; illustrative from baking SCHEMA.md §5 reference list
      # general wear-item guidance; label: inferred.]

  maintenance_schedule:
    daily:
      task: "Feed sourdough starter(s); clean mixer bowl, hook, and bench surfaces; wipe deck oven interior and door seals; empty water tray from proofer; log dough yields and fermentation timing"
      performed_by: operator
    weekly:
      task: "Deep-clean deck oven (remove loose debris from deck, clean door and gasket seals); calibrate proofing cabinet temperature and humidity; inspect mixer motor base for vibration; clean exhaust hood filter"
      performed_by: operator
    quarterly:
      task: "Professional exhaust hood cleaning and grease trap service (health code requirement); deck oven element and thermostat inspection; proofing cabinet full calibration; mixer motor inspection and lubrication"
      performed_by: journeyman
    annual:
      task: "Full deck oven professional service (element test, seal replacement, thermostat calibration, structural inspection); health department kitchen inspection; proofing cabinet professional service; mixer motor overhaul or replacement assessment"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 60
  # Sourdough production carries inherent overhead not present in yeasted-bread
  # or non-fermentation bakery contexts: (1) morning starter check and feeding
  # (~10 min); (2) oven preheat from cold to operating temperature — electric
  # deck ovens require 30-45 min preheat (longer than convection ovens due to
  # thermal mass of deck stones); (3) end-of-day cleanup, sourdough maintenance,
  # and production logging (~15 min). Total: ~55-65 min/day; 60 min used.
  # This overhead is consistent with entry parameters and is subtracted from
  # max_active_hours_per_week when calculating net production hours.
  # [Structural inference from sourdough production scheduling; CITATION-NEEDED:
  # empirical startup/shutdown overhead data for commercial sourdough bakery
  # operations; label: inferred.]

  max_active_hours_realism_note: >
    35 hr/wk is the gross ceiling including startup, shutdown, and sourdough
    maintenance overhead. Derating applied: 60 min/day overhead × 5.5 operating
    days/wk (typical farmers-market schedule includes Saturday) = 5.5 hr/wk
    non-productive overhead, leaving approximately 29.5 hr/wk net active
    production time (mixing, shaping, loading, unloading, packaging, market
    setup). sim_params.throughput_units_equiv_per_year uses a loaves-per-day
    figure (115 loaves/day) that is derived from the full operating-day output
    including both batches; this figure is consistent with the net 29.5 hr/wk
    active window. The gross 35 hr/wk figure is used in E-3 cross-checks as
    stated in the sim_params derivation notes.

  interruption_notes: >
    Farmers-market operations introduce intraday interruptions not present in
    wholesale or subscription-only models: customer interaction at market stall
    (~2-4 hr on market day for a village or town scale market), setup and
    breakdown (~1 hr/market day). These are partially captured in the 35 hr/wk
    ceiling (which includes market overhead) and are folded into
    throughput_units_equiv_per_year via the loaves-per-day estimation rather
    than modeled as a separate downtime fraction. A DTC-only (no farmers market)
    variant would reduce weekly overhead by ~3 hr and could increase net baking
    time proportionally, but the farmers-market model is the base configuration.

  consumables_lead_time_days: { typical: 3, worst: 21 }
  # Typical: commodity bread flour and packaging available from regional
  # food-service distributor (US Foodservice, Sysco, regional co-op) within
  # 3 days in town or village markets with adequate distributor coverage
  # per SCALES.md §6. Worst: specialty flour (heritage wheat, rye, spelt)
  # from smaller regional mills may require 14-21 days in supply-chain
  # stress or mill-production scheduling gaps.
  # [SCALES.md §6 infrastructure baseline; CITATION-NEEDED: empirical
  # consumable lead-time data for artisan bakery flour supply; label: inferred.]

  throughput_variance:
    seasonal: "Summer trough (July-August) from reduced farmers-market attendance; pre-holiday uptick (November-December) for bread-gift and holiday-table demand; January post-holiday slowdown"
    worst_month_fraction_of_average: 0.65
    best_month_fraction_of_average: 1.30

  operator_impact:
    noise_db: 60
    # Electric deck oven and proofing cabinet produce low ambient sound (~40-50
    # dB). Spiral mixer during dough mixing (~65-70 dB during mixing cycle;
    # intermittent). Ambient bakery environment estimated at 55-65 dB(A) during
    # normal production; 60 dB(A) average. Well below OSHA 90 dB(A) PEL.
    # [CITATION-NEEDED: sound level measurement at operator position in
    # commercial bakery with electric deck oven; illustrative estimate;
    # label: inferred. OSHA 29 CFR 1910.95 PEL: 90 dB(A) for 8-hr shift.]
    heat_exposure: "Elevated ambient temperature near deck oven during baking cycles (oven surface 230-260°C; ambient near oven 28-35°C); adequate with kitchen exhaust hood at required 2.5 m ceiling; operator rotation to cool mixing and shaping areas during bake windows reduces sustained heat exposure"
    emissions: "Near-zero combustion emissions from electric deck; steam and flour dust are the primary occupational exposure concerns; kitchen exhaust hood manages steam; flour dust requires PPE (dust mask) during extended mixing operations per OSHA flour-dust guidelines"
    physical_demand: "Moderate; sustained standing; repetitive dough-shaping tasks (approximately 200-400 shaping motions per production day at 115 loaves); 10-15 kg dough-batch lifting; bent-posture work during oven loading/unloading — ergonomic anti-fatigue mats and oven tools (peel, loader) recommended"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Commercial kitchen or light-commercial zoning required; cottage-food laws vary substantially by US state and may permit home-kitchen sales below stated revenue thresholds but do NOT cover deck-oven commercial production — this entry requires a licensed commercial kitchen"
  emissions: "No combustion emissions permit required for electric deck; kitchen exhaust hood may require local building permit and inspection; flour-dust occupational exposure governed by OSHA 29 CFR 1910.1000 Table Z-1"
  other: "Commercial food handler certification required for operator; health department commercial kitchen inspection and licensing required for sales beyond home-kitchen cottage-food exemption; HACCP plan required for wholesale accounts; farmers-market vendor permit required per local market authority"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: good
  cooperative: marginal
  civic: poor

scale_fit:
  village: good
  town: good
  small_city: marginal

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:
  cooperative:
    membership_boundary: >
      Baker members or customers of a shared-kitchen cooperative within the
      village or town; the cooperative form applies primarily to shared-kitchen
      cost-reduction arrangements (shared deck oven and proofing cabinet
      across 2-4 micro-bakery members operating on staggered schedules),
      not to a production cooperative where members pool output. Village or
      town residents with established baking practice may join; membership
      scoped to geographic proximity necessary to sustain shared-kitchen
      scheduling (15-mile radius maximum).
    rules_source: >
      Operating agreement or LLC operating agreement adopted at founding;
      member vote required to amend any scheduling, dues, or access provision;
      annual meeting reviews equipment-use allocation and dues schedule.
      Rules specify: time-block booking protocol for shared oven access,
      cleaning and maintenance responsibility per session, equipment damage
      liability, starter-storage rights (sourdough starters require dedicated
      refrigerator space), and dues schedule.
    monitoring: >
      Equipment usage logged per session via booking ledger; monthly usage
      report to elected member-manager; health-department inspection compliance
      log maintained and available to all members; equipment temperature logs
      reviewed weekly for calibration drift; financial report to membership
      quarterly. Damage or contamination incidents reported to member-manager
      within 24 hours.
    graduated_sanctions: >
      First incident (cleaning failure, booking overage, equipment misuse):
      written warning and mandatory re-orientation on kitchen protocols.
      Second incident within 12 months: $50 fine and 30-day booking suspension.
      Third incident within 24 months: membership review by member-manager
      and member committee; possible termination with dues refund pro-rated.
      Equipment damage: cost-recovery invoice plus warning; willful damage
      triggers immediate membership review. Per Ostrom Principle 5.
      [Ostrom 1990, Governing the Commons]
    conflict_resolution: >
      Member-elected manager handles first-level disputes (scheduling conflicts,
      cleaning disputes, equipment damage attribution); appeal to full membership
      vote at next scheduled meeting; unresolved disputes referred to the LLC
      operating agreement's dispute-resolution provisions. Per Ostrom Principle 6.
      [Ostrom 1990]
    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6]
    # Principle 1 (defined boundaries): membership_boundary above.
    # Principle 2 (rules fit local conditions): shared-kitchen scheduling rules
    # calibrated to 2-4 member micro-bakery scale.
    # Principle 3 (collective choice): member vote to amend operating agreement.
    # Principle 4 (monitoring): booking ledger, temperature logs, usage reports.
    # Principle 5 (graduated sanctions): above.
    # Principle 6 (conflict resolution): above.
    # Principle 7 (external recognition): addressed via legal_form below.
    # Principle 8 (nested governance): not applicable at single-cooperative scale.
    member_amendment_process: >
      2/3 vote of all members at scheduled annual meeting; 30-day notice
      to all members required before any operating-agreement amendment vote;
      emergency amendment (3/4 vote) permissible with 7-day notice for
      health-code compliance or safety-related changes only.
    legal_form: >
      Multi-member LLC (most common structure for shared commercial kitchen
      cooperatives in US jurisdictions); alternatively, state-registered
      unincorporated cooperative association where available. LLC structure
      provides member liability protection and external recognition
      (Ostrom Principle 7 analog) without the overhead of full cooperative
      incorporation. Specific jurisdiction filing required before launch.
    scale_fit_note: >
      Cooperative form is marginal for this entry: the primary cooperative
      value is shared equipment cost reduction (splitting $32,000 capital
      across 2-4 members reduces individual capital burden to $8,000-$16,000),
      not a full shared-production or shared-marketing cooperative. Scheduling
      complexity with 3+ members sharing a single deck oven in a 20-25 m²
      kitchen approaches the practical coordination ceiling; 4 members maximum
      is feasible, 5+ requires a larger footprint (variant entry needed).
      Village scale (500-2,000 residents) may not have sufficient demand to
      support 2-4 independent micro-bakery members; town scale (2,000-15,000)
      is more viable for this cooperative structure.

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 32000
  # Equals economics.capital_cost.mid per E3-R1. [Derived from economics block above]

  cost_sd: 9250
  # Derived: (capital_cost.high - capital_cost.low) / 4 = (55,000 - 18,000) / 4
  # = $9,250. Within E3-R5 plausible range: cost_sd/cost_mean = 9,250/32,000
  # = 0.289; within 0.15-0.50 range. [Derived per catalog/SCHEMA.md §3 default]

  throughput_units_equiv_per_year: 29500
  # Derivation (stated explicitly per baking SCHEMA.md §1 E-3 cross-check):
  # Unit: 800g sourdough boule equivalent (see Key Assumptions).
  # Step 1 — annual operating days:
  #   35 hr/wk ceiling ÷ ~6.4 hr/day effective ≈ 5.5 days/wk × 52 wk = 286
  #   days/yr; use 285 days/yr (accounting for closure days and rest).
  # Step 2 — loaves per day (gross):
  #   throughput.loaves_per_day = 115 loaves/day.
  # Step 3 — apply downtime fraction:
  #   115 loaves/day × 285 days/yr × (1 - 0.10 downtime) = 115 × 285 × 0.90
  #   = 29,497 loaves/yr → rounded to 29,500.
  # E3-R2 cross-check via active-hours method:
  #   max_active_hours_per_week (35) × 52 wk × (1 - 0.10) = 1,638 hr/yr.
  #   Net productive hours (excl. 60 min/day overhead): 1,638 - (1 hr/day × 285 days)
  #   = 1,638 - 285 = 1,353 hr/yr net bake+production hours.
  #   At 115 loaves/day ÷ ~5.8 effective production hr/day ≈ 19.8 loaves/hr;
  #   1,353 hr × 19.8 loaves/hr = 26,789 — within order of magnitude of 29,500;
  #   discrepancy reflects that the loaves/day figure (115) is an oven-constrained
  #   output measure, not a linear function of active hours (the oven runs for
  #   a fixed bake time regardless of operator hours). The loaves-per-day method
  #   is the primary derivation for this entry per baking SCHEMA.md §1 guidance.
  # [Derived from throughput fields, operating-day assumption, and downtime_fraction above]

  variable_cost_per_unit: 0.33
  # Flour and packaging dominate variable costs:
  # Flour: ~0.7 kg/loaf × $0.60/kg commodity bread flour [CITATION-NEEDED]
  #   = $0.42/loaf (flour only; this is the dominant variable cost).
  # Note: annual_consumables ($8,500) covers flour + salt + packaging + starter
  # maintenance across 29,500 loaves: $8,500 ÷ 29,500 = $0.288/loaf all consumables.
  # Energy: 5.5 kWh/active hr × 1,638 hr/yr × $0.125/kWh = $1,126/yr ÷ 29,500
  #   = $0.038/loaf.
  # Total variable: $0.288 + $0.038 = $0.326 → $0.33/loaf (rounded up).
  # [Derived from annual_consumables, energy_consumption_per_active_hour,
  # EIA electricity price $0.125/kWh per SCALES.md §6 footnote; electricity
  # price: US EIA Electric Power Monthly Table 5.3, 2023-2024 blended small-
  # commercial rate $0.10-$0.15/kWh; midpoint $0.125 used]

  labor_hours_per_unit: 0.056
  # 1 hr ÷ ~17.8 loaves/hr (29,500 loaves ÷ 1,638 total active hr/yr) = 0.0555
  # → 0.056 hr/loaf.
  # E3-R3 cross-check: 29,500 × 0.056 = 1,652 hr/yr; target = 35 × 52 × 0.90
  # = 1,638 hr/yr. Discrepancy = 14 hr (0.9%); within P2 threshold.
  # [Derived from throughput_units_equiv_per_year and max_active_hours_per_week]

  downtime_fraction: 0.10
  # Deck element failure at ~2,000 hrs → 14-day lead time = 2 weeks downtime
  # in year one. Proofer element at ~3,000 hrs (may not trigger in year one,
  # but modeled as partial risk). Routine maintenance shutdowns (~1-2 weeks/yr
  # for annual service and deep-clean). Total estimated downtime: 3-5 weeks/yr
  # out of 52 = 6-10%. Using 0.10 (upper end) for conservative modeling given
  # that deck element replacement interrupts the entire production cycle.
  # Consistent with E3-R6: deck element replacement alone = 2 weeks = 3.8%
  # downtime; total with maintenance = ~10%.
  # [Derived from operations_reality.first_year_failures above]

  lifespan_years: 15
  # Commercial electric deck ovens: rated for approximately 15,000-25,000
  # operating hours; at ~5 hr/day × 285 days/yr = 1,425 hr/yr, 15,000 hr
  # service life = ~10.5 years to first major refurbishment. Full design life
  # with professional refurbishment at year 10-12 supports a 15-year total
  # lifespan before full equipment replacement. Shorter than smithing forge
  # entries (which use masonry or structural steel rated for 20-25 years)
  # because commercial electric bakery equipment has a higher electronic
  # and electromechanical component density.
  # [CITATION-NEEDED: service life data for commercial electric deck ovens;
  # illustrative estimate from general commercial kitchen equipment longevity;
  # label: inferred.]

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
  - ref: "catalog/baking/SCHEMA.md v1.0 §1: throughput block structure; loaves/day ranges; E-3 cross-check guidance; baking schema base"
  - ref: "catalog/baking/SCHEMA.md v1.0 §2: electric-deck energy consumption 3-8 kWh/batch; electric-deck temperature ceiling 230-290°C"
  - ref: "catalog/baking/SCHEMA.md v1.0 §3: journeyman-baker skill definition; sourdough cycle management capability boundary"
  - ref: "catalog/baking/SCHEMA.md v1.0 §4: flour_source_declaration required field; industrial-flour-purchased supply-chain risk"
  - ref: "catalog/baking/SCHEMA.md v1.0 §5: first_year_failures reference list; deck element 1,500-3,000 hr; proofer element 1,000-2,500 hr"
  - ref: "catalog/baking/SCHEMA.md v1.0 §6 Group A: flour_source_declaration defining falsifier; product_mix.bread dominance; throughput_variance guidance"
  - ref: "catalog/baking/DECLINE-VERDICT.md: artisan/premium bread is restorable niche; mill dependency must be declared; DECLINE-VERDICT binding guidance"
  - ref: "corpus/program/SCALES.md §6: infrastructure baseline; electricity $0.10-$0.15/kWh (US EIA Electric Power Monthly); supplier density by scale"
  - ref: "Ostrom, Elinor. 1990. Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press. (Chapters 2-3: eight design principles, graduated sanctions, minimum viable group size)"
  - ref: "US Energy Information Administration. Electric Power Monthly, Table 5.3: Average Retail Price of Electricity. Monthly release. https://www.eia.gov/electricity/monthly/ (small-commercial blended rate 2023-2024: $0.10-$0.15/kWh; midpoint $0.125 used)"
  - ref: "OSHA 29 CFR 1910.1000 Table Z-1. Air Contaminants. (Flour dust permissible exposure limit; applicable to commercial baking operations)"
  - ref: "OSHA 29 CFR 1910.95. Occupational noise exposure. (90 dB(A) PEL for 8-hour shift; bakery ambient noise well below this threshold)"
  - ref: "[CITATION-NEEDED: capital cost data for commercial electric deck ovens 8-15 kW range, 2024-2026; vendor catalog data from Bongard, Sveba-Dahlen, Mono Equipment, or equivalent commercial bakery equipment suppliers]"
  - ref: "[CITATION-NEEDED: capital cost data for commercial proofing cabinets and spiral mixers, 2024-2026; Hobart, Globe, Doyon, or equivalent vendor pricing]"
  - ref: "[CITATION-NEEDED: installation cost data for commercial bakery kitchen fitout including electrical service, exhaust hood, and health inspection; general commercial kitchen contractor data, 2024]"
  - ref: "[CITATION-NEEDED: annual maintenance cost data for commercial electric deck bakery operations; trade or operator survey, 2024]"
  - ref: "[CITATION-NEEDED: commodity bread flour pricing per kg at US wholesale distributor level (US Foodservice, Sysco, regional food co-op), 2024; USDA ERS wheat and flour price series would be appropriate verification]"
  - ref: "[CITATION-NEEDED: packaging material costs (paper bags, labels) for small-batch artisan bakery at 100-150 loaves/day volume; trade supplier catalog data, 2024]"
  - ref: "[CITATION-NEEDED: artisan sourdough retail pricing survey at US farmers markets and DTC bakery channels, 2024-2026; USDA AMS farmers-market pricing survey or Specialty Food Association market report]"
  - ref: "[CITATION-NEEDED: US supermarket sourdough bread shelf pricing survey, 2024; IRI or Nielsen retail-scanner data for sourdough bread category]"
  - ref: "[CITATION-NEEDED: commercial electric deck oven element MTBF data; manufacturer service documentation or appliance reliability survey]"
  - ref: "[CITATION-NEEDED: empirical throughput measurement for single-operator sourdough micro-bakery with electric deck oven; operator financial data or academic baking-industry study]"
  - ref: "[CITATION-NEEDED: service life data for commercial electric deck ovens; manufacturer specification or commercial kitchen equipment longevity survey]"
  - ref: "[CITATION-NEEDED: commercial kitchen or light-commercial rental rate per m² in US village and town markets; CoStar, LoopNet, or shared-kitchen aggregator (The Food Corridor, Kitchen United) data, 2024]"
---

## Summary

Bake-001 is a single-operator, naturally-leavened artisan micro-bakery producing sourdough bread for direct-to-consumer and farmers-market sale at village and town scale. Its distinguishing characteristics are: (1) electric deck oven as primary heat source — eliminating combustion permits while delivering the thermal mass and deck-bake crust quality required for premium sourdough; (2) a market-primary revenue model priced at $5-$12/loaf against an industrial baseline of $3; (3) explicit declaration of industrial-flour dependency (no mill ownership) consistent with the DECLINE-VERDICT mill-dependency falsifier; and (4) a journeyman-baker skill floor matching the fermentation-judgment requirement for sourdough management. This entry targets the operator who wants to run a full-time artisan bakery at village or town scale and asks whether that operator can clear $48,000/year in net operator income — the answer at mid-case pricing ($8/loaf, 115 loaves/day) is affirmatively yes, with gross revenue of approximately $236,000 against operating costs of approximately $12,700/year in cash outlays, leaving substantial room for operator wages before capital recovery. The binding constraints are regulatory (commercial kitchen licensing), skill (fermentation judgment takes 3+ years to form), and market relationship (the premium segment is real but bounded).

## Design rationale

This entry addresses a specific and well-defined niche: the solo artisan baker who uses natural leavening, a deck oven, and a direct-market relationship to extract premium pricing from a consumer segment that has demonstrated willingness to pay 2-4× the supermarket baseline for genuine artisan bread. No other entry in the baking catalog covers this combination. The electric deck specification distinguishes bake-001 from wood-fired variants (bake-015 and potentially others) by minimizing regulatory friction for urban-adjacent and town-center operation: an electric deck oven can be placed in any commercially-licensed kitchen space without combustion permits, fuel storage, or air-quality review. The market-primary lens fit distinguishes it from cooperative or civic forms (bake-010 through bake-013), which address different access and ownership structures. The industrial-flour-purchased declaration distinguishes it from entries that claim grain-sourcing differentiation as the basis of premium pricing (a variant for which a separate bake-002 or bake-003 entry with local-mill-partnership would be appropriate). The specific problem this entry solves is: can an artisan baker with journeyman skill, $32,000 in capital, and a farmers-market or DTC channel generate a living wage at village or town scale? The short answer is yes with significant caveats — the market premium is real and the cost structure is favorable, but the regulatory environment and skill formation timeline are genuine barriers to entry.

## Historical lineage

Two functional precedents inform this design — and both require anti-romantic treatment.

**American frontier home-baking tradition** (functional inheritance only): The frontier baking tradition — primarily household bread production for family consumption, with occasional commercial sale — established the operational pattern of a single skilled operator managing fermentation, baking, and direct distribution without intermediaries. The functional inheritance to this entry is the direct-to-consumer relationship and the absence of a distributor or retail markup chain. What the frontier model does *not* provide is economic instruction: frontier baking was household subsistence production (not market-primary revenue), operated on unpaid family labor (not modern market wages), and used sourdough starters because commercial yeast was unavailable (not because of consumer preference). The modern micro-bakery does not inherit the frontier's labor economics or market structure; it inherits only the operator-direct-to-consumer relationship form.

**Modern sourdough revival (DTC and premium-market phenomenon)**: The contemporary artisan sourdough movement — accelerated by social media, DTC logistics platforms, and the COVID-19 home-baking surge of 2020-2021 — created the premium consumer segment this entry targets. This is emphatically *not* a historical revival of household subsistence baking. It is a premium-market phenomenon enabled by: (1) social media as a discovery and trust channel for small producers; (2) DTC fulfillment logistics enabling direct-to-door bread subscription; (3) an affluent consumer segment willing to pay $8-$12/loaf as a quality-lifestyle purchase. The DECLINE-VERDICT baking guidance explicitly identifies this as the restorable artisan/premium niche — restorable because the consumer demand is present and documented, not because it represents a return to historical household practice. Authors of future entries who frame the sourdough revival as historical continuity are making a romantic error; it is a new market phenomenon built on different economics, different distribution infrastructure, and different consumer motivations than any historical precedent.

## Key assumptions

**Mill dependency (prominent per entry parameters):** This entry purchases flour from an industrial distributor. The premium market positioning does NOT require grain-sourcing differentiation: the artisan premium is derived from process (natural leavening, deck baking, skilled fermentation management) and direct relationship, not from ingredient provenance. However, this creates a supply-chain dependency on commodity flour pricing. Wheat price volatility (driven by global markets, weather, and trade policy) is the primary input cost risk. At $0.60/kg commodity bread flour [CITATION-NEEDED], flour accounts for approximately $5,700/yr of the $8,500 annual consumables figure — 67% of consumables and the single largest variable cost driver. A 30% flour price increase would add approximately $1,700/yr to operating costs, reducing operator take-home by that amount but not threatening viability at mid-case revenue.

**Throughput (115 loaves/day):** This is at the high end of the village-artisan range and the low end of the town-artisan range per baking SCHEMA.md §1. It requires consistent execution of two batches per day across a 5.5-day operating week. The figure is labeled inferred and requires verification from empirical micro-bakery operator data [CITATION-NEEDED]. At 80 loaves/day (low-case), annual throughput drops to ~20,500 loaves and revenue at mid pricing ($8) drops to $164,000 — still well above the $48,000 operator income threshold after costs.

**Market pricing ($5-$12/loaf):** Labeled `pricing_validation: inferred`. No formal industry pricing survey underlies these figures. The industrial baseline ($3) is estimated from US supermarket sourdough shelf pricing [CITATION-NEEDED]. Both figures require verification against empirical retail data before promotion to `reviewed` status.

**Capital costs ($18,000-$55,000):** Labeled inferred from market observation of commercial bakery equipment vendors. The mid-point ($32,000) is weighted toward a capable full commercial setup including a proper deck oven, proofing cabinet, and spiral mixer. A minimally-viable setup (secondhand deck oven, basic proofing, entry-level mixer) could operate below $20,000. [CITATION-NEEDED for all equipment cost figures.]

**sim_params derivation:** throughput_units_equiv_per_year (29,500) derived from loaves/day × operating days × (1 - downtime); the unit is the 800g sourdough boule equivalent. All monetary values in USD. Electricity price $0.125/kWh from US EIA Electric Power Monthly blended small-commercial rate 2023-2024.

## Known risks / failure modes

**Regulatory (primary risk):** Cottage-food laws vary dramatically by US state: some states permit home-kitchen commercial baking with annual revenue caps ($5,000-$75,000 depending on jurisdiction); others require full commercial kitchen licensing regardless of scale. An operator who begins selling at farmers markets under cottage-food exemption and grows beyond the threshold faces a regulatory cliff — either obtaining commercial kitchen licensing (costly) or capping revenue growth. For this entry's design (electric deck oven, commercial output volumes), commercial kitchen licensing is assumed to be required; the cottage-food path is noted as a startup option only. HACCP plan requirements for wholesale accounts add documentation overhead that is feasible but requires operator attention. Farmers-market vendor permits are straightforward but jurisdiction-specific.

**Labour pipeline:** Journeyman-baker skill is the entry barrier and the operating constraint. Sourdough fermentation judgment — the ability to read bulk fermentation stage, adjust proofing schedule for ambient temperature, and troubleshoot a sluggish starter — requires 12-24 months of lived practice through seasonal variation cycles. It cannot be acquired from videos or manuals alone. An operator who opens this bakery without prior sourdough production experience will produce inconsistent product for 12-18 months while developing fermentation judgment, during which customer trust and repeat purchase rate will be limited. Succession risk is mitigated by the apprentice path (36-42 months to journeyman standard) but is a real planning constraint: a bakery that loses its sole journeyman baker without an apprentice in Stage 3 or 4 faces a 2+ year gap before a replacement can achieve independent operation.

**Supply chain (flour price volatility):** Commodity wheat prices are volatile; the 2022 price spike (driven by the Russia-Ukraine conflict) pushed US commodity bread flour prices up 30-50% within 12 months. An operator on industrial-flour-purchased with no supply contract and no grain inventory buffer absorbs this volatility directly in consumables costs. Flour accounts for ~67% of annual consumables; a sustained 30% price increase reduces annual operator take-home by ~$1,700 at mid-case throughput. This is material but not existential at mid-case revenue. The risk of a local distributor supply disruption (e.g., distributor warehouse fire, regional logistics failure) is a worst-case 21-day lead time [consumables_lead_time_days.worst]; a 21-day flour inventory buffer ($150-$200 working capital) mitigates this risk.

**Sourdough starter maintenance overhead:** A healthy sourdough starter requires daily feeding, temperature management, and observation. A starter that becomes contaminated, over-acidified, or otherwise compromised can require 7-14 days to restore and represents a production stoppage risk. This overhead is captured in the 60 min/day startup-shutdown figure but is qualitatively distinct from equipment failure: it is an ongoing biological management task that cannot be delegated without skill transfer, and it cannot be skipped over a weekend without consequence. Operators planning regular days off must establish a starter maintenance protocol (refrigerator storage between feedings for 2-3 day gaps; established backup starter culture).

## Target niche

This entry targets the operator who wants to run a full-time premium artisan bakery with direct-to-consumer revenue — either at a farmers market, via a subscription service, or through a small retail window — at village or town scale. The critical economic question per entry parameters is: *can this operator clear $48,000/year in net operator income at village scale?*

At mid-case pricing ($8/loaf × 29,500 loaves/yr = $236,000 gross revenue) and mid-case operating costs ($8,500 consumables + $1,200 maintenance + $3,000 rent + $1,126 energy ≈ $13,826/yr cash costs, not counting capital recovery), the pre-capital, pre-tax operator income is approximately $222,000 — well above the $48,000 threshold. The more realistic question is payback period on capital: $36,000 total investment (capital + installation) recovered at $222,000 gross margin implies theoretical payback in under 0.2 years — but this ignores operator wages. If the operator pays themselves $48,000/year, the remaining $174,000 more than covers capital recovery, further maintenance reserves, and business taxes.

At low-case pricing ($5/loaf × 80 loaves/day × 285 days × 0.90 = $102,600 gross) and full costs, the picture is tighter but still workable: gross - costs ≈ $102,600 - $13,826 = $88,774 before operator pay and capital recovery. Still above $48,000.

The binding constraints are not economic at reasonable pricing and throughput levels. They are: (1) regulatory — commercial kitchen licensing must be cleared before reaching mid-case throughput; (2) skill — 3 years of fermentation experience required before operating at journeyman quality and consistency; (3) market relationship — the premium segment is real and documented by the modern sourdough revival, but it is bounded in village-scale markets (500-2,000 residents), where the addressable customer base for a $8/loaf product may be limited to 50-200 households. At village scale, 80-100 loaves/day sold locally is achievable; 115 loaves/day may require a DTC or CSA delivery component to reach customers beyond the immediate village.

The small_city scale is marginal: a larger market increases the addressable premium customer base, but the operator faces competition from established artisan bakeries with lower unit costs from greater throughput volume, and the direct-market relationship advantage erodes with scale. Town scale is the sweet spot: 2,000-15,000 residents provide an adequate premium customer base for 100-130 loaves/day without the competitive density of a small city.

## Iteration log

- 2026-04-18: v0.1 — initial authoring per Plan G Task 3. All schema fields populated
  including trade_specific.flour_source_declaration per DECLINE-VERDICT mill-dependency
  falsifier; cooperative (marginal) lens_context fully populated per E2-R5;
  civic lens omitted (lens_fit.civic: poor); market pricing labeled pricing_validation:
  inferred per citation policy; 14 CITATION-NEEDED placeholders carried forward for
  post-authoring verification; sim_params derivation stated explicitly in field comments;
  anti-romantic historical lineage section explicitly disclaims modern sourdough revival
  as historical continuity per entry parameter guidance.
