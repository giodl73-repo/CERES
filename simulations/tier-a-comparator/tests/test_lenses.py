"""Failing tests for Tier A lens functions (TDD red phase).

All tests raise NotImplementedError until Wave 2 implements the lens math.

References:
  - corpus/program/ECONOMIC-LENSES.md  (formulas, pass conditions, verdict margins)
  - corpus/program/SCALES.md           (threshold values)

Worked example cross-check (ECONOMIC-LENSES.md §2.4, §3.4, §4.4):
  Entry: forge-003 mid-scenario at Town Scale
    capital_cost=28000, install_cost=6000, annual_maintenance=1500,
    annual_consumables=4200, floor_space_rent_per_year=4800,
    throughput=2400, downtime=0.12, variable_cost_per_unit=3.1,
    market_price_per_unit.mid=45, lifespan_years=25
  MARKET:  payback≈0.44 yr, operator_take_home≈$75,273 → win
  COOP:    break_even=60, feasible_pool≈213 → win
  CIVIC:   per_hh_cost≈$2.28, usage_rate may vary → win (if usage met)
"""
import copy
import pytest

from tier_a.lenses import market_lens, coop_lens, civic_lens, LensResult


# ---------------------------------------------------------------------------
# MARKET LENS
# ---------------------------------------------------------------------------

