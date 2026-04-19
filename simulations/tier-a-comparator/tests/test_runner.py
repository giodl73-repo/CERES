"""Failing integration tests for the Tier A matrix runner (TDD red phase).

References:
  - corpus/program/ECONOMIC-LENSES.md (9-cell matrix: 3 scales × 3 lenses)
  - corpus/program/SCALES.md
"""
import textwrap
from pathlib import Path

import pytest

from tier_a.runner import run_catalog, run_entry, SCALES, LENSES


# ---------------------------------------------------------------------------
# Minimal sample catalog entry (mirrors test_io_catalog.py fixture)
# ---------------------------------------------------------------------------

SAMPLE_ENTRY_CONTENT = textwrap.dedent("""\
    ---
    id: test-forge-001
    trade: smithing
    name: "Test Forge Entry"
    tagline: "Minimal entry for integration testing"
    status: draft
    economics:
      currency: USD
      capital_cost:
        low: 18000
        mid: 28000
        high: 45000
      install_cost: 6000
      annual_maintenance: 1500
      annual_consumables: 4200
      floor_space_rent_per_year: 4800
      market_price_per_unit:
        low: 32
        mid: 45
        high: 70
      industrial_baseline_price: 12
    sim_params:
      cost_mean: 28000
      cost_sd: 8000
      throughput_units_equiv_per_year: 2400
      variable_cost_per_unit: 3.1
      labor_hours_per_unit: 0.6
      downtime_fraction: 0.12
      lifespan_years: 25
      annual_public_use_hours: 17000
      usage_rate_threshold: 2.0
      amortization_years: 30
      per_member_annual_dues: 200
      per_member_labor_offset: 0
    ---

    ## Overview

    Sample entry for runner integration testing.
    """)


def make_catalog_dir(tmp_path: Path) -> Path:
    """Create a minimal catalog directory with one entry."""
    entries_dir = tmp_path / "entries"
    entries_dir.mkdir()
    entry_file = entries_dir / "001-test-forge.md"
    entry_file.write_text(SAMPLE_ENTRY_CONTENT, encoding="utf-8")
    return tmp_path


class TestRunnerMatrix:

    def test_runner_produces_9_cell_result(self, tmp_path):
        """run_catalog() with 1 entry returns a result dict with all 9 cells filled.

        The 9 cells are: 3 scales (village, town, small_city) × 3 lenses (market, coop, civic).
        """
        catalog_dir = make_catalog_dir(tmp_path)

        all_results = run_catalog(catalog_dir)

        assert isinstance(all_results, dict)
        assert len(all_results) == 1  # one entry

        entry_results = all_results["test-forge-001"]
        assert isinstance(entry_results, dict)
        assert len(entry_results) == 9  # 9 cells

        expected_keys = {
            (scale, lens)
            for scale in SCALES
            for lens in LENSES
        }
        assert set(entry_results.keys()) == expected_keys

    def test_runner_each_cell_is_lensresult(self, tmp_path):
        """Each of the 9 cells is a LensResult with verdict/primary_metric/metric_name."""
        from tier_a.lenses import LensResult

        catalog_dir = make_catalog_dir(tmp_path)
        all_results = run_catalog(catalog_dir)

        for (scale, lens), cell in all_results["test-forge-001"].items():
            assert isinstance(cell, LensResult), (
                f"Cell ({scale}, {lens}) must be LensResult, got {type(cell)}"
            )
            assert cell.verdict in ("win", "marginal", "fail"), (
                f"Cell ({scale}, {lens}) has invalid verdict '{cell.verdict}'"
            )
