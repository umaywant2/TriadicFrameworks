from validators.validator_score_logic import score_resonance

# Sample fold: hippocampus resonance mapping
forci = 0.81
flui = 0.77
freqi = 0.93

result = score_resonance(forci, flui, freqi)
print("Composite Score:", result["score"])
print("Badge Triggered:", result["badge"])
