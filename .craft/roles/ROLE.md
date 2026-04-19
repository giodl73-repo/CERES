# CERES Review Organization

CERES's quality system uses three review tiers, each with distinct
intellectual perspectives organized around productive tensions between
competing economic, civic, historical, and practical worldviews.

Every CERES artifact — spec, implementation plan, catalog entry, playbook
file, pitch narrative — passes through review. Reviews surface hidden
assumptions, expose weak claims, and force each design to withstand the
strongest honest objections from every relevant worldview.

## Tier Structure

```
PANEL (6 voices)          ── Every artifact. Permanent reviewers.
  The six voices represent the core productive tensions of
  local-production economics: private profit, member commons,
  municipal stewardship, hands-on craft reality, historical
  realism, and hard-eyed funder rigor.

EDITORIAL (3 lenses)      ── Final pass before an artifact is "validated".
  Citation, scope, numeracy. The cleanup that catches what the
  panel doesn't look for because they are arguing substance,
  not form.

BOARD (per-trade)         ── Assembled on demand for domain claims.
  Trade-specific domain experts (metallurgy, food science,
  textile chemistry, civil engineering, etc.). Not permanent —
  invited when a specific expert claim needs defense.
```

## Panel: Six Productive Tensions

The six voices create deliberate friction. No catalog entry, no economic
claim, no playbook recommendation survives without answering to all six.

```
P-1 Market ────────── P-2 Commons
  "profit or die"    vs    "who owns the tools?"

P-2 Commons ────────── P-3 Civic
  "voluntary assoc." vs    "taxation, public goods"

P-3 Civic ─────────── P-1 Market
  "library model"    vs    "competition, choice"

P-4 Craft ─────────── P-6 Funder
  "practitioner time" vs   "investor time"

P-5 Historian ──────── P-6 Funder
  "realism"          vs    "narrative compression"

P-4 Craft ─────────── P-5 Historian
  "modern adaptation" vs   "did this really work?"
```

These tensions prevent CERES from collapsing into any single mode:
pure market triumphalism, pure commons romance, pure civic paternalism,
pure craft nostalgia, pure historical antiquarianism, or pure
investor-deck polish.

## Role File Index

### Panel (permanent — every artifact)
| ID | Name | Lens |
|----|------|------|
| [P-1](panel/P-1-market-economist.md) | The Market Economist | Private profit, ROI, competitive reality |
| [P-2](panel/P-2-commons-theorist.md) | The Commons Theorist | Member-ownership, shared resources, governance |
| [P-3](panel/P-3-civic-steward.md) | The Civic Steward | Municipal finance, public-goods argument |
| [P-4](panel/P-4-craft-practitioner.md) | The Craft Practitioner | Hands-on reality, failure modes, maintenance |
| [P-5](panel/P-5-historian.md) | The Historian | Historical realism, anti-romanticism, anti-anachronism |
| [P-6](panel/P-6-skeptical-funder.md) | The Skeptical Funder | Check-writer rigor, strongest-objection surfacing |

### Editorial (permanent — validation gate)
| ID | Name | Lens |
|----|------|------|
| [E-1](editorial/E-1-citation-auditor.md) | The Citation Auditor | Every number sourced; no hand-waves |
| [E-2](editorial/E-2-scope-keeper.md) | The Scope Keeper | Scope drift, feature creep, spec/plan divergence |
| [E-3](editorial/E-3-numeracy-checker.md) | The Numeracy Checker | Unit economics sanity, math cross-checks |

### Board (per-trade — assembled on demand)
| ID | Template | Purpose |
|----|----------|---------|
| [B-0](board/ROLE.md) | ROLE.md | Template for creating trade-specific domain experts |

## When Each Tier Fires

| Artifact | Panel | Editorial | Board |
|---|---|---|---|
| Spec | all 6 | E-2 (scope) | optional |
| Implementation plan | all 6 | E-2 (scope) | optional |
| Catalog entry — draft | all 6 | — | — |
| Catalog entry — review → validated | — | all 3 | invited for expert claims |
| Playbook file | all 6 | all 3 | optional |
| Pitch narrative | all 6 | all 3 | — |

## Review Output

Reviews are written in the reviewer's voice — first person, in their
intellectual tradition, with specific references to the artifact under
review. No numeric scoring at the panel stage; that is a separate
scoring step against the rubric in `scoring/RUBRIC.md`.

Reviews land in `reviews/` with filenames that identify artifact,
round, and reviewer.

---

## Role Frontmatter Convention (v1.1)

As of v1.1, every role file carries three additional frontmatter fields.
These fields do not change how the current skills invoke reviewers (the
roster remains hard-coded in each skill). They prepare the role library
for future dynamic role-discovery and composable scoring aggregation.

### `applies_to`

Declares the artifact types this role reviews. Allowed values mirror the
artifact types in the tier-firing table above:

```yaml
applies_to: [spec, plan, catalog-entry, playbook-file, pitch-narrative]
```

**Panel** voices apply to all five artifact types.
**Editorial** gates apply only at promotion time — `[catalog-entry, playbook-file, pitch-narrative]`.
**Board** members default to `[catalog-entry]` but individual board members may override.

A future `ceres-check` skill will use `applies_to` together with
`domain_signals` to dynamically select the appropriate reviewer set for
any given artifact, replacing the current hard-coded roster pattern.

### `domain_signals`

A list of keywords / substrings. When an artifact's content contains one
or more of these signals, this role is a candidate for selection. Used by
future dynamic-discovery tooling (RMM pattern).

```yaml
domain_signals: [market, profit, ROI, payback, revenue, competition, wage, customer, TAM, SAM]
```

Signals are not exclusive: multiple roles may fire on the same signal.
Overlap is intentional — productive tensions require that competing
perspectives both weigh in on the same claim.

### `rubric_contribution`

Declares which scoring dimensions (D1–D6 in `scoring/RUBRIC.md`) this role
contributes to, and with what weight class:

```yaml
rubric_contribution:
  primary: [D4]      # this role dominates scoring for these dimensions
  secondary: [D2, D6] # this role contributes partial signal to these dimensions
```

**Primary** contributors weight 1.0 when scores are aggregated.
**Secondary** contributors weight 0.5.

This field is consumed by `scoring/RUBRIC.md`'s aggregation formula
(see Section "Aggregating role findings into dimension scores"). It does
not change how qualitative panel reviews are written; it maps reviewer
findings to the numeric scoring instrument.

### Placement in frontmatter

These three fields are placed after `scope` and before `collaborates_with`:

```yaml
scope: local
applies_to: [...]
domain_signals: [...]
rubric_contribution:
  primary: [...]
  secondary: [...]
collaborates_with: [...]
```

The `scope` field's semantics are unchanged:
- `local` — operates per-artifact
- `workspace` — operates across multiple artifacts
- `cross-artifact` — operates across the whole repo
