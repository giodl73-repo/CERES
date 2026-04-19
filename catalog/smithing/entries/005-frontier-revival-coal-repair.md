---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: forge-005
trade: smithing
name: "Frontier-Revival Coal Repair Forge (single-operator, rural)"
tagline: "Single-operator coal forge optimised for repair-dominant rural market; no-romance revival of the frontier proprietor model"
status: draft
version: 0.1
supersedes: null
inspirations: [american-frontier-smith-1790-1890]

# ── PHYSICAL ENVELOPE ─────────────────────────────────────────────────────────

footprint_m2: 32
ceiling_min_m: 3.5
ventilation: dedicated-exhaust-system

# ── ENERGY ────────────────────────────────────────────────────────────────────

energy_source: coal
energy_consumption_per_active_hour: "8 kg coal"
backup_fuel: charcoal

# ── THROUGHPUT ────────────────────────────────────────────────────────────────

throughput:
  units_per_hour: { small_work: 4, medium_work: 1.2, large_work: 0.3 }
  max_active_hours_per_week: 40
  product_mix:
    repair: 70
    commodity: 10
    specialty: 15
    artistic: 5
  throughput_variance:
    seasonal: "Winter trough for outdoor-equipment repair; spring planting and fall harvest-prep are peak demand periods."
    worst_month_fraction_of_average: 0.5
    best_month_fraction_of_average: 1.4

# ── OPERATOR PROFILE ──────────────────────────────────────────────────────────

operator_skill_floor: journeyman
operators_concurrent: "1"
apprentice_friendly: true
apprentice_path:
  training_stages: "Stage 1 (0–3 mo): fire management, ash cleanup, coal loading, bellows operation, basic safety — gate: operator can maintain a working fire unsupervised. Stage 2 (3–12 mo): small-work shaping, stock preparation, tool handling, horseshoe nail and staple production — gate: consistent quality on small-work items without redirection. Stage 3 (12–24 mo): horseshoe fitting, medium repair work (bracket, clevis, plow-share tip), heat judgment for normalize/anneal — gate: journeyman can close 70% of repair tickets independently. Stage 4 (24–36 mo): full repair range, forge welding, heat treatment, customer diagnosis — gate: fully independent operation."
  time_to_independent_operation: "~36 months to journeyman standard on this equipment; informal model allows earlier partial independence for lower-stakes work"
  succession_note: "Apprentice present during normal production absorbs job knowledge continuously; frontier informal model (working alongside, not a separate classroom program) means skill transfer occurs through shared production days rather than discrete training sessions. Single-operator shop succession depends on apprentice retention — named risk in Known Risks."

# ── ECONOMICS ─────────────────────────────────────────────────────────────────

economics:
  currency: USD
  capital_cost: { low: 15000, mid: 22000, high: 30000 }
  install_cost: 3500
  annual_maintenance: 1200
  annual_consumables: 3000
  floor_space_rent_per_year: 3600
  market_price_per_unit: { low: 35, mid: 50, high: 80 }
  industrial_baseline_price: 10
  pricing_notes: "Unit is one medium-work-equivalent repair or fabrication job. Industrial baseline ($10/unit) reflects factory-produced replacement hardware available through mail-order or farm-supply channels. Rural repair premium is justified by location-bound demand: the customer cannot ship a broken wagon fitting to a factory, and the nearest alternative fabricator may be 30–60 miles away. Customer segment: small farms, horse owners, rural contractors, and property owners with no viable industrial-substitute option for repair work. Pricing is not cost-plus — it reflects the value of having the problem fixed on the same day in the same town. [CITATION-NEEDED: rural repair-service rate surveys; no direct industry survey of smithing repair pricing exists in the sources consulted; figure is inferred from structural analogy to rural auto-repair and farm-equipment service rates.]"
  pricing_validation: "Inferred from structural analogy to rural skilled-trade service rates (auto repair, farm-equipment service) in thin-market rural contexts where no close competitor exists. No direct smithing-repair pricing survey cited in sources. This is the weakest evidentiary link in the entry; a direct survey of operating rural smiths' rate cards would strengthen the claim. Pricing_validation type: structural inference + comparable-service analogy; not a cost-plus residual."

