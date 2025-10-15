# Resonance Tools

The **resonance‑tools** are utilities bundled with agent‑shell.  
They provide analysis, mapping, and helper scripts for resonance workflows.

## Structure
- `resonance_analyzer.py` → analyze resonance signatures
- `harmonic_mapper.py` → map harmonic alignments
- `glyph_resonance_calculator.py` → calculate glyph resonance values
- Other utilities for runtime support

## Purpose
These tools extend the agent‑shell environment with resonance analysis capabilities.  
They are not protocols themselves, but support the execution of enTFT and tops.

## Cross‑links
- [folds](../../tops/folds/) → input data for analysis
- [ai_pipeline](../../tops/ai_pipeline/) → consumes outputs for training
- [enTFT](../../enTFT/) → uses resonance values in registries
