# Worker lifecycle and submitted-result export checkpoint

Qualified source `ef39ce6d09c4080c40c2d6467964b2f8f0dd100e` preserves original Rust/core/catalog/manifests/
lock/grants and existing two-draft/three-scale reader task. Worker init/evaluation
remain actual Rust WASM. The worker echoes generation/request metadata; main
controller fences old instances, generations, request IDs and duplicate replies.
Boot and computation each have15-second deadlines. Cancel, timeout, error and
edits during active work actually terminate the Worker. Retry creates a new
instance with retained current assumptions. During boot, controls stay editable;
reset preserves original defaults. Results/exports clear immediately on edits.

Completed results carry the actual submitted input snapshot; downloads use that
snapshot, original complete result and source revision. A silent DOM edit cannot
relabel old results. Sharing uses current assumptions and stays separate from
evaluator progress. Invalid shared values retain original default behavior with
an explicit ignored-value message; original numeric bounds/math remain unchanged.
Rust errors, module/constructor failures, runtime crashes and unreadable messages
clear results and provide retry. Source/notices remain independent of the engine.

All43 browser cases pass without skips/flakes. Each viewport drives all120
original native outcomes through actual UI/worker and downloads/verifies every
JSON:240 retained files plus their hash inventory. Native keyboard input and
share/reload match the exact submitted floating-point values. Boot/compute
deadlines, actual termination/cancel/retry, edits/reset, old callbacks, wrong
generations/IDs, duplicate/unknown/malformed messages, Rust error/crash/module/
constructor failure, invalid queries and stale-export prevention are exercised.
Controlled transport faults are simulated in actual browser Workers; separate
real-worker/native cases prove original Rust outcomes. Six desktop/mobile own-
input/failure/source screenshots were inspected. No new funding or catalog claim.

First35pass/2failure observations are retained. The actual Chromium probe found
no `onmessageerror` handler property: assignment was inert while an event
listener fired. Registration via addEventListener fixed it; a corrected37-case
run passed, then Rust-error/crash/invalid-query cases extended the suite to43.
Neither timeout, checks nor original outputs were weakened to obtain the pass.

Receiver review gaps are closed with18 passing source/receiver controls on
checkout and archive. Explicit and default compiled-target overlap are rejected;
unlisted build/config inputs (including .cargo/config.toml) are rejected before
archive build. Documented generated caches remain allowed. Original safe-path,
Git-tree/mode/commit, corruption, junction and non-overwrite controls remain.

The receiver-restored source builds offline from its own verified capsule/new
input tree and Cargo home. All32 external manifest paths are in that independent
input tree; owner registry/Git caches are unused. Seven native tests, fmt, strict
Clippy,135 typed native/WASM pairs,30 original CLI outputs/exits and3 generated
files match. Source ZIPs are identical across checkout/archive; module bytes
differ and are recorded. Shared compiled target reuse/installed prerequisites
are explicit. Runtime1164240 bytes; optional downloads7311493;
total8475733, within reviewed separate budgets.

Hosted current-source worker/receiver/artifact validation is pending after push.
Windows/Linux hosted archive replay, final role review/default/main/live delivery
and separate TRACKER snapshot remain open. This is not a release/portfolio close.
