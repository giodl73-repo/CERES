---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: weave-007
trade: weaving
name: "Coverlet & Americana Revival Studio"
tagline: "Journeyman-operated studio producing hand-woven overshot coverlets and Jacquard-style table linens in the American frontier commission tradition"
status: draft
version: "0.1"
supersedes: null
inspirations:
  - american-frontier-itinerant-coverlet-weaver
  - american-overshot-draft-sheet-tradition
  - shaker-communal-weaving-operation

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 27
# Mid-point of the 20–35 m² operating range: a 4-shaft floor loom (practical
# footprint ~2.0 × 3.0 m) plus warping board / warping mill (1.0 × 1.5 m),
# yarn and warp-beam storage, a finishing and wet-blocking area, and operator
# circulation. 27 m² represents a compact but functional single-operator studio
# in town-scale commercial or mixed-use space. Low end (20 m²) is feasible for
# a small-footprint floor loom with minimal storage; high end (35 m²) adds a
# second loom position, a customer sample-consultation area, and expanded yarn
# storage for commissions specifying specific wool colors.
# [research/trades/weaving/REQUIREMENTS.md R-05; american-frontier chapter §3:
# 4-shaft floor loom practical footprint 2.0 × 3.0 m; 27 m² illustrative mid-point.]

ceiling_min_m: 2.4
# A 4-shaft floor loom stands approximately 1.6–1.9 m tall (beater and breast-
# beam height); no overhead mechanism required (no Jacquard superstructure).
# 2.4 m provides comfortable clearance for the loom frame, task lighting over
# the weaving position, and an upright warping mill if present. No combustion
# clearance or exhaust height requirement applies.
# [research/trades/weaving/REQUIREMENTS.md R-05; catalog/weaving/SCHEMA.md §3
# floor-loom-4shaft notes; no raised superstructure for 4-shaft treadle loom.]

ventilation: natural-sufficient
# Electric-lighting-only studio with no combustion process. Wool fiber lint and
# cut-end dust are the primary air-quality concern; natural ventilation (operable
# windows plus a low-volume exhaust fan) is adequate at single-operator studio
# scale. No OSHA-level industrial extraction permit is anticipated for handloom
# wool-yarn dust at these production volumes.
# [catalog/weaving/SCHEMA.md §2 electric-lighting-only; OSHA 29 CFR 1910.94 not
# triggered at handloom fiber-dust production levels.]

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: electric-lighting-only
# All weaving is hand/treadle-operated; no powered weaving mechanism. Energy
# use is limited to studio and task lighting over the loom position, plus small
# auxiliary tools (electric bobbin winder, yarn swift motor if used). Humidity
# control (humidity_control_required: true for wool) adds climate-system energy;
# see Key Assumptions.
# [catalog/weaving/SCHEMA.md §2 electric-lighting-only.]

energy_consumption_per_active_hour: "1.5 kWh/day (lighting + humidity control)"
# Task and ambient lighting for a 27 m² studio: approximately 15 fixtures at
# 10 W LED = 150 W plus 1–2 task lights at 40 W each = ~230 W; at 8 operating
# hours/day that is ~1.8 kWh/day from lighting alone. A residential-grade
# humidifier for a 27 m² studio adds approximately 0.1–0.3 kWh/day during
# operating hours in a climate-controlled space. Total active-operation
# energy: ~1.5 kWh/day (lighting + auxiliary, excluding building-scale HVAC
# which is a landlord or site cost and is reflected in floor_space_rent_per_year).
# [Derived from standard commercial LED loading for 27 m²; catalog/weaving/
# SCHEMA.md §2 electric-lighting-only range 1–5 kWh/day; illustrative estimate.]

backup_fuel: null
# No combustion fuel used; no backup fuel applicable.

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  meters_per_day: 4.0
  # Net woven length per full operating day for overshot coverlet and
  # Jacquard-style table linen production on a 4-shaft floor loom.
  # Overshot pattern weaving on a 4-shaft loom: 2–6 m/day depending on
  # pattern repeat density and operator experience; mid-range estimate of
  # 4.0 m/day is consistent with journeyman-weaver output on a moderately
  # complex overshot draft (Rose-and-Diamond, Whig Rose, or comparable
  # American-tradition draft). Table-linen weaving (twill ground with
  # supplementary weft patterning at 4 shafts) is slightly faster at
  # 4–8 m/day; the blended daily rate of 4.0 m/day reflects a product mix
  # weighted toward the more complex coverlet production.
  # [research/trades/weaving/REQUIREMENTS.md §Throughput: 4-shaft overshot
  # 2–6 m/day for journeyman; catalog/weaving/SCHEMA.md §1 twill 2–6 m/day
  # floor loom; label: inferred mid-range.]

  warp_width_cm: 120
  # Standard coverlet-width warp: 100–130 cm usable weaving width on a
  # 4-shaft floor loom. American frontier coverlets were typically woven in
  # two panels (each ~60–90 cm) sewn together; the modern revival studio
  # weaves single-width panels at 100–130 cm to serve the bed-covering and
  # table-linen market without piecing. 120 cm is the representative width
  # used in sim_params conversions.
  # [catalog/weaving/SCHEMA.md §3 floor-loom-4shaft 60–150 cm warp width;
  # american-frontier chapter §3 four-shaft loom 60–90 cm historical width;
  # modern floor looms support 120 cm with standard equipment.]

  pattern_complexity: twill
  # Overshot patterns (Rose-and-Diamond, Star-and-Diamond, Whig Rose,
  # Honeysuckle, and related American-tradition drafts) are structurally
  # 4-shaft overshot weave structures, which the schema classifies as
  # "twill" tier: twill-ground structures with supplementary pattern weft.
  # Overshot is more complex than plain-weave twill (herringbone, satin)
  # because the pattern blocks require careful treadling sequence management,
  # but the 4-shaft floor loom is purpose-built for this. The table-linen
  # component (twill-damask or M's & O's at 4 shafts) also falls in the
  # twill complexity tier. Neither product requires master-level drawloom
  # or 8-shaft networked-twill capability.
  # [catalog/weaving/SCHEMA.md §1 pattern_complexity definitions: twill =
  # 2/2 twill, herringbone, satin derivatives; pattern/overshot noted as
  # pattern-tier; overshot is classified at twill tier here because it is
  # within 4-shaft floor-loom scope and journeyman skill floor.]

  max_active_hours_per_week: 32
  # Net active loom-hours per week for a single-operator studio weaving
  # overshot and table-linen commissions. Overshot weaving is slower than
  # plain-weave yardage: pattern-sequence management, color-change per
  # commission, and draft verification reduce loom-side velocity relative
  # to straight-yardage production. 32 hr/wk at loom is realistic for a
  # full-time weaver; total studio time including warping (4–8 hr per new
  # overshot warp), draft preparation, customer communication, and finishing
  # (wet-blocking wool coverlets) may reach 45–50 hr/wk. 32 hr/wk is the
  # derated productive-loom-time figure used in sim_params.
  # [catalog/weaving/SCHEMA.md §1 max_active_hours_per_week guidance:
  # realistic ceiling 30–40 hr/wk at loom for studio weaver; overshot
  # overhead justifies the lower end of this range.]

  product_mix:
    yardage: 0
    rugs_upholstery: 0
    tapestry_art: 0
    garments_accessories: 10
    instruction_open_studio: 15
    # Sum: 25 — NOTE: the remaining 75% is coverlet and table-linen
    # production, which does not fit cleanly into the standard product_mix
    # categories. The schema §1 product_mix categories do not include a
    # "coverlet / specialty commissioned textile" bucket. The trade-specific
    # coverlet category is documented in trade_specific.product_category.
    # garments_accessories (10%): scarves and shawls woven in overshot
    # patterns — a natural secondary output from the same loom threading
    # that requires no separate capital. instruction_open_studio (15%):
    # workshops on overshot draft reading, pattern selection, and 4-shaft
    # floor-loom setup; a practical secondary revenue stream and a customer-
    # acquisition path for commission clients.
    # [catalog/weaving/SCHEMA.md §1 product_mix; coverlet primary category
    # documented in trade_specific block per SCHEMA.md §8.]

  throughput_variance:
    worst_month_fraction_of_average: 0.65
    # Commission-based coverlet weaving is relatively non-seasonal; however,
    # the post-holiday January–February period and the August vacation slow
    # the commission inquiry pipeline. A month with no new commission starts
    # may reach 65% of the monthly average if the backlog is thin.
    # [catalog/weaving/SCHEMA.md §1 commission/market entries typical range
    # 0.60–0.80; illustrative estimate.]
    best_month_fraction_of_average: 1.40
    # Gift and holiday season (October–December) drives above-average
    # commission inquiries from buyers seeking custom textiles as gifts and
    # household furnishing upgrades. Craft fair and market-event concentration
    # in the fall also contributes to peak demand.
    # [catalog/weaving/SCHEMA.md §1 holiday-peak guidance 1.20–1.50 for
    # retail; illustrative estimate.]
    seasonal: "Commission work is year-round; October–December craft-market and gift-season peak; January–February post-holiday trough is the primary low period."

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: journeyman-weaver
# Overshot coverlet production on a 4-shaft floor loom requires: ability to
# read and set up an overshot draft (threading sequence, tie-up, treadling
# order); manage warp tension on a wool warp; execute pattern repeats with
# consistent beat; and diagnose and correct threading errors independently.
# These are journeyman-weaver competencies per catalog/weaving/SCHEMA.md §5.
# A rigid-heddle-novice cannot manage a multi-shaft floor loom threading for
# overshot. Master-weaver level (drawloom or 8+ shaft networked work) is not
# required for the standard American-tradition overshot drafts this entry uses.
# The American frontier chapter confirms: professional itinerant coverlet
# weavers operated at skilled-journeyman level on 4-to-8-shaft looms; the 4-
# shaft version of this entry is the accessible modern analog.
# [catalog/weaving/SCHEMA.md §5 journeyman-weaver: floor-loom-4shaft and
# floor-loom-8shaft operation without supervision; standard pattern structures
# including overshot; research/trades/weaving/REQUIREMENTS.md §235.]

