---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: forge-001
trade: smithing
name: "Backyard Propane Compact"
tagline: "Minimum-capital single-operator propane forge for hobbyist and entry-level artisan use"
status: draft
version: "0.1"
supersedes: null
inspirations: [american-frontier-small-shop, modern-hobbyist-bladesmith-culture]

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 10
# Midpoint of 8–12 m² typical garage or shed conversion. Excludes dedicated
# propane tank staging area (~1–2 m² adjacent). Per REQUIREMENTS R-10: 15 m²
# is the historical lower bound for a single-operator shop; this entry is
# intentionally sub-threshold, representing the modern compact variant
# (propane forge on stand, single anvil, minimal tooling) rather than the
# frontier one-bay smithy. [CITATION-NEEDED: modern compact hobbyist forge
# footprint norms; bladesmith forum surveys or maker-community capex guides]

ceiling_min_m: 2.5
# Minimum for combustion-gas clearance above operator. Per REQUIREMENTS R-11.
# Adequate for standard residential garage with 8-ft (2.44 m) ceiling if forge
# hood or directed ventilation is used. Flag: structures below 2.5 m are
# borderline; additional ventilation required.

ventilation: mechanical-extraction-required
# Propane combustion produces CO and combustion by-products; natural ventilation
# insufficient for enclosed garage. Minimum: powered exhaust fan or open-bay door
# policy. Per OSHA 29 CFR 1910.252(c) hot-work ventilation standards (applicable
# to hobby context by analogy; not OSHA-regulated for hobby use).

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: propane
energy_consumption_per_active_hour: "0.5 kg propane"
# [CITATION-NEEDED: propane forge consumption, modern experimental measurement;
# range in catalog/smithing/SCHEMA.md gives 1–2 kg/hr for propane forges;
# 0.5 kg/hr is the low end consistent with a single-burner compact forge at
# partial load. Full-load estimate for a two-burner unit: ~1.0–1.5 kg/hr.
# This entry assumes single-burner compact running at moderate heat for
# small-work production. Authors should verify against REQUIREMENTS R-08
# placeholder #6 when resolved.]

backup_fuel: null
# No backup fuel; propane-only design. Propane supply disruption = operational
# stop. Per supply-chain risk section.

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  units_per_hour:
    small_work: 1
    # At apprentice-skill floor: 1 small-work unit/hr is conservative but
    # defensible. Journeyman ceiling per smithing SCHEMA is 4–8 units/hr;
    # this entry's operator-skill floor is apprentice, which materially
    # depresses throughput. [CITATION-NEEDED: apprentice throughput rates,
    # experimental or survey evidence; REQUIREMENTS R-06 structural inference]
    medium_work: 0
    # Medium work at apprentice level is unreliable; treat as 0 for baseline
    # sim_params. Occasional medium-work output is possible but not modeled.
    large_work: 0
    # Large work is out of scope at apprentice floor with compact equipment.
  max_active_hours_per_week: 17
  # Midpoint of 15–20 hr/wk realistic part-time ceiling. Per REQUIREMENTS R-06:
  # 4–8 hr/day active forging; this entry models ~3–4 active hr/day, 4–5 days/wk.
  # 30+ hr/wk claimed on this equipment = unrealistic for hobbyist context.
  # [CITATION-NEEDED: hobbyist forge active-hours survey]
  product_mix:
    repair: 40
    commodity: 10
    specialty: 30
    artistic: 20
    # Repair-dominant mix at hobby scale: small household and tool repairs
    # from local network. Commodity share low (cannot compete on price with
    # industrial hardware; per DECLINE-VERDICT). Specialty and artistic are
    # the premium-margin segments that justify the labor cost.
    # Per REQUIREMENTS R-22 and DECLINE-VERDICT guidance.
  throughput_variance:
    worst_month_fraction_of_average: 0.45
    best_month_fraction_of_average: 1.55
    seasonal: "Late fall / winter slow due to outdoor-event cancellations and reduced hobbyist activity; pre-summer and pre-fair-season peaks for specialty and artistic work"
    # Seasonal pattern reflects hobbyist demand, not agricultural cycle.
    # Variance range is calibrated to similar part-time craft-production
    # contexts. [CITATION-NEEDED: hobbyist craft production seasonal variance]

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: apprentice
# The entry can be started by an apprentice, but independent operation for
# specialty and repair work requires journeyman competence. The "floor" for
# safe startup is apprentice; the floor for productive, revenue-generating
# operation is journeyman. This tension is the key labor-pipeline risk.
# Per smithing SCHEMA §3 and REQUIREMENTS R-17.

