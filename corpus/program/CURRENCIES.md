---
title: CERES Currency Reference
version: "1.0"
created: 2026-04-18
spec: specs/2026-04-18-ceres-design.md
companion_methodology: docs/METHODOLOGY.md#4-multi-currency-normalization
companion_style: docs/STYLE-GUIDE.md#5-multi-currency-conventions
---

# CERES Currency Reference

This document is the **single FX reference** for the CERES project. It defines:

1. The project base currency for simulation normalization.
2. The FX snapshot table (exchange rates from each catalog currency to USD).
3. The update cadence and snapshot-history log.
4. The normalization rule used by Tier A simulation.
5. The methodology for bringing historical cost data forward via CPI + FX.

**Division of labor:**

- This document — the FX table, snapshot methodology, normalization rule, and CPI
  methodology for historical conversions.
- `docs/METHODOLOGY.md` Section 4 — the *process* for using this table during
  evaluation (evaluation normalization steps, when snapshot dates must be cited,
  how historical monetary units are handled in prose).
- `docs/STYLE-GUIDE.md` Section 5 — *writing rules* for currency in catalog entries
  (declaration field, no inline conversions in prose, cross-currency comparison only
  in simulation output).

Do not duplicate those sections here; do not replicate CURRENCIES.md content there.

---

## 1. Base Currency

**Project base currency: USD (United States Dollar)**

All simulation normalization targets USD. This choice is made once and held constant
for the life of the project. The rationale:

- The project scales (`corpus/program/SCALES.md`) are defined at US-settlement sizes,
  and the worked examples in the spec (Section 5) use USD.
- Most labor-cost benchmarks and equipment surveys cited in the vertical slice
  (smithing) are USD-denominated.
- US CPI-U (BLS) is available as a continuous, authoritative, freely accessible
  series, which is required for the historical-cost methodology in Section 5 below.

Changing the base currency is a breaking change: all simulation output citing a
specific snapshot would need to be re-evaluated. Any proposal to change the base
currency requires a new version of this document and explicit acknowledgment in the
simulation run metadata.

---

## 2. FX Snapshot Table

> **Illustrative snapshot** — values below approximate recent market rates and are
> placeholders for methodology demonstration. They **must** be refreshed from a named
> authoritative source (ECB reference rates, Federal Reserve H.10, IMF IFS, or OECD
> exchange-rate series) before any simulation run that depends on cross-currency
> comparison. The source and exact snapshot date must be recorded in the simulation
> run's output metadata (see `docs/METHODOLOGY.md` Section 4.3).

