# 📦 3PAK Shell — profile.d
###### By Nawder Loswin 1/4/2026 © www.TriadicFrameworks.org

### TriadicFrameworks — tft‑3pack Environment Bootstrap

The **profile.d** directory contains initialization scripts that prepare the
3PAK environment whenever a shell session loads the 3PAK Shell.  
These scripts are lightweight, non‑intrusive, and designed to give developers
a clean, resonance‑aware workspace inside the tft‑3pack ecosystem.

This folder is part of the **3pak-shell**, the command‑line companion to the
TriadicFrameworks 3‑Pack runtime.

---

## 🧩 Purpose of `profile.d`

The scripts in this directory:

- set up environment variables for 3PAK  
- create local state directories  
- initialize logs  
- provide helper functions for developers  
- ensure the shell starts in a clean, triadic‑aligned state  

They are sourced automatically when the 3PAK Shell is activated.

---

## 📂 Included Script

### **`3pak.sh`**  
This is the primary initialization script for the 3PAK environment.

It provides:

- `THREEPAK_HOME` — local environment directory  
- `THREEPAK_STATE` — state file for notes and markers  
- `THREEPAK_LOG` — lightweight log file  
- helper functions:
  - `threepak_status` — show environment info  
  - `threepak_note` — append a note to state  
  - `threepak_clear` — reset state  
- a friendly startup message  
- a minimal logging helper  

This script is intentionally simple and safe, mirroring the philosophy of the
TriadicFrameworks overlays and shells.

---

## 🚀 How Developers Use the 3PAK Shell

Once the shell is activated, developers can:

```bash
threepak_status
threepak_note "Started a new session"
threepak_clear
```

## Quicklinks
- [3pak-shell README](https://www.triadicframeworks.org/packages/tft-3pack/3pak-shell/README.html)
- [tft primitive wrappers README](https://www.triadicframeworks.org/packages/tft-3pack/3pak-shell/tft_primitive_wrappers/README.html)
