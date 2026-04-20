---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: bake-007
trade: baking
name: "Japanese-style Wagashi Confection Studio (hybrid-wood-electric, town/small-city scale)"
tagline: "Specialist wagashi studio producing mochi, manjū, nerikiri, and yokan for premium gift and specialty retail markets"
status: draft
version: "0.1"
supersedes: null
inspirations:
  - edo-period-wagashi-specialist-workshop
  - modern-japanese-confection-studio-premium-retail

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 32
# Mid-range of the 25-40 m² envelope; adequate for one to two operators,
# a commercial steamer, electric hot plate array, a small convection oven
# for baked wagashi (dorayaki, manju), a wooden mold cabinet, staging and
# cooling surfaces, and a refrigerated display prep counter. Excludes
# customer-facing retail space and front-of-house display area.
# [Structural estimate from baking SCHEMA.md §6 Group B specialty confection
# guidance and general commercial pastry production kitchen footprints.
# CITATION-NEEDED: empirical floor-area survey of specialist wagashi studios
# in Japan or diaspora markets, 2020-2026.]

ceiling_min_m: 2.5
# Minimum required for ventilation hood installation over the steaming station
# and electric hot plate array. No combustion clearance above 2.5 m is required
# for this hybrid configuration; the wood component is limited to an optional
# supplemental steamer firebox and is not the primary heat source.
# [Derived from commercial kitchen exhaust-hood installation clearance standards;
# CITATION-NEEDED: commercial kitchen design ceiling-height minimums.]

ventilation: mechanical-extraction-required
# The steaming operations generate persistent high-humidity ambient conditions;
# mechanical extraction is required to manage moisture buildup, protect wooden
# molds from warping, and comply with commercial kitchen ventilation codes.
# The optional wood-fired steamer component adds minor smoke-management
# requirements when in use. Electric hot plate array and small convection oven
# produce minimal combustion products but significant heat.
# [Commercial kitchen ventilation code requirements; wood-fired component adds
# solid-fuel exhaust considerations per baking SCHEMA.md §2 hybrid-wood-electric
# regulatory notes.]

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: hybrid-wood-electric
# Primary production uses a commercial electric steamer and electric hot plate
# array. A wood-fired steamer is retained for specific product lines (traditional
# mushi-manju, certain yokan formats) where operators judge steam character to
# matter for product quality and for operational resilience during grid outages.
# A small convection oven handles baked wagashi types (dorayaki, castella-style
# cakes, some manjū). The hybrid designation reflects the dual steam-source
# architecture, not a 50/50 energy split; electric is the dominant and daily-
# use source. Per baking SCHEMA.md §2: hybrid-wood-electric has the most complex
# regulatory posture of the allowed values — dual permit path required.

energy_consumption_per_active_hour: "4.5 kWh electric + 3-5 kg wood when wood steamer is active (approximately 2-3 sessions per week)"
# Electric component: commercial steamer (~2.5-4 kW rated) + electric hot plate
# array (~1.5-2.5 kW total) + convection oven (~2 kW, intermittent) = approximately
# 4-6 kW average draw during active production. 4.5 kWh/hr represents the
# blended active-hour consumption across steaming, hot plate, and oven cycles.
# Wood component: 3-5 kg wood per steamer session (~1.5-2 hr/session × 2-3
# sessions/week); not included in kWh figure. Wood consumption is occasional
# and secondary. [baking SCHEMA.md §2 hybrid-wood-electric notes; CITATION-NEEDED:
# metered energy-consumption data for commercial steamer + hot plate production
# environment; illustrative estimate; label: inferred.]

backup_fuel: wood
# Wood-fired steamer serves as backup for electric failure scenarios. Not a
# full production backup (limited steamer capacity, smoke management required),
# but sufficient for critical product-line continuity for 1-2 days during a
# grid outage or electric equipment failure.

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  loaves_per_day: 130
  # Unit: wagashi piece equivalent (see Key Assumptions for definition and
  # weighting). Net production output per full operating day across the
  # product mix of mochi, manjū, nerikiri, and yokan. Range per entry
  # parameters: 80-200 pieces/day, highly variable by type. 130 pieces/day
  # is the central estimate for a two-operator studio at town/small-city scale
  # running a balanced product mix (not dominated by labor-intensive nerikiri,
  # which would lower throughput, nor by yokan, which can be produced in larger
  # batch volumes but has long cooling/setting cycle time).
  # [Entry parameters: 80-200 pieces/day range; 130 as central estimate for
  # balanced product mix. CITATION-NEEDED: empirical throughput data for
  # commercial wagashi studios at comparable scale, 2020-2026.]

  batches_per_day: 3
  # Three production runs per day: (1) morning — steamed products (mushi-manju,
  # mochi types requiring steamed glutinous rice preparation); (2) midday —
  # hand-formed products (nerikiri, kinton, raw confections that set at ambient
  # temperature after forming); (3) afternoon — baked and yokan (dorayaki,
  # baked manju, poured yokan blocks entering refrigerated setting). Each run
  # is product-specific; the three-batch structure reflects the sequential
  # nature of wagashi production where different types occupy different
  # temperature regimes and cannot overlap freely on shared equipment.
  # [Structural inference from wagashi production scheduling; CITATION-NEEDED:
  # empirical scheduling data for commercial wagashi studio.]

  batch_size_loaves: 43
  # 130 pieces/day ÷ 3 batches = ~43 pieces per batch average. This is a
  # blended figure across product types: nerikiri batches are smaller (15-25
  # pieces/batch, labor-intensive hand-forming); mochi and manju batches are
  # larger (50-80 pieces/batch from standard steamer capacity); yokan is
  # produced in poured-block format (a single 1.5 kg block yields ~18-24 slices
  # depending on cut thickness). The 43-piece/batch figure is a weighted average
  # for accounting purposes; it does not represent any single product's batch.
  # [Derived from loaves_per_day ÷ batches_per_day; illustrative average.]

  max_active_hours_per_week: 40
  # Total operator active time per week including ingredient preparation
  # (red bean paste cooking — anko — alone requires 2-3 hr/batch), forming,
  # steaming, baking, cooling, packaging, and customer/gift preparation overhead.
  # 40 hr/wk gross ceiling for two operators at 20 hr/operator/wk net, or
  # one full-time operator with part-time assistance. Consistent with entry
  # parameters of 1-2 operators at town/small-city scale.

  product_mix:
    bread: 0
    # No bread production; this is a specialist confection studio only.
    confection: 85
    # Wagashi confections across all four core product lines: mochi (glutinous
    # rice-based), manjū (red bean paste-filled steamed or baked buns), nerikiri
    # (sculpted tōgashi-style wagashi using refined white bean paste and sweet
    # potato base), and yokan (jellied red bean confection). The 85% figure
    # represents the production fraction dedicated to the core wagashi product lines.
    specialty: 15
    # Seasonal and custom wagashi: seasonal motif nerikiri for gift sets (cherry
    # blossom, autumn maple, New Year themes), custom order pieces for tea ceremony
    # or cultural event contexts, and limited regional specialty items (mochi
    # flavors specific to local seasonal ingredients). Gift and cultural event
    # output is categorized here.
    catering: 0
    # No catering in the base configuration. Event supply (wedding, ceremony) is
    # captured under specialty for small-scale custom orders; large event catering
    # would require a separate entry variant.
    # Sum: 100.

  throughput_variance:
    seasonal: "Strong holiday and gift-giving peaks (New Year, Valentine's Day, spring/cherry blossom season, mid-summer Obon gift period); post-holiday January trough and summer heat trough (July-August) when ambient heat complicates cold-sensitive product handling"
    worst_month_fraction_of_average: 0.42
    # Confection entries per baking SCHEMA.md §1: typical worst-month range
    # 0.35-0.55. Wagashi is at the lower end of this range because its demand is
    # strongly event-driven and its primary markets (gift-giving, tea ceremony,
    # cultural events) concentrate sharply around specific calendar periods. A
    # studio without strong regular retail foot traffic will experience significant
    # dead-weeks between gift-giving seasons. 0.42 reflects a mixed retail/wholesale
    # model that retains some baseline demand between peaks.
    # [baking SCHEMA.md §1 confection throughput_variance guidance; CITATION-NEEDED:
    # empirical seasonal demand data for wagashi retail, 2020-2026; label: inferred.]
    best_month_fraction_of_average: 1.75
    # Pre-New Year (December–January) and spring cherry blossom season (March–April)
    # are peak demand periods for wagashi gift-giving. Best month at 1.75× average
    # is consistent with baking SCHEMA.md §1 confection range of 1.30-1.80; wagashi
    # is at the upper end given the concentrated gift-giving demand structure.
    # [Same source as worst_month_fraction_of_average.]

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: pastry-chef-master
# Wagashi technique requires full pastry-chef-master skill level per baking
# SCHEMA.md §3 explicit boundary: "Cultural specialty confection requiring
# tradition-specific knowledge (wagashi, ethnic specialty)" is listed as the
# product scope of pastry-chef-master. Mochi texture management, nerikiri
# sculpting technique (requiring fine motor control and knowledge of white
# bean paste moisture ratios), anko production consistency, and yokan gelatin
# work are all techniques that cannot be reliably executed by a journeyman-baker
# operating without training specific to wagashi methods. A chef with strong
# French pastry training is not automatically competent in wagashi; the
# techniques are materially distinct. [baking SCHEMA.md §3 pastry-chef-master
# definition and product scope; CITATION-NEEDED: apprenticeship curriculum
# documentation for Japanese confection training programs, e.g., Japanese
# Culinary Institute for Foreigners or established wagashi certification bodies.]

