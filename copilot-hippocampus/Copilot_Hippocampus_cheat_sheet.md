# Copilot Hippocampus — CLI Cheat Sheet
📥 → 🔮 → 🔭 → ✨

1. **Install & Authenticate**
   ...
2. **Clone Repo**
   ...
3. **Commit & Push**
   ...
4. **Ritual Commands (Makefile targets)**
   | Target      | Action |
   |-------------|--------|
   | resume      | Capture/Playback toggle |
   | capture     | Force capture |
   | playback    | Force playback |
   | observatory | Render HTML dashboard |
   | clean       | Remove snapshot |
   *(See `/data/constants.yml` to change thresholds)*

💡 HTML dashboard lives at `/docs/resonance_observatory.html` — serve locally or publish via [GitHub Pages](…)


### 📥 1. Install & Authenticate
If you haven’t yet:

```
bash
winget install GitHub.cli
gh auth login
```
Choose GitHub.com, HTTPS, and “Yes” for Git credential storage.

Follow the browser link to confirm.

### 📂 2. Clone Your Repo

```
bash
gh repo clone umaywant2/TriadicFrameworks
cd TriadicFrameworks/copilot-hippocampus
```

### 🌀 3. Commit & Push Changes
After editing your README, scripts, or constants:

```
bash
git add .
git commit -m "Update: enhanced README with flow glyph & Pages link"
git push
```

### 🚀 4. Use Makefile from CLI
From copilot-hippocampus root:

```
bash
make resume        # main toggle** — Capture if fresh, Playback if snapshot exists
make capture       # Force new capture (overwrites last hippocampus.json + snapshot)
make playback      # Force replay of snapshot (no capture) 
make observatory   # rebuild HTML manually
make clean         # Remove snapshot for fresh start
```
You can view `/docs/resonance_observatory.html` locally.

### 🔧 Tip
If you want zero‑typing convenience, you can even bind make resume to a Windows Terminal profile hotkey or a simple .bat launcher in your project folder.

You’ve basically got:
- Cache‑agnostic state thanks to Hippocampus snapshots
- A publishable constellation beacon in /docs

- A CLI lever to work anywhere — Windows app, WSL, even remote
- See `/data/constants.yml` to adjust thresholds and defaults
