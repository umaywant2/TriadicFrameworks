# RTT Absolute `module.json` Identity Specification  
### Version 1.0 — Canon‑Locked Protocol

---

## 1. Purpose

This specification defines the **absolute identity protocol** for RTT `module.json` files.

Its goals:

- **Guarantee global resolvability** of module metadata  
- **Enable cross‑substrate agentic behavior** (GitHub, Docsbook.io, mirrors, etc.)  
- **Prevent drift** caused by renderer‑relative paths  
- **Lock in a canonical identity surface** for all RTT modules  

This spec is **normative** for all RTT‑aligned modules.

---

## 2. Identity Object

Each RTT module exposes a single **identity object**:

- File name: `module.json`  
- Location: inside the module’s directory (e.g. `/docs/ai/`, `/docs/Structural_Detection/`)  
- Access: via a **canonical absolute URL** to the raw file

Example identity URL:

```text
https://raw.githubusercontent.com/<user>/<repo>/main/docs/My_Module/module.json
```

This URL is the **canonical identity** of the module.

---

## 3. Absolute URL Requirement

### 3.1 Normative Rule

All RTT `module.json` references used for **agentic behavior** MUST be:

- **absolute URLs**
- pointing to the **raw content**
- stable across renderers and hosts

Form:

```text
https://raw.githubusercontent.com/<user>/<repo>/main/<path>/module.json
```

### 3.2 Rationale

Absolute URLs:

- decouple metadata from any specific renderer  
- ensure AI agents can always dereference the module  
- prevent path resolution errors in foreign substrates  
- make the module a **portable service descriptor**  

Relative paths (e.g. `./module.json`) MUST NOT be used for agentic metadata resolution.

---

## 4. Activation Surface (HTML Link Contract)

Modules expose their identity via a **link element** in their primary document (e.g. `README.md`, `index.html`):

```html
<!-- RTT Agentic Module Identity -->
<link rel="rtt-module"
      href="https://raw.githubusercontent.com/<user>/<repo>/main/<path>/module.json">
```

Normative requirements:

- `rel="rtt-module"` — fixed, reserved value  
- `href` — MUST be the canonical absolute URL to `module.json`  
- Only one primary identity link per module document SHOULD be present  

This is the **standard discovery mechanism** for RTT‑aware tools.

---

## 5. Canonical URL Shape

The canonical identity URL MUST conform to:

```text
https://raw.githubusercontent.com/<user>/<repo>/<branch>/<path>/module.json
```

Recommended defaults:

- `<branch>`: `main`  
- `<path>`: path from repo root to module directory  

Example:

```text
https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/main/docs/ai/ai_module.json
```

If a repository uses a different default branch, that branch name MUST be reflected in the URL.

---

## 6. Identity Invariants

For a `module.json` to be considered **identity‑stable**, the following invariants MUST hold:

1. **Single Canonical URL per module**  
   - A module may have mirrors, but one URL is designated canonical.

2. **Content Stability**  
   - Changes to `module.json` SHOULD be versioned via the `version` field.  
   - Breaking changes MUST increment the version appropriately.

3. **Location Stability**  
   - The path to `module.json` SHOULD NOT be moved casually.  
   - If moved, all `rel="rtt-module"` links MUST be updated.

4. **Renderer Independence**  
   - No renderer‑specific query parameters or host‑dependent paths are allowed in the canonical URL.

---

## 7. Relative vs Absolute Path Policy

To preserve cross‑substrate behavior:

- **Absolute paths**  
  - ONLY for `module.json` and other RTT metadata endpoints  
  - Used in `href` attributes for `rel="rtt-module"`

- **Relative paths**  
  - For all internal content links (markdown pages, examples, diagrams, etc.)  
  - Keeps documentation portable across hosts and themes  

This separation is **normative**:

- Metadata → absolute  
- Content → relative  

---

## 8. Minimal Identity Payload (Inside `module.json`)

The identity file MUST at least contain:

```json
{
  "module": "Module Name",
  "version": "1.0",
  "description": "Short description of the module.",
  "roles": ["profile"],
  "operators": ["substrate", "flow"],
  "files": {
    "README.md": "profile"
  }
}
```

Required fields:

- `module` — canonical module name  
- `version` — semantic version string  
- `description` — concise purpose  
- `roles` — RTT file‑role grammar  
- `operators` — RTT operator grammar  
- `files` — file‑to‑role mapping  

The **identity protocol** cares primarily that:

- the file exists  
- the absolute URL resolves  
- the JSON is valid  
- the required fields are present  

---

## 9. Cross‑Substrate Expectations

Any RTT‑aware tool (AI agent, renderer, validator) MAY:

1. Discover `module.json` via `rel="rtt-module"`  
2. Fetch the absolute URL  
3. Parse the JSON  
4. Use the identity to:

   - understand module purpose  
   - map files to roles  
   - reason about operators  
   - integrate the module into larger systems  

Tools MUST NOT assume:

- a specific host (GitHub, Docsbook.io, etc.)  
- a specific visual theme  
- a specific documentation engine  

Only the **absolute URL + JSON schema** are normative.

---

## 10. Compliance Checklist

A module is compliant with the **RTT Absolute `module.json` Identity** spec if:

- [ ] `module.json` exists in the module directory  
- [ ] A canonical absolute raw URL can be constructed  
- [ ] The primary document includes:

  ```html
  <link rel="rtt-module"
        href="https://raw.githubusercontent.com/<user>/<repo>/main/<path>/module.json">
  ```

- [ ] The URL resolves successfully  
- [ ] The JSON is valid and includes required fields  
- [ ] Internal content links remain relative  

---

## 11. Versioning

This is **RTT Absolute `module.json` Identity Specification v1.0**.

Future versions MAY:

- add optional fields  
- define additional discovery mechanisms  
- extend identity semantics  

They MUST NOT:

- break existing absolute URL behavior  
- invalidate compliant v1.0 modules  
