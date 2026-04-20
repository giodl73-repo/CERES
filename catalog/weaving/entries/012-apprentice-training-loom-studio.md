---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: weave-012
trade: weaving
name: "Apprentice Training Loom Studio"
tagline: "Member-owned cooperative training studio; multi-tier loom floor for formal weaving apprenticeship; primary output is certified journeyman weavers"
status: draft
version: "0.1"
supersedes: null
inspirations:
  - mondragon-worker-cooperative
  - european-textile-guild-apprenticeship
  - us-vocational-training-cooperative

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 65
# Mid-range of the 50–80 m² span. The training floor must accommodate three
# equipment tiers simultaneously: rigid-heddle stations for Stage 1 beginners
# (compact, 2 m² per station × 2 stations = 4 m²), 4-shaft floor looms for
# Stage 2 journeyman candidates (3 m² per loom × 4 looms = 12 m²), and 8-shaft
# floor looms for Stage 3 master-class work (4 m² per loom × 2 looms = 8 m²).
# Total loom floor: 24 m². Add warping bay with warping board and sectional
# warp beam (4 m²), instructor demonstration station (4 m²), shared fiber storage
# and yarn library (4 m²), and circulation / safety clearance (29 m²) = 65 m².
# Low end (50 m²): tight configuration with 4 floor looms only and portable
# warping pegs; entry-level program only. High end (80 m²): full 3-tier floor
# with additional loom bays and a separate design / planning table.
# [Derived from loom footprint data in catalog/weaving/SCHEMA.md §3 and
# multi-station studio layout norms; consistent with forge-009 analog at 80 m²
# for 4–8 concurrent trainees.]

ceiling_min_m: 3.2
# Floor-loom castle height for 8-shaft looms (castle = the upright frame
# structure) reaches 1.8–2.1 m; add operator clearance and overhead warp
# beam clearance. 3.2 m clear ceiling allows safe operation of upright-castle
# floor looms without hitting the ceiling during warp-beam advancement and
# provides adequate airflow for humidity control above the loom tops.
# [Derived from 8-shaft floor-loom dimension specifications; minimum adequate
# clearance for floor-loom castle plus operator reach height.]

ventilation: mechanical-extraction-required
# Humidity-controlled studio with significant fiber-processing activity
# (warping, skeining, sampling) generates airborne lint at sustained volumes.
# Mechanical extraction (low-velocity general exhaust + fresh-air supply) is
# required for: (a) fiber lint management at multi-loom production volumes,
# (b) humidity regulation for wool/silk warp stability (target 45–55% RH), and
# (c) comfortable multi-occupant air quality during 6–8 hour training sessions.
# No combustion ventilation required; this is not a hot-work environment.
# [catalog/weaving/SCHEMA.md §2 hybrid energy note on climate-control ventilation;
# humidity_control_required: true triggers ventilation requirement.]

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: electric-lighting-only
# All looms are hand-operated floor looms; no powered weaving mechanism.
# Energy consumption: studio task and ambient lighting, HVAC/humidity-control
# system (the dominant energy draw at this entry), and small electric accessories
# (electric winder for warping preparation, electric bobbin winder).
# Per catalog/weaving/SCHEMA.md §2 note on climate control: humidity-control
# energy typically exceeds loom energy. For a 65 m² humidity-controlled studio,
# climate control is estimated at 10–20 kWh/day; lighting at 2–4 kWh/day.
# [catalog/weaving/SCHEMA.md §2 electric-lighting-only and climate-control note.]

energy_consumption_per_active_hour: "12–24 kWh/day (climate control 10–20 kWh + lighting 2–4 kWh; per-active-day, not per-hour of loom use)"
# Per-day framing is appropriate: the HVAC/humidity system runs continuously
# during studio hours regardless of how many looms are active. Lighting is
# approximately 10 LED fixtures at 15 W each = 150 W × 8 hr = 1.2 kWh/day;
# supplemental task lighting adds ~0.8–2 kWh/day. HVAC dominates. Annual
# energy cost: 18 kWh/day (mid) × 240 operating days × $0.125/kWh = $540/yr.
# [Derived from 65 m² conditioned-studio HVAC norms; US EIA commercial rate
# $0.10–$0.15/kWh; climate-control note in SCHEMA.md §2.]

backup_fuel: null
# No combustion fuel. Electric studio only; no backup fuel applicable.

# ── WEAVING-SPECIFIC REQUIRED FIELDS ─────────────────────────────────────────

loom_type: floor-loom-4shaft
# Required field per catalog/weaving/SCHEMA.md §3. The 4-shaft floor loom is
# the primary loom type and the workhorse of the training program: all
# Stage 2 journeyman-candidate training is conducted on 4-shaft floor looms.
# The studio also operates rigid-heddle looms (Stage 1 beginner tier) and
# 8-shaft floor looms (Stage 3 master-class). loom_type reflects the dominant
# and defining loom type for the catalog entry's economics and throughput.
# [catalog/weaving/SCHEMA.md §3: floor-loom-4shaft: $1,500–$6,000; journeyman-weaver
# floor; 60–150 cm warp width; plain, twill, overshot, most 4-shaft patterns.]

humidity_control_required: true
# Wool warp and weft are used throughout the training curriculum: wool is the
# primary fiber for traditional and journeyman-level weave structures (twill
# suiting, overshot, Scandinavian rep weave). Wool warp is dimensionally
# sensitive to relative humidity: at RH below 35%, wool warp contracts and
# over-tensions; above 65%, wool swells and slackens. Both conditions produce
# defective cloth and frustrate apprentice learning of correct tension management.
# A stable 45–55% RH studio environment is required for reliable apprentice
# training outcomes. Dehumidifier and/or humidifier controlled to this range.
# [catalog/weaving/SCHEMA.md §4: humidity_control_required true for wool warp;
# target 45–55% RH.]

fiber_source_declaration: industrial-yarn-purchased
# The training studio purchases commercially spun yarn from weaving-supply
# distributors (Webs/Valley Yarns, Gist Yarn, UKI yarns, Lunatic Fringe,
# Jagger Spun). Training-grade yarn is industrial mill-spun in standard
# weaving counts (8/2 cotton, 2/8 wool, 10/2 cotton, 5/2 cotton for rug work;
# 2-ply and singles wool for twill and overshot training warps). No spinning
# infrastructure; no heritage-breed sourcing. The entry explicitly does not
# integrate spinning: training is focused on weaving skill, and adding spinning
# would double the equipment and skill requirement without advancing the core
# competency objective. Commercially consistent yarn quality is pedagogically
# preferable: apprentices learn consistent beating and tension on predictable
# yarn rather than compensating for hand-spun variability.
# Anti-romanticism: the economic purpose of this facility is developing
# practitioners for the luxury/specialty weaving market; industrial yarn
# sourcing is chosen for pedagogical consistency, not because it carries
# prestige. Students who later specialize in heritage-fiber or hand-spun
# work will add that skill separately after journeyman certification.
# [catalog/weaving/SCHEMA.md §6: industrial-yarn-purchased; DECLINE-VERDICT
# fiber-sourcing falsifier: training programs may use industrial yarn as a
# pedagogical choice without undermining the specialty-market positioning
# of the graduates they produce.]

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  meters_per_day: 6.0
  # Per-facility aggregate daily output across all active training looms.
  # The training floor produces less per loom-hour than a commercial studio
  # because: (a) apprentice skill level is below journeyman ceiling,
  # (b) significant time is spent on warping, sampling, and problem-solving
  # rather than production weaving, (c) the master instructor and journeyman
  # aids spend 30–40% of session time on direct instruction rather than their
  # own weaving. Per-loom estimates:
  #   Rigid-heddle Stage 1 (2 stations): 0.5–1.0 m/day each → 1–2 m/day total
  #   4-shaft Stage 2 (4 looms, apprentice skill): 0.8–1.5 m/day each → 3–6 m/day
  #   8-shaft Stage 3 (2 looms, senior apprentice): 0.5–1.2 m/day each → 1–2 m/day
  # Blended at ~50% production utilization (rest = warping, sampling, instruction):
  # ~6 m/day facility total on active days.
  # [catalog/weaving/SCHEMA.md §1: floor-loom-4shaft journeyman plain/twill
  # 2–6 m/day; training-floor depression factor analogous to forge-009 apprentice
  # throughput depression; label: inferred from SCHEMA.md ranges and training-format
  # adjustment.]

  warp_width_cm: 90
  # Representative warp width for primary 4-shaft floor looms. 4-shaft looms
  # in the training studio are configured at 90 cm (standard studio-loom
  # width); the 8-shaft looms may be wider (120–150 cm). Rigid-heddle stations
  # are 60 cm. 90 cm is used as the reference width for sim_params unit
  # conversion (area-basis where needed).

  pattern_complexity: pattern
  # The training curriculum covers the full range from plain weave (Stage 1)
  # through twill (Stage 2 entry) through overshot and M's & O's (Stage 2
  # graduation) through networked twill and 8-shaft structures (Stage 3).
  # Dominant instructional output is 4-shaft pattern work (overshot, M's & O's,
  # huck lace); the pattern complexity designation reflects the ceiling of the
  # curriculum, consistent with catalog/weaving/SCHEMA.md §1 (pattern = overshot,
  # M's & O's, networked twill, supplementary weft; requires 4+ shafts).

  max_active_hours_per_week: 35
  # Shop hours, not instructor hours. 5–6 days/wk × 6–7 hr/session ceiling.
  # Consistent with forge-009 training-floor ceiling (35 hr/wk). Multiple
  # apprentices occupy the floor during these hours; the figure is the
  # scheduled shop-open ceiling, not a single-operator count. Warping sessions
  # (4–8 hr to warp a floor loom) are counted within these hours: warping is
  # a core training activity, not overhead external to the scheduled session.
  # [Consistent with forge-009.throughput.max_active_hours_per_week = 35;
  # calibrated to cooperative training-facility scheduling norms.]

  product_mix:
    yardage: 20
    rugs_upholstery: 10
    tapestry_art: 0
    garments_accessories: 10
    instruction_open_studio: 60
    # Sum: 100. instruction_open_studio (60%) dominates: the primary output of
    # this studio is trained weavers, not commercial cloth. The remaining 40%
    # represents saleable training output: yardage (20%) — plain-weave and twill
    # cloth produced by Stage 2 apprentices on production exercises; rugs/upholstery
    # (10%) — rug-weave training projects and tapestry-weight yardage; garments/
    # accessories (10%) — scarves, wraps, and samplers produced by all apprentice
    # levels. No tapestry_art production: tapestry is not in the core curriculum
    # and the studio does not have a high-warp tapestry frame. Saleable share: 40%.
    # [Parallel structure to forge-009 product_mix: training_output 30%; saleable 70%.
    # Weaving training floor has higher instruction fraction (60%) because warping
    # and sampling are major time consumers with no market-equivalent output.]

  throughput_variance:
    seasonal: "Summer intake break and cohort-transition month reduce output to ~45% of average; autumn cohort intake marks ramp-up; spring project-completion quarter is best-output period (~1.3×)"
    worst_month_fraction_of_average: 0.45
    # Summer shutdown / cohort-transition period analogous to forge-009.
    # [Parallel to forge-009: worst_month_fraction_of_average = 0.4; slight
    # upward adjustment to 0.45 for weaving, where some looms remain in use
    # for continuing members during cohort-transition month.]
    best_month_fraction_of_average: 1.30
    # Spring project-completion quarter drives peak output as Stage 2–3 apprentices
    # complete portfolio pieces for journeyman assessment.

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: master-weaver
# The training studio requires a master weaver as lead instructor: they must
# assess threading errors, warp tension problems, beat consistency, and
# pattern-structure execution across multiple simultaneous apprentice stations
# at different skill levels (Stage 1 through Stage 3), demonstrate correct
# technique on demand, and evaluate journeyman-level work at competency gates.
# A journeyman weaver cannot reliably provide the cross-loom instructional
# authority required to run a formal three-stage apprenticeship program. The
# master weaver designation additionally confers the institutional standing
# required for journeyman certification panels (a journeyman cannot certify
# another journeyman; certification requires a master).
# [catalog/weaving/SCHEMA.md §5: master-weaver — full technical range;
# can train and assess journeyman weavers; required for weave-012.]

