# AI-assisted Codebase Overview

This document describes a practical, repeatable workflow for producing a codebase overview for a large codebase.

---

## Goals

Produce a codebase overview that is:

- Grounded in the codebase (no guessing or invented architecture)
- Incremental ("build summaries as it goes")
- Easy to navigate (repo map, component catalogue, runtime flows)
- Easy to keep up to date (repeatable prompts)

---

## Output structure (create these files/folders)

Create the following:

- `docs/architecture/`
  - `architecture-overview.md`
  - `repo-map.md`
  - `glossary.md`
  - `components/`
  - `flows/`
  - `decisions/` (optional, for ADRs)

Recommended minimum set:

- `docs/architecture/architecture-overview.md`
- `docs/architecture/repo-map.md`
- `docs/architecture/components/` (one file per major component)
- `docs/architecture/flows/runtime-flows.md`

---

## Copilot instruction file (make behaviour consistent)

Create this file:

- `.github/copilot-instructions.md`

Paste this content:

```md
# Copilot instructions (architecture documentation)

You are producing a design overview for this codebase.

Hard rules

- Stay grounded in the repository. If you are unsure, say "Unknown from code" and list what you would need to check.
- Prefer evidence: reference file paths and symbols (functions/classes/config keys). Do not invent components.
- Work iteratively: write/update Markdown files under docs/architecture/ as you learn more.
- Keep language simple and use British English.
- Avoid reading huge files end-to-end. Use workspace search to find entry points, then read only relevant sections.
- Exclude generated/vendor folders (e.g. node_modules, dist, build, coverage, .venv, vendor).
- Every time you add a claim to the architecture docs, include at least one "Evidence" bullet pointing to code locations.

Output style

- Use headings, short paragraphs, and bullet lists.
- Where helpful, use Mermaid diagrams in Markdown.
```

---

## Prompt files (repeatable passes)

Create a folder:

- `.github/prompts/`

Then add the following prompt files.

### 1) Repo map prompt

File:

- `.github/prompts/01-repo-map.prompt.md`

Content:

```md
---
description: Build a repo map for architecture documentation
---

Using workspace context, create docs/architecture/repo-map.md.

Steps:

1. Identify top-level folders and what they contain.
2. Identify primary entry points (apps/services, main functions, server startup, CLI entry points).
3. Identify build/deploy artefacts (Dockerfile, Helm, Kubernetes manifests, Terraform, pipelines).
4. Identify key external dependencies (package manifests, lockfiles, major libraries).
5. For each major statement, add "Evidence:" bullets with file paths + symbols/config keys.

Write the file and keep it concise.
```

### 2) Component catalogue prompt

File:

- `.github/prompts/02-component-catalogue.prompt.md`

Content:

```md
---
description: Create component-level summaries and link them from the overview
---

Goal: build docs/architecture/components/\*.md and link them from docs/architecture/architecture-overview.md.

Process:

1. From repo-map.md, pick the 5–15 most important components/modules (services, bounded areas, packages).
2. For each, create docs/architecture/components/<name>.md with:
   - Purpose
   - Responsibilities
   - Key modules/symbols
   - Key inbound/outbound interfaces (HTTP routes, messaging topics, queues, events)
   - Data stores used
   - Config and feature flags (if any)
   - Observability (logging/metrics/tracing)
   - Evidence section (file paths + symbols/config keys)
3. Update architecture-overview.md to include a "Component catalogue" section linking to each file.

Do this iteratively: create a first draft, then refine after searching for more evidence.
```

### 3) Runtime flows prompt

File:

- `.github/prompts/03-runtime-flows.prompt.md`

Content:

```md
---
description: Document key runtime flows with evidence and diagrams
---

Create docs/architecture/flows/runtime-flows.md.

1. Identify 3–6 critical user/system flows (e.g. login, create/update entity, background job, ingestion pipeline).
2. For each flow:
   - A short narrative (what happens)
   - Mermaid sequence diagram
   - Error handling / retries / idempotency notes (if present in code)
   - Evidence: file paths + symbols + config keys
3. Where you are not sure, mark "Unknown from code".

Keep it readable and practical.
```

---

## How to run in VS Code

1. Open **Copilot Chat**.
2. Switch to **Agent** mode (so it can search the workspace and write files).
3. Select **GPT-5.1-Codex** in the model picker.
4. Run the prompt files in this order:
   - `01-repo-map`
   - `02-component-catalogue`
   - `03-runtime-flows`

Expected working pattern:

- Search the workspace for entry points and key modules
- Read only the relevant sections of code/config
- Write/update Markdown under `docs/architecture/`
- Repeat until each artefact is solid

---

## Quality controls (prevents "architecture fiction")

Apply these checks as you go:

- Evidence-first rule
  No architecture claim without an "Evidence" bullet that points to file paths and symbols/config keys.

- Unknowns list
  Keep a section in `docs/architecture/architecture-overview.md` called **Unknowns / to verify**.

- Scope boundaries
  Each component document should state what it _does_ and what it _does not_ own.

- Assumption audit
  After each pass, ask the agent:

  - "List the top 20 assumptions you made. For each, provide evidence or mark ‘Unknown from code’."

- Ignore noise
  Ensure vendor and generated artefacts are excluded (e.g. `node_modules`, `dist`, `.venv`, `build`, `coverage`).

---

## Suggested outline for architecture-overview.md

After the component pass, ensure `docs/architecture/architecture-overview.md` contains:

- Purpose of the system
- High-level architecture (short summary)
- Component catalogue (links to `components/*.md`)
- Key interfaces (HTTP, messaging, scheduled jobs)
- Data storage overview
- Deployment and runtime (how it runs in environments)
- Observability (logs/metrics/traces)
- Security and access (authn/authz, secrets, boundaries)
- Operational concerns (scaling, failure modes, DR)
- Unknowns / to verify
- Glossary link

---

## Optional next passes

Once the basics are in place, add one or more of these:

- C4-style diagrams (Context / Container / Component) using Mermaid
- ADRs for key decisions (write into `docs/architecture/decisions/`)
- Threat model sketch (trust boundaries + key risks)
- Tech debt register (grounded in issues and code hotspots)

---

## Done criteria

You are "done" when:

- `repo-map.md` lets a new engineer find the main moving parts quickly
- Each component file clearly explains responsibilities and interfaces with evidence
- `runtime-flows.md` covers the most important flows and failure cases
- `architecture-overview.md` reads coherently end-to-end and links to everything
- Unknowns are explicitly listed, not guessed
