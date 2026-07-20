# 📘 **RTTcodes for archive_org**  
### *RTT/1‑Aligned Operator Packets for the Internet Archive Gateway*

This directory contains the **RTTcode v1 operator packets** and **example packets** used by the `archive_org` module.  
These packets define how both **students** and **AI agents** interact with the Internet Archive in a **drift‑bounded**, **continuity‑aligned**, **substrate‑aware** way.

The Internet Archive is a massive time‑layered memory substrate.  
RTT provides the **operator grammar** that makes it navigable.

---

# 🧩 Operator Set (RTT/1)

The Internet Archive gateway uses **six operators**, each defined as an RTTcode v1 packet:

| Operator | Family | Purpose |
|---------|--------|---------|
| **WAYBACK_OPERATOR** | T‑Ops | Time‑indexed continuity + drift detection |
| **METADATA_OPERATOR** | R‑Ops | Normalize IA metadata into RTT grammar |
| **LINEAGE_OPERATOR** | L‑Ops | Build continuity kernel + lineage graph |
| **COLLECTION_OPERATOR** | E‑Ops | Construct dimensional envelope |
| **PRESERVATION_OPERATOR** | B‑Ops | Substrate stability + boundary detection |
| **DRIFTBOUND_RETRIEVAL_OPERATOR** | C‑Ops | Final synthesis + drift‑bounded retrieval |

Each operator has:

- strict inputs  
- strict outputs  
- drift rules  
- continuity rules  
- substrate rules  

All packets are **schema‑valid** under `rttcode.v1.json`.

---

# 🔁 Agentic Workflow (Full Chain)

Every retrieval from the Internet Archive must pass through the full operator chain:

1. **METADATA_OPERATOR**  
2. **WAYBACK_OPERATOR**  
3. **LINEAGE_OPERATOR**  
4. **COLLECTION_OPERATOR**  
5. **PRESERVATION_OPERATOR**  
6. **DRIFTBOUND_RETRIEVAL_OPERATOR**

This ensures:

- no direct content reasoning  
- drift is always measured  
- lineage is always preferred  
- substrate is always respected  
- continuity is always explicit  

This is the **RTT/1 safety boundary** for agentic use of archive.org.

---

# 📦 Operator Packets

The following RTTcode packets define the operators:

```
RTT_WAYBACK_OPERATOR_v1.json
RTT_METADATA_OPERATOR_v1.json
RTT_LINEAGE_OPERATOR_v1.json
RTT_COLLECTION_OPERATOR_v1.json
RTT_PRESERVATION_OPERATOR_v1.json
RTT_DRIFTBOUND_RETRIEVAL_OPERATOR_v1.json
```

Each packet is:

- minimal  
- schema‑valid  
- drift‑bounded  
- ready for use by AIs and students  

---

# 🧪 Example Packets (Full Runs)

Three complete examples demonstrate the **entire six‑operator chain** applied to real Internet Archive collections:

```
RTT_EXAMPLE_ARCHIVE_ORG_government_documents_v1.json
RTT_EXAMPLE_ARCHIVE_ORG_vintagesoftware_v1.json
RTT_EXAMPLE_ARCHIVE_ORG_journals_v1.json
```

Each example includes:

- metadata normalization  
- snapshot retrieval  
- drift mapping  
- continuity kernel  
- envelope construction  
- substrate profile  
- final drift‑bounded summary  

These examples are ideal for:

- student learning  
- AI testing  
- operator debugging  
- workflow validation  

---

# 🎓 How Students Use These Packets

Students can:

- inspect each operator’s inputs/outputs  
- follow the continuity chain  
- see drift and substrate warnings  
- compare stable vs unstable snapshots  
- understand how IA objects evolve over time  

This directory is part of the **teaching substrate** for RTT.

---

# 🤖 How AIs Use These Packets

AIs use these packets as:

- **contracts** (I/O rules)  
- **safety boundaries** (drift, substrate, lineage)  
- **workflow steps** (operator order)  
- **validation tools** (schema‑checked)  

No agent may bypass the operator chain.

---

# 📍 Location

This file lives at:

```
/docs/archive_org/RTTcodes/README.md
```

and is part of the **archive_org** module.
