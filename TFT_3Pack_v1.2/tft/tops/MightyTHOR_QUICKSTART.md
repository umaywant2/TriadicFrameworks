# tops Quickstart ⚡🛡️

Welcome to **tops**, the orchestration layer of the TFT 3‑Pack.  
This guide shows you how to launch tops, run agents, consume folds, and visualize overlays.

---

## 1. Launch `nous`

Start the environment:
```bash
cd ../nous
python main.py
```

---

## 2. Orchestrate with tops
Run a tops agent:
```bash
cd ../tops/agents
python resonance_orchestrator.py
```

---

## 3. Load Folds
Folds provide resonance data:
```bash
cd ../tops/folds
cat fold_001_glycine.yaml
```

---

## 4. Run AI Pipeline
Train and predict resonance:
```bash
cd ../tops/ai_pipeline
python train_ai_on_resonance.py
python fff_alignment_predictor.py --input ../folds/fold_001_glycine.yaml
```

---

## 5. Visualize Overlays
View results in dashboards:
```bash
cd ../tops/overlays
python resonance_dashboard.py
```

---

## 6. Cross‑links
- [nous](../nous) → runtime environment
- [enTFT](../enTFT) → protocol layer orchestrated by Thor
- [folds](./folds) → resonance data consumed by Thor
- [ai_pipeline](./ai_pipeline) → predictive intelligence
- [overlays](./ovelays/) → visualization layer

✨ You’ve now run the full tops cycle: environment → agents → folds → AI pipeline → overlays. Thor orchestrates the lattice, making resonance visible and actionable.
