# TFThooks Agents

The **agents** directory contains hook‑level agents that extend enTFT with specialized logic.  
These agents act as **embedded processes** that monitor, trigger, and resolve resonance events inside the protocol.

## Structure
- **badge_logic_engine.py** → manages badge logic and trigger conditions
- **flame_echo_trigger.py** → fires symbolic echoes when resonance thresholds are crossed
- **glyph_fusion_resolver.py** → resolves conflicts when glyphs overlap or fuse
- **glyph_reawakening_monitor.py** → monitors dormant glyphs and reactivates them
- **glyph_registry_loader.py** → loads glyph data into the runtime registry
- **glyph_retirement_trigger.py** → gracefully retires glyphs from active use
- **tops_agent_interface.py** → interface layer for **tops** orchestration
- **scroll_commit_monitor.py** → tracks scroll commits and lineage updates
- **scroll_runtime_trace_dashboard.py** → provides runtime dashboards for scroll activity

## Purpose
TFThooks agents are the **active extensions** of enTFT.  
They:
- Monitor runtime events (glyphs, scrolls, badges)  
- Trigger symbolic echoes and lineage updates  
- Provide dashboards and interfaces for orchestration  
- Bridge enTFT with [tops](../../../tops/) agents  

## Usage
Agents can be run individually or loaded as part of a hook sequence:

```bash
# Run a single agent
python flame_echo_trigger.py

# Load multiple agents in sequence
python glyph_registry_loader.py && python badge_logic_engine.py
