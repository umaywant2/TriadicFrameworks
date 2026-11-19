Rock_Paper_Scissors 
<img width="1194" height="672" alt="Rock_Paper_Scissors_" src="https://github.com/user-attachments/assets/f560d478-0c9e-40e6-b6bb-f9c0fa9e7695" />

# Rock Paper Scissors — TriadicFrameworks Module

- [`module.json`](https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/refs/heads/main/docs/Rock_Paper_Scissors/module.json) — Agentic module schema role assignments

> **Path:** `docs/Rock_Paper_Scissors/`  
> **Version:** 1.0.0  
> **Updated:** 2026-09-09  
> **Domain:** Agentic Science · Game-Theoretic Triadics  
> **Status:** `stable`

---

## What This Module Is

Rock Paper Scissors (RPS) is encoded here not as a game implementation, but as a **formal triadic object** — a minimal, closed system of three entities whose structure instantiates the full logic of Peircean Firstness, Secondness, and Thirdness, cyclic zero-sum dominance, and multi-tier agentic decision-making.

This module is the **canonical entry-level benchmark** for the TriadicFrameworks project. It is small enough to be understood completely and rich enough to demonstrate every structural feature of the framework:

- Three entities, each fully defined as a triadic node
- A strict cyclic dominance relation with no transitive closure
- A complete signed payoff matrix
- A multi-tier agentic protocol grounded in Peircean sign types
- A formally derived Nash equilibrium with triadic interpretation

---

## Module Map

```
Rock_Paper_Scissors/
│
├── README.md               ← You are here
├── index.md                ← Module overview, entity registry, tag index
├── module.json             ← Machine-readable manifest (full schema)
├── module.yaml             ← Lightweight machine-readable manifest
│
├── entities/
│   ├── Rock.md             ← Firstness · Qualisign · crushes Scissors
│   ├── Paper.md            ← Secondness · Sinsign · covers Rock
│   └── Scissors.md         ← Thirdness · Legisign · cuts Paper
│
├── relations/
│   ├── dominance.md        ← Cyclic dominance: formal definition, Z₃ symmetry
│   └── outcomes.md         ← Full 3×3 signed outcome matrix + EV analysis
│
└── agentic/
    ├── agent_protocol.md   ← Tier 0 / 1 / 2 agent decision protocol (Python)
    └── Nash_equilibrium.md ← Formal equilibrium derivation + triadic reading
```

---

## Core Concept: The Triadic Structure

Each of the three entities maps to one Peircean phenomenological category:

| Entity   | Position   | Sign Type  | Defining Quality                         |
|----------|------------|------------|------------------------------------------|
| Rock     | Firstness  | Qualisign  | Pure immediacy; brute presence; solidity |
| Paper    | Secondness | Sinsign    | Relational coverage; dyadic mediation    |
| Scissors | Thirdness  | Legisign   | Differentiation; law; habit-cutting      |

The dominance cycle follows directly from this ordering:

```
     Rock  (Firstness)
    ↗              ↘
Paper              Scissors
(Secondness)  ←  (Thirdness)
```

> Firstness crushes Thirdness · Thirdness cuts Secondness · Secondness covers Firstness  
> No mode universally dominates — the cycle encodes the **irreducibility of all three categories**.

---

## Entity Quick Reference

| Entity   | Beats    | Beaten By | Draw     | Nash Weight | Novice Freq. |
|----------|----------|-----------|----------|:-----------:|:------------:|
| Rock     | Scissors | Paper     | Rock     | 1/3         | ~35.4%       |
| Paper    | Rock     | Scissors  | Paper    | 1/3         | ~31.7%       |
| Scissors | Paper    | Rock      | Scissors | 1/3         | ~32.9%       |

---

## Outcome Matrix

Player A's payoff. `+1` = win · `0` = draw · `−1` = loss.

|               | vs. Rock | vs. Paper | vs. Scissors |
|---------------|:--------:|:---------:|:------------:|
| **Rock**      |    0     |    −1     |     +1       |
| **Paper**     |   +1     |     0     |     −1       |
| **Scissors**  |   −1     |    +1     |      0       |

