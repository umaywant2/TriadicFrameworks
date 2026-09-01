# 🧬 WEEKLY_CHECKINS — Lineage & Drift Audit Subsystem

The **Weekly Check‑In System** is the automated heartbeat of the TriadicFrameworks canon.  
Every Sunday, a GitHub Actions workflow generates a timestamped snapshot of the repository’s structural state, enabling long‑term coherence, drift detection, and defensive publication.

---

## 📅 What the Weekly Workflow Produces

Each run creates a new folder:

```
/docs/WEEKLY_CHECKINS/YYYY-MM-DD/
```

Inside each dated folder, the workflow writes:

### **1. Lineage Snapshot**
A frozen view of the repository at the moment of capture.  
Used for ancestry tracking, module genealogy, and long‑term coherence studies.

### **2. Drift Notes**
Internal notes documenting:
- semantic drift  
- operator drift  
- structural drift  
- module‑level anomalies  

These support RTT’s drift‑awareness and coherence‑preservation mechanisms.

### **3. Module‑Activity Diff**
A diff of all module changes since the previous week:
- added files  
- removed files  
- modified operators  
- metadata updates  

This enables weekly structural auditing.

### **4. Defensive‑Publication Reminder**
A prompt to ensure critical modules have:
- public mirrors  
- redundancy  
- updated metadata  
- external archival  

This prevents knowledge loss and maintains the canon’s indestructibility.

---

## 🧭 Purpose of This Subsystem

The Weekly Check‑In System ensures:

- **Temporal coherence** across the entire canon  
- **Versioned ancestry** for every module  
- **Automatic drift detection**  
- **Long‑term preservation** of structural knowledge  
- **Operational continuity** for TriadicFrameworks  

It is the modern equivalent of a self‑maintaining Library of Alexandria — distributed, versioned, and impossible to burn.

---

## ⚙️ Workflow Location

The automation is defined at:

```
.github/workflows/weekly-checkin.yml
```

It runs:
- **weekly (cron)**  
- **manually (workflow_dispatch)**  

---

## 📁 Folder Structure

```
docs/
└── WEEKLY_CHECKINS/
    ├── 2026-09-01/
    │   └── checkin.md
    ├── 2026-09-08/
    │   └── checkin.md
    └── ...
```

Each folder represents one “scroll” in the ongoing lineage archive.

---

## 🔒 Internal Use

This subsystem is **not user‑facing**.  
It exists to support:
- module maintenance  
- structural genealogy  
- drift calibration  
- defensive publication  
- long‑term canon stability  