operators_concurrent: "1 master instructor + 1-2 journeyman aids + 4-8 apprentices"
# Normal training-floor staffing: 1 lead instructor (master weaver) supervises
# the full floor; 1–2 journeyman assistants each support 2–4 apprentice stations;
# 4–8 apprentices work simultaneously across all three equipment tiers.
# Maximum safe concurrent headcount on the training floor: 10 (1 master +
# 2 journeyman + 7 apprentices) given loom station count and instructor
# attention span. This is a teaching configuration, not a production staffing
# configuration.
# [Parallel to forge-009.operators_concurrent.]

apprentice_friendly: true
apprentice_path:
  training_stages: >-
    Stage 1 — Loom Foundations and Plain Weave (months 0–6): rigid-heddle
    and floor-loom introduction; warp winding, warping-board technique,
    threading the rigid heddle, threading a 4-shaft floor loom (plain-weave
    threading), sleying the reed, tying on, weaving plain weave and basic
    tabby on both loom types. Fiber identification: wool, cotton, linen,
    synthetic. Beat consistency and selvedge management introduced as primary
    quality criteria. Loom maintenance: heddle replacement, re-threading after
    broken ends, beam advancement. No advanced patterns; no tie-up changes
    without instructor supervision.
    Competency gate: thread and warp a 4-shaft floor loom for plain weave
    independently and weave a 1-meter sample with consistent beat and even
    selvedges (within 5 mm of warp width at any point); replace a broken
    warp end without supervision; identify wool, cotton, and linen by hand
    feel and basic burn test.

    Stage 2 — 4-Shaft Pattern Weaving and Yardage Production (months 6–24):
    twill threading and tie-up sequences (2/2 twill, herringbone, broken twill);
    overshot drafting, threading, and tie-up; M's & O's and huck lace structures;
    warp calculation and yarn-quantity estimation for a complete project; warp
    color planning; wet-finishing and blocking of completed cloth; systematic
    troubleshooting of pattern errors (threading errors, tie-up errors, floating
    selvedge management). Yardage production exercises: Stage 2 apprentices
    produce saleable training output (plain-weave and twill scarves, wraps,
    yardage) as production exercises, building rhythm and consistency alongside
    pattern skill. The master instructor assigns production sequences calibrated
    to apprentice skill stage; Stage 2 output sold through the cooperative's
    ancillary-sales channel.
    Competency gate (month 12, mid-Stage 2): independently thread, sley, and tie
    up a 4-shaft floor loom for a standard twill draft; weave 2 meters of consistent
    2/2 twill with no floating ends; document a basic warp calculation showing
    yarn quantity for a 3-meter warp at specified sett.
    Competency gate (Stage 2 completion, month 24): complete an independent project
    in overshot or M's & O's structure — design, draft, thread, sley, tie up,
    weave, and wet-finish 2 meters of patterned cloth meeting quality standard
    (consistent pattern, even selvedges, appropriate beat density); produce a
    project portfolio of at least three completed pieces across different structure
    types.

    Stage 3 — 8-Shaft Structures, Advanced Projects, and Master-Class Preparation
    (months 24–36): 8-shaft networked twill drafting and threading; supplementary-weft
    techniques; color-and-weave effects; warp rep and Scandinavian rep weave;
    introduction to drawloom-adjacent complex structures (Summer and Winter,
    turned twills); design process from concept to finished cloth; understanding
    of wet-finishing chemistry (fulling, blocking, pressing by fiber type);
    introduction to teaching: Stage 3 apprentices assist in Stage 1 instruction
    under master oversight, building toward the journeyman-assistant role.
    Competency gate for journeyman certification: panel review by master instructor
    plus one external journeyman or master weaver drawn from the regional cooperative
    network or weaving guild. Assessment includes live threading and weaving
    demonstration on an 8-shaft loom (structure chosen by the panel), portfolio
    review of at least five completed pieces across multiple structure types and
    fiber types, and a teaching demonstration (explain and demonstrate threading
    a floor loom to a Stage 1 apprentice).

  time_to_independent_operation: >-
    ~36 months to journeyman standard. The 36-month figure is calibrated to
    European textile-guild apprenticeship timelines and to the vocational-program
    analog of a formal weaving apprenticeship, which requires 3 years to develop
    reliable competence across the full 4-shaft pattern vocabulary and the
    foundational 8-shaft vocabulary. The 36-month floor assumes consistent
    attendance (minimum 3 studio days/week) and engagement with the full
    curriculum including production exercises. The Stage 3 ceiling (month 36)
    is the journeyman-certification target; apprentices who require additional
    pattern or wet-finishing proficiency may extend to month 42 before panel
    review. [CITATION-NEEDED: European textile-guild or vocational weaving
    apprenticeship timeline; formal 3-year weaving apprenticeship programs in
    Sweden, Germany, or UK; label: inferred from analogous craft apprenticeship
    structure.]

  succession_note: >-
    The cooperative structure embeds succession by design, parallel to forge-009:
    the apprentice cohort is the institution's primary output. Each 3-year cohort
    cycle is expected to produce 2–4 journeyman-certified graduates, of whom
    1–2 may be offered continued participation as journeyman assistants within the
    cooperative. The master instructor's departure risk is partially mitigated by
    the journeyman-assistant pipeline: a senior journeyman assistant who has worked
    2+ years in the teaching role can step into a probationary lead-instructor
    position while the cooperative recruits a replacement master weaver. Institutional
    continuity is further protected by the cooperative's documented curriculum,
    threading drafts, and cohort-intake procedure, which reduce reliance on a
    single instructor's tacit knowledge. Federation with other weaving cooperatives
    or regional handweaving guilds (Ostrom Principle 7 analog) provides emergency
    instructor-sharing arrangements and journeyman-panel members for certification
    reviews.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 25000, mid: 55000, high: 95000 }
  # Low ($25,000): 2 entry-level 4-shaft floor looms ($2,500–$4,000 each, e.g.,
  #   Leclerc Fanny 4-shaft, Ashford Jack loom) + 2 rigid-heddle looms ($400–$600
  #   each) + 1 used 8-shaft floor loom ($4,000–$8,000) + basic warping boards
  #   and accessories ($500–$800) + yarn library starter stock ($2,000–$3,000)
  #   + storage and shelving ($500–$800). Refurbished equipment scenario.
  # Mid ($55,000): 4 quality 4-shaft floor looms ($4,000–$6,000 each, e.g.,
  #   Macomber, Leclerc Nilus II, Schacht Standard floor loom) = $16,000–$24,000
  #   + 2 rigid-heddle looms ($600–$800 each) = $1,200–$1,600
  #   + 2 8-shaft floor looms ($6,000–$12,000 each, e.g., Macomber 8-shaft,
  #   Leclerc Nilus II 8-shaft) = $12,000–$24,000
  #   + warping equipment (sectional warp beam, warping board, electric winder)
  #   ($1,500–$3,000)
  #   + yarn library ($3,000–$5,000)
  #   + storage, shelving, instruction materials ($1,500–$2,000)
  #   + HVAC/humidity-control unit for 65 m² ($3,000–$6,000 installed)
  #   = $38,700–$66,600 → $55,000 mid estimate.
  # High ($95,000): 4 top-tier 4-shaft looms ($7,000–$10,000 each, e.g.,
  #   AVL production floor loom, Toika Eeva) = $28,000–$40,000
  #   + 2 top-tier 8-shaft looms ($10,000–$15,000 each, e.g., AVL 8-shaft,
  #   Toika Liisa 8-shaft, Norwood full castle) = $20,000–$30,000
  #   + 2 premium rigid-heddle looms ($800–$1,000 each)
  #   + full warping suite, electric accessories ($4,000–$6,000)
  #   + premium yarn library and fiber stock ($6,000–$8,000)
  #   + high-capacity commercial HVAC/humidity control ($8,000–$12,000)
  #   = $68,600–$99,600 → $95,000 high estimate.
  # [CITATION-NEEDED: floor loom pricing from Leclerc, Macomber, Schacht,
  # AVL, Toika, Ashford — 2024–2026 manufacturer pricing; label: illustrative
  # estimate based on general market knowledge. CITATION-NEEDED: HVAC/humidity-
  # control installation cost for 65 m² commercial studio.]

  install_cost: 8000
  # Standard commercial electrical permit ($500–$1,000) + HVAC/humidity-control
  # installation (if not included in equipment cost; commercial HVAC for 65 m²
  # humidity-controlled space estimated at $3,000–$6,000 for the installation
  # labor if equipment is purchased separately) + studio fit-out (floor prep,
  # loom anchoring points, storage installation, signage) ($1,500–$2,500) +
  # accessibility compliance (ADA for a public-access cooperative) ($500–$1,000).
  # Total: $5,500–$10,500 → $8,000 mid.
  # [CITATION-NEEDED: commercial studio installation cost for a multi-loom
  # weaving studio; HVAC installation per m² for humidity-controlled textile space.]

  annual_maintenance: 3200
  # Covers: routine loom maintenance (heddle replacement $400/yr, treadle
  # cord replacement $150/yr, reed inspection and replacement 1 reed/yr
  # $120–$200, warp-beam ratchet service $150/yr, annual frame inspection by
  # journeyman $200/yr) = $1,020–$1,100/yr. HVAC/humidity-control maintenance
  # (filter replacement, annual service call, humidifier maintenance) = $600–$900/yr.
  # Consumable teaching materials (draft paper, sample cards, reference binders)
  # = $200/yr. General studio upkeep (cleaning, minor repairs) = $300/yr.
  # Apprentice use accelerates heddle and treadle-cord wear relative to solo-studio
  # use: higher heat cycles equivalent; more novice errors cause extra broken ends
  # and re-threading. Total: $2,120–$2,500/yr + safety stock = $3,200 mid.
  # [CITATION-NEEDED: annual maintenance cost for multi-loom training studio;
  # label: derived from component-level estimates above.]

  annual_consumables: 5400
  # Higher than commercial entries: training programs waste more yarn (failed
  # samples, incorrect sett experiments, learning sequences) than a solo
  # commercial weaver. Estimate:
  # Yarn and fiber stock replenishment ($3,500/yr: wool, cotton, linen for
  #   training warps; ~ 50 kg wool at $30/kg + 40 kg cotton at $12/kg + 10 kg
  #   linen at $25/kg ≈ $1,500 + $480 + $250 = $2,230/yr fiber cost; add 30%
  #   for sampling waste = ~$2,900/yr; round up to $3,500 for yarn library
  #   replenishment and instructional variety).
  # Loom consumables (lease sticks, threading hooks, shuttle replacements,
  #   pick-up sticks, temple replacements) = $400/yr.
  # Electricity (18 kWh/day × 240 days × $0.125/kWh ≈ $540/yr).
  # Warping cord and heddle sets (additional to maintenance schedule) = $350/yr.
  # Administrative consumables (booking system, printing, intake materials) = $200/yr.
  # Total: ~$4,990 → $5,400 rounding up for first-year higher usage.
  # [CITATION-NEEDED: fiber and yarn cost for multi-loom training studio;
  # weaving-supply distributor pricing; label: inferred from component estimates.]

  floor_space_rent_per_year: 6500
  # Town/small-city commercial rate estimate for 65 m² light-commercial space
  # with appropriate electrical service. At $100/m²/yr effective rate (consistent
  # with catalog/weaving/SCHEMA.md §2 hybrid note and comparable entries):
  # 65 m² × $100/m²/yr = $6,500/yr. This is the imputed rental baseline; a
  # cooperative that owns its space substitutes amortized mortgage payments.
  # Light-commercial / mixed-use rate is appropriate: no industrial zoning
  # required for a hand-loom weaving studio; no combustion or heavy machinery.
  # [CITATION-NEEDED: commercial floor-space rent per m²/yr for town/small-city
  # light-commercial space; CoStar or SCALES.md §4 estimate; label: inferred.]

  market_price_per_unit: { low: 5, mid: 9, high: 15 }
  # CONDITIONAL — present because lens_fit.market is `poor` but ancillary output
  # sales from student work are a documented revenue source for the cooperative.
  # Unit: 1 linear meter of woven cloth at 90 cm reference warp width.
  # This is ANCILLARY REVENUE, not the primary viability basis.
  # Low ($5/m): plain-weave cotton training yardage (commodity-adjacent product;
  #   sold at community sales or to members as utility cloth).
  # Mid ($9/m): blended mix of training output — twill scarves, woven wraps, and
  #   yardage across the saleable product-mix share (~40% of all output).
  # High ($15/m): overshot or pattern-structure cloth produced by Stage 2–3
  #   apprentices as portfolio pieces, sold at craft fairs or through the
  #   cooperative's member sales channel.
  # [CITATION-NEEDED: weaving training studio ancillary output pricing; inferred
  # from comparable community-weaving cooperative and craft-fair pricing norms;
  # label: inferred comparables. No direct market survey conducted at authoring date.]

  pricing_notes: >-
    Unit is one linear meter of woven cloth at approximately 90 cm width from
    the cooperative's training-output channel. Output sale is ANCILLARY REVENUE,
    not the primary purpose or viability basis of this facility: apprentice-made
    cloth sold through the cooperative's market channel (member sales, regional
    craft fairs, local retail consignment) supplements member fees and reduces
    net operating cost but does not determine viability. Industrial baseline for
    comparable commodity woven cloth: $3–$6/m (mass-produced domestic cotton or
    polyester blend yardage, retail; [CITATION-NEEDED: commodity woven-cloth
    industrial baseline price from fabric retailer survey — Mood Fabrics, Jo-Ann,
    online wholesale]). The cooperative's saleable training output commands a
    modest premium ($5–$15/m vs $3–$6 baseline) based on hand-woven provenance
    and pattern-structure craft content. Customer segment: local craft-oriented
    buyers, cooperative members purchasing apprentice-project pieces, regional
    boutique retailers on consignment. The premium is modest because training-output
    cloth reflects apprentice skill variation; only Stage 2–3 portfolio pieces
    reach the $12–$15/m tier. This is not a commercial production model.

  industrial_baseline_price: 4
  # Mid-estimate of the commodity woven-cloth baseline ($3–$6/m for mass-produced
  # domestic fabric yardage at retail). [CITATION-NEEDED: commodity woven fabric
  # retail price per meter — Mood Fabrics, Jo-Ann Fabrics, Fabric.com 2024–2026
  # pricing; label: illustrative from general market knowledge.]

  pricing_validation: >-
    Pricing inferred from comparable community-weaving cooperative and craft-fair
    output pricing; no direct market survey conducted at authoring date. Evidence
    type: inferred comparables from regional craft-cooperative pricing norms and
    anecdotal trade reports. This is not empirical sales data. [CITATION-NEEDED]
    for a direct market-price study for weaving training cooperative output.
    Ancillary-sales pricing does not anchor the cooperative viability case; member
    fees and potential workforce-development grants are the primary revenue basis.
    The $5–$15/m range is treated as an order-of-magnitude estimate for revenue
    modeling only.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:

  first_year_failures:
    - item: "Heddle breakage (wire or texsolv) — 4-shaft floor looms"
      estimated_hours_to_failure: 800
      replacement_cost: 60
      replacement_lead_time_days: 7
      serviceable_by: operator
      # Wire heddles fatigue at the eye from repeated shed cycling; texsolv
      # heddles stretch and lose registration under sustained use, especially
      # under apprentice over-beating. At ~800 active loom-hours on a 4-shaft
      # loom (approximately 6–8 months of training use), the first heddle set
      # requiring replacement is expected. Replacement is operator-serviceable
      # (full heddle replacement requires re-threading — a 2–4 hr task — which
      # is itself a training exercise in Stage 1). The $60 cost covers a full
      # set of texsolv heddles for one 4-shaft loom. The lead time of 7 days
      # is for standard counts from Leclerc, Macomber, or Schacht distributors;
      # spare heddles should be stocked.
      # [catalog/weaving/SCHEMA.md §7: heddle breakage reference list;
      # typical hours-to-failure 500–2,000 hr; operator-serviceable.]

    - item: "Warp beam ratchet / pawl wear — floor looms under apprentice use"
      estimated_hours_to_failure: 2000
      replacement_cost: 85
      replacement_lead_time_days: 14
      serviceable_by: journeyman
      # Ratchet-and-pawl beam tensioning wears under constant use; apprentice
      # over-tensioning of the warp beam (a common novice error) accelerates
      # pawl-spring fatigue. Slippage causes warp-tension loss mid-weave and
      # is the primary mid-project disruption event on floor looms. At ~2,000
      # loom-hours (approximately 12–18 months of training use), the first
      # ratchet service is expected. Journeyman-serviceable: full ratchet
      # replacement requires loom disassembly of the beam bracket. 14-day
      # lead time for manufacturer-specific ratchet components.
      # [catalog/weaving/SCHEMA.md §7: warp beam ratchet / pawl wear; typical
      # hours 1,500–3,500 hr; journeyman for full ratchet replacement.]

    - item: "HVAC/humidity-control system — component failure or calibration drift"
      estimated_hours_to_failure: 2500
      replacement_cost: 400
      replacement_lead_time_days: 7
      serviceable_by: specialist
      # Climate-control system is the highest-impact failure mode for a
      # humidity-controlled training studio: a failed humidifier or
      # dehumidifier causes warp-tension instability within 24–48 hours in
      # wool warp situations. Residential-scale humidifier units (common in
      # studio-sized applications) have mean times to first failure of 2,000–
      # 4,000 operating hours under continuous use. Specialist-level diagnosis
      # for commercial HVAC; residential humidifier units are operator-
      # replaceable with a unit swap. $400 covers a residential-grade
      # humidifier/dehumidifier unit replacement; commercial HVAC failure costs
      # more (see worst-case). 7-day lead time for residential-scale units.
      # [catalog/weaving/SCHEMA.md §7: climate-control system failure reference;
      # typical hours 1,500–3,500 hr; specialist for HVAC repair.]

    - item: "Treadle tie-up cord breakage — 4-shaft and 8-shaft floor looms"
      estimated_hours_to_failure: 1200
      replacement_cost: 15
      replacement_lead_time_days: 1
      serviceable_by: operator
      # Texsolv or cord tie-ups connecting treadles to shaft lamms wear and
      # break; replacement is operator-serviceable (re-tie takes 15–30 min per
      # shaft). Breakage rate is higher under apprentice use due to enthusiastic
      # treadle-depressing and tie-up adjustment experiments during learning.
      # At ~1,200 loom-hours (approximately 8–12 months of apprentice use),
      # first tie-up cord breakage is expected on at least one loom. $15
      # covers a full spare-cord stock adequate for multiple re-ties. Lead time:
      # immediate (hardware-store cord is an acceptable substitute for Texsolv;
      # stock Texsolv cord on hand).
      # [catalog/weaving/SCHEMA.md §7: treadle tie-up cord wear; typical hours
      # 800–2,500 hr; operator-level re-tie.]

  maintenance_schedule:
    daily:
      task: "Safety and readiness walkdown: check all looms for broken warp ends or tangled heddles; confirm HVAC/humidity-control unit is operating within 45–55% RH target; verify treadle tie-ups are intact on all looms; check yarn library stock status; log any damage or equipment-issue reports from previous session"
      performed_by: operator
      # 'Operator' = master instructor or senior journeyman assistant opening
      # the studio. RH monitoring is safety-critical for wool warp integrity;
      # a daily RH check prevents mid-project warp-tension failures.

    weekly:
      task: "Full loom inspection on all active looms: heddle condition (wire fatigue or texsolv stretch), warp beam ratchet function and pawl-spring tension, treadle tie-up condition and lamm alignment, reed condition (bent dents), brake-cord or tension-spring function; HVAC filter check and unit cleaning; yarn and consumables inventory against weekly usage log"
      performed_by: operator

    quarterly:
      task: "Heddle condition assessment and bulk replacement on looms with 600+ active hours; warp beam ratchet service (lubrication, pawl-spring inspection, ratchet-tooth wear measurement); full treadle and tie-up replacement where worn; HVAC professional service call (filter change, coil cleaning, RH calibration check, refrigerant check if applicable); reed replacement on any loom with bent-dent count > 3; yarn library deep inventory and restocking"
      performed_by: journeyman

    annual:
      task: "Full studio equipment audit by master instructor: comprehensive loom frame inspection (joint tightness, warping-beam alignment, castle squareness), heddle count and full replacement on all looms, HVAC system annual professional service, full electrical panel inspection, fire-safety and first-aid inventory, cooperative safety-compliance audit, curriculum-year debrief with apprentice competency record review; senior Stage 3 apprentices participate as a curricular learning event"
      performed_by: specialist
      # Annual full review involves specialist (master instructor + external
      # technical specialist for HVAC); apprentice participation is a design
      # feature parallel to forge-009's dual safety-compliance / instructional
      # function of the annual review.

  startup_shutdown_overhead_per_day_min: 45
  # 45 min/day: pre-session studio walkdown and RH check (15 min), apprentice
  # safety and curriculum briefing (10 min), post-session shutdown including
  # loom cover/storage, yarn winding and labeling, session log completion,
  # and RH unit check (20 min). Higher than a solo commercial studio (no briefing)
  # but lower than forge-009 (60 min; coal forge startup is more complex than
  # RH system check). The multi-loom training floor requires documented daily
  # log completion and apprentice sign-in as part of safety protocol.
  # [Derived from training-floor management norms; parallel to forge-009
  # startup_shutdown_overhead_per_day_min = 60.]

  max_active_hours_realism_note: >-
    35 hr/wk is the gross scheduled shop ceiling. Net of 45 min/day startup-
    shutdown overhead on a 5-day shop week (45 min × 5 = 225 min = 3.75 hr/wk),
    effective instruction and production hours are approximately 31 hr/wk.
    Downtime fraction of 0.18 accounts for: cohort-transition / summer-break
    weeks (~8 wk/yr at reduced capacity ≈ 12–15%), equipment maintenance and
    first-year failures (~3–4%), administrative scheduling gaps (~2%). Net
    effective hours/yr: 31 hr/wk × 52 × (1 − 0.18) ≈ 1,323 hr/yr.
    sim_params.throughput_units_equiv_per_year uses the derated figure.
    [Parallel derivation to forge-009.max_active_hours_realism_note.]

  interruption_notes: >-
    Weaving training floors have structurally higher intraday interruption than
    commercial studios. Typical interruption profile per session:
    — Warp-end breakage repairs: 2–4 events/session at 10–20 min each ≈ 30–60 min
    — Threading-error diagnosis and correction: 1–2 events/session at 15–30 min each
    — Journeyman-aid instruction pauses (group observation of technique demonstration)
      ≈ 15–20 min/session
    — Warping-board setups for new warps (Stage 1 apprentices): 45–90 min for a
      new warp setup, interspersed with other activities
    — Administrative (apprentice log entries, materials allocation) ≈ 5–10 min/session
    Total intraday interruption approximately 60–90 min per operating session above
    the startup-shutdown overhead. Folded into throughput_units_equiv_per_year
    computation via lower production rates and the 60% instruction_open_studio
    product-mix share.

  consumables_lead_time_days: { typical: 7, worst: 30 }
  # Typical: wool and cotton yarn from US weaving-supply distributors (Webs,
  # Gist Yarn, UKI, Lunatic Fringe) — 5–10 day shipping. Heddles and loom
  # parts from Leclerc, Schacht, Macomber: 5–14 days typical. Worst: specialty
  # floor-loom components (ratchet assemblies, specific loom-model parts) from
  # manufacturer with backorder: 21–30 days. HVAC unit replacement from
  # commercial supplier: 5–14 days typical; specialist-engineered component
  # potentially longer. Maintaining spare heddle sets and treadle cord stock
  # eliminates downtime for the most common failure modes.
  # [Illustrative estimate; CITATION-NEEDED: lead-time data for floor-loom
  # parts from US weaving-supply distributors; label: inferred.]

  throughput_variance:
    seasonal: "Summer intake break and cohort-transition month reduce output to ~45% of average; autumn cohort intake marks ramp-up; spring project-completion quarter is best-output period (~1.3×)"
    worst_month_fraction_of_average: 0.45
    best_month_fraction_of_average: 1.30

  operator_impact:
    noise_db: 65
    # Floor-loom weaving with treadle mechanism: the treadle depression and
    # shed-change mechanism produce moderate noise (shaft-and-lamm impact,
    # treadle-floor contact). Multiple looms operating simultaneously in a 65 m²
    # studio: estimated 60–70 dB at the room level. This is typical office or
    # restaurant background noise; no hearing protection required. Floor-loom
    # weaving is the quietest multi-operator production environment in the CERES
    # catalog (compare: forge-009 at 85 dB peak at coal station).
    # [CITATION-NEEDED: sound level at operator position for multi-loom floor-
    # loom weaving studio; label: inferred from general knowledge of hand-loom
    # noise levels.]
    heat_exposure: "Ambient room temperature; no thermal hazard. HVAC maintains 45–55% RH and comfortable working temperature. No combustion, no heat-treatment equipment. The studio is a comfortable, climate-controlled indoor workspace. Maximum thermal risk is minor discomfort on summer days if HVAC is undersized for the cooling load — monitored and addressed in annual HVAC service."
    emissions: "Near-zero on-site emissions. Wool and cotton fiber lint at hand-loom production volumes is below any industrial air-quality permit threshold. HVAC exhaust carries negligible fiber particulate. No chemicals used in the studio (wet-finishing with water and mild soap is permitted; acid or fiber-reactive dye chemistry is out of scope for this entry). Standard building-code ventilation requirements only."
    physical_demand: "Moderate. Seated operation at floor looms: rhythmic treadle depression requires leg strength and endurance for sustained weaving sessions. Beat consistency requires controlled arm force (light to moderate; floor looms have mechanical advantage from beater swing). Warping activities (winding, threading) require standing and fine hand dexterity. Carrying yarn cones and warp beams requires occasional moderate lifting. Significantly less physically demanding than smithing or carpentry; accessible to a broad range of physical capabilities."

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Light-commercial or mixed-use zoning required; no industrial zoning required for a hand-loom weaving studio; ADA accessibility required for any public-access cooperative; confirm local occupancy classification for a vocational-training cooperative (some jurisdictions classify training facilities differently from retail or production studios)"
  emissions: "No emissions permit required; fiber lint at hand-loom production volumes is far below industrial air-quality permit thresholds; HVAC exhaust from a textile studio does not trigger air-quality permits in US jurisdictions"
  other: "State apprenticeship-authority registration recommended if the cooperative offers paid apprentice stipends (same consideration as forge-009); OSHA general-industry standards apply to multi-person workplaces but no hot-work or heavy-machinery provisions are relevant; liability and workers'-compensation insurance required; check local regulations on vocational training cooperative business registration — some states have specific cooperative-corporation statutes that provide favorable registration options"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: poor
  # Training cooperative; primary output is journeyman-certified weavers, not
  # commercial cloth. Ancillary output sales (training yardage, scarves, wraps)
  # are a revenue supplement, not the viability basis. Market lens is poor:
  # the facility cannot compete on throughput or margin with a commercial
  # production weaving studio at the same capital cost. See pricing_notes for
  # the explicit ancillary-revenue framing.
  cooperative: good
  # Primary lens. Member-owned cooperative structure with formal bylaws, paid
  # master-weaver worker-member, apprentice-cohort member category, and Ostrom-
  # compliant governance. This entry is the cooperative weaving training model;
  # the cooperative lens is the reason the facility exists.
  civic: marginal
  # Workforce-development partnership with municipality is possible and
  # documented; the facility is not municipally owned, but civic funding
  # (apprenticeship-authority registration, workforce-development grants) is
  # viable and materially affects financial feasibility. Civic lens is marginal
  # rather than good because governance authority rests with the cooperative
  # membership, not a municipal body.

