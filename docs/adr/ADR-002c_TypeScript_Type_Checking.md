# ADR-002c: TypeScript type checking 🧾

> |              |                                                 |
> | ------------ | ----------------------------------------------- |
> | Date         | `2026-02-08` when the decision was last updated |
> | Status       | `Accepted`                                      |
> | Significance | `Quality attributes`                            |

---

- [ADR-002c: TypeScript type checking 🧾](#adr-002c-typescript-type-checking-)
  - [Context 🧭](#context-)
  - [Decision ✅](#decision-)
    - [Assumptions 🧩](#assumptions-)
    - [Drivers 🎯](#drivers-)
    - [Options 🔀](#options-)
      - [Option A: tsc (Selected) ✅](#option-a-tsc-selected-)
      - [Option B: tsserver](#option-b-tsserver)
      - [Option C: typescript-eslint (type-aware linting)](#option-c-typescript-eslint-type-aware-linting)
      - [Option D: swc (transpile only)](#option-d-swc-transpile-only)
      - [Option E: Babel (transpile only)](#option-e-babel-transpile-only)
    - [Outcome 🏁](#outcome-)
    - [Rationale 🧠](#rationale-)
  - [Consequences ⚖️](#consequences-️)
  - [Compliance 📏](#compliance-)
  - [Notes 🔗](#notes-)
  - [Actions ✅](#actions-)
  - [Tags 🏷️](#tags-️)

## Context 🧭

The TypeScript tech stack needs a reliable, CI-friendly type checker that matches the TypeScript compiler semantics.

## Decision ✅

### Assumptions 🧩

- Node.js 24.13.0 (LTS) is the baseline runtime.
- TypeScript 5.9 is the baseline language version.
- Type checking must run in CI as a blocking gate.

### Drivers 🎯

- Type accuracy and parity with the compiler
- CI and editor integration
- Speed for local workflows
- Configuration simplicity
- Long-term maintenance

### Options 🔀

#### Option A: tsc (Selected) ✅

Use [`tsc`](https://github.com/microsoft/TypeScript) with `--noEmit` for type checking.

| Criteria       | Score/Notes                        |
| -------------- | ---------------------------------- |
| Type accuracy  | ⭐⭐⭐ Source of truth             |
| CI integration | ⭐⭐⭐ Standard for TypeScript     |
| Performance    | ⭐⭐ Good, with project references |
| Configuration  | ⭐⭐ Standard `tsconfig.json`      |
| Maintenance    | ⭐⭐⭐ Canonical tool              |
| Effort         | S                                  |

#### Option B: tsserver

Use the TypeScript language service [`tsserver`](https://github.com/microsoft/TypeScript).

| Criteria       | Score/Notes                 |
| -------------- | --------------------------- |
| Type accuracy  | ⭐⭐⭐ Same engine as tsc   |
| CI integration | ⭐ Low, not intended for CI |
| Performance    | ⭐⭐⭐ Fast for editor use  |
| Configuration  | ⭐⭐ Similar to tsc         |
| Maintenance    | ⭐⭐⭐ Canonical tool       |
| Effort         | M                           |

**Why not chosen**: Great for editor feedback but not designed for CI type checking.

#### Option C: typescript-eslint (type-aware linting)

Use [`typescript-eslint`](https://github.com/typescript-eslint/typescript-eslint) for type-aware linting.

| Criteria       | Score/Notes                                 |
| -------------- | ------------------------------------------- |
| Type accuracy  | ⭐⭐ Uses TS program but not a full checker |
| CI integration | ⭐⭐ Works, but focused on lint rules       |
| Performance    | ⭐⭐ Slower on larger codebases             |
| Configuration  | ⭐⭐ More config for rules                  |
| Maintenance    | ⭐⭐⭐ Active and widely used               |
| Effort         | M                                           |

**Why not chosen**: Helpful for linting, but not a replacement for full type checking.

#### Option D: swc (transpile only)

Use [`swc`](https://github.com/swc-project/swc) for TypeScript transpilation.

| Criteria       | Score/Notes            |
| -------------- | ---------------------- |
| Type accuracy  | ⭐ No type checking    |
| CI integration | ⭐ Low for type safety |
| Performance    | ⭐⭐⭐ Very fast       |
| Configuration  | ⭐⭐ Simple            |
| Maintenance    | ⭐⭐⭐ Active          |
| Effort         | M                      |

**Why not chosen**: Fast transpiler but does not provide type checking.

#### Option E: Babel (transpile only)

Use [`Babel`](https://github.com/babel/babel) with TypeScript presets.

| Criteria       | Score/Notes            |
| -------------- | ---------------------- |
| Type accuracy  | ⭐ No type checking    |
| CI integration | ⭐ Low for type safety |
| Performance    | ⭐⭐ Good              |
| Configuration  | ⭐⭐ Moderate          |
| Maintenance    | ⭐⭐⭐ Widely used     |
| Effort         | M                      |

**Why not chosen**: Transpiles TypeScript but does not enforce type safety.

### Outcome 🏁

Adopt `tsc` as the default type checker. This decision is reversible if a better, compiler-parity checker becomes available.

### Rationale 🧠

`tsc` is the canonical TypeScript type checker with full compiler parity, making it the safest default for CI.

## Consequences ⚖️

- CI must run `tsc --noEmit` for TypeScript projects.
- Alternative tools require explicit justification.

## Compliance 📏

- `pnpm tsc --noEmit` succeeds in CI.

## Notes 🔗

- Tech Radar: `./Tech_Radar.md`

## Actions ✅

- [x] Copilot, 2026-02-08, record the type checking decision

## Tags 🏷️

`#quality #correctness #maintainability`
