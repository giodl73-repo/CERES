# P-5 — The Historian — Review of ceres-design (R1)

**Overall:** The anchor-culture selection is genuinely diverse — Song China, Tokugawa Japan, Islamic Golden Age, Andean ayllu, American frontier, not only medieval Europe — and that prevents the Western-nostalgia trap that kills most local-production writing. But Section 2 ("The Core Claim") states the historical premise as established fact rather than as a claim under investigation, and the spec has no pivot plan for what happens if the research corpus reveals that the claim is wrong.

**What works:**
- Section 3 locks 4–6 anchor cultures across regions and eras. The selection includes Song-era Chinese market towns and Andean ayllu — not obvious choices for a Western author, and specifically the kind of non-European case that disciplines Western romanticism about "the village."
- Research-corpus structure (Section 4.2) separates `research/cultures/` from `research/trades/` — preventing the failure mode where a trade's history gets written once and then assumed to be universal.
- Section 5 schema has an `inspirations:` frontmatter field, which gives cross-cultural borrowing a place to be declared rather than hidden.
- Section 11 cites the Reference repo (MAXIM) as primary citation source. The discipline of citing rather than duplicating historical knowledge is correct.

**What doesn't:**
- **Section 2 states the project's thesis as premise, not hypothesis.** "Local artisan production collapsed in industrialized economies not because communities stopped needing what these trades produced, but because the equipment... no longer penciled out." This is a testable claim. The spec treats it as established. A more rigorous framing would hold this as the project's *working hypothesis*, testable against the historical record — and would name a pivot plan if the historical evidence says the story was simpler (e.g., production migrated and specialized rather than vanishing) or more complicated (e.g., many trades collapsed because of regulatory change, not economic unprofitability).
- The spec gives no guidance on **how to handle conflict between anchor cultures**. Song-era forges, Tokugawa forges, and American frontier forges had different fuel regimes, different labor regimes, and different end-uses. When the functional-requirements extraction produces three different answers, which is "the" functional requirement? The spec does not say.
- "Inspirations:" in the schema is ungoverned. A catalog entry that lists `inspirations: [medieval-european-village-forge, edo-blacksmith-cooperative]` should be required to explain which historical *function* is being carried forward, not just which aesthetic. Otherwise the field decorates rather than informs.
- The historical-research scope defers a large romanticism problem to `docs/STYLE-GUIDE.md` (not yet drafted). The guide should name, up front: the forbidden assumption that pre-industrial life was sustainable, the forbidden claim that guilds were primarily about craft quality rather than market protection, the forbidden elision of household labor (which did most of the work in most trades in most cultures).
- The pitch narrative (Section 9) has a section titled "what was lost when local production collapsed." As written, this presumes the collapse happened as the narrative wants it. It should presume a finding, not a story.

**The question I'd push on:**
What is CERES's pivot plan if the historical research reveals that the "local production collapse" narrative in Section 2 is substantially wrong — that production migrated and specialized rather than vanished, or that the decline was driven by factors the equipment-design focus cannot address? The spec must have an answer before it starts, not after.
