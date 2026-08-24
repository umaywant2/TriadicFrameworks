# RTT Tic-Tac-Toe Bot

## Purpose

RTT Tic-Tac-Toe is the **unit test bot** for the TriadicFrameworks suite.

It exists to prove that the RTT pipeline:

- Lumen → Hephaestus → Aurion → Harmonia → StateEmitter

can be made **fully explicit**, **fully enumerable**, and **fully JSON‑emitting** on the smallest non‑trivial game tree.

## What this bot teaches

- **Conformance:** every position can be evaluated into a triadic JSON document.
- **Projection-loss:** you can *see* when a move collapses a winning line into a forced loss.
- **Continuity:** even in a 3×3 grid, there is a long‑arc identity (win/draw/loss ancestry).
- **Regime:** 1/3 local, 2/3 structural, 3/3 continuity is meaningful even in tiny games.

## Files

- `module_tic_tac_toe.json`  
  Canonical module manifest: pipeline, operators, golden example.

- `module_tic_tac_toe_schema.json`  
  JSON Schema for the StateEmitter output.

- `golden/example_input.txt`  
  A single Tic-Tac-Toe position (board + next player).

- `golden/example.json`  
  The full triadic state for that position, conforming to the schema.

## Pipeline (v1)

1. **Input:** 3×3 board + next player.
2. **Lumen:** detect winning lines, threat lines, fork opportunities.
3. **Hephaestus:** tag each legal move as local / structural / continuity.
4. **Aurion:** classify ancestry of lines (win/draw/loss paths).
5. **Harmonia:** compute numeric triadic scores (local, structural, continuity, final).
6. **StateEmitter:** emit JSON matching `module_tic_tac_toe_schema.json`.

## Scope

- No external engine.
- No randomness.
- No hidden information.
- No UI contract beyond the schema.

This bot is the **reference conformance fixture**: if RTT cannot be made precise here, it cannot be trusted anywhere else.

Once this module is wired to SuperGrok Build, the suite has its first **executable triadic bot**.
