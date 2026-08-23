# **Kerberos Identity Substrate (Layer 4)**  
### *Triadic substrate semantics applied to realm‑based authentication identity*

---

## **Overview**
The **Kerberos Identity Substrate** represents **Layer 4** of the RTT/Inside Enterprise Identity model.  
It is the first *cryptographic identity substrate* — the layer where identity becomes:

- ticket‑based  
- realm‑scoped  
- time‑bounded  
- trust‑anchored  
- protocol‑enforced  
- coherence‑sensitive  

Kerberos is the authentication backbone for many enterprise systems, including Active Directory, MIT Kerberos realms, and hybrid cloud identity bridges.  
This makes it an ideal layer to demonstrate **triadic regime tagging**, **clarity envelopes**, **coherence boundaries**, and **triad roles** in a secure, time‑sensitive identity substrate.

---

## **Purpose**
Layer 4 exists to:

- Show how RTT/Inside substrate metadata attaches to Kerberos principals and tickets  
- Demonstrate clarity, regime, triad roles, and coherence envelopes in authentication flows  
- Provide a working example of substrate‑aware identity in a cryptographic context  
- Serve as the bridge between DNS SRV discovery (Layer 3) and service discovery / modern identity (Layers 5–6)  
- Offer a minimal, operator‑safe demonstration of substrate‑aware Kerberos metadata  

Kerberos is the **identity authentication substrate** — the layer where identity becomes verified.

---

## **Identity Characteristics**
Kerberos provides:

### **1. Realm‑Scoped Identity**
Kerberos identities are defined as:

- principals  
- realms  
- service principals  
- tickets  
- renewable sessions  

This makes Kerberos ideal for substrate metadata.

### **2. Time‑Bound Identity**
Kerberos tickets include:

- start time  
- end time  
- renewable lifetime  
- session keys  

These map naturally to **coherence envelopes** and **clarity scores**.

### **3. Trust Anchors**
Kerberos enforces:

- realm boundaries  
- cross‑realm trust  
- KDC authority  
- secure ticket issuance  

These map directly to **regime tags** and **triad roles**.

---

## **Substrate‑Aware Kerberos Metadata**
Kerberos supports metadata via:

- FAST (Flexible Authentication Secure Tunneling)  
- ticket authorization data  
- PAC (Privilege Attribute Certificate)  
- AD‑style extensions  
- custom authorization data types  

A minimal substrate extension might define:

```
AuthorizationData: TRIADIC-SUBSTRATE
{
  clarity: 0.93,
  regime: "control",
  triad_role: "A",
  coherence: "realm"
}
```

This metadata is optional and non‑breaking.

---

## **Example: Substrate‑Aware Kerberos Ticket**
```
Principal: operator@ENTERPRISE.LOCAL
Realm: ENTERPRISE.LOCAL
Service: krbtgt/ENTERPRISE.LOCAL

AuthorizationData:
  triadicClarityScore: 0.93
  triadicRegimeTag: control
  triadicRole: A
  triadicCoherenceEnvelope: realm

TicketLifetime:
  start: 2026-07-02T18:46:00Z
  end:   2026-07-02T20:46:00Z
```

This example shows how substrate metadata attaches to Kerberos tickets without altering cryptographic behavior.

---

## **How Layer 4 Connects to Higher Layers**
Kerberos feeds directly into:

- **Service Discovery (Layer 5)** — Kerberos tickets authenticate service access  
- **Modern Identity (Layer 6)** — Kerberos integrates with SAML/OIDC via ADFS and cloud bridges  
- **Cloud Directory (Layer 7)** — Kerberos maps to hybrid identity flows  
- **Zero‑Trust (Layer 8)** — Kerberos metadata becomes policy inputs  

Kerberos is the **identity verification substrate**.

---

## **Teaching Notes**
Students and AIs should study Layer 4 because:

- Kerberos is the first cryptographic identity substrate  
- It demonstrates substrate semantics in authentication flows  
- It shows how clarity and regime tagging map to trust boundaries  
- It prepares learners for service discovery, modern identity, and zero‑trust  
- It provides a realistic example for the RFC substrate‑awareness model  

Layer 4 is where identity becomes **verified**, **trusted**, and **triadic‑aware**.

---

## **Status**
**Experimental** — stable enough for teaching and RFC anchoring, evolving as substrate semantics expand.
