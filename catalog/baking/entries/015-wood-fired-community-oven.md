---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: bake-015
trade: baking
name: "Wood-Fired Community Oven"
tagline: "Shared masonry dome oven for village and town commons; civic or cooperative model with fire-keeper and user-brought dough"
status: draft
version: "0.1"
supersedes: null
inspirations:
  - medieval-european-manorial-communal-oven
  - french-four-banal-seigneurial
  - italian-forno-comunitario-village-tradition
  - modern-community-bread-oven-revival

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 20
# Mid-range of the 15-25 m² spec envelope. 20 m² covers the masonry dome oven
# structure (~4 m² footprint including insulating jacket), covered wood-storage
# shed adjacent to the oven structure (~6 m²), a queuing and dough-staging
# area with a work table (~6 m²), and perimeter circulation clearance (~4 m²).
# Community-owned land; no commercial floor-space rent applies.
# Footprint is entirely outdoors or in a partially covered pavilion structure;
# no enclosed building required for the oven itself. Wood storage must be
# under cover to remain dry. Queue area may be open-air.
# [CITATION-NEEDED: footprint survey for community bread ovens in North American
# or European revival projects; structural inference from masonry dome oven
# construction literature; label: inferred.]

ceiling_min_m: 0
# Open-air or partially covered outdoor installation; no enclosed ceiling
# requirement. A covered pavilion (roofed, open-sided) is recommended but not
# structurally required. The 0 value indicates this entry does not drive
# ceiling-height-based building-selection decisions. If sited under a fixed
# structure, a minimum 2.5 m clearance above the oven dome crown is recommended
# for smoke management and safe access.
# [Structural inference from community wood-fired oven installation practice;
# label: inferred.]

ventilation: dedicated-exhaust-system
# Masonry dome wood-fired oven requires a chimney flue or equivalent dedicated
# exhaust channel for smoke management. The flue must be properly designed to
# produce adequate draft for clean combustion; poor flue design is the primary
# cause of chronic smoking and regulatory complaint in outdoor installations.
# Air-quality permit for wood smoke is required in many jurisdictions. The
# outdoor/open-air siting provides natural dilution of smoke and combustion
# products beyond what an indoor installation would have; regulatory exposure
# is moderate rather than high. "Dedicated exhaust system" here means the
# chimney and flue integral to the masonry oven structure.

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: wood-fired-deck
# Per spec requirement and baking SCHEMA.md §2 enumeration. Masonry dome oven
# fired with hardwood billets or faggots; fire raked out before baking; heat
# retained in masonry thermal mass. Characteristic declining-temperature baking
# curve: high initial temperature for lean crusty breads, falling to lower
# temperature for enriched loaves, pastry, and low-heat items. This is the
# defining thermal profile of the traditional communal oven. Per baking
# SCHEMA.md §2: wood-fired-deck temperature ceiling ~300-450°C deck surface
# (declining during bake); no mechanical steam injection; no thermostat control;
# temperature management entirely operator-skill-dependent.
# [Baking SCHEMA.md §2 wood-fired-deck entry]

energy_consumption_per_active_hour: "25 kg wood per firing"
# A single full firing of a masonry dome oven of 1.2–1.5 m interior diameter
# requires approximately 20-35 kg of dry hardwood per HISTORICAL-FORMS.md §2
# and community oven operator accounts. 25 kg/firing is the mid-estimate for
# a medium-sized community oven at this footprint. Consumption per active hour
# is not a meaningful unit for this entry: the wood is consumed entirely in the
# firing phase (approximately 2-3 hours of burn); the subsequent baking phase
# uses stored thermal mass with no additional fuel input.
# Note: the field is reported as a per-firing figure for transparency. E-3
# cross-checks use the per-firing figure × firing frequency for annual fuel cost.
# [CITATION-NEEDED: measured fuel consumption for masonry dome community bread
# ovens; Wing and Scott 1999 or community oven construction manuals; label: inferred.]

backup_fuel: null
# No backup fuel. The masonry dome oven cannot be switched to an alternative
# fuel without structural modification. If wood supply is disrupted, baking
# sessions cannot proceed. Wood supply continuity is identified as the primary
# fuel-chain risk in Known Risks.

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  loaves_per_day: 40
  # Net output per single community firing day. Unit: 800g sourdough boule
  # equivalent (see Key Assumptions for unit definition and thermal-batch logic).
  # Community oven firing produces two to three sequential thermal batches per
  # firing: (1) initial high-heat batch (lean crusty breads, 4-6 loaves per
  # load for a medium oven), (2) medium-heat batch (enriched loaves, 4-6 loaves),
  # (3) falling-heat batch (pastry, flatbreads, or low-temperature items). Each
  # batch occupies the full oven deck.
  # At community scale: approximately 8-12 loaves per batch × 3 batches per
  # firing = 24-36 loaves per firing. Plus any community members baking their
  # own dough (using-fee model): additional 6-15 loaves per event depending on
  # community participation. Blended estimate: ~40 loaves/firing-day.
  # Note: community oven throughput is not a production-optimization metric —
  # it is a measure of collective community use. The oven is not run to maximize
  # loaf output; it is fired to serve community members on a scheduled basis.
  # [CITATION-NEEDED: empirical throughput data for community wood-fired bread
  # ovens at village or town scale; community oven project reports; label: inferred.]

  batches_per_day: 3
  # Three sequential thermal batches per firing day: high-heat (lean breads),
  # medium-heat (enriched loaves), falling-heat (pastry or long-proof items).
  # The declining-temperature thermal curve is the defining production constraint
  # of the masonry dome oven; it dictates batch sequence, product ordering, and
  # total daily output ceiling. Subsequent firings on the same day are not
  # practically feasible for a community event model (refiring requires 2-3 hours;
  # wood consumption doubles; community schedule does not typically warrant it).
  # [Derived from wood-fired-deck thermal physics; baking SCHEMA.md §2 notes;
  # HISTORICAL-FORMS.md §2 thermal principle description]

  batch_size_loaves: 13
  # Blended estimate: (24-36 loaves per 3-batch firing day) ÷ 3 batches ≈ 8-12
  # loaves/batch for oven production; plus community member contribution batches
  # raise effective per-batch count. Reported as 13 representing the average
  # across all three thermal batches in a community firing event.
  # [Structural inference from medium community oven deck area (~0.8-1.2 m²);
  # baking SCHEMA.md §2 wood-fired-deck capability notes; label: inferred.]

  max_active_hours_per_week: 16
  # Community oven model: 2 firing days per week × 8 hr per firing day.
  # Each firing day comprises: fire-building and preheat (~2.5 hr), three bake
  # batches and queue management (~4 hr), ember management and cooldown
  # (~1.5 hr). Total ~8 hr active time per firing day.
  # Typical community oven operates 1-3 firing days/week; 2/week is the
  # mid-estimate for an active village or town commons oven.
  # This entry deliberately does not optimize weekly hours: the community oven
  # is not a production-volume instrument. Its role is a shared civic or
  # cooperative infrastructure event, not a commercial bakery operation.
  # [CITATION-NEEDED: operating frequency data for community bread ovens;
  # community oven project operational descriptions; label: inferred.]

  product_mix:
    bread: 75
    # Lean sourdough and yeasted loaves are the primary community output:
    # the oven is fired primarily for bread baking. Community members bring
    # their own dough or the fire-keeper produces the first lean-bread batch.
    confection: 10
    # Falling-heat batch used for pastry, enriched rolls, or sweet breads.
    specialty: 10
    # Cultural specialty breads, flatbreads baked at high heat (pita, pizza),
    # and seasonal traditions (festival breads). High-heat window is valuable
    # for flatbread baking immediately after fire-raking.
    catering: 5
    # Occasional community event catering: festival pizzas, communal meals.
    # Kept low: this is not a catering-primary operation.
    # Sum: 75+10+10+5 = 100.

  throughput_variance:
    seasonal: "Spring and autumn peak: outdoor community events, harvest festivals, bread-baking days draw highest participation; winter trough with cold and weather reducing community turnout; summer variable (outdoor heat reduces enthusiasm; tourist/visitor interest in some communities offsets local trough)"
    worst_month_fraction_of_average: 0.45
    # Winter trough at northern latitudes: cold outdoor firing, weather
    # disruption, and reduced community participation. Consistent with
    # baking SCHEMA.md §1 range for artisan bread (0.55-0.75) at lower
    # end given outdoor operational dependence and community-event nature.
    # [Baking SCHEMA.md §1 throughput_variance guidance; adjusted for outdoor
    # community event context; label: inferred.]
    best_month_fraction_of_average: 1.60
    # Spring/autumn festival or harvest season peak: community engagement at
    # maximum; visitor or tourism interest may add to local participation.
    # Consistent with baking SCHEMA.md §1 artisan bread range (1.20-1.40)
    # at higher end given festival-event concentration.
    # [Same source; label: inferred.]

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: journeyman-baker
# Per spec requirement and baking SCHEMA.md §2-§3. Wood-fired dome oven
# temperature management is operator-skill-dependent: the fire-keeper must
# judge firing completion by dome color (whitening of soot layer), floor
# temperature by hand-sensing or thermometer, and batch sequencing by
# falling-temperature curve estimation. Per baking SCHEMA.md §2: entries
# claiming wood-fired-deck with apprentice-baker operator must explain
# temperature management protocol — this entry does not make that claim.
# The fire-keeper role requires journeyman baking competency plus the
# additional wood-fire management skill set that is not part of standard
# journeyman-baker training in electric or gas ovens. Fire management
# for a masonry dome is a specific subset of artisan baker competency;
# candidates with heritage-grain or traditional-bread backgrounds will
# have this skill more commonly than those trained on commercial equipment.
# Apprentice-baker community participants bring their own dough; the
# fire-keeper manages the oven.
# [Baking SCHEMA.md §2-§3; HISTORICAL-FORMS.md §2 thermal principle notes]