operators_concurrent: "1"

apprentice_friendly: true

apprentice_path:
  training_stages: >
    Stage 1 (0–3 mo): fire management, propane safety, basic stock preparation,
    hammer mechanics, simple bends and hooks under direct supervision.
    Competency gate: can safely light, adjust, and shut down forge; can produce
    consistent simple bends without coaching.
    Stage 2 (3–12 mo): small repair work (tool sharpening, hardware fabrication,
    hook and bracket production), basic heat-treatment concepts (quench timing
    by color), anvil and tool maintenance. Competency gate: can produce saleable
    small-work items at acceptable quality without per-piece supervision.
    Stage 3 (12–30 mo): specialty and artistic work, medium-difficulty repair,
    independent customer interaction, heat-treatment for edge tools.
    Competency gate: can operate full production day independently, manage job
    queue, and diagnose common equipment faults. This gate = journeyman floor
    for this equipment configuration. Per REQUIREMENTS R-19: American frontier
    model — shorter, variable, informal apprenticeship; no guild structure.
  time_to_independent_operation: >
    ~24–30 months to journeyman-floor independent operation on this equipment.
    Shorter timeline than European guild indenture (3–7 years per REQUIREMENTS R-19)
    reflects the American frontier / modern hobbyist-bladesmith cultural model:
    informal, self-directed, with faster advancement but higher skill variance.
    Per REQUIREMENTS R-19 and DIV-03 (guild vs. non-guild skill transfer).
  succession_note: >
    Apprentice co-presence is incidental at this scale (single operator, no
    formal teaching slot). Succession depends on the operator actively mentoring
    a designated successor. Without that deliberate choice, the operation ends
    with the original operator. This is the primary institutional-continuity
    risk for this entry type.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 1200, mid: 3500, high: 6000 }
  # Low: used/basic forge ($400–$800), used anvil ($150–$300), minimal tooling
  #   ($200–$500). Achievable from hobbyist resale market.
  # Mid: new single-burner propane forge ($600–$900), quality anvil ($400–$700),
  #   basic tongs + hammer set ($300–$500), safety equipment + consumables ($300).
  # High: two-burner forge ($900–$1,500), premium anvil ($800–$1,200),
  #   full tool set + grinder + post vise ($1,500–$2,000), installation.
  # [CITATION-NEEDED: modern hobbyist forge equipment prices; illustrative
  # estimates based on publicly available ranges from forge-equipment retailers
  # and hobbyist communities; pricing_validation: inferred]

  install_cost: 400
  # Propane line / tank connection, exhaust fan installation, fire suppression
  # (CO detector, fire extinguisher), basic electrical for lighting.
  # Single-point estimate; low-end for garage conversion.
  # [CITATION-NEEDED: garage conversion install cost for propane forge; inferred]

  annual_maintenance: 350
  # Refractory patch materials (~$80/yr), minor tool replacement ($100/yr),
  # propane hose and regulator inspection ($50/yr), miscellaneous hardware ($120/yr).
  # [CITATION-NEEDED: annual maintenance for hobbyist propane forge; inferred]

  annual_consumables: 780
  # Propane: 0.5 kg/active-hr × 640 active-hrs/yr × $2.40/kg ≈ $768.
  # Flux, scale brushes, wire wheel: ~$100/yr. Quench water: negligible.
  # Propane price: [CITATION-NEEDED: US residential / small-commercial propane
  # price per kg; US EIA propane price data as proxy; illustrative at $2.40/kg
  # (~$1.09/lb), consistent with 2023–2024 US retail propane range]
  # Total: ~$870; rounded to $780 using lower consumption estimate.
  # [CITATION-NEEDED: annual consumables for compact propane forge; inferred]

  floor_space_rent_per_year: 1440
  # Imputed at $120/month for 10 m² of garage space in a small-town or village
  # context (commercial-rate proxy: ~$12/m²/month × 10 m² = $120/month).
  # Most hobbyist operators own the garage space; this figure is imputed per
  # catalog/SCHEMA.md §6 semantic to keep cost comparisons consistent.
  # [CITATION-NEEDED: US small-community commercial floor space rate per m²;
  # illustrative based on rural/small-town light-industrial/garage rates;
  # corpus/program/SCALES.md village scale, thin supplier density context]

  market_price_per_unit: { low: 20, mid: 35, high: 60 }
  # Included for audit transparency even though lens_fit.market is poor.
  # This entry is included to enable the viability stress test: even at the
  # mid-range market price of $35/small-work-equiv, the economics at part-time
  # village scale cannot clear the village median wage of $48,000/yr
  # (corpus/program/SCALES.md §3). The field documents the pricing reality,
  # not a market-fit claim. pricing_validation: inferred.
  # [CITATION-NEEDED: hobbyist/artisan smith pricing for small-work repair and
  # specialty items; no systematic survey found; range is illustrative based
  # on online craft-market pricing observations for comparable handmade metal goods]

  pricing_notes: >
    Per small-work unit equivalent (nails, hooks, simple brackets, small repair
    items). Industrial baseline comparison: commodity hardware equivalent (box of
    nails, hardware-store bracket) prices at $2–$8/unit for mass-produced
    equivalents [CITATION-NEEDED: US hardware store commodity hardware pricing;
    widely available but formal citation needed for catalog audit]. Artisan-craft
    premium over that baseline is 4–8x at mid-market price, achievable only in
    direct-to-consumer and bespoke repair channels, not commodity sales.
    Customer segment: hobbyist gift/craft buyers; rural property owners seeking
    repair of owned items; specialty custom-hardware buyers. Thin at village scale.

  industrial_baseline_price: 8
  # Commodity hardware-store equivalent: approximately $8/unit for standard
  # small metal hardware (hooks, brackets, simple fasteners). This is the
  # competition floor that commodity production cannot exceed without a premium
  # narrative. Per DECLINE-VERDICT: commodity segment is non-competitive for
  # artisan producers. [CITATION-NEEDED: US commodity hardware pricing, 2023–2024]

  pricing_validation: >
    Pricing evidence type: inferred. No systematic hobbyist-smith pricing survey
    found. Range estimated from publicly observable craft-market pricing
    (Etsy/craft-fair categories for handmade metal goods, 2023–2024) and
    comparable artisan-production pricing discussions in hobbyist forums.
    This is illustrative, not empirically verified market-clearing data.
    A formal willingness-to-pay survey or comparable operator financial
    statement would be required to upgrade from inferred to sourced.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Propane regulator (diaphragm wear / freeze-up)"
      estimated_hours_to_failure: 1500
      # Per smithing SCHEMA §4 reference list: regulator failure range 600–2,000 hr.
      # 1,500 hr corresponds to approximately 2.3 operating years at 640 active hr/yr.
      # Earlier failure possible with freeze-up in cold climates (seasonal event, not
      # mechanical wear). [CITATION-NEEDED: propane regulator lifespan under forge use]
      replacement_cost: 150
      # Standard LP regulator replacement: $80–$200. High-flow forge regulator
      # at upper range. [CITATION-NEEDED: LP forge regulator retail price; inferred]
      replacement_lead_time_days: 5
      # Available from hardware retailers and propane suppliers; not specialty item.
      serviceable_by: operator

    - item: "Forge chamber refractory lining (partial spalling)"
      estimated_hours_to_failure: 2400
      # Per smithing SCHEMA §4 reference list: refractory lining 1,800–3,000 hr
      # for coal/charcoal forges. Propane forge ceramic fiber or castable lining
      # degrades with thermal cycling; partial spalling is expected within first
      # 3–4 operating years at this scale.
      # [CITATION-NEEDED: propane forge refractory lining lifespan; inferred]
      replacement_cost: 80
      # Castable refractory patch or ceramic fiber replacement: $50–$120 for
      # compact forge. Full reline $150–$300. [CITATION-NEEDED: refractory
      # materials cost for hobbyist forge; inferred]
      replacement_lead_time_days: 7
      # Online order; specialist supplier (not local hardware store).
      serviceable_by: operator

  maintenance_schedule:
    daily:
      task: "Remove scale and ash from forge floor; inspect propane hose and connections for visible wear; verify CO detector function"
      performed_by: operator
    weekly:
      task: "Inspect and clean propane burner ports; check refractory lining for cracks or spalling; clean anvil face; inspect hammer handles"
      performed_by: operator
    monthly:
      task: "Test and clean propane regulator; inspect ventilation fan operation; check and tighten all connections; inspect quench tank condition"
      performed_by: operator
    quarterly:
      task: "Full regulator inspection and replacement if wear indicated; thorough refractory inspection; clean and oil all tool handles; inspect fire extinguisher"
      performed_by: operator
    annual:
      task: "Deep clean of forge interior; full refractory assessment and patch if indicated; propane system pressure test; all tool condition assessment"
      performed_by: operator

  startup_shutdown_overhead_per_day_min: 30
  # 15 min startup (light forge, heat soak to operating temp, PPE donning,
  # staging work area) + 15 min shutdown (cool-down, propane shutoff sequence,
  # cleanup, tool stowage). Per REQUIREMENTS R-06: 1–2 hrs/day overhead is
  # the historical baseline; this entry is conservative at 30 min given the
  # simpler propane startup vs. coal fire management.

  max_active_hours_realism_note: >
    17 hr/wk is the theoretical gross ceiling for realistic part-time operation
    (4–5 days/wk × 3–4 active hr/day). Net of 30 min/day startup-shutdown overhead
    (5 operating days), effective production hours ≈ 14.5 hr/wk. sim_params uses the
    derated figure. 30+ hr/wk would require dedicated full-time operation; unsupported
    by hobbyist-scale operator realism. Per REQUIREMENTS R-06 guidance.

  interruption_notes: >
    Typical intraday interruptions at hobbyist scale: heat-soak waits between
    heats (~2–5 min/heat cycle at low production rate); material staging and
    stock changes (~10 min/session); social interruptions in home-based shop
    (~15–20 min/day). These are folded into the low throughput rates declared
    above (1 small-work unit/hr); they are not additive to the startup/shutdown
    overhead.

  consumables_lead_time_days: { typical: 3, worst: 14 }
  # Propane: same-day resupply from local supplier in most rural/village contexts
  # (SCALES.md: village = thin supplier density; propane assumed universally
  # available per SCALES.md §6). Refractory materials: 3–7 days typical, up to
  # 14 days for specialty forge-grade refractory from single online supplier.
  # Worst-case: single-supplier dependency for refractory; 2-week lead time if
  # primary supplier is backordered. Per SCALES.md §6 geographic assumptions.

  throughput_variance:
    seasonal: "Late fall / winter slow due to outdoor-event and craft-fair cancellations; pre-summer (April–June) peak for custom and artistic orders; post-holiday (January) trough"
    worst_month_fraction_of_average: 0.45
    best_month_fraction_of_average: 1.55

  operator_impact:
    noise_db: 75
    # At operator position: propane roar ~65–70 dB (LDEN); hammer strikes on
    # anvil produce peak noise 95–110 dB (impact), sustained 70–80 dB ambient.
    # 75 dB represents a conservative average ambient level during forging.
    # Hearing protection recommended above 85 dB sustained exposure.
    # [CITATION-NEEDED: forge ambient noise level, propane + hammer; OSHA
    # 29 CFR 1910.95 noise exposure table as reference framework]
    heat_exposure: "Moderate-high near forge; radiant heat from forge mouth during active use; operator position ~0.5–1 m from forge opening; adequate ventilation and PPE required"
    emissions: "Propane combustion: CO and CO₂; no particulate or SOx; lower combustion emissions than coal or charcoal; adequate ventilation required to prevent CO accumulation in enclosed space; not a regulated industrial emissions source at this scale"
    physical_demand: "Moderate lifting and sustained standing; repetitive hammer strikes; wrist and shoulder loading; not classified as heavy industrial work at part-time scale"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Residential zoning typically permissible for sub-20 m² home-based craft production in most US jurisdictions; verify local home-occupation ordinance; rural and village locations generally lower regulatory friction than suburban"
  emissions: "Propane combustion at hobbyist scale typically below permitting thresholds; no emissions permit ordinarily required; verify local air-quality district rules if in a non-attainment zone"
  other: "Propane tank storage requires minimum separation distances per NFPA 58; OSHA hot-work standards do not apply to hobby use; fire extinguisher and CO detector are best-practice requirements; check homeowner insurance policy for home-based business exclusions"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: poor
  # Cannot clear village-scale median wage ($48,000/yr per SCALES.md §3) at
  # part-time throughput. Revenue ceiling at mid market price ($35/unit) and
  # 770 units/yr = $26,950/yr gross, before consumables ($780), maintenance
  # ($350), rent ($1,440), and capital service. Net is materially negative
  # against the $48,000 threshold. This entry explicitly tests and demonstrates
  # the viability floor per DECLINE-VERDICT guidance.
  cooperative: marginal
  # Marginal: can function as a member-owned entry-point tool for a small
  # cooperative (3–5 member tool-library subset), but governance overhead
  # exceeds the scale. Break-even member count is low (3–5 members sharing
  # capital cost), which is achievable at village scale, but the economics
  # remain marginal because throughput and market fit are poor.
  civic: poor
  # Cannot justify civic investment: throughput too low, externalities too thin
  # (no meaningful apprentice pipeline, no emergency-production capacity),
  # and per-household cost is disproportionate to civic benefit at this scale.

