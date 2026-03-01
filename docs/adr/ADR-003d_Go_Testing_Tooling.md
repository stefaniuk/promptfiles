# ADR-003d: Go testing tooling 🧾

> |              |                                                 |
> | ------------ | ----------------------------------------------- |
> | Date         | `2026-02-28` when the decision was last updated |
> | Status       | `Accepted`                                      |
> | Significance | `Quality attributes`                            |

---

- [ADR-003d: Go testing tooling 🧾](#adr-003d-go-testing-tooling-)
  - [Context 🧭](#context-)
  - [Decision ✅](#decision-)
    - [Assumptions 🧩](#assumptions-)
    - [Drivers 🎯](#drivers-)
    - [Options 🔀](#options-)
      - [Option A: go test (testing package) (Selected) ✅](#option-a-go-test-testing-package-selected-)
      - [Option B: testify](#option-b-testify)
      - [Option C: ginkgo + gomega](#option-c-ginkgo--gomega)
      - [Option D: go-convey](#option-d-go-convey)
      - [Option E: gocheck](#option-e-gocheck)
    - [Outcome 🏁](#outcome-)
    - [Rationale 🧠](#rationale-)
    - [Property-based testing tooling 🔬](#property-based-testing-tooling-)
  - [Consequences ⚖️](#consequences-️)
  - [Compliance 📏](#compliance-)
  - [Notes 🔗](#notes-)
  - [Actions ✅](#actions-)
  - [Tags 🏷️](#tags-️)

## Context 🧭

The Go tech stack needs a default testing approach that is stable, fast, and widely understood. The user asked for an ADR that compares at least five options and selects the best for the Tech Radar.

## Decision ✅

### Assumptions 🧩

- Go 1.25.7 is the baseline toolchain.
- Tests should integrate with standard Go tooling and CI.
- Additional assertion libraries can be added later if justified.

### Drivers 🎯

- Standard tooling and low barrier to entry
- Fast execution and clear output
- Compatibility with CI and coverage tooling
- Long-term maintenance and community adoption
- Minimal dependencies for the default stack

### Options 🔀

#### Option A: go test (testing package) (Selected) ✅

Use the standard [`testing`](https://github.com/golang/go) package and [`go test`](https://github.com/golang/go) runner.

| Criteria          | Score/Notes                            |
| ----------------- | -------------------------------------- |
| Standard tooling  | ⭐⭐⭐ Built into Go                   |
| Performance       | ⭐⭐⭐ Fast and parallel by default    |
| Ecosystem support | ⭐⭐⭐ Works with coverage and tooling |
| Dependencies      | ⭐⭐⭐ None                            |
| Effort            | S                                      |

#### Option B: testify

Use [`testify`](https://github.com/stretchr/testify) for richer assertions and suites.

| Criteria          | Score/Notes               |
| ----------------- | ------------------------- |
| Standard tooling  | ⭐⭐ Extra dependency     |
| Performance       | ⭐⭐ Slight overhead      |
| Ecosystem support | ⭐⭐⭐ Popular and stable |
| Dependencies      | ⭐⭐ Adds a library       |
| Effort            | S                         |

**Why not chosen**: Helpful for assertions but not necessary as the default baseline.

#### Option C: ginkgo + gomega

Use BDD style testing with [`ginkgo`](https://github.com/onsi/ginkgo) and [`gomega`](https://github.com/onsi/gomega).

| Criteria          | Score/Notes                |
| ----------------- | -------------------------- |
| Standard tooling  | ⭐ Low, separate runner    |
| Performance       | ⭐⭐ Good but extra layers |
| Ecosystem support | ⭐⭐ Active but niche      |
| Dependencies      | ⭐ Low, multiple libraries |
| Effort            | M                          |

**Why not chosen**: Adds cognitive overhead and a non-standard test runner.

#### Option D: go-convey

Use [`go-convey`](https://github.com/smartystreets/goconvey) for a web-based test runner and BDD style assertions.

| Criteria          | Score/Notes             |
| ----------------- | ----------------------- |
| Standard tooling  | ⭐ Low, extra runner    |
| Performance       | ⭐⭐ Acceptable         |
| Ecosystem support | ⭐⭐ Active but smaller |
| Dependencies      | ⭐ Low, extra tooling   |
| Effort            | M                       |

**Why not chosen**: Adds a workflow that is not the Go default.

#### Option E: gocheck

Use [`gocheck`](https://github.com/go-check/check) for the gocheck testing framework.

| Criteria          | Score/Notes                |
| ----------------- | -------------------------- |
| Standard tooling  | ⭐ Low, separate framework |
| Performance       | ⭐⭐ Acceptable            |
| Ecosystem support | ⭐ Low, older project      |
| Dependencies      | ⭐ Low, extra framework    |
| Effort            | M                          |

**Why not chosen**: Older framework with lower adoption and extra dependency cost.

### Outcome 🏁

Adopt `go test` and the standard `testing` package as the default testing approach. Optional assertion libraries can be added if a module demonstrates clear need. This decision is reversible if a stronger Go standard emerges.

### Rationale 🧠

The standard testing toolchain is fast, stable, and universally understood. It keeps dependencies minimal and works with coverage and CI tooling out of the box.

### Property-based testing tooling 🔬

For Go in 2026, we should prefer a modern PBT library that complements native fuzzing rather than replacing it.

| Tool                                              | Score/Notes                                                                                                     |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| [rapid](https://github.com/flyingmutant/rapid)    | ⭐⭐⭐ Strong PBT ergonomics (generators, shrinking, stateful tests), plus `MakeFuzz` bridge to native fuzzing. |
| [testing/quick](https://pkg.go.dev/testing/quick) | ⭐⭐ Stable and dependency-free, but explicitly frozen and limited for complex PBT workflows.                   |
| [gopter](https://github.com/leanovate/gopter)     | ⭐⭐ Capable and mature, but heavier API and slower momentum than newer options.                                |
| [go-check](https://github.com/steffnova/go-check) | ⭐ Clear property model, but lower adoption and weaker ecosystem signal.                                        |
| [gofuzz](https://github.com/google/gofuzz)        | ⭐ Useful random-data generator, but not a full PBT framework and now archived.                                 |

**Recommended choice**: `rapid` as the default PBT companion to `go test`, with native Go fuzzing kept alongside it for coverage-guided exploration.

## Consequences ⚖️

- Tests should be written using the `testing` package by default.
- Property-based tests should use `rapid` with `go test`.
- Any additional framework must be justified by a specific need.

## Compliance 📏

- `go test ./...` succeeds in CI.

## Notes 🔗

- Tech Radar: `./Tech_Radar.md`

## Actions ✅

- [x] Copilot, 2026-02-08, update Tech Radar with the Go stack selection
- [x] Copilot, 2026-02-28, add the PBT tooling comparison and recommendation

## Tags 🏷️

`#testability #quality #maintainability`
