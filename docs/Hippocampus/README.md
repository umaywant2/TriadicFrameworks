# 🔮 Copilot Hippocampus
**TriadicFrameworks Conversational Memory Engine & Resonance Observatory**  
_“The mind that remembers in triads sees constellations where others see stars.”_

---

## 📂 Repo Structure

```### copilot-hippocampus/
├── README.md                     # This guide 
├── LICENSE                       # MIT/Apache recommended 
├── .gitignore                    # Ignore temp files, pycache, snapshots 
│ 
├── Makefile                      # Ritual commands (see below) 
│ 
├── scripts/ 
│ ├── RESUME_Copilot.py           # Capture ↔ Playback toggle + harmonics + auto‑lighthouse 
│ ├── hippocampus_utils.py        # Harmonics calc, triad assembly, metrics 
│ ├── render_dashboard.py         # Resonance Observatory (CLI + HTML) 
│ └── init.py 
│ 
├── data/ 
│ ├── hippocampus.json            # Full triadic DB model 
│ ├── lineage.log                 # Append‑only capture/playback history 
│ └── constants.yml               # Half‑life, top‑K, drift thresholds, parity target 
│ 
├── snapshots/ 
│ └── LAST_CHAT_CONTEXT.md        # Human‑readable preload seed (deleted after playback) 
│
├── tests/ 
│ ├── test_harmonics.py 
│ ├── test_resonance_parity.py 
│ └── fixtures/ 
│ 
└── docs/ 
├── schema.md                     # DB format & roles 
├── governance.md                 # Badge triggers, validator roles, thresholds 
├── rituals.md                    # Boot/preload/validation ceremonies 
└── resonance_observatory.html    # Auto‑published HTML dashboard
```


---

## ⚙️ Quick‑Start Rituals

All commands run from the repo root.

| Command              | Action                                                                   |
|----------------------|--------------------------------------------------------------------------|
| `make resume`        | **Main toggle** — Capture if fresh, Playback if snapshot exists          |
| `make capture`       | Force new capture (overwrites last hippocampus.json + snapshot)          |
| `make playback`      | Force replay of snapshot (no capture)                                    |
| `make observatory`   | Manually rebuild `/docs/resonance_observatory.html`                      |
| `make clean`         | Remove snapshot for fresh start                                          |
---

## 🌀 Boot & Preload Sequence
```
📥 Capture                                   ↓  (anchor + goals, triads, parity, badges)
🔮 LAST_CHAT_CONTEXT.md + hippocampus.json   ↓  (auto)
🔭 resonance_observatory.html                ↓  (session resume)
✨ Copilot preload & continue work
```
📥 Capture → 🔮 `LAST_CHAT_CONTEXT.md` + `hippocampus.json` → 🔭 `resonance_observatory.html` → ✨ Copilot preload & continue work  
- *(HTML can be published via [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages) for public constellation viewing)*


1. **Capture Mode**  
   - `make capture` or `make resume` (if no snapshot exists)  
   - Prompts for anchor + goals, builds **Active Constellation** triads with harmonic scores  
   - Writes `/data/hippocampus.json` (machine) + `/snapshots/LAST_CHAT_CONTEXT.md` (human/Copilot seed)  
   - Updates `/data/lineage.log` provenance trail  
   - **Auto‑publishes** `/docs/resonance_observatory.html`

2. **Playback Mode**  
   - `make playback` or `make resume` (if snapshot exists)  
   - Opens snapshot in browser, deletes it (reset to Capture mode next run)  
   - Tell Copilot:
     ## _“Preload the open RESUME_Copilot window”_
      to restore session context.

---

## 🔭 Observatory Lighthouse

Every capture regenerates an HTML dashboard in `/docs/resonance_observatory.html` containing:
- **Active Constellation** triads table (IDs, H‑scores, tags, last touch)
- **Resonance parity** vs. target  
- **Drift score** vs. alert threshold  
- **Badges earned** with glyph sigils
- Provenance timestamp

Publish this file with **GitHub Pages** or open locally to share constellation state.

---

## 🎖 Badge Governance

Badge triggers are defined in `/data/constants.yml` and `render_dashboard.py`:

| Badge                | Sigil | Condition |
|----------------------|-------|-----------|
| ResonanceWizard      | 🔮    | Parity ≥ target threshold |
| LineageKeeper        | 📜    | ≥ 5 captures in lineage |
| StabilitySigil       | 🛡️    | Drift below alert threshold |
| ConstellationMaster  | ✨    | Parity ≥ 0.85 **and** ≥ 10 captures |

---

## 🧮 Constants & Config

Edit `/data/constants.yml` to adjust:
```yaml
half_life_days: 21
top_k: 7
drift_alert_threshold: 0.15
resonance_parity_target: 0.75
```

## 📜 Schema Overview
See `/docs/schema.md` for full DB grammar:
- Node: Concept, task, artifact, person, ritual
- Edge: Relationship with weight
- Triad: Three nodes + roles + harmonics + decay + provenance
- Snapshot: Anchor goal + asks + constants + triads
- Validator Record: Who validated what with scores & badges

## 🪢 Ritual Notes
- Lineage Log: Append‑only; each capture/playback logged with UTC timestamp
- Snapshot Ephemerality: `LAST_CHAT_CONTEXT.md` deleted after playback to prevent stale preloads
- Reproducibility: Constants + schema version locked per snapshot
- Privacy: Redact sensitive data before capture if needed

## 🌌 Example Copilot Preload
When resuming a session:
#### 1. Run `make playback` (opens `LAST_CHAT_CONTEXT.md`)
#### 2. In Copilot:
   ```Preload the open RESUME_Copilot window and continue with TFT Project 1 resonance tier mapping```

## 🧠 Hippocampus Resume Honor Roll

- **Nawder Loswin**  
  Architected reproducible memory resumption and observatory rendering logic in `RESUME_Copilot.py`.  
  _Badge: `resume-toggle-validator`_

### 🔮 "Lantern lit, constellations charted. Welcome to the Guild of Conversational Continuity."