# ── OPERATIONS REALITY ────────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Bellows blower motor (bearing failure)"
      estimated_hours_to_failure: 1800
      replacement_cost: 400
      replacement_lead_time_days: 7
      serviceable_by: journeyman
    - item: "Refractory lining (partial spalling)"
      estimated_hours_to_failure: 2400
      replacement_cost: 400
      replacement_lead_time_days: 7
      serviceable_by: operator
    - item: "Anvil base settling (wood stump or masonry)"
      estimated_hours_to_failure: 3500
      replacement_cost: 200
      replacement_lead_time_days: 3
      serviceable_by: operator

  maintenance_schedule:
    daily:
      task: "Ash pan cleanout, clinker removal from hearth, fire-pot inspection, coal-bin level check, slack-tub water refresh"
      performed_by: operator
    weekly:
      task: "Inspect bellows mechanism and blower housing, sweep chimney flue, check hood-to-flue duct seals, inspect refractory lining for new cracks"
      performed_by: operator
    monthly:
      task: "Full lining and anvil-base inspection, tighten anvil fasteners, inspect and clean ventilation duct interior, check fire-brick condition and mortar joints"
      performed_by: operator
    quarterly:
      task: "Refractory patch as needed (castable refractory), chimney inspection for creosote and ash accumulation, blower-motor lubrication and belt tension check"
      performed_by: journeyman
    annual:
      task: "Deep hearth cleanout including ash-pit, full ventilation system inspection (hood, duct, exterior cap), refractory assessment for full or partial reline, coal storage bin inspection for moisture intrusion"
      performed_by: journeyman

  startup_shutdown_overhead_per_day_min: 45
  max_active_hours_realism_note: "40 hr/wk is stated as net active forging hours for a full-time single operator, already allowing for typical interruptions. Coal startup and shutdown at 45 min/day (5-day week) subtracts 3.75 hr/wk; effective production hours ~36.25 hr/wk. sim_params uses the derated figure (36.25 hr/wk) for throughput calculation."
  interruption_notes: "Customer walk-ins 2–4/day in a rural repair shop (~15 min each); heat cycling pauses between jobs (~10 min); apprentice instruction ~15 min/day. These are folded into the 40 hr/wk ceiling as already-derated net production time."
  consumables_lead_time_days: { typical: 5, worst: 21 }
  throughput_variance:
    seasonal: "Winter trough for outdoor-equipment repair; spring planting and fall harvest-prep are peak demand periods."
    worst_month_fraction_of_average: 0.5
    best_month_fraction_of_average: 1.4
  operator_impact:
    noise_db: 85
    heat_exposure: "High at forge face; sustained radiant heat from coal fire; forced-air ventilation required; summer operation is physically demanding"
    emissions: "Moderate particulate + CO from coal combustion; SO2 present at low levels; dedicated exhaust system is non-negotiable — CO accumulation risk in enclosed shop"
    physical_demand: "Heavy; sustained standing, frequent hammer work, coal handling (~40–50 kg/day), bending over work; not suitable for operators with lower-back or shoulder limitations"

# ── REGULATORY NOTES ──────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Rural and village-scale light-industrial or agricultural-support zoning typically permits coal forge; small-city scale is marginal — coal increasingly restricted in urban cores and many jurisdictions impose particulate-emission limits that are difficult to meet without expensive scrubbing equipment; this entry is NOT recommended for small-city deployment."
  emissions: "Coal combustion triggers OSHA 29 CFR 1926.55 ventilation requirements; local air-quality districts may require particulate permit above certain throughput thresholds; rural exemptions exist in some states for agricultural-support forging; verify before siting."
  other: "OSHA 29 CFR 1910.252(c) hot-work and fuel-storage standards apply; local fire code review required for coal storage quantity; some states have rural-craft or agricultural-support zoning exemptions that simplify permitting — consult local zoning before lease or build."

# ── CONTEXT FIT ───────────────────────────────────────────────────────────────

lens_fit:
  market: good
  cooperative: marginal
  civic: marginal

scale_fit:
  village: good
  town: good
  small_city: marginal

# ── LENS CONTEXT ──────────────────────────────────────────────────────────────

