use rally_core::{
    BeatRef, EventLogEntry, PacketManifest, SimulationMetric, SimulationRun, ValidationFinding,
    ValidationReport,
};
use serde::Serialize;
use serde_yaml::{Mapping, Value};
use std::collections::BTreeMap;
use std::fmt;
use std::fs;
use std::path::{Path, PathBuf};

const COST_OF_CAPITAL: f64 = 0.08;
const DEFAULT_DUES_PER_MEMBER: f64 = 200.0;
const DEFAULT_AMORTIZATION_YEARS: f64 = 30.0;
const DEFAULT_USAGE_RATE_THRESHOLD: f64 = 2.0;
const MARGIN_WIN: f64 = 0.20;

pub const SCALES: [&str; 3] = ["village", "town", "small_city"];
pub const LENSES: [&str; 3] = ["market", "coop", "civic"];

#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize)]
#[serde(rename_all = "snake_case")]
pub enum Verdict {
    Win,
    Marginal,
    Fail,
}

impl Verdict {
    fn rank(self) -> u8 {
        match self {
            Verdict::Win => 0,
            Verdict::Marginal => 1,
            Verdict::Fail => 2,
        }
    }

    fn worst(left: Self, right: Self) -> Self {
        if left.rank() >= right.rank() {
            left
        } else {
            right
        }
    }
}

impl fmt::Display for Verdict {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Verdict::Win => f.write_str("win"),
            Verdict::Marginal => f.write_str("marginal"),
            Verdict::Fail => f.write_str("fail"),
        }
    }
}

#[derive(Debug, Clone, PartialEq, Serialize)]
pub struct LensResult {
    pub verdict: Verdict,
    pub primary_metric: f64,
    pub metric_name: String,
    pub notes: String,
}

impl LensResult {
    fn new(
        verdict: Verdict,
        primary_metric: f64,
        metric_name: &str,
        notes: impl Into<String>,
    ) -> Self {
        Self {
            verdict,
            primary_metric,
            metric_name: metric_name.to_string(),
            notes: notes.into(),
        }
    }
}

#[derive(Debug, Clone)]
pub struct Scale {
    pub name: &'static str,
    pub population_midpoint: f64,
    pub household_count: f64,
    pub median_wage: f64,
    pub civic_cost_threshold_per_household: f64,
    pub participation_rate: f64,
    pub member_pool_floor: f64,
}

pub fn default_scales() -> BTreeMap<String, Scale> {
    [
        Scale {
            name: "village",
            population_midpoint: 1250.0,
            household_count: 500.0,
            median_wage: 48000.0,
            civic_cost_threshold_per_household: 120.0,
            participation_rate: 0.025,
            member_pool_floor: 10.0,
        },
        Scale {
            name: "town",
            population_midpoint: 8500.0,
            household_count: 3400.0,
            median_wage: 56000.0,
            civic_cost_threshold_per_household: 100.0,
            participation_rate: 0.025,
            member_pool_floor: 10.0,
        },
        Scale {
            name: "small_city",
            population_midpoint: 45000.0,
            household_count: 18000.0,
            median_wage: 62000.0,
            civic_cost_threshold_per_household: 80.0,
            participation_rate: 0.020,
            member_pool_floor: 10.0,
        },
    ]
    .into_iter()
    .map(|scale| (scale.name.to_string(), scale))
    .collect()
}

#[derive(Debug, Clone)]
pub struct CatalogEntry {
    pub id: String,
    pub trade: String,
    pub source_path: Option<PathBuf>,
    data: Mapping,
}

impl CatalogEntry {
    pub fn from_markdown(path: impl AsRef<Path>) -> Result<Self, String> {
        let path = path.as_ref();
        let text = fs::read_to_string(path)
            .map_err(|err| format!("failed to read {}: {err}", path.display()))?;
        let frontmatter = split_frontmatter(&text)
            .ok_or_else(|| format!("{} does not start with YAML frontmatter", path.display()))?;
        let data: Mapping = serde_yaml::from_str(frontmatter)
            .map_err(|err| format!("failed to parse YAML in {}: {err}", path.display()))?;
        let id =
            string_field(&data, "id").ok_or_else(|| format!("{} missing id", path.display()))?;
        let trade = string_field(&data, "trade").unwrap_or_else(|| "unknown".to_string());
        Ok(Self {
            id,
            trade,
            source_path: Some(path.to_path_buf()),
            data,
        })
    }

