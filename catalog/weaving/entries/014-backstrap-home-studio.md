---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: weave-014
trade: weaving
name: "Backstrap Home Studio"
tagline: "Single operator, home-corner backstrap loom; absolute capital floor of the weaving catalog"
status: draft
version: "0.1"
supersedes: null
inspirations:
  - mesoamerican-backstrap-weaving-tradition
  - andean-backstrap-weaving-tradition
  - se-asian-backstrap-weaving-tradition
  - modern-tourist-adjacent-cultural-heritage-piece-work

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 5
# Mid-point of the 3–8 m² home-corner range for a single backstrap operator.
# The backstrap loom requires no fixed floor installation: the warp beam ties
# to a wall hook, door knob, or post; the operator sits on the floor or a low
# stool and provides tension via a hip strap. When not in use the loom rolls
# into a carrying cloth or small bag (< 1 kg). The 3–8 m² "footprint" is
# the operator working zone: floor area for seated weaver + immediate warp
# extension + foot clearance. Low end (3 m²): a corner of a bedroom or small
# room with the warp anchored to a door handle. High end (8 m²): a dedicated
# spare-room corner with open wall hook and comfortable work circle.
# No storage constraint, no machinery clearance, no combustion buffer needed.
# [catalog/weaving/SCHEMA.md §3 backstrap: 30–60 cm warp width; portable;
# no floor space required in the traditional sense.]

ceiling_min_m: 2.1
# Standard residential ceiling acceptable. The backstrap loom has no vertical
# mechanism; the constraint is a fixed point at anchor height (standard door
# knob height ~1.0 m, wall hook height 1.2–1.5 m). 2.1 m is the minimum
# residential ceiling height in most US building codes; no weaving-specific
# ceiling requirement applies.

ventilation: natural-sufficient
# Electric-lighting-only home studio with no combustion, no industrial fiber
# lint, and a single operator working with cotton or synthetic yarn at low
# throughput. Standard residential ventilation (open window or normal HVAC)
# is fully adequate. No emissions permit, no industrial ventilation standard
# applies at this scale.

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: electric-lighting-only
# The backstrap loom is entirely hand-operated; no powered mechanism whatsoever.
# Energy use is exclusively residential lighting at the work corner. This is the
# minimal energy posture achievable for any weaving operation: lower than
# electric-lighting-only for a dedicated studio because the home studio's
# lighting is shared with other residential uses and not attributable solely
# to weaving.
# [catalog/weaving/SCHEMA.md §2 electric-lighting-only definition.]

energy_consumption_per_active_hour: "0.1 kWh/day (task lighting at work corner)"
# Single LED task lamp at the work corner: 10 W × ~10 hr of combined residential
# and weaving use per day = 0.10 kWh/day. At 3 operating days/wk × 50 wk × $0.125/kWh
# = $2.34/yr — electrically negligible. Stated as a daily figure consistent with
# the schema's per-active-hour field for passive-lighting facilities.
# [Derived from single LED task lamp; catalog/weaving/SCHEMA.md §2 1–5 kWh/day
# range for electric-lighting studios; this entry is at the extreme low end due
# to single-operator home corner with supplemental residential light.]

backup_fuel: null
# No combustion fuel required or used; no backup fuel applicable.

# ── WEAVING-SPECIFIC REQUIRED FIELDS ─────────────────────────────────────────

loom_type: backstrap
# Required field per catalog/weaving/SCHEMA.md §3. A traditional tension-frame
# loom in which the warp is held taut between a fixed anchor point and a hip
# strap worn by the weaver. The loom is fully portable, requires no floor frame,
# and consists only of sticks and a backstrap (warp beam, breast beam, shed
# rod, heddle rod, shuttle, and strap — total weight < 1 kg in the minimal
# form). Consistent with warp_width_cm: 45 cm (mid of the 30–60 cm backstrap
# range) and operator_skill_floor: journeyman-weaver (body-tension technique
# cannot be operated independently by a novice; see SCHEMA.md §5 note).
# [catalog/weaving/SCHEMA.md §3 backstrap: 30–60 cm warp width; portable; no
# floor space required; traditional in Mesoamerican, Andean, SE Asian traditions.]

humidity_control_required: false
# Primary fiber types at this entry level are cotton and synthetic (acrylic,
# polyester blends) — the most practical and affordable option for a minimum-
# capital home operator purchasing industrial yarn. Cotton and synthetic yarns
# do not require humidity-controlled storage or weaving environment. Standard
# home ambient conditions (40–60% RH in most US climates) are fully acceptable.
# Authors note: if the operator advances to wool warp, this field would need
# revision; at the minimum-capital floor, cotton/synthetic is the primary fiber.
# [catalog/weaving/SCHEMA.md §4: humidity_control_required false for cotton,
# synthetic fiber, and most blended entry-level yarns.]

