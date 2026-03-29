configs 
# ⚙️ Configs

This folder contains **configuration files and manifests**.  
Configs define how protocols, dashboards, and overlays are initialized.

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