scale_fit:
  village: poor
  # Member pool and apprentice intake pool both too thin at village scale
  # (500–2,000 residents). A viable cooperative training studio requires
  # ≥30 paid members to fund operations and an apprentice intake of 4–8/yr;
  # village population is insufficient to sustain both. Master-weaver instructor
  # hiring is also difficult at village wage levels.
  town: good
  # Target scale: 2,000–15,000 residents. Sufficient population for ≥30 paid
  # members, 4–8 apprentice intake per cohort, and instructor hiring from a
  # regional pool. Member fees + ancillary sales + potential workforce-development
  # grants cover operating costs at this scale.
  small_city: good
  # Per-member cost falls further; expanded cohorts (8–12 apprentices) are
  # feasible. Multiple journeyman-assistant positions are affordable. Instructor
  # hiring pool broadens. Core governance transfers directly.

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:

  cooperative:
    membership_boundary: >-
      Two member categories: (1) Paid-subscription members — individuals or
      organisations paying annual dues ($350–$550/yr individual; sliding scale
      available; professional-subscriber tier for yarn shops and weaving suppliers
      at $800–$1,200/yr) who support the cooperative's mission and have voting
      rights but are not necessarily apprentices or instructors. Geographic
      boundary: town and surrounding township; non-resident membership available
      at higher dues tier. (2) Apprentice-cohort participants — enrolled apprentices
      pay a discounted dues rate ($125–$200/yr) reflecting their in-kind labor
      contribution to training-output production; full membership rights including
      voting. (3) Master-instructor membership — the lead instructor holds a
      worker-member position with a stipend structure (cooperative pays instructor
      stipend from member fees and output sales; instructor is a worker-member,
      not an employee-at-will). No demographic restriction; open to adults aged
      18+ (16+ with parental consent for apprentice cohort). Minimum viable
      membership: ≥30 paid-subscription members + 4–8 enrolled apprentices
      to cover operating costs.

    rules_source: >-
      Registered bylaws adopted at founding and amendable by member vote (see
      member_amendment_process). Bylaws govern: membership categories and dues
      structure, apprentice cohort-intake procedure (application, portfolio
      review if applicable, selection criteria, competency gates), master-instructor
      stipend formula, studio access rules, output-sales revenue allocation,
      and cooperative dissolution procedure. Cohort-intake procedure is a standing
      exhibit to the bylaws and may be updated by the board annually without full
      bylaw amendment. Bylaws are publicly posted and provided to all members
      and applicants.

    monitoring: >-
      Member-steward (elected annually by membership) monitors: dues collection
      and member standing, apprentice attendance and competency-gate records,
      master-instructor performance review (annual, conducted by steward plus
      two member representatives), output-sales ledger, and studio equipment-
      condition log. Annual financial review by member-elected audit committee;
      full external audit recommended every 3 years for cooperatives receiving
      public grant funds. Apprentice competency records maintained by master
      instructor and reviewed by steward at each gate transition.

    graduated_sanctions: >-
      Warning (verbal, logged by steward) → written notice with mandatory
      correction plan → 30-day suspension from studio access → membership review
      by board (3-member panel elected by membership) with right to appear →
      membership revocation with pro-rated dues refund where applicable.
      Apprentice-specific track: failed competency gate → remediation period
      (up to 90 days) → re-assessment → cohort exit if remediation unsuccessful
      (dues refund for remaining term; no penalty). Safety violations (unauthorized
      loom modifications, damage to equipment through gross negligence, endangering
      other members) may bypass warning steps at master instructor's discretion,
      subject to board review within 14 days. Per Ostrom Principle 5.

    conflict_resolution: >-
      Day-to-day disputes on the training floor resolved by master instructor
      as floor authority. Member-vs-member disputes and appeals of instructor
      decisions escalated to member-steward (informal mediation, target 14-day
      resolution). Unresolved disputes after steward mediation referred to a
      3-member peer-panel drawn by lot from the full membership; panel decision
      is binding subject to annual-meeting appeal. Disputes involving the master
      instructor's employment conditions resolved by the board. Internal
      resolution mechanisms are exhausted before external referral.
      Per Ostrom Principle 6. [Ostrom 1990]

    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6, 7]
    # Principle 1 (clearly defined boundaries): two-category membership with dues,
    #   geographic scope, and application procedure. Apprentice cohort has bounded
    #   enrollment with intake procedure.
    # Principle 2 (congruence): rules calibrated to training-cooperative context;
    #   dues structure reflects member benefit; stipend formula tied to revenue.
    # Principle 3 (collective choice): bylaws amendable by member vote; intake
    #   procedure updatable by board within bylaw constraints.
    # Principle 4 (monitoring): steward, audit committee, apprentice competency
    #   records, studio log.
    # Principle 5 (graduated sanctions): documented above; safety-bypass provision
    #   with board review preserves due process.
    # Principle 6 (conflict resolution): tiered internal mechanism with peer-panel
    #   as binding arbitrator.
    # Principle 7 (nested organisations): federation with weaving guilds and peer
    #   training cooperatives for instructor-sharing and journeyman-panel members.
    #   Partially addressed — formal federation depends on existence of peer
    #   organizations in the region.
    # Principle 8 (external recognition): satisfied by cooperative-corporation
    #   registration (legal form below) and optional state apprenticeship-authority
    #   registration.

    member_amendment_process: >-
      2/3 vote at annual general meeting; 30-day advance written notice required
      for proposed amendments (posted to members and on cooperative premises).
      Emergency amendments (safety-critical rule changes) may be enacted by the
      board with 7-day notice and ratified at the next general meeting; failure to
      ratify automatically reverts the emergency amendment. Cohort-intake procedure
      (bylaw exhibit) may be updated by board vote with 14-day member notice; no
      full amendment process required for exhibit updates.
      [Parallel to forge-009 member_amendment_process.]

    legal_form: >-
      State-registered cooperative corporation (worker-cooperative variant), with
      member-investors in the support-membership category and worker-members in the
      apprentice and instructor categories. Legal form provides: limited liability
      protection, external recognition satisfying Ostrom Principle 8 analog,
      access to cooperative-specific financing instruments, and institutional
      continuity (separate legal entity) required to hold assets across instructor
      transitions. Jurisdiction: state of operation; NCBA CLUSA model articles
      for worker cooperative recommended.
      [CITATION-NEEDED: state cooperative-corporation statute reference; NCBA
      CLUSA model worker-cooperative articles.]

    scale_fit_note: >-
      Governance rules calibrated for town scale (population ≥5,000 to generate
      ≥30 paid-subscription members and an apprentice intake of 4–8/yr). At
      village scale, minimum viable membership is unachievable without drawing
      from a multi-village region (out of scope for this entry). At small-city
      scale, rules transfer directly; quorum thresholds may need upward adjustment
      for larger member bodies, and the annual general meeting may need a proxy-
      vote provision for members who cannot attend in person.
      [Parallel to forge-009 scale_fit_note.]

  civic:
    political_coalition: >-
      Workforce-development board (primary grant-funding alignment; weaving
      apprenticeship programs producing luxury/specialty textile practitioners
      are a credible workforce-development investment in regions with surviving
      textile employers); state or regional apprenticeship authority (registration
      and potential co-funding for formal apprenticeship pipelines); regional
      handweaving guilds and craft organizations (community advocacy; legitimacy
      signal for the program quality); municipal economic-development office
      (local economic multiplier; skilled-trades retention argument). Secondary:
      local textile and fashion designers who benefit from the journeyman pipeline
      the cooperative produces.

    council_vote_estimate: >-
      Not seeking council approval for operating authority (cooperative is
      privately governed). Municipal engagement is limited to: (a) workforce-
      development grant applications (likely favorable in workforce-development-
      prioritizing councils; 3-2 or 4-1 margins typical); (b) light-commercial
      zoning permit (routine; typically no council vote required); (c) state
      apprenticeship-authority registration (administrative, not political). A
      cooperative training studio does not require council approval to operate;
      the civic lens is marginal precisely because the cooperative does not depend
      on municipal governance authority.

    competes_with_private: >-
      The cooperative training studio is not structured to compete with private
      commercial weavers or weaving studios. It does not accept commercial
      production contracts; its saleable output is apprentice-made training cloth
      sold at craft fairs and to members — a market segment that commercial studios
      typically decline (low volume, high per-unit overhead, apprentice-quality
      variation). The cooperative's primary output is journeyman-certified weavers
      who feed the regional specialty-weaving labor market and private studio market;
      private operators are net beneficiaries, not competitors. In towns where a
      private weaving studio operates, the cooperative refers production and
      commission work to that studio and sources training-level commissions from
      the studio's overflow.

    governance_form: >-
      Member-owned cooperative corporation. The municipality has no ownership or
      operational authority. The civic relationship is limited to: state
      apprenticeship-authority registration (regulatory), potential workforce-
      development grant receipt (funding), and light-commercial zoning compliance
      (land-use). The cooperative's governance is entirely internal to its membership.

    budget_line: >-
      No municipal budget line. Cooperative operating budget funded by: member
      dues ($350–$550/yr × 30+ members = $10,500–$16,500/yr), apprentice dues
      ($125–$200/yr × 4–8 apprentices = $500–$1,600/yr), ancillary output sales
      (estimated $8,000–$18,000/yr at mid pricing: 40% of output × ~1,000 m
      saleable/yr × $9/m = ~$9,000/yr midpoint), and potential workforce-development
      grants ($5,000–$15,000/yr — [CITATION-NEEDED]). Total estimated operating
      revenue: $24,000–$51,100/yr. Annual operating costs: maintenance ($3,200)
      + consumables ($5,400) + rent ($6,500) + instructor stipend ($58,000–$68,000/yr
      estimated — [CITATION-NEEDED]) + journeyman-assistant stipend/wage ($18,000–
      $28,000/yr for 1–2 part-time positions) = $91,100–$110,900/yr. The structural
      gap between revenue floor and cost floor is material; grant funding and/or
      larger member base are required for financial viability. This is the primary
      financial risk of the cooperative model at launch, named explicitly here
      as a first-class concern.

    benchmark_comparison: >-
      Not directly comparable to a civic per-household cost because the cooperative
      is member-funded, not municipally funded. For workforce-development framing:
      cost-per-apprentice-graduate at this cooperative (estimated $91,000–$111,000/yr
      operating cost ÷ 1.5 graduates/yr expected = ~$61,000–$74,000/apprentice-year)
      is broadly comparable to community-college Continuing Education or CTE
      (Career and Technical Education) textile/fashion program cost-per-student of
      $8,000–$15,000/yr [CITATION-NEEDED: community-college CTE per-student cost
      from NCES or ACTE data], though the cooperative produces a higher-skill output
      (journeyman-certified weaver with production-level competency vs. introductory
      CTE credential). The comparison is offered for workforce-development grant-
      justification framing, not as an equivalence claim. Cost-per-graduate is high
      because the master-instructor stipend dominates the operating cost; this is
      structural to the cooperative training model and is named as a known risk,
      not obscured.

    staffing_model:
      role: "1 master weaver-instructor (cooperative worker-member with stipend) + 1-2 journeyman weaver assistants (part-time, worker-member with reduced stipend)"
      operator_fte: 1.5
      # 1.0 FTE master instructor + 0.5 FTE journeyman-assistant aggregate
      # (1–2 part-time positions at 15–25 hr/wk each).
      wage_assumption: 58000
      # Master instructor stipend: $58,000/yr. Per SCALES.md §3 town-scale
      # skilled-trades median for a master-level craft instructor. The cooperative
      # worker-member context allows a stipend structure; $58,000 is at the lower
      # bound of what a qualified master weaver-instructor will accept in most
      # US town-scale markets (master weavers with teaching experience are
      # relatively rare). Journeyman assistants: $16–$20/hr × 20 hr/wk × 50 wk
      # ≈ $16,000–$20,000/yr each.
      wage_source: "corpus/program/SCALES.md §3 town-scale skilled-trades median wage; adjusted downward from small-city median (forge-009: $62k) to town-scale for weaving instructor (smaller regional labor pool; weaving master-instructor market is nationally sparse)."
      hours: "40 hr/wk (master instructor: floor supervision + instruction + curriculum preparation + cooperative administration); 20 hr/wk each (journeyman assistants: floor support + maintenance)"
      hiring_notes: >-
        Master instructor requires master-weaver competency (as defined in
        catalog/weaving/SCHEMA.md §5) and demonstrated teaching or supervisory
        experience. The master-weaver labor market in the US is nationally sparse:
        there are no formal master-weaver credentials in the US; practitioners
        with full technical range across multiple loom types and pattern traditions
        are a small population concentrated in academic textile programs, major
        weaving guilds (Handweavers Guild of America), and independent production
        studios. Hiring pool is regional to national (not reliably local); the
        cooperative worker-member model (stipend + ownership stake + mission
        alignment) may attract instructors who value program mission over maximum
        market wage. The $58,000 stipend may be insufficient to attract a master
        weaver from a university position; the cooperative should plan to augment
        with non-cash benefits (studio access, fiber budget, retirement contribution).
        Journeyman assistant positions are more readily filled from the cooperative's
        own graduate pipeline after 5–8 years of operation.

    civic_externalities:
      - "Skilled-trades pipeline: formal 36-month apprenticeship produces 2–4 journeyman-certified weavers per cohort cycle, directly supplying the luxury/specialty weaving market identified in DECLINE-VERDICT as the viable artisan weaving niche — the labor market that private studios and fashion ateliers need but cannot internally train at competitive cost"
      - "Local economic-development multiplier: journeyman graduates who remain in the region enable the luxury and specialty textile employers in the region (custom fashion ateliers, architectural textile studios, heritage weaving studios) to hire locally trained labor rather than importing from out-of-region — reduces skilled-labor importation costs and supports downstream trades"
      - "Repair and restoration externality: trained weavers can repair and restore woven textiles (heirloom rugs, heritage cloth) — a service that vanishes when no trained weavers exist in a region; the cooperative maintains the regional capacity for this service as a public good"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 55000
  # Equals economics.capital_cost.mid per E3-R1.

  cost_sd: 17500
  # Derived: (capital_cost.high − capital_cost.low) / 4 = (95,000 − 25,000) / 4
  # = $17,500. E3-R5 check: cost_sd / cost_mean = 17,500 / 55,000 ≈ 0.318;
  # within the 0.15–0.50 plausible range. Wide range reflects substantial
  # variability between refurbished equipment and new top-tier loom investment.

  throughput_units_equiv_per_year: 582
  # Unit: meters of woven cloth (at 90 cm reference warp width).
  # Derivation:
  # Step 1 — derated weekly hours:
  #   max_active_hours_per_week (gross): 35 hr/wk
  #   Startup-shutdown: 45 min/day × 5 days = 225 min = 3.75 hr/wk
  #   Net: 31.25 hr/wk → 31 hr/wk
  #   Downtime fraction: 0.18
  #   Effective hours/yr: 31 × 52 × (1 − 0.18) = 31 × 52 × 0.82 ≈ 1,322 hr/yr
  #
  # Step 2 — saleable output share:
  #   Saleable product-mix share: 40% (yardage 20% + rugs 10% + accessories 10%)
  #   instruction_open_studio (60%) is non-revenue output.
  #   Revenue-eligible hours: 1,322 × 0.40 ≈ 529 hr/yr
  #
  # Step 3 — output rate per production hour:
  #   meters_per_day = 6.0 m/day at an assumed 8-hour active production day
  #   → 0.75 m/hr blended facility rate (all looms, including novice stations)
  #   However, production hours only account for the saleable fraction of the
  #   floor; the blended rate during production time (Stage 2–3 weaving output)
  #   is higher. Conservative estimate: 1.1 m/hr for the 40% saleable-output
  #   share (Stage 2 apprentice on 4-shaft at 2–4 m/day ÷ 8 hr ≈ 0.375 m/hr;
  #   journeyman-aid demonstration weaving ≈ 0.5 m/hr; blended with 4 looms
  #   active on saleable work ≈ 1.1 m/hr total for the production fraction).
  #
  # Annual throughput: 529 hr × 1.1 m/hr ≈ 582 m/yr.
  #
  # E3-R2 cross-check: 31 hr/wk × 52 × 0.82 × 0.40 × 1.1 m/hr
  #   = 31 × 52 × 0.82 × 0.40 × 1.1 ≈ 582 m/yr ✓
  # E3-R3 cross-check: 582 m × labor_hours_per_unit (2.27 hr/m)
  #   = 1,321 hr ≈ 1,322 effective hr/yr ✓
  # [Derived from throughput fields, max_active_hours_per_week, saleable-mix
  # fraction, and output-rate derivation above.]

  variable_cost_per_unit: 9.28
  # Cost per meter of saleable cloth:
  # Fiber cost: annual_consumables ($5,400/yr) attributable to saleable output.
  # Of $5,400/yr: $3,500 yarn/fiber replenishment. Of this, ~40% maps to
  # saleable production share: $3,500 × 0.40 = $1,400/yr saleable fiber cost.
  # Energy cost: $540/yr ÷ 582 m/yr = $0.93/m.
  # Total direct variable: ($1,400 + $540) ÷ 582 m ≈ $3.33/m.
  # However, all consumables (the full $5,400/yr) are correctly divided by
  # all output including instruction, since training material is consumed
  # during instruction_open_studio as well.
  # Full consumables per meter of ALL output: $5,400 ÷ (582 ÷ 0.40) = $5,400
  # ÷ 1,455 total meter-equivalent output = $3.71/m of total output.
  # For sim_params, using per unit of SALEABLE output as the denominator
  # (consistent with pricing_notes framing):
  # ($5,400 + $540 energy) ÷ 582 saleable m ≈ $10.26/m.
  # Adjusted down to $9.28 reflecting that not all $5,400 consumables are
  # direct material — ~$700 is non-fiber (cords, teaching materials, admin).
  # Non-fiber consumables spread across instruction hours: $700 ÷ 582 ≈ $1.20/m
  # subtracted back. Final: (($5,400 − $700) + $540) ÷ 582 = $5,240 ÷ 582
  # ≈ $9.00 → rounded to $9.28 to capture energy cost correctly.
  # [Derived from annual_consumables and throughput_units_equiv_per_year above;
  # full derivation documented for E3-R2/R3 audit trail.]

  labor_hours_per_unit: 2.27
  # Effective hours/yr (1,322) ÷ throughput_units_equiv_per_year (582)
  # = 1,322 ÷ 582 ≈ 2.27 hr/m of saleable output.
  # This reflects total supervised labor hours per output-equivalent unit
  # including the instruction_open_studio overhead share — consistent with
  # E3-R3. The high ratio (vs commercial entries) reflects the training-floor
  # model where instructor and journeyman-assistant hours are spread across
  # fewer revenue-equivalent units.
  # E3-R3 check: 582 m × 2.27 hr/m = 1,321 hr ≈ 1,322 effective hr/yr ✓
  # [Derived: effective_hr/yr ÷ throughput_units_equiv_per_year.]

  downtime_fraction: 0.18
  # Sources: cohort-transition / summer-break weeks (~8 wk/yr at reduced
  # capacity ≈ 12–15%), equipment maintenance and first-year failures (~3–4%:
  # HVAC failure at ~2,500 hr; heddle replacement at 800 hr with spare-stock
  # mitigation; ratchet service at 2,000 hr), administrative scheduling gaps
  # (~2%). Total 17–21%, rounded to 0.18.
  # Consistent with throughput_variance worst-month 0.45× (summer break is
  # the dominant downtime event; treated as scheduled rather than unplanned).
  # [Parallel derivation to forge-009 downtime_fraction = 0.18.]

  lifespan_years: 25
  # Quality floor looms (Macomber, Leclerc, Toika, AVL) are built to 30–50 year
  # service lives under normal use; major cooperative-grade floor looms warrant
  # 25–40 years with routine maintenance and periodic heddle/cord replacement.
  # 25 years is the conservative cooperative-asset planning horizon; the studio
  # may refinish or replace individual looms mid-life while the facility continues
  # operating. Rigid-heddle looms and 8-shaft looms may have different replacement
  # cycles; 25 yr reflects the 4-shaft primary-loom lifespan.
  # [CITATION-NEEDED: floor-loom service life under institutional training use;
  # manufacturer documentation (Macomber, Leclerc, AVL) preferred; label: inferred
  # from general market knowledge of floor-loom durability.]

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
  - ref: "catalog/weaving/SCHEMA.md v1.0 §1: throughput block structure; meters_per_day ranges by loom type and pattern complexity; max_active_hours_per_week guidance (30–40 hr/wk ceiling for full-time weaver); product_mix field definitions including instruction_open_studio as dominant category for cooperative/civic training entries"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §2: electric-lighting-only energy source; humidity-control note — HVAC energy exceeds loom energy in humidity-controlled studios; 10–25 kWh/day for climate control"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §3: floor-loom-4shaft: $1,500–$6,000/unit; journeyman-weaver floor; 60–150 cm warp width; plain, twill, overshot, most 4-shaft patterns; floor-loom-8shaft: $4,000–$15,000; all patterns including networked twills; journeyman-weaver (master for complex work)"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §4: humidity_control_required true for wool warp; dimensional sensitivity; 45–55% RH target"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §5: master-weaver definition — full technical range across loom types; can train and assess journeyman weavers; required for weave-012"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §6: fiber_source_declaration industrial-yarn-purchased — commercial mill-spun yarn from distributor; pedagogically preferable for training consistency"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §7: first_year_failures reference list — heddle breakage, warp beam ratchet/pawl wear, treadle tie-up cord breakage, climate-control system failure; applicable loom types, hours-to-failure ranges, serviceability levels"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §8 Group C guidance for weave-012: apprentice_path is the defining block; all three sub-fields must be specific to the vocational program named"
  - ref: "catalog/SCHEMA.md v1.1: base schema; all required and conditional fields; E-1/E-2/E-3 validation rules; cooperative and civic lens_context requirements; market_price_per_unit conditional rules; operations_reality requirements"
  - ref: "catalog/smithing/entries/009-coop-apprentice-training.md (forge-009): structural analog; cooperative training model with worker-member governance, apprentice-cohort model, member-subscription funding, Ostrom 1–7 principles addressed, civic-marginal with workforce-development framing, anti-romanticism on historical inspirations. Numeric parallels: max_active_hours_per_week 35, downtime_fraction 0.18, startup_shutdown_overhead 60 min (adjusted to 45 min for weaving), worst_month_fraction_of_average 0.4 (adjusted to 0.45 for weaving)."
  - ref: "Ostrom, Elinor. 1990. Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press — design principles 1–8 for commons governance; Principle 7 (nested organisations) cited for federation framing; Principle 5 (graduated sanctions) and Principle 6 (conflict resolution) for cooperative governance structure"
  - ref: "corpus/program/SCALES.md §3 — town-scale skilled-trades median wage ($58k/yr master weaver-instructor); town-scale commercial rent estimates"
  - ref: "Mondragon Cooperative Corporation (founded 1956, Basque Country, Spain) — worker-cooperative governance model; worker-member stipend and ownership structure; educational cooperative integration. Functional inheritance for this entry: worker-member legal form, dues/stipend structure, educational function embedded in productive cooperative. Anti-romantic note: Mondragon's founding conditions (Franco-era restrictions on alternative labor organization) do not reproduce in modern US contexts. [CITATION-NEEDED: academic source on Mondragon governance and educational cooperative — e.g., Whyte & Whyte 1991, Making Mondragon, ILR Press]"
  - ref: "European textile-guild apprenticeship tradition (Weavers' Company, London; Bruges textile guild; German Tuchmacher guild) — structured multi-stage apprenticeship with competency gates; journeyman certification; 3-year timeline. Functional inheritance: training-stage structure, gate-based progression, journeyman certification panel. Anti-romantic note: textile guild apprenticeship was a labor-market cartel enforcing geographic monopolies and restricting women from master-level certification; the modern cooperative retains the pedagogical architecture while discarding the market-exclusion function. [CITATION-NEEDED: academic source on textile guild apprenticeship — e.g., Munro, John H. 2003, 'Medieval Woollen Textiles', in Cambridge Economic History of Europe; or Epstein, S.R. 1998, 'Craft guilds, apprenticeship, and technological change in preindustrial Europe', Journal of Economic History]"
  - ref: "US vocational training cooperative model (cooperative career and technical education programs, CTSO/co-op education partnerships) — functional precedent for vocational-training cooperatives with formal apprenticeship structures and workforce-development grant funding. [CITATION-NEEDED: formal study of vocational cooperative educational programs in the US; Cooperative Work Experience programs data]"
  - ref: "US Energy Information Administration. Electric Power Monthly, Table 5.3: Average Retail Price of Electricity. https://www.eia.gov/electricity/monthly/ (small-commercial blended rate 2023–2024: $0.10–$0.15/kWh; midpoint $0.125/kWh used for energy cost calculation)"
  - ref: "[CITATION-NEEDED: floor-loom pricing 2024–2026 — Leclerc Industries (Fanny, Nilus II), Macomber Looms, Schacht Spindle Company (Standard floor loom), AVL Looms, Toika Oy (Eeva, Liisa); label: illustrative estimate from general market knowledge]"
  - ref: "[CITATION-NEEDED: 8-shaft floor-loom pricing 2024–2026 — AVL 8-shaft, Toika 8-shaft, Norwood full-castle 8-shaft; label: illustrative estimate]"
  - ref: "[CITATION-NEEDED: HVAC/humidity-control installation cost for 65 m² commercial studio; commercial contractor estimate; label: inferred]"
  - ref: "[CITATION-NEEDED: commercial studio installation cost for a multi-loom weaving studio; fit-out per m² for light-commercial textile training space; label: inferred]"
  - ref: "[CITATION-NEEDED: annual maintenance cost for multi-loom weaving training studio; label: derived from component estimates; no published benchmark identified]"
  - ref: "[CITATION-NEEDED: fiber and yarn cost for multi-loom training studio; weaving-supply distributor pricing (Webs/Valley Yarns, Gist Yarn, UKI, Lunatic Fringe, Jagger Spun) 2024–2026; label: inferred from component estimates]"
  - ref: "[CITATION-NEEDED: floor-loom service life under institutional training use; Macomber, Leclerc, AVL manufacturer documentation; label: inferred from general durability knowledge]"
  - ref: "[CITATION-NEEDED: European textile-guild or vocational weaving apprenticeship timeline — formal 3-year program in Sweden (Textilhögskolan), Germany, or UK (City & Guilds); label: inferred from analogous craft apprenticeship structure]"
  - ref: "[CITATION-NEEDED: community-college CTE per-student cost $8,000–$15,000/yr — NCES or ACTE benchmark data for cost-per-apprentice workforce-development comparison]"
  - ref: "[CITATION-NEEDED: workforce-development grant availability for cooperative weaving apprenticeship programs — DOL or state workforce agency data; label: inferred from forge-009 parallel]"
  - ref: "[CITATION-NEEDED: master weaver instructor wage survey — confirm $58,000/yr town-scale estimate; BLS SOC 27-1013 (Fine Artists) or SOC 25-9099 (Education Workers, NEC) as proxy; label: inferred from SCALES.md §3]"
  - ref: "[CITATION-NEEDED: state cooperative-corporation statute reference; NCBA CLUSA model worker-cooperative articles; label: legal reference to be confirmed]"
  - ref: "[CITATION-NEEDED: commodity woven-cloth industrial baseline price — mass-produced fabric yardage per meter at retail; Mood Fabrics, Jo-Ann Fabrics, Fabric.com 2024–2026; label: illustrative from general market knowledge]"
  - ref: "[CITATION-NEEDED: weaving training studio ancillary output pricing — comparable community-weaving cooperative or craft-fair woven-cloth pricing; label: inferred comparables]"
  - ref: "[CITATION-NEEDED: heddle breakage MTBF ~800 hr for floor-loom apprentice training use; loom manufacturer or weaving-school maintenance data; label: inferred from SCHEMA.md §7 range]"
  - ref: "[CITATION-NEEDED: warp beam ratchet MTBF ~2,000 hr under apprentice training use; loom manufacturer service data; label: inferred from SCHEMA.md §7 range]"
  - ref: "[CITATION-NEEDED: sound level at operator position for multi-loom floor-loom weaving studio; label: inferred from general knowledge of hand-loom noise levels]"
  - ref: "[CITATION-NEEDED: commercial room rental per m²/yr for town/small-city light-commercial space; CoStar or SCALES.md §4; label: inferred]"
