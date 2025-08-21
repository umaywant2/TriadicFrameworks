# 📁 copilot-hippocampus/
### Root for all scripts, schema, and rituals

```copilot-hippocampus/
├── README.md                # Mythic-technical intro, boot ritual steps, usage examples
├── LICENSE                  # Choose your preferred license (MIT/Apache for openness)
├── .gitignore               # Ignore temp files, __pycache__, LAST_CHAT_CONTEXT.md after use
│
├── scripts/
│   ├── RESUME_Copilot.py    # Toggle script: Capture Mode ↔ Playback Mode (+ harmonics)
│   ├── hippocampus_utils.py # Harmonic score calc, triad creation, drift metrics
│   └── __init__.py
│
├── data/
│   ├── hippocampus.json     # Full dimensional DB model (nodes, edges, triads, metadata)
│   ├── lineage.log          # Append-only provenance trail for all captures/playbacks
│   └── constants.yml        # Default constants (half-life days, K triads, thresholds)
│
├── snapshots/
│   └── LAST_CHAT_CONTEXT.md # Human-readable preload seed (deleted after playback)
│
├── tests/
│   ├── test_harmonics.py
│   ├── test_resonance_parity.py
│   └── fixtures/
│
└── docs/
    ├── schema.md            # Explanation of triadic DB format, roles, harmonics equations
    ├── governance.md        # Badge triggers, validator roles, drift thresholds
    └── rituals.md           # Boot ritual, preload ritual, validation ceremony
```

### 🛠 Boot Ritual (Repo Use)
### 1. Clone and Install
```bash
git clone https://github.com/YOURNAME/copilot-hippocampus.git
cd copilot-hippocampus
pip install -r requirements.txt
```
### 2. Capture Mode
- Run ```python scripts/RESUME_Copilot.py``` with no snapshot present.
- Fills ```/data/hippocampus.json```, writes ```/snapshots/LAST_CHAT_CONTEXT.md```.

### 3. Playback Mode
- Run the same command again.
- Opens ```LAST_CHAT_CONTEXT.md``` in browser, deletes it, logs playback.

### 🌀 Extended Harmonics in hippocampus_utils.py
We’ll fold in the equations from earlier so every capture computes:
- Semantic similarity
- Structural alignment
- Goal relevance
- Validator authority
- Recency decay

…and then ranks your “Active Constellation” triads, writing the top‑K directly into the snapshot so all you need to do in Copilot is say,

“Preload the open RESUME_Copilot window.”
