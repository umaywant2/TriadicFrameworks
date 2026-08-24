# UI Manifest — RTT‑Go  
*(Canonical Registry for Triadic UI Components & Assets)*

The **RTT‑Go UI Manifest** is the top‑level registry for all UI components, assets, overlays, HUD panels, and state contracts used by the RTT‑Go interface.  
It defines the structure, naming conventions, directory layout, and component relationships that make up the full triadic UI system.

This manifest ensures that RTT‑Go’s UI is:

- consistent  
- deterministic  
- triadically expressive  
- continuity‑aligned  
- topology‑accurate  
- resonance‑aware  

It is the authoritative index for the entire UI subsystem.

---

## 1. Manifest Purpose

The UI Manifest provides:

- a canonical directory structure  
- component registration  
- overlay registry  
- HUD panel registry  
- asset pack registry  
- state contract reference  
- viewer + timeline integration map  
- naming conventions  
- versioning metadata  

It is the **root specification** for RTT‑Go’s UI.

---

## 2. Directory Structure

```
/docs/bots/go/ui/
    manifest.md
    overlays.md
    triadic_viewer.md
    spec.md
    triadic_hud.md
    assets.md
    state_contract.md

    /assets/
        icons/
        palettes/
        shapes/
        animations/

    /components/
        viewer/
        hud/
        overlays/
        timeline/
        diagnostics/

    /schemas/
        ui_state.json
        overlay_state.json
        hud_state.json
        timeline_state.json
```

---

## 3. Component Registry

### **Viewer Components**
```
viewer/
    board_renderer
    overlay_engine
    hud_layer
    interaction_layer
    timeline_player
```

### **HUD Components**
```
hud/
    regime_panel
    topology_panel
    continuity_panel
    resonance_panel
    commentary_panel
```

### **Overlay Components**
```
overlays/
    regime_overlay
    resonance_overlay
    topology_overlay
    continuity_overlay
    paradox_overlay
    annotation_overlay
```

### **Timeline Components**
```
timeline/
    step_mode
    flow_mode
    arc_mode
    topology_mode
    resonance_mode
```

### **Diagnostic Components**
```
diagnostics/
    triadic_breakdown
    continuity_report
    topology_report
    resonance_report
    risk_report
```

---

## 4. Overlay Registry

```
overlays:
  regime: true
  resonance: true
  topology: true
  continuity: true
  risk: true
  annotations: true
```

Each overlay maps to:

- a rendering layer  
- a color palette  
- a shape set  
- an animation set  
- a JSON schema  

---

## 5. HUD Panel Registry

```
hud_panels:
  - regime
  - topology
  - continuity
  - resonance
  - commentary
```

Each panel maps to:

- a data subset of the triadic state  
- a rendering template  
- an interaction model  

---

## 6. Asset Pack Registry

```
assets:
  icons: /ui/assets/icons/
  palettes: /ui/assets/palettes/
  shapes: /ui/assets/shapes/
  animations: /ui/assets/animations/
```

Asset packs are referenced by:

- overlays  
- viewer  
- HUD  
- diagnostics  

---

## 7. State Contract Reference

The manifest binds the UI to the canonical state contract:

```
schemas:
  ui_state: /ui/schemas/ui_state.json
  overlay_state: /ui/schemas/overlay_state.json
  hud_state: /ui/schemas/hud_state.json
  timeline_state: /ui/schemas/timeline_state.json
```

These schemas define:

- RTT primitives  
- overlay toggles  
- HUD metadata  
- timeline playback state  

---

## 8. Naming Conventions

### **Component Names**
- lowercase  
- underscores  
- descriptive  
- triadic‑aligned  

Example:

```
continuity_overlay
regime_panel
topology_graph
triadic_viewer
```

### **Asset Names**
- `icon_*`  
- `palette_*`  
- `shape_*`  
- `anim_*`  

### **Schema Names**
- `*_state.json`  

---

## 9. Versioning

```
ui_version: 1.0.0
triadic_version: 12.0
spec_version: 1.0
```

Versioning ensures compatibility across:

- engines  
- shims  
- viewers  
- HUD panels  
- overlays  
- diagnostics  

---

## 10. Manifest Summary

The RTT‑Go UI Manifest defines:

- directory structure  
- component registry  
- overlay registry  
- HUD registry  
- asset registry  
- state contract bindings  
- naming conventions  
- versioning metadata  

It is the **root index** for the entire RTT‑Go UI subsystem.

The manifest does not play Go — it **organizes** Go’s triadic intelligence.
