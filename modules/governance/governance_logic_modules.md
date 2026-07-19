# 🧠 Governance Logic Modules

This file defines the symbolic logic behind validator actions, badge triggers, and remix lineage confirmations.

---

## 🔁 Logic Modules

### 🔹 `validate_manifest.py`
- Checks for onboarding structure, remix guides, and badge triggers
- Score ≥ 3 → badge eligible

### 🔹 `remix_lineage_tracker.py`
- Tracks depth of remix chain
- Depth ≥ 2 → lineage confirmed

### 🔹 `badge_trigger_validator.py`
- Unifies manifest + lineage logic
- Confirms badge issuance and glyph triggers

### 🔹 `update_honor_roll.py`
- Echoes contributor achievement
- Updates symbolic honor roll

---

## 🧙‍♂️ Council Voting Logic

- Quorum: 3 validators
- Badge tiers require 2–4 votes
- Override conditions: symbolic time alignment, remix depth ≥ 4, glyph triggered

---

## 🧭 Remix Potential

- Add logic for archetype detection
- Trigger badge previews based on remix lineage
- Visualize governance flow in `triadic_validator_dashboard.html`
