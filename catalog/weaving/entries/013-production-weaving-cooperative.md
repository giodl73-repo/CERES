---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: weave-013
trade: weaving
name: "Production Weaving Cooperative"
tagline: "Worker-owned multi-loom cooperative producing wholesale specialty cloth at volume, testing whether shared overhead restores viability at small-city scale"
status: draft
version: 0.1
supersedes: null
inspirations:
  - lancashire-weaving-shed-cooperative
  - mondragon-textile-cooperative
  - new-england-production-weaving-guilds

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 105
# Mid-range of the 80–130 m² span. Accommodates 6–8 floor-loom-4shaft units in
# production bays (~7 m² per loom including operator and immediate staging area),
# a shared warping station (warp mill, sectional warping board, creel: ~10 m²),
# a wet-finishing area (scouring sink, pressing and blocking table: ~12 m²),
# a display and order-sample showroom (~10 m²), and shared storage for yarn
# inventory and finished cloth. Ceiling height must clear upright loom castles
# plus warping mill overhead.
ceiling_min_m: 3.2
ventilation: mechanical-extraction-required
# Wet-finishing requires local exhaust over the scouring and pressing area
# (steam, residual mordant or scour vapors). Main weaving floor requires
# fresh-air circulation for humidity management across 6–8 active members.
# Mechanical air exchange is required for air quality and fire-code compliance
# with 6–8 concurrent operators; natural ventilation alone is insufficient for
# a full-shift production floor.

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: electric-lighting-only
# All primary productive equipment (floor-loom-4shaft treadle mechanisms) requires
# no powered drive. Energy consumption is: studio lighting for 80–130 m² at full
# occupancy, climate-control system for humidity management (required for wool and
# mixed-natural-fiber warps), electric bobbin winder and yarn winder, and the
# wet-finishing area (electric press, scouring vat hot plate). No three-phase power
# required; standard commercial single-phase electrical service is sufficient.
energy_consumption_per_active_hour: "4–8 kWh (lighting + humidity-control HVAC at steady state; wet-finishing pressing adds ~1–2 kWh/hr during active finishing sessions)"
backup_fuel: null

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  meters_per_day: 9.0
  # Aggregate facility daily output across all active looms.
  # Per-loom rate at twill complexity (journeyman-weaver): 2–4 m/day per loom
  # (per weaving SCHEMA.md §1; Chandler 1995 and REQUIREMENTS.md). Representative
  # mid-estimate: ~3 m/day per loom × 7 looms at production rate (accounts for
  # warping-setup days spread across the week, not all looms producing simultaneously
  # every day). Blended facility rate: ~9 m/day aggregate on active production days.
  # Consistent with spec target of 1,000–3,000 m/yr aggregate.
  # [CITATION-NEEDED: multi-loom cooperative aggregate daily throughput at twill;
  #  derived from weaving SCHEMA.md §1 per-loom range and 7-loom midpoint estimate]
  warp_width_cm: 110
  # Representative warp width for the primary production looms (floor-loom-4shaft,
  # standard 45" or 110 cm weaving width). Wholesale cloth in this warp width
  # serves home-furnishing and apparel yardage markets. Some looms may be set
  # at 90 cm for narrower specialty runs; 110 cm is the production-planning default.
  pattern_complexity: twill
  # 2/2 twill and herringbone are the primary structures for wholesale production
  # fabric; plain weave for utility cloth; overshot and more complex 4-shaft
  # structures for premium specialty runs. Throughput calculations use twill as
  # the baseline (conservative vs. plain weave; realistic vs. overshot).
  max_active_hours_per_week: 50
  # Aggregate facility-wide active weaving hours per week, net of major warping
  # and loom-dressing overhead. Derivation: 7 members × ~35 hr/wk total shop
  # time per member = 245 hr/wk gross; approximately 50 hr/wk is the aggregate
  # net weaving-at-the-loom time after subtracting warping sessions (~4–8 hr/warp),
  # loom dressing, wet finishing, administration, and membership governance time.
  # Warping and loom-dressing overhead is the primary throughput limiter in a
  # multi-warp production cooperative; these hours are productive but not
  # "active weaving hours" in the throughput rate sense.
  # [CITATION-NEEDED: warping and loom-dressing time as fraction of total shop
  #  time for journeyman floor-loom weaver; estimated from REQUIREMENTS.md and
  #  Chandler 1995 at 4–8 hr per warp setup; 7-loom cooperative estimate]
  product_mix:
    yardage: 70
    rugs_upholstery: 15
    tapestry_art: 0
    garments_accessories: 10
    instruction_open_studio: 5
    # Wholesale yardage dominates (70%): cloth sold by the meter to retail stores,
    # interior designers, independent garment makers, and fabric distributors.
    # Rugs and upholstery weight cloth (15%): higher per-unit price, slower throughput;
    # serves contract furnishing and hospitality markets.
    # Garments and accessories (10%): finished scarves, shawls, and small runs at
    # premium price; direct-to-consumer and gift trade channel.
    # Instruction/open studio (5%): minimal; production-primary cooperative;
    # brief member mentorship of apprentices or occasional demonstration day.
    # Sum: 70 + 15 + 0 + 10 + 5 = 100.
  throughput_variance:
    seasonal: "Wholesale B2B demand is relatively non-seasonal; trade-show cycle (January market, August market) drives two ordering peaks annually; retail-channel gift season (Oct–Dec) accelerates wholesale orders for garments and accessories."
    worst_month_fraction_of_average: 0.65
    best_month_fraction_of_average: 1.45

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: journeyman-weaver
# All 6–8 member-weavers must hold journeyman-weaver floor competency: independent
# threading, warp tension management, twill structure execution, and selvedge control
# are required for consistent wholesale cloth production. A production cooperative
# cannot sustain quality control at volume if any member operates below journeyman
# standard; defective cloth in a wholesale run cannot be easily sold off and may
# damage the cooperative's buyer relationships. See weaving SCHEMA.md §5 for
# journeyman-weaver competency boundary.
operators_concurrent: "6-8"
# All member-weavers may operate simultaneously; each manages their own loom
# independently. The cooperative does not operate on a shift model; members schedule
# their own shop hours within cooperative rules, with the production plan coordinating
# warp assignments and order fulfillment across members.
apprentice_friendly: true
apprentice_path:
  training_stages: >-
    Stage 1 — Supervised Floor-Loom Basics (0–6 months): new apprentice assigned to
    an experienced member-weaver as day-to-day mentor; works on a dedicated training
    loom (oldest or second-line loom in the cooperative's fleet). Covers: warp
    calculation and winding, loom dressing and threading on a 4-shaft floor loom,
    plain weave to 2/2 twill, selvedge control, shuttle management, and basic warp-tension
    diagnosis.
    Competency gate: independently thread a 4-shaft floor loom from a standard draft,
    weave 10 meters of 2/2 twill meeting the cooperative's selvedge-and-sett quality
    standard, with no intervention from the mentor.

    Stage 2 — Production Integration (6–18 months): apprentice joins the production
    schedule on simpler warp assignments (plain weave, utility twill); output counts
    toward cooperative throughput targets at a reduced rate. Covers: pattern complexity
    within 4-shaft capacity (herringbone, houndstooth, overshot), warping for longer
    production runs (20+ meter warps), cooperative quality-control protocol
    (cloth inspection, recording defects, wet-finishing basics).
    Competency gate: complete a 25-meter production warp end-to-end (wind, dress, weave,
    wet-finish) at marketable quality, accepted by the cooperative's quality-review member.

    Stage 3 — Full Production Membership Eligibility (18–36 months): apprentice manages
    independent warp assignments on the production schedule; participates in member
    governance as an observer (advisory voice, no vote until full membership). Covers:
    specialty twill structures (networked twill, overshot for premium runs), wet-finishing
    for wholesale (scouring, pressing, edge finishing), basic loom maintenance
    (ratchet pawl inspection, reed damage assessment, heddle replacement).
    Competency gate: journeyman-weaver assessment by two existing member-weavers
    and the cooperative's quality-review protocol; formal vote for full worker-member
    admission per cooperative bylaws.
  time_to_independent_operation: "~18 months to production-schedule participation; ~36 months to journeyman assessment and full worker-member vote"
  succession_note: >-
    Production scheduling integrates apprentice training as a normal operating mode:
    the mentoring member-weaver absorbs the supervision overhead within their production
    hours. The cooperative's written warp-assignment records, quality-control protocol,
    and pattern draft library constitute institutional knowledge that survives any
    single member's departure. A rolling apprentice cohort (typically 1–2 apprentices
    at any time) provides a formal succession pipeline; the cooperative governance rules
    require the member assembly to maintain at least one active apprentice when
    total membership falls below 6 full members.

