# **RTT + Docsbook Integration Standard**  
### *How to make your RTT metadata a first‑class citizen in Docsbook.io*

Docsbook.io automatically renders GitHub repositories as structured documentation.  
RTT adds a **machine‑readable metadata layer** that makes your modules:

- discoverable  
- indexable  
- agentic  
- cross‑linked  
- renderer‑agnostic  

This guide shows how to make RTT metadata work **optimally** inside Docsbook.io.

---

# **1. Use Absolute Raw URLs for `module.json`**

Docsbook.io runs your repo in a **foreign substrate**.  
Relative paths like:

```
./module.json
```

resolve incorrectly.

To ensure Docsbook can always load your metadata, use:

```text
https://raw.githubusercontent.com/<user>/<repo>/main/<path>/module.json
```

This is the **canonical identity URL**.

Docsbook treats this as a stable, fetchable endpoint.

---

# **2. Add the RTT Identity Link to Your README**

Docsbook scans HTML `<link>` tags in Markdown.

Add this to your module’s README.md or index.html:

```html
<link rel="rtt-module"
      href="https://raw.githubusercontent.com/<user>/<repo>/main/<path>/module.json">
```

Docsbook will:

- detect the RTT module  
- fetch the metadata  
- index the module  
- expose it to its AI assistant  
- surface it in its sidebar and search  

This is the activation surface.

---

# **3. Keep All Other Links Relative**

Docsbook mirrors your repo structure.

To preserve portability:

- **Relative links** → for content  
- **Absolute links** → only for metadata  

Examples of relative links Docsbook handles perfectly:

```
../examples.md
./operators.md
./maps/overview.md
```

This keeps your repo:

- theme‑agnostic  
- renderer‑agnostic  
- portable across domains  
- drift‑free  

---

# **4. Minimal Docsbook‑Optimized `module.json`**

Docsbook prefers small, clean metadata.

Here is the recommended minimal schema:

```json
{
  "module": "My Module",
  "version": "1.0",
  "description": "Short description of the module.",
  "roles": ["profile", "map"],
  "operators": ["substrate", "flow", "field"],
  "files": {
    "README.md": "profile"
  }
}
```

Docsbook uses this to:

- build its sidebar  
- categorize your module  
- expose metadata to its AI assistant  
- improve search relevance  
- maintain cross‑page coherence  

---

# **5. How Docsbook Uses RTT Metadata**

When Docsbook sees:

```html
<link rel="rtt-module" href="...">
```

…it performs:

### **5.1 Metadata Fetch**
Loads your `module.json` from the absolute URL.

### **5.2 Module Registration**
Adds your module to its internal registry.

### **5.3 Sidebar Integration**
Uses your module name + description to populate navigation.

### **5.4 AI Assistant Integration**
Makes your module:

- queryable  
- explainable  
- cross‑referencable  
- structurally interpretable  

### **5.5 Cross‑Page Linking**
Docsbook uses your `files` map to understand:

- which pages belong to the module  
- which roles they serve  
- how to group them  

---

# **6. Recommended Directory Layout**

Docsbook works best with:

```
/docs
  /My_Module
    README.md
    module.json
    examples.md
    operators.md
```

This mirrors TriadicFrameworks and ensures:

- clean sidebar grouping  
- predictable navigation  
- stable cross‑links  

---

# **7. Validation Checklist (Docsbook‑Specific)**

Your module is Docsbook‑optimized if:

- [ ] `module.json` exists  
- [ ] The README includes a `<link rel="rtt-module">` tag  
- [ ] The `href` uses an absolute raw URL  
- [ ] Docsbook sidebar shows your module name  
- [ ] Docsbook AI assistant can describe your module  
- [ ] All internal links remain relative  

If all six are true, your module is fully integrated.

---

# **8. Example: A Complete Docsbook‑Optimized Module**

### Directory
```
/docs/tutorial/
    README.md
    module.json
    examples.md
```

### README.md
```html
<link rel="rtt-module"
      href="https://raw.githubusercontent.com/example/repo/main/docs/tutorial/module.json">
```

### module.json
```json
{
  "module": "Tutorial",
  "version": "1.0",
  "description": "A simple example module.",
  "roles": ["profile"],
  "operators": ["substrate", "flow"],
  "files": {
    "README.md": "profile"
  }
}
```

Docsbook will:

- show “Tutorial” in the sidebar  
- index the module  
- expose it to its AI assistant  
- maintain stable navigation  

---

# **9. Why RTT + Docsbook Works So Well**

Because both systems are:

- static  
- metadata‑driven  
- renderer‑agnostic  
- zero‑infrastructure  
- cross‑substrate  
- drift‑resistant  

RTT provides the **structure**.  
Docsbook provides the **surface**.

Together they form a **portable agentic documentation ecosystem**.
