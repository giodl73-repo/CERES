---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: forge-012
trade: smithing
name: "Farriery Specialist Propane Forge (mobile or shop-based)"
tagline: "Propane-fired farriery practice for equine clientele — route-based or fixed-shop, serving recurring horseshoeing and hoof-care demand"
status: draft
version: 0.1
supersedes: null
inspirations: [american-frontier-horseshoeing-niche, modern-mobile-farrier-trade]

# ── PHYSICAL ENVELOPE ─────────────────────────────────────────────────────────

footprint_m2: 12
ceiling_min_m: 2.4
ventilation: natural-sufficient

# ── ENERGY ────────────────────────────────────────────────────────────────────

energy_source: propane
energy_consumption_per_active_hour: "0.6 kg propane"
backup_fuel: null

# ── THROUGHPUT ────────────────────────────────────────────────────────────────

throughput:
  units_per_hour: { small_work: 3, medium_work: 0.4, large_work: 0.1 }
  max_active_hours_per_week: 35
  product_mix:
    repair: 90
    commodity: 0
    specialty: 10
    artistic: 0
  throughput_variance:
    seasonal: "Winter trough — cold weather reduces horse use and owner willingness to schedule; spring competition-season onset (April–June) and fall trail/hunting season are primary demand peaks."
    worst_month_fraction_of_average: 0.7
    best_month_fraction_of_average: 1.3

# ── OPERATOR PROFILE ──────────────────────────────────────────────────────────

operator_skill_floor: journeyman
operators_concurrent: "1"
apprentice_friendly: true
apprentice_path:
  training_stages: "Stage 1 (0–6 mo): hoof anatomy, basic trimming technique, hand-tool proficiency, and forge safety under direct supervision; competency gate — can trim a quiet horse unassisted. Stage 2 (6–18 mo): hot-shoe fitting, basic forge work (heating, shaping, and nailing standard keg shoes), client-horse handling; competency gate — can complete a standard four-shoe set under journeyman review. Stage 3 (18–36 mo): cold and hot shoeing on difficult horses, corrective-shoe modification basics, client communication and scheduling; competency gate — can operate a full day's route independently with acceptable quality and no safety incidents over a 30-day evaluation window."
  time_to_independent_operation: "~36 months to journeyman-level independent operation; American Farrier's Association (AFA) Certified Journeyman Farrier (CJF) exam pathway is the formal gate; some practitioners operate independently earlier without formal certification."
  succession_note: "Farriery has one of the oldest informal apprenticeship traditions in the smithing trades; many working farriers take on apprentices for part of their career, integrating skill transfer into regular route work. An apprentice riding the route handles simple trims and preparation while the journeyman performs shoeing; this is a natural on-the-job progression path that does not require a separate training program. Formal programs (community-college farriery courses, AFA-endorsed school programs) offer a structured classroom alternative."

# ── ECONOMICS ─────────────────────────────────────────────────────────────────

economics:
  currency: USD
  capital_cost: { low: 15000, mid: 22000, high: 35000 }
  install_cost: 2000
  annual_maintenance: 1500
  annual_consumables: 4200
  floor_space_rent_per_year: 1800
  market_price_per_unit: { low: 120, mid: 185, high: 250 }
  industrial_baseline_price: null
  pricing_notes: "Unit is one full four-shoe set (medium_work equivalent; approximately 1.5–2.5 hr of on-horse time including travel to the stable, setup, shoeing, and cleanup). Industrial horseshoe manufacturing supplies pre-formed keg shoes (the raw material input) but does not substitute for on-horse farriery work — there is no industrial analog that can shoe a horse. The market price range ($120–$250 per set) reflects regional variation and service type: rural regions and basic keg-shoe work trend toward the lower bound; performance-horse and competition-horse markets, corrective shoeing, and urban-fringe recreational-horse markets trend toward the upper bound. Travel premium is typically included in the per-horse rate for mobile practice. [CITATION-NEEDED: AFA or regional farrier rate survey directly documenting per-set pricing; figures are consistent with practitioner-reported rates in trade publications and forums but a formal survey citation is pending.]"
  pricing_validation: "Inferred from practitioner-reported rates and trade-publication discussions in American Farriers Journal and related equine-professional publications; AFA conducts periodic member surveys on service rates but a specific survey citation has not been located for this entry. Evidence type: practitioner-survey inference from trade media; not a cost-plus residual. Formal AFA rate survey or comparable documented rate study required before promotion to reviewed. [CITATION-NEEDED: AFA member rate survey or equivalent formal farrier compensation study.]"

