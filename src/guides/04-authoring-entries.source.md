# Authoring a Catalog Entry

A catalog entry takes a position in the design-tradeoff space: a specific
combination of size, capital cost, energy source, throughput, skill floor,
and ownership model. Before authoring, know which position you are filling
and why that position is not already covered by an existing entry.

---

## Before you write a single field

**Step 1 — Read the canonical schema.**
`catalog/SCHEMA.md` defines all base fields. Read it in full before authoring
anything.

**Step 2 — Read the trade schema.**
`catalog/<trade>/SCHEMA.md` defines trade-specific extensions (e.g., baking
requires `flour_source_declaration`; smithing requires fuel type and bellows
configuration). These are not optional.

**Step 3 — Read an existing entry.**
Read at least one complete entry in the target trade. The inline comments in
the YAML are the documentation. They explain each field's derivation, the
citation policy, and what the simulation engine expects.

**Step 4 — Read the decline verdict.**
`research/trades/<trade>/DECLINE-VERDICT.md` identifies the binding constraints
that caused this trade to decline. Some of these are **defining falsifiers**:
claims the entry must address or it is not a serious analysis. For baking, the
mill-dependency falsifier requires declaring `flour_source_declaration` and
addressing supply-chain risk explicitly.

```proof:callout kind=warning label="Don't skip the decline verdict"
The decline verdict is not background reading. It defines what a rigorous
entry must address. An entry that ignores the binding falsifiers will fail
panel review at P-6 (Skeptical Funder) and be sent back for revision.
```

---

## Filling the YAML frontmatter

### Identity block

Assign the next sequential id in the trade: if the last entry is `bake-015`,
yours is `bake-016`. Status starts at `draft`. Version starts at `"0.1"`.

```yaml
id: bake-016
trade: baking
name: "Descriptive name including key differentiating features"
tagline: "One sentence: who operates this, what it produces, what makes it distinct"
status: draft
version: "0.1"
supersedes: null
```

### Physical envelope

Fill `footprint_m2`, `ceiling_min_m`, and `ventilation` from the trade schema's
allowed ranges. Every value needs an inline comment explaining the basis:

```yaml
footprint_m2: 40
# Larger than Group A baseline (25 m²) because this design includes an
# integrated cold-room for walk-in proofer. [CITATION-NEEDED: commercial
# kitchen cold-room minimum footprint; illustrative from REQUIREMENTS.md §A2]
```

### Economics — the critical block

Fill all economics fields from the trade schema guidance. Every monetary value
starts as `inferred` and carries a `[CITATION-NEEDED: ...]` tag that names the
specific data source needed to verify it.

**Write the citation tag before the value, not after.** The tag should specify:
- What kind of source would verify this (e.g., "vendor catalog", "BLS survey",
  "trade association report")
