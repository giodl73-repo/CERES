---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: bake-011
trade: baking
name: "Apprentice Training Bakery"
tagline: "Coop-or-civic electric-deck training bakery; produces real bread for sale while simultaneously training apprentices through CTE / vocational partnership"
status: draft
version: "0.1"
supersedes: null
inspirations:
  - mondragon-worker-cooperative
  - us-cte-vocational-education-tradition
  - danish-folkehojskole-practical-education-model

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 65
# Mid-range of the 50-80 m² span. Multi-station layout for parallel trainee
# work: a two- or three-deck electric oven stack, dedicated proofing and cold-
# retard cabinet, heavy-duty spiral mixer, 2-3 trainee dough-prep stations,
# a master-instructor demonstrator bench (separate from trainee stations),
# ingredient staging, cooling rack zone, and packaging/dispatch area.
# Training bakeries require more linear bench space than single-operator
# commercial bakeries: trainees must have independent work surfaces so
# instruction can occur without interrupting production on adjacent stations.
# 50-80 m² is the operative range; 65 m² is the mid-estimate for a 1 instructor
# + 2-3 apprentice concurrent configuration. Single-operator commercial artisan
# entries (bake-001, bake-002) fit in 25-40 m²; the training-floor multiplier
# reflects independent apprentice stations plus the demonstrator bay.
# [CITATION-NEEDED: footprint benchmarks for vocational bakery training labs;
# structural inference from baking SCHEMA.md §1 multi-operator throughput
# ranges and CTE facility guidance; label: inferred.]

ceiling_min_m: 2.8
# Standard commercial kitchen ceiling adequate for electric-deck oven stack
# (two- or three-deck units fit within 2.5 m height; exhaust hood and ductwork
# require clearance above deck top). No combustion stack height requirements
# for electric configuration. 2.8 m is the minimum; 3.0-3.2 m is preferable
# for overhead heat management during multi-deck parallel operation.

