# RTT‑Go Examples  
*(Examples for `/docs/bots/go/examples/rtt_go_examples.md`)*

This document provides **worked examples** demonstrating how the RTT triadic stack (Lumen → Hephaestus → Aurion → Harmonia) interacts with Go engine outputs (KataGo, Leela Zero, PhoenixGo) to produce continuity‑preserving, resonance‑aligned move decisions.

These examples are designed for:

- developers integrating RTT into Go engines  
- readers learning RTT’s triadic interpretation of Go  
- teaching/analysis modes  
- debugging the shim and logic layer  

---

## Example 1 — Local vs Structural vs Continuity Move

### Position
Black has a weak group on the right side. White has a large moyo forming on the left. It is Black’s turn.

### Candidate Moves
- **A:** Atari the cutting stone  
- **B:** Extend the weak group  
- **C:** Expand left‑side moyo boundary  

### RTT Interpretation

#### **Lumen (RTT/1)**
- identifies weak group on right  
- identifies moyo boundary on left  
- influence map shows left side is globally dominant  

#### **Hephaestus (RTT/2)**
- A → **1/3 local**  
- B → **2/3 structural**  
- C → **3/3 continuity**  

#### **Aurion (RTT/3)**
- A → paradox risk (locally good, globally bad)  
- B → stabilizes topology  
- C → continuity‑aligned but risky due to weak group  

#### **Harmonia (RTT/12)**
Triadic scores:

| Move | Local | Structural | Continuity | Paradox | Projection Loss | Final |
|------|-------|------------|------------|---------|------------------|-------|
| A | high | low | low | **high** | medium | **low** |
| B | medium | **high** | medium | low | low | **high** |
| C | low | medium | **high** | medium | **high** | medium |

### **RTT‑Go Decision**
**Move B** — extend the weak group — is selected.

It preserves continuity, avoids paradox, and stabilizes topology.

---

## Example 2 — Ladder Ancestry and Projection‑Loss

### Position
White threatens a ladder. Black can:

- **A:** Play the ladder breaker  
- **B:** Strengthen the laddered group locally  
- **C:** Play a large territorial move elsewhere  

### RTT Interpretation

#### **Lumen**
- detects ladder shape  
- marks ladder ancestry  
- identifies global influence  

#### **Hephaestus**
- A → structural  
- B → local  
- C → continuity  

#### **Aurion**
- A → stabilizes ancestry  
- B → paradox (local fix but ladder still fails)  
- C → catastrophic projection‑loss  

#### **Harmonia**
Triadic scores:

| Move | Ancestry | Projection Loss | Paradox | Final |
|------|----------|------------------|---------|-------|
| A | **aligned** | low | low | **high** |
| B | misaligned | medium | **high** | low |
| C | broken | **very high** | medium | very low |

### **RTT‑Go Decision**
**Move A** — ladder breaker — is selected.

---

## Example 3 — Ko Topology and Continuity Collapse

### Position
A large ko fight threatens the stability of both players’ frameworks.

### Candidate Moves
- **A:** Take the ko  
- **B:** Threaten locally  
- **C:** Play a global ko threat  

### RTT Interpretation

#### **Lumen**
- identifies ko topology  
- marks framework boundaries  

#### **Hephaestus**
- A → local  
- B → local  
- C → structural/continuity  

#### **Aurion**
- A → high collapse risk  
- B → insufficient  
- C → stabilizes continuity  

#### **Harmonia**
Triadic scores:

| Move | Ko Stability | Continuity | Collapse Risk | Final |
|------|--------------|------------|---------------|-------|
| A | low | low | **high** | low |
| B | medium | low | medium | medium |
| C | **high** | **high** | low | **high** |

### **RTT‑Go Decision**
**Move C** — global ko threat — is selected.

---

## Example 4 — Moyo Continuity vs Local Urgency

### Position
White has a massive moyo forming. Black has a small local weakness.

### Candidate Moves
- **A:** Fix local weakness  
- **B:** Reduce moyo  
- **C:** Invade moyo  

### RTT Interpretation

#### **Lumen**
- identifies moyo boundary  
- marks local defect  

#### **Hephaestus**
- A → local  
- B → structural  
- C → continuity  

#### **Aurion**
- A → paradox (fixing local loses global)  
- B → stabilizes topology  
- C → high‑risk continuity move  

#### **Harmonia**
Triadic scores:

| Move | Local | Structural | Continuity | Risk | Final |
|------|-------|------------|------------|------|-------|
| A | high | low | low | medium | low |
| B | medium | **high** | medium | low | **high** |
| C | low | medium | **high** | **high** | medium |

### **RTT‑Go Decision**
**Move B** — reduce the moyo — is selected.

---

## Example 5 — Teaching Mode Output

In teaching mode, RTT does **not** select moves.  
It produces overlays:

```
Move A — Local (1/3)
  - Tactical fix
  - Paradox risk: high
  - Continuity impact: negative

Move B — Structural (2/3)
  - Influence shift
  - Stabilizes topology
  - Continuity impact: positive

Move C — Continuity (3/3)
  - Long-arc moyo evolution
  - Projection-loss risk: medium
```

This mode is ideal for learning RTT‑Go.

---

## Example 6 — Analysis Mode Output

In analysis mode, RTT evaluates human games:

```
Move 57 — Paradox detected
  - Local shape fix
  - Global continuity collapse
  - Ladder ancestry violated

Move 103 — Continuity anchor preserved
  - Framework evolution aligned
  - Influence drift stabilized
```

This mode is ideal for commentary and study.

---

## Summary

These examples demonstrate how RTT:

- interprets Go positions structurally  
- maps moves into triadic regimes  
- detects topology, ancestry, paradox, and collapse  
- synthesizes unified triadic strategy  
- blends with engine policy/value  
- selects continuity‑preserving moves  

RTT‑Go is not a new engine — it is a **triadic intelligence layer** that reveals the deeper structure already inside the game.