operators_concurrent: "1"
# Single operator studio. Overshot weaving on a 4-shaft floor loom is a one-
# person operation: no draw-boy requirement (the Jacquard or 4-shaft
# treadle-and-shaft mechanism is operator-controlled without assistance).
# [research/trades/weaving/REQUIREMENTS.md §258 Jacquard-equipped loom single
# operator; american-frontier chapter §3: 4-shaft and 8-shaft loom single
# operator with Jacquard attachment.]

apprentice_friendly: true
apprentice_path:
  training_stages: >
    Stage 1 (0–3 months): studio safety and floor-loom mechanics; warping a
    floor loom from beam to heddle; plain-weave and 2/2 twill sampling on a
    practice warp; reading a basic threading draft and treadling sequence.
    Gate criterion: winds and dresses a floor loom to correct tension, weaves
    a 50 cm sampler in plain weave and twill without supervision.

    Stage 2 (3–9 months): introduction to overshot structure — reading an
    overshot draft (threading, tie-up, treadling); weaving a complete
    overshot sampler with one pattern draft; pattern-error diagnosis and
    rethreading practice; introduction to wool-warp tension management
    (setting RH, monitoring warp behavior). Gate criterion: completes a
    full overshot sampler from draft setup to finished length, including
    one error-correction cycle, to an accepted quality standard.

    Stage 3 (9–18 months): commission production under supervision — warping
    and threading for a full-width coverlet warp; weaving a complete coverlet
    to customer specification (pattern selection, color sequence, dimension
    targets); wet-blocking and finishing a finished wool coverlet. Gate
    criterion: completes one full commission-quality coverlet from draft
    selection to delivery, meeting dimensional tolerance and customer review.

    Stage 4 (18–30 months): independent commission management — customer
    consultation on pattern selection (from draft-sheet catalog), warp
    planning, quoting, production on commission schedule; table-linen and
    scarf production as secondary products; introduction to draft
    modification for custom pattern requests. Gate criterion: manages a
    full commission cycle independently, from initial customer discussion
    to delivery, with no supervision required.
  time_to_independent_operation: "~24–30 months to journeyman standard on this studio's equipment and pattern vocabulary; overshot production quality achieved by Stage 3 (~18 months); independent commission management follows"
  succession_note: >
    Apprentice co-presence is integrated into normal commission production
    from Stage 2 onward: the apprentice works on parallel warps or assists
    with warping preparation while the primary weaver is at the loom. The
    instruction_open_studio product allocation (15%) provides a natural
    teaching venue that simultaneously serves as customer acquisition for
    commissions. The itinerant-weaver model documented in the American
    frontier chapter depended on informal skill transmission (observation
    and practice, not formal apprenticeship); the modern studio form
    formalizes what the frontier tradition left implicit.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 8000, mid: 18000, high: 35000 }
  # Low ($8,000): a quality 4-shaft floor loom ($2,500–$4,500 for a new
  # Ashford or Leclerc entry-level floor loom, or a used loom in working
  # condition for $800–$2,000); warping board and accessories ($200–$400);
  # yarn and warp starter inventory ($1,500–$2,500); minimal studio fit-out
  # in an already-equipped commercial space ($1,000–$2,000). This is the
  # entry-level configuration for a weaver who already has some tooling and
  # is opening a studio in a shared or low-cost space.
  # Mid ($18,000): quality 4-shaft floor loom with dobby or direct-tie
  # capability ($4,000–$6,000; e.g., Schacht Cranbrook or Macomber);
  # electric warping mill ($600–$900); bobbin winder and yarn swift ($300);
  # draft-design software and pattern catalog production ($300–$500);
  # studio fit-out including humidity management system ($2,000–$3,500);
  # customer-display setup (sample coverlets, pattern catalog binder)
  # ($800–$1,200); starting yarn inventory adequate for 3–4 months of
  # commissions ($3,000–$4,500); signage ($400–$600).
  # High ($35,000): two-loom studio (primary 4-shaft + optional secondary
  # 4- or 8-shaft), professional warping and winding equipment, comprehensive
  # humidity and climate control system, full draft-design capability, large
  # starting yarn inventory for a broad color palette, professional sample
  # display, and build-out of a small customer-consultation space.
  # [CITATION-NEEDED: capital cost data for 4-shaft and 8-shaft floor looms
  # in the 2024–2026 market; vendor pricing from Schacht Spindle Company,
  # Macomber Looms, Leclerc Looms, Ashford; used-loom market from Ravelry,
  # HGA classifieds; label: illustrative estimate.]

  install_cost: 2500
  # Standard commercial electrical permit for lighting upgrade and humidity-
  # control circuit ($1,000–$1,800); minor structural work for humidity
  # management system installation ($400–$600); signage ($200–$400). No
  # combustion system, specialized ventilation, or 3-phase power required.
  # [Illustrative estimate; CITATION-NEEDED: commercial studio fit-out cost
  # for light-duty textile studio in town-scale commercial space; label: inferred.]

  annual_maintenance: 900
  # Loom maintenance: reed inspection and replacement (~$100/yr); heddle
  # replacement on floor loom (~$80/yr); treadle cord and tie-up replacement
  # (~$60/yr); warp-beam ratchet and pawl inspection ($50/yr). Humidity
  # management system: humidifier filter and element replacement (~$150/yr);
  # hygrometer calibration check ($30/yr). General studio maintenance
  # (lighting, display, pattern catalog binder) (~$200/yr). Draft-design
  # software subscription (~$80/yr if applicable). Excludes first-year
  # failure replacements itemized in operations_reality.
  # [Illustrative estimate; catalog/weaving/SCHEMA.md §7 reference list
  # for floor-loom component wear rates; label: inferred.]

  annual_consumables: 4200
  # Primary consumable: commercial wool yarn for weft and warp:
  #   Wool weft yarn (Shetland, Churro, or equivalent worsted-weight):
  #   approximately $2,800–$3,200/yr for 850 m of finished cloth at
  #   120 cm width. Warp yarn (commercial cotton or linen, or wool
  #   warp where humidity-managed): approximately $600–$900/yr.
  # Secondary consumables: bobbin and shuttle materials ($100/yr);
  #   threading hooks and lease sticks ($50/yr); wet-blocking supplies
  #   (wool wash, blocking boards, pins) ($120/yr); packaging for
  #   delivered commissions ($100/yr); draft-sheet printing and catalog
  #   materials ($80/yr); sample warp materials ($150/yr).
  # Electricity (~1.5 kWh/day × 240 days × $0.125/kWh ≈ $45/yr): negligible;
  #   included in variable_cost_per_unit at <$0.05/linear meter.
  # Total: ~$4,200/yr at mid-output of 850 m/yr.
  # [Illustrative estimate; commercial wool yarn pricing oriented from WEBS
  # (yarn.com), Halcyon Yarn, Paradise Fibers; label: inferred.
  # CITATION-NEEDED: production wool-yarn cost per linear meter of overshot
  # coverlet at journeyman studio output level.]

  floor_space_rent_per_year: 3240
  # Imputed at ~$120/m² per year for commercial studio space in a town-scale
  # market. 27 m² × $120/m²/yr = $3,240/yr. Village-scale space would
  # typically be cheaper ($80–$100/m²/yr); the village-viable scale_fit
  # is supported by the lower capital entry and lower rent overhead at that
  # scale. Town-scale commercial studio rent at $120/m²/yr is consistent
  # with secondary US market rates for light-commercial studio space.
  # [Illustrative estimate; compare to weave-005 at $120/m²/yr for 55 m²
  # town-scale commercial space; CITATION-NEEDED: commercial rent per m²
  # in town-scale US markets 2024; CoStar or local broker data preferred;
  # label: inferred.]

  market_price_per_unit: { low: 60, mid: 130, high: 350 }
  # Unit = 1 linear meter of finished hand-woven cloth at 120 cm width
  # (equivalent to approximately 1.2 m² per meter stated).
  # Low ($60/m): basic overshot-pattern table runners or scarves sold
  #   direct at craft fairs or online; entry price for recognizable
  #   American-tradition patterns in commercial wool yarn.
  # Mid ($130/m): commissioned overshot coverlet panel (full-width,
  #   customer-specified pattern and color) or table-linen set (runner
  #   plus napkins); consistent with mid-range studio-weaver commission
  #   rates in the US handcraft market.
  # High ($350/m): premium custom coverlet in heritage-adjacent wool
  #   (named draft, documentation of historical pattern lineage, signed
  #   and dated by weaver) or a complex table-linen set for gift or
  #   heirloom purchase; boutique market, collector buyers, and gift
  #   buyers willing to pay for cultural-tradition provenance.
  # Industrial baseline: $12/m (mass-produced throw or machine-made
  #   pattern blanket at big-box retail — see industrial_baseline_price).
  # [CITATION-NEEDED: US studio-weaver commission pricing for overshot
  # coverlets and handwoven table linens, 2024–2026; Handweavers Guild
  # of America market-rate data, Etsy studio-weaver listings, and
  # comparable operator financials; label: pricing_validation: inferred.]

  pricing_notes: >
    Unit is 1 linear meter of finished hand-woven cloth at 120 cm width.
    Premium over the industrial baseline ($12/m for a mass-produced machine-
    woven throw or pattern blanket at US big-box retail, e.g., a standard
    acrylic patterned throw at $24–$30 retail ÷ ~2 linear meters = $12–$15/m)
    reflects: (1) custom pattern selection from the studio's draft-sheet
    catalog — American overshot patterns that factory production does not
    offer in hand-woven form; (2) natural wool fiber with associated tactile
    and thermal properties that synthetic alternatives cannot match; (3) a
    named and dated commission from an identified weaver (provenance and
    non-fungibility that factory cloth cannot provide); and (4) the cultural-
    tradition context — American-frontier draft vocabulary — that constitutes
    the product's identity for buyers who are purchasing historical revival,
    not just a blanket. The target customer segment is homeowners seeking a
    custom heirloom textile, gift buyers at the $100–$500 range, and craft-
    market buyers who specifically seek American-tradition handwork. Factory
    alternatives ($12–$25/m machine-woven) do not replicate custom pattern
    selection, named draft lineage, or the natural-wool construction of a
    commissioned overshot coverlet.
    [CITATION-NEEDED: industrial throw/blanket pricing at US retail 2024;
    label: inferred from general market knowledge.]

  pricing_validation: >
    Pricing evidence: inferred from orientation-level review of US studio-
    weaver commission pricing via Etsy studio-weaver handwoven coverlet and
    table-linen listings (2024–2026) and general familiarity with craft-market
    commission rates in the US handweaving community. NOT derived from a
    formal industry pricing survey, published rate-card study, or audited
    studio-weaver financial statements. Recommended verification: direct
    survey of operating studio weavers producing overshot or American-
    tradition revival commissions, or a Handweavers Guild of America pricing
    study; comparable operator financial statements would provide empirical
    willingness-to-pay evidence for the $60–$350/m range. The spread reflects
    the market segmentation between craft-fair retail pricing (low) and
    premium-commission heirloom pricing (high); the mid at $130/m is the
    central claim and is the figure most in need of empirical citation.
    Label: pricing_validation: inferred.

  industrial_baseline_price: 12
  # Mass-produced machine-woven throw or patterned blanket (acrylic or
  # polyester/cotton blend, standard sizes, no custom option) at US big-box
  # or online retail, 2024. $12/m ≈ a standard throw at $24–$30 ÷ 2 m
  # linear length. Machine-woven jacquard-patterned throws ($20–$40/m) are
  # a secondary comparison point; the $12 figure represents the commodity
  # substitute available to a cost-only buyer who does not require custom
  # pattern selection or natural-wool construction.
  # [CITATION-NEEDED: mass-market throw and patterned blanket pricing at US
  # retail 2024; Target, Walmart, Wayfair standard-throw pricing per linear
  # meter; label: inferred from general market knowledge.]

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Heddle breakage (wire or texsolv heddles, overshot sett)"
      estimated_hours_to_failure: 800
      replacement_cost: 90
      replacement_lead_time_days: 5
      serviceable_by: operator
      # Overshot weaving places heddles under repeated lateral stress as the
      # pattern weft passes through shed openings; wire heddles at tight setts
      # (10–16 epi for wool coverlet) fatigue at the eye and snap; texsolv
      # heddles stretch and lose shaft registry. A bulk heddle replacement for
      # one shaft takes 2–4 hours of rethreading; the material cost is low
      # ($90 covers a full replacement set for two shafts). Operator-serviceable;
      # spare heddles should be stocked. Lead time 3–7 days from standard loom
      # suppliers (Halcyon Yarn, WEBS, or direct from loom manufacturer).
      # [catalog/weaving/SCHEMA.md §7 heddle breakage reference: 500–2,000 hr
      # typical; lower estimate used here for tight-sett wool overshot; label: inferred.]

    - item: "Warp beam ratchet / pawl wear (floor loom beam tensioning)"
      estimated_hours_to_failure: 1800
      replacement_cost: 75
      replacement_lead_time_days: 10
      serviceable_by: journeyman
      # The ratchet-and-pawl beam tensioning system on the floor loom wears
      # under the constant tension of a wool warp (which requires higher tension
      # than cotton or linen for crisp overshot sheds). Slippage causes warp-
      # tension loss mid-pattern, producing density inconsistency in the
      # coverlet surface. Journeyman-level pawl and spring replacement; 10-day
      # lead time for parts from loom manufacturer or aftermarket supplier.
      # [catalog/weaving/SCHEMA.md §7 warp beam ratchet reference: 1,500–3,500 hr
      # typical; 1,800 hr used for moderate-tension wool overshot; label: inferred.]

    - item: "Climate-control (humidity) system failure"
      estimated_hours_to_failure: 2000
      replacement_cost: 280
      replacement_lead_time_days: 5
      serviceable_by: journeyman
      # A residential-grade humidifier (the most common humidity-management
      # solution for a small studio) fails at the evaporative pad, heating
      # element, or fan bearing after 1,500–3,000 operating hours. Humidity
      # failure in a wool studio causes warp-tension instability: dry conditions
      # cause wool to become static-prone and brittle; humid conditions cause
      # wool fibers to swell and stick in heddle eyes. Both effects produce
      # weaving defects and potential warp breakage. A replacement residential
      # humidifier unit ($150–$280) is journeyman-serviceable; commercial-grade
      # HVAC repair requires a specialist. Lead time 3–7 days for residential
      # unit; 7–21 days for commercial system repair.
      # [catalog/weaving/SCHEMA.md §7 climate-control failure: 1,500–3,500 hr
      # typical for humidity_control_required: true entries; label: inferred.]

  maintenance_schedule:
    daily:
      task: "Remove fiber lint from loom frame and heddle eyes; check warp tension on active warp; monitor studio RH with hygrometer and adjust humidifier output; record commission progress and fiber usage"
      performed_by: operator
    weekly:
      task: "Inspect all heddles for bent or broken eyes; check treadle tie-up cords for fraying; verify warp-beam ratchet engagement under working tension; clean and refill humidifier reservoir; review wool yarn inventory against active commission queue"
      performed_by: operator
    quarterly:
      task: "Full loom mechanical inspection: shaft suspension, beater alignment, warp-beam ratchet and pawl condition, brake pad wear; replace worn tie-up cords as preventive maintenance; deep-clean humidifier (descale evaporative pad or heating element); audit draft-sheet catalog and yarn inventory against forward commission pipeline"
      performed_by: journeyman
    annual:
      task: "Full loom maintenance: replace all texsolv tie-up cords and heddle sets on worn shafts; inspect and re-treat wooden loom frame (oil or wax per manufacturer); review reed condition across standard overshot setts; service or replace humidity management system components; capital equipment insurance review"
      performed_by: journeyman

  startup_shutdown_overhead_per_day_min: 20
  # Startup: check warp tension, verify hygrometer RH reading, review
  # draft and treadling sequence for active commission, confirm yarn
  # staging at shuttle (~10 min). Shutdown: secure shuttles and bobbins,
  # record daily production and pattern position, adjust humidifier for
  # overnight RH maintenance (~10 min). No combustion warm-up required;
  # 20 min/day is a realistic studio-management overhead for a focused
  # single-product commission studio.
  # [Structural inference from studio-weaving operations; illustrative estimate.]

  max_active_hours_realism_note: >
    32 hr/wk is the net active loom-time ceiling, derated from a gross
    studio presence of approximately 45–50 hr/wk. Deductions from gross
    to net: startup-shutdown overhead 20 min/day × 5 days = 1.67 hr/wk;
    customer consultation and commission quotation averaging ~30 min/day
    = 2.5 hr/wk; draft preparation and warp planning for new commissions
    averaging ~45 min/day = 3.75 hr/wk. Warping and loom-dressing time
    (4–8 hr per new overshot warp) is not subtracted from the 32 hr/wk
    figure; it is instead reflected in the 240-effective-weaving-days-per-
    year assumption in sim_params, which reserves approximately 20 days/yr
    for warping, loom dressing, and finishing tasks. sim_params uses 32
    hr/wk as the active-production-hours figure, consistent with this
    derated ceiling.

  interruption_notes: >
    Typical intraday interruptions beyond startup-shutdown: craft-market
    setup and participation days (5–10 days/yr remove full production days),
    customer preview visits for commission work-in-progress (~30 min/visit,
    1–2 visits/wk on active commissions), draft error diagnosis and
    rethreading (occasional; 1–4 hr/occurrence for a full shaft rethread;
    included in downtime_fraction). Pattern-repeat verification at interval
    markers: ~5 min/hr during complex overshot production; folded into the
    4.0 m/day output estimate rather than carried separately.

  consumables_lead_time_days: { typical: 7, worst: 28 }
  # Typical: commercial wool yarn from US textile distributors (WEBS,
  # Halcyon Yarn, Paradise Fibers) — 5–7 day shipping to most US locations.
  # Worst: custom dye-lot or specialty Churro, Icelandic, or heritage-adjacent
  # wool yarn may require 3–4 weeks for dye-lot matching, specialty mill
  # sourcing, or back-order clearance. Loom hardware components (heddles, reed
  # replacement) from loom manufacturer: 5–14 day typical; worst 21–28 days
  # for specialty components from international suppliers (Leclerc Canada,
  # Ashford New Zealand).
  # [Illustrative estimate; CITATION-NEEDED: fiber procurement lead-time data
  # for production studio-weaving operations; label: inferred.]

  throughput_variance:
    seasonal: "Commission work is year-round; October–December craft-market and gift-season peak; January–February post-holiday trough is the primary low period."
    worst_month_fraction_of_average: 0.65
    best_month_fraction_of_average: 1.40

  operator_impact:
    noise_db: 60
    # Hand-treadle floor loom during overshot production: rhythmic treadle
    # actuation (low-frequency thump, ~40–50 dB) plus beater bar beating
    # against the fell of the cloth (percussive ~55–65 dB at operator
    # position). Overshot weaving with heavier wool yarns produces a
    # slightly louder beat than fine-yarn plain weaving. 60 dB(A) is the
    # estimated operator-position average; well below hearing-protection
    # thresholds (85 dB OSHA action level). No hearing protection required.
    # [CITATION-NEEDED: sound level measurement at operator position for
    # floor-loom weaving; occupational health textile-trades data; label:
    # inferred from general knowledge of handloom noise levels.]
    heat_exposure: "Ambient studio temperature; no thermal hazard. Electric-lighting-only studio with no combustion or process-heat source. Studio temperature is managed by commercial HVAC for occupant comfort and for wool-warp humidity stability."
    emissions: "Near-zero on-site emissions. Wool fiber lint and cut-end dust are the only air-quality consideration; natural ventilation with periodic air exchange is adequate at single-operator studio scale. No emissions permit required."
    physical_demand: "Moderate; sustained seated operation at the loom; repetitive treadle depression (both legs alternating) for overshot pattern treadling sequences; rhythmic beater-bar beating with both hands; shuttle throwing across 120 cm shed. Warping a floor loom requires sustained standing and arm extension. Wet-blocking a finished wool coverlet (rolling, washing, and stretching) involves moderate lifting (5–10 kg for a wet single-width coverlet). Cumulative daily physical load is moderate and comparable to other artisan-seated-production trades."

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Light-commercial, mixed-use, or downtown retail-studio zoning; handloom textile production at studio scale does not trigger industrial zoning in most US municipalities; customer-consultation area may require ADA accessibility compliance if open to the public"
  emissions: "No emissions permit required; wool fiber dust at handloom production volumes is below industrial air-quality permit thresholds; natural ventilation sufficient under standard commercial occupancy classification"
  other: "Standard commercial business license; no trade-specific licensing for handloom weaving in US jurisdictions; finished-textile flammability labeling requirements apply only if cloth is sold for use in regulated commercial interiors (not applicable to residential commission coverlets and table linens as personal-use items); textile-content labeling (Textile Fiber Products Identification Act) required for retail-sold items claiming specific fiber content"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: good
  cooperative: marginal
  civic: marginal

