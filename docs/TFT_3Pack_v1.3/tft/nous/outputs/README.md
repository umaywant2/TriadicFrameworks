# Nous Outputs

The **nous_outputs** directory contains logs, traces, and generated artifacts from running the agent‑shell.  
This is where remixers can observe the living resonance of the system.

## Structure
- `remix_trace.log` → lineage and remix events
- `validator_handshake.log` → validator protocol traces
- Other logs → performance metrics, symbolic overlays

## Purpose
Outputs are the **echoes** of the agent‑shell.  
They provide transparency, lineage tracking, and debugging insight for contributors.

## Cross‑links
- [core_logic](../nous/core_logic/) → generates logs
- [bots](../nous/bots/) → may produce their own traces
- [tops](../tops/) → consumes outputs for dashboards and overlays