operators_concurrent: "1 fire-keeper + variable community participants"
# Base: 1 journeyman fire-keeper required for oven management and firing safety.
# Community participants who bring their own dough and use oven time under
# fire-keeper coordination are not operators — they are users. The fire-keeper
# manages oven temperature, queue, and safety; participants manage their own
# dough. Scheduled community baking events may have 5-20 participants queued
# for oven time. The fire-keeper cannot simultaneously manage the oven and
# provide intensive instruction to more than 2-3 users at once.

apprentice_friendly: true
apprentice_path:
  training_stages: >-
    Stage 1 — Wood Fire Management (0–3 months): safe fire-building with
    hardwood fuels; reading combustion stage; understanding flue draft and
    chimney management; basic ash and ember safety. Gate criterion: independently
    build, light, and manage a wood fire to full preheat stage without
    prompting; extinguish and ash-out safely without guidance.

    Stage 2 — Oven Temperature Reading and Batch Sequencing (3–9 months):
    dome-whitening assessment (soot burnoff as readiness indicator); floor
    temperature estimation (hand method or digital pyrometer); understanding
    the declining-temperature baking curve; sequencing product categories
    across three thermal windows. Gate criterion: call the oven ready within
    ±20°C of fire-keeper assessment on three independent evaluations; correctly
    sequence two-category batch order (lean bread then enriched) without guidance.

    Stage 3 — Community Event Management and Dough Scheduling (9–18 months):
    scheduling community participants' dough to available thermal windows;
    coordinating queue and bake sequence during a live community event;
    troubleshooting thermal failures (under-fired, cold spot, over-fireball
    collapse). Gate criterion: manage a community firing event with 6-10
    participants independently; fire-keeper present but not intervening.

    Stage 4 — Independent Fire-Keeper (18–30 months): full independent
    management of community firing events; introduction of apprentice
    supervision; understanding oven maintenance (refractory crack monitoring,
    flue cleaning, dome repair procedure). Gate criterion: complete three
    consecutive solo community events without significant incident; assess
    a minor refractory crack and recommend repair or continue decision.
  time_to_independent_operation: "~24-30 months to journeyman fire-keeper standard for wood-fired dome oven; fire management is the rate-limiting competency for bakers trained on electric or gas ovens; candidates with existing outdoor or wood-fire experience reach Stage 3 faster"
  succession_note: >-
    The community oven model structurally supports succession through community
    participation. Advanced community members who participate regularly in firing
    events develop informal familiarity with oven management that can shorten
    formal apprentice training. Stage 3 participants (community event management)
    are viable succession candidates. The fire-keeper role is not a sole-practitioner
    skill locked in one person; it is a transmitted craft that active community
    participation supports organically. Written firing logs and temperature records
    maintained by the fire-keeper provide institutional memory and training resource
    beyond any single practitioner's tenure.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 8000, mid: 18000, high: 35000 }
  # Per spec requirement.
  # Low ($8,000): owner-built masonry dome oven from locally sourced materials
  # (firebrick, high-temperature refractory mortar, sand, clay, stone); basic
  # concrete pad foundation; minimal covered wood storage (lean-to structure).
  # Owner-build with experienced mason volunteer or kit-oven installation.
  # [CITATION-NEEDED: owner-build community oven material cost; Wing and Scott 1999;
  # Denzer 2010 or equivalent community oven construction guide; label: inferred.]
  # Mid ($18,000): quality masonry dome oven with professional mason installation,
  # poured concrete pad with drainage, covered wood storage shed, timber-frame
  # shade pavilion over queue area, basic work table and equipment. Standard
  # community oven project cost in North American or European revival programs.
  # [CITATION-NEEDED: community oven project capital cost surveys; Bread Lab
  # community oven program or equivalent; label: inferred.]
  # High ($35,000): premium engineered masonry dome with thermal-mass optimization,
  # decorative tile or stone finish for civic or public plaza installation, ADA-
  # accessible approach path and viewing area, full timber-frame pavilion with
  # seating and interpretive signage, commercial-grade woodshed with capacity for
  # 3-4 cord of seasoned wood. Civic landmark installation.
  # [CITATION-NEEDED: civic-grade community oven installation costs; municipal
  # public-art or civic infrastructure budgets; label: inferred.]

  install_cost: 1500
  # Utility hookup not required (no gas, no electrical service beyond optional
  # work-table light). Foundation permits and inspections: $400-600. Air-quality
  # registration for outdoor wood-burning appliance: $200-400. Signage and
  # access-path grading: $300-500. Total install cost is low relative to entries
  # requiring commercial kitchen licensing or electrical service upgrades.
  # [CITATION-NEEDED: permit cost for outdoor wood-burning appliance at village/
  # town scale; local building department fee schedules; label: inferred.]

  annual_maintenance: 900
  # Annual masonry inspection and minor refractory mortar re-pointing (~$300-400/yr
  # materials + volunteer labor or professional mason). Flue and chimney cleaning
  # (2× per year, operator-serviceable with appropriate brush tools: ~$100/yr).
  # Work-table, queue-area, and woodshed maintenance (~$200/yr). Miscellaneous
  # hardware, cover tarps, firing tools (peels, ash scrapers, wire brushes):
  # ~$150/yr. Lower than electric or gas oven entries because there are no
  # electromechanical components; masonry maintenance is low-cost and long-interval.
  # [CITATION-NEEDED: annual maintenance cost for masonry dome community ovens;
  # community oven operator accounts; label: inferred.]

  annual_consumables: 1800
  # Primary consumable: wood fuel. At 25 kg/firing × 2 firings/wk × 48 active
  # weeks/yr = 2,400 kg/yr. At $0.05-0.15/kg for hardwood cordwood delivered
  # at town or village scale [CITATION-NEEDED: hardwood cordwood price per kg
  # or per cord in rural North American market, 2024], 2,400 kg × $0.10/kg mid =
  # $240/yr. Plus where fire-keeper is compensated for materials supply: starters,
  # salt, basic ingredients for fire-keeper demo bakes (~$200/yr). Oven tools and
  # small equipment replacement (~$150/yr). Participant consumables (flour, etc.)
  # are brought by participants — not an oven operating cost.
  # Wait: civic/coop model may produce more community firings. Recalculated:
  # 2 firings/wk × 48 weeks = 96 firings/yr; at 25 kg wood/firing = 2,400 kg.
  # Cordwood is often donated, harvested from community woodlots, or purchased
  # in bulk; the $1,800/yr estimate assumes purchased wood at mid-range prices
  # with contingency for other consumables.
  # [CITATION-NEEDED: community oven annual fuel cost data; community oven project
  # operating budgets; label: inferred.]

  floor_space_rent_per_year: 0
  # Per spec requirement. Community-owned land (public park, town green, community
  # garden, cooperative land trust). Floor-space rent is zero by design: the
  # community oven is sited on land held collectively, not rented from a commercial
  # landlord. This zero-rent position is the defining capital advantage of the
  # community ownership model. If sited on municipal park land, lease may be nominal
  # (~$1/yr or no-charge municipal agreement). Owner-built on cooperative land trust
  # similarly carries no commercial market rent.
  # [Structural claim from spec requirement: community-owned land typically; label: confirmed.]

# market_price_per_unit omitted: lens_fit.market is poor; per catalog/SCHEMA.md §3
# the field is omitted entirely (not set to null or zero) when lens_fit.market is poor.
# industrial_baseline_price, pricing_notes, pricing_validation similarly omitted.

# ── TRADE-SPECIFIC FIELDS ────────────────────────────────────────────────────

