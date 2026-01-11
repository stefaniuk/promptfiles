---
applyTo: "**/*.rs"
---

# Rust Engineering Instructions 🦀

These instructions define **Rust-specific engineering patterns** beyond what the Rust Book, compiler, and Clippy already enforce.

They must remain applicable to:

- CLI applications and system tools
- Web services and APIs (Actix, Axum, Rocket)
- Libraries and shared crates
- Async applications (Tokio, async-std)
- Embedded and systems programming
- WebAssembly and Tauri backends

This file does **not** restate Rust fundamentals (ownership, borrowing, `Result`, `Option`, `?` operator). Those are assumed knowledge. It covers **decision criteria, thresholds, and patterns** that require human judgement.

They are **non-negotiable** unless an exception is explicitly documented (with rationale and expiry) in an ADR/decision record.

**Identifier scheme.** Every normative rule carries a unique tag in the form `[RS-<prefix>-NNN]`, where the prefix maps to the containing section (for example `QR` for Quick Reference, `DEC` for Decisions, `ASY` for Async, `API` for API Design). Use these identifiers when referencing, planning, or validating requirements.

---

## 0. Quick reference (apply first) 🧠

This section exists so humans and AI assistants can reliably apply the most important rules even when context is tight.

- [RS-QR-001] **Function size**: split functions exceeding ~50 lines or 3 levels of nesting ([RS-STR-001]).
- [RS-QR-002] **Clone acceptance**: `clone()` is acceptable for small `Copy`-like types, startup paths, or when profiler shows no impact ([RS-DEC-003]).
- [RS-QR-003] **No blocking in async**: never call blocking IO or hold locks across `.await` ([RS-ASY-001], [RS-ASY-003]).
- [RS-QR-004] **Cancellation safety**: document whether async functions are cancellation-safe ([RS-ASY-005]).
- [RS-QR-005] **Error types**: libraries return typed errors; binaries may use `anyhow` ([RS-ERR-001]).
- [RS-QR-006] **Unsafe review**: all `unsafe` blocks require a `// SAFETY:` comment and dedicated review ([RS-SAF-001]).
- [RS-QR-007] **No warnings in CI**: `#![deny(warnings)]` or equivalent in CI; fix, don't suppress ([RS-QG-001]).
- [RS-QR-008] **Feature flag hygiene**: test with `--no-default-features` and `--all-features` ([RS-ORG-004]).

---

## 1. Decision criteria 🎯

### 1.1 When to use `Arc` vs `Rc`

| Scenario                               | Choice                              |
| -------------------------------------- | ----------------------------------- |
| Single-threaded, no `Send` requirement | `Rc<T>`                             |
| Shared across threads or async tasks   | `Arc<T>`                            |
| Shared + mutable, single-threaded      | `Rc<RefCell<T>>`                    |
| Shared + mutable, multi-threaded       | `Arc<Mutex<T>>` or `Arc<RwLock<T>>` |

- [RS-DEC-001] Default to the **simplest** option; escalate only when the scenario requires it.

### 1.2 When to use `Box<dyn Trait>` vs generics

| Scenario                                                   | Choice                                 |
| ---------------------------------------------------------- | -------------------------------------- |
| Known at compile time, performance-critical                | Generics (`impl Trait` / `<T: Trait>`) |
| Heterogeneous collection (mixed concrete types)            | `Box<dyn Trait>`                       |
| Plugin/extensibility boundary (dynamic dispatch required)  | `Box<dyn Trait>`                       |
| Binary size is a concern (generics cause monomorphisation) | `Box<dyn Trait>`                       |

- [RS-DEC-002] Prefer generics unless one of the dynamic-dispatch scenarios applies.

### 1.3 When `clone()` is acceptable

- [RS-DEC-003] `clone()` is acceptable when:
  - The type is small and `Copy`-like (for example `PathBuf` with short paths, small `String`s < 64 bytes)
  - It occurs on a cold path (startup, configuration loading)
  - Profiling shows no measurable impact
  - Borrowing would require complex lifetime annotations that harm readability
- [RS-DEC-004] `clone()` is **not** acceptable in hot loops or when the clone is large (> 1 KB) without justification.

### 1.4 When to split crates

