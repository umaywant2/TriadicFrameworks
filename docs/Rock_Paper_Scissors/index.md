# Rock_Paper_Scissors Module

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