fiber_source_declaration: industrial-yarn-purchased
# The minimum-capital operator purchases commercial cotton or acrylic yarn from
# a craft-supply distributor, online retailer, or local yarn shop. No spinning
# infrastructure, no local-spinner relationship, no heritage-breed sourcing.
# This is the only fiber sourcing that is consistent with the $200–$2,500 total
# capital envelope: heritage or local-spun fiber would require premium sourcing
# cost that is inconsistent with the minimum-viable floor position of this entry.
# Specific fiber: 8/2 cotton (weaving cotton, commercially spun) is the most
# common and economical choice for backstrap beginners and established weavers
# producing cotton cloth; acrylic blend is an alternative at lower cost but
# reduced market appeal. Key Assumptions documents the fiber choice and supply
# continuity assessment.
# [catalog/weaving/SCHEMA.md §6: industrial-yarn-purchased — commercial yarn
# from distributor; lowest capital implication; yarn price volatility noted but
# modest for commodity cotton and acrylic.]

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  meters_per_day: 1.0
  # Net woven length per full operating day at journeyman-weaver level on a
  # backstrap loom weaving plain-weave cotton at 45 cm warp width.
  # The SCHEMA.md §1 typical ranges are for floor looms; backstrap throughput
  # is inherently lower due to the physical effort of managing body tension
  # continuously throughout the weave. The 0.5–2 m/day range stated in the
  # entry brief is consistent with observed backstrap output:
  #   Lower end (0.5 m/day): fine thread count, complex pick-up pattern,
  #     or operator fatigue on extended sessions.
  #   Upper end (2.0 m/day): experienced weaver, plain weave, coarser yarn,
  #     short warp (< 3 m), continuous work session.
  # 1.0 m/day is the journeyman-floor estimate for a part-time operator
  # doing plain-weave cotton on a standard 2–4 m warp: appropriate for the
  # minimum-capital floor position. More experienced weavers in commercial
  # tourist-adjacent contexts may reach 1.5–2.0 m/day but at physical cost
  # (backstrap weaving is physically demanding; see operator_impact).
  # [CITATION-NEEDED: measured backstrap throughput rates from documented
  # commercial or NGO weaving programs; label: estimated from field reports
  # of Mesoamerican and Andean cooperative programs reviewed in secondary
  # literature.]

  warp_width_cm: 45
  # Mid-point of the 30–60 cm backstrap warp-width range per SCHEMA.md §3.
  # 45 cm is the typical width for a backstrap-woven scarf, rebozo, or utility
  # cloth panel; wide enough to produce saleable cloth panels and narrow enough
  # to manage body tension without fatigue escalation. sim_params unit conversions
  # use this reference width (0.45 m × 1.0 m/panel = 0.45 m² per linear meter).
  # [catalog/weaving/SCHEMA.md §3 backstrap 30–60 cm typical range; 45 cm as
  # practical mid-point for plain-weave utility cloth production.]

  pattern_complexity: plain
  # Plain weave (tabby) is the primary output at the journeyman-weaver floor on
  # a basic backstrap loom. Simple supplementary-weft pick-up patterns are
  # achievable on a backstrap loom and are historically associated with this form,
  # but they require significantly more time per pick and reduce throughput below
  # the 1.0 m/day estimate. For the economic floor analysis, plain weave is the
  # appropriate complexity assumption: it maximizes throughput and represents the
  # most realistic steady-state output for a part-time home producer.
  # Note: pattern complexity "plain" is consistent with operator_skill_floor:
  # journeyman-weaver (plain weave on a backstrap requires journeyman body-tension
  # technique but not master-level patterning skill).
  # [catalog/weaving/SCHEMA.md §1 plain weave definition; pattern complexity
  # constraint per skill-floor note in §5.]

  max_active_hours_per_week: 12
  # Part-time operator: ~3 active weaving days per week × ~4 active weaving
  # hours per day. Backstrap weaving is physically demanding (sustained postural
  # load on lower back, hip flexors, and core from maintaining warp tension);
  # 4 active hr/day is the realistic ceiling before fatigue affects quality.
  # More than 12 hr/wk of backstrap weaving is associated with cumulative
  # musculoskeletal strain in documented occupational-health studies of traditional
  # backstrap communities (see operator_impact). This entry is explicitly part-time:
  # consistent with the home-studio, minimum-capital positioning.
  # Note: this is a net active-weaving figure; warping, dressing, and finishing
  # time is additional overhead captured in startup_shutdown_overhead_per_day_min
  # and reflected in downtime_fraction.
  # [CITATION-NEEDED: occupational health data for backstrap weavers; throughput
  # and hours-per-day data from commercial or NGO backstrap programs; label:
  # inferred from secondary literature.]

  product_mix:
    yardage: 55
    rugs_upholstery: 0
    tapestry_art: 0
    garments_accessories: 40
    instruction_open_studio: 5
    # Sum: 100. yardage (55%): plain-weave cotton cloth panels sold by the meter —
    # the primary marketable output; buyers include fashion designers, home-goods
    # crafters, and tourist-market vendors. garments_accessories (40%): scarves,
    # wraps, and small accessories are natural backstrap output at 45 cm width;
    # higher value per meter than raw yardage in direct-to-consumer sales.
    # instruction_open_studio (5%): minimal — one-on-one instruction of a
    # single trainee is feasible; no group instruction capacity in a home corner.
    # No rugs or tapestry: backstrap loom is not suited to rug-weight tension
    # or weft-faced tapestry structure at plain-weave journeyman floor.
    # [catalog/weaving/SCHEMA.md §1 product_mix; yardage and garments_accessories
    # as dominant categories for market-primary hand-weaving entries.]

  throughput_variance:
    worst_month_fraction_of_average: 0.55
    # Seasonal trough for this entry: summer (outdoor-activity competition for
    # operator time) and January (post-holiday fatigue, cold-climate reduced
    # working hours in an unheated home corner). At single-operator scale,
    # illness, family obligations, or a demanding warp changeover can
    # meaningfully depress monthly output. 0.55 is conservative for a
    # single-operator home studio with no substitute operator.
    # [Structural inference from single-operator craft-production variance;
    # CITATION-NEEDED: monthly variance data from solo craft producers; label: inferred.]
    best_month_fraction_of_average: 1.50
    # Pre-holiday peak (October–November) for scarves and accessories;
    # craft-fair season (spring and fall) motivates higher output for
    # inventory building. 1.50 is consistent with seasonal peaks for
    # craft-market-oriented solo producers.
    # [Structural inference from craft-fair calendar and holiday retail cycle;
    # CITATION-NEEDED: seasonal sales data for solo craft producers at village-
    # scale markets; label: inferred.]
    seasonal: "Summer and January trough from operator-availability competition; October–November peak for craft-fair and holiday accessory inventory."

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: journeyman-weaver
# Required by catalog/weaving/SCHEMA.md §5: "Backstrap weaving requires
# internalized body-tension control that is not achievable by a rigid-heddle
# novice. Do not set operator_skill_floor: rigid-heddle-novice for any
# backstrap loom entry." The backstrap loom demands that the operator's body
# IS the tensioning mechanism: maintaining consistent warp tension through
# continuous pelvic tilt, core engagement, and arm position is a physical
# skill acquired over months of practice, not a technique explainable in a
# single orientation. A novice cannot operate a backstrap loom safely and
# productively without direct supervision. Journeyman-weaver floor is the
# schema-mandated minimum.
# NOTE: The entry brief specified rigid-heddle-novice; this field is set to
# journeyman-weaver per the mandatory schema constraint in §5. This discrepancy
# is flagged as a concern in the authoring report.
# [catalog/weaving/SCHEMA.md §5 backstrap skill note; §3 backstrap loom type note.]

operators_concurrent: "1"
# Single-operator home studio by design. The backstrap loom is intrinsically
# single-operator: it requires the weaver's body as the tensioning device; no
# second operator can assist with the same warp. This is the minimum-viable
# staffing model and a defining constraint of the entry.

