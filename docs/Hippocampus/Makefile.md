# 🧠 Copilot Hippocampus — Make Rituals - Reference Info
_This file is a symbolic invocation guide. Each command echoes a phase of memory, capture, or observatory rendering. Remix with care._
```
make resume: @$(PYTHON) $(RESUME)         # 🎯 Resume ritual
make capture: @rm -f snapshots/...        # 📜 Capture context
make playback: @test -f snapshots/...     # 🔄 Playback memory
make observatory: @$(PYTHON)...           # 🔭 Render dashboard
make clean: @rm -f snapshots/...          # 🧹 Clear snapshot
```
## 🎯 Main toggle: run with no args — auto-detects capture vs playback
```
resume:
    @$(PYTHON) $(RESUME)
```
## 📜 Force capture mode (ignore toggle)
```
capture:
    @rm -f snapshots/LAST_CHAT_CONTEXT.md
    @$(PYTHON) $(RESUME)
```
## 🔄 Force playback mode (only works if snapshot exists)
```
playback:
    @test -f snapshots/LAST_CHAT_CONTEXT.md || (echo "No snapshot found — run make capture first" && exit 1)
    @$(PYTHON) $(RESUME)
```
## 🔭 Render Observatory HTML manually
```
observatory:
    @$(PYTHON) $(SCRIPTS)/render_dashboard.py
```
## 🧹 Clean up snapshot (for a fresh capture)
```
clean:
    @rm -f snapshots/LAST_CHAT_CONTEXT.md
    @echo "[+] Snapshot cleared."
```