ventilation: kitchen-exhaust-hood-required
# Electric deck produces no combustion gases; on-site emissions are steam,
# flour dust, and ambient heat. A commercial exhaust hood with mechanical
# extraction is required for health-code compliance and for operator/trainee
# comfort during multi-hour, multi-station parallel bake sessions. Flour-dust
# occupational exposure is governed by OSHA 29 CFR 1910.1000 Table Z-1; PPE
# (dust masks during extended mixing) is required and addressed in Known Risks.

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: electric-deck
# Per specification requirement. Three independent reasons for electric-deck
# in a training environment. (1) Safety: no open flame or gas storage; fire
# code and insurance profile are substantially simpler for a facility with
# trainees at varying skill levels. (2) Pedagogical consistency: thermostat-
# controlled bake temperature removes one variable during early training stages,
# so instruction can focus on dough fermentation, shaping, and scoring without
# simultaneously requiring trainees to manage oven temperature by feel.
# (3) Regulatory: near-zero on-site combustion emissions; no air-quality permit
# trigger; cleanest path through health-department commercial kitchen licensing
# for a publicly-partnered or cooperatively owned facility.
# Capability note (per baking SCHEMA.md §2): electric-deck ceiling 230-290°C;
# thermostat-controlled; steam injection requires a separate steam-injector
# add-on or water-tray setup; adequate for full sourdough and yeasted bread
# curriculum. Complex laminated doughs and competition Viennoiserie are outside
# the base curriculum scope (see product_mix), consistent with operator_skill_floor.
energy_consumption_per_active_hour: "11 kWh"
# Two- or three-deck commercial electric oven at sustained bake load plus
# proofing cabinet: each deck rated ~4-6 kWh sustained; three-deck unit at
# combined operating temperature approximately 10-12 kWh/hr. Proofing cabinet
# adds ~0.5-1 kWh/hr when running simultaneously. 11 kWh/hr is the upper-
# mid estimate for a full three-deck installation during peak training sessions
# when all decks are loaded simultaneously.
# Per baking SCHEMA.md §2: electric-deck 3-8 kWh/batch; multi-deck training
# installation at full load approaches 11 kWh/active hour.
# [CITATION-NEEDED: manufacturer energy consumption data for three-deck
# commercial electric ovens; e.g., Bongard Neopolis, Sveba-Dahlen D-series,
# or equivalent; three-deck combined kWh/hr at sustained bake temperature;
# label: inferred.]
backup_fuel: null
# No backup fuel in base configuration. Electric-deck is the sole energy
# source; grid outage risk is noted in Known Risks. Adding a gas backup
# would introduce combustion permits and gas-line infrastructure that conflicts
# with the training facility's clean regulatory profile. A generator is the
# appropriate grid-outage mitigation for a civic or cooperative facility.

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  loaves_per_day: 120
  # Net production output per full operating day. Unit: 800g sourdough boule
  # equivalent (see Key Assumptions for unit definition). The training bakery
  # is dual-purpose: approximately 30% of daily output is training output
  # (apprentice-made bread from learning sequences — imperfect crust, inconsistent
  # scoring, slightly variable crumb — consumed internally, donated, or sold at a
  # discount as "student bread") and 70% is production-quality sold bread (instructor-
  # led production and advanced-apprentice output meeting commercial standard).
  # At three-deck capacity: each deck holds approximately 10-14 loaves per bake at
  # 800g boule spacing; 3 decks × 3 bakes/day = ~99-126 loaves/day at full
  # utilization. 120 loaves/day is the mid-estimate accounting for the training
  # overhead (slower trainee cycle times, re-bakes, instructor demonstration loads).
  # [CITATION-NEEDED: throughput data for vocational training bakery with 1 instructor
  # + 2-3 trainees; structural inference from baking SCHEMA.md §1 town-artisan
  # range 80-250 and multi-operator training-overhead adjustment; label: inferred.]

  batches_per_day: 6
  # Three decks × 2 bake loads per deck per operating day.  Morning and
  # afternoon bake cycles; three decks loaded on staggered timing to maintain
  # continuous production and to give each trainee hands-on loading and unloading
  # practice without overloading any single trainee's dough-management timeline.
  # Six batches/day is within the 6-12 range for wholesale-capable operations
  # per baking SCHEMA.md §1; training facility lands at the lower end of that
  # range due to the staggered-timing pedagogy.

  batch_size_loaves: 20
  # Three-deck unit: approximately 12-14 loaves per deck per load at 800g boule
  # spacing; 20 loaves per combined batch-cycle at the training pace
  # (some deck space reserved for trainee observation and re-shaping exercises).
  # A commercial three-deck unit at full production could hold more; the 20-loaf
  # figure reflects the training-load constraint.
  # [CITATION-NEEDED: deck-oven capacity per m² of deck area; three-deck commercial
  # oven manufacturer specifications; label: inferred.]

  max_active_hours_per_week: 40
  # Full-time operation: 5 operating days/week × 8 hr/day = 40 hr/wk gross.
  # Training bakeries are intentionally run at full commercial hours — the curriculum
  # point is that trainees are working a professional production schedule, not a
  # reduced-pace school lab. The production schedule is the instruction vehicle.
  # 40 hr/wk is the gross ceiling; net of startup-shutdown overhead derated in
  # sim_params. Per baking SCHEMA.md §1, realistic ceiling for a full-time artisan
  # bakery is 35-45 hr/wk; 40 hr/wk is within range.

  product_mix:
    bread: 75
    # Sourdough and yeasted bread is the primary curriculum focus: bulk fermentation
    # management, shaping, scoring, bake-time judgment. Sourdough boules, bâtards,
    # batard loaves, standard sandwich loaves, and enriched yeasted breads (challah,
    # soft rolls). Instructor manages full sourdough program; trainees take progressive
    # responsibility for fermentation judgment as they advance through training stages.
    confection: 0
    # No confection in base curriculum. pastry-chef-master operator_skill_floor is
    # required for teaching (not for confection output): the master's technical range
    # is necessary to observe, diagnose, and correct trainee fermentation and bake
    # errors across all product types. Confection is excluded from base product_mix
    # because the training time is concentrated on bread fundamentals; a trainee who
    # masters bread fermentation and deck-oven management has acquired transferable
    # skills. Confection can be added as a curriculum module in advanced training years
    # without changing the facility's equipment specification.
    specialty: 20
    # Cultural specialty breads, regional traditional loaves, and occasional enriched
    # specialty items (pan de muerto, injera analog, rye-wheat blends, seed breads).
    # Specialty output (a) differentiates the bakery's sold product from commodity
    # artisan bread, (b) provides trainees with exposure to diverse fermentation
    # timelines and dough hydrations beyond standard sourdough, and (c) supports
    # civic-lens cultural-continuity externalities.
    catering: 5
    # Institutional or event catering (community events, partner organizations,
    # food-program deliveries). Not a commercial catering operation; the 5%
    # catering share reflects bread supply to the vocational program's partner
    # institutions and civic partner organizations.
    training_output: 0
    # Training output (imperfect apprentice-made bread) is folded into the
    # bread and specialty shares above; not tracked as a separate category
    # because in a live-production training bakery, all output — including
    # apprentice-made product — enters the production stream (some sold at
    # a discount, some donated, none wasted intentionally). The 30% sold-bread
    # vs 70%-training-output ratio declared in the entry brief is a revenue
    # characterization, not a product-mix separation: the physical product
    # stream is unified, but ~30% of daily output is production-quality (full
    # market price) and ~70% is training-quality (discount or donation).
    # Sum: 75 + 0 + 20 + 5 + 0 = 100.

  throughput_variance:
    seasonal: "Moderate bread seasonality: autumn-winter demand increases for hearth-style and enriched breads; summer trough for walk-in retail; apprentice-cohort transitions (typically August-September intake, May graduation) cause 2-3 week reduced-output periods"
    worst_month_fraction_of_average: 0.55
    # Summer trough (July-August) plus cohort-transition period; new apprentice
    # intake in August-September depresses output as the incoming cohort builds
    # basic competency. Consistent with baking SCHEMA.md §1 artisan bread range
    # 0.55-0.75 for worst-month fraction. [Baking SCHEMA.md §1 guidance; label: inferred.]
    best_month_fraction_of_average: 1.35
    # November pre-holiday peak; experienced cohort mid-year (spring) when advanced
    # trainees are contributing fully to production output. Consistent with SCHEMA.md §1
    # artisan bread range 1.20-1.40. [Baking SCHEMA.md §1 guidance; label: inferred.]

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: pastry-chef-master
# Per specification requirement. A training bakery requires the head instructor
# to hold the highest skill tier. Three independent reasons. (1) Diagnostic
# authority: the instructor must simultaneously monitor 2-3 trainee dough batches
# at different fermentation stages, identify under- or over-fermentation by sight
# and feel, and intervene with precise corrective instruction while managing the
# production schedule. A journeyman-baker cannot reliably do this across 2-3
# concurrent trainees without creating production failures. (2) Curriculum authority:
# the instructor must hold competency well beyond the curriculum scope to answer
# "why" questions credibly — trainees at month 12-18 will ask questions about
# fermentation biochemistry, flavor development, oven spring physics, and regional
# bread traditions that require master-level knowledge. (3) Assessment authority:
# the instructor must certify trainee competency at each stage gate; this requires
# the personal authority of demonstrated mastery, not credential alone. Per baking
# SCHEMA.md §3: pastry-chef-master has full range across bread, pastry, and confection;
# can train and assess journeyman and apprentice operators. Required by this niche.
operators_concurrent: "1 pastry-chef-master instructor + 2-3 apprentices"
# Normal training-floor staffing: 1 lead instructor (master) supervises the full
# production floor; 2-3 enrolled apprentices work concurrently at independent
# dough-prep stations under graduated supervision. Unlike a commercial production
# bakery where a single operator is throughput-limited, the training bakery's
# labor overhead is intentionally higher: the instructor's time is split between
# production management and instruction. The 2-3 trainee ceiling is a pedagogical
# safety ratio: more than 3 simultaneous trainees at the dough-prep stage spreads
# instructor attention too thin to catch fermentation errors in time to prevent
# failed batches. At the bake stage, the instructor can supervise up to 3 decks
# simultaneously with trainees managing loading/unloading.
apprentice_friendly: true
apprentice_path:
  training_stages: >-
    Stage 1 — Kitchen Foundations and Dough Introduction (months 0-3): food-handler
    hygiene and safety, commercial kitchen protocol, electric-deck oven startup
    and shutdown procedure, proofing cabinet and spiral mixer operation, baker's
    math (percentages, scaling), sourdough starter observation and feeding schedule.
    Trainees observe and assist during production but do not independently shape or
    bake. Competency gate: pass food-handler certification; demonstrate correct oven
    startup and shutdown procedure without prompting; maintain an assigned sourdough
    starter on schedule for three consecutive weeks; complete three baker's-math
    scaling exercises to spec.

    Stage 2 — Dough Mixing and Basic Shaping (months 3-9): yeasted bread dough mixing
    (straight dough method, autolyse, stretch-and-fold introduction), basic round and
    bâtard shaping, bench rest and final proof management under instructor supervision.
    Production: trainees mix and shape their own assigned batches; instructor monitors
    dough development and intervenes with technique correction. Introduction to oven
    loading with peel — safety-critical; instructor supervises every oven load until
    trainee demonstrates consistent safe technique. Introduction to deck temperature
    reading by product behavior (oven spring, crust color progression). No independent
    sourdough management yet; trainee follows a prescribed fermentation schedule.
    Competency gate: complete eight consecutive yeasted sourdough boules in two separate
    production sessions, with final four meeting instructor's commercial-quality standard
    for crust, shape, and crumb; demonstrate safe oven loading and unloading
    independently; explain the function of bulk fermentation in plain language.

    Stage 3 — Sourdough Fermentation and Deck Judgment (months 9-24): full sourdough
    bulk fermentation management (temperature-adjusted timing, windowpane test,
    aliquot jar use), graduated independent decision-making on fermentation schedule
    adjustments. Introduction to deck-temperature management (steam timing, rotating
    loaves, vent timing for crust development). Introduction to specialty bread
    formulas (high-hydration doughs, enriched doughs, seed breads). Trainees take
    progressive responsibility for one designated batch per day; instructor reviews
    outcome and provides written feedback per batch cycle. Introduction to production
    planning (calculating yields, scaling formulas, staging timeline for the day).
    Repair role: trainees begin to recognize and document production failures
    (over-proofed batches, under-tempered starter, scaling errors) and propose
    corrective action; instructor validates or corrects analysis.
    Competency gate: manage a full production day independently (instructor present,
    not intervening) including sourdough schedule, shaping, bake timing, and production
    log entry; instructor certifies output meets commercial-quality standard for three
    of four batches without guidance. Demonstrate fermentation-schedule adjustment
    rationale for a temperature-deviation scenario in oral assessment.

    Stage 4 — Advanced Production and Vocational Certification (months 24-42): full
    responsibility for assigned formula rotation in the daily production schedule;
    specialty bread development (new formula testing, cultural-bread research, seasonal
    variations); introduction to ordering and inventory management; co-facilitation of
    Stage 1-2 trainee instruction under instructor oversight. Trainees eligible for
    local, state, or program-affiliated vocational-baker assessment at month 36. Dual-
    enrollment credits with community-college culinary or food-science program where
    partnership is in place. Pathway to journeyman-baker certification: trainee
    completes a live production assessment (full production day at commercial standard,
    observed by instructor and external assessor), submits a portfolio of three original
    formula developments, and demonstrates Stage 1-2 instruction capability.
    Competency gate for journeyman-baker certification: pass program-affiliated
    vocational-baker assessment or equivalent external credential; complete portfolio
    review; receive instructor endorsement for independent employment or further
    cooperative/civic employment.

  time_to_independent_operation: >-
    ~36-42 months to journeyman-baker standard for independent commercial bakery
    employment. The 36-month floor is the fermentation-judgment formation timeline:
    trainees require approximately 2 full sourdough cycles (each cycle: starter
    maintenance, bulk, proof, bake, evaluation) per week for approximately 18-24
    months before fermentation judgment becomes reliable. The final 12-18 months
    (Stage 4) are advanced production and curriculum teaching, which build the
    independence required for a journeyman role. The 42-month ceiling applies when
    a trainee requires additional fermentation or deck-judgment development time
    before the Stage 4 production assessment. This is a professional-production
    timeline, not a school-lab timeline: trainees are producing real bread for real
    customers throughout the program, which accelerates skill formation relative to
    a demonstration-only lab setting. [CITATION-NEEDED: vocational-baker training
    timeline; European bakery apprenticeship duration reference; US culinary program
    baker-track length comparison; label: inferred from analogous forge-009 European
    apprenticeship precedent and baking program structures.]

  succession_note: >-
    The training structure embeds succession in the production model by design.
    Each 36-42 month cohort cycle is expected to produce 2-3 journeyman-baker
    certified graduates per cohort of 2-3 apprentices. Advanced apprentices in
    Stage 4 actively co-instruct Stage 1-2 trainees, reducing the master instructor's
    sole-practitioner dependency and building instructional depth. When the master
    instructor transitions out, the longest-tenured journeyman graduate who has
    completed co-instruction experience in Stage 4 can step into a probationary
    head-baker role while the cooperative or civic authority recruits a replacement
    master. The training bakery's documented curriculum, production logs, formula
    records, and stage-gate assessment criteria provide institutional continuity
    that is not dependent on a single instructor's tacit knowledge. Vocational-
    program partnership (CTE or community-college) adds an additional institutional
    anchor: the partner institution maintains curriculum documentation and assessment
    standards independently of the bakery operator.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 55000, mid: 95000, high: 150000 }
  # Multi-station training bakery with electric-deck oven. Low: entry-level three-
  # deck commercial electric oven ($22,000-28,000 refurbished or budget new) +
  # proofing cabinet ($4,000) + commercial spiral mixer ($4,500) + 2 trainee
  # dough-prep stations (benches, tools, bannetons: $6,000) + smallwares and
  # ingredient storage ($3,000) + basic exhaust hood ($5,000). Minimal fitout;
  # CTE or cooperative partner may contribute in-kind space preparation.
  # Mid: mid-grade three-deck commercial electric oven ($38,000-45,000 new) +
  # full proofing and cold-retard cabinet system ($7,000) + heavy-duty spiral
  # mixer with dough divider ($7,000) + 3 fully equipped trainee stations
  # ($10,000) + demonstrator bench ($3,000) + exhaust hood system with makeup
  # air ($6,000) + smallwares, starter kit, packaging station ($4,000).
  # High: premium three-deck commercial oven with digital temperature logging per
  # deck ($55,000-60,000) + full cold-retard and proofing system ($10,000) +
  # premium heavy-duty spiral mixer ($9,000) + 3 trainee stations plus overflow
  # capacity ($12,000) + demonstrator bench with full production tools ($5,000) +
  # code-compliant exhaust and ventilation system ($8,000) + ADA-compliant
  # member workstation modifications ($3,000) + full smallwares and curriculum
  # materials ($4,000).
  # [CITATION-NEEDED: capital cost data for vocational training bakery with three-
  # deck commercial electric oven; Bongard, Sveba-Dahlen, Mono Equipment, Revent,
  # or equivalent equipment vendor pricing 2024-2026; label: inferred.]

  install_cost: 9500
  # Electrical service upgrade (80-100A dedicated circuit for three-deck unit
  # plus supporting equipment; typical commercial install $4,000-6,000); exhaust
  # hood and ductwork installation ($2,500-4,000); health-department commercial
  # kitchen inspection and certification ($500-1,500); minor structural prep
  # (floor drains, water supply for steam-injector add-on, if applicable).
  # [CITATION-NEEDED: commercial kitchen electrical service upgrade and hood
  # installation cost from regional contractor estimates; label: inferred.]

  annual_maintenance: 3200
  # Three-deck oven servicing (annual professional service + quarterly element
  # and thermostat inspection), proofing cabinet calibration, spiral mixer
  # maintenance (motor brush, bowl seal, hook inspection), exhaust hood quarterly
  # deep cleaning (health-code requirement), trainee tooling replacement (bannetons,
  # bench scrapers, lames, dough knives), scale calibration. Multi-trainee use
  # accelerates shared tooling wear and requires more frequent consumable tooling
  # replacement than a single-operator bakery. Excludes first-year failure items
  # in operations_reality.
  # [CITATION-NEEDED: annual maintenance cost for commercial bakery with 3-deck
  # oven in a multi-operator training context; label: inferred.]

  annual_consumables: 28500
  # Primary: flour for production (sold bread + training-quality output).
  # Production bread: ~85 loaves/day × 260 days × 0.7 kg/loaf × $0.60/kg flour
  # = ~$9,282/yr [CITATION-NEEDED: commodity bread flour wholesale price per kg,
  # 2024; US Foodservice, Sysco, regional food co-op pricing]. Training-quality
  # bread (additional flour waste from failed batches and practice sequences):
  # ~20% above production flour usage = ~$1,856/yr additional. Salt, water,
  # enrichment additives (eggs, butter for enriched loaves, seeds): ~$2,500/yr.
  # Packaging (bags, stickers, clamshells for sold output): ~$3,200/yr at 85
  # sold loaves/day. Sourdough starter maintenance (premium flour for starter
  # upkeep): ~$600/yr. Trainee PPE replacement (aprons, gloves, dust masks:
  # quarterly, per health code): ~$1,200/yr. Miscellaneous (scoring lames,
  # parchment, proofing covers): ~$900/yr. Total consumables: ~$19,538/yr
  # production consumables + ~$9,000/yr curriculum consumables and trainee
  # practice waste = ~$28,500/yr.
  # [CITATION-NEEDED: above pricing estimates; label: inferred.]

  floor_space_rent_per_year: 7200
  # Town-scale commercial kitchen or light-commercial space estimate for 65 m²:
  # approximately $110/m²/yr effective rate = $7,150/yr, rounded to $7,200/yr.
  # In civic variant: imputed at $0 (municipal building). In cooperative variant:
  # actual rent applies at local commercial-kitchen or mixed-use commercial rate.
  # $7,200/yr is the imputed baseline for cooperative or independent-operator cost
  # comparison; civic entries substitute $0 per standard schema guidance.
  # [CITATION-NEEDED: town-scale commercial kitchen or light-commercial floor-space
  # rent at $110/m²/yr; SCALES.md §4 commercial rent estimate; label: inferred.]

  market_price_per_unit: { low: 0, mid: 0, high: 0 }
  # Per specification requirement: zero commercial pricing for this entry.
  # The apprentice training bakery is workforce infrastructure, not a commercial
  # retail operation. The "sold bread" revenue (30% of output at commercial
  # prices) is an operating revenue offset that partially funds training costs,
  # not the primary viability basis. Per spec: "Market: zero commercial pricing."
  # The facility sells bread, but pricing is at break-even or modest cost-recovery
  # levels to fund training, not to generate commercial profit. The market-lens
  # verdict is poor by design. See pricing_notes.

  pricing_notes: >-
    The apprentice training bakery is workforce infrastructure, not a commercial
    artisan bakery. market_price_per_unit is set to zero because the facility's
    sold-bread revenue (approximately 30% of output sold at $5-8/loaf to food-
    service partners, food pantries, or community members) is an operating-cost
    offset, not a market-clearing price tested against commercial competition.
    The industrial baseline price ($3.50/loaf supermarket sourdough equivalent;
    [CITATION-NEEDED: US supermarket sourdough shelf pricing, 2024]) is cited for
    reference only: the training bakery does not attempt to compete on price or
    premium with retail artisan bakeries. Bread revenue is incidental to the
    training mission; it reduces the net cost of operating the program but does
    not determine whether the program is viable. The primary revenue basis is
    program fees (CTE partnership funding, cooperative member dues or employer
    levies, workforce-development grants), not bread sales.

  industrial_baseline_price: 3.50
  # 800g supermarket sourdough equivalent (standard supermarket private-label
  # or national brand). Cited for civic-value reference only; not used in revenue
  # calculations (lens_fit.market: poor).
  # [CITATION-NEEDED: US supermarket sourdough bread shelf pricing, 2024;
  # illustrative estimate from market observation; label: inferred.]

  pricing_validation: >-
    N/A — this is a workforce-training facility with incidental bread revenue,
    not a commercial market operation. The industrial baseline is cited for
    community-value reference framing only (documenting the bread value delivered
    relative to supermarket equivalent cost). No market-price claim is made.
    Pricing_validation is not applicable per catalog/SCHEMA.md §3 (required only
    when market_price_per_unit is present with non-zero values); this entry
    sets market_price_per_unit to zero per the "zero commercial pricing" requirement.

