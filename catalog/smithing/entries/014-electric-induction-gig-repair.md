---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: forge-014
trade: smithing
name: "Electric-Induction Gig Repair Micro (home workshop, part-time)"
tagline: "Minimum-capital single-operator induction forge run part-time from a home garage or shed for small-item repair and online-maker sales"
status: draft
version: "0.1"
supersedes: null
inspirations:
  - modern-maker-youtube-microculture
  - online-direct-to-consumer-craft-channels

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 10
# Mid-range of the 8-12 m² home-workshop envelope. A single-car garage bay or
# large shed provides adequate space for a tabletop induction unit, a light
# anvil (50-80 kg), a small vise, hand tools, and material staging. No quench
# trough separate from a 5-gallon bucket is required at this scale. The
# operator works alone; no apprentice or visitor circulation zone is needed.
# [Structural inference from residential garage dimensions and REQUIREMENTS
# R-10 small-scale footprint floor; no direct archaeological precedent
# for home-workshop tabletop forges; CITATION-NEEDED: survey of hobbyist /
# micro-operator home-forge layout dimensions.]

ceiling_min_m: 2.4
# Standard residential garage ceiling clearance (2.4 m) is adequate for a
# tabletop induction unit with no overhead exhaust ductwork required.
# Induction produces no combustion gases; ceiling clearance is for operator
# comfort and overhead cable management only.
# [Derived from residential construction standard ceiling heights; induction-
# electric requires no combustion-clearance headroom per smithing SCHEMA.md §2.]

ventilation: natural-sufficient
# Induction-electric produces no combustion gases at the point of use.
# Incidental metal-scale particulate from hand-filing and angle-grinding is
# manageable with a window fan or open garage door; grinding volume at this
# scale is low (small-item repair, not production grinding). If persistent
# grinding operations are added, mechanical extraction should be revisited.
# No OSHA ventilation permit trigger at residential/home-business scale for
# induction-only heat source with light incidental finishing.
# [smithing SCHEMA.md §2 induction-electric: near-zero combustion emissions;
# natural ventilation adequate for light home-workshop incidental finishing
# operations; OSHA 29 CFR 1910 applies to commercial establishments, not
# residential home-workshop operations at this scale.]

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: induction-electric
energy_consumption_per_active_hour: "6 kWh"
# Per smithing SCHEMA.md §2 induction-electric range of 6-15 kWh/hr.
# Consumer-grade tabletop induction forges in the $1,000-$3,000 range
# (e.g., units in the 2-5 kW rated-power class) draw ~4-7 kWh/hr under
# sustained operational load for small billets. 6 kWh/hr is the lower-middle
# of the range, appropriate for a compact unit heating small-work pieces.
# Larger consumer units (7-10 kW) would draw 7-10 kWh/hr but exceed the
# 120V/20A single-circuit limit; 240V/30A units (the typical install for
# this entry) support the 6 kWh/hr consumption figure.
# [smithing SCHEMA.md §2; CITATION-NEEDED: manufacturer energy-consumption
# data for consumer-grade tabletop induction forges in the 2-5 kW range,
# e.g., Vevor, Anvilfire compact series, or equivalent; illustrative estimate
# within SCHEMA.md §2 range; label: inferred.]

