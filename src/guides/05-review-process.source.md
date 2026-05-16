# Review Process

CERES has three review tiers and a fast-audit tool. Every artifact passes
through at least one tier before being used or cited. No exceptions.

---

## Overview

```proof:tree kind=org
Review tiers
- Panel (6 voices): qualitative review — fires on every artifact at draft stage
- Editorial (3 lenses): form gate — fires only at the promotion-to-validated step
- Board (per-trade experts): domain adjudication — on demand for contested claims
- ceres-check (cross-tier): structured findings table — any stage, any concern
```

**When each tier fires:**

| Artifact | Panel | Editorial | Board |
|----------|-------|-----------|-------|
| Spec, plan | all 6 | E-2 (scope) only | optional |
| Catalog entry — draft → reviewed | all 6 | — | — |
| Catalog entry — reviewed → validated | — | all 3 | invited for expert claims |
| Playbook file | all 6 | all 3 | optional |
| Pitch narrative | all 6 | all 3 | — |

---

## Panel — six voices

Panel fires on **every artifact at draft stage**. No exceptions. The six
voices represent productive tensions:

| Voice | Role | Primary lens |
|-------|------|-------------|
| P-1 Market Economist | Private market viability | Does the unit economics actually work? |
| P-2 Commons Theorist | Cooperative governance | Can a commons institution sustain this? |
| P-3 Civic Steward | Municipal investment | Is public expenditure defensible here? |
| P-4 Craft Practitioner | Hands-on reality | Does this actually work in practice? |
| P-5 Historian | Historical accuracy | Is the historical lineage honestly represented? |
| P-6 Skeptical Funder | Due diligence | Would a rigorous funder accept this as evidence? |

The six voices create deliberate friction across the core productive tensions
of local-production economics. No catalog entry is complete until it has
survived all six.

### What panel produces

Six review files, one per voice, in `reviews/`:

```
reviews/R1-P1-market-economist-<artifact-slug>.md
reviews/R1-P2-commons-theorist-<artifact-slug>.md
...
reviews/R1-P6-skeptical-funder-<artifact-slug>.md
```

Each file contains the voice's findings in severity-coded format.

### Finding severity codes

| Code | Meaning |
|------|---------|
| `P1` | Blocking — entry cannot advance until resolved |
| `P2` | Important — author must address and document decision |
| `P3` | Minor — author may resolve or document as acknowledged |

### How to invoke

```
/ceres-panel
```

Pass the artifact slug or file path. The skill runs all six voices in sequence
and writes the six review files. See `skills/ceres-panel/SKILL.md` for the
full invocation reference.

### After panel

Address all P1 findings before advancing `status`. For each finding, either fix
the issue or write a documented response explaining why the finding is not
applicable. Panel reviewers check resolution; they do not accept silence.

If changes are substantive (new fields, revised economics, changed design
premise), a round-2 review (R2) fires before advancing to `reviewed`. Minor
revisions do not require R2; the author documents resolution and advances.

---

## Editorial — three lenses

Editorial fires only when an artifact is ready to advance from `reviewed` to
`validated`. It is **not a discussion** — it is a checklist with teeth.

The three editorial lenses:

| Lens | What it checks | P1 trigger |
|------|----------------|-----------|
| **E-1 Citation Auditor** | Every number cited; historical claims verifiable | ≥3 uncited load-bearing figures |
| **E-2 Scope Keeper** | No spec drift; no non-goal violations; no schema additions | Any non-goal or schema breach |
| **E-3 Numeracy Checker** | Throughput ↔ labor; payback ↔ revenue; currency normalization; OOM sanity | Any order-of-magnitude error or internal contradiction |

**All three must pass.** A single `block` verdict from any lens holds the
artifact. An artifact is cleared only when all three lenses return `pass` or
`fix-and-recheck-resolved`.

### What editorial produces

```
reviews/CLEAN-E1-citation-<artifact-slug>.md
reviews/CLEAN-E2-scope-<artifact-slug>.md
reviews/CLEAN-E3-numeracy-<artifact-slug>.md
```

### How to invoke

```
/ceres-editorial
```

Only invoke after panel findings are resolved and `status: reviewed` is set.
See `skills/ceres-editorial/SKILL.md`.

### After editorial

