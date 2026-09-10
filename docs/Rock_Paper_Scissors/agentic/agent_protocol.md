# Agentic Protocol: Move Selection

**Module:** Rock_Paper_Scissors  
**ID:** `agent_protocol`  

---

## 1. Agent Tiers

### Tier 0 — Naive Agent (Firstness)
Selects uniformly at random. Implements Nash by default.

```python
import random
def naive_agent():
    return random.choice(["rock", "paper", "scissors"])
```

### Tier 1 — Adaptive Agent (Secondness)
Maintains frequency model of opponent; responds with dominant counter.

```python
from collections import Counter
def adaptive_agent(opponent_history: list[str]) -> str:
    if not opponent_history:
        return naive_agent()
    most_frequent = Counter(opponent_history).most_common(1)[0][0]
    counters = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    return counters[most_frequent]
```

### Tier 2 — Triadic Agent (Thirdness)
Models opponent's reasoning tier recursively.

```python
def triadic_agent(opponent_history, opponent_tier_estimate, self_history):
    counters = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    if opponent_tier_estimate == 0:
        if opponent_history:
            most_freq = Counter(opponent_history).most_common(1)[0][0]
            return counters[most_freq]
        return naive_agent()
    elif opponent_tier_estimate == 1:
        if self_history:
            my_most_freq = Counter(self_history).most_common(1)[0][0]
            their_response = counters[my_most_freq]
            return counters[their_response]  # counter the counter
        return naive_agent()
    else:
        return naive_agent()  # Nash is optimal vs. triadic opponent
```

---

## 2. Triadic Position Priors (Pre-history initialization)

| Entity   | Novice Prior | Expert Prior (Nash) |
|----------|:------------:|:-------------------:|
| Rock     | 0.354        | 0.333               |
| Paper    | 0.317        | 0.333               |
| Scissors | 0.329        | 0.333               |

---

## 3. Decision Loop

```
LOOP each round:
  1. Observe opponent history H
  2. Estimate opponent tier T ∈ {0, 1, 2}
  3. Select move M = triadic_agent(H, T, self_history)
  4. Observe outcome O ∈ {win, draw, loss}
  5. Update opponent model and self history
  6. If O = loss → increment tier estimate
  7. If 3+ consecutive wins → freeze current strategy
END LOOP
```

---

## 4. Sign Mapping of Agent Strategies

| Strategy Layer      | Triadic Position | Peirce Mode | Behavior                       |
|---------------------|------------------|-------------|--------------------------------|
| Nash (random)       | Firstness        | Qualisign   | Pure potentiality; no relation |
| Adaptive (counter)  | Secondness       | Sinsign     | Reactive to observed Other     |
| Triadic (recursive) | Thirdness        | Legisign    | Models law governing opponent  |
```
