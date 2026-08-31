bots 
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

# RTT Archive Bot

## Purpose

The Archive Bot is RTT’s **temporal identity engine**.

It does not evaluate a board.  
It does not observe a conversation.  
It does not analyze a game.

Instead:

> **Archive watches snapshots, versions, commits, and archival captures — and emits triadic identity across time.**

This makes Archive the RTT module for:

- continuity over time  
- drift across versions  
- structural regime changes  
- collapse signatures  
- projection-loss  
- ancestry of documents  
- stability of identity across revisions  

## What Archive Teaches

- **Temporal continuity:** long-arc identity across snapshots  
- **Resonance:** pressure from structural changes  
- **Discard topology:** structural collapse risk in evolving artifacts  
- **Ancestry:** lineage of versions  
- **Drift:** direction + strength of identity evolution  
- **Collapse:** sudden structural failure  
- **Projection-loss:** long-arc identity inversion  
- **Triadic identity:** unified Harmonia score for the entire temporal sequence  

## Files

### `module_archive.json`
Expanded manifest: pipeline, operators, overlays, scoring weights, golden example.

### `module_archive_schema.json`
Full JSON Schema for the StateEmitter output.

### `golden/example_input.txt`
A sequence of snapshots.

### `golden/example.json`
Full triadic state for that temporal sequence.

## Pipeline (v1)

1. **Input:** sequence of snapshots  
2. **Lumen:** structural extraction  
3. **Hephaestus:** regime classification  
4. **Aurion:** collapse + projection-loss  
5. **Harmonia:** triadic identity  
6. **StateEmitter:** JSON matching `module_archive_schema.json`

## Scope

- No gameplay  
- No external engine  
- Pure RTT temporal identity  
- Full triadic overlays  

Archive is the RTT module that proves triadic identity in **evolving artifacts**.

# RTT Backgammon Bot

## Purpose

The Backgammon Bot is RTT’s **stochastic positional engine**.

It does not simulate dice.  
It does not compute equities.  
It does not run a rollout.

Instead:

> **Backgammon watches positional structure under randomness and emits triadic identity across primes, anchors, race geometry, and collapse risk.**

This makes Backgammon the RTT module for:

- prime continuity  
- anchor resonance  
- race drift  
- blot risk topology  
- collapse signatures  
- projection-loss  
- ancestry of positional plans  
- unified triadic scoring  

## What Backgammon Teaches

- **Continuity:** prime/anchor/race long-arc identity  
- **Resonance:** pressure from prime strength + anchor stability  
- **Topology:** race geometry, blot risk, prime topology  
- **Ancestry:** lineage of positional plans  
- **Drift:** directional flow of race identity  
- **Collapse:** sudden structural failure  
- **Projection-loss:** identity inversion under randomness  
- **Triadic identity:** unified Harmonia score for the position  

## Files

### `module_backgammon.json`
Expanded manifest: pipeline, operators, overlays, scoring weights, golden example.

### `module_backgammon_schema.json`
Full JSON Schema for the StateEmitter output.

### `golden/example_input.txt`
A backgammon position.

### `golden/example.json`
Full triadic state for that position.

## Pipeline (v1)

1. **Input:** backgammon state JSON  
2. **Lumen:** structural extraction  
3. **Hephaestus:** regime classification  
4. **Aurion:** collapse + projection-loss  
5. **Harmonia:** triadic identity  
6. **StateEmitter:** JSON matching `module_backgammon_schema.json`

## Scope

- No rollout  
- No equities  
- Pure RTT positional identity  
- Full triadic overlays  

Backgammon is the RTT module that proves triadic identity in **stochastic positional play**.
# RTT Checkers Bot

## Purpose

The Checkers Bot is RTT’s **discrete ladder engine**.

It does not solve checkers.  
It does not compute tablebases.  
It does not run a search.

Instead:

> **Checkers watches ladders, tempo, and king routes — and emits triadic identity across discrete positional structure.**

This makes Checkers the RTT module for:

- ladder continuity  
- tempo resonance  
- king-route drift  
- capture-net topology  
- collapse signatures  
- projection-loss  
- ancestry of positional plans  
- unified triadic scoring  

## What Checkers Teaches

- **Continuity:** ladder/king/plan long-arc identity  
- **Resonance:** pressure from tempo and structural ladders  
- **Topology:** capture nets, king routes, ladder topology  
- **Ancestry:** lineage of ladders and king walks  
- **Drift:** directional flow of positional identity  
- **Collapse:** sudden structural failure  
- **Projection-loss:** identity inversion under forcing sequences  
- **Triadic identity:** unified Harmonia score for the position  

