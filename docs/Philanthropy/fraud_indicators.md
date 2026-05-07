# Structural Fraud & Misuse Indicators — Philanthropy & Funding Transparency Module

This file defines RTT-aligned structural indicators of fraud, misuse, leakage, and misalignment in philanthropic funding flows.  
These indicators are **structural**, not moral or legal judgments.  
They identify patterns that correlate with drift, opacity, and value extraction.

The goal: **detect structural red flags early, before harm occurs.**

---

# 1. Purpose of Structural Fraud Indicators

Philanthropy is vulnerable to misuse because it operates with:

- private authority  
- public purpose  
- weak oversight  
- multi-layer flows  
- narrative-heavy reporting  
- complex legal structures  

Structural fraud indicators help:

- donors  
- fund managers  
- auditors  
- journalists  
- regulators  
- AI agents  

…identify misalignment and opacity **without requiring intent**.

These indicators are **pattern-based**, not accusatory.

---

# 2. Red Indicator Categories

RTT identifies six major categories of structural red indicators:

1. **Flow Breaks**  
2. **Opacity Structures**  
3. **Governance Asymmetry**  
4. **Financial Distortion**  
5. **Narrative Inflation**  
6. **Incentive Misalignment**

Each category is mapped using RTT operators.

---

# 3. Flow Break Indicators (RED(flow-break))

Flow breaks occur when money cannot be traced from source to outcome.

Examples:

- Missing or incomplete flow documentation  
- Funds routed through unreported intermediaries  
- Sudden changes in routing paths  
- Unexplained delays in disbursement  
- Funds held indefinitely in DAFs or endowments  

Operators:
```
FLOW(src → dst)
TRACE(path)
LEAK(node)
RED(flow-break)
```

Structural effect: **loss of visibility**.

---

# 4. Opacity Indicators (RED(opacity))

Opacity structures obscure financial, governance, or operational visibility.

Examples:

- Donor-advised funds with no payout  
- Fiscal sponsors with limited reporting  
- Related-party consultancies  
- Shell intermediaries  
- Complex legal vehicles  
- Narrative-heavy, data-light reports  

Operators:
```
VIS(node)
OPA(node)
RED(opacity)
```

Structural effect: **information asymmetry**.

---

# 5. Governance Asymmetry Indicators (RED(asymmetry))

Governance asymmetry occurs when authority exceeds accountability.

Examples:

- Boards accountable only to themselves  
- Donors influencing programs without oversight  
- Executives with unchecked discretion  
- Intermediaries controlling flows without transparency  
- Beneficiaries excluded from governance  

Operators:
```
GOV(node)
ACC(node)
ASYM(node)
RED(asymmetry)
```

Structural effect: **power imbalance**.

---

# 6. Financial Distortion Indicators (RED(financial))

Financial distortion occurs when funds are diverted, diluted, or misallocated.

Examples:

- Overhead exceeding 40–60%  
- Excessive fundraising costs  
- High executive compensation relative to budget  
- Large reserves with low payout  
- Funds used for unrelated activities  
- Repeated budget variances without explanation  

Operators:
```
LOAD(node)
LEAK(node)
CONVERT(input → output)
SET_LEAK(node)
RED(financial)
```

Structural effect: **resource misalignment**.

---

# 7. Narrative Inflation Indicators (RED(narrative))

Narrative inflation occurs when stories replace structural evidence.

Examples:

- Reports dominated by testimonials  
- “Impact” defined as activities, not outcomes  
- Emotional appeals without data  
- Photos replacing metrics  
- Claims unsupported by flow maps  

Operators:
```
SIG(data)
NOI(data)
REG(NAR)
RED(narrative)
```

Structural effect: **signal-to-noise collapse**.

---

# 8. Incentive Misalignment Indicators (RED(incentive))

Misalignment occurs when incentives reward behavior that contradicts mission.

Examples:

- Fundraising firms paid by percentage of donations  
- Intermediaries rewarded for overhead growth  
- Foundations incentivized to preserve endowments  
- NGOs incentivized to maximize reporting, not outcomes  
- Donors incentivized by tax benefits, not impact  

Operators:
```
SET_IN(node)
SET_OUT(node)
SET_LEAK(node)
REG(EMO)
RED(incentive)
```

Structural effect: **drift becomes predictable**.

---

# 9. Composite Red Indicator Score

Each node receives a composite score:

```
RedScore(node) =
  w1 * RED(flow-break)
+ w2 * RED(opacity)
+ w3 * RED(asymmetry)
+ w4 * RED(financial)
+ w5 * RED(narrative)
+ w6 * RED(incentive)
```

Where weights (w1–w6) are tuned by the AI Process Manager Agent.

Example:
```
RedScore(IntermediaryX) = 0.78 (high risk)
```

---

# 10. AI Process Manager Agent (PMA) Role

The PMA uses fraud indicators to:

- detect early warning signs  
- generate structural alerts  
- recommend corrective actions  
- produce donor-facing clarity reports  
- maintain system-wide integrity  

Operators used:
```
SIG, NOI, CTX, SYN
FLOW, TRACE, LEAK
GOV, ACC, VIS
DRF, ALN, COH
RED, OPA, ASYM
```

---

# 11. Summary

Structural fraud indicators reveal:

- where flows break  
- where opacity grows  
- where authority exceeds accountability  
- where financial distortion occurs  
- where narrative replaces structure  
- where incentives drift  

These indicators allow philanthropy to operate with **clarity**, **alignment**, and **structural integrity**, supported by AI-managed oversight.
