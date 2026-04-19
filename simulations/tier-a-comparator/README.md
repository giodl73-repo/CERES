# Tier A Comparator

Deterministic scenario comparator for CERES catalog entries. Evaluates every
entry against all 9 cells (3 scales × 3 economic lenses) using closed-form math
defined in `corpus/program/ECONOMIC-LENSES.md`.

**Status:** Plan D Wave 1 — scaffolding + failing tests (TDD red phase).
Lens math implemented in Wave 2.

---

## Project layout

```
simulations/tier-a-comparator/
├── pyproject.toml          # Project metadata + deps
├── src/
│   └── tier_a/
│       ├── __init__.py     # Version string
│       ├── lenses.py       # MARKET / COOP / CIVIC lens functions
│       ├── scales.py       # Scale parameter loader (SCALES.md)
│       ├── io_catalog.py   # Catalog entry YAML read/write
│       ├── runner.py       # 9-cell matrix runner
│       └── cli.py          # Command-line interface
├── tests/
│   ├── conftest.py         # Fixtures: scales_fixture, entry_fixture
│   ├── test_lenses.py      # 12 lens tests
│   ├── test_scales.py      # 3 scale tests
│   ├── test_io_catalog.py  # 4 catalog I/O tests
│   └── test_runner.py      # 2 integration tests
└── results/                # Output files (git-ignored except .gitkeep)
```

---

## Running the tests

All deps (pyyaml, pytest) are installed globally; no venv required.

```bash
cd simulations/tier-a-comparator
python -m pytest
```

During the red phase (Wave 1), every test should **fail** with
`NotImplementedError`. That is the expected state.

To see verbose output:

```bash
python -m pytest -v
```

---

## Running the full matrix (Wave 2+)

Once lens math is implemented:

```bash
cd simulations/tier-a-comparator
python -m tier_a.cli --catalog ../../catalog/smithing/ --results-dir ./results
```

Options:

| Flag | Default | Description |
|---|---|---|
| `--catalog PATH` | (required) | Catalog trade directory (e.g. `../../catalog/smithing/`) |
| `--results-dir PATH` | `./results` | Output directory for result files |
| `--scales PATH` | built-in | Optional YAML override for scale parameters |
| `--dry-run` | off | Parse + validate only; do not write results |
| `--verbose` | off | Print per-cell verdicts to stdout |

---

## Lens rules summary

| Lens | Primary metric | Pass condition | Verdict: win | Verdict: marginal |
|---|---|---|---|---|
| MARKET | payback_years | payback ≤ 8 yr AND take-home ≥ median_wage | payback margin ≥ 20% | payback margin < 20% OR wage within 20% |
| COOPERATIVE | break_even_members | break_even ≤ feasible_pool | headroom ≥ 20% of pool | headroom < 20% of pool |
| CIVIC | per_household_cost | cost ≤ threshold AND usage_rate ≥ threshold | cost margin ≥ 20% | cost margin < 20% |

Full formula definitions: `corpus/program/ECONOMIC-LENSES.md`
Scale threshold values: `corpus/program/SCALES.md`