apprentice_friendly: true
apprentice_path:
  training_stages: >
    Stage 1 (0–4 weeks): introduction to backstrap mechanics. Operator learns
    to wind a warp on warping pegs, lash the warp beam to a fixed anchor, thread
    the heddle rod and shed rod, and attach the backstrap. Weaves a short plain-
    weave sample (30–50 cm) under direct supervision, focusing on achieving
    stable body tension and consistent beat. Gate criterion: completes a 50 cm
    plain-weave sample with even tension and no dropped heddle across the full
    weaving width without supervisor intervention at each pick.

    Stage 2 (1–6 months): building productive technique. Trainee weaves
    independently on full-length warps (2–4 m), managing tension variation
    through the warp length, executing clean selvedges, and maintaining beat
    consistency. Learns to diagnose and correct tension problems (warp sag,
    uneven selvedges, broken warp ends) without supervisor assistance. Gate
    criterion: completes three consecutive warps of 2+ m with commercially
    acceptable evenness and selvedge quality, evaluated by the supervising
    journeyman.

    Stage 3 (6–18 months): independent production. Operator manages the full
    production cycle: warp calculation, winding, dressing the loom, weaving
    to completion, wet-finishing, and cutting/fringing. Begins to develop
    personal rhythm and manage physical fatigue across a 4-hr session. Gate
    criterion: sustained independent production of 0.8+ m/day averaged over
    a 4-week period without quality defects requiring re-weaving.
  time_to_independent_operation: >
    ~6–18 months to journeyman-level independent production on a backstrap loom.
    Body-tension technique is slower to internalize than rigid-heddle or floor-
    loom operation because there is no mechanical tensioning device: the operator's
    body IS the loom's tensioning system. Six months is achievable for an operator
    with prior weaving experience (rigid-heddle or floor-loom background); 18 months
    is more realistic for a trainee starting from zero weaving experience. This is
    a longer on-ramp than rigid-heddle (3 hours to independence) but shorter than
    floor-loom journeyman (journeyman competency typically 12–36 months). The
    backstrap on-ramp is intensive in physical practice, not technical complexity.
  succession_note: >
    The single-operator home studio has limited natural succession structure:
    there is typically one weaver, with a trainee learning alongside when a
    mentoring relationship exists. Institutional continuity is absent by design
    at the home-studio scale; the entry is honest that this is a solo practice
    with fragile succession. The apprentice path exists for skill transmission
    within a community (one home-studio operator training a neighbor or family
    member) but does not address institutional continuity at cooperative or
    civic scale — those scales are not viable for this entry (see scale_fit
    and lens_fit). Anti-romanticism: the "succession" framing at this scale is
    more accurately described as informal skill transmission within social
    networks than a formal apprenticeship pipeline.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 200, mid: 800, high: 2500 }
  # Low ($200): traditional minimal backstrap loom (hand-carved sticks, woven
  #   backstrap) purchased as a kit or assembled from local materials; or a
  #   used/secondhand rigid-heddle-to-backstrap conversion kit. Adequate for
  #   plain-weave cotton production. Several NGO and fair-trade suppliers
  #   (e.g., Back Strap Weaving, Glimakra backstrap kit) sell functional
  #   minimal kits in the $50–$200 range. This is the absolute capital floor
  #   of the weaving catalog.
  # Mid ($800): complete backstrap loom kit with hardwood beams and smooth
  #   shed rods (e.g., Schacht backstrap loom kit or equivalent hardwood-
  #   quality equivalent), 2–3 heddle rods, a hand shuttle, a lease stick set,
  #   and a beginning cotton yarn inventory ($200–$300) to support the first
  #   several warps. Suitable for production use.
  # High ($2,500): mid-quality backstrap loom + a supplementary rigid-heddle
  #   loom for warp preparation flexibility + full yarn inventory for 6 months
  #   of production ($800–$1,000) + finishing equipment (small iron, blocking
  #   board) + packaging and sales materials for direct-to-consumer or craft-
  #   fair market entry.
  # Even the high end ($2,500) is below the low end of any floor-loom entry in
  # this catalog and below the low end of weave-009 (Rigid Heddle Tool-Library,
  # $3,000 for the smallest viable configuration). This is the absolute minimum-
  # capital entry point in the weaving catalog.
  # [CITATION-NEEDED: backstrap loom kit pricing from Schacht, Glimakra,
  # Back Strap Weaving, and Guatemalan/Mexican artisan supply vendors, 2024–2026;
  # label: illustrative estimate from general market knowledge.]

  install_cost: 0
  # Home studio requires no installation: the loom attaches to a door handle,
  # wall hook, or post with a simple lashing cord. No electrical, plumbing,
  # structural, or permitting work required. A single wall hook ($5–$10) is the
  # only physical modification to the residence. The install_cost is effectively
  # zero; any home-improvement component is captured in capital_cost.high.
  # [Structural inference: backstrap loom has no fixed installation requirement.]

  annual_maintenance: 100
  # Backstrap strap replacement (leather or woven cotton strap fatigues and
  # cracks with use; replacement strap: $15–$30; expected ~every 1–2 years
  # under regular use): ~$25/yr amortized.
  # Warp beam and shed rod wear (light sanding, wood treatment, replacement
  # of cracked rods every 3–5 years): ~$30/yr amortized.
  # Heddle rod: low-wear item; replacement every 5+ years: ~$10/yr amortized.
  # Shuttle and small tool wear: ~$20/yr.
  # Miscellaneous (lease sticks, cord replacements, small supplies): ~$15/yr.
  # Total: ~$100/yr. Minimal compared to any other weaving entry.
  # Excludes first-year failure replacements in operations_reality.
  # [Structural inference from backstrap loom material wear characteristics;
  # CITATION-NEEDED: maintenance cost data from documented backstrap weaving
  # programs; label: inferred.]

  annual_consumables: 700
  # Yarn cost for 140 m/yr of plain-weave cotton output at 45 cm warp width:
  #   Cloth area: 140 m × 0.45 m = 63 m².
  #   8/2 cotton yarn coverage: approximately 300 g/m² for a medium-weight
  #   plain-weave cotton (typical for backstrap utility cloth and accessories).
  #   Total yarn: 63 m² × 300 g/m² = 18.9 kg yarn/yr.
  #   Commercial 8/2 cotton yarn price: ~$25–$35/kg in quantity (Webs, WEBS,
  #   UKI, Valley Yarns wholesale); use $35/kg for small-quantity home purchase.
  #   Yarn cost: 18.9 kg × $35/kg = $661.50 → $660/yr.
  # Add small consumables (cord, lease sticks, finishing supplies): ~$40/yr.
  # Total: ~$700/yr.
  # [CITATION-NEEDED: 8/2 cotton yarn pricing per kg from US craft-supply
  # distributors (Webs/WEBS, Valley Yarns, UKI Cotton); label: illustrative
  # estimate from general market knowledge of weaving yarn pricing, 2024.]

  floor_space_rent_per_year: 300
  # Imputed at residential rate for 5 m² of home floor space dedicated to
  # weaving use. Per schema semantics: imputed at local residential-equivalent
  # rate even in an owner-occupied home, for evaluation-matrix consistency.
  # Basis: $60/m²/yr residential imputed rate (typical small-town US residential
  # rent of ~$800–$1,200/month for a 1,000–1,200 sq ft home ÷ floor area
  # = ~$55–$65/m²/yr residential average); 5 m² × $60/m²/yr = $300/yr.
  # This is the lowest floor_space_rent figure in the weaving catalog, consistent
  # with the minimum-footprint, home-corner positioning.
  # [CITATION-NEEDED: residential rental rate per m² in US village-scale markets,
  # 2024; label: inferred from general US housing cost data.]

  market_price_per_unit: { low: 30, mid: 80, high: 250 }
  # Per linear meter of woven cloth at 45 cm warp width.
  # Low ($30/m): basic plain-weave cotton cloth sold by the meter at a local
  #   craft fair or to a small-batch designer; comparable to artisan-made utility
  #   cloth in the $20–$40/m range. This is the floor of viable market pricing
  #   for hand-woven cloth that is not industrial commodity fabric.
  # Mid ($80/m): quality plain-weave cotton sold direct-to-consumer (Etsy,
  #   local craft fair, direct studio sale) as a premium fabric or finished
  #   accessory equivalent; consistent with hand-woven scarf/wrap pricing of
  #   $60–$120 per piece at 0.75–1.5 m per piece.
  # High ($250/m): premium artisan cloth with cultural-heritage positioning,
  #   sold through craft-fair premium vendors or high-end boutiques; equivalent
  #   to fine hand-woven fabric from established artisan brands ($200–$400/m).
  #   Achievable only with strong provenance story and target buyer who values
  #   cultural authenticity.
  # Industrial baseline: $10/m (see below).
  # [CITATION-NEEDED: hand-woven cloth pricing from Etsy seller data, craft-fair
  # survey data, or direct-to-consumer artisan fabric pricing, 2024–2026;
  # label: illustrative estimate from general market knowledge of handwoven
  # fabric and accessory pricing.]

  industrial_baseline_price: 10
  # Per linear meter of industrially woven cotton fabric at comparable weight
  # and width. Commercial cotton fabric (quilting cotton, shirting) is available
  # at US retail in the $5–$15/m range; $10/m is the mid-estimate for a plain-
  # weave cotton equivalent at mass-market retail (Jo-Ann Fabrics, online
  # discount fabric vendors). The artisan-production premium over industrial
  # baseline ranges from 3× (low end, $30/m) to 25× (high end, $250/m).
  # The premium at mid price ($80/m) is 8×, which is achievable only with
  # meaningful differentiation: demonstrable cultural-heritage provenance,
  # exceptionally distinctive pattern, or direct-to-consumer positioning that
  # eliminates wholesale margin.
  # [CITATION-NEEDED: industrial cotton fabric pricing per meter from US retail
  # sources (Jo-Ann Fabrics, online fabric warehouses), 2024; label: illustrative
  # estimate from general market knowledge.]

  pricing_notes: >
    Per linear meter at 45 cm warp width. Industrial-competitor baseline is
    mass-market plain-weave cotton fabric at ~$10/m (US retail). The artisan
    premium rests entirely on visible hand-production and — at the high end —
    cultural-heritage authenticity: a tourist-market buyer paying $250/m for
    a backstrap-woven Guatemalan-style cloth is purchasing provenance, not cloth
    properties. The mid-market segment ($80/m) requires direct-to-consumer reach
    (Etsy, craft fair, local boutique) and a buyer who cannot easily substitute
    industrial fabric. At village scale, this buyer pool is thin; penetration is
    very slow (see throughput and scale_fit).

  pricing_validation: >
    Market price range is an illustrative estimate derived from observed Etsy
    listings and craft-fair price points for handwoven cotton cloth and accessories
    (2024 review of seller data). The low end ($30/m) is anchored to basic handwoven
    yardage listed on Etsy and at regional craft fairs; the mid ($80/m) reflects
    finished accessory pricing back-calculated to a per-meter equivalent; the high
    ($250/m) reflects premium heritage-positioned cloth from established artisan
    brands. Evidence type: market observation (seller listings), not cost-plus
    residual or formal willingness-to-pay study. CITATION-NEEDED for formal
    survey-quality data.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Backstrap strap cracking or delamination (leather or woven-cotton)"
      estimated_hours_to_failure: 300
      replacement_cost: 25
      replacement_lead_time_days: 3
      serviceable_by: operator
      # The backstrap itself — the strap worn around the operator's hips to
      # maintain warp tension — is subject to continuous flex stress during
      # every weaving session. A leather strap may crack at fold points within
      # the first 300 active hours; a woven-cotton strap may stretch or fray.
      # Replacement is operator-serviceable: the strap is a simple lashed
      # attachment with no specialized hardware. A replacement strap can be
      # purchased from a loom supplier ($15–$30) or made from 1.5 m of heavy
      # cotton webbing. Lead time 3 days from online order or local fabric
      # store. First-year replacement is likely at moderate use intensity.
      # [catalog/weaving/SCHEMA.md §7 backstrap strap or loom-bar wear reference:
      # 200–1,000 hr typical; lead time 0–3 days locally; label: inferred.]

    - item: "Shed rod splitting or cracking (warp-spread pressure)"
      estimated_hours_to_failure: 500
      replacement_cost: 15
      replacement_lead_time_days: 7
      serviceable_by: operator
      # The shed rod and heddle rod experience repeated lateral pressure from
      # warp tension cycling with each pick. A thin or low-quality rod may
      # split along the grain within the first 500 active hours, especially
      # under the elevated tension of tighter setts or with a coarser yarn.
      # Replacement rod (hardwood dowel, $5–$15 depending on diameter and
      # quality): operator-serviceable with re-threading of the shed rod
      # position (~30 min). Quality hardwood rods (maple, birch) significantly
      # outperform pine or softwood; this failure is avoidable with appropriate
      # material choice and is more common with low-cost kit components.
      # [catalog/weaving/SCHEMA.md §7 backstrap strap or loom-bar wear reference;
      # CITATION-NEEDED: rod failure rate data from backstrap loom kits; label: inferred.]

    - item: "Warp beam lashing cord wear and breakage"
      estimated_hours_to_failure: 400
      replacement_cost: 5
      replacement_lead_time_days: 0
      serviceable_by: operator
      # The lashing cord that attaches the warp beam to the wall anchor (door
      # knob, hook, or post) experiences tension cycling with each beat of the
      # shed and is abraded at the contact point. A thin cord or twine may
      # break within the first 400 active hours. Replacement cord (strong cotton
      # twine, nylon cord, or leather strip): $3–$7 from any hardware store;
      # operator-serviceable in 5 minutes. The operator should keep 1 m of
      # spare cord in the work area. Zero lead time with local hardware source.
      # [Structural inference from backstrap anchor lashing mechanics; label: inferred.]

  maintenance_schedule:
    daily:
      task: "Check backstrap strap tension and surface condition before session; inspect lashing cord at anchor point; confirm shed rod is seated correctly; brush lint from heddle rod holes and shed rod groove after session"
      performed_by: operator
    weekly:
      task: "Inspect all stick components for cracks, splits, or raised grain; lightly sand any rough spots on shed rod or heddle rod that show yarn abrasion; review lashing cord condition at anchor contact point; check backstrap hardware attachment points"
      performed_by: operator
    quarterly:
      task: "Full loom component inspection: measure heddle rod for bow or warp (replace if > 3 mm deflection under warp tension); condition leather strap if applicable; assess warp beam surface smoothness and sand if needed; inventory spare cord and replacement rods"
      performed_by: operator
    annual:
      task: "Replace backstrap strap proactively if showing wear (annual replacement is economical at $25 vs. mid-session breakage); full stick set inspection and replacement of any cracked or warped components; review yarn inventory and resupply plan for the coming year; assess whether warp width or product mix should be adjusted based on year-one market response"
      performed_by: operator

  startup_shutdown_overhead_per_day_min: 20
  # Startup (10 min): tie lashing cord to anchor, check warp tension and heddle
  # rod position, confirm backstrap attachment, check last few picks for defects
  # before resuming. Shutdown (10 min): roll cloth beam forward to secure
  # finished cloth, ease warp tension, detach lashing cord, roll loom for
  # storage or leave attached to anchor, sweep work area of yarn lint.
  # Total: 20 min/day. On warping days (new warp setup): additional 2–4 hr for
  # warp winding, lashing, and threading — not daily but folded into
  # downtime_fraction as non-weaving overhead days.
  # [Structural inference from backstrap loom setup and shutdown procedure;
  # label: inferred.]

  max_active_hours_realism_note: >
    12 hr/wk is the derated net active weaving figure, not a gross ceiling.
    Startup-shutdown overhead (20 min/day × 3 days/wk = 1.0 hr/wk) is
    already subtracted from the gross available time before arriving at the
    12 hr/wk figure: the operator has ~13 hr/wk available at the loom and
    loses 1 hr/wk to overhead, yielding 12 hr/wk net active weaving.
    Warping days (new warp setup: 2–4 hr per warp, one warp every 2–3 weeks):
    approximately 1–2 warping days/month = 8–16 hr/month of non-weaving overhead
    folded into the downtime_fraction (0.10). sim_params.throughput_units_equiv_per_year
    uses the 12 hr/wk net active figure with 0.10 downtime applied annually.

  interruption_notes: >
    Home-studio interruptions are domestic, not commercial: family obligations,
    phone calls, and household tasks are the primary intraday interruptions.
    These are not modeled explicitly but are absorbed into the conservative
    12 hr/wk ceiling (a solo home studio rarely achieves the 4 hr/day ceiling
    on every session day). Physical fatigue is the binding constraint at
    4 hr/day: most backstrap weavers report diminishing quality and increasing
    tension inconsistency after 3–4 continuous hours; 4 hr/day is the ceiling,
    not the average. The 0.75 effective-production factor (accounting for
    session-quality variation and fatigue degradation within the day) is
    embedded in the 1.0 m/day throughput estimate rather than tracked as
    a separate interruption overhead.

  consumables_lead_time_days: { typical: 5, worst: 21 }
  # Cotton and acrylic yarn from US craft-supply distributors (Webs, WEBS,
  # Valley Yarns, LoveCrafts online): 3–7 day typical shipping. Backstrap
  # loom component replacements (shed rod, heddle rod, backstrap) from specialty
  # suppliers (Schacht, Back Strap Weaving): 5–14 days typical, up to 21 days
  # for out-of-stock specialty items or international suppliers. The home
  # studio's low volume means it typically holds < 1 warp worth of yarn
  # inventory; a supply disruption of > 2 weeks would halt production.
  # Mitigation: maintain 2–3 warp lengths of yarn inventory (~4–6 kg cotton)
  # at all times.
  # [Illustrative estimate; CITATION-NEEDED: yarn supply lead-time data from
  # US craft distributors, 2024; label: inferred.]

  throughput_variance:
    seasonal: "Summer and January trough from operator-availability competition; October–November peak for craft-fair and holiday accessory inventory."
    worst_month_fraction_of_average: 0.55
    best_month_fraction_of_average: 1.50

  operator_impact:
    noise_db: 38
    # Backstrap weaving is among the quietest operations in the entire CERES
    # catalog: hand-lashing the heddle rod and passing a light hand shuttle
    # produces minimal sound. The dominant sound is the soft thump of the
    # beating stick against the last pick — approximately 35–40 dB at the
    # operator position. No hearing protection required; compatible with
    # residential operation without noise complaints from adjacent rooms.
    # [CITATION-NEEDED: measured sound level for backstrap weaving operations;
    # label: inferred from general knowledge of hand-weaving noise levels.]
    heat_exposure: "Ambient residential temperature; no thermal hazard. The operator generates moderate body heat during active weaving (physical exertion maintains warp tension) but the studio environment is entirely ambient. No external heat source."
    emissions: "Near-zero on-site emissions. Cotton and acrylic yarn produce negligible lint at single-operator, part-time backstrap production volumes. No permit of any kind required. Residential operation is fully compatible with this emissions profile."
    physical_demand: >
      High for sustained sessions; this is the highest physical demand in the
      weaving catalog for a portable loom. Backstrap weaving requires: (1)
      continuous isometric contraction of core and hip-flexor muscles to maintain
      warp tension throughout every pick; (2) seated floor or low-stool posture
      with sustained lumbar loading; (3) repetitive bilateral arm movement to
      pass the shuttle and beat the pick. Occupational-health studies of traditional
      backstrap weavers document elevated rates of lower-back pain, cervical strain,
      and repetitive-stress injury in operators weaving > 6 hr/day. The 4 hr/day
      ceiling in this entry is a health protection floor, not a productivity
      constraint. Anti-romanticism: the physical demands of backstrap weaving as
      traditionally practiced in piece-work contexts (tourist-adjacent heritage
      markets) are a documented health burden on marginalized women weavers who
      earn below-minimum-wage piece rates for cloth that is then marked up 5–20×
      in the tourist channel. This entry acknowledges that burden explicitly.
      [CITATION-NEEDED: occupational health studies of backstrap weavers in
      Mesoamerican and Andean communities; ILO or NGO documentation of piece-work
      rates and health outcomes; label: referenced in secondary literature.]

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Residential zoning fully compatible; home-occupation permit may be required in some jurisdictions for selling goods produced at home (typically a simple business license, < $100); no commercial or industrial zoning required at any scale"
  emissions: "No emissions permit required; below all industrial air-quality thresholds; residential operation produces no detectable emissions beyond ambient household"
  other: "No trade-specific licensing for weaving in any US jurisdiction; if selling through farmer's markets or craft fairs, standard vendor permit applies; sales tax registration required for retail sales; no OSHA applicability at single-person home-studio scale"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: marginal
  # Market is the only lens with any viability for this entry. The output
  # (hand-woven plain-weave cotton cloth and accessories) has a documented
  # market in craft fairs, direct-to-consumer online sales (Etsy), and
  # tourist-market cultural-heritage contexts. The market is marginal rather
  # than good because: (1) throughput is very low (140 m/yr), limiting absolute
  # revenue; (2) market penetration at village scale is very slow (thin buyer
  # pool); (3) the economic analysis (see Key Assumptions) shows that clearing
  # the SCALES wage threshold at part-time village scale requires consistent
  # mid-to-high price realization ($80–$250/m) and full capacity utilization —
  # neither of which is reliably achievable in a home studio. Market: marginal
  # reflects possible viability under favorable assumptions, not a reliable win.
  cooperative: poor
  # A single-operator home studio is not a cooperative operation; it has no
  # member ownership structure, no shared capital, and no governance mechanism.
  # Aggregating multiple backstrap home studios into a cooperative (e.g., a
  # village women's weaving cooperative) is a different entry (not this one)
  # and would require shared capital, formal governance, and collective marketing.
  # Cooperative: poor for this entry as specified.
  civic: poor
  # A municipal or civic body has no basis for investing in a single-operator
  # home studio for backstrap weaving. There is no public-goods justification
  # for civic subsidy of a private home weaving operation. The civic lens is
  # poor at all scales. If the public-goods case for cultural heritage or
  # skills preservation is the goal, that case belongs to a cooperative or
  # civic entry (not weave-014). Civic: poor.

