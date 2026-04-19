---
trade: weaving
doc_type: functional-requirements
version: "1.0"
status: draft
review_status: {panel: pending, editorial: pending}
derived_from:
  - research/cultures/medieval-northern-europe/weaving.md
  - research/cultures/song-china/weaving.md
  - research/cultures/tokugawa-japan/weaving.md
  - research/cultures/american-frontier/weaving.md
sources_count: 19
placeholder_count: 12
---

# Weaving: Cross-Cultural Functional Requirements

## 1. Purpose

This document synthesizes the functional requirements for loom-based textile production
across four anchor cultures (medieval northern Europe ca. 1100–1500, Song-dynasty China
ca. 960–1279, Tokugawa Japan ca. 1603–1867, and the American frontier ca. 1790–1890).
It abstracts what any weaving operation must *do* — humidity envelope, throughput ranges,
loom footprint, operator profile, finishing steps, and supply-chain dependencies — from
the specific cultural and design forms in which those functions were historically
achieved. It is trade-agnostic within weaving: the requirements apply across loom types
and fiber types, from a single-operator backstrap loom to a multi-worker draw-loom
workshop. It is not design-prescriptive: it does not specify wool over cotton, floor
loom over backstrap loom, or any particular organizational form. Plan C catalog authors
use this document as the input specification: every catalog entry for a weaving-trade
operation must address each functional requirement listed here or explicitly state why
the requirement does not apply to that design.

**Key distinction from smithing.** The primary climate requirement for weaving is
humidity, not temperature. Unlike forge-based trades (where temperature is the
controlling physical variable), weaving imposes a humidity envelope: ambient relative
humidity affects thread workability, breakage rates, and surface quality in ways that
are material-specific and operationally significant. This distinction must not be
suppressed in catalog entries.

---

## 2. Humidity Envelope

Weaving has no temperature requirement for the loom itself under normal ambient
conditions. The controlling climate variable is relative humidity (RH). The optimal
range is fiber-specific.

| Fiber | Optimal RH | Temperature notes | Consequence of deviation |
|---|---|---|---|
| Wool | 65–75% | No critical temperature requirement for the loom; workshop temperature affects operator comfort | Below ~45% RH: static charge, brittleness, warp breakage; above ~75%: fiber felts and sticks in heddle eyes [medieval-northern-europe chapter §Functional Requirements Learned; american-frontier chapter §3] |
| Silk | 65–70% | 18–22°C preferred; silk weakens at elevated temperature (above ~30°C ambient sustained); sericulture requires 22–28°C [song-china chapter §Supply Chain] | Low humidity: brittleness, thread breakage, poor selvage formation; high humidity: thread swells, binds in heddles; Jiangnan climate advantage was its high ambient humidity [song-china chapter §3; tokugawa-japan chapter §8] |
| Cotton | 50–65% | No critical temperature requirement | Less sensitive than wool or silk; sizing assists warp durability in low-humidity conditions |
| Linen / bast fiber | 50–65% | No critical temperature requirement | Moderate sensitivity; warp tension consistency affected by moisture absorption [american-frontier chapter §3] |

These ranges derive from the documented operational behavior of each fiber type. The
specific RH figures for wool (65–75%) and cotton (50–70%) are stated in the
american-frontier chapter [§3] with a flag that a textile conservation or technical
source is required for final confirmation [CITATION-NEEDED: RH requirements for wool
and cotton weaving — textile engineering, conservation science, or period workshop
source confirming the 50–75% ranges documented in the american-frontier and
medieval-northern-europe chapters]. The silk range (65–70%) is inferred from the
Jiangnan climate enabling observation and the general hygroscopic-fiber principle
[CITATION-NEEDED: operational RH range for silk-thread weaving — experimental or
conservation textile literature confirming the 65–70% range].

**The humidity requirement is a functional requirement for a weaving workshop, not an
optional environmental preference.** HVAC or building-design provisions for humidity
control are the modern implementation of what the maritime Low Countries climate and
the Jiangnan subtropical climate provided naturally. Any Plan C catalog entry for a
wool or silk weaving workshop operating in a dry-climate or dry-winter context must
specify how humidity is maintained in the 50–75% range appropriate to its fiber mix.

### How each culture managed humidity

Management was largely passive and location-based. The Low Countries' maritime climate
maintained naturally high ambient humidity favorable for wool [medieval-northern-europe
chapter §The Loom]. The Jiangnan subtropical climate provided silk-thread-workable
humidity [song-china chapter §3]. Tokugawa Nishijin workshops used siting, water
vessels, and seasonal scheduling to maintain workable humidity for silk [tokugawa-japan
chapter §8]. The American frontier record documents real operational problems from
humidity extremes in unheated winter workshops [american-frontier chapter §3]. For
implementation forms by culture, see `research/trades/weaving/HISTORICAL-FORMS.md`
Table 1.

---

## 3. Throughput Envelope

Throughput varied substantially by loom type, fiber, and pattern complexity. The
figures below are order-of-magnitude estimates; direct throughput records from historical
weaving accounts are sparse, and most figures derive from production-process reasoning
or explicit analogical inference stated in the source chapters.

### Throughput by loom type and product

| Loom type | Product | Estimated daily output | Operator count | Basis |
|---|---|---|---|---|
| Four-shaft floor loom, plain weave | Plain-weave wool or cotton cloth | 5–25 linear meters | 1 | American frontier chapter §3 [CITATION-NEEDED: Tryon 1917 specific page range]; medieval estimates consistent |
| Horizontal treadle loom, plain silk | Plain-weave silk (*juan*) | 1–3 meters | 1 | Song-China chapter §8 [soft estimate; must be sourced or flagged before citing] |
| Medieval broadcloth, two-person | Woolen broadcloth (1.5–2 m wide) | ~1–2 yards (0.9–1.8 m) | 2 | Medieval-northern-europe chapter §The Loom [CITATION-NEEDED: Munro or Carus-Wilson throughput; present figure is author estimate] |
| Draw-loom, figured silk or brocade | Brocade, damask, complex figures | 0.2–0.5 meters | 2 | Song-China chapter §8 [soft estimate]; Tokugawa chapter §8 [analogical comparator] |
| Tapestry / *kesi* | Pictorial weft-dominant weave | Non-comparable; measured in days per design unit | 1–2 | Song-China chapter §Products (*kesi*); medieval-northern-europe chapter §Products (tapestry) |
| Backstrap loom | Narrow cloth (40–60 cm wide) | Low; not quantified | 1 | Song-China chapter §3; Tokugawa chapter §3 |

