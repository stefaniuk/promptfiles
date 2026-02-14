# ADR-002g: TypeScript TUI framework 🧾

> |              |                                                 |
> | ------------ | ----------------------------------------------- |
> | Date         | `2026-06-15` when the decision was last updated |
> | Status       | `Accepted`                                      |
> | Significance | `Interfaces & contracts, Quality attributes`    |

---

- [ADR-002g: TypeScript TUI framework 🧾](#adr-002g-typescript-tui-framework-)
  - [Context 🧭](#context-)
  - [Decision ✅](#decision-)
    - [Assumptions 🧩](#assumptions-)
    - [Drivers 🎯](#drivers-)
    - [Options 🔀](#options-)
      - [Option A: Ink (Selected) ✅](#option-a-ink-selected-)
      - [Option B: blessed](#option-b-blessed)
      - [Option C: terminal-kit](#option-c-terminal-kit)
      - [Option D: @clack/prompts](#option-d-clackprompts)
      - [Option E: prompts](#option-e-prompts)
    - [Outcome 🏁](#outcome-)
    - [Rationale 🧠](#rationale-)
  - [Consequences ⚖️](#consequences-️)
  - [Compliance 📏](#compliance-)
  - [Notes 🔗](#notes-)
  - [Actions ✅](#actions-)
  - [Tags 🏷️](#tags-️)

## Context 🧭

TypeScript tools need a standard TUI (Text User Interface) framework for building interactive, full-screen terminal applications. This goes beyond CLI argument parsing (covered by ADR-002f with `commander` + `chalk`) — a TUI framework provides layout management, interactive widgets, event handling, and visual theming within the terminal.

Visual styling, richness of output, and end-user usability are the highest-priority criteria. The chosen framework must produce polished, modern-looking terminal interfaces with minimal effort.

## Decision ✅

### Assumptions 🧩

- Node.js 24.13.0 (LTS) and TypeScript 5.9 are the baseline runtime and language.
- TUI applications must run cross-platform (macOS, Linux, Windows).
- The framework should integrate well with the existing tech stack (`pnpm`, `biome`, `tsc`, `vitest`, `commander`, `chalk`).
- Visual polish and UX quality are valued above raw performance or minimal dependencies.
- Strict TypeScript and modern idioms are expected.

### Drivers 🎯

- Visual styling and theming (colours, borders, layout, backgrounds)
- Widget richness (inputs, spinners, tables, progress bars, select lists)
- End-user usability (keyboard navigation, focus management, accessibility)
- Developer experience (API clarity, documentation, testing support, TypeScript types)
- Ecosystem adoption and active maintenance
- Dependency footprint and compatibility with existing stack

Weighted criteria use a 1–5 scale (higher is more important). Scores use ⭐ (1), ⭐⭐ (2), ⭐⭐⭐ (3). Weighted totals exclude Effort and have a maximum of 69.

| Criteria               | Weight | Rationale                                    |
| ---------------------- | ------ | -------------------------------------------- |
| Visual styling/theming | 5      | Highest priority — polished, modern look     |
| Widget richness        | 5      | Core need for interactive applications       |
| End-user usability     | 5      | Keyboard, focus management, accessibility    |
| Developer experience   | 4      | API clarity, docs, type safety, testing      |
| Ecosystem/maintenance  | 2      | Longevity and community support              |
| Dependency footprint   | 2      | Prefer lighter but not at expense of quality |

### Options 🔀

#### Option A: Ink (Selected) ✅

Use [`Ink`](https://github.com/vadimdemedes/ink) (v6.7.0, 34.9k ⭐, 160 contributors, MIT) — a React-based framework for building CLI applications with components, using Yoga for Flexbox layout.

**Top criteria**: Visual styling/theming, Widget richness

**Weighted option score**: 4.9 / 5.0

Ink uses React's component model and hooks to build terminal UIs. It provides Flexbox layout via Yoga, chalk-based colours (named, hex, RGB), seven border styles plus custom borders, background colours, and focus management (Tab/Shift+Tab). It includes screen reader support (ARIA roles, states, labels), React Devtools integration, and `ink-testing-library` for testing. The ecosystem offers community components for text input, spinners, select lists, tables, forms, progress bars, markdown rendering, scroll views, and virtual lists. Used by Claude Code, Gemini CLI, GitHub Copilot CLI, Shopify CLI, Prisma, Cloudflare Wrangler, and Terraform CDK.

| Criteria                | Weight | Score/Notes                                                                               |
| ----------------------- | ------ | ----------------------------------------------------------------------------------------- |
| Visual styling/theming  | 5      | ⭐⭐⭐ Chalk colours (named/hex/RGB), Flexbox layout, 7 border styles, backgrounds        |
| Widget richness         | 5      | ⭐⭐⭐ Rich ecosystem: text input, spinner, select, table, form, progress, markdown, etc. |
| End-user usability      | 5      | ⭐⭐⭐ Focus management (Tab/Shift+Tab), screen reader (ARIA), keyboard hooks, CI adapt   |
| Developer experience    | 4      | ⭐⭐⭐ React paradigm, hooks API, ink-testing-library, TypeScript 99.8%, Devtools support |
| Ecosystem/maintenance   | 2      | ⭐⭐⭐ 34.9k stars, 160 contributors, 2.28M weekly downloads, 93.2k dependents            |
| Dependency footprint    | 2      | ⭐⭐ React, Yoga (Flexbox), chalk; moderate footprint (~418kB)                            |
| Effort                  |        | S — familiar React paradigm; excellent documentation                                      |
| Weighted score (max 69) |        | 67                                                                                        |

#### Option B: blessed

Use [`blessed`](https://github.com/chjj/blessed) (v0.1.81, 11.8k ⭐, 12 contributors, MIT) — a curses-like library with a high-level terminal interface API, reimplementing ncurses in pure JavaScript.

**Top criteria**: Visual styling/theming, Widget richness

**Weighted option score**: 3.4 / 5.0

Blessed provides the most comprehensive native widget set of any Node.js terminal library: Box, Text, List, ListTable, Form, Textarea, Textbox, Button, Checkbox, RadioButton, ProgressBar, Log, Table, Terminal, Image, ANSIImage, Layout, and more. It supports 256/hex colours, transparency, shadows, hover/focus effects, CSS-like positioning (percentages, centering, padding), and mouse/keyboard input. However, the project has been abandoned for 11 years with no updates since 2014. Types are available via `@types/blessed` (DefinitelyTyped) but are not maintained by the author.

| Criteria                | Weight | Score/Notes                                                                          |
| ----------------------- | ------ | ------------------------------------------------------------------------------------ |
| Visual styling/theming  | 5      | ⭐⭐ 256/hex colours, transparency, shadows, hover/focus; no modern theming engine   |
| Widget richness         | 5      | ⭐⭐⭐ Most comprehensive native widget set of any Node.js terminal library          |
| End-user usability      | 5      | ⭐⭐ Keyboard/mouse/scrollbar/focus management; no modern accessibility patterns     |
| Developer experience    | 4      | ⭐ Plain JavaScript, types via DT, callback-based API, no testing framework, 11y old |
| Ecosystem/maintenance   | 2      | ⭐ Abandoned for 11 years, 12 contributors, no active development                    |
| Dependency footprint    | 2      | ⭐⭐⭐ Zero dependencies; fully self-contained                                       |
| Effort                  |        | L — older API patterns; no TypeScript; significant integration effort                |
| Weighted score (max 69) |        | 47                                                                                   |

**Why not chosen**: Abandoned for 11 years with no maintenance or security patches. Plain JavaScript with no native TypeScript types. Callback-based API is outdated. Despite an impressive widget set, adopting an unmaintained library with known stale issues poses unacceptable long-term risk.

#### Option C: terminal-kit

Use [`terminal-kit`](https://github.com/cronvel/terminal-kit) (v3.1.3, 3.3k ⭐, 19 contributors, MIT) — a full terminal library with 256/24-bit colours, key and mouse handling, input fields, progress bars, screen buffers, and a document model.

**Top criteria**: Visual styling/theming, Widget richness

**Weighted option score**: 3.0 / 5.0

terminal-kit provides a broad feature set including styled text output, input fields, single/column/grid menus, progress bars, tables with automatic column computing, spinners, yes/no prompts, screen buffers (32-bit RGBA composition), image loading, and a document model for richer applications. It does not depend on ncurses. However, it is written entirely in JavaScript with no TypeScript types, has a small contributor base, and its last feature work was approximately two years ago.

| Criteria                | Weight | Score/Notes                                                                               |
| ----------------------- | ------ | ----------------------------------------------------------------------------------------- |
| Visual styling/theming  | 5      | ⭐⭐ 256/24-bit colours, style markup, image loading; functional but no modern theming    |
| Widget richness         | 5      | ⭐⭐ Input field, menus, progress bar, table, spinner, screen buffer; decent but narrower |
| End-user usability      | 5      | ⭐⭐ GPM mouse support, keyboard input; decent but not modern UX patterns                 |
| Developer experience    | 4      | ⭐ JavaScript only, no native types, older API style, limited testing support             |
| Ecosystem/maintenance   | 2      | ⭐⭐ 3.3k stars, 19 contributors; last feature work ~2 years ago                          |
| Dependency footprint    | 2      | ⭐⭐ Some dependencies (string-kit and related packages)                                  |
| Effort                  |        | M — reasonable API but no TypeScript support increases integration cost                   |
| Weighted score (max 69) |        | 42                                                                                        |

**Why not chosen**: No TypeScript types — a non-starter for the existing strict TypeScript stack. Small contributor base and slowing development pace. The widget set, whilst decent, lacks the depth and ecosystem breadth of Ink. API patterns are older and do not align with modern TypeScript idioms.

#### Option D: @clack/prompts

Use [`@clack/prompts`](https://github.com/bombshell-dev/clack) (v1.0.1, 7.4k ⭐, 42 contributors, MIT) — opinionated, pre-styled interactive prompt components for JavaScript CLIs, built on `@clack/core`.

**Top criteria**: Visual styling/theming, End-user usability

**Weighted option score**: 3.9 / 5.0

@clack/prompts provides beautifully styled, minimal CLI prompt components including text, confirm, select, multiselect (with grouping), spinner, progress, logs, streaming output, and task runners. It is 100% TypeScript with built-in type declarations, uses modern tooling (pnpm, biome, vitest), and was recently released as v1.0.0. However, it is designed for interactive prompt flows, not full-screen TUI applications — it lacks layout management, persistent UI elements, widget composition, and screen rendering capabilities.

| Criteria                | Weight | Score/Notes                                                                                     |
| ----------------------- | ------ | ----------------------------------------------------------------------------------------------- |
| Visual styling/theming  | 5      | ⭐⭐ Beautiful minimal styling for prompts; no full-screen layout or theming system             |
| Widget richness         | 5      | ⭐ Prompts only (text, confirm, select, spinner, progress); no layout/tables/trees for full TUI |
| End-user usability      | 5      | ⭐⭐⭐ Excellent prompt UX, cancellation handling, grouping, task runner, streaming             |
| Developer experience    | 4      | ⭐⭐⭐ 100% TypeScript, clean API, built-in types, modern tooling (pnpm, biome, vitest)         |
| Ecosystem/maintenance   | 2      | ⭐⭐⭐ 7.4k stars, 42 contributors, v1 just released, 5M weekly downloads, active development   |
| Dependency footprint    | 2      | ⭐⭐⭐ 3 dependencies, 240kB unpacked, "80% smaller than alternatives"                          |
| Effort                  |        | S — simple API for prompts; not applicable for full-screen TUI development                      |
| Weighted score (max 69) |        | 54                                                                                              |

**Why not chosen**: Designed for interactive prompt flows, not full-screen TUI applications. Lacks layout management, persistent screen rendering, widget composition, and the structural capabilities needed for building rich terminal applications. Excellent for CLI wizards and setup prompts but fundamentally different from a TUI framework.

#### Option E: prompts

Use [`prompts`](https://github.com/terkelg/prompts) (v2.4.2, 9.2k ⭐, 71 contributors, MIT) — lightweight, beautiful, and user-friendly interactive prompts.

**Top criteria**: Visual styling/theming, End-user usability

**Weighted option score**: 2.6 / 5.0

prompts provides 12 prompt types (text, password, number, confirm, list, toggle, select, multiselect, autocomplete, autocompleteMultiselect, date, invisible) with a simple promise-based API. It is lightweight (2 dependencies, 187kB) and has enormous adoption (37M weekly downloads, 15.8M dependents). However, it is written in JavaScript with types only via DefinitelyTyped, has not been published in four years, and — like @clack/prompts — is an interactive prompt library, not a full-screen TUI framework.

| Criteria                | Weight | Score/Notes                                                                                |
| ----------------------- | ------ | ------------------------------------------------------------------------------------------ |
| Visual styling/theming  | 5      | ⭐ Basic kleur-based colouring; no layout or theming system                                |
| Widget richness         | 5      | ⭐ 12 prompt types but no TUI widgets (layout, tables, trees, persistent elements)         |
| End-user usability      | 5      | ⭐⭐ Good prompt UX, arrow-key navigation; less polished than @clack/prompts               |
| Developer experience    | 4      | ⭐⭐ Types via DefinitelyTyped, simple API, testable via inject(); JavaScript-only         |
| Ecosystem/maintenance   | 2      | ⭐ Last publish 4 years ago; development appears stalled; 37M downloads is legacy momentum |
| Dependency footprint    | 2      | ⭐⭐⭐ 2 dependencies, 187kB; very lightweight                                             |
| Effort                  |        | S — simple API; not applicable for full-screen TUI development                             |
| Weighted score (max 69) |        | 36                                                                                         |

**Why not chosen**: Development has stalled — last published four years ago. JavaScript-only with external types. Like @clack/prompts, this is a prompt library, not a full-screen TUI framework. Its high download count reflects legacy adoption rather than active preference for new projects.

### Outcome 🏁

Adopt `Ink` as the default TUI framework for TypeScript. This decision is reversible if the project's needs change or a stronger alternative emerges. The decision should be revisited if Ink's maintenance model changes or if a TypeScript-native TUI framework with comparable capabilities emerges.

### Rationale 🧠

Using the weighted criteria, Ink scores 67/69 — well ahead of the next option (@clack/prompts at 54, blessed at 47). The gap is largest in the three highest-weighted criteria (visual styling, widget richness, end-user usability), which aligns directly with the stated priorities.

Ink is the de facto standard for building terminal applications in the TypeScript/Node.js ecosystem. Its React-based component model is familiar to most TypeScript developers, and its Flexbox layout system (via Yoga) provides powerful, predictable positioning. The rich ecosystem of community components (ink-text-input, ink-spinner, ink-select-input, ink-table, ink-progress-bar, etc.) means most common TUI patterns are available as drop-in modules. Its adoption by major CLI tools (Claude Code, Gemini CLI, GitHub Copilot CLI, Shopify CLI, Prisma, Cloudflare Wrangler) validates its production-readiness and longevity.

Ink also integrates naturally with the existing tech stack: it is 99.8% TypeScript, uses chalk for colours (already adopted per ADR-002f), and its testing library works with `vitest`.

| Criteria                    | Weight | Ink    | blessed | terminal-kit | @clack/prompts | prompts |
| --------------------------- | ------ | ------ | ------- | ------------ | -------------- | ------- |
| Visual styling/theming      | 5      | ⭐⭐⭐ | ⭐⭐    | ⭐⭐         | ⭐⭐           | ⭐      |
| Widget richness             | 5      | ⭐⭐⭐ | ⭐⭐⭐  | ⭐⭐         | ⭐             | ⭐      |
| End-user usability          | 5      | ⭐⭐⭐ | ⭐⭐    | ⭐⭐         | ⭐⭐⭐         | ⭐⭐    |
| Developer experience        | 4      | ⭐⭐⭐ | ⭐      | ⭐           | ⭐⭐⭐         | ⭐⭐    |
| Ecosystem/maintenance       | 2      | ⭐⭐⭐ | ⭐      | ⭐⭐         | ⭐⭐⭐         | ⭐      |
| Dependency footprint        | 2      | ⭐⭐   | ⭐⭐⭐  | ⭐⭐         | ⭐⭐⭐         | ⭐⭐⭐  |
| **Weighted score (max 69)** |        | **67** | **47**  | **42**       | **54**         | **36**  |

## Consequences ⚖️

- New TUI applications should use Ink by default.
- Ink introduces a dependency on React and Yoga; this is acceptable given the ecosystem benefits and developer familiarity.
- Chalk is already part of the stack (ADR-002f) and is used by Ink for colour output.
- Alternatives require explicit justification.
- Developers should follow Ink's component-based architecture and use hooks for input handling, focus management, and application lifecycle.
- Tests should use `ink-testing-library` alongside `vitest`.

This decision becomes irrelevant if TUI applications are no longer needed, or if a terminal-independent GUI framework is adopted instead.

## Compliance 📏

- TUI applications use Ink and follow the component-based architecture.
- Keyboard input uses the `useInput` hook; focus uses `useFocus` and `useFocusManager`.
- TUI tests use `ink-testing-library` with `vitest`.

## Notes 🔗

- Tech Radar: `./Tech_Radar.md`
- Related: ADR-002f (CLI argument parsing — `commander` + `chalk`)
- Related: ADR-001g (Python TUI framework — `textual`)
- Ink documentation: [github.com/vadimdemedes/ink](https://github.com/vadimdemedes/ink)
- Ink npm: [npmjs.com/package/ink](https://www.npmjs.com/package/ink)
- Community components: [github.com/vadimdemedes/ink#community](https://github.com/vadimdemedes/ink#community)

## Actions ✅

- [x] Copilot, 2026-06-15, record the TUI framework decision
- [x] Copilot, 2026-06-15, update Tech Radar

## Tags 🏷️

`#usability #interfaces #maintainability #accessibility`

---

> **Version**: 1.0.0
> **Last Amended**: 2026-06-15
