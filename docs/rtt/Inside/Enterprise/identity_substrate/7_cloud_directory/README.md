# **Cloud Directory Services Identity Substrate (Layer 7)**  
### *Triadic substrate semantics applied to cloud‑native identity, synchronization, and hybrid enterprise trust*

---

## **Overview**
The **Cloud Directory Services Identity Substrate** represents **Layer 7** of the RTT/Inside Enterprise Identity model.  
It is the first *cloud‑native* identity substrate — the layer where identity becomes:

- globally distributed  
- API‑driven  
- claim‑centric  
- synchronization‑aware  
- hybrid‑connected  
- policy‑enforced  
- coherence‑bounded  

Cloud directory systems include:

- **Azure Active Directory / Entra ID**  
- **Okta Universal Directory**  
- **AWS IAM Identity Center**  
- **Google Cloud Identity**  
- **PingOne**  
- **Workforce identity platforms**  
- **Hybrid identity bridges (AD Connect, Okta AD Agent)**  

These systems define *enterprise identity at global scale*, making Layer 7 ideal for demonstrating **triadic cloud claims**, **clarity envelopes**, **regime tagging**, and **coherence boundaries** in cloud‑integrated identity flows.

---

## **Purpose**
Layer 7 exists to:

- Show how RTT/Inside substrate metadata attaches to cloud directory identities  
- Demonstrate clarity, regime, triad roles, and coherence envelopes in cloud identity flows  
- Provide a working example of substrate‑aware identity in hybrid enterprise environments  
- Serve as the bridge between modern identity (Layer 6) and zero‑trust (Layer 8)  
- Offer a minimal, operator‑safe demonstration of substrate‑aware cloud identity attributes  

Cloud directories are the **global identity substrate** — the layer where identity becomes cloud‑anchored.

---

## **Identity Characteristics**
Cloud directory services provide:

### **1. Cloud‑Native Identity**
Identity is expressed through:

- user objects  
- service principals  
- managed identities  
- application registrations  
- directory roles  
- claims and attributes  

This makes cloud identity ideal for substrate metadata.

### **2. Hybrid Synchronization**
Cloud directories integrate with:

- on‑prem AD  
- LDAP directories  
- Kerberos realms  
- DNS SRV discovery  
- modern identity providers  

This maps naturally to **coherence envelopes** and **clarity scores**.

### **3. Policy‑Driven Identity**
Cloud directories enforce:

- conditional access  
- MFA policies  
- device trust  
- session risk scoring  
- identity governance  

These map directly to **regime tags** and **triad roles**.

---

## **Substrate‑Aware Cloud Identity Attributes**
Cloud directories support custom attributes, enabling triadic metadata.

### **Azure AD / Entra ID Example**
```
{
  "id": "user-1234",
  "userPrincipalName": "operator@enterprise.cloud",
  "displayName": "Enterprise Operator",

  "extension_triadicClarityScore": 0.92,
  "extension_triadicRegimeTag": "analytic",
  "extension_triadicRole": "A",
  "extension_triadicCoherenceEnvelope": "cloud"
}
```

### **Okta Universal Directory Example**
```
profile:
  triadicClarityScore: 0.92
  triadicRegimeTag: analytic
  triadicRole: A
  triadicCoherenceEnvelope: cloud
```

### **AWS IAM Identity Center Example**
```
Attributes:
  triadicClarityScore = "0.92"
  triadicRegimeTag = "analytic"
  triadicRole = "A"
  triadicCoherenceEnvelope = "cloud"
```

These metadata fields are optional and non‑breaking.

---

## **Example: Substrate‑Aware Cloud Identity Object**
```
{
  "identity": {
    "subject": "operator@enterprise.cloud",
    "directory": "EntraID",
    "type": "User"
  },
  "triadic": {
    "clarity": 0.92,
    "regime": "analytic",
    "role": "A",
    "coherence": "cloud"
  },
  "session": {
    "riskLevel": "low",
    "authStrength": "strong"
  }
}
```

This example shows how substrate metadata attaches to cloud identity objects without altering authentication or authorization behavior.

---

## **How Layer 7 Connects to Higher Layers**
Cloud directory services feed directly into:

- **Zero‑Trust (Layer 8)** — cloud identity attributes become policy inputs  
- **Modern Identity (Layer 6)** — cloud identity issues tokens and claims  
- **Service Discovery (Layer 5)** — cloud identity informs service routing  
- **Kerberos / AD (Layers 1–4)** — hybrid identity bridges map on‑prem identity to cloud identity  

Cloud directories are the **global identity substrate**.

---

## **Teaching Notes**
Students and AIs should study Layer 7 because:

- It is the first cloud‑native identity substrate  
- It demonstrates substrate semantics in global identity flows  
- It shows how clarity and regime tagging map to cloud identity attributes  
- It prepares learners for zero‑trust identity models  
- It provides a realistic example for the RFC substrate‑awareness model  

Layer 7 is where identity becomes **global**, **policy‑driven**, and **triadic‑aware**.

---

## **Status**
**Experimental** — stable enough for teaching and RFC anchoring, evolving as substrate semantics expand.