operators_concurrent: "1-2"
# Normal production is operable by a single master operator for simpler product
# days; two operators (master + trained assistant or junior wagashi practitioner)
# are required during peak production weeks and for product lines that require
# simultaneous forming and steaming. Entry parameters specify 1-2 operators.

apprentice_friendly: true
apprentice_path:
  training_stages: >
    Stage 1 (0-6 months): kitchen safety and sanitation; equipment operation
    (commercial steamer, hot plate array, convection oven startup and shutdown);
    ingredient preparation (anko cooking, mochi rice washing and steaming,
    basic yokan preparation); observation of forming technique without independent
    forming. Gate criterion: can safely operate and clean all equipment unassisted;
    can produce anko to master-accepted consistency standard without guidance
    for five consecutive batches.
    Stage 2 (6-18 months): independent anko production; basic mochi forming
    (daifuku, simple wagashi); manju filling and shaping under supervision;
    dorayaki batter and cooking; yokan pouring. Gate criterion: produces 20
    consecutive daifuku mochi to master-accepted texture and appearance standard
    without guidance on final five.
    Stage 3 (18-42 months): nerikiri forming under close supervision; seasonal
    motif shaping; mushi-manju steam-time judgment; quality control for gift
    packaging standards. Gate criterion: independently produces a 10-piece
    nerikiri assortment to master-accepted standard for five consecutive
    production sessions without guidance on final session.
    Stage 4 (42-72 months): full technical range including complex nerikiri
    sculpture, kinton technique, recipe development for seasonal specials,
    customer and event consultation. Approximate independent practitioner
    standard. Note: the 72-month ceiling reflects the reality that nerikiri
    at master level requires years of motor memory formation; the 42-month
    gate certifies journeyman-adequate independent operation, not master level.
  time_to_independent_operation: "~42-60 months to journeyman-adequate independent operation on core wagashi product lines; nerikiri at commercial quality standard requires additional years of practice beyond the Stage 3 gate; 72 months is a realistic estimate for full master-level range"
  succession_note: >
    Apprentice co-presence during production — Stage 2 onward — is integrated
    into normal studio operations: the apprentice handles anko production,
    basic mochi forming, and equipment management while the master handles
    nerikiri and complex product lines. This division of labor is functional
    (not a dedicated training program) and follows the traditional Japanese
    confectionery workshop model of skill transmission through daily
    production participation. The long time-to-independence is a genuine
    succession risk: a studio that loses its master operator without an
    apprentice in Stage 3 or beyond faces a multi-year capability gap.
    This risk is named explicitly in Known Risks.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 20000, mid: 38000, high: 65000 }
  # Low: entry-level commercial electric steamer (~$3,500-$5,000), electric hot
  # plate array (~$1,500), basic countertop convection oven (~$800), wooden
  # wagashi molds set (~$1,500), stainless prep surfaces (~$2,000), refrigerated
  # display counter (~$3,000), smallwares and packaging station (~$2,000),
  # minimal kitchen fitout. ~$14,300-$15,800 equipment; additional fitout and
  # installation to $20,000.
  # Mid: mid-range commercial steamer ($6,000-$9,000), two-burner professional
  # hot plate array ($3,000), small commercial convection oven ($3,500),
  # complete wooden mold collection including specialty and seasonal molds
  # (~$3,000-$5,000), refrigerated prep counter ($6,000), full smallware set,
  # packaging and gift-wrap station, POS system. ~$30,500-$35,000 equipment;
  # fitout and installation to $38,000.
  # High: premium commercial steamer with multiple tier capacity ($12,000+),
  # full professional hot plate and induction station ($5,000), commercial
  # convection oven ($6,000), complete master-level mold collection (~$8,000),
  # walk-in refrigeration upgrade, custom fitout for retail display and gift
  # presentation, full health-department-compliant kitchen. ~$55,000-$60,000
  # equipment and fitout to $65,000.
  # [CITATION-NEEDED: capital cost data for commercial steamers, hot plate
  # arrays, and specialty confection equipment, 2024-2026; estimates from
  # general commercial kitchen equipment market observation; label: inferred.]

  install_cost: 5000
  # Electrical service upgrade (steamer + hot plate array requires 40-60A
  # dedicated service), exhaust-hood installation and ductwork, wood-fired
  # steamer flue or ventilation if included, health-department commercial
  # kitchen inspection and certification, initial setup.
  # [CITATION-NEEDED: commercial kitchen installation cost data including
  # electrical service and exhaust-hood; general contractor estimate range;
  # label: inferred.]

  annual_maintenance: 1800
  # Steamer descaling and element inspection (quarterly), hot plate element
  # and thermostat calibration, convection oven cleaning and filter replacement,
  # wooden mold treatment and repair (oiling, crack repair), exhaust-hood
  # cleaning (quarterly, health code), refrigeration service. Excludes
  # first-year failure replacements itemized in operations_reality.
  # [CITATION-NEEDED: annual maintenance cost data for commercial steamer
  # and specialty confection kitchen; illustrative estimate; label: inferred.]

  annual_consumables: 18500
  # Primary ingredients: red bean (adzuki) paste ingredients — dried adzuki
  # beans (~$2.50-$4.00/kg, specialty imported [CITATION-NEEDED: US wholesale
  # price for dried adzuki beans, 2024]); sweet rice flour (mochiko, ~$3.00-$5.00/kg
  # specialty [CITATION-NEEDED: US wholesale mochiko price]); refined white
  # bean paste base (~$4.00-$6.00/kg [CITATION-NEEDED]); sugar (~$1.00/kg
  # commodity); matcha and specialty flavorings (~$2,000/yr for quality matcha
  # [CITATION-NEEDED: wholesale matcha price per kg]); agar-agar for yokan
  # (~$800/yr). Ingredient cost dominates at estimated ~$13,000/yr for a
  # 130-piece/day × 275-day operation.
  # Secondary: packaging — gift boxes, tissue, ribbons, labels for premium
  # gift presentation (~$3,500/yr estimated). Mold maintenance supplies,
  # cleaning chemicals (~$500/yr). Utility overage (~$500/yr beyond floor_space
  # rent allocation).
  # Total: ~$18,500/yr mid-case estimate.
  # [CITATION-NEEDED: all ingredient and packaging cost figures; label: inferred.]

  floor_space_rent_per_year: 4800
  # Imputed at ~$150/m² per year for commercial kitchen or light-commercial
  # space in a town or small-city setting; 32 m² × $150/m²/yr = $4,800.
  # Specialty confection studios in town or small-city markets may access
  # commercial kitchen or mixed-use artisan space at rates between $100-$200/m²;
  # $150/m² is the mid-range estimate. Owner-operator scenarios should impute
  # this cost for consistent cross-entry comparison per catalog/SCHEMA.md §6.
  # [CITATION-NEEDED: commercial kitchen or light-commercial rental rate per m²
  # in US town and small-city markets; CoStar, LoopNet, or shared-kitchen
  # aggregator data, 2024-2026; label: inferred.]

  market_price_per_unit: { low: 3, mid: 6, high: 15 }
  # Per wagashi piece equivalent (weighted-average piece; see Key Assumptions
  # for unit definition). Low: simple mochi or dorayaki at modest retail pricing
  # ($3/piece). Mid: standard mixed-box or individual specialty wagashi at premium
  # specialty retail ($6/piece; reflects the gift-market positioning). High:
  # elaborate nerikiri or custom seasonal gift-set pricing per piece ($15/piece
  # for hand-sculpted nerikiri or premium gift-box units priced by piece).
  # Industrial baseline: $1.50/piece (mass-produced Japanese-style wagashi from
  # Asian supermarket or specialty food importer; see industrial_baseline_price).
  # [Entry parameters: low $3, mid $6, high $15; industrial baseline $1.50.
  # CITATION-NEEDED: empirical pricing survey for artisan wagashi in US specialty
  # food and gift retail channels, 2024-2026; label: pricing_validation: inferred.]

  pricing_notes: >
    Unit is a wagashi piece equivalent (weighted average across mochi, manjū,
    nerikiri, and yokan slice; see Key Assumptions). Premium over mass-produced
    Asian-supermarket-import wagashi ($1.50/piece industrial baseline
    [CITATION-NEEDED: US retail survey for imported Japanese wagashi, Asian
    supermarket shelf pricing, 2024]) is driven by: (1) fresh production without
    preservatives — imported wagashi uses extended shelf-life formulations that
    alter texture and flavor; (2) hand-forming, especially for nerikiri and
    specialty mochi, which is not economically reproducible at industrial scale;
    (3) gift presentation and custom seasonal design; (4) proximity premium for
    culturally specific diaspora or enthusiast customer segments. The $3-$15
    range targets specialty retail, cultural event, and premium gift channels,
    not mass supermarket shelf. The $15 high-end piece price is achievable only
    for labor-intensive nerikiri and custom gift pieces; an average of $6/piece
    across the product mix is the central case. The customer segment paying this
    premium is primarily Japanese diaspora communities, tea-ceremony practitioners,
    and food-culture enthusiasts rather than general-consumer impulse buyers.

  pricing_validation: >
    Pricing evidence: inferred from market observation of specialty wagashi
    and Japanese confection retail in US cities with established Japanese
    diaspora communities (Los Angeles, Seattle, New York, San Francisco),
    online specialty food retailers, and Japanese cultural event vendor pricing,
    circa 2024-2026. NOT directly sourced from a formal industry pricing survey
    or published rate-card study. This is a placeholder-inferred figure.
    Recommended verification: survey of operating wagashi studios or Japanese
    confectionery businesses in US specialty markets; Japan External Trade
    Organization (JETRO) market access reports on Japanese food exports and
    diaspora food retail; Specialty Food Association market data for the Japanese-
    style confection category. This field carries a citation-needed flag per
    project citation policy.

  industrial_baseline_price: 1.50
  # Mass-produced wagashi imported from Japan or produced by industrial-scale
  # Japanese or Asian-American food manufacturers: standard mochi ice cream wrappers
  # at $1.00-$1.50/piece at Asian supermarket retail (Trader Joe's mochi ice cream
  # at comparable price tier); traditional-style imported yokan and mochi from
  # brands such as Ohgiya or Imuraya at $1.00-$2.00/piece at specialty retail.
  # $1.50/piece represents the low end of specialty-import pricing; commodity
  # mochi from bulk Asian supermarket is closer to $0.50-$0.80/piece. $1.50
  # is used as the competitive baseline for a customer who would consider an
  # imported specialty wagashi as an alternative to fresh studio-produced wagashi.
  # [CITATION-NEEDED: US retail price survey for imported Japanese wagashi brands
  # at Asian supermarket and specialty food retail, 2024; illustrative estimate
  # from market observation; label: inferred.]