scale_fit:
  village: good
  town: good
  small_city: marginal

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:
  cooperative:
    membership_boundary: >
      Working weavers operating at journeyman level or above; geographic scope
      encompassing the primary town plus surrounding rural township. Village-scale
      entry is feasible given the lower minimum-viable membership for a shared-
      equipment cooperative (3–5 active members can share one floor loom and
      studio space sustainably). Access to the shared loom is gated by demonstrated
      4-shaft floor-loom competency (ability to warp, thread, and operate without
      supervision). Hobbyist or developing weavers may access the studio at a
      workshop or guest rate; production-commission access requires full-member
      skill demonstration. The itinerant-weaver historical model (individual
      loom ownership, individual customer relationships) is the market-primary
      analog; the cooperative form here tests whether shared capital and studio
      overhead can support multiple commission weavers at lower individual entry cost.
      [corpus/program/SCALES.md §5 participation rate; weaving cooperative
      viability analysis in catalog/weaving/SCHEMA.md §8 Group B guidance.]
    rules_source: >
      Operating bylaws adopted at founding general meeting; member vote required
      to amend. Rules govern: loom-booking protocol (advance booking with minimum
      3-day notice for a warp that occupies the loom for multiple days; walk-in
      access for sampler and short warps during unbooked hours); commission
      production rights (members produce commissions on shared loom within booked
      time; studio takes no revenue share unless studio takes the commission
      directly); fiber inventory purchasing (collective buying at wholesale with
      cost-share formula for shared materials; individual commission yarn is
      member-purchased); equipment damage and repair liability policy.
    monitoring: >
      Loom-booking register per session (paper or digital calendar); daily log
      of warp-in-progress, pattern and warp details, and equipment condition;
      monthly usage and inventory summary to elected studio steward; quarterly
      steward inspection of loom mechanical condition and draft-catalog currency.
    graduated_sanctions: >
      First violation (booking breach, equipment misuse, loom left in mid-warp
      state beyond booked time): verbal warning from steward and loom-protocol
      re-orientation. Second violation within 12 months: $60 fine and 30-day
      restricted access (workshop attendance retained). Third violation within
      24 months: membership review; possible suspension or termination. Equipment
      damage above $100: cost-recovery invoice regardless of sanction tier.
      Per Ostrom Principle 5.
      [Ostrom 1990, Governing the Commons.]
    conflict_resolution: >
      Studio steward (elected annually) arbitrates booking disputes and quality-
      standards disagreements; appeal to full membership vote at scheduled monthly
      meeting. Disputes involving the steward are referred to an ad-hoc three-
      member panel elected by remaining members. Per Ostrom Principle 6.
      [Ostrom 1990.]
    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6, 7]
    # Principle 1: membership_boundary — journeyman-gated, geographically scoped.
    # Principle 2: booking rules calibrated to multi-day warp occupation of a
    #   single shared loom; access graduated by competency level.
    # Principle 3: member vote required to amend bylaws; see member_amendment_process.
    # Principle 4: booking register + steward inspection.
    # Principle 5: graduated sanctions above.
    # Principle 6: steward arbitration + member appeal.
    # Principle 7: legal_form registration provides external recognition; applicable
    #   at town-scale; village scale: informal recognition may suffice but registered
    #   form is preferred.
    # Principle 8: nested governance not applicable at single-cooperative scale.
    member_amendment_process: "2/3 vote at annual general meeting; 30-day written notice to all members before any bylaw amendment; emergency amendment by 3/4 vote with 7-day notice for safety-critical or operational-emergency changes only"
    legal_form: "Cooperative corporation or multi-member LLC registered in the operating state; municipal acknowledgment of studio on file preferred. Registration required before accepting member dues or signing commercial lease. Cooperative-corporation form preferred for clarity of member equity; LLC with operating agreement is an acceptable fallback."
    scale_fit_note: >
      Governance rules are calibrated to town-scale (2,000–15,000 residents)
      but the lower minimum-viable membership (3–5 active weavers) makes the
      model feasible at village scale as well — consistent with scale_fit.village:
      good. A village-scale cooperative operates more informally in practice
      (monthly meeting may be a standing weekly gathering given the small size)
      and relies on the steward's direct observation more than formal logging.
      The booking-calendar formality should be calibrated to the number of
      active members: at 3–4 members, informal booking by group message is
      functionally equivalent; at 8–12 members a shared calendar system is
      necessary to prevent conflict. scale_fit.small_city: marginal because
      a journeyman-weaver cooperative is a thin membership pool in any scale
      market; the key advantage at village and town scale is the cultural
      specificity of the American-frontier design tradition as a community-
      identity anchor.
      [corpus/program/SCALES.md §5.]

  civic:
    political_coalition: >
      Cultural-heritage and arts-education advocates; historical society or local
      museum with an interest in American textile tradition documentation; tourism
      or Main Street development agency that recognizes a revival-weaving studio
      as a heritage-tourism draw; workforce-development or artisan-economy program
      if one exists at town or county scale. The civic case for this entry is
      primarily cultural (preservation of American overshot draft tradition and
      the itinerant-weaver model) rather than essential-services provision;
      coalition-building requires framing around heritage tourism and arts-economy
      development, not infrastructure necessity.
    council_vote_estimate: >
      4–3 or 5–2 favorable in a town with active Main Street or heritage-tourism
      program; harder to pass without that framing. Primary opposition arguments:
      (1) market-primary entry with good private-operator viability does not need
      civic subsidy; (2) cultural-heritage argument is thin if no named community
      historical-society partnership is in place. Civic form is marginal because
      the market-primary model is the stronger fit; civic investment is justified
      only if the market operator cannot sustain the heritage-documentation and
      apprentice-training functions as private externalities.
    competes_with_private: >
      A civic coverlet studio competes with any private studio weaver in the
      same trade area. If a private operator already offers overshot-commission
      work in the town, the civic facility is difficult to justify without a
      documented market-failure argument (e.g., the private operator cannot sustain
      apprentice training or heritage-documentation costs independently). The
      stronger civic-facility argument applies in villages or towns with no existing
      private studio weaver — the itinerant-weaver historical model had no permanent
      studio, and a civic studio anchors what the itinerant model could not: a
      permanent draft-catalog archive and an apprentice pipeline.
    governance_form: "Municipally owned or heritage-organization owned; operated by a contracted journeyman weaver under an annual performance agreement; apprentice position funded through workforce-development or arts-education grant."
    budget_line: "Capital via arts-and-culture grant or Main Street revitalization fund; operations under arts-education, heritage-preservation, or workforce-development line; annual operating subsidy targets break-even after commission revenue offset."
    benchmark_comparison: >
      Per-household annual cost at mid-capital ($18,000 equipment + $2,500
      install + $4,200 consumables + $900 maintenance + $48,000 operator wage
      estimate, offset by ~$55,000 commission revenue at mid pricing over 250 m/yr
      at $130/m average): net annual public cost approximately $18,600/yr in
      year 1 (equipment amortized over 25 years = $720/yr + install = $100/yr
      + consumables + maintenance − revenue shortfall). In a village of 1,000
      residents (360 households): ~$52/hh/yr gross operating cost before revenue
      offset, comparable to a small-town library at $40–$60/hh/yr in peer
      communities. If commission revenue at mid-pricing covers consumables and
      maintenance, net civic cost falls to capital amortization + operator-wage
      subsidy: substantially below library cost-equivalent for a heritage-
      anchoring facility with demonstrated apprentice-training function.
      [corpus/program/SCALES.md §3 village household count ~360 households;
      library benchmark: American Library Association 2024 per-household cost
      survey, median small-public-library at ~$42/hh/yr; CITATION-NEEDED:
      confirm ALA figure and methodology; label: illustrative calculation.]
    staffing_model:
      role: "Contracted journeyman weaver (studio operator) + apprentice position (part-time, grant-funded)"
      operator_fte: 1.0
      wage_assumption: 42000
      # Journeyman artisan-studio operator at village-to-town scale; below
      # skilled-trades median reflecting the artisan-studio context and the
      # partial revenue offset from commission income. Range: $36,000–$52,000
      # depending on local wage norms and grant-funding availability.
      wage_source: "corpus/program/SCALES.md §3 village-scale skilled-artisan wage reference; weaving operator at journeyman level below median skilled-trades rate reflecting artisan-market context; CITATION-NEEDED: confirm SCALES.md §3 figure against BLS OEWS SOC 51-6091 (Textile Bleaching and Dyeing Machine Operators) or nearest equivalent code; label: inferred"
      hours: "40 hrs/wk including loom production, commission management, pattern-catalog maintenance, and apprentice supervision"
      hiring_notes: >
        Journeyman-weaver hiring pool is thin at any geographic scale; the
        specialist skill (4-shaft floor loom, overshot draft tradition) is not
        covered by standard vocational programs and requires either self-directed
        or guild-workshop training. Geographic radius may need to extend to
        100–200 miles to find a candidate with the specific American-tradition
        overshot vocabulary this entry requires. Handweavers Guild of America
        chapter networks and online fiber-arts communities (Ravelry) are the
        primary hiring channels. Alternatively, the civic model can be built
        around an existing local weaver who agrees to operate the studio with
        civic capital support — the itinerant-weaver historical model provides
        a precedent for a skilled practitioner operating with community-provided
        space and equipment in exchange for open-access studio time.
    civic_externalities:
      - "Heritage documentation: ongoing maintenance and expansion of the American overshot draft-sheet catalog, preserving a functional archive of American frontier pattern tradition that no private operator has an economic incentive to maintain systematically"
      - "Apprentice training pipeline: produces 1–2 journeyman-level studio weavers per 3-year cycle, sustaining the local artisan capacity for commission weaving beyond the current operator's career"
      - "Community identity anchor: a permanent revival-weaving studio with a public draft-catalog serves heritage-tourism and local-identity functions that an itinerant private operator cannot provide"

