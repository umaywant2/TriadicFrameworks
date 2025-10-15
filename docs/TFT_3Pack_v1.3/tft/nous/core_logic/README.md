# Core Logic

The **core_logic** directory contains the foundational runtime scripts and daemons of the agent‑shell.  
These are the “engine parts” that every shell and bot depends on.

## Structure
- Daemon scripts → manage runtime lifecycle
- Logging modules → resonance trace, validator handshake
- Configs → environment setup, thresholds, resource allocation

## Purpose
Core logic is the **technical spine** of the agent‑shell.  
It ensures stability, logging, and fidelity across all shells and bots.

## Cross‑links
- [logic_shells](../logic_shells/) → shells wrap around core logic
- [bots](../bots/) → bots call into core logic for runtime hooks
- [resonance-tools](../resonance-tools/) → utilities extend core logic functions