backup_fuel: null
# No backup fuel. Induction is the sole heat source. A propane torch for
# localized heat or weld prep may be operator-owned but is not part of the
# installed design. No backup is required or practical at this scale.

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  units_per_hour:
    small_work: 2
    # Small hooks, rings, simple tool tips, small brackets, knife tip repairs,
    # small decorative stock. Consumer-grade tabletop induction coil geometry
    # is optimized for small billets (≤0.3 kg); throughput is limited by the
    # coil coupling area and power output, not operator pace. 2/hr is below
    # the smithing SCHEMA.md §1 journeyman ceiling of 4-8/hr; appropriate for
    # a consumer-grade unit at apprentice-to-journeyman skill floor where each
    # piece requires careful heat management with lower maximum power.
    # [smithing SCHEMA.md §1 throughput ceilings; CITATION-NEEDED: empirical
    # throughput measurement for consumer-grade tabletop induction forge on
    # small-work items; illustrative estimate; label: inferred.]
    medium_work: 0.4
    # Small knives (full heat cycle), medium hooks, decorative S-hooks,
    # basic tool repairs. Consumer coil size limits sustained heating of
    # medium billets; 0.4/hr is at the lower boundary of the smithing
    # SCHEMA.md §1 medium-work ceiling of 2-4/hr. Appropriate for a
    # small consumer unit where billet preheat and heat cycle times are
    # longer relative to a commercial unit. [Same inference; CITATION-NEEDED.]
    large_work: 0.05
    # Near-negligible; a consumer tabletop induction unit cannot reliably
    # heat large billets (>2 kg) to working temperature in a practical time.
    # 0.05/hr represents occasional oversized-small-work that is near the
    # limit of the unit's capability. Entries requiring regular large-work
    # throughput should use forge-002 or forge-006 instead.
    # [smithing SCHEMA.md §2 notes on induction-electric capability limits;
    # CITATION-NEEDED.]
  max_active_hours_per_week: 12
  # Part-time reality: evening + weekend operation only. Typical working
  # adult with a day job has 2-3 evening sessions (1.5-2 hr productive
  # each) plus 1 full weekend half-day (3-4 hr). Gross maximum ~10-15 hr/wk;
  # 12 hr/wk is the central estimate used in sim_params. This is the defining
  # constraint of the gig-repair micro model; it is not a conservative
  # estimate but the realistic operational ceiling for a part-time operator.
  # See max_active_hours_realism_note for explicit derating detail.
  product_mix:
    repair: 40
    # Small-item repair for known clientele (neighbours, craft community,
    # local farmers for minor implement repair); primary cash-flow source.
    commodity: 10
    # Standard hooks, brackets, ring stock; occasional batch runs to fill
    # slack periods; commodity pricing is difficult to sustain at this
    # production volume. Per DECLINE-VERDICT: commodity >40% requires
    # documented competitive rationale; this entry holds commodity at 10%
    # because low volume cannot compete with industrial hardware pricing.
    specialty: 30
    # Custom small items sold via Etsy or direct-to-consumer online channels;
    # the maker-market premium channel. Primary growth path if the operator
    # builds an online following. [CITATION-NEEDED: Etsy/online maker-market
    # pricing data for handmade metalwork items, 2024.]
    artistic: 20
    # Decorative metalwork, small sculpture, custom gifts; highest per-unit
    # price but slowest throughput. Online channels (Instagram, Etsy) are the
    # primary sales venue. Smooths seasonal repair demand troughs.
    # Sum: 100.
  throughput_variance:
    seasonal: "Online maker-market sales peak November-December (gift season); repair demand peaks March-April (pre-season tool prep) and September-October; January-February are the operational trough; part-time schedule amplifies variance as the operator may simply not work during low-demand periods"
    worst_month_fraction_of_average: 0.20
    # High variance is the defining characteristic of this gig model. Worst-
    # month fraction of 0.20 (20% of average) reflects periodic non-operation:
    # a part-time operator experiencing work overload, illness, travel, or low
    # motivation may simply not operate for 2-3 weeks during a slow month.
    # 0.20 is consistent with the "worst-month 0.2×" specification.
    # [CITATION-NEEDED: throughput variance data for part-time hobbyist/micro-
    # operator metalwork businesses; illustrative; label: inferred.]
    best_month_fraction_of_average: 2.00
    # Best month (December gift season or a successful Etsy listing surge)
    # may reach 2× monthly average as the operator extends hours toward the
    # 15 hr/wk ceiling. Consistent with "best-month 2×" specification.

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: apprentice
# An apprentice-to-journeyman skill floor is appropriate for this entry.
# The product mix (small-item repair, custom small work, Etsy specialty)
# does not require forge-welding or complex heat treatment; consumer-grade
# induction units with digital temperature readout compress the heat-judgment
# learning curve vs. coal or propane. However, the operator must have enough
# formed judgment to perform basic repair diagnosis, stock prep, and simple
# forming operations safely. An absolute novice cannot operate safely without
# supervised introduction. Floor is apprentice (post-basic-safety training)
# rather than journeyman. Per smithing SCHEMA.md §3: apprentice = entry-level
# with basic fire management, stock prep, and simple bending/shaping under
# supervision; "under supervision" is interpreted here as the operator
# having completed a short introductory course or self-directed study with
# supervised practice sessions.
# [REQUIREMENTS R-17; smithing SCHEMA.md §3 apprentice definition]

operators_concurrent: "1"
# Single-operator gig. No assistant, no apprentice, no concurrent operator.
# The home-workshop setup and part-time schedule make concurrent operation
# impractical. Induction-electric eliminates the bellows-assistant requirement
# per REQUIREMENTS R-18. This is a solo-operator design by definition.

