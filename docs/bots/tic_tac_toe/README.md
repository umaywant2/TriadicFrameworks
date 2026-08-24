# RTT Tic-Tac-Toe Bot

## Purpose

RTT Tic-Tac-Toe is the **unit test bot** for the TriadicFrameworks suite.

It proves that the RTT pipeline can emit a **fully structured**, **fully replayable**,  
**schema-valid**, and **triadic** JSON document for the smallest non-trivial game tree.

This module is the **build gate**: if RTT cannot be made precise here,  
it cannot be trusted anywhere else.

---

## What this bot demonstrates

- **Conformance:** every position emits a JSON document that validates against  
  `module_tic_tac_toe_schema.json`.

- **Shared Envelope:** the bot emits the standard RTT envelope:
  - `metadata`
  - `timeline`
  - `board` + `legal_moves`
  - `lumen`
  - `regime`
  - `ancestry`
  - `risk`
  - `drift`
  - `triadic_score`

- **Replayability:** the timeline is hand-replayable and produces the exact board  
  shown in the `state` snapshot.

- **Projection-loss:** moves like `C3` demonstrate collapse and projection-loss  
  even in a 3×3 grid.

- **Continuity:** threat-lines and ancestry show long-arc identity  
  (win/draw/loss paths).

- **Regime:** local / structural / continuity tags are meaningful even in tiny games.

---

## Files

- `module_tic_tac_toe.json`  
  Canonical module manifest: pipeline, operators, golden example.

- `module_tic_tac_toe_schema.json`  
  JSON Schema for the StateEmitter output.  
  Validates the **snapshot** (`board`, `legal_moves`, `lumen`, `regime`, etc.).

- `golden/example_input.txt`  
  The exact 7-ply sequence used to produce the golden state.  
  Replayable by hand.

- `golden/example.json`  
  The full triadic state for the position, including:
  - timeline (the move history),
  - snapshot (`board`, `legal_moves`),
  - structural extraction,
  - regime proportions,
  - ancestry,
  - risk,
  - drift,
  - triadic score.

  This file **conforms to the schema** and is the reference fixture for the suite.

---

## Pipeline (v2)

1. **Input:**  
   - 3×3 board  
   - next player  
   - optional timeline

2. **Lumen:**  
   - detect winning lines  
   - detect threat lines  
   - detect fork opportunities

3. **Hephaestus:**  
   - tag each legal move as `local`, `structural`, or `continuity`  
   - compute regime proportions

4. **Aurion:**  
   - classify ancestry (win/draw/loss paths)

5. **Harmonia:**  
   - compute numeric triadic scores  
   - enforce `local + structural + continuity = 1.0`

6. **StateEmitter:**  
   - emit the shared RTT envelope  
   - validate against `module_tic_tac_toe_schema.json`

---

## Scope

- No external engine  
- No randomness  
- No hidden information  
- No UI contract beyond the schema  
- No pruning or heuristics — full enumeration only

This bot is the **reference conformance fixture** for RTT.

Once this module is wired to SuperGrok Build, the suite has its first  
**executable triadic bot**, and all other bots (Collatz, Go, Observer, Session, etc.)  
follow its envelope.
