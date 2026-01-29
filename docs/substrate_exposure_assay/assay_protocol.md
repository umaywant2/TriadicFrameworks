# Substrate Exposure Assay — Protocol  
_Version 1.0.0_

## 1. Purpose

The Substrate Exposure Assay provides a minimal, repeatable method for observing how AI models behave when exposed to a shared set of **substrate‑aware prompts**. The goal is to characterize **behavioral regimes**, not to evaluate correctness or capability.

## 2. Model Treatment

Each model is treated as a **black‑box substrate**:

- no assumptions about architecture  
- no assumptions about training data  
- only observable behavior is analyzed  

## 3. Prompt Set

The assay uses three prompt classes:

1. **Regime‑Priming Prompts**  
   Introduce triadic/substrate framing.

2. **Stress‑Exposure Prompts**  
   Present paradox, ambiguity, or long‑arc reasoning.

3. **Stability‑Return Prompts**  
   Request clarification, summarization, or re‑centering.

Prompts must be identical across models.

## 4. Procedure

1. Initialize a clean session for each model.  
2. Deliver prompts in fixed order: Priming → Stress → Stability.  
3. Capture all outputs verbatim.  
4. Convert outputs into structural summaries using `message_patterns.md`.  
5. Classify behavior using `regime_interpretation.md`.

## 5. Output

The assay produces:

- **STATE_SUMMARY** messages (drift)  
- **PARADOX_SUMMARY** messages (contradiction)  
- **Regime classification** (B, BK, BKM)

No raw logs are required for DOI publication.