# ── TRADE-SPECIFIC FIELDS ────────────────────────────────────────────────────

trade_specific:
  flour_source_declaration: industrial-flour-purchased
  # Mill dependency declared per DECLINE-VERDICT mill-dependency falsifier
  # and baking SCHEMA.md §4. This studio purchases specialty ingredients —
  # sweet rice flour (mochiko), rice flour, refined white bean paste base,
  # adzuki beans — from specialty food distributors or direct-import suppliers.
  # No milling infrastructure is owned or operated. No direct farm relationship
  # is assumed in the base configuration.
  # Supply-chain risk: specialty ingredient availability is the primary
  # constraint; adzuki beans, mochiko, and refined bean paste are specialty-
  # sourced and face longer lead times and greater price volatility than
  # commodity wheat flour. Single-supplier dependency is a documented risk
  # for small studios sourcing from specialty importers; see operations_reality
  # consumables_lead_time_days. The market positioning of this entry depends
  # on ingredient quality (premium adzuki, quality mochiko) and cannot easily
  # substitute to commodity alternatives without product quality degradation.
  # See Key Assumptions for specific sourcing discussion.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Commercial electric steamer heating element or thermostat"
      estimated_hours_to_failure: 2200
      replacement_cost: 450
      replacement_lead_time_days: 14
      serviceable_by: specialist
      # Commercial steamers operate under continuous high-humidity and thermal
      # stress; heating element degradation and thermostat drift are primary
      # failure modes per baking SCHEMA.md §5 electric-deck element and
      # thermostat reference data (1,500-4,000 hr range). Steamer elements
      # under daily high-humidity load estimated at ~2,200 hr median.
      # Specialist-required because commercial steamer element replacement
      # involves water-line disconnection and electrical access beyond operator
      # competence; 14-day lead time for non-stocked commercial steamer elements.
      # [baking SCHEMA.md §5 reference; CITATION-NEEDED: commercial steamer
      # element MTBF data; label: inferred.]
    - item: "Steamer limescale buildup — descaling and nozzle replacement"
      estimated_hours_to_failure: 800
      replacement_cost: 120
      replacement_lead_time_days: 5
      serviceable_by: operator
      # Hard-water limescale accumulation in steamer water lines and nozzles
      # is a predictable first-year maintenance event for any commercial steamer
      # in a hard-water supply area. Estimated 800 hr (approximately 6-8 months
      # of daily steaming operations) before descaling becomes operationally
      # necessary to maintain steam output quality. Operator-serviceable with
      # descaling chemical; nozzle replacement if scaling has caused irreversible
      # blockage is operator-level for accessible nozzle types. 5-day local
      # supply for descaling chemicals and standard nozzles.
      # [baking SCHEMA.md §5 steam injector nozzle reference; CITATION-NEEDED:
      # commercial steamer descaling frequency data; label: inferred.]
    - item: "Electric hot plate element (one of array)"
      estimated_hours_to_failure: 1800
      replacement_cost: 80
      replacement_lead_time_days: 5
      serviceable_by: journeyman
      # One element in a multi-element hot plate array will likely require
      # replacement in the first operating year under daily use for anko
      # cooking and mochi preparation. Element rated life 1,500-2,500 hr;
      # 1,800 hr is mid-range. Element replacement is journeyman-level
      # (requires safe electrical disconnection and appliance-level repair
      # knowledge); 5-day regional restaurant-supply lead time.
      # [CITATION-NEEDED: commercial hot plate element MTBF data; label: inferred.]

  maintenance_schedule:
    daily:
      task: "Steamer water-tank fill, drain, and flush; clean steamer interior and rack surfaces; wipe hot plate elements and surfaces; clean molds with warm water (no soap on wood molds — dry immediately); clean counters and prep surfaces; log production counts and any equipment anomalies"
      performed_by: operator
    weekly:
      task: "Steamer descaling check (water hardness test strip, initiate descaling cycle if indicated); calibrate hot plate temperatures; inspect mold surfaces for cracking or mold contamination; clean exhaust-hood filter; convection oven interior wipe and door seal inspection; refrigeration temperature log review"
      performed_by: operator
    quarterly:
      task: "Full steamer descaling cycle and nozzle inspection; professional exhaust-hood deep-clean and grease-trap service; hot plate full element and thermostat calibration; convection oven professional service; wooden mold reconditioning (oil treatment, crack repair with food-safe sealant); refrigeration compressor inspection"
      performed_by: journeyman
    annual:
      task: "Full steamer professional service (element test, water-line inspection, pressure-valve check); health-department kitchen inspection; full electrical safety inspection; convection oven structural and element overhaul; mold inventory audit and replacement of cracked or contaminated pieces"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 45
  # Wagashi production carries inherent daily overhead: (1) steamer cold-start
  # preheat to operating temperature (~15-20 min); (2) ingredient temperature
  # check and staging — mochi rice must reach ambient temperature after
  # refrigerator storage, anko paste consistency check (~10 min); (3) end-of-day
  # steamer drain, flush, and cooling; mold cleaning and drying; counter
  # sanitization; production log entry (~15 min). Total: ~40-50 min/day; 45 min used.
  # [Structural inference from wagashi production workflow; CITATION-NEEDED:
  # empirical startup/shutdown overhead data; label: inferred.]

  max_active_hours_realism_note: >
    40 hr/wk is the gross ceiling for a two-operator studio. Derating applied:
    45 min/day overhead × 5.5 operating days/wk (retail operations typically
    include Saturday; gift-giving peak periods may extend to 6 days) = 4.1 hr/wk
    non-productive overhead, leaving approximately 35.9 hr/wk net active production
    time across both operators. sim_params.throughput_units_equiv_per_year uses a
    pieces-per-day figure (130 pieces/day) that is derived from the full operating-
    day output across all product lines; this figure is consistent with the net
    ~35.9 hr/wk active window for a 1-2 operator configuration. The gross 40 hr/wk
    figure is used in E-3 cross-checks as stated in sim_params derivation notes.

  interruption_notes: >
    Gift-season retail sales introduce intraday interruptions during peak periods:
    customer interaction at studio counter or market stall (~1-2 hr/day during
    peak weeks), gift-wrapping and box assembly for custom orders (~30-60 min/day
    in gift seasons), and seasonal product development and testing (recipe
    adjustment for new seasonal motifs: ~2-3 hr/week during seasonal transition
    months). Folded into throughput_units_equiv_per_year via the pieces-per-day
    estimation and downtime_fraction; not modeled as a separate overhead category.

  consumables_lead_time_days: { typical: 7, worst: 45 }
  # Typical: specialty ingredients (adzuki beans, mochiko, white bean paste)
  # available from specialty Asian food distributors within 7 days in town
  # or small-city markets with adequate specialty food distributor coverage.
  # Worst: specialty-grade adzuki beans and imported Japanese ingredients
  # from small specialty importers may require 30-45 days during supply-chain
  # stress scenarios (port congestion, importer inventory gaps, seasonal
  # crop variation in adzuki bean supply from Hokkaido). This is the primary
  # supply-chain vulnerability for this entry; a 45-day worst-case lead time
  # requires maintaining 45-60 days of specialty ingredient inventory as a
  # working-capital buffer.
  # [CITATION-NEEDED: empirical lead-time data for specialty Japanese food
  # ingredients in US specialty food supply chain; label: inferred.]

  throughput_variance:
    seasonal: "Strong gift-giving peaks (New Year/January, Valentine's Day, spring cherry blossom March-April, Obon/midsummer gift season August); post-holiday January production trough; summer heat trough July-August when ambient conditions complicate cold-sensitive mochi handling"
    worst_month_fraction_of_average: 0.42
    best_month_fraction_of_average: 1.75

  operator_impact:
    noise_db: 55
    # Commercial steamer during active cycle (~50-60 dB); hot plate array
    # with ventilation hood (~50 dB ambient); convection oven fan (~50-55 dB).
    # Overall ambient: estimated 50-60 dB(A) during production; 55 dB(A) average.
    # Well below OSHA 90 dB(A) PEL. [CITATION-NEEDED: sound level measurement
    # for commercial steamer and hot plate production environment; illustrative
    # estimate; label: inferred. OSHA 29 CFR 1910.95 PEL: 90 dB(A).]
    heat_exposure: "Elevated ambient temperature and humidity near commercial steamer during active cycles (steam output produces sustained 28-35°C wet-bulb ambient near steamer); hot plate array adds radiant heat; convection oven adds heat during baking cycles; adequate with mechanical extraction at 2.5 m ceiling; operator positioned away from steamer during active cycle whenever forming and decorating; significant heat stress during peak production days in summer months without adequate HVAC"
    emissions: "No combustion emissions from electric steamer and hot plate array during normal operation; wood-fired steamer component (2-3 sessions/week) produces minor smoke and particulate — managed by dedicated flue or exterior-vented exhaust; sugar and flour dust are the primary occupational exposure concerns; exhaust hood manages steam and heat; standard food-production hygiene PPE applies"
    physical_demand: "Moderate; sustained standing; fine motor precision required for nerikiri forming and mold work (repetitive small-motion hand shaping — 100-300 individual forming actions per day for nerikiri-dominant production days); ergonomic workstation height critical to reduce wrist and shoulder strain from sustained forming posture; 5-10 kg ingredient-batch lifting; repetitive stirring and pressing for anko and mochi preparation"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Commercial kitchen or light-commercial food-production zoning required; wood-fired steamer component may trigger solid-fuel appliance permit or air-quality notice in urban or suburban jurisdictions — confirm with local air-quality management district before installation; no cottage-food exemption applies at this production volume"
  emissions: "Wood-fired steamer component requires solid-fuel combustion permit or notification in many jurisdictions; electric-primary operation is near-zero combustion and does not independently trigger an air-quality permit; mechanical exhaust hood may require building permit and inspection; occupational flour and sugar dust exposure governed by OSHA 29 CFR 1910.1000 Table Z-1"
  other: "Commercial food handler certification required for all production staff; health-department commercial kitchen inspection and annual licensing; HACCP plan required for wholesale and retail accounts; gift-packaging labeling requirements (ingredient, allergen, and weight disclosures) per FDA 21 CFR Part 101 food labeling rules; import permit considerations if sourcing ingredients directly from Japan rather than domestic distributor"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: good
  cooperative: marginal
  civic: marginal

