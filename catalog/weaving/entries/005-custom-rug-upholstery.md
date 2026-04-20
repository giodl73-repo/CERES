---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: weave-005
trade: weaving
name: "Custom Rug & Upholstery Studio"
tagline: "Journeyman-operated town-scale studio producing custom area rugs and upholstery fabric for interior designers and homeowners"
status: draft
version: "0.1"
supersedes: null
inspirations:
  - american-colonial-rag-rug-tradition
  - scandinavian-rya-flatweave-studio
  - modern-us-custom-rug-atelier

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 55
# Mid-point of the 40–70 m² range: accommodates 2–3 frame looms (rug construction,
# varying widths), one floor loom for upholstery fabric, a cutting and finishing
# bench, yarn and material storage, and a small customer-consultation area for
# sample display. Rug looms require horizontal working space; frame looms can be
# wall-mounted or freestanding. 55 m² is sufficient for a 1–2 operator studio at
# town scale with customer access. Low end (40 m²) suits a solo operator with minimal
# display space; high end (70 m²) allows a second floor loom and larger rug frames.
# [REQUIREMENTS weaving: floor area range for mixed loom studio; illustrative mid-point.]

ceiling_min_m: 2.8
# Rug frame looms and upright loom frames for large rugs may reach 2.2–2.5 m;
# 2.8 m provides clearance for tall frames and overhead lighting without requiring
# industrial ceiling height. No combustion-gas clearance concern; this is a lower
# ceiling requirement than most smithing entries.
# [Structural inference from loom frame heights; catalog/weaving/SCHEMA.md §3.]

ventilation: natural-sufficient
# Electric-lighting-only studio with no combustion processes. Lint and fiber dust
# are the primary air-quality concern; natural ventilation (windows + exhaust fan)
# is sufficient for a small studio with 1–2 operators. No OSHA extraction permit
# anticipated for handweaving-scale fiber dust. Mechanical extraction recommended
# (not required) if the studio processes large volumes of synthetic fiber (acrylic,
# polyester cut strips) where particulate density may increase.
# [catalog/weaving/SCHEMA.md §2 electric-lighting-only; OSHA 29 CFR 1910.94 not
# triggered at handloom fiber-dust levels.]

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: electric-lighting-only
# All looms are hand/treadle-operated; no powered weaving mechanisms. Energy use
# is entirely lighting (studio + task lighting over loom frames, warp boards,
# and finishing bench) and small auxiliary tools (electric yarn winder, bobbin
# winder). No climate control required (humidity_control_required: false for the
# fiber types used in this entry).
# [catalog/weaving/SCHEMA.md §2 electric-lighting-only.]

energy_consumption_per_active_hour: "2 kWh/day (studio lighting + auxiliary)"
# Lighting for a 55 m² studio: approximately 20 fixtures at 10W LED = 200W; plus
# task lighting over loom positions ~100W; auxiliary tools (winder, etc.) ~50W
# intermittent. At 10 operating hours/day: ~2 kWh/day total. Per-hour active rate
# is below 0.25 kWh/hr, making electricity a negligible operating cost.
# [Derived from standard commercial LED lighting load at 55 m²; illustrative
# estimate consistent with catalog/weaving/SCHEMA.md §2 electric-lighting-only
# range of 1–5 kWh/day.]

backup_fuel: null
# No combustion fuel required or used; no backup fuel applicable.

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  meters_per_day: 1.0
  # Net woven length per full operating day across the studio's mixed product:
  # rag-rug construction (plain weave, frame loom) at 1.5–2.5 m/day for simple
  # patterns; upholstery cloth (twill weave, floor loom) at 2–4 m/day at
  # 100 cm width; custom area rugs with pattern elements at 0.5–1.5 m/day.
  # Weighted average over a typical product mix (60% rug, 40% upholstery cloth):
  # ~1.0–1.5 m/day for a single operator. 1.0 m/day is the conservative estimate
  # used for sim_params; 2.0 m/day represents a high-output day on simpler rug
  # construction. Warping and loom-dressing overhead (4–8 hr per new warp,
  # especially for upholstery twill on the floor loom) reduces net weaving days.
  # [catalog/weaving/SCHEMA.md §1 typical ranges: twill 2–6 m/day floor loom;
  # rug construction varies widely; CITATION-NEEDED: measured daily output for
  # custom rug studio operations; label: inferred.]

  warp_width_cm: 120
  # Primary working width for rug frame looms (common custom rug widths: 90–180 cm;
  # 120 cm covers a standard area-rug width). Floor loom for upholstery cloth:
  # 100–130 cm usable width to produce standard upholstery fabric widths.
  # 120 cm is the stated throughput reference width; actual rug commissions may
  # vary from 60 cm (accent rug) to 240 cm (room-size rug requiring two-loom
  # assembly). sim_params converts to m² using this reference width.
  # [catalog/weaving/SCHEMA.md §3 floor-loom-4shaft 60–150 cm; rug frame loom
  # widths: industry standard; illustrative mid-point.]

  pattern_complexity: plain
  # Rag rugs and flat-weave area rugs: plain weave (tabby), soumak, and simple
  # weft-loop pile — all achievable at the plain complexity tier on frame looms.
  # Upholstery cloth on the floor loom: 2/2 twill (herringbone, twill stripes),
  # which qualifies as twill complexity. The mixed-product studio spans both plain
  # and twill; plain is stated here as the dominant tier by volume (rag rugs are
  # the primary market offering). Upholstery twill is documented in Key Assumptions
  # as the secondary product. Entry does not require master-level pattern complexity.
  # [catalog/weaving/SCHEMA.md §1 pattern_complexity definitions.]

  max_active_hours_per_week: 35
  # Net active loom-hours per week including both rug frame loom work and floor
  # loom operation. Excludes: warping and threading time (4–8 hr/new warp on the
  # floor loom; 1–3 hr/new rug warp on frame looms); customer consultation and
  # sample preparation; finishing work (trimming, washing, blocking rugs; cutting
  # and hemming upholstery yardage). Full-time 1-operator studio: 35 hr/wk at
  # loom is achievable; total shop time including setup and customer-facing work
  # may reach 45–50 hr/wk. Consistent with catalog/weaving/SCHEMA.md §1 realistic
  # ceiling of 30–40 hr/wk at loom for a studio weaver.
  # [catalog/weaving/SCHEMA.md §1 max_active_hours_per_week guidance.]

  product_mix:
    yardage: 0
    rugs_upholstery: 85
    tapestry_art: 0
    garments_accessories: 0
    instruction_open_studio: 15
    # Sum: 100. Rugs and upholstery fabric dominate (85%): custom area rugs
    # for residential and commercial interiors, plus upholstery-weight fabric
    # sold to interior designers by the meter. Instruction (15%): one-day or
    # weekend rug-weaving workshops are a practical secondary revenue stream
    # that uses existing frame looms without additional capital; instruction
    # also builds the local customer pipeline for rug commissions.
    # [catalog/weaving/SCHEMA.md §1 product_mix; instruction_open_studio as
    # secondary revenue for market-primary entries.]

  throughput_variance:
    worst_month_fraction_of_average: 0.65
    # Interior-design commissions are relatively non-seasonal, but the slowest
    # months (typically January–February post-holiday, and August vacation period)
    # may reduce order intake to 60–70% of average. Custom rug commissions are
    # project-based and lumpy; a month with no new commission starts produces
    # near-zero throughput unless a backlog exists.
    # [Structural inference from commission-based revenue lumpiness; catalog/
    # weaving/SCHEMA.md §1 commission/market entries typical range 0.60–0.80.]
    best_month_fraction_of_average: 1.40
    # Fall interior-design installation season (Sept–Nov) and pre-holiday
    # residential purchasing peak (Oct–Dec) drive above-average commissions.
    # Custom rugs are a considered purchase with 4–12 week lead time; orders
    # placed in Oct–Nov for holiday installation drive the best-month peak.
    # [Structural inference from interior-design seasonal demand pattern;
    # catalog/weaving/SCHEMA.md §1 holiday-peak guidance.]
    seasonal: "Commission work is year-round; fall/early-winter peak for residential interior-design installation orders; January–February and August are typical slow periods."

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: journeyman-weaver
# Rug construction on frame looms (plain weave, soumak, rya pile) requires
# journeyman-level competency: ability to set up and dress a frame loom, manage
# warp tension independently, execute plain-weave and pile techniques consistently,
# and produce customer-facing quality without supervision. Upholstery twill on
# the floor loom requires floor-loom threading, tie-up, and 4-shaft treadling
# skill. Neither product requires master-level tapestry or drawloom work.
# Rug weaving is more accessible than tapestry (per entry parameters: "rugs are
# more accessible than tapestry") and thus has a lower skill floor than weave-001
# or weave-003; however, a rigid-heddle-novice cannot produce customer-grade
# custom rugs. Journeyman is the correct floor for production-quality output.
# [catalog/weaving/SCHEMA.md §5 journeyman-weaver definition and equipment scope.]

