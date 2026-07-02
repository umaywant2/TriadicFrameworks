# **Modern Identity Substrates (Layer 6)**  
### *Triadic substrate semantics applied to claims‑based, token‑based, and federated identity*

---

## **Overview**
The **Modern Identity Substrates** layer represents **Layer 6** of the RTT/Inside Enterprise Identity model.  
It is the first *claims‑based* identity substrate — the layer where identity becomes:

- tokenized  
- federated  
- claim‑centric  
- protocol‑agnostic  
- cloud‑integrated  
- coherence‑aware  

Modern identity systems include:

- **OIDC (OpenID Connect)**  
- **OAuth 2.0**  
- **SAML 2.0**  
- **JWT‑based identity providers**  
- **AD FS**  
- **Identity bridges (Ping, Okta, Azure AD)**  
- **API gateways and service meshes with identity filters**  

These systems define *who a user or service is* using **claims**, **tokens**, and **assertions**, making Layer 6 ideal for demonstrating **triadic claims**, **clarity envelopes**, **regime tagging**, and **coherence boundaries** in a modern identity context.

---

## **Purpose**
Layer 6 exists to:

- Show how RTT/Inside substrate metadata attaches to identity tokens and claims  
- Demonstrate clarity, regime, triad roles, and coherence envelopes in federated identity flows  
- Provide a working example of substrate‑aware identity in cloud‑integrated environments  
- Serve as the bridge between service discovery (Layer 5) and cloud directory / zero‑trust (Layers 7–8)  
- Offer a minimal, operator‑safe demonstration of substrate‑aware identity claims  

Modern identity is the **claims substrate** — the layer where identity becomes declarative.

---

## **Identity Characteristics**
Modern identity substrates provide:

### **1. Claims‑Based Identity**
Identity is expressed through:

- JWT claims  
- SAML assertions  
- OIDC ID tokens  
- OAuth access tokens  
- custom identity attributes  

This makes modern identity ideal for substrate metadata.

### **2. Tokenized Identity**
Tokens include:

- issuer  
- audience  
- subject  
- expiration  
- scopes  
- claims  

These map naturally to **clarity envelopes** and **coherence boundaries**.

### **3. Federated Identity**
Modern identity supports:

- cross‑realm federation  
- cloud identity bridging  
- hybrid identity flows  
- multi‑provider trust  

These map directly to **regime tags** and **triad roles**.

---

## **Substrate‑Aware Identity Claims**
Modern identity systems support custom claims, enabling triadic metadata.

### **OIDC / OAuth Example (JWT Claims)**
```
{
  "sub": "operator@enterprise.local",
  "iss": "https://id.enterprise.local",
  "aud": "https://api.enterprise.local",

  "triadicClarityScore": 0.89,
  "triadicRegimeTag": "analytic",
  "triadicRole": "B",
  "triadicCoherenceEnvelope": "cloud"
}
```

### **SAML Example**
```
<saml:Attribute Name="triadicClarityScore">
  <saml:AttributeValue>0.89</saml:AttributeValue>
</saml:Attribute>

<saml:Attribute Name="triadicRegimeTag">
  <saml:AttributeValue>analytic</saml:AttributeValue>
</saml:Attribute>

<saml:Attribute Name="triadicRole">
  <saml:AttributeValue>B</saml:AttributeValue>
</saml:Attribute>

<saml:Attribute Name="triadicCoherenceEnvelope">
  <saml:AttributeValue>cloud</saml:AttributeValue>
</saml:Attribute>
```

### **API Gateway / Mesh Identity Filter**
```
identity:
  user: operator
  triadic:
    clarity: 0.89
    regime: analytic
    role: B
    coherence: cloud
```

These metadata fields are optional and non‑breaking.

---

## **Example: Substrate‑Aware ID Token**
```
{
  "sub": "operator",
  "name": "Enterprise Operator",
  "email": "operator@enterprise.local",

  "triadicClarityScore": 0.89,
  "triadicRegimeTag": "analytic",
  "triadicRole": "B",
  "triadicCoherenceEnvelope": "cloud",

  "exp": 1762100000,
  "iat": 1762096400
}
```

This example shows how substrate metadata attaches to identity tokens without altering authentication or authorization behavior.

---

## **How Layer 6 Connects to Higher Layers**
Modern identity feeds directly into:

- **Cloud Directory (Layer 7)** — identity claims map to cloud identity attributes  
- **Zero‑Trust (Layer 8)** — claims become policy inputs  
- **Service Discovery (Layer 5)** — identity claims inform service routing  
- **Kerberos (Layer 4)** — identity bridges map Kerberos principals to claims  

Modern identity is the **claims substrate**.

---

## **Teaching Notes**
Students and AIs should study Layer 6 because:

- It is the first claims‑based identity substrate  
- It demonstrates substrate semantics in federated identity flows  
- It shows how clarity and regime tagging map to modern identity claims  
- It prepares learners for cloud identity and zero‑trust  
- It provides a realistic example for the RFC substrate‑awareness model  

Layer 6 is where identity becomes **tokenized**, **federated**, and **triadic‑aware**.

---

## **Status**
**Experimental** — stable enough for teaching and RFC anchoring, evolving as substrate semantics expand.
