use std::env;
use std::fs;
use std::path::PathBuf;

fn main() {
    if let Err(err) = run() {
        eprintln!("{err}");
        std::process::exit(1);
    }
}

fn run() -> Result<(), String> {
    let mut catalog = None;
    let mut baseline = None;
    let mut candidate = None;
    let mut scale = "town".to_string();
    let mut lens = "market".to_string();
    let mut json = false;
    let mut jsonl: Option<PathBuf> = None;
    let mut args = env::args().skip(1);
    while let Some(arg) = args.next() {
        match arg.as_str() {
            "--catalog" => catalog = args.next().map(PathBuf::from),
            "--compare" => {
                baseline = args.next().map(PathBuf::from);
                candidate = args.next().map(PathBuf::from);
            }
            "--scale" => {
                scale = args
                    .next()
                    .ok_or_else(|| "missing --scale value".to_string())?
            }
            "--lens" => {
                lens = args
                    .next()
                    .ok_or_else(|| "missing --lens value".to_string())?
            }
            "--json" => json = true,
            "--jsonl" => jsonl = args.next().map(PathBuf::from),
            "--help" | "-h" => {
                print_help();
                return Ok(());
            }
            other => return Err(format!("unknown argument: {other}")),
        }
    }

    if baseline.is_some() || candidate.is_some() {
        let baseline =
            baseline.ok_or_else(|| "missing --compare <BASELINE> <CANDIDATE>".to_string())?;
        let candidate =
            candidate.ok_or_else(|| "missing --compare <BASELINE> <CANDIDATE>".to_string())?;
        let comparison = ceres::compare_entry_paths(&baseline, &candidate, &scale, &lens)?;
        if json {
            println!(
                "{}",
                serde_json::to_string_pretty(&comparison).map_err(|err| err.to_string())?
            );
        } else {
            println!(
                "CERES comparison {} -> {} at {}/{}: {} ({} improved)",
                comparison.baseline_id,
                comparison.candidate_id,
                comparison.scale,
                comparison.lens,
                comparison.status,
                comparison.improved_count
            );
        }
        return Ok(());
    }

    let catalog = catalog.ok_or_else(|| "missing --catalog <PATH>".to_string())?;
    let run = ceres::run_catalog(&catalog)?;
    if let Some(path) = jsonl {
        if let Some(parent) = path.parent() {
            fs::create_dir_all(parent)
                .map_err(|err| format!("failed to create {}: {err}", parent.display()))?;
        }
        fs::write(&path, ceres::event_jsonl(&run.cells))
            .map_err(|err| format!("failed to write {}: {err}", path.display()))?;
    }
    if json {
        println!(
            "{}",
            serde_json::to_string_pretty(&run).map_err(|err| err.to_string())?
        );
    } else {
        println!(
            "CERES Tier A Rust run {}: {} cells, validation={}",
            run.run_id,
            run.cells.len(),
            run.validation_status
        );
    }
    Ok(())
}

fn print_help() {
    println!("Usage:");
    println!("  ceres --catalog <catalog-trade-dir> [--json] [--jsonl <path>]");
    println!("  ceres --compare <baseline-entry.md> <candidate-entry.md> [--scale town] [--lens market] [--json]");
}