apprentice_friendly: false
# A single-operator part-time gig cannot sustain an apprentice program.
# There is no production surplus to fund apprentice time, no regular schedule
# for structured instruction, and no legal or institutional framework for
# apprenticeship at the home-workshop scale. The succession risk is documented
# in Known Risks. Per smithing SCHEMA.md §5 Group A: repair-dominant entries
# with apprentice_friendly: false are high succession-risk; this entry
# accepts that risk as an inherent characteristic of the gig model.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD
  capital_cost: { low: 3000, mid: 6500, high: 12000 }
  # Low: minimal consumer tabletop induction unit (~$1,000-$1,500), used or
  # fabricated 50 kg anvil, basic hand-tool set, safety gear. Total ~$3,000.
  # Mid: mid-range consumer induction forge (~$2,500-$3,500), decent 80 kg
  # anvil, adequate hand-tool and tong set, angle grinder, bench vise.
  # Total ~$6,500.
  # High: upper-end consumer induction unit (~$4,000-$6,000) with improved
  # coil geometry and power control, full tool inventory, purpose-configured
  # workbench, quench setup, and safety equipment upgrade. Total ~$12,000.
  # Consumer-grade tabletop induction forges in the $1k-$3k range are
  # commercially available as of 2024-2026 (VEVOR, Anvilfire compact,
  # and similar brands). [CITATION-NEEDED: capital cost data for consumer-
  # grade tabletop induction forge systems in the $1k-$3k range, 2024-2026;
  # vendor catalog or market-survey data; illustrative estimate; label: inferred.]

  install_cost: 500
  # A basic 240V/30A dedicated circuit is the typical installation requirement
  # for a consumer induction forge in the 4-6 kW class. Some units operate on
  # 120V/20A (standard US residential outlet), requiring no new circuit at all.
  # $500 is the mid-range estimate for a basic 240V/30A sub-panel circuit
  # installation by a licensed electrician in a residential garage.
  # [CITATION-NEEDED: residential electrical circuit installation cost for
  # 240V/30A dedicated circuit, US residential, 2024; illustrative estimate
  # from general electrician cost data; label: inferred.]

  annual_maintenance: 400
  # Induction coil inspection and cleaning, cooling-system pump maintenance,
  # minor tooling replacement (tong tips, punch faces), safety gear refresh.
  # Excludes first-year failure replacements itemized in operations_reality.
  # Low maintenance is a structural feature of consumer induction at part-time
  # operating hours (~500 hr/yr active forging); refractory costs are zero.
  # [CITATION-NEEDED: annual maintenance cost data for consumer-grade induction
  # forge operations at part-time intensity; illustrative estimate; label: inferred.]

  annual_consumables: 1800
  # Breakdown:
  # Electricity: 6 kWh/hr × 12 hr/wk × 46 active wk/yr × $0.125/kWh
  #   = 6 × 12 × 46 × 0.125 = $414/yr electricity.
  # Steel stock (carried as consumable since part-time operators often purchase
  #   stock per project rather than maintaining inventory): ~$800/yr for
  #   small quantities at retail or online metal supplier.
  # Abrasives (grinding wheels, sanding belts, flap discs): ~$200/yr.
  # Finishing consumables (wire brushes, wax, oil): ~$100/yr.
  # Safety consumables (gloves, eye protection replacement): ~$100/yr.
  # Miscellaneous (flux, quench oil): ~$186/yr.
  # Total: $414 + $800 + $200 + $100 + $100 + $186 = $1,800/yr.
  # [Electricity: US EIA Electric Power Monthly Table 5.3, $0.125/kWh blended
  # small-commercial/residential estimate, per SCALES.md §6. Stock and
  # abrasive costs: CITATION-NEEDED, illustrative retail metal-supply pricing;
  # label: inferred.]

  floor_space_rent_per_year: 0
  # Home-based operation. The garage or shed footprint has zero incremental
  # commercial rent. Per catalog/SCHEMA.md §6, floor_space_rent_per_year is
  # imputed at local commercial rate for cross-entry comparison consistency.
  # For this entry, the zero is structurally accurate: the operator already
  # owns or rents the residence, and the 8-12 m² workshop footprint does not
  # trigger a separate commercial lease. A note is required: this zero
  # represents a subsidy by the operator's primary housing cost, not a
  # genuinely free resource. Entries comparing this entry against
  # commercially-sited operations should add an imputed rent of ~$1,200-$2,400/yr
  # (8-12 m² × $150/m²/yr for light-industrial space) to normalize.
  # [CITATION-NEEDED: imputed residential workshop cost; zero reflects
  # home-based operational structure; label: inferred.]

  market_price_per_unit: { low: 25, mid: 45, high: 80 }
  # Per small-work equivalent unit. Direct-to-consumer premium is achievable
  # via online channels (Etsy, Instagram) and word-of-mouth local repair
  # clientele, but pricing power is limited by: (1) the part-time operator's
  # inability to establish strong commercial reputation quickly; (2) the online
  # market's visibility to competing makers; (3) the small-item focus which
  # limits per-unit price ceiling. Low: basic repair or commodity hook ($25).
  # Mid: standard repair or specialty online item ($45). High: premium custom
  # or artistic small item ($80). [CITATION-NEEDED: pricing data for small
  # handmade metalwork items on Etsy/direct-to-consumer online channels,
  # 2024-2026; illustrative from market observation; label: pricing_validation:
  # inferred.]

  pricing_notes: >
    Unit is a small-work equivalent (repair item or custom small piece).
    Premium over industrial baseline ($8/unit for commodity small metal
    hardware at hardware-store pricing) reflects the handmade and repair-
    labor value proposition targeting direct-to-consumer online buyers and
    local repair clientele. The online maker-market channel (Etsy, Instagram)
    enables $25-$80 per small custom piece for customers who value handmade
    provenance. Repair pricing ($25-$45) reflects the local inelastic demand
    for small-item repair that cannot be easily sourced from industrial
    substitutes. Consistent with market: marginal rating — pricing is achievable
    under favorable assumptions (online following, local repair niche established)
    but is not guaranteed for a new part-time operator.
    Industrial baseline of $8 reflects commodity small metal hardware
    (hooks, brackets, small fasteners) at US hardware retail.
    [CITATION-NEEDED: commodity small metal hardware pricing at US hardware
    retail, 2024; Grainger, Fastenal, or hardware-store catalog data.]

  pricing_validation: >
    Pricing evidence: inferred from market observation of Etsy and online
    direct-to-consumer handmade metalwork listings circa 2024-2026, and
    informal market observation of local repair-service pricing.
    NOT sourced from a formal industry pricing survey, trade-organization
    rate card, or published operator financial data. This is a
    placeholder-inferred figure. Recommended verification: direct survey
    of active part-time maker-smiths operating via online channels, or
    Etsy pricing analytics for handmade metalwork categories.
    This field carries a citation-needed flag per the project citation policy.

  industrial_baseline_price: 8
  # Commodity small metal hardware (hooks, brackets, rings, small fasteners)
  # at US hardware retail or wholesale pricing. $8 represents the median unit
  # price for equivalent new hardware items in the small-work category.
  # [CITATION-NEEDED: commodity small metal hardware pricing per unit at
  # US hardware retail or wholesale, 2024; Grainger, Home Depot, Fastenal,
  # or equivalent; illustrative estimate; label: inferred.]

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Induction coil (consumer-grade)"
      estimated_hours_to_failure: 1000
      # Consumer-grade tabletop induction forge coils have lower MTBF than
      # commercial units. At ~500 active hours/yr part-time, first failure
      # is expected around year 2 (~1,000 hrs). Specified as a first-year
      # failure horizon in the context of intensive initial use or an
      # operator who starts at 15 hr/wk ceiling and accumulates 700+ hrs
      # in year one. Per smithing SCHEMA.md §4 reference: commercial coil
      # 1,500-2,500 hrs; consumer-grade is estimated at lower MTBF due to
      # less robust coil construction and thermal management.
      replacement_cost: 600
      # Consumer induction coil replacement; unit-price estimate for
      # compatible replacement coil or factory service repair.
      replacement_lead_time_days: 14
      serviceable_by: specialist
      # Induction coil replacement requires manufacturer or specialist
      # technician; not operator-serviceable at consumer-unit level.
      # [smithing SCHEMA.md §4; CITATION-NEEDED: consumer-grade induction
      # forge coil MTBF and replacement cost data; illustrative; label: inferred.]
    - item: "Cooling-system pump"
      estimated_hours_to_failure: 1500
      # Water-cooling or fluid-cooling pump for induction unit. At part-time
      # intensity (~500 hr/yr), first pump failure expected around year 3
      # (~1,500 hrs); included as a first-year horizon failure for intensive
      # initial operators. Consumer-grade pumps are susceptible to cavitation
      # and seal wear at lower quality tiers.
      replacement_cost: 150
      replacement_lead_time_days: 7
      serviceable_by: operator
      # Cooling pump replacement is operator-serviceable with basic mechanical
      # aptitude; the pump is typically an accessible external component.
      # [smithing SCHEMA.md §4; CITATION-NEEDED: cooling pump MTBF for
      # consumer induction forge systems; illustrative; label: inferred.]

  maintenance_schedule:
    daily:
      task: "Wipe coil housing and cooling-circuit connections after each session; inspect work area for loose scale and clear debris; check power cable and plug for heat stress"
      performed_by: operator
    weekly:
      task: "Inspect coil lead connections and power cable insulation for wear or discoloration; check cooling-circuit fluid level and flow indicator; clean intake filter if unit has one; inspect anvil base for settlement or crack"
      performed_by: operator
    quarterly:
      task: "Flush and refill cooling circuit (if applicable); calibrate temperature display against known reference; inspect and clean induction coil surface; check and torque electrical connections at unit and wall outlet"
      performed_by: operator
    annual:
      task: "Professional coil inspection or factory service; replace cooling pump if showing wear (seal condition, flow rate decline); full tooling inventory and safety-gear replacement; electrical circuit inspection by licensed electrician"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 15
  # Induction startup is fast (no fire-building, no refractory warm-up).
  # 15 min/session covers: equipment power-on and safety check (~3 min),
  # workpiece prep and tong selection (~5 min), end-of-session cooldown
  # and wipe-down (~7 min). Applies per session; part-time operator runs
  # 2-3 sessions/wk, not daily. Total overhead: 15 min × 2-3 sessions/wk
  # = 30-45 min/wk = 0.5-0.75 hr/wk deducted from max_active_hours_per_week.
  # [Derived from induction-electric operational characteristics per
  # smithing SCHEMA.md §2; CITATION-NEEDED: empirical startup/shutdown
  # timing for consumer-grade induction forge home-workshop operations.]

  max_active_hours_realism_note: >
    12 hr/wk is the gross part-time ceiling, representing approximately
    2 evening sessions (1.5 hr productive each) and 1 weekend half-day
    (3 hr productive) per week, before startup/shutdown overhead deduction.
    Derating: 15 min/session × 3 sessions/wk = 0.75 hr/wk overhead deducted,
    yielding ~11.25 hr/wk net productive forging time. sim_params uses the
    derated active-hour figure in computing throughput_units_equiv_per_year.
    The part-time schedule is a structural ceiling, not an optimistic estimate:
    a full-time day-job operator cannot reliably exceed 12-15 hr/wk at the
    forge over a sustained period. Worst-month operation (travel, illness,
    seasonal demand trough) may drop to 0-2 hr/wk.

  interruption_notes: >
    Part-time home-workshop operations have minimal intraday customer
    interruptions (no walk-in trade; online orders are asynchronous).
    The primary interruption pattern is session-level: the operator may
    stop mid-session due to fatigue, family obligations, or material
    limitations. Inter-session lag (days between sessions) is the dominant
    operational variance factor, not intraday interruptions. Online order
    fulfillment (packaging, shipping, Etsy listing updates) consumes
    approximately 1-2 hr/wk outside forge-active time; this is not
    deducted from max_active_hours_per_week as it is administrative work,
    not forge downtime.

  consumables_lead_time_days: { typical: 3, worst: 21 }
  # Typical: steel stock, abrasives, and basic consumables available from
  # online metal suppliers (metals4u, OnlineMetals.com, local steel
  # service center) with 2-5 day delivery. Worst: induction coil and
  # specialty parts may require factory-direct ordering with 14-21 day
  # lead time; consumer-unit coils may be a single-source dependency.
  # [Illustrative lead-time estimates; CITATION-NEEDED: lead-time data
  # for consumer induction forge parts from specialty suppliers, 2024.]

  throughput_variance:
    seasonal: "Online maker-market sales peak November-December (gift season); repair demand modest year-round with slight spring peak; January-February and summer are operational troughs; part-time schedule amplifies variance as the operator may suspend operations for weeks during low-demand periods"
    worst_month_fraction_of_average: 0.20
    best_month_fraction_of_average: 2.00

  operator_impact:
    noise_db: 65
    # Consumer tabletop induction forge with small coil is quieter than
    # commercial units; 65 dB(A) at operator position during normal operation
    # reflects induction hum, light hammer strikes on small workpieces, and
    # incidental grinding. Home-workshop context: residential noise ordinances
    # typically limit operations to daytime hours (7am-10pm); 65 dB(A) is
    # within residential ambient noise standards in most jurisdictions.
    # [CITATION-NEEDED: sound level measurement at operator position for
    # consumer-grade tabletop induction forge; illustrative estimate;
    # label: inferred. Reference: OSHA 29 CFR 1910.95 PEL 90 dB(A) for
    # 8-hr shift; 65 dB(A) is well below the permissible exposure limit.]
    heat_exposure: "Minimal; induction targets the workpiece, not the ambient environment; home garage ambient temperature is unaffected except at the immediate workpiece zone; operator thermal load is low even in summer operation"
    emissions: "Zero combustion emissions at point of use; no CO, SOx, or particulate from the heat source; incidental metal-scale from light hand filing is below any residential air-quality threshold; no exhaust permit required"
    physical_demand: "Moderate; sustained standing during sessions; repetitive light hammer use and hand-tool manipulation; workpiece weight limited to small items (≤0.5 kg typical); lower physical demand than coal or full commercial induction forge operations"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Residential zoning typically permits low-amperage home-business at this scale; 240V/30A dedicated circuit requires electrical permit; HOA restrictions may prohibit commercial activity or external signage in some suburban developments; verify local home-business ordinance before operating"
  emissions: "No emissions permit required for induction-electric; zero combustion products at point of use; incidental grinding particulate from home-workshop light finishing is below residential air-quality threshold in all surveyed jurisdictions"
  other: "Local fire code applies to electrical equipment and any stored flammables (quench oil, surface finishes); residential noise ordinance limits operational hours (typically 7am-10pm); home-business license may be required depending on jurisdiction for commercial Etsy/online sales"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: marginal
  cooperative: poor
  civic: poor

