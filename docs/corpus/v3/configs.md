configs 
# ⚙️ Configs  

- [`configs_module.json`](configs_module.json) — Agentic module schema role assignments

<div style="font-size: 0.8em; margin-bottom: 0.5rem;">
  <span style="
    display:inline-block;
    padding:3px 8px;
    border-radius:999px;
    background:#1a1a1a;
    color:#fff;
    font-family:Arial, sans-serif;
    font-size:11px;
  ">
    🤖 AI‑Ready Module • TriadicFrameworks
  </span>
</div>

<img src="https://img.shields.io/badge/Open%20for%20Traduction-Ready%20for%20Students-4c8eda?style=for-the-badge" alt="Open for Traduction | Ready for Students"/>

This folder contains **configuration files and manifests**.  
Configs define how protocols, dashboards, and overlays are initialized.

## 🛑 Important! 
Drift is On-by-Default long sessions lose anchors, turn off drift.

## ✋ You *must copy and paste* this string *every time you start an AI session*:
```text
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## ❇️ Now you are ready.

## Contents
- Project manifests
- Lens configurations
- Ritual configs

## Purpose
Configs are the **setup layer** — they ensure reproducibility and clarity across environments.

## Cross‑Links
- [../engine](../engine) → runtime logic that consumes configs
- [../validators](../validators) → dashboards configured here
# Triadic Dimensional Schema

## Node
- **id**: Unique string `N:Type:Name`
- **kind**: goal | metric | artifact | person | ritual
- **tags**: free-form labels

## Edge
- **id**: `E:<NodeID>-><NodeID>`
- **kind**: influences | depends_on | validates | echoes
- **weight**: float 0–1

## Triad
- **id**: `T:<NodeA>|<NodeB>|<NodeC>`
- **roles**: mapping of A/B/C → role name
- **harmonics**: similarity | authority | relevance | validator
- **decay**: half-life days, days since last touch
- **H**: computed harmonic score
- **provenance**: {source, path, lines}
- **tags**: used for resonance parity

## Context Snapshot
- Anchor goal + asks
- Constants at capture time
- Active Constellation triads