# ── OPERATIONS REALITY ────────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Propane regulator (diaphragm wear or cold-weather freeze-up)"
      estimated_hours_to_failure: 1500
      replacement_cost: 150
      replacement_lead_time_days: 5
      serviceable_by: operator
    - item: "Anvil base settling or portable-anvil mount wear (tripod stand fatigue, stump cracking)"
      estimated_hours_to_failure: 3000
      replacement_cost: 200
      replacement_lead_time_days: 3
      serviceable_by: operator
    - item: "Vehicle maintenance event (for mobile practices — tire, brake, or minor mechanical; annual budget item)"
      estimated_hours_to_failure: 2000
      replacement_cost: 2000
      replacement_lead_time_days: 7
      serviceable_by: specialist

  maintenance_schedule:
    daily:
      task: "Post-visit cleanup: rinse hoof-care tools and rasp, inspect propane hose and fittings for wear or damage, stow all tooling and stock securely, check vehicle (mobile) or forge area (shop) for safety hazards"
      performed_by: operator
    weekly:
      task: "Inspect anvil stand for loosening fasteners or base movement, check propane tank level and manifold connections, inspect tongs and hammers for handle integrity and head security, review rasp and nippers for wear — replace worn rasps on schedule"
      performed_by: operator
    quarterly:
      task: "Full propane regulator test and pressure-drop check, inspect propane hose for cracking or UV degradation, inspect and clean forge burner orifice, check portable anvil stand welds or stump mounting hardware"
      performed_by: operator
    annual:
      task: "Replace propane regulator if approaching rated service life, full forge burner service (clean or replace burner tip), vehicle full service if mobile (oil, filters, brakes, tires), review and restock consumable inventory (shoe blanks, rasps, clinchers, nails)"
      performed_by: operator

  startup_shutdown_overhead_per_day_min: 30
  max_active_hours_realism_note: "35 hr/wk is the gross ceiling for active farriery time on a full route week; in practice, travel between stables, client consultation, and horse-handling overhead consume a further 10–15 hr/wk on a busy mobile route. The 30 min/day startup-shutdown overhead covers forge prep, tool staging, and post-visit cleanup only; it does not capture travel time or horse-handling delays. For a 5-day week, the 30 min/day overhead subtracts 2.5 hr/wk from the gross ceiling, yielding 32.5 hr/wk net active farriery time. sim_params uses 32.5 hr/wk net for throughput calculation. Full-time farriers on a mature route may operate closer to 30–35 horses per week (shoeing) or 8–10 per day (trim-only); the sim_params figure reflects a mix-weighted rate consistent with the product_mix."
  interruption_notes: "Horse-handling delays are a common and unpredictable interruption: a difficult or nervous horse can extend a shoeing from 1.5 hr to 3 hr; early-career farriers experience this more frequently than experienced practitioners with trained client horses. Client scheduling gaps and no-shows are also meaningful — mobile farriers are highly time-sensitive because travel overhead is sunk. These interruptions are folded into the downtime_fraction and the reduced throughput_units_equiv_per_year; they are not separately itemized."
  consumables_lead_time_days: { typical: 3, worst: 14 }
  throughput_variance:
    seasonal: "Winter trough — cold weather reduces horse use and owner willingness to schedule; spring competition-season onset (April–June) and fall trail/hunting season are primary demand peaks."
    worst_month_fraction_of_average: 0.7
    best_month_fraction_of_average: 1.3
  operator_impact:
    noise_db: 75
    heat_exposure: "Low to moderate — propane forge produces local heat at the fire; outdoor or stable-yard work means the forge heat is not contained; summer outdoor work in direct sun raises heat stress risk for a physically demanding trade"
    emissions: "Propane combustion only: CO and combustion products; no particulate, no SOx; outdoor or open-stable work ensures natural dispersion; no permit-triggering emissions under normal operation"
    physical_demand: "High — farriery is physically demanding in a distinctive way: sustained bent-over posture while holding a horse's hoof between the thighs (the farrier's working stance), repeated hammer strikes, heavy rasping, and carrying anvil and tool kit at each stable. Physical toll accumulates over a career; back, shoulder, and knee problems are a documented occupational pattern in the farriery trade. [CITATION-NEEDED: occupational health data on farriery physical toll; general recognition in trade literature but a formal epidemiological citation has not been located for this entry.]"

