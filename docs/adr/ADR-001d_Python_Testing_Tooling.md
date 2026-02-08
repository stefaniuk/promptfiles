# ADR-001d: Python testing tooling 🧾

> |              |                                                 |
> | ------------ | ----------------------------------------------- |
> | Date         | `2026-02-08` when the decision was last updated |
> | Status       | `Accepted`                                      |
> | Significance | `Quality attributes`                            |

---

- [ADR-001d: Python testing tooling 🧾](#adr-001d-python-testing-tooling-)
  - [Context 🧭](#context-)
  - [Decision ✅](#decision-)
    - [Assumptions 🧩](#assumptions-)
    - [Drivers 🎯](#drivers-)
    - [Options 🔀](#options-)
      - [Option A: pytest (Selected) ✅](#option-a-pytest-selected-)
      - [Option B: unittest (standard library)](#option-b-unittest-standard-library)
      - [Option C: nose2](#option-c-nose2)
      - [Option D: behave](#option-d-behave)
      - [Option E: Robot Framework](#option-e-robot-framework)
    - [Outcome 🏁](#outcome-)
    - [Rationale 🧠](#rationale-)
  - [Consequences ⚖️](#consequences-️)
  - [Compliance 📏](#compliance-)
  - [Notes 🔗](#notes-)
  - [Actions ✅](#actions-)
  - [Tags 🏷️](#tags-️)

## Context 🧭

The Python tech stack needs a default test framework that is fast, expressive, and widely adopted, with good plugin support for CI.

## Decision ✅

### Assumptions 🧩

- Python 3.14.3 is the baseline runtime.
- Tests must be deterministic and quick for local runs.
- Integration and end-to-end tiers may be added later.

### Drivers 🎯

- Developer productivity and readability
- Plugin ecosystem and CI integrations
- Speed and reliability
- Low onboarding overhead
- Long-term maintenance

### Options 🔀

#### Option A: pytest (Selected) ✅

Use [`pytest`](https://github.com/pytest-dev/pytest) as the primary test framework.

| Criteria           | Score/Notes                         |
| ------------------ | ----------------------------------- |
| Expressiveness     | ⭐⭐⭐ Rich fixtures and assertions |
| Ecosystem support  | ⭐⭐⭐ Large plugin ecosystem       |
| Performance        | ⭐⭐ Fast and parallelisable        |
| Ease of onboarding | ⭐⭐⭐ Simple and familiar          |
| Maintenance        | ⭐⭐⭐ Active and stable            |
| Effort             | S                                   |

#### Option B: unittest (standard library)

Use the standard [`unittest`](https://github.com/python/cpython) framework.

| Criteria           | Score/Notes                         |
| ------------------ | ----------------------------------- |
| Expressiveness     | ⭐⭐ Works but more verbose         |
| Ecosystem support  | ⭐⭐ Smaller plugin ecosystem       |
| Performance        | ⭐⭐ Reasonable                     |
| Ease of onboarding | ⭐⭐ Familiar but boilerplate-heavy |
| Maintenance        | ⭐⭐⭐ Standard library             |
| Effort             | S                                   |

**Why not chosen**: More boilerplate and less flexibility for fixtures and plugins.

#### Option C: nose2

Use [`nose2`](https://github.com/nose-devs/nose2) as a test runner.

| Criteria           | Score/Notes               |
| ------------------ | ------------------------- |
| Expressiveness     | ⭐⭐ Reasonable           |
| Ecosystem support  | ⭐ Low, small ecosystem   |
| Performance        | ⭐⭐ Acceptable           |
| Ease of onboarding | ⭐⭐ Simple               |
| Maintenance        | ⭐⭐ Maintained but niche |
| Effort             | M                         |

**Why not chosen**: Smaller ecosystem and lower adoption.

#### Option D: behave

Use [`behave`](https://github.com/behave/behave) for BDD-style tests.

| Criteria           | Score/Notes                  |
| ------------------ | ---------------------------- |
| Expressiveness     | ⭐⭐ Good for BDD            |
| Ecosystem support  | ⭐⭐ Active but smaller      |
| Performance        | ⭐ Low for large suites      |
| Ease of onboarding | ⭐⭐ Requires BDD discipline |
| Maintenance        | ⭐⭐ Maintained              |
| Effort             | M                            |

**Why not chosen**: BDD style adds overhead for the baseline stack.

#### Option E: Robot Framework

Use [`Robot Framework`](https://github.com/robotframework/robotframework) for keyword-driven testing.

| Criteria           | Score/Notes                        |
| ------------------ | ---------------------------------- |
| Expressiveness     | ⭐⭐ Good for acceptance testing   |
| Ecosystem support  | ⭐⭐ Active but separate ecosystem |
| Performance        | ⭐ Low for large suites            |
| Ease of onboarding | ⭐ Low for Python-first teams      |
| Maintenance        | ⭐⭐ Maintained                    |
| Effort             | M                                  |

**Why not chosen**: A different workflow with higher onboarding costs.

### Outcome 🏁

Adopt `pytest` as the default testing framework. This decision is reversible if a stronger standard emerges.

### Rationale 🧠

`pytest` offers the best mix of expressiveness, plugin support, and performance. It is the most widely adopted option for modern Python projects.

## Consequences ⚖️

- Tests should be written using `pytest` by default.
- Other frameworks require explicit justification.

## Compliance 📏

- `uv run pytest` succeeds in CI.

## Notes 🔗

- Tech Radar: `./Tech_Radar.md`

## Actions ✅

- [x] Copilot, 2026-02-08, record the testing decision

## Tags 🏷️

`#testability #quality #maintainability`
