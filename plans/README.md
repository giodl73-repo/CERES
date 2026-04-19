# Plans Directory

## 1. Purpose

This directory holds implementation plans for **CERES** (the Local Production Atlas).
Each plan covers one subsystem of the CERES pipeline and is self-contained: it states
what files it creates, what order to build them in, and what "done" looks like.

Plans are sequenced but not serial. Plan A produces the trade-agnostic framework that
every downstream plan depends on. Plans B-E can proceed in parallel once Plan A
completes, subject to the dependency graph encoded in each plan's `depends_on:` and
`blocks:` frontmatter fields.

One plan per subsystem. Do not scatter a subsystem's work across multiple plans; if a
subsystem grows, extend its plan and bump `version:`.

### Why plans carry YAML frontmatter

Plain prose plans are hard to query: you cannot filter by status, phase, or trade
without reading every file. Structured frontmatter makes the plan set machine-readable.
A script (or an agent) can answer "which plans are `in_progress`?" or "what does
plan-d-sim block?" by parsing frontmatter alone, without touching plan bodies. The
index table in §3 is a human-readable projection of that same structured data; it is
derived from the frontmatter, not the source of truth. When the two disagree, the
frontmatter on the individual plan file wins.

---

## 2. Plan Frontmatter Convention

Every file under `plans/` that is a plan document (not this README) **must** open with
YAML frontmatter in exactly this schema:

```yaml
---
id: plan-{letter}-{slug}         # e.g. plan-a-scaffolding, plan-b-research-smithing
name: {human-readable title}
description: {one-line summary}
status: draft | in_progress | completed | deferred | superseded
version: "X.Y"
created: YYYY-MM-DD
phase: 0 | 1 | 2 | 3 | 4 | 5     # 0 = infra; 1-5 = CERES pipeline phases
subsystem: scaffolding | research-corpus | catalog | simulation | playbook
trade: null | smithing | baking | ...
depends_on: [plan-id, ...]
blocks: [plan-id, ...]
estimated_effort: "{duration}"
primary_artifact_type: framework-docs | research | catalog | code | playbook
success_signal: >
  {one or two sentences describing the completion condition}
spec: {path to the authoring spec that governs this plan}
---
```

### Field glossary

| Field | Required | Notes |
|---|---|---|
| `id` | yes | kebab-case; must match the filename slug after the date prefix |
| `name` | yes | Title-cased human label shown in the index table |
| `description` | yes | One-line; fits in a table cell |
| `status` | yes | See §5 Status flow below |
| `version` | yes | Quoted string; bump minor on task additions, major on scope change |
| `created` | yes | ISO-8601 date the plan file was first committed |
| `phase` | yes | Integer 0–5 matching the CERES pipeline phase (0 = infrastructure) |
| `subsystem` | yes | One of the five canonical subsystem slugs |
| `trade` | yes | `null` for cross-trade plans; trade slug (e.g. `smithing`) for trade-specific |
| `depends_on` | yes | YAML list of `id` values; empty list `[]` if none |
| `blocks` | yes | YAML list of plan `id` values this plan must finish before they start |
| `estimated_effort` | yes | Free-text duration estimate (e.g. `"1-2 weeks focused"`) |
| `primary_artifact_type` | yes | Describes the dominant output kind |
| `success_signal` | yes | Block scalar; one or two sentences; used as acceptance criterion |
| `spec` | yes | Repo-relative path to the spec section that governs this plan |

### Canonical subsystem slugs

| Slug | Covers |
|---|---|
| `scaffolding` | Framework docs, conventions, schema, glossary, rubric |
| `research-corpus` | Primary and secondary source research for a trade |
| `catalog` | Catalog entries (YAML + prose) for a trade |
| `simulation` | Simulation tiers A / B / C and evaluation matrix |
| `playbook` | Per-trade playbook files and the project pitch narrative |

### Canonical phase numbers

| Phase | Pipeline stage |
|---|---|
| 0 | Infrastructure (cross-trade framework) |
| 1 | Functional requirements and research corpus |
| 2 | Catalog population |
| 3 | Economic lens formalization and Tier A simulation |
| 4 | System-dynamics and agent-based simulation |
| 5 | Playbook and pitch narrative |

---

## 3. Current Plan Index

Plans marked `not-yet-authored` are planned but not yet written. Their row data
describes intent derived from Plan A's blocking relationship and the project spec;
actual frontmatter will be the authoritative record once those files exist.

