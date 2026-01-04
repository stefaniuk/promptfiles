---
agent: agent
description: Create component-level summaries
---

**Mandatory preparation:** read [codebase overview](../instructions/include/codebase-overview.md) in full and follow strictly its rules before executing any step below.

Goal: create [component catalogue](../../../docs/codebase-overview/component-*.md)

Steps:

1. From [repository map](../../../docs/codebase-overview/repository-map.md), pick the 7-12 most important components or modules (services, bounded areas, packages).
2. For each component, create `docs/codebase-overview/component-[XXX]-[name].md` covering:
   - Purpose
   - Responsibilities
   - Key modules/symbols
   - Key inbound/outbound interfaces (HTTP routes, messaging topics, queues, events)
   - Data structures and data stores used
   - Config and feature flags (if any)
   - Observability (logging/metrics/tracing)
   - Evidence section (file paths + symbols/config keys)
3. Write the file and keep it concise while preserving the evidence-first rule.
4. Iterate, create a first draft, search for more evidence, then refine links and unknowns while keeping the document readable and practical
5. Update [codebase overview](../../../docs/codebase-overview/README.md) with a **Component Catalogue** section linking to every component document.

---

> **Version**: 1.0.0
> **Last Amended**: 2026-01-04
