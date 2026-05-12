# **Add RTT to Your GitHub Repo**  
### *A minimal, zero‑infrastructure way to make your documentation AI‑ready*

RTT provides a **tiny metadata layer** that makes any GitHub repository:

- easier for AI tools to understand  
- easier for documentation engines (like Docsbook.io) to render  
- more structured, more navigable, and more self‑describing  
- agentic without requiring servers, APIs, or hosting  

This guide shows you how to add RTT to your repo in **under 60 seconds**.

---

# **1. Create a `module.json` file**

Inside your documentation folder (or any module folder), add:

```
module.json
```

Example directory:

```
/docs
  /my-module
    README.md
    module.json
```

---

# **2. Add this minimal metadata**

Paste this into `module.json`:

```json
{
  "module": "My Module",
  "version": "1.0",
  "description": "Short description of what this module provides.",
  "roles": ["profile", "map"],
  "operators": ["substrate", "flow", "field"],
  "files": {
    "README.md": "profile"
  }
}
```

This is the smallest valid RTT metadata block.

---

# **3. Link your metadata from your README**

Add this line at the top (or bottom) of your module’s README.md:

```html
<link rel="rtt-module"
      href="https://raw.githubusercontent.com/<user>/<repo>/main/<path>/module.json">
```

Replace `<user>`, `<repo>`, and `<path>` with your repo details.

This is the **activation surface**.  
It tells AI tools and documentation renderers where your metadata lives.

---

# **4. Use absolute paths for metadata**

Your `module.json` link **must** use an absolute URL:

```
https://raw.githubusercontent.com/<user>/<repo>/main/docs/my-module/module.json
```

This ensures:

- AI agents can load your metadata  
- Docsbook.io can resolve it  
- GitHub Pages can resolve it  
- mirrors and forks still work  

---

# **5. Use relative paths for everything else**

Inside your documentation:

- links to other pages  
- examples  
- diagrams  
- maps  
- references  

…should stay **relative**.

This keeps your repo portable across:

- GitHub  
- GitHub Pages  
- Docsbook.io  
- offline mirrors  
- future renderers  

---

# **6. That’s it — your repo is now RTT‑enabled**

You now have:

- a machine‑readable module identity  
- a portable metadata contract  
- a renderer‑agnostic structure  
- a zero‑infrastructure agentic layer  
- AI‑friendly documentation  

No servers.  
No APIs.  
No backend.  
Just metadata.

---

# **7. Optional: Expand your metadata**

You can add more structure later:

- `analyzer_layer`  
- `lineage`  
- `regime`  
- `crosslinks`  
- `signature`  
- `diagnostic`  

But the minimal version above is enough to activate RTT.

---

# **8. Example: A complete minimal module**

### Directory
```
/docs/tutorial/
    README.md
    module.json
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

---

# **9. Why developers use RTT**

Because it gives them:

- **structure**  
- **discoverability**  
- **AI‑readability**  
- **cross‑renderer stability**  
- **zero drift**  
- **zero overhead**  

It’s the smallest possible step that makes a repo feel like a real documentation system.