**Throughput is product-type-dependent, not estimable from a general "weaving" rate.**
The figures above span two orders of magnitude (0.1–25 m/day). Averaging them is not
meaningful. Plan C `sim_params.throughput_units_equiv_per_year` fields must specify
loom type and product category and must not be compared across categories without
explicit conversion and justification.

**Throughput floor — structural caveat.** These figures are author estimates from
production-process reasoning. The historical record does not provide verified
throughput bounds for most categories. The primary verification path (Tryon 1917 and
Munro/Carus-Wilson) is noted in the source chapters but specific page-level citations
remain unresolved. Until those are confirmed, throughput values in catalog entries
must carry a high-uncertainty flag.

**Pattern complexity penalty.** For any loom type, pattern complexity reduces
throughput substantially. Plain tabby weave on a four-shaft loom: near the upper end
of the range. Complex overshot coverlet on an eight-shaft loom: 30–50% lower than
plain-weave on the same loom. Draw-loom figured silk: 80–95% lower than plain silk
on the same equipment. Catalog entries claiming pattern capability must state the
throughput figure at the claimed pattern complexity level, not at plain-weave speed.

**The spinner-to-loom ratio is a supply-chain throughput constraint.** Historical
evidence consistently indicates that 4–10 spinners were needed to keep a single loom
continuously supplied with weft thread [medieval-northern-europe chapter §Labor
Regime; CITATION-NEEDED: spinner-to-loom ratio primary source — Munro or Carus-Wilson
for the 4–10 figure; this is widely cited but primary-source verification is
outstanding]. This is a system-level throughput constraint, not a loom-level one: a
loom operating at nominal throughput will be thread-starved without a functioning
spinning supply. Catalog entries must specify whether spinning is included in the
operation or whether spun yarn is purchased externally; the latter is the likely path
for modern restoration and resolves the spinner-to-loom constraint by transferring it
to the industrial supply chain.

---

## 4. Fiber Supply Regime Options

All four cultures demonstrate that raw fiber was always an externally produced input.
This is the weaving equivalent of the mill-dependency in baking and the bar-stock
dependency in smithing. No weaving operation in any anchor culture produced its own
fiber.

| Fiber | Cultures/scales | Key characteristics | Supply chain notes |
|---|---|---|---|
| Wool (raw fleece) | Medieval N. Europe (dominant); American frontier (primary early-period fiber) | Requires shearing, washing, carding/combing, spinning before weaving; 4–10 spinners per loom | English premium wool from Cotswolds and Lincolnshire to Flemish manufacturers via Staple at Calais [Power 1941]; frontier households maintained sheep but carding/spinning was the throughput bottleneck |
| Raw silk | Song China (dominant prestige fiber); Tokugawa Japan (Nishijin dominant) | Requires sericulture (mulberry, silkworms), cocoon reeling, and thread preparation; non-separable upstream; highly sensitive to supply disruption | Jiangnan household production for Song workshops; Nishijin depended on Chinese imports via Nagasaki under *sakoku*, then expanded domestic sericulture [tokugawa-japan chapter §6] |
| Cotton (raw or ginned) | American frontier (mid-period); Tokugawa Japan (cotton weaving belt) | Post-cotton-gin (1793): ginned cotton still requires spinning; machine-spun cotton yarn available in American markets by 1830s–1840s | American frontier transitioned from home-spun cotton to purchased machine-spun yarn within a generation [american-frontier chapter §6] |
| Flax / linen | American frontier (early period linsey-woolsey warp); Medieval N. Europe (linen sector) | Labor-intensive processing (retting, scutching, hackling, spinning) before weaving; flax cultivation declined sharply on American frontier by mid-19th century | Fiber-supply collapse eliminated linsey-woolsey production more completely than loom or skill shortage [american-frontier chapter §8] |
| Ramie / bast fiber | Song China (dominant everyday fiber in Song period); Tokugawa Japan (rural poor and summer wear) | Retting, beating, spinning required; labor-intensive; displaced by cotton under Yuan/Ming [song-china chapter §7] | Song household tax-cloth obligation; Echigo-chijimi is a surviving premium ramie specialty [tokugawa-japan chapter §4] |
| Machine-spun yarn (purchased) | Modern; American frontier (mid-to-late period) | Eliminates spinning step; transfers spinner-to-loom ratio upstream; standard modern pathway | Any modern restoration catalog entry that sources machine-spun yarn eliminates the spinning dependency and should state this explicitly |

**The autonomy myth for weaving.** No anchor culture operated a supply-chain-autonomous
weaving operation for its primary fiber. Fiber was always externally sourced, whether
from household flocks, state sericulture households, or commodity markets. Modern
weaving operations are in the same structural position: purchased spun yarn from
industrial supply. Claims of fiber-supply independence are not supported by any anchor
culture and must be documented explicitly if made.

**Spinning as a prior step.** Even where raw fiber was locally available, it had to be
spun before weaving. The spinner-to-loom ratio (4–10:1) implies that a community
weaving operation that also spins requires a substantial spinning workforce. For modern
catalog entries, this dependency is most cleanly resolved by sourcing machine-spun yarn,
which separates weaving from spinning entirely. Entries must state which path they take.

---

## 5. Physical Envelope

### Loom footprint