# ── TRADE-SPECIFIC FIELDS ─────────────────────────────────────────────────────

trade_specific:
  loom_type: floor-loom-4shaft
  # Standard studio floor loom with 4 shafts (harnesses). Sufficient for
  # the full vocabulary of American overshot patterns (Rose-and-Diamond,
  # Star-and-Diamond, Whig Rose, Honeysuckle, and related drafts), twill-
  # ground table linens, and M's & O's patterned cloth. An 8-shaft loom
  # extends the pattern vocabulary to double-weave and networked twill
  # structures; this entry is specified at 4-shaft because it is the
  # accessible entry point for the American tradition revival niche and
  # keeps capital cost in the $8,000–$18,000 range rather than the
  # $15,000–$35,000 range of an 8-shaft professional loom.
  # [catalog/weaving/SCHEMA.md §3 floor-loom-4shaft: $1,500–$6,000 per loom;
  # journeyman-weaver operator floor; 60–150 cm warp width.]

  humidity_control_required: true
  # Wool warp and weft: humidity-sensitive fiber. Warp tension changes with
  # relative humidity; dimensional stability of finished wool coverlets is
  # affected by RH variation. Target studio RH: 50–65% (wool-warp stable
  # range; below 45% causes static and brittleness; above 75% causes fiber
  # felting in heddle eyes). A residential-grade humidifier or combination
  # humidifier-dehumidifier is the standard solution for a small studio in
  # a temperate climate; climate-controlled leased space reduces the
  # capital and operating burden if the HVAC system maintains a stable RH.
  # [catalog/weaving/SCHEMA.md §4 humidity_control_required: true for wool;
  # research/trades/weaving/REQUIREMENTS.md R-01: 65–75% RH for wool warp.]

  fiber_source_declaration: industrial-yarn-purchased
  # Commercially spun wool yarns purchased from US textile distributors
  # (WEBS, Halcyon Yarn, Paradise Fibers, and equivalents). No spinning
  # infrastructure at the studio; no direct farm-to-loom fiber relationship.
  # Fiber types: worsted-weight or DK-weight wool warp and weft yarn
  # (Shetland, Churro, or equivalent 2-ply worsted construction); cotton
  # or linen warp yarn for specific commission requirements. Industrial
  # sourcing keeps capital and supply-chain complexity low; it also means
  # the product's premium rests on pattern heritage and commission
  # customization rather than fiber provenance. This is consistent with
  # the anti-romantic framing of this entry: the American frontier
  # itinerant professional weavers adopted factory-spun yarn as soon as
  # it became available (from the 1830s–1840s onward) because it
  # eliminated the spinner-to-loom bottleneck, not because it preserved
  # a pre-industrial tradition.
  # [catalog/weaving/SCHEMA.md §6 industrial-yarn-purchased; american-
  # frontier chapter §6: factory-spun yarn adoption eliminated spinning
  # dependency by the 1840s.]

  product_category: "coverlet-and-table-linen"
  # Primary product category not covered by the base schema product_mix
  # enumeration. Coverlets: hand-woven wool bed coverings in American
  # overshot or related draft traditions, produced to commission for
  # residential buyers. Table linens: runners, napkins, and placemats
  # in overshot or twill-damask structure, produced to commission or
  # as ready-to-sell studio stock. The coverlet-and-table-linen category
  # accounts for approximately 75% of studio output by linear meter.

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 18000
  # Equals economics.capital_cost.mid per E3-R1. [Derived from economics block above.]

  cost_sd: 6750
  # Derived: (capital_cost.high − capital_cost.low) / 4 = (35,000 − 8,000) / 4
  # = $6,750. E3-R5 check: cost_sd / cost_mean = 6,750 / 18,000 = 0.375;
  # within the 0.15–0.50 plausible range. [Derived per catalog/SCHEMA.md §3 default.]

  throughput_units_equiv_per_year: 850
  # Unit: linear meters of finished hand-woven cloth at 120 cm width.
  # Derivation:
  #
  # Step 1 — effective weaving days/year:
  #   260 working days − ~20 warping/setup-only days = 240 effective weaving days.
  #   (20 setup days accommodate: warping and loom-dressing per new overshot warp
  #   [4–8 hr each, ~10–15 warps/yr]; wet-blocking and finishing of completed
  #   commissions; draft preparation for new commissions. Consistent with
  #   max_active_hours_realism_note above.)
  #
  # Step 2 — output per effective weaving day:
  #   meters_per_day: 4.0 m/day (conservative overshot output estimate).
  #
  # Step 3 — derating for downtime fraction:
  #   240 days × 4.0 m/day × (1 − 0.10 downtime) = 240 × 4.0 × 0.90 = 864 m
  #   → rounded to 850 m/yr.
  #
  # E3-R2 cross-check (via hours):
  #   max_active_hours_per_week (32) × 52 × (1 − 0.10) = 32 × 52 × 0.90 = 1,497.6 hr/yr
  #   Output per hr: 4.0 m/day ÷ 8 hr/day = 0.50 m/hr
  #   1,497.6 hr/yr × 0.50 m/hr = 748.8 m/yr
  #   Day-based calculation gives 864 m/yr (before rounding to 850);
  #   hours-based gives ~749 m/yr. Discrepancy reflects that warping-overhead days
  #   are carved out of the 240 effective days but not from the 32 hr/wk figure;
  #   the day-based method accounts for this correctly by reserving 20 setup days.
  #   Using 850 m/yr (day-based, rounded down) as conservative mid-point. P2
  #   threshold: within order of magnitude. ✓
  # [Derived from throughput fields, operating-days assumption, and downtime_fraction
  #  above; units stated in Key Assumptions.]

  variable_cost_per_unit: 4.94
  # Cost per linear meter of finished cloth:
  # Fiber and consumable cost:
  #   annual_consumables $4,200/yr ÷ 850 m/yr = $4.94/m
  # Energy cost:
  #   ~$45/yr electricity ÷ 850 m = $0.053/m (negligible; absorbed in rounding)
  # Total: $4.94/m (fiber and consumables dominate; energy is negligible).
  # [Derived from annual_consumables and throughput_units_equiv_per_year above.]

  labor_hours_per_unit: 1.76
  # Derived directly from derated annual hours and throughput:
  #   1,497.6 hr/yr ÷ 850 m/yr = 1.762 hr/m → 1.76 hr/m.
  # E3-R3 cross-check:
  #   850 m × 1.76 hr/m = 1,496 hr/yr; target = 32 × 52 × 0.90 = 1,497.6 hr/yr.
  #   Discrepancy = 1.6 hr (<0.1%); within P2 threshold. ✓
  # [Derived from throughput_units_equiv_per_year and derated active hours above.]

  downtime_fraction: 0.10
  # First-year failure profile:
  #   Heddle breakage at ~800 active hr: rethreading takes 2–4 hr; negligible
  #     downtime if spare heddles are stocked (no wait); call it 0.5 days/yr.
  #   Warp-beam ratchet at ~1,800 hr: 10-day lead time for parts = 10 days/yr.
  #   Humidifier failure at ~2,000 hr: 5-day lead time (residential unit) = 5 days.
  #   Routine maintenance schedule: quarterly journeyman visit ~0.5 days × 4 = 2 days.
  #   Total planned + first-year: ~17.5 days / 240 effective days = 0.073.
  #   Using 0.10 to account for unplanned interruptions: warp breakage requiring
  #   re-threading, commission-revision requests that require unwinding and re-
  #   weaving a section, and the lumpy commission-booking pattern (days with no
  #   active warp while waiting for next commission to start). 0.10 is conservative
  #   but realistic for a commission-primary studio with irregular workflow.
  # [Derived from operations_reality.first_year_failures above; consistent with
  #  catalog/weaving/SCHEMA.md §7 guidance on loom-setup overhead counting toward
  #  non-production overhead in downtime_fraction.]

  lifespan_years: 25
  # Quality 4-shaft floor looms (Schacht, Macomber, Leclerc, AVL) have documented
  # service lives of 25–50+ years under routine maintenance; the wooden frame
  # requires periodic refinishing and the metal hardware is near-indefinitely
  # serviceable with replacement parts. 25 years is a conservative estimate for
  # the full studio equipment package including the lower-cost auxiliary items
  # (warping mill, bobbin winder, humidity system). Major refurbishment at 10–15
  # years (heddle sets, reed inventory, beam components).
  # [CITATION-NEEDED: service life data for production 4-shaft floor looms;
  # manufacturer documentation (Schacht, Macomber) preferred; label: inferred
  # from general knowledge of floor-loom longevity in studio use.]

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
  - ref: "research/cultures/american-frontier/weaving.md §3: four-shaft and eight-shaft floor loom specifications; itinerant professional weaver model; coverlet production as primary specialty niche; draft-sheet inventory as professional catalog"
  - ref: "research/cultures/american-frontier/weaving.md §7–§8: restructuring of professional coverlet-weaving trade; industrial competition context; skilled-labor reproduction failure as terminal mechanism"
  - ref: "research/cultures/american-frontier/weaving.md §6: factory-spun yarn adoption eliminating spinning dependency by 1830s–1840s; itinerant professional adoption of industrial inputs"
  - ref: "research/trades/weaving/HISTORICAL-FORMS.md §Table 1 American Frontier column: four-shaft floor loom primary; eight-shaft coverlet loom; Jacquard attachment from 1840s–1850s; itinerant single-operator loom design [Vlach 1991; Tryon 1917]"
  - ref: "research/trades/weaving/HISTORICAL-FORMS.md §Table 3 American Frontier: itinerant professional paid per-yard commission; household supplied fiber; draft-sheet pattern inventory [Hood 2003; Vlach 1991]"
  - ref: "research/trades/weaving/HISTORICAL-FORMS.md §Synthesis: American frontier commodity cloth demand-collapse; coverlet specialty restructuring with terminal trajectory; factory-spun yarn as industrial input"
  - ref: "research/trades/weaving/REQUIREMENTS.md R-01: wool humidity requirement 65–75% RH; below 45% static and breakage; above 75% felting"
  - ref: "research/trades/weaving/REQUIREMENTS.md R-05: four-shaft floor loom footprint 2.0 × 3.0 m practical"
  - ref: "research/trades/weaving/REQUIREMENTS.md §235: multi-shaft overshot pattern weaving journeyman-to-master skill requirement"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §1: throughput block structure; meters_per_day ranges by pattern complexity; twill tier 2–6 m/day floor loom; max_active_hours_per_week guidance"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §2: electric-lighting-only energy source; 1–5 kWh/day range"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §3: floor-loom-4shaft loom type; warp width 60–150 cm; journeyman-weaver operator floor; capital range $1,500–$6,000 per floor loom"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §4: humidity_control_required: true for wool warp or weft"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §5: journeyman-weaver definition — floor-loom-4shaft operation, standard pattern structures including overshot, production quality without supervision"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §6: fiber_source_declaration industrial-yarn-purchased — commercial yarn from distributor; yarn price volatility noted"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §7: first_year_failures reference — heddle breakage 500–2,000 hr; warp beam ratchet 1,500–3,500 hr; climate-control failure 1,500–3,500 hr for humidity_control_required: true"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §8 Group B guidance for weave-007: journeyman-accessible tradition at 4-shaft; historical lineage must cite American frontier chapter"
  - ref: "catalog/SCHEMA.md v1.1: base schema; all required and conditional fields; E-1/E-2/E-3 validation rules; cooperative and civic lens_context requirements"
  - ref: "corpus/program/SCALES.md §3: village- and town-scale wage thresholds; BLS OEWS basis"
  - ref: "corpus/program/SCALES.md §5: cooperative member-pool formula; participation rate for artisan cooperative viability"
  - ref: "Ostrom, Elinor. 1990. Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press. (Chapters 2–3: eight design principles, graduated sanctions, conflict resolution; applied to lens_context.cooperative governance structure)"
  - ref: "Tryon, Rolla Milton. 1917. Household Manufactures in the United States 1640–1860. University of Chicago Press. [Primary economic-history source for American frontier household and professional weaving; factory-cloth displacement timeline; flax cultivation decline; fulling mill geography]"
  - ref: "Strasser, Susan. 1982. Never Done: A History of American Housework. Pantheon Books. [American household textile production as unpaid women's labor; industrial substitution of household production; context for itinerant professional weaving as the paid-labor parallel]"
  - ref: "Vlach, John Michael. 1991. By the Work of Their Hands: Studies in Afro-American Folklife. University Press of Virginia. [Itinerant professional weaver material culture and craft production context; referenced for American frontier professional weaver model — verify specific coverage before promoting to load-bearing citation position]"
  - ref: "Hood, Adrienne D. 2003. The Weaver's Craft: Cloth, Commerce, and Industry in Early Pennsylvania. University of Pennsylvania Press. [Professional coverlet weaving in early American context; draft-sheet documentation; commission structure; used as adjacent-region comparative; U.S.-specific source preferred for frontier itinerant weaver citation]"
  - ref: "Stein, Stephen J. 1992. The Shaker Experience in America. Yale University Press. [Shaker communal weaving as cooperative production model; collective capital, directed labor, commercial output; contrast with itinerant and household forms]"
  - ref: "Dublin, Thomas. 1979. Women at Work: The Transformation of Work and Community in Lowell, Massachusetts, 1826–1860. Columbia University Press. [Industrial cloth production context; Lowell mills as competitive pressure on frontier household and professional weaving from the 1820s onward]"
  - ref: "US Energy Information Administration. Electric Power Monthly, Table 5.3: Average Retail Price of Electricity. https://www.eia.gov/electricity/monthly/ [small-commercial blended rate 2023–2024: $0.10–$0.15/kWh; midpoint $0.125/kWh used for energy cost per unit]"
  - ref: "American Library Association. 2024. Library Operating Expenditures Survey. https://www.ala.org/tools/libstats/ [per-household operating cost for small public libraries; $42/hh/yr median used as civic benchmark comparison; CITATION-NEEDED: confirm specific figure and methodology from ALA 2024 survey]"
  - ref: "[CITATION-NEEDED: capital cost data for 4-shaft floor looms in the 2024–2026 market; vendor pricing from Schacht Spindle Company, Macomber Looms, Leclerc Looms, Ashford; used-loom market from Ravelry or HGA classifieds; label: illustrative estimate]"
  - ref: "[CITATION-NEEDED: annual fiber procurement cost data for production overshot-coverlet studio; commercial wool-yarn supplier pricing from WEBS, Halcyon Yarn, Paradise Fibers; label: inferred]"
  - ref: "[CITATION-NEEDED: US studio-weaver commission pricing for overshot coverlets and handwoven table linens, 2024–2026; Etsy studio-weaver listings, Handweavers Guild of America rate-card data, or comparable operator financials; label: pricing_validation: inferred]"
  - ref: "[CITATION-NEEDED: mass-market throw and patterned-blanket pricing at US retail 2024; Target, Walmart, Wayfair standard-throw price per linear meter; label: inferred]"
  - ref: "[CITATION-NEEDED: commercial studio rent per m² in town-scale US markets, 2024; CoStar or local broker data preferred; label: inferred]"
  - ref: "[CITATION-NEEDED: service life data for production 4-shaft floor looms; manufacturer documentation from Schacht, Macomber, or AVL; label: inferred]"
  - ref: "[CITATION-NEEDED: sound level measurement at operator position for floor-loom weaving operations; occupational health or textile-trades data; label: inferred]"
  - ref: "[CITATION-NEEDED: professional coverlet-weaving specialization and persistence into mid-19th century; U.S.-specific textile-history source; Hood 2003 covers Ontario as adjacent comparative; label: structurally inferred per HISTORICAL-FORMS.md]"
  - ref: "[CITATION-NEEDED: Jacquard adoption timeline in American professional hand-weaving, mid-19th century; textile-history monograph or museum collection study; Smithsonian American History collection coverlet holdings documentation; label: structurally inferred]"
