# ADR-002b: TypeScript linting and formatting 🧾

> |              |                                                 |
> | ------------ | ----------------------------------------------- |
> | Date         | `2026-02-08` when the decision was last updated |
> | Status       | `Accepted`                                      |
> | Significance | `Quality attributes, Delivery & build`          |

---

- [ADR-002b: TypeScript linting and formatting 🧾](#adr-002b-typescript-linting-and-formatting-)
  - [Context 🧭](#context-)
  - [Decision ✅](#decision-)
    - [Assumptions 🧩](#assumptions-)
    - [Drivers 🎯](#drivers-)
    - [Options 🔀](#options-)
      - [Option A: Biome (Selected) ✅](#option-a-biome-selected-)
      - [Option B: ESLint + Prettier + typescript-eslint](#option-b-eslint--prettier--typescript-eslint)
      - [Option C: ESLint + Prettier + XO](#option-c-eslint--prettier--xo)
      - [Option D: StandardJS](#option-d-standardjs)
      - [Option E: Rome (deprecated)](#option-e-rome-deprecated)
    - [Outcome 🏁](#outcome-)
    - [Rationale 🧠](#rationale-)
  - [Consequences ⚖️](#consequences-️)
  - [Compliance 📏](#compliance-)
  - [Notes 🔗](#notes-)
  - [Actions ✅](#actions-)
  - [Tags 🏷️](#tags-️)

## Context 🧭

The TypeScript tech stack needs a fast, consistent linting and formatting setup with minimal configuration overhead and good editor support.

## Decision ✅

### Assumptions 🧩

- Node.js 24.13.0 (LTS) is the baseline runtime.
- TypeScript 5.9 is the baseline language version.
- Formatting must be deterministic and automated.

### Drivers 🎯

- One-tool workflow where possible
- Fast lint and format cycles
- Deterministic output
- High signal diagnostics
- Active maintenance and ecosystem support

### Options 🔀

#### Option A: Biome (Selected) ✅

Use [`Biome`](https://github.com/biomejs/biome) for linting and formatting.

| Criteria               | Score/Notes                    |
| ---------------------- | ------------------------------ |
| Formatting consistency | ⭐⭐⭐ Built-in formatter      |
| Lint coverage          | ⭐⭐⭐ Broad rules in one tool |
| Performance            | ⭐⭐⭐ Very fast               |
| Config overhead        | ⭐⭐ Simple config             |
| Ecosystem support      | ⭐⭐⭐ Strong and growing      |
| Effort                 | S                              |

#### Option B: ESLint + Prettier + typescript-eslint

Use [`ESLint`](https://github.com/eslint/eslint), [`Prettier`](https://github.com/prettier/prettier), and [`typescript-eslint`](https://github.com/typescript-eslint/typescript-eslint).

| Criteria               | Score/Notes                      |
| ---------------------- | -------------------------------- |
| Formatting consistency | ⭐⭐⭐ Prettier is stable        |
| Lint coverage          | ⭐⭐⭐ Strong with plugins       |
| Performance            | ⭐⭐ Multiple tools add overhead |
| Config overhead        | ⭐⭐ Several configs to manage   |
| Ecosystem support      | ⭐⭐⭐ Very strong               |
| Effort                 | M                                |

**Why not chosen**: Strong but slower and more complex than a single-tool workflow.

#### Option C: ESLint + Prettier + XO

Use [`ESLint`](https://github.com/eslint/eslint), [`Prettier`](https://github.com/prettier/prettier), and [`XO`](https://github.com/xojs/xo).

| Criteria               | Score/Notes                              |
| ---------------------- | ---------------------------------------- |
| Formatting consistency | ⭐⭐⭐ Prettier is stable                |
| Lint coverage          | ⭐⭐ Opinionated defaults                |
| Performance            | ⭐⭐ Multiple tools add overhead         |
| Config overhead        | ⭐⭐ XO reduces config but still layered |
| Ecosystem support      | ⭐⭐ Smaller ecosystem                   |
| Effort                 | M                                        |

**Why not chosen**: More opinionated than needed and still multi-tool.

#### Option D: StandardJS

Use [`StandardJS`](https://github.com/standard/standard) for linting and formatting.

| Criteria               | Score/Notes                      |
| ---------------------- | -------------------------------- |
| Formatting consistency | ⭐⭐ StandardJS formatting style |
| Lint coverage          | ⭐⭐ Good but less flexible      |
| Performance            | ⭐⭐ Reasonable                  |
| Config overhead        | ⭐⭐⭐ Minimal                   |
| Ecosystem support      | ⭐⭐ Moderate                    |
| Effort                 | M                                |

**Why not chosen**: Less flexible and not as strong for TypeScript-specific rules.

#### Option E: Rome (deprecated)

Use [`Rome`](https://github.com/rome/tools) for linting and formatting.

| Criteria               | Score/Notes              |
| ---------------------- | ------------------------ |
| Formatting consistency | ⭐⭐ Good but deprecated |
| Lint coverage          | ⭐⭐ Reasonable          |
| Performance            | ⭐⭐ Fast                |
| Config overhead        | ⭐⭐ Moderate            |
| Ecosystem support      | ⭐ Low, project archived |
| Effort                 | M                        |

**Why not chosen**: Deprecated in favour of Biome.

### Outcome 🏁

Adopt `Biome` for linting and formatting. This decision is reversible if a more suitable toolchain becomes the standard.

### Rationale 🧠

Biome delivers fast linting and formatting with a single configuration, keeping the workflow simple and consistent.

## Consequences ⚖️

- Projects should configure Biome in `package.json` or `biome.json`.
- Additional lint tools require explicit justification.

## Compliance 📏

- `pnpm biome format --write .` produces no changes.
- `pnpm biome lint .` succeeds in CI.

## Notes 🔗

- Tech Radar: `./Tech_Radar.md`

## Actions ✅

- [x] Copilot, 2026-02-08, record the linting and formatting decision

## Tags 🏷️

`#quality #consistency #maintainability`
