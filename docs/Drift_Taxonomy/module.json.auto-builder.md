# module.json Auto‑Builder — Usage Guide

The auto‑builder provides a reusable template for creating new TriadicFrameworks
module.json files. It ensures consistency across modules and reduces manual
metadata work.

---

## 1. How to Use the Auto‑Builder

1. Copy the JSON object from `module.json.auto-builder`.
2. Replace all placeholder fields:
   - `<MODULE_NAME>`
   - `<CATEGORY>`
   - `<ONE_SENTENCE_SUMMARY>`
   - `<ONE_PARAGRAPH_PURPOSE>`
   - `<KW1>`, `<KW2>`, `<KW3>`
   - `<TARGET_AUDIENCE>`
   - `<OPERATOR_1>`, `<OPERATOR_2>`
   - `<REGIME_1>`, `<REGIME_2>`
   - `<DRIFT_1>`, `<DRIFT_2>`
   - `<AUTHOR_NAME>`
   - `<YEAR>`
   - `<MODULE_TITLE>`
   - `<SUBJECT>`
3. Ensure file paths match the actual directory structure.
4. Validate the result using `module.schema.json`.
5. Run lint checks using `module.json.lint.md`.

---

## 2. Required Fields

Every generated module.json MUST include:

- `module`
- `roles`
- `analyzer_layer`
- `files`
- `ai`
- `citation`

These are enforced by the schema and lint rules.

---

## 3. Recommended Workflow

1. **Start with the auto‑builder template.**
2. **Fill in module identity fields first** (name, category, summary).
3. **Define roles** based on the module’s purpose.
4. **Add analyzer layers** only after the module’s conceptual structure is clear.
5. **Map files** once the directory is created.
6. **Add AI metadata** last.
7. **Validate** using the schema.
8. **Lint** using the lint rules.

---

## 4. Common Mistakes

- Forgetting to update `ai.module` to match `module.name`.
- Using non‑semantic versioning (must be `X.Y.Z`).
- Missing required roles (engine, profile, signature, diagnostic, map, example, index).
- Incorrect file paths.
- Leaving placeholder fields in the final JSON.

---

## 5. Best Practices

- Keep summaries short.
- Keep purposes descriptive.
- Use consistent terminology across modules.
- Reuse operator families and drift types where applicable.
- Validate early and often.

---

Using this auto‑builder ensures every module in TriadicFrameworks remains coherent, discoverable, and AI‑ready.