class TestMarketLens:

    def test_market_clear_win(self, entry_fixture, scales_fixture):
        """Cheap forge, high throughput, strong wage — payback < 4 yr → verdict='win'.

        Using the canonical worked-example entry (ECONOMIC-LENSES.md §2.4):
          capital=28000, install=6000, price.mid=45, throughput=2400, downtime=0.12
          variable_cost=3.1, op_cost=10500
          => effective_units=2112, gross_margin≈77993, payback≈0.44 yr << 6.4 yr threshold
          => take_home≈75273 >> 56000 (town median)
        Both margins >> 20%, so verdict must be 'win'.
        """
        result = market_lens(entry_fixture, "town", scales_fixture)

        assert isinstance(result, LensResult)
        assert result.verdict == "win"
        assert result.metric_name == "payback_years"
        assert result.primary_metric < 4.0  # well inside win zone

    def test_market_marginal_payback_range(self, entry_fixture, scales_fixture):
        """Payback in 6.4–8.0 yr range → verdict='marginal'.

        We push payback into the marginal zone by reducing price and throughput:
          Lower market_price_per_unit.mid to force payback ≈ 7 yr.
          capital=28000, install=6000, total_invested=34000
          annual_gross_margin ≈ 34000/7 ≈ 4857 to hit payback≈7
          op_cost=10500; variable_cost stays proportionally small
          => set throughput=300, downtime=0, price=25 (effective=300)
          revenue=7500, var_cost=930, gross_margin=7500-930-10500=-3930 (fail)
          -- need to engineer marginal carefully:
          Use price=80, throughput=500, downtime=0, variable=1, op_cost=10500
          effective=500, revenue=40000, var=500, margin=29000
          payback=34000/29000≈1.17 (win) -- too low

        Engineering approach: inflate capital to push payback to ~7 yr.
          Set capital_cost.mid=200000, install=0
          effective=2112, price=45 => margin=77993
          payback = 200000/77993 ≈ 2.56 yr → win (too low)
          Need margin ≈ 200000/7 ≈ 28571
          => use capital=200000, low price = 20
          revenue=2112×20=42240, var=2112×3.1=6547, op=10500
          gross=42240-6547-10500=25193 → payback=200000/25193≈7.94 (fail, too high)
          => price=21: revenue=44352, gross=27305, payback=200000/27305≈7.32 → marginal!
          take_home = 27305 - 200000*0.08 = 27305 - 16000 = 11305 (below median — fail on wage)
          => need high enough take-home to not fail on wage
          Use capital=170000, price=22, throughput=2400, downtime=0.12
          effective=2112, revenue=2112×22=46464, var=6547, op=10500
          gross=46464-6547-10500=29417
          payback=170000/29417≈5.78 yr (win, not marginal — payback < 6.4)
          => capital=175000, price=21
          gross = 2112×21 - 6547 - 10500 = 44352 - 17047 = 27305
          payback = 175000/27305 ≈ 6.41 yr (just at margin boundary)
          take_home = 27305 - 175000×0.08 = 27305 - 14000 = 13305 (below $56k median)
          => wage sub-condition fails → verdict would be 'fail' not 'marginal'

        Correct approach: keep take_home above median, push payback to 6.5–7.5 yr.
          Need: take_home ≥ 56000 AND payback between 6.4 and 8.
          take_home = gross_margin - capital_service ≥ 56000
          payback = (capital+install) / gross_margin ∈ [6.4, 8.0]
          => gross_margin = (capital+install) / payback
          For payback=7: gross_margin = (capital+install)/7
          take_home = gross_margin - (capital+install)×0.08
               = (capital+install)/7 - (capital+install)×0.08
               = (capital+install) × (1/7 - 0.08)
               = (capital+install) × (0.1429 - 0.08)
               = (capital+install) × 0.0629
          Need take_home ≥ 56000 → (capital+install) ≥ 56000/0.0629 ≈ 890,300
          That requires capital ≈ $890k — unrealistic for a forge.

        Alternative: use wage just above median AND payback in marginal zone:
          => set capital=50000, install=0
          => tune price so payback=7 yr
          gross_margin needed = 50000/7 ≈ 7143
          take_home = 7143 - 50000×0.08 = 7143 - 4000 = 3143 (way below $56k)
          → wage always fails at payback=7 given forge-scale economics.

        Per ECONOMIC-LENSES.md §5.2, marginal also triggers when:
          "operator_take_home within 20% below median-wage threshold"
          i.e., take_home ≥ 0.80 × median_wage AND payback ≤ 8.
        So engineer: payback ≤ 8 AND take_home ∈ [0.80×median, median).
          town median = 56000 → target take_home ∈ [44800, 56000)
          take_home = gross - capital_service = gross - (capital+install)×0.08
          Use canonical entry (gross≈77993, capital_service=2720, take_home≈75273)
          To reduce take_home to ~50000, cut price:
          target_gross = 50000 + 2720 = 52720
          actual_gross_at_price_p = 2112×p - 6547 - 10500 = 2112p - 17047
          52720 = 2112p - 17047 → p = (52720+17047)/2112 = 69767/2112 ≈ 33.03
          Use price=33: gross = 2112×33 - 17047 = 69696 - 17047 = 52649
          take_home = 52649 - 2720 = 49929 (within [44800, 56000) → marginal on wage)
          payback = 34000/52649 ≈ 0.65 yr → win on payback
          Combined verdict: marginal (wage sub-condition is marginal)
        """
        entry = copy.deepcopy(entry_fixture)
        # Drop price to push take_home into marginal range [44800, 56000)
        # at town scale (median=56000)
        entry["economics"]["market_price_per_unit"]["mid"] = 33

        result = market_lens(entry, "town", scales_fixture)

        assert result.verdict == "marginal"
        assert result.metric_name == "payback_years"

    def test_market_fail_payback(self, entry_fixture, scales_fixture):
        """Payback > 8 yr → verdict='fail'.

        Set capital very high so payback exceeds 8 years.
        gross_margin with canonical entry ≈ 77993
        payback > 8 → capital+install > 8×77993 = 623944
        Use capital_cost.mid = 650000, install_cost = 0.
        payback = 650000/77993 ≈ 8.33 yr → fail.
        """
        entry = copy.deepcopy(entry_fixture)
        entry["economics"]["capital_cost"]["mid"] = 650000
        entry["economics"]["install_cost"] = 0

        result = market_lens(entry, "town", scales_fixture)

        assert result.verdict == "fail"
        assert result.primary_metric > 8.0

    def test_market_fail_wage(self, entry_fixture, scales_fixture):
        """Operator take-home below scale median wage → verdict='fail'.

        Suppress revenue by cutting price to $5/unit:
          effective=2112, revenue=2112×5=10560, var=6547, op=10500
          gross = 10560-6547-10500 = -6487 (negative → take_home deeply negative)
          payback = 34000 / -6487 → negative (also signals fail)
        Take-home < 0 < median_wage → verdict='fail'.
        """
        entry = copy.deepcopy(entry_fixture)
        entry["economics"]["market_price_per_unit"]["mid"] = 5

        result = market_lens(entry, "town", scales_fixture)

        assert result.verdict == "fail"

    def test_market_uses_mid_price_and_capital(self, entry_fixture, scales_fixture):
        """MARKET lens reads economics.market_price_per_unit.mid and capital_cost.mid."""
        # Sanity check: the canonical entry gives payback ≈ 0.44 yr at town scale
        result = market_lens(entry_fixture, "town", scales_fixture)

        # payback = (28000+6000) / 77993 ≈ 0.436
        assert result.primary_metric == pytest.approx(34000 / 77993, rel=1e-3)


