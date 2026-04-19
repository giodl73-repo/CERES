---
trade: baking
doc_type: functional-requirements
version: "1.0"
status: draft
review_status: {panel: pending, editorial: pending}
derived_from:
  - research/cultures/medieval-northern-europe/baking.md
  - research/cultures/song-china/baking.md
  - research/cultures/tokugawa-japan/baking.md
  - research/cultures/american-frontier/baking.md
sources_count: 22
placeholder_count: 7
---

# Baking: Cross-Cultural Functional Requirements

## 1. Purpose

This document synthesizes the functional requirements for grain-food baking
across four anchor cultures (medieval northern Europe ca. 1100–1500, Song-dynasty
China ca. 960–1279, Tokugawa Japan ca. 1603–1867, and the American frontier ca.
1790–1890). It abstracts what any baking operation must *do* — temperature
envelopes, throughput ranges, fuel options, physical envelope, operator profile,
and supply-chain dependencies — from the specific cultural and design forms in
which those functions were historically achieved. It is trade-agnostic within
baking: the requirements apply across scales and product mixes, from a single
household oven to a multi-operator commercial bakehouse.

It is not design-prescriptive: it does not specify stone dome over cast-iron
stove, sourdough over chemical leavening, or any particular organizational form.
Plan C catalog authors use this document as the input specification: every
catalog entry for a baking-trade facility must address each functional requirement
listed here or explicitly state why the requirement does not apply to that design.

**Critical framing note.** The word "baking" does not map onto a single
temperature regime or equipment type across the four anchor cultures. Song China
and Tokugawa Japan produced their primary grain foods at steam temperature
(~100°C); the European dome oven and American cast-iron stove operated at
190–280°C. The term covers a range of practices that share a common social
function — grain-food production as a commercial or household trade — but that
differ in equipment, thermal regime, and supply-chain structure. Section 10
(Divergence Log) documents this divergence explicitly. Plan C catalog authors
must specify which thermal regime and cultural form their entry represents rather
than relying on a single undifferentiated "baking" baseline.

---

## 2. Temperature Envelope

The temperature requirement for baking is **not** constant across all four anchor
cultures. This is the primary divergence in this trade and must be stated at the
outset.

| Process / culture | Temperature range | Equipment | Notes |
|---|---|---|---|
| Wheat bread baking — medieval N. Europe | ~220–280°C (peak at oven opening); ~190–230°C during bake | Wood-fired masonry dome oven | Declining temperature curve; wheat loaves loaded first, rye/maslin second, pastry last |
| Shaobing flatbread baking — Song China | ~200–250°C at oven wall | Clay barrel oven (*tian lu*) | Dough slapped onto hot interior walls; radiant heat; structural analog to tandoor [CITATION-NEEDED: clay barrel oven wall temperatures during shaobing baking — experimental or food-history source; figure is author inference] |
| Steamed grain foods — Song China (dominant form) | ~100°C (steam) | Tiered bamboo/clay steamer (*zheng*) over open fire or clay stove | Most Song wheat-based foods were steamed, not oven-baked; capital requirement orders of magnitude lower than oven |
| Kasutera sponge cake baking — Tokugawa Japan | ~140–170°C [CITATION-NEEDED: kasutera baking temperature — Japanese food-science or confectionery-history source; this is an approximation pending verification] | Wooden mold with radiant charcoal above and below | Isolated Portuguese-influence exception within the wagashi repertoire |
| Iron-surface baking (*yakimono* wagashi) — Tokugawa Japan | ~180–220°C surface temperature [CITATION-NEEDED: monaka-shell iron-surface production temperatures; same sourcing requirement as kasutera] | Iron mold (*kata*) over charcoal brazier | Short contact time; not enclosed-oven baking |
| Steaming — Tokugawa Japan (dominant form) | ~100°C (steam) | Tiered *seiro* steamer over charcoal brazier | Primary heat process for most wagashi; sustained heat maintenance rather than high-temperature peak |
| Bread baking — American frontier (cookstove) | ~175–230°C; temperature variation of ±20–40°C within a session from fire cycling | Cast-iron cookstove oven | No thermostat; operator managed fire cycle; pan bread, not hearth-form |
| Bread baking — American frontier (Dutch oven) | ~180–220°C (estimated); highly variable | Cast-iron Dutch oven with embers above and below | Portable; small volume; non-uniform heat distribution |

**The defining functional divergence.** "Baking" across these four cultures spans
a range from 100°C (steaming) to approximately 280°C (European masonry oven peak).
The appropriate temperature envelope for any Plan C catalog entry cannot be read
from a single historical baseline; it depends entirely on which product type and
cultural form the entry represents. Catalog authors must specify the product
category they are targeting and select the corresponding temperature row above.

### How each culture achieved the temperature envelope

For physical equipment, fuel types, and the specific oven and steamer forms used
across the four anchor cultures, see `research/trades/baking/HISTORICAL-FORMS.md`
Table 1 (Physical Equipment by Culture). The requirement here is the temperature
envelope itself; implementation forms are forms-document territory.

---

## 3. Throughput Envelope

Throughput varied substantially across cultures, scales, and product types. The
figures below are order-of-magnitude estimates; direct throughput records from
historical bakehouse accounts are sparse, and most figures derive from
process-time and capacity reasoning or from analogical inference.

### By culture and product type