# ── TRADE-SPECIFIC FIELDS ────────────────────────────────────────────────────

trade_specific:
  loom_type: floor-loom-4shaft
  # Standard production equipment. 6–8 floor-loom-4shaft units are the core
  # capital item; a journeyman-weaver operating a 4-shaft floor loom at 110 cm
  # warp width can execute all required pattern structures (plain, twill,
  # herringbone, overshot) for the wholesale specialty-cloth positioning.
  # 8-shaft looms are not included in the base configuration: the capital premium
  # ($4,000–$15,000 per 8-shaft unit vs. $1,500–$6,000 per 4-shaft unit) is not
  # justified at wholesale twill price points unless a premium networked-twill
  # or fashion-fabric positioning is explicitly adopted (see Known Risks).
  humidity_control_required: true
  # The production cooperative uses wool warps and wool/linen mixed-fiber yarns as
  # the primary specialty-positioning material (see fiber_source_declaration and
  # Key Assumptions). Wool warp is humidity-sensitive: RH below 40% causes warp
  # breakage and tension instability; RH above 65% causes blooming and blocking
  # problems in finished cloth. Target RH 45–55% is required for consistent
  # production quality. Climate-control system is a required capital item;
  # see Key Assumptions for HVAC cost disaggregation.
  fiber_source_declaration: industrial-yarn-purchased
  # The cooperative purchases commercially spun yarn from regional or national
  # distributors: wool, wool-cotton, wool-linen, and occasional specialty yarn
  # (mohair, silk blend) for premium runs. Industrial-yarn-purchased is the correct
  # declaration: the cooperative has no spinning operation and maintains no direct
  # sheep-to-loom supply chain. Specialty yarn (premium wool, natural-dyed) may
  # be sourced from a limited pool of distributors; this is documented as a supply-chain
  # risk below. The specialty-cloth positioning rests on pattern complexity, production
  # quality, and B2B channel discipline — not on heritage-fiber provenance.
  # See Group C SCHEMA guidance and DECLINE-VERDICT notes.
  annual_coop_dividend_pool: 0
  # Placeholder field (trade_specific namespace). Actual dividend pool is
  # derived from annual revenue net of operating costs and reserve contributions;
  # computed at simulation time from sim_params and market_price_per_unit.
  # Documented here as a named cooperative-governance concept per lens_context.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 45000, mid: 90000, high: 150000 }
  # Low ($45,000): 6 used floor-loom-4shaft units + basic warping station + minimal
  #   wet-finishing setup + modest showroom fit-out.
  # Mid ($90,000): 7 new floor-loom-4shaft units ($2,500–$5,000 each, mid-grade studio
  #   looms; Schacht, Leclerc, or Macomber equivalent) × 7 = $21,000–$35,000; warping
  #   station (warp mill, creel, sectional warping board) = $2,000–$5,000; wet-finishing
  #   area (stainless scouring sink, industrial pressing board, steam press or blocking
  #   equipment) = $4,000–$8,000; commercial humidity-control system = $5,000–$12,000;
  #   showroom display and sample library fit-out = $3,000–$7,000; studio fit-out
  #   (lighting, shelving, yarn storage, signage, safety) = $5,000–$10,000; cooperative
  #   formation costs (legal, bylaw drafting, worker-coop registration) = $3,000–$5,000.
  # High ($150,000): 8 high-specification looms (Macomber or AVL equivalent),
  #   professional wet-finishing with commercial press, full climate-control HVAC,
  #   purpose-built showroom, and professional cooperative formation with legal counsel.
  # [CITATION-NEEDED: floor-loom-4shaft capital cost — equipment retailer pricing
  #  (Schacht Spindle Co., AVL Looms, Leclerc Industries, Macomber Looms) for
  #  mid-grade production-quality 4-shaft studio looms, 2024–2025]

  install_cost: 12000
  # Covers: humidity-control HVAC installation for 80–130 m² studio, wet-finishing
  # area plumbing (floor drain, scouring sink), electrical service upgrade for
  # climate-control load plus multi-station power needs, and studio fit-out
  # (loom bay markings, storage shelving, showroom build-out). Rough estimate;
  # actual cost varies with building condition and jurisdiction.
  # [CITATION-NEEDED: HVAC, plumbing, and electrical installation cost for
  #  equivalent commercial studio footprint; derived from trade-cost estimators]

  annual_maintenance: 6000
  # Multi-loom production facility: heddle replacement across 7 looms (~$400/yr);
  # reed replacement or repair (~$350/yr); treadle tie-up cord renewal (~$200/yr);
  # warp-beam ratchet and pawl service (~$500/yr across 7 looms); HVAC filter
  # replacement quarterly and annual HVAC service contract (~$1,200/yr);
  # wet-finishing equipment maintenance (scouring sink, press, drain) (~$500/yr);
  # general studio maintenance (lighting, safety equipment, shelving repair) (~$500/yr);
  # miscellaneous first-year failure remediation reserve (~$1,350/yr).
  # [CITATION-NEEDED: annual maintenance estimate for comparable multi-loom
  #  production studio; no published benchmark identified; derived from per-item
  #  estimates in weaving literature and SCHEMA §7 reference list]

  annual_consumables: 8400
  # Warping yarn stock for sample and start-up warps (~$2,400/yr; production yarn
  # is billed to job cost, not here); heddle sets (annual replacement on high-use
  # looms: ~$600/yr); reed replacement cycle (~$500/yr); treadle cord stock
  # (~$200/yr); wet-finishing supplies (scour, softener, pH test, edge treatments)
  # (~$1,200/yr); threading accessories (lease sticks, raddle, temple replacement)
  # (~$400/yr); packaging for wholesale delivery (tissue, core tubes, labels) (~$600/yr);
  # office and sample-library supplies (~$500/yr); humidity-control system consumables
  # (filters, demineralized water for humidifier) (~$400/yr).
  # [CITATION-NEEDED: weaving cooperative annual consumables estimate; derived from
  #  per-item supply catalog pricing; no multi-loom coop published benchmark identified]

  floor_space_rent_per_year: 14400
  # Imputed at small-city light-commercial rate: ~110 m² × $130/m²/yr.
  # Small-city light-commercial/arts-district rate estimated at $100–$160/m²/yr;
  # $130/m² is the mid-point estimate for a modest commercial space with standard
  # services. Worker-cooperative ownership of the building would reduce this to $0
  # plus amortized acquisition cost; leased space is the base case.
  # [CITATION-NEEDED: light-commercial lease rate per m² for small-city markets
  #  in the US, 2024–2025; $130/m²/yr is a rough estimate from commercial real
  #  estate data; requires local-market validation at implementation]

  market_price_per_unit: { low: 40, mid: 100, high: 250 }
  # Per linear meter of wholesale specialty cloth.
  # Low ($40/m): commodity-adjacent twill, sold to fabric distributors or
  #   cut-and-sew operations on thin margin; plain weave utility cloth.
  # Mid ($100/m): specialty wholesale twill — herringbone, houndstooth,
  #   wool-cotton blend — sold to independent retailers, interior designers,
  #   and independent clothing labels; craft-fair and direct-to-consumer yardage.
  # High ($250/m): premium handwoven cloth (fine wool, overshot or networked-twill
  #   structures, high-end interior fabric) sold to boutique retailers, upholstery
  #   specifiers, and luxury fashion makers.
  # Industrial baseline ($12/m): commodity industrial plain-weave cotton or
  #   synthetic-blend equivalent from domestic importers.
  # [CITATION-NEEDED: wholesale handwoven specialty cloth market price per meter;
  #  ranges derived from fiber arts trade survey estimates and comparable Etsy/
  #  craft-fair wholesale pricing; no single published benchmark identified]

  pricing_notes: >-
    Unit is one linear meter of wholesale specialty cloth at 110 cm warp width.
    Premium over industrial baseline ($12/m for commodity plain-weave cotton or
    poly-blend from commercial importers) is justified by: (1) material quality
    (wool, linen, and specialty blends not available in commodity industrial cloth),
    (2) pattern complexity (twill structures, herringbone, overshot unavailable at
    industrial scale in small-run specialty colorways), (3) short-run flexibility
    (buyer can specify colorway and structure for minimum orders of 20–50 m, which
    industrial mills cannot profitably fulfill). Primary customer segments: independent
    clothing designers (20–100 m orders), interior design studios (upholstery and
    drapery cloth, 10–50 m orders), specialty fabric retailers (consignment and
    wholesale accounts), and direct-to-consumer craft fair and online channels
    (scarves, accessories at the high end of the range). The cooperative's survival
    depends on sustaining the $100/m mid price point; at $40/m the margin is
    insufficient to cover rent and consumables without member dividend sacrifice.

  industrial_baseline_price: 12
  # Commodity plain-weave cotton or synthetic-blend equivalent from domestic
  # fabric importers and wholesale distributors, per meter at 110 cm width.
  # [CITATION-NEEDED: US wholesale commodity fabric price per meter, standard
  #  cotton or poly-blend plain weave, 110 cm width, 2024–2025; estimated from
  #  domestic distributor price lists; requires confirmation]

  pricing_validation: >-
    Market price evidence: handwoven specialty cloth pricing ranges are drawn from
    craft-trade survey estimates and comparable Etsy wholesale-tier and Faire platform
    pricing for handwoven fabric (wool twill, herringbone) from US-based production
    cooperatives and small studios. The $40–$250/m range covers the actual observed
    range from discount utility cloth to luxury interior-design-grade handwoven fabric.
    The $100/m mid is supported by comparable wholesale rates for journeyman-quality
    wool-blend handwoven yardage from regional US producers. [CITATION-NEEDED:
    formal trade survey or comparable operator financials for US handwoven specialty
    cloth wholesale pricing; Etsy/Faire platform pricing is indicative, not a formal
    industry survey; replace with Handweavers Guild of America market survey or
    comparable trade association data before status promotion]

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:

  first_year_failures:
    - item: "Heddle breakage (wire heddles, floor-loom-4shaft × 7 units, production intensity)"
      estimated_hours_to_failure: 600
      # Production-intensity multi-member operation: wire heddles under continuous
      # use across 7 looms, with journeyman-level operators executing production
      # warp changes 2–3 times per month per loom. First failure expected within
      # 600 aggregate active hours (~12 weeks at 50 hr/wk net). Spot heddle
      # replacement is frequent and treated as a consumable; bulk set replacement
      # (all 4 shafts on one loom) is the first-year capital event.
      replacement_cost: 140
      # Wire heddle set for one shaft on a floor-loom-4shaft: ~$30–40 × 4 shafts
      # = $120–160 per full set. Spot replacement is lower; first full-set event
      # estimated at $140 mid.
      replacement_lead_time_days: 5
      serviceable_by: operator
      # Re-threading after heddle replacement is operator-level; takes 2–4 hours
      # per shaft on a floor loom. No specialist required.

    - item: "Warp beam ratchet / pawl wear (first floor loom to fail)"
      estimated_hours_to_failure: 2000
      # Per-loom aggregate hours at first failure (not facility aggregate): the
      # first ratchet-and-pawl failure is expected in the loom with highest
      # individual utilization. At ~50 hr/wk facility aggregate ÷ 7 looms =
      # ~7 hr/wk per loom average; first failure at 2,000 per-loom hours ≈
      # year 5.5, but some looms will exceed average use; expect first occurrence
      # within 3–4 years under production conditions. Listed as first-year
      # failure in the sense of "first occurrence across the fleet in the
      # early operating period."
      replacement_cost: 220
      replacement_lead_time_days: 12
      serviceable_by: journeyman
      # Ratchet pawl spring replacement is journeyman-level; full ratchet
      # replacement requires disassembling the warp beam assembly.

    - item: "Climate-control humidifier system failure"
      estimated_hours_to_failure: 2200
      # Commercial humidifier under continuous load in an 80–130 m² production
      # studio occupied full-time by 6–8 weavers generating body-heat moisture
      # load. First-year failure probability is significant for any residential-scale
      # unit; commercial unit failure within the first two operating years is
      # documented [CITATION-NEEDED]. Warp tension and production quality are
      # immediately affected by humidity loss.
      replacement_cost: 900
      replacement_lead_time_days: 10
      serviceable_by: specialist
      # Central commercial HVAC humidifier component requires specialist diagnosis
      # and replacement; a standalone portable backup unit is operator-deployable
      # as a bridge measure (cost ~$300; should be kept as operational continuity
      # equipment).

    - item: "Reed damage (bent dents) on high-production loom"
      estimated_hours_to_failure: 1800
      # Production-intensity beating on a 12-dent or 15-dent reed at full warp
      # width; first bent-dent failure expected within 1,800 production hours on
      # the highest-use loom. A bent dent creates a streak in the cloth that
      # renders the warp section unmarketable at wholesale grade.
      replacement_cost: 95
      replacement_lead_time_days: 8
      serviceable_by: journeyman
      # Reed replacement requires re-sleying the entire warp; journeyman-level
      # task, 3–6 hours per replacement on a full-width production warp.

  maintenance_schedule:
    daily:
      task: "End-of-shift walkdown: inspect warp tension and heddle condition on all active warps (operator responsible for their own loom); humidity and temperature log entry; wet-finishing area drain and vat check; yarn inventory spot-check if a warp is scheduled to start the next day"
      performed_by: operator
      # Each member-weaver is responsible for their own loom's daily check
      # within the cooperative's quality protocol. The cooperative's floor
      # manager (elected annually) performs a facility-level walkdown at
      # session open.

    weekly:
      task: "Collective maintenance session (scheduled 1 hr/wk): treadle tie-up cord inspection on all looms, reed alignment and bent-dent check across all active reeds, warp-beam ratchet function test, rigid-heddle slot wear check on supplementary equipment, humidity-control filter visual inspection, warping station creel and tensioner check, wet-finishing area full clean and pH-test equipment check"
      performed_by: operator
      # The weekly collective maintenance session is a cooperative governance
      # norm: all members present one hour per week for shared equipment
      # care. This is factored into the member time commitment and max_active_hours
      # derivation; it reduces production hours but prevents equipment deterioration
      # under multi-user conditions.

    quarterly:
      task: "Comprehensive equipment service: ratchet/pawl inspection and lubrication on all 7 looms, bulk heddle inventory count and replacement order trigger, HVAC filter replacement, wet-finishing vat and scouring-sink descale, fire-suppression check, cooperative book review (financial audit by elected treasurer), patron and wholesale-account relationship review"
      performed_by: journeyman
      # Quarterly service is performed by the most experienced member-weavers
      # collectively; no outside specialist required for loom-level service.
      # HVAC service at this interval is operator-level (filter change only);
      # the annual HVAC inspection requires specialist.

    annual:
      task: "Full facility inspection: structural loom-frame joint assessment across all units, warp and cloth beam inspection for warping or cracking, HVAC system annual service (specialist contract), electrical panel review and insurance compliance walkthrough, cooperative governance review (annual general meeting, bylaw review, member vote on rule amendments), quality-protocol review and pattern draft library update"
      performed_by: specialist
      # Annual HVAC service requires a licensed HVAC technician. All other annual
      # tasks are performed by member-weavers collectively (loom frame and beam
      # inspection) or by the elected officers (governance and compliance).

  startup_shutdown_overhead_per_day_min: 30
  # Per-session overhead per active member: 10 min loom readiness check and warp
  # tension adjustment at session start, 10 min shuttle cleanup, bobbin winding
  # station reset, and cloth-beam advancement log at session end, 10 min quality
  # and clip-and-fold check on any completed sections. This is a cooperative
  # production floor, not a casual studio: quality documentation and loom handoff
  # discipline are required for B2B wholesale orders.

  max_active_hours_realism_note: >-
    The max_active_hours_per_week of 50 is the facility's aggregate net active weaving
    hours per week — not the theoretical ceiling. Derivation: 7 members × ~35 hr/wk
    total shop time (full-time working member commitment) = 245 hr/wk gross. Of that,
    approximately 80% is spent on loom-adjacent non-weaving tasks: warping and loom
    dressing (~4–8 hr per warp per member, 2–3 warps/month = ~15–24 hr/month per
    member on warping), wet finishing (0.5–1 hr per production run), cooperative
    administration (governance meetings, sales, quality review: ~2 hr/wk per member),
    and the weekly collective maintenance session (1 hr/wk per member).
    Net loom-weaving hours: 245 × (1 − 0.80) = ~49 hr/wk aggregate ≈ 50 hr/wk.
    This is the gross figure; sim_params derate further for downtime (0.12).
    Effective annual hours: 50 × 52 × (1 − 0.12) = 2,288 hr/yr.

  interruption_notes: >-
    In a production cooperative, intraday interruptions are lower per-member than in a
    supervised public studio (weave-010), but coordination overhead replaces member-
    supervision overhead. Typical interruptions per member per day: warp-related tension
    or broken-end problem diagnosis (~10–15 min, 1–2 occurrences); shuttle or reed
    consultation with another member on a quality or sett question (~5–10 min);
    order-management or wholesale-buyer communication (email/call, ~15 min/day for
    the member-weaver handling sales in a given week). These are folded into the warping-
    and-overhead reduction in max_active_hours_per_week derivation above and into the
    downtime_fraction.

  consumables_lead_time_days: { typical: 7, worst: 35 }
  # Typical: standard weaving hardware (heddles, reeds, tie-up cord, threading
  # accessories) from regional weaving suppliers or online distributors.
  # Worst: specialty yarn (premium wool, mohair, silk blend) from limited
  # distributor pool; non-standard reed setts; HVAC system components. 35-day
  # worst case covers a documented single-supplier specialty-yarn backorder scenario
  # that can halt a specific warp pattern without substitute sourcing.

  throughput_variance:
    seasonal: "Wholesale B2B demand is relatively non-seasonal; trade-show ordering cycle (January and August markets) drives moderate biannual peaks; gift-season retail orders (Oct–Dec) accelerate the accessories and garment-cloth portion of the mix."
    worst_month_fraction_of_average: 0.65
    best_month_fraction_of_average: 1.45

  operator_impact:
    noise_db: 62
    # Floor-loom production: rhythmic beater impact, treadle mechanism, and shuttle
    # throw; estimated 58–65 dB(A) at operator position in a 7-loom production studio
    # with hard flooring and minimal acoustic treatment. Below OSHA 8-hour TWA action
    # level (85 dB) by a wide margin; sustained conversation is possible; compatible
    # with a full production workday. [CITATION-NEEDED: floor-loom noise level
    # measurement in a multi-loom production environment; estimated from single-loom
    # acoustic data in weave-010 and production-floor scaling factor]
    heat_exposure: "Low to moderate; no open-flame or high-heat source; humidity-control system maintains a comfortable working environment; wet-finishing pressing operation (steam press) produces localized heat and steam at the finishing station, not at the weaving floor"
    emissions: "No significant air emissions from weaving or dry fiber handling; wet-finishing scour and rinse baths (non-ionic scour agents, mild acid rinse) require pH-neutral drain disposal; no synthetic dye VOCs at standard production cooperative scale with purchased pre-dyed yarn; fabric pressing produces minimal steam vapor"
    physical_demand: "Moderate: sustained seated treadling with repetitive upper-body shuttle and beater motion for 6–8 hours per day; warping is standing work with significant arm and shoulder loading (winding a production warp requires 30–60 min of continuous mill-winding); wet finishing involves lifting and handling wet cloth (up to 5–8 kg per run); long-term repetitive strain risk for wrist, shoulder, and lower back documented in production weaving"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Light-industrial or mixed-use commercial zoning required; floor-loom production cooperative is a light manufacturing use in most jurisdictions; confirm with local zoning authority that 6–8 simultaneous operators and a showroom are permitted under the target building's occupancy classification; arts-district or creative-economy overlay zoning, where available, provides the most permissive path"
  emissions: "No air-permit trigger from floor-loom weaving or purchased pre-dyed yarn at this throughput; wet-finishing drain discharge (non-ionic scour, mild acid rinse) requires pH-neutral disposal under most municipal sewer pretreatment rules — confirm with local POTW before committing to a building with floor-drain discharge; no hazardous-waste classification expected for standard wool scour agents"
  other: "Worker-cooperative formation requires legal entity registration (state LLC or LCA depending on jurisdiction); worker-cooperative-specific legal counsel strongly recommended during formation; humidity-control HVAC installation requires mechanical permit; showroom component may require certificate of occupancy for retail occupancy in addition to the production floor; check local fire code for maximum simultaneous occupancy on 105 m² production floor"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: good
  # Production volume and B2B wholesale channel make the market lens the
  # primary evaluation mode. At $100/m mid price × 2,000 m/yr = $200,000
  # gross revenue; with shared overhead across 7 members, per-member gross
  # contribution is ~$28,600/yr before operating costs. The question is
  # whether the $100/m wholesale price is achievable and sustainable; this
  # is the critical dependency. Market lens good with specialty-cloth
  # positioning; market lens fail if commodity-cloth pricing ($40/m) prevails.
  cooperative: good
  # Worker-cooperative primary structure. Ostrom-compliant governance,
  # full dividend distribution, and documented member-amendment process.
  # This entry is the cooperative lens anchor for the weaving catalog at
  # production scale.
  civic: marginal
  # The cooperative's primary function is private production and member
  # livelihoods; civic externalities are limited compared to weave-010.
  # Civic lens is marginal: a municipal government might provide startup
  # grant funding, subsidized lease of a town-owned industrial property,
  # or economic-development support, but direct civic operation is not the
  # primary model. See lens_context.civic for the marginal case.