    pub fn from_yaml_str(value: &str) -> Result<Self, String> {
        let data: Mapping = serde_yaml::from_str(value).map_err(|err| err.to_string())?;
        let id = string_field(&data, "id").ok_or_else(|| "entry missing id".to_string())?;
        let trade = string_field(&data, "trade").unwrap_or_else(|| "unknown".to_string());
        Ok(Self {
            id,
            trade,
            source_path: None,
            data,
        })
    }

    fn required_number(&self, path: &[&str]) -> Result<f64, String> {
        nested_number(&self.data, path)
            .ok_or_else(|| format!("{} missing numeric field {}", self.id, path.join(".")))
    }

    fn optional_number(&self, path: &[&str], default: f64) -> f64 {
        nested_number(&self.data, path).unwrap_or(default)
    }
}

#[derive(Debug, Clone, PartialEq, Serialize)]
pub struct CellResult {
    pub entry_id: String,
    pub trade: String,
    pub scale: String,
    pub lens: String,
    pub verdict: Verdict,
    pub primary_metric: f64,
    pub metric_name: String,
    pub notes: String,
    pub rally_run_id: String,
    pub rally_metric: String,
}

impl CellResult {
    fn from_lens(entry: &CatalogEntry, scale: &str, lens: &str, result: LensResult) -> Self {
        let run = SimulationRun::new("ceres-tier-a", &entry.id, &format!("{scale}-{lens}"));
        let metric = SimulationMetric::new(&result.metric_name, result.primary_metric);
        Self {
            entry_id: entry.id.clone(),
            trade: entry.trade.clone(),
            scale: scale.to_string(),
            lens: lens.to_string(),
            verdict: result.verdict,
            primary_metric: result.primary_metric,
            metric_name: result.metric_name,
            notes: result.notes,
            rally_run_id: run.run_id,
            rally_metric: metric.name,
        }
    }

    pub fn to_event_jsonl(&self) -> String {
        EventLogEntry {
            run_id: self.rally_run_id.clone(),
            beat: BeatRef::new("tier-a", &self.scale, &self.lens),
            event_type: "ceres_lens_result".to_string(),
            message: format!(
                "{} {} {} {}={:.3}",
                self.entry_id, self.scale, self.verdict, self.metric_name, self.primary_metric
            ),
        }
        .to_jsonl()
    }
}

#[derive(Debug, Clone, PartialEq, Serialize)]
pub struct CatalogRun {
    pub run_id: String,
    pub catalog: String,
    pub cells: Vec<CellResult>,
    pub validation_status: String,
    pub evidence_packet_id: String,
}