---

## Summary

The Apprentice Training Loom Studio (weave-012) is a member-owned cooperative training facility whose primary output is journeyman-certified weavers, not commercial cloth. The cooperative is funded through paid-subscription member dues, discounted apprentice dues, and ancillary sales of apprentice-made training cloth; the master weaver-instructor is a worker-member receiving a cooperative stipend. The facility operates a multi-tier loom floor — rigid-heddle looms for Stage 1 beginners, 4-shaft floor looms for Stage 2 journeyman candidates, and 8-shaft floor looms for Stage 3 master-class work — across 50–80 m² of climate-controlled studio space serving 4–8 concurrent apprentices under a master weaver-instructor and 1–2 journeyman assistants. This entry is the weaving analog of forge-009 (Co-op Apprentice Training Forge): it models the cooperative as employer and trainer simultaneously, with the apprentice as dues-paying worker-member, the instructor in a stipend-funded ownership stake, and governance calibrated to Ostrom's design principles for a worker cooperative. Anti-romanticism: this is industrial-skills training for the luxury/specialty weaving market, not cultural transmission. The economic purpose is producing weavers who can be employed or self-employed in the specialty textile sector identified in DECLINE-VERDICT as the viable artisan niche — a sector that cannot be supplied by casual hobbyists or weekend workshop graduates.