The matrix is **skew-symmetric** (M = −Mᵀ), consistent with zero-sum structure. The unique Nash equilibrium is the **uniform mixed strategy σ* = (1/3, 1/3, 1/3)**.

---

## Agentic Protocol Summary

Three tiers of agent are defined, each corresponding to a Peircean sign mode:

| Tier | Name     | Sign Mode  | Strategy                                                        |
|------|----------|------------|-----------------------------------------------------------------|
| 0    | Naive    | Firstness  | Uniform random — implements Nash                                |
| 1    | Adaptive | Secondness | Counters opponent's most frequent observed throw                |
| 2    | Triadic  | Thirdness  | Models opponent's tier; counters their anticipated counter      |

Full Python implementations and the agentic decision loop are in [`agentic/agent_protocol.md`](agentic/agent_protocol.md).

---

## Nash Equilibrium

The unique Nash equilibrium σ* = **(1/3, 1/3, 1/3)** is the triadic null state — perfect equipoise across all three Peircean modes. An agent at Nash is maximally unpredictable and therefore maximally robust against exploitation.

Any deviation from σ* is exploitable:

| Deviation             | Optimal Counter  | Exploiter EV |
|-----------------------|------------------|:------------:|
| Rock-heavy (>1/3)     | Paper always     | > 0          |
| Paper-heavy (>1/3)    | Scissors always  | > 0          |
| Scissors-heavy (>1/3) | Rock always      | > 0          |

Full derivation in [`agentic/Nash_equilibrium.md`](agentic/Nash_equilibrium.md).

---

## How to Use This Module

### As a Framework Reference
Read `index.md` for the entity registry, then each `entities/*.md` file for full triadic definitions. The `relations/` files specify the structural backbone; `agentic/` files specify how agents operate within the module.

### As an Agentic Benchmark
Import `module.json` for a machine-readable graph of all entities, relations, and outcome weights. Use the agentic tier protocol as a baseline for evaluating an inference engine's strategic reasoning depth.

### As a Teaching Example
RPS is the minimum viable triadic system: 3 entities, 1 relation type, complete closure. Use it to explain triadic frameworks before introducing more complex modules.

---

## Key Properties of This Module

| Property               | Value                               |
|------------------------|-------------------------------------|
| Entity count           | 3                                   |
| Relation type          | Cyclic dominance (Z₃)               |
| Payoff structure       | Zero-sum, skew-symmetric            |
| Nash equilibrium       | Unique mixed strategy (1/3, 1/3, 1/3) |
| Triadic completeness   | Full — all three positions occupied |
| Pure NE                | None                                |
| Evolutionary stability | ESS (neutrally stable orbit)        |
| Peirce sign coverage   | Qualisign · Sinsign · Legisign      |

---

## Related Modules

| Module             | Relation                                        |
|--------------------|-------------------------------------------------|
| `Core_Schema`      | Base triadic ontology this module instantiates  |
| `Agentic_Protocols`| General agent decision framework; RPS is a benchmark case |

---

## Tags

