# Entity: Scissors

**Module:** Rock_Paper_Scissors  
**Triadic Position:** Thirdness  
**ID:** `scissors`  

---

## 1. Triadic Definition

Scissors occupies the **Third** position in the RPS triad. Thirdness is the mode of being defined by mediation, law, habit, and sign — it brings First and Second into relation. Scissors is the only entity that is itself a dyadic structure (two blades) operating as a unity. Its power is *differentiation*: it cuts, divides, and produces distinct edges. Scissors is the sign-vehicle of the triad.

### 1.1 Positional Semantics

| Dimension      | Value                                                        |
|----------------|--------------------------------------------------------------|
| Peirce Mode    | Thirdness                                                    |
| Quality        | Precision, differentiation, cutting, duality-in-unity        |
| Modality       | Mediation; law-like regularity; habit-formation              |
| Sign-type      | Legisign (general rule or type as sign)                      |
| Phenomenology  | Thirdness as synthesis; brings relation into act             |

### 1.2 Formal Triadic Slot

```
Triadic(Scissors) = <First=∅, Second=∅, Third=Scissors>
  → Scissors as mediating node; defined by the rule it instantiates
  → Affordance for dominance: over Paper (cuts/differentiates mediation)
  → Vulnerability to immediacy: by Rock (crushes the mechanism of distinction)
```

---

## 2. Relational Profile

| Relation     | Partner | Outcome | Sign Value | Mechanism                              |
|--------------|---------|---------|------------|----------------------------------------|
| Dominates    | Paper   | Win     | `+1`       | Cut (differentiation severs coverage)  |
| Dominated by | Rock    | Loss    | `-1`       | Crush (force destroys precision)       |
| Symmetric    | Scissors| Draw    | `0`        | Equal differentiation                  |

---

## 3. Agentic Properties

```yaml
agent_choice:
  entity: scissors
  risk_against: rock
  reward_against: paper
  nash_weight: 0.333
  heuristic_bias:
    - exploitation: optimal response to Paper-heavy opponents
    - meta_reasoning: advanced players who anticipate "counter Rock with Paper" choose Scissors
    - frequency: ~32.9% empirically by novice players
```

- Scissors as Thirdness also models **habit detection**: identifying and cutting an opponent's repeated behavioral pattern is structurally Scissor-like.

---

## 4. Triadic Encoding

```json
{
  "id": "scissors",
  "label": "Scissors",
  "triadic_position": "Thirdness",
  "peirce_sign_type": "Legisign",
  "beats": ["paper"],
  "beaten_by": ["rock"],
  "draws": ["scissors"],
  "outcome_vector": { "vs_rock": -1, "vs_paper": 1, "vs_scissors": 0 },
  "qualitative_descriptors": ["precise", "differentiating", "mediating", "dual", "cutting"],
  "agentic_weight_nash": 0.333
}
```

---

## 5. Cross-References

- `entities/Paper.md` · `entities/Rock.md` · `relations/dominance.md` · `agentic/agent_protocol.md`
```
