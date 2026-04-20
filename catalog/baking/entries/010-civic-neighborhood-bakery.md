---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: bake-010
trade: baking
name: "Civic Neighborhood Bakery"
tagline: "Municipally-owned electric-deck neighborhood bakery; library-model access with journeyman-instructor and apprentice training pipeline"
status: draft
version: "0.1"
supersedes: null
inspirations:
  - french-boulangerie-sociale-tradition
  - us-public-library-model
  - cooperative-extension-community-kitchen-programs

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 52
# Mid-range of the 40-65 m² spec envelope. 52 m² supports a two-deck electric
# oven, proofing cabinet, commercial spiral mixer, dough-prep tables, member
# workstations (2 simultaneous supervised bakers), and staging/cooling area.
# Town-owned space; footprint drives building-selection and interior-fitout costs.
# [CITATION-NEEDED: commercial community bakery footprint survey; structural
# inference from baking SCHEMA.md §1 throughput ranges and multi-user layout
# requirements; label: inferred.]

ceiling_min_m: 2.8
# Minimum for overhead clearance above two-deck oven stack plus commercial
# exhaust hood installation. 2.8 m adequate for electric-deck configuration
# without combustion stack height requirements.
# [Structural inference from commercial kitchen design standards; baking SCHEMA.md §2.]

ventilation: kitchen-exhaust-hood-required
# Electric deck produces heat and steam; commercial exhaust hood required for
# health-code compliance and operator/member comfort during multi-hour baking
# sessions. No combustion gases; no air-quality permit trigger from oven.
# Steam load is higher in a supervised multi-user context (parallel bake cycles).

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: electric-deck
# Per spec requirement. Cleanest permit path for a public-access civic facility:
# near-zero on-site combustion emissions, thermostat-controlled temperature
# (essential for supervised use by members at varying skill levels), and
# elimination of fuel-storage requirements that would complicate a library-model
# public building. Two-deck unit provides parallel capacity for instructor and
# member bake sessions.
# Per baking SCHEMA.md §2: electric-deck temperature ceiling 230-290°C;
# thermostat control is a key safety and usability advantage in a supervised
# multi-skill context.
energy_consumption_per_active_hour: "9 kWh"
# Two-deck commercial electric oven at operating temperature: approximately
# 7-11 kWh combined rated draw per hour at sustained bake load.
# 9 kWh/hr is a mid-range estimate for a two-deck unit (each deck ~4-6 kW rated,
# combined sustained consumption at operating temperature approximately 8-10 kWh/hr).
# Proofing cabinet and mixer draw additional ~1 kWh/hr when concurrent.
# Per baking SCHEMA.md §2: electric-deck 3-8 kWh/batch; two-deck unit at
# combined load approaches 9 kWh/active baking hour.
# [CITATION-NEEDED: manufacturer energy consumption data for two-deck commercial
# electric ovens, e.g., Bongard, Sveba-Dahlen, or equivalent; label: inferred.]
backup_fuel: null
# No backup fuel in civic base configuration. Grid outage risk is noted in
# Known Risks. A propane backup combi would substantially increase capital cost
# and permitting complexity for a public-access facility; omitted from base design.

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  loaves_per_day: 80
  # Net production output per operating day. Unit: 800g sourdough boule equivalent
  # (see Key Assumptions for unit definition). Civic model is not throughput-
  # maximized: output is shared between instructor-led production (saleable loaves)
  # and member practice sessions (training-output loaves, not all sold commercially).
  # Two-deck oven supports parallel use: instructor deck + member deck simultaneously.
  # Productive (saleable) output estimated at 60% of bakes; remainder is training-
  # output and community-access bakes consumed by members or donated. 80 loaves/day
  # is the blended daily output including both productive and community-access work.
  # [CITATION-NEEDED: empirical throughput for civic/community bakery model;
  # structural inference from baking SCHEMA.md §1 village-artisan range 30-100;
  # label: inferred.]

  batches_per_day: 4
  # Two decks × 2 bake loads per deck per operating day. Each deck runs one
  # morning batch and one afternoon batch; 4 total deck-loads per day.
  # Civic scheduling: 5 operating days/week with occasional community-event
  # sixth day (captured in operating-day estimate). [Structural inference from
  # two-deck operation scheduling.]

  batch_size_loaves: 20
  # Two-deck unit: approximately 10 loaves per deck per load at 800g boule
  # spacing; 20 loaves per combined batch-load cycle. Instructor deck and
  # member deck operate semi-independently on staggered timing.
  # [CITATION-NEEDED: deck-oven capacity per m² of deck area; two-deck
  # commercial oven manufacturer specifications; label: inferred.]

  max_active_hours_per_week: 32
  # Civic scheduling: 5-6 operating days per week × ~5.5 active hr/day = 32 hr/wk.
  # Lower than single-operator commercial entries (35-45 hr/wk): civic scheduling
  # includes member check-in, orientation briefings, and handoffs not present in
  # single-operator production. Gross ceiling; derated in sim_params. Per entry
  # parameters: civic model is supply-constrained by scheduled shifts and staff
  # capacity, not by demand.

  product_mix:
    bread: 65
    # Artisan sourdough and yeasted loaves: core production for community
    # distribution. Includes plain sourdoughs, enriched loaves, traditional
    # cultural breads per community requests. Instructor manages sourdough
    # program; members focus on yeasted and simpler enriched breads during
    # supervised sessions.
    confection: 10
    # Basic pastry and enriched rolls for community events, nutrition education
    # sessions, and donated food-program supply. Kept to journeyman-baker-
    # accessible confection (no laminated doughs in base configuration).
    specialty: 15
    # Cultural specialty breads per community baking traditions (see
    # civic_externalities: cultural traditions preservation). Varies by community
    # demographics and instructor expertise.
    catering: 0
    # No commercial catering; civic facility. Community events served via
    # donation or member-access model, not commercial catering contract.
    training_output: 10
    # Member-practice bakes not sold commercially; distributed as community
    # donations to food-access programs or consumed at nutrition education events.
    # Sum: 65+10+15+0+10 = 100.

  throughput_variance:
    seasonal: "Moderate civic seasonality: summer community event uptick; post-holiday (January) slowdown; school-year alignment boosts nutrition-education program demand September-June"
    worst_month_fraction_of_average: 0.60
    # Artisan bread range 0.55-0.75 per baking SCHEMA.md §1; 0.60 reflects the
    # moderate trough in a civic facility that maintains floor activity through
    # community-program scheduling even in slow bread-demand months.
    # [Baking SCHEMA.md §1 throughput_variance guidance; label: inferred.]
    best_month_fraction_of_average: 1.35
    # Pre-holiday community event demand and school-year nutrition program peaks.
    # Consistent with baking SCHEMA.md §1 artisan bread range 1.20-1.40.
    # [Same source; label: inferred.]

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: journeyman-baker
# Per spec requirement. Civic multi-user model requires a journeyman baker
# who functions as instructor: independently manages full sourdough cycle,
# supervises member bakers at varying skill levels, and provides instruction
# without creating safety or quality failures. Per baking SCHEMA.md §3:
# journeyman-baker can manage full sourdough cycle, run deck oven without
# supervision, execute standard enriched doughs, and supervise an apprentice.
# The instructor role adds pedagogical responsibility not present in single-
# operator commercial entries; hiring notes in staffing_model address this.
# [Baking SCHEMA.md §3 operator skill definitions]

operators_concurrent: "1 instructor + up to 2 members"
# Scheduled shift model: 1 journeyman baker-instructor present at all times
# during public-access sessions; up to 2 community members work simultaneously
# under supervision. Session size limited by available workstations (2 member
# stations + instructor station) and supervision capacity. Instructor cannot
# safely supervise more than 2 novice bakers simultaneously on a commercial
# deck oven without compromising safety or instruction quality.

