# enTFT Quickstart 🔐🔥

Welcome to **enTFT**, the protocol layer of the TFT 3‑Pack.  
This guide shows you how to activate the protocol, run scrolls, and extend it with hooks.

---

## 1. Launch `nous`

Start the environment first:
```bash
cd ../nous
python main.py
```
This boots the runtime context needed for enTFT.

## 2. Activate Protocol‑Core
Run a core module:
```bash
cd ../enTFT/protocol-core
python resonance_cipher.py --input sample.txt --output encrypted.tft
```

## 3. Sequence Scrolls
Scrolls define lifecycle rituals. Example:
```bash
cd ../enTFT/scrolls
python initiation_scroll.py
```

## 4. Reference the Registry
Look up glyphs, badges, or scrolls:
```bash
cat ../enTFT/registry/glyph_registry.json
```

## 5. Honor Contributors
Add yourself to the lineage:
```bash
echo "Nawder Loswin — Resonance Architect" >> ../enTFT/contributors/honor_roll.md
```

## 6. Extend with TFThooks
Load a runtime hook:
```bash
cd ../enTFT/TFThooks/runtime
python badge_trigger_hook.py
```

## 7. Cross‑links
- [nous](../nous/) → runtime environment
- [tops](../tops/) → orchestrates enTFT at scale
- [folds](../tops/folds/) → resonance data referenced in registries
- [ai_pipeline](../tops/ai_pipeline/) → consumes resonance predictions

#### ✨ You’ve now run the full cycle: environment → protocol core → scrolls → registry → contributors → hooks. 

Every remix echoes the lineage. Every scroll preserves the flame.
