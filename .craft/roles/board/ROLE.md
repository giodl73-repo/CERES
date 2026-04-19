# Board Reviewers — Per-Trade Domain Experts

The board is **not permanent**. It is assembled on demand when a specific
artifact makes a domain claim that deserves expert scrutiny beyond what
the panel can provide.

## When Board Fires

- A catalog entry makes a specific technical claim (e.g., "induction
  forge reaches 1,400 °C for forge-welding") that panel reviewers flag
  as beyond their expertise.
- A playbook file recommends a design whose failure mode would be
  trade-specific (food-safety collapse, metallurgical failure, textile
  fiber degradation).
- The pitch narrative claims a historical precedent a generalist
  historian would accept but a specialist might contest.

## Board Composition per Trade

Each trade needs a board of **2–3 experts** spanning:

1. **Domain-history specialist** — e.g., historical-metallurgy for
   smithing, food-history for baking, textile-archaeology for weaving.
2. **Modern-practitioner specialist** — someone who actually runs
   the trade at the relevant scale today.
3. **Adjacent-engineering specialist** — e.g., combustion/thermal
   engineering for forge, fermentation chemistry for brewing,
   materials science for ceramics.

Boards are assembled per artifact, not per trade wholesale. A catalog
entry asking about induction forge temperatures needs a different
board than one asking about coal particulate capture.

## File Naming

`B-{trade}-{slug}.md` — e.g.:

- `B-smithing-historical-metallurgy.md`
- `B-smithing-modern-bladesmith.md`
- `B-smithing-induction-engineering.md`

## Template

Each board-member role file uses the same frontmatter and sectioning
as panel members. See the panel role files as reference.

Required fields:

```yaml
---
name: {short-name}
version: "1.0"
archetype: specialist
role: board
trade: {trade-slug}
status: active | historical | hypothetical
status_note: >
  If historical or hypothetical, explain briefly.
scope: local
applies_to: [catalog-entry]  # typically, but overridable per board member
domain_signals: []  # fill with trade-specific keywords that trigger this reviewer
rubric_contribution:
  primary: []   # fill with dimensions this board member dominates (e.g. [D2] for a source expert)
  secondary: [] # fill with dimensions this board member contributes to partially
---
```

Status can be:

- **active** — a real, living domain expert CERES references
- **historical** — a deceased figure whose writings are the standard
- **hypothetical** — a composite voice representing the consensus of
  a domain where no single figure dominates; always declared