# ── REGULATORY NOTES ──────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "No fixed-site zoning requirement for a fully mobile practice (home-based tool storage); shop-based practice requires light-agricultural, rural-residential, or light-industrial zoning tolerant of livestock presence if horses are brought to the smith rather than the smith going to the horses"
  emissions: "Propane forge emissions well below permit thresholds under normal single-burner portable use; propane storage subject to NFPA 58 (LP Gas Code) for tank size and location; no particulate or SOx emissions"
  other: "Farriery is an unregulated trade in most US states — no state license required; AFA certification (Certified Journeyman Farrier or higher) is voluntary but widely expected by equine-professional clientele; equine-liability insurance is essential and substantially affects annual operating cost; CDL not typically required for a light-truck and small trailer configuration below GVWR threshold; business license required per county on route"

# ── CONTEXT FIT ───────────────────────────────────────────────────────────────

lens_fit:
  market: good
  cooperative: poor
  civic: poor

scale_fit:
  village: good
  town: marginal
  small_city: poor

# ── LENS CONTEXT ──────────────────────────────────────────────────────────────
# lens_context.cooperative: OMITTED — lens_fit.cooperative is poor; block not required per schema §4.
# lens_context.civic: OMITTED — lens_fit.civic is poor; block not required per schema §4.

lens_context: ~

# ── SIMULATION PARAMETERS ─────────────────────────────────────────────────────

sim_params:
  cost_mean: 22000
  cost_sd: 5000
  throughput_units_equiv_per_year: 550
  variable_cost_per_unit: 7.64
  labor_hours_per_unit: 2.70
  downtime_fraction: 0.12
  lifespan_years: 20

# ── RESULTS ───────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: win
    primary_metric: 0.3063481462873668
    metric_name: payback_years
    notes: ''
  village_coop:
    verdict: fail
    primary_metric: 44.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=44, total_annual_cost=8700
  village_civic:
    verdict: fail
    primary_metric: 13.0
    metric_name: per_household_cost
    notes: per_hh=13.00, threshold=120, hrs/capita=0.000 vs threshold=2.0
  town_market:
    verdict: win
    primary_metric: 0.3063481462873668
    metric_name: payback_years
    notes: ''
  town_coop:
    verdict: win
    primary_metric: 44.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=44, total_annual_cost=8700
  town_civic:
    verdict: fail
    primary_metric: 1.911764705882353
    metric_name: per_household_cost
    notes: per_hh=1.91, threshold=100, hrs/capita=0.000 vs threshold=2.0
  small_city_market:
    verdict: win
    primary_metric: 0.3063481462873668
    metric_name: payback_years
    notes: ''
  small_city_coop:
    verdict: win
    primary_metric: 44.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=44, total_annual_cost=8700
  small_city_civic:
    verdict: fail
    primary_metric: 0.3611111111111111
    metric_name: per_household_cost
    notes: per_hh=0.36, threshold=80, hrs/capita=0.000 vs threshold=2.0
