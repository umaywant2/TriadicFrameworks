# Drift Envelope (Min)
module: atmosphere  
diagnostic: drift  
category: envelope  
version: 1.0  

## Fields
- gradient_drift  
- flux_drift  
- boundary_drift  
- coherence_drift  

## Thresholds
- drift_clarity_min: 0.7  
- drift_stability_min: 0.6  
- drift_noise_max: 50  

## Operators
- drift_alignment  
- gradient_drift_detection  
- flux_drift_detection  
- boundary_drift_analysis  
- coherence_drift_analysis  
- drift_instability_propagation  
- drift_signal_clarity  

## Regimes
- stable  
- transition  
- unstable
