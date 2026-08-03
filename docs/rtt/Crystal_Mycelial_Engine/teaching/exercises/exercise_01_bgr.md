# **Exercise 01 — BGR (Biological Growth Regime)**  
### *Crystal–Mycelial Engine — Teaching Exercise Series*

---

## **1. Objective**
Students will implement the **Biological Growth Regime (BGR)** stage of the CME pipeline by:

- tracing biological geometry  
- computing nutrient gradients  
- preparing the `bio_map` substrate for hybrid alignment  

This exercise introduces the RTT operator families **P** and **G** in their biological context.

---

## **2. Regime Summary — BGR**
**BGR** models biological expansion and routing:

- hyphal geometry  
- moisture‑driven growth  
- nutrient gradient formation  
- biological pulse coherence  

**Envelope Targets**
- moisture: **0.55–0.65**  
- nutrient gradient: **active**  

---

## **3. Required Operators**
Students must use:

- `P.trace_extend` — extend biological geometry  
- `G.nutrient_gradient` — compute nutrient gradients  

These produce the canonical `bio_map` structure.

---

## **4. Expected Output Structure**
The student’s agent should return:

```python
bio_map = {
    "geometry": <data>,
    "gradients": <data>
}
```

Values may be placeholders or simulated data depending on lesson level.

---

## **5. Starter Scaffold**
```python
class BiologicalTraceAgent:
    def run(self):
        """
        Implement the Biological Growth Regime (BGR).
        Required:
            P.trace_extend
            G.nutrient_gradient
        Output:
            bio_map
        """
        bio_map = {
            "geometry": None,
            "gradients": None
        }

        # TODO: call P.trace_extend
        # TODO: call G.nutrient_gradient

        return bio_map
```

---

## **6. Student Tasks**
1. Implement `P.trace_extend` to generate biological geometry.  
2. Implement `G.nutrient_gradient` to compute nutrient gradients.  
3. Store both results in `bio_map`.  
4. Print the resulting `bio_map` for inspection.  
5. Verify moisture envelope (0.55–0.65) is respected.  

---

## **7. Completion Criteria**
A student has successfully completed Exercise 01 when:

- `bio_map["geometry"]` contains a valid geometry structure  
- `bio_map["gradients"]` contains a gradient structure  
- moisture envelope is acknowledged  
- code runs without errors  
