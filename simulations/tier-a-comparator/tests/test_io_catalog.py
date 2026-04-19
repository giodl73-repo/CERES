"""Failing tests for catalog I/O functions (TDD red phase — stub for Wave 2).

References:
  - catalog/SCHEMA.md v1.1
  - catalog/smithing/SCHEMA.md
"""
import textwrap
from pathlib import Path

import pytest

from tier_a.io_catalog import read_entry, write_results


# ---------------------------------------------------------------------------
# Minimal sample entry content (subset of SCHEMA.md v1.1 fields)
# ---------------------------------------------------------------------------

SAMPLE_ENTRY_CONTENT = textwrap.dedent("""\
    ---
    id: test-forge-001
    trade: smithing
    name: "Test Forge Entry"
    tagline: "Minimal entry for unit testing"
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
    ---

    ## Overview

    Sample entry for testing io_catalog functions.
    """)


class TestReadEntry:

    def test_read_entry_returns_frontmatter_dict(self, tmp_path):
        """read_entry() parses YAML frontmatter and returns a dict with required keys."""
        entry_file = tmp_path / "test-forge-001.md"
        entry_file.write_text(SAMPLE_ENTRY_CONTENT, encoding="utf-8")

        result = read_entry(entry_file)

        assert isinstance(result, dict)
        assert result["id"] == "test-forge-001"
        assert result["trade"] == "smithing"
        assert "economics" in result
        assert "sim_params" in result
        # Nested access
        assert result["economics"]["capital_cost"]["mid"] == 28000
        assert result["sim_params"]["throughput_units_equiv_per_year"] == 2400

    def test_read_entry_preserves_prose_body(self, tmp_path):
        """read_entry() does not error on entries with prose body after frontmatter."""
        entry_file = tmp_path / "test-forge-001.md"
        entry_file.write_text(SAMPLE_ENTRY_CONTENT, encoding="utf-8")

        # Should not raise; prose body is ignored but must not break parsing
        result = read_entry(entry_file)
        assert result is not None


class TestWriteResults:

    def test_write_results_preserves_other_fields(self, tmp_path):
        """write_results() only modifies the results block; all other fields are unchanged."""
        entry_file = tmp_path / "test-forge-001.md"
        entry_file.write_text(SAMPLE_ENTRY_CONTENT, encoding="utf-8")

        new_results = {
            "village": {
                "market": {"verdict": "win", "payback_years": 0.44},
                "coop": {"verdict": "win", "break_even_members": 60},
                "civic": {"verdict": "win", "per_household_cost": 2.28},
            }
        }

        write_results(entry_file, new_results)

        # Re-read and verify structure
        updated = read_entry(entry_file)
        assert updated["id"] == "test-forge-001"  # identity preserved
        assert updated["trade"] == "smithing"      # trade preserved
        assert updated["economics"]["capital_cost"]["mid"] == 28000  # economics preserved
        assert "results" in updated
        assert updated["results"]["village"]["market"]["verdict"] == "win"

    def test_write_results_roundtrip(self, tmp_path):
        """Writing then reading results produces identical data."""
        entry_file = tmp_path / "test-forge-001.md"
        entry_file.write_text(SAMPLE_ENTRY_CONTENT, encoding="utf-8")

        results_in = {"town": {"market": {"verdict": "marginal", "payback_years": 7.1}}}
        write_results(entry_file, results_in)

        updated = read_entry(entry_file)
        assert updated["results"] == results_in
