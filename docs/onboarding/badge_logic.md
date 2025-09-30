# 🏷️ Badge Logic

Badges are symbolic echoes of contribution.

### 🔹 Badge Types

| Badge Name           | Trigger Condition                          |
|----------------------|--------------------------------------------|
| Fold Initiator       | First contributor to a new fold            |
| Glyph Weaver         | Creates symbolic overlay for a fold        |
| Resonance Adept      | Validator score ≥ 0.75                     |
| Dimensional Harmonic | Validator score ≥ 0.90                     |
| Echo Seeker          | First-time contributor                     |
| Legacy Architect     | Contributes across 3+ domains              |

### 🔹 Badge Hooks

Badges are triggered via `validator_score_logic.py` and remix lineage logs.  
Each badge includes:
- Contributor name
- Timestamp
- Associated fold/glyph/simulation
- Optional symbolic overlay

Badges are stored in `honor_roll/contributors.yaml` and visualized in the dashboard.