sources:
  - ref: "research/trades/smithing/DECLINE-VERDICT.md v1.0 (2026-04-18). Horseshoeing as smithing's longest-surviving commodity niche; farriery survival via location-bound demand; Stage 2 decline mechanism (automobile displacement of working horse); specialty farriery niche persistence post-automobile."
  - ref: "catalog/smithing/SCHEMA.md v1.0 (schema_base_version 1.1). Throughput ceilings for medium_work and large_work, propane energy-source table and consumption range, operator-skill-floor definitions, first_year_failures reference list (propane regulator, anvil base)."
  - ref: "corpus/program/SCALES.md v1.0 (2026-04-18). Village-scale population and demand context; scale-fit calibration."
  - ref: "[CITATION-NEEDED: AFA (American Farrier's Association) member rate survey or regional farrier compensation study documenting per-set pricing for standard shoeing and trim services; trade-publication references suggest $120–$250 range for shoeing but a formal survey citation is required before promotion to reviewed.]"
  - ref: "[CITATION-NEEDED: AFA Certified Journeyman Farrier (CJF) program documentation — certification pathway, exam structure, time-to-certification norms; cited in apprentice_path.time_to_independent_operation.]"
  - ref: "[CITATION-NEEDED: US horse population statistics, post-automobile — surviving recreational and working horse population, geographic distribution (rural/agricultural concentration); Olmstead and Rhode or USDA agricultural census series; see also DECLINE-VERDICT citation #26.]"
  - ref: "[CITATION-NEEDED: Occupational health literature on farriery physical demands — back, shoulder, and knee injury patterns in the farriery trade; general recognition in trade media but a formal epidemiological source is required for the physical_demand citation in operator_impact.]"
  - ref: "[CITATION-NEEDED: Propane forge energy consumption at farriery scale — 0.6 kg/hr is within the catalog/smithing/SCHEMA.md §2 range of 1–2 kg/hr and reflects a single-burner compact portable forge at partial operational load between heats; measured experimental value for a comparable portable farriery forge required before promotion.]"
---## Summary

Forge-012 is a propane-fired farriery practice: horseshoeing, trimming, and corrective hoof care for equine clientele. The entry is unique in the smithing catalog in that its primary product is not a manufactured object but a service performed on a living animal — the horse's hoof. The intended operator is a journeyman farrier certified (or certification-eligible) through the American Farrier's Association, working either as a mobile practitioner who travels a route of stables, ranches, and equine facilities, or from a small fixed shop where horse owners bring their animals. Capital requirements are the lowest of any forge entry in the catalog, reflecting the minimal forge footprint of farriery work: a portable propane forge, a portable anvil, and a set of hand tools are the full working kit. The entry serves a surviving niche that never went through the generalized smithing-trade collapse documented in the DECLINE-VERDICT: farriery persisted because horse-dependent demand was always location-bound and has continued, in reduced but stable form, into modern equine-recreational and agricultural contexts.

## Design rationale

No other entry in the smithing catalog specifically addresses farriery. Forge-007 (containerized mobile) mentions farriery as a structural analog for mobile pricing, but its operator is a general repair smith, not a farrier; its capital envelope ($35,000–$80,000) is dominated by the container conversion and vehicle, not a farriery kit. Forge-012 occupies a distinct design-space cell: the operator is specifically trained in equine hoof care, the product is defined by horse throughput rather than metalwork units, and the capital structure is simpler and lower-cost than any other mobile smithing configuration in the catalog. The entry exists because farriery's economics are structurally different from general repair smithing: pricing is set by the equine-professional market (not by metalwork complexity), demand is appointment-based and recurring at 4-8 week intervals per horse, and the competitive moat is client trust in the farrier's equine-handling skill and judgment — not forge capability alone. These distinctions justify a dedicated entry rather than treating farriery as a variant of a general repair-smith design.

## Historical lineage

Horseshoeing is the longest-surviving segment of the smithing trade in documented history. The DECLINE-VERDICT records the mechanism clearly: farriery survived because its demand base was inherently location-bound. You cannot ship a horse's feet to a factory. Industrial mass production transformed every other segment of smithing work — nails, hinges, bolts, and hardware moved to factories; plow parts became standardized and distributable — but the horseshoe on a living horse required a skilled practitioner present at the horse. This is the single structural reason why farriery is the only smithing niche that never went through the industrial displacement cycle that collapsed the general smithing trade. The working horse itself was the demand anchor; as long as horses worked, farriers worked.