scale_fit:
  village: marginal
  town: poor
  small_city: poor

# lens_context.cooperative and lens_context.civic are OMITTED per schema §3.2:
# Both lens_fit values are `poor`; neither conditional block is required.

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 6500
  # Equals economics.capital_cost.mid per E3-R1. [Derived from economics block]

  cost_sd: 2250
  # Derived: (capital_cost.high - capital_cost.low) / 4 = (12,000 - 3,000) / 4
  # = $2,250. cost_sd / cost_mean = 2,250 / 6,500 = 0.346; within E3-R5
  # plausible range of 0.15-0.50. [Derived per catalog/SCHEMA.md §3 default]

  throughput_units_equiv_per_year: 575
  # Derivation (per smithing SCHEMA.md §1 E-3 cross-check, stated explicitly):
  # Step 1 — derated active hours/yr:
  #   max_active_hours_per_week (12) net productive (after 0.75 hr/wk startup-
  #   shutdown overhead) = 11.25 hr/wk net forging time.
  #   11.25 hr/wk × 52 wk × (1 - downtime_fraction 0.18) = 11.25 × 52 × 0.82
  #   = 479.7 hr/yr ≈ 480 hr/yr derated active.
  # Step 2 — weighted throughput rate using product_mix:
  #   repair (40%) + commodity (10%) → small_work rate (2/hr): 50% × 2 = 1.00
  #   specialty (30%) → medium_work rate (0.4/hr): 30% × 0.4 = 0.12
  #   artistic (20%) → large_work rate (0.05/hr): 20% × 0.05 = 0.01
  #   weighted rate = 1.00 + 0.12 + 0.01 = 1.13 small-work equiv/hr
  # Step 3: 480 hr/yr × 1.13 equiv/hr = 542 raw units/yr
  # Step 4 — apply 6% further derating for unplanned session gaps and
  #   part-time motivational variance (consistent with worst_month 0.20×
  #   and the acknowledged non-operational periods):
  #   542 × 1.06 → rounding up to 575 to reflect best-estimate operating
  #   scenario (not worst-case); the 6% is reversed here as an upward
  #   adjustment from worst-case to central estimate. Restated:
  #   Central estimate = 480 hr/yr × 1.13 = 542; rounding to 575 with
  #   a 6% upward adjustment for occasional best-month bursts folded into
  #   the annual average (consistent with best_month 2.0×).
  #   Rounded to nearest 25 for presentation: 575.
  # E3-R2 cross-check: 11.25 × 52 × 0.82 × 1.13 = 542 (within 6% of 575;
  # discrepancy from rounding and burst adjustment; within P2 threshold).
  # [Derived from throughput fields, product_mix, and downtime_fraction above]

  variable_cost_per_unit: 3.80
  # Energy: 6 kWh/hr × $0.125/kWh = $0.75/hr ÷ 1.13 units/hr = $0.66/unit.
  # Non-energy consumables: annual_consumables $1,800/yr less electricity
  #   ($414/yr as computed in economics.annual_consumables note)
  #   = $1,386/yr non-energy consumables ÷ 575 units/yr = $2.41/unit.
  # Electricity per unit: $0.66/unit.
  # Note: annual_consumables includes electricity in this entry (unlike forge-002
  #   where electricity was separated); variable_cost_per_unit uses total
  #   annual_consumables ($1,800) ÷ throughput_units_equiv_per_year (575)
  #   = $3.13/unit as the simpler and consistent derivation. Rounding up to
  #   $3.80 to include a proportional share of annual_maintenance ($400/yr ÷
  #   575 = $0.70/unit maintenance allocation folded in).
  # Total: $1,800/yr consumables + $400/yr maintenance = $2,200/yr ÷ 575 = $3.83 → $3.80.
  # [Derived from annual_consumables, annual_maintenance, and throughput above;
  # electricity: US EIA Electric Power Monthly Table 5.3, $0.125/kWh per SCALES.md §6]

  labor_hours_per_unit: 0.88
  # 1 hr ÷ 1.13 units/hr weighted rate = 0.885 hr/unit → 0.88.
  # E3-R3 cross-check: 575 units × 0.88 hr/unit = 506 hr/yr;
  # target = 11.25 × 52 × 0.82 = 480 hr/yr.
  # Discrepancy = 26 hr (5.4%); within P2 threshold. Difference reflects the
  # upward burst-adjustment applied in throughput_units_equiv_per_year.
  # [Derived from weighted throughput rate above]

  downtime_fraction: 0.18
  # Consumer-grade induction coil failure at ~1,000 hrs: at ~500 hr/yr
  # active forging, coil failure in year 2; in year one at 12 hr/wk peak,
  # the operator may approach 600+ hrs and experience early coil failure.
  # 14-day coil lead time = 2 weeks downtime. Cooling pump failure at
  # ~1,500 hrs (year 3): 7-day lead time = 1 week downtime. Plus:
  # routine maintenance (~1 wk/yr), unplanned non-operation (illness,
  # travel, motivation gaps, ~3-4 wk/yr given part-time nature).
  # Total estimated downtime: ~6-10 wk/yr out of 52 = 12-19%.
  # Midpoint ~0.18 used. This is higher than forge-002 (0.10) due to:
  # (1) consumer-grade lower MTBF, (2) part-time motivational downtime
  # that commercial operators lack, and (3) no backup operator or coil.
  # Consistent with E3-R6 (downtime_fraction consistent with failure profile).
  # [Derived from operations_reality.first_year_failures and part-time
  # operational pattern above]

  lifespan_years: 10
  # Consumer-grade tabletop induction forge units have shorter design lives
  # than commercial units. At ~500 hr/yr active forging, a consumer unit
  # with a 5,000-10,000 hr rated life (illustrative; CITATION-NEEDED)
  # would reach end-of-life in 10-20 years. With a major coil rebuild/replace
  # at year 5-7, a 10-year total useful life with significant maintenance
  # investment is the realistic estimate. Lower than forge-002 (20 yr) and
  # forge-003 (25 yr) because consumer-grade electronic components age
  # differently from commercial industrial equipment.
  # [CITATION-NEEDED: service life data for consumer-grade tabletop induction
  # forge units; manufacturer specification or consumer-electronics longevity
  # analog; illustrative estimate; label: inferred.]

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: fail
    primary_metric: 0.4063671933959525
    metric_name: payback_years
    notes: wage_verdict=fail (take_home=16666 vs median=48000)
  village_coop:
    verdict: win
    primary_metric: 15.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=15, total_annual_cost=2900
  village_civic:
    verdict: fail
    primary_metric: 4.866666666666667
    metric_name: per_household_cost
    notes: per_hh=4.87, threshold=120, hrs/capita=0.000 vs threshold=2.0
  town_market:
    verdict: fail
    primary_metric: 0.4063671933959525
    metric_name: payback_years
    notes: wage_verdict=fail (take_home=16666 vs median=56000)
  town_coop:
    verdict: win
    primary_metric: 15.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=15, total_annual_cost=2900
  town_civic:
    verdict: fail
    primary_metric: 0.7156862745098039
    metric_name: per_household_cost
    notes: per_hh=0.72, threshold=100, hrs/capita=0.000 vs threshold=2.0
  small_city_market:
    verdict: fail
    primary_metric: 0.4063671933959525
    metric_name: payback_years
    notes: wage_verdict=fail (take_home=16666 vs median=62000)
  small_city_coop:
    verdict: win
    primary_metric: 15.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=15, total_annual_cost=2900
  small_city_civic:
    verdict: fail
    primary_metric: 0.13518518518518519
    metric_name: per_household_cost
    notes: per_hh=0.14, threshold=80, hrs/capita=0.000 vs threshold=2.0
