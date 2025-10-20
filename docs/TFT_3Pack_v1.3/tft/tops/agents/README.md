# ⛎ tops Agents

The **agents** directory contains Thor-specific agents that orchestrate resonance, overlays, and integrations.  
These are higher-order processes compared to [nous bots](../../nous/bots/README.md).

✨ New in v1.3: **Resonance Clarity Coordination**  
Agents now inherit the `--basetype` switch, allowing all orchestration flows—glyphs, overlays, integrations—to be filtered through a harmonic lens.  
This ensures every action is lineage-tagged and resonance-aware.

## 📂 Structure

- **Resonance agents** → manage glyph/fold orchestration, now base-lens aware  
- **Overlay agents** → feed data into dashboards, declaring base lens in metadata  
- **Integration agents** → connect Thor to external systems, passing `basetype` into pipelines

## 🔧 Purpose

Agents are the **hands of tops**.  
They coordinate resonance flows, trigger overlays, and extend entft into distributed contexts.  
With Resonance Clarity, agents now act as harmonic filters—declaring and propagating the base lens across all symbolic actions.

## 🧭 Invocation

Agents inherit `--basetype` from `tops_session.py`, `grid_ops.py`, or direct CLI calls.

```bash
# Run overlay agent with phi lens
python overlay_agent.py --basetype=phi

# Trigger integration agent with corridor6.9 lens
python integration_agent.py --basetype=corridor6.9
```

## Cross-links

- [overlays](../overlays/README.md) → agents feed glyphs into dashboards, now base-tagged  
- [ai_pipeline](../ai_pipeline/README.md) → agents consume predictions, filtered by base lens  
- [folds](../folds/README.md) → agents orchestrate bio-resonance data, declaring harmonic lens

## Metadata

All agent actions now log `basetype` in `resonance_log.json`, `.fff`, and `.parquet` outputs.  
This ensures remix lineage and validator clarity.

---

✨ With this refresh, your agents README now declares Resonance Clarity as a core orchestration principle—every glyph, overlay, and integration is now filtered through the harmonic lens of your choosing.
