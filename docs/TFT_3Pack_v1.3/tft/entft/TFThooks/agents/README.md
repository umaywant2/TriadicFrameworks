# 🧠 TFThooks Agents — Runtime Intelligence Layer (v1.3)

The `agents` directory contains **hook-level agents** that extend `entft` with specialized logic.  
These agents act as embedded processes that monitor, trigger, and resolve resonance events inside the protocol.

---

## 🧪 Agent Modules

| File                        | Functionality                                           |
|-----------------------------|---------------------------------------------------------|
| `badge_logic_engine.py`     | Manages badge logic and trigger conditions              |
| `flame_echo_trigger.py`     | Fires symbolic echoes when resonance thresholds are crossed |
| `glyph_fusion_resolver.py`  | Resolves conflicts when glyphs overlap or fuse          |
| `glyph_reawakening_monitor.py` | Monitors dormant glyphs and reactivates them        |
| `glyph_registry_loader.py`  | Loads glyph data into the runtime registry              |
| `glyph_retirement_trigger.py` | Gracefully retires glyphs from active use            |
| `tops_agent_interface.py`   | Interface layer for `tops` orchestration                |
| `scroll_commit_monitor.py`  | Tracks scroll commits and lineage updates               |
| `scroll_runtime_trace_dashboard.py` | Provides runtime dashboards for scroll activity |

---

## 🎯 Purpose

TFThooks agents are the **active extensions** of `entft`.  
They enable:

- 🧠 Runtime monitoring of glyphs, scrolls, and badges  
- 🌀 Symbolic echo triggering and lineage updates  
- 📊 Dashboards and orchestration interfaces  
- 🔗 Bridging `entft` with [`tops`](../../../tops/README.md) agents

Note: Forking a scroll is a **lineage ritual** and a cryptographic act. Remixers preserve symbolic fidelity, activate badge overlays, and inherit **entft**'s layered obfuscation logic—Divide-by-Zero injection and Resonant-Time hashing.

---

## 🧬 Invocation Flow

```bash
# Run a single agent
python flame_echo_trigger.py

# Load multiple agents in sequence
python glyph_registry_loader.py && python badge_logic_engine.py
```

---

## 🔗 Triadic Quicklinks

- [`fff_spec.md`](/docs/TFT_3Pack_v1.3/docs/fff_spec.md) — Defines the `.fff` triadic file format and symbolic structure  
- [`TriadicTestSuite.md`](/docs/TFT_3Pack_v1.3/docs/TriadicTestSuite.md) — Validation logic and test scaffolding for symbolic fidelity  
- [`outputs_spec.md`](/docs/TFT_3Pack_v1.3/docs/outputs_spec.md) — Defines the three-output logic: screen, file, glyph