apprentice_friendly: true
apprentice_path:
  training_stages: >-
    Stage 1 — Orientation and Safety (0–2 months): food-handler hygiene,
    kitchen safety protocol, equipment orientation (deck oven startup/shutdown,
    proofing cabinet, mixer use), sourdough starter observation. Gate criterion:
    pass food-handler certification; demonstrate correct equipment startup and
    shutdown procedure independently; maintain a sourdough starter on schedule
    for two weeks without prompting.

    Stage 2 — Supervised Basic Baking (2–8 months): yeasted bread dough mixing,
    basic shaping (round loaf), oven-load timing under instructor supervision.
    Introduction to fermentation observation (not independent judgment yet).
    Gate criterion: complete 8 consecutive yeasted boules to journeyman-accepted
    shape standard without guidance on the final three; load and unload oven
    safely without prompting.

    Stage 3 — Fermentation Judgment Development (8–24 months): bulk fermentation
    monitoring, proofing-schedule reading under graduated supervision, deck oven
    temperature management. Begin sourdough production with instructor review.
    Introduction to cultural specialty breads per program curriculum. Gate criterion:
    operate a full production day independently (instructor present, not intervening)
    with acceptable yield and crumb quality for three consecutive sessions.

    Stage 4 — Journeyman Progression and Community Teaching (24–42 months):
    full sourdough program management, specialty loaf recipes, nutrition education
    co-facilitation with instructor, introduction to member supervision (Stage 1–2
    co-facilitation). Gate criterion: journeyman-baker standard assessment by
    instructor; eligible to lead a member session independently with instructor
    oversight.
  time_to_independent_operation: "~36-42 months to journeyman-baker standard; fermentation judgment formation is the rate-limiting step; civic program structure provides consistent supervised practice that accelerates competency development vs. self-directed learning"
  succession_note: >-
    The civic model structurally embeds succession: apprentice training is integrated
    into the facility's normal operation mode, not a separate program. Each training
    cycle (3-4 years) produces 1-2 journeyman-baker candidates from the community
    workforce-development pipeline. Advanced apprentices (Stage 4) assist in
    member instruction, reducing the instructor's sole-practitioner risk and building
    institutional curriculum depth. The facility committee's curriculum records and
    production logs provide institutional continuity beyond any single instructor's tenure.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 45000, mid: 80000, high: 130000 }
  # Per spec requirement. Low: entry-level two-deck commercial electric oven
  # (~$18,000-22,000 refurbished or budget new), basic proofing cabinet (~$3,000),
  # commercial spiral mixer (~$3,500), member workstations (tables, tools: ~$5,000),
  # smallwares and starter kit (~$2,000). Minimal civic fitout.
  # Mid: mid-grade two-deck commercial oven ($28,000-35,000 new), full proofing
  # cabinet with humidity control ($5,000), commercial spiral mixer ($5,000),
  # two fully equipped member stations ($8,000), display shelving and community
  # room integration ($4,000), curriculum signage and storage ($2,000).
  # High: premium two-deck commercial oven ($42,000-50,000), full proofing
  # and cold-retard system ($8,000), heavy-duty spiral mixer with divider ($7,000),
  # complete member training stations ($10,000), kitchen exhaust system upgrade
  # ($5,000), full civic fitout (accessibility compliance, community room).
  # [CITATION-NEEDED: capital cost data for commercial two-deck electric ovens
  # and community bakery fitout, 2024-2026; illustrative estimates from market
  # observation of bakery equipment vendors; label: inferred.]

  install_cost: 8000
  # Electrical service upgrade (60-80A dedicated circuit for two-deck unit),
  # exhaust hood installation and ductwork, health-department commercial kitchen
  # inspection and certification, accessibility compliance modifications to
  # member workstation heights. Civic building may reduce some costs if existing
  # commercial kitchen infrastructure is present.
  # [CITATION-NEEDED: installation cost for commercial two-deck bakery kitchen
  # in civic facility; illustrative estimate; label: inferred.]

  annual_maintenance: 2800
  # Two-deck oven servicing, proofing cabinet calibration, mixer maintenance,
  # exhaust hood quarterly cleaning (health-code requirement), member tooling
  # replacement (bannetons, lames, misc). Multi-user intensity elevates wear
  # on shared tooling relative to single-operator entries. Excludes first-year
  # failure replacements itemized in operations_reality.
  # [CITATION-NEEDED: annual maintenance data for community bakery operations;
  # illustrative estimate; label: inferred.]

  annual_consumables: 9500
  # Primary: flour for both instructor production and member practice sessions.
  # Instructor production (~50 loaves/day × 260 days × 0.7 kg/loaf × $0.60/kg
  # = ~$5,460/yr flour for saleable output [CITATION-NEEDED: commodity bread
  # flour wholesale price per kg]). Member practice flour and consumables
  # (~$1,500/yr additional). Salt, packaging, starter maintenance (~$800/yr).
  # Member food-access donations and nutrition-education ingredients (~$1,000/yr).
  # Surplus absorbed by community food programs; total consumables ~$9,500/yr.
  # [CITATION-NEEDED: commodity bread flour pricing; packaging materials costs;
  # label: inferred.]

  floor_space_rent_per_year: 0
  # Per spec requirement. Town-owned facility; floor space imputed at $0.
  # Civic ownership eliminates rent as an operating cost. The full building
  # capital is amortized in the town's broader civic facility budget, not in
  # this bakery-module entry. This is the defining cost advantage of the civic
  # model over private or cooperative operators who must pay market rent
  # (~$4,000-8,000/yr for comparable commercial kitchen space at town scale).

  market_price_per_unit: { low: 0, mid: 0, high: 0 }
  # Per spec requirement: zero commercial pricing; civic operation.
  # The facility does not sell output at market prices. Community access is
  # provided as a civic service; any nominal bread sales (e.g., at community
  # events or food-program partnerships) are priced at cost or donated, not
  # at market-clearing artisan prices. Member access fees ($30-60/yr) are
  # civic access charges comparable to a library card, not unit prices.
  # See pricing_notes for full civic context.

  pricing_notes: >-
    This is a civic food-access and training facility, not a commercial bakery.
    market_price_per_unit is set to zero because the facility does not operate
    as a commercial producer: bread produced by the instructor and members is
    distributed through community food-access channels (food pantries, nutrition
    education programs, neighborhood events) or consumed by members as part of
    their training, not sold at artisan market rates. The industrial baseline
    price ($3.00 per 800g supermarket sourdough loaf equivalent [CITATION-NEEDED:
    US supermarket sourdough shelf pricing survey, 2024]) is cited for reference
    only — to document the community value delivered relative to market cost of
    equivalent product — not as a revenue or premium argument. Annual member
    access fees ($30-60/yr) are a minimal civic-access charge, not per-unit
    output pricing.

  industrial_baseline_price: 3
  # 800g supermarket sourdough loaf equivalent (Sara Lee, Pepperidge Farm,
  # or major private-label). Cited for civic-value reference only; not used
  # in revenue calculations (lens_fit.market: poor).
  # [CITATION-NEEDED: US supermarket sourdough bread shelf pricing, 2024;
  # illustrative estimate from market observation; label: inferred.]

  pricing_validation: >-
    N/A — civic operation with no commercial output pricing. Member access fees
    are civic access charges, not unit prices. Industrial baseline cited for
    community-value reference comparison only; evidence type is commodity
    retail-shelf pricing observation [CITATION-NEEDED]. No market-price claim
    is made; pricing_validation is not applicable per catalog/SCHEMA.md §3
    (pricing_validation required only when market_price_per_unit is present
    with non-zero values; zero-priced civic entries cite industrial_baseline
    for reference framing only).

# ── TRADE-SPECIFIC FIELDS ────────────────────────────────────────────────────