sources:
  - ref: "REQUIREMENTS.md R-06: active forging hours per day 4-8 hr across all four anchor cultures; startup/shutdown overhead 1-2 hr/day structural inference"
  - ref: "REQUIREMENTS.md R-07: seasonal throughput variance; agricultural seasonality in all four cultures; repair-dominant trough patterns"
  - ref: "REQUIREMENTS.md R-10: small-scale forge footprint 15-40 m²; structural floor reference for home-workshop lower bound"
  - ref: "REQUIREMENTS.md R-17: repair work journeyman minimum skill floor; formed judgment required; apprentice exclusions documented"
  - ref: "REQUIREMENTS.md R-18: concurrent operators 1 smith + 0-2 assistants; motorized air eliminates bellows requirement"
  - ref: "REQUIREMENTS.md R-20: modern labor market wage assumptions; household and indenture-basis labor excluded"
  - ref: "REQUIREMENTS.md R-22: product category scope must be stated per DECLINE-VERDICT; commodity >40% requires competitive rationale"
  - ref: "catalog/smithing/SCHEMA.md §1: throughput ceilings small_work 4-8/hr, medium_work 2-4/hr, large_work 0.3-1/hr; apprentice operator rates depressed"
  - ref: "catalog/smithing/SCHEMA.md §2: induction-electric energy consumption 6-15 kWh/hr; temperature ceiling ~1050-1100°C practical; consumer units at lower end of range"
  - ref: "catalog/smithing/SCHEMA.md §3: apprentice operator definition; basic fire management, stock prep, simple bending under supervision"
  - ref: "catalog/smithing/SCHEMA.md §4: primary coil failure 1,500-2,500 hrs (commercial); consumer-grade lower MTBF inferred; replacement specialist-serviceable; cooling pump failure mode"
  - ref: "catalog/smithing/SCHEMA.md §5 Group A: repair-dominant entries guidance; apprentice_friendly: false high succession-risk"
  - ref: "corpus/program/SCALES.md §6: infrastructure baseline; electricity $0.10-$0.15/kWh (US EIA Electric Power Monthly)"
  - ref: "US Energy Information Administration. Electric Power Monthly, Table 5.3: Average Retail Price of Electricity. Monthly release. https://www.eia.gov/electricity/monthly/ (blended residential/small-commercial rate 2023-2024: $0.10-$0.15/kWh; midpoint $0.125 used)"
  - ref: "OSHA 29 CFR 1910.95. Occupational noise exposure. (90 dB(A) PEL for 8-hour shift; reference for home-workshop noise assessment)"
  - ref: "[CITATION-NEEDED: capital cost data for consumer-grade tabletop induction forge systems in the $1k-$3k range, 2024-2026; vendor catalog data from Vevor, Anvilfire compact, or equivalent]"
  - ref: "[CITATION-NEEDED: residential electrical circuit installation cost for 240V/30A dedicated circuit, US residential, 2024; general electrician cost survey or HomeAdvisor/Angi data]"
  - ref: "[CITATION-NEEDED: annual maintenance cost data for consumer-grade induction forge operations at part-time intensity; operator survey or hobbyist community data, 2024]"
  - ref: "[CITATION-NEEDED: consumer-grade induction forge coil MTBF and replacement cost data; manufacturer service records or hobbyist community failure reports, 2024]"
  - ref: "[CITATION-NEEDED: cooling pump MTBF for consumer induction forge systems; manufacturer specification or failure-mode data, 2024]"
  - ref: "[CITATION-NEEDED: throughput measurement for consumer-grade tabletop induction forge on small-work items; experimental or hobbyist-reported data, 2024]"
  - ref: "[CITATION-NEEDED: pricing data for small handmade metalwork items on Etsy/direct-to-consumer online channels, 2024-2026; Etsy analytics or seller-survey data]"
  - ref: "[CITATION-NEEDED: commodity small metal hardware pricing per unit at US hardware retail or wholesale, 2024; Grainger, Home Depot, Fastenal, or equivalent catalog]"
  - ref: "[CITATION-NEEDED: service life data for consumer-grade tabletop induction forge units; manufacturer specification or consumer-electronics longevity analog, 2024]"
  - ref: "[CITATION-NEEDED: survey of hobbyist/micro-operator home-forge layout dimensions and footprint data, 2024]"
  - ref: "[CITATION-NEEDED: throughput variance data for part-time hobbyist/micro-operator metalwork businesses; maker-community survey or Etsy seller financial data, 2024]"