If all three lenses pass: advance `status` to `validated` and record the
editorial clearance date in the entry's `## Iteration log`.

If any lens returns a P1 finding: set `status: held`. Fix the P1 findings, then
re-run the blocking lens. You do not need to re-run the passing lenses unless
the fix touches their domain.

---

## Board — domain experts

Board fires on demand when a panel voice flags a claim as beyond their
expertise, or when an author proactively requests adjudication of a contested
technical or historical claim.

```proof:callout kind=note label="When to invoke Board"
Board is not a routine review tier. Invoke it when:
(1) a panel reviewer writes "this claim requires specialist domain knowledge"
(2) an author is making a specific technical claim (e.g., alloy properties,
    firing temperatures, structural load capacity) that the six standard panel
    voices cannot verify.
```

Board members are assembled per claim — 2-3 domain experts relevant to the
specific trade and claim type. Definitions: `.roles/board/ROLE.md`.

### What board produces

```
reviews/BOARD-B-<trade>-<slug>-<artifact-slug>.md
```

### How to invoke

```
/ceres-board
```

Pass the specific claim to adjudicate, the trade context, and any relevant
background. See `skills/ceres-board/SKILL.md`.

---

## ceres-check — fast structured audit

`ceres-check` is not a separate review tier. It is a structured cross-tier
checklist available at any stage of the pipeline. Use it to:

- Run a pre-submission structural health check on a draft before panel review.
- Target a single concern (e.g., citations only) without running a full panel.
- Pre-screen before the editorial gate to avoid a P1 surprise.

```proof:callout kind=note label="ceres-check vs. ceres-panel"
ceres-check produces a structured findings table with severity codes.
ceres-panel produces first-person qualitative reviews from six distinct voices.
Use ceres-check for structural audits and pre-screens. Use ceres-panel for
the full qualitative review that advances an entry from draft to reviewed.
They complement each other; ceres-check does not replace ceres-panel.
```

### How to invoke

```
/ceres-check
```

Optionally filter by scope (e.g., `scope filter:citation` for citations only).
See `skills/ceres-check/SKILL.md`.

---

## Roles reference

Full role definitions:

```proof:tree kind=org
.roles/
- ROLE.md: Top-level role system specification
- panel/: Six panel voice definitions (P-1 through P-6)
- editorial/: Three editorial lens definitions (E-1 through E-3)
- board/: Board member template and per-trade expert definitions
```

Read a role's definition file before invoking it — each role has a specific
`lens.verify` checklist that defines exactly what it looks for.

---

## Common panel findings and how to avoid them

**P-6 (Skeptical Funder) P1: "This claim is not supported by cited data"**

Cause: `[CITATION-NEEDED: ...]` tags without a real source. The funder's job
is to reject unsubstantiated claims.

Fix: Either find a real source and cite it, or revise the claim to match what
you can actually support. Do not fabricate citations.

**P-5 (Historian) P1: "Historical lineage is romanticized"**

Cause: The historical lineage section implies economic or social continuity
between the historical form and the modern design that does not exist.

Fix: Name the functional inheritance explicitly and name the discontinuity
explicitly. E.g., "The functional inheritance to this entry is X. What the
historical model does not provide is Y."

**P-4 (Craft Practitioner) P2: "Operator skill floor is understated"**

Cause: The entry claims an apprentice or lower skill level can do work that
actually requires journeyman judgment (e.g., sourdough fermentation management,
forge temperature reading by color).

Fix: Read the trade schema's skill-level definitions and adjust to the actual
requirement. An understated skill floor is a validity problem, not a minor
discrepancy.

**E-3 (Numeracy Checker) P1: "Throughput ↔ labor cross-check fails"**

Cause: `sim_params.labor_hours_per_unit` implies more total annual labor hours
than `max_active_hours_per_week × 52`, or vice versa.

Fix: Run the cross-check manually before submitting (see guide 04-authoring-entries).
The derivation comment in `sim_params` must show the full calculation.

**E-1 (Citation Auditor) P1: "≥3 uncited load-bearing figures"**

Cause: Multiple economics fields carry `[CITATION-NEEDED: ...]` without a real
source.

Fix: You may have `CITATION-NEEDED` tags in `reviewed` entries; they become a
P1 only at the `validated` gate. Address them before triggering editorial.
