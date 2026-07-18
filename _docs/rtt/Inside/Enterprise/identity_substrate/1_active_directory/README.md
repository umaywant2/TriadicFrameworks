# **Active Directory Identity Substrate (Layer 1)**  
### *Triadic substrate semantics applied to domain identity*

---

## **Overview**
The **Active Directory Identity Substrate** represents **Layer 1** of the RTT/Inside Enterprise Identity model.  
It is the first *external* identity substrate above the local layer, and the first point where enterprise identity becomes:

- centralized  
- directory‑backed  
- schema‑driven  
- policy‑enforced  
- discoverable  
- trust‑anchored  

Active Directory (AD) is historically the successor to Banyan StreetTalk and the conceptual ancestor of modern cloud identity systems.  
This makes it the perfect layer to demonstrate **triadic substrate semantics** in a real enterprise environment.

---

## **Purpose**
Layer 1 exists to:

- Show how RTT/Inside substrate metadata attaches to domain identity  
- Demonstrate clarity, regime, triad roles, and coherence envelopes in a directory context  
- Provide a working example for the RFC substrate‑awareness model  
- Serve as the bridge between local identity (Layer 0) and LDAP/Kerberos/DNS SRV layers  
- Offer a minimal, operator‑safe demonstration of substrate‑aware AD attributes  

This layer is the first “enterprise‑grade” identity substrate in the model.

---

## **Identity Characteristics**
Active Directory provides:

### **1. Domain Identity**
- Domain users  
- Domain computers  
- Domain groups  
- Domain service accounts  
- Domain controllers  

### **2. Schema‑Driven Attributes**
AD supports custom attributes, making it ideal for substrate metadata:

- `triadicClarityScore`  
- `triadicRegimeTag`  
- `triadicRole`  
- `triadicCoherenceEnvelope`  

These attributes are optional and non‑breaking.

### **3. Trust & Policy**
AD enforces:

- authentication  
- authorization  
- group policy  
- domain trust boundaries  

These map naturally to **coherence envelopes** and **regime boundaries**.

---

## **Substrate‑Aware AD Attributes**
A minimal substrate extension for AD might define:

```
triadicClarityScore: FLOAT (0.0–1.0)
triadicRegimeTag: STRING ("analytic" | "mythic" | "control")
triadicRole: STRING ("A" | "B" | "C")
triadicCoherenceEnvelope: STRING ("local" | "domain" | "forest")
```

These attributes can be added via:

- AD Schema Editor  
- LDIF import  
- PowerShell AD module  
- Directory Services Restore Mode (DSRM) for testing  

They do not alter authentication or authorization behavior.

---

## **Example: Substrate‑Aware Domain User**
```
{
  "domain_identity": {
    "userPrincipalName": "operator@enterprise.local",
    "displayName": "Enterprise Operator",
    "distinguishedName": "CN=Operator,OU=Users,DC=enterprise,DC=local"
  },
  "substrate": {
    "clarity": 0.91,
    "regime": "analytic",
    "triad_role": "B",
    "coherence_envelope": "domain"
  }
}
```

This example shows how substrate metadata can be attached to a domain identity without modifying AD’s core behavior.

---

## **How Layer 1 Connects to Higher Layers**
Active Directory feeds directly into:

- **LDAP (Layer 2)** — AD is LDAP‑backed  
- **DNS SRV (Layer 3)** — AD publishes SRV records for service discovery  
- **Kerberos (Layer 4)** — AD is the Kerberos KDC  
- **Service Discovery (Layer 5)** — AD exposes services via SRV  
- **Modern Identity (Layer 6)** — AD FS, OIDC, SAML  
- **Cloud Directory (Layer 7)** — Azure AD Connect, hybrid identity  
- **Zero‑Trust (Layer 8)** — AD becomes a policy anchor  

This makes Layer 1 the **enterprise identity foundation**.

---

## **Teaching Notes**
Students and AIs should study Layer 1 because:

- It is the first real enterprise identity substrate  
- It demonstrates substrate semantics in a directory context  
- It shows how clarity and regime tagging map to domain identity  
- It prepares learners for LDAP, Kerberos, DNS SRV, and cloud identity  
- It provides a realistic example for the RFC substrate‑awareness model  

Layer 1 is where substrate awareness becomes *visible* to enterprise operators.

---

## **Status**
**Experimental** — stable enough for teaching and RFC anchoring, evolving as substrate semantics expand.
