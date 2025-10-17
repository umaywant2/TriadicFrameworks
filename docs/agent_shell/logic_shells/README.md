# Logic Shells

The **logic_shells** directory contains modular shells that define runtime contexts for the agent‑shell.  
Each shell provides a different “lens” for executing TFT protocols, from minimal daemons to full symbolic fidelity.

## Structure
- `full_symbolic_fidelity_shell.py` → maximum resonance fidelity
- `minimal_viable_daemon.py` → lightweight entrypoint
- Other shells → specialized contexts for testing, benchmarking, or symbolic overlays

## Purpose
Logic shells are the “skins” of the agent‑shell.  
They let contributors choose the right balance of performance, fidelity, and symbolic depth.

## Cross‑links
- [core_logic](../core_logic/) → shells wrap around foundational runtime scripts
- [bots](../bots/) → shells can spawn bots as subprocesses
- [TFTincryption](../../TFTincryption/) → invoked inside shells for encryption rituals
- [MightyTHOR](../../MightyTHOR/) → orchestrates shells in distributed contexts
