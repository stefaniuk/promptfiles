# ADR-004f: Rust CLI argument parsing 🧾

> |              |                                                 |
> | ------------ | ----------------------------------------------- |
> | Date         | `2026-02-08` when the decision was last updated |
> | Status       | `Accepted`                                      |
> | Significance | `Interfaces & contracts`                        |

---

- [ADR-004f: Rust CLI argument parsing 🧾](#adr-004f-rust-cli-argument-parsing-)
  - [Context 🧭](#context-)
  - [Decision ✅](#decision-)
    - [Assumptions 🧩](#assumptions-)
    - [Drivers 🎯](#drivers-)
    - [Options 🔀](#options-)
      - [Option A: clap (Selected) ✅](#option-a-clap-selected-)
      - [Option B: structopt (deprecated)](#option-b-structopt-deprecated)
      - [Option C: argh](#option-c-argh)
      - [Option D: docopt](#option-d-docopt)
      - [Option E: pico-args](#option-e-pico-args)
    - [Outcome 🏁](#outcome-)
    - [Rationale 🧠](#rationale-)
  - [Consequences ⚖️](#consequences-️)
  - [Compliance 📏](#compliance-)
  - [Notes 🔗](#notes-)
  - [Actions ✅](#actions-)
  - [Tags 🏷️](#tags-️)

## Context 🧭

Rust tools need a CLI parsing library that supports subcommands, clear help output, and a stable API.

## Decision ✅

### Assumptions 🧩

- Rust 1.93.0 is the baseline toolchain.
- CLIs should provide consistent `--help` output and exit codes.
- Derive-based parsing is preferred for readability.

### Drivers 🎯

- Subcommand support and help output quality
- Type-safe parsing and derive ergonomics
- Ecosystem adoption and maintenance
- Reasonable dependency footprint
- Ease of onboarding

### Options 🔀

#### Option A: clap (Selected) ✅

Use [`clap`](https://github.com/clap-rs/clap) for CLI parsing.

| Criteria     | Score/Notes                            |
| ------------ | -------------------------------------- |
| Features     | ⭐⭐⭐ Rich subcommands and help       |
| Type safety  | ⭐⭐⭐ Derive macros and strong typing |
| Ease of use  | ⭐⭐⭐ Widely documented               |
| Maintenance  | ⭐⭐⭐ Active and popular              |
| Dependencies | ⭐⭐ External dependency               |
| Effort       | S                                      |

#### Option B: structopt (deprecated)

Use [`structopt`](https://github.com/TeXitoi/structopt).

| Criteria     | Score/Notes              |
| ------------ | ------------------------ |
| Features     | ⭐⭐ Good but deprecated |
| Type safety  | ⭐⭐⭐ Derive macros     |
| Ease of use  | ⭐⭐ Similar to clap     |
| Maintenance  | ⭐ Low, deprecated       |
| Dependencies | ⭐⭐ External dependency |
| Effort       | M                        |

**Why not chosen**: Deprecated in favour of clap.

#### Option C: argh

Use [`argh`](https://github.com/google/argh) for lightweight parsing.

| Criteria     | Score/Notes                       |
| ------------ | --------------------------------- |
| Features     | ⭐⭐ Good for simpler CLIs        |
| Type safety  | ⭐⭐⭐ Derive-based               |
| Ease of use  | ⭐⭐ Smaller feature set          |
| Maintenance  | ⭐⭐ Active but smaller ecosystem |
| Dependencies | ⭐⭐ External dependency          |
| Effort       | M                                 |

**Why not chosen**: Less feature-complete than clap for complex CLIs.

#### Option D: docopt

Use [`docopt`](https://github.com/docopt/docopt.rs) for docstring-driven parsing.

| Criteria     | Score/Notes                        |
| ------------ | ---------------------------------- |
| Features     | ⭐⭐ Flexible but less structured  |
| Type safety  | ⭐ Low, runtime parsing            |
| Ease of use  | ⭐⭐ Depends on docstring accuracy |
| Maintenance  | ⭐⭐ Maintained but less common    |
| Dependencies | ⭐⭐ External dependency           |
| Effort       | M                                  |

**Why not chosen**: Less type-safe and harder to maintain as CLIs grow.

#### Option E: pico-args

Use [`pico-args`](https://github.com/RazrFalcon/pico-args) for minimal parsing.

| Criteria     | Score/Notes                 |
| ------------ | --------------------------- |
| Features     | ⭐ Low, minimal feature set |
| Type safety  | ⭐ Low, manual parsing      |
| Ease of use  | ⭐⭐ Simple for small tools |
| Maintenance  | ⭐⭐ Active                 |
| Dependencies | ⭐⭐⭐ Very small footprint |
| Effort       | M                           |

**Why not chosen**: Too minimal for general CLI needs.

### Outcome 🏁

Adopt `clap` as the default CLI argument parsing library. This decision is reversible if a better standard emerges.

### Rationale 🧠

Clap provides strong derive-based ergonomics, robust help output, and wide adoption, making it the safest default.

## Consequences ⚖️

- Rust CLIs should use clap by default.
- Alternative libraries require explicit justification.

## Compliance 📏

- CLI entrypoints use clap and include `--help` output.

## Notes 🔗

- Tech Radar: `./Tech_Radar.md`

## Actions ✅

- [x] Copilot, 2026-02-08, record the CLI parsing decision

## Tags 🏷️

`#usability #interfaces #maintainability`
