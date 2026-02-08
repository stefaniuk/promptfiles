# ADR-004d: Rust testing tooling 🧾

> |              |                                                 |
> | ------------ | ----------------------------------------------- |
> | Date         | `2026-02-08` when the decision was last updated |
> | Status       | `Accepted`                                      |
> | Significance | `Quality attributes`                            |

---

- [ADR-004d: Rust testing tooling 🧾](#adr-004d-rust-testing-tooling-)
  - [Context 🧭](#context-)
  - [Decision ✅](#decision-)
    - [Assumptions 🧩](#assumptions-)
    - [Drivers 🎯](#drivers-)
    - [Options 🔀](#options-)
      - [Option A: cargo test (Selected) ✅](#option-a-cargo-test-selected-)
      - [Option B: nextest](#option-b-nextest)
      - [Option C: rstest](#option-c-rstest)
      - [Option D: proptest](#option-d-proptest)
      - [Option E: criterion](#option-e-criterion)
    - [Outcome 🏁](#outcome-)
    - [Rationale 🧠](#rationale-)
  - [Consequences ⚖️](#consequences-️)
  - [Compliance 📏](#compliance-)
  - [Notes 🔗](#notes-)
  - [Actions ✅](#actions-)
  - [Tags 🏷️](#tags-️)

## Context 🧭

The Rust tech stack needs a default testing approach that is fast, stable, and aligned with the standard toolchain.

## Decision ✅

### Assumptions 🧩

- Rust 1.93.0 is the baseline toolchain.
- Tests must run deterministically in CI.
- Additional test styles may be introduced when required.

### Drivers 🎯

- Standard tooling and low friction
- Speed for local and CI runs
- Good diagnostics and reporting
- Ecosystem adoption
- Long-term maintenance

### Options 🔀

#### Option A: cargo test (Selected) ✅

Use the built-in test harness via `cargo test`.

| Criteria         | Score/Notes                         |
| ---------------- | ----------------------------------- |
| Standard tooling | ⭐⭐⭐ Built into Rust              |
| Performance      | ⭐⭐⭐ Fast and parallel by default |
| Diagnostics      | ⭐⭐⭐ Clear and familiar           |
| Ecosystem        | ⭐⭐⭐ Universal                    |
| Effort           | S                                   |

#### Option B: nextest

Use [`nextest`](https://github.com/nextest-rs/nextest) as an alternative test runner.

| Criteria         | Score/Notes                    |
| ---------------- | ------------------------------ |
| Standard tooling | ⭐⭐ External runner           |
| Performance      | ⭐⭐⭐ Very fast with reuse    |
| Diagnostics      | ⭐⭐ Good but different output |
| Ecosystem        | ⭐⭐ Growing adoption          |
| Effort           | M                              |

**Why not chosen**: Great performance but adds a separate runner for the baseline.

#### Option C: rstest

Use [`rstest`](https://github.com/la10736/rstest) for fixture-driven tests.

| Criteria         | Score/Notes              |
| ---------------- | ------------------------ |
| Standard tooling | ⭐⭐ External crate      |
| Performance      | ⭐⭐ Good                |
| Diagnostics      | ⭐⭐ Good with fixtures  |
| Ecosystem        | ⭐⭐ Popular but smaller |
| Effort           | M                        |

**Why not chosen**: Useful add-on but not necessary for the baseline.

#### Option D: proptest

Use [`proptest`](https://github.com/proptest-rs/proptest) for property-based testing.

| Criteria         | Score/Notes                        |
| ---------------- | ---------------------------------- |
| Standard tooling | ⭐⭐ External crate                |
| Performance      | ⭐⭐ Can be slower for large cases |
| Diagnostics      | ⭐⭐ Good for shrinking failures   |
| Ecosystem        | ⭐⭐ Common for property testing   |
| Effort           | M                                  |

**Why not chosen**: Excellent for specific cases but not the default test runner.

#### Option E: criterion

Use [`criterion`](https://github.com/bheisler/criterion.rs) for benchmarking.

| Criteria         | Score/Notes                   |
| ---------------- | ----------------------------- |
| Standard tooling | ⭐⭐ External crate           |
| Performance      | ⭐⭐ Focused on benchmarks    |
| Diagnostics      | ⭐⭐ Strong benchmark reports |
| Ecosystem        | ⭐⭐ Common for perf testing  |
| Effort           | M                             |

**Why not chosen**: Benchmarking tool, not a primary test framework.

### Outcome 🏁

Adopt `cargo test` as the default testing approach. This decision is reversible if a new standard emerges.

### Rationale 🧠

The built-in test harness is fast, stable, and universally supported across the Rust ecosystem.

## Consequences ⚖️

- Tests should use Rust's standard test harness by default.
- Alternative runners require explicit justification.

## Compliance 📏

- `cargo test` succeeds in CI.

## Notes 🔗

- Tech Radar: `./Tech_Radar.md`

## Actions ✅

- [x] Copilot, 2026-02-08, record the testing decision

## Tags 🏷️

`#testability #quality #maintainability`
