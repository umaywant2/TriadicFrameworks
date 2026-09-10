# Nash Equilibrium Reference

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