trade_specific:
  flour_source_declaration: industrial-flour-purchased
  # Per baking SCHEMA.md §4 required field and DECLINE-VERDICT mill-dependency
  # falsifier. Base configuration purchases commodity or specialty bread flour
  # from an industrial mill or regional food-service distributor. No mill
  # infrastructure is owned or operated; no direct farm relationship assumed.
  # Civic facility rationale: the base civic model is intentionally low-complexity
  # in supply chain — the facility's distinctive value is food-access and training,
  # not grain-sourcing differentiation. A local-mill-partnership upgrade is noted
  # as a potential Phase 2 enhancement (see Key Assumptions) consistent with the
  # spec's "potential local-mill-partnership upgrade later" annotation, but the
  # base entry does not require or assume it.
  # Supply-chain risk: commodity flour price volatility (wheat market exposure);
  # distributor availability disruption. Partially mitigated by civic purchasing
  # power (municipal procurement contracts may secure better pricing and
  # supply continuity than a single private operator).
  # See Key Assumptions for full flour sourcing discussion.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Deck heating element (electric) — one of two decks"
      estimated_hours_to_failure: 2000
      replacement_cost: 650
      replacement_lead_time_days: 14
      serviceable_by: specialist
      # Two-deck unit: element failure on one deck does not halt facility
      # operation (second deck remains functional), but reduces daily output
      # and disrupts member-session scheduling. 2,000 hr to failure at ~5
      # active bake-hours/day × 260 days/yr = 1,300 hr/yr — likely to
      # trigger in year 1-2. Specialist replacement required per baking
      # SCHEMA.md §5 reference list.
      # [Baking SCHEMA.md §5 deck element 1,500-3,000 hr range; label: inferred.]

    - item: "Oven door seal / gasket — deck unit"
      estimated_hours_to_failure: 1800
      replacement_cost: 120
      replacement_lead_time_days: 5
      serviceable_by: operator
      # Multi-user operation accelerates door gasket wear: members less
      # practiced at door handling introduce more thermal stress than a
      # single experienced operator. Door gasket degradation causes heat
      # loss and inconsistent bake. Operator-serviceable per baking
      # SCHEMA.md §5 reference list; 5-day regional supply lead time.
      # [Baking SCHEMA.md §5 door gasket 1,500-3,000 hr range; label: inferred.]

    - item: "Proofing cabinet heating element or thermostat"
      estimated_hours_to_failure: 2500
      replacement_cost: 200
      replacement_lead_time_days: 5
      serviceable_by: journeyman
      # Standard proofing cabinet element failure; per baking SCHEMA.md §5
      # reference list 1,000-2,500 hr typical. Multi-user demand on the
      # proofer (parallel member and instructor proof cycles) may accelerate
      # failure toward lower end of range. Journeyman-level replacement.
      # [Baking SCHEMA.md §5 proofer element range; label: inferred.]

  maintenance_schedule:
    daily:
      task: "Feed sourdough starter(s); clean both deck surfaces, door seals, and oven interiors; clean mixer bowl and hook; reset member workstations; log instructor and member production output; wipe proofing cabinet interior; complete member session sign-in log"
      performed_by: operator
      # 'Operator' here = the journeyman baker-instructor or designated opening
      # staff. Multi-user facility requires thorough daily reset of all shared
      # surfaces; health-department standards apply to community food production.
    weekly:
      task: "Deep-clean both oven decks and exhaust hood filter; calibrate proofing cabinet temperature and humidity; inspect mixer motor base; inventory and restock member tooling (bannetons, lames, bench scrapers); review session sign-in log for anomalies; replenish sourdough starter supply for member use"
      performed_by: operator
    quarterly:
      task: "Professional exhaust hood and grease-trap service (health-code requirement); full deck element and thermostat inspection; proofing cabinet professional calibration; mixer motor inspection and lubrication; full member-equipment inventory and replacement assessment; facility committee usage review"
      performed_by: journeyman
    annual:
      task: "Full deck oven professional service (element test, seal replacement, thermostat calibration, structural inspection); health department commercial kitchen inspection and license renewal; proofing cabinet and mixer professional overhaul; full civic facility inspection per town facilities protocol; insurance assessment update"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 55
  # Civic multi-user model overhead is higher than single-operator commercial
  # entry: (1) oven preheat from cold — two-deck electric requires 35-45 min
  # warm-up time from cold start; (2) member session check-in, orientation
  # review for new members, and safety sign-off (~10 min per operating session);
  # (3) end-of-day equipment shutdown, sourdough maintenance, surface sanitization,
  # and log completion (~15 min). Total per operating day: ~55 min.
  # Subtracted from max_active_hours_per_week in sim_params throughput derivation.
  # [Structural inference from two-deck oven warm-up requirements and civic
  # facility operating protocols; baking SCHEMA.md §2 electric-deck notes; label: inferred.]

  max_active_hours_realism_note: >-
    32 hr/wk is the gross ceiling for civic scheduling. Net of 55 min/day
    overhead on a 5-operating-day week: 55 min × 5 days / 60 = 4.6 hr/wk
    non-productive overhead, leaving approximately 27.4 hr/wk net active
    production and instruction time. Civic scheduling adds further reduction:
    public holidays, member no-shows, community-event prep, and administrative
    tasks account for an additional ~10% effective reduction beyond the mechanical
    overhead, folded into the downtime_fraction of 0.13. sim_params uses the
    derated figure (~27 hr/wk effective) for throughput derivation.

  interruption_notes: >-
    Civic multi-user setting introduces intraday interruptions structurally higher
    than single-operator production: member skill-check pauses (~5-8 min per
    member per session), dough-stage coordination between instructor and member
    decks (~5 min per handoff), safety and hygiene coaching (~5-10 min/session),
    session documentation and food-program donation staging (~10 min/session).
    Total typical intraday interruption: 25-40 min per operating session.
    Folded into throughput_units_equiv_per_year via the loaves-per-day figure
    and operating-day assumption rather than as a separate downtime component.

  consumables_lead_time_days: { typical: 3, worst: 21 }
  # Typical: commodity bread flour and packaging from regional food-service
  # distributor within 3 days at town scale per SCALES.md §6 infrastructure
  # baseline. Worst: specialty flour (heritage wheat, cultural specialty grains)
  # from smaller regional mills may require 14-21 days. Civic purchasing power
  # (municipal procurement contract) may improve typical lead time vs. private
  # operator; distributor network resilience is moderate at town scale.
  # [SCALES.md §6; label: inferred.]

  throughput_variance:
    seasonal: "School-year alignment boosts nutrition-education program demand September-June; summer community event uptick offset by reduced structured programming; January post-holiday slowdown most pronounced"
    worst_month_fraction_of_average: 0.60
    best_month_fraction_of_average: 1.35

  operator_impact:
    noise_db: 58
    # Electric deck oven and proofing cabinet: low ambient sound (~40-50 dB).
    # Commercial spiral mixer during mixing cycles: ~65-70 dB intermittent.
    # Member activity (conversation, dough handling) adds ambient; estimated
    # 55-62 dB(A) average at instructor position. Well below OSHA 90 dB(A) PEL.
    # [CITATION-NEEDED: sound level measurement at instructor position in
    # community bakery; OSHA 29 CFR 1910.95 PEL: 90 dB(A) for 8-hr shift;
    # illustrative estimate; label: inferred.]
    heat_exposure: "Elevated ambient near deck ovens during baking cycles (deck surface 230-260°C; ambient near oven 28-35°C); manageable with kitchen exhaust hood and 2.8 m ceiling; instructor and member rotation to cool prep areas during bake windows reduces sustained exposure; two-deck layout permits thermal zoning"
    emissions: "Near-zero combustion emissions from electric deck; steam and flour dust are the primary occupational exposures; kitchen exhaust hood manages steam; flour dust requires PPE (dust mask) per OSHA flour-dust guidelines during extended mixing; member orientation must include PPE instruction"
    physical_demand: "Moderate; sustained standing for instructor role (6+ hr/session); repetitive shaping instruction and demonstration; oven loading/unloading with peel (10-15 kg dough batches); instructor must also perform real-time supervision across two member workstations — moderate cognitive and physical multitasking demand"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Town-owned civic facility in institutional or municipal zoning; commercial food production in a public building requires health-department commercial kitchen licensing regardless of civic ownership; confirm local ordinance on public-building food production; accessibility compliance (ADA or equivalent) applies to community member workstations"
  emissions: "No combustion emissions permit required for electric deck; kitchen exhaust hood requires building permit and inspection; flour-dust occupational exposure governed by OSHA 29 CFR 1910.1000 Table Z-1; food-program donation activity (food bank supply) may require additional health department approval depending on jurisdiction"
  other: "Commercial food handler certification required for instructor (and for any member selling or donating product); health department commercial kitchen license required; HACCP plan required if output donated to food banks or institutional food programs; member access agreement (liability waiver) required — town counsel review needed before opening; food safety training for members should be part of orientation curriculum"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: poor
  # Civic operation with zero commercial output pricing. The facility does not
  # compete on market terms, does not sell output commercially, and has no
  # revenue stream that would support a market-lens evaluation.
  cooperative: good
  # Member-access model layered on civic ownership creates cooperative-analogous
  # governance. Ostrom principles 1-6 addressed through documented bylaws,
  # sign-in monitoring, graduated sanctions, and member amendment process.
  # The legal form is municipal (not a registered cooperative), but the operating
  # model functions cooperatively with schedule-booked shifts per spec requirement.
  civic: good
  # Primary lens per spec requirement. Municipal ownership, library-model access,
  # substantive food-security and training externalities, and political coalition
  # fully documented in lens_context.civic below.

