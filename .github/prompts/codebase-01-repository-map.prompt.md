---
agent: agent
description: Build a repository map to document the architecture
---

**Mandatory preparation:** read [codebase overview](../instructions/include/codebase-overview.md) in full and follow strictly its rules before executing any step below.

Goal: create [repository map](../../../docs/codebase-overview/repository-map.md)

Steps:

1. Identify top-level folders and summarise what they contain.
2. Identify primary entry points (apps/services, main functions, server start-up, CLI entry points).
3. Identify build/deploy processes and artefacts (Makefile, Dockerfile, Terraform, respective GitHub workflows and actions, and CI/CD pipelines).
4. Identify key external dependencies (package manifests, lockfiles, major frameworks and libraries, languages and technologies, cloud managed services).
5. For each major statement, add **Evidence** section with file paths + symbols/config keys.

Write the file and keep it concise while preserving the evidence-first rule. Iterate, create a first draft, search for more evidence, then refine links and unknowns. Keep the document readable and practical; link from [codebase overview](../../../docs/codebase-overview/README.md).

---

> **Version**: 1.0.0
> **Last Amended**: 2026-01-04