---

## Summary

The Coverlet & Americana Revival Studio is a journeyman-operated, single-operator studio producing hand-woven overshot coverlets and Jacquard-style table linens in the American frontier commission tradition. It operates in 20–35 m² (27 m² representative) on a 4-shaft floor loom using commercial wool yarns, serving residential commission buyers and craft-market customers at town and village scale. It is the only weaving-catalog entry targeting the American overshot-coverlet tradition as its primary market identity — a niche that survived industrial competition on the frontier precisely because its product (custom-patterned, named-draft, natural-wool commissioned bed covering) was non-fungible against factory cloth. The entry tests the modern version of the itinerant-weaver commercial model in a fixed-studio form: can a permanent studio weaver at journeyman level, using the same draft-sheet inventory approach the frontier professional used, sustain a commission business at village-to-town scale? The capital requirement ($8,000–$18,000 mid) is lower than any other multi-shaft weaving entry in the catalog, making this the accessible entry point for the American textile revival category.

## Design rationale

This entry solves a specific problem no other entry in the weaving catalog solves: it evaluates the economic viability of the American overshot-coverlet tradition as a modern commercial studio niche, at the accessible 4-shaft journeyman level, at village-to-town scale with market as the primary lens. Weave-002 (Heritage Wool/Natural-Dye) is a heritage-fiber entry with a different fiber-sourcing logic (heritage-breed wool, not industrial yarn) and a different cultural tradition focus. Weave-006 (Traditional Revival, if authored) targets a specific non-American textile tradition at master-weaver level. This entry is justified as distinct because: (1) the American frontier draft-tradition — overshot patterns with named historical drafts as the product catalog — is a specific, named, historically documented commercial model that the HISTORICAL-FORMS chapter explicitly identifies and that no other entry covers; (2) the 4-shaft floor-loom configuration at $8,000–$18,000 capital is the lowest entry-point multi-shaft studio in the catalog, which has implications for village-scale viability that higher-capital entries cannot test; (3) the industrial-yarn-purchased fiber sourcing is an explicit anti-romantic design choice that mirrors what frontier professional weavers actually did (adopted factory-spun yarn as soon as it was available); (4) village-good scale fit is a distinctive feature of this entry — the itinerant model demonstrated that small communities, each too small to sustain a permanent studio, could support a weaver who traveled to them, and the fixed-studio modern analog works at village scale because the commission model does not require a dense customer pool the way a retail-yardage studio does.

