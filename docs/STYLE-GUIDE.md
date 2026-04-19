---
title: CERES Style Guide
version: "1.0"
created: 2026-04-18
spec: specs/2026-04-18-ceres-design.md
sections:
  - quality-bar
  - citation-format
  - tone
  - forbidden-framings
  - multi-currency-conventions
  - unit-conventions
  - voice-and-point-of-view
---

# CERES Style Guide

Writing and citation conventions for all CERES artifacts. Every rule in this document
is concrete enough to be flagged mechanically by the editorial roles E-1 (Citation
Auditor), E-2 (Scope Keeper), and E-3 (Numeracy Checker). When a rule names an
editorial role, that role is the enforcement owner.

---

## 1. Quality Bar

**Standard:** Research-paper-level estimates. This means:

- Every economic number (capital cost, throughput, maintenance cost, market price,
  wage threshold) has a source citation. A number without a citation is a
  promotion-blocking finding for E-1 (P1).
- Every range is labeled as a range. Write `$18,000–$45,000 (low-to-high estimate)`
  or use the schema's `{ low: 18000, mid: 28000, high: 45000 }` triple. Do not
  collapse a range to a single number without stating that you are quoting the midpoint.
- Every estimate is labeled as an estimate. If a figure is derived, modeled, or
  interpolated rather than directly observed, say so: "estimated from [source],"
  "order-of-magnitude based on [source]," or "interpolated from [source] using
  [method]."
- Every historical claim has a citation to a recognized source in economic history,
  archaeology, or primary-source literature. Wikipedia-only or popular-press-only
  citations for load-bearing historical claims are a P1 finding for E-1.
- CERES is explicitly **not** due-diligence-grade (spec Section 13 non-goal). The
  quality bar is research-paper estimates, not supplier BOMs or real procurement
  quotes. Overstating precision is as bad as understating it.

**E-1 enforcement trigger:** Any numeric field in a catalog entry's frontmatter
(`capital_cost`, `annual_maintenance`, `market_price_per_unit`, `sim_params.*`) that
lacks a matching entry in `sources:` is a P1 finding. Any historical claim in prose
lacking an inline citation is a P1 finding.

**E-3 enforcement trigger:** Any number presented as a point estimate that is
actually an order-of-magnitude rough figure (i.e., precision implies more certainty
than the source supports) is a P3 finding. Any figure that does not cross-check
internally against other numbers in the same entry is a P1 or P2 finding depending
on severity (see `E-3-numeracy-checker.md`).

---

## 2. Citation Format

### Inline citations

Use `[Author YEAR]` format inline in prose:

> "Community forge capital costs in the range of $18,000–$45,000 [Weisdorf 2018]."

When citing to a specific page or section, include it:

> "Journeyman hourly output in a coal forge was approximately 6 small-work units per
> active hour [Smith 2014, pp. 112–115]."

When citing a dataset or survey (not a narrative work), name the dataset and year:

> "Tool-library capex ranges [ToolLibrary.org 2024 capex survey, Table 3]."

When citing a standard (OSHA, ISO, etc.), name the standard and section:

> "Ventilation requirements for hot-work environments [OSHA 29 CFR 1910.252(c)]."

### Sources blocks

**Catalog entries** use a `sources:` YAML array in frontmatter. Each entry has at
minimum a `ref:` string. Include page or section when available:

```yaml
sources:
  - ref: "Weisdorf 2018, Economic History Review, vol. 71(3), pp. 880–906"
  - ref: "ToolLibrary.org 2024 capex survey, Table 3"
  - ref: "OSHA 29 CFR 1910.252(c)"
```

**Research documents** (`research/trades/*/SOURCES.md`, `research/cultures/*/`)
use a `## Sources` section at the end of the document, formatted as a numbered list:

```markdown
## Sources

1. Weisdorf, Jacob. 2018. "From foraging to farming..." *Economic History Review*
   71(3): 880–906.
2. ToolLibrary.org. 2024. "Community Tool Library Capital Cost Survey." Table 3.
```