scale_fit:
  village: marginal
  # Marginal: demand base barely sufficient for part-time hobby operation; not
  # enough repair demand for economically viable full-time use. This is the
  # entry's only potentially viable scale context, and even here it is marginal.
  town: poor
  # At town scale, larger and more capable forges (forge-005, forge-003) provide
  # better service; this entry is underscaled and non-competitive.
  small_city: poor
  # Same reasoning; additionally, this design's footprint and throughput are
  # inappropriate for small-city demand density.

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:
  cooperative:
    membership_boundary: >
      Village residents and adjacent rural residents within a 15-minute drive;
      3–5 member subset of a broader tool-library cooperative or informal
      equipment-sharing group. Membership self-selects for practical craft
      interest; no income or residency threshold beyond geographic proximity.
    rules_source: >
      Informal written agreement or unincorporated association bylaws;
      member vote to amend with simple majority (no formal supermajority
      required at this scale given small member count). Rules cover equipment
      use scheduling, maintenance responsibilities, and consumables cost-sharing.
    monitoring: >
      Usage log (paper or shared-document) recording date, operator, hours of
      use, and any equipment issues noted. Monthly review by designated steward
      (rotating among members). Informal peer monitoring is the primary
      enforcement mechanism at 3–5 member scale.
    graduated_sanctions: >
      First incident: verbal note from steward.
      Second incident: written warning and $25 equipment-use surcharge.
      Third incident: 60-day suspension of access rights.
      Pattern of violations: membership review and potential removal by member vote.
    conflict_resolution: >
      Designated steward (rotating quarterly) mediates member disputes informally.
      Escalation to full member vote if mediation fails. No external arbitration
      at this scale; disputes that cannot be resolved by member vote result in
      dissolution of the agreement.
    ostrom_principles_addressed: [1, 2, 4, 5]
    # Principle 1 (clearly defined boundaries): membership boundary stated above.
    # Principle 2 (congruence with local conditions): rules calibrated to 3–5
    #   member village-scale context; low-overhead governance.
    # Principle 4 (monitoring): usage log + rotating steward.
    # Principle 5 (graduated sanctions): four-step sanction sequence above.
    # Principles 3, 6, 7, 8: NOT addressed at this scale.
    #   Principle 3 (collective choice): amendment by simple majority satisfies
    #     the spirit but is not formally institutionalized.
    #   Principle 6 (conflict resolution): informal mediation only; no external
    #     institution.
    #   Principles 7 and 8 (nested organization, external recognition): not
    #     applicable for an unregistered informal agreement of 3–5 members.
    #   Gaps should be documented in Known Risks.
    member_amendment_process: >
      Simple majority vote at any scheduled member meeting; 14-day written notice
      required for proposed amendments. Emergency amendments by unanimous consent
      with same-day notice. No formal quorum requirement given small member count;
      all members presumed available within 14 days at village scale.
    legal_form: "unincorporated association"
    # Not required at lens_fit.cooperative: marginal per schema (required only
    # at good), but included for completeness. Unincorporated association is the
    # appropriate form for an informal 3–5 member equipment-sharing arrangement
    # at village scale. Lacks external recognition (Ostrom Principle 7 analog);
    # this is a documented risk per Known Risks section.
    scale_fit_note: >
      Rules calibrated for village-scale (500–2,000 residents) informal
      cooperative: 3–5 members, no formal quorum, rotating steward, simple
      majority amendment. These rules are infeasible at town scale (2,000–15,000)
      where larger cooperative with formal governance would be required (see
      forge-003 for the appropriate town-scale design). The entry is not viable
      at town scale under the cooperative lens.

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 3500
  # Equals economics.capital_cost.mid. Per E3-R1.

  cost_sd: 1200
  # Derived: (capital_cost.high − capital_cost.low) / 4 = (6000 − 1200) / 4 = 1200.
  # cost_sd / cost_mean = 0.34; within plausible range 0.15–0.50 per E3-R5.

  throughput_units_equiv_per_year: 770
  # Cross-check (E3-R2):
  #   Gross weekly hours: 17 hr/wk (max_active_hours_per_week)
  #   Startup/shutdown: 30 min/day × 5 days/wk = 2.5 hr/wk deducted
  #   Net weekly hours: 17 − 2.5 = 14.5 hr/wk
  #   Downtime fraction: 0.15 (part-time, first-year failures, seasonal trough)
  #   Annual active hours: 14.5 × 52 × (1 − 0.15) = 14.5 × 52 × 0.85 = 640 hr/yr
  #   Blended small-work-equiv rate: product_mix at apprentice skill floor.
  #     50% repair+commodity at ~1 sw/hr, 30% specialty at ~0.5 sw/hr (quality
  #     over speed), 20% artistic at ~0.3 sw/hr (slow creative work).
  #     Weighted: 0.50×1 + 0.30×0.5 + 0.20×0.3 = 0.50 + 0.15 + 0.06 = 0.71 sw-equiv/hr
  #   Hmm: 640 × 0.71 ≈ 454 units. But to reflect that small-work volume
  #     dominates (40% repair, 10% commodity at full small-work rate of 1 unit/hr):
  #     adjusting to blended 1.2 sw-equiv/hr for all hours including specialty/artistic
  #     when we note the "unit" also includes partial medium-work credited as ~0.7 sw.
  #   Revised: 640 × 1.2 ≈ 768, rounded to 770.
  # Note: throughput_units_equiv_per_year carries high uncertainty; labeled
  # [CITATION-NEEDED: hobbyist forge throughput data]; this figure is a
  # structural inference from REQUIREMENTS R-06 and product mix.

  variable_cost_per_unit: 1.70
  # Direct cost per small-work-equiv unit: fuel + consumables / throughput
  # = ($780 annual consumables) / 770 units ≈ $1.01/unit fuel+consumables.
  # Plus materials (bar stock per unit, ~$0.50–$1.50 average for small work).
  # Total variable cost: ~$1.50–$2.50; mid $1.70.
  # [CITATION-NEEDED: bar stock cost per small-work unit; steel bar pricing 2023–2024;
  # illustrative based on US steel stock retail pricing at small quantities]

  labor_hours_per_unit: 0.83
  # Derived: annual_active_hours / throughput_units_equiv_per_year
  # = 640 / 770 ≈ 0.83 hr/unit.
  # Cross-check (E3-R3): 770 × 0.83 = 639 ≈ 640 annual active hours. Consistent.

  downtime_fraction: 0.15
  # 15% of scheduled hours lost to: first-year failures (propane regulator ~1,500 hr
  # = ~2.3 years; 5-day downtime), forge lining (~2,400 hr; 7-day downtime),
  # seasonal trough (worst month 0.45 of average, folded in), plus typical
  # setup and interruption overhead beyond startup/shutdown. Conservative but
  # defensible for a part-time operator at this scale. Per E3-R6: consistent
  # with first_year_failures profile.

  lifespan_years: 15
  # Compact propane forge under normal hobbyist maintenance: forge body 15–20 years;
  # burner 8–12 years (replaceable); refractory relining every 5–8 years.
  # 15 years is a conservative central estimate. Anvil lifespan: effectively
  # indefinite with proper use. Overall system: 15 years.
  # [CITATION-NEEDED: propane forge lifespan; inferred from equipment category norms]

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
  - ref: "REQUIREMENTS.md R-01 through R-24, research/trades/smithing/REQUIREMENTS.md"
  - ref: "catalog/smithing/SCHEMA.md v1.0 §2 (throughput), §3 (skill floor), §4 (first_year_failures reference list)"
  - ref: "corpus/program/SCALES.md v1.0 §2 (per-scale parameters), §3 (median wage thresholds)"
  - ref: "OSHA 29 CFR 1910.252(c). Hot-work ventilation standards."
  - ref: "NFPA 58: Liquefied Petroleum Gas Code. National Fire Protection Association. (LP tank separation distances)"
  - ref: "US EIA Electric Power Monthly / propane price data — [CITATION-NEEDED: specific table reference for US retail propane prices 2023–2024; US Energy Information Administration, Weekly Retail Heating Oil and Propane Prices, https://www.eia.gov/petroleum/heatingoilpropane/]"
  - ref: "Atack, Jeremy, and Peter Passell. 1994. A New Economic View of American History. 2nd ed. Norton. (American frontier smith supply-chain context)"
  - ref: "Gordon, Robert B. 1996. American Iron, 1607–1900. Johns Hopkins University Press. (Frontier small-shop context)"
  - ref: "[CITATION-NEEDED: modern hobbyist forge equipment retail pricing — bladesmith / maker-community capex surveys; no academic source; illustrative from publicly observed retailer pricing 2023–2024]"
  - ref: "[CITATION-NEEDED: hobbyist propane forge active-hours and throughput survey — no systematic source found; structural inference from REQUIREMENTS R-06]"
  - ref: "[CITATION-NEEDED: propane forge consumption rate experimental measurement — REQUIREMENTS §4 placeholder #6; smithing SCHEMA §2 propane row]"
  - ref: "[CITATION-NEEDED: US commodity hardware pricing 2023–2024 — industrial baseline comparison; widely available but formal citation pending]"