| Culture | Product type | Estimated throughput | Cadence | Basis |
|---|---|---|---|---|
| Medieval N. Europe (professional) | Wheat/rye loaves | 60–240 loaves/working day | 1–3 batch loads per firing, typically once-daily firing | Author estimate from oven-capacity and firing-cycle reasoning [CITATION-NEEDED: direct throughput evidence — English or French professional baker records; medieval-northern-europe chapter notes this is not directly documented] |
| Song China (mantou vendor) | Steamed wheat buns | Small-batch continuous production; scale-up additive by steamer tiers | Continuous during market hours; no single-firing cadence constraint | Song-china chapter §Functional Requirements Learned; no quantified figure in sources consulted |
| Song China (shaobing vendor) | Clay-oven flatbread | Street-food scale; small batches to meet passing trade demand | Semi-continuous; oven required sustained operation to be economical | Song-china chapter §3; intermittent-use oven has throughput-floor constraint from reheat time |
| Tokugawa Japan (steamed wagashi) | Manjū (steamed buns) | ~40–80 per hour per steamer station [CITATION-NEEDED: estimate from ~12–20 per tray at 15–20 min steaming; no Tokugawa production records verified; label as estimate in downstream use] | Batch-process rhythm | Tokugawa-japan chapter §8 |
| Tokugawa Japan (hand-formed wagashi) | Nerikiri | ~10–20 pieces per operator-hour at skilled level [CITATION-NEEDED: same sourcing caveat — estimate requiring corroboration] | Skill-limited; no heat-process constraint | Tokugawa-japan chapter §8 |
| American frontier (household) | Loaves, biscuits, pies | 1–4 loaves or equivalent per baking session | Weekly or twice-weekly cycle; not daily | American-frontier chapter §8 |

**Throughput floor — structural caveat.** The product-specific figures above are
author estimates from process-time and equipment-capacity reasoning. No verified
throughput upper or lower bound has been established from historical production
records for most product categories. Plan C catalog entries must carry
high-uncertainty flags on throughput figures until better-sourced verification
is available.

**Throughput-cadence divergence.** European and frontier baking was organized
around discrete firing or baking-day cycles; Song commercial steaming was
effectively continuous during market hours. These are categorically different
production models. A catalog entry derived from the European batch-oven model
cannot use the Song continuous-production model as its throughput baseline, and
vice versa.

**Seasonal pattern.** All four cultures show seasonal throughput variation.
Medieval European baking tracked grain-market cycles and festive demand. Tokugawa
wagashi production spiked sharply at the New Year and calendar festivals (mochi
production especially). American frontier baking varied with harvest supply and
winter fuel constraints. Plan C catalog entries must populate `throughput_variance.seasonal`.

---

## 4. Fuel Regime Options

All four cultures demonstrate that the required temperature envelopes are
achievable with more than one fuel type. The choice of fuel is an implementation
variable, not a functional requirement, subject to the physical constraint that
the chosen fuel must achieve the temperature envelope specified for the target
product type.

| Fuel | Cultures / scales | Achievable temp. | Key trade-offs |
|---|---|---|---|
| Dry wood (faggots, billets) | Medieval N. Europe (primary for oven); American frontier (primary for cookstove in forested east) | 200–280°C in masonry oven; 175–230°C in cast-iron stove | Variable heat from combustion cycling; requires drying and storage; abundant in forested zones; scarce on open plains |
| Charcoal | Song China (clay stove fuel); Tokugawa Japan (brazier fuel, primary) | 100°C sustained for steaming; 140–220°C for wagashi direct-heat operations; 200–250°C for shaobing barrel oven | Consistent heat; portable brazier use; lower smoke than wood; requires charcoal supply chain |
| Coal | Song China (urban fuel in northern cities — Northern Song Kaifeng) [CITATION-NEEDED: coal as domestic/cooking fuel in Northern Song Kaifeng; Hartwell 1962 covers industrial coal; separate urban-fuel source required]; American frontier (coal-burning stove, railroad-served areas) | Equivalent to charcoal/wood with appropriate equipment | Consistent output; requires coal-capable firebox; only economical where freight makes it competitive |
| Buffalo chips / prairie fuel substitutes | American frontier (Great Plains only) | Below wood; reduced and less controllable | Lower heat output; harder temperature management; baking quality degraded; a fuel-scarcity response, not a preferred option |
| No-fuel (soaking, cold-set) | Tokugawa Japan (yokan cooling, certain rice-paste preparations) | Ambient temperature | Setting by cooling or gelling; no combustion requirement; passive stage only — a supplement to heat-processing, not a standalone fuel-free baking process |

**Fuel-scarcity constraint (American frontier finding).** On the Great Plains,
wood fuel was genuinely scarce; buffalo chips and twisted hay produced lower and
less controllable heat than hardwood, making cast-iron stove oven temperature
management more difficult and baking quality more variable. This is a documented
supply-chain constraint, not a skill failure. Any Plan C catalog entry for a
plains-context baking operation must model fuel sourcing as a primary constraint,
not an assumption. [American frontier chapter §6; Fite 1966]

**Charcoal for low-temperature confectionery.** The Tokugawa case establishes
that a charcoal brazier is a fully adequate heat source for steaming and
low-temperature wagashi production. The capital cost and infrastructure
requirement of a masonry oven is not necessary for a confectionery or
steamed-grain-food operation. This has a direct implication for Plan C catalog
entries in that product tier.

---

## 5. Physical Envelope

### Footprint