scale_fit:
  village: poor
  # Capital requirement ($80,000 mid) and staffing cost (~$52-56k/yr journeyman-
  # instructor) are disproportionate at village scale (500-2,000 residents);
  # per-household cost would exceed political tolerance at village scale
  # (~$66-85/hh/yr before amortization at 400 households, vs $120 village
  # threshold). Scheduling demand insufficient to justify FT journeyman-instructor.
  town: good
  # Target scale per spec. 2,000-15,000 residents (3,000 typical households at
  # town midpoint). Per-household cost at ~$24-28/hh/yr is well within the $100
  # town civic threshold. Sufficient scheduling demand to sustain 32 hr/wk
  # operation and support the staffing model. Political coalition viable.
  small_city: good
  # Per-household cost falls to ~$5-7/hh/yr at small-city scale (16,000 hh) —
  # well below $80 threshold. Scheduling demand may support extended hours;
  # multiple staff positions become viable. Governance rules transfer directly.

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:

  cooperative:
    membership_boundary: >-
      Town residents and immediate township equivalents; access granted via
      library-card equivalent credential (town residency verification plus
      food-handler orientation completion). Non-residents may join at a higher
      fee tier ($60/yr vs $30/yr resident rate) subject to session-slot
      availability. Open to all ages with standard adjustments: under-18
      requires parental consent and additional supervision confirmation;
      no demographic restriction beyond residency and safety-orientation
      completion. Geographic scope calibrated to town scale; commuter
      access (within 10-mile radius) permitted at non-resident rate.

    rules_source: >-
      Posted facility bylaws adopted by the bakery facility committee
      (a standing subcommittee of the town library board or recreation
      department). Bylaws govern: session booking protocol (advance online
      or phone reservation required; walk-in subject to availability),
      member skill-tier certification (basic orientation → certified member →
      advanced member eligible for independent session), food-safety requirements
      (food handler certification required before supervised production),
      equipment responsibility and damage liability, starter-culture access
      rights, and member dues schedule. Rules displayed in facility and
      published on town website.

    monitoring: >-
      Mandatory sign-in log for every session (member ID, date, session type,
      bake output, instructor sign-off); instructor observation during all
      operating hours (journeyman baker-instructor present at all times by
      policy); monthly facility-committee review of usage logs and production
      records; food-program donation tracking maintained and reviewed quarterly
      by facility committee and public health liaison; equipment temperature
      calibration logs reviewed weekly.

    graduated_sanctions: >-
      First incident (cleaning failure, booking no-show without notice,
      equipment misuse): verbal warning logged in member record; mandatory
      re-orientation on kitchen protocols.
      Second incident within 12 months: written notice plus 30-day booking
      suspension and $30 fine.
      Third incident within 24 months: membership review by facility committee;
      possible termination with pro-rated dues refund.
      Food safety violation (hygiene breach, contamination risk): immediate
      session suspension pending instructor review; may escalate directly to
      membership review regardless of prior incident history.
      Per Ostrom Principle 5.

    conflict_resolution: >-
      Day-to-day disputes resolved by journeyman baker-instructor as floor
      authority. Member-vs-member disputes and appeals of instructor decisions
      escalated to facility committee (3-5 members drawn from library board
      or recreation department); facility-committee decisions are final subject
      to town board appeal. Resolution meeting required within 14 days of
      formal written complaint. Per Ostrom Principle 6.

    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6]
    # Principle 1 (clear boundaries): residency-based membership with
    #   documented eligibility criteria and food-handler certification gate.
    # Principle 2 (congruence): rules calibrated to civic food-production
    #   context (supervised use, food safety requirements, not autonomous
    #   commons management).
    # Principle 3 (collective choice): bylaw amendment process below.
    # Principle 4 (monitoring): sign-in logs, production records, usage reports.
    # Principle 5 (graduated sanctions): documented above.
    # Principle 6 (conflict resolution): facility-committee mechanism above.
    # Principles 7-8 (nested/external recognition): municipal ownership provides
    #   external recognition (Principle 8 analog); nesting into town governance
    #   structure satisfies Principle 7. Not via member self-governance but
    #   via civic umbrella — acceptable and structurally stronger for a
    #   municipally-owned commons.

    member_amendment_process: >-
      2/3 vote of active members at annual facility-review meeting (held
      concurrently with or adjacent to town library board annual meeting);
      30-day advance notice to all members required before any bylaw amendment
      vote. Emergency amendments (food-safety, health-code compliance) may be
      enacted by facility committee with 7-day notice and ratified at next
      member meeting. Town board retains override authority on budget-related
      rule changes.

    legal_form: >-
      Municipal operation under town government authority (not a registered
      cooperative entity). The member-user governance layer operates within
      civic ownership: the town holds title and operational authority; the
      facility committee provides member-facing governance and policy oversight.
      This structure satisfies Ostrom Principle 7 analog (external recognition)
      via municipal charter and budget-line accountability rather than by
      cooperative registration. Municipal legal form provides stronger liability
      protection for food-production activities than an unincorporated cooperative.

    scale_fit_note: >-
      Governance rules calibrated for town scale (2,000-15,000 residents).
      Minimum viable active member population: approximately 20-40 regular
      members to fill 32 hr/wk of scheduled session slots (2 members per
      session × ~5 sessions/day × 5 days/wk = 50 member-session slots per
      week; realistic fill rate 40-60% = 20-30 regular members needed).
      At village scale, member population and scheduling demand both fall
      below minimum viable threshold for this governance structure. At
      small-city scale, governance transfers directly; staff complement
      may expand to accommodate higher demand.

  civic:
    political_coalition: >-
      Food-equity advocates and neighborhood food-security coalitions (primary:
      food-desert remediation argument; aligns with public health department
      priorities); library board (operational home and philosophical alignment
      with library-model access; libraries and neighborhood bakeries share the
      access-as-public-good framing); workforce-development board (apprentice
      training pipeline; grant-funding alignment with state and federal
      workforce programs); public health department (nutrition education;
      food-security for under-served neighborhoods; anti-hunger program support).
      Secondary coalition partners: K-12 school district (nutrition education
      curriculum partnership; student apprenticeship exposure); emergency-
      management office (food-resilience argument); cultural organizations
      (cultural baking traditions preservation; immigrant and heritage community
      engagement); faith communities (food-donation network alignment).

    council_vote_estimate: >-
      5-2 favorable in towns with documented food-insecurity or food-desert
      conditions and an active library board; 4-3 marginal in budget-conservative
      councils where the capital ask ($80,000 mid) and staffing cost (~$52-56k/yr)
      trigger fiscal-responsibility opposition. Primary opposition argument:
      "municipal government entering the food-production business" — countered by
      the library-model framing (civic access service, not commercial competition).
      Secondary opposition: health department liability exposure and commercial
      kitchen compliance costs. Swing vote typically held by a fiscal-moderate
      council member; the benchmark comparison (~$24/hh/yr vs library at ~$40-55/hh/yr)
      is the most effective counter-argument. Food-equity framing with documented
      neighborhood food-access gap is a decisive coalition asset.

    competes_with_private: >-
      The civic neighborhood bakery is structurally complementary to, not
      competitive with, private artisan bakeries. The facility does not sell
      output commercially, does not accept production contracts at market
      rates, and explicitly refers commercial custom work to private operators.
      Its apprentice training pipeline supplies future journeyman bakers to
      the regional labor market, including private bakeries. In neighborhoods
      where no private artisan bakery operates — the common case in under-served
      town neighborhoods and food-desert areas — the civic facility provides
      access to quality bread and baking education that the market has declined
      to supply. In neighborhoods where private bakeries operate, the civic
      facility targets a different customer segment (food-access, training,
      community nutrition) not served by premium artisan pricing. The "competing
      with private bakeries" council-opposition argument fails: a civic food-
      access facility providing free or low-cost community bread is not competing
      with a $10/loaf artisan shop any more than a public library competes with
      a bookstore.

    governance_form: >-
      Town-owned; operated under town library system, recreation department,
      or community services department (whichever has existing facility-management
      capacity and community-access program infrastructure). Journeyman baker-
      instructor is a town employee or long-term contractor. Facility committee
      (3-5 members, appointed by library board or recreation director with
      community representation) sets operating policy within town-approved
      bylaws. Annual budget line reviewed by town council. Food-program
      partnerships managed through public health department liaison.

    budget_line: >-
      Capital: one-time appropriation or 20-25 year general-obligation bond
      (~$3,200-4,000/yr amortized at mid-capital + install cost of $88,000
      over 25 yr at 4% municipal rate). Operating: ~$65,000-72,000/yr gross
      covering staffing ($52,000-56,000/yr journeyman-instructor + ~$5,000
      part-time admin/apprentice stipend), annual maintenance ($2,800),
      consumables ($9,500), and administration/program (~$2,000); gross
      operating ~$70,300/yr mid. Revenue offsets: member access fees
      (~$1,500-3,000/yr at 50-100 active members × $30-60/yr), workforce-
      development grants ($5,000-15,000/yr), food-security program grants
      ($5,000-20,000/yr), and community foundation support (~$2,000-5,000/yr);
      total offsets ~$15,000-40,000/yr. Net municipal cost after offsets:
      ~$30,000-55,000/yr mid-case. Budget line: community services, library,
      or public-health capital and operating accounts. Civic food-security
      programs qualify for USDA Community Food Projects Competitive Grant
      Program and SNAP-Ed funding in many jurisdictions.
      [CITATION-NEEDED: grant availability and typical award amounts for
      civic community bakery and food-access programs; USDA CFPCGP and
      SNAP-Ed funding ranges; label: inferred.]

    benchmark_comparison: >-
      At town scale (3,000 households as representative mid-point per SCALES.md
      §2 town midpoint): gross annual operating cost ~$70,300/yr ÷ 3,000 hh
      = ~$23.43/hh/yr gross; net municipal cost after offsets (~$40,000/yr
      mid-case) ≈ $13.33/hh/yr net operating. Amortized capital: $88,000 ÷
      25 yr ÷ 3,000 hh = ~$1.17/hh/yr. All-in net municipal cost: ~$14-16/hh/yr.

      Benchmark comparisons: IMLS Public Library Survey FY 2021 reports
      national median library operating expenditure per capita ~$40-55, equating
      to ~$100-138/hh/yr at 2.5 persons/household [corpus/program/SCALES.md
      §4.2 library per-capita benchmark]. Town recreation center: ~$45-80/hh/yr
      [SCALES.md §4.2]. Food bank / community meal program per-household cost
      in comparable town-scale programs: ~$20-40/hh/yr [CITATION-NEEDED:
      per-household cost data for food-bank or community meal programs in towns
      of 2,000-15,000 population; Feeding America network data or local food
      bank annual reports would be appropriate verification].

      The civic neighborhood bakery at ~$14-16/hh/yr net municipal cost is:
      approximately one-fifth of public library cost; comparable to or below
      food-bank per-household cost while providing food-production capacity and
      skills training the food-bank model does not; and well within the $100/hh/yr
      civic lens pass threshold for town scale. Per-household cost argument is
      the primary political-viability tool for council votes.

    staffing_model:
      role: "1 journeyman baker-instructor (town employee or contractor) + 1 part-time apprentice or program assistant (~15-20 hr/wk)"
      operator_fte: 1.4
      # 1.0 FTE journeyman-instructor + 0.4 FTE part-time apprentice/assistant
      # (15-20 hr/wk). Apprentice position is the civic training investment —
      # a paid or stipended position consistent with workforce-development
      # program funding models.
      wage_assumption: 54000
      # Journeyman baker-instructor: $52,000-56,000/yr per spec requirement.
      # $54,000 is the mid-point. Per corpus/program/SCALES.md §3: town-scale
      # median wage threshold for skilled trades is $56,000/yr; $54,000 is
      # slightly below this threshold, consistent with a civic/nonprofit
      # employment context where non-wage benefits (stability, mission alignment,
      # civic employer status) partially compensate for below-market cash wage.
      # [corpus/program/SCALES.md §3 town-scale skilled-trades median]
      wage_source: "corpus/program/SCALES.md §3 town-scale skilled-trades median; per spec requirement $52-56k/yr for journeyman baker-instructor at town scale"
      hours: "40 hr/wk (instructor: production supervision, member instruction, food-program coordination, curriculum development, admin); 15-20 hr/wk (apprentice/assistant: session support, food-program logistics, maintenance assistance)"
      hiring_notes: >-
        Journeyman baker with teaching or community-education experience is the
        ideal hire; this profile is uncommon in most regional labor markets. The
        hiring pool is regional (50-100 mile radius) and may require active
        outreach to culinary programs, food-service industry networks, and
        workforce-development organizations. $54,000/yr is at the low end of
        journeyman-baker market wages in most US regions [CITATION-NEEDED:
        BLS Occupational Employment and Wage Statistics for Bakers (SOC 51-3011),
        2024]; the civic employer advantages (stability, benefits, mission) are
        necessary to close the compensation gap. The apprentice/assistant position
        can be filled from the local workforce-development pipeline; culinary
        program graduates, food-service workers seeking advancement, or community
        members completing the facility's own training program are viable sources.

    civic_externalities:
      - "Food security in under-served neighborhoods: provides reliable access to quality baked bread in food-desert or food-insecure neighborhoods where market-rate artisan bakeries do not operate and supermarket access is limited; bread distribution through food-pantry and community-meal partnerships addresses a documented nutritional gap the market and existing food-access programs do not fully fill"
      - "Apprentice training pipeline: structured 36-42 month program produces 1-2 journeyman bakers per cycle from the local community workforce, supplying regional food-service employers, food-access organizations, and community institutions who cannot sustain their own apprenticeship programs; reduces dependence on labor-market imports for a foundational food-production skill"
      - "Cultural baking traditions preservation: supervised facility provides the physical space, equipment, and instructor expertise for community members to practice, document, and transmit heritage baking traditions (cultural breads, traditional fermented products, immigrant-community specialty items) that cannot be maintained in home kitchens at adequate scale or food-safety compliance levels; non-excludable cultural-continuity externality the market systematically undervalues"
      - "Nutrition education and food literacy: structured community programming (baking classes, nutrition workshops, school partnerships) increases household food literacy — understanding of fermentation, ingredient composition, and home baking — reducing dependence on ultra-processed products; nutrition education externality is well-documented in public health literature as a long-run health-cost reducer that the market does not price"
      - "Community gathering and social cohesion: the civic bakery functions as a neighborhood institution that generates the social-fabric externalities Jane Jacobs identified in civic infrastructure — incidental social contact, intergenerational skill exchange, and community identity formation around a shared food-production practice; these externalities are real, documented in community-cohesion literature, and not priced by any market mechanism"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 80000
  # Equals economics.capital_cost.mid per E3-R1.
  # [Derived from economics.capital_cost above]

  cost_sd: 21250
  # Derived: (capital_cost.high - capital_cost.low) / 4 = (130,000 - 45,000) / 4
  # = $21,250. E3-R5 ratio: 21,250 / 80,000 = 0.266; within 0.15-0.50 range.
  # [Derived per catalog/SCHEMA.md §3 default; E3-R5 compliance confirmed]

  throughput_units_equiv_per_year: 17500
  # Derivation (explicit per baking SCHEMA.md §1 E-3 guidance):
  # Unit: 800g sourdough boule equivalent (see Key Assumptions).
  # Step 1 — annual operating days:
  #   5 operating days/wk × 52 wk - civic closure days (~10-15/yr) = 250 days/yr.
  # Step 2 — loaves per operating day (gross):
  #   throughput.loaves_per_day = 80 loaves/day.
  # Step 3 — apply downtime fraction:
  #   80 loaves/day × 250 days/yr × (1 - 0.13 downtime) = 80 × 250 × 0.87
  #   = 17,400 loaves/yr → rounded to 17,500.
  # E3-R2 cross-check via active-hours method:
  #   max_active_hours_per_week (32) × 52 wk × (1 - 0.13) = 1,446 hr/yr gross.
  #   Net of 55 min/day overhead × 250 days / 60 = 229 overhead hr/yr:
  #   Net active hr/yr: 1,446 - 229 ≈ 1,217 hr/yr.
  #   At 80 loaves/day ÷ ~5.5 effective hr/day ≈ 14.5 loaves/hr;
  #   1,217 hr × 14.5 loaves/hr ≈ 17,647 — consistent with 17,500; within P2 threshold.
  # [Derived from throughput fields, operating-day assumption, and downtime_fraction above]

  variable_cost_per_unit: 0.54
  # Flour + packaging + energy per loaf-equivalent:
  # Consumables: $9,500/yr ÷ 17,500 loaves = $0.543/loaf.
  # (Flour dominates: ~0.7 kg/loaf × $0.60/kg = $0.42/loaf within consumables figure.)
  # Energy: 9 kWh/hr × 1,446 hr/yr × $0.125/kWh = $1,627/yr ÷ 17,500
  #   = $0.093/loaf; but energy is partially covered by utility budget, not
  #   consumables. Total variable including energy: ($9,500 + $1,627) / 17,500
  #   = $11,127 / 17,500 = $0.636/loaf; using $0.54 which reflects consumables
  #   only per the field definition (energy is a separate operating cost line
  #   in civic budget, not per-unit consumable).
  # [Derived from annual_consumables and throughput_units_equiv_per_year above;
  # electricity rate from US EIA Electric Power Monthly Table 5.3, 2023-2024
  # blended small-commercial rate $0.10-$0.15/kWh; midpoint $0.125 used per
  # SCALES.md §6 footnote]

  labor_hours_per_unit: 0.083
  # Instructor hours per loaf-equivalent:
  # Net active hours/yr (1,217) ÷ throughput_units_equiv_per_year (17,500)
  # ≈ 0.0696 hr/loaf (instructor direct production time only).
  # Including apprentice/assistant pro-rated contribution (~0.4 FTE × 1,446 hr
  # = 578 hr/yr total; shared across production and program work):
  # Production-attributable assistant hrs: ~250 hr/yr ÷ 17,500 = 0.014 hr/loaf.
  # Combined: ~0.070 + 0.014 = 0.083 hr/loaf.
  # E3-R3 cross-check: 17,500 × 0.083 = 1,453 hr/yr; target = 32 × 52 × 0.87
  # = 1,447 hr/yr. Discrepancy = 6 hr (0.4%); within P2 threshold.
  # [Derived from throughput_units_equiv_per_year and active-hours calculation above]

  downtime_fraction: 0.13
  # Sources: deck element failure on one deck (~2,000 hr to failure; partial
  # downtime of ~50% while other deck operational, plus 14-day lead time for
  # specialist repair = ~1.5 weeks effective downtime = ~3-4% when one deck
  # fails and second deck carries reduced load); door gasket replacement
  # (5-day lead, operator-serviceable, ~1% downtime); proofing cabinet element
  # (~2,500 hr, journeyman-level, 5-day lead ~1% downtime); civic administrative
  # and scheduling gaps (public holidays, community events, staff absence ~5-6%);
  # routine maintenance shutdowns (~2%). Total: ~13%.
  # Consistent with E3-R6: deck element partial failure contributes 3-4%
  # (not full shutdown since two decks), within 13% total.
  # [Derived from operations_reality.first_year_failures above; SCALES.md §2
  # civic scheduling pattern; label: inferred]

  lifespan_years: 20
  # Commercial two-deck electric oven: ~15,000-20,000 operating hours rated;
  # at ~5 hr/day × 250 days/yr = 1,250 hr/yr, 15,000 hr = ~12 years to first
  # major refurbishment; with professional service at year 10-12, full design
  # life of 18-22 years is achievable. 20-year horizon is a conservative civic
  # infrastructure estimate; aligns with municipal facility planning cycles.
  # Shorter than smithing forge entries (masonry or structural steel rated for
  # 25 years) due to electromechanical component density.
  # [CITATION-NEEDED: service life data for commercial two-deck electric ovens;
  # manufacturer specification; label: inferred]

  annual_public_use_hours: 8320
  # REQUIRED: civic lens utilization diagnostic input per Plan E civic-lens
  # diagnostic fix. Computed as facility open hours × concurrent users:
  # facility_hours = max_active_hours_per_week × 52 = 32 × 52 = 1,664 hr/yr.
  # concurrent_users = 5 (1 journeyman instructor + up to 2 members +
  # 1 apprentice/assistant + ~1 average additional community participant
  # in nutrition education / observation sessions that accompany regular
  # baking sessions; conservative estimate of 5 average concurrent persons).
  # annual_public_use_hours = 1,664 × 5 = 8,320 person-hours/yr.
  # At town scale (7,500 residents), this delivers:
  # 8,320 ÷ 7,500 = 1.11 hr/capita/yr. Well above the typical specialized
  # civic facility lower threshold of 0.15 hr/capita/yr (per forge-004 precedent
  # using usage_rate_threshold: 0.15 for specialized supervised facilities).
  # The civic neighborhood bakery serves a somewhat broader audience than a forge
  # (food is universally accessible; metalworking is a specialist activity);
  # 1.11 hr/capita/yr is consistent with a modestly utilized civic food facility.
  # [Derived from max_active_hours_per_week, operating weeks, and concurrent
  # user count; concurrent user estimate is conservative — actual nutrition
  # education sessions may bring group sizes of 8-15; this estimate uses 5
  # average including non-baking program participants]

  usage_rate_threshold: 0.15
  # Specialized civic facility lower threshold per ECONOMIC-LENSES.md §4.3
  # (specialized-equipment exception with documented rationale).
  # Rationale: The civic neighborhood bakery is a supervised, food-safety-gated
  # facility with 2 member workstations and an instructor station; it cannot
  # simultaneously serve more than ~5-8 persons regardless of demand. The 2.0
  # hr/capita default is calibrated for high-traffic open-access facilities
  # (libraries, recreation centers). A civic bakery with supervised sessions
  # has structural throughput limits analogous to a civic forge; the 0.15
  # hr/capita threshold preserves the civic-lens pass for a facility providing
  # meaningful access at 1.11 hr/capita/yr (town scale) and 0.21 hr/capita/yr
  # (small_city scale).

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
    primary_metric: 84.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=84, total_annual_cost=16700
  village_civic:
    verdict: win
    primary_metric: 31.64
    metric_name: per_household_cost
    notes: per_hh=31.64, threshold=120, hrs/capita=6.656 vs threshold=0.15
  town_market:
    verdict: fail
    primary_metric: -1.0
    metric_name: payback_years
    notes: market_price_per_unit absent or zero; entry not designed for market lens
  town_coop:
    verdict: win
    primary_metric: 84.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=84, total_annual_cost=16700
  town_civic:
    verdict: win
    primary_metric: 4.652941176470589
    metric_name: per_household_cost
    notes: per_hh=4.65, threshold=100, hrs/capita=0.979 vs threshold=0.15
  small_city_market:
    verdict: fail
    primary_metric: -1.0
    metric_name: payback_years
    notes: market_price_per_unit absent or zero; entry not designed for market lens
  small_city_coop:
    verdict: win
    primary_metric: 84.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=84, total_annual_cost=16700
  small_city_civic:
    verdict: win
    primary_metric: 0.8788888888888889
    metric_name: per_household_cost
    notes: per_hh=0.88, threshold=80, hrs/capita=0.185 vs threshold=0.15