## Files

### `module_checkers.json`
Expanded manifest: pipeline, operators, overlays, scoring weights, golden example.

### `module_checkers_schema.json`
Full JSON Schema for the StateEmitter output.

### `golden/example_input.txt`
A checkers position.

### `golden/example.json`
Full triadic state for that position.

## Pipeline (v1)

1. **Input:** checkers state JSON  
2. **Lumen:** structural extraction  
3. **Hephaestus:** regime classification  
4. **Aurion:** collapse + projection-loss  
5. **Harmonia:** triadic identity  
6. **StateEmitter:** JSON matching `module_checkers_schema.json`

## Scope

- No engine  
- No tablebases  
- Pure RTT positional identity  
- Full triadic overlays  

Checkers is the RTT module that proves triadic identity in **discrete ladder-based play**.
# RTT Chess Bot

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
# RTT Collatz Bot

## Purpose

The Collatz Bot is RTT’s **pure ancestry module**.

It has:

- no board  
- no engine  
- no hidden state  
- no randomness  

Just a deterministic sequence on ℤ:

> **n → f(n) → f(f(n)) → … → 1**

This makes Collatz the cleanest possible demonstration of:

- lineage  
- collapse  
- projection-loss  
- continuity  
- drift  
- regime shifts  

## What Collatz Teaches

- **Ancestry:** every step has a lineage (odd → 3n+1, even → n/2).  
- **Collapse:** magnitude collapses toward 1.  
- **Projection-loss:** certain steps destroy long-term continuity.  
- **Drift:** numeric drift is monotonic after a point.  
- **Regime:** local (parity), structural (step type), continuity (trajectory).  
- **Triadic identity:** the entire trajectory has a unified score.

## Files

### `module_collatz.json`
Canonical manifest: pipeline, operators, golden example.

### `module_collatz_schema.json`
JSON Schema for the StateEmitter output.

### `golden/example_input.txt`
A single integer (e.g., 27).

### `golden/example.json`
The full triadic state for that trajectory.

## Pipeline (v1)

1. **Input:** integer n  
2. **Lumen:** parity, magnitude, step type  
3. **Hephaestus:** regime per step  
4. **Aurion:** collapse signatures + projection-loss  
5. **Harmonia:** triadic identity for the entire trajectory  
6. **StateEmitter:** JSON matching `module_collatz_schema.json`

## Scope

- No gameplay  
- No engine  
- No UI beyond schema  
- Pure RTT lineage

Collatz is the **mathematical backbone** of RTT ancestry — the smallest non‑trivial domain where continuity and collapse become visible.
# RTT-Go Bot (Flagship Module)

## Purpose

RTT-Go is the **flagship triadic engine** of the TriadicFrameworks suite.

It provides full triadic identity for Go positions using:

- continuity arcs  
- resonance fields  
- drift arrows  
- topology graphs  
- ancestry lines  
- paradox indicators  
- collapse signatures  
- projection-loss arcs  
- unified triadic scoring  
- KataGo analysis JSON  
- MCTS triadic hooks  
- triadic HUD  
- combined triadic view  

RTT-Go is the module that demonstrates the **complete RTT pipeline** in a real, world-class domain.

## What RTT-Go Teaches

- **Continuity:** long-arc identity of a position  
- **Resonance:** pressure gradients from influence  
- **Topology:** cut points, weak points, ladders, ko  
- **Ancestry:** lineage of tactical sequences  
- **Drift:** influence flow direction  
- **Risk:** paradox, collapse, projection-loss  
- **Triadic scoring:** unified Harmonia synthesis  
- **MCTS integration:** triadic-aware priors and ordering  

## Files

### `module_go.json`
Expanded flagship manifest: pipeline, operators, overlays, MCTS hooks, scoring weights, KataGo integration, golden example.

### `module_go_schema.json`
Full JSON Schema for the StateEmitter output.

### `golden/example_input.sgf`
AlphaGo vs Lee Sedol, Game 4, Move 78.

### `golden/example.json`
Full triadic state for the flagship example.

## Pipeline (v1)