**Snapshot date:** 2026-04-18
**Source:** European Central Bank (ECB) reference rates (https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/); USD/non-EUR rates derived via ECB EUR pivot where ECB does not publish directly. Federal Reserve H.10 release (https://www.federalreserve.gov/releases/H10/) used as cross-check for USD bilateral pairs.

| Currency | Code | USD per 1 unit | Snapshot date | Source |
|---|---|---:|---|---|
| US Dollar | USD | 1.0000 | 2026-04-18 | Definition (base) |
| Euro | EUR | 1.0850 | 2026-04-18 | ECB reference rate |
| Pound sterling | GBP | 1.2700 | 2026-04-18 | ECB reference rate |
| Japanese yen | JPY | 0.00665 | 2026-04-18 | ECB reference rate |
| Canadian dollar | CAD | 0.7350 | 2026-04-18 | Federal Reserve H.10 |
| Australian dollar | AUD | 0.6420 | 2026-04-18 | Federal Reserve H.10 |
| Swiss franc | CHF | 1.1250 | 2026-04-18 | ECB reference rate |
| Chinese yuan (renminbi) | CNY | 0.1380 | 2026-04-18 | Federal Reserve H.10 |
| Indian rupee | INR | 0.01195 | 2026-04-18 | Federal Reserve H.10 |
| Mexican peso | MXN | 0.05070 | 2026-04-18 | Federal Reserve H.10 |
| Brazilian real | BRL | 0.1790 | 2026-04-18 | Federal Reserve H.10 |
| South African rand | ZAR | 0.05500 | 2026-04-18 | Federal Reserve H.10 |

**Notes on the table:**

- USD = 1.0000 by definition; no conversion is needed for USD-denominated entries.
- JPY, INR, MXN, BRL, and ZAR are all less than 0.25 USD per unit — small-denomination
  currencies where 1 unit buys a fraction of a US cent (JPY, INR) or a few cents.
  When reading the table, verify the decimal placement: e.g., 1 JPY ≈ 0.00665 USD,
  so 10,000 JPY ≈ $66.50 USD.
- CNY is the official ISO 4217 code (also referred to as CNH in offshore markets);
  CERES uses CNY throughout.
- These rates are mid-market (not buy/sell spread); they are appropriate for
  order-of-magnitude cost normalization, not for actual currency transactions.

---

## 3. Update Cadence

### When rates are refreshed

Rates are updated as a deliberate project action — not automatically — under either
of the following conditions:

1. **New currency enters the catalog.** When a catalog entry is authored in a
   currency not currently in the table, the table must be updated before the entry
   can be promoted from `draft` to `reviewed`. The new rate is added to the table
   with the current snapshot date. All other rates are refreshed at the same time to
   keep the snapshot date uniform across the table.

2. **Snapshot is more than 12 months old and a new evaluation run is being
   performed.** Stale rates do not invalidate prior simulation output (that output
   cites its snapshot date), but a new evaluation run that relies on year-old rates
   must acknowledge the staleness explicitly in its output metadata.

### Snapshot-history protocol

When rates are updated:
- The prior snapshot is archived in the Appendix (Section A below) with its full date,
  source, and all rate values.
- The table in Section 2 is replaced with the new rates.
- The version field in the document frontmatter is incremented.
- A git commit records the change with the message format:
  `corpus/program/CURRENCIES.md: refresh FX snapshot YYYY-MM-DD`

Prior simulation output that cites a specific snapshot date remains valid. It is not
silently invalidated by a rate update; the reader can consult the Appendix to
reconstruct the rates used.

---

## 4. Normalization Rule

**Rule:** When Tier A simulation compares catalog entries denominated in different
currencies, all cost and revenue fields are converted to USD using the rates in the
Section 2 table. The snapshot date used for the conversion is recorded in the
simulation run's output metadata.

**Mechanics:**

```
usd_equivalent = declared_amount × rate_for_currency_code
```

where `rate_for_currency_code` is the value in the "USD per 1 unit" column of the
Section 2 table for the entry's `economics.currency` field.

**Examples:**

```
EUR entry: capital_cost.mid = 25,000 EUR
  → usd_equivalent = 25,000 × 1.0850 = $27,125 USD

JPY entry: capital_cost.mid = 3,500,000 JPY
  → usd_equivalent = 3,500,000 × 0.00665 = $23,275 USD

GBP entry: capital_cost.mid = 18,000 GBP
  → usd_equivalent = 18,000 × 1.2700 = $22,860 USD
```

**What normalization is NOT:**

- Normalization does not rewrite catalog entry frontmatter. The entry retains its
  declared currency. Conversion happens only in simulation output.
- Normalization does not appear in catalog entry prose. A EUR-denominated entry's
  prose body states all amounts in EUR; USD equivalents appear only in simulation
  output tables.
- Normalization is not a validity judgment. A GBP entry is not "better" or "worse"
  than a USD entry because of the exchange rate; the normalization makes them
  comparable in the simulation, nothing more.

See `docs/METHODOLOGY.md` Section 4.2 for the full evaluation normalization process,
and `docs/STYLE-GUIDE.md` Section 5.3 for the writing rule prohibiting cross-currency
comparisons in catalog entry prose.

---

## 5. Historical Cost Data: CPI + FX Methodology

### 5.1 Scope

This section covers two distinct cases:

1. **Pre-2020 modern-currency amounts** — e.g., a 1985 USD cost figure that needs
   to be brought forward to 2024 USD for comparison with a current-year catalog entry.
2. **Pre-modern or non-decimal monetary units** — e.g., shillings, livres, thalers,
   koku, maravedís, or other historical monetary units that have no direct FX rate.

Case 1 uses CPI adjustment only (no FX step if the source currency matches the base).
Case 2 uses a two-step process: purchasing-power reconstruction followed by CPI
adjustment and FX conversion.

### 5.2 CPI series used

**Series: US CPI-U — Consumer Price Index, Urban All Consumers, All Items**

- Issuing body: US Bureau of Labor Statistics (BLS)
- Data access: https://www.bls.gov/cpi/ (public, free)
- Base period: 1982–84 = 100 (BLS standard base)
- Frequency: Monthly; annual averages used for year-to-year adjustment
- Citation format in CERES: `[BLS CPI-U, year]` in inline citations;
  full reference in `## Sources` blocks:
  > US Bureau of Labor Statistics. *Consumer Price Index, Urban All Consumers, All
  > Items (CPI-U)*. Series ID: CUUR0000SA0. Retrieved from https://www.bls.gov/cpi/

**Why CPI-U:** CPI-U is the standard US general-price-level index for converting
historical USD amounts to a common year. It covers the urban consumer basket (about
93% of the US population) and has continuous monthly data from 1913. It is freely
accessible, widely cited in economic literature, and reproducible without proprietary
data access.

**Limitation to acknowledge:** CPI-U reflects the consumer basket, not the producer
or capital-equipment price level. For equipment costs, the Producer Price Index
(PPI) for final demand capital equipment would be more precise. CERES uses CPI-U
for simplicity and transparency, given the order-of-magnitude precision of all
estimates. When a specific entry's CPI vs. PPI divergence is likely to be
material (e.g., heavy industrial equipment with a long and divergent price history),
the author may substitute the relevant PPI series and must cite it explicitly.

### 5.3 Adjustment formula (Case 1: pre-2020 USD to current USD)

```
adjusted_amount = original_amount × (CPI_target_year / CPI_source_year)
```

where `CPI_target_year` and `CPI_source_year` are annual-average CPI-U values for
the respective years.

**Example:**

```
Original: $12,000 in 1990 USD
CPI-U 1990 annual average: 130.7
CPI-U 2024 annual average: ~314.0 (approximate; use current BLS published figure)

adjusted = $12,000 × (314.0 / 130.7) ≈ $28,820 in 2024 USD
```

Label the result: "approximately $29,000 in 2024 USD (CPI-U adjusted from 1990;
[BLS CPI-U, 1990 and 2024 annual averages])."