The decisive break came not from industrial competition but from the automobile. Stage 2 of the American frontier chapter's documented decline (1910s–1930s) replaced the working horse across American agriculture and transportation; the demand for horseshoeing collapsed not because factories could shoe horses better, but because the horses were replaced by machines that did not need shoes. The demand-collapse was thus causal from a different direction than for any other smithing niche [DECLINE-VERDICT §2.3]. The survival of farriery today is a restructuring into a residual niche: horses kept for recreation (eventing, show jumping, dressage, trail riding), competitive sport (racing, cutting, barrel racing), and working ranch purposes. This is a smaller and geographically concentrated market, but it is a real and recurring one. Modern farriery is functionally continuous with 19th-century farriery in every important respect: the operator travels to the horse (the horse cannot come to a fixed shop), the work requires the forge, the anvil, and formed skill judgment, and the relationship between farrier and client is built over years of recurring visits. What the modern entry carries forward from the historical form is this structural logic entire. What it does not carry forward: the working draft horse as the primary client has been replaced by the recreational and sport horse; the demand volume per geographic unit is lower; and the training pathway is now partly formalized through the AFA rather than purely informal guild-style apprenticeship.

## Key assumptions

Capital-cost range ($15,000–$35,000, mid $22,000) covers three components: (1) forge equipment — portable propane forge ($500–$1,500), portable anvil ($300–$800), farriery-specific tooling set (hoof knives, nippers, rasps, clinch cutters, hardy, pritchel, tongs, hammer set: $1,000–$3,000), total forge kit ~$1,800–$5,300; (2) truck or light vehicle for mobile operation ($8,000–$20,000 depending on age and configuration; shop-based operators may already own a vehicle or not require one); and (3) shop buildout if fixed-shop rather than mobile ($3,000–$10,000 for a simple stall-and-forge area on agricultural property or rented space). [CITATION-NEEDED: current retail pricing for portable propane farriery forges, portable farriery anvils, and standard farriery tooling sets; figures are consistent with trade-supplier catalogs and practitioner forum discussions circa 2024–2025 but a formal commercial pricing survey has not been located.] The capital_cost.mid ($22,000) represents a capable mobile setup — a serviceable used light truck, a complete tool kit, and a good portable forge — without new-vehicle cost. The low ($15,000) is a minimal viable setup with an already-owned vehicle; the high ($35,000) includes a newer vehicle or a hybrid mobile-plus-fixed-shop configuration. Install cost ($2,000) covers vehicle-related setup (tool storage box fitting, hitch and trailer wiring if applicable) and initial shop adaptation if fixed-based. Annual maintenance ($1,500) covers tool wear and replacement budget (~$600/yr rasps and nippers are the highest-consumption consumables), vehicle maintenance for mobile practice (~$600/yr), and forge maintenance (~$300/yr). Annual consumables ($4,200) covers propane (~0.6 kg/hr × 1,540 active hr/yr × $1.80/kg ≈ $1,664), steel shoe blanks and keg shoes (~$1,200/yr assuming 500–550 shoeing sets), rasps on a scheduled replacement cycle (~$600/yr), nails and clinchers (~$500/yr), and sundry supplies (~$236/yr); rounded to $4,200. [CITATION-NEEDED: retail propane price $1.80/kg and keg-shoe blank pricing; consistent with LP-gas retail and farrier-supply pricing circa 2024–2025 but formal sourcing required.] Floor-space rent ($1,800/yr) is the midpoint estimate for a shop-based practice using ~12 m² in agricultural or light-industrial space; a fully mobile practice with home-based tool storage has $0 floor-space rent. The stated $1,800/yr represents a blended estimate for a practice that may operate from a rented stall or small covered workspace part-time; authors note the variance and flag it in the known risks section.