sources:
  - ref: "corpus/program/SCALES.md §2 — town scale parameters; household count multiplier (0.40); civic cost threshold $100/hh/yr at town scale"
  - ref: "corpus/program/SCALES.md §3 — town-scale skilled-trades median wage $56,000/yr; journeyman baker-instructor wage reference at $52-56k/yr per spec requirement"
  - ref: "corpus/program/SCALES.md §4.2 — public library per-capita operating cost benchmark; IMLS Public Library Survey FY 2021 national median $40-55/capita (~$100-138/hh/yr)"
  - ref: "catalog/baking/SCHEMA.md v1.0 §1 — throughput block structure; loaves/day ranges; E-3 cross-check guidance; baking schema base"
  - ref: "catalog/baking/SCHEMA.md v1.0 §2 — electric-deck energy consumption 3-8 kWh/batch; temperature ceiling 230-290°C; thermostat control capability"
  - ref: "catalog/baking/SCHEMA.md v1.0 §3 — journeyman-baker skill definition; sourdough cycle capability; apprentice supervision capability"
  - ref: "catalog/baking/SCHEMA.md v1.0 §4 — flour_source_declaration required field; industrial-flour-purchased supply chain risk and capital implications"
  - ref: "catalog/baking/SCHEMA.md v1.0 §5 — first_year_failures reference list; deck element 1,500-3,000 hr; door gasket 1,500-3,000 hr; proofer element 1,000-2,500 hr"
  - ref: "catalog/baking/SCHEMA.md v1.0 §6 Group C — civic/cooperative entries guidance; lens_context.civic.benchmark_comparison must name food-access program; staffing_model must cite public-sector wages"
  - ref: "catalog/baking/DECLINE-VERDICT.md — niche targeting; mill-dependency falsifier; civic community bakery as restorable civic-primary niche"
  - ref: "catalog/smithing/entries/004-community-civic-makerspace.md — civic lens precedent; annual_public_use_hours derivation methodology; usage_rate_threshold 0.15 for specialized civic facilities; library-model governance structure"
  - ref: "Ostrom, Elinor. 1990. Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press. (Chapters 2-3: eight design principles for commons governance; graduated sanctions; conflict resolution mechanisms)"
  - ref: "US Energy Information Administration. Electric Power Monthly, Table 5.3: Average Retail Price of Electricity. Monthly release. https://www.eia.gov/electricity/monthly/ (small-commercial blended rate 2023-2024: $0.10-$0.15/kWh; midpoint $0.125 used)"
  - ref: "OSHA 29 CFR 1910.1000 Table Z-1. Air Contaminants. (Flour dust permissible exposure limit; applicable to commercial baking and community bakery operations)"
  - ref: "OSHA 29 CFR 1910.95. Occupational noise exposure. (90 dB(A) PEL for 8-hour shift; civic bakery ambient noise well below threshold)"
  - ref: "Jacobs, Jane. 1961. The Death and Life of Great American Cities. Random House. (Civic infrastructure as neighborhood resilience and social cohesion anchor; public-goods framing for non-commercial community services; social-fabric externalities of civic institutions)"
  - ref: "Institute of Museum and Library Services. Public Library Survey, FY 2021. Published 2023. https://www.imls.gov/research-evaluation/data-collection/public-libraries-survey (per-capita library operating expenditure; benchmark for civic facility per-household cost comparison)"
  - ref: "[CITATION-NEEDED: capital cost data for commercial two-deck electric ovens, 2024-2026; Bongard, Sveba-Dahlen, Mono Equipment, Revent, or equivalent commercial bakery equipment supplier vendor catalogs]"
  - ref: "[CITATION-NEEDED: installation cost for commercial two-deck bakery kitchen in civic facility; general commercial kitchen contractor cost ranges, 2024]"
  - ref: "[CITATION-NEEDED: annual maintenance cost data for community bakery operations; trade or operator survey, 2024]"
  - ref: "[CITATION-NEEDED: commodity bread flour pricing per kg at US wholesale distributor level (US Foodservice, Sysco, regional food co-op), 2024; USDA ERS wheat and flour price series]"
  - ref: "[CITATION-NEEDED: packaging material costs for community bakery at 80 loaves/day volume; trade supplier catalog data, 2024]"
  - ref: "[CITATION-NEEDED: BLS Occupational Employment and Wage Statistics, Baker (SOC 51-3011), 2024; journeyman baker wage range in US town-scale markets]"
  - ref: "[CITATION-NEEDED: grant availability and typical award amounts for civic community bakery and food-access programs; USDA Community Food Projects Competitive Grant Program; SNAP-Ed funding ranges; state workforce-development grant programs]"
  - ref: "[CITATION-NEEDED: per-household cost data for food-bank or community meal programs in towns of 2,000-15,000 population; Feeding America network data or local food bank annual reports]"
  - ref: "[CITATION-NEEDED: US supermarket sourdough bread shelf pricing survey, 2024; IRI or Nielsen retail-scanner data for sourdough bread category; Sara Lee / Pepperidge Farm equivalent pricing]"
  - ref: "[CITATION-NEEDED: service life data for commercial two-deck electric ovens; manufacturer specification or commercial kitchen equipment longevity survey]"
  - ref: "[CITATION-NEEDED: empirical throughput data for civic or community bakery model; operator financial data or community food program evaluation studies]"
  - ref: "[CITATION-NEEDED: French boulangerie sociale tradition — functional description of municipally-supported neighborhood bread access programs in France; academic or policy source on French bread access policy and boulangerie sociale historical precedents]"