## Historical lineage

Three precedents inform this design, ordered from most to least direct functional inheritance.

**American frontier itinerant professional coverlet weaver (ca. 1800–1890).** The primary model. The functional inheritance is the entire commercial structure of this entry: a journeyman-level weaver with a 4-shaft (or 8-shaft) floor loom serving rural customers by commission, charging a per-yard or per-item fee for pattern weaving in the customer's wool yarn, operating with a draft-sheet inventory as the product catalog. The American frontier chapter documents this clearly: "the professional equivalent of a product catalog" (draft sheets); "the economic viability of the itinerant professional weaver depended entirely on the segment of the market that industrial production did not serve" (custom coverlets, rag rugs). The labor regime of the frontier professional — paid market-rate commission fees, loom as personal capital asset, itinerant travel as the distribution system — is directly reproducible in modern form as a fixed-studio equivalent. The crucial anti-romantic point, documented explicitly in the frontier chapter and required to be stated here: the itinerant coverlet weaver was not a pre-industrial folk craftsman preserving a timeless tradition. They were an economic response to factory displacement, operating in a niche that factories had not yet commoditized. By the 1840s they had adopted factory-spun yarn, eliminating the household spinning dependency. By the 1870s–1890s the trade had disappeared due to skilled-labor reproduction failure, not demand collapse — customers still wanted custom coverlets, but no one was training new weavers. The modern revival studio addresses precisely this failure mode: by formalizing an apprentice path, it solves the reproduction problem the frontier itinerant form left unresolved. [Tryon 1917; Vlach 1991; Hood 2003; american-frontier chapter §3, §7–§8]