| Loom type | Body footprint (m²) | Practical operating footprint | Ceiling height | Notes |
|---|---|---|---|---|
| Backstrap loom | None permanent; requires fixed anchor point | Body + 0.5 m | No minimum; low | Song-China chapter §3; Tokugawa chapter §3; anchor-point requirement is fixed infrastructure |
| Household treadle loom (narrow cloth, 38–60 cm wide) | ~1.0–1.5 × 1.5–2.0 m | ~1.5–2.0 × 2.5–3.0 m including weaver space | ~2.0 m sufficient | Tokugawa chapter §8 [CITATION-NEEDED: folk-museum record confirmation]; Song chapter §3 |
| Four-shaft floor loom (60–90 cm weaving width) | ~1.5 × 2.0 m | ~2.0 × 3.0 m | ~2.0 m sufficient | American frontier chapter §8; §3 [CITATION-NEEDED: period source or museum collection measurement] |
| Broadcloth horizontal treadle loom (1.5–2 m wide) | ~2.0–2.5 × 3.0–5.0 m | ~2.5–3.0 × 4.0–5.5 m | ~2.0 m minimum | Medieval-northern-europe chapter §The Loom [CITATION-NEEDED: guild or archaeological record confirmation] |
| Eight-shaft floor loom for coverlets | ~2.0 × 2.5 m | ~2.5 × 3.5 m | ~2.0–2.5 m | American frontier chapter §8 |
| Draw-loom (figured silk, with pattern superstructure) | ~1.5–2.0 × 3.0–4.0 m | ~2.0–2.5 × 3.5–4.5 m | **2.5–3.5 m minimum** (pattern heddle rack adds 1–2 m vertical clearance) | Song-China chapter §3; Tokugawa chapter §3 and §8 [CITATION-NEEDED: physical dimensions from Song or Ming archaeological or technical source; Kuhn 1988 expected reference] |

**Ceiling height is a draw-loom-specific requirement.** For all loom types except the
draw-loom, ceiling height is not a binding constraint under normal building conditions.
The draw-loom's pattern-heddle superstructure requires clear vertical height of
2.5–3.5 m — the only weaving configuration where this becomes significant. Catalog
entries proposing draw-loom or Jacquard-loom installations must declare ceiling height
as a constraint parameter.

**Loom footprint is not the total workshop footprint.** Warping frames (for warp
preparation), wet-finishing areas, drying/tentering space, and material storage all
add to the total space requirement beyond the loom body. See Section 6 (Auxiliary
Infrastructure) for the full footprint calculation.

### Auxiliary infrastructure

All four cultures indicate the following auxiliary infrastructure as functional
requirements, not optional additions:

- **Warping frame.** Warp preparation (measuring and winding warp threads to length
  under uniform tension) requires a separate warping frame or warping board before
  loom threading. This step is a significant fraction of total production time; a
  workshop without dedicated warping infrastructure is not a production-ready operation.
- **Wet-finishing area.** Woven wool cloth is not finished at the loom. Wet-finishing
  — washing, optional fulling, drying under tension — is mandatory for quality wool
  and silk production [american-frontier chapter §8; medieval-northern-europe chapter
  §Functional Requirements Learned; tokugawa-japan chapter §8]. This requires: water
  supply, wash tubs, and drying/stretching frames. For fulled woolen broadcloth,
  fulling capacity (mill or powered equivalent) is required. Catalog entries proposing
  woolen cloth production must include wet-finishing infrastructure or state dependency
  on third-party finishers.
- **Thread storage and preparation area.** Bobbins, shuttles, and prepared weft thread
  (wound on bobbins) require a preparation area separate from the loom working space.
- **Fiber and yarn storage.** All four cultures stored raw or spun fiber adjacent to
  the workshop. Unlike forge fuel storage, there is no fire-safety separation
  requirement; the constraint is humidity control (see Section 2).
- **Dyestuff supply (if dyeing on-site).** Dyeing was a distinct guild operation in
  medieval northern Europe [medieval-northern-europe chapter §Supply Chain]; a separate
  dye house with water access, heating, and mordant storage is required if dyeing is
  performed on-site. Modern operations typically purchase pre-dyed yarn, deferring
  this dependency to the supply chain.

---

## 6. Operator Profile

### Skill floor by operation type

| Operation type | Minimum skill level | Notes |
|---|---|---|
| Winding bobbins, fetching thread, general material handling | Untrained helper | Historically performed by household members, children, apprentices |
| Simple backstrap or rigid-heddle weaving (narrow cloth, plain weave) | Apprentice-accessible | Can be learned in weeks to months; no complex shedding or pattern required |
| Four-shaft plain-weave production (household treadle loom) | Journeyman | Setting a warp, maintaining even sett, managing tension, correcting errors requires formed judgment; competent weaver trainable in 1–3 years [medieval-northern-europe chapter §Functional Requirements Learned] |
| Multi-shaft pattern weaving (overshot coverlet, twill, complex tabby structures) | Journeyman to master | Eight-shaft overshot or coverlet-quality production requires experience with draft interpretation and tension management |
| Draw-loom pattern operation (draw-boy / pattern assistant) | Trained assistant, not full weaver skill | Pattern reading and cord-pulling in sequence; physically distinct from primary weaver skill; historically performed by children or adolescents [song-china chapter §2; tokugawa-japan chapter §2] |
| Figured silk on draw-loom (master weaver role) | Master | Coordinating shed sequence, managing fine silk warp under tension, correcting figured-pattern errors requires extensive experience [song-china chapter §8; tokugawa-japan chapter §8] |
| Tapestry / *kesi* / *tsuzure-ori* | Master only | Discontinuous weft, pictorial representation, pattern fidelity without mechanical guidance; not learnable from a production schedule [song-china chapter §Products; tokugawa-japan chapter §Products] |
| Warp sizing (starch application and preparation) | Journeyman | Correct starch concentration and application technique affects warp durability throughout the entire production run; errors are not correctable after threading |
| Wet-finishing (washing, fulling, tentering) | Trained helper to journeyman | Fulling and tentering require judgment to avoid over-felting or distortion; washing is helper-level |

