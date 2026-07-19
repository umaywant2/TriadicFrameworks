# ⚙️ TFThooks Runtime — Live Extension Layer (v1.3)

The `runtime` folder contains **hook scripts** that extend entft dynamically at execution time.  
These are plug-ins activated by the agent-shell, enabling symbolic overlays, badge logic, and validator handshakes.

---

## 🧪 Hook Examples

| File                      | Purpose                                                  |
|---------------------------|----------------------------------------------------------|
| `badge_trigger_hook.py`   | Adds new badge logic and symbolic triggers               |
| `glyph_overlay_hook.py`   | Overlays glyph resonance data during runtime             |
| `validator_extension.py`  | Extends validator handshake and echo fidelity            |

---

## 🎯 Purpose

Runtime hooks are the **live extensions** of entft.  
They let remixers experiment with new behaviors without modifying the protocol core.

- 🔌 Plug-in architecture for symbolic overlays  
- 🌀 Dynamic badge logic and echo triggers  
- 🧠 Validator extensions for scroll fidelity

---

## 🧬 Runtime Invocation Flow

1. `nous` loads runtime environment  
2. Hooks are registered via `runtime.extend()`  
3. Badge triggers and glyph overlays activate based on symbolic context  
4. Validator extensions echo lineage and scroll fidelity

---

## 🔗 Triadic Quicklinks

- [`fff_spec.md`](/docs/TFT_3Pack_v1.3/docs/fff_spec.md) — Defines the `.fff` triadic file format and symbolic structure  
- [`TriadicTestSuite.md`](/docs/TFT_3Pack_v1.3/docs/TriadicTestSuite.md) — Validation logic and test scaffolding for symbolic fidelity  
- [`outputs_spec.md`](/docs/TFT_3Pack_v1.3/docs/outputs_spec.md) — Defines the three-output logic: screen, file, glyph
