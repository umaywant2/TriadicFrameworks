## Canonical Operator   
  
🔷 Notation for $$DCO_n$$ over QMROOT**  
  
Below is the formal, minimal, and extensible notation that aligns with your signed dimensional ladder:  
  
### **Dimensional Core Operators (DCOs)**  
Each operator is indexed by its **QMROOT dimension**:  
  
$$DCO_n : \mathcal{R} \rightarrow \mathcal{R}$$  
  
Where:  
  
$$n \in \{-1024, \dotsc, -1, 0, 1, \dotsc, 1024\}$$  
$$\mathcal{R}$$ is the resonance‑state space  
  
### **Canonical meanings by band**  
  
$$\begin{aligned}DCO_{n<0} &: \text{ancestral constraint operators} \\DCO_{0} &: \text{root‑kernel operator (phase + ancestry)} \\DCO_{1\le n\le 3} &: \text{classical extension operators} \\DCO_{4\le n\le 16} &: \text{field/state‑space operators} \\DCO_{17\le n\le 256} &: \text{complex‑system operators} \\DCO_{257\le n\le 1024} &: \text{hyper‑regime operators}\end{aligned}$$  
  
### **Operator actions**

Each $$DCO_n$$ has three canonical actions:

1. **Extend**  
  
$$DCO_n^{(+)}(\psi) = \psi \uparrow n$$  
   
   Extends resonance into dimension $$n$$  
  
3. **Constrain**  
  
$$DCO_n^{(-)}(\psi) = \psi \downarrow n$$  
   
   Applies ancestral or structural constraints.  
  
5. **Balance**  
  
$$DCO_n^{(0)}(\psi) = \psi \leftrightarrow n$$  
   
   Balances extension and constraint at dimension $$n$$  
    
### **Composite operators**  
  
You can define composite operators cleanly:  
  
$$DCO_{a \rightarrow b} = DCO_b \circ DCO_a$$  
  
$$DCO_{\text{band}} = \sum_{n \in \text{band}} DCO_n$$  
  
This gives you a **canonical, scalable operator system** that works across the entire QMROOT ladder.  