---
## Summary

Bake-010 is a municipally-owned neighborhood bakery operating on the library-model of civic access: town residents book supervised baking sessions, participate in nutrition education programs, and receive access to quality bread produced by a journeyman baker-instructor — all at civic-service pricing rather than market rates. The facility houses a commercial two-deck electric oven, proofing cabinet, spiral mixer, and two supervised member workstations in approximately 52 m² of town-owned floor space. Its defining characteristic is its civic-primary orientation: the facility exists not to generate commercial revenue but to address food security in under-served neighborhoods, build a local apprentice pipeline for journeyman bakers, preserve cultural baking traditions, and provide nutrition education. It is the baking equivalent of forge-004 (Community Civic Makerspace), translated from metalworking to food production. The per-household municipal cost at town scale (~$14-16/hh/yr net) is approximately one-fifth of public library per-household cost and comparable to or below community meal program costs — making it politically viable at the town council level when the food-equity case is clearly presented.

## Design rationale

This entry solves a specific problem that no other baking catalog entry addresses: the case for public investment in a neighborhood bakery as civic food-access infrastructure. Entries bake-001 through bake-005 address market-primary operators; bake-006 through bake-009 address specialty confection niches; all presuppose a private revenue model. Bake-010 is the first entry that takes seriously the possibility that a town-owned, zero-commercial-pricing bakery is a legitimate use of municipal funds — not a romantic notion but a calculable per-household cost that compares favorably against established civic services. The electric-deck specification is deliberately civic rather than commercially optimal: it eliminates combustion permits and fuel storage, producing a cleaner regulatory profile for a public building while providing the thermostat-controlled temperature essential for safe supervised use by community members at varying skill levels. The library-model access structure (scheduled shifts, food-safety orientation required, graduated member certification) borrows directly from the forge-004 civic makerspace governance design and adapts it to food production's additional regulatory dimension (food handler certification, HACCP requirements, health-department oversight). The entry is distinct from bake-013 (Farm-to-Table Integrated Bakery) because bake-010 makes no grain-sourcing differentiation claim: the civic value proposition is food access, training, and community gathering, not ingredient provenance.

