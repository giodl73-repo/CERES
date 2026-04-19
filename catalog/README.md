# catalog/

Phase 2 artifacts: THE STAR. Equipment-design entries for each trade, each as
a single markdown file with structured YAML frontmatter ingested by simulation
code. 20–40 variants per trade spanning size, capital cost, energy source,
throughput, shareability, and skill floor.

- `<trade>/` — one subdirectory per trade (e.g., `smithing/`, `baking/`, `weaving/`)
- `<trade>/SCHEMA.md` — trade-level extensions to the canonical schema
- `<trade>/entries/` — individual equipment-design files

Canonical schema at `catalog/SCHEMA.md` (Plan A Task 15); trade extensions at
`catalog/<trade>/SCHEMA.md`.

Populated by Plan C (catalog authoring for smithing) and parallel plans for later trades.