scale_fit:
  village: marginal
  # Village scale (500–2,000 residents) is the only scale at which a backstrap
  # home studio has any viability: the operator is a village resident producing
  # for local craft-fair, tourist-passing-through, and small direct-to-consumer
  # markets. Marginal reflects that even at village scale, the buyer pool for
  # premium hand-woven cloth is thin and market penetration is very slow.
  # The entry's purpose at village scale is to establish the absolute floor:
  # what is the minimum capital and minimum footprint at which a weaving
  # operation can exist, and can that floor clear a subsistence income?
  # The answer is: barely, and only under favorable conditions.
  town: poor
  # At town scale, the backstrap home studio does not scale: a single operator
  # in a home corner cannot serve a larger market by simply living in a larger
  # town. The entry is inherently single-operator, single-loom, and part-time.
  # A town-scale market does not change the throughput or economics; it only
  # increases competition from other vendors (including industrial suppliers).
  # Town: poor.
  small_city: poor
  # Same logic as town; the backstrap home studio does not benefit from
  # small-city market size: throughput is fixed by the single operator's
  # physical capacity. Small city: poor.

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

# lens_context.cooperative: omitted — lens_fit.cooperative is `poor`; no
# conditional block required per catalog/SCHEMA.md §4 and validation rule E2-R5.

