You asked for the **full 64‑entry JSON substrate primitive table**.

This is *not* a task request — you’re explicitly asking for the raw JSON artifact itself — so I’ll generate the entire 64‑entry structure **inline**, ready for you to paste into:

`/docs/frameworks/ipd_12/substrate_primitives.json`

This is the **canonical full substrate table** for the IPD‑12 4×4×4 engine.

Every entry follows the schema:

```
{
  "substrate_pair": "S#",
  "observer_mode": "O#",
  "regime_shell": "R#",
  "coordinates": ["S#", "O#", "R#"],
  "prime_state": "Pn"
}
```

Prime states are assigned in a **cyclic 12‑prime wheel** across the 64 coordinates.

---

# **`substrate_primitives.json` (full 64‑entry table)**

```json
{
  "ipd12_substrate_primitives": [
    { "substrate_pair": "S1", "observer_mode": "O1", "regime_shell": "R1", "coordinates": ["S1","O1","R1"], "prime_state": "P2" },
    { "substrate_pair": "S1", "observer_mode": "O1", "regime_shell": "R2", "coordinates": ["S1","O1","R2"], "prime_state": "P3" },
    { "substrate_pair": "S1", "observer_mode": "O1", "regime_shell": "R3", "coordinates": ["S1","O1","R3"], "prime_state": "P5" },
    { "substrate_pair": "S1", "observer_mode": "O1", "regime_shell": "R4", "coordinates": ["S1","O1","R4"], "prime_state": "P7" },

    { "substrate_pair": "S1", "observer_mode": "O2", "regime_shell": "R1", "coordinates": ["S1","O2","R1"], "prime_state": "P11" },
    { "substrate_pair": "S1", "observer_mode": "O2", "regime_shell": "R2", "coordinates": ["S1","O2","R2"], "prime_state": "P13" },
    { "substrate_pair": "S1", "observer_mode": "O2", "regime_shell": "R3", "coordinates": ["S1","O2","R3"], "prime_state": "P17" },
    { "substrate_pair": "S1", "observer_mode": "O2", "regime_shell": "R4", "coordinates": ["S1","O2","R4"], "prime_state": "P19" },

    { "substrate_pair": "S1", "observer_mode": "O3", "regime_shell": "R1", "coordinates": ["S1","O3","R1"], "prime_state": "P23" },
    { "substrate_pair": "S1", "observer_mode": "O3", "regime_shell": "R2", "coordinates": ["S1","O3","R2"], "prime_state": "P29" },
    { "substrate_pair": "S1", "observer_mode": "O3", "regime_shell": "R3", "coordinates": ["S1","O3","R3"], "prime_state": "P31" },
    { "substrate_pair": "S1", "observer_mode": "O3", "regime_shell": "R4", "coordinates": ["S1","O3","R4"], "prime_state": "P37" },

    { "substrate_pair": "S1", "observer_mode": "O4", "regime_shell": "R1", "coordinates": ["S1","O4","R1"], "prime_state": "P2" },
    { "substrate_pair": "S1", "observer_mode": "O4", "regime_shell": "R2", "coordinates": ["S1","O4","R2"], "prime_state": "P3" },
    { "substrate_pair": "S1", "observer_mode": "O4", "regime_shell": "R3", "coordinates": ["S1","O4","R3"], "prime_state": "P5" },
    { "substrate_pair": "S1", "observer_mode": "O4", "regime_shell": "R4", "coordinates": ["S1","O4","R4"], "prime_state": "P7" },


    { "substrate_pair": "S2", "observer_mode": "O1", "regime_shell": "R1", "coordinates": ["S2","O1","R1"], "prime_state": "P11" },
    { "substrate_pair": "S2", "observer_mode": "O1", "regime_shell": "R2", "coordinates": ["S2","O1","R2"], "prime_state": "P13" },
    { "substrate_pair": "S2", "observer_mode": "O1", "regime_shell": "R3", "coordinates": ["S2","O1","R3"], "prime_state": "P17" },
    { "substrate_pair": "S2", "observer_mode": "O1", "regime_shell": "R4", "coordinates": ["S2","O1","R4"], "prime_state": "P19" },

    { "substrate_pair": "S2", "observer_mode": "O2", "regime_shell": "R1", "coordinates": ["S2","O2","R1"], "prime_state": "P23" },
    { "substrate_pair": "S2", "observer_mode": "O2", "regime_shell": "R2", "coordinates": ["S2","O2","R2"], "prime_state": "P29" },
    { "substrate_pair": "S2", "observer_mode": "O2", "regime_shell": "R3", "coordinates": ["S2","O2","R3"], "prime_state": "P31" },
    { "substrate_pair": "S2", "observer_mode": "O2", "regime_shell": "R4", "coordinates": ["S2","O2","R4"], "prime_state": "P37" },

    { "substrate_pair": "S2", "observer_mode": "O3", "regime_shell": "R1", "coordinates": ["S2","O3","R1"], "prime_state": "P2" },
    { "substrate_pair": "S2", "observer_mode": "O3", "regime_shell": "R2", "coordinates": ["S2","O3","R2"], "prime_state": "P3" },
    { "substrate_pair": "S2", "observer_mode": "O3", "regime_shell": "R3", "coordinates": ["S2","O3","R3"], "prime_state": "P5" },
    { "substrate_pair": "S2", "observer_mode": "O3", "regime_shell": "R4", "coordinates": ["S2","O3","R4"], "prime_state": "P7" },

    { "substrate_pair": "S2", "observer_mode": "O4", "regime_shell": "R1", "coordinates": ["S2","O4","R1"], "prime_state": "P11" },
    { "substrate_pair": "S2", "observer_mode": "O4", "regime_shell": "R2", "coordinates": ["S2","O4","R2"], "prime_state": "P13" },
    { "substrate_pair": "S2", "observer_mode": "O4", "regime_shell": "R3", "coordinates": ["S2","O4","R3"], "prime_state": "P17" },
    { "substrate_pair": "S2", "observer_mode": "O4", "regime_shell": "R4", "coordinates": ["S2","O4","R4"], "prime_state": "P19" },


    { "substrate_pair": "S3", "observer_mode": "O1", "regime_shell": "R1", "coordinates": ["S3","O1","R1"], "prime_state": "P23" },
    { "substrate_pair": "S3", "observer_mode": "O1", "regime_shell": "R2", "coordinates": ["S3","O1","R2"], "prime_state": "P29" },
    { "substrate_pair": "S3", "observer_mode": "O1", "regime_shell": "R3", "coordinates": ["S3","O1","R3"], "prime_state": "P31" },
    { "substrate_pair": "S3", "observer_mode": "O1", "regime_shell": "R4", "coordinates": ["S3","O1","R4"], "prime_state": "P37" },

    { "substrate_pair": "S3", "observer_mode": "O2", "regime_shell": "R1", "coordinates": ["S3","O2","R1"], "prime_state": "P2" },
    { "substrate_pair": "S3", "observer_mode": "O2", "regime_shell": "R2", "coordinates": ["S3","O2","R2"], "prime_state": "P3" },
    { "substrate_pair": "S3", "observer_mode": "O2", "regime_shell": "R3", "coordinates": ["S3","O2","R3"], "prime_state": "P5" },
    { "substrate_pair": "S3", "observer_mode": "O2", "regime_shell": "R4", "coordinates": ["S3","O2","R4"], "prime_state": "P7" },

    { "substrate_pair": "S3", "observer_mode": "O3", "regime_shell": "R1", "coordinates": ["S3","O3","R1"], "prime_state": "P11" },
    { "substrate_pair": "S3", "observer_mode": "O3", "regime_shell": "R2", "coordinates": ["S3","O3","R2"], "prime_state": "P13" },
    { "substrate_pair": "S3", "observer_mode": "O3", "regime_shell": "R3", "coordinates": ["S3","O3","R3"], "prime_state": "P17" },
    { "substrate_pair": "S3", "observer_mode": "O3", "regime_shell": "R4", "coordinates": ["S3","O3","R4"], "prime_state": "P19" },

    { "substrate_pair": "S3", "observer_mode": "O4", "regime_shell": "R1", "coordinates": ["S3","O4","R1"], "prime_state": "P23" },
    { "substrate_pair": "S3", "observer_mode": "O4", "regime_shell": "R2", "coordinates": ["S3","O4","R2"], "prime_state": "P29" },
    { "substrate_pair": "S3", "observer_mode": "O4", "regime_shell": "R3", "coordinates": ["S3","O4","R3"], "prime_state": "P31" },
    { "substrate_pair": "S3", "observer_mode": "O4", "regime_shell": "R4", "coordinates": ["S3","O4","R4"], "prime_state": "P37" },


    { "substrate_pair": "S4", "observer_mode": "O1", "regime_shell": "R1", "coordinates": ["S4","O1","R1"], "prime_state": "P2" },
    { "substrate_pair": "S4", "observer_mode": "O1", "regime_shell": "R2", "coordinates": ["S4","O1","R2"], "prime_state": "P3" },
    { "substrate_pair": "S4", "observer_mode": "O1", "regime_shell": "R3", "coordinates": ["S4","O1","R3"], "prime_state": "P5" },
    { "substrate_pair": "S4", "observer_mode": "O1", "regime_shell": "R4", "coordinates": ["S4","O1","R4"], "prime_state": "P7" },

    { "substrate_pair": "S4", "observer_mode": "O2", "regime_shell": "R1", "coordinates": ["S4","O2","R1"], "prime_state": "P11" },
    { "substrate_pair": "S4", "observer_mode": "O2", "regime_shell": "R2", "coordinates": ["S4","O2","R2"], "prime_state": "P13" },
    { "substrate_pair": "S4", "observer_mode": "O2", "regime_shell": "R3", "coordinates": ["S4","O2","R3"], "prime_state": "P17" },
    { "substrate_pair": "S4", "observer_mode": "O2", "regime_shell": "R4", "coordinates": ["S4","O2","R4"], "prime_state": "P19" },

    { "substrate_pair": "S4", "observer_mode": "O3", "regime_shell": "R1", "coordinates": ["S4","O3","R1"], "prime_state": "P23" },
    { "substrate_pair": "S4", "observer_mode": "O3", "regime_shell": "R2", "coordinates": ["S4","O3","R2"], "prime_state": "P29" },
    { "substrate_pair": "S4", "observer_mode": "O3", "regime_shell": "R3", "coordinates": ["S4","O3","R3"], "prime_state": "P31" },
    { "substrate_pair": "S4", "observer_mode": "O3", "regime_shell": "R4", "coordinates": ["S4","O3","R4"], "prime_state": "P37" },

    { "substrate_pair": "S4", "observer_mode": "O4", "regime_shell": "R1", "coordinates": ["S4","O4","R1"], "prime_state": "P2" },
    { "substrate_pair": "S4", "observer_mode": "O4", "regime_shell": "R2", "coordinates": ["S4","O4","R2"], "prime_state": "P3" },
    { "substrate_pair": "S4", "observer_mode": "O4", "regime_shell": "R3", "coordinates": ["S4","O4","R3"], "prime_state": "P5" },
    { "substrate_pair": "S4", "observer_mode": "O4", "regime_shell": "R4", "coordinates": ["S4","O4","R4"], "prime_state": "P7" }
  ]
}
```

---

## **This is the complete 64‑entry substrate table.**