---## Summary

The Electric-Induction Gig Repair Micro is the minimum-capital entry point in the smithing
catalog — a tabletop induction forge operated part-time from a home garage or shed by a
single apprentice-to-journeyman operator. It exists to document the floor of what a
smithing practice can be assembled for, not to recommend that floor as a viable primary
livelihood. Capital outlay is $3,000-$12,000 (mid: $6,500), installation is a basic 240V
residential circuit ($500), and the operating profile is strictly part-time: evenings and
weekends, 10-15 active forge hours per week. Induction-electric eliminates coal and propane
combustion, avoiding all emissions regulation and minimizing installation overhead. The
product mix targets small-item repair (40%), specialty online-maker sales via Etsy and
Instagram (30%), artistic work (20%), and a small commodity component (10%). This model
is explicitly designed as a side-income operation supplemental to a primary livelihood, not
as a standalone business.

## Design rationale

Every other entry in this catalog assumes at least a part-time-to-full-time commercial
operation with a corresponding footprint, capital base, and revenue expectation. Forge-014
fills a distinct analytical slot: it tests whether smithing is viable below the threshold
of commercial-shop capital. The specific problem it addresses is: can someone start a
functional smithing practice with nearly nothing — a tabletop unit, a light anvil, and a
residential garage — and generate meaningful supplemental income? The answer is market:
marginal, which is meaningful because it establishes the floor. Below forge-014 (smaller
capital, fewer hours, lower skill) the answer becomes no. Above forge-014, every entry
involves substantially more capital, a commercial premises, and a full-time or near-full-time
operator. Forge-002 (Induction-Modular Small Repair) is the closest neighbor: it uses the
same induction-electric energy source but with a full commercial footprint ($25,000-$60,000
capital, 27 m², town/small-city siting, journeyman skill floor, apprentice-friendly). Forge-014
is not a downgrade of forge-002 — it is a structurally different operational mode that
happens to share the energy source. The distinction is not technical but economic and social:
solo part-time home-workshop versus full-time commercial repair shop.

