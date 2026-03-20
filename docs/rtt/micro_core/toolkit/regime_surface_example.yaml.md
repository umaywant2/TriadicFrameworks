```yaml

# RTT Regime Surface Example
# This file defines a regime boundary without encoding behavior.

regime:
  name: "Thermal-Coherence-Band"
  description: >
    Stable operation where temperature gradients dominate
    over electrical coupling noise.

signals:
  spin:
    role: orientation
    stability: high
  elec:
    role: coupling
    stability: medium
  temp:
    role: governor
    stability: dominant

constraints:
  qroot_boundary:
    allow_raw_state: false
    export_aggregates_only: true

status_conditions:
  - Ready
  - Degraded
  - Transitioning
  - Unknown

```