# ---------------------------------------------------------------------------
# COOPERATIVE LENS
# ---------------------------------------------------------------------------

class TestCoopLens:

    def test_coop_clear_win(self, entry_fixture, scales_fixture):
        """Break-even 60 members, feasible pool ≈ 213 → verdict='win'.

        Canonical entry at town scale (ECONOMIC-LENSES.md §3.4):
          annual_capital_charge = 34000/25 = 1360
          annual_op_cost = 10500
          total_annual_cost = 11860
          break_even = ceil(11860/200) = 60
          feasible_pool = 8500 × 0.025 = 212.5 → 213 (or floor 10)
          headroom_ratio = (213-60)/213 ≈ 0.718 ≥ 0.20 → win
        """
        result = coop_lens(entry_fixture, "town", scales_fixture)

        assert isinstance(result, LensResult)
        assert result.verdict == "win"
        assert result.metric_name == "break_even_members"
        assert result.primary_metric == 60  # ceil(11860/200)

    def test_coop_marginal(self, entry_fixture, scales_fixture):
        """Break-even at ≥80% of feasible pool → verdict='marginal'.

        Engineer: break_even / feasible_pool ∈ (0.80, 1.00].
        Town feasible_pool = 8500×0.025 = 212.5, use 212.
        Target break_even ∈ (0.80×212, 212] = (169.6, 212] → use 180.
        break_even = ceil(total_annual_cost / dues) = 180
        total_annual_cost = 180 × 200 = 36000
        total = capital_charge + op_cost → inflate capital so total ≈ 36000.
        op_cost = 10500 → capital_charge ≈ 36000 - 10500 = 25500
        capital_charge = (capital+install)/lifespan → (capital+6000)/25 = 25500
        capital = 25500×25 - 6000 = 637500 - 6000 = 631500
        headroom = (212-180)/212 ≈ 0.151 < 0.20 → marginal.
        """
        entry = copy.deepcopy(entry_fixture)
        entry["economics"]["capital_cost"]["mid"] = 631500

        result = coop_lens(entry, "town", scales_fixture)

        assert result.verdict == "marginal"
        assert result.primary_metric == 180

    def test_coop_fail(self, entry_fixture, scales_fixture):
        """Break-even exceeds feasible pool → verdict='fail'.

        Town feasible_pool ≈ 213.
        Need break_even > 213 → total_annual_cost > 213×200 = 42600.
        op_cost=10500 → capital_charge > 32100 → (capital+6000)/25 > 32100
        → capital > 32100×25 - 6000 = 802500 - 6000 = 796500.
        Use capital=800000.
        capital_charge = (800000+6000)/25 = 806000/25 = 32240
        total = 32240+10500 = 42740
        break_even = ceil(42740/200) = 214 > 213 → fail.
        """
        entry = copy.deepcopy(entry_fixture)
        entry["economics"]["capital_cost"]["mid"] = 800000

        result = coop_lens(entry, "town", scales_fixture)

        assert result.verdict == "fail"
        assert result.primary_metric > 213


# ---------------------------------------------------------------------------
# CIVIC LENS
# ---------------------------------------------------------------------------

