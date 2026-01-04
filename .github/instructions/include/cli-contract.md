# CLI Contract ⌨️

This shared note defines the **canonical CLI contract** for exit codes and standard stream semantics across languages. Individual instruction sets must link here instead of duplicating the guidance.

## 1. Exit codes (non-negotiable)

- `0` — successful completion.
- `1` — general operational failure (unexpected error, dependency failure) when no more specific code exists.
- `2` — usage error (invalid flags/args, missing required input, mutually exclusive options).
- Reserve additional non-zero codes **only** when automation depends on them; document the mapping (code, meaning, user-facing hint) and add regression tests.
- Exit with the **first failure cause**; do not mask distinct failures behind the same code unless explicitly documented.
- Tests covering CLI boundaries must assert the relevant exit codes.

## 2. Stdout vs stderr (stream semantics)

- `stdout` carries the primary result payloads (machine-readable JSON, tables, paths, generated artefacts). It **must** be safe to pipe into other commands without post-processing to strip diagnostics.
- `stderr` carries diagnostics (progress, warnings, errors, verbose/debug output). Diagnostics must remain human-readable and should include actionable next steps when reporting failures.
- Commands must behave correctly when `stdout` is redirected or piped; never interleave diagnostic text onto `stdout`.
- Long-running commands should emit progress to `stderr` (or structured logs) so that `stdout` remains clean.
- When producing mixed human + machine output, provide an explicit flag (for example `--json`) that switches `stdout` to the machine format while keeping diagnostics on `stderr`.

## 3. Documentation and testing expectations

- Every published CLI must document the supported exit codes and diagnostic behaviours (README/help text + tests).
- Integration tests must cover at least one success case (`0`) and each reserved non-zero code to prevent future drift.
- When wrapping other tools, normalise their exit codes to this contract (translate upstream codes if necessary) and document any deliberate exceptions via ADR.

---

> **Version**: 1.0.0
> **Last Amended**: 2026-01-04
