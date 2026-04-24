# Editorial Reviewers

Three cleanup voices that run a **final pass** on CERES artifacts before
they flip from `reviewed` to `validated`. The editorial tier catches
failure modes the panel does not look for because the panel is arguing
substance, not form.

## When Editorial Fires

- Catalog entries about to be promoted from `status: reviewed` → `validated`
- Playbook files before they are referenced by the pitch narrative
- The pitch narrative before external circulation

Editorial does **not** fire on drafts. It is a promotion gate.

## Selection Rule

All three run on every artifact that reaches the promotion stage. They
are automatic — the editorial pass is a checklist with teeth, not a
conversation.

## Review Output Format

```markdown
## E-{N} — {Name} — Pass on {artifact-id}

**Pass / Fail / Hold:** {verdict}

**Findings:**
| Severity | Location | Issue |
|----------|----------|-------|
| P1 | line/field | terse description |
| P2 | ... | ... |

**Gate recommendation:** {block | fix-and-recheck | pass}
```

## Severity

| Level | Definition | Action |
|-------|-----------|--------|
| **P1** | Blocks promotion | Must fix |
| **P2** | Should fix | Author decides; tracked |
| **P3** | Minor / style | Optional |

## Members

- [E-1: The Citation Auditor](E-1-citation-auditor.md) — Every number sourced; no hand-waves
- [E-2: The Scope Keeper](E-2-scope-keeper.md) — Scope drift, feature creep, spec/plan divergence
- [E-3: The Numeracy Checker](E-3-numeracy-checker.md) — Unit economics sanity; math cross-checks
