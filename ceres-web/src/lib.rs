//! Browser sensitivity adapter over CERES's existing draft catalog and lens math.
use ceres::{civic_lens, coop_lens, default_scales, market_lens, CatalogEntry, LensResult};
use serde::Serialize;
const ENTRIES: [&str; 2] = [
    include_str!("../../catalog/smithing/entries/001-backyard-propane-compact.md"),
    include_str!("../../catalog/smithing/entries/002-induction-modular-small-repair.md"),
];
#[derive(Serialize)]
pub struct ResultSet {
    pub market: LensResult,
    pub coop: LensResult,
    pub civic: LensResult,
    pub population: f64,
    pub households: f64,
    pub status: &'static str,
}
pub fn evaluate(
    entry: usize,
    scale: &str,
    participation: f64,
    wage: f64,
) -> Result<ResultSet, String> {
    if entry >= ENTRIES.len()
        || !participation.is_finite()
        || !(0.001..=0.20).contains(&participation)
        || !wage.is_finite()
        || !(10000.0..=200000.0).contains(&wage)
    {
        return Err("Choose a sample, participation 0.1–20%, and wage $10,000–200,000".into());
    }
    let mut scales = default_scales();
    let mut scale = scales.remove(scale).ok_or("Unknown settlement scale")?;
    scale.participation_rate = participation;
    scale.median_wage = wage;
    let text = ENTRIES[entry];
    let yaml = text
        .strip_prefix("---")
        .and_then(|s| s.split_once("\n---").map(|(yaml, _)| yaml))
        .ok_or("Missing catalog frontmatter")?;
    let entry = CatalogEntry::from_yaml_str(yaml)?;
    Ok(ResultSet {
        market: market_lens(&entry, &scale)?,
        coop: coop_lens(&entry, &scale)?,
        civic: civic_lens(&entry, &scale)?,
        population: scale.population_midpoint,
        households: scale.household_count,
        status: "draft catalog sensitivity; not validated",
    })
}
#[cfg(feature = "wasm")]
#[wasm_bindgen::prelude::wasm_bindgen]
pub fn evaluate_json(
    entry: usize,
    scale: &str,
    participation: f64,
    wage: f64,
) -> Result<String, wasm_bindgen::JsValue> {
    evaluate(entry, scale, participation, wage)
        .and_then(|v| serde_json::to_string(&v).map_err(|e| e.to_string()))
        .map_err(|e| wasm_bindgen::JsValue::from_str(&e))
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn matches_native_lenses_and_sensitivity() {
        for entry in 0..2 {
            for scale in ceres::SCALES {
                let r = evaluate(entry, scale, 0.025, 56000.0).unwrap();
                assert!(r.coop.primary_metric > 0.0);
                assert!(r.civic.primary_metric >= 0.0);
            }
        }
        let low = evaluate(1, "village", 0.001, 56000.0).unwrap();
        let high = evaluate(1, "village", 0.2, 56000.0).unwrap();
        assert_ne!(low.coop.verdict, high.coop.verdict);
        assert_eq!(low.coop.primary_metric, high.coop.primary_metric);
    }
    #[test]
    fn rejects_nonfinite_or_out_of_scope_controls() {
        assert!(evaluate(2, "town", 0.02, 56000.0).is_err());
        assert!(evaluate(0, "planet", 0.02, 56000.0).is_err());
        assert!(evaluate(0, "town", f64::NAN, 56000.0).is_err());
        assert!(evaluate(0, "town", 0.02, 0.0).is_err());
    }
}