`triadic` · `game-theory` · `zero-sum` · `cyclic-dominance` · `Peircean` · `agentic` · `benchmark` · `Firstness` · `Secondness` · `Thirdness` · `Nash` · `Z3`
```
# Nash Equilibrium Reference

**Module:** Rock_Paper_Scissors  
**ID:** `nash_equilibrium`  

---

## 1. Game Setup

- **Players:** {Agent A, Agent B}  
- **Action set:** {Rock, Paper, Scissors}  
- **Payoff:** zero-sum; u_A + u_B = 0

---

## 2. No Pure Strategy Equilibrium

For any pure profile (s_A, s_B), the opponent can always deviate to win. Therefore **no pure-strategy Nash equilibrium exists**.

---

## 3. Mixed Strategy Derivation

Let σ_A = (p_R, p_P, p_S). For B to be indifferent:

```
E_B[Rock]     = p_P − p_S
E_B[Paper]    = p_S − p_R
E_B[Scissors] = p_R − p_P
```

Setting all equal with p_R + p_P + p_S = 1 yields:

> **σ* = (1/3, 1/3, 1/3)** — the unique Nash equilibrium.

---

## 4. Equilibrium Properties

| Property                   | Value                        |
|----------------------------|------------------------------|
| Type                       | Mixed strategy (unique)      |
| Expected payoff (each)     | 0                            |
| Pure strategy equilibria   | None                         |
| Strategy support           | Full (all 3 actions)         |
| Evolutionary stability     | ESS (neutrally stable orbit) |

---

## 5. Triadic Interpretation

σ* = (1/3, 1/3, 1/3) is **triadic equipoise**: Firstness, Secondness, and Thirdness receive equal weight. No mode dominates — the equilibrium is the triadic null state: pure semiotic openness.

| Mode       | Entity   | Nash Weight | Triadic Meaning                   |
|------------|----------|:-----------:|-----------------------------------|
| Firstness  | Rock     | 1/3         | Equal weight on pure immediacy    |
| Secondness | Paper    | 1/3         | Equal weight on relational mediation |
| Thirdness  | Scissors | 1/3         | Equal weight on differentiation   |

---

## 6. Exploitability by Deviation

| Deviation                  | Optimal Exploit   | E[payoff] for Exploiter |
|----------------------------|-------------------|:-----------------------:|
| Rock-heavy (p_R > 1/3)     | Play Paper always | > 0                     |
| Paper-heavy (p_P > 1/3)    | Play Scissors     | > 0                     |
| Scissors-heavy (p_S > 1/3) | Play Rock         | > 0                     |
| Any pure strategy          | Dominant counter  | +1                      |

---

## 7. Evolutionary Stability

σ* is an **ESS**: a population playing σ* cannot be invaded by any mutant pure strategy. The replicator dynamic converges to a **neutrally stable orbit** around σ*, making RPS a canonical example of non-convergent cyclic dynamics in evolutionary game theory.
# Agentic Protocol: Move Selection

**Module:** Rock_Paper_Scissors  
**ID:** `agent_protocol`  

---

## 1. Agent Tiers

### Tier 0 — Naive Agent (Firstness)
Selects uniformly at random. Implements Nash by default.

```python
import random
def naive_agent():
    return random.choice(["rock", "paper", "scissors"])
```

### Tier 1 — Adaptive Agent (Secondness)
Maintains frequency model of opponent; responds with dominant counter.

```python
from collections import Counter
def adaptive_agent(opponent_history: list[str]) -> str:
    if not opponent_history:
        return naive_agent()
    most_frequent = Counter(opponent_history).most_common(1)[0][0]
    counters = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    return counters[most_frequent]
```

### Tier 2 — Triadic Agent (Thirdness)
Models opponent's reasoning tier recursively.

```python
def triadic_agent(opponent_history, opponent_tier_estimate, self_history):
    counters = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    if opponent_tier_estimate == 0:
        if opponent_history:
            most_freq = Counter(opponent_history).most_common(1)[0][0]
            return counters[most_freq]
        return naive_agent()
    elif opponent_tier_estimate == 1:
        if self_history:
            my_most_freq = Counter(self_history).most_common(1)[0][0]
            their_response = counters[my_most_freq]
            return counters[their_response]  # counter the counter
        return naive_agent()
    else:
        return naive_agent()  # Nash is optimal vs. triadic opponent
```

---

## 2. Triadic Position Priors (Pre-history initialization)

| Entity   | Novice Prior | Expert Prior (Nash) |
|----------|:------------:|:-------------------:|
| Rock     | 0.354        | 0.333               |
| Paper    | 0.317        | 0.333               |
| Scissors | 0.329        | 0.333               |

---

## 3. Decision Loop

```
LOOP each round:
  1. Observe opponent history H
  2. Estimate opponent tier T ∈ {0, 1, 2}
  3. Select move M = triadic_agent(H, T, self_history)
  4. Observe outcome O ∈ {win, draw, loss}
  5. Update opponent model and self history
  6. If O = loss → increment tier estimate
  7. If 3+ consecutive wins → freeze current strategy