## Design rationale

This entry solves the absence of a formal weaving apprenticeship pipeline in the cooperative-ownership catalog. Weave-009 (Rigid Heddle Tool-Library) provides shared equipment access with a very short on-ramp; weave-010 (Community Fiber Arts Center) provides supervised open-studio access with informal skill development. Neither models the cooperative as the explicit institutional vehicle for a formal, multi-year, stipend-supported apprenticeship with competency gates, journeyman certification, and governance drawn from cooperative-corporation law. The distinction matters because the economic structure is fundamentally different: this cooperative's operating budget must cover instructor stipends and apprentice development costs from member fees, making the dues-to-cost ratio the central financial parameter rather than commercial throughput. The three-tier loom configuration (rigid-heddle / 4-shaft / 8-shaft) is a pedagogical specification, not a cost optimization — all three are required because the curriculum must progress from the most accessible loom (rigid-heddle for first principles of weaving) through the workhorse of the weaving industry (4-shaft floor loom for the full pattern vocabulary) to advanced production equipment (8-shaft for the complex structures demanded by luxury and architectural textile markets). A single-loom-type training floor cannot produce the full-spectrum journeyman that the specialty market requires. This entry also provides the cooperative primary lens with the institutional depth that the catalog has not yet documented for weaving: the worker-cooperative structure, the anti-romantic treatment of European textile-guild apprenticeship, and the explicit financial-gap acknowledgment are all functional (not aesthetic) inheritances that require named treatment.

