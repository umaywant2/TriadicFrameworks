# RTT Tic-Tac-Toe Bot

## Purpose

RTT Tic-Tac-Toe is the **unit test bot** for the TriadicFrameworks suite.

It demonstrates that the RTT pipeline can emit a **fully structured**,  
**fully replayable**, **schema-valid**, and **triadic** JSON document for the  
smallest non-trivial perfect-information game.

This module is the **build gate**: if RTT cannot be made precise here,  
it cannot be trusted anywhere else.

---

## What this bot demonstrates

### ✔ Conformance  
Every position emits a JSON document that validates against  
`module_tic_tac_toe_schema.json`.

### ✔ Shared Envelope  
The bot emits the standard RTT envelope:

- `metadata`
- `timeline`
- `board` + `legal_moves`
- `lumen`
- `regime`
- `ancestry`
- `risk`
- `drift`
- `triadic_score`
- `winner`

### ✔ Replayability  
The timeline is hand-replayable and produces the exact board shown in the snapshot.  
Coordinates use **A1 = top-left**, **C3 = bottom-right**, row-major.

### ✔ Projection-loss  
The golden position shows a live choice where the current player (O) can:

- play **A3** → immediate win (local), or  
- misplay **B3** → projection-loss (hands X a future continuity win path)

### ✔ Continuity  
Threat-lines and ancestry show long-arc identity (win/draw/loss paths)  
even in a 3×3 grid.

### ✔ Regime  
Local / structural / continuity tags are meaningful even in tiny games  
and are enforced by Hephaestus.

---

## Files

- `module_tic_tac_toe.json`  
  Canonical module manifest: pipeline, operators, golden example.

- `module_tic_tac_toe_schema.json`  
  JSON Schema for the StateEmitter output.  
  Validates the **snapshot** (`board`, `legal_moves`, `lumen`, `regime`, etc.)  
  and the shared envelope.

- `golden/example_input.txt`  
  The exact 7‑ply sequence used to produce the golden state.  
  Replayable by hand and consistent with turn parity.

- `golden/example.json`  
  The full triadic state for the position, including:
  - timeline (move history)
  - snapshot (`board`, `legal_moves`)
  - structural extraction
  - regime proportions
  - ancestry
  - risk
  - drift
  - triadic score (with published Harmonia weights)
  - winner (null for this position)

This file **conforms to the schema** and is the reference fixture for the suite.

---

## Pipeline (v2)

1. **Input**  
   - timeline (ply, coord, player)  
   - 3×3 board derived from timeline  
   - next player  
   - coordinate system: `A1` top-left → `C3` bottom-right

2. **Lumen**  
   - detect winning lines  
   - detect threat lines  
   - detect fork opportunities

3. **Hephaestus**  
   - tag each legal move as `local`, `structural`, or `continuity`  
   - compute regime proportions  
   - enforce `local + structural + continuity = 1.0`

4. **Aurion**  
   - classify ancestry (win/draw/loss paths)

5. **Harmonia**  
   - compute numeric triadic scores using published weights  
   - derive `final` from those weights

6. **StateEmitter**  
   - emit the shared RTT envelope  
   - validate against `module_tic_tac_toe_schema.json`

---

## Scope

- No external engine  
- No randomness  
- No hidden information  
- No pruning or heuristics  
- No UI contract beyond the schema  
- Full enumeration only

This bot is the **reference conformance fixture** for RTT.

Once this module is wired to SuperGrok Build, the suite has its first  
**executable triadic bot**, and all other bots (Collatz, Go, Observer, Session, etc.)  
follow its envelope.
