# ADR-004b: Rust linting and formatting 🧾

> |              |                                                 |
> | ------------ | ----------------------------------------------- |
> | Date         | `2026-02-08` when the decision was last updated |
> | Status       | `Accepted`                                      |
> | Significance | `Quality attributes, Delivery & build`          |

---

- [ADR-004b: Rust linting and formatting 🧾](#adr-004b-rust-linting-and-formatting-)
  - [Context 🧭](#context-)
  - [Decision ✅](#decision-)
    - [Assumptions 🧩](#assumptions-)
    - [Drivers 🎯](#drivers-)
    - [Options 🔀](#options-)
      - [Option A: rustfmt + clippy (Selected) ✅](#option-a-rustfmt--clippy-selected-)
      - [Option B: rustfmt only](#option-b-rustfmt-only)
      - [Option C: clippy only](#option-c-clippy-only)
      - [Option D: rustfmt + clippy (pedantic by default)](#option-d-rustfmt--clippy-pedantic-by-default)
      - [Option E: dprint + clippy](#option-e-dprint--clippy)
    - [Outcome 🏁](#outcome-)
    - [Rationale 🧠](#rationale-)
  - [Consequences ⚖️](#consequences-️)
  - [Compliance 📏](#compliance-)
  - [Notes 🔗](#notes-)
  - [Actions ✅](#actions-)
  - [Tags 🏷️](#tags-️)

## Context 🧭

The Rust tech stack needs a standard linting and formatting workflow that is consistent, fast, and aligned with community conventions.

## Decision ✅

### Assumptions 🧩

- Rust 1.93.0 is the baseline toolchain.
- Formatting should be deterministic and standard.
- Linting should provide meaningful correctness checks with manageable noise.

### Drivers 🎯

- Canonical formatting and community alignment
- High-signal linting
- Fast CI and local execution
- Low configuration overhead
- Active maintenance

### Options 🔀

#### Option A: rustfmt + clippy (Selected) ✅

Use [`rustfmt`](https://github.com/rust-lang/rustfmt) for formatting and [`clippy`](https://github.com/rust-lang/rust-clippy) for linting.

| Criteria               | Score/Notes                        |
| ---------------------- | ---------------------------------- |
| Formatting consistency | ⭐⭐⭐ rustfmt is standard         |
| Lint coverage          | ⭐⭐⭐ Clippy provides rich checks |
| Performance            | ⭐⭐ Fast enough for CI            |
| Configuration overhead | ⭐⭐ Minimal with defaults         |
| Maintenance            | ⭐⭐⭐ Official Rust tools         |
| Effort                 | S                                  |

#### Option B: rustfmt only

Use [`rustfmt`](https://github.com/rust-lang/rustfmt) without linting.

| Criteria               | Score/Notes                |
| ---------------------- | -------------------------- |
| Formatting consistency | ⭐⭐⭐ rustfmt is standard |
| Lint coverage          | ⭐ None                    |
| Performance            | ⭐⭐⭐ Fast                |
| Configuration overhead | ⭐⭐⭐ Minimal             |
| Maintenance            | ⭐⭐⭐ Official tool       |
| Effort                 | S                          |

**Why not chosen**: Misses important correctness and quality checks.

#### Option C: clippy only

Use [`clippy`](https://github.com/rust-lang/rust-clippy) without formatting.

| Criteria               | Score/Notes          |
| ---------------------- | -------------------- |
| Formatting consistency | ⭐ None              |
| Lint coverage          | ⭐⭐⭐ Rich checks   |
| Performance            | ⭐⭐ Fast enough     |
| Configuration overhead | ⭐⭐ Minimal         |
| Maintenance            | ⭐⭐⭐ Official tool |
| Effort                 | S                    |

**Why not chosen**: Formatting consistency is required for readability.

#### Option D: rustfmt + clippy (pedantic by default)

Use [`rustfmt`](https://github.com/rust-lang/rustfmt) with Clippy configured for `clippy::pedantic` by default.

| Criteria               | Score/Notes                |
| ---------------------- | -------------------------- |
| Formatting consistency | ⭐⭐⭐ rustfmt is standard |
| Lint coverage          | ⭐⭐⭐ Very strict         |
| Performance            | ⭐⭐ Similar to Option A   |
| Configuration overhead | ⭐ Low, more tuning needed |
| Maintenance            | ⭐⭐⭐ Official tools      |
| Effort                 | M                          |

**Why not chosen**: Too strict for the baseline, likely to produce noise.

#### Option E: dprint + clippy

Use [`dprint`](https://github.com/dprint/dprint) for formatting with Clippy for linting.

| Criteria               | Score/Notes                        |
| ---------------------- | ---------------------------------- |
| Formatting consistency | ⭐⭐ Not Rust standard             |
| Lint coverage          | ⭐⭐⭐ Clippy provides rich checks |
| Performance            | ⭐⭐ Fast                          |
| Configuration overhead | ⭐⭐ Additional tool configuration |
| Maintenance            | ⭐⭐ Active but smaller ecosystem  |
| Effort                 | M                                  |

**Why not chosen**: Adds a non-standard formatter with limited upside.

### Outcome 🏁

Adopt rustfmt for formatting and Clippy for linting. This decision is reversible if community standards change.

### Rationale 🧠

Rustfmt and Clippy are official tools, widely supported, and give a strong balance of consistency and correctness with minimal overhead.

## Consequences ⚖️

- CI should run `cargo fmt --check` and `cargo clippy`.
- Additional linters require explicit justification.

## Compliance 📏

- `cargo fmt --check` produces no changes.
- `cargo clippy --all-targets --all-features -D warnings` succeeds.

## Notes 🔗

- Tech Radar: `./Tech_Radar.md`

## Actions ✅

- [x] Copilot, 2026-02-08, record the linting and formatting decision

## Tags 🏷️

`#quality #consistency #maintainability`
