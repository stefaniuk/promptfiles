---
agent: speckit.implement
---

$ARGUMENTS

Mandatory requirements:

- When tooling/ops/infrastructure is needed, consult the repository-template skill at `.github/skills/repository-template/SKILL.md` and check for existing or partial capability first
- Prefer extending existing template patterns over duplicating; only add missing pieces
- If adopting capabilities, follow the skill's critical integration rules (core make system first, include `scripts/init.mk`, `config::`, `.tool-versions`)
