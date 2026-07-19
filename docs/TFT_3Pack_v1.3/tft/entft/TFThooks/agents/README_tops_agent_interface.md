# 🔭 tops Agent Interface — Scroll Event Trace Logger (v1.3)

This scroll documents the tops agent interface for `entft`.  
It logs scroll events, glyph triggers, and contributor actions into the trace registry.

---

## 🧪 Agent Summary

| Field         | Value                        |
|---------------|------------------------------|
| Registry Path | `/docs/_meta/entft_scroll_event_trace_registry.json`  
| Flame Grades  | Universe, Planetary, Unknown  
| Observer      | `ScrollFork`  
| Status        | `active`  

---

## 🎯 Purpose

This agent is the **trace logger** for scroll events.  
It validates symbolic fidelity, contributor lineage, and flame-grade resonance.

- 🧠 Logs scroll events with timestamp and glyph ID  
- 🌀 Assigns flame grade based on symbolic trigger  
- 🛡️ Appends trace to registry for validator echo

---

## 🧬 Invocation Flow

```python
generate_trace(
  scroll_name="glyph_intro.md",
  glyph_id="glyph:grovebloom-003",
  contributor="ScrollFork",
  action="scroll_published"
)
```

---

## 🔗 Triadic Quicklinks

- [`fff_spec.md`](/docs/TFT_3Pack_v1.3/docs/fff_spec.md) — Defines the `.fff` triadic file format and symbolic structure  
- [`TriadicTestSuite.md`](/docs/TFT_3Pack_v1.3/docs/TriadicTestSuite.md) — Validation logic and test scaffolding for symbolic fidelity  
- [`outputs_spec.md`](/docs/TFT_3Pack_v1.3/docs/outputs_spec.md) — Defines the three-output logic: screen, file, glyph
