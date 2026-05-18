# CERES Capability Expansion

Source: `ceres-expansion` agent run.  
Status: proposal set for rubric-driven expansion.

CERES should expand through validated local-production capabilities while keeping
route geography in PORTO, identity in CANON, game rules in downstream games, and
shared validation plumbing in RALLY.

## Capability candidates

| Capability id | Title | Pressure |
|---|---|---|
| `ceres-capability:ceramics-kiln` | Community kiln systems | facility/production: firing capacity, ventilation, fuel |
| `ceres-capability:woodworking-shop` | Local woodworking shops | production/labor: joinery skill, tool access |
| `ceres-capability:leatherworking` | Leather repair and goods | storage/market: hides, tanning inputs, niche demand |
| `ceres-capability:milling-grain` | Grain mill dependency | facility/storage: upstream flour bottleneck |
| `ceres-capability:butchery-charcuterie` | Small butchery/curing | storage/regulatory: cold chain, inspection |
| `ceres-capability:dairy-creamery` | Micro-creamery | storage/facility: refrigeration, sanitation |
| `ceres-capability:soap-rendering` | Soap/candle rendering | production/storage: fats, lye, scent inputs |
| `ceres-capability:glass-studio` | Small glass hot shop | facility/energy: furnace heat, safety |
| `ceres-capability:paper-print` | Paper and print workshop | production/market: stationery, civic documents |
| `ceres-capability:brewery-cidery` | Local fermentation works | storage/market: tanks, licensing, seasonal demand |
| `ceres-capability:facility-spec-library` | Generic facility archetypes | shared vocabulary beyond entries |
| `ceres-capability:multi-trade-makerspace` | Civic makerspace bundle | shared tools, scheduling, labor |
| `ceres-capability:mobile-workshop` | Mobile production units | route-dependent demand |
| `ceres-capability:seasonal-popups` | Seasonal production pop-ups | temporary demand peaks |
| `ceres-capability:shared-storage` | Shared raw-material storage | inventory, spoilage, security |
| `ceres-capability:energy-backup` | Backup fuel/energy resilience | outages and fuel switching |
| `ceres-capability:ventilation-permit` | Ventilation and emissions classes | zoning constraints |
| `ceres-capability:tool-library-governance` | Tool-library operating model | booking, maintenance, sanctions |
| `ceres-capability:civic-budget-benchmarks` | Civic service comparator set | household cost defensibility |
| `ceres-capability:apprentice-school-facility` | School-linked training shop | succession pipeline |
| `ceres-capability:input-dependency-map` | Upstream input dependency map | missing suppliers |
| `ceres-capability:perishable-inputs` | Perishable-input modeling | spoilage, cold chain |
| `ceres-capability:bulk-purchase-coop` | Bulk purchasing cooperatives | member pooled inputs |
| `ceres-capability:local-substitute-index` | Local substitute materials | alternatives under shock |
| `ceres-capability:import-exposure-score` | Import exposure scoring | external route fragility |
| `ceres-capability:waste-byproduct-loop` | Byproduct reuse loops | waste into inputs |
| `ceres-capability:maintenance-parts-risk` | Spare-parts risk register | downtime from parts |
| `ceres-capability:inventory-carry-cost` | Inventory carrying cost model | capital tied in stock |
| `ceres-capability:hazardous-materials` | Hazardous input handling classes | fire, chemical, emissions |
| `ceres-capability:regional-input-atlas` | Regional input availability hooks | place-specific feasibility |
| `ceres-capability:skill-floor-taxonomy` | Cross-trade skill taxonomy | apprentice/journeyman floors |
| `ceres-capability:apprentice-throughput` | Apprentice throughput model | training reduces output |
| `ceres-capability:succession-risk` | Succession failure scenarios | operator retires or leaves |
| `ceres-capability:operator-health-load` | Operator health/load index | heat, noise, ergonomics |
| `ceres-capability:multi-operator-crews` | Crew-size economics | concurrent staffing |
| `ceres-capability:guild-patterns` | Guild/cohort governance patterns | standards, exclusion, mentoring |
| `ceres-capability:volunteer-burnout` | Volunteer burnout model | unpaid staffing failure |
| `ceres-capability:skill-transfer-cost` | Skill-transfer cost ledger | teaching time as cost |
| `ceres-capability:certification-friction` | Licensing/certification friction | legal operator constraints |
| `ceres-capability:inclusive-access` | Access and exclusion checks | who can use facilities |
| `ceres-capability:demand-pool-estimator` | Demand-pool estimator | customers by scale |
| `ceres-capability:industrial-substitution` | Industrial competitor baseline library | price pressure |
| `ceres-capability:premium-segment-map` | Premium niche segmentation | artisan premium viability |
| `ceres-capability:repair-demand-model` | Repair demand estimator | local durable-goods repair |
| `ceres-capability:civic-externalities` | Civic externality scoring | education, resilience, access |
| `ceres-capability:coop-member-pool` | Cooperative member-pool refinement | member participation |
| `ceres-capability:price-sensitivity-band` | Price sensitivity bands | premium tolerance |
| `ceres-capability:seasonality-demand` | Seasonality demand profiles | peak/trough operations |
| `ceres-capability:wholesale-vs-retail` | Wholesale/retail channel split | throughput and margin |
| `ceres-capability:public-procurement` | Civic procurement channel | schools, libraries, parks |
| `ceres-capability:tier-b-dependency` | Tier B inter-trade dependency graphs | cascade risk |
| `ceres-capability:tier-c-succession` | Tier C succession shocks | operator pipeline failure |
| `ceres-capability:scenario-fixtures` | Scenario fixture library | repeatable validation cases |
| `ceres-capability:validation-anchors` | Known-parallel validation anchors | real-world sanity checks |
| `ceres-capability:rally-evidence-pack` | RALLY evidence packet standard | portable run/report artifacts |
| `ceres-capability:banish-economy-gate` | BANISH economy gate templates | facility/storage/labor alternatives |
| `ceres-capability:porto-location-hooks` | PORTO location hook schema | terrain, climate, routes |
| `ceres-capability:facility-unlock-tree` | Game facility unlock mapping | capability progression |
| `ceres-capability:failure-event-catalog` | Failure event catalog | shocks and repairs |
| `ceres-capability:playbook-decision-trees` | Playbook decision trees | choose lens/scale/design |

