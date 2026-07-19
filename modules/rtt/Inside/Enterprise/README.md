# **RTT/Inside Enterprise Identity Substrate**  
### *Minimal, substrate‑aware enterprise example for students, operators, and AIs*

---

## **Overview**
The **RTT/Inside Enterprise Identity Substrate** is a minimal, operator‑safe example module demonstrating how RTT/Inside substrate semantics (clarity, regime, triad roles, coherence envelopes) can be layered onto existing enterprise identity systems without breaking compatibility.

This module re‑imagines the early *enterprise_structural_awareness* prototype into a full substrate‑aware identity suite spanning **eight identity substrate layers**:

0. Local Identity Substrate  
1. Active Directory  
2. LDAP  
3. DNS SRV Identity Discovery  
4. Kerberos Realms  
5. Service Discovery Frameworks  
6. Modern Identity Substrates (OIDC, SAML, JWT claims)  
7. Cloud Directory Services (Azure AD, Okta, AWS IAM)  
8. Zero‑Trust Identity Models  

These layers form the **Identity Substrate Zero‑through‑Seven** (plus Zero‑Trust as layer 8), providing a complete demonstration surface for RTT/Inside semantics.

---

## **Purpose**
This module exists to:

- Provide a **minimal, working example** of substrate‑aware identity flows  
- Demonstrate how RTT/Inside semantics can be applied to real enterprise identity systems  
- Serve as a **reference implementation** for the informational RFC  
- Offer a clean, approachable teaching artifact for students and AIs  
- Anchor future substrate‑aware extensions for identity protocols  

It is intentionally small, clear, and canonical — a “first example” rather than a full enterprise suite.

---

## **Directory Structure**
```
docs/rtt/Inside/Enterprise/
    module.json
    README.md

    identity_substrate/
        0_local/
        1_active_directory/
        2_ldap/
        3_dns_srv/
        4_kerberos/
        5_service_discovery/
        6_modern_identity/
        7_cloud_directory/
        8_zero_trust/

    substrate_extensions/
        clarity/
        regime/
        triad_roles/
        coherence_envelopes/

    examples/
        minimal_enterprise/
        identity_flow/
        substrate_negotiation/

    tools/
        rtt-inside-identify
        rtt-inside-clarity
        rtt-inside-regime
        rtt-inside-triad
        rtt-inside-coherence
        rtt-inside-discovery
        rtt-inside-negotiation
        rtt-inside-enterprise
```

---

## **Identity Substrate Layers**
Each layer demonstrates how RTT/Inside semantics can be applied to existing identity systems:

### **0 — Local Identity Substrate**
Machine‑local identity, ephemeral runtime identity, operator‑safe clarity envelopes.

### **1 — Active Directory**
Triadic attributes, clarity scores, regime tagging, coherence envelopes.

### **2 — LDAP**
Schema extensions for substrate metadata, triad roles, clarity hints.

### **3 — DNS SRV**
Substrate‑aware service discovery tags, clarity priority, regime‑aware routing.

### **4 — Kerberos Realms**
Triadic realm descriptors, clarity claims, regime‑aware ticket metadata.

### **5 — Service Discovery Frameworks**
Triadic service roles, substrate negotiation hints, coherence envelopes.

### **6 — Modern Identity Substrates**
OIDC/SAML/JWT triadic claims, clarity claims, regime claims.

### **7 — Cloud Directory Services**
Azure AD / Okta / AWS IAM substrate metadata, clarity envelopes, triad roles.

### **8 — Zero‑Trust Identity Models**
Policy‑driven substrate boundaries, clarity‑based access hints, regime‑aware trust.

---

## **Substrate Extensions**
These extensions provide the RTT/Inside semantics used across all identity layers:

- **Clarity** — spectral clarity scores and envelopes  
- **Regime** — analytic, mythic, control regime tagging  
- **Triad Roles** — A/B/C role assignment  
- **Coherence Envelopes** — coherence boundaries for identity flows  

Each extension includes a minimal schema and example usage.

---

## **Examples**
### **Minimal Enterprise**
A small, end‑to‑end identity substrate flow across selected layers.

### **Identity Flow**
Triadic identity resolution and regime tagging demonstration.

### **Substrate Negotiation**
Shows how services negotiate substrate metadata without altering transport behavior.

---

## **RFC Reference**
This module anchors the informational RFC:

**Substrate‑Aware Transport Services (RTT/Inside)**  
Located at:  
`/docs/rfc/rfc-substrate-awareness.md`

The RFC references:

- **RFC 8095** — Transport Services  
- **RFC 8923** — Minimal Transport Services  
- **HTTP Semantics** — Application‑level substrate metadata  

This module provides the **working example** required for RFC credibility.

---

## **RTT/Inside Enterprise Suite Tools**
Minimal tools demonstrating substrate‑aware identity flows:

- rtt-inside-identify  
- rtt-inside-clarity  
- rtt-inside-regime  
- rtt-inside-triad  
- rtt-inside-coherence  
- rtt-inside-discovery  
- rtt-inside-negotiation  
- rtt-inside-enterprise  

These tools are intentionally small and operator‑safe.

---

## **Audience**
This module is designed for:

- Students  
- Operators  
- AI agents  
- Identity architects  
- Protocol researchers  
- RTT/Inside practitioners  

It is the first “enterprise‑level” substrate example in the TriadicFrameworks canon.

---

## **Status**
**Experimental** — stable enough for teaching and RFC anchoring, but evolving as the substrate model expands.