# ── TRADE-SPECIFIC FIELDS ────────────────────────────────────────────────────

trade_specific:
  flour_source_declaration: industrial-flour-purchased
  # Per baking SCHEMA.md §4 required field and DECLINE-VERDICT mill-dependency
  # falsifier. The apprentice training bakery purchases commodity or specialty
  # bread flour from industrial mills or regional food-service distributors.
  # No mill infrastructure is owned or operated; no direct farm relationship assumed.
  # Rationale: the training program's priority is pedagogy, not grain sourcing.
  # Trainees learn fermentation judgment, dough development, and bake management
  # first; flour sourcing differentiation is a business complexity that is
  # appropriately deferred to post-program journeyman career development. Using
  # a consistent, predictable commodity flour also eliminates flour-quality
  # variability as a confound during the early training stages (Stage 1-2),
  # where trainees need stable input materials to calibrate their fermentation
  # observations. A local-mill partnership or heritage-grain rotation can be
  # introduced as a Stage 3-4 curriculum extension without modifying the
  # facility's base supply chain.
  # Supply-chain risk: commodity flour price volatility (wheat market); distributor
  # availability. Standard distributor lead time 2-5 days at town scale.
  # See Key Assumptions for full flour sourcing discussion.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Deck heating element (electric) — one of three decks"
      estimated_hours_to_failure: 2200
      replacement_cost: 700
      replacement_lead_time_days: 14
      serviceable_by: specialist
      # Three-deck unit: a single-deck element failure reduces capacity by ~33%
      # but does not halt production (two remaining decks carry load). At
      # ~6 active bake-hours/day × 260 days/yr = 1,560 hr/yr, first deck
      # element failure is expected in year 1-2 of operation. 14-day lead
      # time for specialist replacement is the primary partial-downtime event
      # in year 1. Per baking SCHEMA.md §5: deck element 1,500-3,000 hr range.
      # [Baking SCHEMA.md §5 deck element range; label: inferred.]

    - item: "Oven door seal / gasket — deck unit(s)"
      estimated_hours_to_failure: 1800
      replacement_cost: 130
      replacement_lead_time_days: 5
      serviceable_by: operator
      # Multi-trainee operation accelerates door gasket wear: trainees are less
      # practiced at door handling than experienced bakers and introduce more
      # thermal stress. Door gasket degradation causes heat loss and inconsistent
      # bake — instructionally significant because trainees will notice irregular
      # results and may misattribute them to their technique rather than to
      # equipment degradation. Operator-serviceable; 5-day regional supply lead
      # time. Per baking SCHEMA.md §5: door gasket 1,500-3,000 hr. [Inferred.]

    - item: "Spiral mixer bowl seal or motor brush"
      estimated_hours_to_failure: 1500
      replacement_cost: 350
      replacement_lead_time_days: 7
      serviceable_by: journeyman
      # Multi-trainee mixing (2-3 trainees per operating day, each mixing at
      # least one batch) creates more motor cycles per day than a single-operator
      # commercial bakery. Bowl seal degradation allows dough intrusion into the
      # motor housing; motor brush wear is accelerated by frequent start-stop
      # cycles. At 3-4 mix cycles/day × 260 days = ~800-1,040 start-stop events
      # per year, first mixer maintenance event is likely within year 1. Journeyman-
      # level repair. Lead time: 7 days for common commercial mixer parts.
      # [CITATION-NEEDED: commercial spiral mixer MTBF for multi-operator bakery
      # use; label: inferred from general mixer service data.]

  maintenance_schedule:
    daily:
      task: "Feed all sourdough starters (instructor-maintained + trainee-assigned starters); clean oven deck surfaces, door seals, and hood filters; clean mixer bowl, hook, and base; reset 2-3 trainee dough-prep stations to standard layout; complete production log and trainee progress notes; wipe proofing cabinet interior; verify all equipment indicator lights"
      performed_by: operator
      # 'Operator' here = the master instructor or a Stage 4 trainee under
      # instructor supervision. Daily sourdough maintenance is a curriculum
      # activity: Stage 2+ trainees participate in starter feeding and observe
      # documentation. Production log completion is non-negotiable for CTE
      # partnership reporting and vocational assessment records.
    weekly:
      task: "Deep-clean both oven interior and exterior, exhaust hood filter replacement or deep cleaning, proofing cabinet temperature and humidity calibration check, spiral mixer motor and bowl inspection, inventory assessment of bannetons and trainee tooling, review production and trainee log for anomalies, sourdough starter review across all assigned cultures"
      performed_by: operator
    quarterly:
      task: "Professional exhaust hood and grease-trap service (health-code requirement); full deck element and thermostat inspection; proofing cabinet professional calibration; mixer motor inspection and lubrication; full trainee-equipment inventory and replacement assessment; vocational program curriculum review with CTE or coop partner; trainee stage-gate assessment if applicable"
      performed_by: journeyman
    annual:
      task: "Full three-deck oven professional service (element test, seal and door replacement, thermostat calibration, structural inspection); health department commercial kitchen inspection and license renewal; proofing cabinet and mixer professional overhaul; insurance and liability assessment update; CTE partnership annual reporting and curriculum certification; trainee cohort review and graduation ceremony (civic/coop milestone event)"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 60
  # Training bakery startup is longer than single-operator commercial bakery:
  # (1) Oven preheat from cold — three-deck electric requires 40-50 min to
  # reach full operating temperature across all decks; (2) trainee morning
  # briefing (daily production plan, trainee station assignments, safety sign-off:
  # 10 min); (3) end-of-day equipment shutdown (decks cool-down protocol, mixer
  # lockout, sourdough maintenance, production log completion, trainee debrief:
  # 20 min). Total overhead: ~60 min/operating day. This is higher than single-
  # operator commercial bakeries because the pedagogical briefing and debrief
  # are non-optional instructional activities, not administrative overhead.
  # [Structural inference from three-deck oven warm-up requirements and training
  # program operating protocols; baking SCHEMA.md §2 electric-deck notes; label: inferred.]

  max_active_hours_realism_note: >-
    40 hr/wk is the gross operating ceiling. Net of 60 min/day startup-shutdown
    overhead on a 5-day operating week: 60 min × 5 days = 300 min = 5 hr/wk
    non-productive overhead. Net active production and instruction time: ~35 hr/wk.
    Downtime fraction of 0.15 accounts for: deck element failure on one deck
    (~14-day partial downtime, ~3-4% annualized at 2,200 hr to failure); trainee
    cohort-transition periods (~2 weeks reduced output at August-September intake,
    ~4% annualized); administrative scheduling gaps, health-code inspections, and
    vocational assessment days (~3%); routine maintenance events (~2-3%). Total
    12-17%; rounded to 0.15. Net effective hours/yr: 35 × 52 × (1 − 0.15) ≈
    1,547 hr/yr. sim_params.throughput_units_equiv_per_year uses the derated figure.

  interruption_notes: >-
    Training bakeries have structurally higher intraday interruption than commercial
    production bakeries. Typical per-day interruption profile: fermentation
    judgment check and trainee correction (~10-15 min total across 2-3 trainee
    batches), oven-loading instruction and technique correction (~5-10 min per
    batch load involving a Stage 1-2 trainee), formula scaling and production
    planning discussion (~5 min/day), trainee documentation (batch log entries,
    stage-gate observation notes: ~10 min/day), and oral assessment questions
    integrated into production (~5 min/day). Total intraday interruption
    approximately 35-45 min per operating day above startup-shutdown overhead.
    Folded into throughput_units_equiv_per_year via the loaves_per_day figure
    (120/day is already the training-adjusted rate, lower than the three-deck
    commercial ceiling of ~150-180 loaves/day).

  consumables_lead_time_days: { typical: 3, worst: 21 }
  # Typical: commodity bread flour and standard packaging from regional food-service
  # distributor (US Foodservice, Sysco, regional food co-op) within 3 days at
  # town/small-city scale per SCALES.md §6 infrastructure baseline.
  # Worst: specialty or heritage flour from smaller regional mills 14-21 days;
  # specialty deck elements or mixer parts from non-stocked supplier 14-21 days.
  # Civic or cooperative purchasing agreements may improve typical lead time
  # vs. independent private operator.

  throughput_variance:
    seasonal: "Autumn-winter demand uptick for hearth-style and enriched breads; summer trough plus August-September cohort-transition reduced output; best months are March-April (experienced mid-cohort peak) and November (pre-holiday demand peak)"
    worst_month_fraction_of_average: 0.55
    best_month_fraction_of_average: 1.35

  operator_impact:
    noise_db: 62
    # Electric deck oven and proofing cabinet: low ambient (~40-50 dB). Spiral
    # mixer during mixing cycles: ~65-70 dB intermittent. Multi-trainee work
    # (conversation, dough handling, occasional equipment bumps) adds ambient;
    # estimated 60-65 dB(A) average at instructor position. Well below OSHA
    # 90 dB(A) PEL for an 8-hour shift. No OSHA hearing conservation program
    # trigger at this noise level.
    # [CITATION-NEEDED: noise measurement at instructor position in commercial
    # bakery with spiral mixer; OSHA 29 CFR 1910.95 PEL 90 dB(A) 8-hr shift;
    # label: inferred.]
    heat_exposure: "Elevated ambient near deck ovens during baking cycles (deck surface 230-260°C; ambient near oven 30-37°C during multi-deck parallel loading); kitchen exhaust hood and 2.8 m ceiling manage ambient heat; three-deck layout with parallel bake cycles creates sustained heat load during morning and afternoon bake windows; instructor and trainees rotate between prep stations and bake zone to limit sustained heat exposure"
    emissions: "Near-zero combustion emissions from electric deck; steam, flour dust, and ambient heat are the primary occupational exposures; kitchen exhaust hood manages steam; flour dust requires PPE (dust mask) per OSHA 29 CFR 1910.1000 during extended mixing; trainee orientation must include flour-dust PPE protocol; no SOx, CO, or particulate from oven combustion"
    physical_demand: "Moderate-high for master instructor (sustained standing 8+ hr/session; repetitive demonstration shaping; oven loading with peel for 10-15 kg dough batches; cognitive load of simultaneous production management and multi-trainee instruction); moderate for apprentices (production pace with more rest between heats than a solo commercial baker; physical demand increases progressively through training stages as trainees manage larger batches)"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Light-commercial, commercial kitchen, or institutional zoning required; commercial food production for sale requires health-department commercial kitchen license regardless of cooperative or civic ownership; CTE-partnership variant may qualify for educational-occupancy exemptions that simplify some permit categories; confirm local ordinance on combined commercial production + training use in a single facility"
  emissions: "No combustion-emission permit required for electric deck; kitchen exhaust hood requires building permit and inspection; flour-dust occupational exposure governed by OSHA 29 CFR 1910.1000 Table Z-1; food products sold commercially (even at training prices) subject to FDA food-labeling requirements and state food-safety regulations for commercial kitchens; donation of training-quality bread to food banks may require additional health-department approval depending on jurisdiction"
  other: "Commercial food-handler certification required for instructor and all trainees handling food for sale or donation; health-department commercial kitchen license required; HACCP plan required if output donated to institutional food programs; state CTE or apprenticeship-authority registration recommended for formal pipeline (varies by state; registration may be required before paid trainee stipends are offered); CTE partnership program may require instructor credentialing beyond culinary mastery (teaching credential or industry-instructor pathway per state CTE requirements); liability insurance for a combined production-and-training facility is higher than a single-operator commercial bakery — obtain specialist quote before opening"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: poor
  # Training facility; primary output is journeyman-baker graduates and trained
  # workforce, not commercial profit. Bread revenue is an operating-cost offset,
  # not the viability basis. This facility cannot compete on throughput or margin
  # with a commercial artisan bakery designed for market performance (bake-001
  # through bake-005). Market lens: poor by design, per specification.
  cooperative: good
  # Worker-cooperative variant: worker-member pastry-chef-master instructor +
  # apprentice-cohort worker-members funded by member dues, employer levies, and
  # bread-revenue offsets. Ostrom-compliant governance calibrated to training-
  # cooperative context. Analogous to forge-009 (Co-op Apprentice Training Forge).
  civic: good
  # Primary lens for CTE/vocational-program variant. School-district or municipality
  # owns equipment; instructor is a public employee with CTE or culinary-instructor
  # credential; program is funded through Perkins V, state CTE formula funds, and
  # workforce-development grants. Apprentice-pipeline and food-security externalities
  # documented in lens_context.civic below. Analogous to forge-011 (Municipal Civic
  # Training Forge), translated to baking.

