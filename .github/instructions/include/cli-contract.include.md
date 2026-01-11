# CLI Contract ⌨️

This shared note defines the **canonical CLI contract** for exit codes and standard stream semantics across languages. Individual instruction sets must link here instead of duplicating the guidance.

## 1. Exit codes (non-negotiable)

- `0` — successful completion.
- `1` — general operational failure (unexpected error, dependency failure) when no more specific code exists.
- `2` — usage error (invalid flags/args, missing required input, mutually exclusive options).
- Reserve additional non-zero codes **only** when automation depends on them; document the mapping (code, meaning, user-facing hint) and add regression tests.
- Exit with the **first failure cause**; do not mask distinct failures behind the same code unless explicitly documented.
- Tests covering CLI boundaries must assert the relevant exit codes.
- Wrappers translating upstream tools or libraries must normalise their exit codes to this contract. If the wrapped system emits rich errors (for example JSON error payloads) surface the actionable snippet in diagnostics and map the numeric code to `0/1/2` (or a documented reserved value).

## 2. Stdout vs stderr (stream semantics)

- `stdout` carries the primary result payloads (machine-readable JSON, tables, paths, generated artefacts). It **must** be safe to pipe into other commands without post-processing to strip diagnostics.
- `stderr` carries diagnostics (progress, warnings, errors, verbose/debug output). Diagnostics must remain human-readable and should include actionable next steps when reporting failures.
- Commands must behave correctly when `stdout` is redirected or piped; never interleave diagnostic text onto `stdout`.
- Long-running commands should emit progress to `stderr` (or structured logs) so that `stdout` remains clean.
- When producing mixed human + machine output, provide an explicit flag (for example `--json`) that switches `stdout` to the machine format while keeping diagnostics on `stderr`.
- Cloud runtimes (Lambda, Cloud Run, Functions) often wire `stdout/stderr` into log aggregators; keep payloads compact and avoid ANSI control codes unless the platform supports them.
- Flush and close streams explicitly before exiting short-lived serverless handlers so platforms do not drop trailing bytes.

## 3. Documentation and testing expectations

- Every published CLI must document the supported exit codes and diagnostic behaviours (README/help text + tests).
- Integration tests must cover at least one success case (`0`) and each reserved non-zero code to prevent future drift.
- When wrapping other tools, normalise their exit codes to this contract (translate upstream codes if necessary) and document any deliberate exceptions via ADR.
- Help output (`--help`, `-h`) must describe the primary flags, mutually exclusive options, default value sources (env vars, config files), and provide a short usage example that demonstrates piping/JSON output when relevant.
- Include smoke tests for wrapper CLIs proving that upstream failures still yield deterministic codes/diagnostics.

## 4. Developer ergonomics

- Provide `--help`, `--version`, and `--verbose` (or `--quiet`) switches consistently so that scripts can introspect capabilities and humans can self-serve.
- Prefer explicit flags over positional arguments once more than two inputs are required; accept configuration via environment variables only when documented, and echo which sources were used in verbose diagnostics.
- Offer `--dry-run` when the command mutates resources so that automation can validate intent without side effects.
- Keep interactive prompts opt-in (`--interactive` or detection of TTY) and always provide a non-interactive equivalent flag for CI/CD use.

## 5. Wrappers and shared libraries

- Keep CLI entrypoints as thin adapters: parse/validate input, hand off to shared library functions, and forward exit codes. No business logic or domain processing belongs in the CLI handler itself.
- When discrepancies arise between CLI behaviour and the underlying library (forked validation, duplicated transformations, etc.), schedule and execute a refactor to relocate the logic back into the shared code before adding new features.
- When exposing library functionality through a CLI wrapper, surface the same validation rules and defaults as the library API so that behaviours stay aligned.
- If multiple CLIs share common parsing or logging helpers, centralise that code in a module to keep flag semantics identical (for example the same `--region`, `--profile`, `--timeout` handling everywhere).
- Ensure wrapper CLIs can be imported as libraries themselves where sensible (for example `main(args: list[str]) -> int`) so that AWS Lambda or other orchestrators can reuse the parsing logic without shelling out.

## 6. Cloud and serverless workloads

- Design CLIs so they run cleanly inside short-lived containers/functions: avoid relying on background daemons, global temp dirs, or writable current directories unless you provision them explicitly.
- Honour platform-imposed timeouts by surfacing `--timeout` flags and by writing periodic progress logs to `stderr` so that CloudWatch / Stackdriver shows activity.
- Emit structured logs that comply with the shared observability baseline so that managed log routers can parse request IDs, correlation IDs, and severity levels.
- Do not require interactive authentication flows; support token injection (`AWS_PROFILE`, `AZURE_TENANT_ID`, etc.) or credential files suitable for automation.

---

> **Version**: 1.1.0
> **Last Amended**: 2026-01-10