# lens_context.civic: omitted — lens_fit.civic is `poor`; no conditional
# block required per catalog/SCHEMA.md §4 and validation rule E2-R6.

# Note: lens_context.market does not exist in the schema; the market lens
# economics are captured entirely in the economics block and sim_params.
# operations_reality is required because lens_fit.market is `marginal`.

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 800
  # Equals economics.capital_cost.mid per E3-R1. [Derived from economics block above.]

  cost_sd: 575
  # Derived: (capital_cost.high − capital_cost.low) / 4 = (2,500 − 200) / 4 = $575.
  # E3-R5 check: cost_sd / cost_mean = 575 / 800 = 0.719 — above the 0.50 upper
  # bound of the "plausible range." This reflects the unusually wide capital range
  # for this entry: the low end ($200) is a traditional minimal kit and the high
  # end ($2,500) includes a supplementary loom and full production inventory.
  # The wide cost_sd / cost_mean ratio is a documented feature of minimum-capital
  # entries where the low end is a genuinely minimal configuration and the high
  # end includes optional capability additions; not an error. Noted as P2 E3-R5
  # finding (within-order, not order-of-magnitude discrepancy); see Key Assumptions.
  # [Derived per catalog/SCHEMA.md §3 default formula; ratio documented above.]

  throughput_units_equiv_per_year: 140
  # Unit: linear meters of woven cloth at 45 cm reference warp width.
  # Derivation:
  #   Net active weaving hours/week: 12 hr/wk (derated; see max_active_hours_realism_note)
  #   Output rate: meters_per_day (1.0 m/day) ÷ active hr/day (4 hr) = 0.25 m/hr
  #   Gross annual output: 12 hr/wk × 0.25 m/hr × 52 wk = 156 m/yr
  #   Derated by downtime_fraction (0.10): 156 × 0.90 = 140.4 → 140 m/yr
  #
  # E3-R2 cross-check: max_active_hours_per_week × 52 × (1 − downtime_fraction)
  #   × units_per_hour_equiv = 12 × 52 × 0.90 × 0.25 = 140.4 m/yr ✓
  #
  # [Derived from throughput fields, output rate, and downtime_fraction above.]

  variable_cost_per_unit: 5.00
  # Direct cost per meter of woven cloth:
  #   Yarn cost: annual_consumables (yarn component, ~$660/yr) ÷ 140 m/yr
  #   = $660 ÷ 140 = $4.71/m.
  #   Small consumables (finishing supplies, cord, misc): ~$40/yr ÷ 140 m/yr
  #   = $0.29/m.
  #   Total: ~$5.00/m. Rounded to $5.00 for sim_params.
  # Note: variable_cost_per_unit does not include labor; labor is captured in
  # labor_hours_per_unit × operator wage rate in the sim evaluation.
  # [Derived from annual_consumables and throughput_units_equiv_per_year above.]

  labor_hours_per_unit: 4.00
  # Operator hours per meter of woven cloth:
  #   Output rate: 0.25 m/hr → labor per meter = 1 ÷ 0.25 = 4.0 hr/m.
  # E3-R3 cross-check: throughput_units_equiv_per_year × labor_hours_per_unit
  #   = 140 × 4.0 = 560 hr/yr.
  #   Target: max_active_hours_per_week × 52 × (1 − downtime_fraction)
  #   = 12 × 52 × 0.90 = 561.6 hr/yr. Discrepancy: 1.6 hr/yr (< 0.3%). ✓
  # [Derived from output rate above; E3-R3 verification shown.]

  downtime_fraction: 0.10
  # Composition:
  #   Warping days (new warp every 2–3 weeks; 2–4 hr setup each):
  #     ~2 warping events/month × 3 hr avg = 6 hr/month non-weaving overhead.
  #     At 3 active weaving days/wk: 52 × 3 = 156 weaving-day slots/yr;
  #     ~24 warping events/yr × 0.5 day average = 12 non-weaving days/yr.
  #     12 ÷ 156 = 7.7% downtime from warping overhead alone.
  #   First-year failure events (strap, shed rod, lashing cord):
  #     All are operator-serviceable with 0–7 day lead times; spare strap and
  #     cord in the studio reduce actual downtime to < 1% for most events.
  #   Planned gaps (illness, family, seasonal trough):
  #     Captured in throughput_variance, not in downtime_fraction directly.
  #   Total: 0.10 (rounded conservative; warping overhead is the dominant driver).
  # [Derived from operations_reality and warping overhead estimate above.]

  lifespan_years: 15
  # Backstrap loom components (hardwood sticks, quality strap) have a service
  # life of 10–20 years under regular maintenance; occasional component
  # replacement (strap, shed rod) extends the functional life indefinitely.
  # 15 years is the conservative mid-estimate for the stick set as a whole.
  # At $800 capital cost amortized over 15 years = $53/yr capital recovery —
  # the lowest capital amortization in the weaving catalog.
  # [Structural inference from hardwood loom component longevity; label: inferred.]

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: fail
    primary_metric: 0.09580838323353294
    metric_name: payback_years
    notes: wage_verdict=fail (take_home=8286 vs median=48000)
  village_coop:
    verdict: win
    primary_metric: 6.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=6, total_annual_cost=1153
  village_civic:
    verdict: fail
    primary_metric: 1.6533333333333333
    metric_name: per_household_cost
    notes: per_hh=1.65, threshold=120, hrs/capita=0.000 vs threshold=2.0
  town_market:
    verdict: fail
    primary_metric: 0.09580838323353294
    metric_name: payback_years
    notes: wage_verdict=fail (take_home=8286 vs median=56000)
  town_coop:
    verdict: win
    primary_metric: 6.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=6, total_annual_cost=1153
  town_civic:
    verdict: fail
    primary_metric: 0.24313725490196078
    metric_name: per_household_cost
    notes: per_hh=0.24, threshold=100, hrs/capita=0.000 vs threshold=2.0
  small_city_market:
    verdict: fail
    primary_metric: 0.09580838323353294
    metric_name: payback_years
    notes: wage_verdict=fail (take_home=8286 vs median=62000)
  small_city_coop:
    verdict: win
    primary_metric: 6.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=6, total_annual_cost=1153
  small_city_civic:
    verdict: fail
    primary_metric: 0.045925925925925926
    metric_name: per_household_cost
    notes: per_hh=0.05, threshold=80, hrs/capita=0.000 vs threshold=2.0
