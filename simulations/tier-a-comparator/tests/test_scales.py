"""Failing tests for scales.load_scales() (TDD red phase).

References: corpus/program/SCALES.md v1.0 (2026-04-18)
"""
import pytest

from tier_a.scales import load_scales


REQUIRED_SCALE_FIELDS = {
    "median_wage",
    "civic_cost_threshold_per_household",
    "participation_rate",
    "population_midpoint",
    "household_count",
}


class TestLoadScales:

    def test_scales_has_three_scales(self):
        """load_scales() returns a dict with village, town, small_city keys."""
        scales = load_scales()

        assert isinstance(scales, dict)
        assert set(scales.keys()) == {"village", "town", "small_city"}

    def test_each_scale_has_required_fields(self):
        """Each scale dict has all required fields (SCALES.md §2)."""
        scales = load_scales()

        for scale_name, scale_data in scales.items():
            missing = REQUIRED_SCALE_FIELDS - set(scale_data.keys())
            assert not missing, (
                f"Scale '{scale_name}' is missing required fields: {missing}"
            )

    def test_scale_values_match_authoritative_anchors(self):
        """Scale threshold values match SCALES.md v1.0 illustrative anchors."""
        scales = load_scales()

        assert scales["village"]["median_wage"] == 48000
        assert scales["town"]["median_wage"] == 56000
        assert scales["small_city"]["median_wage"] == 62000

        assert scales["village"]["civic_cost_threshold_per_household"] == 120
        assert scales["town"]["civic_cost_threshold_per_household"] == 100
        assert scales["small_city"]["civic_cost_threshold_per_household"] == 80

        assert scales["village"]["participation_rate"] == pytest.approx(0.025)
        assert scales["town"]["participation_rate"] == pytest.approx(0.025)
        assert scales["small_city"]["participation_rate"] == pytest.approx(0.020)
