# TriadicFrameworks Module Dependency Graph

This graph shows how modules relate to each other across the TriadicFrameworks
ecosystem. It helps contributors understand conceptual flow, operator reuse,
and metadata alignment.

---

## 1. High-Level Graph

```
Core_Concepts
    │
    ├── Gravity_Foundations
    │       │
    │       ├── Drift_Taxonomy
    │       │       ├── d_Capture
    │       │       ├── d_Classify
    │       │       ├── d_Operators
    │       │       ├── d_Examples
    │       │       └── d_Paper
    │       │
    │       └── FFF_Gravity
    │
    ├── RTT_Operators
    │       └── Operator_Families
    │
    └── Module_Graph
            └── modules_group.json
```

---

## 2. Drift Taxonomy Internal Graph

```
Drift_Taxonomy
    │
    ├── d_Capture.md
    │       └── Defines drift types
    │
    ├── d_Classify.md
    │       └── Uses drift types to classify papers
    │
    ├── d_Operators.md
    │       └── Provides algebraic corrections for each drift
    │
    ├── d_Examples.md
    │       └── Applies corrections to representative works
    │
    └── d_Paper.md
            └── Assembles the unified meta-paper
```

---

## 3. Cross-Module Dependencies

### **Depends On**
- Gravity_Foundations (conceptual grounding)
- Operator_Families (operator patterns)
- Module_Graph (metadata consistency)

### **Provides**
- Drift classification system
- Operator correction system
- Publication-ready meta-paper
- Templates for future drift modules

---

## 4. Metadata Flow

```
module.json
    ├── roles → maps files to conceptual functions
    ├── analyzer_layer → defines operator/drift/regime sets
    ├── files → anchors directory structure
    ├── ai → enables AI discovery and navigation
    └── citation → anchors publication identity
```

---

## 5. Usage

This graph helps contributors:

- understand how Drift Taxonomy fits into the broader ecosystem  
- identify where new modules should connect  
- ensure metadata consistency  
- maintain conceptual coherence  
