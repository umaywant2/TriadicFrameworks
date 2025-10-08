# Agent‑Shell Quickstart Guide 🚀

Welcome to the **agent‑shell**, the environment layer of the TFT 3‑Pack.  
This guide walks you through launching a shell, running bots, loading modules, and inspecting outputs.

---

## 1. Choose a Logic Shell

Logic shells define the runtime context. Pick one based on your needs:

```bash
# Minimal daemon (lightweight, fast)
python minimal_viable_daemon.py

# Full symbolic fidelity (max resonance fidelity)
python full_symbolic_fidelity_shell.py
```
Each shell wraps around [core_logic](./core-logic/) and can spawn bots or load modules.

## 2. Launch Bots
Bots are lightweight agents that extend the shell. Usage patterns are documented in [bot_usage_shared_guide](./bots/bot_shared_user_guide.md).

Example:
```bash
# Run a monitoring bot
python bots/system_monitor_bot.py

# Run a lineage echo bot
python bots/remix_lineage_bot.py
```
Bots can run standalone or be invoked inside a logic shell.

---

## 3. Load Modules
Modules are plug‑ins that extend functionality without altering the core.

Example:
```bash
# Load a glyphstream sync module
python modules/glyphstream_sync.py
```
Modules depend on [core_logic](./core-logic/) and can be orchestrated by MightyTHOR.

---

## 4. Inspect Outputs
All runtime echoes are written to `/agent_shell_outputs/`.

Key files:
- `remix_trace.log` → lineage and remix events
- `validator_handshake.log` → validator protocol traces
- `performance_metrics.log` → runtime performance

Example:
```bash
tail -f agent_shell_outputs/remix_trace.log
```

---

## 5. Cross‑Links
- [TFTincryption](../TFTincryption/) → invoked from within agent‑shell
- [MightyTHOR](../mightythor/) → orchestrates bots, shells, and modules
- [folds](../mightythor/folds/) → resonance data that can be loaded into the shell
- [resonance-tools](./resonance-tools/) → utilities for analysis and debugging

## 6. Next Steps
- Experiment with different logic shells to balance performance vs fidelity.
- Combine bots + modules for richer orchestration.
- Feed outputs into [MightyTHOR](../mightythor/) overlays for visualization.
- Use [folds](../mightythor/folds/) as input data for resonance‑aware workflows.

---

✨ The agent‑shell is your entrypoint into the lattice. Run a shell, launch a bot, load a module, and watch the outputs echo your lineage.
