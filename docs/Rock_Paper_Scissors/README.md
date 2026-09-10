# Rock Paper Scissors — TriadicFrameworks Module

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
