---
trade: smithing
doc_type: functional-requirements
version: "1.0"
status: draft
review_status: {panel: pending, editorial: pending}
derived_from:
  - research/cultures/medieval-northern-europe/smithing.md
  - research/cultures/song-china/smithing.md
  - research/cultures/tokugawa-japan/smithing.md
  - research/cultures/american-frontier/smithing.md
sources_count: 28
---

# Smithing: Cross-Cultural Functional Requirements

## 1. Purpose

This document synthesizes the functional requirements for forge-based metalworking
across four anchor cultures (medieval northern Europe ca. 1100–1500, Song-dynasty
China ca. 960–1279, Tokugawa Japan ca. 1603–1867, and the American frontier ca.
1790–1890). It abstracts what any forge must *do* — temperature envelopes, throughput
ranges, fuel options, physical envelope, operator profile, and supply-chain
dependencies — from the specific cultural and design forms in which those functions
were historically achieved. It is trade-agnostic within smithing: the requirements
apply across forge scales and product mixes, from a single-operator repair shop to
a multi-worker production facility. It is not design-prescriptive: it does not specify
charcoal over coal, box bellows over bag bellows, or any particular organizational
form. Plan C catalog authors use this document as the input specification: every
catalog entry for a smithing-trade forge must address each functional requirement
listed here or explicitly state why the requirement does not apply to that design.

---

## 2. Temperature Envelope

The fundamental temperature requirement for ferrous metalworking is constant across
all four anchor cultures and all scales of operation. The specific fuel and air-delivery
mechanism varied; the required temperature ranges did not.

| Process | Temperature range | Visual indicator | Notes |
|---|---|---|---|
| Annealing | ~700–750°C | Dull red | Softens work-hardened iron between operations |
| Shaping | ~800–1000°C | Cherry-red to bright orange | Forming, bending, drawing; used for most operations |
| Welding | ~1100–1300°C | White heat with sparks | Forge-welding; requires sustained duration at temperature |
| Heat treatment | ~200–850°C (variable) | Below red to orange | Quenching (~750–850°C), tempering (~200–400°C); alloy- and process-dependent |

These ranges derive from the universal constraints of ferrous metallurgy. Explicit
temperature documentation for individual historical forges is absent in most of the
sources consulted; the ranges are inferred from the documented operating requirements
of the processes performed and are consistent across all four chapters
[CITATION-NEEDED: archaeometallurgy or experimental-archaeology temperature
measurements for pre-industrial charcoal and coal forges confirming these ranges].

**Any forge design in the Plan C catalog must sustain a minimum of ~800°C for
shaping.** Forge-welding capability requires ~1100°C sustained. Temperature control
matters as much as peak temperature: overheating above ~1300°C burns the iron,
degrading its properties.

### How each culture achieved the temperature envelope

**Charcoal + hand bellows (all four cultures at village/small scale).** Without
forced air, a charcoal hearth reaches approximately 700°C — adequate for annealing
but insufficient for shaping. Bellows-forced air raises the temperature to the
900–1100°C shaping range and, at full blast, into the welding range
[CITATION-NEEDED: charcoal forge thermal output with and without bellows, experimental
archaeology source; see also medieval-northern-europe chapter §Forge].

**Coal + bellows (Song-era China large ironworks, American frontier post-railroad,
19th-century industrial Europe).** Coal with forced air achieves the same
temperature envelope as charcoal. The Song transition from charcoal to coal in
northern China ironworks is documented from the 10th–11th centuries [Hartwell 1962].
The American frontier transition from charcoal to coal followed railroad freight
economics, not technical preference [Atack and Passell 1994].

**Hydraulic bellows (Song China large ironworks only).** Waterwheel-driven bellows
provided continuous forced air without relying on hand labor, sustaining high
temperatures across long production runs [Needham 1965, vol. IV pt. 2].

**Fuigo double-acting piston bellows (Tokugawa Japan).** The *fuigo*'s double-acting
piston delivered continuous blast on both push and pull strokes, unlike single-action
European bag bellows that delivered air only on the compression stroke
[CITATION-NEEDED: technical description of *fuigo* mechanism; Tokugawa chapter §3].
Both designs achieved the required temperature ranges; the *fuigo* provided more
continuous airflow per operator effort.