END LOOP
```

---

## 4. Sign Mapping of Agent Strategies

| Strategy Layer      | Triadic Position | Peirce Mode | Behavior                       |
|---------------------|------------------|-------------|--------------------------------|
| Nash (random)       | Firstness        | Qualisign   | Pure potentiality; no relation |
| Adaptive (counter)  | Secondness       | Sinsign     | Reactive to observed Other     |
| Triadic (recursive) | Thirdness        | Legisign    | Models law governing opponent  |
```
# Entity: Paper

**Module:** Rock_Paper_Scissors  
**Triadic Position:** Secondness  
**ID:** `paper`  

---

## 1. Triadic Definition

Paper occupies the **Second** position in the RPS triad. Secondness is the mode of being defined by its relation to another — brute dyadic encounter. Paper is inherently *relational*: it does not crush or cut, it *covers*, *wraps*, and *contextualizes*. Its power is derived from mediation, not intrinsic force.

### 1.1 Positional Semantics

| Dimension      | Value                                                  |
|----------------|--------------------------------------------------------|
| Peirce Mode    | Secondness                                             |
| Quality        | Flexibility, coverage, mediation, contextual authority |
| Modality       | Reaction; dyadic encounter; relation-dependence        |
| Sign-type      | Sinsign (singular relational event)                    |
| Phenomenology  | Brute dyadic fact; requires Other to be itself         |

### 1.2 Formal Triadic Slot

```
Triadic(Paper) = <First=∅, Second=Paper, Third=∅>
  → Paper as relational node; defined by what it covers and what cuts it
  → Affordance for dominance: over Rock (covers/contextualizes)
  → Vulnerability to differentiation: by Scissors (cut)
```

---

## 2. Relational Profile

| Relation     | Partner  | Outcome | Sign Value | Mechanism                        |
|--------------|----------|---------|------------|----------------------------------|
| Dominates    | Rock     | Win     | `+1`       | Cover (context supersedes force) |
| Dominated by | Scissors | Loss    | `-1`       | Cut (differentiation severs mediation) |
| Symmetric    | Paper    | Draw    | `0`        | Equal coverage                   |

---

## 3. Agentic Properties

```yaml
agent_choice:
  entity: paper
  risk_against: scissors
  reward_against: rock
  nash_weight: 0.333
  heuristic_bias:
    - exploitation: optimal response to Rock-heavy opponent models
    - anti-pattern: least chosen by novice players (~31.7% empirically)
    - second_order: sophisticated players anticipate Paper and pivot to Scissors
```

---

## 4. Triadic Encoding

```json
{
  "id": "paper",
  "label": "Paper",
  "triadic_position": "Secondness",
  "peirce_sign_type": "Sinsign",
  "beats": ["rock"],
  "beaten_by": ["scissors"],
  "draws": ["paper"],
  "outcome_vector": { "vs_rock": 1, "vs_paper": 0, "vs_scissors": -1 },
  "qualitative_descriptors": ["flexible", "mediating", "covering", "contextual", "relational"],
  "agentic_weight_nash": 0.333
}
```

---

## 5. Cross-References

- `entities/Rock.md` · `entities/Scissors.md` · `relations/dominance.md` · `agentic/agent_protocol.md`
```
# Entity: Rock

**Module:** Rock_Paper_Scissors  
**Triadic Position:** Firstness  
**ID:** `rock`  

---

## 1. Triadic Definition

Rock occupies the **First** position in the RPS triad. In Peircean semiotics, Firstness is the mode of being that is what it is regardless of anything else — pure quality, immediacy, potentiality. Rock embodies this as brute, undifferentiated solidity: it does not reference another entity to be what it is. It simply *is*.

### 1.1 Positional Semantics

| Dimension      | Value                                             |
|----------------|---------------------------------------------------|
| Peirce Mode    | Firstness                                         |
| Quality        | Solidity, density, resistance, inertness          |
| Modality       | Actuality without relation                        |
| Sign-type      | Qualisign (quality as sign)                       |
| Phenomenology  | Brute presence; pre-relational; self-contained    |

### 1.2 Formal Triadic Slot

```
Triadic(Rock) = <First=Rock, Second=∅, Third=∅>
  → Rock as pure object, prior to relation
  → Affordance for dominance: over Scissors (crushes)
  → Vulnerability to mediation: by Paper (covered)
