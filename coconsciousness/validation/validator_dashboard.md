# 🧪 CoConsciousness — Validator Dashboard

This file is updated by `score_coherence.py` after each run.

## How to use
- Run:
  ```bash
  python coconsciousness/validation/score_coherence.py
  ```
- Check the updated scores, sync logs, and any badges awarded below.
  
---

## Optional: tiny demo upgrade (if you want it)

If you want your demo to print a single combined sync line the validator can read easily by eye, you can keep your file as-is and add this echo:

### coconsciousness/demos/hello_coconsciousness.py (snippet)

```python
# Add near your loop prints:
both_sync = in_sync_looker and in_sync_planner
print(f"[SYNC] both={both_sync} {'🟢' if both_sync else '🔴'}")
```
- Why: Gives a one-glance “green or red” line while the validator script runs its own simulation separately.