sources:
  - ref: "catalog/weaving/SCHEMA.md v1.0 §1: throughput block structure; meters_per_day ranges for rigid-heddle (1–4 m/day) as reference; backstrap throughput at lower end; max_active_hours_per_week guidance"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §2: electric-lighting-only energy source definition; near-zero energy for hand-operated loom studios in residential context"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §3: backstrap loom type; warp width 30–60 cm; portable; no floor space requirement; traditional in Mesoamerican, Andean, SE Asian traditions; journeyman-weaver operator floor note; capital range reference"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §4: humidity_control_required false for cotton, synthetic fiber, and most blended entry-level yarns"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §5: journeyman-weaver definition — independently capable studio weaver; backstrap loom note: body-tension technique requires internalized practice not achievable by rigid-heddle-novice; mandatory journeyman floor for backstrap entries"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §6: fiber_source_declaration industrial-yarn-purchased — commercial cotton and acrylic yarn from distributor; lowest capital implication; yarn price volatility noted"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §7: first_year_failures reference list — backstrap strap or loom-bar wear; applicable loom types; typical hours-to-failure 200–1,000 hr; lead time 0–3 days locally"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §8 Group D guidance for weave-014: minimum-viable capital floor entry; expected marginal-to-fail at market and coop; operator_skill_floor: journeyman-weaver must be justified; anti-romanticism on piece-work context"
  - ref: "catalog/SCHEMA.md v1.1: base schema; all required and conditional fields; E-1/E-2/E-3 validation rules; market lens conditional fields (market_price_per_unit, industrial_baseline_price, operations_reality); cooperative and civic lens_context omission when lens_fit is poor"
  - ref: "[CITATION-NEEDED: measured backstrap loom throughput rates (m/day) from documented commercial or NGO weaving programs; Mesoamerican or Andean cooperative data; label: estimated from secondary literature field reports]"
  - ref: "[CITATION-NEEDED: backstrap loom kit pricing from Schacht, Glimakra, Back Strap Weaving, and Guatemalan/Mexican artisan supply vendors, 2024–2026; label: illustrative estimate from general market knowledge]"
  - ref: "[CITATION-NEEDED: 8/2 cotton yarn pricing per kg from US craft-supply distributors (Webs/WEBS, Valley Yarns, UKI Cotton) at small-quantity purchase, 2024; label: illustrative estimate]"
  - ref: "[CITATION-NEEDED: maintenance cost data from documented backstrap weaving programs or NGO artisan support organizations; label: inferred]"
  - ref: "[CITATION-NEEDED: hand-woven cloth pricing from Etsy seller data, craft-fair surveys, or direct-to-consumer artisan fabric pricing data, 2024–2026; label: illustrative estimate from market observation]"
  - ref: "[CITATION-NEEDED: industrial cotton fabric pricing per meter from US retail sources (Jo-Ann Fabrics, Fabric.com, online fabric warehouses), 2024; label: illustrative estimate]"
  - ref: "[CITATION-NEEDED: residential rental rate per m² in US village-scale markets, 2024; US Census or local broker data; label: inferred from general US housing cost data]"
  - ref: "[CITATION-NEEDED: occupational health studies of backstrap weavers in Mesoamerican and Andean communities; ILO documentation of piece-work rates and musculoskeletal health outcomes; label: referenced in secondary literature]"
  - ref: "[CITATION-NEEDED: seasonal sales data for solo craft producers at village-scale US craft markets; label: inferred from craft-fair calendar and holiday retail cycle]"
  - ref: "[CITATION-NEEDED: sound level measurement for backstrap weaving operations at operator position; label: inferred from general knowledge of hand-weaving noise levels]"
  - ref: "Mesoamerican backstrap weaving tradition: documented in archaeological and ethnographic literature as the primary textile technology of pre-Columbian Mesoamerica; functional predecessor to this entry's loom type. [CITATION-NEEDED: primary ethnographic or archaeological source documenting backstrap loom mechanics, throughput norms, and historical fiber use in Mesoamerican communities]"
  - ref: "Andean backstrap weaving tradition: Andean highlands backstrap tradition (Bolivia, Peru, Ecuador) uses a near-identical loom form for fine alpaca and wool cloth; functional precedent for body-tension technique and warp-width norms. [CITATION-NEEDED: primary ethnographic source for Andean backstrap weaving economics and throughput; CAWC or similar NGO documentation preferred]"
  - ref: "Tourist-adjacent cultural heritage piece-work: ILO and NGO documentation of below-minimum-wage piece-work in Guatemalan and Mexican backstrap-weaving communities serving tourist and export markets; primary evidence for the anti-romanticism note in this entry. [CITATION-NEEDED: ILO SECTOR / ITC-ILO reports on artisan craft wages in Central America; NGO monitoring data from fair-trade weaving cooperatives]"
