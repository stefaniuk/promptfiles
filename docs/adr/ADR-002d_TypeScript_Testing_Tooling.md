# ADR-002d: TypeScript testing tooling 🧾

> |              |                                                 |
> | ------------ | ----------------------------------------------- |
> | Date         | `2026-02-08` when the decision was last updated |
> | Status       | `Accepted`                                      |
> | Significance | `Quality attributes`                            |

---

- [ADR-002d: TypeScript testing tooling 🧾](#adr-002d-typescript-testing-tooling-)
  - [Context 🧭](#context-)
  - [Decision ✅](#decision-)
    - [Assumptions 🧩](#assumptions-)
    - [Drivers 🎯](#drivers-)
    - [Options 🔀](#options-)
      - [Option A: Vitest (Selected) ✅](#option-a-vitest-selected-)
      - [Option B: Jest](#option-b-jest)
      - [Option C: Mocha + Chai](#option-c-mocha--chai)
      - [Option D: AVA](#option-d-ava)
      - [Option E: node test](#option-e-node-test)
    - [Outcome 🏁](#outcome-)
    - [Rationale 🧠](#rationale-)
  - [Consequences ⚖️](#consequences-️)
  - [Compliance 📏](#compliance-)
  - [Notes 🔗](#notes-)
  - [Actions ✅](#actions-)
  - [Tags 🏷️](#tags-️)

## Context 🧭

The TypeScript tech stack needs a fast, modern test runner with good TypeScript support and CI integration.

## Decision ✅

### Assumptions 🧩

- Node.js 24.13.0 (LTS) is the baseline runtime.
- TypeScript 5.9 is the baseline language version.
- Unit tests must run quickly in CI and locally.

### Drivers 🎯

- TypeScript support and speed
- Good assertion and mocking support
- CI stability and coverage tooling
- Developer experience and readability
- Active maintenance

### Options 🔀

#### Option A: Vitest (Selected) ✅

Use [`Vitest`](https://github.com/vitest-dev/vitest) for TypeScript-first testing.

| Criteria           | Score/Notes                        |
| ------------------ | ---------------------------------- |
| TypeScript support | ⭐⭐⭐ First-class and fast        |
| Performance        | ⭐⭐⭐ Fast with Vite engine       |
| Ecosystem support  | ⭐⭐⭐ Active and growing          |
| CI integration     | ⭐⭐⭐ Good coverage and reporters |
| Ease of use        | ⭐⭐⭐ Modern API                  |
| Effort             | S                                  |

#### Option B: Jest

Use [`Jest`](https://github.com/jestjs/jest) for testing.

| Criteria           | Score/Notes                        |
| ------------------ | ---------------------------------- |
| TypeScript support | ⭐⭐ Requires ts-jest or swc       |
| Performance        | ⭐⭐ Slower on larger suites       |
| Ecosystem support  | ⭐⭐⭐ Mature and stable           |
| CI integration     | ⭐⭐⭐ Good coverage and reporters |
| Ease of use        | ⭐⭐⭐ Familiar API                |
| Effort             | M                                  |

**Why not chosen**: Solid but slower and more setup for TypeScript.

#### Option C: Mocha + Chai

Use [`Mocha`](https://github.com/mochajs/mocha) with [`Chai`](https://github.com/chaijs/chai).

| Criteria           | Score/Notes                        |
| ------------------ | ---------------------------------- |
| TypeScript support | ⭐⭐ Needs ts-node or build step   |
| Performance        | ⭐⭐ Reasonable                    |
| Ecosystem support  | ⭐⭐ Mature but more manual setup  |
| CI integration     | ⭐⭐ Requires extra tooling        |
| Ease of use        | ⭐⭐ Flexible but more boilerplate |
| Effort             | M                                  |

**Why not chosen**: More manual setup than Vitest.

#### Option D: AVA

Use [`AVA`](https://github.com/avajs/ava) for concurrent tests.

| Criteria           | Score/Notes                |
| ------------------ | -------------------------- |
| TypeScript support | ⭐⭐ Good but needs config |
| Performance        | ⭐⭐⭐ Very fast           |
| Ecosystem support  | ⭐⭐ Smaller ecosystem     |
| CI integration     | ⭐⭐ Reasonable            |
| Ease of use        | ⭐⭐ Different API         |
| Effort             | M                          |

**Why not chosen**: Smaller ecosystem and different patterns than most teams expect.

#### Option E: node test

Use the built-in [`node:test`](https://github.com/nodejs/node) runner.

| Criteria           | Score/Notes                     |
| ------------------ | ------------------------------- |
| TypeScript support | ⭐⭐ Requires transpile step    |
| Performance        | ⭐⭐⭐ Fast                     |
| Ecosystem support  | ⭐⭐ Growing, but fewer plugins |
| CI integration     | ⭐⭐ Basic support              |
| Ease of use        | ⭐⭐ Minimal API                |
| Effort             | M                               |

**Why not chosen**: Smaller ecosystem and fewer conveniences than Vitest.

### Outcome 🏁

Adopt `Vitest` as the default testing framework. This decision is reversible if a better standard emerges.

### Rationale 🧠

Vitest is fast, TypeScript-friendly, and integrates well with modern build tooling, giving the best developer experience for this repo.

## Consequences ⚖️

- TypeScript tests should use Vitest by default.
- Other test runners require explicit justification.

## Compliance 📏

- `pnpm vitest run` succeeds in CI.

## Notes 🔗

- Tech Radar: `./Tech_Radar.md`

## Actions ✅

- [x] Copilot, 2026-02-08, record the testing decision

## Tags 🏷️

`#testability #quality #maintainability`
