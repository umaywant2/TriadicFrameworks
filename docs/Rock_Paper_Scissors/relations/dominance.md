# Relation: Dominance

**Module:** Rock_Paper_Scissors  
**Relation Type:** Cyclic Triadic Dominance  
**ID:** `dominance`  

---

## 1. Formal Definition

Let `E = {Rock, Paper, Scissors}` and `≻` denote "dominates."

```
Rock     ≻ Scissors   (crushes)
Scissors ≻ Paper      (cuts)
Paper    ≻ Rock       (covers)
```

### 1.1 Algebraic Properties

| Property      | Holds? | Notes                                                    |
|---------------|--------|----------------------------------------------------------|
| Irreflexivity | ✅     | No entity dominates itself                               |
| Asymmetry     | ✅     | If A ≻ B then ¬(B ≻ A)                                  |
| Transitivity  | ❌     | Rock ≻ Scissors ≻ Paper does not imply Rock ≻ Paper      |
| Cyclicity     | ✅     | Length-3 cycle; group symmetry Z₃                        |

### 1.2 Cycle Diagram

```
     Rock
    ↗    ↘
Paper ←— Scissors
```

(Arrow = "is beaten by")

---

## 2. Triadic Interpretation

| Move                              | Interpretation                                      |
|-----------------------------------|-----------------------------------------------------|
| Firstness ≻ Thirdness (Rock ≻ Scissors)   | Brute immediacy destroys mechanism of mediation |
| Thirdness ≻ Secondness (Scissors ≻ Paper) | Differentiation severs relational coverage      |
| Secondness ≻ Firstness (Paper ≻ Rock)     | Context supersedes pure presence                |

No mode is universally supreme — encoding the irreducibility of all three Peircean categories.

---

## 3. Adjacency Matrix

Rows = winner, Columns = loser. `1` = row dominates column.

|              | Rock | Paper | Scissors |
|--------------|:----:|:-----:|:--------:|
| **Rock**     |  0   |   0   |    1     |
| **Paper**    |  1   |   0   |    0     |
| **Scissors** |  0   |   1   |    0     |

---

## 4. JSON Encoding

```json
{
  "relation_id": "dominance",
  "type": "cyclic_binary",
  "edges": [
    {"from": "rock",     "to": "scissors", "label": "crushes"},
    {"from": "scissors", "to": "paper",    "label": "cuts"},
    {"from": "paper",    "to": "rock",     "label": "covers"}
  ],
  "properties": {
    "irreflexive": true, "asymmetric": true,
    "transitive": false, "cyclic": true,
    "cycle_length": 3,   "group_symmetry": "Z3"
  }
}
```