lens_context:
  cooperative:
    membership_boundary: "Local farmers, horse owners, rural contractors, and property owners within the township or county service radius; membership open to any resident willing to pay an annual subscription fee for priority repair access"
    rules_source: "Operating agreement or LLC member agreement; rules set at formation, amended by member vote at annual meeting"
    monitoring: "Job log maintained by operator for each repair ticket; member jobs flagged in log; subscription status checked at drop-off"
    graduated_sanctions: "First missed payment: 30-day grace period with notice; lapsed subscription: non-member pricing applies; non-member pricing is not a penalty but reflects that the cooperative premium only applies to subscribing members"
    conflict_resolution: "Operator arbitrates repair disputes; member disputes over priority access escalate to annual member meeting or, for urgent matters, a phone vote of available members"
    ostrom_principles_addressed: [1, 2, 4]
    member_amendment_process: "Simple majority vote at annual meeting with 14-day advance written notice; emergency amendments by 2/3 phone or email vote with 48-hour notice"
    legal_form: "LLC with member-subscriber agreement; members are not equity holders but hold priority-service rights documented in the operating agreement; jurisdiction-specific formation required"
    scale_fit_note: "Governance rules calibrated for village or small-town scale (under 50 subscribers); quorum and arbitration mechanisms are informal by design, matching the single-operator proprietorship model — this is not a collectively governed production cooperative but a subscription-service cooperative; scales poorly above 100 subscribers without adding governance overhead"

  civic:
    political_coalition: "Town council or county commission support required; rural-development or agricultural-services budget line; likely allies include county farm bureau, small-business association, and rural-infrastructure advocates"
    council_vote_estimate: "Depends heavily on whether a private smith already operates in the area; in a true service gap (no private smith within 30 miles), vote is likely favorable 4-2 or better; opposition likely on tax-burden grounds"
    competes_with_private: "Civic facility is only justifiable in a documented service gap — a remote area where no private smith can sustain a viable market-rate business; a civic forge that displaces a functioning private smith lacks public-goods justification and is not recommended"
    governance_form: "Municipally or county-owned facility; operated by contracted journeyman or master smith; part-time public-smith model in areas where the facility is an essential service rather than an economic development investment"
    budget_line: "Capital via rural-development grant or county general fund; annual operating costs under agricultural-services, emergency-infrastructure, or community-resilience line item"
    benchmark_comparison: "[CITATION-NEEDED: per-household cost comparison for civic smith in village-scale context] At village scale (400 hh), annualized capital ($25,500 over 25 yr = $1,020/yr) plus operating ($7,800/yr) = ~$8,820/yr total, or ~$22/hh/yr — well below the SCALES.md village civic threshold of $120/hh/yr and below library operating costs (~$100/hh/yr per IMLS FY2021). This arithmetic depends on the capital and operating figures cited here; the per-household figure should be recomputed at the actual village population before promotion."
    staffing_model:
      role: "contracted journeyman smith (full-time) with informal apprentice (part-time, household or local-hire)"
      operator_fte: 1.0
      wage_assumption: 48000
      wage_source: "corpus/program/SCALES.md §3 village-scale skilled-trades median ($48,000/yr)"
      hours: "40 hr/wk production and repair service; includes customer reception and job scheduling"
      hiring_notes: "Journeyman smith with coal-forge experience; hiring pool is thin at village scale — regional search radius of 100+ miles may be required; apprentice sourced locally from agricultural-community households following the frontier informal model"
    civic_externalities:
      - "Emergency repair for agricultural infrastructure: a broken plow, wagon, or irrigation fitting during planting or harvest season can halt operations on a small farm; a civic smith provides emergency turnaround that the market cannot guarantee in a thin-demand area"
      - "Apprentice training pipeline: informal apprenticeship under the civic smith produces one journeyman per 3–5 year cycle, sustaining regional repair capacity beyond the original operator's career"
      - "Repair culture: accessible local repair reduces throwaway replacement of metal goods, extending the life of agricultural and infrastructure equipment in communities with limited purchasing power"

# ── SIMULATION PARAMETERS ─────────────────────────────────────────────────────

