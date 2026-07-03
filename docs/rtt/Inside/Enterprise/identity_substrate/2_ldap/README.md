# **LDAP Identity Substrate (Layer 2)**  
### *Triadic substrate semantics applied to schema‑driven directory identity*

---

## **Overview**
The **LDAP Identity Substrate** represents **Layer 2** of the RTT/Inside Enterprise Identity model.  
It is the first *pure directory* layer — independent of domain controllers, Kerberos, or DNS SRV — and the first layer where identity becomes:

- schema‑defined  
- attribute‑centric  
- extensible  
- cross‑platform  
- cross‑vendor  
- protocol‑neutral  

LDAP is the structural backbone behind many enterprise identity systems, including Active Directory, OpenLDAP, 389 Directory Server, and cloud directory bridges.  
This makes it an ideal substrate for demonstrating **triadic metadata**, **clarity envelopes**, **regime tags**, and **coherence boundaries**.

---

## **Purpose**
Layer 2 exists to:

- Show how RTT/Inside substrate metadata attaches to LDAP entries  
- Demonstrate clarity, regime, triad roles, and coherence envelopes in a schema‑driven directory  
- Provide a neutral identity substrate example (not tied to AD or Kerberos)  
- Serve as the bridge between AD (Layer 1) and DNS SRV / Kerberos (Layers 3–4)  
- Offer a minimal, operator‑safe demonstration of substrate‑aware LDAP attributes  

LDAP is the “identity substrate core” — the layer where identity becomes structured.

---

## **Identity Characteristics**
LDAP provides:

### **1. Schema‑Defined Identity**
LDAP entries are structured objects with:

- objectClasses  
- attributes  
- distinguished names  
- hierarchical placement  
- extensible schema  

This makes LDAP ideal for substrate metadata.

### **2. Cross‑Platform Neutrality**
LDAP is used by:

- AD (as its directory engine)  
- OpenLDAP  
- 389 Directory Server  
- ApacheDS  
- Cloud directory connectors  

This neutrality makes Layer 2 universally applicable.

### **3. Extensible Attributes**
LDAP supports custom attributes, enabling:

- `triadicClarityScore`  
- `triadicRegimeTag`  
- `triadicRole`  
- `triadicCoherenceEnvelope`  

These can be added via:

- schema LDIF  
- slapd configuration  
- AD schema editor (for AD‑backed LDAP)  
- cloud directory sync rules  

---

## **Substrate‑Aware LDAP Attributes**
A minimal LDAP schema extension might define:

```
attributeType ( 1.3.6.1.4.1.99999.1
  NAME 'triadicClarityScore'
  DESC 'RTT/Inside clarity score'
  SYNTAX 1.3.6.1.4.1.1466.115.121.1.26 SINGLE-VALUE )

attributeType ( 1.3.6.1.4.1.99999.2
  NAME 'triadicRegimeTag'
  DESC 'RTT/Inside regime tag'
  SYNTAX 1.3.6.1.4.1.1466.115.121.1.15 SINGLE-VALUE )

attributeType ( 1.3.6.1.4.1.99999.3
  NAME 'triadicRole'
  DESC 'RTT/Inside triad role'
  SYNTAX 1.3.6.1.4.1.1466.115.121.1.15 SINGLE-VALUE )

attributeType ( 1.3.6.1.4.1.99999.4
  NAME 'triadicCoherenceEnvelope'
  DESC 'RTT/Inside coherence envelope'
  SYNTAX 1.3.6.1.4.1.1466.115.121.1.15 SINGLE-VALUE )
```

These attributes are optional and non‑breaking.

---

## **Example: Substrate‑Aware LDAP Entry**
```
dn: uid=operator,ou=People,dc=enterprise,dc=local
objectClass: inetOrgPerson
objectClass: triadicSubstrateIdentity
uid: operator
cn: Enterprise Operator
sn: Operator

triadicClarityScore: 0.88
triadicRegimeTag: analytic
triadicRole: C
triadicCoherenceEnvelope: domain
```

This example shows how substrate metadata attaches to LDAP entries without altering authentication or directory behavior.

---

## **How Layer 2 Connects to Higher Layers**
LDAP feeds directly into:

- **DNS SRV (Layer 3)** — LDAP services are discoverable via SRV  
- **Kerberos (Layer 4)** — LDAP stores Kerberos principal metadata  
- **Service Discovery (Layer 5)** — LDAP exposes service entries  
- **Modern Identity (Layer 6)** — LDAP attributes become identity claims  
- **Cloud Directory (Layer 7)** — LDAP sync engines map attributes to cloud identity  
- **Zero‑Trust (Layer 8)** — LDAP attributes become policy inputs  

LDAP is the **identity substrate spine**.

---

## **Teaching Notes**
Students and AIs should study Layer 2 because:

- LDAP is the most universal identity substrate  
- It demonstrates substrate semantics in a schema‑driven directory  
- It shows how clarity and regime tagging map to structured identity  
- It prepares learners for DNS SRV, Kerberos, and cloud identity  
- It provides a realistic example for the RFC substrate‑awareness model  

Layer 2 is where identity becomes **structured**, **extensible**, and **triadic‑ready**.

---

## **Status**
**Experimental** — stable enough for teaching and RFC anchoring, evolving as substrate semantics expand.