operators_concurrent: "1-2"
# Base operation: one journeyman weaver operates rug and upholstery looms in
# rotation. Second operator (apprentice or skilled helper) assists with warping,
# rug finishing (washing, trimming, backing), and customer sample preparation.
# A second concurrent operator on a separate loom is feasible and increases
# throughput; the studio is designed for 1–2 independent production positions.
# [Entry parameters: 1–2 operators.]

apprentice_friendly: true
apprentice_path:
  training_stages: >
    Stage 1 (0–3 months): studio safety, loom mechanics, winding a warp,
    dressing a rag-rug frame loom, plain-weave technique on a sample warp.
    Gate criterion: winds a warp independently, dresses a frame loom to
    correct tension, and weaves a 30 cm sample at consistent sett without
    supervision.

    Stage 2 (3–9 months): rug construction — plain-weave area rugs with
    straight edges and consistent density; introduction to soumak and weft-loop
    pile on frame looms; rug finishing (washing, blocking, trimming). Gate
    criterion: completes one full customer-size rug (minimum 90 × 120 cm)
    to accepted quality standard.

    Stage 3 (9–18 months): floor-loom operation for upholstery cloth —
    threading a 4-shaft loom for twill, tie-up and treadling, producing
    consistent yardage to width specification; introduction to yarn
    substitution and fiber selection for upholstery durability requirements.
    Gate criterion: threads and dresses the floor loom independently, weaves
    2 meters of upholstery twill to specification.

    Stage 4 (18–30 months): customer consultation assistance — taking
    commission briefs, presenting sample cards, estimating yardage requirements,
    quotation support; independent rug commission production including patterned
    flat-weave; introduction to rug restoration technique (rewinding and
    reweaving worn areas). Gate criterion: manages a full rug commission from
    brief to delivery independently.
  time_to_independent_operation: "~24–30 months to journeyman standard on this studio's equipment; rug construction reaches independent production quality by Stage 3 (~18 months); upholstery cloth competency follows"
  succession_note: >
    Apprentice co-presence during Stages 2–4 is integrated into normal
    production: warping assistance and rug-finishing work during Stage 2,
    floor-loom operation alongside the primary weaver during Stage 3.
    The instruction_open_studio product-mix allocation (15%) creates a natural
    teaching venue that doubles as customer-acquisition for commissions.
    The 24–30 month progression is shorter than tapestry or architectural
    weaving (weave-001, weave-003) because rug-construction techniques are
    more accessible, reducing succession-cliff risk.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 20000, mid: 42000, high: 70000 }
  # Low ($20,000): 2–3 small frame looms ($800–$1,500 each), one entry-level
  # 4-shaft floor loom ($1,500–$3,000), basic warping board and accessories
  # ($500), cutting and finishing bench ($400–$800), lighting and electrical
  # fit-out ($2,000–$4,000), yarn and material inventory startup ($3,000–$5,000),
  # display/consultation setup ($1,000–$2,000). Suitable for a solo operator in
  # an already-fitted commercial or studio space.
  # Mid ($42,000): 2 purpose-built rug frame looms with adjustable tensioning
  # ($3,000–$5,000 each), one quality 4-shaft floor loom for upholstery cloth
  # ($3,000–$5,000), warping mill, bobbin winder, and loom accessories ($2,000),
  # cutting table and finishing equipment ($1,500–$2,500), customer sample
  # display and consultation area ($2,000–$3,000), lighting and fit-out
  # ($4,000–$6,000), starting yarn inventory ($6,000–$8,000), signage ($500).
  # High ($70,000): three professional-grade rug looms (including a wide-format
  # frame for room-size commissions), floor loom with 4-shaft and potential
  # 8-shaft capacity, professional finishing equipment (industrial washing
  # capability, steam blocking), full display studio with sample library,
  # comprehensive fiber inventory for immediate-availability quotes.
  # [CITATION-NEEDED: capital cost data for rug frame looms and 4-shaft floor
  # looms in the 2024–2026 market; label: illustrative estimate. Vendor
  # references: Schacht Spindle, Leclerc, Gilmore Looms, Ashford (frame looms
  # and floor looms); pricing inferred from general loom market knowledge.]

  install_cost: 3500
  # Standard commercial electrical permit for lighting upgrade (~$1,500–$2,500);
  # floor reinforcement assessment and minor structural work for large rug-loom
  # frames if required (~$500–$1,000); signage and exterior installation (~$500).
  # Low install cost reflects the absence of combustion systems, specialized
  # ventilation, or heavy mechanical equipment. 3-phase power is not required.
  # [Illustrative estimate; CITATION-NEEDED: commercial studio fit-out costs for
  # light-duty textile studio in town-scale commercial space; label: inferred.]

  annual_maintenance: 1200
  # Loom maintenance: reed replacement or repair (~$150/yr), heddle replacement
  # on floor loom (~$100/yr), treadle cord and tie-up replacement (~$80/yr),
  # frame loom component repair (~$100/yr), warping board and accessory
  # maintenance (~$70/yr). General studio maintenance (lighting, fixtures,
  # display upkeep): ~$300/yr. Rug washing/blocking equipment maintenance: ~$200/yr.
  # Excludes first-year failure replacements itemized in operations_reality.
  # [Illustrative estimate derived from weaving equipment maintenance literature;
  # CITATION-NEEDED: annual maintenance cost data for production rug/upholstery
  # weaving studio; label: inferred.]

  annual_consumables: 9500
  # Primary consumables — fiber inputs:
  # Rugmaking wool (commercial/industrial wool rug yarn): ~$3,500–$4,500/yr
  # Cotton rag strips and cotton warp yarn: ~$1,500–$2,000/yr
  # Upcycled fabric strips (T-shirt yarn, denim strips): ~$500–$800/yr
  # Upholstery-weight cotton and linen warp/weft yarn: ~$1,500–$2,000/yr
  # Secondary consumables: threading hooks, shuttle wear parts, rug backing
  # material, washing supplies, blocking pins (~$300/yr), sample card
  # materials (~$200/yr), packaging and shipping (~$400/yr).
  # Total: ~$8,000–$10,500/yr; $9,500 mid-point.
  # Electricity (negligible at ~2 kWh/day × 240 days × $0.125/kWh ≈ $60/yr)
  # is included in variable_cost_per_unit at negligible level.
  # [Illustrative estimate; CITATION-NEEDED: fiber procurement cost data for
  # production rug and upholstery weaving studios; wool yarn pricing from
  # commercial rug-yarn suppliers (Webs, Halcyon Yarn, Paradise Fibers); label: inferred.]

  floor_space_rent_per_year: 6600
  # Imputed at ~$120/m² per year for commercial studio space in a town-scale
  # market (2,000–15,000 residents). 55 m² × $120/m²/yr = $6,600/yr.
  # Town-scale commercial rents in secondary US markets are lower than small-city
  # rates; $120/m²/yr reflects a realistic midpoint for light-commercial
  # studio/retail space in a small town with artisan-economy identity or existing
  # maker community. Owner-operator in owned space: imputed at the same rate for
  # cost-comparison consistency across the evaluation matrix.
  # [Illustrative estimate; CITATION-NEEDED: commercial studio rent per m² in
  # town-scale US markets, 2024; CoStar or local broker data preferred; label: inferred.
  # Compare to forge-006 $180/m²/yr for small-city light-industrial; rug studio
  # in town context uses lower rate appropriate to scale.]

  market_price_per_unit: { low: 80, mid: 180, high: 450 }
  # Unit = 1 m² of finished custom rug or upholstery fabric.
  # Low ($80/m²): basic rag rug, simple flat-weave or plain-weave area rug;
  #   direct-to-homeowner or craft-market pricing for a standard accent rug.
  # Mid ($180/m²): custom area rug with color specification and basic pattern
  #   (stripes, simple geometric); interior-designer commission at standard
  #   custom-work rates; consistent with mid-range custom rug pricing in US
  #   handcraft market.
  # High ($450/m²): premium custom rug with complex patterning (kilim-style
  #   geometric, hand-knotted pile technique), specialty fiber (natural wool,
  #   organic cotton), or commercial interior installation specification (high
  #   durability, specific colorway, delivery guarantee); interior-designer
  #   B2B channel at premium rates.
  # Upholstery fabric pricing: $80–$200/m at 120 cm width = $67–$167/m²;
  #   this falls within the low–mid range stated above. Blended across rug
  #   and upholstery, $180/m² mid represents a realistic weighted average.
  # Industrial baseline: $25/m² (commodity machine-made area rug at mass-market
  #   retail — see industrial_baseline_price).
  # [CITATION-NEEDED: empirical custom-rug and handwoven upholstery fabric pricing
  # from US studio weavers and interior-design trade channels, 2024–2026;
  # label: pricing_validation: inferred. Sources consulted for orientation:
  # Houzz custom-rug marketplace, Etsy handwoven rug listings, interior-design
  # trade publications (Architectural Digest, Elle Decor trade resources).]

  pricing_notes: >
    Unit is 1 m² of finished custom-woven rug or upholstery fabric. Premium
    over the industrial baseline ($25/m² for a mass-market machine-made area
    rug at big-box retail — e.g., a standard 8×10 ft polypropylene rug at
    $200 retail ÷ ~7.4 m² = $27/m²) reflects: (1) custom colorway and
    pattern not available in the mass market, (2) natural-fiber material
    choice (wool, cotton) that durability-sensitive and health-conscious buyers
    prefer, (3) B2B interior-designer channel requiring specification-grade
    consistency and delivery reliability, and (4) rug restoration services
    (reweaving worn areas) that extend rug lifespan without replacement.
    The $80–$450/m² range targets homeowners with renovation budgets, interior
    designers specifying custom furnishing textiles for residential and commercial
    projects, and buyers who explicitly reject commodity rug manufacturing.
    Factory alternatives ($25–$60/m² for machine-made polypropylene or basic
    wool rugs) do not replicate custom dimensions, specified colorways, or the
    restorable durability of hand-woven natural-fiber construction.
    [CITATION-NEEDED: industrial rug pricing at US retail 2024; label: inferred.]

  pricing_validation: >
    Pricing evidence: inferred from orientation-level review of US custom-rug
    market pricing via Houzz, Etsy, and interior-design trade channel resources
    (2024–2026). NOT derived from a formal industry pricing survey, published
    rate-card study, or audited studio-weaver financial statements. This is a
    placeholder-inferred figure consistent with the project's citation policy for
    uncertified market-price claims. Recommended verification: direct survey of
    operating custom-rug studios with documented commission pricing and sales
    data, or a trade association pricing study (e.g., Handweavers Guild of
    America, American Craft Council market pricing data). The $80–$450/m² spread
    reflects reasonable bounds for the hand-woven custom-rug segment but has not
    been confirmed against willingness-to-pay research. Label: pricing_validation: inferred.

  industrial_baseline_price: 25
  # Mass-market machine-made area rug (polypropylene or low-grade wool blend,
  # standard sizes, no custom options) at US big-box or online retail, 2024.
  # $25/m² ≈ a standard 8×10 ft rug at $200 retail ÷ ~7.4 m². Machine-woven
  # mid-range alternatives ($50–$80/m²) are noted in pricing_notes as a secondary
  # comparison. The $25 figure represents the commodity substitute available to a
  # cost-only buyer who does not require custom dimensions or natural-fiber
  # construction.
  # [CITATION-NEEDED: mass-market area rug pricing at US retail 2024; e.g.,
  # Home Depot, Wayfair, Target standard rug price per m²; label: inferred from
  # general market knowledge.]

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Floor-loom reed (bent dents from warping or handling)"
      estimated_hours_to_failure: 1500
      replacement_cost: 120
      replacement_lead_time_days: 7
      serviceable_by: operator
      # Reed dents bend or break from dropped objects, excess beating force,
      # or improper storage of the 4-shaft floor loom reed. A bent dent creates
      # a streak in upholstery cloth. Operator-diagnosis and replacement; lead
      # time 3–14 days for a replacement reed to specification. $120 is a
      # typical replacement cost for a floor-loom reed at standard sett.
      # [catalog/weaving/SCHEMA.md §7 reed damage reference; CITATION-NEEDED:
      # reed replacement cost and lead time data; label: inferred.]

    - item: "Warp beam ratchet / pawl wear (floor loom)"
      estimated_hours_to_failure: 2000
      replacement_cost: 85
      replacement_lead_time_days: 10
      serviceable_by: journeyman
      # Ratchet-and-pawl beam tensioning system on the 4-shaft floor loom wears
      # under continuous use; slippage causes warp-tension loss mid-weave in
      # upholstery yardage, producing density inconsistency. Journeyman-level
      # replacement of ratchet pawl and spring; 10-day lead time for parts from
      # loom manufacturer or aftermarket supplier.
      # [catalog/weaving/SCHEMA.md §7 warp beam ratchet reference; CITATION-NEEDED:
      # ratchet/pawl wear data for production floor-loom operation; label: inferred.]

    - item: "Rug frame loom tensioning cord wear or breakage"
      estimated_hours_to_failure: 800
      replacement_cost: 25
      replacement_lead_time_days: 1
      serviceable_by: operator
      # Tensioning cords on rug frame looms (adjustable-tension bar systems)
      # wear and fray from the lateral tension of heavy rug warps (cotton, wool).
      # Operator-replaceable with hardware-store cord; 1-day lead time with
      # spare stock on hand. $25 covers a full re-cord of a standard frame loom.
      # Low cost, high frequency; should be in routine maintenance inventory.
      # [CITATION-NEEDED: frame loom cord wear data; label: inferred from general
      # knowledge of rug-frame tensioning systems.]

  maintenance_schedule:
    daily:
      task: "Remove fiber lint and cut yarn ends from all loom frames and floor loom; check warp tension on active warps; wipe down finishing bench; record commissions completed and materials used"
      performed_by: operator
    weekly:
      task: "Inspect floor-loom reed and heddles for bent or broken elements; check treadle tie-up cords for fraying; lubricate floor-loom moving parts (pivot points, treadle pivots) per manufacturer schedule; verify rug frame loom tensioning cords and replace if frayed; review fiber inventory against active commission queue"
      performed_by: operator
    quarterly:
      task: "Full floor-loom mechanical inspection: shaft suspension, beater alignment, warp-beam ratchet, brake pad condition; inspect frame loom frame joints and tensioning hardware for wear; replace worn heddles in bulk as preventive maintenance; audit yarn inventory for quality and quantity against forward commission pipeline"
      performed_by: journeyman
    annual:
      task: "Full loom mechanical overhaul: replace all texsolv heddle cords and tie-up cords on floor loom; inspect and re-treat wooden loom components (oil or wax as specified by manufacturer); review reed condition across all standard setts; professional cleaning of studio lighting and ventilation fixtures; capital equipment insurance and valuation review"
      performed_by: journeyman

  startup_shutdown_overhead_per_day_min: 20
  # Startup: check warp tension on active looms, review commission queue and
  # thread count, confirm fiber staging at loom positions (~10 min). Shutdown:
  # secure shuttles and bobbins, cover active warps if dusty environment,
  # record daily production (~10 min). No warm-up time required (no combustion
  # or electrical heating); 20 min/day is a realistic studio-management overhead.
  # [Structural inference from studio weaving operations; illustrative estimate.]

  max_active_hours_realism_note: >
    35 hr/wk is the net active loom-time ceiling after derating for startup-shutdown
    overhead (20 min/day × 5 days = 1.67 hr/wk) and customer-consultation time
    (~30 min/day average). Gross ceiling: ~38 hr/wk theoretical active loom time
    from a 45–50 hr/wk total shop presence. The 35 hr/wk figure does not include
    warping and loom-dressing time (4–8 hr per new floor-loom warp; 1–3 hr per
    rug frame warp), which is accounted for by the 240 operating-days assumption
    in sim_params (allowing approximately 20 non-weaving setup days per 260
    working-day year). sim_params.throughput_units_equiv_per_year uses 240
    effective weaving days as the denominator, which is the derated figure.

  interruption_notes: >
    Typical intraday interruptions: customer consultation walk-ins or scheduled
    appointments (30–60 min each, 2–4/week), sample card preparation for new
    commission inquiries (~20 min/inquiry), supplier calls and fiber ordering
    (~15 min/day). Instruction sessions (15% product mix) are scheduled as
    dedicated blocks and do not interrupt production warps. Commission photography
    for portfolio and social-media sales channel (~15 min/day). Total intraday
    interruption beyond startup-shutdown: ~45–60 min/day, folded into the
    35 hr/wk derated active-loom figure.

  consumables_lead_time_days: { typical: 7, worst: 30 }
  # Typical: rugmaking wool yarn and cotton warp yarn from US textile distributors
  # (Webs, Halcyon Yarn, WEBS) — 5–7 day shipping to most US locations. Worst:
  # specialty natural-fiber rug yarn, heritage wool, or custom dye-lot orders may
  # require 3–4 weeks for dye matching or specialty mill lead time. Upholstery-weight
  # fabric strips sourced from local upholstery suppliers have 1–3 day typical lead.
  # [Illustrative estimate; CITATION-NEEDED: fiber procurement lead-time data for
  # rug and upholstery weaving studios; label: inferred.]

  throughput_variance:
    seasonal: "Commission work is year-round; fall/early-winter peak for residential interior-design installation orders; January–February and August are typical slow periods."
    worst_month_fraction_of_average: 0.65
    best_month_fraction_of_average: 1.40

  operator_impact:
    noise_db: 55
    # Hand-treadle floor loom during weaving: rhythmic beating of the beater bar
    # against the fell of the cloth produces 50–60 dB at the operator position.
    # Frame loom rug weaving is quieter (no heavy beater mechanism). No hearing
    # protection required; well within conversational-speech levels. Significant
    # contrast with metalworking catalog entries.
    # [CITATION-NEEDED: sound level measurement at operator position for floor-loom
    # weaving operations; label: inferred from general knowledge of loom noise levels.]
    heat_exposure: "Ambient studio temperature; no thermal hazard. Electric-lighting-only with no combustion or heating elements in the production equipment. Studio temperature management is standard commercial HVAC."
    emissions: "Near-zero on-site emissions. Fiber lint and fine yarn dust are the primary air-quality concern; natural ventilation is sufficient at studio scale. Synthetic fiber dust (acrylic strips in rag rugs) warrants periodic air turnover but does not trigger industrial emissions permits at handloom production volumes."
    physical_demand: "Moderate; sustained seated or standing operation at loom; repetitive treadle action (leg); beating the fell of the cloth with beater bar (arm/shoulder); rug warping requires sustained arm extension and moderate tension management. Heavy rug finishing (rolling, washing, and blocking large rugs) requires lifting up to 15 kg for a wet room-size rug. Cumulative daily physical load is moderate and lower than metalworking trades."

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Light-commercial, mixed-use, or downtown retail/studio zoning; rug-making and textile production at handloom scale does not trigger industrial zoning in most US municipalities; customer-facing consultation area may require ADA accessibility compliance"
  emissions: "No emissions permit required; fiber dust at handloom production volumes is below industrial air-quality permit thresholds; natural ventilation sufficient per standard commercial occupancy"
  other: "Standard commercial business license; no trade-specific licensing for rug weaving in US jurisdictions; rug-pile height regulations may apply for commercial building installations (fire code: pile height restrictions in commercial corridors — verify with local code); flammability labeling for upholstery fabric sold B2B to commercial interior designers (UFAC Voluntary Action Program or Cal TB 117 testing may be required by specification)"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: good
  cooperative: marginal
  civic: poor

