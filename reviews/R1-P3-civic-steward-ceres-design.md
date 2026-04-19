# P-3 — The Civic Steward — Review of ceres-design (R1)

**Overall:** The civic lens is properly named and the library / fire-department mental model is invoked correctly. But the spec does not address the two questions that kill civic proposals at town-council meetings: what political coalition funds this, and how does a civic-owned facility interact with existing private operators in the same town. Neither is in the schema. Both are why civic projects fail.

**What works:**
- Section 6 CIVIC lens rule names per-household cost and hours-of-use per capita as the viability metrics. These are the right civic-finance questions.
- Section 3 locks a municipal lifespan of 25–40 years for capital amortization, which is realistic for bond-financed infrastructure.
- The three-scale architecture (Section 3) correctly recognizes that civic viability depends sharply on scale — a village of 1,000 and a small city of 50,000 have radically different civic-budget envelopes.
- Section 12 non-goals refuses policy-advocacy framing. Analytical rigor before narrative. Good discipline.

**What doesn't:**
- The catalog schema (Section 5) has no field for the **political coalition** that would fund a civic entry. Who champions this? What is the council vote count? What is the opposition argument? A civic proposal that cannot name its political path is a research paper, not a program.
- The schema has no field for the **competitive relationship** between a civic facility and existing private operators in the same town. A civic forge in a town that already has a private smith is a policy problem the spec never addresses — it could be (a) redundancy, (b) unfair competition against a private business, or (c) legitimate capacity for a population the private smith does not serve. Three different verdicts, none expressible in the current schema.
- Section 6 CIVIC lens thresholds are deferred to `corpus/program/SCALES.md` without even a draft sketch. What is a defensible per-household cost threshold at village vs town vs small-city scale? Without guidance, each catalog author will invent their own.
- The spec invokes "the library / fire-department model" as rhetorical shorthand but does not commit CERES to a specific civic-form typology. Are all civic entries municipally owned and operated? Or could some be municipally owned, privately operated (concession)? Public-private hybrids? This matters for the political-case analysis.

**The question I'd push on:**
When a catalog entry is marked `civic: good`, where in the spec does the author address two things: (1) the political coalition that would fund this at a council vote, and (2) the relationship to any existing private operator in the same town? Without these, civic-good is a well-intentioned label with no path to implementation.
