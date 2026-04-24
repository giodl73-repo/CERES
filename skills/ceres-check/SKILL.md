You are running /ceres-check for: {{artifact}}, scope: {{scope | "full"}}

`ceres-check` is a **fast, filtered audit** skill — a checker/summarizer, not a
persona-voice reviewer. It dynamically selects applicable roles from the role
library based on artifact type and content signals, then evaluates each role's
`lens.verify` checklist against the artifact, producing a structured findings
table with severity codes.

This skill **complements** `ceres-panel`. Panel does deep qualitative first-
person reviews. `ceres-check` is the fast pre-promotion audit or targeted-concern
scan. Both coexist; neither replaces the other.

---

## Input

- **Artifact**: absolute path to any CERES artifact. Typical types:
  - `specs/*.md` — design specification
  - `plans/*.md` — implementation plan
  - `catalog/<trade>/entries/*.md` — catalog entry
  - `playbook/<trade>/*.md` — playbook file
  - `playbook/pitch/*.md` — pitch narrative
- **Scope** (optional, default `full`):
  - `full` — all roles that apply to this artifact type
  - `filter:<signal>` — further restrict to roles whose `domain_signals` includes
    the given substring (e.g., `filter:historical` fires only roles with
    "historical" in `domain_signals`)
  - `tier:<panel|editorial|board>` — restrict to a single review tier

---

## Step 1 — Role Discovery

### 1a. Enumerate the role library

Glob `.roles/**/*.md` to list every file in the role library.

**Exclude any file named `ROLE.md`** — those are tier overview/template files,
not individual reviewer roles. Only files with individual role IDs (e.g.,
`P-1-market-economist.md`, `E-2-scope-keeper.md`) are candidates.

After globbing you should have up to 9 individual role files (6 panel + 3
editorial + any board members present):

```
.roles/panel/P-1-market-economist.md
.roles/panel/P-2-commons-theorist.md
.roles/panel/P-3-civic-steward.md
.roles/panel/P-4-craft-practitioner.md
.roles/panel/P-5-historian.md
.roles/panel/P-6-skeptical-funder.md
.roles/editorial/E-1-citation-auditor.md
.roles/editorial/E-2-scope-keeper.md
.roles/editorial/E-3-numeracy-checker.md
.roles/board/B-*.md           (zero or more, assembled on demand)
```

### 1b. Read frontmatter from each role

For each candidate role file, extract from YAML frontmatter:

| Field | Used for |
|-------|----------|
| `name` | Display name |
| `role` | Tier (`panel`, `editorial`, `board`) |
| `applies_to` | Artifact-type filter |
| `domain_signals` | Signal-keyword filter + relevance scoring |
| `rubric_contribution` | Dimension aggregate section |
| `lens.verify` | Per-item checklist evaluation |
| `lens.simplify` | Editing directives (referenced in findings but not executed) |

### 1c. Derive artifact type from path

Map the artifact's path to one of the allowed `applies_to` values:

| Path pattern | Artifact type |
|---|---|
| `specs/*.md` | `spec` |
| `plans/*.md` | `plan` |
| `catalog/*/entries/*.md` | `catalog-entry` |
| `playbook/<trade>/*.md` (not pitch) | `playbook-file` |
| `playbook/pitch/*.md` | `pitch-narrative` |

If the path does not match a known pattern, default to `catalog-entry` and
note the ambiguity in the output header.

### 1d. Filter by artifact type

Exclude any role where `applies_to` does not include the derived artifact type.

### 1e. Apply scope filter

- `full` (default): no additional filtering.
- `filter:<signal>`: keep only roles where at least one element of
  `domain_signals` contains the given substring (case-insensitive).
- `tier:<x>`: keep only roles where `role == x`.

### 1f. Score relevance

For each surviving role, compute:

```
relevance_score = 1                          # base: passed all filters
                + count(domain_signal in artifact_content)
                                             # +1 per signal keyword found
                                             # (case-insensitive substring match)
```

