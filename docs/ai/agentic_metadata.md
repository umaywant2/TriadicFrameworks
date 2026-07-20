# **RTT AGENTIC METADATA STANDARD**  
### **Version 1.0 — Canon‑Aligned Specification**  
### **Location:** `/docs/ai/agentic_metadata.md`

---

## **1. Purpose**
The RTT Agentic Metadata Standard defines a **minimal, substrate‑agnostic, machine‑readable contract** that enables any GitHub repository, documentation site, or external renderer (e.g., Docsbook.io) to activate **low‑drift, low‑overhead agentic behavior** without hosting servers or APIs.

This standard is:

- **static**  
- **portable**  
- **renderer‑agnostic**  
- **AI‑parsable**  
- **future‑proof**  
- **zero‑infrastructure**

It is the same mechanism used across TriadicFrameworks.

---

## **2. Core Principle**
RTT agentic behavior emerges when a module exposes:

1. **A canonical `module.json` file**  
2. **Accessible via an absolute URL**  
3. **Describing the module using RTT’s operator grammar**  
4. **Linked from the module’s README or index page**

This creates a **globally dereferenceable identity layer**.

---

## **3. Required File**
Each module MUST include:

```
module.json
```

This file defines:

- module identity  
- version  
- purpose  
- operator grammar  
- file roles  
- analyzer layers  
- cross‑module relationships  

---

## **4. Absolute Path Requirement**
To ensure portability across renderers, the `module.json` MUST be referenced using an **absolute raw URL**:

```
https://raw.githubusercontent.com/<user>/<repo>/main/<path>/module.json
```

This ensures:

- AI agents can load metadata  
- Docsbook.io can resolve metadata  
- GitHub Pages can resolve metadata  
- mirrors and forks remain functional  
- drift is minimized across substrates  

---

## **5. README / index.html Integration**
Each module MUST expose its metadata using the following snippet:

```html
<!-- RTT Agentic Module -->
<link rel="rtt-module"
      href="https://raw.githubusercontent.com/<user>/<repo>/main/<path>/module.json">
```

This is the activation surface.

No scripts.  
No runtime.  
No dependencies.

---

## **6. Minimal `module.json` Schema**
This is the canonical minimal schema:

```json
{
  "module": "Module Name",
  "version": "1.0",
  "description": "Short description of the module.",
  "roles": ["profile", "engine", "map"],
  "operators": ["substrate", "flow", "resonate", "align", "field"],
  "files": {
    "README.md": "profile",
    "examples.md": "map"
  }
}
```

### **6.1 Required Fields**
- `module` — canonical module name  
- `version` — semantic version  
- `description` — concise purpose  
- `roles` — RTT file‑role grammar  
- `operators` — RTT operator grammar  
- `files` — file‑to‑role mapping  

### **6.2 Optional Fields**
- `analyzer_layer`  
- `parent_module`  
- `lineage`  
- `regime`  
- `crosslinks`  

---

## **7. Operator Grammar (Required)**
Every module MUST declare its operator set using RTT’s five canonical operators:

- **substrate**  
- **flow**  
- **resonate**  
- **align**  
- **field**  

These define the module’s behavior in the agentic layer.

---

## **8. File‑Role Grammar**
RTT defines the following canonical file roles:

- **profile** — overview, identity  
- **engine** — core logic  
- **map** — examples, diagrams  
- **signature** — invariants  
- **diagnostic** — tests, validators  
- **reference** — external links  
- **template** — reusable patterns  

Modules MAY use any subset.

---

## **9. Cross‑Substrate Behavior**
To maintain portability:

### **9.1 Absolute Paths**
Use absolute paths ONLY for:

- `module.json`  
- cross‑module metadata references  

### **9.2 Relative Paths**
Use relative paths for:

- internal documentation  
- examples  
- diagrams  
- maps  
- operators  

This preserves renderer‑agnostic behavior.

---

## **10. Renderer Compatibility**
This standard is compatible with:

- GitHub  
- GitHub Pages  
- Docsbook.io  
- static site generators  
- AI agents  
- offline mirrors  
- future renderers  

No renderer‑specific logic is required.

---

## **11. Zero‑Infrastructure Guarantee**
This standard requires:

- no backend  
- no API  
- no server  
- no authentication  
- no runtime  
- no dependencies  

It is **pure metadata**.

---

## **12. Example Implementation**
### **12.1 Directory**
```
/docs/my-module/
    README.md
    module.json
    examples.md
```

### **12.2 README**
```html
<link rel="rtt-module"
      href="https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/main/docs/my-module/module.json">
```

### **12.3 module.json**
```json
{
  "module": "My Module",
  "version": "1.0",
  "description": "Example RTT agentic module.",
  "roles": ["profile", "map"],
  "operators": ["substrate", "flow", "field"],
  "files": {
    "README.md": "profile",
    "examples.md": "map"
  }
}
```

---

## **13. Validation**
A module is considered **RTT‑Agentic‑Ready** when:

- `module.json` exists  
- absolute URL resolves  
- operator grammar is declared  
- file roles are mapped  
- README exposes the metadata  

---

## **14. Canonical Invariants**
This standard is:

- **substrate‑agnostic**  
- **domain‑agnostic**  
- **renderer‑agnostic**  
- **future‑proof**  
- **drift‑resistant**  
- **triadic‑aligned**  

It is the minimal contract required for agentic behavior.

---

## **15. Versioning**
This is **RTT Agentic Metadata Standard v1.0**.  
Future versions will extend but never break the canonical minimal schema.