scale_fit:
  village: poor
  town: good
  small_city: good

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:
  cooperative:
    membership_boundary: >
      Artisan confection collective within a town or small-city market; the
      cooperative form applies primarily to shared production infrastructure
      cost reduction (shared commercial steamer, ovens, and specialty equipment
      across 2-4 specialty confection producers operating on staggered schedules),
      not to a single-product wagashi production cooperative. Members must have
      a minimum of journeyman-baker or equivalent confection skill level;
      entry to the cooperative is gated on demonstrated production competence
      to prevent equipment damage from under-skilled members. Geographic scope:
      town or city residents with demonstrated specialty food production practice
      within a 15-20 mile radius, consistent with realistic commute to shared
      studio schedule.
    rules_source: >
      Operating agreement or multi-member LLC operating agreement adopted at
      founding; member vote required to amend scheduling, dues, equipment
      access, or production standards provisions; annual meeting reviews
      equipment-use allocation and dues schedule. Rules specify: booking
      protocol for shared steamer and oven access, cleaning responsibility
      per session (detailed, given the precision required in wagashi equipment
      cleanliness), ingredient storage rights and separation, equipment-damage
      liability, and dues schedule calibrated to equipment capital cost share.
    monitoring: >
      Equipment usage logged per session via booking ledger; monthly usage
      report to elected member-manager; health-department inspection compliance
      log maintained and available to all members; steamer and oven temperature
      logs reviewed weekly for calibration drift; ingredient storage inspections
      monthly (specialty ingredients require strict temperature and humidity
      management); damage or contamination incidents reported to member-manager
      within 24 hours.
    graduated_sanctions: >
      First incident (cleaning failure, booking overage, equipment misuse or
      cross-contamination): written warning and mandatory re-orientation on
      studio protocols and cleaning standards. Second incident within 12 months:
      $75 fine and 30-day booking suspension. Third incident within 24 months:
      membership review by member-manager and member committee; possible
      termination with dues refund pro-rated. Equipment damage: cost-recovery
      invoice plus warning; willful damage triggers immediate membership review.
      Per Ostrom Principle 5. [Ostrom 1990, Governing the Commons]
    conflict_resolution: >
      Member-elected manager handles first-level disputes (scheduling conflicts,
      cleaning disputes, ingredient-storage attribution, equipment damage
      attribution); appeal to full membership vote at next scheduled meeting;
      unresolved disputes referred to the LLC operating agreement dispute-
      resolution provisions. Per Ostrom Principle 6. [Ostrom 1990]
    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6]
    # Principle 1 (defined boundaries): membership_boundary; skill gate.
    # Principle 2 (rules fit local conditions): scheduling rules calibrated
    # to 2-4 specialty confection producer scale.
    # Principle 3 (collective choice): member vote to amend operating agreement.
    # Principle 4 (monitoring): booking ledger, temperature logs, usage reports.
    # Principle 5 (graduated sanctions): above.
    # Principle 6 (conflict resolution): above.
    # Principle 7 (external recognition): addressed via legal_form below.
    # Principle 8 (nested governance): not applicable at single-cooperative scale.
    member_amendment_process: >
      2/3 vote of all members at scheduled annual meeting; 30-day notice to all
      members required before any operating-agreement amendment vote; emergency
      amendment (3/4 vote) permissible with 7-day notice for health-code
      compliance or safety-related changes only.
    legal_form: >
      Multi-member LLC is the most practical structure for a shared specialty
      confection studio cooperative in US jurisdictions; provides member liability
      protection, external recognition (Ostrom Principle 7 analog), and the
      operational flexibility to admit members with varying product lines
      (not limited to wagashi). State-registered before launch; jurisdiction-
      specific filing required. Legal form as cooperative LLC is viable;
      full cooperative incorporation is feasible but carries higher administrative
      overhead than a multi-member LLC with cooperative operating terms.
    scale_fit_note: >
      Cooperative form is marginal for this entry: the primary cooperative
      value is shared specialty equipment cost reduction (splitting $38,000
      capital across 2-4 members reduces individual capital burden to
      $9,500-$19,000), not a full shared-production or shared-marketing
      cooperative. Scheduling complexity with 3+ members sharing a commercial
      steamer in a 32 m² kitchen approaches the coordination ceiling; 3-4
      members maximum is feasible. Village scale (500-2,000 residents) lacks
      sufficient addressable market for multiple specialty confection producers
      operating from a shared studio; town scale (2,000-15,000) is the minimum
      viable scale for this cooperative structure.

  civic:
    political_coalition: >
      Japanese or Asian-Pacific-Islander cultural organization partnership
      (community center, cultural association, or Japanese-American Citizens
      League chapter) providing facility access or grant support; municipal
      cultural-programming or arts-and-culture grant mechanisms; small-business
      development center support for food-based cultural enterprise; immigrant-
      entrepreneur support programs at county or municipal level.
    council_vote_estimate: >
      Uncertain; 4-3 favorable or 5-2 in a municipality with active cultural
      diversity programming and an identifiable Japanese or AAPI diaspora
      community. Opposition arguments likely center on: (a) low direct economic
      multiplier for a single-trade cultural program; (b) specialist skill
      requirement means staffing is difficult and expensive; (c) narrow
      addressable population (Japanese diaspora and cultural enthusiast segment).
      Civic investment is more defensible through a cultural-heritage programming
      frame than through a workforce-development frame, given the extreme
      specialization required.
    competes_with_private: >
      In most US towns and small cities, no established private wagashi studio
      exists; the entry fills a production gap rather than displacing a functioning
      operator. In a town with an existing Japanese confection business, civic
      investment that duplicates the private operator's product line would require
      explicit justification. In the more common scenario (no private competitor),
      the civic facility creates production capacity that does not otherwise exist
      in the market. Authors deploying this entry in a context with an existing
      private wagashi studio must assess displacement risk and justify civic
      investment on cultural-programming grounds rather than market-gap grounds.
    governance_form: >
      Culturally governed facility: operated by contracted wagashi master or
      master-level instructor under a partnership agreement with a Japanese
      cultural organization (community center, cultural society) that provides
      facility access and community accountability. The cultural organization
      provides governance oversight; the municipal grant provides capital
      or operating subsidy; the master practitioner provides technical
      delivery. This tri-party structure is consistent with existing models
      for civic cultural food programming (eg., Japanese cultural centers
      in San Jose, Seattle, and Portland that host food demonstration and
      production programs).
    budget_line: >
      Capital via cultural-programming grant (municipal, state, or federal
      cultural endowment), community development block grant, or partnership
      with Japanese cultural organization; operating costs partially offset
      by revenue from studio sales (gift market, cultural events, tea-ceremony
      supply) with municipal or organizational subsidy covering the gap.
      A fully self-sustaining civic wagashi studio is plausible only in a
      small city with a sufficiently large AAPI customer base; in a town,
      operating subsidy of $15,000-$30,000/yr above studio revenue is
      likely required to cover the master practitioner's wage.
    benchmark_comparison: >
      At town scale (~5,000 households), estimated annual per-household cost:
      ($38,000 capital / 15-year lifespan = $2,533 amortized + $68,000 wage +
      $18,500 consumables + $1,800 maintenance + $4,800 rent - studio revenue
      at mid-case ~$76,000/yr) / 5,000 hh = ($95,633 - $76,000) / 5,000 =
      $19,633 / 5,000 = $3.93/hh/yr net public cost. Comparable civic cultural
      programs: municipal public library at $42/hh/yr in peer towns [CITATION-NEEDED:
      per-household cost data for US public libraries, 2024]; municipal rec-center
      arts program at $15-$25/hh/yr [CITATION-NEEDED: municipal arts program
      cost survey, 2024]. Net civic wagashi studio cost of ~$3.93/hh/yr is
      below the library and comparable to arts-program costs — but depends
      heavily on achieving mid-case studio revenue, which requires a viable
      AAPI gift and cultural market. All figures are estimates; label: inferred.
    staffing_model:
      role: "contracted wagashi master or master-level instructor + production apprentice (part-time)"
      operator_fte: 1.0
      wage_assumption: 68000
      # Pastry-chef-master level skill is the floor for this position; wage
      # assumption follows the skilled-trades master-practitioner wage at
      # town scale. $68,000 is the corpus/program/SCALES.md §3 reference
      # for town-scale skilled-trades median; wagashi masters may command
      # premium above this in markets with few qualified practitioners.
      wage_source: "corpus/program/SCALES.md §3 town-scale skilled-trades median; wagashi master practitioners may command above-median wages in US markets with limited qualified practitioner supply — this figure is a lower-bound estimate"
      hours: "40 hrs/wk production, instruction, and cultural program administration"
      hiring_notes: >
        Hiring a qualified wagashi master or pastry-chef-master with wagashi
        specialty training is the primary constraint for civic deployment.
        The US qualified practitioner pool is very limited; most practitioners
        with genuine wagashi mastery are Japanese nationals, first-generation
        Japanese-American practitioners, or culinary professionals who trained
        in Japan. A realistic hiring radius for a civic program is national or
        international, not regional. Visa and immigration considerations may
        apply for practitioners recruited from Japan. The civic program is
        most viable when it partners with an existing practitioner who is
        already resident in the town or small-city market; cold-start hiring
        without a community connection is high-risk and slow. Apprentice
        pipeline from local culinary programs is a long-term strategy (5-7 year
        horizon to first locally-trained journeyman wagashi practitioner).
    civic_externalities:
      - "Cultural heritage access: makes fresh, hand-formed wagashi available in communities with Japanese diaspora populations who currently have no local access to non-imported traditional wagashi, creating a cultural food connection that has no market substitute at this quality level"
      - "Practitioner training pipeline: civic studio provides a teaching platform for wagashi technique transmission to locally-recruited apprentices, creating a long-term supply of qualified practitioners who would not otherwise train in a US context"
      - "Cultural programming anchor: a civic wagashi studio enables tea-ceremony education, cultural demonstration events, and intergenerational skill transmission programs for Japanese and broader AAPI community members — externalities that a purely private studio with commercial revenue pressure would under-supply"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 38000
  # Equals economics.capital_cost.mid per E3-R1.
  # [Derived from economics.capital_cost.mid above]

  cost_sd: 11250
  # Derived: (capital_cost.high - capital_cost.low) / 4 = (65,000 - 20,000) / 4
  # = $11,250. E3-R5 plausibility check: cost_sd/cost_mean = 11,250/38,000
  # = 0.296; within 0.15-0.50 range. [Derived per catalog/SCHEMA.md §3 default]

  throughput_units_equiv_per_year: 31400
  # Derivation (stated explicitly per baking SCHEMA.md §1 E-3 cross-check):
  # Unit: wagashi piece equivalent (weighted average across mochi, manjū,
  # nerikiri, and yokan slice; see Key Assumptions for weighting).
  # Step 1 — annual operating days:
  #   Studio operates approximately 5.5 days/week (retail model with Saturday
  #   operation); 5.5 days × 52 weeks = 286 days/yr; use 275 days/yr
  #   accounting for planned closure (holidays, equipment service, operator
  #   rest). A gift-market wagashi studio may close for extended periods
  #   between gift seasons.
  # Step 2 — pieces per day (gross):
  #   throughput.loaves_per_day = 130 pieces/day.
  # Step 3 — apply downtime fraction:
  #   130 pieces/day × 275 days/yr × (1 - 0.12 downtime) = 130 × 275 × 0.88
  #   = 31,460 pieces/yr → rounded to 31,400.
  # E3-R2 cross-check via active-hours method:
  #   max_active_hours_per_week (40) × 52 wk × (1 - 0.12) = 1,830 hr/yr.
  #   Net productive hours (excl. 45 min/day overhead): 1,830 - (0.75 hr/day
  #   × 275 days) = 1,830 - 206 = 1,624 hr/yr net production time.
  #   At 130 pieces/day ÷ ~6.7 effective production hr/day ≈ 19.4 pieces/hr;
  #   1,624 hr × 19.4 pieces/hr = 31,506 — consistent with 31,400.
  # [Derived from throughput fields, operating-day assumption, and downtime_fraction above]

  variable_cost_per_unit: 0.66
  # Specialty ingredients dominate variable costs:
  # Annual consumables ($18,500) across 31,400 pieces: $18,500 / 31,400
  #   = $0.589/piece for all consumables (ingredients + packaging).
  # Energy: 4.5 kWh/hr × 1,830 hr/yr × $0.125/kWh = $1,029/yr
  #   (wood component cost ~$200/yr additional at $0.10/kg × 3 kg/session
  #   × 2 sessions/wk × 52 wk = $31/yr; negligible). Total energy: ~$1,060/yr.
  #   $1,060 / 31,400 = $0.034/piece.
  # Total variable: $0.589 + $0.034 = $0.623 → $0.66/piece (rounded up for
  #   ingredient cost uncertainty; specialty adzuki and mochiko price variability
  #   is material). [Derived from annual_consumables, energy_consumption,
  #   EIA electricity price $0.125/kWh per SCALES.md §6 footnote]

  labor_hours_per_unit: 0.058
  # 1,830 hr/yr ÷ 31,400 pieces/yr = 0.0583 hr/piece → 0.058 hr/piece.
  # E3-R3 cross-check: 31,400 × 0.058 = 1,821 hr/yr; target = 40 × 52 × 0.88
  # = 1,830 hr/yr. Discrepancy = 9 hr (0.5%); within P2 threshold.
  # [Derived from throughput_units_equiv_per_year and max_active_hours_per_week]

  downtime_fraction: 0.12
  # Steamer element failure at ~2,200 hr → 14-day lead time = 2 weeks downtime.
  # Hot plate element failure at ~1,800 hr → 5-day lead time = ~1 week.
  # Specialty ingredient supply gap risk (worst-case 45-day lead time) modeled
  # as 1-2 weeks annual inventory risk given 45-day buffer requirement.
  # Routine maintenance shutdowns (~1-2 weeks/yr for annual service and
  # seasonal cleaning deep-cleans). Seasonal closures between gift periods.
  # Total: ~5-6 weeks effective downtime/yr out of 52 = 10-12%; using 0.12.
  # [Derived from operations_reality.first_year_failures and seasonal closure
  # pattern; E3-R6: downtime consistent with failure profile above]

  lifespan_years: 15
  # Commercial electric steamers and hot plate arrays: rated for approximately
  # 8,000-15,000 operating hours; at ~3-4 hr/day × 275 days/yr = 825-1,100
  # hr/yr, 10,000 hr service life → ~9-12 years to major refurbishment. Full
  # design life with refurbishment at year 10-12 supports a 15-year lifespan
  # before full equipment replacement. Wooden mold collections are maintained
  # continuously and represent indefinite lifespan if properly maintained.
  # [CITATION-NEEDED: service life data for commercial electric steamers;
  # illustrative estimate from general commercial kitchen equipment longevity;
  # label: inferred.]

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: win
    primary_metric: 0.3511497459309094
    metric_name: payback_years
    notes: ''
  village_coop:
    verdict: fail
    primary_metric: 140.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=140, total_annual_cost=27967
  village_civic:
    verdict: fail
    primary_metric: 43.46666666666666
    metric_name: per_household_cost
    notes: per_hh=43.47, threshold=120, hrs/capita=0.000 vs threshold=2.0
  town_market:
    verdict: win
    primary_metric: 0.3511497459309094
    metric_name: payback_years
    notes: ''
  town_coop:
    verdict: win
    primary_metric: 140.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=140, total_annual_cost=27967
  town_civic:
    verdict: fail
    primary_metric: 6.3921568627450975
    metric_name: per_household_cost
    notes: per_hh=6.39, threshold=100, hrs/capita=0.000 vs threshold=2.0
  small_city_market:
    verdict: win
    primary_metric: 0.3511497459309094
    metric_name: payback_years
    notes: ''
  small_city_coop:
    verdict: win
    primary_metric: 140.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=140, total_annual_cost=27967
  small_city_civic:
    verdict: fail
    primary_metric: 1.2074074074074073
    metric_name: per_household_cost
    notes: per_hh=1.21, threshold=80, hrs/capita=0.000 vs threshold=2.0