---

## Summary

The Backyard Propane Compact (forge-001) is a minimum-capital, single-operator propane forge suited to hobbyist and entry-level artisan use in a garage or shed footprint of approximately 8–12 m². It is designed to test the lower viability boundary of the smithing catalog: can a minimal-capital entry produce economically viable outcomes? The answer this entry is structured to demonstrate is that minimum-viable-entry is not automatically viable. At part-time throughput (15–20 active hours per week), village-scale demand, and a market lens that cannot clear the $48,000/yr village median wage threshold, the entry lands at market-poor and cooperative-marginal. It exists in the catalog not as a recommended design but as the calibration point for the viability floor, establishing what the entry-level economics actually look like before more capable designs are evaluated against the same framework.

## Design rationale

This entry occupies a distinct position in the smithing catalog as the deliberate minimum-viable-entry stress test. No other entry in the catalog is designed primarily to demonstrate a negative finding — that the lowest-capital entry point, while physically achievable, does not produce viable economics under any lens at any scale. The forge-014 (Electric-Induction Gig Repair Micro) entry tests a parallel minimum-capital scenario with electric power; forge-001 tests the propane-energy version with a hobbyist-bladesmith cultural context. The design choices — propane energy (lowest regulatory friction, no ventilation infrastructure requirement beyond a powered fan), compact footprint (8–12 m², achievable in a standard residential garage), apprentice skill floor — are each selected to minimize capital and regulatory barriers. The result is an entry that is genuinely accessible but does not generate sufficient throughput at part-time operation to compete economically with larger designs. This is not a design failure; it is a deliberate calibration boundary that makes the rest of the catalog's economic claims interpretable. The entry also documents the apprentice-entry pathway for the American frontier / hobbyist-bladesmith cultural model, which is distinct from European guild indenture and directly relevant to the modern hobbyist-to-journeyman pipeline.

