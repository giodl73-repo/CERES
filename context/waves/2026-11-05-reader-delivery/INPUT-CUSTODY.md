# Locked input custody checkpoint

The tracked `cargo-inputs/inputs.zip` is4,830,483 bytes and preserves27 locked
registry archives/all members, five Cargo Git packages and four complete pinned
public Git trees with original blobs/modes/manifests/grants. Verifier checks
actual archive members against vendor bytes, Git blobs, Cargo checksums and the
unchanged root lock. All108 vendored Git non-manifest files match pinned source
exactly; five build manifests are Cargo-normalized and originals remain present.
No pins, economic code, catalogs or grants changed. Ten integrity/restore checks
pass, including actual full restore, corrupted registry/Git input, modified lock,
unsafe paths and preserving existing destinations.

At source `e24440667f7fc32b710beb49955c6d7c680d19ad`, an Git-produced ZIP outside Git resolves all32
packages from a separate copied input tree/new Cargo home with package acquisition
offline and no credentials. Seven native tests, fmt, strict all-feature/workspace
Clippy, native control and actual unknown-target build pass. All135 typed native/
WASM JSON/error strings are exact. Four raw JS integer seams remain separate.
The shared compiled target was reused; installed toolchains were not bundled.
The rebuilt module has a different hash/size from the original; both are retained
with exact identities. This proves behavior/input independence, not byte-level
reproducibility. This first replay predates the tracked restoration helper/capsule;
a separate exact committed-source helper replay remains required.

The first hosted foundation run failed before Rust validation because latest
Ubuntu26.04 does not support pinned Playwright1.58.2. Pinning Ubuntu24.04 produced
a successful hosted run42055540998 at e244406. The new pipeline verifies/restores
tracked inputs into a new Cargo home, builds offline and executes the135 native/
WASM controls before browser tests. Its result is pending.

The source capsule is not yet copied into Pages; its4.83MB size alone would exceed
the current5MB site budget when added to the existing site. Complete source ZIP,
receiver/manifest proof, explicit download-budget review/layout, full worker
lifecycle, Windows hosted source replay, downloaded artifacts and default/main/
live delivery remain open. This checkpoint does not qualify a release.

## Archive identity correction

Subsequent full-blob validation caught273 ordinary text files converted by
Windows `git archive` inheriting `core.autocrlf=true`. Earlier replay archives
therefore prove behavior from converted checkout text, not exact Git-blob export.
Original archives/results are retained. A new command-scoped conversion-disabled
archive matches every source blob before build, but initially rejected the
capsule lock identity: that first manifest had captured checkout CRLF rather than
canonical Git LF bytes. The corrected verifier binds canonical LF SHA plus Git
blob and permits only CRLF-to-LF checkout conversion. Tests cover both LF/CRLF and
reject changed lock content. Root Cargo.lock and pins are unchanged. The corrected
capsule SHA is `c27c7321b2fc45991db6e464cc100b9b64b3bdf5ac570bc2caebf34b2d8be97c`.
The first exact-blob archive stopped before build, and its failure is retained.
Corrected committed-source/helper replay and hosted result remain pending.