pub fn market_lens(entry: &CatalogEntry, scale: &Scale) -> Result<LensResult, String> {
    let capital_cost = entry.required_number(&["economics", "capital_cost", "mid"])?;
    let install_cost = entry.optional_number(&["economics", "install_cost"], 0.0);
    let total_invested = capital_cost + install_cost;
    let annual_fixed = entry.optional_number(&["economics", "annual_maintenance"], 0.0)
        + entry.optional_number(&["economics", "annual_consumables"], 0.0)
        + entry.optional_number(&["economics", "floor_space_rent_per_year"], 0.0);
    let throughput = entry.required_number(&["sim_params", "throughput_units_equiv_per_year"])?;
    let downtime = entry.optional_number(&["sim_params", "downtime_fraction"], 0.0);
    let effective_units = throughput * (1.0 - downtime);
    let Some(market_price) =
        nested_number(&entry.data, &["economics", "market_price_per_unit", "mid"])
    else {
        return Ok(LensResult::new(
            Verdict::Fail,
            -1.0,
            "payback_years",
            "market_price_per_unit absent or zero; entry not designed for market lens",
        ));
    };
    if market_price == 0.0 {
        return Ok(LensResult::new(
            Verdict::Fail,
            -1.0,
            "payback_years",
            "market_price_per_unit absent or zero; entry not designed for market lens",
        ));
    }
    let variable_cost_per_unit =
        entry.optional_number(&["sim_params", "variable_cost_per_unit"], 0.0);
    let annual_revenue = effective_units * market_price;
    let annual_variable = effective_units * variable_cost_per_unit;
    let annual_gross_margin = annual_revenue - annual_variable - annual_fixed;
    let capital_service = total_invested * COST_OF_CAPITAL;
    let operator_take_home = annual_gross_margin - capital_service;
    if annual_gross_margin <= 0.0 {
        return Ok(LensResult::new(
            Verdict::Fail,
            -1.0,
            "payback_years",
            "annual_gross_margin <= 0; payback never recoverable",
        ));
    }
    let payback_years = total_invested / annual_gross_margin;
    let wage_win_threshold = scale.median_wage * 1.20;
    let wage_fail_threshold = scale.median_wage * 0.80;
    let wage_verdict = if operator_take_home < wage_fail_threshold {
        Verdict::Fail
    } else if operator_take_home < wage_win_threshold {
        Verdict::Marginal
    } else {
        Verdict::Win
    };
    let payback_verdict = if payback_years > 8.0 {
        Verdict::Fail
    } else if payback_years > 8.0 * (1.0 - MARGIN_WIN) {
        Verdict::Marginal
    } else {
        Verdict::Win
    };
    let verdict = Verdict::worst(wage_verdict, payback_verdict);
    let mut notes = Vec::new();
    if wage_verdict != Verdict::Win {
        notes.push(format!(
            "wage_verdict={wage_verdict} (take_home={operator_take_home:.0} vs median={})",
            scale.median_wage
        ));
    }
    if payback_verdict != Verdict::Win {
        notes.push(format!(
            "payback_verdict={payback_verdict} (payback={payback_years:.2} yr)"
        ));
    }
    Ok(LensResult::new(
        verdict,
        payback_years,
        "payback_years",
        notes.join("; "),
    ))
}

pub fn coop_lens(entry: &CatalogEntry, scale: &Scale) -> Result<LensResult, String> {
    let capital_cost = entry.required_number(&["economics", "capital_cost", "mid"])?;
    let install_cost = entry.optional_number(&["economics", "install_cost"], 0.0);
    let total_invested = capital_cost + install_cost;
    let annual_op_cost = entry.optional_number(&["economics", "annual_maintenance"], 0.0)
        + entry.optional_number(&["economics", "annual_consumables"], 0.0)
        + entry.optional_number(&["economics", "floor_space_rent_per_year"], 0.0);
    let lifespan_years = entry.optional_number(&["sim_params", "lifespan_years"], 25.0);
    let annual_capital_charge = total_invested / lifespan_years;
    let total_annual_cost = annual_capital_charge + annual_op_cost;
    let dues = entry.optional_number(
        &["sim_params", "per_member_annual_dues"],
        DEFAULT_DUES_PER_MEMBER,
    );
    let break_even = (total_annual_cost / dues).ceil();
    let feasible_pool =
        (scale.population_midpoint * scale.participation_rate).max(scale.member_pool_floor);
    let verdict = if break_even > feasible_pool {
        Verdict::Fail
    } else {
        let headroom_ratio = (feasible_pool - break_even) / feasible_pool;
        if headroom_ratio >= MARGIN_WIN {
            Verdict::Win
        } else {
            Verdict::Marginal
        }
    };
    Ok(LensResult::new(
        verdict,
        break_even,
        "break_even_members",
        format!(
            "feasible_pool={feasible_pool:.1}, break_even={break_even:.0}, total_annual_cost={total_annual_cost:.0}"
        ),
    ))
}

