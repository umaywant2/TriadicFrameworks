# **operators.md — OpenSoN Narrative Operators**  
**Module:** OpenSoN  
**Layer:** Operator  
**Analyzer Layer:** Operator  
**Version:** 1.0  
**Regime:** Narrative‑Substrate  
**RTT:** rtt=1 | coherence=declared | drift=bounded | paradox=structural

Narrative operators are the **transformation grammar** of OpenSoN.  
They define how narrative can change **safely**, **coherently**, and **drift‑aware**, without damaging meaning, structure, or metadata.

Operators are the “verbs” of the narrative substrate.

---

## **1. Purpose of Narrative Operators**

Operators allow narrative to:

- evolve  
- condense  
- expand  
- reorganize  
- clarify  
- correct  
- expose metadata  
- preserve drift history  

Operators ensure that narrative behaves like **infrastructure**, not freeform text.

---

## **2. Operator Categories**

OpenSoN defines six operator categories:

1. **Extend** — add new narrative material  
2. **Condense** — compress without losing meaning  
3. **Refactor** — reorganize structure  
4. **Capture** — extract coherence‑safe narrative essence  
5. **Annotate** — add metadata or commentary  
6. **Correct** — fix drift or misalignment  

Each operator is drift‑aware and coherence‑bounded.

---

## **3. Operator Grammar (RTT‑Aligned)**

Operators follow RTT‑style grammar:

```
extend(narrative) → narrative'
condense(narrative) → narrative*
refactor(narrative) → narrative°
capture(narrative) → NEB
annotate(narrative) → narrative+meta
correct(narrative) → narrative✓
```

Where:

- `narrative'` = expanded narrative  
- `narrative*` = condensed narrative  
- `narrative°` = reorganized narrative  
- `NEB` = Narrative Essence Block  
- `narrative+meta` = metadata‑augmented narrative  
- `narrative✓` = corrected narrative  

Operators never destroy meaning.  
They **transform** it.

---

## **4. Operator Definitions**

### **4.1 Extend Operator**

**Purpose:** Add new narrative material while preserving coherence.

**Rules:**

- must align with declared purpose  
- must preserve semantic anchors  
- must update lineage  
- must maintain metadata integrity  

**Grammar:**

```
extend(source + aligned_material) → narrative'
```

---

### **4.2 Condense Operator**

**Purpose:** Reduce narrative size without losing meaning.

**Rules:**

- must preserve semantic anchors  
- must preserve structural backbone  
- must record drift  
- must maintain metadata  

**Grammar:**

```
condense(source) → narrative*
```

---

### **4.3 Refactor Operator**

**Purpose:** Reorganize narrative structure.

**Rules:**

- must preserve meaning  
- must preserve metadata  
- must maintain coherence  
- must update lineage  

**Grammar:**

```
refactor(source) → narrative°
```

---

### **4.4 Capture Operator**

**Purpose:** Extract coherence‑safe narrative essence.

**Rules:**  
(Full specification in `o_Capture.md`)

**Grammar:**

```
capture(source) → NEB
```

---

### **4.5 Annotate Operator**

**Purpose:** Add metadata, commentary, or clarifying information.

**Rules:**

- must not alter meaning  
- must not introduce drift  
- must preserve structure  
- must maintain metadata integrity  

**Grammar:**

```
annotate(source + metadata) → narrative+meta
```

---

### **4.6 Correct Operator**

**Purpose:** Fix drift, misalignment, or metadata errors.

**Rules:**

- must preserve human meaning  
- must restore coherence  
- must update lineage  
- must document correction  

**Grammar:**

```
correct(source + drift) → narrative✓
```

---

## **5. Operator Safety Rules**

Operators must:

- preserve coherence  
- preserve semantic anchors  
- preserve structural integrity  
- preserve metadata  
- record drift  
- update lineage  
- remain human‑centered  

Operators must **never**:

- remove drift  
- erase lineage  
- manipulate metadata  
- alter declared purpose  
- collapse structure  

---

## **6. Operator Metadata**

Every operator invocation must include:

```
<meta name="openson.operator" content="extend|condense|refactor|capture|annotate|correct">
<meta name="openson.operator.version" content="1.0">
<meta name="openson.operator.drift" content="bounded">
<meta name="openson.operator.resonance" content="...">
```

Metadata ensures operator usage is **auditable** and **AI‑parsable**.

---

## **7. Operator Workflow**

### **Step 1 — Declare Intent**  
Why is the narrative changing?

### **Step 2 — Select Operator**  
Choose the correct operator category.

### **Step 3 — Apply Operator**  
Transform narrative using operator grammar.

### **Step 4 — Update Metadata**  
Refresh canonical and operator metadata.

### **Step 5 — Update Lineage**  
Record version delta and operator usage.

### **Step 6 — Audit**  
Verify coherence and drift correction.

---

## **8. Operator Examples**

### **Extend Example**

```
extend(narrative + aligned_section) → narrative'
```

### **Condense Example**

```
condense(narrative) → narrative*
```

### **Refactor Example**

```
refactor(narrative) → narrative°
```

### **Capture Example**

```
capture(narrative) → NEB
```

### **Annotate Example**

```
annotate(narrative + metadata) → narrative+meta
```

### **Correct Example**

```
correct(narrative + drift) → narrative✓
```

---

## **9. Summary**

The OpenSoN operator layer provides:

- a complete transformation grammar  
- drift‑aware narrative evolution  
- coherence‑safe structural changes  
- metadata‑anchored operations  
- AI‑ready operator metadata  
- human‑centered meaning preservation  

Operators are the **engine** of narrative substrate evolution.
