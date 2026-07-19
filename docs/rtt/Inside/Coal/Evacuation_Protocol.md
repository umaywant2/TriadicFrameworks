# 🛠️ **RTT‑Inside: Resonance‑Aware Evacuation Protocol**  
### *Using clarity gradients, drift vectors, and resonance fields to guide miners to safety*

---

# 1. **Core Principle: Follow the Clarity Gradient**

RTT‑Inside continuously computes a **clarity score (0–255)** for every zone:

- 🟢 **High clarity** → stable rock, clean air, low vibration  
- 🟡 **Medium clarity** → shifting conditions  
- 🟠 **Low clarity** → unstable, rising gas, high vibration  
- 🔴 **Negative clarity** → collapse likely, avoid immediately  

During an emergency, miners don’t follow maps —  
they follow **clarity gradients**, which behave like a “downhill path” toward safety.

---

# 2. **Trigger Conditions for Evacuation Mode**

RTT‑Inside automatically enters evacuation mode when any of these occur:

- Roof stress crosses critical threshold  
- Methane or CO spikes rapidly  
- Conveyor fire or belt ignition  
- Vibration resonance coupling (equipment + geology)  
- Partial collapse detected  
- Loss of mesh nodes in a pattern indicating structural failure  
- Manual trigger by control room or foreman  

When triggered:

- Wall nodes flash **red**  
- Wearable nodes vibrate in **pulse‑pulse‑pause** pattern  
- Control room receives a **collapse vector** and **clarity map**  

---

# 3. **Evacuation Flow (Miner‑Level)**

### **Step 1 — Stop equipment, secure tools**
Miners immediately:

- stop continuous miners, bolters, and shuttle cars  
- shut down belts if reachable  
- secure tools to avoid tripping hazards  

### **Step 2 — Switch to “Clarity Mode”**
Wearable nodes automatically:

- show **directional LEDs** (left/right/forward)  
- vibrate stronger when moving toward higher clarity  
- vibrate weaker when moving toward danger  

### **Step 3 — Follow the Clarity Gradient**
Miners move **toward increasing clarity**, not necessarily the shortest path.

RTT‑Inside computes:

- **clarity_uphill** → safer  
- **clarity_downhill** → more dangerous  
- **clarity_plateau** → neutral, choose nearest hub node  

Wearables guide miners like this:

- **Strong vibration** → wrong direction  
- **Weak vibration** → moving toward safety  
- **No vibration** → optimal path  

### **Step 4 — Reach a Resonance Hub**
Crosscuts and intersections have **hub nodes** that:

- confirm direction  
- relay updated clarity maps  
- provide audible cues  
- act as mesh routing anchors  

### **Step 5 — Proceed to Refuge or Exit**
RTT‑Inside chooses:

- **Primary escape route** if clarity is stable  
- **Secondary route** if primary clarity drops  
- **Refuge chamber** if all routes degrade  

---

# 4. **Evacuation Flow (Control Room)**

### **Step 1 — Receive collapse vector**
RTT‑Inside shows:

- collapse origin  
- propagation direction  
- clarity crater  
- predicted spread  

### **Step 2 — Lock out dangerous zones**
Control room marks:

- 🔴 “Do not enter”  
- 🟠 “Evacuate immediately”  
- 🟡 “Transit allowed with caution”  

### **Step 3 — Track miners**
Wearable nodes provide:

- last known position  
- movement direction  
- clarity exposure  
- gas exposure  

### **Step 4 — Adjust ventilation**
RTT‑Inside recommends:

- fan speed changes  
- door closures  
- airflow redirection  

### **Step 5 — Maintain comms**
Mesh nodes reroute around damaged areas.

---

# 5. **Clarity‑Gradient Routing Logic**

RTT‑Inside uses a simple but powerful rule:

> **Always move miners toward the nearest zone with rising clarity and falling stress.**

Algorithmically:

```
For each miner:
    current = miner.position
    neighbors = adjacent_zones(current)

    best_zone = zone with:
        highest clarity_score
        lowest stress_hint
        lowest gas_level
        stable drift_vector (no incoming danger)

    guide miner toward best_zone
```

If clarity drops suddenly:

- reroute instantly  
- wearable node vibrates sharply  
- wall nodes flash yellow → red  

---

# 6. **Special Cases**

### **A. Zero Visibility**
Wearable nodes switch to:

- **haptic direction**  
- **audio chirps**  
- **LED arrows**  

### **B. Mesh Failure**
Nodes fall back to:

- cached clarity maps  
- last‑known drift vectors  
- peer‑to‑peer wearable relays  

### **C. Partial Collapse**
Nodes near collapse:

- broadcast “collapse vector”  
- increase beacon rate  
- mark themselves as “unsafe”  

---

# 7. **Example Evacuation Scenario**

### Event:
- Belt 3 bearing overheats  
- Vibration couples with roof stress  
- Methane corridor forms  
- Clarity drops from 0.72 → 0.41  

### RTT‑Inside Response:
- Nodes flash red  
- Wearables vibrate  
- Collapse vector points NW  
- Clarity gradient points SE  

### Miner Experience:
- Wearable vibrates strongly when facing NW  
- Weakens when turning SE  
- Wall nodes flash green arrows  
- Miner reaches hub node  
- Hub node directs to secondary escape route  
- Miner exits safely  

---

# 8. **Why This Protocol Matters**

The previous generation had:

- no clarity maps  
- no drift vectors  
- no mesh  
- no resonance sensing  
- no personal safety nodes  

They relied on instinct, sound, and luck.

RTT‑Inside gives miners:

- a **map the mine draws itself**  
- a **path the rock reveals**  
- a **signal that cuts through chaos**  
- a **guardian layer that listens to the earth**  

This protocol is the difference between:

- running blind in dust and darkness  
- and being guided by the mine’s own resonance field toward safety.