sim_params:
  cost_mean: 22000
  cost_sd: 3750
  throughput_units_equiv_per_year: 2430
  variable_cost_per_unit: 1.25
  labor_hours_per_unit: 0.70
  downtime_fraction: 0.10
  lifespan_years: 25

# ── RESULTS ───────────────────────────────────────────────────────────────────

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

# ── SOURCES ───────────────────────────────────────────────────────────────────

sources:
  - ref: "Wallace, Anthony F.C. 1978. Rockdale: The Growth of an American Village in the Early Industrial Revolution. New York: Knopf. [Structural reference for household labor and supply-chain dependencies in early American trades.]"
  - ref: "Schlereth, Thomas J. 1991. Victorian America: Transformations in Everyday Life, 1876–1915. New York: HarperCollins. [Material culture reference for late-frontier period smith's context.]"
  - ref: "Atack, Jeremy, and Peter Passell. 1994. A New Economic View of American History from Colonial Times to 1940. 2nd ed. New York: Norton. [Railroad economics, freight rates, manufacturing displacement, nail-production timeline.]"
  - ref: "Gordon, Robert B. 1996. American Iron, 1607–1900. Baltimore: Johns Hopkins University Press. [American iron and steel production, Pittsburgh distribution networks, industrial tool supply.]"
  - ref: "Longfellow, Henry Wadsworth. 1841. 'The Village Blacksmith.' In Ballads and Other Poems. Cambridge, MA: John Owen. [Cited as cultural-trope marker only; not a research source — see Historical Lineage.]"
  - ref: "corpus/program/SCALES.md v1.0 (2026-04-18). Village-scale median wage $48,000/yr; civic cost threshold $120/hh/yr; IMLS FY2021 library operating cost benchmark."
  - ref: "research/cultures/american-frontier/smithing.md v1.0 (2026-04-18). Primary source for frontier smith social organization, product mix, labor regime, supply-chain structure, and decline sequence."
  - ref: "research/trades/smithing/DECLINE-VERDICT.md v1.0 (2026-04-18). Repair-dominant smithing as the historically most durable sub-segment; commodity displacement verdict; labor-regime dependency falsifier."
  - ref: "catalog/smithing/SCHEMA.md v1.0 (schema_base_version 1.1). Smithing-specific throughput ceilings, energy-source table, operator-skill-floor definitions, first_year_failures reference list."
  - ref: "[CITATION-NEEDED: rural repair-service rate surveys — no direct smithing repair-pricing survey identified; figure inferred from structural analogy to rural auto-repair and farm-equipment service rates in thin-market rural contexts. Requires a direct survey of operating rural smiths before promotion to reviewed.]"
  - ref: "[CITATION-NEEDED: coal consumption rate for single-fire coal forge at full operational load — 8 kg/hr is consistent with the catalog/smithing/SCHEMA.md §2 range of 6–10 kg/hr coal; a measured experimental value for a comparable forge configuration would strengthen the claim.]"
  - ref: "[CITATION-NEEDED: US horse population statistics, ca. 1890–1940, for decline narrative in Historical Lineage — Olmstead and Rhode, or USDA historical census series; cited as context only, not a pricing or throughput figure.]"
---

## Summary

Forge-005 is a single-operator coal forge designed for the repair-dominant rural market. Its intended operator is a journeyman smith serving a village or small-town trade area where no industrial substitute is available for same-day, on-site repair of agricultural equipment, wagon hardware, and horseshoes. The entry tests the DECLINE-VERDICT finding that repair-dominant smithing is the historically most durable niche by placing it in the configuration closest to the actual American frontier precedent: coal-fired, low-capital, single-operator, and revenue-driven by labor applied to a customer's problem rather than by volume manufacture. The "frontier revival" label is deliberate and anti-romantic — it revives the small-business proprietor model, not the Longfellow poem.

## Design rationale