**American overshot draft-sheet tradition.** The functional inheritance is the draft-catalog operating model: a portfolio of named historical patterns (Rose-and-Diamond, Star-and-Diamond, Whig Rose, Honeysuckle, Federal Star, and the larger overshot vocabulary) that constitutes the studio's product differentiation. The historical frontier professional carried these drafts on paper; the modern studio maintains them digitally or in printed binders, with the same functional role: a customer chooses from the catalog, and the weaver executes the commission to that specification. This is not aesthetic inheritance — it is a specific operational model for managing customer choice in a commission-based single-operator studio. The pattern names themselves carry historical provenance that functions as premium-pricing justification to buyers who are purchasing American textile heritage, not merely a blanket. [Hood 2003; CITATION-NEEDED: draft-sheet documentation for American coverlet weavers; american-frontier chapter §3]

**Shaker communal weaving operation.** The Shaker form is the cooperative-lens precedent. The functional inheritance is limited but real: Shaker production demonstrated that a coordinated communal weaving operation could achieve quality and commercial viability that individual household production could not. The cooperative model in this entry inherits the principle of shared capital (loom ownership) and collective studio access, while abandoning the specific organizational preconditions (communal residence, celibacy, directed labor) that cannot be reproduced. The Shaker form is cited here as an honest comparator for the cooperative-lens evaluation, not as a romantic model: Shaker communal cloth production was commercially viable through mid-century but eventually withdrew from commodity textile production as factory costs fell below the level where communal production provided a quality premium. The coverlet-and-table-linen specialty niche is structurally better positioned than commodity cloth — it is the sector where Shaker production did sustain a premium — but the cooperative form remains marginal rather than good in this entry because the thin journeyman-weaver membership pool at any scale limits the cooperative's robustness. [Stein 1992; american-frontier chapter §3]