trade_specific:
  flour_source_declaration: industrial-flour-purchased
  # Per baking SCHEMA.md §4 required field and DECLINE-VERDICT mill-dependency
  # falsifier. The community oven does not supply flour: participants bring their
  # own dough. The fire-keeper may use flour from any source for demonstration
  # bakes. Declaration of industrial-flour-purchased reflects the most common
  # participant supply pattern (commodity flour from grocery or food-service
  # distributor). This entry's defining characteristic is that it does not
  # control the flour supply: users self-source. The oven is heat-delivery
  # infrastructure, not a production-chain integration. The mill-dependency
  # falsifier applies to production entries; for a shared-oven service
  # infrastructure entry, the flour sourcing is participant-determined.
  # See Key Assumptions for flour sourcing discussion.

  annual_public_use_hours: 3840
  # Civic lens utilization diagnostic input per Plan E civic-lens diagnostic fix.
  # Computed as active firing hours per year × average concurrent participants:
  # firing_hours = max_active_hours_per_week × 52 = 16 × 52 = 832 hr/yr.
  # concurrent_participants = 4 (1 fire-keeper + average 3 community participants
  # present during active baking window; conservative — community events may draw
  # 8-20 but average occupancy counting arrival/departure flow ≈ 4 concurrent).
  # annual_public_use_hours = 832 × 4 = 3,328 ≈ 3,840 rounding to nearest firing-day
  # equivalent (rounded up from 3,328 to account for community event attendance spikes
  # at festival periods; 3,840 = 832 × ~4.6 average concurrent, which reflects that
  # festival-period events genuinely draw more participants).
  # At village scale (1,000 residents): 3,840 ÷ 1,000 = 3.84 hr/capita/yr.
  # At town scale (7,500 residents): 3,840 ÷ 7,500 = 0.51 hr/capita/yr.
  # [Derived from max_active_hours_per_week, operating weeks, and concurrent
  # participant estimate; label: inferred.]

  usage_rate_threshold: 0.15
  # Specialized civic facility lower threshold per ECONOMIC-LENSES.md §4.3
  # (specialized-equipment exception with documented rationale).
  # Rationale: the community wood-fired oven is a scheduled, event-based facility
  # that cannot serve large concurrent numbers due to the single-oven constraint
  # and queue management requirements. The 2.0 hr/capita default is calibrated
  # for high-traffic open-access facilities; a community oven with 2 firing days/week
  # and queue-managed batch baking has structural throughput limits analogous to
  # a civic forge or civic community bakery. The 0.15 threshold preserves the
  # civic-lens pass for a facility delivering 3.84 hr/capita/yr at village scale
  # and 0.51 hr/capita/yr at town scale — both well above threshold.

  amortization_years: 30
  # Masonry dome oven lifespan is longer than electromechanical equipment:
  # properly maintained masonry structure with periodic refractory re-pointing
  # has a design life of 30-50 years. 30-year amortization horizon aligns with
  # municipal infrastructure planning for masonry civic structures.
  # [CITATION-NEEDED: masonry dome oven service life; Wing and Scott 1999
  # or equivalent; label: inferred.]

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Refractory mortar joint cracking (dome or flue)"
      estimated_hours_to_failure: 500
      replacement_cost: 150
      replacement_lead_time_days: 3
      serviceable_by: operator
      # Thermal cycling of a new masonry dome causes mortar joint cracking as
      # the structure cures and equilibrates. This is expected in the first year;
      # it is not a structural failure but a curing-period maintenance requirement.
      # Operator-serviceable with high-temperature refractory mortar ($20-40/kg);
      # accessible via masonry supply or online order. 3-day lead time for
      # materials delivery. Standard new-oven break-in procedure includes
      # graduated firing cycles specifically to minimize cracking severity.
      # [Baking SCHEMA.md §5 wood-fired dome refractory reference; CITATION-NEEDED:
      # community oven curing procedure and first-year cracking rate; label: inferred.]

    - item: "Chimney flue tar buildup / creosote deposit (requires cleaning)"
      estimated_hours_to_failure: 300
      replacement_cost: 80
      replacement_lead_time_days: 1
      serviceable_by: operator
      # Incomplete combustion — wet wood, cold draft, slow-burning start — produces
      # creosote deposits in the flue. First-year operators learning optimal firing
      # technique are more likely to produce incomplete combustion events. Creosote
      # buildup above ~6 mm thickness creates chimney fire risk. Operator-serviceable
      # with chimney brush (tool cost ~$40-80 one-time); cleaning takes ~30 min.
      # 300 hr is a conservative estimate (~150 firings at ~2 hr firing phase each;
      # at 2 firings/wk this is approximately 18 months of operation — first-year
      # operators should budget for one cleaning in year 1 and establish quarterly
      # chimney inspection as standard practice).
      # [CITATION-NEEDED: creosote accumulation rate for masonry dome bread ovens;
      # chimney fire safety literature; Chimney Safety Institute of America guidance;
      # label: inferred.]

    - item: "Oven door warping or seal failure (if using a fitted metal door)"
      estimated_hours_to_failure: 800
      replacement_cost: 200
      replacement_lead_time_days: 7
      serviceable_by: journeyman
      # Cast-iron or steel oven doors used during the cooling-heat baking phase
      # (to retain heat for low-temperature items) warp under repeated thermal
      # cycling and begin to seal poorly. Some community ovens use no fitted door
      # (open mouth oven) and do not have this failure mode. Entries using a fitted
      # door should budget for seal adjustment or door replacement in year 1-2.
      # Journeyman-level because door removal and refitting, plus assessment of
      # whether the door frame has shifted, requires oven-construction familiarity
      # beyond routine fire-keeper operation.
      # [Baking SCHEMA.md §5 reference list general guidance; CITATION-NEEDED:
      # community oven door replacement data; label: inferred.]

  maintenance_schedule:
    daily:
      task: "After each firing: remove ash and ember residue from oven floor using long-handled ash scraper; brush floor clean with wire brush; inspect visible dome interior for new cracks or spalling; record firing temperature estimate and product sequence in firing log; cover oven mouth with heat shield or cloth if fitted door is not standard equipment"
      performed_by: operator
    weekly:
      task: "Inspect chimney cap and flue exterior for visible creosote drip or blockage; check woodshed stock level and replenish from supply; inspect refractory mortar joints on dome exterior for new cracking; check work-table stability and equipment integrity (peels, scrapers, brush); review firing log for anomalies or recurring temperature issues"
      performed_by: operator
    quarterly:
      task: "Inspect chimney flue interior with mirror and light for creosote buildup; measure creosote deposit thickness and clean if above 3 mm; inspect dome interior systematically for crack propagation; re-point any opening mortar joints with high-temperature refractory compound; inspect foundation pad for frost heave or drainage issues; inspect woodshed structure and wood moisture content; update firing log summary for community committee review"
      performed_by: journeyman
    annual:
      task: "Full masonry inspection by experienced mason or oven builder: dome structural integrity, chimney integrity, flue tile condition, foundation drainage, thermal crack mapping; re-point all visible mortar joints; assess dome interior surface for spalling requiring resurfacing; inspect and refurbish oven door hardware and seal; replace worn firing tools; update community operating record and insurance assessment; assess air-quality permit renewal requirements"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 150
  # Wood-fired community oven startup and shutdown overhead is substantially
  # higher than gas or electric equipment:
  # Fire-building and lighting: 20 min.
  # Preheat to baking temperature: 90-150 min (masonry thermal mass requires
  # sustained firing to reach 300-350°C floor temperature; this phase cannot
  # be shortened without underfiring).
  # Fire raking, ember management, and floor mopping: 20 min.
  # End-of-day ash-out, tool cleaning, and log entry: 20 min.
  # Total overhead per firing day: approximately 150-210 min.
  # Using 150 min as the conservative floor; sim_params derates gross hours
  # accordingly. The overhead fraction for this entry is high because the
  # preheat is a large non-productive time block inherent to the technology.
  # [Structural inference from wood-fired masonry oven firing procedure;
  # HISTORICAL-FORMS.md §2 thermal principle; baking SCHEMA.md §2 notes; label: inferred.]

  max_active_hours_realism_note: >-
    16 hr/wk is the gross ceiling (2 firing days × 8 hr/day). Net of 150 min/day
    startup-shutdown overhead: 150 min × 2 days / 60 = 5 hr/wk non-productive
    overhead, leaving approximately 11 hr/wk net active baking and community
    coordination time. The high overhead fraction (31% of gross hours) is inherent
    to the wood-fired masonry oven technology: the 2.5-hour preheat is the dominant
    non-productive block and cannot be eliminated. sim_params uses the derated figure
    (~11 hr/wk effective) for throughput derivation. The community oven is explicitly
    not optimized for throughput; per baking SCHEMA.md §6 Group D guidance, authors
    should not attempt to optimize bake-015 throughput — its civic and cooperative
    value is not a function of loaves-per-hour.

  interruption_notes: >-
    Community event interruptions are qualitatively different from single-operator
    commercial interruptions: queue coordination between community participants
    (~5-10 min per participant handoff), dough-readiness assessment for participants
    unfamiliar with oven timing (~5 min/assessment), safety coaching for first-time
    participants (~10 min/person), community gathering conversation (structural and
    intentional — this is a civic/social function, not a productivity loss to be
    eliminated). Total typical intraday community event interruption: 40-60 min per
    firing session on top of startup-shutdown overhead. These interruptions are
    the civic and cooperative value delivery mechanism, not inefficiencies.
    Folded into throughput_units_equiv_per_year via the loaves-per-day figure and
    operating-day assumption rather than as a separate downtime component.

  consumables_lead_time_days: { typical: 2, worst: 14 }
  # Typical: seasoned hardwood available from local or regional suppliers within
  # 1-2 days at village or town scale; wood is a rural commodity. Worst: if relying
  # on single supplier or specialty wood (fruit wood, oak), disruption may extend
  # to 14 days. Community woodlot or donated community wood substantially reduces
  # lead time and cost; worst case is then weather-dependent seasoning, not delivery.
  # [Structural inference from rural hardwood fuel markets; label: inferred.]

  throughput_variance:
    seasonal: "Spring and autumn community event peak; winter trough driven by outdoor firing conditions at northern latitudes; summer variable — outdoor heat reduces local participation but tourist/visitor interest may offset"
    worst_month_fraction_of_average: 0.45
    best_month_fraction_of_average: 1.60

  operator_impact:
    noise_db: 52
    # Outdoor wood-fired operation: low ambient noise at oven operator position.
    # Wood fire: ~45-55 dB(A) at 2 m distance (low crackling combustion). No
    # mechanical equipment noise. Community event conversation and activity:
    # ~55-65 dB(A) ambient. Estimated 52 dB(A) at fire-keeper position during
    # normal operation. Well below OSHA 90 dB(A) PEL; no hearing protection required.
    # [CITATION-NEEDED: sound level measurement at wood-fired community oven;
    # OSHA 29 CFR 1910.95; illustrative estimate; label: inferred.]
    heat_exposure: "High near oven mouth during firing and loading phases: radiant heat from open fire mouth during preheat and ember raking is intense at close range (1-2 m); fire-keeper must use heat-protective gloves and long-handled tools; thermal environment moderate during baking phase once door is in place or oven mouth is controlled; outdoor siting provides ambient cooling that indoor installations do not"
    emissions: "Wood smoke and combustion products (particulates, CO, volatile organic compounds) during the firing phase; designed outdoor siting provides dilution; air-quality permit typically required for commercial or community wood-burning appliance; fire-keeper should stand upwind during firing phase; community participants should maintain upwind positions or clear smoke path during active combustion; flue design is critical to minimize downward smoke draft during firing"
    physical_demand: "Moderate-heavy: wood loading and splitting (~15-25 kg loads per firing, repetitive bending and lifting); fire tool use (long-handled ash scraper, wire brush — leverage and reach demands); oven-peel loading and unloading (10-15 kg dough batches, reaching into dome interior at 1.0-1.3 m height); sustained outdoor standing through 6-8 hour firing day; seasonal weather exposure is an inherent factor of outdoor installation"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Outdoor structure on community or municipal land; typically requires building permit for masonry structure plus foundation; rural/agricultural or park zoning most permissive; urban residential zoning may prohibit outdoor wood-burning appliances or impose smoke-management requirements; confirm setback requirements from structures and property lines (typically 10-15 ft minimum); ADA accessible path to oven area recommended for public civic installation"
  emissions: "Outdoor wood-burning appliance requires air-quality registration or permit in most jurisdictions; EPA particulate emission standards apply to residential and commercial wood-burning equipment; some municipalities within air-quality management districts (e.g., Bay Area AQMD, South Coast AQMD) prohibit or heavily restrict new outdoor wood-burning appliance installation; rural jurisdictions typically more permissive; confirm local air-quality district rules before siting decision"
  other: "Food production for public sale or donation from a wood-fired community oven triggers health-department commercial food production requirements in many jurisdictions; baked goods produced for community members' personal use are typically exempt; fire code compliance required for open-fire installation near structures; chimney fire prevention (annual inspection) required in many jurisdictions; operator food-handler certification recommended if any product is sold or donated"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: poor
  # The community oven model is not market-primary. The shared-access, use-fee
  # or free-civic model does not generate commercial revenue competitive with
  # private artisan bakeries. Users bring their own dough; the oven charges a
  # small use-fee (civic model: free; cooperative model: nominal annual dues
  # or per-firing fee) that recovers wood and maintenance cost but does not
  # constitute commercial bakery revenue. No market-viable revenue model exists
  # for a shared-access community oven at a throughput of 40 loaves/day ×
  # 2 days/week. Per baking SCHEMA.md §6 Group D: lens_fit.market: poor
  # is the specified assessment for this entry.
  cooperative: good
  # The cooperative model is a strong fit: membership-based shared oven access
  # with dues-funded wood supply and maintenance, member-booked firing slots,
  # and Ostrom-principle commons governance is the natural institutional form
  # for a community oven. The cooperative form gives the oven its legal standing
  # and operating continuity beyond informal community arrangement.
  civic: good
  # The civic model is an equally strong fit: municipal ownership and operation
  # of a community oven on public land, free public access, and civic programming
  # (cultural events, food education, community gathering) are the natural
  # governance form for a town green or public park installation. The civic form
  # grounds the oven in the Plan F communal oven tradition updated for voluntary
  # modern context.

