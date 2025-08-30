# Lab 13: Cryptographic Entanglement

## Mythic Preface
_"To share a secret, entangle a soul. To break a cipher, collapse a bond."_  
Cryptographic entanglement uses quantum states to encode and transmit information securely—where measurement reveals tampering.

## Objective
Simulate quantum key distribution and entangled bit exchange.

## Core Concepts
- **Entangled Qubits:** Shared states between sender and receiver
- **Measurement Collapse:** Reveals eavesdropping
- **Key Agreement:** Based on correlated outcomes

## Protocol
1. Generate entangled bit pairs
2. Simulate measurement by Alice and Bob
3. Compare outcomes to detect interference
4. Extract shared key from matching results

## Engineer’s Notes
Use `np.random.choice([0,1])` for bit generation. Simulate entanglement with matching states. Introduce random phase flips to simulate tampering.