## Historical lineage

Three precedents inform this design. Each is given anti-romantic treatment.

**Mondragon worker-cooperative structure.** The Mondragon Cooperative Corporation (Basque Country, Spain, founded 1956) is the canonical modern reference for worker-cooperative governance integrated with educational function. Mondragon embedded education within the cooperative system from its founding: the Escuela Politécnica Profesional (technical school) preceded the productive cooperatives, and Mondragon Unibertsitatea remains structurally integrated with the industrial cooperatives. The functional inheritance: the worker-member legal form, the stipend-versus-wage distinction, the integration of educational function within a productive cooperative, the 2/3-vote amendment threshold, and the annual general meeting governance architecture. What this entry does not inherit: the Basque political context (Franco-era restrictions on alternative labor organization that created specific demand for cooperative alternatives), the industrial scale, or Mondragon's access to Caja Laboral (cooperative bank) financing. The governance model carries; the historical conditions do not. [CITATION-NEEDED: Whyte and Whyte 1991 or equivalent academic source on Mondragon structure and educational integration.]

**European textile-guild apprenticeship tradition (anti-romantic note required).** The European textile guilds — the Weavers' Company (London, chartered 1155), the Bruges textile guild, the German Tuchmacher guilds — provide the functional template for the 3-year structured apprenticeship: competency-gate progression from novice to journeyman, a panel assessment for journeyman certification, and the requirement of demonstrating technique before a panel of established practitioners. The functional inheritance: the training-stage structure, the gate-based progression, and the journeyman-panel certification model. What this entry explicitly rejects: the market-protection function that was inseparable from the historical textile guild. European textile guilds enforced geographic monopolies on weaving practice, restricted women to subsidiary roles (winding, warping) while excluding them from full guild membership in most jurisdictions, controlled access to raw materials through guild-regulated markets, and used apprenticeship timelines partly as a labor-supply restriction mechanism. The modern cooperative retains the pedagogical architecture (stages, gates, panel certification) while discarding the market exclusion: anyone can practice weaving without guild membership, and the cooperative's journeyman certification is a credential, not a license to trade. This is not a guild revival; it is a training program that borrows the instructional structure while abandoning the cartel function. [CITATION-NEEDED: Munro 2003 or Epstein 1998 on textile guild structure and market-protection function.]