scale_fit:
  village: poor
  # Insufficient demand base for 6–8 looms of wholesale production at village
  # scale (500–2,000 residents); no B2B wholesale buyer concentration within
  # practical logistics range; cooperative membership pool too small for
  # worker-coop viability at 6–8 weavers.
  town: marginal
  # Possible at larger town scale (10,000–15,000 residents) with strong regional
  # craft-market presence and established wholesale buyer relationships; but
  # cooperative governance becomes thin when the skilled-weaver pool is limited.
  # Lease costs in small towns may partially offset lower demand risk.
  small_city: good
  # Target scale. Small-city population (15,000–75,000) provides: sufficient
  # skilled-weaver recruitment pool for 6–8 worker-members; accessible B2B
  # wholesale buyers (regional fabric retailers, interior designers, boutique
  # clothing labels within 1–3 hour logistics radius); commercial lease market
  # with appropriate light-industrial space; civic economic-development interest
  # in supporting artisan production businesses.

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:

  cooperative:
    membership_boundary: >-
      Worker-member eligibility is limited to journeyman-level weavers who have
      completed the cooperative's 36-month apprentice path or who can demonstrate
      equivalent competency by journeyman assessment from two existing members.
      Geographic boundary: no formal residence requirement, but practical membership
      assumes commuting distance to the cooperative's studio (typically 30–45 minute
      radius in a small-city context). Member count is capped at 10 full worker-members
      by the founding bylaws to preserve the cooperative's character as a small-scale
      production unit; expansion beyond 10 requires a 3/4 supermajority vote at a
      special general meeting. Non-member apprentices (1–2 at any time) participate
      in production but do not vote or receive dividends until full member admission.

    rules_source: >-
      Worker-cooperative bylaws adopted at founding by all charter members, filed
      with the state cooperative corporation registry (or LLC operating agreement for
      jurisdictions without a dedicated cooperative statute). Bylaws govern: member
      admission criteria, production schedule and warp-assignment process, quality
      control protocol, dividend distribution formula and reserve fund policy,
      member exit and buyout terms, apprentice admission and progression standards,
      and governance meeting cadence. Bylaws are posted in the studio and provided
      to all apprentices at admission. Amendments require a member vote at the
      annual general meeting per the member_amendment_process below.

    monitoring: >-
      Production tracking: each member records completed meters per warp per day
      in the shared production log (paper or digital; must be legible and auditable).
      Quality review: completed cloth is inspected by the designated quality-review
      member (rotating quarterly responsibility) before folding and labeling for
      wholesale delivery; defects recorded and attributed. Financial monitoring:
      elected treasurer maintains income and expense ledger, reviewed monthly by all
      members; annual external review or audit at member discretion. Equipment
      condition log: maintained in the studio; each member signs off on their loom's
      daily condition check. Governance monitoring: member meeting attendance required
      at minimum 75% of scheduled meetings for retention of full voting rights.

    graduated_sanctions: >-
      Quality violations (cloth submitted below standard, defects not declared):
      Written notice → quality review suspension (cloth must pass dual-member review
      for 60 days) → reduced dividend share for affected production quarter (30%
      reduction) → membership review.
      Equipment neglect (loom damage not reported, maintenance task skipped without
      notice):
      Verbal notice (recorded) → written warning → cost-recovery charge for
      remediation + 15% dividend reduction for the quarter → membership review.
      Production shortfall (persistent failure to meet individual production target
      without approved leave):
      Monthly check-in conversation → formal performance review by member assembly
      → probationary status (90 days; production target monitored monthly) →
      membership review with possibility of voluntary exit negotiation.
      Governance non-participation (attendance below 75%, decisions blocked without
      good cause):
      Reminder notice → advisory-voice-only status until attendance restored →
      membership review.
      Membership review is conducted at a special general meeting with full member
      vote (2/3 required for involuntary exit); exit terms are governed by the
      buyout clause in the bylaws.

    conflict_resolution: >-
      Day-to-day production disputes (warp-assignment priority, loom-time scheduling
      conflicts, quality-attribution disagreements) are resolved by the elected floor
      manager with authority to issue binding production-schedule decisions within
      the same working week.
      Member-vs-member disputes not resolved at floor-manager level are escalated to
      a full member meeting with a 14-day convening notice; decision by majority vote
      with the disputing member(s) excluded from the relevant vote.
      Disputes involving the floor manager role itself are escalated directly to the
      full member meeting.
      External disputes (wholesale buyer complaints, supplier disagreements, legal
      matters) are handled by the elected cooperative representative (sales and
      external relations role) with authority to negotiate settlements up to $5,000;
      above that threshold, full member vote required.
      A structured mediation process (external mediator agreed by all parties) is
      available for any dispute that cannot be resolved by member vote within 30 days.

    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6, 7, 8]
    # Principle 1 (clear boundaries): membership limited to journeyman-assessed
    #   weavers; cap of 10 full members; apprentice status clearly distinguished
    #   from full membership; no open-access ambiguity.
    # Principle 2 (congruence): production rules (warp assignment, quality protocol)
    #   calibrated to wholesale B2B market requirements; dividend formula reflects
    #   actual production contribution.
    # Principle 3 (collective choice): all members can propose bylaw amendments;
    #   annual general meeting is the primary decision-making venue; emergency
    #   process available.
    # Principle 4 (monitoring): daily production logs, quality-review rotation,
    #   and monthly financial review create a comprehensive monitoring structure.
    # Principle 5 (graduated sanctions): four-level sanction structure above.
    # Principle 6 (conflict resolution): floor manager, member meeting, and
    #   external mediation hierarchy above.
    # Principle 7 (nested enterprises): cooperative is embedded in the local
    #   small-city artisan economy; wholesale buyer relationships and supplier
    #   agreements connect it to larger commercial structures; civic economic-
    #   development programs may provide nesting support.
    # Principle 8 (external recognition): state-registered worker cooperative
    #   (or LLC with cooperative operating agreement) provides external legal
    #   recognition; municipal economic-development acknowledgment adds civic
    #   legitimacy.

    member_amendment_process: >-
      2/3 vote of full members at the annual general meeting; 30-day advance written
      notice of proposed amendments required, with written rationale circulated to
      all members. Emergency amendments (safety-critical or compliance-related) may
      be enacted by 3/4 vote at a special general meeting convened with 7-day notice.
      Amendments to the member cap, dividend formula, and buyout terms require 3/4
      vote at the annual general meeting. No member may unilaterally amend or
      override a bylaw provision; founding member override rights are explicitly
      prohibited in the cooperative charter.

    legal_form: >-
      State-registered worker cooperative corporation or worker-cooperative LLC,
      depending on jurisdiction. Preferred: a state with a dedicated cooperative
      corporation statute (e.g., California AB 816, Colorado, Massachusetts, or
      Oregon worker cooperative statutes) providing legal recognition and liability
      protection for the worker-member structure. Alternatively, a multi-member LLC
      with a comprehensive worker-cooperative operating agreement (exit rights, buyout
      formula, voting structure, and dividend distribution documented). Worker-coop-
      specific legal counsel required at formation; a template-only approach without
      counsel creates governance ambiguity that is a documented cooperative-failure
      mode. External recognition via state registry satisfies Ostrom Principle 8.

    scale_fit_note: >-
      Governance rules calibrated for small-city scale (15,000–75,000 residents)
      with a 6–10 member worker cooperative. At this scale, a journeyman-weaver
      recruitment pool of 10–20 candidates exists within a reasonable commuting
      radius, supporting the membership cap and the apprentice pipeline.
      At village or small town scale, the skilled-weaver pool shrinks below the
      cooperative's minimum viable membership (6 members), and the member-cap of
      10 becomes binding before natural governance load limits apply.
      At large-city scale, the cooperative model remains viable but the production
      niche faces greater competition from other specialty cloth producers; the
      governance rules do not need structural adjustment for larger cities, only
      market-positioning refinement.

  civic:
    political_coalition: >-
      Economic development department (small-business and artisan-economy support
      mandate); workforce development board (skilled-trades apprenticeship pipeline);
      arts council (cultural economy and creative-sector employment). Secondary:
      small-business association (locally owned enterprise alignment); regional
      craft and fiber arts guild network (technical validation and buyer referrals).
      Primary civic ask is typically a subsidized lease on a town-owned industrial
      property or a small-business startup grant; not direct municipal operation.

    council_vote_estimate: >-
      4-3 to 5-2 favorable in economically development-minded small-city councils
      where the case is framed as job creation and artisan economy support rather
      than arts subsidy. Primary opposition argument: "private cooperative should
      not receive public subsidy; market should allocate." Countered by: the
      cooperative's seven living-wage jobs, apprenticeship pipeline (workforce
      development), and the $0 ongoing municipal operating cost (the cooperative
      self-funds after any startup grant). Swing vote typically responds to the
      job-creation framing and the cooperative's legal status as a legitimate
      private business seeking economic development support — not charity.

    competes_with_private: >-
      The production weaving cooperative competes directly with other wholesale
      handwoven-cloth producers in the region. The civic case must acknowledge this:
      civic support (startup grant, subsidized lease) gives the cooperative a
      competitive advantage over a purely private weaving studio. The justification
      is: (1) the cooperative form produces seven living-wage jobs rather than one
      owner's income; (2) the apprenticeship pipeline has a public-goods character
      that a sole-proprietor studio cannot sustain; (3) economic-development subsidy
      for a worker-cooperative is standard practice under small-business and
      community-development finance frameworks, not a market distortion.
      If an existing private weaving studio already serves the target market, the
      civic body must assess whether the cooperative adds genuinely new production
      capacity or simply displaces the existing operator; this assessment should be
      part of the economic-development review and is not answered here generically.

    governance_form: >-
      Privately owned by its worker-members; civic body (municipality or economic
      development authority) may hold a minority non-voting observer seat on the
      cooperative's board as a condition of startup grant funding. The cooperative
      operates under its own bylaws and is fully self-governing; the civic body
      does not control operations. Governance form: worker-cooperative corporation
      with an elected board (all members) and rotating officer roles (floor manager,
      treasurer, external relations representative, quality-review coordinator).

    budget_line: >-
      Capital: potential one-time economic-development startup grant ($25,000–$50,000)
      or subsidized lease arrangement on a town-owned property. No ongoing municipal
      operating cost; the cooperative is self-financing after startup. Grant funding
      may be available through US Small Business Administration (SBA) cooperative
      development programs, USDA Rural Development (in eligible communities),
      or state cooperative development funds. [CITATION-NEEDED: SBA and USDA
      cooperative development grant availability and typical award amounts, 2024–2025]

    benchmark_comparison: >-
      At small-city scale (12,000 households as representative mid-point of
      15,000–75,000 residents at 2.5 persons/household):
      One-time startup grant of $40,000 ÷ 12,000 hh = $3.33/hh (one-time, not
      annual). Annual municipal cost after startup: $0 (cooperative is self-funding).
      Amortized over 20 years: $0.17/hh/yr equivalent.
      Benchmark: per corpus/program/SCALES.md §3, municipal small-business
      development programs typically spend $5–$25/hh/yr on economic-development
      grants and incentives [CITATION-NEEDED: SCALES.md §3 small-city economic-
      development spending benchmark]. At $0.17/hh/yr amortized, this facility
      represents a very low-cost economic-development investment per household —
      well within the civic service cost continuum for job-creation programs
      producing seven living-wage jobs.

    staffing_model:
      role: "7 worker-members (owner-operators); no municipal staff"
      operator_fte: 7.0
      # All 7 member-weavers are full-time owner-operators. This is not municipal
      # staffing; it is the cooperative's worker-membership. The civic body
      # employs no staff for this facility.
      wage_assumption: 38000
      # Per-member gross income from cooperative dividends, estimated at
      # $38,000/yr at mid-price ($100/m) and 2,000 m/yr aggregate throughput:
      # $200,000 gross revenue − $28,800 operating (maintenance + consumables) −
      # $14,400 rent = $156,800 net before reserve; ÷ 7 members = ~$22,400/member
      # before reserve contributions. At ~15% reserve: $22,400 × 0.85 = $19,040/member.
      # This is the base scenario; higher prices or higher throughput improve
      # substantially. $38,000 target requires $100/m at ~3,000 m/yr or $140/m
      # at 2,000 m/yr. The economics are tight at mid assumptions.
      # [NOTE: wage_assumption here represents the cooperative's target member
      # income, not a municipal wage; sourced to SCALES.md §3 small-city artisan
      # wage median as the comparison benchmark]
      wage_source: "corpus/program/SCALES.md §3 small-city skilled-artisan median wage used as comparison benchmark for member income target; not a municipal wage figure"
      hours: "Full-time owner-operator commitment: ~35 hr/wk total shop time per member (weaving + warping + finishing + cooperative administration)"
      hiring_notes: >-
        Member recruitment (not hiring) requires journeyman-assessed weavers
        willing to invest member capital (buyout share) in a worker cooperative
        at small-city scale. The founding cohort is the highest recruitment challenge:
        assembling 6–8 journeyman-level weavers in one metropolitan area who are
        prepared to commit to a worker-cooperative ownership structure simultaneously.
        Experienced cooperatives in other trades suggest that founding cohorts often
        emerge from an existing informal network (weaving guild, community studio
        alumni, shared-studio members) rather than from open market recruitment.
        Apprentice pipeline mitigates long-term succession risk but does not solve
        the founding-cohort challenge.

    civic_externalities:
      - "Living-wage job creation: seven worker-member owner-operator positions at journeyman-weaver skill level, plus 1–2 active apprenticeships at any time; an economic-development outcome that a sole-proprietor studio or a civic facility (weave-010) does not generate at equivalent scale"
      - "Apprenticeship pipeline: rolling 1–2 apprentices receiving structured 36-month journeyman-weaver training within a working production cooperative; the cooperative's production context provides more intensive training than a civic open-studio can offer, producing weavers with wholesale-ready production skills rather than studio-craft skills only"
      - "Specialty-cloth production capacity: a production weaving cooperative maintains a local source of specialty handwoven cloth (wool twill, herringbone, custom colorways at short-run minimums) that is unavailable from industrial textile importers; this capacity is a resilience asset for local designers, upholstery trades, and heritage-fabric customers during supply-chain disruptions"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 90000
  # Equals economics.capital_cost.mid per E3-R1.

  cost_sd: 26250
  # (high − low) / 4 = (150,000 − 45,000) / 4 = 26,250.
  # cost_sd / cost_mean = 26,250 / 90,000 = 0.292; within 0.15–0.50 acceptable
  # range per E3-R5.

  throughput_units_equiv_per_year: 2000
  # Derivation (per weaving SCHEMA.md §1 E-3 guidance):
  # Aggregate net active weaving hours: max_active_hours_per_week (50) × 52 = 2,600 hr/yr gross.
  # Derate for downtime: 2,600 × (1 − 0.12) = 2,288 hr/yr net.
  # Aggregate throughput rate: ~0.875 m/hr (7 looms × ~3 m/day ÷ 8 active weaving
  # hr/day per loom, adjusted for warping days and non-weaving overhead already
  # removed in the max_active_hours derivation: 7 × 3 / 8 / 7 × 50/(245-195) ≈
  # 2,000 m/yr ÷ 2,288 hr ≈ 0.874 m/hr; consistent).
  # Annual throughput: 2,288 hr × 0.875 m/hr ≈ 2,002 m/yr; rounded to 2,000 m/yr.
  # Unit: 1 linear meter of woven cloth at 110 cm warp width.
  # Consistent with spec target of 1,000–3,000 m/yr aggregate across 6–8 looms.

  variable_cost_per_unit: 4.20
  # Direct variable cost per meter:
  # annual_consumables ($8,400) / throughput_units_equiv_per_year (2,000) = $4.20/m.
  # This represents per-unit wear of heddles, reeds, tie-up cord, wet-finishing
  # supplies, packaging, and yarn sampling costs allocated per output meter.
  # Yarn cost for wholesale production is billed to each job and recovered in
  # pricing; it is not included here as it is a pass-through in the B2B channel.

  labor_hours_per_unit: 1.14
  # Effective active hours/yr (2,288) ÷ throughput_units_equiv_per_year (2,000)
  # = 1.14 hr/m. Reflects total member time per output meter including warping
  # and finishing overhead already baked into max_active_hours_per_week.
  # E3-R3 check: 2,000 × 1.14 = 2,280 ≈ 2,288 (within rounding). ✓

  downtime_fraction: 0.12
  # Sources: equipment maintenance and first-year failure events (~4%: heddle
  # replacement across 7 looms, ratchet service, humidifier lead time at
  # ~2,200 hr — approximately 1.9 yr at 50 hr/wk; contributes ~2% in first
  # operating year plus ~2% across the fleet in subsequent years); scheduling
  # gaps and production-coordination overhead (~4%: member leave, warp changeover
  # gaps, seasonal demand lulls); cooperative governance and administrative
  # events not captured in startup_shutdown_overhead (~4%: annual general
  # meeting, quality review sessions, external trade-show attendance, buyer
  # visits). Total: 12%.

  lifespan_years: 20
  # Floor-loom-4shaft units with regular maintenance have a 20–40 year service
  # life [CITATION-NEEDED: floor-loom manufacturer expected lifespan — same
  # citation as weave-010]. 20 years is the conservative planning horizon for
  # a production cooperative where loom intensity is higher than a civic studio;
  # production-intensity use accelerates wear on beams, ratchets, and heddle sets.
  # The cooperative formation costs amortize over the full cooperative lifespan
  # rather than any single loom's replacement cycle.

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
  - ref: "Ostrom, Elinor. 1990. Governing the Commons. Cambridge University Press — design principles for cooperative and commons governance; all eight principles applied in lens_context.cooperative"
  - ref: "Chandler, Deborah. 1995 (rev. 2009). Learning to Weave. Interweave Press — floor-loom throughput ranges at twill complexity, warping overhead time estimates, and loom operation fundamentals"
  - ref: "corpus/program/SCALES.md §3 — small-city skilled-artisan median wage and civic facility per-household cost benchmarks used for member income target comparison and civic benchmark_comparison"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §1 — weaving throughput block structure, per-loom meters_per_day ranges by pattern_complexity, and E-3 cross-check guidance"
  - ref: "catalog/weaving/REQUIREMENTS.md — functional requirements for weaving entries; throughput ranges, loom type capability, operator skill definitions; primary authority for throughput and loom-configuration parameters"
  - ref: "catalog/weaving/DECLINE-VERDICT.md — specialty-cloth positioning requirements; commodity-cloth exclusion; fiber-sourcing falsifier; binding authority for weave-013 specialty argument"
  - ref: "Mondragon Cooperative Corporation — worker-cooperative governance model; dividend distribution, member capital structure, and apprenticeship integration precedent [CITATION-NEEDED: academic treatment of Mondragon cooperative governance applicable to small-scale artisan cooperatives; suggest Whyte & Whyte 1991, Making Mondragon, Cornell ILR Press]"
  - ref: "[CITATION-NEEDED: floor-loom-4shaft capital cost — equipment retailer pricing (Schacht Spindle Co., AVL Looms, Leclerc Industries, Macomber Looms) for production-quality 4-shaft studio looms, 2024–2025; $2,500–$5,000/unit range requires confirmation from current retailer catalogs]"
  - ref: "[CITATION-NEEDED: wholesale handwoven specialty cloth market price per meter — US market 2024–2025; $40–$250/m range requires confirmation from Handweavers Guild of America market survey, Faire platform wholesale pricing, or comparable US production cooperative operator financials]"
  - ref: "[CITATION-NEEDED: US wholesale commodity fabric price per meter — plain-weave cotton or poly-blend, 110 cm width, domestic importer pricing 2024–2025; $12/m industrial baseline requires confirmation]"
  - ref: "[CITATION-NEEDED: multi-loom production cooperative annual maintenance estimate — no published benchmark identified; derived from per-item estimates in weaving literature; requires confirmation from cooperative operator records or trade association cost data]"
  - ref: "[CITATION-NEEDED: light-commercial lease rate per m² for small-city US markets — 2024–2025; $130/m²/yr estimate requires local-market validation from commercial real estate data (CoStar, LoopNet, or local broker survey)]"
  - ref: "[CITATION-NEEDED: floor-loom noise level measurement at operator position in multi-loom production environment — 62 dB(A) estimate derived from single-loom acoustic data in weave-010; multi-loom scaling factor not empirically verified]"
  - ref: "[CITATION-NEEDED: floor-loom expected service life under production-intensity cooperative use — 20-year conservative estimate; manufacturer documentation or cooperative operating records would improve confidence]"
  - ref: "[CITATION-NEEDED: SBA and USDA cooperative development grant availability and typical award amounts for small-scale worker cooperatives in artisan manufacturing, 2024–2025]"
  - ref: "[CITATION-NEEDED: SCALES.md §3 small-city economic-development spending benchmark — $5–$25/hh/yr range for small-business development grants requires confirmation from municipal budget survey]"
  - ref: "Lancashire weaving shed cooperative tradition (19th–20th century UK) — production-loom cooperative precedent; weaver-owned collective production sheds; see Historical Lineage [CITATION-NEEDED: primary historical source on Lancashire cooperative weaving shed structure and governance, e.g., Farnie 1979, The English Cotton Industry and the World Market, Oxford UP]"