scale_fit:
  village: poor
  town: good
  small_city: good

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:
  cooperative:
    membership_boundary: >
      Working weavers and textile-craft practitioners operating at journeyman
      level or above; geographic scope town-and-surrounding-township. Member
      access covers shared rug-loom time and floor-loom booking; commission
      production on shared looms requires demonstrable journeyman-weaver
      competency (safety and quality gate). Hobbyist members may access the
      studio at a guest/workshop rate but do not hold full production-access
      membership. Minimum viable membership: 6 members to cover shared
      capital amortization; maximum practical: 15–20 at town scale.
      [corpus/program/SCALES.md §5 2.0% participation × town midpoint ~8,500 pop
      → ~170 craft-participant pool; journeyman-weaver fraction is small;
      6–12 members is a realistic cooperative pool at town scale.]
    rules_source: >
      Operating bylaws adopted at founding general meeting; member vote required
      to amend. Rules govern: loom-booking protocol (advance booking for floor
      loom; frame looms available walk-in during business hours), commission
      production rights (members may produce commissions on shared looms within
      booked time; studio takes no revenue share unless studio takes the
      commission directly), fiber inventory purchasing (collective buying at
      wholesale with cost-share formula), and equipment-damage liability.
    monitoring: >
      Loom-booking register per session (paper or digital); daily log of
      active commissions, fiber drawdown, and equipment condition maintained
      by the member on duty; monthly usage and inventory summary to elected
      studio steward; quarterly steward walkthrough of equipment condition
      and fiber inventory.
    graduated_sanctions: >
      First violation (booking breach, equipment misuse, quality shortcut
      producing damaged output): verbal warning from steward and equipment
      re-orientation. Second violation within 12 months: $75 fine and
      30-day restricted access (workshop/instruction access retained).
      Third violation within 24 months: membership review; possible suspension
      or termination. Equipment damage above $150: cost-recovery invoice
      regardless of sanction tier. Per Ostrom Principle 5.
      [Ostrom 1990, Governing the Commons]
    conflict_resolution: >
      Studio steward (elected annually) arbitrates booking disputes and quality
      standards disagreements; appeal to full membership vote at scheduled
      monthly meeting. Disputes involving the steward are referred to an ad-hoc
      three-member panel elected by remaining members. Per Ostrom Principle 6.
      [Ostrom 1990]
    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6, 7]
    # Principle 1: membership_boundary — journeyman-gated, geographically scoped.
    # Principle 2: booking rules calibrated to mixed rug-frame + floor-loom sharing.
    # Principle 3: member vote to amend bylaws.
    # Principle 4: loom-booking log + steward walkthrough.
    # Principle 5: graduated sanctions above.
    # Principle 6: steward arbitration + member appeal.
    # Principle 7: legal_form registration (cooperative corp or LLC) gives external
    #   recognition; Ostrom P7 applicable at town-scale cooperative.
    # Principle 8: nested governance not applicable at single-cooperative scale.
    member_amendment_process: "2/3 vote at annual general meeting; 30-day written notice to all members before any bylaw amendment vote; emergency amendment (3/4 vote) permissible with 7-day notice for safety-critical or operational-emergency rule changes only"
    legal_form: "Cooperative-corporation or multi-member LLC; registered in the operating state; municipal acknowledgment of facility on file. Cooperative-corporation preferred for clarity of member-ownership; LLC with operating agreement acceptable fallback. Registration required before accepting member dues or signing lease."
    scale_fit_note: >
      Governance rules are calibrated to town-scale (2,000–15,000 residents).
      A 6–12 member rug-weaving cooperative is feasible at town scale; village
      scale (500–2,000 residents) would reduce the journeyman-weaver pool below
      minimum viable membership of 6, making the cooperative model fragile.
      Scale_fit.village: poor and lens_fit.cooperative: marginal reflect the
      thin membership pool at smaller scales: rug-studio cooperatives are viable
      but not robust at town scale, and are typically led by a single market-
      primary operator with 2–4 member participants sharing overhead rather
      than a fully democratic production cooperative.
      [corpus/program/SCALES.md §5]

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 42000
  # Equals economics.capital_cost.mid per E3-R1. [Derived from economics block above.]

  cost_sd: 12500
  # Derived: (capital_cost.high − capital_cost.low) / 4 = (70,000 − 20,000) / 4
  # = $12,500. E3-R5 check: cost_sd / cost_mean = 12,500 / 42,000 = 0.298;
  # within the 0.15–0.50 plausible range. [Derived per catalog/SCHEMA.md §3 default.]

  throughput_units_equiv_per_year: 250
  # Unit: m² of finished rug/upholstery fabric.
  # Derivation:
  #
  # Step 1 — effective weaving days/year:
  #   260 working days − ~20 warping/setup-only days = 240 effective weaving days.
  #   (20 setup days accommodates the warping and loom-dressing overhead for the
  #   floor loom [4–8 hr/new warp] and periodic rug frame rewarps, consistent with
  #   max_active_hours_realism_note above.)
  #
  # Step 2 — output per weaving day:
  #   meters_per_day: 1.0 m/day × warp_width_cm: 120 cm = 1.2 m²/day gross.
  #
  # Step 3 — derating for downtime fraction:
  #   240 days × 1.2 m²/day × (1 − 0.12 downtime) = 240 × 1.2 × 0.88 = 253.4 m²
  #   → rounded to 250 m²/yr.
  #
  # E3-R2 cross-check (via hours):
  #   max_active_hours_per_week (35) × 52 × (1 − 0.12) = 35 × 52 × 0.88 = 1,601.6 hr/yr
  #   Output per hr: 1.0 m/day ÷ 7 hr/day × 1.2 m/m_width = ~0.171 m²/hr
  #   1,601.6 × 0.171 ≈ 274 m²/yr → within the 240-day derivation (the discrepancy
  #   reflects that 1.0 m/day is a conservative daily output estimate; the hours-based
  #   cross-check yields 274 m²/yr assuming 7 productive hr/weaving day, confirming
  #   250 m²/yr is conservative but internally consistent). P2 threshold: within order
  #   of magnitude. ✓
  # [Derived from throughput fields, warp_width_cm, operating-days assumption,
  #  and downtime_fraction above.]

  variable_cost_per_unit: 38.20
  # Cost per m² of finished rug/upholstery fabric:
  # Fiber cost per m²:
  #   annual_consumables $9,500/yr ÷ 250 m²/yr = $38.00/m²
  # Energy cost per m²:
  #   ~$60/yr electricity ÷ 250 m²/yr = $0.24/m²
  # Total: $38.00 + $0.24 = $38.24 → $38.20 (rounded to nearest $0.20).
  # Note: fiber cost dominates entirely; energy is negligible at electric-
  # lighting-only level.
  # [Derived from annual_consumables and energy_consumption_per_active_hour above.]

  labor_hours_per_unit: 6.41
  # Derived: 1 hr ÷ 0.171 m²/hr (output rate from throughput cross-check above)
  # = 5.85 hr/m².
  # Alternatively, directly: derated annual hours ÷ annual output:
  #   1,601.6 hr/yr ÷ 250 m²/yr = 6.41 hr/m².
  # E3-R3 cross-check:
  #   250 m² × 6.41 hr/m² = 1,602.5 hr/yr; target = 35 × 52 × 0.88 = 1,601.6 hr/yr.
  #   Discrepancy = 0.9 hr (<0.1%); within P2 threshold. ✓
  # [Derived from throughput_units_equiv_per_year and derated active hours above.]

  downtime_fraction: 0.12
  # First-year failure profile:
  #   Floor-loom reed at ~1,500 active hr: 7-day replacement lead time.
  #   Warp-beam ratchet at ~2,000 hr: 10-day replacement lead time.
  #   Frame-loom cord wear at ~800 hr: 1-day replacement (minimal downtime
  #     if spare cord on hand; treated as near-zero downtime event).
  # At 35 hr/wk, 800 hr ≈ 22.9 wks (early year); 1,500 hr ≈ 42.9 wks (late year).
  # Planned downtime events: ratchet repair (10 days) + reed replacement (7 days)
  #   + frame cord (1 day) + routine maintenance (5 days) ≈ 23 days/yr.
  # As fraction of 260 working days: 23 ÷ 260 = 0.088.
  # Using 0.12 to include unplanned interruptions (customer consultations running
  #   long, fiber reorder delays, commission revisions) consistent with the
  #   lumpiness of commission-based throughput. Conservative estimate; 0.08–0.10
  #   is achievable in a well-managed studio with spare-parts inventory.
  # [Derived from operations_reality.first_year_failures above.]

  lifespan_years: 25
  # Quality floor-loom-4shaft and rug frame looms have service lives of 20–40 years
  # under routine maintenance (wooden components require periodic refinishing; metal
  # components have near-indefinite life if not subjected to impact damage). 25 years
  # is a conservative estimate for the full studio equipment package including the
  # lower-cost frame looms and studio fit-out. Major refurbishment (heddle
  # replacement, reed inventory, warp-beam bearing replacement) at 10–15 years.
  # [CITATION-NEEDED: service life data for production floor-loom and rug-frame-loom
  # equipment; loom manufacturer documentation (Leclerc, Schacht) preferred;
  # label: inferred from general knowledge of loom longevity in studio use.]

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: fail
    primary_metric: 3.274323546344272
    metric_name: payback_years
    notes: wage_verdict=fail (take_home=10256 vs median=48000)
  village_coop:
    verdict: fail
    primary_metric: 96.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=96, total_annual_cost=19120
  village_civic:
    verdict: fail
    primary_metric: 24.433333333333334
    metric_name: per_household_cost
    notes: per_hh=24.43, threshold=120, hrs/capita=0.000 vs threshold=2.0
  town_market:
    verdict: fail
    primary_metric: 3.274323546344272
    metric_name: payback_years
    notes: wage_verdict=fail (take_home=10256 vs median=56000)
  town_coop:
    verdict: win
    primary_metric: 96.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=96, total_annual_cost=19120
  town_civic:
    verdict: fail
    primary_metric: 3.5931372549019605
    metric_name: per_household_cost
    notes: per_hh=3.59, threshold=100, hrs/capita=0.000 vs threshold=2.0
  small_city_market:
    verdict: fail
    primary_metric: 3.274323546344272
    metric_name: payback_years
    notes: wage_verdict=fail (take_home=10256 vs median=62000)
  small_city_coop:
    verdict: win
    primary_metric: 96.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=96, total_annual_cost=19120
  small_city_civic:
    verdict: fail
    primary_metric: 0.6787037037037037
    metric_name: per_household_cost
    notes: per_hh=0.68, threshold=80, hrs/capita=0.000 vs threshold=2.0
