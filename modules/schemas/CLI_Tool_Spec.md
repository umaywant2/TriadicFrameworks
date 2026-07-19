# 🛠️ **2. CLI Tool Spec — `rtt-schema`**  
*A command‑line validator for the entire schema universe.*

This spec defines a CLI tool you can implement in Python, Rust, Go, or Node.

---

# 📦 **Tool Name**
```
rtt-schema
```

# 🎯 **Purpose**
Validate, explore, and analyze the TriadicFrameworks schema universe.

---

# 🧩 **Commands**

## 1. `rtt-schema validate`
Validates:

- JSON syntax  
- Schema structure  
- Cross‑domain dependencies  
- Manifest completeness  
- Orphan schemas  
- Missing references  

**Example:**
```
rtt-schema validate
```

**Output:**
```
✔  184 schemas loaded
✔  Manifest version 1.0.0
✔  All schemas valid
✔  No missing dependencies
✔  Universe integrity: PASS
```

---

## 2. `rtt-schema tree`
Displays the domain → schema tree.

```
rtt-schema tree
```

Output:
```
canon/
  - canon_entry.schema.json
  - universe_definition.schema.json
dimensional/
  - dimensional_layer.schema.json
  - resonance_interface.schema.json
...
```

---

## 3. `rtt-schema info <schema>`
Shows details for a specific schema.

```
rtt-schema info quantum_state
```

Output:
```
Schema: quantum_state.schema.json
Domain: quantum
Fields:
  - state_id: string
  - basis: string
  - amplitudes: object
Dependencies:
  - dimensional_layer
Used by:
  - quantum_event
```

---

## 4. `rtt-schema deps <schema>`
Shows dependency graph for a schema.

```
rtt-schema deps coeus_contract
```

Output:
```
coeus_contract
  ├── state_model
  ├── operator
  └── resonance_constraints
```

---

## 5. `rtt-schema graph`
Generates a DOT/JSON graph of the entire universe.

```
rtt-schema graph --format=dot > universe.dot
```

---

## 6. `rtt-schema search <term>`
Searches schema names and descriptions.

```
rtt-schema search quantum
```

---

## 7. `rtt-schema manifest`
Prints the manifest in a pretty format.

---

# 🔧 **Configuration File**
Optional `.rttschema.json`:

```json
{
  "schemaRoot": "docs/schemas",
  "manifest": "docs/schemas/schema-manifest.json",
  "output": "build/schema"
}
```

---

# 🧠 **Why this CLI matters**

It gives you:

- **Universe integrity checks**  
- **Cross‑domain validation**  
- **Schema discovery**  
- **Dependency visualization**  
- **Tooling for future contributors**  

This is how TriadicFrameworks becomes a *platform*, not just a repository.
