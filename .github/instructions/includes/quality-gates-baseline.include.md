# Quality Gates Baseline ✅

Use this shared baseline for quality gate execution expectations. Domain-specific instruction sets should list their canonical commands and reference these rules for how to run them.

**Identifier scheme.** Every normative rule carries a unique tag in the form `[QG-BASE-<prefix>-NNN]`, where the prefix maps to the containing section (for example `RUN` for Running, `DEF` for Defects, `SRC` for Sources). Use these identifiers when referencing, planning, or validating requirements.

---

## 1. Running rules 🏃

- [QG-BASE-RUN-001] Use repository-provided targets or scripts; avoid ad-hoc commands unless the spec requires it.
- [QG-BASE-RUN-002] If canonical targets do not exist, discover and run the project-approved equivalents.

## 2. Defect handling 🐛

- [QG-BASE-DEF-001] Iterate until all checks complete with **no errors or warnings**.
- [QG-BASE-DEF-002] Treat warnings as defects unless explicitly waived in an ADR (with rationale and expiry).

---

> **Version**: 1.0.1
> **Last Amended**: 2026-01-17
