# Bots

The **bots** directory contains lightweight agents that extend the **agent‑shell** environment.  
Each bot is a modular process designed to handle specific resonance tasks, from monitoring system load to echoing lineage events.

## Structure
- Individual bot scripts (Python/JS) → self‑contained, pluggable
- Shared usage guide → see [`bot_usage_shared_guide.md`](../bot_usage_shared_guide.md)

## Purpose
Bots are the “hands and feet” of the agent‑shell.  
They run alongside daemons and logic shells, providing adaptive functionality without bloating the core.

## Cross‑links
- [core_logic](../core_logic/) → bots rely on foundational runtime scripts
- [logic_shells](../logic_shells/) → bots can be invoked inside shells
- [resonance-tools](../resonance-tools/) → bots may call utilities for analysis
- [MightyTHOR](../../MightyTHOR/) → Thor agents can orchestrate bots at scale