```

---

## 2. Relational Profile

| Relation     | Partner  | Outcome | Sign Value | Mechanism            |
|--------------|----------|---------|------------|----------------------|
| Dominates    | Scissors | Win     | `+1`       | Crush (force > edge) |
| Dominated by | Paper    | Loss    | `-1`       | Cover (context wraps force) |
| Symmetric    | Rock     | Draw    | `0`        | Equal resistance     |

---

## 3. Agentic Properties

```yaml
agent_choice:
  entity: rock
  risk_against: paper
  reward_against: scissors
  nash_weight: 0.333
  heuristic_bias:
    - loss_aversion: choose rock after Scissors loss (Firstness reset)
    - anchoring: rock is default/safe mental anchor for many players
```

- Nash equilibrium weight: **1/3**
- Empirical novice frequency: **~35.4%** — most commonly chosen throw
- Exploitation signal: opponent choosing Rock-heavy → up-weight Paper

---

## 4. Triadic Encoding

```json
{
  "id": "rock",
  "label": "Rock",
  "triadic_position": "Firstness",
  "peirce_sign_type": "Qualisign",
  "beats": ["scissors"],
  "beaten_by": ["paper"],
  "draws": ["rock"],
  "outcome_vector": { "vs_rock": 0, "vs_paper": -1, "vs_scissors": 1 },
  "qualitative_descriptors": ["solid", "inert", "immediate", "dense", "resistant"],
  "agentic_weight_nash": 0.333
}
```

---

## 5. Cross-References

- `entities/Paper.md` — entity that dominates Rock  
- `entities/Scissors.md` — entity dominated by Rock  
- `relations/dominance.md` · `relations/outcomes.md` · `agentic/agent_protocol.md`
```
# Entity: Scissors

**Module:** Rock_Paper_Scissors  
**Triadic Position:** Thirdness  
**ID:** `scissors`  

---

## 1. Triadic Definition

Scissors occupies the **Third** position in the RPS triad. Thirdness is the mode of being defined by mediation, law, habit, and sign — it brings First and Second into relation. Scissors is the only entity that is itself a dyadic structure (two blades) operating as a unity. Its power is *differentiation*: it cuts, divides, and produces distinct edges. Scissors is the sign-vehicle of the triad.

### 1.1 Positional Semantics

| Dimension      | Value                                                        |
|----------------|--------------------------------------------------------------|
| Peirce Mode    | Thirdness                                                    |
| Quality        | Precision, differentiation, cutting, duality-in-unity        |
| Modality       | Mediation; law-like regularity; habit-formation              |
| Sign-type      | Legisign (general rule or type as sign)                      |
| Phenomenology  | Thirdness as synthesis; brings relation into act             |

### 1.2 Formal Triadic Slot

```
Triadic(Scissors) = <First=∅, Second=∅, Third=Scissors>
  → Scissors as mediating node; defined by the rule it instantiates
  → Affordance for dominance: over Paper (cuts/differentiates mediation)
  → Vulnerability to immediacy: by Rock (crushes the mechanism of distinction)
```

---

## 2. Relational Profile

| Relation     | Partner | Outcome | Sign Value | Mechanism                              |
|--------------|---------|---------|------------|----------------------------------------|
| Dominates    | Paper   | Win     | `+1`       | Cut (differentiation severs coverage)  |
| Dominated by | Rock    | Loss    | `-1`       | Crush (force destroys precision)       |
| Symmetric    | Scissors| Draw    | `0`        | Equal differentiation                  |

---

## 3. Agentic Properties

