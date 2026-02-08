# ADR-002a: TypeScript dependency management 🧾

> |              |                                                 |
> | ------------ | ----------------------------------------------- |
> | Date         | `2026-02-08` when the decision was last updated |
> | Status       | `Accepted`                                      |
> | Significance | `Dependencies, Delivery & build`                |

---

- [ADR-002a: TypeScript dependency management 🧾](#adr-002a-typescript-dependency-management-)
  - [Context 🧭](#context-)
  - [Decision ✅](#decision-)
    - [Assumptions 🧩](#assumptions-)
    - [Drivers 🎯](#drivers-)
    - [Options 🔀](#options-)
      - [Option A: pnpm (Selected) ✅](#option-a-pnpm-selected-)
      - [Option B: npm](#option-b-npm)
      - [Option C: Yarn Berry](#option-c-yarn-berry)
      - [Option D: Yarn Classic](#option-d-yarn-classic)
      - [Option E: Bun](#option-e-bun)
    - [Outcome 🏁](#outcome-)
    - [Rationale 🧠](#rationale-)
  - [Consequences ⚖️](#consequences-️)
  - [Compliance 📏](#compliance-)
  - [Notes 🔗](#notes-)
  - [Actions ✅](#actions-)
  - [Tags 🏷️](#tags-️)

## Context 🧭

The TypeScript tech stack needs a default package manager that is deterministic, fast, and supports workspaces for multi-package repos.

## Decision ✅

### Assumptions 🧩

- Node.js 24.13.0 (LTS) is the baseline runtime.
- TypeScript 5.9 is the baseline language version.
- Lock files are required for deterministic installs.

### Drivers 🎯

- Deterministic installs and lock file integrity
- Workspace support for multi-package repos
- Performance for local and CI installs
- Security and supply-chain controls
- Active maintenance and ecosystem adoption

### Options 🔀

#### Option A: pnpm (Selected) ✅

Use [`pnpm`](https://github.com/pnpm/pnpm) with a lock file and workspace support.

| Criteria           | Score/Notes                       |
| ------------------ | --------------------------------- |
| Determinism        | ⭐⭐⭐ Strong lock file           |
| Workspace support  | ⭐⭐⭐ First-class workspaces     |
| Performance        | ⭐⭐⭐ Fast installs and caching  |
| Security controls  | ⭐⭐ Strict dependency resolution |
| Ecosystem adoption | ⭐⭐⭐ Broad and growing          |
| Effort             | S                                 |

#### Option B: npm

Use [`npm`](https://github.com/npm/cli) with `package-lock.json`.

| Criteria           | Score/Notes                           |
| ------------------ | ------------------------------------- |
| Determinism        | ⭐⭐⭐ Lock file is standard          |
| Workspace support  | ⭐⭐ Supported but less ergonomic     |
| Performance        | ⭐⭐ Slower than pnpm in larger repos |
| Security controls  | ⭐⭐ Good but fewer strict modes      |
| Ecosystem adoption | ⭐⭐⭐ Default for many teams         |
| Effort             | S                                     |

**Why not chosen**: Works well but slower and less space-efficient for large repos.

#### Option C: Yarn Berry

Use [`Yarn Berry`](https://github.com/yarnpkg/berry) with Plug'n'Play.

| Criteria           | Score/Notes                             |
| ------------------ | --------------------------------------- |
| Determinism        | ⭐⭐⭐ Strong and strict                |
| Workspace support  | ⭐⭐⭐ Excellent                        |
| Performance        | ⭐⭐ Fast but PnP can add friction      |
| Security controls  | ⭐⭐ Good, but PnP compatibility needed |
| Ecosystem adoption | ⭐⭐ Moderate                           |
| Effort             | M                                       |

**Why not chosen**: PnP adds tooling friction for some ecosystems.

#### Option D: Yarn Classic

Use [`Yarn Classic`](https://github.com/yarnpkg/yarn).

| Criteria           | Score/Notes                             |
| ------------------ | --------------------------------------- |
| Determinism        | ⭐⭐ Lock file is stable                |
| Workspace support  | ⭐⭐ Supported but older implementation |
| Performance        | ⭐⭐ Reasonable                         |
| Security controls  | ⭐ Low, fewer modern features           |
| Ecosystem adoption | ⭐⭐ Declining                          |
| Effort             | M                                       |

**Why not chosen**: Older stack with fewer modern features.

#### Option E: Bun

Use [`Bun`](https://github.com/oven-sh/bun) as the package manager.

| Criteria           | Score/Notes                     |
| ------------------ | ------------------------------- |
| Determinism        | ⭐⭐ Lock file supported        |
| Workspace support  | ⭐⭐ Improving but less mature  |
| Performance        | ⭐⭐⭐ Very fast                |
| Security controls  | ⭐⭐ Growing set of features    |
| Ecosystem adoption | ⭐⭐ Growing but still emerging |
| Effort             | M                               |

**Why not chosen**: Still evolving and not yet the safest default.

### Outcome 🏁

Adopt `pnpm` as the default package manager for TypeScript projects. This decision is reversible if ecosystem support shifts.

### Rationale 🧠

`pnpm` provides fast, deterministic installs with strong workspace support and good ecosystem adoption, making it the best default for this repo.

## Consequences ⚖️

- TypeScript projects should commit `pnpm-lock.yaml`.
- Alternative package managers require explicit justification.

## Compliance 📏

- `pnpm install --frozen-lockfile` succeeds in CI.

## Notes 🔗

- Tech Radar: `./Tech_Radar.md`
- Node.js downloads: <https://nodejs.org/en/download>
- TypeScript releases: <https://www.typescriptlang.org/download>

## Actions ✅

- [x] Copilot, 2026-02-08, record the dependency management decision

## Tags 🏷️

`#dependencies #build #reproducibility #maintainability`
