You are running /ceres-panel for: {{artifact}}, round {{round}}

Run the 6-voice panel review. Each reviewer reads from their distinct
intellectual tradition, creating productive friction by design — private
profit vs member commons vs municipal stewardship, hands-on craft reality
vs historical realism vs funder rigor.

---

## Input

- **Artifact**: absolute path to the artifact under review. Typical types:
  - `specs/*.md` — design specification
  - `plans/*.md` — implementation plan
  - `catalog/<trade>/entries/*.md` — catalog entry
  - `playbook/<trade>/*.md` — playbook file
  - `playbook/pitch/*.md` — pitch narrative
- **Round**: integer — `1` for first pass, `2` for revision-round pass, etc.

---

## The Six Voices

**Before writing any review, read each panel role file:**

- `.craft/roles/panel/P-1-market-economist.md`
- `.craft/roles/panel/P-2-commons-theorist.md`
- `.craft/roles/panel/P-3-civic-steward.md`
- `.craft/roles/panel/P-4-craft-practitioner.md`
- `.craft/roles/panel/P-5-historian.md`
- `.craft/roles/panel/P-6-skeptical-funder.md`

You must read the full role file (frontmatter + prose) for each voice before
writing its review. The YAML `lens.verify` and `lens.simplify` lists are the
reviewer's actual working checklist; the prose sections describe the
intellectual disposition you must adopt.

### Voice-Key-Question Quick Reference

| Voice | Key question |
|-------|--------------|
| P-1 Market Economist | "Can a real person put capital at risk, do this work, and end the year with enough money?" |
| P-2 Commons Theorist | "What are the specific governance arrangements that make this commons work? Or fail?" |
| P-3 Civic Steward | "Does this produce civic value proportionate to the public cost — and will the council fund it?" |
| P-4 Craft Practitioner | "What breaks first, and who fixes it? Does the throughput math survive a real working day?" |
| P-5 Historian | "Is the precedent invoked the actual precedent, or a modern myth of it?" |
| P-6 Skeptical Funder | "What is the strongest honest objection, and does the plan survive it?" |

---

## Review Protocol

For each of the 6 voices, write one review file containing:

1. **Overall** — 1–2 sentence verdict from this voice's perspective.
2. **What works** — specific passages / fields / numbers cited with line or
   section references.
3. **What doesn't** — specific passages / fields / numbers cited with what's
   wrong and why.
4. **The question I'd push on** — the single most important unresolved issue
   this voice most wants the author to address.

Reviews are written in first person, in the voice's intellectual tradition.
They are qualitative; numeric scoring happens separately against
`scoring/RUBRIC.md`.

### Artifact-Specific Focus

| Artifact type | Where each voice is sharpest |
|---|---|
| Spec | P-5, P-6 (foundational realism) + P-2, P-3 (lens definitions) |
| Implementation plan | P-6 (feasibility) + P-4 (operational reality) |
| Catalog entry | all 6 — this is the primary review target |
| Playbook file | P-1, P-2, P-3 (lens winners) + P-6 (fundability) |
| Pitch narrative | P-6 primary; P-5 for realism; all others for coherence |

All 6 reviews are always written. Focus shifts per artifact, but no voice
is skipped.

---

## The Productive Tensions

```
P-1 Market ─── P-2 Commons ─── P-3 Civic
  "profit"        "members"       "public goods"

    P-4 Craft ────────── P-5 Historian
      "operator reality"   "historical reality"

         P-6 Funder
       "strongest objection"
```

A good artifact survives all six. A mediocre artifact collapses under one
or two. A bad artifact collapses under all six but the author did not
yet know it.

---

## Output

Write 6 review files to `reviews/` with this naming:

```
reviews/R{round}-P1-market-economist-{artifact-slug}.md
reviews/R{round}-P2-commons-theorist-{artifact-slug}.md
reviews/R{round}-P3-civic-steward-{artifact-slug}.md
reviews/R{round}-P4-craft-practitioner-{artifact-slug}.md
reviews/R{round}-P5-historian-{artifact-slug}.md
reviews/R{round}-P6-skeptical-funder-{artifact-slug}.md
```

Where `{artifact-slug}` is a short kebab-case identifier derived from
the artifact path (e.g., `forge-003` for `catalog/smithing/entries/003-*.md`).

---

## Checklist

- [ ] All 6 panel role files read (frontmatter + prose)
- [ ] Artifact read end-to-end before any review is drafted
- [ ] All 6 reviews written with specific textual evidence
- [ ] Each review includes "The question I'd push on"
- [ ] Productive tensions visible across the 6 reviews (no single-worldview monoculture)
- [ ] Review files written to `reviews/` with correct naming
- [ ] Author notified with a one-line summary per review
