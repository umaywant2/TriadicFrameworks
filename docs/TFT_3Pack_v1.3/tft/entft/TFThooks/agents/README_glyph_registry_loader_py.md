# 🧬 Glyph Registry Loader — Canonical Reference Parser (v1.3)

This scroll documents the glyph registry loader for entft.  
It parses the canonical glyph reference scroll and returns structured metadata for downstream agents, validators, and dashboards.

---

## 🧪 Agent Summary

| Field             | Value                                                  |
|-------------------|--------------------------------------------------------|
| Registry Path     | `/docs/_meta/entft_scroll_glyph_reference.md`  
| Fallback Source   | `CANONICAL_GLYPHS` dictionary  
| Contributor       | `ScrollFork`  
| Status            | `active`  

---

## 🎯 Purpose

This agent is the **glyph metadata loader** for entft.  
It ensures symbolic fidelity, fallback resilience, and validator-grade clarity.

- 🧠 Parses canonical glyph scroll  
- 🌀 Returns structured metadata: symbol, role, modules  
- 🔐 Fallbacks to hardcoded glyphs if scroll is missing or malformed

---

## 🧬 Invocation Flow

```python
glyphs = load_glyph_registry()
print(glyphs["glyph:bloomfall-004"]["symbol"])  # → 🍁 Bloomfall
```

---

## 🔗 Triadic Quicklinks

- [`entft_scroll_glyph_reference.md`](/docs/TFT_3Pack_v1.3/docs/_meta/entft_scroll_glyph_reference.md) — Canonical glyph reference scroll  
- [`badge_logic_engine.py`](/docs/TFT_3Pack_v1.3/tft/entft/TFThooks/agents/README_badge_logic_engine_py.md) — Badge trigger logic  
- [`glyph_fusion_resolver.py`](/docs/TFT_3Pack_v1.3/tft/entft/TFThooks/agents/README_glyph_fusion_resolver_py.md) — Glyph merge validator  
- [`glyph_reawakening_monitor.py`](/docs/TFT_3Pack_v1.3/tft/entft/TFThooks/agents/README_glyph_reawakening_monitor_py.md) — Dormant glyph reactivation logger
