# 📘 **How to Read RTTcode (Student Guide)**  
### *Understanding RTTcode v1 packets for the Internet Archive Gateway*

RTTcode is a **minimal, structured, machine‑readable format** used across TriadicFrameworks to describe:

- operators  
- workflows  
- continuity  
- drift  
- substrate behavior  
- lineage  
- examples  

This guide teaches you how to read RTTcode packets, especially the ones used in the **archive_org** module.

---

# 🧩 1. What an RTTcode Packet *Is*

An RTTcode packet is:

- a **JSON document**  
- validated by the RTTcode v1 schema  
- containing **strict fields**  
- describing an **operator**, **workflow**, or **example**  

RTTcode is intentionally:

- minimal  
- explicit  
- drift‑bounded  
- easy for students and AIs to read  

---

# 🧱 2. The Basic Structure

Every RTTcode packet has these top‑level fields:

```json
{
  "$schema": "…/rttcode.v1.json",
  "id": "RTT_SOMETHING_v1",
  "version": "1.0",
  "type": "operator | example | workflow",
  "name": "…",
  "target": "… (if example)",
  "operators": { … }  // if example
}
```

### Key ideas:

- **`$schema`** tells tools how to validate the packet.  
- **`id`** is the canonical name.  
- **`type`** tells you what kind of RTTcode this is.  
- **`operators`** appears only in *example* packets.  

---

# 🧠 3. Reading an Operator Packet

Operator packets define:

- what the operator does  
- what it takes in  
- what it outputs  
- what constraints it must obey  

Example (simplified):

```json
{
  "type": "operator",
  "family": "T-Ops",
  "name": "WAYBACK_OPERATOR",
  "inputs": { … },
  "outputs": { … },
  "constraints": { … }
}
```

### How to read this:

- **family** tells you the operator’s “role” in RTT.  
- **inputs** tells you what data it needs.  
- **outputs** tells you what it produces.  
- **constraints** tell you the safety rules.  

For example:

- T‑Ops = time operators  
- R‑Ops = relation/metadata  
- L‑Ops = lineage  
- E‑Ops = envelope  
- B‑Ops = boundary/substrate  
- C‑Ops = coherence/synthesis  

---

# 🔁 4. Reading a Full Example Packet

Example packets show **all six operators chained** for a real Internet Archive URL.

Inside an example packet:

```json
"operators": {
  "METADATA_OPERATOR": { … },
  "WAYBACK_OPERATOR": { … },
  "LINEAGE_OPERATOR": { … },
  "COLLECTION_OPERATOR": { … },
  "PRESERVATION_OPERATOR": { … },
  "DRIFTBOUND_RETRIEVAL_OPERATOR": { … }
}
```

Each operator block shows:

- what the operator *saw*  
- what it *computed*  
- what it *warned about*  
- what it *passed forward*  

This is the **agentic workflow** in action.

---

# 🧭 5. How the Six Operators Fit Together

RTT always processes Internet Archive objects in this order:

1. **METADATA_OPERATOR**  
2. **WAYBACK_OPERATOR**  
3. **LINEAGE_OPERATOR**  
4. **COLLECTION_OPERATOR**  
5. **PRESERVATION_OPERATOR**  
6. **DRIFTBOUND_RETRIEVAL_OPERATOR**  

This ensures:

- drift is measured  
- continuity is explicit  
- substrate is respected  
- lineage is preserved  
- the final answer is safe  

If an RTTcode example includes all six, it represents a **complete run**.

---

# 📚 6. How to Interpret the Outputs

### **Snapshots**
From WAYBACK_OPERATOR:

- timestamps  
- URIs  
- drift between versions  
- continuity breaks  

### **Lineage**
From LINEAGE_OPERATOR:

- how versions relate  
- what changed  
- regime shifts  

### **Envelope**
From COLLECTION_OPERATOR:

- what collection it belongs to  
- coherence clusters  
- related objects  

### **Substrate**
From PRESERVATION_OPERATOR:

- format  
- stability  
- drift risk  

### **Final Answer**
From DRIFTBOUND_RETRIEVAL_OPERATOR:

- summary  
- earliest stable version  
- most reliable version  
- key changes  
- warnings  

This is the **student‑safe output**.

---

# 🧪 7. How to Use the Example Packets

The three example packets in this directory show:

- Government Documents  
- Vintage Software  
- Journals  

Each one demonstrates:

- how drift is detected  
- how continuity is mapped  
- how substrate affects reliability  
- how the final answer is synthesized  

Students can:

- compare stable vs unstable collections  
- see how metadata affects reasoning  
- understand why some snapshots drift  
- learn how IA objects evolve over time  

---

# 🎓 8. Why RTTcode Matters

RTTcode gives you:

- a **clear grammar** for complex systems  
- a **safe way** to explore the Internet Archive  
- a **structured method** for understanding drift  
- a **continuity‑first mindset**  
- a **substrate‑aware approach** to digital history  

It turns the Internet Archive into a **teaching substrate**, not just a search box.

---

# 📍 Location

This guide belongs at:

```
/docs/archive_org/RTTcodes/README.md
```

or

```
/docs/archive_org/RTTcodes/how_to_read_rttcode.md
```

Either location is canon‑correct.