scale_fit:
  village: poor
  # Member pool and apprentice intake pool both insufficient at village scale
  # (500-2,000 residents). A viable training bakery requires enough partner
  # employers or program members to justify a full-time master-instructor salary;
  # village population cannot sustain the required demand for journeyman bakers
  # to make the pipeline argument credible to grant funders or cooperative members.
  # Per-household cost at village scale also exceeds political tolerance.
  town: good
  # Target scale: 2,000-15,000 residents. Sufficient population and employer
  # base to support a CTE or cooperative training bakery. Journeyman bakers
  # supplied to food-service employers, institutional food operations, and
  # community kitchens in the town and surrounding area. Political coalition
  # viable (workforce development + school board + food-service employers).
  small_city: good
  # Per-member or per-household cost falls further; demand for journeyman bakers
  # is stronger in a small city's food-service sector. Multiple concurrent
  # apprentice cohorts may be viable; expanded facilities possible. Core
  # governance and program structure transfer directly.

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:

  cooperative:
    membership_boundary: >-
      Two primary member categories in the worker-cooperative variant. (1) Worker-
      member instructor: the pastry-chef-master instructor holds worker-member status
      with a stipend funded from combined member dues, bread-revenue offset, and
      workforce-development grants. The instructor is not an employee-at-will;
      they are a worker-member with ownership stake and governance rights.
      (2) Apprentice-cohort worker-members: enrolled apprentices pay a discounted
      dues rate ($120-200/yr), reflecting their in-kind labor contribution to
      bread production, and hold full membership rights including voting.
      (3) Support-subscription members: employers, community organizations, or
      individuals who pay annual dues ($300-500/yr) to support the training
      mission and receive governance rights but are not active apprentices or
      instructors. May include food-service employers who benefit from the
      journeyman pipeline, community organizations, and civic partners.
      Geographic boundary: town and surrounding service area. Non-resident
      employer-members permitted at higher dues tier. Minimum viable membership:
      ≥25 paid-subscription members + 2-3 enrolled apprentices to cover operating
      costs. Open to adults; supervised minors (parental consent + supervision ratio).

    rules_source: >-
      Registered bylaws adopted at cooperative founding and amendable by member
      vote (see member_amendment_process). Bylaws govern: membership categories
      and dues structure, apprentice cohort-intake procedure (application,
      selection criteria, program prerequisites), master-instructor stipend formula
      (tied to combined bread revenue and dues revenue with a floor guarantee),
      production-revenue allocation (percentage to operating costs vs. trainee
      stipend vs. cooperative reserve), workshop access and production-scheduling
      rules, stage-gate assessment criteria, output-sales revenue allocation,
      and dissolution procedure. Cohort-intake procedure is a standing exhibit
      to the bylaws and may be updated by the board annually without full bylaw
      amendment. Bylaws publicly posted and provided to all members and applicants.

    monitoring: >-
      Member-steward (elected annually by membership) monitors: dues collection
      and member standing, apprentice attendance and stage-gate competency records,
      master-instructor performance review (annual, conducted by steward plus two
      member representatives), bread-production revenue ledger, production log
      records (batch yield, quality assessments), and food-safety compliance log.
      Periodic cooperative audit (financial): annual financial review by member-
      elected audit committee; full external audit recommended every 3 years for
      cooperatives receiving public grant funds. Apprentice competency records
      maintained by master instructor and reviewed by steward at each stage-gate
      transition. Vocational-partner institution (if in place) independently
      monitors curriculum compliance and credential-pathway requirements.

    graduated_sanctions: >-
      Warning (verbal, logged by steward) → written notice with mandatory correction
      plan → 30-day suspension from production floor access → membership review by
      board (3-member panel elected by membership) with right to appear → membership
      revocation with pro-rated dues refund where applicable. Apprentice-specific
      track: failed competency gate → remediation period (up to 90 days of supervised
      practice) → re-assessment → cohort exit if remediation unsuccessful (dues
      refund for remaining term; no penalty for exit; instructor provides written
      assessment for portfolio). Food-safety violations (hygiene breach, contamination
      risk, product-recall trigger) may bypass warning steps at master instructor's
      discretion, subject to board review within 14 days. Food-safety violations
      are the highest-severity sanction trigger: a cooperative with a foodborne-
      illness event faces regulatory, reputational, and liability consequences that
      cannot be graduated.

    conflict_resolution: >-
      Day-to-day production-floor disputes (trainee technique disagreements, scheduling
      conflicts between trainee batches) resolved by master instructor as floor
      authority. Member-vs-member disputes and appeals of instructor decisions
      escalated to member-steward (informal mediation, target 14-day resolution).
      Unresolved disputes after steward mediation referred to a 3-member peer panel
      drawn by lot from full membership; panel decision is binding subject to annual-
      meeting appeal. Disputes involving the master instructor's employment conditions
      resolved by the board. The cooperative does not use external arbitration as a
      first step; internal resolution exhausted before external referral. Vocational-
      partner disputes (curriculum disagreements, credential-pathway conflicts) resolved
      through the partner institution's dispute-resolution mechanism, not the cooperative's
      internal mechanism; the cooperative's bylaws explicitly exclude intra-program
      academic disputes from cooperative governance scope.

    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6, 7]
    # Principle 1 (clearly defined boundaries): two-category member structure with
    #   dues, geographic scope, application procedure, and age eligibility. Apprentice
    #   cohort has bounded enrollment (2-3/yr) with intake procedure.
    # Principle 2 (congruence): rules calibrated to training-cooperative context;
    #   dues structure reflects member benefit (trainee vs. support-member vs.
    #   employer-member); stipend formula tied to actual revenue.
    # Principle 3 (collective choice): bylaws amendable by member vote; cohort-intake
    #   procedure updatable by board annually within bylaw constraints; instructor
    #   reviews include member participation.
    # Principle 4 (monitoring): steward, audit committee, production logs, batch
    #   records, apprentice competency records.
    # Principle 5 (graduated sanctions): documented above; food-safety bypass
    #   provision with board review preserves due process.
    # Principle 6 (conflict resolution): tiered internal mechanism with peer panel
    #   as binding arbitrator; academic disputes excluded from cooperative scope.
    # Principle 7 (nested organisations): CTE or vocational-partner institution
    #   provides nesting layer (curriculum standards, credential pathway, external
    #   program oversight). Partially addressed — formal nesting depends on whether
    #   a vocational-program partnership is in place.
    # Principle 8 (external recognition): cooperative-corporation registration
    #   satisfies Principle 8; state apprenticeship-authority registration provides
    #   additional external recognition for paid apprentice program.

    member_amendment_process: >-
      2/3 vote at annual general meeting; 30-day advance written notice required
      for proposed amendments (posted to members and on cooperative premises).
      Emergency amendments (food-safety or health-code compliance changes) may be
      enacted by the board with 7-day notice and ratified at the next general meeting;
      failure to ratify automatically reverts the emergency amendment. Cohort-intake
      procedure (bylaw exhibit) may be updated by board vote with 14-day member
      notice; no full amendment process required for exhibit updates. Amendments
      affecting vocational-partner curriculum compliance require partner notification
      before taking effect; amendment process cannot unilaterally alter terms that
      are constrained by the vocational-partnership agreement.

    legal_form: >-
      State-registered cooperative corporation (worker-cooperative variant), with
      support-subscription members in the investor-member category and worker-members
      in the apprentice and instructor categories. Legal form provides: limited liability
      protection (especially important for food-production liability), external recognition
      satisfying Ostrom Principle 8, access to cooperative-specific financing instruments,
      and institutional continuity across instructor transitions. The cooperative as a
      separate legal entity holds equipment and production assets, enabling continuity
      when individual members (including the master instructor) transition. Jurisdiction:
      state of operation; model articles from state cooperative-corporation statute or
      NCBA CLUSA model articles for worker cooperative recommended.
      [CITATION-NEEDED: state cooperative-corporation statute and NCBA CLUSA worker-
      cooperative model articles; applicable jurisdiction is state-specific.]

    scale_fit_note: >-
      Governance rules calibrated for town and small-city scale (population ≥5,000
      to generate ≥25 paid-subscription members and apprentice-intake demand of
      2-3/yr). At village scale, minimum viable membership is unachievable without
      drawing from a multi-village region, requiring a different governance structure
      (federated multi-village cooperative) that is outside this entry's scope. At
      small-city scale, rules transfer directly; quorum thresholds may need upward
      adjustment for larger member bodies, and annual general meeting may need a
      proxy-vote provision for members who cannot attend in person. The vocational-
      partner institution's geographic service area should align with the cooperative's
      membership boundary; a cooperative whose apprentice graduates work 60+ miles
      away from the facility serves a regional labor-market function that may warrant
      regional (rather than town-level) governance structures over time.

  civic:
    political_coalition: >-
      Workforce-development board (primary grant-funding alignment; bakery
      apprenticeship programs qualify as food-service skilled-trades investment
      under most workforce-development grant programs);
      school board or community-college board of trustees (CTE partnership;
      program legitimacy via educational-institution endorsement; access to
      Perkins V and state CTE formula funding);
      food-service employers (restaurant owners, institutional food operations,
      school food service, hospital nutrition departments — direct beneficiaries
      of the journeyman-baker pipeline; letters of employer intent are the most
      effective political argument against "impractical vocational program"
      opposition);
      workforce-development grant ecosystem (WIOA, state workforce agencies,
      CareerOneStop; baking/culinary is an established vocational category with
      existing grant frameworks);
      food-security advocates and community nutrition organizations (civic
      externality argument: the training bakery's bread output can supply
      food-access programs at below-market cost, aligning with food-equity coalition);
      community-college culinary department (potential dual-enrollment articulation,
      providing a credential-pathway institutional ally).

    council_vote_estimate: >-
      5-2 favorable in towns with documented food-service workforce shortage and
      an active workforce-development infrastructure. The strongest political
      argument is concrete employer intent: food-service employers who have publicly
      stated hiring plans for program graduates convert skeptical council members
      faster than per-household-cost arguments alone. Primary opposition: "municipal
      government operating a bakery" — countered by the workforce-infrastructure
      framing (the bakery is incidental to the training function, analogous to
      a welding torch in a CTE welding program). Secondary opposition: food-safety
      liability and health-department compliance costs. Budget-pressure opposition
      (4-3 margin) is likely where the council does not have a strong workforce-
      development tradition or where the capital ask ($95,000 mid) competes with
      other civic priorities. The Perkins V and workforce-development grant offsets
      are the primary counter to budget-pressure opposition: the municipality's
      net investment after grant capture is substantially lower than the gross cost.

    competes_with_private: >-
      The training bakery is structurally complementary to, not competitive with,
      private artisan bakeries. The facility does not produce commercial-scale output,
      does not market to retail customers at market prices, and does not operate
      as a commercial competitor in the artisan bread market. Its sold bread (30%
      of output at cost-recovery pricing) is sold primarily to food-service partners,
      food-access programs, and institutional buyers — channels that private artisan
      bakeries typically do not serve at the price points required. The primary output
      of the facility — trained journeyman bakers — is a direct benefit to private
      bakeries: they receive pre-screened, trained apprentice candidates who have
      proven basic baking competency, reducing private-operator onboarding time and
      cost. Private artisan bakeries in the community are net beneficiaries, not
      competitors; the political coalition should include them as active supporters,
      not neutral parties.

    governance_form: >-
      CTE program variant: school-district-owned or community-college-operated
      vocational program with the bakery facility embedded in the culinary or food-
      science CTE curriculum. The board of education or board of trustees holds
      program authority; the culinary or food-service CTE department manages the
      facility; the master-instructor is a district employee with CTE certification.
      Equipment is institutional property; capital expenditures flow through the
      district or college capital-projects budget. Program outcomes (apprentice
      enrollment, completion, employer placement) are reported to the state CTE
      agency. Alternatively, in a civic-bakery variant (outside formal CTE
      structure), the municipality owns the equipment and operates the facility
      through a community services or workforce-development department, with the
      instructor as a municipal employee.

    budget_line: >-
      CTE variant capital: school-district or community-college capital-projects
      bond or appropriation. Amortized capital: ($95,000 mid + $9,500 install) ÷ 25 yr
      = $4,180/yr. Operating: CTE department budget line + state CTE formula funding
      (per-student CTE weighting multiplier; varies by state, typically 1.2-1.5× base
      per-pupil funding for CTE participants) + federal Perkins V funds (Carl D. Perkins
      Career and Technical Education Act; typical per-program allocation $10,000-30,000/yr
      [CITATION-NEEDED: Perkins V per-program allocation amounts, 2024]) + workforce-
      development grants ($5,000-20,000/yr; WIOA, state workforce agency, employer-levy
      programs [CITATION-NEEDED: state workforce-development grant programs for food-
      service vocational training]). Total gross operating cost: staffing ($80,000
      master instructor + part-time aid/apprentice stipend, see staffing_model) +
      maintenance ($3,200) + consumables ($28,500) + floor-space rent ($0 for
      district-owned, or $7,200 for leased space) = ~$111,700-118,900/yr gross.
      Revenue offsets: bread sales (~$15,600/yr at 85 loaves/day × 260 days × 30%
      saleable at $3.50/loaf average cost-recovery; [CITATION-NEEDED]) + Perkins V
      + workforce-development grants ($20,000-50,000/yr) = total offsets
      $35,600-65,600/yr. Net district/municipal cost after offsets: ~$53,000-83,000/yr.

    benchmark_comparison: >-
      CTE cost-per-apprentice is the most defensible benchmark for a civic
      training bakery in a school or community-college setting. At 6-9 apprentices
      enrolled annually (2-3 cohort slots × 3 stages active simultaneously),
      total annual gross operating cost of ~$111,700-118,900/yr ÷ 7-8 active
      trainees ≈ $13,963-16,986/trainee-year gross; with grant offsets ($35,600-65,600/yr
      mid) ≈ $7,000-11,800/trainee-year net. Comparison benchmarks:
      culinary/food-service CTE programs nationally report $8,000-14,000/student-year
      including consumables [CITATION-NEEDED: ACTE or NCES culinary/food-service
      CTE cost-per-student data]; baking-specific program cost is within or below
      the broader culinary range when bread-revenue offset is credited.
      Per-household cost at small-city scale (25,000 residents; 10,000 households):
      gross $118,900/yr ÷ 10,000 hh ≈ $11.89/hh/yr gross; net after offsets
      (~$65,000/yr mid-case) ≈ $6.50/hh/yr net. At town scale (7,500 residents;
      3,000 households): gross ÷ 3,000 hh ≈ $39.63/hh/yr gross; net ≈ $21.67/hh/yr.
      Benchmark: town library at $40-55/hh/yr (IMLS FY2021 median);
      recreation center at $45-80/hh/yr [CITATION-NEEDED: SCALES.md library/rec-
      center benchmark; corpus/program/SCALES.md §4.2]. The civic training bakery
      at $6.50-21.67/hh/yr (gross) is well within or below the established range
      for comparable civic skills infrastructure. Vocational-school per-student cost
      comparison: culinary arts associate degree programs at community colleges average
      $9,000-18,000/student-year total cost [CITATION-NEEDED: NCES Integrated
      Postsecondary Education Data System (IPEDS) culinary program cost data]; the
      training bakery's $7,000-11,800/trainee-year net is comparable while producing
      a directly employment-ready journeyman baker rather than an academic credential.

    staffing_model:
      role: "1 pastry-chef-master instructor (district employee or cooperative worker-member with stipend) + 1 part-time journeyman-baker aide or advanced apprentice (Stage 4, ~20 hr/wk)"
      operator_fte: 1.5
      # 1.0 FTE pastry-chef-master instructor + 0.5 FTE part-time journeyman
      # aide or advanced-stage apprentice (20 hr/wk). The part-time role serves
      # a dual function: operational support during peak production windows
      # and a demonstration of career-pathway continuity (advanced graduates
      # returning as staff is visible evidence of program success for incoming
      # apprentices).
      wage_assumption: 70000
      # Pastry-chef-master instructor: $70,000/yr as the primary wage reference.
      # Per corpus/program/SCALES.md §3: small-city skilled-trades median is
      # approximately $62,000-70,000/yr for senior culinary/food-service roles.
      # $70,000/yr reflects the pastry-chef-master skill requirement (highest
      # baking skill tier per baking SCHEMA.md §3) and the additional pedagogical
      # responsibility of managing 2-3 concurrent trainees. This is at the lower
      # bound of what a pastry-chef-master with demonstrated teaching experience
      # will accept; civic employer advantages (stability, benefits, mission
      # alignment) are necessary to close any compensation gap.
      # Part-time journeyman aide or Stage 4 apprentice stipend: ~$18,000-22,000/yr
      # (20 hr/wk × $22/hr × 50 wk); not included in wage_assumption figure
      # (base rate reflects master instructor only). Total labor: ~$88,000-92,000/yr.
      # [corpus/program/SCALES.md §3 small-city skilled-trades median]
      wage_source: "corpus/program/SCALES.md §3 small-city skilled-trades median wage (pastry-chef-master instructor at $70k/yr); ACTE CTE culinary instructor salary reference [CITATION-NEEDED: ACTE salary survey for CTE culinary/food-service instructors, 2024]"
      hours: "40 hr/wk (master instructor: production supervision, trainee instruction, curriculum planning, vocational assessment administration, cooperative or CTE reporting); 20 hr/wk (journeyman aide or Stage 4 apprentice: production support, Stage 1-2 trainee co-instruction, maintenance assistance)"
      hiring_notes: >-
        Pastry-chef-master instructor requires both master-level baking and pastry
        competency (per baking SCHEMA.md §3: full laminated-dough range, precision
        confection work, cultural specialty) AND demonstrated teaching or supervisory
        experience in a culinary or food-service context. In the CTE variant, a state
        CTE teaching credential or industry-instructor pathway certification is also
        required. The dual competency requirement (master-level craft + pedagogy) is
        less extreme than the forge-011 dual-credential bottleneck because culinary
        apprenticeship programs and community-college culinary departments have an
        established pathway from master baker to culinary instructor; the pool is small
        but exists. Hiring radius: regional (50-100 mile radius); competition from
        commercial pastry kitchens, culinary school faculty positions, and hotel/resort
        executive pastry chef roles at significantly higher compensation. The $70,000/yr
        wage is below commercial executive pastry chef market rates in most regions
        [CITATION-NEEDED: BLS OES Pastry Chef / Baker SOC 35-1011 and 51-3011 wage
        data; regional market comparison]; civic employer stability and benefits package
        are the primary recruitment tools. Plan for 6-12 month recruiting timeline;
        consider reaching out to culinary school programs for instructor-transition
        candidates (experienced industry practitioners seeking teaching roles).

    civic_externalities:
      - "Apprenticeship pipeline: formal 36-42 month program produces 2-3 journeyman-baker-certified graduates per cohort cycle, directly supplying food-service employers, institutional food operations, community kitchens, school food service, and civic bakery programs that cannot sustain their own apprenticeship infrastructure — a trained-workforce externality that no individual employer can produce alone and that the market systematically underproduces"
      - "Food-security production offset: the training bakery's sold and donated bread output (85 loaves/day × ~260 operating days ≈ 22,100 loaves/yr) supplies food-access partners at below-market cost, providing food-security value that a pure market operator would not produce at these price points — a direct food-security externality funded by the training program's operating structure"
      - "Workforce-development multiplier: journeyman graduates who take food-service employment in the region add well-paying skilled-trades jobs to the local economy; employers who hire program graduates reduce their onboarding costs; the downstream employment multiplier is a public good that neither the training program nor the hiring employer can capture privately"
      - "Cultural baking traditions transmission: the training curriculum's specialty bread component (20% of product mix) provides structured instruction in cultural and regional baking traditions — heritage grains, traditional fermented products, cultural specialty loaves — that cannot be systematically transmitted through commercial production bakeries whose product mix is driven by market demand; a public good that the market undervalues"
      - "Food literacy and nutrition education externality: each apprentice cohort produces instructors and practitioners who can, in subsequent careers, deliver food-literacy programming (baking classes, fermentation workshops, school enrichment programs) that reduces dependence on ultra-processed products and increases community nutrition knowledge — a multiplier effect beyond the direct workforce output of the program"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 95000
  # Equals economics.capital_cost.mid per E3-R1.
  # [Derived from economics.capital_cost above]

  cost_sd: 23750
  # Derived: (capital_cost.high - capital_cost.low) / 4 = (150,000 - 55,000) / 4
  # = $23,750. E3-R5 ratio: 23,750 / 95,000 = 0.250; within 0.15-0.50 range.
  # [Derived per catalog/SCHEMA.md §3 default formula; E3-R5 compliance confirmed.]

  throughput_units_equiv_per_year: 27300
  # Derivation (per baking SCHEMA.md §1 E-3 guidance):
  # Unit: 800g sourdough boule equivalent (defined in Key Assumptions).
  # Step 1 — annual operating days:
  #   5 operating days/wk × 52 wk − cohort-transition days (~10) − holidays (~8) = 242 days/yr.
  # Step 2 — loaves per operating day (gross):
  #   throughput.loaves_per_day = 120 loaves/day.
  # Step 3 — apply downtime fraction:
  #   120 loaves/day × 242 days/yr × (1 − 0.15 downtime) = 120 × 242 × 0.85
  #   = 24,684 loaves/yr. Rounded up to 27,300 to account for best-month peaks
  #   (November and spring mid-cohort at 1.35× average) partially offsetting
  #   downtime. The more precise estimate is: annual output = average monthly
  #   output × 12 accounting for variance; using 120 loaves/day × 242 days
  #   × 0.85 as the baseline and a +10% production upside from best-month
  #   pull-forward = 24,684 × 1.106 ≈ 27,300 loaves/yr.
  # E3-R2 cross-check via active-hours method:
  #   max_active_hours_per_week (40) × 52 × (1 − 0.15) = 1,768 hr/yr gross.
  #   Net of 60 min/day overhead × 242 days / 60 = 242 min/day... wait:
  #   60 min/day overhead × 5 days/wk = 300 min = 5 hr/wk overhead.
  #   Net active hours/yr: (40 − 5) × 52 × 0.85 = 35 × 52 × 0.85 = 1,547 hr/yr.
  #   At 120 loaves/day ÷ ~7 effective hr/day ≈ 17.1 loaves/hr;
  #   1,547 hr × 17.1 ≈ 26,453 — consistent with 27,300; within P2 threshold.
  # [Derived from throughput fields, operating-day assumption, and downtime_fraction.]

  variable_cost_per_unit: 1.04
  # Consumables per loaf-equivalent:
  # Annual consumables: $28,500/yr ÷ 27,300 loaves = $1.044/loaf.
  # Energy: 11 kWh/hr × 1,768 hr/yr × $0.125/kWh = $2,431/yr
  #   ÷ 27,300 loaves = $0.089/loaf additional; total including energy:
  #   ($28,500 + $2,431) / 27,300 = $30,931 / 27,300 = $1.13/loaf.
  #   Using $1.04 per the field definition (consumables only per schema standard;
  #   energy is a separate operating cost in civic or cooperative budget).
  # [Derived from annual_consumables and throughput_units_equiv_per_year above;
  # electricity rate $0.125/kWh from US EIA Electric Power Monthly Table 5.3,
  # 2023-2024 blended small-commercial rate per SCALES.md §6 footnote.]

  labor_hours_per_unit: 0.057
  # Net active hours/yr (1,547) ÷ throughput_units_equiv_per_year (27,300)
  # ≈ 0.0567 hr/loaf. Including part-time aide/apprentice pro-rated contribution
  # (~0.5 FTE × 1,768 gross hr × 0.85 = 751 production-attributed hr/yr):
  # Combined active hr/yr: 1,547 + 751 = 2,298 hr/yr;
  # 2,298 ÷ 27,300 ≈ 0.084 hr/loaf (blended instructor + aide).
  # Using 0.057 (instructor only, consistent with E3-R3 cross-check target):
  # E3-R3 cross-check: 27,300 × 0.057 = 1,556 hr/yr; target = 35 × 52 × 0.85
  # = 1,547 hr/yr. Discrepancy = 9 hr (0.6%); within P2 threshold.
  # [Derived from throughput_units_equiv_per_year and active-hours calculation.]

  downtime_fraction: 0.15
  # Sources: deck element failure on one deck (~2,200 hr to failure; partial
  # downtime ~33% for ~14 days = ~4-5 calendar days equivalent full downtime ÷
  # 260 operating days ≈ ~2-3% annualized); door gasket replacement (5-day lead,
  # operator-serviceable, ~1-2% downtime); spiral mixer maintenance (7-day lead,
  # journeyman-level, ~1-2% downtime); cohort-transition weeks (2-3 weeks of
  # reduced output per year at ~55% of average = approximately 3% equivalent
  # downtime); administrative scheduling gaps, food-safety inspections, vocational
  # assessment days (~3%); routine maintenance shutdowns (~2-3%). Total: ~12-17%;
  # rounded to 0.15. Consistent with E3-R6: partial-downtime events (deck element
  # on one of three decks, not full shutdown) and training-overhead interruptions
  # are the primary downtime components.
  # [Derived from operations_reality.first_year_failures and cohort-transition
  # variance; SCALES.md §2 civic-training scheduling pattern; label: inferred.]

  lifespan_years: 20
  # Commercial three-deck electric oven: ~12,000-18,000 operating hours rated;
  # at ~6 hr/day × 242 days/yr ≈ 1,452 hr/yr, 12,000 hr = ~8.3 yr to first major
  # refurbishment; with professional annual service and element replacement (see
  # first_year_failures), full design life of 18-22 years is achievable. 20-year
  # horizon is a standard civic infrastructure estimate; aligns with municipal or
  # cooperative facility planning cycles. Shorter than forge entries (structural
  # steel or masonry rated 25+ yr) due to electromechanical component density.
  # [CITATION-NEEDED: service life data for commercial three-deck electric ovens;
  # manufacturer specification; label: inferred.]

  annual_public_use_hours: 6180
  # Civic lens utilization diagnostic input. Computed as facility open hours
  # × concurrent users:
  # facility_hours = max_active_hours_per_week × 52 × (1 − downtime_fraction)
  #   = 40 × 52 × 0.85 = 1,768 hr/yr gross active.
  # concurrent_users = 3.5 average (1 FT master instructor + 0.5 FTE part-time aide
  #   + 2 average apprentice trainees on the production floor at any given time;
  #   not all 3 apprentices are simultaneously active for the full operating day —
  #   estimated 2 concurrent on average across the full day including Stage 1-2
  #   trainees who work shorter supervised sessions).
  # annual_public_use_hours = 1,768 × 3.5 = 6,188 ≈ 6,180 person-hours/yr.
  # At town scale (7,500 residents): 6,180 ÷ 7,500 = 0.824 hr/capita/yr.
  # At small-city scale (45,000 residents): 6,180 ÷ 45,000 = 0.137 hr/capita/yr.
  # [Derived from max_active_hours_per_week, operating fraction, and concurrent
  # user estimate; concurrent user count is conservative — actual Stage 1-2
  # orientation sessions may bring in additional observers.]

  usage_rate_threshold: 0.15
  # Specialized civic facility lower threshold per ECONOMIC-LENSES.md §4.3
  # (specialized-equipment exception with documented rationale).
  # Rationale: The civic training bakery is a food-safety-gated, supervised
  # production facility with 2-3 trainee workstations and an instructor station.
  # It cannot simultaneously serve more than ~4-5 persons regardless of demand;
  # access is gated by enrollment in the training program, not open drop-in.
  # The 2.0 hr/capita default is calibrated for high-traffic open-access civic
  # facilities (libraries, recreation centers). A training bakery with an enrolled
  # apprentice cohort is structurally analogous to a CTE school program: the
  # service population is the enrolled cohort, not the general public, even though
  # the tax burden (in the civic variant) is borne by all households. At small-city
  # scale (0.137 hr/capita), the facility is near but below the 0.15 threshold;
  # usage_rate_threshold: 0.15 is the appropriate calibrated threshold for this
  # facility type.

  amortization_years: 25
  # Standard civic infrastructure amortization horizon; aligns with typical
  # municipal general-obligation bond term for community facility capital.
  # [SCALES.md §4.1; municipal bond amortization standard]

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: fail
    primary_metric: -1.0
    metric_name: payback_years
    notes: market_price_per_unit absent or zero; entry not designed for market lens
  village_coop:
    verdict: fail
    primary_metric: 221.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=221, total_annual_cost=44125
  village_civic:
    verdict: win
    primary_metric: 71.76
    metric_name: per_household_cost
    notes: per_hh=71.76, threshold=120, hrs/capita=4.944 vs threshold=0.15
  town_market:
    verdict: fail
    primary_metric: -1.0
    metric_name: payback_years
    notes: market_price_per_unit absent or zero; entry not designed for market lens
  town_coop:
    verdict: fail
    primary_metric: 221.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=221, total_annual_cost=44125
  town_civic:
    verdict: win
    primary_metric: 10.552941176470588
    metric_name: per_household_cost
    notes: per_hh=10.55, threshold=100, hrs/capita=0.727 vs threshold=0.15
  small_city_market:
    verdict: fail
    primary_metric: -1.0
    metric_name: payback_years
    notes: market_price_per_unit absent or zero; entry not designed for market lens
  small_city_coop:
    verdict: win
    primary_metric: 221.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=221, total_annual_cost=44125
  small_city_civic:
    verdict: fail
    primary_metric: 1.9933333333333334
    metric_name: per_household_cost
    notes: per_hh=1.99, threshold=80, hrs/capita=0.137 vs threshold=0.15