- The approximate year range (e.g., "2024-2026")
- What specifically it would confirm (e.g., "price range for commercial spiral
  mixers in the 20-qt class")

Example:

```yaml
capital_cost: { low: 22000, mid: 38000, high: 65000 }
# [CITATION-NEEDED: capital cost data for commercial wood-fired deck ovens
# 2024-2026; vendor catalog data from Valoriani, Moretti Forni, or equivalent;
# NOT derived from gas or electric equivalents — wood-fired ovens are a
# distinct equipment category.]
# Low: entry-level new or high-quality used (~$22k). Mid: capable mid-range
# ($38k). High: premium purpose-built ($65k).
```

### sim_params — derive, don't guess

The `sim_params` block must be derived from the fields above it. Write the
derivation explicitly in the comment, not just the result:

```yaml
throughput_units_equiv_per_year: 18200
# Derivation:
# Step 1 — annual operating days:
#   5 days/wk × 52 wk × (1 − 0.10 holiday/rest) = 234 days/yr
# Step 2 — units per day:
#   80 loaves/day (throughput.loaves_per_day)
# Step 3 — apply downtime:
#   80 × 234 × (1 − 0.03 maintenance downtime) = 80 × 234 × 0.97 = 18,158
#   → rounded to 18,200.
# [Derived from throughput block above]
```

E-3 (Numeracy Checker) will verify this derivation. If the comment is absent,
the editorial gate will block promotion.

### results block

**Do not fill the results block manually.** It is populated by the Tier A
simulation run. Leave it empty or with null verdicts until the simulation has
run. If you see hand-filled results in an entry without a corresponding
simulation run record, flag it as a potential E-3 finding.

---

## The citation policy

```proof:callout kind=note label="The rule"
Every number that is not directly derivable from other fields in the same
entry must carry a citation or a [CITATION-NEEDED: ...] tag. An uncited
number blocks promotion to `validated`.
```

**Three tiers of citation:**

1. **Direct source** — a specific publication, survey, or dataset with enough
   detail to locate the relevant figure. E.g., "US EIA Electric Power Monthly,
   Table 5.3, 2023–2024 small-commercial blended rate."

2. **Structural inference** — a figure derived from other cited figures or from
   the trade schema's guidance ranges, with the derivation stated. The label
   is `label: inferred`.

3. **Placeholder** — a figure that is a best-estimate placeholder pending
   verification. The label is `[CITATION-NEEDED: ...]` with a specific source
   description. These figures are acceptable in `draft` and `reviewed` entries
   but block `validated`.

Never let a figure be uncategorized. Every number is either cited, structurally
inferred (with derivation), or flagged as needing verification.

---

## Prose sections

After the YAML closing `---`, write these sections in order:

### Summary (required)

Two paragraphs. First: what this design is and what makes it distinct from
other entries. Second: what the economics show at the target scale — the
binding constraints and what they mean.

Avoid narrative throat-clearing ("This entry explores..."). Start with the
design: "Bake-016 is a..."

### Design rationale (required)

Why does this specific design point exist in the catalog? What design question
does it answer that no other entry covers? Name the adjacent entries it differs
from and explain the differentiator.

### Historical lineage (required)

Which historical forms informed this design? Name them. Give the functional
inheritance: what requirement came from this historical form. Then add the
anti-romantic treatment: what the historical form does *not* provide (labor
economics, market structure, demand conditions that no longer apply).

```proof:callout kind=warning label="Anti-romantic requirement"
Historical forms supply functional requirements — temperature ranges,
throughput, fuel options. They do not supply economic instruction. Medieval
guild economics operated under labor-regime conditions that no longer exist.
Frontier subsistence production used unpaid family labor. Name the inheritance
and name the discontinuity. Panel reviewer P-5 (Historian) will catch any
historical romanticism.
```

### Key assumptions (required)

List the four or five largest load-bearing assumptions in the entry. Flag which
are `inferred` and which are supported by cited sources. This section is where
you flag the figures most likely to change under scrutiny.

### Operations reality

What does running this look like day-to-day? Use the `operations_reality`
YAML block as the source. The prose section should add context the YAML cannot:
what it feels like to run this in a bad week, what the operator is doing at
6 AM, what the failure mode looks like in practice.

### Known risks / failure modes

Name the top three to five failure modes. For each: what triggers it, how
severe it is, and whether there is a mitigation available within the design.
Do not omit failure modes because they are inconvenient.

### Target niche

Who is this design for? What specific combination of operator background, scale,
and market context makes this design the right choice? Answer the economic
question directly: at mid-case pricing and throughput, does the operator clear
the median wage threshold?

---

## E-3 sanity checks

Before submitting for panel review, run these cross-checks manually:

**Throughput ↔ labor:**
```
total_annual_hours = max_active_hours_per_week × 52 × (1 − downtime_fraction)
hours_per_unit = total_annual_hours ÷ throughput_units_equiv_per_year

These should match labor_hours_per_unit within factor-of-2.
```

**Payback ↔ implied revenue:**
```
gross_revenue = throughput_units_equiv_per_year × market_price_per_unit.mid
gross_margin = gross_revenue − (throughput × variable_cost) − annual_op_cost
payback = (capital_cost.mid + install_cost) ÷ gross_margin

Should match results block if populated.
```

**cost_sd range check:**
```
cost_sd ÷ cost_mean should be between 0.15 and 0.50.
cost_sd = (capital_cost.high − capital_cost.low) ÷ 4  (default derivation)
```

If any cross-check fails by more than a factor of 2, fix the inputs before
submitting. E-3 will catch it in editorial, but finding it now saves a review
cycle.

---

## Submitting for panel review

Once the entry is complete:

1. Set `status: draft`.
2. Verify that all YAML fields required by `catalog/SCHEMA.md` and
   `catalog/<trade>/SCHEMA.md` are present (even if their values carry
   `CITATION-NEEDED` tags).
3. Verify that all prose sections are written.
4. Run the E-3 cross-checks above.
5. Invoke `/ceres-panel` to trigger the six-voice panel review.

The panel will produce findings in `reviews/R1-P{1-6}-<entry-slug>.md`. After
addressing the findings, update the entry and increment the version. If changes
are substantial, a round-2 panel review (R2) fires.

After panel findings are resolved, advance `status` to `reviewed` and invoke
`/ceres-editorial` to trigger the promotion gate.