- [RS-DEC-005] Split into separate crates when:
  - Compile times exceed ~60 seconds for incremental builds
  - A clear domain boundary exists (for example `myapp-core`, `myapp-cli`, `myapp-server`)
  - A subset is intended for external consumption (library vs binary)
- [RS-DEC-006] Do **not** split prematurely; a well-organised single crate is preferable to many tiny crates with circular dependencies.

---

## 2. Code structure 🏗️

- [RS-STR-001] Split functions exceeding **~50 lines** or **3 levels of nesting**; extract helpers with descriptive names.
- [RS-STR-002] Keep modules focused on a single domain concept; aim for < 500 lines per module (excluding tests).
- [RS-STR-003] Place `mod tests` at the **bottom** of the file; integration tests go in `tests/`.
- [RS-STR-004] Keep `main.rs` or `lib.rs` minimal (< 50 lines); delegate to modules.
- [RS-STR-005] Order items: `use` → `mod` → types → traits → impls → functions → tests.

---

## 3. Async patterns ⚡

### 3.1 Blocking and runtime hygiene

- [RS-ASY-001] **Never** call blocking IO (`std::fs`, `std::net`, blocking HTTP clients) inside async functions; use async equivalents or `spawn_blocking`.
- [RS-ASY-002] **Never** call `.block_on()` from within an async context; it causes deadlocks.
- [RS-ASY-003] **Never** hold a `Mutex` or `RwLock` guard across an `.await` point; use `tokio::sync` primitives or restructure.

### 3.2 Cancellation safety

- [RS-ASY-004] Assume any `.await` can be cancelled (dropped); design accordingly.
- [RS-ASY-005] Document cancellation safety in rustdoc for public async functions that have side effects.
- [RS-ASY-006] Use `tokio::select!` with cancellation tokens for cooperative shutdown.

### 3.3 Backpressure and resource limits

- [RS-ASY-007] Bound channels and queues; unbounded channels are a memory leak waiting to happen.
- [RS-ASY-008] Apply timeouts to all outbound IO (`tokio::time::timeout`); never wait indefinitely.
- [RS-ASY-009] Limit concurrent tasks with semaphores or task pools; uncontrolled spawning exhausts resources.

### 3.4 Runtime choice (guidance, not mandate)

- [RS-ASY-010] For most server/CLI workloads, **Tokio** is the default choice (ecosystem, maturity).
- [RS-ASY-011] Document runtime requirements in `Cargo.toml` and README; do not assume a runtime in library crates.

---

## 4. Error handling ⚠️

- [RS-ERR-001] **Libraries**: define typed errors (prefer `thiserror` for ergonomics); expose `Result<T, MyError>`.
- [RS-ERR-002] **Binaries**: may use `anyhow` or `eyre` for convenience; convert at boundaries.
- [RS-ERR-003] Provide **context** when propagating errors: `.context("loading config")` or custom error variants.
- [RS-ERR-004] Error messages must be **user-safe** (no internal paths, no secrets); include structured context for logs.
- [RS-ERR-005] Validate arguments early; return `Result` rather than panicking on bad input.

---

## 5. Unsafe code 🔓

- [RS-SAF-001] Every `unsafe` block must have a `// SAFETY:` comment immediately above, explaining why invariants are upheld.
- [RS-SAF-002] `unsafe` code requires **dedicated review** by a second engineer or explicit sign-off in PR.
- [RS-SAF-003] Prefer safe abstractions from crates (`bytemuck`, `zerocopy`, `pin-project`) over hand-rolled unsafe.
- [RS-SAF-004] Test unsafe code with Miri (`cargo +nightly miri test`) where feasible.
- [RS-SAF-005] Document **all** safety invariants that callers must uphold for `unsafe fn`.

---

## 6. API design 📐

### 6.1 Trait implementation

- [RS-API-001] Implement `Debug` on **all** public types; derive where possible.
- [RS-API-002] Implement `Clone`, `PartialEq`, `Eq`, `Hash`, `Default` **only** when semantically meaningful; do not derive blindly.
- [RS-API-003] Implement `Send` and `Sync` only if the type is genuinely safe to share; rely on auto-impl.

### 6.2 Type safety

- [RS-API-004] Use **newtypes** to distinguish domain concepts (for example `UserId(u64)` vs raw `u64`).
- [RS-API-005] Avoid `bool` parameters; use enums (for example `Overwrite::Yes` vs `overwrite: bool`).
- [RS-API-006] Accept `impl AsRef<Path>` or `&str` where flexibility is needed; return owned types.