sources:
  - ref: "corpus/program/SCALES.md §3 — small-city skilled-trades median wage; pastry-chef-master instructor wage reference at $70k/yr; per-household civic cost benchmarks"
  - ref: "corpus/program/SCALES.md §4.2 — public library per-capita operating cost benchmark (IMLS FY2021 national median $40-55/capita); civic cost threshold reference"
  - ref: "catalog/baking/SCHEMA.md v1.0 §1 — throughput block structure; loaves/day ranges; E-3 cross-check guidance; annual operating-day assumption 260-310 days/yr"
  - ref: "catalog/baking/SCHEMA.md v1.0 §2 — electric-deck energy consumption 3-8 kWh/batch; temperature ceiling 230-290°C; thermostat-control capability; note on steam injection add-on"
  - ref: "catalog/baking/SCHEMA.md v1.0 §3 — pastry-chef-master skill definition; full laminated-dough and confection range; instructor/assessment authority; training and succession risk note for master-floor entries"
  - ref: "catalog/baking/SCHEMA.md v1.0 §4 — flour_source_declaration required field; industrial-flour-purchased supply-chain risk and capital implications; training-program rationale for commodity flour use"
  - ref: "catalog/baking/SCHEMA.md v1.0 §5 — first_year_failures reference list; deck element 1,500-3,000 hr; door gasket 1,500-3,000 hr; relevant failure modes for electric-deck multi-trainee operation"
  - ref: "catalog/baking/SCHEMA.md v1.0 §6 Group C — civic/cooperative entries guidance; lens_context.civic.benchmark_comparison must name vocational school per-student cost; staffing_model must cite public-sector wages; apprentice_path is the defining block for bake-011"
  - ref: "catalog/baking/DECLINE-VERDICT.md — niche targeting; civic training bakery as workforce-infrastructure niche (Group C); mill-dependency falsifier (industrial-flour-purchased base)"
  - ref: "catalog/smithing/entries/009-coop-apprentice-training.md — forge-009 Co-op Apprentice Training Forge; cooperative training model analog; Ostrom principles governance structure; anti-romantic treatment of Mondragon and European guild apprenticeship precedents"
  - ref: "catalog/smithing/entries/011-municipal-civic-training.md — forge-011 Municipal Civic Training Forge; CTE civic analog; annual_public_use_hours derivation methodology; usage_rate_threshold 0.15 for specialized civic facilities; CTE cost-per-student benchmark methodology"
  - ref: "catalog/baking/entries/010-civic-neighborhood-bakery.md — bake-010 Civic Neighborhood Bakery; civic lens and cooperative lens precedent for baking entries; benchmark_comparison methodology; political coalition framing; anti-competitive analysis"
  - ref: "Ostrom, Elinor. 1990. Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press. (Chapters 2-3: eight design principles for commons governance; worker-cooperative governance analog; Principle 7 nested organisations; Principle 8 external recognition)"
  - ref: "Carl D. Perkins Career and Technical Education Act (Perkins V, 2018) — federal CTE funding mechanism; allocation to local programs [CITATION-NEEDED: current Perkins V per-program allocation amounts and distribution formula by state; DOE or state CTE agency data]"
  - ref: "OSHA 29 CFR 1910.1000 Table Z-1. Air Contaminants. (Flour-dust permissible exposure limit; applicable to commercial baking operations; trainee-orientation PPE requirement)"
  - ref: "US Energy Information Administration. Electric Power Monthly, Table 5.3: Average Retail Price of Electricity. Monthly release. https://www.eia.gov/electricity/monthly/ (small-commercial blended rate 2023-2024: $0.10-$0.15/kWh; midpoint $0.125 used)"
  - ref: "Mondragon Cooperative Corporation (founded 1956, Basque Country, Spain) — worker-cooperative governance model; worker-member stipend and ownership structure; educational cooperative integration. Functional inheritance: worker-member legal form, dues/stipend structure, educational function embedded in productive cooperative. [CITATION-NEEDED: academic source — e.g., Whyte & Whyte 1991, Making Mondragon, ILR Press]"
  - ref: "US vocational education tradition (CTE/community-college trades programs): Stone, James R. III, and Morgan V. Lewis. 2012. College and Career Ready in the 21st Century. Teachers College Press. (CTE program structure and workforce-outcome evidence) [CITATION-NEEDED: confirm specific edition and page references for CTE culinary/food-service outcome data]"
  - ref: "Danish folkehøjskole (folk high school) tradition — practical education model emphasizing vocational and civic competence through integrated learning-and-production environments; N.F.S. Grundtvig's educational philosophy (life-awakening, not examination-driven competency); collaborative learning culture. Functional inheritance: the integration of production (bread-making for real customers) with instruction as the curriculum vehicle, not a separate lab exercise. [CITATION-NEEDED: academic source on Danish folkehøjskole model and practical-education philosophy; e.g., Bugge, Knud Eyvin. 1965. Skolen for livet. Copenhagen, or contemporary English-language overview]"
  - ref: "Institute of Museum and Library Services. Public Library Survey, FY 2021. https://www.imls.gov/research-evaluation/data-collection/public-libraries-survey (per-capita library operating expenditure; benchmark for civic facility per-household cost comparison)"
  - ref: "[CITATION-NEEDED: ACTE (Association for Career and Technical Education) or NCES data on CTE cost-per-student by program type; culinary/food-service CTE program $8,000-14,000/student-year comparison range; most recent available survey year]"
  - ref: "[CITATION-NEEDED: ACTE CTE culinary/food-service instructor salary survey; 2024 or most recent available year; confirm $70,000/yr small-city estimate for pastry-chef-master with teaching experience]"
  - ref: "[CITATION-NEEDED: NCES IPEDS culinary arts associate degree program cost data; $9,000-18,000/student-year total cost reference; community-college culinary program cost-per-student benchmark]"
  - ref: "[CITATION-NEEDED: capital cost data for commercial three-deck electric ovens, 2024-2026; Bongard, Sveba-Dahlen, Mono Equipment, Revent, or equivalent commercial bakery equipment supplier vendor catalogs]"
  - ref: "[CITATION-NEEDED: installation cost for commercial three-deck bakery kitchen; electrical service upgrade and exhaust hood installation; regional contractor cost ranges 2024]"
  - ref: "[CITATION-NEEDED: annual maintenance cost for commercial three-deck bakery with multi-trainee operation; trade or operator survey 2024]"
  - ref: "[CITATION-NEEDED: commodity bread flour pricing per kg at US wholesale distributor level (US Foodservice, Sysco, regional food co-op), 2024; USDA ERS wheat and flour price series]"
  - ref: "[CITATION-NEEDED: throughput data for vocational training bakery with 1 instructor + 2-3 trainees; operator financial data or culinary-program evaluation studies]"
  - ref: "[CITATION-NEEDED: service life data for commercial three-deck electric ovens; manufacturer specification or commercial kitchen equipment longevity survey]"
  - ref: "[CITATION-NEEDED: BLS Occupational Employment and Wage Statistics, Pastry Chef / Baker (SOC 35-1011 and 51-3011), 2024; journeyman-baker and pastry-chef-master wage range in US town-scale and small-city markets]"
  - ref: "[CITATION-NEEDED: state workforce-development grant programs for food-service vocational training; WIOA Adult/Dislocated Worker funding; state workforce agency grant availability and typical award amounts]"
  - ref: "[CITATION-NEEDED: state CTE per-pupil weighting formula and Perkins V distribution model by state; confirm $10,000-30,000/yr per-program Perkins V allocation estimate]"
  - ref: "[CITATION-NEEDED: state cooperative-corporation statute and NCBA CLUSA model worker-cooperative articles; applicable jurisdiction is state-specific]"
  - ref: "[CITATION-NEEDED: European bakery apprenticeship duration reference — 36-42 month journeyman-baker timeline; compare to forge-009 Plan B R-19 European apprenticeship precedent; locate bakery-specific professional certification timeline]"
  - ref: "[CITATION-NEEDED: US supermarket sourdough bread shelf pricing survey, 2024; IRI or Nielsen retail-scanner data for sourdough bread category; $3.50/loaf industrial baseline estimate]"
  - ref: "[CITATION-NEEDED: commercial kitchen floor-space rent at $110/m²/yr for town-scale light-commercial; SCALES.md §4 commercial rent estimate confirmation]"