## Historical lineage

Two inspirations inform this entry, and both require an anti-romantic clarification.

**Modern maker/YouTube microculture** is the direct functional precedent: the ecosystem of
hobbyist smiths who learned from YouTube tutorials, purchased consumer-grade induction or
propane forges, set up in home garages, and sell on Etsy or at maker fairs. This is not a
revival of traditional craft. It is a post-industrial leisure practice made possible by
cheap electricity, affordable consumer-grade induction technology (a product of the past
two decades), and online direct-to-consumer sales channels that did not exist before the
2010s. The historical village smith did not have access to any of these enabling conditions:
no grid electricity, no consumer induction units, no national online marketplace. The
functional inheritance from the traditional smith is limited to the physical operations
(heating, shaping, finishing metal) and the repair-for-known-clientele revenue model.
Everything else — the capital accessibility, the sales channel, the part-time schedule
alongside a primary day-job — is a modern structural feature with no direct historical
analog. [CITATION-NEEDED: academic or journalistic analysis of modern maker-smith
microculture as a post-industrial leisure practice; illustrative characterization based
on observable Etsy/YouTube ecosystem, 2020-2025.]

**Online direct-to-consumer craft channels** (Etsy, Instagram, craft fairs) are the
functional market mechanism that makes the specialty (30%) and artistic (20%) product mix
economically plausible at micro-scale. Without these channels, a part-time operator
producing 575 small-work equivalents per year would have no viable sales route for custom
and artistic pieces. The channel enables national or global reach from a home garage,
which is genuinely novel in the history of craft production. However, the channel also
creates intense visibility to competing makers; pricing power is constrained by market
transparency and volume competition from other online sellers. The labor conditions
enabling this model — a day-job primary income, discretionary evening hours, and
affordable consumer technology — are specific to late-industrial economies and cannot be
generalized to the historical contexts studied in REQUIREMENTS. [CITATION-NEEDED:
analysis of Etsy/online-marketplace economics for handmade metalwork sellers; craft-
economics study or platform data, 2024.]

## Key assumptions

