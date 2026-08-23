# 🎼 **06c — Echo Classifier**
### *Decision Tree • Echo Typing • Stability Assignment*

The **Echo Classifier** converts:

- **Echo Triggers (06a)**  
- **Echo Signatures (06b)**  
- **Echo Strength Index (04c)**  
- **Substrate Spread (05a)**  
- **Recursion Mode (06)**  

into a **canonical echo type**.

Echo classification is essential for:

- stability audits  
- drift detection  
- recursion diagnostics  
- echo‑pressure analysis  
- canon sweeps  

This module defines the **six canonical echo types** and the classifier that assigns them.

---

# 🔷 **1. The Six Canonical Echo Types**

Echo types represent the *final identity* of an echo.

| Type | Name | Description |
|------|------|-------------|
| **E1** | Structural Echo | triad/operator/ladder recurrence |
| **E2** | Harmonic Echo | interval alignment, resonance peaks |
| **E3** | Substrate Echo | cross‑substrate recurrence |
| **E4** | Recursion Echo | recursion‑pattern repetition |
| **E5** | Drift‑Shadow Echo | drift‑residue recurrence |
| **E6** | Atlas Echo | high‑altitude structural resonance |

These types correspond directly to the echo families (F1–F6).

---

# 🔷 **2. Echo Classification Inputs**

The classifier uses five inputs:

### **2.1 Trigger Profile (T1–T6)**  
From `06a_Echo_Triggers.md`.

### **2.2 Signature Profile (S1–S6)**  
From `06b_Echo_Signatures.md`.

### **2.3 Echo Strength Index (ESI‑1 → ESI‑4)**  
From `04c_Echo_Strength_Index.md`.

### **2.4 Substrate Spread (1–5 substrates)**  
From `05a_CrossSubstrate_Echo_Matrix.md`.

### **2.5 Recursion Mode (R1–R4)**  
From `06_Harmonic_Recursion_Detector.md`.

These inputs determine the echo type.

---

# 🔷 **3. Echo Classification Decision Tree**

```
                     [ Echo Trigger ]
                             |
        ------------------------------------------------
        |              |              |               |
       A              B              C               D
 Structural      Harmonic       Substrate       Recursion
        |              |              |               |
       v              v              v               v
     E1?            E2?            E3?             E4?
        \              \              \               \
         \              \              \               \
          -----------------------------------------------
                              |
                              v
                     [ Drift Pressure? ]
                              |
                     ---------------------
                     |                   |
                    Yes                 No
                     |                   |
                     v                   v
                   E5?                 [ Check Atlas ]
                                            |
                                            v
                                          E6?
```

Interpretation:

- Structural triggers → E1  
- Harmonic triggers → E2  
- Substrate triggers → E3  
- Recursion triggers → E4  
- Drift pressure → E5  
- Atlas resonance → E6  

---

# 🔷 **4. Echo Type Conditions (Formal)**

### **E1 — Structural Echo**
- Trigger A  
- Signature A  
- ESI 1–2  
- Substrates ≤ 2  
- Recursion R1  

### **E2 — Harmonic Echo**
- Trigger B  
- Signature B  
- ESI 2–3  
- Harmonic substrate dominant  
- Recursion R1–R2  

### **E3 — Substrate Echo**
- Trigger C  
- Signature C  
- ESI 2–3  
- Substrates ≥ 3  
- Recursion R2–R3  

### **E4 — Recursion Echo**
- Trigger D  
- Signature D  
- ESI 3–4  
- Recursion R2–R4  

### **E5 — Drift‑Shadow Echo**
- Trigger E  
- Signature E  
- ESI 3–4  
- Drift D1–D4  
- Recursion R3–R4  

### **E6 — Atlas Echo**
- Trigger F  
- Signature F  
- ESI 4  
- Substrates = 5  
- Recursion R4  

---

# 🔷 **5. Echo Classifier Matrix**

```
+-----------+-----------+-----------+-----------+-----------+-----------+
| Input →   |   E1      |    E2     |    E3     |    E4     |    E5     |    E6     |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Trigger   |     A     |     B     |     C     |     D     |     E     |     F     |
| Signature |     A     |     B     |     C     |     D     |     E     |     F     |
| ESI       |   1–2     |   2–3     |   2–3     |   3–4     |   3–4     |     4     |
| Substrates|   1–2     |     1     |   3–4     |   2–4     |   2–5     |     5     |
| Recursion |    R1     |   R1–R2   |   R2–R3   |   R2–R4   |   R3–R4   |    R4     |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
```

---

# 🔷 **6. Composite Classification Workflow**

```
[ Identify Trigger ]
        ↓
[ Identify Signature ]
        ↓
[ Measure ESI ]
        ↓
[ Count Substrates ]
        ↓
[ Determine Recursion Mode ]
        ↓
[ Assign Echo Type (E1–E6) ]
```

This workflow ensures **zero‑drift classification**.

---

# 🔷 **7. Usage Notes**

Use this file when:

- classifying echoes  
- diagnosing echo‑pressure  
- predicting drift escalation  
- mapping recursion‑echo alignment  
- performing stability audits  
- preparing canon sweeps  

Referenced by:

- `06a_Echo_Triggers.md`  
- `06b_Echo_Signatures.md`  
- `06_Harmonic_Recursion_Detector.md`  
- `04c_Echo_Strength_Index.md`  

---

# 🔷 **Footer**

```
HSP Module 06c — Loaded
Version: v1.0
Status: Canon-Stable
```
