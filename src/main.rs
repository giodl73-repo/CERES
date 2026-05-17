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
    let mut json = false;
    let mut jsonl: Option<PathBuf> = None;
    let mut args = env::args().skip(1);
    while let Some(arg) = args.next() {
        match arg.as_str() {
            "--catalog" => catalog = args.next().map(PathBuf::from),
            "--json" => json = true,
            "--jsonl" => jsonl = args.next().map(PathBuf::from),
            "--help" | "-h" => {
                print_help();
                return Ok(());
            }
            other => return Err(format!("unknown argument: {other}")),
        }
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
    println!("Usage: ceres --catalog <catalog-trade-dir> [--json] [--jsonl <path>]");
}