Read the artifact's full content before scoring. Count each distinct signal
keyword that appears at least once — do not double-count repeated occurrences
of the same keyword.

Record: `role_id`, `display_name`, `tier`, `relevance_score`,
`triggering_signals` (the matched keywords).

---

## Step 2 — Selection Plan

Before running any checks, print the selection plan so the reader sees what
is being audited.

```markdown
## Selection Plan

| Role | Tier | Relevance | Triggering signals |
|------|------|-----------|-------------------|
| P-1 Market Economist | panel | 4 | market, payback, ROI, wage |
| P-4 Craft Practitioner | panel | 3 | operator, throughput, consumables |
| E-1 Citation Auditor | editorial | 2 | source, citation |
| ... | ... | ... | ... |
```

Roles excluded by filtering are not listed here. Include a note below the
table: `{N} roles excluded (not applicable to this artifact type or scope).`

---

## Step 3 — Per-Role Checklist Evaluation

For each selected role (in descending relevance order), read the role file's
`lens.verify` list and `lens.simplify` list fully. Then evaluate each
`verify` item against the artifact.

### Verdict codes

| Code | Meaning |
|------|---------|
| **PASS** | Condition is met |
| **FAIL** | Condition is not met — assign P1/P2/P3 severity |
| **N/A** | Condition does not apply (e.g., checks a field absent from this artifact type) |

### Severity assignment for FAIL

| Level | Definition | Examples |
|-------|-----------|---------|
| **P1** | Blocks promotion — must fix | Missing required field; uncited load-bearing number; order-of-magnitude error; schema violation |
| **P2** | Should fix — tracked | Weak citation; minor inconsistency; unclear wording; unverified range presented as point estimate |
| **P3** | Nice to have — optional | Style; minor precision overclaim; formatting |

If a `verify` item does not obviously map to a severity level, assign **P2**
and add `(ambiguous severity)` in the issue description.

### Finding record format

Every FAIL produces one finding row:

| Field | Content |
|-------|---------|
| `#` | Sequential finding number across all roles |
| `Role` | Role ID (e.g., `P-1`) |
| `Severity` | P1 / P2 / P3 |
| `Location` | `field:<name>`, `line:<N>`, `section:<heading>`, or `prose` |
| `Issue` | One sentence — what condition failed and why |
| `Suggested fix` | Concrete, specific remediation |

PASS and N/A items are not listed in the Findings table (they are audited but
not reported unless the output summary notes the count).

---

## Step 4 — Dimension Aggregate

Using `rubric_contribution` from each **selected** role's frontmatter, build
the dimension aggregate table.

```markdown
## Dimension Aggregate

| Dimension | Primary contributors (1.0x) | Secondary (0.5x) | Rough score estimate |
|-----------|----------------------------|------------------|---------------------|
| D1 Schema Completeness | E-2 | — | {pass count}/{total verify items for this dim} |
| D2 Citation Strength   | E-1 | P-1, P-5 | ... |
| D3 Operations Realism  | E-3 | P-4 | ... |
| D4 Lens-Context Rigor                 | P-1, P-2, P-3 | E-3 | ... |
| D5 Historical Honesty                 | P-5 | P-6 | ... |
| D6 Design Rationale and Differentiation | P-6 | P-1, P-2, P-3, P-4 | ... |
```

Only include dimensions where at least one selected role contributes.

Rough score estimate = count of PASS findings for roles contributing to that
dimension ÷ total verify items evaluated by those roles. This is a heuristic
only — use `scoring/RUBRIC.md` for formal scoring.

Note below the table: `Dimension scores are rough (findings-count based). Use
scoring/RUBRIC.md for formal scoring.`

---

## Step 5 — Summary and Verdict

