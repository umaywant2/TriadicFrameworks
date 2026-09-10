# Relation: Outcomes

**Module:** Rock_Paper_Scissors  
**Relation Type:** Full Outcome Matrix  
**ID:** `outcomes`  

---

## 1. Outcome Matrix

Rows = Player A's choice. Cell = outcome for **Player A**.  
`+1` = win · `0` = draw · `-1` = loss

|               | **vs. Rock** | **vs. Paper** | **vs. Scissors** |
|---------------|:------------:|:-------------:|:----------------:|
| **Rock**      |      0       |      −1       |       +1         |
| **Paper**     |     +1       |       0       |       −1         |
| **Scissors**  |     −1       |      +1       |        0         |

Matrix is **antisymmetric** and **skew-symmetric** (M = −Mᵀ) — hallmark of zero-sum symmetric games.

---

## 2. Formal Properties

| Property       | Value  |
|----------------|--------|
| Zero-sum       | ✅     |
| Antisymmetric  | ✅     |
| Diagonal       | All 0  |
| Matrix rank    | 2      |

---

## 3. JSON Encoding

```json
{
  "relation_id": "outcomes",
  "encoding": {"win": 1, "draw": 0, "loss": -1},
  "matrix": {
    "rock":     {"vs_rock": 0,  "vs_paper": -1, "vs_scissors": 1},
    "paper":    {"vs_rock": 1,  "vs_paper": 0,  "vs_scissors": -1},
    "scissors": {"vs_rock": -1, "vs_paper": 1,  "vs_scissors": 0}
  },
  "nash_equilibrium": "uniform_mixed_1/3"
}
```

---

## 4. Expected Value Table (Nash Play)

| Matchup Scenario       | E[Payoff for A] |
|------------------------|:---------------:|
| Nash vs. Nash          | 0.000           |
| Nash vs. Rock-only     | +0.333          |
| Nash vs. Paper-only    | +0.333          |
| Nash vs. Scissors-only | +0.333          |
| Pure strategy vs. Nash | −0.333          |
```