**Draw-loom is a two-operator-minimum configuration.** Draw-loom patterned weaving
cannot be performed by a single operator in its historical form: the master weaver at
the treadles and the draw-boy at the pattern heddles above are simultaneously required.
This is a binding minimum crew specification, not an efficiency optimization.
The Jacquard mechanism converts this to a single-operator task by automating the
pattern-selection function; any catalog entry claiming single-operator patterned draw-
loom-equivalent production must specify Jacquard (or computer-controlled dobby/Jacquard)
as the mechanism, not the historical draw-loom form [tokugawa-japan chapter §3;
song-china chapter §Functional Requirements Learned].

### Concurrent operators

| Loom type | Minimum viable crew | Notes |
|---|---|---|
| Backstrap, rigid heddle, household treadle (plain weave) | 1 weaver | Single-operator form across all cultures |
| Broadcloth floor loom (1.5–2 m wide, pre-flying-shuttle) | 2 weavers (shuttle throw + return) | Medieval-northern-europe chapter §The Loom; [CITATION-NEEDED: Carus-Wilson or Munro on two-person broadcloth operation confirmation] |
| Draw-loom (figured silk, pre-Jacquard) | 1 master weaver + 1 draw-boy | Song-China chapter §2 and §3; Tokugawa chapter §2 and §3 |
| Jacquard-equipped loom (any width) | 1 weaver | Jacquard eliminates draw-boy requirement; single operator can produce patterned cloth |

### Apprenticeship and skill transfer

The four cultures transferred weaving skill through structurally different mechanisms.
The divergences are significant for Plan C entries claiming `apprentice_friendly: true`.

| Culture | Apprenticeship mechanism | Duration | Notes |
|---|---|---|---|
| Medieval N. Europe (guild town) | Formal indenture; guild-regulated; masterpiece required | 3–7 years | Market-exclusion function alongside quality function [Ogilvie 2019]; guild weavers predominantly male for broadcloth |
| Medieval N. Europe (putting-out rural) | Informal; intergenerational household transmission | Variable | No institutional control; women weavers; piece-rate not training-based |
| Song China (household) | Informal; mother-daughter transmission (*nangeng nüzhi* dyad) | Variable | Intergenerational; no institutional oversight; female-dominated |
| Song China (imperial workshop) | Hereditary artisan registration (*jianghu*); not a training program — an administrative binding | Lifelong; hereditary | Not voluntary occupational identity [song-china chapter §2] |
| Tokugawa Japan (Nishijin) | *Detchi-boko* indenture; master-workshop binding | Multi-year; non-standardized | Vertical authority within workshop lineage; no horizontal guild body; no city-wide examination [Leupp 1992] |
| Tokugawa Japan (rural cotton) | Informal; mother-daughter; seasonal | Not formalized | No licensed entry; no credential; household transmission only |
| American frontier (professional itinerant) | Informal; private indenture or observed practice | Shorter, variable | No formal examination; high skill variance across practitioners |
| American frontier (household) | Intergenerational household; daughters from mothers | Not formalized | Collapsed when factory cloth adoption eliminated the economic rationale for learning |

**Minimum pipeline for succession.** A weaving operation targeting professional-grade
output requires a multi-year skill acquisition path — 1–3 years for journeyman plain-
weave competence; more for pattern or draw-loom mastery. The collapse of household
weaving on the American frontier was accelerated by the simultaneous failure of
informal skill transmission once factory cloth made the skill economically irrational
to acquire [american-frontier chapter §7]. Any Plan C catalog entry claiming
`apprentice_friendly: true` must populate the `apprentice_path` sub-fields and specify
the transmission model being followed.

**Labor-regime falsifier.** Historical per-unit economics incorporated: unpaid household
women's labor (all four cultures for spinning and domestic-level weaving), household
child labor in sericulture and draw-loom operation (Song China, Tokugawa Japan),
*jianghu* hereditary-registration compulsion (Song China), guild-suppressed journeyman
wages (medieval northern Europe), and putting-out piece rates without collective
bargaining (medieval and Tokugawa). None of these cost structures are replicable under
contemporary labor law. Modern weaving operations must price skilled weaver labor,
spinning-step labor or purchased yarn, and draw-loom assistant labor at market rates.
The historical cost structure does not transfer; the functional technical requirements
do [medieval-northern-europe chapter §Functional Requirements Learned; song-china
chapter §8].

---

## 7. Supply-Chain Dependencies

No anchor culture operated a supply-chain-autonomous weaving operation.

