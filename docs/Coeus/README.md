<!-- ---
status: generated
version: "0.4"
description: "Coeus is TriadicFrameworks' multi-agent AI research sandbox, with a runnable three-agent quickstart and symbolic research tasks."
--- -->

<img width="1194" height="672" alt="Coeus_" src="https://github.com/user-attachments/assets/0562f8b9-86c1-477e-9dc6-cf90e536628c" />

- [`coeus_module.json`](https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/main/docs/Coeus/coeus_module.json) — Agentic module schema role assignments

# 🧠 Coeus Protocol
**A multi-agent AI research sandbox, part of [TriadicFrameworks](https://docs.triadicframeworks.org)**

Coeus is not a cryptocurrency, token or blockchain product — "coin" below is this module's own name for a research task, not a financial instrument — and it is unrelated to other software that shares the name "Coeus" (such as usecoeus.com, an unrelated AI note-taking tool). Coeus orchestrates multiple AI agents against those research coins for recursive cognition, remixable research, and observer-grade ethics.

## 🛑 Important!
Drift is On-by-Default long sessions lose anchors, turn off drift.

## ✋ Session string

```text
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## 🔧 What Is Coeus?

Coeus is a sandbox-ready module of TriadicFrameworks for orchestrating multi-agent AI research using symbolic "coin"-based tasking — an internal naming convention only, with no cryptocurrency, token or blockchain involved.

## 🚀 Quickstart

```bash
git clone https://github.com/umaywant2/TriadicFrameworks.git
cd TriadicFrameworks/docs/Coeus
python sandbox/launch_sandbox.py
```

This assigns roles across the `nous`, `entft` and `tops` agents and reports the sandbox as ready. `launch_sandbox.py` takes no command-line flags; the agent count and mode are fixed in the script.

The rest of the coin lifecycle is implemented as importable Python classes. There is no `mint_coin.py` yet, so a coin must be built as a plain dict before it can be tokenized, remixed, or reviewed.

## 🪙 Coin Lifecycle

1. **Mint:** create a symbolic research task
2. **Discover:** search the sandbox using FFF lens emitters
3. **Interpret:** convene agents to decode meaning
4. **Resolve:** apply TFT loop logic
5. **Validate:** review output for remixability
6. **Exchange:** share a citable research artifact; no cryptocurrency or blockchain step is involved

## Continue

- [TriadicFrameworks overview](/docs/ABOUT)
- [Core Terms glossary](/docs/GLOSSARY)
- [Coeus agent files](/docs/Coeus/agents/)
- [Coeus sandbox files](/docs/Coeus/sandbox/)