### 6.3 Future-proofing

- [RS-API-007] Struct fields should be **private** with accessors; use `#[non_exhaustive]` for enums/structs exposed publicly.
- [RS-API-008] Use sealed traits when downstream implementations are not intended.
- [RS-API-009] Validate arguments at public API boundaries; internal functions may assume valid input.

---

## 7. Testing 🧪

- [RS-TST-001] Unit tests go in `mod tests` within the same file; integration tests go in `tests/`.
- [RS-TST-002] Test **behaviour**, not implementation; avoid testing private functions directly.
- [RS-TST-003] Use `#[should_panic]` sparingly; prefer `Result`-returning tests with `?`.
- [RS-TST-004] For async tests, use `#[tokio::test]` (or equivalent); do not mix runtimes.
- [RS-TST-005] Mock external services at the boundary (trait objects, channels); avoid compile-time feature-gated test doubles in production code.
- [RS-TST-006] Aim for **80%+ line coverage** of public API; 100% is not a goal.

---

## 8. Quality gates ✅

- [RS-QG-001] CI must fail on warnings: use `RUSTFLAGS="-D warnings"` or `#![deny(warnings)]` in CI builds.
- [RS-QG-002] Run `cargo fmt --check` and `cargo clippy -- -D warnings` before merge.
- [RS-QG-003] Run `cargo test` with default features, `--no-default-features`, and `--all-features`.
- [RS-QG-004] Run `cargo doc --no-deps` to catch documentation errors.
- [RS-QG-005] Run `cargo audit` in CI; fail on known vulnerabilities above threshold.

---

## 9. Project organisation 📁

- [RS-ORG-001] Use semantic versioning; follow [Cargo SemVer compatibility](https://doc.rust-lang.org/cargo/reference/semver.html).
- [RS-ORG-002] Include metadata in `Cargo.toml`: `description`, `license`, `repository`, `keywords`, `categories`.
- [RS-ORG-003] Use **feature flags** for optional functionality; document each feature in `Cargo.toml` and README.
- [RS-ORG-004] Test feature flag combinations: `--no-default-features`, `--all-features`, and critical subsets.
- [RS-ORG-005] Pin dependency versions for binaries (`Cargo.lock` committed); allow ranges for libraries.

---

## 10. Anti-patterns ❌

- [RS-ANT-001] **Do not** ignore warnings; fix or explicitly allow with a comment explaining why.
- [RS-ANT-002] **Do not** use `unwrap()` or `expect()` in library code; use `?` or return `Result`.
- [RS-ANT-003] **Do not** use `unwrap()` in production binary code except in proven-unreachable paths with a comment.
- [RS-ANT-004] **Do not** hold locks across `.await` points.
- [RS-ANT-005] **Do not** call blocking IO in async functions.
- [RS-ANT-006] **Do not** use unbounded channels in production.
- [RS-ANT-007] **Do not** clone large types (> 1 KB) in hot paths without profiler justification.
- [RS-ANT-008] **Do not** use `unsafe` without a `// SAFETY:` comment and review.
- [RS-ANT-009] **Do not** derive `Default` on types where a zero/empty value is semantically invalid.
- [RS-ANT-010] **Do not** expose `pub` fields on structs intended for evolution; use accessors.

---

## 11. Quality checklist ✅

Before shipping Rust code, verify:

- [RS-CHK-001] Functions are ≤ ~50 lines with ≤ 3 levels of nesting
- [RS-CHK-002] All `unsafe` blocks have `// SAFETY:` comments
- [RS-CHK-003] No blocking IO or lock-holding across `.await`
- [RS-CHK-004] Async functions document cancellation safety where relevant
- [RS-CHK-005] Errors are typed (libraries) or contextual (binaries)
- [RS-CHK-006] Public types implement `Debug`; other traits only when meaningful
- [RS-CHK-007] Feature flags are tested in combination
- [RS-CHK-008] No `unwrap()` in library code; justified only in binaries
- [RS-CHK-009] No anti-patterns from §10 are present
- [RS-CHK-010] Code passes `cargo fmt`, `cargo clippy`, `cargo test`, `cargo doc`

---

> **Version**: 2.0.0
> **Last Amended**: 2026-01-11
