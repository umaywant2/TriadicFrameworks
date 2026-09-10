# Entity: Rock

**Module:** Rock_Paper_Scissors  
**Triadic Position:** Firstness  
**ID:** `rock`  

---

## 1. Triadic Definition

Rock occupies the **First** position in the RPS triad. In Peircean semiotics, Firstness is the mode of being that is what it is regardless of anything else — pure quality, immediacy, potentiality. Rock embodies this as brute, undifferentiated solidity: it does not reference another entity to be what it is. It simply *is*.

### 1.1 Positional Semantics

| Dimension      | Value                                             |
|----------------|---------------------------------------------------|
| Peirce Mode    | Firstness                                         |
| Quality        | Solidity, density, resistance, inertness          |
| Modality       | Actuality without relation                        |
| Sign-type      | Qualisign (quality as sign)                       |
| Phenomenology  | Brute presence; pre-relational; self-contained    |

### 1.2 Formal Triadic Slot

```
Triadic(Rock) = <First=Rock, Second=∅, Third=∅>
  → Rock as pure object, prior to relation
  → Affordance for dominance: over Scissors (crushes)
  → Vulnerability to mediation: by Paper (covered)
```

---

## 2. Relational Profile

| Relation     | Partner  | Outcome | Sign Value | Mechanism            |
|--------------|----------|---------|------------|----------------------|
| Dominates    | Scissors | Win     | `+1`       | Crush (force > edge) |
| Dominated by | Paper    | Loss    | `-1`       | Cover (context wraps force) |
| Symmetric    | Rock     | Draw    | `0`        | Equal resistance     |

---

## 3. Agentic Properties

```yaml
agent_choice:
  entity: rock
  risk_against: paper
  reward_against: scissors
  nash_weight: 0.333
  heuristic_bias:
    - loss_aversion: choose rock after Scissors loss (Firstness reset)
    - anchoring: rock is default/safe mental anchor for many players
```

- Nash equilibrium weight: **1/3**
- Empirical novice frequency: **~35.4%** — most commonly chosen throw
- Exploitation signal: opponent choosing Rock-heavy → up-weight Paper

---

## 4. Triadic Encoding

```json
{
  "id": "rock",
  "label": "Rock",
  "triadic_position": "Firstness",
  "peirce_sign_type": "Qualisign",
  "beats": ["scissors"],
  "beaten_by": ["paper"],
  "draws": ["rock"],
  "outcome_vector": { "vs_rock": 0, "vs_paper": -1, "vs_scissors": 1 },
  "qualitative_descriptors": ["solid", "inert", "immediate", "dense", "resistant"],
  "agentic_weight_nash": 0.333
}
```

---

## 5. Cross-References

- `entities/Paper.md` — entity that dominates Rock  
- `entities/Scissors.md` — entity dominated by Rock  
- `relations/dominance.md` · `relations/outcomes.md` · `agentic/agent_protocol.md`
```
