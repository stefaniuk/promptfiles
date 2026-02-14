# ADR-001g: Python TUI framework 🧾

> |              |                                                 |
> | ------------ | ----------------------------------------------- |
> | Date         | `2026-02-14` when the decision was last updated |
> | Status       | `Accepted`                                      |
> | Significance | `Interfaces & contracts, Quality attributes`    |

---

- [ADR-001g: Python TUI framework 🧾](#adr-001g-python-tui-framework-)
  - [Context 🧭](#context-)
  - [Decision ✅](#decision-)
    - [Assumptions 🧩](#assumptions-)
    - [Drivers 🎯](#drivers-)
    - [Options 🔀](#options-)
      - [Option A: Textual (Selected) ✅](#option-a-textual-selected-)
      - [Option B: urwid](#option-b-urwid)
      - [Option C: prompt-toolkit](#option-c-prompt-toolkit)
      - [Option D: PyTermGUI](#option-d-pytermgui)
      - [Option E: asciimatics](#option-e-asciimatics)
    - [Outcome 🏁](#outcome-)
    - [Rationale 🧠](#rationale-)
  - [Consequences ⚖️](#consequences-️)
  - [Compliance 📏](#compliance-)
  - [Notes 🔗](#notes-)
  - [Actions ✅](#actions-)
  - [Tags 🏷️](#tags-️)

## Context 🧭

Python tools need a standard TUI (Text User Interface) framework for building interactive, full-screen terminal applications. This goes beyond CLI argument parsing (covered by ADR-001f with `typer` + `rich`) — a TUI framework provides layout management, interactive widgets, event handling, and visual theming within the terminal.

Visual styling, richness of output, and end-user usability are the highest-priority criteria. The chosen framework must produce polished, modern-looking terminal interfaces with minimal effort.

## Decision ✅

### Assumptions 🧩

- Python 3.14.3 is the baseline runtime.
- TUI applications must run cross-platform (macOS, Linux, Windows).
- The framework should integrate well with the existing tech stack (`uv`, `ruff`, `mypy`, `pytest`, `typer`, `rich`).
- Visual polish and UX quality are valued above raw performance or minimal dependencies.
- Type hints and modern Python idioms are expected.

### Drivers 🎯

- Visual styling and theming (predefined themes, CSS-like customisation)
- Widget richness (buttons, inputs, tables, trees, lists, text areas)
- End-user usability (keyboard navigation, mouse support, command palette)
- Developer experience (API clarity, documentation, testing support)
- Ecosystem adoption and active maintenance
- Dependency footprint and compatibility with existing stack

Weighted criteria use a 1–5 scale (higher is more important). Scores use ⭐ (1), ⭐⭐ (2), ⭐⭐⭐ (3). Weighted totals exclude Effort and have a maximum of 69.

| Criteria               | Weight | Rationale                                       |
| ---------------------- | ------ | ----------------------------------------------- |
| Visual styling/theming | 5      | Highest priority — polished, modern look        |
| Widget richness        | 5      | Core need for interactive applications          |
| End-user usability     | 5      | Keyboard, mouse, command palette, accessibility |
| Developer experience   | 4      | API clarity, docs, type hints, testing          |
| Ecosystem/maintenance  | 2      | Longevity and community support                 |
| Dependency footprint   | 2      | Prefer lighter but not at expense of quality    |

### Options 🔀

#### Option A: Textual (Selected) ✅

Use [`Textual`](https://github.com/Textualize/textual) (v7.5.0, 34.3k ⭐, 189 contributors, MIT) — a modern TUI framework from Textualize, built on top of Rich.

**Top criteria**: Visual styling/theming, Widget richness

**Weighted option score**: 4.6 / 5.0

Textual provides a CSS-based styling system with predefined themes, a comprehensive widget gallery (buttons, data tables, tree controls, inputs, text areas, list views, tabs, and more), a built-in command palette (Ctrl+P), a dev console for debugging, and first-class async support. Applications can also be served in a web browser via `textual serve`. The framework includes a dedicated testing framework for snapshot and integration tests.

| Criteria                | Weight | Score/Notes                                                              |
| ----------------------- | ------ | ------------------------------------------------------------------------ |
| Visual styling/theming  | 5      | ⭐⭐⭐ CSS-based styling, predefined themes, dark/light mode, custom CSS |
| Widget richness         | 5      | ⭐⭐⭐ Most comprehensive widget library of any Python TUI framework     |
| End-user usability      | 5      | ⭐⭐⭐ Mouse, keyboard, command palette, clipboard, focus management     |
| Developer experience    | 4      | ⭐⭐⭐ Modern API, type hints, rich docs, built-in test framework        |
| Ecosystem/maintenance   | 2      | ⭐⭐⭐ Very active (209 releases), 34.3k stars, strong Discord community |
| Dependency footprint    | 2      | ⭐⭐ Depends on Rich; moderate footprint                                 |
| Effort                  |        | S — straightforward to learn; excellent documentation                    |
| Weighted score (max 69) |        | 67                                                                       |

#### Option B: urwid

Use [`urwid`](https://github.com/urwid/urwid) (v3.0.5, 3k ⭐, 136 contributors, LGPL-2.1) — a mature console UI library with curses foundations.

**Top criteria**: Visual styling/theming, Widget richness

**Weighted option score**: 2.7 / 5.0

Urwid is a long-standing library with edit boxes, buttons, check boxes, radio buttons, and a powerful list box. It supports multiple event loops (asyncio, Twisted, Tornado, trio, ZeroMQ), UTF-8/CJK, and 24-bit colour. Styling is palette-based rather than CSS-driven.

| Criteria                | Weight | Score/Notes                                                                   |
| ----------------------- | ------ | ----------------------------------------------------------------------------- |
| Visual styling/theming  | 5      | ⭐ Palette-based, no theming engine; visual output is functional but dated    |
| Widget richness         | 5      | ⭐⭐ Core widgets present but less varied than Textual                        |
| End-user usability      | 5      | ⭐⭐ Keyboard-focused; mouse support exists but basic                         |
| Developer experience    | 4      | ⭐⭐ Older API style, less idiomatic modern Python; documentation is adequate |
| Ecosystem/maintenance   | 2      | ⭐⭐⭐ Active maintenance (Feb 2026 release), used by 11.1k projects          |
| Dependency footprint    | 2      | ⭐⭐⭐ Lightweight; minimal dependencies                                      |
| Effort                  |        | M — steeper learning curve; lower-level API                                   |
| Weighted score (max 69) |        | 42                                                                            |

**Why not chosen**: Styling is palette-based and dated. Widget set is less rich. The API is older and more verbose, requiring significantly more effort to achieve the same visual quality Textual provides out of the box. LGPL-2.1 licence is more restrictive than MIT.

#### Option C: prompt-toolkit

Use [`python-prompt-toolkit`](https://github.com/prompt-toolkit/python-prompt-toolkit) (v3.0.52, 10.3k ⭐, 219 contributors, BSD-3-Clause) — a library for building powerful interactive command-line applications.

**Top criteria**: Visual styling/theming, Widget richness

**Weighted option score**: 2.6 / 5.0

prompt-toolkit excels at interactive prompts with syntax highlighting, code completion, Emacs/Vi key bindings, and multi-line input. It powers `ptpython` and is used by IPython. However, it is designed primarily for prompt/REPL-style interactions, not full-screen TUI applications with complex layouts and widget hierarchies.

| Criteria                | Weight | Score/Notes                                                                    |
| ----------------------- | ------ | ------------------------------------------------------------------------------ |
| Visual styling/theming  | 5      | ⭐ Prompt/input colouring; no layout theming system                            |
| Widget richness         | 5      | ⭐ Focused on prompts, completions, and input buffers; no buttons/tables/trees |
| End-user usability      | 5      | ⭐⭐⭐ Excellent for prompt UX — auto-complete, Vi/Emacs, mouse                |
| Developer experience    | 4      | ⭐⭐ Well-documented prompt API; full-screen layout API is lower-level         |
| Ecosystem/maintenance   | 2      | ⭐⭐⭐ Mature (powers IPython), 10.3k stars, wide adoption                     |
| Dependency footprint    | 2      | ⭐⭐⭐ Lightweight (Pygments + wcwidth)                                        |
| Effort                  |        | M — simple for prompts, complex for full-screen TUIs                           |
| Weighted score (max 69) |        | 39                                                                             |

**Why not chosen**: Designed for interactive prompts, not full-screen TUI applications. Lacks a widget system, layout engine, and theming for building rich user interfaces. The full-screen API exists but is low-level and not comparable in capability.

#### Option D: PyTermGUI

Use [`PyTermGUI`](https://github.com/bczsalba/pytermgui) (v7.7.4, 2.6k ⭐, 18 contributors, MIT) — a TUI framework with mouse support, a window manager, and TIM markup language.

**Top criteria**: Visual styling/theming, Widget richness

**Weighted option score**: 2.7 / 5.0

PyTermGUI features YAML-based styling, a TIM markup language for text styling, a desktop-inspired window manager with modals, mouse support, `NO_COLOR` compliance, and SVG/HTML export. However, the author has indicated that core ideas are being rewritten in the [Shade 40](https://github.com/shade40) project, effectively putting PTG into maintenance mode.

| Criteria                | Weight | Score/Notes                                                                       |
| ----------------------- | ------ | --------------------------------------------------------------------------------- |
| Visual styling/theming  | 5      | ⭐⭐ YAML styling and TIM markup; decent but less polished than CSS-based theming |
| Widget richness         | 5      | ⭐⭐ Window manager, inputs, buttons, containers; narrower than Textual           |
| End-user usability      | 5      | ⭐⭐ Mouse support out of the box; good NO_COLOR compliance                       |
| Developer experience    | 4      | ⭐⭐ Readable API; documentation is adequate; small community                     |
| Ecosystem/maintenance   | 2      | ⭐ Author redirected to Shade 40; 18 contributors; uncertain future               |
| Dependency footprint    | 2      | ⭐⭐⭐ Lightweight                                                                |
| Effort                  |        | M — reasonable API but uncertain long-term investment                             |
| Weighted score (max 69) |        | 43                                                                                |

**Why not chosen**: The author has effectively sunset this project in favour of Shade 40. Small contributor base (18) and uncertain maintenance trajectory make it a risky long-term choice. Widget set and visual polish are narrower than Textual.

#### Option E: asciimatics

Use [`asciimatics`](https://github.com/peterbrittain/asciimatics) (v1.15.0, 4.3k ⭐, 40 contributors, Apache-2.0) — a cross-platform package for full-screen text UIs and ASCII animations.

**Top criteria**: Visual styling/theming, Widget richness

**Weighted option score**: 2.3 / 5.0

asciimatics provides low-level screen control, 256-colour support, mouse/keyboard input, ASCII animations (sprites, particles, banners), image-to-ASCII conversion, and form widgets (buttons, text boxes, radio buttons). It shines for ASCII art and animation effects but lags behind modern frameworks for structured TUI application development.

| Criteria                | Weight | Score/Notes                                                                   |
| ----------------------- | ------ | ----------------------------------------------------------------------------- |
| Visual styling/theming  | 5      | ⭐ 256-colour support; no theming engine; animations are niche                |
| Widget richness         | 5      | ⭐⭐ Basic form widgets; strong animation/effects but not typical TUI widgets |
| End-user usability      | 5      | ⭐⭐ Mouse/keyboard input; functional but not modern UX patterns              |
| Developer experience    | 4      | ⭐ Older API; setup.py-based; documentation is adequate but aging             |
| Ecosystem/maintenance   | 2      | ⭐ Last release Oct 2023; development pace has slowed significantly           |
| Dependency footprint    | 2      | ⭐⭐ Moderate (Pillow, pyfiglet, wcwidth)                                     |
| Effort                  |        | L — lower-level API; more boilerplate for standard TUI patterns               |
| Weighted score (max 69) |        | 33                                                                            |

**Why not chosen**: Last release over two years ago. Development has slowed. Focused more on ASCII art and animations than structured, modern TUI applications. API is older and less ergonomic. Widget set is basic compared to Textual.

### Outcome 🏁

Adopt `Textual` as the default TUI framework for Python. This decision is reversible if the project's needs change or a stronger alternative emerges. The decision should be revisited if Textual's maintenance model changes (e.g. if Textualize pivots away from open-source development).

### Rationale 🧠

Using the weighted criteria, Textual scores 67/69 — far ahead of the next option (PyTermGUI at 43, urwid at 42). The gap is largest in the three highest-weighted criteria (visual styling, widget richness, end-user usability), which aligns directly with the stated priorities.

Textual integrates naturally with the existing tech stack: it is built on `rich` (already adopted for CLI output per ADR-001f), supports `mypy` type checking, and installs cleanly via `uv`. Its CSS-based styling, predefined themes, comprehensive widget gallery, and built-in testing framework make it the most productive choice for building polished terminal applications.

| Criteria                    | Weight | Textual | urwid  | prompt-toolkit | PyTermGUI | asciimatics |
| --------------------------- | ------ | ------- | ------ | -------------- | --------- | ----------- |
| Visual styling/theming      | 5      | ⭐⭐⭐  | ⭐     | ⭐             | ⭐⭐      | ⭐          |
| Widget richness             | 5      | ⭐⭐⭐  | ⭐⭐   | ⭐             | ⭐⭐      | ⭐⭐        |
| End-user usability          | 5      | ⭐⭐⭐  | ⭐⭐   | ⭐⭐⭐         | ⭐⭐      | ⭐⭐        |
| Developer experience        | 4      | ⭐⭐⭐  | ⭐⭐   | ⭐⭐           | ⭐⭐      | ⭐          |
| Ecosystem/maintenance       | 2      | ⭐⭐⭐  | ⭐⭐⭐ | ⭐⭐⭐         | ⭐        | ⭐          |
| Dependency footprint        | 2      | ⭐⭐    | ⭐⭐⭐ | ⭐⭐⭐         | ⭐⭐⭐    | ⭐⭐        |
| **Weighted score (max 69)** |        | **67**  | **42** | **39**         | **43**    | **33**      |

## Consequences ⚖️

- New TUI applications should use Textual by default.
- Textual introduces a dependency on `rich`, which is already part of the stack (ADR-001f).
- Alternatives require explicit justification.
- Developers should follow Textual's CSS-based styling approach and use predefined themes for consistency.
- The built-in testing framework (`textual.testing`) should be used for TUI tests alongside `pytest`.

This decision becomes irrelevant if TUI applications are no longer needed, or if a terminal-independent GUI framework is adopted instead.

## Compliance 📏

- TUI applications use Textual and include at least one predefined theme.
- Widget usage follows Textual's `compose()` pattern.
- TUI tests use `textual.testing` with `pytest`.

## Notes 🔗

- Tech Radar: `./Tech_Radar.md`
- Related: ADR-001f (CLI argument parsing — `typer` + `rich`)
- Textual documentation: [textual.textualize.io](https://textual.textualize.io/)
- Textual GitHub: [github.com/Textualize/textual](https://github.com/Textualize/textual)

## Actions ✅

- [x] Copilot, 2026-02-14, record the TUI framework decision
- [x] Copilot, 2026-02-14, update Tech Radar

## Tags 🏷️

`#usability #interfaces #maintainability #accessibility`

---

> **Version**: 1.0.0
> **Last Amended**: 2026-02-14
