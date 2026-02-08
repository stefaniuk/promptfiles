# ADR-004a: Rust dependency management 🧾

> |              |                                                 |
> | ------------ | ----------------------------------------------- |
> | Date         | `2026-02-08` when the decision was last updated |
> | Status       | `Accepted`                                      |
> | Significance | `Dependencies, Delivery & build`                |

---

- [ADR-004a: Rust dependency management 🧾](#adr-004a-rust-dependency-management-)
  - [Context 🧭](#context-)
  - [Decision ✅](#decision-)
    - [Assumptions 🧩](#assumptions-)
    - [Drivers 🎯](#drivers-)
    - [Options 🔀](#options-)
      - [Option A: Cargo (Selected) ✅](#option-a-cargo-selected-)
      - [Option B: Bazel + rules_rust](#option-b-bazel--rules_rust)
      - [Option C: Buck2](#option-c-buck2)
      - [Option D: Pants](#option-d-pants)
      - [Option E: Nix](#option-e-nix)
    - [Outcome 🏁](#outcome-)
    - [Rationale 🧠](#rationale-)
  - [Consequences ⚖️](#consequences-️)
  - [Compliance 📏](#compliance-)
  - [Notes 🔗](#notes-)
  - [Actions ✅](#actions-)
  - [Tags 🏷️](#tags-️)

## Context 🧭

The Rust tech stack needs a default dependency manager and build workflow that aligns with the Rust toolchain and supports reproducible builds.

## Decision ✅

### Assumptions 🧩

- Rust 1.93.0 is the baseline toolchain.
- `Cargo.lock` is required for deterministic builds in applications.
- Standard Rust workflows are preferred over bespoke build systems.

### Drivers 🎯

- Alignment with Rust ecosystem conventions
- Deterministic builds and lock file support
- Developer productivity and tooling support
- Low operational complexity
- Long-term maintenance and stability

### Options 🔀

#### Option A: Cargo (Selected) ✅

Use [`Cargo`](https://github.com/rust-lang/cargo) with `Cargo.toml` and `Cargo.lock`.

| Criteria                | Score/Notes                          |
| ----------------------- | ------------------------------------ |
| Toolchain alignment     | ⭐⭐⭐ Canonical Rust tool           |
| Reproducibility         | ⭐⭐⭐ `Cargo.lock` for applications |
| Ecosystem compatibility | ⭐⭐⭐ Works with all Rust tooling   |
| Operational complexity  | ⭐⭐ Low, standard workflow          |
| Effort                  | S                                    |

#### Option B: Bazel + rules_rust

Use [`Bazel`](https://github.com/bazelbuild/bazel) with [`rules_rust`](https://github.com/bazelbuild/rules_rust).

| Criteria                | Score/Notes                            |
| ----------------------- | -------------------------------------- |
| Toolchain alignment     | ⭐⭐ Strong, but non-standard workflow |
| Reproducibility         | ⭐⭐⭐ Hermetic builds                 |
| Ecosystem compatibility | ⭐⭐ Extra integration work            |
| Operational complexity  | ⭐ Low, higher build system overhead   |
| Effort                  | L to XL                                |

**Why not chosen**: High complexity for the baseline stack.

#### Option C: Buck2

Use [`Buck2`](https://github.com/facebook/buck2) for builds and dependency management.

| Criteria                | Score/Notes                                    |
| ----------------------- | ---------------------------------------------- |
| Toolchain alignment     | ⭐⭐ Works, but not standard for Rust          |
| Reproducibility         | ⭐⭐⭐ Strong caching and deterministic builds |
| Ecosystem compatibility | ⭐⭐ Extra integration work                    |
| Operational complexity  | ⭐ Low, higher system complexity               |
| Effort                  | L                                              |

**Why not chosen**: Adds a non-standard build system for limited benefit.

#### Option D: Pants

Use [`Pants`](https://github.com/pantsbuild/pants) for multi-language builds.

| Criteria                | Score/Notes                          |
| ----------------------- | ------------------------------------ |
| Toolchain alignment     | ⭐ Low, not Rust-native              |
| Reproducibility         | ⭐⭐ Good but requires setup         |
| Ecosystem compatibility | ⭐ Low, smaller Rust community usage |
| Operational complexity  | ⭐ Low, higher tooling overhead      |
| Effort                  | L                                    |

**Why not chosen**: Not a Rust-first solution.

#### Option E: Nix

Use [`Nix`](https://github.com/NixOS/nix) for reproducible builds and dependency management.

| Criteria                | Score/Notes                            |
| ----------------------- | -------------------------------------- |
| Toolchain alignment     | ⭐⭐ Works alongside Cargo             |
| Reproducibility         | ⭐⭐⭐ Strong, system-wide determinism |
| Ecosystem compatibility | ⭐⭐ Requires Nix expertise            |
| Operational complexity  | ⭐ Low, steeper learning curve         |
| Effort                  | M to L                                 |

**Why not chosen**: Strong determinism but adds a separate toolchain.

### Outcome 🏁

Adopt Cargo as the default Rust dependency manager. This decision is reversible if a different build system becomes a hard requirement.

### Rationale 🧠

Cargo is the canonical tool for Rust and integrates with the full ecosystem, providing the most predictable and lowest-friction workflow.

## Consequences ⚖️

- Rust projects must include `Cargo.toml` and `Cargo.lock`.
- Alternative build systems require explicit justification.

## Compliance 📏

- `cargo build` succeeds in CI.
- `cargo update -p` only updates dependencies when explicitly requested.

## Notes 🔗

- Tech Radar: `./Tech_Radar.md`
- Rust downloads: <https://www.rust-lang.org/tools/install>l>

## Actions ✅

- [x] Copilot, 2026-02-08, record the dependency management decision

## Tags 🏷️

`#dependencies #build #reproducibility #maintainability`
