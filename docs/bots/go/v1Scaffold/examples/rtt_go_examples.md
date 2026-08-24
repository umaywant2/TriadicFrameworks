# RTT‑Go Examples  
*(Examples for `/docs/bots/go/examples/rtt_go_examples.md`)*

This document provides **worked examples** demonstrating how the RTT triadic stack  
**Lumen → Hephaestus → Aurion → Harmonia**  
interacts with Go engine outputs (KataGo, Leela Zero, PhoenixGo) to produce continuity‑preserving, resonance‑aligned move decisions.

These examples are designed for:

- developers integrating RTT into Go engines  
- readers learning RTT’s triadic interpretation of Go  
- teaching/analysis modes  
- debugging the shim and logic layer  

---

# Example 1 — Local vs Structural vs Continuity Move

### Position  
Black has a weak group on the right side.  
White has a large moyo forming on the left.  
It is Black’s turn.

### Candidate Moves  
- **A:** Atari the cutting stone  
- **B:** Extend the weak group  
- **C:** Expand left‑side moyo boundary  

---

## RTT Interpretation

### **Lumen (RTT/1)**  
- identifies weak group on right  
- identifies moyo boundary on left  
- influence map shows left side is globally dominant  

### **Hephaestus (RTT/2)**  
- A → **1/3 local**  
- B → **2/3 structural**  
- C → **3/3 continuity**  

### **Aurion (RTT/3)**  
- A → paradox risk (locally good, globally bad)  
- B → stabilizes topology  
- C → continuity‑aligned but risky due to weak group  

### **Harmonia (RTT/12)**  
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

# Example 2 — Ladder Ancestry & Projection‑Loss

### Position  
White threatens a ladder on the right side.  
Black has a potential ladder‑breaker on the left, but it is thin.

### Candidate Moves  
- **A:** Play the ladder‑breaker  
- **B:** Strengthen the laddered group  
- **C:** Ignore and expand center influence  

---

## RTT Interpretation

### **Lumen (RTT/1)**  
- identifies ladder path  
- identifies thin ladder‑breaker  
- pressure map shows center expansion is viable  

### **Hephaestus (RTT/2)**  
- A → **2/3 structural**  
- B → **1/3 local**  
- C → **3/3 continuity**  

### **Aurion (RTT/3)**  
- A → ladder ancestry unstable  
- B → stabilizes ancestry  
- C → projection‑loss risk (ignoring ladder breaks continuity)  

### **Harmonia (RTT/12)**  
Triadic scores:

| Move | Ladder Stability | Structural | Continuity | Projection Loss | Final |
|------|------------------|------------|------------|------------------|-------|
| A | **unstable** | high | medium | medium | medium |
| B | **stable** | medium | medium | low | **high** |
| C | medium | medium | **high** | **high** | low |

### **RTT‑Go Decision**  
**Move B** — strengthen the laddered group — is selected.  
It preserves ancestry, avoids projection‑loss, and maintains continuity.

---

# Example 3 — Moyo Continuity vs Local Gain

### Position  
White has a large moyo on the top side.  
Black has a chance to invade locally or expand globally.

### Candidate Moves  
- **A:** Local invasion  
- **B:** Reduce moyo from the outside  
- **C:** Expand Black’s own moyo on the bottom  

---

## RTT Interpretation

### **Lumen (RTT/1)**  
- identifies moyo boundaries  
- identifies invasion points  
- pressure map shows top moyo is strong  

### **Hephaestus (RTT/2)**  
- A → **1/3 local**  
- B → **2/3 structural**  
- C → **3/3 continuity**  

### **Aurion (RTT/3)**  
- A → paradox risk (local gain, global collapse)  
- B → stable reduction  
- C → continuity‑aligned but risky if moyo is thin  

### **Harmonia (RTT/12)**  
Triadic scores:

| Move | Local | Structural | Continuity | Drift | Final |
|------|-------|------------|------------|-------|-------|
| A | high | low | low | negative | low |
| B | medium | **high** | medium | positive | **high** |
| C | low | medium | **high** | medium | medium |

### **RTT‑Go Decision**  
**Move B** — reduce the moyo from the outside — is selected.  
It preserves continuity while avoiding paradox.

---

# Example 4 — Ko Topology & Paradox Suppression

### Position  
A large ko fight is developing in the center.  
Both players have ko threats, but Black’s threats are weaker.

### Candidate Moves  
- **A:** Start the ko  
- **B:** Strengthen ko threats  
- **C:** Play a stabilizing move elsewhere  

---

## RTT Interpretation

### **Lumen (RTT/1)**  
- identifies ko shape  
- identifies weak threats  
- pressure map shows center instability  

### **Hephaestus (RTT/2)**  
- A → **1/3 local**  
- B → **2/3 structural**  
- C → **3/3 continuity**  

### **Aurion (RTT/3)**  
- A → paradox risk (ko unstable)  
- B → stabilizes ko ancestry  
- C → continuity‑aligned but may concede initiative  

### **Harmonia (RTT/12)**  
Triadic scores:

| Move | Ko Stability | Structural | Continuity | Paradox | Final |
|------|--------------|------------|------------|---------|-------|
| A | **unstable** | medium | low | **high** | low |
| B | **stable** | high | medium | low | **high** |
| C | medium | medium | **high** | medium | medium |

### **RTT‑Go Decision**  
**Move B** — strengthen ko threats — is selected.  
It stabilizes ko topology and avoids paradox.

---

# Example 5 — Drift & Coherence Alignment

### Position  
The game is transitioning from midgame to endgame.  
Influence drift is shifting from left → center.

### Candidate Moves  
- **A:** Play a large endgame move on the left  
- **B:** Reinforce center influence  
- **C:** Start a small fight on the right  

---

## RTT Interpretation

### **Lumen (RTT/1)**  
- identifies drift direction  
- identifies influence arcs  
- identifies weak points  

### **Hephaestus (RTT/2)**  
- A → **1/3 local**  
- B → **2/3 structural**  
- C → **1/3 local**  

### **Aurion (RTT/3)**  
- A → drift‑misaligned  
- B → drift‑aligned  
- C → paradox risk  

### **Harmonia (RTT/12)**  
Triadic scores:

| Move | Drift Alignment | Structural | Continuity | Final |
|------|------------------|------------|------------|-------|
| A | negative | medium | medium | low |
| B | **positive** | **high** | high | **high** |
| C | negative | low | low | low |

### **RTT‑Go Decision**  
**Move B** — reinforce center influence — is selected.  
It aligns with drift, preserves continuity, and stabilizes structure.

---

# Summary

These examples demonstrate how RTT‑Go:

- interprets Go positions through triadic identity  
- resolves paradox vs continuity  
- stabilizes ladders, ko, and ancestry  
- aligns moves with drift/coherence  
- avoids projection‑loss  
- produces continuity‑preserving decisions  

RTT does not replace Go engines — it **reveals** the deeper structure already inside the game.
