//! Native observation control for the existing bounded reader, not a new model.
use std::env;

fn main() {
    let args: Vec<String> = env::args().skip(1).collect();
    if args.len() != 4 {
        eprintln!("expected entry, scale, participation and wage");
        std::process::exit(1);
    }
    let values = args[0].parse::<usize>().map(|entry| {
        // Keep typed conversion separate from the original evaluation admission.
        (entry, args[2].parse::<f64>(), args[3].parse::<f64>())
    });
    let (entry, participation, wage) = match values {
        Ok((entry, Ok(participation), Ok(wage))) => (entry, participation, wage),
        _ => {
            eprintln!("invalid typed control argument");
            std::process::exit(1);
        }
    };
    let result = ceres_web::evaluate(entry, &args[1], participation, wage)
        .and_then(|result| serde_json::to_string(&result).map_err(|error| error.to_string()));
    let response = match result {
        Ok(json) => serde_json::json!({"ok": true, "json": json}),
        Err(error) => serde_json::json!({"ok": false, "error": error}),
    };
    println!("{response}");
}