1. **Input:** KataGo analysis JSON  
2. **Lumen:** influence, pressure, connectivity  
3. **Hephaestus:** regime mapping  
4. **Aurion:** topology + ancestry  
5. **Harmonia:** triadic scoring  
6. **StateEmitter:** JSON matching `module_go_schema.json`

## Scope

- KataGo-only integration  
- No engine forking  
- No UI beyond schema  
- Full triadic overlays  
- Full MCTS hook definitions  

RTT-Go is the **canonical RTT demonstration** — the module that proves triadic identity in a deep, complex, world-class domain.
# RTT Hanabi Bot

## Purpose

Hanabi is RTT’s **cooperative hidden-information module**.

It is the only bot where:

- players cannot see their own cards  
- communication is constrained  
- cooperation is mandatory  
- continuity is shared  
- collapse is collective  
- Harmonia means synthesis  

This makes Hanabi the RTT demonstration of **cooperative inference**.

## What Hanabi Teaches

- **Shared continuity:** long-arc team identity  
- **Cooperative resonance:** pressure from clue economy and stack stability  
- **Discard topology:** structural collapse risk  
- **Ancestry:** lineage of shared plans  
- **Drift:** alignment of team intent  
- **Collapse:** bomb risk, clue collapse  
- **Projection-loss:** team-level identity inversion  
- **Triadic identity:** unified Harmonia score for the team  

## Files

### `module_hanabi.json`
Expanded manifest: pipeline, operators, overlays, scoring weights, golden example.

### `module_hanabi_schema.json`
Full JSON Schema for the StateEmitter output.

### `golden/example_input.txt`
A cooperative inference sequence.

### `golden/example.json`
Full triadic state for that sequence.

## Pipeline (v1)

1. **Input:** Hanabi state JSON  
2. **Lumen:** structural extraction  
3. **Hephaestus:** regime classification  
4. **Aurion:** cooperative ancestry  
5. **Harmonia:** triadic synthesis  
6. **StateEmitter:** JSON matching `module_hanabi_schema.json`

## Scope

- No external engine  
- Cooperative hidden-information domain  
- Full triadic overlays  
- Harmonia as synthesis  

Hanabi is the RTT module that proves triadic identity in **cooperative play**.

# RTT Moderation Bot

## Purpose

The Moderation Bot is RTT’s **governance substrate engine**.

It does not enforce rules.  
It does not judge users.  
It does not run a community.

Instead:

> **Moderation watches governance events and emits triadic identity across time.**

This makes Moderation the RTT module for:

- continuity of norms  
- drift in governance  
- structural regime changes  
- collapse signatures  
- projection-loss  
- ancestry of rule applications  
- stability of identity across incidents  

## What Moderation Teaches

- **Governance continuity:** long-arc identity of rule enforcement  
- **Resonance:** pressure from moderation actions  
- **Discard topology:** structural collapse risk in governance  
- **Ancestry:** lineage of rule applications  
- **Drift:** direction + strength of norm evolution  
- **Collapse:** sudden governance failure  
- **Projection-loss:** identity inversion in rule application  
- **Triadic identity:** unified Harmonia score for the entire moderation sequence  

## Files

### `module_moderation.json`
Expanded manifest: pipeline, operators, overlays, scoring weights, golden example.

### `module_moderation_schema.json`
Full JSON Schema for the StateEmitter output.

### `golden/example_input.txt`
A sequence of moderation events.

### `golden/example.json`
Full triadic state for that governance timeline.

## Pipeline (v1)

1. **Input:** sequence of moderation events  
2. **Lumen:** structural extraction  
3. **Hephaestus:** regime classification  
4. **Aurion:** collapse + projection-loss  
5. **Harmonia:** triadic identity  
6. **StateEmitter:** JSON matching `module_moderation_schema.json`

## Scope

- No gameplay  
- No external engine  
- Pure RTT governance identity  
- Full triadic overlays  

Moderation is the RTT module that proves triadic identity in **governance and rule enforcement**.
# RTT Observer Bot

## Purpose

The Observer Bot is the **Triadic Observer Layer** — the RTT lens itself.

It does not play.  
It does not choose moves.  
It does not run an engine.

Instead:

> **Observer watches any sequence — game states, engine outputs, conversations, or events — and emits triadic identity over time.**

This makes Observer the **meta‑bot** of the entire TriadicFrameworks suite.

## What Observer Teaches

- **Regime shifts** across time  
- **Continuity drift** (direction + strength)  
- **Collapse signatures**  
- **Projection-loss**  
- **Structural signals**  
- **Ancestry stability**  
- **Triadic identity of a sequence**  