## Key assumptions

Capital costs ($8,000–$35,000 range, $18,000 mid) are illustrative estimates derived from orientation-level review of US floor-loom vendor pricing (Schacht, Macomber, Leclerc, Ashford) and commercial studio fit-out cost ranges; no formal vendor bill-of-materials underlies these figures [CITATION-NEEDED]. The lower end of the range ($8,000) reflects a used-loom purchase plus minimal studio investment, which the American frontier precedent supports — the itinerant weaver's loom was a personal capital asset of modest cost within the artisan-equipment range of the period. The mid ($18,000) represents a quality new or like-new 4-shaft loom with humidity management and adequate starting yarn inventory. Market pricing ($60–$350/m linear) is the central economic claim and is explicitly labeled pricing_validation: inferred: it reflects orientation-level review of Etsy studio-weaver listings and general familiarity with US handcraft commission markets but is not sourced from a formal survey or published rate-card [CITATION-NEEDED]. The mid at $130/m is the figure most in need of empirical citation. The industrial baseline ($12/m for a mass-produced throw) is inferred from general knowledge of US big-box retail blanket and throw pricing [CITATION-NEEDED]. Throughput (850 m/yr) is derived from a conservative 4.0 m/day output estimate at 120 cm warp width, 240 effective weaving days, and 10% downtime; the output rate is an illustrative estimate for overshot weaving at journeyman level [CITATION-NEEDED]. The downtime fraction (0.10) is conservative relative to the minimum-event calculation (~0.07) to account for the irregular commission-booking pattern that can create short idle periods between warps. Fiber sourcing (industrial-yarn-purchased, commercial wool) keeps supply-chain complexity minimal; the premium pricing rests entirely on pattern heritage and commission customization, not fiber provenance. This is a deliberate design choice consistent with the historical model: frontier professional weavers adopted factory-spun yarn as soon as it was available and did not return to household-spun as a differentiating input.

## Known risks / failure modes

**Regulatory:** Textile-content labeling under the US Textile Fiber Products Identification Act applies to any finished textile sold retail claiming a specific fiber content (wool, cotton, etc.). A studio selling finished coverlets and table linens must label correctly; mislabeling is an FTC enforcement risk. Flammability testing is generally not required for residential-use commission textiles (coverlets, bed coverings, table linens for personal use); it becomes relevant only if the studio sells into commercial interior applications — not the primary market for this entry. ADA accessibility compliance applies to customer-consultation space if the studio is open to the public, which may require ramp access or layout modification in some commercial spaces.

**Labor pipeline:** The journeyman-weaver skill floor for overshot draft production is a meaningful barrier. The specific vocabulary of American overshot patterns — reading a threading draft, executing tie-up sequences, managing pattern repeats across a full-width wool warp — is not taught in standard vocational programs and is not covered by rigid-heddle-level guild workshops. The hiring pool for a civic or cooperative version of this studio is thin (regional radius likely required); a market-primary version depends on the operator already possessing this skill set. The apprentice path (24–30 months) addresses succession risk but requires an active primary operator committed to mentorship. The historical failure mode of the frontier professional trade — skilled-labor reproduction failure, not demand collapse — is the dominant risk for this entry: if the apprentice path is not actively maintained, the studio's lifespan equals the operator's career.

**Supply chain:** Commercial wool yarn sourced from US textile distributors has a typical 7-day lead time with a worst-case 28-day lead for specialty dye-lot orders. A commission requiring a specific colorway not in stock creates a delivery-gap risk for time-sensitive orders; maintaining a 4–6 week yarn inventory buffer in core colors mitigates this. The humidifier system is a second supply chain risk: residential-grade units have a 5–10 day replacement lead time, during which a wool warp under active production may experience tension instability. Stocking a replacement unit or a reliable service-call relationship with an HVAC contractor is the mitigation. Loom hardware components (heddles, reeds) from loom manufacturers may have 10–21 day lead times for specialty items; standard heddle sets should be kept in on-hand stock.

**Anti-romanticism and market positioning risk:** The primary strategic risk of this entry is misrepresentation of the historical context to customers. The American overshot-coverlet tradition is not a continuous pre-industrial folk craft: it was a commercial response to factory displacement, adopted industrial inputs (factory-spun yarn) as soon as they became available, and disappeared as an active trade within two generations when the apprenticeship mechanism failed. A revival studio that markets itself as a "preserved tradition" rather than a "revived commercial model" invites the romantic framing the historical record does not support and risks alienating customers when the historical complexity is known. The correct market narrative is: this studio uses the same operating model (named draft-sheet catalog, commission production, journeyman skill level) that the frontier professional used — not that it preserves a timeless pre-industrial practice that never was.

## Iteration log

- 2026-04-18: v0.1 — initial authoring per Plan I Task 9 (weave-007). Full v1.1 schema populated; lens_fit market: good / cooperative: marginal / civic: marginal; all three lens_context blocks populated (all triggers met); four-stage apprentice_path at journeyman level for overshot production; three operations_reality first_year_failures items including climate-control failure for humidity_control_required: true; trade_specific block with loom_type, humidity_control_required, fiber_source_declaration, and product_category; sim_params with explicit E3-R2/R3 cross-checks; anti-romantic historical framing of itinerant-weaver economic context documented throughout; pricing_validation labeled inferred throughout per citation policy; 11 CITATION-NEEDED placeholders carried for post-authoring verification. Village-good scale fit documented and justified via low-capital entry and commission-model operation. Industrial-yarn-purchased fiber sourcing confirmed as consistent with historical frontier professional adoption of factory-spun yarn.
