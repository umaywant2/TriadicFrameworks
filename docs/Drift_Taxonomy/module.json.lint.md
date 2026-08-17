# module.json Lint Rules

These lint rules ensure consistency across all TriadicFrameworks modules.

---

## 1. Required Top-Level Fields
Every module.json MUST contain:

- `module`
- `roles`
- `analyzer_layer`
- `files`
- `ai`
- `citation`

---

## 2. Module Block Rules
- `module.name` MUST be unique across the repo.
- `module.version` MUST follow semantic versioning: `MAJOR.MINOR.PATCH`.
- `module.summary` MUST be one sentence.
- `module.purpose` MUST be one paragraph.
- `module.keywords` SHOULD contain 5–12 items.

---

## 3. Roles Block Rules
- `engine`, `profile`, `signature`, `diagnostic`, `map`, `example`, `index` MUST exist.
- Roles MUST describe the function of files in this module.
- Roles SHOULD NOT duplicate each other.

---

## 4. Analyzer Layer Rules
- `operator` MUST list all operator families used in this module.
- `drift` MUST list all drift types defined in d_Capture.md.
- `regime` MUST match the regime tags used in d_Classify.md.
- `dimensional` MUST include macro, micro, hybrid, cosmic, extreme-curvature.

---

## 5. Files Block Rules
- All file paths MUST exist in the directory.
- `README` MUST point to `README.md`.

---

## 6. AI Metadata Rules
- `ai.module` MUST match `module.name`.
- `ai.version` MUST match `module.version`.
- `ai.license` MUST be “Open educational use permitted”.

---

## 7. Citation Rules
- `citation.author` MUST be the module’s primary author.
- `citation.publication_date` MUST be a year.
- `citation.title` MUST match the module’s identity.

---

## 8. Coherence Rules
- Drift types MUST match operator families.
- Examples MUST reference operators defined in d_Operators.md.
- Paper MUST reference examples from d_Examples.md.

---

## 9. Style Rules
- JSON MUST use 2-space indentation.
- Keys MUST use lower-case with hyphens only where needed.
- No trailing commas.

---

Following these lint rules ensures module.json files remain consistent across the TriadicFrameworks ecosystem.