| id | name | status | phase | trade | depends_on | success_signal |
|---|---|---|---|---|---|---|
| plan-a-scaffolding | Scaffolding and Framework Docs | draft | 0 | null | _(none)_ | All trade-agnostic framework files exist with cited content and no TODO/TBD placeholders. A reader unfamiliar with CERES can open the repo and understand what the project is, how it works, and where every artifact type lives. |
| plan-b-research-smithing | Research Corpus — Smithing | completed | 1 | smithing | plan-a-scaffolding | 4 cultural chapters (medieval N. Europe, Song China, Tokugawa Japan, American frontier) + cross-cultural REQUIREMENTS, HISTORICAL-FORMS, DECLINE-VERDICT, SOURCES — anti-romantic, P-5-Historian-grade citations, feeds Plan C. |
| plan-c-catalog-smithing | Catalog — Smithing | completed | 2 | smithing | plan-a-scaffolding, plan-b-research-smithing | 15 forge catalog entries spanning repair/specialty/shared-civic niches per DECLINE-VERDICT; every entry schema-compliant per catalog/SCHEMA.md v1.1; actual niche split 8/3/2/2 (drifted from target 6/3/4/2; accepted honestly); cross-entry audit confirms 9-cell matrix coverage; ready for ceres-panel R1 and Plan D Tier A sim. |
| plan-d-sim | Simulation and Evaluation Matrix | draft | 3 | null | plan-a-scaffolding, plan-c-catalog-smithing | Tier A comparator (Python 3.12 + pytest + PyYAML) runs all 135 evaluation cells (15 entries × 9 contexts); `results:` blocks populated in each catalog entry; SUMMARY.md aggregates findings; Tier B and C directories scaffolded with intent READMEs. |
| plan-e-playbook | Playbook and Pitch Narrative | not-yet-authored | 5 | smithing | plan-d-sim | Three per-scale smithing playbook files are written and the pitch narrative first draft exists, citing catalog and simulation evidence. |

---

## 4. How to Add a New Plan

### File naming

```
plans/YYYY-MM-DD-plan-{letter}-{slug}.md
```

- `YYYY-MM-DD` — the ISO-8601 date the plan file is created (not the start of work).
- `{letter}` — next sequential letter (a, b, c, …). Use lowercase.
- `{slug}` — kebab-case slug matching the `id` field, without the `plan-{letter}-` prefix.

Example: `plans/2026-05-01-plan-f-catalog-baking.md` with `id: plan-f-catalog-baking`.

### Steps

1. Create the file with full frontmatter as specified in §2.
2. Set `status: draft`.
3. Populate every required field; leave no field blank or with a placeholder value.
4. Update every plan whose `id` appears in your new plan's `depends_on:` list: add your
   new plan's `id` to that upstream plan's `blocks:` array and commit the upstream
   plan file.
5. Add a row to the index table in §3 of this file.
6. Commit the new plan file and this README in the same commit, or in adjacent commits
   with a clear message linking them.

### Naming the success signal

The `success_signal` field is an acceptance criterion, not a progress note. Write it so
a reviewer who has never spoken to the plan author can answer "pass or fail?" by
inspecting the repo. Good form: "All X catalog entries exist with field Y populated and
status Z." Bad form: "Smithing research is mostly done." If the criterion requires
judgment, name the reviewer role that exercises the judgment (e.g., "passes panel
review").

### Checklist before merging a new plan

- [ ] `id` matches the filename slug.
- [ ] `depends_on` lists are accurate and reciprocal (`blocks:` on upstream plans
      updated).
- [ ] `success_signal` is testable: a reviewer can determine pass/fail without asking
      the plan author.
- [ ] `spec` points at a real file path in the repo.
- [ ] Index table row added to this README.

---

## 5. Status Flow

```
draft → in_progress → completed
```

| Status | Meaning |
|---|---|
| `draft` | Plan is authored but work has not started |
| `in_progress` | Active implementation underway |
| `completed` | All tasks done; success signal met; `TRACKER.md` updated |
| `deferred` | Accepted plan, work not currently scheduled; body should explain why and when it may resume |
| `superseded` | Replaced by another plan; body must link the replacement plan |

**Transition rules:**

- Move `draft → in_progress` when the first task commit lands.
- Move `in_progress → completed` only after the success signal is verifiably met
  (not just "tasks checked off").
- `deferred` and `superseded` are dead-end states for the current plan document. A
  superseded plan is never deleted — it stays in the directory as a record, with its
  frontmatter updated and a note in the body identifying the replacement.
- A plan cannot move to `completed` while any of its `blocks:` dependents are
  `in_progress` — check that the dependency is still accurate first.

---

## 6. Relationship to `TRACKER.md`

These two files operate at different granularities and serve different audiences:

| | `plans/README.md` | `TRACKER.md` |
|---|---|---|
| **Granularity** | Plan-level (one row per plan) | Artifact-level (one row per file or deliverable) |
| **Status tracked** | Plan lifecycle (`draft → completed`) | Individual artifact progress |
| **Audience** | Plan authors deciding what to work on next | Day-to-day workers checking which specific file is done |
| **Updated when** | A plan changes status | A task within any plan is completed |
| **Machine-readable** | Yes — frontmatter on each plan file | Yes — table rows with status columns |

The two files must remain consistent: when a plan reaches `completed`, all its
constituent artifacts should be `completed` in `TRACKER.md` as well. If they diverge,
`TRACKER.md` is finer-grained and more likely to be current — reconcile by updating
the plan status, not by downgrading `TRACKER.md`.

When evaluating overall project health, read both: the plan index shows whether whole
subsystems are unblocked and ready; `TRACKER.md` shows whether the individual building
blocks within those subsystems are in place.