---

## Summary

The Production Weaving Cooperative (weave-013) is a worker-owned multi-loom facility housing 6–8 floor-loom-4shaft units operated by an equal number of journeyman-weaver member-owners, producing wholesale specialty cloth for B2B and retail channels at a scale of 1,000–3,000 meters per year. It is the production-scale anchor of the weaving catalog: where earlier Group C entries (weave-009, weave-010) model civic and educational access, and where weave-012 models apprentice training, weave-013 models whether a worker-cooperative structure can generate sufficient shared-overhead economies and production volume to support living-wage member incomes from handwoven cloth in a world where industrial fabric costs $12/m. The entry is small-city primary, cooperative lens good, market lens good with strong qualification: viability is contingent on sustaining the $100/m mid wholesale price point for specialty cloth, which in turn requires credible B2B buyer relationships and a non-commodity product positioning. The cooperative primary structure is not incidental — it is the design's economic mechanism, spreading fixed overhead (rent, HVAC, warping station, showroom, governance) across 7 members and enabling each to specialize within the production division rather than duplicating setup costs as solo operators.

## Design rationale

No other entry in the weaving catalog solves the problem that weave-013 is designed to address: whether production volume through shared overhead can restore economic viability for handwoven cloth that a single studio cannot achieve. weave-001 through weave-005 are market-primary specialty entries at single-studio or atelier scale; they establish that high-price niches exist but do not test whether cooperative production volume changes the economics. weave-009 (rigid-heddle tool library) and weave-010 (community fiber arts center) are access and education models that explicitly reject commercial production. weave-012 (apprentice training cooperative) is education-primary. weave-013 occupies the production niche: it is asking a genuinely different question from any other catalog entry. The specific economic mechanism under test is shared overhead at production scale — the claim that six to eight weavers sharing a studio, warping station, humidity control system, showroom, and governance overhead can produce a combined economics that no single weaver operating a home studio can match, and that this shared overhead is the path to sustainable wholesale pricing below the luxury-market ceiling but above commodity cloth. The DECLINE-VERDICT constraint is central to the design rationale: the cooperative must not produce commodity cloth (where $12/m industrial baseline makes artisan production economically futile) but must produce specialty cloth with a credible non-commodity positioning. This entry documents that argument explicitly and places it as the critical viability dependency.

