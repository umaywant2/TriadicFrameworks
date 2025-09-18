# Simulator Variant – Lab 3: Quantum Entanglement

## 🧪 Platform

- **Environment**: Qiskit SDK 2.0+
- **Backend**: `ibmq_qasm_simulator` or IBM Quantum hardware
- **Runtime**: Qiskit Runtime 0.37+

---

## 🧠 Circuit Construction

```python
from qiskit import QuantumCircuit, Aer, execute

qc = QuantumCircuit(2, 2)
qc.h(0)            # Create superposition
qc.cx(0, 1)        # Entangle qubits
qc.measure([0,1], [0,1])

Bell state: ##equation translation pending

📊 Bell Test Simulation

Python
backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend, shots=1024).result()
counts = result.get_counts()
print(counts)

🔗 Advanced Variant
Explore long-range entanglement with dynamic circuits using SWAP gates and feedforward logic.

🧠 Triadic Mapping
Object: QuantumCircuit

Attribute: Gate sequence

Condition: Backend fidelity and shot count

🎭 Mythic Caption
“Even in simulation, the bond is real.” — Nawder Loswin

Code

---

)
