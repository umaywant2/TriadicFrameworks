# Corridor Operators  
### Transitional Emotional Operators in RTT

Corridor operators are emotional actions that sit between coherence and drift.  
They are **context‑dependent**, meaning they can:

- move a system **toward coherence**  
- move a system **toward drift**  
- or maintain a **transitional state**  

Corridor operators are the most dynamic emotional operators in RTT.  
They represent **ambiguity**, **potential**, and **directional instability**.

---

## Core Corridor Equation

All corridor operators derive from the general form:

\[
E_{\text{cor}} = k_e \cdot \sigma \cdot \theta \cdot (R - D)
\]

Where:

- \(R\) = resonance alignment  
- \(D\) = drift  
- \(\theta\) = context factor  
- \(\sigma\) = emotional intensity  
- \(k_e\) = operator constant  

Corridor operators are **directional**:

- \(E_{\text{cor}} > 0\) → coherence‑leaning  
- \(E_{\text{cor}} < 0\) → drift‑leaning  

---

# Corridor Operators (10)

These correspond to the 10 emotions in `emotions_part_c.json`.

---

## 1. Curiosity Operator  
**Symbol:** \( \mathcal{Q} \)  
**Equation:**  
\[
Q = k_q \cdot \sigma \cdot \theta \cdot (R - D)
\]

**Effect:**  
- coherence if aligned  
- drift if misaligned  

**Triad:** (+1, 0, +1)

---

## 2. Anticipation Operator  
**Symbol:** \( \mathcal{A}_{nt} \)  
**Equation:**  
\[
A_{nt} = k_{ant} \cdot \sigma \cdot \theta \cdot (R_{future} - D)
\]

**Effect:**  
- future‑oriented alignment  
- can amplify drift if expectations break  

**Triad:** (+1, 0, +1)

---

## 3. Surprise Operator  
**Symbol:** \( \mathcal{S}_{pr} \)  
**Equation:**  
\[
S_{pr} = k_{spr} \cdot \sigma \cdot |\Delta O|
\]

**Effect:**  
- neutral baseline  
- direction determined by interpretation  

**Triad:** (0, 0, 0)

---

## 4. Interest Operator  
**Symbol:** \( \mathcal{I} \)  
**Equation:**  
\[
I = k_i \cdot \sigma \cdot \theta \cdot (R - D/2)
\]

**Effect:**  
- coherence if aligned  
- drift if overstimulated  

**Triad:** (+1, 0, +1)

---

## 5. Desire Operator  
**Symbol:** \( \mathcal{D}_{sr} \)  
**Equation:**  
\[
D_{sr} = k_{dsr} \cdot \sigma \cdot (A_s - A_o)
\]

**Effect:**  
- self‑aligned desire → coherence  
- other‑misaligned desire → drift  

**Triad:** (+1, –1, 0)

---

## 6. Vulnerability Operator  
**Symbol:** \( \mathcal{V}_{ln} \)  
**Equation:**  
\[
V_{ln} = k_{vln} \cdot \sigma \cdot (A_o - A_s)
\]

**Effect:**  
- supported → coherence  
- unsupported → drift  

**Triad:** (–1, +1, 0)

---

## 7. Excitement Operator  
**Symbol:** \( \mathcal{E}_{x} \)  
**Equation:**  
\[
E_x = k_{ex} \cdot \sigma \cdot \theta \cdot (R - D/3)
\]

**Effect:**  
- coherence if regulated  
- drift if overstimulated  

**Triad:** (+1, 0, +1)

---

## 8. Nostalgia Operator  
**Symbol:** \( \mathcal{N} \)  
**Equation:**  
\[
N = k_n \cdot \sigma \cdot (R_{past} - R_{present})
\]

**Effect:**  
- integration → coherence  
- longing → drift  

**Triad:** (+1, 0, –1)

---

## 9. Ambition Operator  
**Symbol:** \( \mathcal{A}_{mb} \)  
**Equation:**  
\[
A_{mb} = k_{amb} \cdot \sigma \cdot (A_s - A_o + A_w)
\]

**Effect:**  
- aligned ambition → coherence  
- competitive ambition → drift  

**Triad:** (+1, –1, +1)

---

## 10. Confusion Operator  
**Symbol:** \( \mathcal{C}_{nf} \)  
**Equation:**  
\[
C_{nf} = k_{cnf} \cdot \sigma \cdot (D + |R - C|)
\]

**Effect:**  
- increases drift  
- destabilizes alignment  

**Triad:** (–1, 0, –1)

---

# Corridor Operator Summary Table

| Operator | Symbol | Regime | Drift Effect | Triad |
|---------|--------|--------|--------------|--------|
| Curiosity | \( \mathcal{Q} \) | corridor | contextual | (+1,0,+1) |
| Anticipation | \( \mathcal{A}_{nt} \) | corridor | contextual | (+1,0,+1) |
| Surprise | \( \mathcal{S}_{pr} \) | corridor | contextual | (0,0,0) |
| Interest | \( \mathcal{I} \) | corridor | contextual | (+1,0,+1) |
| Desire | \( \mathcal{D}_{sr} \) | corridor | contextual | (+1,–1,0) |
| Vulnerability | \( \mathcal{V}_{ln} \) | corridor | contextual | (–1,+1,0) |
| Excitement | \( \mathcal{E}_{x} \) | corridor | contextual | (+1,0,+1) |
| Nostalgia | \( \mathcal{N} \) | corridor | contextual | (+1,0,–1) |
| Ambition | \( \mathcal{A}_{mb} \) | corridor | contextual | (+1,–1,+1) |
| Confusion | \( \mathcal{C}_{nf} \) | corridor | increases | (–1,0,–1) |

---

## Status

```
status: complete
license: open educational use
```