## Historical lineage

Three traditions inform this design, each requiring precise anti-romantic treatment.

**French boulangerie sociale tradition.** In France, municipal support for neighborhood bread access has a documented policy history: the boulangerie is considered by French food policy as a social infrastructure service, and in isolated or under-served communities, municipal subsidies have supported neighborhood bakeries that would not survive on market economics alone. [CITATION-NEEDED: academic or policy source on French boulangerie sociale history and municipal bread-access programs.] The functional inheritance to this entry is the concept of publicly supported neighborhood bread access as a food-security intervention — the idea that reliable, affordable access to quality bread is a community concern, not solely a market outcome. What this design explicitly does not inherit from the French model is the regulatory and cultural context that makes French bread policy viable: France has a national bread-quality law (décret pain), a strong cultural consensus on the value of artisan bread, and a regulatory structure that protects bakery trade norms in ways that have no US equivalent. The civic model here adapts the food-access principle without assuming French regulatory or cultural conditions.

**US public library model (Jane Jacobs civic-infrastructure framing).** The library-card access model, zero-rent civic ownership, benchmark comparison against library per-household costs, and the governance structure (municipal ownership + member-facing facility committee) are all inherited from the US public library tradition. Jane Jacobs's argument in *The Death and Life of Great American Cities* (1961) that civic infrastructure generates neighborhood resilience, social cohesion, and incidental contact that the market systematically under-provides is the functional frame for the civic_externalities block. The functional inheritance is the pricing model (access fee, not unit price), the governance form, and the public-goods justification structure. What this design does not inherit from the library model is any assumption that the facility can operate without food-safety oversight: a commercial bakery is not a library shelf, and the health-code compliance dimension requires more active management than book lending.