## Historical lineage

Three precedents inform this design.

**Lancashire weaving shed cooperative (19th–20th century UK).** The Lancashire cotton textile industry produced a distinctive cooperative institutional form: the weaving shed, a purpose-built shared production facility in which individual weaver-operators (typically self-employed or part of small household enterprises) rented loom space and shared the fixed infrastructure of the shed — building, power transmission, warp preparation, and finishing. Some sheds were worker-owned cooperatives; others were company-owned with long-term loom-room tenants. The functional inheritance is the shared-overhead model: the reason weave-013's economics differ from a solo home studio is precisely the Lancashire insight that cloth production requires infrastructure (building, humidity control, warping equipment) whose fixed costs must be spread across multiple looms to be recoverable. What the modern design cannot reproduce: Lancashire weaving was mechanized (power loom), operating in a national industrial supply chain, and the cooperative shed form was viable partly because labor costs were suppressed through piece-rate systems and family labor. The modern production cooperative must pay living wages to journeyman weavers in a context where handwoven specialty cloth competes against industrial fabric, not alongside it. The governance form is also substantially different: 19th-century Lancashire sheds were not Ostrom-compliant commons — they were industrial production arrangements. The inheritance is the infrastructure-sharing economic logic, not the governance or labor structure.

**Mondragon Cooperative Corporation (Basque region, 20th century).** The Mondragon worker-cooperative system, documented by Whyte and Whyte (*Making Mondragon*, 1991), developed a durable institutional form for worker-owned production enterprises: internal capital accounts for each member, democratic governance with graduated voting rights, apprenticeship integration into production, and a reserve fund structure that buffers the cooperative through demand cycles. The functional inheritance for weave-013 is specific: the member-capital buyout structure (new members invest equity, departing members receive buyout at defined terms), the production-contribution-weighted dividend formula, and the governance norm that apprentices participate in production before achieving full member voting rights. What the design does not inherit: Mondragon's scale (hundreds of member enterprises, thousands of workers, internal finance institutions) is not reproducible at a 7-person artisan cooperative. The governance overhead and formal structures that work for Mondragon require adaptation for a small cooperative where all governance is face-to-face and all members know each other personally. The entry's governance design borrows Mondragon's structural logic while scaling it to the face-to-face register.