## Repeated rubric gaps

1. Dependency and cascade rigor: upstream inputs, byproducts, route exposure, and
   inter-trade dependencies.
2. Storage and inventory realism: perishability, cold/dry/hazard storage,
   carrying costs, and spoilage.
3. Regulatory and safety boundary: permits, emissions, food safety, hazardous
   materials, and operator safety.
4. Labor pipeline and succession: apprentice throughput, burnout, credential
   friction, and operator replacement.
5. Market substitution and demand evidence: industrial baseline, premium
   tolerance, and demand-pool sizing.
6. Scenario and fixture coverage: repeatable validation scenarios across scale,
   lens, and shock.
7. Downstream consumer fit: explicit facility, storage, labor, and market outputs
   for games and sibling systems.
8. Location and route sensitivity: climate, terrain, supplier density, and
   transport fragility, likely shared with PORTO.

## Rust scenario commands

```powershell
cargo test
cargo run -- --catalog catalog\smithing --jsonl simulations\tier-a-comparator\results\smithing-rust-events.jsonl --packet simulations\tier-a-comparator\results\smithing-rust.packet.json
cargo run -- --catalog catalog\baking
cargo run -- --catalog catalog\weaving
cargo run -- --compare catalog\smithing\entries\001-backyard-propane-compact.md catalog\smithing\entries\002-induction-modular-small-repair.md --scale town --lens market --json --packet simulations\tier-a-comparator\results\smithing-comparison.packet.json
```
