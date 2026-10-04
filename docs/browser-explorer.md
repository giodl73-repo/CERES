# Draft production sensitivity workbench

`ceres-web` embeds exactly two existing draft smithing catalog frontmatters and
calls the native market, co-op, and civic lenses. It changes only the settlement
scale, participation rate, and median wage. Catalog equations and entries stay
unchanged. Draft status and citation gaps remain visible; this is not catalog
promotion, an equipment design, or a procurement plan.

The scale retains its native population, household counts, civic threshold,
and co-op membership floor. Participation is 0.1–20%; wage is $10,000–200,000.
Default controls select town/2.5%/$56,000. Wage affects market categories;
participation affects co-op feasibility; civic results follow settlement scale.
Native negative payback sentinel displays as Not recoverable. Favorable
categories describe only threshold outcomes and do not validate feasibility.

Calculations run in a worker; URLs share bounded assumptions; downloadable JSON
includes inputs and results. RALLY's retired master dependency is replaced with
an explicit current main revision, and RLINE is pinned for reproducible builds.
CI validates native tests, scoped adapter clippy/fmt, actual-WASM browser checks,
release artifacts and a 5 MB bundle budget before main Pages deployment.

The distribution includes LICENSE: software is MIT, catalog/research content
is CC BY-NC 4.0. Embedded catalog data retains that content license; the adapter
crate license does not relicense the included designs.
