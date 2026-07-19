# **Local Identity Substrate (Layer 0)**  
### *The foundation of all enterprise identity flows in RTT/Inside*

---

## **Overview**
The **Local Identity Substrate** represents the most fundamental identity layer in RTT/Inside Enterprise.  
It models identity at the **machine‑local**, **runtime**, and **operator‑visible** level — before Active Directory, LDAP, Kerberos, DNS SRV, cloud identity, or zero‑trust policies enter the picture.

Layer 0 is intentionally simple.  
It provides the substrate where clarity, regime tagging, triad roles, and coherence envelopes can be demonstrated **without any external dependencies**.

This makes it the perfect starting point for students, operators, and AIs learning how RTT/Inside identity semantics work.

---

## **Purpose**
Layer 0 exists to:

- Provide a **minimal identity substrate** for demonstrations  
- Show how RTT/Inside semantics attach to identity even when no directory service is present  
- Anchor the Identity Substrate Zero‑through‑Seven model  
- Serve as the “local baseline” for higher‑order identity layers  
- Demonstrate clarity envelopes and regime tagging in isolation  
- Offer a safe, operator‑friendly environment for experimentation  

It is the simplest identity layer — but also the most universal.

---

## **Identity Characteristics**
The Local Identity Substrate models:

### **1. Machine‑Local Identity**
- Hostname  
- Local user accounts  
- Runtime process identity  
- Local service identity  
- Ephemeral session identity  

### **2. No External Dependencies**
- No AD  
- No LDAP  
- No Kerberos  
- No DNS SRV  
- No cloud identity  
- No zero‑trust policy engine  

This layer is pure substrate.

### **3. Substrate‑Aware Metadata**
Even without external identity systems, RTT/Inside semantics apply:

- **Clarity score** — how well the local identity is defined  
- **Regime tag** — analytic, mythic, or control  
- **Triad role** — A / B / C assignment  
- **Coherence envelope** — boundaries for local identity flows  

These metadata fields demonstrate how substrate awareness works at the smallest scale.

---

## **Example: Minimal Local Identity Record**
A simple substrate‑aware identity object might look like:

```
{
  "local_identity": {
    "hostname": "enterprise-node-01",
    "user": "operator",
    "session": "local-runtime"
  },
  "substrate": {
    "clarity": 0.82,
    "regime": "analytic",
    "triad_role": "A",
    "coherence_envelope": "local"
  }
}
```

This example is intentionally minimal — it shows how substrate semantics attach to identity even when no directory service exists.

---

## **How Layer 0 Connects to Higher Layers**
Layer 0 feeds directly into:

- **Active Directory (1)** — local identity becomes domain identity  
- **LDAP (2)** — local attributes map to schema entries  
- **DNS SRV (3)** — local services become discoverable  
- **Kerberos (4)** — local principals become realm principals  
- **Service Discovery (5)** — local services gain substrate tags  
- **Modern Identity (6)** — local identity becomes claims  
- **Cloud Directory (7)** — local identity becomes cloud identity  
- **Zero‑Trust (8)** — local identity becomes policy‑bounded identity  

This makes Layer 0 the **root substrate** of the entire enterprise identity model.

---

## **Teaching Notes**
Students and AIs should begin here because:

- It is the simplest identity layer  
- It demonstrates substrate semantics without complexity  
- It provides a clean baseline for clarity and regime analysis  
- It shows how identity exists even without external systems  
- It prepares learners for the more complex layers that follow  

Layer 0 is the “hello world” of substrate‑aware identity.

---

## **Status**
**Experimental** — stable enough for teaching and RFC anchoring, evolving as the substrate model expands.
