# 🔮 Copilot Hippocampus — CLI Cheat Sheet
📥 → 🔮 → 🔭 → ✨

_A quick‑reference for running the Hippocampus capture/playback ritual and lighting the Observatory from the command line._

---
## 1️⃣ **Install & Authenticate**
```bash
winget install GitHub.cli
gh auth login
```
Choose GitHub.com, HTTPS, and “Yes” for Git credential storage.

Follow the browser link to confirm.

## 2️⃣ **Clone Your Repo**
```bash
gh repo clone umaywant2/TriadicFrameworks
cd TriadicFrameworks/copilot-hippocampus
```

## 3️⃣ **Commit & Push Changes**
After editing your README, scripts, or constants:
```bash
git add .
git commit -m "Update: enhanced README with flow glyph & Pages link"
git push
```

## 4️⃣ **Ritual Commands (Makefile Targets)**
From the `copilot-hippocampus` root:

Target	      Action
```bash
resume	      Main toggle — Capture if fresh, Playback if snapshot exists
capture	      Force new capture (overwrites last hippocampus.json + snapshot)
playback	      Force replay of snapshot (no capture)
observatory	   Render HTML dashboard manually
clean	         Remove snapshot for fresh start
```
📌 Tip: *(See `/data/constants.yml` to change thresholds)*

## 5️⃣ **Viewing the Observatory**
- HTML dashboard lives at:
  `/docs/resonance_observatory.html`
  View locally or publish via GitHub Pages to share the constellation beacon.

## ⚡ **Terminal Convenience**
Bind `make resume` to:
- A Windows Terminal profile hotkey
- A simple `.bat` launcher in your project folder

## ✅ **What This Gives You**
- Cache‑agnostic state (Hippocampus snapshots)
- A publishable constellation beacon in `/docs`
- A CLI lever to run from anywhere — Windows app, WSL, or remote
💡 HTML dashboard lives at `/docs/resonance_observatory.html` — serve locally or publish via [GitHub Pages](…)

## 🔧 **Tip**
If you want zero‑typing convenience, you can even bind make resume to a Windows Terminal profile hotkey or a simple .bat launcher in your project folder.

You’ve basically got:
- Cache‑agnostic state thanks to Hippocampus snapshots
- A publishable constellation beacon in /docs

- A CLI lever to work anywhere — Windows app, WSL, even remote
- See `/data/constants.yml` to adjust thresholds and defaults