**New England production weaving guilds (mid-20th century revival).** Mid-century New England weaving guilds (Connecticut, Massachusetts, Vermont) developed cooperative production models in which guild members collaborated on wholesale cloth production for regional markets, sharing pattern drafts, warp contracts, and customer relationships across individual home studios. This form produced shared specialization without shared physical infrastructure — a lighter-weight cooperative form than weave-013. The functional inheritance is the B2B wholesale channel discipline and the pattern-draft library as shared intellectual capital: weave-013 incorporates both as institutional features. What the design does not inherit from the guild model: the guild form relied on member voluntarism and did not enforce production quality standards at a level required for consistent wholesale supply. The production cooperative model replaces guild voluntarism with worker-member accountability structures (quality-review protocol, graduated sanctions) that the guild form did not require.

## Key assumptions

**Capital cost ($45,000–$150,000, mid $90,000).** No published benchmark for a purpose-built 7-loom production weaving cooperative was identified at authoring date. The estimate is built up from equipment pricing: 7 floor-loom-4shaft units at $2,500–$5,000 each (mid-grade new; Schacht Wolf Loom, Leclerc Compact, or equivalent) = $17,500–$35,000; warping station (warp mill, sectional warping board, creel, tensioners) = $2,000–$5,000; wet-finishing area (stainless scouring sink, pressing equipment, blocking and drying setup) = $4,000–$8,000; commercial humidity-control system (HVAC with humidifier/dehumidifier for 80–130 m²) = $5,000–$12,000; showroom display and sample library fit-out = $3,000–$7,000; studio fit-out (lighting, storage, yarn shelving, signage, safety equipment) = $5,000–$10,000; cooperative formation costs (legal, bylaw drafting, state registration) = $3,000–$5,000; contingency and first-year working capital = $5,000–$8,000. All equipment cost figures are flagged [CITATION-NEEDED] and should be replaced with actual procurement quotes before status promotion. The high asymmetry (mid $90,000 is much closer to high $150,000 than low $45,000) reflects the possibility of an all-used-equipment founding cohort versus a purpose-built professional studio; the mid assumes primarily new equipment.