sources:
  - ref: "catalog/weaving/SCHEMA.md v1.0 §1: throughput block structure; meters_per_day ranges by pattern complexity; max_active_hours_per_week guidance for studio weaver; product_mix field definitions"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §2: electric-lighting-only energy source definition; 1–5 kWh/day consumption range"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §3: floor-loom-4shaft loom type; warp width 60–150 cm; operator skill floor journeyman-weaver; capital range $1,500–$6,000 per floor loom"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §4: humidity_control_required false for cotton, synthetic fiber, and coarse upholstery-weight materials"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §5: journeyman-weaver definition — floor-loom-4shaft operation, standard pattern structures, production yardage without supervision"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §6: fiber_source_declaration industrial-yarn-purchased — commercial yarn from distributor; no spinning infrastructure; yarn price volatility noted"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §7: first_year_failures reference list — reed damage, warp beam ratchet/pawl wear; applicable loom types and typical hours-to-failure ranges"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §8 Group A guidance for weave-005: B2B channel dependency (interior designers) as key risk; market_price_per_unit + industrial_baseline_price as load-bearing pair"
  - ref: "catalog/SCHEMA.md v1.1: base schema; all required and conditional fields; E-1/E-2/E-3 validation rules; cooperative and civic lens_context requirements"
  - ref: "corpus/program/SCALES.md §3: median wage thresholds; town-scale and small-city-scale basis; BLS OEWS SOC basis [referenced for cooperative governance calibration, no wage figure required for market-primary entry]"
  - ref: "corpus/program/SCALES.md §5: cooperative member-pool formula; 2.0% participation rate at town scale; basis for 6–12 member cooperative viability assessment"
  - ref: "Ostrom, Elinor. 1990. Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press. (Chapters 2–3: eight design principles, graduated sanctions, conflict resolution; applied to lens_context.cooperative governance structure)"
  - ref: "US Energy Information Administration. Electric Power Monthly, Table 5.3: Average Retail Price of Electricity. Monthly release. https://www.eia.gov/electricity/monthly/ (small-commercial blended rate 2023–2024: $0.10–$0.15/kWh; midpoint $0.125/kWh used for energy cost per unit)"
  - ref: "[CITATION-NEEDED: capital cost data for rug frame looms and 4-shaft floor looms in the 2024–2026 market; vendor pricing from Schacht Spindle Company, Leclerc Looms, Gilmore Looms, Ashford]"
  - ref: "[CITATION-NEEDED: annual fiber procurement cost data for production rug and upholstery weaving studios; commercial rug-yarn supplier pricing (Webs, Halcyon Yarn, Paradise Fibers)]"
  - ref: "[CITATION-NEEDED: empirical custom-rug and handwoven upholstery fabric pricing from US studio weavers and interior-design trade channels, 2024–2026; Houzz custom-rug marketplace, Etsy, interior-design trade publications]"
  - ref: "[CITATION-NEEDED: industrial area rug pricing at US retail 2024; Home Depot, Wayfair, Target standard rug price per m²]"
  - ref: "[CITATION-NEEDED: commercial studio rent per m² in town-scale US markets, 2024; CoStar or local broker data]"
  - ref: "[CITATION-NEEDED: annual maintenance cost data for production rug/upholstery weaving studio; trade or operator survey]"
  - ref: "[CITATION-NEEDED: measured daily output rates for custom rug studio operations by product type; studio-weaver productivity surveys or documented production logs]"
  - ref: "[CITATION-NEEDED: floor-loom reed and ratchet/pawl replacement cost and lead-time data; loom manufacturer service documentation (Leclerc, Schacht, AVL)]"
  - ref: "[CITATION-NEEDED: service life data for production floor-loom and rug-frame-loom equipment; manufacturer documentation preferred]"
  - ref: "[CITATION-NEEDED: sound level measurement at operator position for floor-loom weaving operations; occupational health data for textile weaving]"
  - ref: "American Colonial rag-rug tradition: general reference — Howard, Constance. 1980. Textile Crafts. Pitman. (Flat-weave rag-rug construction as low-capital, accessible weave structure; functional inheritance of material-waste upcycling and plain-weave simplicity) [CITATION-NEEDED: academic economic history source for colonial rag-rug production as commercial or household-subsistence form]"
  - ref: "Scandinavian rya and röllakan flat-weave tradition: general reference — Davison, Marguerite Porter. 1967. A Handweaver's Pattern Book. Swarthmore. (Flat-weave and knotted-pile rug structures informing the design space of custom rug weaving; functional inheritance of natural-wool pile and geometric patterning) [CITATION-NEEDED: economic history source for Scandinavian flat-weave rug production as commercial cottage industry]"
  - ref: "Handweavers Guild of America. https://weavespindye.org/ (US studio-weaver community; primary professional network for custom rug and upholstery fabric market-rate data; referenced for orientation on market pricing; formal rate-card data CITATION-NEEDED)"
