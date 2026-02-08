# ADR-001f: Python CLI argument parsing 🧾

> |              |                                                 |
> | ------------ | ----------------------------------------------- |
> | Date         | `2026-02-08` when the decision was last updated |
> | Status       | `Accepted`                                      |
> | Significance | `Interfaces & contracts`                        |

---

- [ADR-001f: Python CLI argument parsing 🧾](#adr-001f-python-cli-argument-parsing-)
  - [Context 🧭](#context-)
  - [Decision ✅](#decision-)
    - [Assumptions 🧩](#assumptions-)
    - [Drivers 🎯](#drivers-)
    - [Options 🔀](#options-)
      - [Option A: Typer (Selected) ✅](#option-a-typer-selected-)
      - [Option B: Click](#option-b-click)
      - [Option C: argparse (standard library)](#option-c-argparse-standard-library)
      - [Option D: docopt](#option-d-docopt)
      - [Option E: Fire](#option-e-fire)
    - [Outcome 🏁](#outcome-)
    - [Rationale 🧠](#rationale-)
  - [Consequences ⚖️](#consequences-️)
  - [Compliance 📏](#compliance-)
  - [Notes 🔗](#notes-)
  - [Actions ✅](#actions-)
  - [Tags 🏷️](#tags-️)

## Context 🧭

Python tools need a standard CLI framework that supports subcommands, clear help output, and type-safe argument handling.

## Decision ✅

### Assumptions 🧩

- Python 3.14.3 is the baseline runtime.
- CLIs must provide predictable help output and exit codes.
- Type hints should be used for CLI arguments.

### Drivers 🎯

- Subcommand support and help output quality
- Type hint integration
- Developer productivity and clarity
- Ecosystem adoption and maintenance
- Reasonable dependency footprint

### Options 🔀

#### Option A: Typer (Selected) ✅

Use [`Typer`](https://github.com/tiangolo/typer) for type-hinted CLI parsing.

| Criteria         | Score/Notes                      |
| ---------------- | -------------------------------- |
| Features         | ⭐⭐⭐ Subcommands and rich help |
| Type integration | ⭐⭐⭐ Built around type hints   |
| Ease of use      | ⭐⭐⭐ Simple, Pythonic API      |
| Maintenance      | ⭐⭐⭐ Active and widely used    |
| Dependencies     | ⭐⭐ Depends on Click            |
| Effort           | S                                |

#### Option B: Click

Use [`Click`](https://github.com/pallets/click) for decorator-based CLI parsing.

| Criteria         | Score/Notes                      |
| ---------------- | -------------------------------- |
| Features         | ⭐⭐⭐ Strong subcommand support |
| Type integration | ⭐⭐ Some typing support         |
| Ease of use      | ⭐⭐ More boilerplate than Typer |
| Maintenance      | ⭐⭐⭐ Mature and stable         |
| Dependencies     | ⭐⭐ External dependency         |
| Effort           | M                                |

**Why not chosen**: Typer provides better type-driven ergonomics with less boilerplate.

#### Option C: argparse (standard library)

Use the standard [`argparse`](https://github.com/python/cpython) module.

| Criteria         | Score/Notes                  |
| ---------------- | ---------------------------- |
| Features         | ⭐⭐ Subcommands supported   |
| Type integration | ⭐ Low, manual conversions   |
| Ease of use      | ⭐⭐ Verbose for larger CLIs |
| Maintenance      | ⭐⭐⭐ Standard library      |
| Dependencies     | ⭐⭐⭐ None                  |
| Effort           | M                            |

**Why not chosen**: More verbose and less ergonomic for type-rich CLIs.

#### Option D: docopt

Use [`docopt`](https://github.com/docopt/docopt) for docstring-driven parsing.

| Criteria         | Score/Notes                         |
| ---------------- | ----------------------------------- |
| Features         | ⭐⭐ Simple but less structured     |
| Type integration | ⭐ Low, manual conversions          |
| Ease of use      | ⭐⭐ Depends on docstring precision |
| Maintenance      | ⭐⭐ Maintained but less common     |
| Dependencies     | ⭐⭐ External dependency            |
| Effort           | M                                   |

**Why not chosen**: Less structured than Typer and harder to maintain as CLIs grow.

#### Option E: Fire

Use [`Fire`](https://github.com/google/python-fire) for automatic CLI generation.

| Criteria         | Score/Notes                        |
| ---------------- | ---------------------------------- |
| Features         | ⭐⭐ Quick to start                |
| Type integration | ⭐ Low, dynamic                    |
| Ease of use      | ⭐⭐ Magic-heavy and less explicit |
| Maintenance      | ⭐⭐ Maintained but niche          |
| Dependencies     | ⭐⭐ External dependency           |
| Effort           | M                                  |

**Why not chosen**: Too implicit for stable, user-facing CLIs.

### Outcome 🏁

Adopt `Typer` as the default CLI argument parsing library. This decision is reversible if CLI needs change or a stronger standard emerges.

### Rationale 🧠

Typer offers a modern, type-hint-friendly API with clear help output and strong subcommand support, while keeping developer effort low.

## Consequences ⚖️

- New CLIs should use Typer by default.
- Alternatives require explicit justification.

## Compliance 📏

- CLI entrypoints use Typer and include `--help` output.

## Notes 🔗

- Tech Radar: `./Tech_Radar.md`

## Actions ✅

- [x] Copilot, 2026-02-08, record the CLI parsing decision

## Tags 🏷️

`#usability #interfaces #maintainability`