class TestCivicLens:

    def test_civic_clear_win(self, entry_fixture, scales_fixture):
        """Per-hh cost ≥ 30% below threshold → verdict='win'.

        Town threshold=$100/hh, household_count=3400.
        Target per_hh_cost ≤ 0.80×100 = $80.
        Canonical entry (civic, ECONOMIC-LENSES.md §4.4):
          annual_capital_charge = 34000/30 ≈ 1133
          annual_op_cost_civic = maintenance+consumables = 1500+4200 = 5700
            (floor_space_rent excluded for civic)
          total_civic_cost = 1133+5700 = 6833
          per_hh_cost = 6833/3400 ≈ $2.01 << $80 threshold
        cost_margin = (100-2.01)/100 ≈ 0.98 >> 0.20 → win (if usage met).
        entry_fixture has annual_public_use_hours=3120 → hrs/capita=3120/8500≈0.367
        Default usage_rate_threshold=2.0 hr/capita → usage fails!
        Need to set usage_rate_threshold low enough to pass, or raise public hours.
        ECONOMIC-LENSES.md §4.3: "specialized equipment may apply a lower threshold".
        For clear_win test: set annual_public_use_hours high enough to pass at threshold=2.
          pop=8500, threshold=2.0 → need hours ≥ 8500×2 = 17000
        """
        entry = copy.deepcopy(entry_fixture)
        entry["sim_params"]["annual_public_use_hours"] = 17000  # ≥ 8500×2 → passes usage

        result = civic_lens(entry, "town", scales_fixture)

        assert isinstance(result, LensResult)
        assert result.verdict == "win"
        assert result.metric_name == "per_household_cost"
        assert result.primary_metric < 80.0  # well below $100 threshold × 0.80

    def test_civic_marginal(self, entry_fixture, scales_fixture):
        """Per-hh cost within 20% of threshold → verdict='marginal'.

        Town threshold=$100. Target cost_margin ∈ [0, 0.20) → per_hh_cost ∈ (80, 100].
        per_hh_cost = total_civic_cost / household_count
        total_civic_cost = (capital+install)/30 + maintenance + consumables
        household_count (town) = 3400
        Target per_hh_cost = 90 → total_civic_cost = 90×3400 = 306000
        total = capital_charge + 5700 = 306000 → capital_charge = 300300
        (capital+6000)/30 = 300300 → capital = 300300×30 - 6000 = 9003000 (unrealistic)

        Alternative: use village scale (threshold=$120) and craft toward per_hh_cost ≈ 105.
        Village: household_count=500, threshold=120, target per_hh ∈ (96, 120].
        Use per_hh_cost=108: total = 108×500 = 54000
        capital_charge = 54000-5700 = 48300 = (capital+6000)/30
        capital = 48300×30 - 6000 = 1449000 - 6000 = 1443000.

        Simpler: use town, inflate capital moderately.
        per_hh = 90 → total = 306000 → too high capital.

        Best approach: use village with moderate capital.
        Village: hh=500, threshold=120.
        per_hh_target = 110 (within 20% of 120: cost_margin=(120-110)/120≈0.083 < 0.20)
        total = 110×500 = 55000
        capital_charge = 55000-5700 = 49300
        (capital+6000)/30 = 49300 → capital = 49300×30-6000 = 1479000-6000 = 1473000.

        Alternative via town: shrink consumables/maintenance drastically.
        Keep capital=28000, install=6000.
        Canonical per_hh_cost≈$2.01 at town/hh=3400. That's well below threshold.
        To get per_hh ≈ $90 at town: need total=306000 → unrealistic.

        Use small_city scale instead: threshold=$80, hh_count=18000.
        per_hh_target=72 → total=72×18000=1296000 → capital_charge=1290300 → unreal.

        The canonical forge entry is so cheap it always wins on CIVIC at any scale.
        For a marginal test, inflate capital enough to push per_hh into (0.80×threshold, threshold].
        Village (threshold=120, hh=500):
          target per_hh = 110 → total = 55000 → capital_charge = 49300
          capital = 49300×30 - 6000 = 1473000 — still high.
        Use small capital with high op_cost? — op_cost fixed by schema fields.
        Use very small amortization period instead (amortization=1 yr, capital=25000):
          capital_charge = (25000+6000)/1 = 31000
          op_cost_civic = 5700
          total = 36700
          per_hh at town/3400 = 36700/3400 ≈ 10.79 → still win
        At village/500: per_hh = 36700/500 = 73.4 → win (73.4 < 96 = 0.80×120)
        Need per_hh ∈ (96, 120] at village.
        Use amortization=1, capital=50000:
          total = 56000/1 + 5700 = 61700; per_hh=61700/500=123.4 → fail (>120)
        Use capital=45000, amort=1:
          total = 51000+5700=56700; per_hh=56700/500=113.4 → marginal! (96<113.4<120)
        And usage must pass: pop=1250, threshold=2.0 → hours ≥ 2500.
        Set annual_public_use_hours=2600 (≥2500), amortization=1, capital=45000, scale=village.
        cost_margin = (120-113.4)/120 = 0.055 < 0.20 → marginal on cost.
        usage passes → verdict marginal. ✓
        """
        entry = copy.deepcopy(entry_fixture)
        entry["economics"]["capital_cost"]["mid"] = 45000
        entry["sim_params"]["amortization_years"] = 1  # aggressive: forces high annual charge
        entry["sim_params"]["annual_public_use_hours"] = 2600  # 2600/1250=2.08 > 2.0 → usage passes

        result = civic_lens(entry, "village", scales_fixture)

        assert result.verdict == "marginal"
        assert result.metric_name == "per_household_cost"
        # 113.4 < 120 (below threshold, so not fail)
        assert result.primary_metric < scales_fixture["village"]["civic_cost_threshold_per_household"]
        # But within 20% of threshold (cost_margin < 0.20)
        threshold = scales_fixture["village"]["civic_cost_threshold_per_household"]
        assert (threshold - result.primary_metric) / threshold < 0.20

    def test_civic_fail_cost(self, entry_fixture, scales_fixture):
        """Per-hh cost exceeds threshold → verdict='fail'.

        Village: threshold=$120, hh=500.
        Use capital=50000, amortization=1 yr:
          total = (50000+6000)/1 + 5700 = 56000+5700=61700; per_hh=61700/500=123.4 > 120 → fail.
        """
        entry = copy.deepcopy(entry_fixture)
        entry["economics"]["capital_cost"]["mid"] = 50000
        entry["sim_params"]["amortization_years"] = 1
        entry["sim_params"]["annual_public_use_hours"] = 3000  # usage would pass

        result = civic_lens(entry, "village", scales_fixture)

        assert result.verdict == "fail"
        assert result.primary_metric > scales_fixture["village"]["civic_cost_threshold_per_household"]

    def test_civic_fail_utilization(self, entry_fixture, scales_fixture):
        """Utilization below threshold → verdict='fail' even if cost passes.

        Town: threshold=$100/hh, hh=3400. Canonical entry cost ≈ $2.01 → passes easily.
        Set annual_public_use_hours=100 → hours/capita=100/8500≈0.012 < 2.0 → fail.
        """
        entry = copy.deepcopy(entry_fixture)
        entry["sim_params"]["annual_public_use_hours"] = 100  # far below 8500×2=17000 needed

        result = civic_lens(entry, "town", scales_fixture)

        assert result.verdict == "fail"
        # Cost still passes (per_hh ≈ $2.01 << $100 threshold)
        assert result.primary_metric < scales_fixture["town"]["civic_cost_threshold_per_household"]


