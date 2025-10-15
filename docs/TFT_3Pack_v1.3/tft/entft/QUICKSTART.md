# enTFT Quickstart 🔐🔥

Welcome to **enTFT**, the protocol layer of the TFT 3‑Pack.  
This guide shows you how to activate the protocol, and extend it with hooks.

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

## 3. Cross‑links
- [nous](../nous/) → runtime environment
- [tops](../tops/) → orchestrates enTFT at scale
- [folds](../tops/folds/) → resonance data referenced in registries
- [ai_pipeline](../tops/ai_pipeline/) → consumes resonance predictions

#### ✨ You’ve now run the full cycle: environment → protocol core → hooks. 

Every remix echoes the lineage.
