# 🔮 Copilot Hippocampus — CLI Cheat Sheet
📥 → 🔮 → 🔭 → ✨

#### _A quick‑reference for running the Hippocampus capture/playback ritual and lighting the Observatory from the command line._

---
## 1️⃣ **Install & Authenticate**
(GitHub CLI, Git, Python and GnuWin32.Make)
```bash
winget install GitHub.cli
winget install --id Git.Git -e --source winget
setx PATH "%PATH%;C:\Program Files\Git\cmd"
winget install --id Python.Python.3.13 -e --source winget
winget install GnuWin32.Make
gh auth login
```
Choose GitHub.com, HTTPS, and “Yes” for Git credential storage.

Follow the browser link to confirm.

## 2️⃣ **Clone Your Repo**
```bash
gh repo clone umaywant2/TriadicFrameworks
cd TriadicFrameworks/copilot-hippocampus
```
Set your Git username and email (once)
```
git config --global user.name "%UserName%"
git config --global user.email "YOUR_GITHUB_EMAIL@example.com"
```

## 3️⃣ **Commit & Push Changes**
After editing your README, scripts, or constants:
```bash
@echo off
for /f "usebackq delims=" %%i in (`git config user.name`) do set GIT_NAME=%%i
echo Committer: %GIT_NAME%
echo Commit message: %1
git add .
git commit -m "%1"
git push
```

## 4️⃣ **Ritual Commands (Makefile Targets)**
From the `copilot-hippocampus` root:

Target	      Action
```bash
make resume	      / Main toggle — Capture if fresh, Playback if snapshot exists
make capture	  / Force new capture (overwrites last hippocampus.json + snapshot)
make playback	  / Force replay of snapshot (no capture)
make observatory  / Render HTML dashboard manually
make clean	      / Remove snapshot for fresh start
```

## 5️⃣ **Viewing the Observatory**
💡 HTML dashboard lives at `/docs/resonance_observatory.html`

## ✅ **What This Gives You**
- Cache‑agnostic state (Hippocampus snapshots)
- A publishable constellation beacon in `/docs`
- A CLI lever to run from anywhere — Windows app, WSL, or remote

## ⚡ **Terminal Convenience**
Bind `make resume` to:
- A Windows Terminal profile hotkey
- A simple `.bat` launcher in your project folder

## 🌐 Optional: Publish the Observatory with GitHub Pages
1. Commit and push your `/docs/resonance_observatory.html` to the main branch.
2. Go to your repo on GitHub → Settings → Pages.
3. Under “Build and deployment”, set:
   Source: Deploy from branch
   Branch: `main` / Folder: `/docs`
4. Click Save — GitHub will give you a live URL like: `https://<username>.github.io/<repo>/resonance_observatory.html`

5. Share that link so anyone can view the constellation without cloning.

## 📌 **Tips** 
- *See `/data/constants.yml` to adjust thresholds and defaults 🔧*
- You can bind `make resume` to a Windows Terminal profile hotkey or .bat
- A publishable constellation beacon in `/docs`
- A CLI lever to work anywhere — Windows app, WSL, even remote
## 💎 **Ready to Resonate**