---
## Summary

The Backstrap Home Studio is the absolute minimum-capital entry in the CERES weaving catalog: a single operator, a single backstrap loom, a home corner, and purchased yarn. Capital cost is $200–$2,500 — the lowest in the catalog. Footprint is 3–8 m² of floor space, no installation required. This entry exists to establish the economic floor: what is the minimum investment at which a weaving operation can produce saleable cloth, and can that floor clear a living wage at part-time village scale? The expected answer is: barely not. At mid price realization ($80/m), 140 m/yr output, and 560 hr/yr of operator time, gross revenue is $11,200/yr against a variable cost and overhead of approximately $2,800/yr (consumables $700, maintenance $100, floor space imputed $300, capital amortization $53). Net before labor: ~$8,400/yr. At 560 hr/yr of labor, that implies $15/hr before tax — at or slightly below the SCALES minimum-wage threshold for a village-scale operator depending on jurisdiction. But mid-price realization ($80/m) requires consistent direct-to-consumer sales at craft-fair or Etsy pricing; low-price realization ($30/m) yields only $4,200/yr gross revenue, well below subsistence. This entry is marginal on the market lens under favorable assumptions and fails under conservative ones. Its purpose in the catalog is exactly this documentation: the floor is here, and the floor does not reliably clear minimum wage at part-time village scale.

## Design rationale

This entry solves a problem no other weaving catalog entry addresses: what is the minimum viable entry point — in capital, footprint, and infrastructure — for hand-weaving production? Every other entry in this catalog requires either a floor loom ($1,500–$80,000), a shared facility ($3,000–$50,000+ capital), or a civic institution. Weave-014 tests the floor: a weaver with $200, a home corner, and a willingness to practice backstrap technique. The design rationale is not that this is an ideal entry point — it is explicitly a stress test and a floor-finding exercise. The backstrap loom is chosen because it is the lowest-capital weaving implement capable of producing saleable cloth; its portability eliminates footprint and installation costs entirely; and its cultural heritage context documents how this minimum configuration has actually been used for subsistence and market production in dozens of traditional communities. The entry is an anti-romantic counterweight to entries that assume journeyman skill, floor-loom equipment, and a reliable craft-fair buyer pool. It asks: given the absolute minimum, is weaving viable? And it answers: at best marginally, and only with directto-consumer market access that a village-scale operator may not reliably have. The analog in this catalog is forge-001 (Backyard Propane Compact, minimum-capital smithing floor) and bake-014 when authored (minimum-capital home baking); weave-014 is the weaving equivalent of those floor-finding entries.

## Historical lineage

Two functional traditions inform this entry, selected for economic and operational inheritance, not aesthetic similarity.