**Wholesale price ($40–$250/m, mid $100/m).** The $100/m mid price point for wholesale specialty cloth is the single most load-bearing assumption in this entry. It rests on the claim that journeyman-level handwoven wool or wool-blend twill at 110 cm width has an established wholesale market at this price point from US-based small producers. The evidence base is indicative (Faire platform wholesale pricing, Etsy wholesale-tier data) rather than formal (trade association survey, published market study). The mid price is achievable in the premium channel but vulnerable to: (1) buyer negotiation pressure in established wholesale relationships; (2) competition from lower-cost handwoven cloth importers; (3) failure to differentiate from commodity fabric at the point of sale. The cooperative's survival at mid assumptions requires holding $100/m or better; the simulation should show that the market lens produces a marginal or fail verdict at the $40/m low-price scenario.

**Throughput (2,000 m/yr).** Derived as documented in sim_params derivation above. The key assumption is the 50 hr/wk aggregate net active weaving hours — the remainder of each member's shop time being consumed by warping, finishing, administration, and governance. The 80% overhead fraction for non-weaving tasks is an authorial estimate based on Chandler 1995 warping time estimates (4–8 hr per warp) and cooperative governance load. Measured throughput data from an operating 7-loom production cooperative would substantially improve confidence in this number. The annual range of 1,000–3,000 m/yr spans the realistic outcome range from low utilization (member absences, prolonged warp changeovers) to high utilization (full production schedule, efficient warp management).

