# Pinned native and browser build inputs

`inputs.zip` contains all 32 external packages from the unchanged `Cargo.lock`:
27 original registry archives and every original member, plus five Git packages
from four complete pinned public Git trees. Original Git blobs, modes, package
manifests, dotfiles and root grants remain under `original-git/`. The buildable
`vendor/` tree preserves all registry members. Cargo normalizes the five Git
build manifests; the original manifests are preserved separately. Every other
vendored Git file matches its pinned original bytes. No upstream grant changes.
The full inventory and Git identities are in `manifest.json` and in the ZIP.

Python 3.11+, installed Rust 1.95.0 with rustfmt/Clippy and the
`wasm32-unknown-unknown` target, a native linker, and wasm-bindgen CLI 0.2.127
are prerequisites. Node and Playwright remain separate browser-test prerequisites.
This capsule bundles dependency inputs, not those installed tools.

Verify first, using the SHA from a trusted checkout or release receipt:

```powershell
$expected = (Get-Content cargo-inputs/sha256.txt).Split()[0]
python tools/input-custody.py --sha256 $expected
python tests/input_custody.py
```

Restore into two **new, separate folders outside the source repository**:

```powershell
python tools/input-custody.py --sha256 $expected --inputs C:/scratch/ceres-inputs --cargo-home C:/scratch/ceres-cargo-home
$env:CARGO_HOME = 'C:/scratch/ceres-cargo-home'
$env:CARGO_NET_OFFLINE = 'true'
$env:CARGO_INCREMENTAL = '0'
cargo +1.95.0 test --workspace --all-targets --locked --offline
cargo +1.95.0 build --release --target wasm32-unknown-unknown -p ceres-web --lib --features wasm --locked --offline
```

Choose unused paths suitable for your computer. Restoration never replaces an
existing destination. Keep the compiled target separate; a shared compiled
target can be reused and is not evidence of a fresh compiled-cache build.
The new Cargo home resolves only the verified vendor inputs, with acquisition
offline. Keep the original `Cargo.lock` and source manifests unchanged.

The outer SHA and file inventories detect corruption against the trusted
checkout; they do not independently authenticate an upstream author or validate
the draft equipment economics. CERES's existing software/content scope and all
third-party grants remain distinct. This dependency capsule alone does not
qualify a complete source download, browser lifecycle, hosted replay or release.

Lock identity is the canonical Git LF blob and SHA. Verification admits only
Windows checkout CRLF-to-LF conversion; both forms are tested, and altered lock
content is rejected. Source ZIP export must disable Git checkout conversion and
verify every exported blob before claiming exact source custody.
