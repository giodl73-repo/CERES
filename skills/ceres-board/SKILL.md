You are running /ceres-board for: {{artifact}}, claim: "{{claim}}", trade: {{trade}}

Board review is **on-demand**, not routine. It fires when a specific artifact
makes a domain claim that the panel flagged as beyond their expertise, or
when an author proactively requests expert adjudication of a contested
technical or historical claim.

The board is assembled for this claim — not a standing committee.

---

## Input

- **Artifact**: absolute path to the artifact containing the contested claim.
- **Claim**: the specific sentence, field, or number under scrutiny. Must be
  a bounded, checkable claim — not a general theme.
- **Trade**: the trade whose domain expertise is required (smithing, baking,
  weaving, etc.).
- Usually invoked because a panel voice (P-4 or P-5 most often) wrote
  something like: "This claim about induction-forge temperature is beyond
  my expertise — recommend board review."

---

## Board Assembly

Each board is 2–3 domain experts per `.roles/board/ROLE.md`, spanning:

1. **Domain-history specialist** (e.g., historical metallurgy for smithing)
2. **Modern-practitioner specialist** (e.g., working bladesmith, working baker)
3. **Adjacent-engineering specialist** (e.g., combustion / thermal eng, food chemistry, materials science)

### Assembly Procedure

1. Check `.roles/board/` for existing trade-specific role files matching the claim's domain needs.
2. If the needed expert role does not yet exist:
   - **Create it**, using `.roles/board/ROLE.md` as the template.
   - Name the file `B-{trade}-{slug}.md` — e.g., `B-smithing-induction-engineering.md`.
   - Declare `status: active | historical | hypothetical` in frontmatter; explain in `status_note` if not a real named figure.
3. Read each assembled board member's role file before writing their review.

### Board Size

- **Simple factual claim** (e.g., a temperature number): 2 experts suffice.
- **Complex claim** (e.g., a compound historical+engineering argument): 3 experts.
- More than 3 is diminishing returns; one voice usually dominates in the resulting document.

---

## Review Protocol

Each board member writes a **focused** review of just the flagged claim —
not the whole artifact. Format:

```markdown
## B-{trade}-{slug} — {role name} — Claim review

**Claim under review:** {exact quote from artifact}

**Verdict:** supported | partially supported | contested | unsupported

**Evidence:**
- {citation / reasoning}

**Recommended correction (if any):**
{specific text or number the author should adopt}
```

### Verdict Definitions

| Verdict | Meaning | Author action |
|---------|---------|---------------|
| **supported** | Claim is defensible as written | No change needed |
| **partially supported** | Claim is defensible with caveats or bounds | Author should add the caveat |
| **contested** | Experts disagree; claim cannot be stated as certain | Rephrase to acknowledge the contention |
| **unsupported** | Claim is incorrect or has no defensible evidence | Remove or replace |

A **split verdict** across the board (e.g., one supported, one contested) is
itself a finding: the claim as written is stronger than the evidence allows.

---

## Output

Write one review file per board member to `reviews/`:

```
reviews/BOARD-B-{trade}-{slug}-{artifact-slug}.md
```

Also write a **board summary**:

```
reviews/BOARD-SUMMARY-{artifact-slug}-{claim-slug}.md
```

containing: the claim, verdicts from each member, any split verdicts, and
the recommended author action.

---

## Checklist

- [ ] The contested claim is specific and bounded
- [ ] Board assembled with 2–3 domain experts
- [ ] Missing role files created from `.roles/board/ROLE.md` template
- [ ] Each role's `status` declared honestly (active / historical / hypothetical)
- [ ] Each board member's review focuses on the claim, not the artifact
- [ ] Verdicts assigned per member
- [ ] Summary captures any split verdicts
- [ ] Author receives a clear recommendation: supported / modify / remove
