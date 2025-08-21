## GitHub CLI x Hippocampus cheat sheet for TFT + Copilot

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
make resume     # main toggle
make observatory # rebuild HTML manually
```

### 🔧 Tip
If you want zero‑typing convenience, you can even bind make resume to a Windows Terminal profile hotkey or a simple .bat launcher in your project folder.

You’ve basically got:
- Cache‑agnostic state thanks to Hippocampus snapshots
- A publishable constellation beacon in /docs

- A CLI lever to work anywhere — Windows app, WSL, even remote