**Playbook and pitch files** use inline `[Author YEAR]` citations and a `## Sources`
section at the end. The pitch narrative (`playbook/pitch/PITCH-NARRATIVE.md`) is not
a catalog entry and does not use YAML frontmatter for sources.

### Source quality hierarchy

In order of preference:
1. Primary sources: original research, peer-reviewed journals, government statistical
   series, recognized trade-organization surveys.
2. Secondary sources: academic books citing primary research, established economic
   history literature.
3. Grey literature: industry association reports, NGO surveys — acceptable when
   primary/secondary sources are not available, but must be named explicitly and their
   provenance noted.
4. Not acceptable as sole support for a load-bearing claim: blog posts,
   Wikipedia, press releases, personal communications. These may appear as
   context or leads, but must be accompanied by a traceable primary or secondary
   source for any number or historical claim that appears in the artifact itself.

**E-1 enforcement trigger:** A source that cannot be located (dead URL, journal
article that does not exist, misquoted author or date) is a P1 finding regardless
of the claim it is meant to support.

---

## 3. Tone

### Analytical first, narrative second

CERES is not a manifesto and not an argument that industrial production is bad
(spec Section 13). The project's claim is about restoring *optionality and local
capacity*, not displacing industrial supply.

- Lead with evidence: data, cross-checks, simulation verdicts, cited historical forms.
- Narrative framing (the "why this matters" arc) belongs in the pitch narrative
  (`playbook/pitch/PITCH-NARRATIVE.md`), not in catalog entries, research documents,
  or playbook files.
- Catalog entries are technical records. Research documents are evidence compilations.
  Playbook files are action guides. The pitch narrative is the one place where
  persuasive voice is appropriate and expected.

### Avoid advocacy framing

Do not frame CERES findings as political positions. Specifically:

- Do not imply that restoring local production is a moral obligation.
- Do not frame industrial supply chains as inherently harmful or "corporate."
- Do not frame craft production as inherently virtuous.
- Do not invoke sustainability as a moral claim without citing a specific,
  quantified metric. "Local production is more sustainable" is forbidden without
  a source for the specific claim (lifecycle analysis, carbon accounting, water
  use, etc.).
- Policy advocacy belongs outside the scope of CERES (spec Section 13:
  "Not a political manifesto").

**E-2 enforcement trigger:** Advocacy framing in a catalog entry or research document
is a scope violation (P1 finding). The spec explicitly excludes political-manifesto
content. Advocacy framing in the pitch narrative is a P2 finding — persuasive but
rigorous is the standard; unsubstantiated advocacy is not.

### Don't romanticize pre-industrial life

Pre-industrial production was not a golden age. It involved dangerous working
conditions, child and apprentice labor, guild-enforced market exclusion, and forms
of household dependency that modern workers are not willing to reproduce. Documenting
historical forms honestly means documenting all of this, not only the craft skill.

See Section 4 (Forbidden Framings) for specific language to avoid.

---

## 4. Forbidden Framings

The following framings are prohibited across all CERES artifacts. Each is listed with
the specific language pattern to watch for and the rule violation it represents. These
are drawn from the P-5 Historian panel review (R1) and the CERES spec (Section 2
falsifiers, Section 13 non-goals).

### 4.1 "In the good old days" / nostalgia framing

**Prohibited phrases and equivalents:**
- "in the good old days"
- "when craftspeople still made things properly"
- "before industrialization destroyed local production"
- "once-vibrant traditions"
- "the way things used to be"
- "lost craftsmanship"
- "returning to our roots"
- "the craft revival"
- Any framing that positions pre-industrial production as a past optimum to be
  recovered rather than a historical baseline to be studied.

**Why:** CERES's working hypothesis (spec Section 2) is that the *equipment economics*
failed, not that something spiritually better was lost. The project tests this
hypothesis; it does not pre-assume a romantic narrative. If the research shows that
the historical form was actually limited, cruel, or economically contingent in ways
that cannot be reproduced, that is a finding.

**E-2 enforcement trigger:** Any instance of the prohibited phrases or their structural
equivalents in a catalog entry or research document is a P1 scope violation.
In the pitch narrative, P2 (should fix — replace with a specific, sourced claim).

