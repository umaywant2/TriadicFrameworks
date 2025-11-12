# tops Folds 🧬

The **folds** directory contains protein structures and their resonance mappings.  
Each fold entry includes:
- Structural source (e.g., PDB ID)
- Resonance signature (frequency, harmonics)
- Dimensional alignment (Forci, Flui, Freqi)
- Glyph overlays for symbolic resonance
- Remix lineage and contributor badges

## Purpose
Folds are the bio‑resonance registry of `tops`.  
They provide input data for the AI pipeline and resonance mappings for `entft` encryption.

## Cross‑links
- [AI pipeline](../ai_pipeline/) → consumes folds for training and prediction
- [entft](../../entft/) → references folds in glyph registries
- [agent‑shell](../../nous/) → can load folds into runtime