```yaml
agent_choice:
  entity: scissors
  risk_against: rock
  reward_against: paper
  nash_weight: 0.333
  heuristic_bias:
    - exploitation: optimal response to Paper-heavy opponents
    - meta_reasoning: advanced players who anticipate "counter Rock with Paper" choose Scissors
    - frequency: ~32.9% empirically by novice players
```

- Scissors as Thirdness also models **habit detection**: identifying and cutting an opponent's repeated behavioral pattern is structurally Scissor-like.

---

## 4. Triadic Encoding

```json
{
  "id": "scissors",
  "label": "Scissors",
  "triadic_position": "Thirdness",
  "peirce_sign_type": "Legisign",
  "beats": ["paper"],
  "beaten_by": ["rock"],
  "draws": ["scissors"],
  "outcome_vector": { "vs_rock": -1, "vs_paper": 1, "vs_scissors": 0 },
  "qualitative_descriptors": ["precise", "differentiating", "mediating", "dual", "cutting"],
  "agentic_weight_nash": 0.333
}
```

---

## 5. Cross-References

- `entities/Paper.md` · `entities/Rock.md` · `relations/dominance.md` · `agentic/agent_protocol.md`
```
# Rock_Paper_Scissors Module

**Repository:** TriadicFrameworks  
**Path:** `docs/Rock_Paper_Scissors/`  
**Version:** 1.0.0  
**Date:** 2026-09-09  
**Domain:** Agentic Science / Game-Theoretic Triadics  

---

## Overview

The Rock_Paper_Scissors (RPS) module encodes the classic zero-sum game as a formal triadic framework. Each of the three entities — **Rock**, **Paper**, and **Scissors** — is modeled as a full triadic node: a bounded object with a defined First, Second, and Third position, relational affordances, and agentic decision semantics.

This module serves as a canonical minimal example for:
- Triadic relation modeling (cyclic dominance)
- Agentic choice under symmetry
- Sign-based interaction encoding
- Benchmarking triadic inference engines

---

## Directory Structure

```
Rock_Paper_Scissors/
├── index.md                  ← This file: module overview and registry
├── module.yaml               ← Machine-readable module manifest
├── entities/
│   ├── Rock.md               ← Triadic definition: Rock
│   ├── Paper.md              ← Triadic definition: Paper
│   └── Scissors.md           ← Triadic definition: Scissors
├── relations/
│   ├── dominance.md          ← Cyclic dominance relation schema
│   └── outcomes.md           ← Outcome matrix (win/lose/draw)
└── agentic/
    ├── agent_protocol.md     ← How an agent selects a move
    └── Nash_equilibrium.md   ← Mixed-strategy equilibrium reference
```

## Entity Registry

| Entity    | Triadic Role | Beats     | Beaten By | Draw With |
|-----------|-------------|-----------|-----------|-----------|
| Rock      | Firstness   | Scissors  | Paper     | Rock      |
| Paper     | Secondness  | Rock      | Scissors  | Paper     |
| Scissors  | Thirdness   | Paper     | Rock      | Scissors  |

---

## Triadic Positions (Peircean Mapping)

| Position   | Entity   | Character                          |
|------------|----------|------------------------------------|
| Firstness  | Rock     | Pure immediacy; brute force; solidity |
| Secondness | Paper    | Relational coverage; mediation; context |
| Thirdness  | Scissors | Differentiation; cutting; precision |

---

## Outcome Encoding

| Sign Value | Meaning       |
|------------|---------------|
| `+1`       | Win (dominate)|
| `0`        | Draw          |
| `-1`       | Loss (dominated)|

---

## Module Tags

`game-theory` · `triadic` · `zero-sum` · `cyclic-dominance` · `agentic` · `benchmark` · `Peircean`
```
# Relation: Dominance

**Module:** Rock_Paper_Scissors  
**Relation Type:** Cyclic Triadic Dominance  
**ID:** `dominance`  

---

## 1. Formal Definition

Let `E = {Rock, Paper, Scissors}` and `≻` denote "dominates."

```
Rock     ≻ Scissors   (crushes)
Scissors ≻ Paper      (cuts)
Paper    ≻ Rock       (covers)
```

