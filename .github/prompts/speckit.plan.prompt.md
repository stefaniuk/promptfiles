---
agent: speckit.plan
---

$ARGUMENTS

## Documentation (Mandatory)

When making architectural or significant technical decisions, document them as Architecture Decision Records (ADRs):

**What requires an ADR:**

- [ ] Architectural style choices (e.g. event-driven vs layered, monolith vs microservices)
- [ ] Architectural pattern choices (e.g. composition over inheritance, repository pattern, event sourcing)
- [ ] Language and framework selections
- [ ] Any other significant technical decision that shapes the system

**ADR requirements:**

- [ ] Use the template at [docs/adr/adr-template.md](../../docs/adr/adr-template.md)
- [ ] Follow the existing ADR format for consistency
- [ ] Always present 3 or more options with trade-offs
- [ ] Include the conversational context that led to the decision
- [ ] Document decisions regardless of whether you made them independently or were guided by the user

This requirement is mandatory, especially during the spec-driven development cycle: `spec` → `plan` → `tasks` → `implement`.

## Toolchain Version (Mandatory)

- [ ] Use the latest stable language, runtime, and framework versions at the time of change
- [ ] Pin versions in the repository (for example `.tool-versions`, `.python-version`, `.node-version`, `pyproject.toml` `requires-python`, `package.json` `engines`)
- [ ] Avoid floating `latest` tags; if blocked, document the reason and chosen version in an ADR

---

> **Version**: 1.0.0
> **Last Amended**: 2026-01-21