Round to two significant figures consistent with the order-of-magnitude precision
standard in `docs/METHODOLOGY.md` Section 3.5.

### 5.4 Two-step process (Case 2: pre-modern monetary units)

Pre-modern monetary units (shillings, livres, thalers, koku, maravedís, etc.) do not
have continuous exchange-rate series to modern currencies. Converting them requires
a purchasing-power reconstruction step before any CPI or FX adjustment.

**Step 1 — Purchasing-power reconstruction.**
Use a wage-based or commodity-basket-based reconstruction from the economic-history
literature. Acceptable series:

- **Allen real wage series** (Robert Allen, Oxford): daily wages in grams of silver
  and in commodity-basket equivalents, 1300–1850, multiple cities and regions.
  [Allen 2001, *Explorations in Economic History*]
- **Phelps Brown and Hopkins commodity basket** (UK): seven-commodity basket price
  index, 1264–1954. [Phelps Brown and Hopkins 1956, *Economica*]
- **Broadberry et al. GDP per capita series**: for macro-level purchasing power
  comparisons across pre-modern economies. [Broadberry et al. 2015]

Do not use informal "X shillings = Y modern dollars" conversions found on the web
or in popular-press sources. These are typically undocumented and inconsistent.

**Step 2 — CPI adjustment and FX conversion to USD.**
Once a modern-currency equivalent in a reference year has been established via Step 1,
apply the CPI-U adjustment (Section 5.3) and, if not already in USD, multiply by
the appropriate FX rate from the Section 2 table (or a historical FX rate if the
target year is before the current snapshot).

**Labeling requirement.** The full conversion chain must be stated explicitly:

> "Approximately $X in 2024 USD (wage-basket reconstruction via [Allen 2001,
> Table 2], adjusted to 2024 via CPI-U [BLS CPI-U, reference year and 2024 annual
> averages], converted from GBP via [FX rate with snapshot date])."

See `docs/METHODOLOGY.md` Section 4.4 for the editorial enforcement rule: a
historical-currency conversion without a stated methodology is a P1 finding for E-1.

---

## Sources

1. European Central Bank. *Euro foreign exchange reference rates*. Published daily
   at https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/

2. Board of Governors of the Federal Reserve System. *Foreign Exchange Rates — H.10
   Statistical Release*. Published weekly at
   https://www.federalreserve.gov/releases/H10/

3. US Bureau of Labor Statistics. *Consumer Price Index, Urban All Consumers, All
   Items (CPI-U)*. Series ID: CUUR0000SA0. Published monthly at
   https://www.bls.gov/cpi/

4. Allen, Robert C. 2001. "The great divergence in European wages and prices from
   the Middle Ages to the First World War." *Explorations in Economic History* 38(4):
   411–447.

5. Phelps Brown, E. H., and Sheila V. Hopkins. 1956. "Seven centuries of the prices
   of consumables, compared with builders' wage-rates." *Economica* 23(92): 296–314.

6. Broadberry, Stephen, Bruce Campbell, Alexander Klein, Mark Overton, and Bas van
   Leeuwen. 2015. *British Economic Growth, 1270–1870*. Cambridge University Press.

---

## Appendix A: Snapshot History

This appendix archives all prior FX snapshots. When a new snapshot is published in
Section 2, the previous snapshot is moved here. Each archived snapshot preserves
the full table, date, and source so that prior simulation output remains reproducible.

### Snapshot 2026-04-18 (initial; current)

See Section 2. This is the first snapshot; no prior snapshot to archive.

| Currency | Code | USD per 1 unit | Source |
|---|---|---:|---|
| US Dollar | USD | 1.0000 | Definition (base) |
| Euro | EUR | 1.0850 | ECB reference rate |
| Pound sterling | GBP | 1.2700 | ECB reference rate |
| Japanese yen | JPY | 0.00665 | ECB reference rate |
| Canadian dollar | CAD | 0.7350 | Federal Reserve H.10 |
| Australian dollar | AUD | 0.6420 | Federal Reserve H.10 |
| Swiss franc | CHF | 1.1250 | ECB reference rate |
| Chinese yuan | CNY | 0.1380 | Federal Reserve H.10 |
| Indian rupee | INR | 0.01195 | Federal Reserve H.10 |
| Mexican peso | MXN | 0.05070 | Federal Reserve H.10 |
| Brazilian real | BRL | 0.1790 | Federal Reserve H.10 |
| South African rand | ZAR | 0.05500 | Federal Reserve H.10 |
