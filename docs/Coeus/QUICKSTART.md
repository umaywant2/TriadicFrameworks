# 🚀 Coeus QUICKSTART  
*Launch your multi-AI research sandbox in minutes*

---

## 🧱 Requirements

- Python 3.10+  
- Git  
- Basic terminal access  
- Optional: Docker for containerized runs

---

## 📦 Setup

```bash
# Clone the TriadicFrameworks repo
git clone https://github.com/umaywant2/TriadicFrameworks.git
cd TriadicFrameworks/docs/Coeus

# Install dependencies (if any)
pip install -r requirements.txt
```

---

## 🧠 Launch Sandbox

```bash
# Start sandbox with 3 AI agents
python sandbox/launch_sandbox.py --agents 3 --mode enTFT

# Agents: nous, enTFT, tops
# Mode: enTFT encryption active
```

---

## 🪙 Mint a Coin

```bash
# Create a new research coin
python sandbox/mint_coin.py --type legacy --name "PharmaTFT"

# Coin types: legacy, priority, remix
# Coin names: any symbolic stub or challenge
```

---

## 🔍 Monitor Agent Logs

```bash
# View trace log for coin resolution
cat sandbox/logs/coin_001_trace.log

# Includes agent actions, folding events, observer notes
```

---

## 🔐 Exchange or Tossback

- Completed coins are minted into artifacts or tokenized for exchange  
- Unsolved coins are returned to the sandbox for reattempt  
- All transactions encrypted via enTFT

---

## 🧩 Optional: Fork & Remix

- Fork the repo  
- Add your own coin stubs to `coins/coin_templates.json`  
- Customize agent logic in `agents/`  
- Launch your own sandbox instance

---

## 🧠 Reminder

Coeus is designed to be minimal, forkable, and remixable.  
No fluff. Just cognition. Let it echo.

---