| Dependency | Medieval N. Europe | Song China | Tokugawa Japan | American frontier |
|---|---|---|---|---|
| Raw fiber | English premium wool via Staple at Calais; finest Flemish broadcloth entirely dependent on imported English wool [Power 1941; Lloyd 1977] | Silk: sericulture in Jiangnan (non-separable upstream); ramie/hemp: rural tax-household production; cotton: marginal in Song period | Silk: Chinese imports via Nagasaki or domestic sericulture in Joshinetsu region; cotton: Kinai and Tokai cultivation via Osaka commodity market; indigo: Awa domain near-monopoly | Wool: local flocks but carding/spinning bottleneck; flax: cultivation collapsed by mid-19th c.; cotton: purchased machine-spun yarn from 1830s–1840s onward |
| Spinning (prior step) | 4–10 household spinners per loom (women and children); spinning jenny (1764) first broke this bottleneck — handloom weaving *expanded* initially when cheap machine-spun yarn became available | Household women spun ramie and hemp; silk reeling by specialist reelers or same household; draw-loom weavers purchased thread | Cotton spun in same household or purchased via Osaka thread merchants; silk thread purchased from sericulture households | Household spinning was labor bottleneck; custom carding/spinning mills appeared 10–30 years after frontier settlement; machine-spun purchased yarn by 1830s–1840s [american-frontier chapter §6] |
| Dyestuffs | Woad (Picardy/Toulouse), madder (Zeeland), weld (northern Europe), kermes grain (Mediterranean import); dyers' guild separate from weavers [Cardon 2007] | Safflower, indigo, gardenia yellow, lac insect purple; some imported via maritime Silk Road [song-china chapter §Supply Chain] | Indigo: Awa domain (*sukumo*); safflower: Yamagata domain; both through wholesale networks [tokugawa-japan chapter §6] | Indigo: imported throughout period; madder, walnut hull: regional; aniline dyes displaced natural dyeing from mid-1860s [american-frontier chapter §6] |
| Finishing (fulling, tentering, shearing) | Fulling mills (water-powered by 12th–13th c. in England; later in Flanders); tenter frames; cloth shearers — all distinct from weaving; broadcloth cannot be sold without finishing [Carus-Wilson 1941] | Degumming (*jingsuo*) for silk: 20–30% weight loss; specialized finishing process [Kuhn 1988; CITATION-NEEDED: weight-loss figure confirmation] | Wet finishing on *shinshi* stretcher frames; silk degumming; separate finishing step from loom production [tokugawa-japan chapter §8] | Fulling mills (water-powered) on frontier rivers; geographic access constraint; hand-fulling was fallback [american-frontier chapter §6] |
| Distribution | Merchant-clothiers organized finishing and sale; Flemish *ton'ya* equivalent held distribution; Italian merchant capital financed English wool trade [Power 1941] | State imperial workshops: administrative distribution; commercial workshops: silk merchants (*sibo*) and *shibo si* export licensing [Shiba 1970] | Wholesale *ton'ya* controlled Nishijin silk distribution and cotton-cloth markets; weavers were price-takers [Leupp 1992; tokugawa-japan chapter §5] | Itinerant professional weavers: direct customer relationship; household production: no market channel; Shaker: communal sale; general merchandise stores supplied finished factory cloth by 1840s |

---

## 8. Product Category Matrix

Four product categories appear consistently across all four anchor cultures, with
distinct throughput, skill, and market characteristics.

| Category | Throughput profile | Skill floor | Industrial displacement | Survived? [canonical verdict] |
|---|---|---|---|---|
| **Commodity plain cloth** (everyday cotton, wool flannel, linsey-woolsey, plain ramie) | Higher volume; repetitive plain weave | Journeyman or household-level | Displaced earliest: American factory cloth from 1814–1880s; Japanese machine-cloth by 1890s; Song-era ramie displaced by cotton first (Yuan/Ming), then by machine cloth (19th c.) | No — genuine demand-collapse in all 4 cultures [`decline`] |
| **Commercial broadcloth / figured-ground cloth** (wool broadcloth, plain-ground silk) | Medium volume; requires guild-quality warp setup and consistent production | Journeyman (broadcloth); journeyman-to-master for fine grades | Partly displaced by factory production; guild-town organization collapsed (Flemish cities); putting-out survived longer; factory power-loom eventually displaced | Partial — from guild-town form to putting-out [`restructuring`]; eventually [`decline`] for hand-woven commodity grade |
| **Pattern weaving and specialty cloth** (overshot coverlets, multi-shaft pattern cloth, Nishijin brocade, Echigo-chijimi ramie crepe) | Lower volume; pattern-specific; non-fungible | Journeyman-to-master | Partial displacement; pattern complexity and non-fungibility provided partial protection; Jacquard adoption extended viability; Nishijin survived as luxury specialty | Partial — `restructuring` into luxury and custom specialty niche; not continuity of the pre-industrial volume form |
| **Tapestry and pictorial weave** (*kesi*, Arras/Brussels tapestry, *tsuzure-ori* panels) | Very low volume; measured in days per unit area; bespoke commissions | Master only | Not displaced by industrial production (technique is not mechanizable at equivalent quality); market is entirely luxury and institutional | Yes — `restructuring` into prestige craft; surviving precisely because standardization cannot replicate it |

**Commodity-cloth displacement was total and rapid.** The American frontier weaving
chapter provides the clearest case: household commodity cloth production experienced
demand-collapse driven by factory competition; the women who stopped weaving did so
willingly because factory cloth was cheaper and better [Strasser 1982]. This
pattern repeated across all four cultures, on different timescales. Catalog entries
modeling revenue from plain-commodity-cloth production are not matching this historical
precedent.

**Pattern complexity and non-fungibility are the surviving structural features.** The
product categories that survived industrialization (tapestry, prestige brocade, custom
coverlets) shared the property that industrial production could not replicate the
specific product at a price point competitive with custom or specialty demand. This is
the relevant design criterion for a modern revival weaving operation: not "can it
compete with a factory on plain cloth?", but "does it produce something a factory
cannot replicate at a relevant price point?"

---

## 9. Functional Requirements Summary Table

This table is the direct handoff to Plan C catalog authorship. Every catalog entry for
a weaving-trade operation must address each row or explicitly state inapplicability.

**Caveat on throughput requirements (R-07 through R-09):** Throughput values are
order-of-magnitude estimates from production-process reasoning. Primary-source
verification (Tryon 1917, Munro/Carus-Wilson, Kuhn 1988) is cited but page-level
confirmation is outstanding. Catalog entries citing these figures must carry a
high-uncertainty flag until primary-source page citations are confirmed.