The throughput calculation uses a product-mix-weighted rate: dominant channel is medium_work shoeing sets (0.90 × 0.4 units/hr = 0.36) plus specialty corrective work (0.10 × 0.1 units/hr = 0.01), yielding 0.37 units/hr equivalent (where one unit = one full four-shoe set). Net active hours: 35 hr/wk gross minus 30 min/day × 5 days = 2.5 hr/wk overhead = 32.5 hr/wk net. Annual derated hours: 32.5 × 52 × (1 − 0.12) = 32.5 × 52 × 0.88 = 1,486 hr/yr. Throughput: 1,486 × 0.37 ≈ 550 units/yr. Cross-checks: cost_sd = (35,000 − 15,000) / 4 = 5,000; labor_hours_per_unit = 1,486 / 550 = 2.70; cross-check: 550 × 2.70 = 1,485 ≈ 1,486 ✓; variable_cost_per_unit = $4,200 / 550 = $7.64; downtime_fraction (0.12) reflects weather-related schedule disruptions (~4%), horse-handling delays and no-shows (~4%), and equipment-related downtime (~4%); lower than forge-007 (0.18) because this practice has no intermodal container or complex transit logistics. Lifespan (20 years) reflects the durability of hand tools and portable forge equipment under regular maintenance; a mobile vehicle has a shorter service life but the forge kit itself can last a practitioner's full career with tool replacement.

## Known risks / failure modes

**Regulatory.** The primary regulatory risk is equine liability. Farriery involves working on a living animal, and an injury to a horse attributable to shoeing or hoof care — whether a nail driven incorrectly, a corrective shoe that causes lameness, or an accidental cut from a hoof knife — can produce a liability claim from the horse owner. Equine-liability insurance is not optional; its annual cost is a meaningful fixed expense not captured in the economics block's annual maintenance figure and should be treated as a cost-of-revenue item. [CITATION-NEEDED: equine-liability insurance premium ranges for farriers; premium is practitioner-acknowledged in trade media but a specific actuarial or broker citation has not been located.] A second regulatory risk is propane LP-gas storage compliance under NFPA 58: a mobile farrier carrying a 100-lb propane tank in a truck bed or trailer must comply with local vehicle transport rules, which vary by jurisdiction and in some states require specific restraint configurations and ventilation. This is a manageable compliance issue, not a showstopper, but it requires attention.

**Labour pipeline.** Farriery has a genuine apprenticeship tradition, but the physical demands create a distinctive attrition risk: back and knee injuries are a documented occupational pattern in the farriery trade, and an operator who develops a career-limiting physical injury has no ability to hand off work mid-route without a prepared successor. The single-operator model means a health event produces immediate revenue cessation. An operator planning a long-term practice should develop a named succession path — either a trained apprentice ready to assume the route or a referral agreement with a neighboring farrier. The physical toll of farriery is the primary long-run labour-pipeline risk for this entry.

**Supply chain.** Keg-shoe blanks (pre-formed steel horseshoes shaped for hot-fitting) are a commodity input sourced from a small number of major farrier-supply wholesalers (Mustad, St. Croix, Diamond, and regional distributors). Supply disruption is low risk in normal conditions but a sudden shortage of a specific shoe type or size — particularly therapeutic and orthopedic shoe blanks used in corrective work — could delay or cancel specialty services. The practical mitigation is maintaining a 4-6 week stock of the most common shoe sizes and types. Rasps are a consumable with a lead time of 3–14 days from farrier-supply channels; a two-rasp reserve is sufficient buffer for normal operations. Vehicle mechanical failure is the mobile practice's primary supply-chain-adjacent risk: a truck breakdown eliminates the ability to reach client stables and cannot be substituted without a replacement vehicle or a client transport arrangement.

## Iteration log

- 2026-04-18: v0.1 — initial entry authored per Plan C Task 14. Propane farriery specialist, mobile or shop-based, equine clientele. Market-good lens only; cooperative and civic omitted (poor). Industrial baseline N/A (no industrial substitute for on-horse farriery work) — industrial_baseline_price set to null with explanation in pricing_notes. apprentice_path populated per farriery apprenticeship tradition. Horse-health / equine-liability / physical-toll named in Known Risks. Mobile-vs-shop structural alternative documented. Historical lineage: horseshoeing as smithing's longest-surviving niche, surviving via location-bound demand — you cannot ship a horse's feet to a factory. No docs/superpowers/ paths used.
