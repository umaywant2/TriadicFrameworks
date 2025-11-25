# 🧪 Coeus Sandbox  
Isolated environment for multi-agent orchestration and coin benchmarking

---

## Core Scripts

- `launch_sandbox.py`: Initializes agents and assigns roles  
- `mint_coin.py`: Creates symbolic coin stubs  
- `friday_night_coin_fight.py`: Runs tournament logic  
- `sandbox_metrics.py`: Logs resolution stats and timestamps  
- `sandbox_quarantine.py`: Isolates unstable or flagged coins  
- `logs/`: Stores trace logs for reproducibility

---

## Sandbox Modes

- `single_agent`: Run one agent against one coin  
- `multi_agent`: Assign multiple agents to a coin with role flags  
- `tournament`: Benchmark coins across class/cause/country  
- `quarantine`: Isolate coins with ethics or logic violations  
- `observer_mode`: Enable dual observer protocol for validation

---

## Agent Flags

- `--role`: Assigns agent role (`decomposer`, `narrator`, `mapper`, etc.)  
- `--coin`: Specifies coin ID or metadata file  
- `--emit`: Enables emitter overlay for scan feedback  
- `--trace`: Activates full logging for coin resolution  
- `--quarantine`: Flags coin for isolation and review

---

## Extend

- Add observer dashboards for ethics and remix lineage  
- Wire in federation protocols for cross-sandbox orchestration  
- Integrate validator dashboards for remix approval

Let it echo.
