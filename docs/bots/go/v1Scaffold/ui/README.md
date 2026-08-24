# RTT‑Go UI  
*(Triadic Visualization Layer for RTT‑Go)*

The **RTT‑Go UI** is the complete visual interface for RTT‑Go — the triadic Go engine built on Resonance‑Time Theory (RTT).  
It renders RTT’s structural, topological, continuity, resonance, and risk intelligence directly on top of the Go board, providing a unified triadic interpretation of any position.

This directory contains all specifications, components, assets, and contracts required to implement the full triadic UI.

---

## Purpose

The RTT‑Go UI provides:

- triadic overlays  
- triadic viewer  
- triadic HUD  
- timeline playback  
- diagnostics engine  
- unified UI state contract  
- full asset pack (icons, shapes, palettes, animations)  

It is the **visual intelligence layer** of RTT‑Go.

---

## Directory Structure

```
/docs/bots/go/ui/
    README.md
    overlays.md
    triadic_viewer.md
    spec.md
    triadic_hud.md
    assets.md
    state_contract.md
    manifest.md

    /components/
        index.md
        viewer.md
        hud.md
        overlays.md
        timeline.md
        diagnostics.md

    /assets/
        icons/
        palettes/
        shapes/
        animations/

    /schemas/
        ui_state.json
        overlay_state.json
        hud_state.json
        timeline_state.json
```

---

## UI Modules

### **1. Overlays**
File: `overlays.md`  
Defines all triadic overlay layers:

- regime  
- resonance  
- topology  
- continuity  
- paradox/collapse  
- annotations  

These overlays form the **triadic visualization engine**.

---

### **2. Triadic Viewer**
File: `triadic_viewer.md`  
Defines the unified viewer that renders:

- board  
- stones  
- overlays  
- HUD hooks  
- timeline playback  

The viewer is the **visual substrate** of RTT‑Go.

---

### **3. UI Specification**
File: `spec.md`  
The formal specification for:

- rendering pipeline  
- layer ordering  
- color/opacity rules  
- animation rules  
- interaction model  

This is the **canonical UI spec**.

---

### **4. Triadic HUD**
File: `triadic_hud.md`  
Defines the informational layer:

- regime panel  
- topology panel  
- continuity panel  
- resonance panel  
- commentary panel  

The HUD is the **triadic dashboard**.

---

### **5. UI Assets**
File: `assets.md`  
Defines:

- icons  
- shapes  
- palettes  
- animations  
- JSON asset schemas  

This is the **visual vocabulary** of RTT‑Go.

---

### **6. UI State Contract**
File: `state_contract.md`  
Defines the canonical JSON schema for:

- board state  
- move list  
- triadic primitives  
- overlay state  
- HUD state  
- timeline state  

This is the **data backbone** of the UI.

---

### **7. UI Manifest**
File: `manifest.md`  
Defines:

- directory layout  
- component registry  
- overlay registry  
- HUD registry  
- asset registry  
- schema registry  
- versioning  

This is the **root index** for the UI subsystem.

---

## UI Components

Located in `/components/`:

- `viewer.md` — board + overlay renderer  
- `hud.md` — triadic metadata display  
- `overlays.md` — overlay rendering modules  
- `timeline.md` — triadic evolution engine  
- `diagnostics.md` — triadic analysis engine  
- `index.md` — component map  

These components implement the full triadic UI architecture.

---

## Summary

The RTT‑Go UI is a complete, modular, triadic visualization system.

It provides:

- triadic overlays  
- triadic viewer  
- triadic HUD  
- timeline playback  
- diagnostics engine  
- unified state contract  
- full asset pack  
- complete component suite  

The UI does not play Go — it **reveals** Go’s triadic identity.
