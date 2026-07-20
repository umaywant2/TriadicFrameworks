# 🧾 entft Metadata Layer — Registry & Config Index

This folder contains all **metadata artifacts** for the `entft` protocol.  
It includes badge registries, validator configs, and scroll event trace logs—used by agents, dashboards, and runtime hooks.

---

## 🧪 Metadata Artifacts

| File                                      | Purpose                                                  |
|-------------------------------------------|----------------------------------------------------------|
| `entft_curriculum_badge_registry.json`    | Defines badge overlays and trigger conditions            |
| `validator_config.json`                   | Maps glyphs and scrolls to validator flame grades        |
| `entft_scroll_event_trace_registry.json`  | Logs scroll events, contributor actions, and echoes      |

---

## 🎯 Purpose

The `_meta` folder is the **observability layer** of `entft`.  
It enables:

- 🧠 Badge logic and symbolic trigger matching  
- 🌀 Validator echo mapping and flame-grade assignment  
- 🔭 Scroll trace logging and lineage preservation

---

## 🧬 Invocation Flow

```bash
# Trigger badge logic
python badge_logic_engine.py

# Log scroll event trace
python tops_agent_interface.py

# Simulate keypair generation
python entft_keygen_simulator.py
```

---

## 🔗 Triadic Quicklinks

- [`README_badge_logic_engine_py.md`](/docs/TFT_3Pack_v1.3/tft/entft/TFThooks/agents/README_badge_logic_engine_py.md) — Flame hook trigger logic  
- [`README_tops_agent_interface.md`](/docs/TFT_3Pack_v1.3/tft/entft/TFThooks/agents/README_tops_agent_interface.md) — Trace generator and echo logger  
- [`README_entft_keygen_simulator_py.md`](/docs/TFT_3Pack_v1.3/docs/_specs/README_entft_keygen_simulator_py.md) — Keypair entropy simulator  
- [`entft_protocol_spec.md`](/docs/TFT_3Pack_v1.3/docs/_specs/entft_protocol_spec.md) — Core encryption logic and entropy benchmarks