---
## Summary

The Custom Rug & Upholstery Studio is a journeyman-operated, town-scale studio producing custom area rugs and upholstery fabric for interior designers and homeowners. It occupies 40–70 m² (55 m² representative), uses electric-lighting-only energy, and operates two or three rug frame looms alongside a 4-shaft floor loom for upholstery cloth. It is the only weaving-catalog entry targeting the furnishing-textile segment — rugs and upholstery fabric for residential and commercial interiors — which sits at the intersection of craft-market premium pricing and a real B2B channel (interior designers as specifying buyers). The entry was created because this niche survives the DECLINE-VERDICT's market test: custom rugs and upholstery cloth are commoditized at the mass-market end ($25/m²) but command genuine premiums ($80–$450/m²) for custom dimensions, natural fiber, and specified colorways that industrial production cannot deliver to order. The entry also captures the weaving trade's strongest repair-analog: rug restoration and reweaving — a service with no commodity substitute, directly analogous to the smithing repair niche.

## Design rationale

This entry solves a specific problem no other entry in the weaving catalog solves: how does a journeyman-level studio produce custom furnishing textiles — area rugs and upholstery fabric — at town scale, with a B2B interior-designer channel, at a price point ($80–$450/m²) that survives against mass-market competition ($25/m²)? Weave-001 (Tapestry) operates in the fine-art segment at master-weaver skill floor; it does not address the furnishing-textile commission market. Weave-002 (Heritage Wool/Natural-Dye) targets a cultural-preservation niche with different loom type, fiber sourcing (heritage breed), and market positioning. Weave-003 (Architectural Textile) addresses large-format commercial commissions at a higher skill floor and capital level. Weave-005 is justified as a distinct entry because: (1) rug construction uses frame looms in addition to a floor loom — a unique equipment configuration in the weaving catalog; (2) the upholstery-fabric product (B2B to interior designers) requires a different channel and pricing logic than retail yardage (weave-004) or tapestry commissions; (3) rug restoration is a distinct service offering with no equivalent in any other catalog entry — it extends the economic model beyond production into the repair-adjacent niche; (4) the journeyman skill floor makes this accessible to a wider operator pool than master-required entries, with real implications for apprentice pipeline and cooperative viability. A catalog without this entry would miss the furnishing-textile commission market entirely and leave the rug-restoration niche undocumented.

