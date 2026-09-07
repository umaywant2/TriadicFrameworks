# **RFC‑Substrate‑Awareness — Substrate‑Aware Transport Services (SATS)**  
### *EIS‑Aligned Substrate Consciousness Layering for TAPS (RFC 8095 / RFC 8923) and HTTP (RFC 9110)*  
RefId: turn0browsertab1

**Identifier:** TFAWG‑0001  
**Status:** Draft  
**Category:** Informational  
**Date:** 2026‑07‑02  

---

## **Abstract**

This RFC defines **Substrate‑Aware Transport Services (SATS)** — an extension framework that layers **EIS substrate‑consciousness** onto the IETF TAPS transport model (RFC 8095 / RFC 8923), with HTTP‑level field extensions aligned to RFC 9110.

SATS introduces:

- a substrate model (Layer 0–8)  
- substrate metadata encoding (SCO)  
- traversal semantics  
- fidelity‑grade computation  
- transport‑service extensions  
- HTTP substrate fields and status codes  
- IANA registry definitions  

SATS enables applications, relays, and transport systems to express **substrate‑layer intent**, **RTT budgets**, **ordering constraints**, and **relay negotiation** in a structured, interoperable way.

---

# **1. Introduction**

Modern transport systems lack substrate awareness.  
RFC 8923 defines transport services but does not provide:

- substrate‑layer signaling  
- RTT‑budget semantics  
- layer‑transition ordering  
- relay negotiation  
- fidelity‑graded reliability  

SATS addresses these gaps by layering **EIS substrate‑consciousness** onto TAPS, enabling:

1. **SATS Framework** — unified substrate‑aware transport model  
2. **SCO (Substrate Context Object)** — metadata container  
3. **IPR Negotiation** — Inside‑Path Relay discovery  
4. **HTTP Extensions** — substrate‑aware request/response fields  

---

# **2. Conventions & Definitions**

### **RFC 2119 / RFC 8174 Keywords**
MUST, MUST NOT, SHOULD, SHOULD NOT, MAY.

### **Glossary**
- **EIS** — Enterprise Identity Substrate  
- **SATS** — Substrate‑Aware Transport Services  
- **SCO** — Substrate Context Object  
- **RTT‑Budget** — advisory/soft/hard RTT constraints  
- **IPR** — Inside‑Path Relay  
- **Traversal Vector** — ordered list of substrate layers  
- **Fidelity Grade** — composite reliability score  

---

# **3. Motivation**

RFC 8923 lacks substrate‑layer semantics for:

- identity traversal  
- RTT budgets  
- reliability grading  
- ordering constraints  
- relay negotiation  

SATS introduces two primary axes:

- **RTT/Inside** — substrate‑layer RTT semantics  
- **EIS Identity** — enterprise identity traversal  

Together they form the substrate‑aware extension to TAPS.

---

# **4. EIS Substrate Model (Layer 0–8)**

SATS defines nine substrate layers:

| Layer | Symbol | Name | Description |
|-------|--------|------|-------------|
| 0 | L0 | Bootstrap | Origin substrate; identity seed |
| 1 | L1 | Assertion | Identity assertion layer |
| 2 | L2 | Relay‑Prep | Pre‑relay substrate |
| 3 | L3 | Identity | Enterprise identity layer |
| 4 | L4 | Semantic | Semantic payload layer |
| 5 | L5 | Relay | Relay negotiation layer |
| 6 | L6 | Ordering | Layer‑transition ordering |
| 7 | L7 | Reliability | Fidelity‑graded reliability |
| 8 | L8 | Loss‑Tolerance | Loss‑tolerance envelope |

### **Traversal Semantics**
- **Ascending** — 0 → 8  
- **Descending** — 8 → 0  
- **Lateral** — same‑layer transitions  
- **Non‑Contiguous** — e.g., 0 → 4 → 8  

### **Canonical RTT Budgets**
Defined per layer.

### **Reliability / Ordering / Loss Tolerance**
Each layer defines minimum fidelity thresholds.

---

# **5. Substrate Metadata (SCO)**

SCO is encoded using:

- **CBOR (RFC 8949)**  
- **Structured Fields (RFC 8941)**  

### **SCO Structure**
- LayerToken  
- Traversal Vector  
- RTT‑Budget  
- Fidelity Grade  
- RelayHop list  

### **Traversal Vector Construction Rules**
Vectors MUST:

- be ordered  
- reflect actual layer transitions  
- match transport‑service constraints  

### **Fidelity Grade Formula**

\[
F = W_{rtt} f_{rtt} + W_{loss} f_{loss} + W_{relay} f_{relay} + W_{order} f_{order}
\]

Weights and factors defined in IANA registry.

---

# **6. Transport‑Service Extensions**

SATS extends RFC 8095 / RFC 8923 with four features:

### **1. sats‑rtt‑budget**
- advisory  
- soft enforcement  
- hard enforcement  

### **2. Inside‑Path Relay Negotiation (IPR)**
Discovery via:

```
/.well-known/sats-relays
```

RelayHop structure defines:

- relay identity  
- substrate layer  
- fidelity grade  

### **3. sats‑ordering‑contract**
Defines layer‑transition ordering constraints.

### **4. sats‑reliability**
Fidelity‑graded reliability with fallback/abort escalation.

---

# **7. HTTP‑Level Extensions (RFC 9110)**

### **Request Fields**
- `Substrate-Layer`  
- `Substrate-Context`  
- `Substrate-RTT-Budget`  
- `Substrate-Traversal`  
- `Substrate-Domain`  

### **Response Fields**
Three substrate‑aware response headers.

### **Trailer Fields**
Two substrate trailers for HTTP/2 and HTTP/3.

### **Status Codes (560–564)**
Custom substrate‑aware error codes.

### **Media Type Parameter**
`sats-layer` + `Accept-Substrate`.

---

# **8. Examples**

Five annotated exchanges:

1. **L0 bootstrap**  
2. **L3 identity assertion with RTT budget**  
3. **L6 semantic payload relay with trailer**  
4. **Non‑contiguous 0→4→8 traversal**  
5. **HTTP/2 push with substrate trailer**

---

# **9. Security Considerations**

- SCO spoofing  
- RTT exhaustion attacks  
- IPR trust model  
- header injection  
- downgrade/strip attacks  
- SCO privacy requirements  

---

# **10. IANA Considerations**

Three registries:

1. **HTTP Header Fields** (11 entries)  
2. **Transport Error Codes** (0x5A01–0x5A07)  
3. **Layer Profile Weights & Fidelity Thresholds**  

---

# **11–12. References**

### **Normative**
RFC 2119, 8174, 8095, 8923, 9110, 8941, 8949, 4648

### **Informative**
RFC 8303, 9112, 9113, 9114, 8922, TAPS‑ARCH