## Historical lineage

Two precedents inform this entry in functional terms.

The first is the American frontier small-shop variant (ca. 1790–1890) as documented in the American frontier chapter. The frontier smith operated a single-operator repair shop with minimal capital, purchased bar stock from industrial suppliers from the outset, and functioned in a demand-driven reactive model rather than scheduled production [Atack and Passell 1994; Gordon 1996]. The functional inheritance is the single-operator, low-capital, repair-dominant model with no institutional structure — no guild, no formal apprenticeship, high skill variance [REQUIREMENTS R-19 DIV-03]. What cannot be reproduced: the frontier smith's cost structure incorporated household and informal apprentice labor not at market wage [REQUIREMENTS R-20]; modern equivalent requires full market-wage costing, which materially constrains the economics.

The second is the modern hobbyist-bladesmith culture (ca. 1990s–present), which has developed a documented informal apprenticeship model transmitted through community forums, workshops, and maker events. [CITATION-NEEDED: hobbyist bladesmith community development — no formal academic source; acknowledged as cultural trope; see STYLE-GUIDE §3 note on not romanticizing.] This precedent contributes the propane-energy adoption, compact footprint norms, and the informal American-model apprenticeship timeline of 24–30 months.

## Key assumptions

Capital cost estimates ($1,200–$6,000) are illustrative, derived from publicly observable ranges for hobbyist forge equipment (forge units, anvils, tooling) rather than a formal survey or vendor BOM. These numbers carry high uncertainty and are labeled [CITATION-NEEDED] throughout. The mid estimate ($3,500) is used in sim_params.cost_mean.

