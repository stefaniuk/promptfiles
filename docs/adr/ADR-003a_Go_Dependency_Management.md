# ADR-003a: Go dependency management 🧾

> |              |                                                 |
> | ------------ | ----------------------------------------------- |
> | Date         | `2026-02-08` when the decision was last updated |
> | Status       | `Accepted`                                      |
> | Significance | `Dependencies, Delivery & build`                |

---

- [ADR-003a: Go dependency management 🧾](#adr-003a-go-dependency-management-)
  - [Context 🧭](#context-)
  - [Decision ✅](#decision-)
    - [Assumptions 🧩](#assumptions-)
    - [Drivers 🎯](#drivers-)
    - [Options 🔀](#options-)
      - [Option A: Go modules (go mod) (Selected) ✅](#option-a-go-modules-go-mod-selected-)
      - [Option B: dep (deprecated)](#option-b-dep-deprecated)
      - [Option C: Glide (deprecated)](#option-c-glide-deprecated)
      - [Option D: govendor](#option-d-govendor)
      - [Option E: Bazel with rules_go](#option-e-bazel-with-rules_go)
    - [Outcome 🏁](#outcome-)
    - [Rationale 🧠](#rationale-)
  - [Consequences ⚖️](#consequences-️)
  - [Compliance 📏](#compliance-)
  - [Notes 🔗](#notes-)
  - [Actions ✅](#actions-)
  - [Tags 🏷️](#tags-️)

## Context 🧭

The user asked for a Go tech stack entry in the Tech Radar. Each category must have an ADR comparing at least five alternatives and selecting the best option. The Go toolchain has a standard dependency workflow and the decision should align with Go 1.25.7 (latest stable on 2026-02-08) and with low-maintenance, reproducible builds.

## Decision ✅

### Assumptions 🧩

- Go 1.25.7 is the baseline toolchain.
- The repository should rely on standard Go tooling where possible.
- Reproducible builds and secure dependency verification are required.

### Drivers 🎯

- Alignment with the official Go toolchain and ecosystem
- Reproducible builds with locked dependency versions
- Security and integrity checks for dependencies
- Low maintenance and low operational complexity
- Good editor and CI support

### Options 🔀

#### Option A: Go modules (go mod) (Selected) ✅

Use [`go mod`](https://github.com/golang/go) with `go.mod` and `go.sum`, optionally with `go mod vendor` for offline builds.

| Criteria                | Score/Notes                                              |
| ----------------------- | -------------------------------------------------------- |
| Toolchain alignment     | ⭐⭐⭐ Default and supported by Go                       |
| Ecosystem compatibility | ⭐⭐⭐ Widely supported by tools and editors             |
| Reproducibility         | ⭐⭐⭐ `go.sum` provides checksums                       |
| Operational complexity  | ⭐⭐ Low, but needs proxy configuration in some networks |
| Effort                  | S                                                        |

#### Option B: dep (deprecated)

Use [`dep`](https://github.com/golang/dep) (deprecated), a legacy dependency manager no longer maintained.

| Criteria                | Score/Notes                           |
| ----------------------- | ------------------------------------- |
| Toolchain alignment     | ⭐ Low, not supported by modern Go    |
| Ecosystem compatibility | ⭐ Low, many tools assume modules     |
| Reproducibility         | ⭐⭐ Works but ecosystem is shrinking |
| Operational complexity  | ⭐⭐ Extra tooling and migration risk |
| Effort                  | M                                     |

**Why not chosen**: Deprecated and conflicts with the current Go ecosystem.

#### Option C: Glide (deprecated)

Use [`Glide`](https://github.com/Masterminds/glide) (deprecated), a legacy vendoring tool for pre-modules workflows.

| Criteria                | Score/Notes                         |
| ----------------------- | ----------------------------------- |
| Toolchain alignment     | ⭐ Low, no longer standard          |
| Ecosystem compatibility | ⭐ Low, unsupported by most tooling |
| Reproducibility         | ⭐⭐ Relies on vendor directory     |
| Operational complexity  | ⭐⭐ Requires manual upkeep         |
| Effort                  | M                                   |

**Why not chosen**: Deprecated and incompatible with modern module-aware tooling.

#### Option D: govendor

Use [`govendor`](https://github.com/kardianos/govendor), a vendoring tool with a manifest file.

| Criteria                | Score/Notes                               |
| ----------------------- | ----------------------------------------- |
| Toolchain alignment     | ⭐ Low, not the default                   |
| Ecosystem compatibility | ⭐⭐ Limited tooling support              |
| Reproducibility         | ⭐⭐ Vendor directory works but is manual |
| Operational complexity  | ⭐⭐ Extra tool and workflows             |
| Effort                  | M                                         |

**Why not chosen**: Adds process overhead without benefits over modules.

#### Option E: Bazel with rules_go

Use [`Bazel`](https://github.com/bazelbuild/bazel) with [`rules_go`](https://github.com/bazelbuild/rules_go) for dependency and build management.

| Criteria                | Score/Notes                                            |
| ----------------------- | ------------------------------------------------------ |
| Toolchain alignment     | ⭐⭐ Integrates but diverges from default Go workflows |
| Ecosystem compatibility | ⭐⭐ Requires Bazel knowledge and config               |
| Reproducibility         | ⭐⭐⭐ Strong hermetic builds                          |
| Operational complexity  | ⭐ Low, higher build system complexity                 |
| Effort                  | L to XL                                                |

**Why not chosen**: Too heavy for the baseline tech stack and increases maintenance cost.

### Outcome 🏁

Adopt Go modules (`go mod`) as the default dependency management approach. Vendoring via `go mod vendor` is allowed only when offline or regulated build environments require it. This decision is reversible, but only if Go changes the default workflow or a build system requirement emerges.

### Rationale 🧠

Go modules are the official and most widely supported approach. They deliver strong reproducibility via `go.sum`, work with standard tooling, and keep the workflow simple. The alternatives are either deprecated, too niche, or impose unnecessary operational burden.

## Consequences ⚖️

- The repository must include `go.mod` and `go.sum`.
- Teams should configure module proxy settings where required.
- Migration from legacy tooling may be required if older Go projects are added.

## Compliance 📏

- `go.mod` and `go.sum` exist in any Go module.
- `go mod tidy` produces no changes.
- `go mod verify` succeeds in CI.

## Notes 🔗

- Tech Radar: `./Tech_Radar.md`
- Go downloads: <https://go.dev/dl/>

## Actions ✅

- [x] Copilot, 2026-02-08, update Tech Radar with the Go stack selection

## Tags 🏷️

`#dependencies #build #maintainability #reproducibility`