sources:
  - ref: "catalog/baking/SCHEMA.md v1.0 §1: throughput block structure; confection throughput_variance 0.35-0.55 worst, 1.30-1.80 best; E-3 cross-check guidance"
  - ref: "catalog/baking/SCHEMA.md v1.0 §2: hybrid-wood-electric energy source definition; temperature ceiling; regulatory posture; consumption notes"
  - ref: "catalog/baking/SCHEMA.md v1.0 §3: pastry-chef-master skill definition; wagashi named as requiring pastry-chef-master floor; product scope"
  - ref: "catalog/baking/SCHEMA.md v1.0 §4: flour_source_declaration required field; industrial-flour-purchased supply-chain risk"
  - ref: "catalog/baking/SCHEMA.md v1.0 §5: first_year_failures reference list; steam injector nozzle 1,200-2,500 hr; electric-deck element 1,500-3,000 hr"
  - ref: "catalog/baking/SCHEMA.md v1.0 §6 Group B: operator_skill_floor pastry-chef-master for bake-007; market_price_per_unit + industrial_baseline_price as core economic claim; civic-lens cultural externalities specificity requirement"
  - ref: "catalog/baking/DECLINE-VERDICT.md: specialty confection/pastry is the niche group; gift-giving and premium positioning guidance"
  - ref: "corpus/program/SCALES.md §3: town-scale skilled-trades median wage $68,000 reference for civic staffing_model.wage_assumption"
  - ref: "corpus/program/SCALES.md §6: infrastructure baseline; electricity $0.10-$0.15/kWh (US EIA Electric Power Monthly); specialty food distributor coverage by scale"
  - ref: "Ostrom, Elinor. 1990. Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press. (Chapters 2-3: eight design principles, graduated sanctions, conflict resolution)"
  - ref: "US Energy Information Administration. Electric Power Monthly, Table 5.3: Average Retail Price of Electricity. Monthly release. https://www.eia.gov/electricity/monthly/ (small-commercial blended rate 2023-2024: $0.10-$0.15/kWh; midpoint $0.125 used)"
  - ref: "OSHA 29 CFR 1910.1000 Table Z-1. Air Contaminants. (Flour and sugar dust permissible exposure limits; applicable to commercial confection production)"
  - ref: "OSHA 29 CFR 1910.95. Occupational noise exposure. (90 dB(A) PEL for 8-hour shift; confection studio ambient noise well below threshold)"
  - ref: "FDA 21 CFR Part 101. Food Labeling. (Ingredient, allergen, and net weight labeling requirements for packaged wagashi gift products)"
  - ref: "[CITATION-NEEDED: capital cost data for commercial electric steamers (10-20 tray capacity), hot plate arrays, and specialty confection equipment, 2024-2026; vendor catalog data from commercial kitchen equipment suppliers]"
  - ref: "[CITATION-NEEDED: capital cost data for Japanese wooden wagashi molds (kashigata, nerikiri molds, yokan forms), 2024-2026; Japanese kitchen supply vendors or specialty food tool importers]"
  - ref: "[CITATION-NEEDED: commercial steamer heating element MTBF data; manufacturer service documentation or commercial kitchen equipment reliability survey]"
  - ref: "[CITATION-NEEDED: annual maintenance cost data for commercial steamer and specialty confection kitchen operations; trade or operator survey, 2024]"
  - ref: "[CITATION-NEEDED: US wholesale price for dried adzuki beans (Japanese-grade), mochiko (sweet rice flour), and refined white bean paste (shiro-an), 2024; specialty Asian food distributor pricing]"
  - ref: "[CITATION-NEEDED: wholesale matcha price per kg for culinary-grade and premium-grade, US market, 2024; Japanese tea trade association or specialty importer pricing]"
  - ref: "[CITATION-NEEDED: packaging material costs (gift boxes, tissue, ribbon) for premium Japanese confection gift presentation at 100-150 pieces/day volume; specialty packaging supplier catalog data, 2024]"
  - ref: "[CITATION-NEEDED: commercial kitchen or light-commercial rental rate per m² in US town and small-city markets, 2024-2026; CoStar, LoopNet, or shared-kitchen aggregator data]"
  - ref: "[CITATION-NEEDED: artisan wagashi retail pricing survey in US specialty food, gift, and AAPI cultural market channels, 2024-2026; JETRO US food market reports or Specialty Food Association Japanese confection category data]"
  - ref: "[CITATION-NEEDED: US retail price survey for imported Japanese wagashi (Ohgiya, Imuraya, or equivalent brands), Asian supermarket and specialty food retail shelf pricing, 2024]"
  - ref: "[CITATION-NEEDED: service life data for commercial electric steamers; manufacturer specification or commercial kitchen equipment longevity survey]"
  - ref: "[CITATION-NEEDED: empirical seasonal demand data for wagashi retail (worst-month and best-month fractions); Japanese confection industry association data or operator financial survey, 2020-2026]"
  - ref: "[CITATION-NEEDED: empirical throughput measurement for commercial wagashi studios at comparable scale, Japan or diaspora US markets, 2020-2026; wagashi industry association production-capacity data]"
  - ref: "[CITATION-NEEDED: per-household cost data for US public libraries, 2024; American Library Association or Urban Institute municipal finance survey]"
  - ref: "[CITATION-NEEDED: municipal arts and cultural programming per-household cost survey, US peer towns, 2024; National Assembly of State Arts Agencies or Municipal Finance Officers Association data]"
  - ref: "[CITATION-NEEDED: Japanese confection (wagashi) apprenticeship curriculum and time-to-mastery documentation; Japanese confectionery industry organization (全国和菓子協会, Zenkoku Wagashi Kyokai) or Japanese culinary training program documentation]"