### 4.2 Pre-industrial sustainability as an implicit assumption

**Prohibited implicit claims:**
- Asserting or implying that pre-industrial production was inherently "sustainable"
  without a source quantifying the specific claim.
- Treating the absence of fossil-fuel energy in historical forges or kilns as
  evidence of ecological virtue (charcoal production at scale caused extensive
  deforestation across medieval Europe and East Asia).
- Implying that local production = low environmental impact without citations.

**Rule:** Any sustainability claim requires a specific, quantified citation. Vague
sustainability language without a source is a P1 finding for E-1.

**Example of what to say instead:** "Song-era iron production required charcoal at
estimated rates of X kg per kg of iron produced [citation]; the regional deforestation
impact is documented in [citation]." State the evidence; let the reader draw
conclusions.

### 4.3 Elision of household and apprentice labor regimes

**Prohibited elisions:**
- Describing historical guild production without acknowledging that it typically
  relied on household labor (spouse, children, extended kin) and apprentice labor
  that was frequently coercive and unpaid or below-subsistence.
- Presenting historical per-unit costs that do not account for the labor of
  household members who were not paid a market wage.
- Citing a historical "craftsman's income" without specifying whether that figure
  includes or excludes household and apprentice contributions to production.

**Rule:** When citing historical per-unit costs or throughput figures, the citation
must address whether household and apprentice labor is included or excluded in the
source's methodology. If excluded, note it. This is a P1 citation finding for E-1 if
omitted from a load-bearing economic claim.

**Why this matters for CERES:** If historical viability rested on labor regimes that
cannot be ethically reproduced, then the working hypothesis has a falsifier (spec
Section 2: "Labor-regime dependency"). Eliding the labor regime makes a fair test
of the hypothesis impossible.

### 4.4 Guild-as-craft-quality framing

**Prohibited claim:**
- "Guilds ensured quality craftsmanship" as a stand-alone sentence or framing.
- Treating guild systems primarily as quality-assurance institutions without
  acknowledging their primary function as market-entry barriers, price-fixing
  cartels, and mechanisms for excluding competitors.

**Rule:** Any discussion of guild systems must acknowledge both functions: quality
regulation *and* market exclusion. A one-sided guild narrative is a P2 finding for
E-2 (scope drift toward romanticization) and for P-5 (historical inaccuracy).

**What to write instead:** "Guild systems served dual functions: establishing minimum
quality standards *and* restricting market entry to limit competition
[Epstein 1998; Richardson 2004]." Then assess both functions for the CERES context.

### 4.5 "Lost knowledge" claims without documentation

**Prohibited claim pattern:**
- "Traditional techniques have been lost" without citing what specific techniques
  are undocumented, why they are undocumented, and what the evidence base for
  the claim is.
- "Knowledge passed through apprenticeship chains that no longer exist" as an
  explanation for why a design is not in commercial use today, without sourcing the
  claim.
- Implying that reconstruction is necessary because knowledge was "lost" when the
  actual reason may be that the technique was economically noncompetitive or that
  modern analogs exist.

**Rule:** Claims about lost knowledge or lost techniques require:
1. A specific description of what knowledge is asserted to be undocumented.
2. A citation to a source that establishes the absence of documentation (not just
   the absence of a Wikipedia article).
3. A statement of what the evidence base for the historical technique is.

An unsourced "lost knowledge" claim is a P1 finding for E-1.

---

## 5. Multi-Currency Conventions

CERES catalog entries are authored in the currency that best matches the source data.
A German equipment comparison may be in EUR; an Australian tool-library survey in AUD.
These rules prevent silent currency conflation.

### 5.1 Declaration rule

Every catalog entry declares its currency in the `economics.currency` field. This
is a required field. An entry without a declared currency is incomplete and cannot
be promoted past `draft`.

```yaml
economics:
  currency: USD   # or EUR, GBP, JPY, etc.
```

### 5.2 Prose currency rule

Prose sections of a catalog entry use the declared currency without conversion. If
the entry's declared currency is EUR, all amounts in the prose body are in EUR.

Do not convert amounts to USD (or any other currency) in catalog entry prose. The
reason: informal prose conversions become stale when exchange rates change, and
they are not reproducible. Conversion lives only in simulation output.

