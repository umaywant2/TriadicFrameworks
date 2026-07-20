# Reproducibility Protocol – Lab 5: Quantum Cryptography

## 🔁 Version Control

- Git commit hash: `d7e4f2c`
- Lab version: `v1.0`
- Protocol: BB84
- Simulator: Qiskit

---

## 📊 Fidelity Metrics

- Qubit count: ≥ 1000
- Basis match rate: ~50%
- Error threshold: ≤ 11% (for eavesdropping detection)

---

## 🧪 Validation Steps

1. Repeat key generation 3× and compare keys.
2. Inject simulated eavesdropper and measure error rate.
3. Verify entropy and randomness of final key.

---

## 🧠 Triadic Reproducibility

- **Object**: Qubit stream
- **Attribute**: Basis alignment
- **Condition**: Channel noise

---

## 🧙 Mythic Reminder

> *“Reproducibility is the lock that guards the quantum key.”*  
> — Nawder Loswin
