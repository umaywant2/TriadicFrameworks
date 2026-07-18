## 🎮 Space Cadet Pinball → Civilizational Regime Stack  
### *RTT/vST Game Theme (Pseudocode)*

### Core Concept
The **ball** is *coordination energy*.  
The **table** is the Civilizational Regime Stack.  
The **player’s job** is to keep regimes aligned long enough to stabilize civilization.

---

### Game Objects

```pseudo
Ball {
    energy_level
    regime_alignment_score
}

Layer {
    name
    stability_threshold
    failure_mode
    bonus_multiplier
}
```

---

### Table Layout (Bottom → Top)

```pseudo
Layers = [
    MaterialsRegime,
    DeviceRegime,
    TechnologyRegime,
    EconomicRegime,
    InfrastructureRegime,
    CognitiveCulturalRegime
]
```

Each layer has **targets**, **ramps**, and **traps**.

---

### Example Layer Mechanics

#### Materials Regime (Bottom Bumpers)

```pseudo
if ball_hits("PhaseDiagramBumper"):
    increase(ball.energy_level)
    unlock("MetastableBonus")

if ball_hits("DefectTrap"):
    decrease(ball.energy_level)
    trigger("DegradationWarning")
```

---

#### Technology Regime (Mid‑Table Ramps)

```pseudo
if ramp_completed("ScaleUpRamp"):
    if EconomicRegime.aligned:
        score += high_bonus
    else:
        trigger("BrittleScaleFailure")
```

---

#### Cognitive & Cultural Regime (Top Targets)

```pseudo
if target_hit("IntegrativeMode"):
    stabilize_all_layers()
    score_multiplier += 2

if target_hit("DefensiveMode"):
    lock_flippers_temporarily()
    trigger("RegimeLockIn")
```

---

### Regime Mismatch Penalty

```pseudo
if TechnologyRegime.active and InfrastructureRegime.misaligned:
    trigger("ShadowSystemMode")
    ball_speed += chaos
```

---

### Win Condition

```pseudo
if all Layers.stable for time > threshold:
    trigger("CivilizationStabilized")
    multiball("ResilientFuture")
```

---

### Lose Condition

```pseudo
if ball.energy_level <= 0:
    trigger("SystemicCollapse")
    end_game()
```

---

## Why This Works Pedagogically

- Players **feel** regime mismatch before they can name it
- Success requires **phase separation** (explore vs stabilize)
- Defensive play *feels* safe but kills long‑term score
- Integrative play unlocks compounding bonuses

This is RTT/vST **embodied**, not explained.
