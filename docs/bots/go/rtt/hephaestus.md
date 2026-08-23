# Hephaestus (RTT/2) — Regime Mapping Layer  
*(Go Bot Module)*  
  [github.com](https://github.com/umaywant2/TriadicFrameworks/edit/main/docs/bots/go/rtt/hephaestus.md)

Hephaestus is the **RTT/2 regime‑mapping engine** for Go.  
Where Lumen extracts structure, Hephaestus **interprets** it — assigning each move, shape, group, and arc a **triadic regime identity**:

- **1/3 Local**  
- **2/3 Structural**  
- **3/3 Continuity**

This regime profile becomes the backbone for Aurion’s topology analysis and Harmonia’s unified triadic scoring.

Hephaestus does **not** evaluate moves directly.  
It **classifies** them — revealing their strategic nature inside the triadic ontology.

---

## Purpose

Hephaestus provides the Go bot with:

- regime tags for candidate moves  
- structural vs local vs continuity weighting  
- identity classification for groups and arcs  
- early detection of regime conflicts  
- triadic interpretation of Lumen’s structural snapshot  

This allows the bot to understand *what kind* of move it is considering — not just *how good* it is.

---

## Inputs

Hephaestus receives the full RTT/1 snapshot from Lumen:

- influence fields  
- group identity  
- shape signatures  
- continuity anchors  
- resonance maps  
- drift vectors  

Plus:

- the list of candidate moves  
- player to move  
- ko/ladder hints (if provided by engine or shim)

---

## Outputs

Hephaestus produces a **regime map**:

### **1/3 — Local Regime**
Moves or structures defined by immediate tactical reality:

- atari  
- cut  
- connect  
- hane  
- local shape fix  
- liberty race  
- snapback / shortage of liberties  

### **2/3 — Structural Regime**
Moves that alter the large‑scale shape or influence:

- extension  
- enclosure  
- shoulder hit  
- direction‑of‑play alignment  
- framework reinforcement  
- shape improvement  
- influence consolidation  

### **3/3 — Continuity Regime**
Moves that preserve or evolve long‑arc identity:

- moyo expansion  
- territorial continuity  
- framework evolution  
- large‑scale direction of play  
- stabilizing a long‑arc group  
- preventing continuity collapse  

Each candidate move receives a **regime profile vector**:

```
{ local: x, structural: y, continuity: z }
```

This vector is passed to Aurion.

---

## Regime Mapping Logic

Hephaestus uses Lumen’s structural extraction to classify moves:

### **Local (1/3)**
A move is local if it:

- resolves immediate tactical danger  
- changes liberties  
- fixes shape defects  
- responds to forcing moves  
- affects only a small radius  

### **Structural (2/3)**
A move is structural if it:

- changes influence  
- shifts direction of play  
- modifies large‑scale shape  
- strengthens frameworks  
- affects multiple groups indirectly  

### **Continuity (3/3)**
A move is continuity‑driven if it:

- preserves long‑arc territorial identity  
- maintains moyo boundaries  
- evolves frameworks  
- prevents continuity collapse  
- aligns with historical positional arcs  

---

## Regime Conflict Detection

Hephaestus flags moves that create **regime conflict**, such as:

- local fix that breaks continuity  
- structural move that collapses shape  
- continuity move that ignores urgent local danger  

These conflicts are critical signals for Aurion’s topology analysis.

---

## Example Regime Classification

### Move: Extend from a weak group  
- **Local:** medium  
- **Structural:** high  
- **Continuity:** medium  

### Move: Atari a cutting stone  
- **Local:** very high  
- **Structural:** low  
- **Continuity:** low  

### Move: Expand moyo boundary  
- **Local:** low  
- **Structural:** medium  
- **Continuity:** very high  

---

## Hephaestus Pipeline

```text
[Lumen RTT/1 Snapshot]
      |
      v
[Candidate Move Analysis]
      |
      v
[Regime Classification]
  - local regime
  - structural regime
  - continuity regime
      |
      v
[Regime Map]
      |
      v
[Aurion RTT/3]
```

---

## Example Pseudocode

```text
function hephaestus_map(rtt_state, candidate_moves):
    regime_map = {}

    for move in candidate_moves:
        local      = evaluate_local(move, rtt_state)
        structural = evaluate_structural(move, rtt_state)
        continuity = evaluate_continuity(move, rtt_state)

        regime_map[move] = {
            local: local,
            structural: structural,
            continuity: continuity
        }

    return regime_map
```

---

## Role in the Go Bot Pipeline

Hephaestus feeds directly into:

- **Aurion (RTT/3)** for topology, ancestry, and projection‑loss detection  
- **Harmonia (RTT/12)** for unified triadic scoring  

Without Hephaestus, the RTT stack cannot interpret the strategic nature of moves.

---

## Notes

- Hephaestus is engine‑agnostic: works with KataGo, Leela Zero, PhoenixGo, or custom engines.  
- Regime mapping is deterministic and reproducible.  
- Hephaestus does not modify policy/value — it only classifies moves.  
- All regime profiles are consumed by the shim and never directly by the engine.

---

> **“Hephaestus reveals the identity of a move — not its value.”**