Observer is the backbone of:

- RTT diagnostics  
- session drift  
- coherence tracking  
- meta‑analysis  
- engine validation  
- bot validation  
- SuperGrok Build introspection  

## Files

### `module_observer.json`
Canonical manifest: pipeline, operators, golden example.

### `module_observer_schema.json`
JSON Schema for the StateEmitter output.

### `golden/example_input.txt`
A short sequence of observed items.

### `golden/example.json`
The full triadic state for that sequence.

## Pipeline (v1)

1. **Input:** sequence of states/messages/events  
2. **Lumen:** extract structural signals  
3. **Hephaestus:** classify regime per item  
4. **Aurion:** detect collapse signatures + projection-loss  
5. **Harmonia:** compute triadic identity for the entire sequence  
6. **StateEmitter:** emit JSON matching `module_observer_schema.json`

## Scope

- No engine integration  
- No gameplay  
- No randomness  
- No hidden information  
- No UI contract beyond the schema  

Observer is the **diagnostic core** of the entire bots suite.

Once wired to SuperGrok Build, Observer becomes the **triadic debugger** for every other module.
# RTT Poker Bot

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
# RTT Session Bot

## Purpose

The Session Bot is RTT’s **conversation engine**.

It does not play a game.  
It does not evaluate a board.  
It does not run an external engine.

Instead:

> **Session watches dialogue and emits triadic identity across time.**

This makes it the RTT engine for:

- coherence  
- drift  
- regime shifts  
- collapse signatures  
- projection-loss  
- semantic continuity  
- emotional resonance  
- long-arc identity of a conversation  

## What Session Teaches

- **Regime:** local (message-level), structural (topic-level), continuity (session-level)  
- **Drift:** direction + strength of semantic/emotional flow  
- **Collapse:** sudden topic or intent failure  
- **Projection-loss:** inversion of long-term conversational identity  
- **Ancestry:** lineage of topics and intents  
- **Triadic identity:** unified Harmonia score for the entire session  

## Files

### `module_session.json`
Expanded manifest: pipeline, operators, overlays, scoring weights, golden example.

### `module_session_schema.json`
JSON Schema for the StateEmitter output.

### `golden/example_input.txt`
A short conversation.

### `golden/example.json`
Full triadic state for that conversation.

## Pipeline (v1)

1. **Input:** sequence of messages  
2. **Lumen:** structural extraction  
3. **Hephaestus:** regime classification  
4. **Aurion:** collapse + projection-loss  
5. **Harmonia:** triadic identity  
6. **StateEmitter:** JSON matching `module_session_schema.json`

## Scope

- No gameplay  
- No external engine  
- Pure RTT conversation identity  
- Full triadic overlays  

Session is the **coherence backbone** of the entire bots suite.
# RTT Tic-Tac-Toe Bot

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
# RTT Validator Bot

## Purpose

The Validator Bot is RTT’s **meta-engine**.

It does not play.  
It does not observe.  
It does not infer.

Instead:

> **Validator checks every other bot for correctness, consistency, and triadic conformance.**

This makes Validator the backbone of:

- SuperGrok Build  
- module correctness  
- schema validation  
- golden example verification  
- operator lineage consistency  
- drift/coherence stability  
- risk signature correctness  
- suite-wide integrity  

## What Validator Teaches

- **Manifest correctness:** required fields, pipeline, operators  
- **Schema correctness:** triadic fields, risk fields, timeline fields  
- **Golden example correctness:** input/output conformance  
- **Lineage correctness:** operator order, pipeline consistency  
- **Triadic conformance:** unified Harmonia score  

## Files

### `module_validator.json`
Expanded manifest: pipeline, checks, scoring weights, golden example.

### `module_validator_schema.json`
JSON Schema for the StateEmitter output.

### `golden/example_input.txt`
A module bundle to validate.

### `golden/example.json`
Full triadic validation output.

## Pipeline (v1)

1. **Input:** RTT module bundle  
2. **Lumen:** structural extraction  
3. **Hephaestus:** regime classification  
4. **Aurion:** lineage + collapse signatures  
5. **Harmonia:** triadic conformance score  
6. **StateEmitter:** JSON matching `module_validator_schema.json`

## Scope

- No gameplay  
- No external engine  
- Pure RTT meta-validation  
- Full triadic checks  

Validator is the **integrity engine** of the entire bots suite.

