# Entity: Paper

**Module:** Rock_Paper_Scissors  
**Triadic Position:** Secondness  
**ID:** `paper`  

---

## 1. Triadic Definition

Paper occupies the **Second** position in the RPS triad. Secondness is the mode of being defined by its relation to another — brute dyadic encounter. Paper is inherently *relational*: it does not crush or cut, it *covers*, *wraps*, and *contextualizes*. Its power is derived from mediation, not intrinsic force.

### 1.1 Positional Semantics

| Dimension      | Value                                                  |
|----------------|--------------------------------------------------------|
| Peirce Mode    | Secondness                                             |
| Quality        | Flexibility, coverage, mediation, contextual authority |
| Modality       | Reaction; dyadic encounter; relation-dependence        |
| Sign-type      | Sinsign (singular relational event)                    |
| Phenomenology  | Brute dyadic fact; requires Other to be itself         |

### 1.2 Formal Triadic Slot

```
Triadic(Paper) = <First=∅, Second=Paper, Third=∅>
  → Paper as relational node; defined by what it covers and what cuts it
  → Affordance for dominance: over Rock (covers/contextualizes)
  → Vulnerability to differentiation: by Scissors (cut)
```

---

## 2. Relational Profile

| Relation     | Partner  | Outcome | Sign Value | Mechanism                        |
|--------------|----------|---------|------------|----------------------------------|
| Dominates    | Rock     | Win     | `+1`       | Cover (context supersedes force) |
| Dominated by | Scissors | Loss    | `-1`       | Cut (differentiation severs mediation) |
| Symmetric    | Paper    | Draw    | `0`        | Equal coverage                   |

---

## 3. Agentic Properties

```yaml
agent_choice:
  entity: paper
  risk_against: scissors
  reward_against: rock
  nash_weight: 0.333
  heuristic_bias:
    - exploitation: optimal response to Rock-heavy opponent models
    - anti-pattern: least chosen by novice players (~31.7% empirically)
    - second_order: sophisticated players anticipate Paper and pivot to Scissors
```

---

## 4. Triadic Encoding

```json
{
  "id": "paper",
  "label": "Paper",
  "triadic_position": "Secondness",
  "peirce_sign_type": "Sinsign",
  "beats": ["rock"],
  "beaten_by": ["scissors"],
  "draws": ["paper"],
  "outcome_vector": { "vs_rock": 1, "vs_paper": 0, "vs_scissors": -1 },
  "qualitative_descriptors": ["flexible", "mediating", "covering", "contextual", "relational"],
  "agentic_weight_nash": 0.333
}
```

---

## 5. Cross-References

- `entities/Rock.md` · `entities/Scissors.md` · `relations/dominance.md` · `agentic/agent_protocol.md`
```