### 1.1 Algebraic Properties

| Property      | Holds? | Notes                                                    |
|---------------|--------|----------------------------------------------------------|
| Irreflexivity | ✅     | No entity dominates itself                               |
| Asymmetry     | ✅     | If A ≻ B then ¬(B ≻ A)                                  |
| Transitivity  | ❌     | Rock ≻ Scissors ≻ Paper does not imply Rock ≻ Paper      |
| Cyclicity     | ✅     | Length-3 cycle; group symmetry Z₃                        |

### 1.2 Cycle Diagram

```
     Rock
    ↗    ↘
Paper ←— Scissors
```

(Arrow = "is beaten by")

---

## 2. Triadic Interpretation

| Move                              | Interpretation                                      |
|-----------------------------------|-----------------------------------------------------|
| Firstness ≻ Thirdness (Rock ≻ Scissors)   | Brute immediacy destroys mechanism of mediation |
| Thirdness ≻ Secondness (Scissors ≻ Paper) | Differentiation severs relational coverage      |
| Secondness ≻ Firstness (Paper ≻ Rock)     | Context supersedes pure presence                |

No mode is universally supreme — encoding the irreducibility of all three Peircean categories.

---

## 3. Adjacency Matrix

Rows = winner, Columns = loser. `1` = row dominates column.

|              | Rock | Paper | Scissors |
|--------------|:----:|:-----:|:--------:|
| **Rock**     |  0   |   0   |    1     |
| **Paper**    |  1   |   0   |    0     |
| **Scissors** |  0   |   1   |    0     |

---

## 4. JSON Encoding

```json
{
  "relation_id": "dominance",
  "type": "cyclic_binary",
  "edges": [
    {"from": "rock",     "to": "scissors", "label": "crushes"},
    {"from": "scissors", "to": "paper",    "label": "cuts"},
    {"from": "paper",    "to": "rock",     "label": "covers"}
  ],
  "properties": {
    "irreflexive": true, "asymmetric": true,
    "transitive": false, "cyclic": true,
    "cycle_length": 3,   "group_symmetry": "Z3"
  }
}
```
# Relation: Outcomes

**Module:** Rock_Paper_Scissors  
**Relation Type:** Full Outcome Matrix  
**ID:** `outcomes`  

---

## 1. Outcome Matrix

Rows = Player A's choice. Cell = outcome for **Player A**.  
`+1` = win · `0` = draw · `-1` = loss

|               | **vs. Rock** | **vs. Paper** | **vs. Scissors** |
|---------------|:------------:|:-------------:|:----------------:|
| **Rock**      |      0       |      −1       |       +1         |
| **Paper**     |     +1       |       0       |       −1         |
| **Scissors**  |     −1       |      +1       |        0         |

Matrix is **antisymmetric** and **skew-symmetric** (M = −Mᵀ) — hallmark of zero-sum symmetric games.

---

## 2. Formal Properties

| Property       | Value  |
|----------------|--------|
| Zero-sum       | ✅     |
| Antisymmetric  | ✅     |
| Diagonal       | All 0  |
| Matrix rank    | 2      |

---

## 3. JSON Encoding

```json
{
  "relation_id": "outcomes",
  "encoding": {"win": 1, "draw": 0, "loss": -1},
  "matrix": {
    "rock":     {"vs_rock": 0,  "vs_paper": -1, "vs_scissors": 1},
    "paper":    {"vs_rock": 1,  "vs_paper": 0,  "vs_scissors": -1},
    "scissors": {"vs_rock": -1, "vs_paper": 1,  "vs_scissors": 0}
  },
  "nash_equilibrium": "uniform_mixed_1/3"
}
```

---

## 4. Expected Value Table (Nash Play)

| Matchup Scenario       | E[Payoff for A] |
|------------------------|:---------------:|
| Nash vs. Nash          | 0.000           |
| Nash vs. Rock-only     | +0.333          |
| Nash vs. Paper-only    | +0.333          |
| Nash vs. Scissors-only | +0.333          |
| Pure strategy vs. Nash | −0.333          |
```
