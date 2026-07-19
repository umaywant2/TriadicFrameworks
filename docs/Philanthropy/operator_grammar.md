# Operator Grammar — Philanthropy & Funding Transparency Module

This file defines the RTT operator grammar used to analyze, map, and correct philanthropic funding flows.  
These operators allow donors, organizations, auditors, and AI agents to speak a shared structural language.

---

# 1. Core Operators (Funding Flow)

## **FLOW(src → dst)**  
Maps the movement of funds from one node to another.  
Used for: donor → foundation → intermediary → NGO → beneficiary.

**Example:**  
FLOW(DonorA → FoundationB)

---

## **LOAD(node)**  
Measures the structural load placed on a node (financial, administrative, governance).

**Example:**  
LOAD(LocalPartnerX)

---

## **LEAK(node)**  
Identifies points where funds are lost, diluted, or diverted.

**Example:**  
LEAK(IntermediaryY)

---

## **CONVERT(input → output)**  
Maps how funds are transformed (e.g., money → overhead, money → services).

**Example:**  
CONVERT($1M → $600k programs)

---

## **ROUTE(path)**  
Describes the full multi-layer path of funds.

**Example:**  
ROUTE(Donor → Foundation → NGO → Subcontractor → Community)

---

# 2. Regime Operators (Authority, Narrative, Emotional, Structural)

## **REG(type)**  
Tags the dominant regime influencing a decision or flow.

Types:  
- AUTH (authority)  
- NAR (narrative)  
- EMO (emotional)  
- STR (structural)

**Example:**  
REG(NAR) — impact story driving funding

---

## **DRF(type)**  
Detects drift between stated purpose and actual behavior.

Types:  
- mission  
- financial  
- governance  
- reporting  

**Example:**  
DRF(financial)

---

## **ALN(target)**  
Measures alignment between intent, flow, and outcome.

**Example:**  
ALN(ProgramGoal)

---

## **COH(system)**  
Evaluates coherence across nodes (donor, org, community).

**Example:**  
COH(FundingChain)

---

# 3. Governance Operators

## **GOV(node)**  
Maps governance authority and decision rights.

**Example:**  
GOV(Board)

---

## **SUB(node)**  
Maps the governance substrate supporting or constraining flows.

**Example:**  
SUB(FoundationStructure)

---

## **ACC(node)**  
Measures accountability strength.

**Example:**  
ACC(ExecutiveDirector)

---

## **VIS(node)**  
Measures structural visibility (not narrative visibility).

**Example:**  
VIS(ProgramBudget)

---

# 4. SET (Structural Energy Theory) Operators for Funding

## **SET_IN(node)**  
Energy (funding, incentives, mandates) entering a node.

---

## **SET_OUT(node)**  
Energy leaving a node (services, grants, outcomes).

---

## **SET_LEAK(node)**  
Energy lost to inefficiency, overhead, or misalignment.

---

## **SET_BAL(node)**  
Balance between input and output.

---

# 5. Triadic Observer Operators (Signal / Noise / Regime)

## **SIG(data)**  
Extracts structural signal from reports, budgets, or narratives.

---

## **NOI(data)**  
Identifies noise (PR, emotional appeals, branding).

---

## **CTX(data)**  
Binds context to a claim or flow.

---

## **SYN(data)**  
Produces a structural synthesis (AI summary).

---

# 6. Fraud & Misuse Operators (Structural, Not Accusatory)

## **RED(flag)**  
Flags structural red indicators (not moral judgments).

Examples:  
- RED(related-party)  
- RED(overhead > 50%)  
- RED(flow-break)  

---

## **OPA(node)**  
Measures opacity level.

---

## **ASYM(node)**  
Detects asymmetry between authority and accountability.

---

# 7. Donor Alignment Operators

## **INTENT(donor)**  
Maps donor’s stated purpose.

---

## **IMPACT(flow)**  
Maps actual measurable outcomes.

---

## **GAP(intent ↔ impact)**  
Measures divergence between donor intent and real-world results.

---

## **SCORE(donor)**  
Produces an alignment score (AI-generated).

---

# 8. Flow Integrity Operators

## **TRACE(path)**  
Ensures every step of the flow is visible.

---

## **MAP(system)**  
Generates a full structural map of flows, regimes, and drift.

---

## **CHECK(node)**  
Performs a structural integrity check.

---

## **FIX(node)**  
Recommends structural corrections.

---

# Summary

These operators form the structural grammar of the Philanthropy & Funding Transparency module.  
They allow all actors — donors, organizations, auditors, communities, and AI agents — to analyze funding flows using a shared, triadic, RTT-aligned language.

This grammar is the foundation of the module’s clarity engine.