**Divergence note.** The double-acting piston bellows (fuigo) was standard in
Tokugawa Japan. The medieval European record shows bag bellows as the dominant type,
with double-action box bellows appearing in later periods; its use in northern Europe
specifically before ca. 1500 is not firmly established [CITATION-NEEDED: medieval
bellows types, northern European iconographic evidence]. The Song ironworks used
hydraulic bellows at large scale. All three designs achieved the same temperature
requirements; the divergence is in air-delivery mechanism, not functional outcome.
Modern motor-driven blowers provide the functional equivalent of any of these designs
with lower labor input.

---

## 3. Throughput Envelope

Throughput varied substantially across cultures and scales. The figures below are
order-of-magnitude estimates; direct throughput records from historical forge
accounts are sparse, and most figures derive from product-weight and heating-cycle
reasoning or from structural analogy across comparable operations.

### Small-scale (village / single-operator) forge

| Culture | Product type | Estimated daily output | Active hours/day | Basis |
|---|---|---|---|---|
| Medieval N. Europe | Horseshoes | 20–40 | 4–8 | Author estimate from product-weight reasoning [CITATION-NEEDED: Langdon 1986 for manorial-account verification] |
| Medieval N. Europe | Plowshares | 2–4 | 4–8 | Author estimate [same caveat] |
| Tokugawa Japan | Simple nails | 20–50 | 6–8 | Analogical estimate [CITATION-NEEDED: Tokugawa chapter §4 analogical comparator note] |
| Tokugawa Japan | Medium hardware | 8–15 | 6–8 | Same |
| Tokugawa Japan | Edge tools (with hardening) | 2–5 | 6–8 | Same |
| American frontier | Horseshoes (fitting) | Irregular; bursty | 4–8 | Structural inference; chapter 4 §9 |

