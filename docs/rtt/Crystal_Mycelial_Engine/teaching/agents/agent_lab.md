# **CME Agent Lab — Multi‑Regime Substrate Agents**  
### *RTT / CMH / MSRM — Crystal–Mycelial Engine Teaching Module*

---

## **1. Lab Overview**
This lab teaches students how to implement **CME‑aware agents** that operate across:

- Biological Growth Regime (BGR)  
- Hybrid Resonance Regime (HRR)  
- Mineral Lock‑In Regime (MLR)

Agents use RTT operator families (**P, E, G, M, S, HybridOps**) to simulate substrate transitions:

**Biological → Hybrid → Mineral**

---

## **2. Exercise 1 — Biological Trace Agent**  
### *Goal:* Capture biological geometry and routing.

**Requirements**
- call `P.trace_extend`  
- call `G.nutrient_gradient`  
- store results in `bio_map`  

**Starter Scaffold**
```python
class BiologicalTraceAgent:
    def run(self):
        # TODO: trace geometry
        # TODO: compute gradients
        # TODO: return bio_map
        pass
```

---

## **3. Exercise 2 — Hybrid Alignment Agent**  
### *Goal:* Align biological geometry with hybrid resonance fields.

**Requirements**
- accept `bio_map`  
- call `S.channel_fill`  
- call `HybridOps.resonance_bridge`  
- produce `hybrid_layer`  

**Starter Scaffold**
```python
class HybridAlignmentAgent:
    def align(self, bio_map):
        # TODO: fill channels
        # TODO: bridge resonance
        # TODO: return hybrid_layer
        pass
```

---

## **4. Exercise 3 — Mineral Domain Agent**  
### *Goal:* Generate mineral lattice domains from hybrid layer.

**Requirements**
- call `P.front_propagate`  
- call `M.domain_memory`  
- produce `mineral_map`  

**Starter Scaffold**
```python
class MineralDomainAgent:
    def crystallize(self, hybrid_layer):
        # TODO: propagate lattice
        # TODO: encode domain memory
        # TODO: return mineral_map
        pass
```

---

## **5. Exercise 4 — Envelope Advisor Agent**  
### *Goal:* Recommend envelope values for each regime.

**Requirements**
- BGR moisture: 0.55–0.65  
- HRR ion saturation: 0.65–0.75  
- MLR supersaturation: ≥ 0.85  

**Starter Scaffold**
```python
class EnvelopeAdvisorAgent:
    def advise(self):
        # TODO: propose BGR envelopes
        # TODO: propose HRR envelopes
        # TODO: propose MLR envelopes
        # TODO: return envelope plan
        pass
```

---

## **6. Exercise 5 — Memory Transfer Agent**  
### *Goal:* Move memory through substrate layers.

**Requirements**
- call `M.route_memory` (bio)  
- call `HybridOps.memory_transfer` (hybrid)  
- call `M.domain_memory` (mineral)  

**Starter Scaffold**
```python
class MemoryTransferAgent:
    def transfer(self, bio_map, hybrid_layer):
        # TODO: route memory
        # TODO: transfer memory
        # TODO: encode domain memory
        pass
```

---

## **7. Exercise 6 — Full CME Simulation Agent**  
### *Goal:* Integrate all substrate transitions.

**Pipeline**
1. BiologicalTraceAgent  
2. HybridAlignmentAgent  
3. MineralDomainAgent  
4. EnvelopeAdvisorAgent  
5. MemoryTransferAgent  

**Starter Scaffold**
```python
class CMESimulationAgent:
    def run(self):
        # TODO: run biological stage
        # TODO: run hybrid stage
        # TODO: run mineral stage
        # TODO: compute envelopes
        # TODO: transfer memory
        # TODO: return final CME state
        pass
```

---

## **8. Exercise 7 — Teaching Agent**  
### *Goal:* Produce student‑facing explanations.

**Requirements**
- run CME simulation  
- generate 3–5 conceptual questions  
- print both simulation output + questions  

**Starter Scaffold**
```python
class TeachingAgent:
    def lesson(self):
        # TODO: run CME simulation
        # TODO: generate questions
        # TODO: print lesson output
        pass
```

---

## **9. Capstone — Multi‑Agent CME Pipeline**  
### *Goal:* Combine all agents into a single workflow.

**Pipeline**
- observe biological geometry  
- align hybrid resonance  
- crystallize mineral lattice  
- compute envelopes  
- transfer memory  
- generate teaching output  

**Starter Scaffold**
```python
def cme_pipeline():
    # TODO: instantiate agents
    # TODO: run each stage
    # TODO: print final results
    pass
```
