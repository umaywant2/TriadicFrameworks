# 🚀 Coeus Protocol — Quickstart Guide  
Initialize sandbox, mint coins, assign agents, and begin benchmarking

---

## 1. Clone the Repo

```bash
git clone https://github.com/your-org/CoeusProtocol.git
cd CoeusProtocol
```

---

## 2. Mint a Coin

```bash
python sandbox/mint_coin.py --name ElectroniumRedux --cause encryption
```

This creates a symbolic coin stub with metadata and UUID.

---

## 3. Launch Sandbox

```bash
python sandbox/launch_sandbox.py --coin ElectroniumRedux --role decomposer
```

Assign agents and initialize sandbox orchestration.

---

## 4. Run Tournament

```bash
python sandbox/friday_night_coin_fight.py --mode class
```

Benchmarks coins by class, cause, or country.

---

## 5. Tokenize Coin

```bash
python tokens/coin_tokenizer.py --coin ElectroniumRedux
```

Converts coin to token and registers in `token_ledger.json`.

---

## 6. Remix Coin

```bash
python coins/coin_remixer.py --coin ElectroniumRedux --mutation emotional
```

Forks coin with mutation and logs remix lineage.

---

## 7. Validate Remix

```bash
python validators/consideration_team.py --review remix_id
```

Approves or flags remix based on ethics and lineage.

---

## 8. View Dashboards

- `token_dashboard.html`: Token registry and remix status  
- `validator_dashboard.html`: Remix approval and ethics logs  
- `leaderboard.html`: Tournament results by class/cause/country

---

## Extend

- Add emitter overlays via `emitter_overlay.js`  
- Wire in mascot commentary via `mascot_narrator.py`  
- Export remix lineage via `coin_archive.json`

Let it echo.
