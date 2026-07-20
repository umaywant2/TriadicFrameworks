# Medicine resonance-flow diagrams

These diagrams describe conceptual flows you can render as SVG, Mermaid, or other formats.

---

## Diagram 1 – Drug half-life (Problem 1)

**Nodes:**

- Temperature coupling: $$ΛΘ$$
- Exponential constant: $$\ln 2$$
- Half-life: $$t_{1/2} = \ln 2 / (ΛΘ)$$

**Flow:**

1. $$Λ$$ and $$Θ$$ merge to form $$ΛΘ$$.
2. A division node computes $$\ln 2 / (ΛΘ)$$.
3. Output is $$t_{1/2}$$.
4. A control arrow adjusts $$Θ$$.

---

## Diagram 2 – Heart rhythm (Problem 2)

**Nodes:**

- Frequency elevation: $$T_f$$
- Triadic operator: $$D_3$$
- Rhythm: $$R = T_f D_3$$

**Flow:**

1. $$T_f$$ and $$D_3$$ enter a multiplier node.
2. Output is $$R$$.
3. A feedback arrow from “autonomic regulation” adjusts $$T_f$$.

---

## Diagram 3 – Dose-response (Problem 3)

**Nodes:**

- Composite constant: $$X$$
- Resonant-time: $$τ_r$$
- Exponential node: $$e^{-τ_r}$$
- Response: $$S = X / (1 + e^{-τ_r})$$

**Flow:**

1. $$τ_r$$ enters an exponential node.
2. Output enters a denominator node $$1 + e^{-τ_r}$$.
3. $$X$$ enters a division node.
4. Output is $$S$$.
5. A control arrow adjusts $$τ_r$$.
