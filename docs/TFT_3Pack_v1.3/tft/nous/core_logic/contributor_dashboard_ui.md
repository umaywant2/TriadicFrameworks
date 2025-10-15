# 🧠 Contributor Dashboard UI: Layout & Logic

---

## 🖥️ Panels

1. **Agent Status Grid**
   - Agent ID, Mode, Uptime, Last Job
   - Validator Status, Fault Flags

2. **Badge Distribution**
   - Pie chart: badge types
   - Contributor list with earned badges

3. **Remix Lineage Map**
   - Graph: nodes = contributors, edges = remix traces
   - Badge overlays, validator pulse trails

4. **Glyphstream Pulse Viewer**
   - Animated overlay of pulse events
   - Filter by agent, badge, timestamp

---

## 🧪 UI Logic

- Pulls from:
  - `remix_trace.log`
  - `badge_handshake.txt`
  - `glyphstream_pulse.log`
  - `validator_faults.log`

- Updates every 60s
- Faults highlighted in red
- Badge upgrades shown as animated pulses