| Culture / context | Floor area (m²) | Basis |
|---|---|---|
| Medieval N. Europe (professional bakehouse, single oven) | ~20–50 m² | Author estimate; [CITATION-NEEDED: archaeological or documentary evidence for medieval English or French professional bakehouse floor area, including oven, fuel storage, and work area; Grenville or equivalent medieval-archaeology source] |
| Medieval N. Europe (household oven alcove or manorial oven) | ~5–15 m² for oven structure; housed in existing building | Structural inference; oven typically built into or against an existing wall |
| Song China (steamed-food vendor, minimum viable) | ~10–20 m² | Song-china chapter §Functional Requirements Learned; low capital-barrier entry; no oven chamber required |
| Song China (shaobing barrel-oven vendor) | ~15–25 m² | Song-china chapter §3; clay barrel oven plus work area and fuel storage |
| Tokugawa Japan (commercial *kashi-ya*) | ~15–30 m² (production + ingredient storage; excluding retail area) | Tokugawa-japan chapter §8 [CITATION-NEEDED: kashi-ya physical dimensions; historical or ethnographic sources; this is an estimate from process-space reasoning] |
| American frontier (household kitchen, baking area) | Baking occurs within existing kitchen; no dedicated structure | American-frontier chapter §3; no community oven; all baking in kitchen or over open fire |
| American frontier (small commercial town bakery) | ~20–40 m² | Author estimate by analogy with frontier smithy scale; American-frontier chapter §2 [CITATION-NEEDED: frontier commercial bakery physical dimensions; regional commercial history] |

Small-scale baking operations across all four cultures fall broadly in the
**10–50 m²** range for dedicated production space, with the lower bound
representing a minimum steaming-only or household-baking configuration and the
upper bound representing a multi-oven professional bakehouse with fuel storage.
The American frontier household baking model required no dedicated structure.

### Thermal mass and oven construction

The masonry dome oven (medieval northern Europe; partially Song China shaobing
form) requires substantial thermal mass to sustain temperature through a batch
load. Minimum masonry thickness for floor and dome walls adequate to hold heat
through a standard batch load was approximately 10–20 cm of stone or fired brick
[CITATION-NEEDED: thermal mass specifications for dome bread ovens — experimental
thermodynamics or contemporary artisan-oven engineering literature;
medieval-northern-europe chapter §Functional Requirements Learned]. A steel-shell
oven cannot sustain declining-temperature batch baking in the same mode; thermal
mass is a non-optional functional constraint for the dome-oven form.

The cast-iron stove oven (American frontier) substitutes iron thermal mass for
masonry. It is lower in total stored heat than a masonry oven and loses
temperature more rapidly during the bake; the baker compensated by managing the
fire. This is a different thermal regime, not an inferior one: it enabled
portable or semi-portable baking independent of fixed masonry construction.

The steamer (*zheng*, *seiro*) requires no thermal mass storage; it operates on
sustained active heat (100°C steam). Thermal mass is irrelevant for the steaming
form; the functional requirement is sustained fuel input, not stored heat.

### Ventilation

All four cultures produced combustion gases during fuel operations. A heat source
adequate for baking requires adequate ventilation for the operator's breathing
environment. Masonry ovens were built with a chimney or smoke aperture;
cast-iron stoves had flue-pipe connections; charcoal brazier use in enclosed
spaces presents carbon monoxide risk. Any Plan C catalog entry must specify the
ventilation configuration for the fuel and heat equipment used.

---

## 6. Operator Profile

### Skill floor by operation type

