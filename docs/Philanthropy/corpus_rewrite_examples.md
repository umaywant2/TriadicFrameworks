# Corpus Rewrite Examples — Philanthropy & Funding Transparency Module

This file provides examples of how to rewrite narrative-heavy, ambiguous, or PR-shaped philanthropic text into clean, structural, RTT-aligned corpus entries.

Each example includes:
- Original text  
- Structural rewrite  
- Operators used  
- Explanation of structural improvements  

These examples teach students, auditors, donors, and AI agents how to convert narrative into signal.

---

# 1. Example A — “Impact Story” Rewrite

## Original (Narrative)
“Our foundation proudly supported over 200,000 lives last year through our inspiring education initiatives, empowering communities and transforming futures.”

## Structural Rewrite (RTT-Aligned)
```
FLOW(Foundation → NGO) = $4.2M
CONVERT($4.2M → $2.9M direct services)
SET_LEAK(Foundation) = 31%
SET_LEAK(NGO) = 18%
IMPACT: 12,480 students received instructional hours
REG(NAR) detected in reporting
DRF(reporting) = moderate
```

## Operators Used
SIG, NOI, FLOW, CONVERT, SET_LEAK, IMPACT, REG, DRF

## Why This Rewrite Works
- Removes narrative inflation  
- Replaces “lives touched” with measurable outputs  
- Identifies leakage and drift  
- Converts PR into structural signal  

---

# 2. Example B — “Program Success” Rewrite

## Original (Narrative)
“Our climate resilience program made tremendous strides, partnering with local heroes to build a brighter, greener tomorrow.”

## Structural Rewrite (RTT-Aligned)
```
FLOW(Donor → Intermediary) = $8M
FLOW(Intermediary → NGO) = $3.9M
SET_LEAK(Intermediary) = 51%
OUTPUT: 14 community workshops delivered
OUTCOME: 3 measurable resilience improvements
REG(NAR) at Intermediary
DRF(financial) = high
```

## Operators Used
FLOW, SET_LEAK, OUTPUT, OUTCOME, REG, DRF

## Why This Rewrite Works
- Removes emotional framing  
- Reveals leakage and drift  
- Converts “tremendous strides” into measurable outputs  
- Identifies regime distortion  

---

# 3. Example C — “Emergency Relief” Rewrite

## Original (Narrative)
“In the wake of the devastating floods, our rapid response team brought hope and healing to thousands.”

## Structural Rewrite (RTT-Aligned)
```
SET_IN(GlobalReliefFoundation) = $12M (surge)
FLOW(GRF → RegionalHub) = $9.6M
FLOW(RegionalHub → LocalNGO) = $6.2M
SET_LEAK(RegionalHub) = 35%
OUTPUT: 4,800 households received supplies
OUTCOME: 3,200 households stabilized within 30 days
REG(EMO) at Donor
DRF(governance) at GRF
```

## Operators Used
SET_IN, FLOW, SET_LEAK, OUTPUT, OUTCOME, REG, DRF

## Why This Rewrite Works
- Removes emotional language  
- Reveals bottlenecks and leakage  
- Shows measurable outcomes  
- Identifies regime drivers  

---

# 4. Example D — “Innovation Pilot” Rewrite

## Original (Narrative)
“Our groundbreaking mobile clinic initiative revolutionized access to healthcare in underserved regions.”

## Structural Rewrite (RTT-Aligned)
```
FLOW(Donor → Foundation) = $2M
FLOW(Foundation → NGO) = $1.9M
SET_LEAK(Foundation) = 5%
OUTPUT: 6 mobile clinics deployed
OUTCOME: 18,400 patient visits
SET_BAL(NGO) = 0.92
REG(STR) across all nodes
DRF = none
```

## Operators Used
FLOW, SET_LEAK, OUTPUT, OUTCOME, SET_BAL, REG

## Why This Rewrite Works
- Removes hype language  
- Shows real outputs and outcomes  
- Identifies strong structural alignment  
- Confirms absence of drift  

---

# 5. Example E — “Community-Led Success” Rewrite

## Original (Narrative)
“By working hand-in-hand with local champions, we empowered communities to take control of their own housing future.”

## Structural Rewrite (RTT-Aligned)
```
FLOW(Donor → CommunityFoundation) = $3M
FLOW(CF → Council) = $2.85M
FLOW(Council → Committees) = $2.7M
SET_LEAK(CF) = 5%
SET_LEAK(Council) = 5%
OUTPUT: 112 housing units repaired
OUTCOME: 87 households stabilized
REG(STR) across all nodes
DRF = none
```

## Operators Used
FLOW, SET_LEAK, OUTPUT, OUTCOME, REG

## Why This Rewrite Works
- Removes vague empowerment language  
- Shows measurable results  
- Highlights strong governance substrate  
- Confirms structural coherence  

---

# Summary

These corpus rewrite examples demonstrate how to convert narrative-heavy philanthropic text into:

- measurable flows  
- structural outcomes  
- regime analysis  
- drift detection  
- SET load mapping  
- alignment scoring  

This file teaches the core skill of **turning narrative into signal**, enabling clarity, accountability, and structural integrity across the philanthropic ecosystem.