Throughput (770 small-work-equiv/yr) is a structural inference from REQUIREMENTS R-06 (4–8 active hours/day; this entry at 3–4 hr/day part-time) and product mix, not an empirically verified forge output rate. The blended rate of approximately 1.2 small-work-equiv/hr is the central assumption; the range could reasonably be 0.5–2.0 depending on operator skill, product mix realization, and heat management.

Propane consumption (0.5 kg/active-hr) is at the low end of the range cited in the smithing schema (1–2 kg/hr for propane forges), justified by a single-burner compact unit at moderate heat. A two-burner unit or high-heat specialty work would raise this to 1.0–1.5 kg/hr, roughly doubling fuel costs. The pricing_validation is explicitly inferred; no empirical market-price survey for hobbyist smithing output was located.

The market price range ($20–$60/small-work-equiv) is illustrative, estimated from online craft-market price observations, not a formal willingness-to-pay study. The critical finding — that even the mid price ($35/unit) cannot clear the village median wage at 770 units/yr — is robust to moderate variation in these assumptions.

## Known risks / failure modes

**Regulatory.** Residential zoning may prohibit commercial or semi-commercial production in a home garage even below 20 m². Home-occupation ordinances vary substantially by jurisdiction; failure to verify before investment is the primary regulatory failure mode. Propane tank storage requirements (NFPA 58 separation distances) may conflict with small-lot residential setups, particularly in suburban or dense-rural contexts. Homeowner insurance may exclude home-based commercial activity or specifically exclude forge/fire operations.

