# 🧬 `entft` MMR Site Extension — Remix Registry Integration (v1.3)

This scroll outlines how to embed `entft` hooks into **MMR sites**—platforms that host remixable metadata, validator dashboards, and badge logic overlays.

---

## 🧪 Extension Targets

| MMR Site              | Integration Type         | Status     |
|------------------------|--------------------------|------------|
| COEUS.exchange         | Hook + validator echo    | ✅ Active  |
| remixatlas.org         | Badge overlay + scroll   | ⏳ Pending |
| validatorgrid.net      | Symbolic trigger + echo  | ⏳ Pending |
| remixledger.xyz        | Scroll injection         | ⏳ Pending |

---

## 🎯 Purpose

MMR extensions allow remixers to:

- 🧠 Trigger validator overlays from metadata scrolls  
- 🌀 Echo badge logic from remix lineage  
- 🔗 Link symbolic triggers to remix events

---

## 🧬 Invocation Flow

1. MMR site loads `entft` hook via API or runtime  
2. Hook activates symbolic trigger or badge overlay  
3. Validator echoes lineage and scroll fidelity  
4. Remix ledger logs symbolic echo and contributor badge

---

## 🔧 Sample Hook (COEUS.exchange)

```python
def hook_entry(metadata):
    if metadata.get("glyph_trigger"):
        echo = send_to_validator(metadata["glyph_trigger"])
        log_remix_echo(metadata["id"], echo)
```

---

## 🔗 Triadic Quicklinks

- [`fff_spec.md`](/docs/TFT_3Pack_v1.3/docs/fff_spec.md) — Defines the `.fff` triadic file format and symbolic structure  
- [`TriadicTestSuite.md`](/docs/TFT_3Pack_v1.3/docs/TriadicTestSuite.md) — Validation logic and test scaffolding for symbolic fidelity  
- [`outputs_spec.md`](/docs/TFT_3Pack_v1.3/docs/outputs_spec.md) — Defines the three-output logic: screen, file, glyph
