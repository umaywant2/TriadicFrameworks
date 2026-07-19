# UE6 Example Project — Folder Structure  
**RTT / Integrations / UE6 / ExampleProject**

This structure defines a minimal UE6 project demonstrating RTT operators, resonance fields, entropy boundaries, and hybrid behavior.

```
ExampleProject/
    Config/
    Content/
        RTT/
            Core/
                RTTComponent.uasset
                RTT_Primitives.uasset
            Examples/
                BP_RTT_Primitives.uasset
                BP_RTT_ResonanceDemo.uasset
                BP_RTT_EntropyDemo.uasset
                BP_RTT_HybridDemo.uasset
            Materials/
                M_RTT_ResonanceHeatmap.uasset
                M_RTT_EntropyField.uasset
            UI/
                WBP_RTT_Timeline.uasset
                WBP_RTT_OperatorPanel.uasset
        Maps/
            RTT_Showcase.umap
            RTT_ResonanceRoom.umap
            RTT_EntropyField.umap
    Plugins/
        RTTUE6/
            Source/
            Resources/
    Scripts/
        RTTTools.py
        RTT_ResonanceVisualizer.py
        RTT_EntropyInspector.py
        RTT_OperatorTimeline.py
        RTT_MenuExtension.py
    README.md
```

### Highlights
- **RTT/Core** → C++ bindings + primitive Blueprint  
- **RTT/Examples** → ready‑to‑run operator demos  
- **RTT/Materials** → resonance + entropy visualization shaders  
- **RTT/UI** → editor + runtime widgets  
- **Maps** → curated scenes for φ–V–R, entropy, hybrid operators  
- **Scripts** → all editor utilities in one place  

This structure is **AI‑parsable**, **student‑ready**, and **zero‑drift**.