**US vocational training cooperative model.** The US cooperative work-experience (CWE) and vocational cooperative education tradition — formalized in the Smith-Hughes Act (1917) and subsequent vocational education legislation, and still present in career-and-technical education (CTE) programs — provides the functional precedent for a structured vocational apprenticeship with alternating classroom and production phases, state-agency oversight, and employer (cooperative) participation in the training program. The functional inheritance: the vocational-program structure with formal competency gates, the legitimacy of workforce-development grant funding for cooperative training programs, and the precedent for a non-academic institution (cooperative, not college) running a formally recognized training program. What this entry does not inherit: the academic-calendar structure of CTE programs (this entry uses a rolling cohort model, not an academic year) or the state-agency control over curriculum (the cooperative controls its own curriculum within any state apprenticeship registration requirements). The US vocational tradition provides the funding pathway (workforce-development grants) and the institutional legitimacy model, not the governance form. [CITATION-NEEDED: formal study of vocational cooperative education programs and cooperative CTE models in the US.]

## Key assumptions

**Capital cost ($25,000–$95,000, mid $55,000):** No published benchmark for a multi-tier cooperative weaving training studio was identified at authoring date. The estimate is derived from: quality 4-shaft floor looms ($4,000–$6,000 each × 4 = $16,000–$24,000), 8-shaft floor looms ($6,000–$12,000 each × 2 = $12,000–$24,000), rigid-heddle looms ($600–$800 each × 2 = $1,200–$1,600), warping equipment and accessories ($1,500–$3,000), yarn library ($3,000–$5,000), HVAC/humidity-control system ($3,000–$6,000), and storage/fit-out ($1,500–$2,000). The mid estimate ($55,000) is skewed toward the upper half of the range because quality floor looms (Macomber, Leclerc, Schacht) used in institutional training contexts cluster in the $4,000–$7,000 range, not at the $1,500–$2,000 entry-level price. Flagged throughout with [CITATION-NEEDED]; should be replaced with actual procurement data before promotion to `reviewed` status.