### 5.3 Cross-currency comparison rule

Cross-currency comparisons (e.g., comparing a USD-denominated forge entry with a
EUR-denominated one) happen only in Tier A simulation output, using the FX snapshot
table in `corpus/program/CURRENCIES.md`. The snapshot date is recorded in that table
and must be cited when simulation results are quoted.

Do not compare cross-currency amounts in prose, catalog entries, or playbook files.

### 5.4 Historical cost data

Historical cost data cited in pre-2020 currencies (or in units such as shillings,
livres, or bushels of grain) must be:
1. Stated in the original unit as cited.
2. If converted to a modern currency for comparison, converted via the methodology
   documented in `corpus/program/CURRENCIES.md` (CPI adjustment + FX conversion,
   with the CPI series cited).
3. Labeled as a converted estimate with the conversion methodology stated.

**E-1 enforcement trigger:** Any cross-currency amount appearing in catalog entry
prose (not in simulation output) is a P2 finding. An amount in historical units
converted without citing the conversion methodology is a P1 finding.

---

## 6. Unit Conventions

### 6.1 Physical dimensions and masses

Use SI units throughout:
- Length: meters (m), millimeters (mm). Do not use feet/inches except when quoting
  a source that uses imperial units — in that case, keep the source's unit and add
  the SI equivalent in parentheses: "12 ft (3.66 m)."
- Area: square meters (m²).
- Mass: kilograms (kg). Larger masses: tonnes (t = 1,000 kg). Do not use "tons"
  without specifying metric ton (t) or short ton (US ton = 0.907 t).
- Temperature: degrees Celsius (°C) for operational ranges. Kelvin (K) only when
  citing thermochemical literature that uses it; add °C equivalent.

### 6.2 Energy

- Energy: kilowatt-hours (kWh) for electrical and thermal energy.
- Power: kilowatts (kW).
- Fuel quantities: state in natural units as sourced (kg coal, liters of propane,
  cubic meters of natural gas) and note the energy-content equivalent in kWh when
  relevant to cross-comparison.

```yaml
# Correct
energy_consumption_per_active_hour: "8 kg coal (~66 kWh thermal equivalent)"

# Incorrect (unitless or ambiguous)
energy_consumption_per_active_hour: 8
```

### 6.3 Throughput

Throughput must always carry:
- An explicit unit definition. Use the schema's named unit type (e.g., `small_work`,
  `medium_work`, `large_work`) as defined in the trade's SCHEMA.md. Do not use bare
  counts like "6 pieces/hour" without defining what "piece" means.
- An explicit timeframe: per-hour, per-week, per-year. Do not write throughput
  figures without stating the timeframe.

```yaml
# Correct
throughput:
  units_per_hour: { small_work: 6, medium_work: 2, large_work: 0.5 }
  max_active_hours_per_week: 45

# Incorrect (ambiguous timeframe)
throughput: 270 units
```

In prose, write: "6 small-work unit equivalents per active hour" — not "6 units/hour"
(which omits the unit type) and not "6/hr" (which is dimensionless).

### 6.4 Rates in prose