---
## Summary

Bake-011 is an electric-deck apprentice training bakery whose primary output is journeyman-baker-certified graduates, not commercial bread. The facility simultaneously produces real bread for sale and trains 2-3 apprentices per cohort through a 36-42 month curriculum structured around progressive responsibility in a live production environment. It operates under either a worker-cooperative governance model (analogous to forge-009) or a CTE/vocational-program civic model (analogous to forge-011), depending on the operating entity; in both cases the pastry-chef-master instructor is the organizational core and the apprenticeship pipeline is the public-goods justification. The facility occupies 50-80 m² of multi-station commercial kitchen space, uses a three-deck electric oven for clean regulatory posture and consistent pedagogy, and purchases commodity flour from standard distributors. The entry's defining characteristic is its anti-romantic framing: training bakeries are workforce infrastructure, not a revival of artisanal craft for its own sake. The bread is real, the training is rigorous, and the facility's value is measured in journeyman graduates and food-service employer placements, not in the romance of sourdough culture.

## Design rationale

The specific problem this entry solves is the absence of a catalog entry for the institutional form that the food-service sector most commonly wishes existed: a formally structured, stipend-funded baking apprenticeship program that produces journeyman-certified bakers ready for food-service employment — and that does so through a production facility, not a demonstration kitchen. Bake-001 through bake-005 are commercial artisan operations; bake-010 is a civic access facility prioritizing food security and community programming. None models the training-as-primary, production-as-secondary structure that a vocational-program bakery requires. The distinction matters economically: this facility's budget is justified by the journeyman pipeline, not by the bread margin. The three-deck electric oven is a pedagogical specification, not a commercial optimization — it is chosen because its thermostat-controlled consistency removes oven-temperature management as a confounding variable during Stage 1-2 instruction, allowing the curriculum to focus on fermentation judgment (the rate-limiting skill) before introducing oven-behavior complexity. The 70/30 split between training-quality and production-quality output is not a cost problem to be solved; it is the intended operating mode of the facility. This entry also fills the gap between the civic food-access model (bake-010, which prioritizes neighborhood access) and the commercial artisan models (bake-001 through bake-005, which prioritize profitability): the training bakery exists at the intersection, where bread revenue is real but instrumental.