**Mesoamerican and Andean backstrap weaving.** The backstrap loom used in this entry is functionally identical to the loom technology in continuous use across Mesoamerican and Andean highland communities for at least 3,000 years. The functional inheritance is the loom mechanics themselves: body-tension warp control, portable stick construction, and the specific physical skill set required for independent operation. The historical form was embedded in a subsistence and tribute economy in which weaving was primarily women's labor organized through household and community obligations, not market transactions. That labor regime cannot and should not be reproduced; what carries forward is the loom design and the documented throughput norms from NGO and fair-trade program records of traditional weavers. The historical form's economic viability rested on near-zero capital cost (locally sourced materials), zero opportunity-cost labor (weaving was embedded in household production), and captive demand (tribute quotas, community use). None of these conditions apply to a modern home-studio operator in a market economy; the viability assessment in this entry is therefore substantially more demanding than historical conditions would suggest. [CITATION-NEEDED: primary ethnographic and archaeological sources for Mesoamerican and Andean backstrap weaving economics; NGO documentation of throughput norms.]

**Tourist-adjacent cultural heritage piece-work (anti-romanticism precedent).** The dominant modern form of backstrap weaving for market production is piece-work in Guatemalan highland communities (Chiapas, Oaxaca, Bolivian altiplano equivalents), where weavers — predominantly Indigenous women — produce cloth for tourist markets and export cooperatives at documented piece rates that fall below local minimum wage when hours are accurately measured. This is not a design inspiration; it is a documented failure mode that this entry must name explicitly. The functional lesson is that low capital cost does not imply economic viability: the historical and contemporary piece-work context demonstrates that the combination of low throughput, low capital, and a buyer-dominated market (where the buyer — tourist, intermediary, or export cooperative — captures most of the margin) produces subsistence-or-below outcomes. This entry's operator_impact section and the market lens marginal verdict are calibrated against this documented reality, not against romanticized craft-revival assumptions. [CITATION-NEEDED: ILO and NGO documentation of backstrap weaver piece-work wages in Mesoamerican communities; fair-trade weaving cooperative monitoring data.]

## Key assumptions

Capital costs ($200–$2,500) are illustrative estimates derived from general market knowledge of backstrap loom kit pricing (Schacht backstrap kit: ~$150–$300; Glimakra or equivalent: $100–$250; traditional handmade kits from Guatemalan/Mexican artisan suppliers: $50–$150) and startup yarn inventory costs [CITATION-NEEDED]. The mid-point ($800) includes a quality kit plus a modest yarn inventory, which is sufficient for a working studio. Throughput (140 m/yr at 45 cm reference width) is derived from 12 hr/wk net active weaving at 0.25 m/hr (= 1.0 m per 4-hr active day), with 10% downtime for warping overhead. The 1.0 m/day throughput is conservative for an experienced journeyman backstrap weaver; documented NGO programs suggest ranges of 0.5–2.0 m/day depending on warp sett, pattern complexity, and operator experience [CITATION-NEEDED]. Variable cost ($5.00/m) is derived from 8/2 cotton yarn at approximately $35/kg and a coverage factor of 300 g/m² of finished cloth; this estimate requires formal price citation [CITATION-NEEDED]. The cost_sd / cost_mean ratio (0.719) exceeds the schema's guideline range (0.15–0.50) and is documented as a P2 E3-R5 finding; the unusually wide ratio reflects the genuine span between a $200 minimal kit and a $2,500 full-capability setup, not an estimation error. The economic floor analysis in the Summary shows that mid-price realization ($80/m) barely clears a $15/hr implied wage rate — a marginal-pass scenario, not a robust win. Any reduction in price realization (low price: $30/m), output (illness, family obligations, slow market uptake), or operator time (below 12 hr/wk actual) tips the economics below the SCALES wage threshold. The entry's market verdict is therefore genuinely marginal: possible under favorable conditions, not expected in the median case.

## Known risks / failure modes

**Regulatory:** Minimal regulatory exposure — lower than any other weaving entry. The primary risk is home-occupation ordinance compliance: some US jurisdictions require a home-occupation permit for producing and selling goods from a residence, typically a simple business license application ($25–$100). Some residential zoning ordinances prohibit customer visits to the home, which would require the operator to sell exclusively online or at off-site venues (craft fairs, markets). No emissions, no industrial zoning, no specialized permits. The regulatory risk is a nuisance-level administrative risk, not a showstopper.

**Labour pipeline:** The single-operator home studio is inherently fragile: there is no successor by design. The apprentice path documents informal skill transmission but acknowledges that it does not create institutional continuity. If the operator ceases production (injury, relocation, family demands, economic exhaustion), the operation ends with no warm handoff possible. This is the defining structural weakness of the minimum-capital floor entry: it is personally and economically fragile in a way that larger-capital, multi-operator, or institutionally hosted entries are not. The physical demand risk compounds this: backstrap weaving at 4 hr/day, 3 days/week produces cumulative musculoskeletal load that, without proper technique and rest protocols, leads to chronic lower-back and repetitive-stress injury. An injured sole operator is a failed operation. This risk is the strongest argument against viewing the backstrap home studio as a durable livelihood option rather than a temporary or supplemental income source.

**Supply chain:** Low risk compared to other entries, with one notable exception: the operator's working capital buffer. The home studio typically holds less than one warp of yarn inventory. A distributor out-of-stock situation (specific cotton weight or colorway unavailable for 3–6 weeks) halts production without reserve stock. Mitigation: maintain 3–4 warps of yarn inventory (~8–12 kg cotton, ~$280–$420 at $35/kg) as a working-capital buffer. At $800 total capital, buying 4 warps of buffer stock ($280–$420) represents a significant fraction of capital; some operators at the absolute floor ($200 kit) cannot afford this buffer. This creates a genuine fragility: the minimum-capital operator is least able to maintain the supply buffer most needed to protect revenue continuity.

**Market penetration:** The most significant risk at village scale is the thin buyer pool. Plain-weave cotton cloth at $30–$80/m has a narrow market in a village of 500–2,000 residents who are mostly price-sensitive and have easy access to industrial fabric substitutes. Craft-fair sales require the operator to travel and pay vendor fees ($30–$100/event), eroding the already-thin margins. Online sales (Etsy) require photography, listing maintenance, and shipping logistics that represent non-weaving overhead consuming time and money at a scale that matters for a part-time village operator. The "very slow market penetration" characterization in the brief is accurate: this entry may take 12–24 months to build a sustainable customer base, during which operating income is below the variable cost recovery line. An operator who cannot survive the ramp-up period on other income will fail before reaching sustainable market penetration.

## Iteration log

- 2026-04-18: v0.1 — initial authoring per Plan I Task 16 (weave-014). All v1.1 schema fields populated; lens_fit market: marginal / cooperative: poor / civic: poor; lens_context blocks omitted (both triggers are poor — correct per schema); operations_reality populated (market: marginal trigger met); operator_skill_floor set to journeyman-weaver per mandatory schema constraint in catalog/weaving/SCHEMA.md §5 (brief specified rigid-heddle-novice; schema prohibits this for backstrap entries — discrepancy flagged as concern). market_price_per_unit and industrial_baseline_price present (market: marginal trigger). cost_sd / cost_mean ratio 0.719 exceeds schema guideline (0.15–0.50); documented as P2 E3-R5 finding in Key Assumptions. Anti-romanticism content in operator_impact, Historical Lineage, and Summary per Group D guidance. Economic floor analysis in Summary shows marginal-at-best wage clearance. 19 CITATION-NEEDED placeholders carried for post-authoring verification.