## Historical lineage

Three precedents inform this design.

**American colonial rag-rug tradition.** The colonial and early-American rag rug — produced on simple frame looms using cut strips of worn fabric as weft, with cotton or linen warp — represents the oldest functional precedent for this entry. The functional inheritance is the low-capital frame-loom configuration, the material-waste upcycling model (fabric strips as weft), and the plain-weave construction accessible to journeyman-level weavers without the apprenticeship duration required for tapestry or pattern weaving. The colonial rag rug was produced primarily as household utility rather than commercial commodity; the modern equivalent transforms the same accessible technique into a custom-order commercial product at premium pricing. The supply-chain condition that made the colonial form viable — worn household fabric available as a free input — is partially reproduced in the upcycled-fabric-strip sourcing option documented in fiber_source_declaration; modern studios purchase T-shirt yarn and fabric strips commercially rather than processing household waste, reflecting the modern wage-labor baseline. The indenture or household-labor basis of colonial production cannot be reproduced and is not assumed. [CITATION-NEEDED: academic economic history source for colonial rag-rug production as commercial or household-subsistence craft form.]

**Scandinavian rya and flatweave (röllakan/kilim) studio tradition.** The Scandinavian tradition of specialized rug weavers — particularly the Swedish röllakan flatweave and Norwegian rya pile rug — represents a precedent for studio-scale commercial rug production targeting premium buyers. The functional inheritance is: natural-wool pile and weft construction (directly analogous to the rugmaking-wool fiber sourcing in this entry), geometric patterning accessible at journeyman skill level, and a market-facing studio model selling to domestic and export buyers at premium over industrial carpeting. The Scandinavian tradition also demonstrates that plain-weave and knotted-pile structures can support a commercial studio model without requiring the complexity or master-weaver skill floor of tapestry weaving. The property structure of the historical Scandinavian cottage-industry form (household-based, family-owned equipment, cooperative marketing through craft guilds) is not reproduced — the modern studio operates under commercial lease and market-wage labor — but the equipment configuration (frame looms for pile, flat-loom frames for flatweave) directly informs the multi-loom studio design. [CITATION-NEEDED: economic history source for Scandinavian flatweave rug production as commercial cottage industry; labor and market structure documentation.]