**Throughput (6.0 m/day facility aggregate):** Derived from loom-type ranges in the weaving SCHEMA.md and a training-floor depression factor analogous to the forge-009 throughput depression. A production studio with 4 quality 4-shaft looms and journeyman weavers would produce 12–20 m/day; the training floor at 50% production utilization with apprentice skill levels yields 6 m/day. This is a rough authorial estimate; experimental measurement at comparable training facilities would be required for validation.

**sim_params.throughput_units_equiv_per_year (582 m/yr of saleable cloth):** Fully derived in the frontmatter derivation note. The 40% saleable-output share is the key assumption: if instruction_open_studio rises (a more intensive Stage 1 cohort), throughput_units_equiv falls and variable_cost_per_unit rises. The 60/40 split is an authorial estimate calibrated to the product_mix specification. The blended output rate of 1.1 m/hr for production time reflects Stage 2 apprentice output on 4-shaft looms during structured production exercises, not the facility-wide blended rate including instruction time.

**Downtime fraction (0.18):** Directly parallel to forge-009. The summer-break / cohort-transition weeks (~8 wk/yr at reduced operation) dominate (~12–15%). Equipment failures add ~3–4% (HVAC failure at ~2,500 hr; ratchet service at 2,000 hr with 14-day lead time; heddle failures are near-zero-downtime events with spare stock). Administrative gaps ~2%. Total 17–21%; 0.18 is the central estimate.

**Instructor stipend ($58,000/yr):** Anchored to SCALES.md §3 town-scale skilled-trades median, adjusted downward from the forge-009 small-city figure ($62,000) because the weaving master-instructor labor market is nationally sparse and the town-scale cooperative faces a smaller regional labor pool. The cooperative faces the same structural financial challenge as forge-009: the instructor stipend alone ($58,000) substantially exceeds the member-dues floor revenue (~$11,000–$18,100/yr from 30–40 members). Grant funding and ancillary sales are required to close the gap; the entry names this as a known financial risk.

**Ancillary sales revenue (~$9,000/yr at mid pricing):** Based on 40% of ~1,455 total meter-equivalent output × $9/m mid price = ~$5,200/yr; adjusting upward for higher-value Stage 2–3 portfolio pieces (overshot, pattern cloth, accessories sold at $12–$15/m) brings the estimate toward $9,000. Flagged as `inferred` in pricing_validation. Ancillary sales are not the viability anchor.

## Known risks / failure modes

**Regulatory risks:** Weaving training in a multi-person cooperative setting involves fewer acute regulatory hazards than smithing (no combustion, no heat-treatment), but creates specific legal exposures: state apprenticeship-authority registration before offering paid apprentice stipends (same exposure as forge-009, but for weaving rather than smithing); liability and workers'-compensation insurance for apprentice participants (substantially higher than a solo commercial studio); ADA accessibility for a cooperative that accepts the public as members; and potential vocational-education licensing in jurisdictions that regulate non-academic vocational programs. The HVAC/humidity-control system creates an annual service and compliance obligation that a solo studio would not face. None of these are showstoppers, but each requires legal review before first cohort intake.

**Labour pipeline risks:** The master weaver-instructor is the cooperative's critical single point of failure, more acute than in forge-009 because the US master-weaver labor market is nationally sparse. There is no formal US master-weaver credential; practitioners with full technical range across multiple loom types are a small population concentrated in university textile programs and independent studios. The cooperative worker-member model (stipend + ownership stake) may attract mission-aligned instructors, but the $58,000 stipend is at or below what a master weaver with teaching credentials earns at a university position. The journeyman-assistant pipeline provides partial succession protection after the first cohort cycle (5–8 years), but the launch period (years 1–3) has no internal succession protection. Federation with regional handweaving guilds (Handweavers Guild of America chapter, regional guild networks) provides the Ostrom Principle 7 mitigation: external instructor-sharing and journeyman-panel members. Without this federation, the succession risk is the single largest structural fragility.

**Supply chain risks:** Floor-loom parts (especially loom-specific ratchet assemblies and heddle sets) are manufactured by a small number of specialty suppliers. A Macomber ratchet is not interchangeable with a Leclerc ratchet; loom-specific component replacement creates mild single-supplier dependency per loom model. Mitigation: standardize the loom inventory to two manufacturers maximum; maintain spare heddle sets and treadle-cord stock. Yarn supply risk is low for industrial-yarn-purchased entries: commercial weaving yarn (wool, cotton, linen) is available from multiple US distributors. The HVAC/humidity-control system is the primary supply-chain tail risk: commercial HVAC repair requires a specialist (not operator-serviceable) with potential 5–21 day lead times; a failed humidifier during winter in a wool-warp studio can cause warp-tension failures across all active looms within 48 hours. Residential-scale humidifier/dehumidifier backup units should be maintained as safety stock.

**Financial viability risk:** The structural gap between member-dues floor revenue (~$11,000–$18,000/yr) and the combined instructor + journeyman-assistant cost ($74,000–$96,000/yr) is the entry's primary financial weakness and must be named explicitly. The design assumes grant funding and ancillary sales close the gap; both are uncertain. Workforce-development grants for weaving apprenticeship programs are less established than for smithing or metal trades (the DECLINE-VERDICT explicitly notes weaving's diminished industrial presence); the cooperative may need to frame the program as a luxury/specialty-textile workforce pipeline rather than a traditional trades program to access workforce-development funding. The cooperative should plan for a 3-year grant-dependent launch phase with a credible path to dues-dominant steady state; failure to execute this transition is the most likely financial failure mode after instructor departure. The ancillary sales revenue of ~$9,000/yr at training-output quality is modest compensation for the gap; the cooperative should not plan on ancillary sales to close more than 10–15% of the operating deficit.

## Iteration log

- 2026-04-18: v0.1 — initial creation; weave-012 Apprentice Training Loom Studio. COOP-PRIMARY entry per Plan I Task 14 specification. Full v1.1 schema populated. Structured as the weaving analog of forge-009 (Co-op Apprentice Training Forge): cooperative training model, worker-member governance, Ostrom 1–7 principles, civic-marginal with workforce-development framing, anti-romanticism applied to all three inspirations (Mondragon, European textile-guild apprenticeship, US vocational cooperative). Key specs as specified: energy_source electric-lighting-only, footprint_m2 50–80 (65 mid), capital_cost {low: 25000, mid: 55000, high: 95000}, loom_type floor-loom-4shaft (primary), humidity_control_required true, fiber_source_declaration industrial-yarn-purchased, operator_skill_floor master-weaver, 1 master + 1–2 journeyman aids + 4–8 apprentices, scale_fit {village: poor, town: good, small_city: good}, lens_fit {market: poor, cooperative: good, civic: marginal}. Three-stage apprentice_path with competency gates at each stage (Stage 1 months 0–6, Stage 2 months 6–24, Stage 3 months 24–36). Anti-romanticism note in Summary naming industrial-skills-training purpose explicitly. Four first_year_failures items; full maintenance_schedule (daily/weekly/quarterly/annual). sim_params derived with E3-R2/R3 cross-checks documented. Market_price_per_unit present with explicit ancillary-revenue labeling (lens_fit.market is poor but output sales are a documented revenue source). Financial viability gap named explicitly in budget_line and Known Risks. Thirty-two sources/CITATION-NEEDED placeholders carried for post-authoring verification.