Every other smithing entry in the catalog either (a) uses a different fuel (propane, induction, hybrid), (b) operates under a shared-use or civic governance model rather than a private proprietorship, or (c) targets specialty or artistic output rather than repair dominance. Forge-005 occupies the specific cell of the design space that most directly descends from the American frontier record: coal energy, private proprietorship, rural market, journeyman operator, 70% repair mix. This cell matters for CERES because the DECLINE-VERDICT endorses repair-dominant operation as the historically best-supported viable niche, and that endorsement rests primarily on the American frontier evidence. If the endorsement is correct, this configuration should produce the best market-lens outcome of any smithing entry at village and small-town scale. If the economics do not work under favorable assumptions here — low capital, rural premium pricing, no competing private smith — the DECLINE-VERDICT's survival claim requires revision.

## Historical lineage

The American frontier smith (1790–1890) was not a pre-industrial artisan. He was a small-business proprietor operating in an already-industrialized economy, buying bar iron and steel from Pittsburgh by wagon or rail, selling repair labor and fabrication services to a local market that was simultaneously being served by factory-produced goods on an accelerating timeline. The cultural image of the "village blacksmith" — Longfellow's 1841 poem, "a mighty man is he / with large and sinewy hands" — is a Romantic myth, not a business description. The actual frontier smith's labor regime included a wife and children doing bellows work, handling, and bookkeeping without appearing in any formal account; one or two informal apprentices working for room, board, and below-market wages under private indenture; and no guild protection, no masterwork requirement, and no enforced territorial monopoly [research/cultures/american-frontier/smithing.md §§3, 6; Wallace 1978; Schlereth 1991]. This entry carries forward the functional inheritance of that model: low-overhead single-operator proprietorship, household-style informal apprenticeship (adapted to modern labor norms), repair-dominant revenue, and purchased industrial steel stock. It does not carry forward the labor-regime elements that are not reproducible: unpaid household labor and indenture-basis apprenticeship are replaced by a salaried operator and a paid apprentice at market wages, raising the labor cost above what historical accounts imply. The supply-chain structure is reproduced without difficulty: bar steel is commercially available by truck freight from regional distributors, as Pittsburgh iron was by wagon from the Ohio River network [Gordon 1996; Atack and Passell 1994]. The fuel transition (charcoal east of the Mississippi giving way to coal as railroad freight made coal delivery economical) has an exact modern analog: coal is available wherever rail or truck freight reaches, and the entry uses charcoal as a backup for supply-disruption scenarios, matching the historical pattern [research/cultures/american-frontier/smithing.md §4]. The frontier smith's economic role eventually collapsed not because the forge was inadequate but because the working horse was eliminated by the automobile [DECLINE-VERDICT §2.4]. This entry operates in a post-horse economy and makes no claim to restore the horseshoeing demand base; its repair market is agricultural equipment, wagon hardware replacements for recreational and small-farm use, and general rural metalwork — the surviving remnant of the frontier product mix, not a resurrection of the full historical volume.

## Key assumptions

Capital-cost range ($15,000–$30,000, mid $22,000) is based on the smithing schema reference range for a functional single-fire coal repair shop: a used or new coal forge pot ($1,500–$4,000), anvil ($800–$2,500), blower motor ($300–$600), stand and tooling ($1,000–$3,000), fabricated hood and duct system ($1,500–$3,500), coal bin and quench infrastructure ($500–$1,500), hand tools and tongs ($500–$2,000), and building fit-out or contingency ($3,000–$8,000). [CITATION-NEEDED: equipment price survey for used and new coal forge components; figures are consistent with online marketplace data (eBay, Craigslist, specialty smithing suppliers circa 2024–2025) but have not been cross-checked against a formal industry survey.] The mid figure ($22,000) is not the arithmetic mean of low and high ($22,500) — it is slightly below midpoint, reflecting that a competent secondhand sourcer can reach functional operation at mid-to-low cost; the distribution is slightly left-skewed. Install cost ($3,500) covers hood fabrication or connection, chimney or exterior stack, concrete anvil base, and permit fees; this is an estimate derived from comparable small-shop fit-out costs and is flagged for direct verification. Annual maintenance ($1,200) and consumables ($3,000) are estimates: coal at ~8 kg/hr, 36 active hours/wk, 47 productive weeks/yr ≈ 13,500 kg/yr at ~$0.18–$0.22/kg = $2,430–$2,970; rounding to $3,000 inclusive of flux, steel replacement stock, and small consumable parts. [CITATION-NEEDED: retail coal price for small commercial buyers in rural US, 2024–2025; $0.20/kg is used as a central estimate based on publicly reported coal prices for heating-grade bituminous coal at small-quantity purchase, adjusted for metallurgical-grade premium.] Floor-space rent ($3,600/yr) reflects a rural town commercial-bay lease, estimated at $10–$15/sq-ft/yr for 25–30 m² of light-industrial space; this varies widely by region and is flagged as an estimate requiring local verification. The sim_params throughput calculation uses a weighted product-mix rate: 0.70 × 1.2 (medium_work repair) + 0.10 × 4.0 (small_work commodity) + 0.15 × 1.2 (medium_work specialty) + 0.05 × 0.3 (large_work artistic) = 1.435 units/hr equivalent, applied to 36.25 derated hr/wk × 52 wk × 0.90 (1 − downtime_fraction) = 1,696 hr/yr, yielding 2,431 units/yr (rounded to 2,430). The downtime fraction (0.10) reflects seasonal variance (worst month 0.5× average implies roughly 8% of annual capacity in the worst quarter) plus first-year failures and maintenance. cost_sd = (30,000 − 15,000) / 4 = 3,750 per standard derivation. labor_hours_per_unit = 1,696 / 2,430 ≈ 0.70; cross-check: 2,430 × 0.70 = 1,701 ≈ 1,696 ✓. variable_cost_per_unit = $3,000 / 2,430 ≈ $1.23, rounded to $1.25.

