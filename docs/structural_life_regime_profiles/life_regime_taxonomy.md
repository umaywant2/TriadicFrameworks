# **Life‑Regime Taxonomy**  
*A scalable classification system for biological and artificial life‑regimes*

The Life‑Regime Taxonomy provides a unified, vST‑aligned classification system for mapping life‑regimes across species, autonomous agents, robotics platforms, and synthetic lifeforms. It organizes life‑regimes into structural categories, subcategories, and regime‑invariant descriptors that support large‑scale comparative research and dataset construction.

This taxonomy is designed to be minimal, extensible, and architecture‑agnostic.

---

## **1. Taxonomy Overview**

Life‑regimes are classified along three structural layers:

- **Structural Regime**  
- **Sensory Regime**  
- **Environmental Regime**

Each layer is subdivided into categories and subcategories that describe how a system maintains coherence, perceives its environment, and acts within constraints.

The taxonomy is compatible with:

- biological organisms  
- autonomous AI systems  
- robotics stacks  
- hybrid or emergent systems  
- synthetic lifeforms  

---

## **2. Structural Regime Categories**

### **2.1 Reflexive Systems**
Systems with fixed or minimally adaptive internal patterns.

Examples:  
- insects with hard‑coded behaviors  
- simple robotics controllers  
- rule‑based agents  

**Subcategories:**  
- fixed‑pattern  
- low‑memory  
- non‑learning  

---

### **2.2 Adaptive Systems**
Systems capable of learning within their lifetime.

Examples:  
- mammals  
- reinforcement‑learning agents  
- adaptive robotics stacks  

**Subcategories:**  
- associative learning  
- reinforcement learning  
- supervised adaptation  

---

### **2.3 Strategic Systems**
Systems capable of long‑term planning and multi‑step reasoning.

Examples:  
- primates  
- advanced autonomous planners  

**Subcategories:**  
- tactical planning  
- strategic planning  
- multi‑agent coordination  

---

### **2.4 Symbolic Systems**
Systems capable of abstraction, meta‑models, and symbolic reasoning.

Examples:  
- humans  
- symbolic‑augmented AI systems  
- hybrid neuro‑symbolic architectures  

**Subcategories:**  
- language‑enabled  
- meta‑reasoning  
- model‑based abstraction  

---

## **3. Sensory Regime Categories**

### **3.1 Single‑Modality Systems**
Dominated by one sensory channel.

Examples:  
- chemical‑dominant insects  
- single‑sensor robots  

**Subcategories:**  
- chemical  
- vibrational  
- optical  
- tactile  

---

### **3.2 Dual‑Modality Systems**
Two primary sensory channels.

Examples:  
- many reptiles  
- basic robotics stacks  

**Subcategories:**  
- optical + chemical  
- tactile + optical  
- audio + optical  

---

### **3.3 Multimodal Systems**
Multiple integrated sensory channels.

Examples:  
- mammals  
- sensor‑rich autonomous systems  

**Subcategories:**  
- integrated multimodal  
- high‑bandwidth multimodal  
- specialized multimodal  

---

### **3.4 Extended‑Modality Systems**
Systems with prosthetic or synthetic sensory extensions.

Examples:  
- humans with instruments  
- AI systems with high‑dimensional sensor arrays  

**Subcategories:**  
- prosthetic sensing  
- synthetic sensing  
- high‑dimensional sensing  

---

## **4. Environmental Regime Categories**

### **4.1 Static Environments**
Low variation, predictable conditions.

Examples:  
- deep‑sea organisms  
- fixed‑task robots  

**Subcategories:**  
- low‑entropy  
- resource‑stable  

---

### **4.2 Cyclic Environments**
Periodic or seasonal variation.

Examples:  
- temperate‑zone species  
- time‑scheduled autonomous systems  

**Subcategories:**  
- seasonal  
- diurnal  
- tidal  

---

### **4.3 Dynamic Environments**
High variation, multi‑agent, unpredictable.

Examples:  
- primates  
- autonomous vehicles  

**Subcategories:**  
- multi‑agent  
- adversarial  
- resource‑volatile  

---

### **4.4 Constructed Environments**
Self‑modified or artificial environments.

Examples:  
- human societies  
- engineered AI ecosystems  

**Subcategories:**  
- socio‑technical  
- synthetic operational domains  
- hybrid environments  

---

## **5. Behavioral Regime Categories**

### **5.1 Reflexive Behavior**
Stimulus → action loops.

### **5.2 Tactical Behavior**
Short‑term planning.

### **5.3 Strategic Behavior**
Long‑term planning and adaptation.

### **5.4 Symbolic Behavior**
Abstraction, language, meta‑models.

These categories apply equally to biological and artificial systems.

---

## **6. Drift Condition Categories**

### **6.1 Low‑Drift Systems**
Stable under variation.

### **6.2 Moderate‑Drift Systems**
Stable with recovery mechanisms.

### **6.3 High‑Drift Systems**
Unstable under stress.

### **6.4 Catastrophic‑Drift Systems**
Rapid collapse under overload.

---

## **7. Stability Anchor Categories**

### **7.1 Intrinsic Anchors**
Internal mechanisms (homeostasis, redundancy).

### **7.2 Extrinsic Anchors**
Environmental or social scaffolding.

### **7.3 Hybrid Anchors**
Combination of internal and external stability.

### **7.4 Synthetic Anchors**
Engineered safeguards (AI/robotics).

---

## **8. Taxonomy Encoding for Big‑Data Research**

Life‑regime profiles can be encoded as structured records:

```
species_or_system:
  structural_regime:
    category:
    subcategory:
  sensory_regime:
    category:
    modalities:
  environmental_regime:
    category:
    subcategory:
  behavioral_regime:
    category:
  drift_conditions:
    category:
  stability_anchors:
    category:
```

This format supports:

- large‑scale comparative datasets  
- machine learning classification  
- cross‑species modeling  
- autonomous system benchmarking  
- vST‑aligned regime analysis  

---

## **9. Relationship to Other TriadicFrameworks Artifacts**

The taxonomy integrates with:

- **substrate_definition.md** — structural foundation  
- **regime_axes.md** — coordinate system  
- **cross_species_comparison.md** — biological mapping  
- **autonomous_system_alignment.md** — AI mapping  
- **drift_and_stability_profiles.md** — resilience analysis  

Together, they form a complete structural grammar for life‑regime modeling.
