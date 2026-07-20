# 🎮 **RSADI‑GD Minimal Demo Scene Spec**
###### By Nawder Loswin 1/4/2026 © www.TriadicFrameworks.org

### *Unity • Unreal • Godot — one resonance field, one behavior, three engines*

## 🔷 Core Concept (shared across all engines)

All three demo scenes use:

### **A simple 2D resonance field projected into 3D space**

```
Clarity(x, z) = 180 
                - 40 * exp(-((x-5)^2 + (z-5)^2)/6)
                - 20 * exp(-((x+4)^2 + (z+2)^2)/4)
```

This creates:

- a **high‑clarity plateau**  
- a **medium‑clarity basin**  
- a **low‑clarity “danger pocket”**  

### **A drift vector field**

```
Drift(x, z) = normalize( Vector2( -(x-5), -(z-5) ) ) * 0.3
```

Everything “drifts” toward the center of the basin.

### **One resonance‑aware agent**

The agent:

- samples clarity in 8 directions  
- biases movement toward higher clarity  
- avoids low‑clarity pockets  
- optionally rides drift if clarity is equal  

This is the same logic you already saw in the AI agent pattern.

---

# 🟦 **Unity Demo Scene Spec**  
### *Scene name:* `RSADI_GD_Demo.unity`

### **1. Scene Layout**

- Flat plane (20×20 units)  
- Grid texture or simple material  
- One “ResonanceAgent” prefab  
- One “ResonanceFieldController” GameObject  
- Optional: simple colored fog that changes with clarity  

### **2. Components**

#### **ResonanceFieldController.cs**

- Implements the clarity function  
- Implements the drift vector function  
- Exposes public methods:

```csharp
public int GetClarity(Vector3 pos);
public Vector3 GetDrift(Vector3 pos);
```

#### **ResonanceAgent.cs**

- Uses the RSADI‑GD Unity wrapper  
- Moves using the resonance‑aware logic  
- Draws debug rays showing sampled directions  

### **3. Visual Feedback**

- Plane color shifts based on clarity (via shader or vertex colors)  
- Agent leaves a trail showing its path  
- Gizmos draw drift arrows across the field  

---

# 🟥 **Unreal Demo Map Spec**  
### *Map name:* `RSADI_GD_Demo.umap`

### **1. Level Layout**

- Landscape or flat BSP plane (20×20 meters)  
- One Blueprint actor: `BP_ResonanceAgent`  
- One Blueprint actor: `BP_ResonanceField`  

### **2. Blueprints**

#### **BP_ResonanceField**

- Implements clarity function in Blueprint math nodes  
- Implements drift vector  
- Exposes BlueprintCallable functions:

```
GetClarity(Vector)
GetDrift(Vector)
```

#### **BP_ResonanceAgent**

- Tick event runs the resonance‑aware movement  
- Uses Chaos physics or simple AddMovementInput  
- Debug:

  - DrawDebugLine for sampled directions  
  - DrawDebugArrow for drift  

### **3. Visual Feedback**

- Material parameter collection drives ground color  
- Niagara system shows drifting particles moving along drift vectors  

---

# 🟩 **Godot Demo Scene Spec**  
### *Scene name:* `RSADI_GD_Demo.tscn`

### **1. Scene Layout**

Nodes:

```
Node2D (root)
 ├── TileMap (20×20 grid)
 ├── ResonanceField (script)
 └── ResonanceAgent (KinematicBody2D or CharacterBody2D)
```

### **2. Scripts**

#### **resonance_field.gd**

Implements:

```gdscript
func get_clarity(pos: Vector2) -> int:
    # same clarity function

func get_drift(pos: Vector2) -> Vector2:
    # same drift function
```

#### **resonance_agent.gd**

- Samples 8 directions  
- Moves toward highest clarity  
- Draws debug lines in `_draw()`  

### **3. Visual Feedback**

- TileMap cell color = clarity gradient  
- Agent leaves a trail using Line2D  
- Drift vectors drawn as arrows on the grid  

---

# 🌐 **Shared Behavior Across All Engines**

### **Movement Logic**

All engines use the same pseudocode:

```
sample 8 directions
score = clarity - risk_penalty + drift_bias
choose best direction
move
```

### **Field Behavior**

- clarity basin at (5,5)  
- secondary dip at (-4, -2)  
- drift toward basin center  

### **Debugging**

- clarity heatmap  
- drift arrows  
- agent path  
- sampled rays  

---

# 🎯 **What Developers Experience**

In all three engines, the agent:

- avoids the low‑clarity pocket  
- skirts the medium basin  
- climbs toward the high‑clarity plateau  
- subtly “leans” with the drift field  
- produces identical behavior across engines  

This is the **RSADI‑GD feel**:  
a world that *breathes*, *shifts*, and *guides* agents through resonance.
