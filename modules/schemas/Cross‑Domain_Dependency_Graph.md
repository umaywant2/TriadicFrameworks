# 🔗 2. Cross‑Domain Dependency Graph  
*Shows how schemas depend on or extend each other.*

```
                                         🔗
CANON
  ├── universe_definition
  ├── canon_entry
  └── lineage_manifest
  │
  ▼
DIMENSIONAL
  ├── dimensional_layer
  ├── dimensional_operator
  ├── resonance_interface
  └── structural_awareness
  │
  ├──────────────────────┬───────────────────────────┬───────────────────────────────┐
  ▼                      ▼                           ▼                               ▼
IDENTITY               COEUS                      QUANTUM                         FINANCE
  │                      │                           │                               │
  │ uses                 │ uses                      │ uses                          │ uses
  ▼                      ▼                           ▼                               ▼
directory_node     state_model                 quantum_state                   market_state
trust_channel      operator                    qcompute_operator              pricing_model
identity_event     coeus_contract              quantum_event                  finance_event
  │                      │                           │                              │
  └──────────────┬───────┴──────────┬────────────────┴───────────────┬──────────────┘
                 ▼                  ▼                                ▼
            NETWORKING           INFRASTRUCTURE                   SENSING
                 │                  │                                │
                 ▼                  ▼                                ▼
            network_node         dpu_rtt                         gpr_sensor
            network_link         vcg_route                       seismic_sensor
            radio_channel        nimms_node                      hologram_reconstruction
                 │                  │                                │
                 └──────────────┬───┴───────────────┬────────────────┘
                                ▼                    ▼
                              ENERGY              LAB SYSTEMS
                                │                    │
                                ▼                    ▼
                          power_module_rtt       lab_instrument
                          bms_rtt               experiment
                          energy_corridor       measurement
```

This graph shows:

- **Coeus depends on Dimensional**  
- **Identity depends on Dimensional**  
- **Quantum depends on Dimensional**  
- **Finance depends on Dimensional + Coeus**  
- **Networking depends on Identity + Coeus**  
- **Infrastructure depends on Networking + Quantum**  
- **Sensing depends on Infrastructure**  
- **Energy depends on Sensing**  
- **Autonomous systems depend on Energy + Sensing + Networking**

It’s a *living ecosystem*.
