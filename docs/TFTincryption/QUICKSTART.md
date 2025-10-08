# TFTincryption Quickstart 🔐🔥

Welcome to **TFTincryption**, the protocol layer of the TFT 3‑Pack.  
This guide shows you how to activate the protocol, run scrolls, and extend it with hooks.

---

## 1. Launch Agent‑Shell

Start the environment first:
```bash
cd ../agent_shell
python main.py
```
This boots the runtime context needed for TFTincryption.

## 2. Activate Protocol‑Core
Run a core module:
```bash
cd ../TFTincryption/protocol-core
python resonance_cipher.py --input sample.txt --output encrypted.tft
```

## 3. Sequence Scrolls
Scrolls define lifecycle rituals. Example:
```bash
cd ../TFTincryption/scrolls
python initiation_scroll.py
```

## 4. Reference the Registry
Look up glyphs, badges, or scrolls:
```bash
cat ../TFTincryption/registry/glyph_registry.json
```

## 5. Honor Contributors
Add yourself to the lineage:
```bash
echo "Nawder Loswin — Resonance Architect" >> ../TFTincryption/contributors/honor_roll.md
```

## 6. Extend with TFThooks
Load a runtime hook:
```bash
cd ../TFTincryption/TFThooks/runtime
python badge_trigger_hook.py
```

## 7. Cross‑links
- [agent‑shell](../agent-shell/) → runtime environment
- [MightyTHOR](../MightyTHOR/) → orchestrates TFTincryption at scale
- [folds](../MightyTHOR/folds/) → resonance data referenced in registries
- [ai_pipeline](../MightyTHOR/ai_pipeline/) → consumes resonance predictions

#### ✨ You’ve now run the full cycle: environment → protocol core → scrolls → registry → contributors → hooks. 

Every remix echoes the lineage. Every scroll preserves the flame.