```markdown
## Summary

- {count} P1 findings — blocks promotion to `validated`
- {count} P2 findings — should fix
- {count} P3 findings — optional
- {count} N/A items (not applicable to this artifact type)
- {count} PASS items

**Verdict:** PASS | HOLD | BLOCK

**Verdict logic:**
- PASS = zero P1 findings
- HOLD = 1–3 P1 findings
- BLOCK = 4+ P1 findings or critical structural failure (missing required
  schema block, artifact type cannot be determined)
```

---

## Output

Write a **single markdown file** to:

```
reviews/CHECK-{artifact-slug}.md
```

Where `{artifact-slug}` is a short kebab-case identifier derived from the
artifact path (e.g., `forge-003` for `catalog/smithing/entries/003-*.md`,
`specs-local-prod` for `specs/local-production-spec.md`).

The file must have this exact structure:

```markdown
# ceres-check — {artifact-name}

**Artifact:** {absolute path}
**Scope:** {full | filter:X | tier:X}
**Roles selected:** {count} of {total individual roles in library}
**Run date:** {YYYY-MM-DD}

## Selection Plan

| Role | Tier | Relevance | Triggering signals |
|------|------|-----------|-------------------|
| ... | ... | ... | ... |

{N} roles excluded (not applicable to this artifact type or scope).

## Findings

| # | Role | Severity | Location | Issue | Suggested fix |
|---|------|----------|----------|-------|---------------|
| 1 | P-1 | P1 | field:economics.market_price_per_unit | Missing; market lens claimed | Add market_price_per_unit to frontmatter |
| 2 | E-3 | P2 | sim_params | throughput × labor_hours exceeds max_active_hours | Reconcile per METHODOLOGY §3.1 |
| ... |

## Dimension Aggregate

Using `rubric_contribution` from each selected role's frontmatter:

| Dimension | Primary contributors (1.0x) | Secondary (0.5x) | Rough score estimate |
|-----------|----------------------------|------------------|---------------------|
| ... | ... | ... | ... |

Dimension scores are rough (findings-count based). Use `scoring/RUBRIC.md`
for formal scoring.

## Summary

- {count} P1 findings — blocks promotion to `validated`
- {count} P2 findings — should fix
- {count} P3 findings — optional
- {count} N/A items (not applicable to this artifact)
- {count} PASS items

**Verdict:** PASS | HOLD | BLOCK
```

---

## When to Use ceres-check vs. ceres-panel

| Situation | Use |
|-----------|-----|
| First-pass draft review, qualitative debate wanted | `ceres-panel` |
| Pre-promotion fast audit, structured findings needed | `ceres-check` |
| Only one signal matters (e.g., citations) | `ceres-check --scope filter:citation` |
| Only editorial lenses needed | `ceres-check --scope tier:editorial` |
| Full qualitative + structured audit | both, in sequence |

`ceres-panel` always fires all 6 voices. `ceres-check` fires only the roles
whose applicability and signal match the artifact — and reports findings as a
table, not as first-person qualitative reviews.

---

## Checklist

- [ ] Glob `.roles/**/*.md` executed; `ROLE.md` files excluded
- [ ] Frontmatter read from every individual role file
- [ ] Artifact type derived from path; noted if ambiguous
- [ ] Filters applied in order: artifact type → scope → (relevance scored)
- [ ] Selection plan printed before any finding is evaluated
- [ ] Artifact read end-to-end before any `verify` item is evaluated
- [ ] Every `verify` item evaluated: PASS / FAIL / N/A
- [ ] Every FAIL has: role id, severity (P1/P2/P3), location, issue, suggested fix
- [ ] Ambiguous severity items marked `(ambiguous severity)` with P2 default
- [ ] Dimension aggregate uses `rubric_contribution.primary` (1.0x) and `.secondary` (0.5x)
- [ ] Rough score estimates noted as rough; `scoring/RUBRIC.md` referenced for formal scoring
- [ ] Verdict logic applied: PASS / HOLD / BLOCK per P1 count
- [ ] Output written to `reviews/CHECK-{artifact-slug}.md`
- [ ] No persona-voice first-person prose — this is a checker, not a panel reviewer
