# P-4 — The Craft Practitioner — Review of ceres-design (R1)

**Overall:** The schema captures more operator reality than most specs — operator_skill_floor, operators_concurrent, apprentice_friendly, downtime_fraction — which I appreciate. But it misses the two fields that separate a paper design from a working shop: what breaks first, and what a bad week looks like. You cannot plan an artisan business around average conditions; the real question is whether the worst month is survivable.

**What works:**
- `operator_skill_floor` field (Section 5) acknowledges that some designs require a master, not a journeyman. The difference is thousands of dollars a year in wage and years of apprentice pipeline.
- `apprentice_friendly: true/false` is exactly the succession question I would ask. A one-person-only design dies with the operator.
- `downtime_fraction: 0.12` demonstrates awareness that real operation is not continuous. 12% is honest for a working shop; many specs pretend equipment runs 100% of scheduled hours.
- The D-layered simulation structure (Section 7) reserves Tier C (agent-based) for "labor pipeline failures (smith retires, no apprentice)." Someone thought about succession. Good.

**What doesn't:**
- The schema has no **first-year-failures** or **maintenance-schedule** field. What are the first two things to break? At what hours? Who fixes them and at what cost? Every working practitioner has this list in their head for their own equipment; every catalog entry should too.
- No **consumables lead-time** field. A forge that needs a specific flux available only from one Ohio supplier with 6-week lead time is a different business than one that uses commonly-sourced propane. The schema captures consumables cost but not supply risk.
- Throughput is captured as average (`throughput_units_equiv_per_year: 2400`) with no **variance or seasonality** model. Artisan businesses are feast-and-famine. A forge averaging 2,400 units a year might have a February with 80 units and a November with 300. Cashflow, not average revenue, is what kills small shops.
- No **noise / heat / emissions field for operator impact** — only a regulatory-notes field for outside-the-shop compliance. A coal forge is a different job than an induction forge for the person standing in front of it for twenty years. This affects hiring, retention, and who actually applies to apprentice.
- The `operator_skill_floor: journeyman` field is binary-ish (apprentice / journeyman / master) but the spec provides no definition of what those levels mean for a given trade. Will three different authors classify the same design as three different skill floors? Yes, unless the spec says otherwise.

**The question I'd push on:**
Where does a catalog entry describe what an operator's worst month looks like — not the average, the worst — and the first two things that break in year one? Paper designs assume the average case. Real shops die in the tail.