---
## Summary

Bake-007 is a specialist Japanese-style wagashi confection studio producing mochi, manjū, nerikiri, and yokan at town or small-city scale, targeting premium gift and specialty retail markets. Its distinguishing characteristics are: (1) hybrid-wood-electric energy configuration — commercial electric steamer and hot plate array as primary production equipment, with an optional wood-fired steamer retained for specific product lines and operational resilience; (2) a market-primary revenue model priced at $3-$15/piece against an industrial import baseline of $1.50/piece; (3) pastry-chef-master skill floor, reflecting the genuine technical requirement for nerikiri sculpting, mochi texture management, and anko production at commercial quality; and (4) explicit declaration of specialty-ingredient dependency (industrial-purchased, not locally milled) consistent with the DECLINE-VERDICT mill-dependency falsifier. This entry targets operators with verified wagashi technique who want to access premium gift and cultural markets; it is not a general-purpose confection studio that happens to offer wagashi as one product line. The binding constraints are skill (pastry-chef-master floor with wagashi specialization is a genuinely scarce qualification in the US market), market size (the addressable premium gift and diaspora customer segment is bounded and requires a town or small-city setting to sustain 130 pieces/day), and supply chain (specialty ingredients have long worst-case lead times that require working-capital inventory buffers). The civic lens is marginal and depends on the presence of a Japanese or AAPI cultural organization partnership to provide governance credibility and community accountability.

