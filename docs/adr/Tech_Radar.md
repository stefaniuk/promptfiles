# Tech Radar

## Python tech stack

- Python and dependency management: `uv`
- Linting and formatting: `ruff`
- Type checking: `mypy`
- Testing: `pytest`
- Logging: `structlog` or `Powertools for AWS Lambda`
- CLI argument parsing: `typer`

## TypeScript tech stack

- TypeScript and dependency management: Node.js (LTS) and `pnpm`
- Linting and formatting: `biome`
- Type checking: `tsc`
- Testing: `vitest`
- Logging: `winston` or `Powertools for AWS Lambda`
- CLI argument parsing: `commander`

Note: Selecting any default tool above still requires an ADR that compares and assesses at least two or three popular alternatives using the [ADR template](./ADR-nnn_Any_Decision_Record_Template.md).

---

> **Version**: 1.0.0
> **Last Amended**: 2026-01-29