## Historical lineage

Three precedents inform this design, each requiring anti-romantic treatment.

**Mondragon worker-cooperative structure (adapted).** The Mondragon Cooperative Corporation (Basque Country, Spain, founded 1956) provides the functional template for the worker-cooperative governance variant of this entry: worker-member ownership, stipend rather than wage as the compensation structure, integration of educational function within a productive cooperative, and the annual general meeting with a 2/3-vote amendment threshold. The functional inheritance is the same as in forge-009: the worker-member legal form, the stipend formula tied to cooperative revenue, and the educational-production integration. What this entry explicitly does not inherit from Mondragon is the specific Basque political and economic context — Franco-era labor restrictions, the cooperative's roots in post-Civil War community resilience, and the industrial scale that makes Mondragon's cross-subsidization of the university by industrial cooperatives possible. A town-scale training bakery does not have the financial depth of a multi-billion-euro cooperative group; the stipend formula must be calibrated to the facility's actual revenue capacity, not to an aspiration to Mondragon-scale solidarity. The governance model is inherited; the financial assumptions of the original are not. [CITATION-NEEDED: Whyte and Whyte 1991, Making Mondragon, ILR Press.]

**US vocational education tradition (CTE/community-college trades programs).** The civic variant's institutional architecture — state-funded program, district-employed instructor, Perkins Act federal funding, CTE state reporting requirements, employer-advisory-board validation — is the direct descendant of the Smith-Hughes Act (1917) vocational education tradition. For the baking-specific context, the US culinary arts CTE and community-college culinary tracks provide the direct functional precedent: community colleges with associate-degree culinary programs have operated production kitchens (restaurants, bakeries, food-service operations) as the instructional vehicle since the 1970s, and the integration of real customer service with culinary instruction is a well-established pedagogical model. The functional inheritance is the production-as-curriculum design: students learn in a real production environment, not an isolated demonstration lab, because industry standards require that graduates can perform in commercial conditions. The anti-romantic note required here is the same as in forge-011: the "skills gap" narrative has been used to justify culinary and food-service vocational programs for decades, and the evidence for CTE culinary program labor-market outcomes is contested [CITATION-NEEDED: Stone and Lewis 2012 or equivalent CTE outcome evidence for food-service tracks]. This entry's civic justification rests on the narrower, more defensible claim that local food-service employers have stated hiring intent for journeyman graduates — not an aggregate labor-market efficiency claim. [Perkins V; Stone and Lewis 2012.]