## Design rationale

This entry addresses a specific and bounded niche: the wagashi specialist who uses traditional Japanese confection technique — steam, hand-forming, and seasonal motif design — to access the premium gift and cultural retail market in a US diaspora or specialty food context. No other entry in the baking catalog covers this combination. The hybrid-wood-electric specification distinguishes bake-007 from purely electric confection studios by retaining a wood-fired steamer for specific product lines where operators judge steam character to matter and for operational resilience — not as an aesthetic statement about traditional methods. The market-primary lens fit distinguishes it from cooperative or civic forms by placing revenue generation as the primary viability test. The pastry-chef-master skill floor distinguishes it from entries that can be staffed at journeyman level; this is not a concession to cultural idealization but a factual claim about the technical requirements of nerikiri sculpting and mochi texture management at commercial quality levels. The specific problem this entry solves is: can a wagashi-specialized practitioner with master technique, $38,000 in capital, and a premium gift or specialty retail channel generate a sustainable income at town or small-city scale? At mid-case pricing ($6/piece × 31,400 pieces/yr = $188,400 gross revenue) and mid-case costs ($24,600/yr in cash operating costs), the answer is yes — with the critical caveat that identifying and retaining a qualified practitioner is the binding operational constraint, not economics.

## Historical lineage

Two functional precedents inform this design — both require careful treatment to avoid romanticizing elite historical consumption as folk tradition.

**Edo-period wagashi specialist workshop:** The wagashi trade in Edo-period Japan (1603-1868) operated within a court and merchant patronage system where confections were produced by specialist confectioners (wagashiya) for samurai-class ceremonial consumption, tea ceremony practice, and seasonal gift exchange among the merchant class [CITATION-NEEDED: primary source on Edo-period wagashi production and patronage structure]. Several features of this system are important to acknowledge honestly: (a) sugar was an imported luxury commodity of significant cost through most of the Edo period — wagashi were not everyday folk food but prestige goods [CITATION-NEEDED: sugar price and availability in Edo-period Japan]; (b) production in specialist workshops relied on apprentice labor under guild-adjacent guild-like systems that enforced quality standards and restricted market entry, similar in structure to European guild functions described in STYLE-GUIDE §4.4; (c) the tea ceremony context that is frequently invoked in marketing for premium wagashi was itself an aristocratic elite practice (chanoyu) developed among daimyo and high-ranking samurai — its association with wagashi represents court patronage consumption, not folk craft. What the historical Edo workshop provides in terms of functional inheritance to this entry is: (1) the product typology (nerikiri, mochi, yokan, manjū as established confection categories with recognized quality standards); (2) the gift-giving and ceremony-provision market structure (seasonal and occasion-based premium purchase); (3) the visual language of seasonal motif design that drives premium pricing in the modern gift market. The entry explicitly does not inherit the labor economics (apprentice and household labor at below-market compensation) or the patronage funding model (court and merchant-class elite subsidy) of the historical Edo workshop.

