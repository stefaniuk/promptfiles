---
agent: agent
description: Document key runtime flows with diagrams
---

**Mandatory preparation:** read [codebase overview](../instructions/include/codebase-overview.md) in full and follow strictly its rules before executing any step below.

Goal: create [runtime flows](../../../docs/codebase-overview/runtime-flow-*.md)

Steps:

1. Identify 3-6 critical user/system flows (for example login, create/update entity, scheduled/background job, ingestion pipeline).
2. For each flow, create `docs/codebase-overview/runtime-flow-[XXX]-[name].md` covering:
   - A short narrative covering the trigger, main steps, and outcome.
   - A Mermaid sequence diagram of the collaborating components.
   - Error handling, retries, and idempotency notes where the code documents them.
   - Evidence section (file paths + symbols/config keys).
3. Mark anything unclear as **Unknown from code** so it can be verified later.
4. Write the file and keep it concise while preserving the evidence-first rule.
5. Iterate, create a first draft, search for more evidence, then refine links and unknowns while keeping the document readable and practical
6. Update [codebase overview](../../../docs/codebase-overview/README.md) with a **Runtime Flows** section linking to every flow document.

---

> **Version**: 1.0.0
> **Last Amended**: 2026-01-04