**Realistic active forging time.** All four cultures indicate 4–8 hours of actual
active forging per day. Remaining time is consumed by: fire management and fuel
loading; setup, tool change, and stock preparation; customer interaction; and
non-production tasks. Claiming 10–12 hours of active forging per day is not
supported by the historical record and would overstate throughput in catalog
`sim_params` [CITATION-NEEDED: working-hours evidence for small-scale forge
operation; Swanson 1989 for medieval English craft; structural inference supported
by all four chapters' operational descriptions].

**Seasonal pattern.** Throughput was not uniform across the year. Rural smithing
in all four cultures peaked before planting (tool preparation) and after harvest
(repair), with lower intensity in summer. The American frontier pattern was
"bursty" — irregular demand from horseshoeing, wagon repair, and custom work —
rather than continuous production [CITATION-NEEDED: seasonal patterns, medieval
English smithing, 13th–14th c.; Hanley 1997 for Tokugawa Japan].

### Large-scale (Song-era China)

Song ironworks achieved outputs orders of magnitude higher than village-scale
operations, with Hartwell's research indicating Northern Song iron output comparable
in aggregate to early 18th-century British output [Hartwell 1962].

**Scale caveat (mandatory carry-forward).** Hartwell's specific tonnage figures
must be treated as order-of-magnitude estimates, not precise measurements. Von
Glahn 2016 is the recommended verification source and this tonnage comparison must
not be treated as resolved until that verification is complete [CITATION-NEEDED:
verification of Hartwell tonnage estimates against von Glahn 2016]. Any Plan C
catalog entry that draws on Song-era scale claims must carry this caveat.

Large-scale Song throughput was achieved by substituting coordinated labor and
engineering infrastructure (sustained fuel supply, hydraulic air, organized
workflow) for individual craft skill — demonstrating that high aggregate iron
throughput does not require skilled smiths at each production station. Village-scale
Song smithing was qualitatively comparable to other pre-industrial village smithing;
the large ironworks did not displace village-level production [Song-China chapter
§Functional Requirements Learned].

---

## 4. Fuel Regime Options

All four cultures demonstrate that the required temperature envelope is achievable
with more than one fuel type. The choice of fuel is an implementation variable, not
a functional requirement.

| Fuel | Cultures/scales | Achievable temp. | Key trade-offs |
|---|---|---|---|
| Charcoal | All 4 cultures at village scale; medieval N. Europe as dominant fuel | 700°C unforced; 900–1300°C with bellows | Low sulfur (preferred for quality iron); requires coppiced woodland supply chain; progressive deforestation pressure at scale |
| Coal (bituminous) | Song China large ironworks (10th–11th c. onward); American frontier post-railroad | Same envelope as charcoal with forced air | Higher sulfur → hot-shortness risk; requires venting; lower transport cost where coal is available near surface; requires deeper firebox and improved draft vs. charcoal hearth |
| Coke | Song China large ironworks | Same as coal | Reduces sulfur content vs. raw coal; requires coking infrastructure upstream |
| Wood | Fallback in resource-constrained settings | Lower and less consistent than charcoal | Lower energy density; less controllable; not documented as a preferred forge fuel in any anchor culture |
| Propane / natural gas | Not historical; modern analog | Controllable; equivalent to charcoal range | [CITATION-NEEDED: propane forge temperature output, modern experimental measurement] |

**Sulfur and iron quality.** Coal contains sulfur; sulfur in the fire produces
sulfur dioxide, which induces hot-shortness (brittleness at forging temperature) in
iron. Song China's large-scale coal-fueled ironworks required management techniques
including low-sulfur coal selection and multi-stage refining to mitigate this
[CITATION-NEEDED: sulfur management techniques in Song iron production; Needham 1965
provides background]. This is a direct technical warning for any modern coal-forge
design.

**Forest pressure from charcoal.** The charcoal supply chain for pre-industrial
smithing was not ecologically stable at high demand levels. Medieval England and
Germany experienced progressive deforestation and woodland-protection legislation
in response to charcoal demand from ironworking [CITATION-NEEDED: medieval English
and German woodland-protection legislation; Wrigley 2010 for English fuel-transition
context]. Tokugawa Japan experienced parallel forest pressure near population centers
[CITATION-NEEDED: Morris-Suzuki on Tokugawa deforestation]. Presenting charcoal
as an inherently sustainable fuel without quantifying the specific supply context
is not supported by the historical record (see STYLE-GUIDE §4.2).

**The coal transition was demand-driven, not technically forced.** Song China's
transition from charcoal to coal was driven by the geographic co-location of coal
and iron ore in northern China, not by charcoal scarcity — coal was simply cheaper
to transport in those regions [Hartwell 1962]. The American frontier transition
followed railroad freight economics [Atack and Passell 1994]. Neither transition
implies charcoal inferiority; both reflect local supply-chain economics.

---

## 5. Physical Envelope

### Footprint

| Culture / context | Floor area (m²) | Basis |
|---|---|---|
| Medieval N. Europe (rural forge) | 20–40 m² | [CITATION-NEEDED: archaeological evidence, English or Low Countries forge dimensions] |
| Tokugawa Japan (utility *kajiya*) | 15–40 m² | [CITATION-NEEDED: Tokugawa chapter §8; historical archaeology or ethnographic record] |
| American frontier (one-bay smithy) | 15–30 m² | American frontier chapter §9; Wallace 1978 |
| Song China village forge | Comparable to above; not independently documented | Structural inference from analogous forms |
| Song China large ironworks | Different scale entirely; not a single-operator shop | Hartwell 1962; Needham 1965 |

The small-scale forge across all four cultures falls in the range of **15–40 m²**.
This is the baseline for Plan C's small-footprint catalog tier. The 15 m² lower bound
represents the minimum viable configuration; the 40 m² upper bound represents a
full-featured single-operator shop with adequate fuel storage and work area.

### Ceiling and ventilation

A minimum ceiling height of approximately 2.5 m is required for comfortable operation
and adequate combustion-gas clearance above the hearth. Ventilation is a non-optional
functional requirement: the forge hearth produces sustained combustion gases
(carbon monoxide, carbon dioxide, smoke from fuel, scale particles from hot iron).
Without adequate ventilation, chronic respiratory exposure was a documented working
condition [CITATION-NEEDED: medieval forge ventilation forms, louvre or chimney;
OSHA 29 CFR 1910.252(c) for modern hot-work ventilation standards]. Medieval and
later forges used louvres or chimneys; the functional requirement (extract combustion
gases above the operator's breathing zone) is constant across all periods.

### Anvil and base mass

The anvil was the forge's principal capital asset in all four cultures
[CITATION-NEEDED: medieval anvil weights and forms, English or German sources].
Typical pre-industrial beak anvils ranged from approximately 30–150 kg of iron or
steel. The anvil requires a substantial base — a dense hardwood stump, masonry, or
steel stand — to transmit hammer force into the work rather than into the structure.
Anvil base mass matters for energy efficiency: a light or resonant base dissipates
hammer energy as vibration. Modern equivalent: same functional requirement; modern
anvils are typically 50–200 kg cast or forged steel on a dense base.

### Auxiliary infrastructure

All four cultures indicate the following auxiliary infrastructure as functional
requirements, not optional additions:

- **Quench trough (slack tub).** Water supply at close range for heat treatment and
  for quenching incidental fires. Present in every forge configuration documented.
- **Fuel storage.** Charcoal or coal storage adjacent to (but not inside) the forge
  for fire-safety reasons. Charcoal could not be stored indefinitely; working
  inventory of 1–3 days' fuel was typical.
- **Stock storage.** Bar iron and steel stored adjacent to the forge. In all four
  cultures the smith purchased bar stock rather than smelting; storage for incoming
  stock and outgoing finished goods is a required functional area.
- **Water source.** For the quench trough, tool cooling, and incidental fire control.
  Not required to be on-site if a reliable source is within carrying distance, but
  distance increases operational friction.

---

## 6. Operator Profile

### Skill floor by operation type

| Operation type | Minimum skill level | Notes |
|---|---|---|
| Fire management, fuel loading | Trained helper (no craft skill required) | Historically performed by household members or apprentices |
| Bellows operation | Trained helper | Requires physical endurance; no craft skill |
| Routine repair (horseshoe fitting, simple bends, basic tool sharpening) | Journeyman | Requires formed judgment, not just procedure |
| Standard production (nails, hardware, agricultural tools) | Journeyman | Consistent quality requires experience |
| Precision edge-tool making (laminated blades, differential hardening) | Master | Tokugawa Japan chapter §4 documents this as a distinct skill tier |
| Forge welding | Journeyman to master | Requires temperature judgment and quick execution |
| Bespoke fabrication (custom fittings, structural metalwork) | Master | Requires problem-solving under novel constraints |

Routine repair work — the segment that persisted longest in all four cultures —
operated at journeyman level with non-skilled assistance at the bellows and stock
handling. This is the relevant skill floor for catalog entries targeting the repair
and maintenance segment.

### Concurrent operators

The historical standard across all four cultures was: one skilled operator (smith)
plus zero to two non-skilled assistants (bellows operator, stock handler, apprentice).
Motorized air supply eliminates the bellows-operator requirement, reducing the
minimum viable crew to a single skilled operator for most operations.

At Song-era large-scale ironworks, concurrent specialized workers were required for
charging, tapping, and pouring molten iron — a different organizational form, not
directly analogous to the single-operator forge.

### Apprenticeship and skill transfer

The four cultures implemented skill transfer through structurally different mechanisms.
This is a significant divergence documented in Section 11.

| Culture | Apprenticeship mechanism | Duration | Notes |
|---|---|---|---|
| Medieval N. Europe (urban guild) | Formal indenture; guild-regulated | 3–7 years | Entry fee, masterwork requirement; market-exclusion function alongside quality function [Ogilvie 2019; Epstein 1998] |
| Medieval N. Europe (rural) | Informal; father-son or farm household | Variable | No institutional control; probate evidence for tool inheritance [CITATION-NEEDED: rural forge apprenticeship, English manorial source] |
| Song China (village) | Informal; family-based | Variable | No guild structure; hereditary artisan household registration (*jianghu*) at state-ironworks level [CITATION-NEEDED: *jianghu* system, Song dynasty] |
| Tokugawa Japan | *Detchi-boko* indenture; master lineage (*shokunin*) | Multi-year | No horizontal corporate body; vertical master-lineage authority; no city-wide quality enforcement [Leupp 1992] |
| American frontier | Informal; private indenture or paid assistant | Shorter, variable | No formal examination; high skill variance across trade [CITATION-NEEDED: American apprenticeship, Rorabaugh 1986] |

**Minimum pipeline for succession.** A functional forge targeting repair and bespoke
work requires a minimum 3-year apprentice pipeline to sustain operator succession
[medieval-northern-europe chapter §Functional Requirements Learned]. Apprentice
co-presence during production was structurally built into normal operations across
all four cultures, not a separate training program. Plan C catalog entries claiming
`apprentice_friendly: true` must populate the `apprentice_path` sub-fields.

**Labor-regime falsifier.** Historical per-unit economics incorporated household
labor (spouse, children at bellows and stock handling) and indenture-basis apprentice
labor, neither of which was costed at market wage rates. Modern operations under
contemporary labor law cannot replicate this cost structure. The falsifier constrains
the economics, not the functional achievability: bellows work is replaceable by
electric blowers; other household-labor functions by standard operational overhead.
Historical economics must be adjusted upward when informing catalog cost estimates
[see spec §2 falsifier: labor-regime dependency; de Vries 2008, framework extended;
CITATION-NEEDED: medieval-specific evidence for household-labor contribution to
forge economics].

---

## 7. Supply-Chain Dependencies

No anchor culture operated a supply-chain-autonomous forge. This is a consistent
finding across all four cultures and all scales.

| Dependency | Medieval N. Europe | Song China | Tokugawa Japan | American frontier |
|---|---|---|---|---|
| Iron/steel | Regional markets; Hanseatic network for Swedish bar iron [CITATION-NEEDED: Hanseatic iron trade] | State distribution for large ironworks; merchant networks for village smiths; regional smelting | *Tatara* smelting in Chugoku region; distributed via licensed merchant monopoly (*ton'ya*) [CITATION-NEEDED: Morris-Suzuki on iron commodity circuits] | Pittsburgh and industrial-center bar stock by wagon and rail from the start; never locally autonomous [Gordon 1996] |
| Fuel (charcoal/coal) | Charcoal from coppiced woodland; specialist colliers [CITATION-NEEDED: medieval charcoal production, coppice management] | Coal from mines in northern China (large ironworks); charcoal for village smiths; coal logistics state-managed for largest facilities | Charcoal via mountain/forest trade routes; specialist supply chain; progressive deforestation pressure near urban centers [CITATION-NEEDED: Morris-Suzuki on fuel supply] | Charcoal locally in forested east; coal after railroad; transition driven by rail freight economics [Atack and Passell 1994] |
| Steel for cutting edges | Imported Styrian or carburized bar [CITATION-NEEDED: Styrian steel trade history] | Commercial production via state or merchant ironworks | Commercial bar iron; *tamahagane* for sword smiths only | Commercially sourced from industrial supply; not locally produced |
| Downstream market | Agricultural households, manorial estates; repair demand largely non-discretionary | State distribution for ag tools; merchant networks for consumer goods | Seasonal agricultural households; castle-town commerce; *ton'ya* wholesale pressure | Direct customer market; repair-dominant; no guild territorial protection |

**The autonomy myth.** The popular image of a self-sufficient forge making goods from
locally gathered raw materials is not supported by any anchor culture. Every forge in
every culture purchased iron bar stock and fuel from regional supply networks.
Modern equivalents are similarly dependent on commercial metal stock and energy
supply [American frontier chapter §7; Tokugawa chapter §6; medieval-northern-europe
chapter §Supply Chain].

**State demand as a demand anchor (Song China finding).** Northern Song large-scale
production required a demand anchor — state military procurement and agricultural
tool distribution — that small-scale consumer markets alone could not provide.
Without that demand anchor, the large-capacity fixed-cost organizational form could
not sustain itself. Modern analogs include bulk municipal procurement or cooperative
bulk purchasing [Song-China chapter §Functional Requirements Learned]. This finding
applies to any Plan C catalog entry at large capacity.

---

## 8. Product Category Matrix

Four product categories appear consistently across all four anchor cultures, with
distinct throughput, skill, and market characteristics.

| Category | Throughput profile | Skill floor | Industrial displacement | Survived? |
|---|---|---|---|---|
| **Commodity hardware** (nails, fasteners, standard fittings) | High-volume, repetitive | Journeyman to apprentice | Displaced first and most completely — cut nails from 1790s (US), wire nails from 1880s; factory hinges/bolts mid-19th century | No — actual revenue loss in all 4 cultures |
| **Agricultural and trade tools** (hoes, plowshares, chisels, plane blades) | Medium volume; mix of new manufacture and repair | Journeyman to master (edge tools) | Partial — factory production undercut standard tools but edge-tool quality lagged (Tokugawa Japan precision segment); repair and custom fitting persisted | Partial — new manufacture displaced; repair persisted |
| **Repair and maintenance** (horseshoe fitting, wagon parts, implement maintenance) | Irregular/bursty; labor-intensive per unit | Journeyman | Survived longest in all 4 cultures — repair is inherently location-bound, requires on-site judgment, not replicable by factory product | Yes — longest-surviving segment in every culture |
| **Specialty / artistic / armory** (swords, ornamental ironwork, bespoke structural metalwork) | Low volume; high skill; high margin | Master | Partially displaced; sword smithing in Japan survived via regulatory preservation (government licensing, production quotas) [CITATION-NEEDED: Agency for Cultural Affairs sword-smith licensing; Tokugawa chapter §7] | Partial — only via regulatory or niche-market mechanisms |

**Repair-dominance implication for Plan C.** The repair and maintenance category
survived longest in all four cultures because it is location-bound, judgment-intensive,
and not replicable by factory-produced substitutes. Plan C catalog entries modeling
primary revenue from manufacturing volume are not matching this historical precedent.
Revenue from labor applied to a customer's problem (repair-dominant model) is the
better-supported historical baseline [American frontier chapter §5 and §9].

---

## 9. Functional Requirements Summary Table

This table is the direct handoff to Plan C catalog authorship. Every catalog entry
for a smithing-trade forge must address each row or explicitly state inapplicability.

| # | Requirement | Historical value(s) | Modern-equivalent expectation for Plan C entries |
|---|---|---|---|
| R-01 | Minimum shaping temperature | ~800°C (cherry-red) — consistent across all 4 cultures | Forge must sustain ≥800°C at the work zone during active operation |
| R-02 | Forge-welding temperature (if claimed) | ~1100–1300°C (white heat with sparks) — consistent across all 4 cultures | If catalog entry claims welding capability: sustain ≥1100°C; state whether this is achieved with the standard fuel/air configuration or requires modification |
| R-03 | Annealing temperature | ~700–750°C | Achievable by any forge that reaches R-01; no separate requirement |
| R-04 | Heat treatment range | ~200–850°C (variable by process) | Temperature controllability in this range; quench infrastructure (water supply, slack tub) required |
| R-05 | Temperature control, not just peak | Overheating destroys work; judgment-based in pre-industrial context | Modern catalog entries must specify temperature monitoring method (pyrometer, visual indicator, other) |
| R-06 | Active forging hours per day | 4–8 hours across all 4 cultures; not 10–12 | `max_active_hours_per_week` must reflect realistic active time after setup, shutdown, and non-production overhead; `operations_reality.startup_shutdown_overhead_per_day_min` field required |
| R-07 | Seasonal throughput variance | Agricultural seasonality in all 4 cultures; "bursty" on frontier | `throughput_variance.seasonal` field must be populated; worst-month fraction required |
| R-08 | Fuel type | Charcoal (all cultures, small scale); coal/coke (Song China large scale; American frontier post-railroad); wood (fallback only) | State fuel type explicitly; document sulfur-management approach if coal; document supply-chain for charcoal |
| R-09 | Forced-air delivery | Bellows (hand or foot) in all 4 cultures; hydraulic at Song large scale | Modern electric blower, propane burner air circuit, or equivalent; specify delivery mechanism and its failure modes |
| R-10 | Forge footprint | 15–40 m² across all small-scale forms; large ironworks at different scale | Declare `footprint_m2`; explain if below 15 m² (minimal config) or above 40 m² (expanded) |
| R-11 | Ceiling height minimum | ~2.5 m for combustion-gas clearance | Declare `ceiling_min_m`; flag if space is below 2.5 m |
| R-12 | Ventilation | Mandatory; combustion gases require extraction | Declare `ventilation` field; specify extraction method; note regulatory requirement [OSHA 29 CFR 1910.252(c)] |
| R-13 | Anvil base mass | 30–150 kg pre-industrial anvil on dense base; base mass critical for energy efficiency | Specify anvil mass (kg) and base type; justify if below 50 kg for medium or heavy work |
| R-14 | Quench infrastructure | Universal across all 4 cultures | Specify water source, slack tub; declare as required or N/A with justification |
| R-15 | Fuel and stock storage | Adjacent but separate (fire-safety) in all 4 cultures | Declare storage configuration; fire separation from production area |
| R-16 | Bar stock supply chain | Regional purchase in all 4 cultures; no smelting on-site | State source of bar iron/steel; no entry may claim supply-chain autonomy without explicit documentation |
| R-17 | Operator skill floor | Repair work: journeyman minimum; precision edge tools: master | Declare `operator_skill_floor`; specify which operations are within scope |
| R-18 | Concurrent operators | 1 smith + 0–2 assistants at small scale; more at large scale | Declare `operators_concurrent`; state whether motorized air eliminates bellows-assistant requirement |
| R-19 | Apprentice path | 3-year minimum pipeline in all 4 cultures for succession | If `apprentice_friendly: true`, populate all `apprentice_path` sub-fields per schema |
| R-20 | Labor-regime adjustment | Historical costs incorporated household and indenture labor not at market wage | State explicitly whether cost estimates assume market-wage labor throughout; historical figures must be upward-adjusted if not |
| R-21 | Demand anchor (large-capacity only) | Song China: state procurement was load-bearing; consumer markets insufficient alone | For entries at large capacity: state demand anchor and quantify minimum viable demand |
| R-22 | Product category scope | See §8 matrix; repair dominates survival across all 4 cultures | State product mix scope; if manufacture-focused, document departure from repair-dominant historical baseline |
| R-23 | Industrial displacement trajectory | Commodity hardware displaced first; repair last | Catalog entry's `## Known risks` section must address which product segment the entry competes in and that segment's displacement history |
| R-24 | Scale of operation | Village/small-scale: 15–40 m², 1 operator; large-scale (Song): different form entirely | `scale_fit` field must be populated; large-capacity entries must differ from small-scale entries in form, not just size |

---

## 10. Divergence Log

Per METHODOLOGY §7: where anchor cultures disagree on what a forge must do or be,
the disagreement is documented here rather than suppressed in favor of consensus.

**DIV-01: Fuel type — charcoal vs. coal/coke.**
Medieval northern Europe used charcoal throughout the period and was under
resource pressure by the late medieval era; coal use was not dominant until early
modern England [Wrigley 2010; CITATION-NEEDED: charcoal-to-coal transition,
English smithing]. Song China's large ironworks transitioned to coal and coke in
northern regions by the 10th–11th centuries [Hartwell 1962], centuries before
European blast furnaces made the same shift. Tokugawa Japan remained charcoal-only
due to the absence of mining infrastructure and distribution networks for coal
[CITATION-NEEDED: Morris-Suzuki on Japanese fuel supply]. The American frontier
shifted from charcoal to coal as railroad freight made coal delivery economical
[Atack and Passell 1994]. *Implication for Plan C:* No single historical fuel type
can be presented as the default. Catalog entries must declare fuel type and explain
the choice.

**DIV-02: Production scale and organizational form.**
Song China operated simultaneously at large-scale state/merchant ironworks and at
small-scale village forges — a two-tier structure with no close parallel in the other
three cultures [Song-China chapter §Smith's Place]. Medieval northern Europe
distinguished between rural farm-smiths and urban guild smiths — different scales
with different legal protections and supply chains. Tokugawa Japan had the *shokunin*
estate structure with no horizontal guild body; authority was vertical through master
lineages. The American frontier had no institutional regulation whatsoever. *Implication:*
The "typical forge" abstraction is misleading; catalog entries must specify the
organizational form they represent, not rely on a undifferentiated historical baseline.

**DIV-03: Guild vs. non-guild skill transfer.**
Medieval northern European urban guilds enforced formal indenture, admission fees,
and a masterwork requirement — serving both quality-assurance and market-exclusion
functions [Ogilvie 2019; Epstein 1998]. Tokugawa Japan's *shokunin* system used
vertical master-lineage authority with no horizontal corporate body. Song China's
village smiths used informal family transmission; the state ironworks used hereditary
artisan household registration (*jianghu*) binding labor across generations
[CITATION-NEEDED: *jianghu* system, Song dynasty]. The American frontier used
informal apprenticeship with high skill variance. *Implication:* The "apprentice
path" in Plan C catalog entries cannot be modeled on a single historical form; entries
should specify which model they follow and acknowledge the variance.

**DIV-04: Repair-dominant vs. production-dominant operation.**
The American frontier forge was explicitly repair-dominant from the outset;
manufacturing revenue was eroded early by industrial competition [American frontier
chapter §5]. Medieval European and Tokugawa Japanese village smiths combined
repair with new manufacture of agricultural tools and hardware; the repair share
grew as industrial competition eroded the manufacturing share. Song China's large
ironworks were production-dominant (standardized agricultural tools, cast cookware,
military equipment) with no repair function at scale. *Implication:* The repair-vs.-
production axis is a genuine design choice for catalog entries, not a fixed historical
characteristic. The historical record shows repair-dominance as the more durable form
at small scale; production-dominance required the demand anchors available only to
large-scale Song-type operations.

**DIV-05: Iron supply chain — local vs. regional vs. industrial.**
All four cultures purchased bar iron from outside the forge. The supply chain
differed in character: medieval northern Europe used regional bloomery iron via
Hanseatic networks [CITATION-NEEDED: Hanseatic iron trade, Swedish bar iron];
Song China had state-managed distribution for large ironworks and merchant
networks for village smiths; Tokugawa Japan used *tatara*-smelted iron via
licensed merchant monopolies; the American frontier used industrially produced
Pittsburgh bar stock by wagon and rail [Gordon 1996]. The American frontier case
is distinctively modern in character — the smith was downstream of industrial
production from the first day of operation. *Implication:* Modern catalog entries
are in the same structural position as the frontier smith: purchased bar stock
from industrial supply. Claims of supply-chain independence are unsupported by
any anchor culture.

**DIV-06: Presence or absence of regulatory preservation mechanisms.**
Japanese sword smithing survived industrialization only because explicit
government cultural-property legislation created a licensed scarcity for
traditional production methods [CITATION-NEEDED: Agency for Cultural Affairs
licensing regulations; Tokugawa chapter §7]. No parallel mechanism existed for
utility smithing in Japan, medieval Europe, Tokugawa Japan, or the American
frontier. Commodity utility smithing declined or was displaced in all four cultures
without regulatory protection. *Implication:* Catalog entries targeting specialty
or prestige-market production must specify whether their viability depends on a
regulatory-preservation mechanism and whether that mechanism exists in the target
modern context.

---

## 11. Sources

Sources cited in this document, inherited from the four anchor-culture chapters.
Full bibliography deferred to `research/trades/smithing/SOURCES.md` (Task 8).

1. Hartwell, Robert. 1962. "A Revolution in the Chinese Iron and Coal Industries
   During the Northern Sung, 960–1126 A.D." *Journal of Asian Studies* 21(2): 153–162.
2. Hartwell, Robert. 1967. "A Cycle of Economic Change in Imperial China: Coal and
   Iron in Northeast China, 750–1350." *Journal of the Economic and Social History
   of the Orient* 10(1): 102–159.
3. Needham, Joseph. 1965. *Science and Civilisation in China*, vol. IV pt. 2.
   Cambridge University Press.
4. Elvin, Mark. 1973. *The Pattern of the Chinese Past*. Stanford University Press.
5. Pomeranz, Kenneth. 2000. *The Great Divergence*. Princeton University Press.
6. von Glahn, Richard. 2016. *The Economic History of China: From Antiquity to the
   Nineteenth Century*. Cambridge University Press. [Required for Hartwell tonnage
   verification — blocking for scale claims.]
7. Ogilvie, Sheilagh. 2019. *The European Guilds: An Economic Analysis*. Princeton
   University Press.
8. Epstein, S.R. 1998. "Craft guilds, apprenticeship, and technological change in
   preindustrial Europe." *Journal of Economic History* 58(3): 684–713.
9. de Vries, Jan. 2008. *The Industrious Revolution*. Cambridge University Press.
   [Household labor framework; medieval-specific evidence still needed.]
10. Mokyr, Joel. 1990. *The Lever of Riches*. Oxford University Press.
11. Wrigley, E.A. 2010. *Energy and the English Industrial Revolution*. Cambridge
    University Press.
12. Richardson, Gary. 2004. "Guilds, laws, and markets for manufactured merchandise
    in late-medieval England." *Explorations in Economic History* 41(1): 1–25.
13. Langdon, John. 1986. *Horses, Oxen and Technological Innovation*. Cambridge
    University Press. [Throughput verification pending.]
14. Swanson, Heather. 1989. *Medieval Artisans*. Basil Blackwell.
15. Tylecote, R.F. 1992. *A History of Metallurgy*. 2nd ed. Maney Publishing.
16. Hanley, Susan B. 1997. *Everyday Things in Premodern Japan*. University of
    California Press.
17. Leupp, Gary P. 1992. *Servants, Shophands, and Laborers in the Cities of
    Tokugawa Japan*. Princeton University Press.
18. Morris-Suzuki, Tessa. 1994. *The Technological Transformation of Japan*.
    Cambridge University Press.
19. Wallace, Anthony F.C. 1978. *Rockdale*. Knopf.
20. Schlereth, Thomas J. 1991. *Victorian America*. HarperCollins.
21. Atack, Jeremy, and Peter Passell. 1994. *A New Economic View of American History*.
    2nd ed. Norton.
22. Gordon, Robert B. 1996. *American Iron, 1607–1900*. Johns Hopkins University Press.
23. Longfellow, Henry Wadsworth. 1841. "The Village Blacksmith." [Cultural-trope
    marker only; not a research source.]
24. OSHA 29 CFR 1910.252(c). Hot-work ventilation standards.
25. [CITATION-NEEDED: Archaeometallurgy or experimental-archaeology temperature
    measurements confirming pre-industrial forge operating ranges.]
26. [CITATION-NEEDED: Propane forge temperature output — modern experimental
    measurement confirming equivalence to charcoal range.]
27. [CITATION-NEEDED: von Glahn 2016 verification of Hartwell tonnage figures —
    blocking for Song-scale claims.]
28. [CITATION-NEEDED: Agency for Cultural Affairs sword-smith licensing regulations,
    Japan — production quotas and method requirements; verify currency.]
