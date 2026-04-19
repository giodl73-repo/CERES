You are running /ceres-editorial for: {{artifact}}

> **Role v1.1 fields note.** Each editorial role file now carries three additional frontmatter
> fields: `applies_to` (artifact types the lens reviews — editorial gates fire only at
> promotion time on `catalog-entry`, `playbook-file`, and `pitch-narrative`), `domain_signals`
> (keywords that signal relevance), and `rubric_contribution` (primary scoring dimensions in
> `scoring/RUBRIC.md`). This skill continues to invoke all three lenses unconditionally via
> the hard-coded roster below. However, each lens's `rubric_contribution.primary` field
> declares which dimension it owns — E-1 owns D2 (Citation Strength), E-2 owns D1 (Schema
> Completeness), E-3 owns D3 (Operations Realism) — and findings from these lenses feed
> directly into the scoring instrument when a scorer later applies `scoring/RUBRIC.md`.

Run the 3-lens editorial cleanup pass. Editorial is a **promotion gate** —
it fires on artifacts being promoted from `reviewed` to `validated`, not
on drafts. The three lenses are structural, not substantive: citations,
scope, and numeracy. Editorial does not debate the content; it verifies
the form.

---

## Input

- **Artifact**: absolute path to the artifact up for promotion. Typical types:
  - `catalog/<trade>/entries/*.md` — most common
  - `playbook/<trade>/*.md`
  - `playbook/pitch/*.md`
- The artifact must already have passed panel review (`reviews/R{N}-P*-{slug}.md`
  exist and panel feedback has been addressed).

---

## The Three Lenses

**Before writing any editorial output, read each editorial role file:**

- `.craft/roles/editorial/E-1-citation-auditor.md`
- `.craft/roles/editorial/E-2-scope-keeper.md`
- `.craft/roles/editorial/E-3-numeracy-checker.md`

### Lens Summary

| Lens | Catches | Blocking severity |
|------|---------|-------------------|
| **E-1 Citation Auditor** | Missing sources, unverifiable references, mismatched citations, unit/FX errors | P1 if ≥3 P1-level findings |
| **E-2 Scope Keeper** | Artifact drift, duplication, non-goal violations, schema violations | P1 on non-goal or schema violation |
| **E-3 Numeracy Checker** | Unit-economics cross-check failures, order-of-magnitude errors, internal contradictions | P1 on order-of-magnitude errors or contradictions |

---

## Editorial Protocol

For each lens, produce a findings table:

```markdown
## E-{N} — {Role} — Pass on {artifact-slug}

**Pass / Fail / Hold:** {verdict}

**Findings:**
| Severity | Location | Issue |
|----------|----------|-------|
| P1 | field / line | terse description of the problem |
| P2 | ... | ... |
| P3 | ... | ... |

**Gate recommendation:** {block | fix-and-recheck | pass}
```

### Severity Definitions

| Level | Definition | Action |
|-------|-----------|--------|
| **P1** | Blocks promotion | Author must fix before re-running editorial |
| **P2** | Should fix | Author decides; tracked |
| **P3** | Minor / style | Optional |

### Overall Gate Rule

The artifact is **cleared for promotion** only if all three lenses return
`pass` or `fix-and-recheck-resolved`. Any single `block` verdict holds
the artifact until fixed.

---

## Lens-Specific Procedures

### E-1 Citation Auditor

1. Extract every numeric claim and every historical claim from the artifact.
2. Build a check-table: `claim | source | verified?`
3. For each source: does it exist? Does it support the claim? Is it appropriate?
4. Output findings table.

### E-2 Scope Keeper

1. Identify the artifact's declared scope (header + spec cross-reference).
2. Read against scope. Flag every section or claim outside that scope.
3. For each flag: drift (cut/move) or legitimate expansion (propose spec amendment)?
4. Output findings table.

### E-3 Numeracy Checker

1. Extract all numeric fields (frontmatter + prose).
2. Run standard cross-checks:
   - throughput ↔ labor
   - payback ↔ implied revenue
   - currency normalization
   - order-of-magnitude sanity
   - results-block internal consistency
3. Output findings table with specific numbers involved.

---

## Output

Write 3 editorial files to `reviews/` with this naming:

```
reviews/CLEAN-E1-citation-{artifact-slug}.md
reviews/CLEAN-E2-scope-{artifact-slug}.md
reviews/CLEAN-E3-numeracy-{artifact-slug}.md
```

Also write a **consolidated editorial summary** at:

```
reviews/CLEAN-SUMMARY-{artifact-slug}.md
```

containing: overall pass/block verdict, count of P1/P2/P3 findings per
lens, and a one-paragraph recommendation to the author.

---

## Checklist

- [ ] All 3 editorial role files read
- [ ] Panel review already complete and addressed
- [ ] Artifact read end-to-end before any finding is drafted
- [ ] Each lens produces its own findings table
- [ ] Severity assigned per finding
- [ ] Consolidated summary written
- [ ] Overall gate verdict (clear / block) is explicit