| # | Requirement | Historical value(s) | Modern-equivalent expectation for Plan C entries |
|---|---|---|---|
| R-01 | Humidity control — wool | 65–75% RH; below 45%: static and breakage; above 75%: felting [american-frontier §3; medieval-N-europe §Functional Requirements] | Declare humidity management method for wool workshop; flag if operating in dry-climate or dry-winter environment without active humidity control |
| R-02 | Humidity control — silk | 65–70% RH; temperature 18–22°C preferred; silk weakens at sustained high temperature [song-china §3; tokugawa §8] | Declare humidity and temperature management for silk workshop; passive management (siting, seasonal scheduling) must be specified or active HVAC required |
| R-03 | Humidity control — cotton/linen | 50–65% RH; less sensitive than wool or silk | Declare ambient humidity range; flag if below 45% (warp tension problems) or above 80% (adhesion and mold risk) |
| R-04 | No temperature requirement (loom) | Loom itself has no temperature requirement under normal ambient conditions; operator comfort is the practical temperature floor | No temperature requirement field for loom; sericulture (if on-site) has a separate 22–28°C silkworm-rearing requirement |
| R-05 | Loom footprint — plain weave | 4-shaft floor loom: 2.0 × 3.0 m practical; narrow household treadle: 1.5 × 2.5 m; broadcloth: 2.5 × 4.5 m+; backstrap: none permanent [american-frontier §8; medieval-N-europe §Functional Requirements] | Declare `footprint_m2` for loom plus operating space; specify loom type; backstrap entries may declare 0 fixed footprint with anchor-point requirement |
| R-06 | Loom footprint — draw-loom | 2.0–2.5 × 3.5–4.5 m practical; ceiling height 2.5–3.5 m minimum [song-china §3; tokugawa §8] | Declare ceiling height constraint for any draw-loom or tall-superstructure loom; this is the one weaving configuration where ceiling height is a binding requirement |
| R-07 | Throughput — plain weave | 5–25 m/day (4-shaft floor loom); 1–3 m/day (plain silk); 0.9–1.8 m/day (broadcloth, two-person) | Declare `throughput_m_per_day` and specify loom type and product type; do not use a generic "weaving throughput" figure |
| R-08 | Throughput — pattern weaving | 0.2–0.5 m/day (figured silk draw-loom); days per unit area (tapestry/*kesi*) | Declare throughput at claimed pattern complexity level; plain-weave throughput may not be cited for a pattern-weaving catalog entry |
| R-09 | Spinner-to-loom ratio | 4–10 spinners per active loom [CITATION-NEEDED: primary source verification] | State whether spinning is included in the operation or whether spun yarn is purchased externally; if purchased, state that the spinner-to-loom constraint is transferred to the industrial supply chain |
| R-10 | Fiber supply chain | Raw fiber always externally sourced in all 4 cultures; no fiber-autonomous weaving operation documented | Declare fiber type and source; no entry may claim fiber-supply autonomy without explicit documentation of on-site sericulture or fiber production capacity |
| R-11 | Operator skill floor | Backstrap/simple: apprentice-accessible; 4-shaft plain: journeyman; multi-shaft pattern: journeyman-to-master; draw-loom master: master; tapestry: master only | Declare `operator_skill_floor`; specify which operations are within scope; draw-loom master weaver and tapestry weaver are distinct skill categories |
| R-12 | Concurrent operators — draw-loom | 1 master + 1 draw-boy minimum (pre-Jacquard historical form) | Declare `operators_concurrent`; if pattern weaving is claimed, specify whether Jacquard (single-operator) or draw-loom (two-operator minimum) form is being evaluated |
| R-13 | Concurrent operators — broadcloth | 2 weavers for pre-flying-shuttle broadcloth (shuttle throw + return) | For broadcloth-width loom entries: declare two-operator requirement; flying shuttle removes this constraint for modern floor looms |
| R-14 | Warping infrastructure | Warping frame or board required for warp preparation; not optional for production-scale operation | Declare warping equipment as part of workshop infrastructure; warp preparation time is a non-trivial fraction of total production time |
| R-15 | Wet-finishing — wool | Washing + optional fulling + tentering mandatory for finished woolen cloth quality; fulling mill or powered equivalent required for broadcloth [american-frontier §8; medieval-N-europe §Supply Chain] | Declare wet-finishing method; state whether on-site (wash tubs, stretching frames, fulling mechanism) or third-party finisher dependency |
| R-16 | Wet-finishing — silk | Degumming (*jingsuo*): 20–30% weight loss in sericin removal; mandatory for finished-silk quality [Kuhn 1988; song-china §8] [CITATION-NEEDED: weight-loss figure confirmation] | Declare degumming method and pricing implications of weight loss for silk catalog entries |
| R-17 | Finishing — broadcloth specifically | Fulling + tentering + shearing all required; commercially organized as three separate guild operations in medieval northern Europe; merchant-clothier coordinated finishing | State whether all three finishing steps are on-site, contracted, or omitted (and if omitted, whether output is marketed as unfinished cloth) |
| R-18 | Apprentice path | 1–3 years journeyman plain-weave competence; longer for pattern and draw-loom mastery; cultural models vary widely (European guild: 3–7 years; Japanese *detchi-boko*: multi-year informal; frontier: variable informal) | If `apprentice_friendly: true`, populate all `apprentice_path` sub-fields; specify which cultural model is being followed; household-transmission model (female, seasonal) is a distinct form from guild indenture |
| R-19 | Labor-regime adjustment | Household women's unpaid labor, child labor (sericulture and draw-boy), *jianghu* compulsion, guild-suppressed wages — none replicable under modern labor law | State explicitly whether cost estimates assume market-wage labor throughout; historical per-unit costs must be upward-adjusted for modern operations |
| R-20 | Industrial displacement trajectory | Commodity plain cloth displaced earliest and most completely; pattern and specialty survived longest via non-fungibility; tapestry never mechanically displaced | Catalog entry's `## Known risks` section must address which product segment the entry competes in and that segment's displacement history |
| R-21 | Dyestuff supply chain | Dyestuffs always externally sourced (woad, madder, kermes, indigo, safflower) or from regional commodity monopolies (Awa indigo, Yamagata safflower); modern aniline dyes from chemical supply | Declare dye source; if natural dyeing claimed, state botanical/mineral sourcing; if aniline (standard modern path), state supplier type |
| R-22 | Product category scope | See §8 matrix; plain commodity cloth is not a viable primary revenue segment for a modern hand-weaving operation; pattern, specialty, and custom categories are the supported segments | State product mix scope; if commodity cloth is proposed, document departure from historical survival baseline and justify against industrial competition |
| R-23 | Scale of operation | Household/backstrap: 1 operator, minimal footprint; professional floor-loom: 1–2 operators, 20–40 m² workshop; draw-loom figured silk: 2+ operators, dedicated climate-managed workshop | Declare `scale_fit`; draw-loom entries require separate humidity, ceiling, and crew specifications from plain-weave entries |
| R-24 | Sericulture dependency (silk entries only) | Silk thread is non-separable from sericulture upstream; a modern silk weaving operation that sources reeled thread from a market supplier transfers but does not eliminate this dependency [song-china §8] | If silk weaving entry: declare whether sericulture is on-site, contracted, or purchased thread; if purchased, name the supply source and its robustness to disruption |
| R-25 | Warp sizing | Rice-starch paste sizing of cotton and ramie warp documented in Song China and Tokugawa Japan; reduces warp breakage under repeated shed-opening tension [tokugawa-japan §8; CITATION-NEEDED: Song warp-sizing primary source] | Declare warp-sizing method for cotton and ramie entries; specify sizing material and drying time in production schedule |

---

## 10. Divergence Log

Per METHODOLOGY §7: where anchor cultures disagree on what a weaving operation must do
or be, the disagreement is documented here rather than suppressed.

**DIV-01: Fiber — wool vs. silk vs. cotton vs. bast fiber.**
The four cultures used different primary fibers: medieval northern Europe was
wool-dominant (with linen secondary); Song China was silk-dominant for prestige and
ramie-dominant for everyday cloth (cotton marginal in the Song period); Tokugawa Japan
was silk-dominant at the prestige level and cotton-dominant for everyday rural use by
the mid-period; the American frontier was wool-and-linen-dominant early, transitioning
to cotton mid-period. Each fiber has a distinct humidity requirement, upstream
dependency structure, and finishing requirement. *Implication for Plan C:* No single
fiber can be presented as "the" historical baseline. Catalog entries must declare
fiber type explicitly, and the requirements of each fiber type (humidity, spinning
upstream, finishing) vary materially.

**DIV-02: Loom type — plain treadle vs. draw-loom.**
All four cultures used multiple loom types simultaneously at different scales and for
different products. The draw-loom was the prestige production instrument for figured
silk in Song China and Tokugawa Japan; it did not exist in the American frontier
context; it was present but for tapestry only in medieval northern Europe. The
plain four-shaft treadle loom was the dominant form for household and commodity
production across all four cultures. *Implication:* A catalog entry for a "weaving
operation" without specifying loom type is incomplete. The functional requirements
(crew, ceiling height, throughput, skill floor) differ substantially between loom
types.

**DIV-03: Guild vs. household vs. commercial vs. state workshop organizational form.**
Medieval northern Europe had a sophisticated urban guild structure (for broadcloth
masters) operating simultaneously with a rural putting-out system (piece-rate rural
weavers with no guild protection). Song China had state imperial workshops (*guansi*)
binding *jianghu* households, rural household tax-production, and urban merchant-
commercial workshops — three forms with no equivalents elsewhere. Tokugawa Japan
had the Nishijin *nakama* guild-analog with vertical workshop authority, rural cotton
household production, and regional specialist workshops. The American frontier had
household production (female, unpaid), itinerant professional production (male, paid),
and Shaker communal production (cooperative, commercial). *Implication:* The "typical
weaver" abstraction is misleading. Catalog entries must specify the organizational
form they represent.

**DIV-04: Spinning as integrated vs. separated step.**
Medieval northern Europe treated spinning as an integrated upstream step: 4–10 household
spinners per loom, part of the same household or putting-out network. Song China
integrated sericulture-reeling-weaving in the same household for plain silk; specialized
reelers existed for commercial silk. The American frontier separated spinning from
weaving progressively: first via water-powered carding mills (10–30 years post-
settlement), then via purchased machine-spun yarn (by 1830s–1840s). Tokugawa Japan
had the same trajectory: domestic cotton spinning displaced by machine-spun yarn in
the Meiji period. *Implication:* The spinner-to-loom ratio (R-09) is a load-bearing
constraint for any catalog entry that includes spinning on-site, and an explicitly
dismissed constraint for entries that source purchased machine-spun yarn. Both are
historically documented paths; catalog authors must declare which path they follow.

**DIV-05: Finishing dependency — on-site vs. contracted vs. absent.**
Medieval northern Europe organized finishing (fulling mill, tenter frames, shearing) as
three distinct guild operations coordinated by the merchant-clothier; no single-workshop
operation controlled all three. The American frontier used water-powered fulling mills
at the frontier settlement scale — a contracted dependency. Song China integrated
degumming within the household or commercial workshop. Tokugawa Japan used *shinshi*
stretcher finishing within the workshop plus silk degumming. *Implication:* The
finishing dependency is structurally variable by fiber and scale. A modern catalog
entry must state explicitly whether finishing is on-site or contracted, and must not
imply that loom output equals finished cloth without documenting the finishing step.

**DIV-06: Industrial displacement timing — early vs. late in the period.**
American frontier weaving competed against machine-made cloth from the period's start:
the Boston Manufacturing Company's power looms were operational at Waltham by 1814,
within the period's opening decade. Medieval northern Europe's handloom weaving did not
face power-loom displacement until the 1820s–1840s, well after the period documented
here. Song China faced machine-textile competition from British imports only from the
1840s onward. Tokugawa Japan's household cotton weaving was displaced in the Meiji
period (1868 onward). *Implication:* The "frontier as early adopter of industrial cloth"
is a genuine divergence from the other three cultures. Any synthesis that assumes
the pre-industrial period represents a uniform baseline before industrial displacement
is incorrect for the American frontier case.

---

## 11. Sources

Sources cited in this document, inherited from the four anchor-culture chapters.
Full bibliography deferred to `research/trades/weaving/SOURCES.md` (Task 8).

1. Power, Eileen. 1941. *The Wool Trade in English Medieval History*. Oxford University
   Press. [English wool trade, Flemish dependence on English wool, Cistercian wool
   production — foundational on medieval wool economy]
2. Power, Eileen. 1975. *Medieval Women*. Edited by M.M. Postan. Cambridge University
   Press. [Gender division of labor in medieval craft production]
3. Carus-Wilson, E.M. 1941. "An industrial revolution of the thirteenth century."
   *Economic History Review* 11(1): 39–60. [Fulling mills, water power in cloth
   production, English cloth industry rise]
4. Carus-Wilson, E.M. 1952. "The woollen industry." In *The Cambridge Economic History
   of Europe*, vol. 2. Cambridge University Press. [Comprehensive survey of English
   and Flemish cloth industry]
5. Ogilvie, Sheilagh. 2019. *The European Guilds: An Economic Analysis*. Princeton
   University Press. [Guild economic function, journeyman wage controls, admission
   barriers]
6. Kuhn, Dieter. 1988. *Science and Civilisation in China*, vol. V pt. 9: Textile
   Technology — Spinning and Reeling. Cambridge University Press. [Authoritative
   reference for Song-period loom technology, silk reeling, sericulture, draw-loom
   mechanics; degumming weight loss]
7. Bray, Francesca. 1997. *Technology and Gender: Fabrics of Power in Late Imperial
   China*. University of California Press. [Gender and household labor in Chinese
   textile production; fiber hierarchy; cotton expansion]
8. Shiba, Yoshinobu. 1970. *Commerce and Society in Sung China*. University of Michigan
   Center for Chinese Studies. [Hangzhou and Jiangnan commercial organization; silk
   merchant networks]
9. von Glahn, Richard. 2016. *The Economic History of China: From Antiquity to the
   Nineteenth Century*. Cambridge University Press. [Comprehensive fiscal and monetary
   history; Song *liangshui* system; silk as currency]
10. Leupp, Gary P. 1992. *Servants, Shophands, and Laborers in the Cities of Tokugawa
    Japan*. Princeton University Press. [*Shokunin* estate; *detchi-boko* apprenticeship;
    merchant economic power over craft labor]
11. Francks, Penelope. 1984. *Technology and Agricultural Development in Pre-War Japan*.
    Yale University Press. [Household cotton weaving; regional textile specialization;
    cotton adoption and spread in Japan]
12. Hanley, Susan B. 1997. *Everyday Things in Premodern Japan*. University of
    California Press. [Rural household economies; textile consumption and production]
13. Morris-Suzuki, Tessa. 1994. *The Technological Transformation of Japan*. Cambridge
    University Press. [Tokugawa and Meiji textile technology; Jacquard adoption in
    Nishijin; cotton and silk commodity circuits]
14. Dublin, Thomas. 1979. *Women at Work: The Transformation of Work and Community in
    Lowell, Massachusetts, 1826–1860*. Columbia University Press. [Lowell mill history;
    factory cloth production scale and timeline]
15. Strasser, Susan. 1982. *Never Done: A History of American Housework*. Pantheon Books.
    [Household labor economics; women's adoption of factory goods; demand-collapse
    analysis for household weaving]
16. Tryon, Rolla Milton. 1917. *Household Manufactures in the United States, 1640–1860*.
    University of Chicago Press. [Primary statistical source for household textile
    production, fiber supply, and decline — load-bearing for throughput and decline
    claims; page-level citations outstanding]
17. Ulrich, Laurel Thatcher. 1990. *A Midwife's Tale*. Knopf. [New England household
    economy including textile exchange; market dimension of household weaving]
18. Cardon, Dominique. 2007. *Natural Dyes: Sources, Tradition, Technology and Science*.
    Archetype Publications. [Woad, madder, weld, kermes — medieval dyestuffs]
19. Lloyd, T.H. 1977. *The English Wool Trade in the Middle Ages*. Cambridge University
    Press. [English wool quality, Staple system, export regulation]
20. [CITATION-NEEDED: RH requirements for wool weaving — textile engineering or
    conservation science source confirming the 65–75% range; american-frontier chapter
    §3 flags this as needing a citable primary source.]
21. [CITATION-NEEDED: Operational RH range for silk-thread weaving — experimental or
    conservation textile literature confirming the 65–70% range; song-china chapter
    §3 flags this as requiring an explicit humidity-range source.]
22. [CITATION-NEEDED: Spinner-to-loom ratio primary source — 4–10 figure widely cited;
    Munro or Carus-Wilson for medieval-northern-europe chapter §Labor Regime
    confirmation.]
23. [CITATION-NEEDED: Medieval broadcloth weaving throughput — picks per day or yards
    per day figures — Munro or Carus-Wilson; note present figures are author estimates.]
24. [CITATION-NEEDED: Tryon 1917 specific page range for throughput figures for
    19th-century American hand-loom weaving — load-bearing for R-07 and R-08.]
25. [CITATION-NEEDED: Draw-loom physical dimensions, Song or Ming period — height,
    length, working area; Kuhn 1988 expected reference for R-06 ceiling-height
    requirement.]
26. [CITATION-NEEDED: Degumming weight-loss figure (20–30% for silk) — Kuhn 1988
    technical basis; verify figure before citing R-16 as confirmed.]
27. [CITATION-NEEDED: Warp-sizing practice in Song China — starch sizing of silk and
    ramie warp; Kuhn 1988 or Song-period agricultural treatise; needed for R-25.]
28. [CITATION-NEEDED: Two-person broadcloth shuttle operation confirmation — Carus-Wilson
    or Munro on Flemish loom configuration; needed for R-13 and Concurrent Operators
    table.]
29. [CITATION-NEEDED: Floor-loom dimensional specifications for period American frontier
    floor looms — period weaving manual or museum collection dimensional data; needed
    for R-05 and Summary Table R-05.]
30. [CITATION-NEEDED: Jacquard adoption timeline in American professional hand-weaving;
    a textile-history monograph or museum collection study; needed for DIV-04 modern
    implications.]
31. Watt, James C.Y., and Anne E. Wardwell. 1997. *When Silk Was Gold: Central Asian
    and Chinese Textiles*. Metropolitan Museum of Art. [Kesi and luxury silk technical
    description; tapestry-weave silk production rate context]
