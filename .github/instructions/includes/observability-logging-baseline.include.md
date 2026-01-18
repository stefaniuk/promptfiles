# Observability Logging Baseline 🔭

Use this shared baseline checklist for any runtime that produces structured logs (services, CLIs, workers, UI backends). Instruction sets must link here so log expectations change in **one** place.

**Identifier scheme.** Every normative rule carries a unique tag in the form `[OBS-<prefix>-NNN]`, where the prefix maps to the containing section (for example `SVC` for Services, `CLI` for CLIs, `SEC` for Secrecy, `TAX` for Taxonomy, `DIA` for Diagnostics, `TST` for Testing). Use these identifiers when referencing, planning, or validating requirements.

---

## 1. Required fields (services, APIs, async workers) 📡

Every structured log emitted around a request/task boundary must include:

- [OBS-SVC-001] `timestamp` (UTC, ISO 8601)
- [OBS-SVC-002] `level`
- [OBS-SVC-003] `service` / `component`
- [OBS-SVC-004] `environment` (dev/stage/prod)
- [OBS-SVC-005] `version` / `build_sha`
- [OBS-SVC-006] `request_id` / `correlation_id` (when available)
- [OBS-SVC-007] `trace_id` / `span_id` (when tracing is enabled)
- [OBS-SVC-008] `operation` / `route` / `use_case`
- [OBS-SVC-009] `status` / `outcome`
- [OBS-SVC-010] `duration_ms`
- [OBS-SVC-011] `error_code` (for failures)
- [OBS-SVC-012] `exception.type` and `exception.stack` (servers only, never in user-facing output)

## 2. Required fields (CLIs) ⌨️

For CLI invocations (especially long-running ones):

- [OBS-CLI-001] `timestamp`, `level`
- [OBS-CLI-002] `command` / `subcommand`
- [OBS-CLI-003] `args` (sanitised)
- [OBS-CLI-004] `cwd`
- [OBS-CLI-005] `request_id` / `invocation_id` (generate if not provided)
- [OBS-CLI-006] `duration_ms`
- [OBS-CLI-007] `exit_code`
- [OBS-CLI-008] `mode` / `target_env` when applicable

## 3. Sensitive data & secrecy rules 🔒

- [OBS-SEC-001] Never log secrets, API tokens, passwords, raw personal data, or full payloads unless the specification explicitly calls for it **and** data is masked/anonymised.
- [OBS-SEC-002] When capturing identifiers, prefer hashed/truncated forms unless the value is already public.
- [OBS-SEC-003] Classify and scrub structured fields before logging (for example `user_email` → masked).
- [OBS-SEC-004] Treat log files as production data: enforce retention, access control, and scrubbing policies consistently.

## 4. Event naming & taxonomy 🏷️

- [OBS-TAX-001] Use stable, lower-kebab or dot-delimited event names (for example `request.start`, `request.end`, `dependency.call`, `dependency.error`).
- [OBS-TAX-002] Emit both `*.start` and `*.end` (or success/failure) events around expensive boundaries to aid tracing without full distributed tracing support.
- [OBS-TAX-003] Capture dependency metadata: host, target, attempt, timeout, retry count.
- [OBS-TAX-004] Include `severity_reason` / `alert_hint` in error events that should page SRE/on-call teams.

## 5. Diagnostics & sampling 🔬

- [OBS-DIA-001] Default logging level for services is `info`; enable `debug` only when explicitly requested (flag/env var) and clearly documented.
- [OBS-DIA-002] When verbose or debug logging is enabled, emit a single function/method entry log for **every** call path, capturing the operation name and a sanitised summary of arguments (masking or omitting anything covered by §3). This keeps diagnostic runs self-explanatory without leaking secrets.
- [OBS-DIA-003] For noisy components, support sampling (for example only log 1/N successes but 100% of errors).
- [OBS-DIA-004] When sampling, log the sampling rate so downstream systems can extrapolate.
- [OBS-DIA-005] Keep log size bounded: truncate oversized payloads with a clear `truncated=true` flag.
- [OBS-DIA-006] Every exception, whether the software can recover or not, must trigger exactly one `ERROR`-level log entry that includes the `error_code`, correlation identifiers, and (server-side only) the stack trace; never downgrade exception logs just because the failure was handled.

## 6. Testing & validation 🧪

- [OBS-TST-001] Add regression tests (unit/integration) that assert the presence of key fields for representative success and failure cases.
- [OBS-TST-002] Lint or schema-validate structured logs where tooling exists (for example JSON schema, OpenTelemetry log schemas).
- [OBS-TST-003] Document log schemas/runbooks alongside the service so operators know how to search and interpret events.

---

> **Version**: 1.2.2
> **Last Amended**: 2026-01-17
