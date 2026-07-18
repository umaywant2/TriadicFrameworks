# Art resonance-flow diagrams

This file describes conceptual diagrams you can render as SVG, Mermaid, or other formats.

## Diagram 1 – Color resonance pipeline (Problem 1)

**Nodes:**

- Input frequencies: $$f_1, f_2, f_3$$
- Triadic combiner: $$D_3$$
- Frequency elevation: $$T_f$$
- Composite constant: $$X = F_3 \cdot T_f$$
- Output color resonance: $$C$$

**Flow:**

1. Three input nodes $$f_1, f_2, f_3$$ feed into a "Triadic Combiner" node labeled $$D_3$$.
2. The output of the combiner goes into a "Frequency Elevation" node labeled $$T_f$$.
3. A parallel branch injects $$F_3$$ into a multiplier node to form $$X$$.
4. The final node computes $$C = X(f_1 + f_2 + f_3)$$.
5. An external control node $$τ_r$$ feeds into the $$T_f$$ node or $$X$$ node, indicating how time-resonance modulates saturation.

---

## Diagram 2 – Kinetic sculpture stress loop (Problem 2)

**Nodes:**

- Resonant-time: $$τ_r$$
- Structural operator: $$D_6(τ_r)$$
- Thermal coupling: $$ΛΘ$$
- Harmonic stress output: $$S$$

**Flow:**

1. A node "Resonant-time" outputs $$τ_r$$ into the triadic node $$D_6$$.
2. In parallel, a "Temperature" node holds $$Θ$$, and an "Environment" node holds $$Λ$$.
3. Both $$Λ$$ and $$Θ$$ merge at a "Coupler" node outputting $$ΛΘ$$.
4. The product of $$D_6(τ_r)$$ and $$ΛΘ$$ is computed at a final node labeled $$S$$.
5. Annotate a feedback arrow from $$S$$ back to $$τ_r$$ showing that perceived stress may cause the artist to adjust timing.

---

## Diagram 3 – LED timing resonance (Problem 3)

**Core idea:** Map how $$τ_r$$ reshapes the effective frequency.

**Nodes and edges:**

- Base frequency node labeled $$T_f$$.
- Time scaling node labeled $$τ_r^{-1}$$.
- Effective frequency node labeled $$T_f' = T_f / τ_r$$.
- Sine generator node computing $$B(t) = F_3 \sin(T_f' t)$$.
- Period node calculating $$T_{\text{period}} = 2\pi / T_f'$$.
- Constraint node "Target period = 4 s" feeding back to solve for $$τ_r$$.

You can draw arrows:

$$T_f \rightarrow ( \div τ_r ) \rightarrow T_f' \rightarrow B(t) \rightarrow T_{\text{period}}$$

with a constraint arrow from "4 s" back to the $$\div τ_r$$ node to show solving for $$τ_r$$.