All rates in prose carry an explicit timeframe. Acceptable: "per hour," "per week,"
"per year," "per active hour," "per shift." Not acceptable: bare rates ("the forge
produces 6 units") without a stated timeframe.

**E-3 enforcement trigger:** A throughput figure without an explicit timeframe is a
P2 finding. A throughput figure using an undefined unit type is a P1 finding (the
sim code cannot ingest it).

### 6.5 Economic rates

Annual costs, annual revenue, and payback periods are stated per year unless
explicitly noted otherwise. Do not mix annual and monthly figures in the same
arithmetic chain without converting.

```
# Correct
annual_maintenance: 1500    # per year, USD
capital_cost.mid: 28000     # one-time, USD

# Incorrect (monthly and annual mixed silently)
annual_maintenance: 125     # this is monthly, mislabeled
```

**E-3 enforcement trigger:** Any mix of annual and monthly figures in a sim_params
cross-check is a P1 finding.

---

## 7. Voice and Point of View

Different artifact types require different voices. Using the wrong voice for the
artifact type is an E-2 scope finding.

### 7.1 Catalog entries — neutral technical voice

Catalog entries are technical records. Voice is third-person, declarative, neutral.
The entry describes; it does not advocate.

- Correct: "This forge design is suited to shared-access models in towns of
  2,000–15,000 residents. Coal fuel requires mechanical extraction; propane
  backup is included for periods when coal supply is disrupted."
- Incorrect: "This innovative forge reimagines community metalworking, bringing
  craft back to town centers and empowering local makers."

Do not use marketing language in catalog entries: no "innovative," "revolutionary,"
"empowering," "reimagining," "game-changing," "transformative." These phrases carry
no information and inflate the prose.

**E-2 enforcement trigger:** Marketing language in a catalog entry is a P2 finding
(stylistic drift toward non-goal: "not a political manifesto").

### 7.2 Research documents — evidential voice

Research documents (`research/cultures/*/`, `research/trades/*/`) present evidence.
Voice is scholarly: hedged where the evidence is thin, confident where it is strong,
transparent about the basis for each claim.

- State the strength of evidence: "The archaeological record for Song-era forges is
  thin before the 11th century; the following figures derive from Song Huiyao and
  secondary accounts [citations]."
- Do not substitute narrative confidence for evidential confidence. If the evidence
  is weak, say so.
- Do not editorialize. Present the historical record; do not tell the reader what
  to feel about it.

### 7.3 Playbook files — directive voice

Playbook files (`playbook/<trade>/<scale>.md`) tell practitioners what to do. Voice
is clear and directive.

- Correct: "At town scale (2,000–15,000), the cooperative lens produces the best
  verdicts. Start with forge-003 (Shared Tool-Library Coal Forge): break-even at
  18 members, achievable at this scale."
- Incorrect: "One might consider the possibility that forge-003 could potentially
  offer a viable pathway..."

Do not hedge in playbooks. The purpose is to synthesize the catalog and simulation
results into actionable recommendations. Uncertainty has already been accounted for
in the simulation; the playbook states the recommendation and names the open risks
explicitly, not through hedged language.

### 7.4 Pitch narrative — persuasive but rigorous voice

The pitch narrative (`playbook/pitch/PITCH-NARRATIVE.md`) is the one CERES artifact
written for persuasion. It argues that the project's findings are fundable and
actionable. But:

- Every claim in the pitch narrative must be traceable to catalog entries, simulation
  results, or cited research. The pitch cites the catalog as evidence; it does not
  generate new claims.
- Persuasion comes from the evidence, not from rhetorical amplification. "Fifteen
  forge designs evaluated across 135 simulation cells; 7 achieve win under the
  cooperative lens at town scale" is more persuasive than "local smithing is making
  a comeback."
- The pitch narrative may use narrative framing (opening with a problem, closing
  with an ask), but the body is evidence-driven.
- Marketing language is forbidden in the pitch as in any other artifact. If a claim
  cannot be sourced to the catalog or research corpus, it does not appear in the pitch.

**E-1/E-2 enforcement trigger:** An unsourced claim in the pitch narrative that
does not trace to the catalog, research corpus, or cited literature is a P1 finding.

---

## Self-Review Checklist

Before committing any artifact under this style guide, the author confirms:

- [ ] Every economic number has a source in the `sources:` block or `## Sources`
      section.
- [ ] Every range is labeled as a range; every estimate labeled as an estimate.
- [ ] Every historical claim cites a recognized source (not Wikipedia-only).
- [ ] No forbidden framing language appears (Section 4 checklist).
- [ ] Currency is declared in frontmatter (catalog entries); no cross-currency
      comparisons in prose.
- [ ] All physical units are SI (or quoted in source units with SI equivalent).
- [ ] All throughput figures carry explicit unit types and explicit timeframes.
- [ ] All economic rates are stated per year (or explicitly per month, with conversion
      if mixed).
- [ ] Voice matches artifact type (Section 7).
- [ ] No marketing language anywhere.
- [ ] No advocacy framing outside the pitch narrative (and none unsourced even there).
