---
agent: agent
description: Enforce repository-wide compliance with go.instructions.md
---

**Mandatory preparation:**

- Read the [constitution](../../.specify/memory/constitution.md) for non-negotiable rules, if you have not done already.
- Read the [Go instructions](../instructions/go.instructions.md).
- Reference identifiers (for example `[GO-QR-001]`) as you must assess compliance against each of them across the codebase and remediate any deviations.
- Read the [codebase overview instructions](../instructions/includes/codebase-overview-baseline.include.md) and adopt the approach for gathering supporting evidence.

## User Input ⌨️

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal 🎯

Enumerate every Go artefact in the repository, detect any discrepancies against `go.instructions.md`, plan the refactor/rework workstream, implement the required changes, and confirm compliance.

---

## Discovery (run before writing) 🔍

### A. Enumerate Go scope

1. Run `git ls-files '*.go'` (include glue files such as `go.mod`, `go.sum`, `Makefile`, `.golangci.yml`, `tools.go`, `go.work`, CI configs) to capture the full Go footprint.
2. Categorise each file into **CLI entrypoints**, **APIs/services**, **libraries/modules**, **tests**, **tooling/scripts**, or **configuration**.
3. Record locations that declare tooling (gofmt, golangci-lint, staticcheck, go test, CI workflows) to ensure the instructions apply consistently.

### B. Load enforcement context

1. Re-read the relevant sections of `go.instructions.md` for the surfaces present (CLI, API, Lambda, etc.).
2. Note any repository ADRs or docs that explicitly override defaults; if none exist, assume the instructions are fully binding.
3. Summarise uncertainties as **Unknown from code – verify {topic} with maintainers** before proceeding.

---

## Steps 👣

> **Note:** On subsequent runs, check whether artefacts from earlier executions (for example `docs/prompts/go-inventory.md`, `docs/prompts/go-instructions-alignment-plan.md`) already exist and parse them so progress is cumulative rather than duplicated.

### 1) Build the Go artefact matrix

1. Produce a table (for example in `docs/prompts/go-inventory.md`) listing each Go file or folder, its role, and the key instruction tags that apply.
2. Highlight high-risk areas (CLI entrypoints, HTTP handlers, concurrency, error handling, logging, tests) where divergence is most likely.

### 2) Detect discrepancies against instructions

1. For each artefact, scan for violations of the instruction tags (CLI contract, error handling, concurrency, observability, security, local-first tooling, etc.).
2. Assess each artefact and file against compliance of each reference identifier (for example `[GO-QR-001]`) from the `go.instructions.md` file.
3. Verify toolchain and local-first requirements per [GO-LCL-009]–[GO-LCL-016] (Go version pinning, go.mod/go.sum, gofmt, golangci-lint, staticcheck, race tests).
4. Capture findings with precise evidence links, formatted as `- Evidence: [path/to/file](path/to/file#L10-L40) — violates [GO-ERR-002] because ...`.
5. Record unknowns explicitly using **Unknown from code – {action}** (for example missing quality gates or undocumented runtime modes).

### 3) Plan refactoring and rework

1. Group findings into actionable workstreams (for example "CLI stream separation", "Error handling alignment", "Concurrency safety", "Structured logging", "Quality gate parity").
2. For each workstream, provide:
   - Objective
   - Files to touch (with justification)
   - Specific instruction tags they satisfy
   - Order of execution (prioritise safety-critical fixes first)
3. Store the plan in `docs/prompts/go-instructions-alignment-plan.md` for traceability.

### 4) Implement the changes (iterative, safe batches)

1. Execute the plan in small batches, keeping commits narrowly scoped and referencing instruction tags.
2. Prefer refactors that move logic into shared modules, enforce deterministic outputs, align CLI/APIs to contracts, and fix unsafe concurrency patterns.
3. Update docs, Makefiles, CI, and configuration to keep guidance, automation, and behaviour in sync.

### 5) Validate quality gates and behavioural parity

1. After each batch, run `make lint`, `make staticcheck`, and `make test`; if make targets do not exist, run the repository equivalents and follow the quality gates baseline per [GO-QG-001]–[GO-QG-005].
2. If additional checks exist (for example `make test-all`, `go test -race ./...`), run them when the touched areas require it.
3. Document failures and fixes in the plan file; unresolved issues must be tracked as blockers.

### 6) Summarise outcomes and next steps

1. Produce a final enforcement report (append to `docs/prompts/go-instructions-alignment-plan.md`) covering:
   - Resolved discrepancies (with references)
   - Remaining gaps / technical debt
   - Follow-up actions with owners and due dates
2. Confirm there are no lingering **Unknown from code** items; if any remain, convert them into explicit follow-ups.
3. Share the plan/report with maintainers (for example via PR description) to keep the team aligned.

---

## Output requirements 📋

- Use concrete evidence links for every finding or change request.
- Reference instruction identifiers (for example `[GO-ERR-001]`) when explaining discrepancies or fixes.
- Keep activities broken into the steps above; do not skip steps even if the code appears compliant.
- Prefer automation (linters, staticcheck, tests) over manual spot checks where feasible.
- Maintain ASCII-only text unless the repository already contains Unicode in the touched files.
- When information is missing, record **Unknown from code – {suggested action}** instead of guessing.

Context for prioritization: $ARGUMENTS

---

> **Version**: 1.0.0
> **Last Amended**: 2026-02-08