| Operation type | Minimum skill level | Cultural context | Notes |
|---|---|---|---|
| Fire management for steaming | Household helper (no craft skill required) | Song China, Tokugawa Japan | Maintaining a boil is a basic skill; no judgment about temperature range |
| Dutch oven or cast-iron stove baking | Household baker with developed judgment | American frontier | Temperature reading by hand-test; fire management; no formal training path |
| Routine bread baking in masonry dome oven | Baker with 2–3 years developed judgment | Medieval N. Europe | Temperature reading, batch sequencing, timing; guild-assisted skill transfer; [CITATION-NEEDED: baker's apprenticeship duration and skill acquisition — guild records or food-history source] |
| Commercial steamed-bun production | Experienced operator; no formal credential | Song China (vendor) | Fermentation-starter management is the critical skill; equipment operation is learnable quickly |
| Standard wagashi (manjū, simple steamed forms) | Entry-level confectioner; apprentice-accessible | Tokugawa Japan | Basic steaming and anko preparation; teachable within 1–2 years |
| Complex hand-formed wagashi (nerikiri, premium namagashi) | Master confectioner | Tokugawa Japan | 10–20 pieces per hour only at skilled level; design judgment, material feel; multi-year acquisition |
| Kasutera and specialized baked wagashi | Experienced confectioner | Tokugawa Japan (Nagasaki concentration) | Specialized technique from Portuguese-contact tradition; not generalized across the trade |

**Skill floor divergence.** The skill floor for baking spans from basic household
competence (frontier biscuit production with chemical leavening) to master-level
craft (elite wagashi). No single skill floor applies across the four cultures.
Plan C catalog entries must declare which operator tier they target.

**Guild vs. non-guild transmission.** Medieval northern Europe used formal guild
indenture (5–7 years in larger English and Flemish towns) [CITATION-NEEDED:
baker's guild apprenticeship terms, England or Flanders, 13th–15th century].
Tokugawa Japan used *detchi-boko* (multi-year indenture; no standardized duration).
Song China used informal household and market transmission with no institutional
equivalent. The American frontier used informal household transmission (female-to-
female, no formal path). The guild-duration figure is not universal; catalog
entries claiming `apprentice_friendly: true` must specify which model they follow.

### Concurrent operators

| Culture / form | Typical crew | Notes |
|---|---|---|
| Medieval N. Europe (professional) | 1 baker + 1 assistant (fuel, loading, unloading) | Household baking: 1 operator with incidental family labor |
| Song China (steaming) | 1–2 adults (household or vendor unit) | Scale-up additive: more tiers, more workers |
| Tokugawa Japan (mochi pounding) | 2 operators required (pounder + turner) | Synchronization requirement; finger-injury risk if timing lapses |
| Tokugawa Japan (general confectionery) | 1–3 depending on product mix | Anko preparation may be a separate workstation |
| American frontier (household) | 1 operator (household woman); incidental family labor | Single-operator, single-oven constraint |

**Two-person mochi-pounding requirement.** Mochi production requires two concurrent
operators: one pounding, one turning and wetting the mass between strikes. This is a
physical synchronization constraint, not a skill preference. Any Plan C catalog entry
that includes mochi production must specify the two-operator concurrent requirement
and the safety dimension (finger-injury risk during synchronization lapse).

### Apprenticeship and skill transfer

| Culture | Mechanism | Duration | Notes |
|---|---|---|---|
| Medieval N. Europe (urban guild) | Formal indenture; guild-regulated | 5–7 years in major English and Flemish towns [CITATION-NEEDED: baker's guild apprenticeship terms — guild ordinances or court records] | Entry fee; market-exclusion function alongside quality function [Ogilvie 2019] |
| Song China (vendor) | Informal; family or market-based | Variable; no institutional control | No guild equivalent; commercial food vending under merchant licensing |
| Tokugawa Japan | *Detchi-boko* indenture; master lineage | Multi-year; no standardized duration | Vertical master-lineage authority; *tedai* (paid assistant) stage before independent operation [Leupp 1992] |
| American frontier | Informal; household transmission (female) | Variable; no formal path | No examination or certification; skill quality variable and unreliable in the primary record |

---

## 7. Supply-Chain Dependencies

No anchor culture operated a supply-chain-autonomous baking operation. This is a
consistent finding across all four cultures.

**The mill dependency as the primary baking falsifier.** In all four cultures,
bakers did not mill their own grain. Milling was a capital-intensive, water-power
or wind-power dependent operation controlled by specialist millers, lords, or
commercial investors [Langdon 2004; Song-china chapter §6; American-frontier
chapter §6]. The professional baker's minimum viable operation began at the
point of milled flour purchase; the flour supply chain was external to the baking
trade. This is the primary supply-chain falsifier for baking:

> **Restoration of a local baking operation requires a local or regional flour
> mill OR acceptance of continued dependence on industrial flour supply. A baking
> operation that proposes to integrate grain-to-loaf vertical production is a
> combined milling-and-baking trade, not a baking trade alone, and must account
> for the capital and skill requirements of the milling stage.**

| Dependency | Medieval N. Europe | Song China | Tokugawa Japan | American frontier |
|---|---|---|---|---|
| Flour (milling upstream) | Regional mills; seigneurial *banalité* in France; town mills in England; baker holds no buffer stock beyond a few days [Langdon 2004; Jordan 1996] | Commercial urban mills (water-powered or animal-powered); milling fee or flour-share; vendor not vertically integrated [Song-china chapter §6] | Commercial milled flour (*komugiko*) for manjū and wheat wrappers; rice milling for mochigome separate; vendor purchased milled inputs | Industrially milled commercial flour from the first day; Oliver Evans automated mill widely adopted by early 1800s; frontier households purchased flour by the barrel [Cronon 1991; american-frontier chapter §6] |
| Leavening | Barm from ale fermentation (primary northern England/Low Countries); sourdough starter maintained internally | Wild-yeast starter (*jiaomu*) maintained internally; low-cost but technically demanding [Huang 2000] | Managed starter cultures maintained internally; fermentation management as core craft skill | Sourdough starter (self-perpetuating; vulnerable to loss); saleratus/baking soda (commercial, 1840s+); compressed yeast (Fleischmann's, 1868+) |
| Sugar | Minor in bread baking; not a structural dependency | Minor in most grain foods; oil and sesame for shaobing | **Binding constraint throughout Tokugawa period**; imported via Nagasaki; premium commodity; determined which products were accessible to which social classes [Tokugawa-japan chapter §6] | Commercial purchase; not locally produced; less critical for bread-dominant product mix |
| Fuel | Dry wood purchased from specialist fuel sellers or by contract; fuel cost recognized in some English assize proceedings [medieval-northern-europe chapter §Supply Chain] | Wood, charcoal, or coal (northern cities); no special fuel-supply infrastructure for steaming | Charcoal; modest consumption relative to masonry-oven baking; charcoal via standard urban supply | Wood (forested east; abundant); plains fuel substitutes (buffalo chips, twisted hay) where wood absent; coal post-railroad |
| Speciality inputs | Salt (purchased; Bay of Bourgneuf and coastal sources for northern Europe) | Sesame and oil for shaobing; fermentation starters | Rice, mochigome, adzuki beans, kanten (agar-agar from specialized seaweed-processing regions); each a distinct supply chain [Tokugawa-japan chapter §6] | Salt; lard; pies required fruit/vegetable fillings (seasonal or dried) |

**Leavening supply hierarchy.** Sourdough starters are self-perpetuating (no
external supply once established) but are vulnerable to loss from freezing, heat
damage, or neglect — an internal operational risk. Chemical leavening (saleratus,
baking soda, baking powder) and commercial yeast are industrial inputs dependent
on commercial distribution. Any Plan C catalog entry must declare which leavening
type it depends on and model the corresponding supply-chain risk.

**Sugar as the wagashi falsifier.** For any Plan C catalog entry modeled on the
Tokugawa confectionery form, sugar is not a peripheral ingredient cost. High-sugar
wagashi (yokan, premium anko preparations, higashi) were luxury items throughout
the Tokugawa period precisely because sugar was expensive. A modern replication
of the commercial wagashi trade must cost sugar at market rates and recognize
that product accessibility in the historical case was rationed by sugar price.

---

## 8. Product Category Matrix

Five product categories appear across the four anchor cultures with distinct
throughput, skill, and market characteristics.

| Category | Throughput profile | Skill floor | Industrial displacement | Survived? [canonical verdict] |
|---|---|---|---|---|
| **Staple grain bread** (European wheat/rye loaves; American sourdough and yeast bread) | Medium-volume batch production; weekly cycle at household scale; daily at commercial | Journeyman/experienced household baker | Displaced by industrial factory bread (England from 1880s; US from 1890s–1920s); factory bread was more consistent, not less, than median household product | Artisan segment `restructuring` into premium niche; mass-market household baking `demand-collapse` |
| **Quick bread and biscuits** (frontier biscuits; flatbreads) | High tolerance for imprecision; fast bake; leavening-dependent | Low to moderate; chemical leavening reduces skill threshold | Not displaced in same way; remains common household and restaurant item; industrial version (sliced bread) took mass market | `restructuring` into household staple and restaurant side; not a premium niche specifically |
| **Steamed grain foods** (*mantou*, *baozi*, *seiro* wagashi; Song China dominant form) | Batch-process; additive scale; no oven required | Low to moderate; starter management is the critical skill | Not displaced; commercial vendor trade continuous for over a millennium in China; structurally robust because hand-preparation and hot consumption were not separable from the product | `continuous` (Song China); `restructuring` (Tokugawa wagashi — now premium-cultural positioning) |
| **High-skill confectionery** (nerikiri, premium namagashi, elite *kyo-gashi*) | Low volume; high hand-labor per piece; skill-capped throughput | Master confectioner | Survived via premium-cultural differentiation from industrial confectionery; no regulatory-preservation mechanism equivalent to sword smithing | `restructuring` into premium cultural market; gift-economy and tourism demand sustained |
| **Specialty baked goods** (pies; pastry; shaobing; kasutera) | Medium volume; seasonal for pies; continuous for shaobing vendor | Moderate; shaobing oven management is specialized | Shaobing vendor trade continuous in China; pie production partially household, partially commercial, partially restaurant; kasutera survives as regional Nagasaki product | Mixed: shaobing `continuous`; pies `restructuring`; kasutera `restructuring` |

**Steamed-grain-food stability finding.** The Song China case demonstrates that
the commercial grain-food vendor form operating on steaming technology has been
commercially viable continuously for over a millennium. This stability appears
to derive from structural features: low capital barrier, no minimum-scale
threshold enforced by equipment cost, hand-preparation that is not replicable
by factory product, and hot-consumption requirement that is not separable from
the product. Plan C catalog entries targeting steamed-grain-food production have
a stronger historical viability precedent than entries targeting oven-bread
production in mass-market contexts.

---

## 9. Functional Requirements Summary Table

This table is the direct handoff to Plan C catalog authorship. Every catalog
entry for a baking-trade facility must address each row or explicitly state
inapplicability.

**Caveat on temperature requirements (R-01 through R-08).** Temperature values
are inferred from the documented operating requirements of the processes performed
and from analogical inference with comparable modern processes. Direct measurement
data from pre-industrial ovens, steamers, and braziers are largely absent from
the sources consulted. Plan C catalog entries that cite these requirements should
note that values are process-physics inferences pending experimental confirmation.

| # | Requirement | Historical value(s) | Modern-equivalent expectation for Plan C entries |
|---|---|---|---|
| R-01 | Temperature regime: steaming (if claimed) | ~100°C at steam surface; sustained throughout batch | Declare if catalog entry uses steaming as primary heat process; specify heat source sustaining boil; no upper-temperature precision required |
| R-02 | Temperature regime: masonry dome oven (if claimed) | ~220–280°C at oven opening; ~190–230°C during bread bake; declining curve through batch loads | If catalog entry uses masonry dome or equivalent: must sustain ≥220°C at baking surface for wheat bread; thermal mass (floor + dome, ~10–20 cm masonry) is non-optional |
| R-03 | Temperature regime: cast-iron or enclosed metal oven (if claimed) | ~175–230°C; ±20–40°C variation from fire cycling; pre-heat required | Declare `oven_type`; specify pre-heat time; acknowledge ±40°C operating variation if no thermostat |
| R-04 | Temperature regime: clay barrel oven / shaobing form (if claimed) | ~200–250°C at oven wall [CITATION-NEEDED: experimental source] | If modeling shaobing-form oven: specify preheat time (~30–45 min [CITATION-NEEDED: blocking citation for this figure]); continuous operation required for economic throughput |
| R-05 | Temperature regime: low-temperature direct-heat baking (*yakimono*, kasutera) | ~140–220°C depending on form [CITATION-NEEDED: kasutera and monaka temperature sources] | Specify surface temperature and heat source; charcoal brazier is historically attested and functionally adequate |
| R-06 | Steam injection (masonry dome oven) | Present in high-quality European wheat bread baking; moisture from sealed dough environment; sometimes a water vessel introduced | If claiming European hearth-bread crust quality: specify steam injection mechanism; cast-iron oven bread has a different crust specification (softer) and does not require steam injection |
| R-07 | Thermal mass (masonry oven only) | ~10–20 cm stone or fired brick for floor and dome | Declare thermal-mass specification; steel-shell oven cannot fulfill this requirement |
| R-08 | Batch cadence | European: 1–3 loads per firing; typically once-daily firing; Song steaming: continuous; frontier: weekly or twice-weekly | Declare production cadence model; batch-oven entries must specify loads per firing and firing frequency; continuous entries must specify operating hours and minimum throughput floor |
| R-09 | Batch size / throughput | 60–240 loaves/day (medieval professional); 1–4 loaves per session (frontier household); 40–80 manjū/hr per steamer station (wagashi, estimate); 10–20 nerikiri pieces/hr (master, estimate) | Declare `throughput_units_equiv_per_session`; flag as estimate if not directly sourced; populate `throughput_variance.seasonal` |
| R-10 | Fuel type | Dry wood (medieval, frontier forested); charcoal (Song China, Tokugawa Japan); coal (northern Song cities, frontier railroad-served areas); fuel substitutes on plains | Declare fuel type; document heat adequacy for declared temperature regime; note supply-chain source |
| R-11 | Leavening type | Sourdough starter (self-perpetuating; loss risk); barm from ale (medieval NW Europe); wild-yeast starter (*jiaomu*) (Song China); chemical leavening (frontier 1840s+); commercial yeast (frontier 1868+) | Declare leavening type; if sourdough, specify starter-management protocol and loss-recovery path; if chemical/commercial yeast, specify supply-chain source |
| R-12 | Flour supply chain | Purchased milled flour in all 4 cultures; no self-milling at commercial scale | Declare flour source explicitly; if claiming grain-to-loaf vertical integration, add full milling requirements; no entry may claim supply-chain autonomy at commercial scale without explicit documentation |
| R-13 | Sugar supply (confectionery only) | Binding constraint in Tokugawa Japan (imported, expensive); minor in other cultures for bread | For any confectionery entry: declare sugar source and cost structure; note historical premium character; do not assume industrial-era commodity pricing represents the historical baseline |
| R-14 | Footprint | 10–50 m² across scales; household baking requires no dedicated structure | Declare `footprint_m2`; entries claiming no dedicated structure must specify where production occurs; entries at 10 m² represent minimum steaming-only configuration |
| R-15 | Ventilation | Chimney/smoke aperture for masonry oven; flue for cast-iron stove; carbon monoxide risk for charcoal brazier in enclosed space | Declare `ventilation` field; charcoal entries must specify CO-risk management; masonry oven entries must specify smoke extraction |
| R-16 | Operator skill floor | Household steaming/biscuit: no formal credential; routine bread: 2–3 years judgment acquisition; premium wagashi: master multi-year | Declare `operator_skill_floor`; specify which operations are within scope; do not apply guild-duration figure to non-guild forms |
| R-17 | Concurrent operators | 1–2 for most forms; 2 required for mochi pounding (non-negotiable physical synchronization) | Declare `operators_concurrent`; mochi-pounding entries must specify 2-operator requirement and safety note |
| R-18 | Apprentice path | Guild indenture (5–7 yr, medieval NW Europe guild); *detchi-boko* multi-year (Tokugawa); informal household transmission (frontier, Song); duration and formalization highly variable | If `apprentice_friendly: true`, populate all `apprentice_path` sub-fields; specify which cultural model is being followed; do not default to guild duration for non-guild forms |
| R-19 | Labor-regime adjustment | All 4 cultures incorporated unpaid household labor (primarily female) and/or indenture-basis apprentice labor not at market wages | State explicitly whether cost estimates assume market-wage labor throughout; historical figures must be adjusted upward for modern operations under contemporary labor law |
| R-20 | Seasonal throughput variance | All 4 cultures show seasonal peaks (festive demand, harvest cycles); Tokugawa mochi peaks sharply at New Year | `throughput_variance.seasonal` field required; worst-month and peak-month fractions required |
| R-21 | Product category scope | See §8 matrix; steamed grain foods show strongest multi-century commercial viability; oven-bread mass production displaced in most cultures | State product mix scope; if mass-market oven-bread focused, document departure from steamed-grain-food viability precedent |
| R-22 | Industrial displacement trajectory | Staple oven-bread displaced by factory production (England 1880s+, US 1890s+); steamed-grain-food trade continuous; confectionery restructured into premium niche | `## Known risks` section must address which product segment the entry competes in and that segment's displacement history |
| R-23 | Scale of operation | Household/minimum-viable (1 oven/steamer, 1 operator); small commercial (1–3 operators, single bakehouse); large-scale continuous (Song commercial density model) | `scale_fit` field must be populated; large-capacity entries must specify the demand anchor sustaining continuous operation |
| R-24 | Demand anchor (continuous-production forms) | Song China large-scale steaming was commercially viable because of urban population density of millions; the density-dependent model does not transfer directly to small settlements | For entries at continuous-production scale: state demand anchor; quantify minimum viable demand population; Song street-vendor model requires urban density not typical of small CERES-scale settlements |

---

## 10. Divergence Log

Per METHODOLOGY §7: where anchor cultures disagree on what a baking facility must
do or be, the disagreement is documented here rather than suppressed in favor of
consensus.

**DIV-01: Temperature regime — steaming vs. oven-baking.**
The fundamental thermal regime for grain-food production differs between cultures
in a way that cannot be reconciled into a single temperature envelope. Song China
and Tokugawa Japan produced their primary grain foods at steam temperature
(~100°C); medieval northern Europe produced bread at 190–280°C in a masonry dome
oven; the American frontier operated at 175–230°C in a cast-iron stove. These
are not variations on a single process; they are categorically different heat
applications requiring categorically different equipment. A catalog entry modeled
on European bread baking and one modeled on Song steamed-bun production differ
in capital cost, footprint, thermal mass requirements, fuel consumption, and
operator skill profile. *Implication for Plan C:* "Baking" is not a single trade
category for catalog purposes. Entries must declare the thermal regime they
represent; no single temperature floor or ceiling applies across the trade.

**DIV-02: Equipment capital requirement — masonry oven vs. steamer.**
The masonry dome oven required substantial fixed capital construction (masonry
walls, dome, hearth floor, chimney) with periodic maintenance from thermal
cycling damage. The steamer (*zheng*, *seiro*) required only a pot, tiered
baskets, and an open fire — capital requirements an order of magnitude lower.
The clay barrel oven for shaobing occupied an intermediate position. The American
cast-iron stove was purchased industrial equipment, requiring commercial
distribution but no on-site construction. These differences affect minimum viable
capital, entry barrier, and the scale at which commercial viability begins. Song
China's low capital barrier contributed to its dense competitive market structure;
medieval Europe's high capital barrier contributed to its guild-protected monopoly
structure. *Implication:* Capital requirements for a Plan C catalog entry vary
by a factor of 10 or more depending on which cultural form is modeled. This must
be explicit in catalog fields, not hidden inside a generic "baking" category.

**DIV-03: Mill dependency — self-evident but frequently elided.**
All four cultures depended on an upstream milling operation for flour. This is the
single most consistent finding across the trade and the one most frequently
obscured by romantic self-sufficiency narratives. Medieval northern European
bakers purchased flour from seigneurial or commercial mills; Song China vendors
purchased from commercial urban mills; Tokugawa confectioners purchased milled
*komugiko* and *mochigome*; American frontier households purchased barrels of
commercially milled flour. No culture provides precedent for a commercial baking
operation that also milled its own grain at commercial scale. *Implication:*
Any Plan C catalog entry claiming grain-to-loaf vertical integration is not
following historical precedent for the baking trade; it is claiming a combined
milling-plus-baking operation and must model both.

**DIV-04: Operator gender — systematically female in household production,
systematically male in commercially visible guild production.**
Household baking in all four cultures was primarily performed by women: medieval
European rural and household baking [Bennett 1996; Hanawalt 1986], Song Chinese
domestic mantou and grain-food preparation [Bray 1994], Tokugawa domestic
wagashi production [Tokugawa-japan chapter §5], American frontier household
baking [Strasser 1982]. Commercial baking in institutionally visible forms (guild
membership, named shops, commercial bakeries) was predominantly male in the
medieval European and Tokugawa contexts. Song street vending was family-based
with less gender segregation. The American frontier had no guild structure, but
commercial bakers were predominantly male immigrants. *Implication:* The skill
and labor structure of baking is systematically different between household and
commercial production in the historical record. Catalog entries should not assume
either form is universal. The labor-regime falsifier (§6) applies to both: neither
the male commercial baker's indenture-subsidized labor nor the female household
baker's unpaid domestic labor is reproducible under modern labor law.

**DIV-05: Guild vs. no-guild skill certification.**
Medieval northern European professional baking in major towns operated under guild
ordinances and the Assize of Bread — formal indenture, wage ceilings for
journeymen, prosecutable price controls, masterwork requirements [Davis 2004;
Ogilvie 2019]. Tokugawa Japan had *detchi-boko* master-lineage indenture without
a horizontal corporate body. Song China had merchant licensing (tax compliance
framework) without occupational certification. The American frontier had no
institutional structure whatsoever; trade unions appeared only in the 1860s–1880s
as labor organizations, not craft-certification bodies. *Implication:* The
institutional history of baking has no single model. Plan C catalog entries
cannot apply a default "guild structure" to the trade; entries must specify what
skill-certification or quality-regulation mechanism, if any, they operate under,
and which historical model they follow.

**DIV-06: Leavening technology — self-perpetuating starters vs. industrial inputs.**
Sourdough and wild-yeast starters (*jiaomu*, barm) are self-perpetuating once
established: their supply chain is internal to the operation, and the key risk
is management failure (starter death), not external supply disruption. Chemical
leavening (saleratus, baking soda, baking powder) and commercial yeast are
industrial inputs requiring commercial distribution; their availability is
contingent on supply-chain reach. The American frontier pattern shows that the
transition from sourdough to commercial yeast reduced a management-intensive
internal dependency but substituted an external commercial dependency. *Implication:*
Catalog entries relying on chemical leavening or commercial yeast must model the
supply-chain dependency explicitly and note the historical date of commercial
availability (saleratus, 1840s; compressed yeast, 1868). Entries relying on
sourdough must model the starter-management requirement and the loss-recovery path.

**DIV-07: Commercial survival trajectory — steamed grain foods vs. oven-baked
staple bread.**
The Song China commercial steamed-grain-food vendor trade has been continuously
viable for over a millennium with no structural collapse comparable to the
European guild-bread displacement. The medieval European professional bread baker
was substantially displaced by factory bread in England from the 1880s and in
other markets by the early twentieth century. The American household baker was
similarly displaced. Tokugawa wagashi restructured into a premium-cultural niche.
*Implication:* These are not equivalent survival trajectories. Plan C catalog
entries for steamed-grain-food production have a materially stronger multi-century
commercial-viability precedent than entries for oven-bread mass production. Catalog
authors should not treat all baking forms as having equivalent historical survival
evidence.

---

## 11. Sources

Sources cited in this document, inherited from the four anchor-culture chapters.
Full bibliography deferred to `research/trades/baking/SOURCES.md`.

1. Kaplan, Steven L. 1984. *Provisioning Paris: Merchants and Millers in the Grain
   and Flour Trade during the Eighteenth Century*. Cornell University Press.
2. Kaplan, Steven L. 2006. *Good Bread Is Back: A Contemporary History of French
   Bread, the Way It Is Made, and the People Who Make It*. Duke University Press.
3. Dyer, Christopher. 2002. *Making a Living in the Middle Ages: The People of
   Britain, 850–1520*. Yale University Press.
4. Davis, James. 2004. "Baking for the Common Good: A Reassessment of the Assize
   of Bread in Medieval England." *Economic History Review* 57(3): 465–502.
5. Jordan, William Chester. 1996. *The Great Famine: Northern Europe in the Early
   Fourteenth Century*. Princeton University Press.
6. Bennett, Judith M. 1996. *Ale, Beer, and Brewsters in England: Women's Work in
   a Changing World, 1300–1600*. Oxford University Press.
7. Hanawalt, Barbara A. 1986. *The Ties That Bound: Peasant Families in Medieval
   England*. Oxford University Press.
8. Langdon, John. 2004. *Mills in the Medieval Economy: England, 1300–1540*.
   Oxford University Press.
9. Ogilvie, Sheilagh. 2019. *The European Guilds: An Economic Analysis*. Princeton
   University Press.
10. Anderson, E.N. 1988. *The Food of China*. Yale University Press.
11. Bray, Francesca. 1994. *Science and Civilisation in China*, vol. VI, pt. II:
    Agriculture. Cambridge University Press.
12. Huang, H.T. 2000. *Science and Civilisation in China*, vol. VI, pt. V:
    Fermentations and Food Science. Cambridge University Press.
13. Elvin, Mark. 1973. *The Pattern of the Chinese Past*. Stanford University Press.
14. von Glahn, Richard. 2016. *The Economic History of China: From Antiquity to the
    Nineteenth Century*. Cambridge University Press.
15. Rath, Eric C. 2010. *Food and Fantasy in Early Modern Japan*. University of
    California Press.
16. Cwiertka, Katarzyna J. 2006. *Modern Japanese Cuisine: Food, Power and National
    Identity*. Reaktion Books.
17. Hanley, Susan B. 1997. *Everyday Things in Premodern Japan*. University of
    California Press.
18. Leupp, Gary P. 1992. *Servants, Shophands, and Laborers in the Cities of
    Tokugawa Japan*. Princeton University Press.
19. Strasser, Susan. 1982. *Never Done: A History of American Housework*. Pantheon.
20. Cowan, Ruth Schwartz. 1983. *More Work for Mother*. Basic Books.
21. Levenstein, Harvey. 1988. *Revolution at the Table*. Oxford University Press.
22. Cronon, William. 1991. *Nature's Metropolis: Chicago and the Great West*. Norton.
23. Fite, Gilbert C. 1966. *The Farmers' Frontier, 1865–1900*. Holt, Rinehart
    and Winston.
24. Beecher, Catharine E., and Harriet Beecher Stowe. 1869. *The American Woman's
    Home*. J.B. Ford. [Period primary source for household baking temperature
    management and equipment; public domain.]
25. [CITATION-NEEDED: Clay barrel oven wall temperatures during shaobing baking —
    experimental or food-history source; current figure (200–250°C) is author
    inference.]
26. [CITATION-NEEDED: Preheating time for shaobing-type clay barrel oven (~30–45
    min) — no historical source identified; contemporary-practice or experimental
    account required; blocking citation before Plan C reference.]
27. [CITATION-NEEDED: Kasutera baking temperature range (~140–170°C) — Japanese
    food-science or confectionery-history source; current figure is approximation.]
28. [CITATION-NEEDED: Monaka-shell iron-surface baking temperature (~180–220°C) —
    same sourcing requirement as kasutera.]
29. [CITATION-NEEDED: Manjū throughput estimate (~40–80/hr per steamer station) —
    no Tokugawa production records verified; downstream use must label as estimate.]
30. [CITATION-NEEDED: Nerikiri production rate (~10–20 pieces/hr at skilled level) —
    estimate requiring corroboration from production records or craft-knowledge
    interviews.]
31. [CITATION-NEEDED: Baker's guild apprenticeship terms, England or Flanders,
    13th–15th century — guild ordinances, court records, or contract evidence;
    medieval-northern-europe chapter cites 5–7 years.]
32. [CITATION-NEEDED: Thermal mass specifications for dome bread ovens (~10–20 cm
    masonry) — experimental thermodynamics or contemporary artisan-oven engineering
    literature.]