**Modern US custom-rug atelier.** Contemporary US studio weavers operating in the custom-rug and upholstery segment represent the living precedent for this entry. The functional inheritance is the entire commercial model: B2B channels (interior designers, commercial specifiers), direct-to-homeowner commissions, sample-card marketing, and rug restoration as a service complement. This precedent is entirely modern; no pre-modern labor regime is assumed. The US maker-community pricing orientation ($80–$450/m²), the interior-designer channel structure (commission-based, specification-grade delivery), and the Handweavers Guild of America as the professional network are all contemporary and verifiable without romantic historicization. [Handweavers Guild of America, https://weavespindye.org/; CITATION-NEEDED: formal pricing survey from studio-weaver community.]

## Key assumptions

Capital costs ($20,000–$70,000) are illustrative estimates inferred from market-orientation review of rug-frame-loom and floor-loom pricing from major US loom vendors (Schacht, Leclerc, Gilmore, Ashford) and commercial studio fit-out cost ranges; no formal vendor bill-of-materials underlies these figures [CITATION-NEEDED]. The mid-point ($42,000) represents a capable two-loom-plus-floor-loom studio with reasonable fit-out; the low ($20,000) is a minimal viable configuration for a solo operator in already-fitted space. Market pricing ($80–$450/m²) is the central economic claim of this entry and is explicitly labeled pricing_validation: inferred: it reflects orientation-level review of US custom-rug market channels but is not sourced from a formal pricing survey or published rate-card study [CITATION-NEEDED]. The industrial baseline ($25/m²) is inferred from general knowledge of US big-box retail area rug pricing [CITATION-NEEDED]. Throughput (250 m²/yr) is derived from a conservative 1.0 m/day output estimate at 120 cm warp width, 240 effective weaving days, and 12% downtime; the output rate is an illustrative estimate rather than an empirically measured figure [CITATION-NEEDED]. The downtime fraction (0.12) is deliberately conservative relative to the minimum-event calculation (~0.09 without unplanned interruptions) to account for commission revision delays and B2B specification iterations that interrupt production scheduling. Fiber sourcing is declared as industrial-yarn-purchased (rugmaking wool, cotton rag, upcycled fabric strips from commercial suppliers); no spinning infrastructure or heritage-breed dependency is assumed, which keeps the capital and supply-chain structure simpler than a heritage-fiber entry but requires explicit acknowledgment that premium pricing depends on custom specification and craft quality rather than fiber provenance. The B2B interior-designer channel is identified in catalog/weaving/SCHEMA.md §8 Group A as a key risk for this entry: designer-channel dependency creates single-channel revenue risk if designer relationships are lost; the entry addresses this by including 15% instruction/open-studio allocation to maintain a direct-to-homeowner revenue base.

## Known risks / failure modes

**Regulatory:** Upholstery fabric sold into the commercial-installation channel may be subject to flammability testing requirements (UFAC Voluntary Action Program, California Technical Bulletin 117, or NFPA 260/261 for contract applications). A studio weaver selling upholstery cloth to commercial interior designers for hospitality or public-space installation must verify flammability compliance before delivery; non-compliant fabric in a commercial installation is a liability and reputational risk. Rug pile height may trigger fire-code restrictions for commercial corridor installations (NFPA 101 or IBC floor-covering regulations for means of egress). ADA accessibility compliance applies to customer-facing consultation space, which may require ramp access or layout modification in some commercial spaces.

**Labor pipeline:** The journeyman-weaver skill floor is achievable via community-college textile programs, Handweavers Guild workshops, and self-directed study with a mentor; unlike master-weaver entries, this entry does not face the near-zero hiring-pool risk of a drawloom or tapestry studio. However, rug construction on frame looms is a specific technical competency distinct from general studio weaving; a journeyman trained primarily in yardage weaving (rigid-heddle or basic floor-loom cloth) may lack rug-specific skills (warp tensioning under high rug-yarn weight, pile management, large-format finishing). The apprentice path (24–30 months) mitigates this but requires an active mentorship commitment. The instruction_open_studio product allocation (15%) is also a succession-building mechanism, as workshop participants who progress to commission clients may eventually become operators.

**Supply chain:** Commercial rugmaking wool yarn and specialty rug-weight fiber is supplied by a small number of US distributors (Webs, Halcyon Yarn, Paradise Fibers and equivalents). A supply disruption — distributor consolidation, inventory shortage in a specific colorway, or shipping disruption — can interrupt the studio's ability to fulfill custom-color commissions with the specific match required by interior-designer specifications. The worst-case lead time (30 days for specialty dye-lot orders) represents a real production gap for time-sensitive installations. Maintaining a minimum 4–6 week fiber inventory buffer is strongly recommended. Upcycled fabric strip sourcing (T-shirt yarn, denim strips) is more supply-resilient as it can be sourced locally from upholstery shops and textile recyclers.

**B2B channel concentration:** Interior-designer clients may represent 50–70% of revenue in a successful studio, creating channel-concentration risk if a major designer relationship ends or the designer's clientele shifts away from custom rugs toward imported alternatives. This is the primary structural risk named in catalog/weaving/SCHEMA.md §8 for this entry. Mitigation: maintain the direct-to-homeowner channel (workshop instruction, craft-market presence, social-media portfolio) as an independent revenue base; diversify designer relationships across 3–5 independent specifiers rather than relying on one firm.

## Iteration log

- 2026-04-18: v0.1 — initial authoring per Plan I Task 7 (weave-005). All v1.1 schema fields populated; lens_fit market: good / cooperative: marginal / civic: poor; lens_context.cooperative populated (marginal trigger met); lens_context.civic omitted (civic: poor; trigger not met); four-stage apprentice_path at journeyman level; three operations_reality first_year_failures items; sim_params derived with explicit E3-R2/R3 cross-checks; rug-restoration service documented in prose and product_mix; B2B channel dependency risk named in Known Risks and §8 Group A guidance; pricing_validation labeled inferred throughout per citation policy; 13 CITATION-NEEDED placeholders carried for post-authoring verification.
