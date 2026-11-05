# Rebuild the CERES reader and native tools

The complete source ZIP contains the original CERES Git tree, original file
modes, its exact commit object and a verified locked Cargo dependency capsule.
`SOURCE-MANIFEST.json` reconstructs the complete Git tree rather than listing a
selected source subset. Original software/content and third-party grants apply.
Draft entries and their citation gaps are preserved. Rebuilding repeats their
assumptions; it does not validate equipment, economics or historical claims.

Prerequisites: Python 3.11+, Rust 1.95.0, a native linker, rustfmt/Clippy, the
`wasm32-unknown-unknown` target and wasm-bindgen CLI 0.2.127. Node 22 and pinned
Playwright 1.58.2/its Chromium are needed for browser tests. Those installed tools
are not bundled. Package acquisition for Cargo is offline after input restoration.
The Rust toolchain/CLI and npm/browser acquisition are separate prerequisites.

## Verify before restoration

Obtain the expected `BUILD-MANIFEST.json` SHA from a separately trusted CI or
release receipt. A file cannot independently authenticate its own manifest.
Use the receiver from a trusted CERES checkout:

```powershell
python tools/receive-site.py --site C:/scratch/CERES --manifest-sha256 <trusted-manifest-sha> --restore-source C:/scratch/ceres-source
```

Use unused paths on your machine. The receiver reads all artifact files and
verifies hashes, runtime identity, the complete source Git tree/commit, original
modes, original dependency sources and notices before creating the new source
folder. It rejects existing or linked destinations and never overwrites a source
folder. On Unix, it restores executable bits; Windows does not enforce Unix modes.
Manifest and source ZIP remain available if the browser evaluator fails.

To verify just the complete source download, use the source SHA and commit from
the trusted build receipt:

```powershell
python tools/receive-source.py --source ceres-source.zip --sha256 <trusted-source-sha> --commit <source-commit> --restore-source C:/scratch/ceres-source
```

## Restore offline dependencies

From the restored source directory, use two more **new, separate folders outside
the source repository**. See `cargo-inputs/README.md` for the complete input policy.

```powershell
$expected = (Get-Content cargo-inputs/sha256.txt).Split()[0]
python tools/input-custody.py --sha256 $expected --inputs C:/scratch/ceres-inputs --cargo-home C:/scratch/ceres-cargo-home
$env:CARGO_HOME = 'C:/scratch/ceres-cargo-home'
$env:CARGO_NET_OFFLINE = 'true'
$env:CARGO_INCREMENTAL = '0'
cargo +1.95.0 test --workspace --all-targets --locked --offline
cargo +1.95.0 fmt --all --check
cargo +1.95.0 clippy --workspace --all-targets --all-features --no-deps --locked --offline -- -D warnings
```

If you set `CARGO_TARGET_DIR`, keep it outside the source, inputs and Cargo home.
A shared compiled target may be reused; this is not a fresh compiled-cache claim.
The new Cargo home and all dependency inputs are independent of an owner's cache.
Canonical lock identity permits only CRLF-to-LF checkout conversion, without
changing dependency pins or other lock content.

## Native CLI and actual WASM

Native filesystem catalog/comparison/events/SCENARIUM packet operations remain
available. They are not browser features. For example:

```powershell
cargo +1.95.0 run --locked --offline -- --help
cargo +1.95.0 run --locked --offline -- --catalog catalog --scale town --lens market --json
cargo +1.95.0 build --locked --offline -p ceres-web --example reader-control
```

Use the source revision shown on the downloaded page as `<source-commit>`. Build
from the source ZIP without Git, into a **new** folder under `dist`:

```powershell
python tools/build-pages.py --expected-source-head <source-commit> --output dist/rebuild/CERES
node tools/check-reader.mjs dist/rebuild/CERES/pkg/ceres_web.js <compiled-target>/debug/examples/reader-control.exe dist/reader-parity.json
```

On Unix, omit `.exe`. The native control path follows your actual Cargo target.
The parity report compares exact Rust JSON/error strings for135 typed inputs;
four raw JavaScript integer-conversion seams are recorded separately. The worker
rejects those values before bindgen conversion. Equivalent results do not imply
identical compiled-module bytes across toolchains, paths or platforms.

## Separate download budgets

The runtime, notices and build record stay below5,000,000 bytes. Optional
`downloads/` files stay below12,000,000 bytes; total below17,000,000. The complete
source kit is fetched only when selected. Nothing is trimmed from the Git tree
or licensed input closure to meet a smaller runtime budget. Limits are reviewed
in implementation-plan section9 and measured separately in `BUILD-MANIFEST.json`.

These instructions support software inspection/replay. Worker lifecycle,
Windows/Linux hosted archive replay and default-branch/live release evidence
must be checked in the current delivery wave before calling a release qualified.

## Complete checkout versus archive replay

With a freshly built site and the same installed prerequisites, the portable
qualifier verifies the site, restores its complete source outside Git, restores
all dependency inputs into a new Cargo home, and runs native, actual WASM,
receiver and browser checks against the archive build:

```powershell
$manifestSha = (Get-FileHash dist/CERES/BUILD-MANIFEST.json -Algorithm SHA256).Hash.ToLowerInvariant()
python tools/qualify-source.py --site dist/CERES --manifest-sha256 $manifestSha --scratch C:/scratch/ceres-replay
```

Use a new scratch folder outside source and compiled target. The manifest SHA
here identifies a locally built test fixture; external artifact reception still
requires the independently trusted CI/release receipt described above. The
qualifier preserves full stdout/stderr/exits and generated files for all30
original CLI controls on both paths, verifies the unchanged original8-file
native contract, and compares source ZIP bytes without normalizing outputs.
Seven native tests,135 typed native/WASM controls,18 receivers and43 archive
browser cases run. The120 UI results/downloads per viewport remain separate from
the four raw JavaScript integer ABI seams. Installed pinned npm/browser tools are
copied/reused; Cargo inputs and home are independent. Compiled target reuse and
different module hashes are explicit. Reports are retained under scratch.

The workflow pins Ubuntu24.04 and Windows2022 with an explicit Bash shell, using
the supported [runner labels](https://docs.github.com/en/actions/how-tos/write-workflows/choose-where-workflows-run/choose-the-runner-for-a-job)
and [Windows Bash behavior](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).
Both jobs must succeed before the Linux Pages artifact can deploy. A PR can build
GitHub's merge commit; its actual source identity must remain distinct from the
PR branch even when their complete trees match. Hosted results remain unqualified
until the current run and downloaded evidence are inspected.

Archive builds reject files outside the exact source manifest, except documented
generated `dist/`, `target/`, `node_modules/`, `test-results/` and Python bytecode
cache directories. In particular, an unlisted `.cargo/config.toml` is rejected
before build. Receiver destinations may not overlap the default repository
`target/` or an explicit `CARGO_TARGET_DIR`.
