# ADR-003c: Go static analysis and type checking 🧾

> |              |                                                 |
> | ------------ | ----------------------------------------------- |
> | Date         | `2026-02-08` when the decision was last updated |
> | Status       | `Accepted`                                      |
> | Significance | `Quality attributes`                            |

---

- [ADR-003c: Go static analysis and type checking 🧾](#adr-003c-go-static-analysis-and-type-checking-)
  - [Context 🧭](#context-)
  - [Decision ✅](#decision-)
    - [Assumptions 🧩](#assumptions-)
    - [Drivers 🎯](#drivers-)
    - [Options 🔀](#options-)
      - [Option A: staticcheck (Selected) ✅](#option-a-staticcheck-selected-)
      - [Option B: go vet](#option-b-go-vet)
      - [Option C: golangci-lint (type checks only)](#option-c-golangci-lint-type-checks-only)
      - [Option D: errcheck](#option-d-errcheck)
      - [Option E: nilaway](#option-e-nilaway)
    - [Outcome 🏁](#outcome-)
    - [Rationale 🧠](#rationale-)
  - [Consequences ⚖️](#consequences-️)
  - [Compliance 📏](#compliance-)
  - [Notes 🔗](#notes-)
  - [Actions ✅](#actions-)
  - [Tags 🏷️](#tags-️)

## Context 🧭

Go has compile-time type checking, but the tech stack still needs a default static analysis tool to catch deeper issues. The user asked for an ADR comparing at least five alternatives and selecting the best option for this category.

## Decision ✅

### Assumptions 🧩

- Go 1.25.7 is the baseline toolchain.
- The compiler already enforces type correctness for builds.
- A static analysis tool should add meaningful value with low noise.

### Drivers 🎯

- Early detection of correctness issues beyond the compiler
- Low false positive rate
- Fast enough for CI and local use
- Active maintenance and community trust
- Simple integration with standard workflows

### Options 🔀

#### Option A: staticcheck (Selected) ✅

Use [`staticcheck`](https://github.com/dominikh/go-tools) for deep static analysis and extra type correctness checks.

| Criteria        | Score/Notes                     |
| --------------- | ------------------------------- |
| Issue detection | ⭐⭐⭐ Broad, high-value checks |
| Signal to noise | ⭐⭐ Generally strong, tunable  |
| Performance     | ⭐⭐ Acceptable for CI          |
| Maintenance     | ⭐⭐⭐ Active and widely used   |
| Effort          | S                               |

#### Option B: go vet

Use the Go standard library [`go vet`](https://github.com/golang/go) tool.

| Criteria        | Score/Notes                    |
| --------------- | ------------------------------ |
| Issue detection | ⭐⭐ Useful but narrower scope |
| Signal to noise | ⭐⭐ Good default checks       |
| Performance     | ⭐⭐⭐ Fast                    |
| Maintenance     | ⭐⭐⭐ Standard Go tool        |
| Effort          | S                              |

**Why not chosen**: Useful but narrower than `staticcheck` and often overlapped by other linting.

#### Option C: golangci-lint (type checks only)

Use the type-related linters inside [`golangci-lint`](https://github.com/golangci/golangci-lint) without the full suite.

| Criteria        | Score/Notes                      |
| --------------- | -------------------------------- |
| Issue detection | ⭐⭐ Depends on selected linters |
| Signal to noise | ⭐⭐ Configurable but mixed      |
| Performance     | ⭐⭐ Acceptable with tuning      |
| Maintenance     | ⭐⭐ Active, but more config     |
| Effort          | M                                |

**Why not chosen**: Adds config complexity and overlaps with the linting decision.

#### Option D: errcheck

Use [`errcheck`](https://github.com/kisielk/errcheck) to find unchecked error returns.

| Criteria        | Score/Notes                       |
| --------------- | --------------------------------- |
| Issue detection | ⭐⭐ Focused, useful for a subset |
| Signal to noise | ⭐⭐ Good but narrow scope        |
| Performance     | ⭐⭐⭐ Fast                       |
| Maintenance     | ⭐⭐ Active but narrow focus      |
| Effort          | S                                 |

**Why not chosen**: Too narrow to be the main static analysis tool.

#### Option E: nilaway

Use [`nilaway`](https://github.com/uber-go/nilaway) to detect potential nil dereferences.

| Criteria        | Score/Notes                         |
| --------------- | ----------------------------------- |
| Issue detection | ⭐⭐ Helpful but specialised        |
| Signal to noise | ⭐⭐ Can be noisy in some codebases |
| Performance     | ⭐ Low on larger projects           |
| Maintenance     | ⭐⭐ Active but niche               |
| Effort          | M                                   |

**Why not chosen**: Specialised analysis, better as an optional add-on.

### Outcome 🏁

Adopt `staticcheck` as the default static analysis tool for the Go tech stack. The compiler remains the primary type checker, and `staticcheck` adds higher-value analysis. This decision is reversible if it becomes unmaintained or loses ecosystem trust.

### Rationale 🧠

`staticcheck` provides broad and high-signal checks that go beyond the compiler. It is widely adopted, stable, and complements the linting decision without replacing it.

## Consequences ⚖️

- CI should run `staticcheck` for Go modules.
- Developers will need to handle issues that the compiler alone does not catch.

## Compliance 📏

- `staticcheck ./...` succeeds in CI.

## Notes 🔗

- Tech Radar: `./Tech_Radar.md`

## Actions ✅

- [x] Copilot, 2026-02-08, update Tech Radar with the Go stack selection

## Tags 🏷️

`#quality #correctness #maintainability`
