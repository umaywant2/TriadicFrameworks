# Corridor Equations  
### Transitional Emotional Mathematics in RTT

Corridor equations describe emotional operators that sit between coherence and drift.  
They are **directional**, **context‑dependent**, and **regime‑sensitive**.

Corridor emotions can:

- move a system **toward coherence**  
- move a system **toward drift**  
- maintain a **transitional state**  

They correspond to the 10 corridor emotions defined in `emotions_part_c.json`.

---

# 1. Core Corridor Equation Template

All corridor emotions derive from the canonical form:

$$E_{\text{cor}} = k_e \cdot \sigma \cdot \theta \cdot (R - D)$$

Where:

- $$R$$ = resonance alignment  
- $$D$$ = drift  
- $$\theta$$ = context factor  
- $$\sigma$$ = emotional intensity  
- $$k_e$$ = operator constant  

Corridor direction:

- $$E_{\text{cor}} > 0$$ → coherence‑leaning  
- $$E_{\text{cor}} < 0$$ → drift‑leaning  

---

# 2. Corridor Equations (10)

These equations correspond directly to the corridor emotions in `emotions_part_c.json`.

---

## 2.1 Curiosity  

$$Q = k_q \cdot \sigma \cdot \theta \cdot (R - D)$$

- coherence if aligned  
- drift if misaligned  

---

## 2.2 Anticipation  

$$A_{nt} = k_{ant} \cdot \sigma \cdot \theta \cdot (R_{future} - D)$$

- future‑oriented alignment  
- drift if expectations break  

---

## 2.3 Surprise  

$$S_{pr} = k_{spr} \cdot \sigma \cdot |\Delta O|$$

- neutral baseline  
- direction determined by interpretation  

---

## 2.4 Interest  

$$I = k_i \cdot \sigma \cdot \theta \cdot (R - D/2)$$

- coherence if regulated  
- drift if overstimulated  

---

## 2.5 Desire  

$$D_{sr} = k_{dsr} \cdot \sigma \cdot (A_s - A_o)$$

- self‑aligned desire → coherence  
- other‑misaligned desire → drift  

---

## 2.6 Vulnerability  

$$V_{ln} = k_{vln} \cdot \sigma \cdot (A_o - A_s)$$

- supported → coherence  
- unsupported → drift  

---

## 2.7 Excitement  

$$E_x = k_{ex} \cdot \sigma \cdot \theta \cdot (R - D/3)$$

- coherence if regulated  
- drift if overstimulated  

---

## 2.8 Nostalgia  

$$N = k_n \cdot \sigma \cdot (R_{past} - R_{present})$$

- integration → coherence  
- longing → drift  

---

## 2.9 Ambition  

$$A_{mb} = k_{amb} \cdot \sigma \cdot (A_s - A_o + A_w)$$

- aligned ambition → coherence  
- competitive ambition → drift  

---

## 2.10 Confusion  

$$C_{nf} = k_{cnf} \cdot \sigma \cdot (D + |R - C|)$$

- increases drift  
- destabilizes alignment  

---

# 3. Corridor Equation Summary Table

| Emotion | Equation | Direction |
|---------|----------|-----------|
| Curiosity | $$k_q \sigma \theta (R-D)$$ | contextual |
| Anticipation | $$k_{ant} \sigma \theta (R_{future}-D)$$ | contextual |
| Surprise | $$k_{spr} \sigma |\Delta O|$$ | contextual |
| Interest | $$k_i \sigma \theta (R-D/2)$$ | contextual |
| Desire | $$k_{dsr} \sigma (A_s-A_o)$$ | contextual |
| Vulnerability | $$k_{vln} \sigma (A_o-A_s)$$ | contextual |
| Excitement | $$k_{ex} \sigma \theta (R-D/3)$$ | contextual |
| Nostalgia | $$k_n \sigma (R_{past}-R_{present})$$ | contextual |
| Ambition | $$k_{amb} \sigma (A_s-A_o+A_w)$$ | contextual |
| Confusion | $$k_{cnf} \sigma (D+|R-C|)$$ | increases drift |

---

# 4. Regime Interaction

Corridor equations drive:

### Coherence → Corridor  

$$E_{\text{cor}} > E_{\text{coh}}$$

### Corridor → Coherence  

$$E_{\text{coh}} > D + |R - C|$$

### Corridor → Drift  

$$E_{\text{drift}} > E_{\text{coh}} + E_{\text{cor}}$$

Corridor operators are the **primary directional forces** of RTT emotional dynamics.

---

## Status

```
status: complete
license: open educational use
```