# ---------------------------------------------------------------------------
# SHAPE / TYPE TESTS
# ---------------------------------------------------------------------------

class TestLensResultShape:

    def test_market_returns_lensresult_shape(self, entry_fixture, scales_fixture):
        """market_lens returns a LensResult NamedTuple with required fields."""
        try:
            result = market_lens(entry_fixture, "town", scales_fixture)
        except NotImplementedError:
            pytest.xfail("NotImplementedError raised — red phase expected")

        assert hasattr(result, "verdict")
        assert hasattr(result, "primary_metric")
        assert hasattr(result, "metric_name")
        assert hasattr(result, "notes")
        assert result.verdict in ("win", "marginal", "fail")
        assert isinstance(result.primary_metric, float)
        assert isinstance(result.metric_name, str)

    def test_coop_returns_lensresult_shape(self, entry_fixture, scales_fixture):
        """coop_lens returns a LensResult NamedTuple with required fields."""
        try:
            result = coop_lens(entry_fixture, "town", scales_fixture)
        except NotImplementedError:
            pytest.xfail("NotImplementedError raised — red phase expected")

        assert hasattr(result, "verdict")
        assert result.verdict in ("win", "marginal", "fail")

    def test_civic_returns_lensresult_shape(self, entry_fixture, scales_fixture):
        """civic_lens returns a LensResult NamedTuple with required fields."""
        try:
            result = civic_lens(entry_fixture, "town", scales_fixture)
        except NotImplementedError:
            pytest.xfail("NotImplementedError raised — red phase expected")

        assert hasattr(result, "verdict")
        assert result.verdict in ("win", "marginal", "fail")

    def test_all_lenses_return_lensresult_namedtuple(self, entry_fixture, scales_fixture):
        """All three lens functions raise NotImplementedError (red phase) or return LensResult."""
        for fn in (market_lens, coop_lens, civic_lens):
            try:
                result = fn(entry_fixture, "town", scales_fixture)
                assert isinstance(result, LensResult), (
                    f"{fn.__name__} must return LensResult, got {type(result)}"
                )
            except NotImplementedError:
                pass  # Expected in red phase; test confirms stub signature exists
