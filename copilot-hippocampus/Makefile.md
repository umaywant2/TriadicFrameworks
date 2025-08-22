# Copilot Hippocampus — Make Rituals

PYTHON := python3
SCRIPTS := scripts
RESUME := $(SCRIPTS)/RESUME_Copilot.py

.PHONY: resume playback capture observatory clean

## 🔄 Main toggle: run with no args — auto-detects capture vs playback
```
resume:
    @$(PYTHON) $(RESUME)
```
## 🎯 Force capture mode (ignore toggle)
```
capture:
    @rm -f snapshots/LAST_CHAT_CONTEXT.md
    @$(PYTHON) $(RESUME)
```
## 📜 Force playback mode (only works if snapshot exists)
```
playback:
    @test -f snapshots/LAST_CHAT_CONTEXT.md || (echo "No snapshot found — run make capture first" && exit 1)
    @$(PYTHON) $(RESUME)
```
# 🔭 Render Observatory HTML manually
```
observatory:
    @$(PYTHON) $(SCRIPTS)/render_dashboard.py
```
# 🧹 Clean up snapshot (for a fresh capture)
```
clean:
    @rm -f snapshots/LAST_CHAT_CONTEXT.md
    @echo "[+] Snapshot cleared."
```