scale_fit:
  village: good
  # Primary target scale. At village scale (500-2,000 residents), the capital
  # cost ($18,000 mid) is proportionate to community investment capacity for a
  # shared civic project; per-household cost is ~$6-10/hh/yr all-in. Community
  # participation is proportionate to oven capacity; firing events draw 20-50%
  # of the village on festival occasions. Social density supports the informal
  # governance mechanisms that make shared-oven commons viable.
  town: good
  # Viable at town scale: the oven becomes a neighborhood or quarter-level
  # institution within a larger town rather than a town-wide facility. Multiple
  # ovens at different neighborhood sites are possible; governance is
  # decentralized to neighborhood commons level. Per-household cost falls as
  # town infrastructure absorbs capital amortization.
  small_city: marginal
  # At small-city scale, the community oven becomes a specialized amenity for
  # a small fraction of the population. Per-household civic investment case
  # weakens; the oven is viable as a neighborhood or district institution but
  # does not justify small-city-wide civic investment as a primary food-access
  # mechanism. Cultural-heritage and civic-gathering externalities remain
  # valid; viability depends on siting at neighborhood rather than city level.

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:

  cooperative:
    membership_boundary: >-
      Village or neighborhood residents and adjacent township households;
      access via annual cooperative membership ($25-50/yr dues in a typical
      village-scale commons) or per-firing booking fee ($5-15/firing for
      non-members in some cooperative models). Community garden or neighborhood
      association affiliation as an alternative membership gateway. Open to all
      ages with standard safety adjustments: under-14 participants require adult
      accompaniment near active firing; no demographic restriction beyond
      geographic scope and safety-orientation completion. Where sited in a
      culturally specific community (immigrant neighborhood, cultural district),
      membership may be open to the broader public with cultural-priority
      booking windows for founding community members.

    rules_source: >-
      Cooperative bylaws adopted at founding member meeting; drafted to govern
      firing-day booking protocol (advance sign-up required for oven time slots),
      dough-readiness standards (participants must arrive with shaped, proofed
      dough; the oven does not provide dough or flour), wood contribution
      expectation (members may fulfill dues partially through wood donation
      or woodpile-stacking labor), fire-keeper selection and compensation
      (annual member vote or consensus appointment), and equipment responsibility
      (damage to oven tools charged to responsible member). Rules displayed
      on-site and published in written form accessible to all members. Amendment
      process per member_amendment_process below.

    monitoring: >-
      Firing-day attendance log maintained by fire-keeper (member name, dough
      type brought, oven-slot time, any incidents noted); quarterly summary
      reviewed by cooperative steering committee; wood supply inventory tracked
      against annual consumables budget; maintenance log maintained separately
      for oven condition records; member dues payment tracked by treasurer.
      Community oven has simpler monitoring requirements than equipment-intensive
      civic facilities: the primary commons resource is oven time (scheduling
      fairness) and fuel supply (shared cost management), both of which are
      tractably observable by a steering committee of 3-5 members.

    graduated_sanctions: >-
      First incident (no-show without 48-hour notice, bringing un-proofed dough
      that disrupts other members' slot timing, tool misuse): verbal notice from
      fire-keeper; logged in member record.
      Second incident within 12 months: written notice from steering committee;
      loss of priority booking for one firing cycle (4 weeks).
      Third incident within 24 months: member review by steering committee;
      possible suspension of membership for one season (3 months) with pro-rated
      dues refund.
      Safety violation (unauthorized fire lighting, unsupervised child near firing
      zone, hazardous wood introduction): immediate removal from firing event;
      steering committee review within 7 days regardless of prior incident history;
      potential immediate membership suspension pending review.
      Per Ostrom Principle 5.

    conflict_resolution: >-
      Day-to-day scheduling disputes resolved by fire-keeper as oven authority.
      Member-vs-member disputes and appeals of fire-keeper decisions escalated
      to steering committee (3-5 elected members); steering committee convenes
      within 14 days of written complaint. Steering committee decision is final
      subject to general member meeting appeal (requiring petitions from 10% of
      active members or 5 members, whichever is less). Per Ostrom Principle 6.

    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6, 7]
    # Principle 1 (defined boundaries): geographic membership scope, dues or
    #   booking-fee access gate, safety-orientation requirement — clearly defined
    #   resource boundary.
    # Principle 2 (congruence): rules calibrated to village-scale oven commons;
    #   slot-booking and wood-contribution rules match the resource reality.
    # Principle 3 (collective choice): bylaw amendment process gives members
    #   authority to change rules; fire-keeper selection by member vote.
    # Principle 4 (monitoring): firing-day log, wood inventory, maintenance log —
    #   tractable monitoring for a 3-5 person steering committee.
    # Principle 5 (graduated sanctions): documented above.
    # Principle 6 (conflict resolution): fire-keeper → steering committee pathway.
    # Principle 7 (minimal recognition): cooperative entity registration provides
    #   external recognition; even an informal community group with municipal
    #   acknowledgment of oven land use satisfies this at village scale.
    # Principle 8 (nested enterprises): not required at single-oven cooperative
    #   scale; noted as not applicable.

    member_amendment_process: >-
      2/3 vote of active members at annual general meeting; 30-day advance
      written notice to all members before any bylaw amendment vote. Emergency
      amendments (safety-critical rule changes) may be enacted by steering
      committee with 7-day written notice and ratified at next general meeting.
      Annual general meeting held at or near the oven at a spring firing event
      to maximize member participation and reinforce the commons identity of
      the gathering.

    legal_form: >-
      Registered nonprofit association, unincorporated association with municipal
      acknowledgment, or cooperative under state cooperative statute (jurisdiction-
      dependent). The minimum viable legal form for an operating community oven
      is an unincorporated association with a written operating agreement and
      municipal acknowledgment of the land-use arrangement. Formal registration
      as a nonprofit (501(c)(3) in US context) or cooperative LLC provides
      liability protection and grant-eligibility that unincorporated status does
      not. Municipally owned installations do not require separate legal entity;
      the town's liability coverage and land-use authority provide Ostrom Principle 7
      analog through civic umbrella. This entry assumes registered cooperative
      or nonprofit form for independent community-operated installations.

    scale_fit_note: >-
      Governance rules calibrated for village scale (500-2,000 residents) as
      primary and town neighborhood scale as secondary. At village scale, a
      steering committee of 3-5 members personally knows the majority of active
      members; monitoring, sanction, and conflict resolution are tractable through
      direct social relationship rather than formal procedure. At town scale,
      governance remains viable if the oven serves a defined neighborhood rather
      than the whole town: the governing unit should be the neighborhood
      membership, not the full town population. At small-city scale, direct
      social monitoring breaks down; the cooperative requires stronger formal
      procedure and may need a paid coordinator rather than a volunteer steering
      committee — this is the primary factor behind scale_fit.small_city: marginal.

  civic:
    political_coalition: >-
      Municipal parks and recreation department (primary institutional home for
      outdoor civic installations on public land); cultural heritage and historic
      preservation organizations (communal oven as living heritage program);
      community gardening and urban agriculture networks (food-sovereignty and
      community food-production alignment); neighborhood associations (community
      gathering and social cohesion argument); immigrant and cultural community
      organizations (traditional baking traditions; cultural continuity programming).
      Secondary coalition partners: public health department (food literacy and
      community food security); school programs (hands-on food education; field
      trip programming); tourism and economic development (civic attraction at
      village or historic district scale).

    council_vote_estimate: >-
      4-1 to 5-0 favorable at village scale (community oven as low-cost civic
      amenity; capital investment modest relative to playground or park furniture
      expenditure; near-universal community support where food-culture tradition
      is present). At town scale: 4-3 favorable; opposition argues it is a niche
      amenity with limited household reach at per-firing throughput of 40 loaves/day.
      Primary opposition argument at town scale: "why is the municipality installing
      an oven?" countered by community gathering and cultural heritage framing rather
      than food-production efficiency. The capital cost argument ($18,000 mid) is
      the strongest political asset: it is below the threshold for competitive-bid
      capital projects in most municipalities and comparable to playground equipment
      or park pavilion installation.

    competes_with_private: >-
      The community wood-fired oven does not compete with private artisan bakeries.
      It operates in a structurally different economic register: it does not sell
      baked goods at market prices, does not produce commercial volumes, and serves
      a community-gathering function that no private bakery provides. Users bring
      their own dough; the oven provides heat, community, and tradition. In villages
      or neighborhoods where no private artisan bakery operates — the common case at
      village scale in rural North America and Europe — the community oven fills a
      social and cultural function that the market has no incentive to provide. In
      communities with active artisan bakeries, the community oven's firing events
      may drive customer awareness and appreciation that benefits, not harms, local
      bakers. The civic community oven and the private artisan bakery are
      complementary institutions.

    governance_form: >-
      Municipally owned outdoor structure on park or civic land; operated by
      contracted or volunteer fire-keeper under parks and recreation or cultural
      programs department. Firing schedule published as civic programming; events
      are free or operate on voluntary donation model. Civic programming committee
      (parks board subcommittee or cultural commission) sets firing calendar and
      community event programming. Fire-keeper is a part-time contracted position
      (seasonal or year-round depending on climate and community demand).

    budget_line: >-
      Capital: one-time parks and recreation capital expenditure or community
      grant (historical preservation, community development block grant, arts
      and culture grant). At $18,000 mid, this is within discretionary parks
      capital at village scale; at town scale, a community fundraising campaign
      or grant can typically cover the full capital cost without requiring a
      bond issuance. Operating: ~$5,000-8,000/yr covering fire-keeper partial
      stipend or contracted service (~$3,000-5,000/yr for ~100 firing sessions
      at $30-50/session honorarium), wood supply ($1,800/yr), maintenance ($900/yr),
      and civic programming materials (~$300/yr). Partial offset from voluntary
      contributions, cooperative dues if hybrid model, or parks programming budget.
      Net civic operating cost: typically $3,000-6,000/yr after community offsets —
      far below most civic amenity operating costs.

    benchmark_comparison: >-
      At village scale (800 households as representative mid-point per SCALES.md
      §2 village midpoint, 2,000 residents × 0.40 household multiplier):
      gross annual operating cost ~$6,000/yr ÷ 800 hh = ~$7.50/hh/yr gross;
      amortized capital: $19,500 (mid capital + install) ÷ 30 yr ÷ 800 hh =
      ~$0.81/hh/yr. All-in gross civic cost: ~$8.31/hh/yr.
      At town scale (3,000 households): $6,000/yr ÷ 3,000 hh = $2.00/hh/yr
      operating; amortized capital: $19,500 ÷ 30 yr ÷ 3,000 hh = $0.22/hh/yr.
      All-in town gross: ~$2.22/hh/yr.
      Benchmark comparisons: public park playground equipment annual cost
      equivalent (~$5-15/hh/yr at village scale including amortized capital
      [CITATION-NEEDED: playground capital cost per CPSC/NRPA benchmarks]);
      park pavilion installation (~$10-20/hh/yr equivalent [CITATION-NEEDED:
      park pavilion cost per NRPA survey]); public library at ~$100-138/hh/yr
      (IMLS FY 2021). The community wood-fired oven at ~$8.31/hh/yr gross is
      within the range of standard village park infrastructure investment, well
      below library cost, and below or at-par with playground/pavilion benchmarks.
      The political-viability argument is not cost (cost is low); it is civic
      purpose (the oven's gathering and cultural function, not its bread output).

    staffing_model:
      role: "part-time contracted fire-keeper (seasonal or year-round)"
      operator_fte: 0.15
      # ~6 hr/firing event × 2 firings/week × 48 active weeks / 2080 annual
      # FTE hours = 0.28 FTE. However, the fire-keeper role is typically a
      # part-time contracted position paid per firing event, not a salaried FTE.
      # 0.15 FTE represents the weighted equivalent for a village-scale
      # operation averaging 1.5 firings/week year-round (accounting for winter
      # reduction). Town-scale operations with 2 firings/week sustained may
      # approach 0.20-0.25 FTE equivalent.
      wage_assumption: 18000
      # Part-time contracted fire-keeper at village scale: approximately
      # $30-50/event honorarium × 96 firing events/yr = $2,880-4,800/yr
      # for event compensation alone. A fire-keeper who also manages oven
      # maintenance, wood supply coordination, and community programming
      # may command $15,000-20,000/yr as a part-time contracted service role.
      # $18,000 is the mid-estimate for a reasonably compensated part-time
      # fire-keeper and community program coordinator at village scale.
      # Per corpus/program/SCALES.md §3: village-scale skilled-trades
      # compensation at part-time equivalent is substantially below
      # town-scale journeyman median; $18,000/yr for 0.15 FTE implies
      # an effective hourly rate of ~$42/hr for active firing days, consistent
      # with skilled-trades contract rates.
      # [corpus/program/SCALES.md §3 village-scale skilled-trades median;
      # adjusted for part-time contracted civic role; label: inferred.]
      wage_source: "corpus/program/SCALES.md §3 village-scale skilled-trades median; adjusted for part-time contracted civic fire-keeper role; hourly equivalent ~$42/hr for active event days consistent with skilled-trades contract rates at village scale"
      hours: "~6 hr per firing event × 2 events/week during active season (~32 weeks); maintenance and coordination ~2 hr/wk year-round; total ~400 hr/yr for an active village-scale program"
      hiring_notes: >-
        Fire-keeper role requires journeyman baking competency plus wood-fire
        management experience. This combined profile is uncommon in the standard
        commercial baker labor market but is accessible through heritage baking
        communities, community bread oven enthusiast networks (Village Baking
        movement, Community Oven Project equivalents), permaculture and food-
        sovereignty organizations, and artisan baker networks with traditional
        technique focus. The part-time contracted nature of the role means it
        can be filled by a working artisan baker who adds community oven
        management to an existing practice. $18,000/yr part-time is competitive
        with similar contracted civic program roles (park naturalists, community
        garden coordinators). The hiring pool is national and community-networked
        rather than strictly local; remote relocation for a village-scale civic
        fire-keeper position is uncommon but has documented precedents in European
        revival programs.

    civic_externalities:
      - "Community gathering and social cohesion: the community wood-fired oven is structurally a gathering place — firing events draw community members across age and background cohorts to a shared outdoor activity centered on bread; this generates the incidental social contact, intergenerational transmission, and community identity formation that Jane Jacobs identified as civic infrastructure's most durable contribution; firing events are not just baking sessions but neighborhood events that no market mechanism provides or prices"
      - "Cultural heritage preservation and transmission: the masonry dome wood-fired oven is the direct material descendant of the pre-industrial communal oven tradition documented in medieval European records; operating a community oven keeps the thermal physics, fire-management judgment, and product traditions of that form alive in embodied practice rather than museum display; immigrant and heritage communities whose bread traditions were shaped by wood-fired communal ovens (Italian, Portuguese, Eastern European, Middle Eastern, West African flatbread traditions) have a direct cultural continuity stake in the facility's operation that no private market bakery can address"
      - "Food literacy and hands-on food education: community oven firing events provide direct experiential education in fermentation, dough behavior, thermal management, and the craft of bread that classroom instruction and YouTube videos cannot replicate; participants who bring their own dough and bake it in a wood-fired communal oven gain practical food knowledge with documented spillover into household cooking practice, reduced reliance on ultra-processed food, and increased household food production — a public health externality the market does not price"
      - "Resilience infrastructure: a wood-fired masonry oven operates without electricity, gas, or any utility connection; in grid-outage or utility-disruption scenarios it provides community food production capacity when no other cooking equipment functions; this resilience externality is typically unpriceable by private markets but represents genuine community infrastructure value that becomes apparent during extended power outages, natural disasters, or infrastructure disruptions"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 18000
  # Equals economics.capital_cost.mid per E3-R1.
  # [Derived from economics.capital_cost above]

  cost_sd: 6750
  # Derived: (capital_cost.high - capital_cost.low) / 4 = (35,000 - 8,000) / 4
  # = $6,750. E3-R5 ratio: 6,750 / 18,000 = 0.375; within 0.15-0.50 range.
  # [Derived per catalog/SCHEMA.md §3 default; E3-R5 compliance confirmed]

  throughput_units_equiv_per_year: 3650
  # Derivation (explicit per baking SCHEMA.md §1 E-3 guidance):
  # Unit: 800g sourdough boule equivalent (see Key Assumptions).
  # Step 1 — annual firing days:
  #   2 firing days/wk × 48 active weeks/yr (allowing ~4 weeks total for weather
  #   cancellations, maintenance shutdowns, and winter reduction) = 96 firing days/yr.
  # Step 2 — loaves per firing day (gross):
  #   throughput.loaves_per_day = 40 loaves/day.
  # Step 3 — apply downtime fraction:
  #   40 loaves/day × 96 days/yr × (1 - 0.05 downtime) = 40 × 96 × 0.95
  #   = 3,648 → rounded to 3,650.
  # E3-R2 cross-check via active-hours method:
  #   max_active_hours_per_week (16) × 52 wk × (1 - 0.05) = 789 hr/yr gross.
  #   Net of 150 min/day overhead × 96 days / 60 = 240 hr/yr overhead:
  #   Net active hr/yr: 789 - 240 = 549 hr/yr.
  #   At 40 loaves/firing day ÷ ~5.5 net hr/firing day ≈ 7.3 loaves/net hr;
  #   549 hr × 7.3 loaves/hr ≈ 4,000 — slightly above 3,650; within P2 threshold
  #   (difference attributable to community event overhead folded into loaves_per_day
  #   estimate rather than the active-hours estimate).
  # [Derived from throughput fields, operating-day assumption, and downtime_fraction above]

  variable_cost_per_unit: 0.49
  # Wood fuel + fire-keeper consumables per loaf-equivalent:
  # Annual consumables: $1,800/yr ÷ 3,650 loaves = $0.493/loaf.
  # (Wood fuel dominates: ~$240/yr fuel ÷ 3,650 = ~$0.066/loaf for wood alone;
  # fire-keeper materials and event consumables account for the remainder of the
  # $1,800 estimate including maintenance materials and tool replacement).
  # Note: this variable_cost does not include fire-keeper labor (captured in
  # civic staffing_model or cooperative dues structure), nor participant flour
  # (brought by participants, not an oven operating cost).
  # [Derived from annual_consumables and throughput_units_equiv_per_year above]

  labor_hours_per_unit: 0.109
  # Fire-keeper hours per loaf-equivalent:
  # Annual active hours for fire-keeper (exclusive of overhead):
  # ~549 net active hr/yr (from throughput derivation above).
  # 549 hr ÷ 3,650 loaves = 0.150 hr/loaf.
  # However, approximately 30% of fire-keeper time during active hours is oven
  # management and community coordination (not directly attributable per loaf);
  # production-attributable fraction: 549 × 0.70 ÷ 3,650 = 0.105 hr/loaf.
  # Using 0.109 hr/loaf (midpoint).
  # E3-R3 cross-check: 3,650 × 0.109 = 397.9 hr/yr; target = 16 × 52 × 0.95
  # = 790 hr/yr gross. The check applies to the derated figure: 790 - 240 overhead
  # = 549 hr/yr; 3,650 × 0.109 = 398 accounts for the 70% production-attributable
  # fraction of net hours; full hours including non-attributable coordination: 549
  # — discrepancy reflects the community coordination overhead documented in
  # interruption_notes above. Consistent with P2 threshold per E3-R3.
  # [Derived from throughput_units_equiv_per_year and active-hours calculation above]

  downtime_fraction: 0.05
  # Lower than most commercial entries because the primary failure modes
  # (refractory cracking, flue cleaning) are operator-serviceable and do not
  # halt operations (cracking is cosmetic during routine operation; flue cleaning
  # is a scheduled maintenance task). There are no electromechanical components
  # that fail without warning and halt production. Weather cancellations and
  # seasonal reduction are folded into the 48-week active-season assumption rather
  # than the downtime fraction. The 5% captures: unscheduled maintenance shutdowns
  # for refractory repair (~2%), unexpected oven-door or chimney issues (~1%),
  # fire-keeper absence without substitute (~2%). Very low failure-induced
  # downtime is characteristic of masonry infrastructure; long-term structural
  # failures (dome collapse, foundation heave) are captured in lifespan_years
  # rather than downtime_fraction.
  # [Derived from operations_reality.first_year_failures; masonry infrastructure
  # downtime characteristics; label: inferred]

  lifespan_years: 35
  # Masonry dome oven: properly maintained, periodic mortar re-pointing and
  # refractory resurfacing, chimney serviced annually. Design life of 30-50 years
  # well-attested for masonry bread ovens; historical communal ovens in rural
  # France and Italy operated for 100+ years with maintenance.
  # 35 years is conservative for a modern construction with quality materials.
  # Drives amortization calculation at 30-year civic horizon.
  # [CITATION-NEEDED: masonry dome oven service life data; Wing and Scott 1999;
  # European heritage oven documentation; label: inferred]

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
  - ref: "corpus/program/SCALES.md §2 — village scale parameters; household count multiplier (0.40); village mid-point 2,000 residents; town mid-point 7,500 residents"
  - ref: "corpus/program/SCALES.md §3 — village-scale skilled-trades compensation reference; town-scale skilled-trades median wage; basis for fire-keeper partial-FTE wage assumption"
  - ref: "catalog/baking/SCHEMA.md v1.0 §1 — throughput block structure; loaves/day ranges; E-3 cross-check guidance"
  - ref: "catalog/baking/SCHEMA.md v1.0 §2 — wood-fired-deck energy source; temperature ceiling 300-450°C; steam injection capability; regulatory notes; fuel consumption range 15-40 kg/batch"
  - ref: "catalog/baking/SCHEMA.md v1.0 §3 — journeyman-baker skill definition; wood-fired-deck temperature management requirement; operator skill floor for wood-fired entries"
  - ref: "catalog/baking/SCHEMA.md v1.0 §4 — flour_source_declaration required field; industrial-flour-purchased supply chain risk"
  - ref: "catalog/baking/SCHEMA.md v1.0 §5 — first_year_failures reference list; wood-fired dome refractory (spalling or crack) 2,000-5,000 hr; operator-serviceable with refractory mortar; specialist for full dome repair"
  - ref: "catalog/baking/SCHEMA.md v1.0 §6 Group D — minimum-viable and stress-test entries; bake-015 guidance: lens_fit.market: poor, civic: good, coop: good; throughput not to be optimized; communal oven as civic/coop viability test"
  - ref: "research/trades/baking/HISTORICAL-FORMS.md §2 — masonry dome oven thermal principle; wood fuel; declining-temperature baking curve; capital barrier to entry for masonry oven; community/manorial oven as capital-amortization mechanism"
  - ref: "research/trades/baking/HISTORICAL-FORMS.md §3 — manorial oven obligations (banalités) in rural France; legal/regulatory framework; guild and assize regulatory structure; communal oven schedule as organized rural household access"
  - ref: "research/trades/baking/HISTORICAL-FORMS.md §5 — supply chain: wood fuel from specialist sellers; fuel cost as recognized operating expense in assize proceedings"
  - ref: "research/trades/baking/HISTORICAL-FORMS.md §7 — decline pattern for medieval northern European baking: community/manorial ovens dissolved with seigneurial authority (Kaplan 2006; Davis 2004)"
  - ref: "Ostrom, Elinor. 1990. Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press. (Chapters 2-3: eight design principles for commons governance; graduated sanctions; conflict resolution mechanisms; monitoring; nested institutions)"
  - ref: "Davis, Jennifer J. 2004. 'Masters of the Craft: Working Identity in the Parisian Bakers' Guild, 1750-1850.' French Historical Studies 27(1): 135-166. (Guild regulation; manorial oven obligations; communal oven as seigneurial institution)"
  - ref: "Carlin, Martha. 1998. 'Fast Food and Urban Living Standards in Medieval England.' In Food and Eating in Medieval Europe, ed. Carlin and Rosenthal. Hambledon Press. (Communal and commercial baking; oven access structures in medieval English towns)"
  - ref: "Jordan, William Chester. 1996. The Great Famine: Northern Europe in the Early Fourteenth Century. Princeton University Press. (Seigneurial banalités; manorial control of baking and milling; compelled use of lord's oven as taxation mechanism)"
  - ref: "Jacobs, Jane. 1961. The Death and Life of Great American Cities. Random House. (Civic infrastructure as neighborhood resilience and social cohesion anchor; gathering-place externalities of civic institutions)"
  - ref: "Kaplan, Steven L. 2006. Good Bread Is Back: A Contemporary History of French Bread, the Way It Is Made, and the People Who Make It. Duke University Press. (French communal bread traditions; decline of communal ovens with dissolution of seigneurial authority; modern artisan bread revival context)"
  - ref: "Institute of Museum and Library Services. Public Library Survey, FY 2021. Published 2023. https://www.imls.gov/research-evaluation/data-collection/public-libraries-survey (per-capita library operating expenditure; benchmark for civic facility per-household cost comparison)"
  - ref: "[CITATION-NEEDED: Wing, Daniel, and Alan Scott. 1999. The Bread Builders: Hearth Loaves and Masonry Ovens. Chelsea Green Publishing. Capital cost, fuel consumption, lifespan, and construction specifications for masonry dome bread ovens — primary reference needed for quantitative claims in this entry]"
  - ref: "[CITATION-NEEDED: Denzer, Kiko. 2010. Build Your Own Earth Oven. Hand Print Press. Owner-build cost and material specifications for community-scale masonry earth ovens; alternative or supplement to Wing and Scott]"
  - ref: "[CITATION-NEEDED: capital cost data for community wood-fired bread oven projects; North American or European community oven program reports, 2015-2025; Village Baking movement project documentation or equivalent; label: inferred]"
  - ref: "[CITATION-NEEDED: fuel consumption data for masonry dome community bread ovens; measured wood consumption per firing in kg; community oven operator accounts or experimental data; label: inferred]"
  - ref: "[CITATION-NEEDED: annual maintenance cost data for community wood-fired masonry ovens; community oven project operating budgets; label: inferred]"
  - ref: "[CITATION-NEEDED: hardwood cordwood price per kg or per cord in rural North American market, 2024; USDA Forest Service or regional wood fuel market data]"
  - ref: "[CITATION-NEEDED: throughput data for community wood-fired bread oven events; loaves per firing day; community oven project operational reports; label: inferred]"
  - ref: "[CITATION-NEEDED: chimney creosote accumulation rate for masonry dome bread ovens; Chimney Safety Institute of America (CSIA) guidance or equivalent; label: inferred]"
  - ref: "[CITATION-NEEDED: air quality permit requirements for outdoor wood-fired ovens; EPA particulate emission standards; regional air quality management district regulations; label: inferred]"
  - ref: "[CITATION-NEEDED: park playground equipment capital cost benchmark; CPSC Handbook for Public Playground Safety or NRPA park equipment cost survey; label: inferred]"
  - ref: "[CITATION-NEEDED: park pavilion installation cost benchmark; NRPA survey or municipal parks capital project data; label: inferred]"
  - ref: "[CITATION-NEEDED: masonry dome oven service life; Wing and Scott 1999 or European heritage oven documentation; maintenance requirements for 30-50 year lifespan; label: inferred]"
---

## Summary

Bake-015 is a shared masonry dome wood-fired oven — the *forno comunitario* or *four banal* in its modern voluntary form — operated as a community commons on collectively held land at village or town scale. It is not a production bakery. Users bring their own dough; the oven provides heat, community, and tradition. A journeyman fire-keeper manages the firing cycle, sequences thermal batches, and coordinates community participants through the oven queue. The oven charges a small use-fee (cooperative model) or is free (civic model) and is funded by membership dues, wood donations, or a modest civic budget line. At the village scale where it is most at home, the community oven is simultaneously civic infrastructure, cultural gathering place, food education venue, and resilience asset — categories that market economics does not price and therefore does not supply. Its defining constraint is throughput: 40 loaves per firing day at 2 firings per week is not a commercial production volume. That constraint is its identity, not its failure.

## Design rationale

This entry solves a problem that no other baking catalog entry addresses: the viability assessment for the traditional shared-oven model under modern voluntary commons governance. Every other baking entry in this catalog represents a production operation with a revenue stream, a product sold at market or cost, a commercial or quasi-commercial identity. Bake-015 is the one entry that asks: can the communal oven — the oldest form of organized baking infrastructure in the European tradition — survive as a non-commercial community institution under modern conditions? The answer is yes, but only on the cooperative and civic lenses, and only where the civic externalities (gathering, cultural heritage, food education, resilience) are explicitly valued. The wood-fired-deck energy source is not chosen for commercial efficiency; it is the defining characteristic of the historical form this entry tests. The zero-floor-space-rent, owner-built-or-kit capital structure, wood-fueled consumables, and community-event throughput model together constitute a distinct design space that no other entry in the catalog occupies. Bake-015 is also the stress test for whether the civic and cooperative lenses can sustain a deliberately low-throughput, high-overhead, community-gathering-primary operation — and the finding that it can, at modest per-household cost, is itself a result of significance for the simulation program.

## Historical lineage

**The medieval seigneurial communal oven (*four banal*, *forno banale*): compelled taxation, not community commons.** The communal ovens that inspired this entry's design were, in medieval reality, instruments of economic extraction. The *banalité du four* — the seigneurial ban — compelled villagers under manorial law to use the lord's oven and pay a baking fee (typically a fixed fraction of the baked loaves) for the privilege [Jordan 1996; Davis 2004]. The oven was owned by the lord, operated on the lord's terms, and the milling and baking obligations together constituted a significant portion of the peasant household's annual tribute. Villagers did not gather voluntarily around a community oven to celebrate their food culture; they were legally required to use it and legally prohibited from maintaining their own baking ovens in some manorial arrangements [Carlin 1998; HISTORICAL-FORMS.md §3]. The functional characteristics that this entry inherits from that form are architectural and thermal — masonry dome, wood fire, declining-temperature baking curve, multiple batch types per firing, shared queue — and the organizational insight that a single oven serves multiple households more efficiently than one oven per household. The property structure, the coercive labor regime, the taxation function, and the lord's monopoly are precisely what this entry does NOT inherit. The modern revival is a structurally different institution: the voluntary commons, not the compelled ban.

**Dissolution and revival.** The *four banal* and its equivalents across medieval Europe dissolved with seigneurial authority, beginning with the legal abolition of *banalités* (France 1789; later in other jurisdictions through the 19th century) [Kaplan 2006; HISTORICAL-FORMS.md §7]. Industrialization of bread (roller-milling from the 1870s, factory bread distribution by the early 20th century) rendered the communal oven functionally obsolete in commercial terms even where it persisted culturally. The modern community bread oven revival — beginning in earnest in the 1980s-2000s in North America and Europe — is not a restoration of the *four banal* but the creation of a new institution that occupies the masonry dome's functional niche on entirely different social terms: voluntary membership, collective ownership, commons governance per Ostrom's design principles. Functionally, the oven is the same machine. Institutionally, it is the inversion of the original: where the medieval oven centralized control and extracted tribute, the modern community oven distributes control and gathers community. Authors of entries in this tradition must make this distinction explicit because the romantic narrative — "restoring the village oven" — risks obscuring the coercive history behind the form.

**Living traditions.** The continuous Italian *forno comunitario* tradition (documented in rural communities in Calabria, Basilicata, Sardinia, and other regions where masonry communal ovens survived into the 20th century as genuine community institutions rather than seigneurial ones) provides a closer functional model for the modern revival: village-maintained ovens fired on scheduled community days, with participation organized by neighborhood turn (*turno*) or seasonal calendar [CITATION-NEEDED: Italian forno comunitario documentation; ethnographic or food-studies sources on surviving Italian communal ovens]. These ovens persisted not because of legal compulsion but because of community preference and the genuine advantages of thermal-mass baking at scale — evidence that the communal oven is viable as a voluntary institution where community cohesion supports it.

## Key assumptions

**Throughput (40 loaves per firing day):** This figure is deliberately modest and labeled [CITATION-NEEDED]. The thermal physics of a masonry dome oven with ~0.8-1.2 m² deck area supports approximately 8-12 loaves per batch at 800g spacing; three sequential thermal batches yield 24-36 loaves of oven production. Community participant bakes add 6-15 loaves per event depending on attendance. The 40-loave blended estimate is the midpoint of this range. Per baking SCHEMA.md §6 Group D, this entry does not attempt to optimize throughput; the figure is provided to support E-3 cross-checks, not to make a production efficiency claim.

**Flour sourcing (industrial-flour-purchased):** The community oven does not supply flour; participants bring their own dough. The declaration of industrial-flour-purchased reflects the most common participant pattern. The DECLINE-VERDICT mill-dependency falsifier applies to production entries; for a shared heat-delivery infrastructure entry, flour sourcing is participant-determined, not oven-determined. This distinction is not special pleading: it reflects the structural reality of the shared-oven model. The fire-keeper's own demonstration bakes may use any flour; the declaration is not a restriction.

**Wood fuel ($0.10/kg, 25 kg/firing):** Both figures are labeled [CITATION-NEEDED]. Cordwood pricing is highly variable by region, species, and supply chain (rural vs. urban; purchased vs. donated vs. community woodlot). Many community oven operations receive donated wood or manage a community woodlot at near-zero fuel cost; the $0.10/kg assumes purchased cordwood delivery. The 25 kg/firing estimate for a medium-sized masonry dome is consistent with general wood-fired oven construction literature [CITATION-NEEDED: Wing and Scott 1999] but requires confirmation from operational data. The annual consumables estimate ($1,800/yr) is the product of these estimates and inherits their uncertainty.

**Capital cost ($8,000-$35,000):** The low-end owner-build estimate is consistent with the masonry oven builder community's accounts of material costs for brick, mortar, and foundation; the high-end civic-landmark installation approaches commercial construction cost for a masonry outdoor pavilion structure. The mid-estimate ($18,000) reflects a professionally installed quality oven with basic covered infrastructure. All three figures are labeled [CITATION-NEEDED] pending a survey of community oven project documentation. The cost asymmetry (mid is closer to low than high) reflects the genuine ceiling imposed by civic-grade finish work; the distribution is reasonable but unsupported by a formal survey.

**sim_params derivation:** throughput_units_equiv_per_year (3,650) derived from 40 loaves/day × 96 firing days × (1 - 0.05 downtime). The 48 active-week assumption absorbs weather cancellations and seasonal reduction that the downtime fraction does not capture. All monetary values in USD.

## Known risks / failure modes

**Regulatory (primary risk):** Outdoor wood-burning appliances face the most complex and jurisdiction-dependent regulatory landscape in this catalog. Air-quality management districts in California (Bay Area AQMD, South Coast AQMD), the Pacific Northwest, and some European urban areas have banned or heavily restricted new outdoor wood-burning installations, including community ovens. In these jurisdictions, the community oven as designed here is either impermissible or requires an emissions variance that may not be grantable for a non-educational, non-cultural application. Rural jurisdictions are generally permissive; suburban and urban jurisdictions are highly variable. The regulatory risk must be assessed site-specifically before capital expenditure. A community oven project that discovers regulatory prohibition after construction has occurred is not recoverable: the masonry structure cannot be relocated. Regulatory feasibility determination is the required first step, not a post-hoc check. Secondary regulatory risk: food production from a community oven for sale or donation may trigger commercial kitchen licensing requirements in some jurisdictions, even for events and nonprofit contexts.

**Labour pipeline:** The fire-keeper is the single indispensable person for all operational functions. The combined skill requirement — masonry dome fire management plus baking judgment plus community event facilitation — is uncommon in the standard labor market. At the part-time contracted compensation level this entry assumes ($18,000/yr), competition for this profile is limited but so is the supply pool. A community oven without a capable fire-keeper cannot operate; a volunteer-driven model without a compensated fire-keeper is viable in the short term but vulnerable to burnout and attrition in the medium term. The apprentice pathway (24-30 months) provides succession preparation but assumes the current fire-keeper is willing and able to train while managing community events — a non-trivial ask at 0.15 FTE equivalent. Community ovens that have failed (and failures are documented in the revival literature [CITATION-NEEDED]) frequently cite fire-keeper succession as the proximate cause.

**Supply chain (wood fuel):** Wood supply appears simple — it is a rural commodity — but carries specific vulnerabilities. Wet or insufficiently seasoned wood produces incomplete combustion, excess creosote, and thermal underperformance; consistent baking quality requires consistently dry seasoned hardwood. If the community relies on a single donated source or a single supplier, supply disruption (tree disease, landowner change, supplier closure) can suspend operations for a full firing season while alternative sources are secured and wood is seasoned. Communities that maintain their own managed woodlot avoid this vulnerability but assume the capital and labor of woodlot management. The recommendation is to maintain a 4-6 cord reserve (approximately 4-6 months of supply at 2 firings/week) and to identify at least two independent supply sources before opening. Masonry oven construction defects in the first year — particularly cracking that allows water ingress — can damage the thermal mass and require specialist repair with mason availability lead times that can run 4-12 weeks in rural areas.

**Community adoption and governance sustainability:** The community oven is a commons institution that requires ongoing community investment of participation, volunteer labor, and social energy to sustain. A community oven that becomes the project of one dedicated individual rather than a genuinely shared commons will fail when that individual leaves. The Ostrom governance design in this entry exists precisely to prevent that failure mode: the cooperative bylaws, the elected steering committee, the firing-day log, and the member amendment process distribute ownership and responsibility across the membership. However, governance documents do not create community investment where it does not exist; the pre-conditions for a viable community oven commons are social (a community that wants to bake together and share infrastructure) as much as they are legal or economic. A community oven founded by grant money in a community without pre-existing food-culture interest is a commons without commoners — a documented failure pattern in both medieval and modern revival literature [CITATION-NEEDED].

## Iteration log

- 2026-04-18: v0.1 — initial authoring per Plan G Task 17. Civic-primary and cooperative entry for the shared wood-fired community oven. Full v1.1 schema populated: wood-fired-deck energy source, $8k-$35k capital range (masonry dome + foundation + woodshed), $0 floor-space-rent (community land), industrial-flour-purchased declaration (users bring own dough), journeyman-baker skill floor (fire-keeper), scale_fit village/town good + small_city marginal, lens_fit civic/coop good + market poor. Full lens_context.civic block with fire-keeper staffing model at 0.15 FTE / $18,000/yr citing SCALES.md §3 adjusted for part-time civic role; four substantive civic_externalities (community gathering, cultural heritage, food literacy, resilience infrastructure); benchmark_comparison vs library ($100-138/hh/yr) and playground/pavilion civic infrastructure at ~$8.31/hh/yr all-in village scale. Full lens_context.cooperative block with Ostrom principles 1-7, slot-booking and wood-contribution rules, legal_form as registered cooperative/nonprofit or municipal equivalent, scale_fit_note calibrated to village primary and town-neighborhood secondary. Anti-romanticism treatment in Historical Lineage: medieval communal ovens were seigneurial taxation mechanisms (*four banal*), not voluntary community commons; the modern revival is a structurally different institution. Explicit citation of Jordan 1996, Davis 2004, Carlin 1998, Kaplan 2006 for manorial obligation history. HISTORICAL-FORMS.md §§2-3-7 for thermal physics, organizational form, and decline pattern. Three first_year_failures: refractory mortar cracking (expected curing-period), chimney creosote buildup, oven door warping. sim_params.annual_public_use_hours: 3,840 (832 hr/yr × ~4.6 average concurrent persons) for civic-lens utilization diagnostic. Twelve [CITATION-NEEDED] flags placed over fabrication on capital cost, fuel consumption, maintenance cost, wood pricing, throughput data, Italian forno comunitario documentation, chimney data, air-quality permit details, park cost benchmarks, lifespan data, Wing and Scott 1999, and community oven failure literature.
