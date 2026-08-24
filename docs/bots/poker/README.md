# RTT Poker Bot

## Purpose

The Poker Bot is RTT’s **uncertainty engine**.

It does not solve poker.  
It does not compute EV.  
It does not run a solver.

Instead:

> **Poker watches betting lines under hidden information and emits triadic identity across pressure, continuity, and bluff/value lineage.**

This makes Poker the RTT module for:

- bluff continuity  
- pressure resonance  
- range topology  
- collapse signatures  
- projection-loss  
- ancestry of betting lines  
- drift of identity under uncertainty  
- unified triadic scoring  

## What Poker Teaches

- **Continuity:** bluff/value long-arc identity  
- **Resonance:** pressure from pot geometry + stack depth  
- **Topology:** range compression, pressure nodes  
- **Ancestry:** lineage of betting sequences  
- **Drift:** directional flow of betting identity  
- **Collapse:** sudden line failure  
- **Projection-loss:** bluff inversion  
- **Triadic identity:** unified Harmonia score for the hand  

## Files

### `module_poker.json`
Expanded manifest: pipeline, operators, overlays, scoring weights, golden example.

### `module_poker_schema.json`
Full JSON Schema for the StateEmitter output.

### `golden/example_input.txt`
A betting-line sequence.

### `golden/example.json`
Full triadic state for that hand.

## Pipeline (v1)

1. **Input:** poker state JSON  
2. **Lumen:** structural extraction  
3. **Hephaestus:** regime classification  
4. **Aurion:** collapse + projection-loss  
5. **Harmonia:** triadic identity  
6. **StateEmitter:** JSON matching `module_poker_schema.json`

## Scope

- No solver  
- No EV calculation  
- Pure RTT uncertainty identity  
- Full triadic overlays  

Poker is the RTT module that proves triadic identity in **hidden-information, pressure-driven play**.