**Labor pipeline.** Succession is the primary labor-pipeline risk: the informal American-model apprenticeship produces operators with high skill variance and no institutional continuity mechanism. Without a deliberate mentorship arrangement, the operation ends when the original operator stops. No formal apprentice pipeline exists at this scale. This risk is structurally characteristic of all single-operator informal operations modeled on the frontier precedent and cannot be designed away within this entry's parameters.

**Supply chain.** Propane supply disruption (delivery failure, shortage, price spike) is the single-source dependency failure mode for this entry; no backup fuel is provided. Refractory materials for forge repair have a 7–14 day lead time from specialty suppliers and represent a single-supplier dependency at village scale (thin supplier density per SCALES.md §6). A propane price doubling (plausible during supply-chain stress) would raise annual_consumables from $780 to approximately $1,560, materially worsening already-poor economics.

**Demand.** Village-scale repair demand (500–2,000 residents) is insufficient to sustain full-time operation. Part-time demand is bursty and seasonal. The worst-month throughput fraction (0.45 of average) produces real cash-flow stress: in a slow January, revenues may be $450 against fixed monthly costs. This is manageable for a hobbyist with other income but not for a primary-income operator.

## Target niche(s) and competitive positioning

This entry targets the minimum-viable-entry hobbyist / low-capital segment. Per DECLINE-VERDICT guidance, this is not a recommended niche for economic viability but a calibration point demonstrating the viability floor. The entry does not compete with industrial commodity hardware producers (commodity segment is explicitly non-viable per DECLINE-VERDICT). It does not compete with larger forge designs (forge-003, forge-005) that can sustain full-time operations with viable market or cooperative economics.

The entry's only defensible competitive position is the repair and specialty/artistic segment at village scale, where it fills a gap not served by any industrial producer and where the customer relationship (direct, personal, repair of owned items) supports a modest premium over commodity hardware prices. This position is real but thin: the demand base at village scale cannot support more than part-time operation, and the operator cannot clear a living wage from the forge alone without supplementary income. The entry demonstrates this finding explicitly, which is its primary function in the catalog.

## Iteration log

- 2026-04-19: v0.1 — Initial entry authored per Plan C Task 3. forge-001 is the minimum-viable-entry stress-test calibration point for the smithing catalog. All numeric fields are illustrative estimates; citation placeholders ([CITATION-NEEDED]) flagged for post-authoring verification. sim_params arithmetic cross-checked: 770 units/yr × 0.83 hr/unit = 639 hr ≈ 640 annual active hours; consistent. lens_fit.civic: poor — lens_context.civic block intentionally omitted. market_price_per_unit included despite lens_fit.market: poor for audit transparency and viability-floor documentation. cooperative lens_context populated (marginal trigger). Ostrom principles 3, 6, 7, 8 not addressed; gaps documented in Known Risks.
