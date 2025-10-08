# Modules

The **modules** directory contains optional runtime modules that can be plugged into the agent‑shell.  
Modules extend functionality without altering the core or shells.

## Structure
- `glyphstream_sync.py` → symbolic overlay synchronization
- Other modules → experimental or specialized runtime extensions

## Purpose
Modules are the **plug‑ins** of the agent‑shell.  
They allow remixers to extend the environment with new capabilities while keeping the core clean.

## Cross‑links
- [core_logic](../core_logic/) → modules depend on foundational runtime
- [logic_shells](../logic_shells/) → shells can load modules dynamically
- [MightyTHOR](../../MightyTHOR/) → Thor can orchestrate modules across distributed nodes