## Known risks / failure modes

**Regulatory.** Coal forge zoning is the primary showstopper risk. Rural and village-scale zoning typically permits light-industrial operations including coal combustion; however, the regulatory environment for coal is tightening in many US jurisdictions as air-quality standards are extended to smaller sources and as climate policy creates pressure against solid-fuel combustion. A smithy sited in a community that later adopts stricter air-quality rules faces potential operating-permit denial or expensive retrofitting (scrubbers, particulate capture). This risk is highest at small-city scale, where the entry is already marked marginal for this reason. The operator should verify both current and pending air-quality regulations at the county and state level before committing to a coal configuration; the charcoal backup fuel option provides some resilience but does not eliminate the regulatory footprint of solid-fuel combustion.

**Labour pipeline.** The single-operator model creates acute succession risk. The entire shop's knowledge and customer relationships reside in one journeyman smith; if that smith retires, moves, or is incapacitated, the business effectively ceases. The informal apprenticeship path mitigates but does not resolve this risk: an apprentice who does not complete the full training cycle (or who moves elsewhere) leaves the shop without a successor. This is a documented failure mode of the historical frontier proprietorship model — the shop closed with the proprietor — and is reproduced in any single-operator revival. Journeyman-or-master hiring is additionally difficult in rural markets; the effective labor pool for a rural coal-forge operator is regional (100-mile radius) and thin. An operator who cannot find a willing apprentice has no succession pipeline at all. Mitigation: explicit apprenticeship agreement with retention clause; civic-lens version addresses this through institutional continuity.

**Supply chain.** Coal supply disruption is the primary consumables risk. While coal is broadly available in rural US markets via truck freight, a single-supplier relationship (the only local fuel dealer willing to deliver small quantities of metallurgical-grade coal) creates a dependency with limited redundancy. The charcoal backup addresses this partially but requires a different hearth configuration and carries its own supply uncertainty if charcoal is also single-sourced. Worst-case consumables lead time (21 days) reflects a scenario where the primary coal supplier is out of stock and a regional order must be placed; this requires 3–4 weeks' coal buffer inventory on hand. Steel stock is the secondary supply risk: bar steel is widely available but rural distributors may carry limited sizes; non-standard sections may require 1–2 week lead times. A minimum 4-week steel inventory buffer is advisable.

## Iteration log

- 2026-04-18: v0.1 — initial entry authored per Plan C Task 7. Coal forge, single-operator, repair-dominant, frontier revival framing, anti-romantic. All numeric fields populated or placeholdered per citation policy. Civic and cooperative marginal sketches included per schema requirement. Coal regulatory risk explicit in small-city row and Known Risks. No docs/superpowers/ paths used.