**Cooperative extension community kitchen programs.** The US Cooperative Extension System (land-grant university network) has operated community food production demonstration programs since the early twentieth century, including community canning, food preservation, and baking programs that brought supervised food production capacity to rural communities. The functional inheritance is the apprentice-instruction model (expert instructor + community participants learning in a supervised production environment), the nutrition education programming layer, and the workforce-development rationale for civic investment in food-production skills. What this design does not inherit from the cooperative extension model is its land-grant university institutional context: the civic neighborhood bakery is operated by the municipality, not a university extension office, and targets ongoing community access rather than periodic demonstration events. The apprentice training pipeline structure owes more to the Cooperative Extension model than to any purely commercial baking tradition.

## Key assumptions

**Flour sourcing (industrial-flour-purchased base):** This entry purchases commodity bread flour from regional food-service distributors. The civic value proposition does not depend on grain-sourcing differentiation: food access, training, and community gathering are the public-goods justifications. A local-mill-partnership upgrade (per spec annotation) would strengthen supply-chain resilience and potentially support cultural or heritage grain programming, but is not required for the civic case. Commodity flour price volatility (wheat market exposure) is the primary consumables risk; at $0.60/kg commodity bread flour [CITATION-NEEDED], flour accounts for approximately 57% of annual consumables ($5,460 of $9,500). A 30% price increase adds ~$1,600/yr to operating costs — material in a tight civic budget but not threatening viability.

**Throughput (80 loaves/day):** This is intentionally below the single-operator commercial ceiling: the civic model is not throughput-maximized. The two-deck configuration supports parallel instructor and member baking, but member-session coordination, training overhead, and community programming reduce effective saleable output. The 80 loaves/day figure is the blended output including both productive (instructor-led saleable bakes) and community-access (member practice, donation, nutrition-education) bakes. The labeled unit is 800g sourdough boule equivalent per baking SCHEMA.md §1. The figure is labeled [CITATION-NEEDED] as empirical community bakery throughput data is not available at authoring date.

**Staffing ($54,000/yr journeyman instructor):** Per spec requirement, $52-56k per SCALES.md. The $54,000 mid-point is at the lower bound of journeyman-baker wages in most US markets [CITATION-NEEDED: BLS OEWS SOC 51-3011 Baker, 2024]. The civic employer advantage (stability, benefits, community mission) is assumed to close the compensation gap; hiring_notes flag this as contested. The part-time apprentice/assistant position (0.4 FTE, ~$12,000-15,000/yr) is funded through workforce-development grant programs in the base configuration.

**Per-household cost calculation:** Uses 3,000 households as the town-scale representative mid-point per SCALES.md §2 (7,500 population × 0.40 household multiplier). Gross operating $70,300/yr ÷ 3,000 hh = $23.43/hh/yr. Net after offsets ($15,000-40,000/yr in grants and fees) ≈ $13-24/hh/yr depending on grant capture; amortized capital adds ~$1.17/hh/yr. The grant-funding assumptions are the most uncertain inputs [CITATION-NEEDED]; without grants, gross municipal cost is ~$24-25/hh/yr — still well below the $100 town civic threshold.

**sim_params derivation:** throughput_units_equiv_per_year (17,500) derived from 80 loaves/day × 250 operating days × (1 - 0.13 downtime). Electricity rate $0.125/kWh from US EIA Electric Power Monthly blended small-commercial rate 2023-2024. All monetary values in USD.

## Known risks / failure modes

**Regulatory (primary risk):** Food production in a public building carries a more complex regulatory profile than metalworking in a civic forge. Health-department commercial kitchen licensing is required regardless of civic ownership; some jurisdictions impose stricter requirements on food produced for public donation (food-bank supply triggers HACCP plan requirements and potentially additional health-department permits). The intersection of member-access food production (members handling food that may be donated or sold) with commercial kitchen licensing standards varies by jurisdiction; town counsel and the local health department must be engaged before any product leaves the facility. Liability exposure is more complex than in a non-food civic facility: foodborne illness affecting a community member or food-bank recipient creates municipal liability that requires specialist insurance and careful policy documentation. ADA accessibility compliance for member workstations (height-adjustable surfaces, knee-clearance) may add fitout cost beyond the mid-range capital estimate.

**Labour pipeline:** The journeyman baker-instructor is the single point of failure for the entire civic operation. The combined skill profile required — journeyman baking competency plus community instruction capability — is uncommon in the regional labor market, and $54,000/yr may not attract or retain a qualified candidate in regions where commercial bakeries pay market rates. If the instructor position is vacant for more than a few weeks, the supervised-production model cannot operate; no member can use the facility without instructor presence. The apprentice pipeline mitigates this over a 4-6 year horizon but provides no short-term succession protection. Civic employer stability (permanent position, benefits, mission alignment) and active workforce-development partnership are the primary hiring tools; these advantages are real but not guaranteed to close a significant compensation gap.

**Supply chain:** Commodity flour is available through regional food-service distributors at town scale per SCALES.md §6 infrastructure baseline. The primary supply-chain risk is price volatility (wheat market), not availability. Specialty flour for cultural programming (heritage wheat, rye, cultural specialty grains) may have longer lead times (14-21 days) and single-source dependencies that the typical 3-day lead applies only to commodity bread flour. The civic facility should maintain a 2-3 week flour inventory buffer as standard operating practice. Grid electricity is the single energy source with no backup; extended grid outages halt production. Municipal facilities typically have emergency generator capacity for critical systems, but a bakery oven is unlikely to be on the emergency circuit; this risk should be noted in the facility plan.

**Community adoption and political sustainability:** The food-equity framing must be grounded in documented local need. A civic bakery in a neighborhood with adequate supermarket and artisan bakery access faces legitimate "why is the municipality in the bread business?" opposition that benchmark-comparison data alone cannot answer. The political coalition (food-equity advocates, library board, public health department) is viable where food insecurity is measurably present; it is fragile where the need case is not documented. The per-household cost argument ($14-16/hh/yr net) is the primary political-viability tool but must be anchored to actual local food-access conditions, not assumed to hold in all town contexts.

## Iteration log

- 2026-04-18: v0.1 — initial authoring per Plan G Task 12. Civic-primary entry per spec requirement; baking equivalent of forge-004 Community Civic Makerspace. Full v1.1 schema populated: electric-deck energy source, $45k-$130k capital range, $0 floor_space_rent (town-owned), industrial-flour-purchased declaration with local-mill upgrade note, journeyman-baker skill floor (instructor + supervised member use), scale_fit town/small_city good + village poor, lens_fit civic/coop good + market poor. Full lens_context.civic block: food-equity political coalition (food-equity advocates + library board + workforce development + public health), staffing_model journeyman baker-instructor at $54k/yr citing SCALES.md §3, five substantive civic_externalities (food security, apprentice pipeline, cultural traditions, nutrition education, community gathering), benchmark_comparison vs library ($100-138/hh/yr) and food bank programs, council vote 5-2 favorable in food-insecure contexts. Full lens_context.cooperative block with Ostrom principles 1-6, schedule-booked member shifts, legal_form as municipal, scale_fit_note calibrated to town. sim_params.annual_public_use_hours: 8,320 (32 hr/wk × 52 × 5 concurrent persons) required for civic-lens utilization diagnostic; usage_rate_threshold: 0.15 per specialized civic facility exception precedent from forge-004. Market lens zero-priced with industrial_baseline_price $3 cited for reference; pricing_validation marked N/A for civic operation. Three historical lineage precedents with anti-romantic treatment (French boulangerie sociale, US library model, cooperative extension). Fifteen [CITATION-NEEDED] flags placed over fabrication on capital cost, install cost, wages, throughput data, flour pricing, grant availability, and historical lineage sources.