pub fn civic_lens(entry: &CatalogEntry, scale: &Scale) -> Result<LensResult, String> {
    let capital_cost = entry.required_number(&["economics", "capital_cost", "mid"])?;
    let install_cost = entry.optional_number(&["economics", "install_cost"], 0.0);
    let total_invested = capital_cost + install_cost;
    let annual_op_cost_civic = entry.optional_number(&["economics", "annual_maintenance"], 0.0)
        + entry.optional_number(&["economics", "annual_consumables"], 0.0);
    let amortization_years = entry.optional_number(
        &["sim_params", "amortization_years"],
        DEFAULT_AMORTIZATION_YEARS,
    );
    let total_civic_cost = total_invested / amortization_years + annual_op_cost_civic;
    let per_household_cost = total_civic_cost / scale.household_count;
    let annual_public_use_hours =
        nested_number(&entry.data, &["sim_params", "annual_public_use_hours"])
            .or_else(|| nested_number(&entry.data, &["trade_specific", "annual_public_use_hours"]))
            .unwrap_or(0.0);
    let usage_rate_threshold = entry.optional_number(
        &["sim_params", "usage_rate_threshold"],
        DEFAULT_USAGE_RATE_THRESHOLD,
    );
    let hours_per_capita = if scale.population_midpoint > 0.0 {
        annual_public_use_hours / scale.population_midpoint
    } else {
        0.0
    };
    let cost_verdict = if per_household_cost > scale.civic_cost_threshold_per_household {
        Verdict::Fail
    } else {
        let cost_margin = (scale.civic_cost_threshold_per_household - per_household_cost)
            / scale.civic_cost_threshold_per_household;
        if cost_margin >= MARGIN_WIN {
            Verdict::Win
        } else {
            Verdict::Marginal
        }
    };
    let usage_verdict = if hours_per_capita >= usage_rate_threshold {
        Verdict::Win
    } else {
        Verdict::Fail
    };
    Ok(LensResult::new(
        Verdict::worst(cost_verdict, usage_verdict),
        per_household_cost,
        "per_household_cost",
        format!(
            "per_hh={per_household_cost:.2}, threshold={}, hrs/capita={hours_per_capita:.3} vs threshold={usage_rate_threshold}",
            scale.civic_cost_threshold_per_household
        ),
    ))
}

pub fn run_entry(entry: &CatalogEntry) -> Result<Vec<CellResult>, String> {
    let scales = default_scales();
    let mut cells = Vec::new();
    for scale_name in SCALES {
        let scale = scales
            .get(scale_name)
            .ok_or_else(|| format!("missing scale {scale_name}"))?;
        for lens in LENSES {
            let result = match lens {
                "market" => market_lens(entry, scale)?,
                "coop" => coop_lens(entry, scale)?,
                "civic" => civic_lens(entry, scale)?,
                _ => unreachable!("static lens list"),
            };
            cells.push(CellResult::from_lens(entry, scale_name, lens, result));
        }
    }
    Ok(cells)
}

pub fn run_catalog(catalog_dir: impl AsRef<Path>) -> Result<CatalogRun, String> {
    let catalog_dir = catalog_dir.as_ref();
    let entries_dir = catalog_dir.join("entries");
    let mut entry_paths = fs::read_dir(&entries_dir)
        .map_err(|err| format!("failed to read {}: {err}", entries_dir.display()))?
        .filter_map(Result::ok)
        .map(|entry| entry.path())
        .filter(|path| path.extension().is_some_and(|ext| ext == "md"))
        .collect::<Vec<_>>();
    entry_paths.sort();

    let mut cells = Vec::new();
    let mut findings = Vec::new();
    for path in entry_paths {
        match CatalogEntry::from_markdown(&path).and_then(|entry| run_entry(&entry)) {
            Ok(mut entry_cells) => cells.append(&mut entry_cells),
            Err(message) => findings.push(ValidationFinding::error(
                "ceres-tier-a-entry",
                &path.display().to_string(),
                &message,
            )),
        }
    }

    let catalog_name = catalog_dir
        .file_name()
        .and_then(|value| value.to_str())
        .unwrap_or("catalog");
    let run = SimulationRun::new("ceres-tier-a", catalog_name, "full-matrix");
    let report = ValidationReport {
        subject: catalog_name.to_string(),
        findings,
    };
    let mut packet = PacketManifest::new(&format!("ceres-tier-a-{catalog_name}"));
    packet.add_artifact("catalog", &catalog_dir.display().to_string());
    packet.add_artifact(
        "python-reference",
        "simulations/tier-a-comparator/src/tier_a",
    );

    Ok(CatalogRun {
        run_id: run.run_id,
        catalog: catalog_name.to_string(),
        cells,
        validation_status: report.status().to_string(),
        evidence_packet_id: packet.packet_id,
    })
}