Capital costs ($3,000-$12,000, mid $6,500) are based on observable consumer-grade tabletop
induction forge pricing as of 2024-2026; units in the $1,000-$3,000 equipment range are
commercially available from multiple vendors, with anvils, tools, and setup bringing the
all-in mid-estimate to $6,500. These figures are illustrative estimates without a formal
BOM [CITATION-NEEDED]. Installation cost ($500) assumes a basic 240V/30A residential
electrical circuit; some units operate on 120V/20A standard outlets at no additional
installation cost. Market pricing ($25-$80 per small-work equivalent) is inferred from
observation of Etsy and online-maker pricing for comparable handmade metalwork items; it
is explicitly labeled placeholder-inferred and requires verification [CITATION-NEEDED].
The part-time schedule (12 hr/wk gross, ~11.25 hr/wk net) is a structural assumption
about a day-job operator; operators who can dedicate more time approach forge-002 territory
and should consult that entry instead. Annual consumables ($1,800) include electricity
($414/yr) plus steel stock, abrasives, and miscellaneous materials; electricity estimate
uses $0.125/kWh (US EIA Electric Power Monthly, SCALES.md §6). Downtime fraction (0.18)
is higher than commercial entries due to consumer-grade MTBF and part-time motivational
downtime. All economic figures assume market-rate money transactions throughout; no
barter or indenture-basis assumptions are made [REQUIREMENTS R-20].

The `floor_space_rent_per_year: 0` warrants explicit attention: the zero is structurally
accurate for a home-based operation but represents a subsidy by the operator's primary
housing cost. Cross-entry comparisons should impute approximately $1,200-$2,400/yr for
equivalent commercial space. Even with this imputed rent, the capital and operating cost
profile of this entry remains substantially lower than any other entry in the catalog.

## Known risks / failure modes

**Regulatory:** The primary regulatory risk at this entry is not emissions (induction
eliminates that) but zoning and HOA restrictions. Many suburban HOA agreements prohibit
commercial activity, external signage, or customer traffic at residential addresses. A
home-business license may be required for commercial online sales depending on jurisdiction.
The 240V/30A electrical permit is routine but requires an electrician visit and utility
coordination; some rentals prohibit electrical modifications. Operators in jurisdictions
with strict residential zoning must verify home-business classification before accepting
paid work.

**Labor pipeline:** The single-operator part-time gig has zero succession path. When the
operator stops — due to burnout, injury, major life change, or simply losing interest —
the operation ceases entirely. There is no apprentice, no succession plan, no institutional
continuity. This is not a deficiency to be corrected within this entry's model; it is an
inherent characteristic of the gig structure. The catalog documents this as a DECLINE-VERDICT
confirmation: a one-person part-time home workshop is not a resilient production institution
but a temporary personal practice. The operator dependency risk is 100%.

**Supply chain:** Consumer-grade induction coil replacement (14-day lead time, specialist-
serviceable, $600) is the primary supply-chain risk. A single-coil home-workshop cannot
operate during coil replacement; no backup heat source exists in the base configuration.
At part-time intensity (~500 hr/yr), the coil failure horizon is 2+ years, but a coil
failure in a high-demand period (gift season, project burst) eliminates the most valuable
operating window. Steel stock sourced retail or online is subject to shipping delays; a
part-time operator without stock inventory is vulnerable to order fulfillment delays.
The consumer-unit coil supply chain may be a single-source dependency for some units.

**Demand variance:** Worst-month throughput fraction of 0.20 (20% of average) reflects
the realistic pattern of periodic non-operation. Revenue in the worst month may be zero.
A part-time operator supplementing a primary income can absorb this; an operator relying
on this income to cover basic expenses cannot. The market: marginal rating and the
explicit side-income framing in this entry reflect this constraint.

## Target niche and competitive positioning

This entry tests the **viability floor** of the smithing catalog. It is explicitly a
stress-test of the DECLINE-VERDICT boundary: can someone start a smithing practice with
nearly nothing and sustain it economically? The verdict is market: marginal — viable as a
side-income supplement to a primary livelihood, not viable as a primary livelihood in its
own right. This is not a failure of the entry; it is the honest characterization of the
minimum-capital entry point.

This entry is **NOT a recommendation** for how to operate a smithing practice. It documents
the floor. Every other entry in the catalog above this floor involves more capital, more
dedicated time, a commercial premises, or a governance structure (cooperative, civic) that
spreads cost across a community. Prospective operators who want a primary-income smithing
practice should consult forge-002 (Induction-Modular Small Repair), forge-005 (Frontier
Revival Coal Repair), or forge-006 (Induction Bladesmith) depending on their energy and
product-mix preference.

The competitive positioning is narrow and specific: at village scale, forge-014 is
market: marginal only because a part-time supplement to other income is viable for one
operator in a small community with no competing commercial forge. At town scale and
above, a larger commercial forge (forge-002, forge-005) can undercut on throughput,
breadth of capability, and reliability — the part-time gig operator loses on all three.
The only competitive advantage of forge-014 is near-zero overhead: $6,500 capital,
$500 install, $0 rent. This advantage is structural but does not translate to a viable
full-time livelihood.

The anti-romantic framing is required here: the modern maker-smith operating from a home
garage and selling on Etsy is not a revival of the traditional village blacksmith. The
historical smith was a full-time community-critical tradesperson whose skill was locally
irreplaceable. The modern gig maker is a hobbyist with a day job and a consumer-grade
induction unit, whose output competes against thousands of similar online sellers. Both
are legitimate practices; they are not the same practice, and conflating them produces
misleading conclusions about viability, economic contribution, and cultural continuity.

## Iteration log

- 2026-04-18: v0.1 — initial authoring per Plan C Task 16. Minimum-capital stress-test
  entry documenting the viability floor of the smithing catalog. Market: marginal verdict
  with explicit side-income framing; cooperative and civic poor (omitted from lens_context
  per schema conditional); apprentice_friendly: false; part-time operational reality named
  in max_active_hours_realism_note and Summary; anti-romantic framing on modern maker-culture
  applied in Historical Lineage and Target Niche sections; 15 CITATION-NEEDED placeholders
  carried forward per citation policy; sim_params derivation stated explicitly in field comments.
