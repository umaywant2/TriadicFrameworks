# RTT Chess Bot

## Purpose

The Chess Bot is RTT’s **deterministic structural engine**.

It does not run Stockfish.  
It does not compute centipawn loss.  
It does not evaluate tactics.

Instead:

> **Chess watches structure, initiative, tension, and continuity — and emits triadic identity across deterministic positional play.**

This makes Chess the RTT module for:

- initiative drift  
- structural regimes  
- tension resonance  
- pawn-structure topology  
- collapse signatures  
- projection-loss  
- ancestry of plans  
- unified triadic scoring  

## What Chess Teaches

- **Continuity:** long-arc plan identity  
- **Resonance:** pressure from tension and king safety  
- **Topology:** pawn structure, tension graph, king safety graph  
- **Ancestry:** lineage of plans and structural regimes  
- **Drift:** directional flow of initiative  
- **Collapse:** sudden structural failure  
- **Projection-loss:** identity inversion under forcing lines  
- **Triadic identity:** unified Harmonia score for the position  

## Files

### `module_chess.json`
Expanded manifest: pipeline, operators, overlays, scoring weights, golden example.

### `module_chess_schema.json`
Full JSON Schema for the StateEmitter output.

### `golden/example_input.fen`
A chess position.

### `golden/example.json`
Full triadic state for that position.

## Pipeline (v1)

1. **Input:** chess state JSON  
2. **Lumen:** structural extraction  
3. **Hephaestus:** regime classification  
4. **Aurion:** collapse + projection-loss  
5. **Harmonia:** triadic identity  
6. **StateEmitter:** JSON matching `module_chess_schema.json`

## Scope

- No engine  
- No centipawn evaluation  
- Pure RTT positional identity  
- Full triadic overlays  

Chess is the RTT module that proves triadic identity in **deterministic structural play**.