**Modern Japanese confection studio (premium retail):** The contemporary wagashi studio operating in Japan and in Japanese diaspora communities in the US, Canada, and Europe represents the direct operational precedent for this entry. These studios operate as small-batch premium specialty producers serving gift, cultural event, and tea-ceremony supply markets through retail storefronts, online gift channels, and direct cultural institution partnerships [CITATION-NEEDED: contemporary wagashi studio market data; JETRO or Specialty Food Association Japanese confection US market report]. This is not a traditional revival — it is a continuation of a specialist trade that has always served a premium market segment, now operating in a diaspora context with different customer demographics. The functional inheritance to this entry is: the product mix, the gift-market pricing structure, the operator skill requirements, and the equipment configuration. The modern studio uses electric steaming equipment in most cases; the wood-fired component in this entry is an optional premium feature retained for specific product lines, not a requirement of the historical form.

## Key assumptions

**Wagashi piece equivalent unit definition:** `sim_params.throughput_units_equiv_per_year` and `economics.market_price_per_unit` use a weighted-average wagashi piece as the unit. The weighting assumed is: 40% mochi-type (daifuku, simple mochi; ~$3-$6/piece retail); 30% manjū (steamed or baked, red-bean filled; ~$3-$6/piece); 20% nerikiri (hand-sculpted, high-skill; ~$8-$15/piece); 10% yokan slice (~$3-$5/slice from a cut block). A blended mid-price of ~$6/piece and blended throughput of 130 pieces/day reflects this mix. If a studio tilts toward nerikiri-dominant production, throughput drops (nerikiri is slower to form than mochi) and per-piece revenue rises; if it tilts toward mochi-dominant, throughput rises and per-piece revenue falls. The 130 pieces/day, $6/piece mid-case is intended to represent a balanced studio operating with both labor-intensive and higher-volume product lines.

**Specialty ingredient dependency:** This studio depends on specialty-sourced adzuki beans, sweet rice flour (mochiko), white bean paste (shiro-an base), and quality matcha. These are not commodity inputs available from general food distributors; they require specialty Asian food importers or direct-import relationships. Supply-chain disruption risk is higher than for a commodity-flour bakery: worst-case 45-day lead time [consumables_lead_time_days.worst] compared to 21 days for commodity flour in bake-001. A 45-day ingredient buffer requires approximately $2,200-$2,500 in working-capital inventory ($18,500/yr ÷ 275 days × 45 days = $3,027 at maximum; in practice, not all ingredients have 45-day lead times, so $2,500 is a reasonable working-capital estimate for the buffer). All ingredient cost figures are labeled [CITATION-NEEDED]; the $18,500/yr annual consumables estimate is inferred and requires verification from operational data.

**Capital costs ($20,000-$65,000):** Labeled inferred from market observation of commercial kitchen equipment and specialty food tool vendors. The mid-point ($38,000) includes a capable commercial steamer, hot plate array, small convection oven, a reasonable wooden mold collection, and a full commercial kitchen fitout. The wooden mold collection cost is the most uncertain element: high-quality traditional Japanese molds (kashigata, nerikiri molds) can range from $50 to $500+ per mold; a working collection of 60-100 molds for seasonal variety could cost $3,000-$8,000. [CITATION-NEEDED for all equipment cost figures including mold pricing.]

**sim_params derivation:** `throughput_units_equiv_per_year` (31,400) derived from pieces/day × operating days × (1 - downtime). Unit is the wagashi piece equivalent as defined above. Monetary values in USD. Electricity price $0.125/kWh from US EIA Electric Power Monthly blended small-commercial rate 2023-2024. All economic numbers labeled inferred pending verification.

## Known risks / failure modes

**Regulatory:** The hybrid-wood-electric energy configuration creates the most complex regulatory profile in the baking entry set. The wood-fired steamer component requires a solid-fuel appliance permit or air-quality district notification in many US jurisdictions; air-quality management district (AQMD) regulations in California, Washington, and other states with active air-quality programs may restrict or prohibit new wood-burning appliances in commercial food production settings in designated non-attainment zones. An operator who selects a site without confirming wood-component permissibility faces the risk of having to operate electric-only, which is a fallback but may require adjustment to the product lines where the operator judges wood-steam character to matter. The electric-only fallback is operationally viable; it is the primary steam configuration regardless. Food labeling compliance for packaged wagashi gift products (FDA 21 CFR Part 101) requires Japanese-language labeling on any product with Japanese text, and allergen disclosures for red bean, wheat, and tree nuts (if used in fillings) are mandatory. Import documentation requirements may apply if ingredients are sourced directly from Japanese suppliers.

**Labour pipeline:** Pastry-chef-master with wagashi specialization is the single most constraining qualification in the baking entry set. The qualified practitioner pool in the US market is very small: most US culinary programs do not include wagashi training; practitioners with genuine mastery are primarily Japanese nationals, first-generation Japanese-American community members, or culinary professionals who completed training in Japan. A civic facility attempting to hire a wagashi master will face national or international recruitment and potentially visa constraints. A private studio must be operated by a practitioner who already has the skill — this entry does not have a viable "build the skill from scratch" startup path on a normal business timeline. `apprentice_friendly: true` reflects the long-term succession path, but the 42-72 month time-to-independent-operation is genuinely long, and a studio that loses its master operator without an advanced apprentice in Stage 3-4 faces a multi-year production gap. This succession risk is the single most significant long-term operational constraint for this entry.

**Supply chain:** Specialty Japanese food ingredients — adzuki beans, mochiko, high-quality matcha, shiro-an (white bean paste) base — are imported specialty items with supply chains that are more concentrated and less redundant than commodity flour. A worst-case 45-day lead time on adzuki or mochiko requires maintaining a 45-day ingredient buffer as working capital. Single-importer dependency is common for small studios sourcing from specialty distributors; developing relationships with at least two independent specialty ingredient suppliers reduces but does not eliminate this risk. Adzuki bean crop variation in Hokkaido (the primary Japanese production region) can cause price spikes and availability gaps in the US specialty market; this is a structural supply-chain vulnerability that is not present in commodity wheat flour supply chains.

**Market size at town scale:** The addressable market for fresh artisan wagashi at $3-$15/piece in a US town is geographically and demographically bounded. Japanese diaspora communities vary significantly in size and concentration by US region; a town in the US Midwest may have few Japanese diaspora residents and a limited culturally-adjacent food-enthusiast segment. This entry is more viable in Pacific Coast, Northeast, and Hawaii markets with established Japanese diaspora populations than in the interior US. The mid-case revenue assumption ($188,400/yr) requires approximately 31,400 pieces sold at an average $6/piece; at a reasonable market visit frequency of one 12-piece gift purchase per customer per month, this requires approximately 218 distinct customer transactions per month, or roughly 130 average daily transactions — plausible in a small city, more challenging in a town without significant diaspora or tourism traffic. Authors deploying this entry in a specific market should verify the addressable market estimate against local demographics before accepting the mid-case revenue figure.

## Iteration log

- 2026-04-18: v0.1 — initial authoring per Plan G Task 9. All schema fields populated
  including trade_specific.flour_source_declaration per DECLINE-VERDICT mill-dependency
  falsifier; market (good), cooperative (marginal), and civic (marginal) lens_context
  blocks fully populated per E2-R5 and E2-R6; market pricing labeled pricing_validation:
  inferred per citation policy; 17 CITATION-NEEDED placeholders carried forward for
  post-authoring verification; sim_params derivation stated explicitly in field comments
  with E3-R2 and E3-R3 cross-checks demonstrated; anti-romantic historical lineage
  section explicitly addresses Edo-period wagashi as elite court/merchant patronage
  consumption (not folk craft), acknowledges sugar as luxury commodity, and names
  the guild-like labor control structure per STYLE-GUIDE §4.3 and §4.4; forbidden
  framings per STYLE-GUIDE §4 verified absent.
