# RTT Bots Registry

The **Bots** directory contains all RTT engines that interpret structure, drift, continuity, collapse, projection‑loss, and ancestry across different domains.

Each bot is a self‑contained module with:

- a manifest (`module_<bot>.json`)
- a schema (`module_<bot>_schema.json`)
- a golden example (`golden/example.json`)
- a golden input (`golden/example_input.txt`)
- a README describing the bot’s purpose

This directory is the **index** for all bots.

## Purpose

The Bots Registry provides:

- a unified catalog of all RTT bots  
- metadata for discovery and navigation  
- cross‑module lineage  
- triadic categorization  
- integration surfaces for engines and pipelines  

## Bots Included

- **archive** — temporal identity across snapshots  
- **arrival_substrate_model** — substrate‑level arrival dynamics  
- **backgammon** — race geometry, prime topology, collapse  
- **checkers** — ladder topology, king routes, capture nets  
- **chess** — deterministic structure, tension, continuity arcs  
- **collatz** — regime cycling (S/E/R), collapse, projection‑loss  
- **go** — influence fields, territory resonance, shape ancestry  
- **hanabi** — hidden‑information continuity, hint resonance  
- **moderation** — signal extraction, collapse, projection‑loss  
- **observer** — meta‑bot for cross‑module state watching  
- **poker** — pressure resonance, bluff continuity, range compression  
- **session** — multi‑bot session identity  
- **tic_tac_toe** — minimal triadic engine  
- **validator** — manifest/schema/golden validation  

## Files

### `module_bots.json`
Registry manifest listing all bots and their metadata.

### `module_bots_schema.json`
Schema for the registry manifest.

### `README.md`
This file.

