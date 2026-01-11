# 📦 3PAK Shell
###### By Nawder Loswin 1/4/2026 © www.TriadicFrameworks.org

### TriadicFrameworks — tft‑3pack Command-Line Environment

The **3PAK Shell** provides a lightweight, resonance‑aware environment for
executing the three core TFT primitives and managing triadic workflows.

It is the command‑line companion to the tft‑3pack package.

---

## 🧩 What the Shell Provides

- environment initialization  
- state tracking  
- lightweight logging  
- primitive wrappers  
- profile.d startup scripts  
- a clean, triadic‑aligned workspace  

---

## 📂 Key Components

### **profile.d/**
Contains initialization scripts, including:

- `3pak.sh` — sets up environment variables and helper functions  

### **tft_primitive_wrappers/**
Contains shell wrappers for the three TFT primitives:

- `primitive1.sh`  
- `primitive2.sh`  
- `primitive3.sh`  

These wrappers call the primitives and record state markers.

### **install.sh**
Bootstraps the 3PAK environment.

---

## 🚀 Usage

```bash
primitive1.sh
primitive2.sh
primitive3.sh
threepak_status
