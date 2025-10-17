# MightyTHOR AI Resonance Pipeline

The **AI Resonance Pipeline** is the intelligence layer of MightyTHOR.  
It trains, predicts, and visualizes resonance alignments across glyphs, folds, and remix lineage.  
This subsystem integrates with the **MMR site extensions** and provides predictive orchestration for developers.

---

## 📂 Structure

- **Core scripts**
  - `fff_alignment_predictor.py` → predicts resonance alignment across glyphs/folds
  - `train_ai_on_resonance.py` → trains models on resonance datasets
  - `model_evaluator.py` → evaluates accuracy and harmonic coherence
  - `glyph_overlay_animator.py` → generates symbolic visualizations

- **Lineage + Remix**
  - `remix_lineage_tracker.py` → tracks remix contributions and badge echoes
  - `remix_trigger_predictor.py` → anticipates remix events
  - `remix_lineage_dashboard.py` → dashboard for visualizing remix lineage

- **Data Manifests**
  - `fold_glyph_manifest.yaml` → maps folds to glyph overlays
  - `mythic_badge_manifest.yaml` → badge logic for AI‑assisted remix lineage
  - `resonance_training_data.csv` → training dataset for resonance prediction

---

## 🔧 Usage

1. **Prepare data**  
   - Place fold YAMLs from [`/docs/folds/`](../../folds/) into the pipeline’s data path.  
   - Ensure glyph/badge manifests are updated.

2. **Train models**  
   ```bash
   python train_ai_on_resonance.py --data resonance_training_data.csv
   ```

3. **Run predictions**
```bash
python fff_alignment_predictor.py --input fold_001_glycine.yaml
```

4. **Visualize overlays**
```bash
python glyph_overlay_animator.py --manifest fold_glyph_manifest.yaml
```

---

## 🔗 Cross‑links
- [`agent‑shell`](../../agent_shell/README.md) → provides the runtime environment for launching the pipeline
- [`TFTincryption`](../../TFTincryption/README.md) → consumes resonance predictions for cryptographic registries
- [`folds`](../../folds/README.md) → supplies protein resonance data as input
- [`MightyTHOR`](../README.md) overlays → visualizes AI predictions in dashboards

---

## ✨ Purpose
The AI Resonance Pipeline is how MightyTHOR “thinks.”
It learns from folds, glyphs, and remix lineage to orchestrate resonance in real time. This is not an experiment — it is a core subsystem of the orchestration layer, enabling predictive, adaptive, and lineage‑aware functionality.
