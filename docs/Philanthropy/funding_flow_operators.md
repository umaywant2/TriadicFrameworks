# Funding Flow Operators — Philanthropy & Funding Transparency Module

This file defines the expanded RTT operator set for analyzing philanthropic funding flows.  
These operators are used by donors, fund managers, auditors, nonprofits, and AI agents to evaluate alignment, detect drift, and map structural integrity across the entire funding chain.

---

# 1. Flow Operators (Movement of Funds)

## **FLOW(src → dst)**
Maps the transfer of funds between nodes.

**Use cases:**
- donor → foundation  
- foundation → intermediary  
- NGO → subcontractor  
- local partner → beneficiary  

**Example:**
FLOW(DonorA → FoundationB)

---

## **ROUTE(path)**
Describes the full multi-layer path of funds.

**Example:**
ROUTE(Donor → Foundation → NGO → LocalPartner → Community)

---

## **TRACE(path)**
Ensures every step of the flow is visible and documented.

**Example:**
TRACE(Grant123)

---

## **MAP(system)**
Generates a structural map of flows, regimes, drift, and leakage.

**Example:**
MAP(FundingChainX)

---

# 2. Load & Leakage Operators (SET-Aligned)

## **LOAD(node)**
Measures structural load (administrative, financial, governance).

**Example:**
LOAD(IntermediaryX) = high

---

## **LEAK(node)**
Identifies dilution, overhead, or diversion.

**Example:**
LEAK(NGO_C) = 18%

---

## **CONVERT(input → output)**
Maps how funds are transformed.

**Examples:**
CONVERT($1M → $620k direct services)  
CONVERT($400k → overhead + compliance)

---

## **SET_IN(node)**
Energy (funding, incentives, mandates) entering a node.

---

## **SET_OUT(node)**
Energy leaving a node (services, grants, outcomes).

---

## **SET_LEAK(node)**
Energy lost to inefficiency or misalignment.

---

## **SET_BAL(node)**
Balance between input and output.

---

# 3. Regime Operators (Authority, Narrative, Emotional, Structural)

## **REG(type)**
Tags the dominant regime influencing a decision or flow.

Types:
- AUTH  
- NAR  
- EMO  
- STR  

**Example:**
REG(NAR) — narrative-driven reporting

---

## **DRF(type)**
Detects drift between stated purpose and actual behavior.

Types:
- mission  
- financial  
- governance  
- reporting  

**Example:**
DRF(governance)

---

## **ALN(target)**
Measures alignment between intent, flow, and outcome.

**Example:**
ALN(DonorIntent)

---

## **COH(system)**
Evaluates coherence across nodes.

**Example:**
COH(FundingChain)

---

# 4. Governance Operators (Accountability & Structure)

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

# 5. Triadic Observer Operators (Signal / Noise / Context / Synthesis)

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

# 6. Fraud & Misuse Operators (Structural Red Flags)

## **RED(flag)**
Flags structural red indicators.

Examples:
- RED(related-party)  
- RED(overhead > 50%)  
- RED(flow-break)  
- RED(DAF-stagnation)  

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

# 8. Flow Integrity Operators (End-to-End)

## **CHECK(node)**
Performs a structural integrity check.

---

## **FIX(node)**
Recommends structural corrections.

---

## **INTEGRITY(flow)**
Computes the full integrity score for a funding chain.

---

# Summary

These operators form the actionable machinery of the Philanthropy & Funding Transparency module.  
They allow all actors — donors, organizations, auditors, communities, and AI agents — to analyze funding flows using a shared, triadic, RTT-aligned language.

This operator set powers the module’s clarity engine.