**Member income (~$19,000–$38,000/member/yr).** At mid price ($100/m) and mid throughput (2,000 m/yr): gross revenue $200,000; operating costs (maintenance $6,000 + consumables $8,400 + rent $14,400) = $28,800; net before reserve ~$171,200; less 15% reserve contribution ($25,680) = $145,520 distributable; ÷ 7 members = $20,789/member. This is below the $38,000 target. Reaching $38,000/member requires either 3,000 m/yr at $100/m ($300,000 gross; $271,200 net; $230,520 distributable; $32,931/member — still short), or $140/m at 2,000 m/yr ($280,000 gross; $216,200 distributable; $30,886/member — closer). The economics are tight; the simulation will likely show marginal-to-good on the cooperative lens depending on price assumption, and the $38,000 wage_assumption is aspirational rather than base-case. This is documented as a known risk below.

**Downtime fraction (0.12).** Estimated consistent with a production cooperative that is well-managed but subject to multiple concurrent first-year failure risks. The 12% figure is derived from: equipment failure (~4%), scheduling/demand gaps (~4%), governance overhead (~4%). It is modestly lower than weave-010 (0.13) because the production cooperative does not incur the high administrative overhead of a public-access supervised studio, but higher than a single-operator private studio because multi-loom coordination and cooperative governance add overhead not present in sole-proprietor operations.

## Known risks / failure modes

**Regulatory.** The primary regulatory exposure is the cooperative formation process: worker-cooperative statute availability varies by state, and an inadequately drafted operating agreement creates governance ambiguity that is a documented cooperative-failure mode (Ostrom Principle 3 analog). Jurisdictions without a dedicated cooperative statute require a multi-member LLC with a comprehensive cooperative operating agreement; template-only formation without legal counsel is insufficient and should be treated as a founding-stage showstopper. Secondary regulatory risk: light-manufacturing zoning confirmation is required before committing to a building — a 7-loom production floor occupying 105 m² is a light manufacturing use in most jurisdictions, but arts-district or commercial-only zoning may not permit it. Wet-finishing drain discharge (non-ionic scour, mild acid) requires pre-confirmation with the local POTW; failure to confirm before buildout is a post-opening shutdown risk.

**Labour pipeline.** The founding-cohort assembly problem is the primary labor risk and has no standard mitigation: recruiting 6–8 journeyman-level weavers prepared to simultaneously invest member capital and commit full-time to a new worker cooperative in one metropolitan area is a substantial coordination challenge with no reliable mechanism. The cooperative-business literature documents this as the primary failure mode for worker-cooperative formation in skilled-craft trades: many cooperatives that survive 10+ years began from an existing informal network rather than from open market recruitment. The entry notes this in hiring_notes but cannot fully resolve it in the schema. Secondary labor risk: at the $20,000–$33,000 per-member income range implied by mid-price mid-throughput assumptions, member retention against solo-studio or employment alternatives is a long-term concern; price growth or throughput improvement is required to sustain the cooperative's economic attractiveness relative to alternatives.

**Supply chain.** The specialty-yarn supply chain is the primary material risk: the cooperative's non-commodity positioning depends on access to premium wool, wool-linen, and specialty blend yarns from a limited distributor pool. A 35-day worst-case lead time for specialty yarn represents a genuine production interruption risk; the cooperative should maintain a minimum 60-day working inventory of primary warp yarn for all active production runs. The secondary supply-chain risk is B2B buyer concentration: if 50% or more of annual revenue comes from two or three wholesale accounts, loss of a single major buyer can destabilize the cooperative's economics in a way that a diversified retail channel cannot. Wholesale buyer diversification is a strategic risk-management requirement, not just a sales preference, and should be an explicit governance policy documented in the cooperative's business plan.

## Iteration log

- 2026-04-18: v0.1 — initial creation; weave-013 Production Weaving Cooperative. PRODUCTION-SCALE / COOPERATIVE-PRIMARY / MARKET-GOOD entry per Plan I Task 15 specification. Full v1.1 schema populated: YAML frontmatter with all required and triggered conditional fields; six prose sections. Cooperative lens fully documented (all Ostrom principles 1–8 addressed; worker-coop structure; dividend distribution; four-level graduated sanctions; floor manager and member-assembly conflict resolution; state-registered legal form). Market lens good with specialty-cloth viability dependency explicitly documented. Civic lens marginal with economic-development framing. Member income calculation documented as tight at mid assumptions; income gap between $20,789 base case and $38,000 target flagged as a known risk. Seventeen [CITATION-NEEDED] flags placed over fabricated estimates for capital cost, wholesale pricing, consumables, HVAC, lease rates, noise levels, service life, grant availability, and historical sources. Anti-romantic treatment applied to Lancashire, Mondragon, and New England guild precedents. Group C SCHEMA guidance and DECLINE-VERDICT specialty-positioning requirements addressed explicitly.