pub fn event_jsonl(cells: &[CellResult]) -> String {
    cells.iter().map(CellResult::to_event_jsonl).collect()
}

fn split_frontmatter(text: &str) -> Option<&str> {
    let rest = text.strip_prefix("---")?;
    let rest = rest
        .strip_prefix("\r\n")
        .or_else(|| rest.strip_prefix('\n'))?;
    let end = rest.find("\n---").or_else(|| rest.find("\r\n---"))?;
    Some(&rest[..end])
}

fn string_field(data: &Mapping, key: &str) -> Option<String> {
    data.get(Value::String(key.to_string()))?
        .as_str()
        .map(str::to_string)
}

fn nested_number(data: &Mapping, path: &[&str]) -> Option<f64> {
    let (first, rest) = path.split_first()?;
    let mut current = data.get(Value::String((*first).to_string()))?;
    for key in rest {
        current = current
            .as_mapping()?
            .get(Value::String((*key).to_string()))?;
    }
    yaml_number(current)
}

fn yaml_number(value: &Value) -> Option<f64> {
    match value {
        Value::Number(number) => number.as_f64(),
        Value::String(text) => text.parse::<f64>().ok(),
        _ => None,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const ENTRY: &str = r#"
id: test-forge-001
trade: smithing
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
  throughput_units_equiv_per_year: 2400
  variable_cost_per_unit: 3.1
  downtime_fraction: 0.12
  lifespan_years: 25
  annual_public_use_hours: 17000
  usage_rate_threshold: 2.0
  amortization_years: 30
  per_member_annual_dues: 200
"#;

    #[test]
    fn market_lens_matches_python_reference() {
        let entry = CatalogEntry::from_yaml_str(ENTRY).expect("entry parses");
        let scales = default_scales();
        let result = market_lens(&entry, scales.get("town").unwrap()).expect("lens runs");

        assert_eq!(result.verdict, Verdict::Win);
        assert_eq!(result.metric_name, "payback_years");
        assert!((result.primary_metric - (34000.0 / 77993.0)).abs() < 0.001);
    }

    #[test]
    fn tier_a_runs_nine_cells_with_rally_run_ids() {
        let entry = CatalogEntry::from_yaml_str(ENTRY).expect("entry parses");
        let cells = run_entry(&entry).expect("entry runs");

        assert_eq!(cells.len(), 9);
        assert!(cells.iter().all(|cell| cell
            .rally_run_id
            .starts_with("ceres-tier-a:test-forge-001:")));
        assert!(event_jsonl(&cells).contains("\"event_type\":\"ceres_lens_result\""));
    }

    #[test]
    fn missing_required_fields_become_validation_errors() {
        let temp = std::env::temp_dir().join(format!("ceres-tier-a-test-{}", std::process::id()));
        let entries = temp.join("entries");
        fs::create_dir_all(&entries).expect("temp entries");
        fs::write(
            entries.join("broken.md"),
            "---\nid: broken\ntrade: smithing\n---\n",
        )
        .expect("write broken entry");

        let run = run_catalog(&temp).expect("catalog run returns validation state");

        assert_eq!(run.validation_status, "error");
        fs::remove_dir_all(temp).ok();
    }
}
