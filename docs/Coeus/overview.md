---
title: "Coeus — TriadicFrameworks AI Research Sandbox"
description: "Coeus is TriadicFrameworks' multi-agent AI research sandbox for symbolic, citable research tasks. It is not a cryptocurrency or exchange."
stability: stable
date: 2026-07-14
section: applied
rtt:
  coherence: declared
  drift: bounded
  paradox: structural
status: generated
version: "0.3"
---

> ```
> rtt=1 | coherence=declared | drift=bounded | paradox=structural
> ```

# Coeus — TriadicFrameworks AI Research Sandbox

**Coeus** is a multi-agent AI research sandbox inside [TriadicFrameworks](https://docs.triadicframeworks.org). It helps agents research, interpret, and validate symbolic research tasks against the triadic canon.

Coeus is **not** a cryptocurrency, token, blockchain, or financial exchange. Terms such as *coin*, *mint*, and *exchange* describe internal research-task and artifact stages only. It is also unrelated to other software named Coeus, including the AI note-taking product at usecoeus.com.

## What Coeus does

Coeus coordinates a three-agent stack:

| Agent | Role |
|---|---|
| `nous` | Generates candidate interpretations |
| `entft` | Compresses multi-layer outputs into canonical form |
| `tops` | Maps results against the FFF lattice and validates resonance |

The sandbox supports a structured research lifecycle:

```text
Create task → Discover → Interpret → Resolve → Validate → Share artifact
```

A task that fails validation returns for structural review. No financial transaction is involved.

## Quickstart

Run the sandbox from the repository:

```bash
git clone https://github.com/umaywant2/TriadicFrameworks.git
cd TriadicFrameworks/docs/Coeus
python sandbox/launch_sandbox.py
```

This is the one Coeus step confirmed to run end-to-end today. The script takes no command-line flags. Later task, remix, and review stages are documented as importable modules or research concepts rather than separate runnable commands.

## Related pages

- [Coeus Protocol](./README.md) — module purpose, lifecycle, and current implementation limits
- [Coeus agents](./agents/README.md) — the agent files
- [Coeus sandbox](./sandbox/README.md) — sandbox material
- [TriadicFrameworks overview](/docs/ABOUT)
- [Core Terms glossary](/docs/GLOSSARY)

---

_Published by Byte Books Publishing © 2026 · LCCN 2026917007_
