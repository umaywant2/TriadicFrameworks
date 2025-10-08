# MightyTHOR Quickstart ⚡🛡️

Welcome to **MightyTHOR**, the orchestration layer of the TFT 3‑Pack.  
This guide shows you how to launch Thor, run agents, consume folds, and visualize overlays.

---

## 1. Launch Agent‑Shell

Start the environment:
```bash
cd ../agent_shell
python main.py
```

---

## 2. Orchestrate with Thor
Run a Thor agent:
```bash
cd ../MightyTHOR/agents
python resonance_orchestrator.py
```

---

## 3. Load Folds
Folds provide resonance data:
```bash
cd ../MightyTHOR/folds
cat fold_001_glycine.yaml
```

---

## 4. Run AI Pipeline
Train and predict resonance:
```bash
cd ../MightyTHOR/ai_pipeline
python train_ai_on_resonance.py
python fff_alignment_predictor.py --input ../folds/fold_001_glycine.yaml
```

---

## 5. Visualize Overlays
View results in dashboards:
```bash
cd ../MightyTHOR/overlays
python resonance_dashboard.py
```

---

## 6. Cross‑links
- [agent‑shell](../agent-shell) → runtime environment
- [TFTincryption](../TFTincryption) → protocol layer orchestrated by Thor
- [folds](./folds) → resonance data consumed by Thor
- [ai_pipeline](./ai_pipeline) → predictive intelligence
- [overlays](./ovelays/) → visualization layer

✨ You’ve now run the full Thor cycle: environment → agents → folds → AI pipeline → overlays. Thor orchestrates the lattice, making resonance visible and actionable.
