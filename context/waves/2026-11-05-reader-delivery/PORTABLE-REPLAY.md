# Portable source archive replay

The portable tools/qualify-source.py at `468383adf3d4c6f66710d0e93a348f104909e969` passes a full local
Windows replay. It verifies the actual complete built source kit before restoring
source outside Git, restores original32-input capsule into new inputs/Cargo home,
and records all external Cargo manifest paths within that independent tree.
Package acquisition is offline; shared compiled target and installed compiler/
linker/target/bindgen/Node/pinned npm/browser reuse are explicit. No owner registry
or Git cache is acquired inside the new Cargo home. Original8-file native
contract fingerprints bind original5a69 Rust/manifests/lock/bundled catalog data.

All30 native CLI stdout/stderr/exits and3 generated files match across checkout
and archive. On this Windows rehearsal they also match the original frozen
Windows controls exactly; only output destination argv is rebased. No output
normalization/tolerance. Seven archive native tests, formatting, strict Clippy,
135 typed native/WASM controls and18 receivers pass. Archive-built source ZIP
is exact to the checkout source ZIP; compiled module hashes differ and remain
recorded. All43 browser cases run against the archive-built actual module/UI
with no skips/flakes, including120 native outcome/download pairs per viewport.

Only the exact installed pinned Playwright1.58.2/npm tools are copied into the
archive as documented generated prerequisites. A separately owned HTTP server
uses argv spawning and its exact process handle for cleanup. Native paths/
executable suffix are selected from Cargo metadata for each host. No source-
relative TRACKER path, extra package acquisition or cache clearing is required.
Raw commands, native outputs, parity, browser and receiver evidence are retained
in validation/portable-replay; complete original/qualified artifacts stay outside
the shared mutable compiler target. This is software proof, not catalog/economic
or independent human validation.

The existing public workflow now proposes Ubuntu24.04 and Windows2022 matrix
jobs, explicit Bash, per-OS evidence and required success on both before the
Linux Pages artifact may deploy. actionlint passes. Each platform must run
checkout validation and a separate complete archive rebuild/native/WASM/receiver/
browser replay. Hosted results/artifacts are pending after push, and remain
distinct from this local rehearsal. Final role review/default/main/live delivery
and a separate TRACKER snapshot remain open.