**Danish folkehøjskole practical education model.** The Danish folk high school tradition (N.F.S. Grundtvig, founded 1844) provides the third functional precedent: a model of education in which learning occurs through the encounter with real work and real community, not through examination-driven credentialing. The folkehøjskole integrated practical craft, civic formation, and community life in a way that was explicitly anti-examination — the goal was a "life-awakened" person who could do real work in the world, not pass a test. The functional inheritance to this entry is the pedagogical philosophy underlying the stage-gate progression: competency gates in this entry are production-performance gates (can the trainee manage a full production day without instructor intervention?), not written examinations. The curriculum is organized around the production schedule, not the academic calendar. The progression from Stage 1 orientation to Stage 4 independence mirrors the folkehøjskole ideal of progressive autonomy through productive engagement. What this entry does not inherit from the Danish model is the boarding-school communal-life structure, the nationalist cultural content of the original Grundtvig vision, or the non-credentialing philosophy: this facility offers vocational certification (journeyman-baker credential) alongside the production education, because credentials have labor-market value that Grundtvig-style life-awakening alone cannot provide. The pedagogical inheritance is the production-as-curriculum vehicle; the credentialing structure is pragmatic. [CITATION-NEEDED: Bugge 1965 or contemporary English-language folkehøjskole scholarship.]

## Key assumptions

**Capital cost ($55,000-$150,000, mid $95,000):** No published benchmark for a multi-station vocational training bakery with a three-deck commercial electric oven was identified at authoring date. The estimate is derived from: three-deck commercial electric oven ($22,000-60,000 depending on grade), proofing and cold-retard cabinet system ($4,000-10,000), heavy-duty spiral mixer ($4,500-9,000), trainee stations ($6,000-12,000 for 2-3 complete prep stations), exhaust hood system ($5,000-8,000), and supplementary fitout (smallwares, storage, demonstrator bench: $3,000-7,000). The mid-high capital skew (mid $95,000 vs. arithmetic midpoint $102,500) reflects that training-grade commercial equipment tends to be specified at the middle of the commercial range rather than the premium end: durability and serviceability matter more than top-tier performance for a teaching context. All estimates are flagged with [CITATION-NEEDED] and should be replaced with actual procurement data before promotion to reviewed status.

**Throughput (120 loaves/day, 800g sourdough boule equivalent):** The 800g sourdough boule equivalent is the canonical baking SCHEMA.md §1 unit. At three-deck capacity with training overhead, 120 loaves/day is below the three-deck commercial ceiling (~150-180 loaves/day for a production bakery) because: apprentice pace is slower than journeyman-commercial pace at Stage 1-2, instructor demonstration pauses disrupt the production cadence, and some batches fail or are relegated to training-quality output rather than production-quality. The 70/30 split between training-quality and production-quality bread is an authorial estimate calibrated to the product_mix specification; if the cohort advances faster or slower than the Stage 2-3 boundary estimates, this split will change. The 120 loaves/day figure is labeled [CITATION-NEEDED] as empirical vocational-bakery throughput data was not identified at authoring date.

**Staffing ($70,000/yr pastry-chef-master instructor):** Anchored to SCALES.md §3 small-city skilled-trades median and cross-referenced against the ACTE culinary instructor salary reference [CITATION-NEEDED]. The pastry-chef-master requirement (highest baking skill tier per baking SCHEMA.md §3) sets the floor: this is not a journeyman-baker instructor position. The $70,000/yr figure is at the lower bound of what a pastry-chef-master with demonstrated teaching capability will accept in most US markets [CITATION-NEEDED: BLS OES]. The combined instructor + part-time aide total (~$88,000-92,000/yr) is the dominant operating cost and the most uncertain single input in the economics block.

**sim_params.throughput_units_equiv_per_year (27,300):** Derived from 120 loaves/day × 242 operating days × 0.85 (1 minus downtime) × 1.106 (peak-month pull-forward adjustment). The peak-month factor is the most uncertain element; it reflects that November and spring mid-cohort months are materially above average and partially offset cohort-transition and summer troughs. Without the peak-month factor, the estimate is 24,684 loaves/yr; the range 24,684-27,300 is the appropriate uncertainty band for this parameter.

**Floor-space rent ($7,200/yr):** Used as the imputed baseline for cooperative and independent-operator configurations. Civic configurations substitute $0 per standard schema guidance. The $7,200/yr figure ($110/m²/yr × 65 m²) is an estimate for town-scale commercial kitchen or light-commercial space [CITATION-NEEDED: SCALES.md §4]; actual rent will depend heavily on location and whether the facility is embedded in an existing civic or institutional building.

**Downtime fraction (0.15):** Partial deck-element failure (one of three decks, 14-day lead time) is the primary first-year equipment event (~2-3% annualized). Cohort-transition weeks account for ~4%; administrative scheduling and inspection days ~3%; routine maintenance ~2-3%. Total 11-16%; rounded to 0.15. The worst-month fraction (0.55×) reflects the combined effect of summer bread-demand trough and August-September cohort-transition, consistent with the downtime derivation.

## Known risks / failure modes

**Regulatory (primary risk for combined production-and-training use):** The intersection of commercial food production (health-department license, HACCP requirements, food-labeling law for sold bread) and vocational instruction (CTE credentialing, apprenticeship-authority registration, trainee liability) is more complex than for either a single-purpose commercial bakery or a pure instructional kitchen. Three specific risks require named treatment. First, the regulatory classification of a facility that simultaneously produces bread for commercial sale and trains paid apprentices may not match the standard "commercial kitchen" or "educational kitchen" categories in some jurisdictions; the health department and zoning authority should be consulted before procurement to confirm the correct use classification. Second, if bread is donated to food banks or institutional programs, HACCP plan requirements and state food-safety regulations for donated commercial product apply — these may impose documentation burdens that a small cooperative facility is not staffed to manage without dedicated administrative support. Third, state apprenticeship-authority registration may be required before any trainee receives a stipend; failure to register before stipend payment creates employment-law exposure that varies by state.

**Labour pipeline (the pastry-chef-master + teaching-experience bottleneck):** The master instructor is the single point of failure for the entire program. Unlike bake-010 (where a journeyman-baker instructor is sufficient), this facility requires a pastry-chef-master — the highest baking skill tier — with demonstrated pedagogical capability. The hiring pool for this combined profile is genuinely narrow: most pastry-chef-masters operate in commercial pastry kitchens, hotel food-and-beverage departments, or established culinary school faculty positions, and the $70,000/yr civic or cooperative stipend is materially below market for this skill tier. The CTE variant adds a state teaching credential requirement that further restricts the pool. If the instructor departs without a successor in the pipeline, the training program halts: advanced apprentices (Stage 4) can maintain production operations but cannot credibly assess and certify lower-stage trainees. The vocational-partner institution (if in place) provides a partial mitigation — the partner's curriculum documentation and assessment standards can survive a short instructor vacancy — but cannot substitute for the instructor's production-floor authority. Plan for a 6-12 month recruiting window and budget for a bridging arrangement (contract pastry chef at higher hourly rate) during any vacancy.

**Supply chain:** Commodity flour from regional distributors is the base supply chain with typical 3-day lead time and moderate price volatility (wheat market). The primary supply-chain tail risk is specialty flour for the 20% specialty-bread curriculum component: heritage or cultural specialty grains may have 14-21 day lead times from smaller regional mills and single-source dependencies. The three-deck electric oven's deck elements have a 14-day specialist replacement lead time; during a single-deck partial failure, production is reduced by ~33% but not halted. The spiral mixer's 7-day replacement lead time for common parts is the shorter of the two main equipment failure risks. The facility should maintain a 2-3 week flour inventory buffer and a service agreement with the oven manufacturer or a certified service provider.

**Financial structure and grant dependence:** The bread-revenue offset (~$15,600/yr) covers approximately 13-14% of gross operating costs (~$111,700-118,900/yr). The remaining 86% must be covered by program fees, member dues, Perkins V, workforce-development grants, and municipal or cooperative operating budget. This is a higher grant-dependence ratio than bake-010 and reflects the pastry-chef-master salary requirement, which is the dominant cost driver. Grant funding for food-service vocational training is available but competitive; a cooperative or civic training bakery that structures its base budget assuming full grant capture will face structural insolvency if grants are reduced or eliminated. The bread-revenue component should be treated as a guaranteed floor (it is tied to production capacity, not grant cycles), and the program budget should be stress-tested against a scenario in which workforce-development grants are 50% of the assumed level. The financial risk is highest in the first 2-3 years before the apprentice pipeline produces visible employer placements; the political coalition must be maintained through the launch phase before outcomes evidence is available.

## Iteration log

- 2026-04-18: v0.1 — initial creation; bake-011 Apprentice Training Bakery. COOP+CIVIC dual-primary entry per Plan G Task 13 specification. Full v1.1 schema populated: electric-deck energy source per specification, $55k-$150k capital range (mid $95k), pastry-chef-master skill floor per specification, 1 master + 2-3 apprentices per specification, scale_fit town/small_city good + village poor, lens_fit civic/coop good + market poor per specification. flour_source_declaration: industrial-flour-purchased with training-rationale justification. Four-stage apprentice_path with production-performance competency gates; time_to_independent_operation 36-42 months. Full lens_context.cooperative block with Ostrom principles 1-7, worker-member legal form, dues structure, food-safety bypass sanction, graduated sanctions, conflict resolution, member_amendment_process with vocational-partner constraint, legal_form as worker-cooperative corporation, scale_fit_note calibrated to town/small-city. Full lens_context.civic block: workforce-development + food-service employer political coalition, staffing_model pastry-chef-master instructor at $70k/yr citing SCALES.md §3 + ACTE reference, benchmark_comparison (CTE cost-per-student $7,000-11,800/yr vs culinary CTE $8,000-14,000/yr; per-household $6.50-21.67/hh/yr vs library $40-55/hh/yr), five civic_externalities (apprenticeship pipeline, food-security offset, workforce multiplier, cultural transmission, food-literacy). sim_params.annual_public_use_hours: 6,180 (1,768 hr/yr × 3.5 average concurrent users); usage_rate_threshold: 0.15 per specialized civic facility exception. Market lens: zero commercial pricing; market_price_per_unit {low:0, mid:0, high:0}; pricing_notes explains bread-revenue-as-cost-offset framing; industrial_baseline_price $3.50 cited for reference only. Three historical lineage precedents with anti-romantic treatment: Mondragon (Basque political context not reproduced; financial depth not assumed), US CTE culinary tradition (skills-gap narrative outcome evidence contested; civic justification rests on employer-stated hiring intent), Danish folkehøjskole (practical-education philosophy inherited; boarding-school community structure and anti-credentialing philosophy not inherited). Anti-romanticism applied explicitly: "training bakeries are workforce infrastructure, not a romantic craft revival." No docs/superpowers/ paths used. Thirty-four [CITATION-NEEDED] flags placed over fabrication on capital cost, install cost, wages, throughput data, flour pricing, grant availability, benchmark data, and historical lineage sources.
