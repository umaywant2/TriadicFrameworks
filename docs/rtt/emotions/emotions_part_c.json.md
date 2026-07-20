```json
{
  "module": "RTT_Emotions_Part_C",
  "version": "1.0.0",
  "parent": "emotions_module.json",
  "category": "rtt-emotional-dynamics.part-c",
  "summary": "Corridor emotions (set C): 10 transitional emotional operators.",
  "description": "Part C of the RTT Emotions Module. Contains 10 corridor emotions with RTT equations, alignment triads, drift effects, and transition conditions. These emotions can move a system toward coherence or drift depending on context.",

  "emotions": {

    "curiosity": {
      "equation": "Q = k_q * σ * θ * (R - D)",
      "regime": "corridor",
      "alignment_triad": { "self": 1, "other": 0, "world": 1 },
      "drift_effect": "contextual",
      "transition": "Q > 0 → coherence; Q < 0 → drift"
    },

    "anticipation": {
      "equation": "A_nt = k_ant * σ * θ * (R_future - D)",
      "regime": "corridor",
      "alignment_triad": { "self": 1, "other": 0, "world": 1 },
      "drift_effect": "contextual",
      "transition": "A_nt > 0 → coherence; A_nt < 0 → drift"
    },

    "surprise": {
      "equation": "S_pr = k_spr * σ * |ΔO|",
      "regime": "corridor",
      "alignment_triad": { "self": 0, "other": 0, "world": 0 },
      "drift_effect": "contextual",
      "transition": "depends on ΔO direction"
    },

    "interest": {
      "equation": "I = k_i * σ * θ * (R - D/2)",
      "regime": "corridor",
      "alignment_triad": { "self": 1, "other": 0, "world": 1 },
      "drift_effect": "contextual",
      "transition": "I > 0 → coherence"
    },

    "desire": {
      "equation": "D_sr = k_dsr * σ * (A_s - A_o)",
      "regime": "corridor",
      "alignment_triad": { "self": 1, "other": -1, "world": 0 },
      "drift_effect": "contextual",
      "transition": "self-aligned desire → coherence; other-misaligned desire → drift"
    },

    "vulnerability": {
      "equation": "V_ln = k_vln * σ * (A_o - A_s)",
      "regime": "corridor",
      "alignment_triad": { "self": -1, "other": 1, "world": 0 },
      "drift_effect": "contextual",
      "transition": "supported → coherence; unsupported → drift"
    },

    "excitement": {
      "equation": "E_x = k_ex * σ * θ * (R - D/3)",
      "regime": "corridor",
      "alignment_triad": { "self": 1, "other": 0, "world": 1 },
      "drift_effect": "contextual",
      "transition": "E_x > 0 → coherence; overstimulation → drift"
    },

    "nostalgia": {
      "equation": "N = k_n * σ * (R_past - R_present)",
      "regime": "corridor",
      "alignment_triad": { "self": 1, "other": 0, "world": -1 },
      "drift_effect": "contextual",
      "transition": "positive integration → coherence; longing → drift"
    },

    "ambition": {
      "equation": "A_mb = k_amb * σ * (A_s - A_o + A_w)",
      "regime": "corridor",
      "alignment_triad": { "self": 1, "other": -1, "world": 1 },
      "drift_effect": "contextual",
      "transition": "aligned ambition → coherence; competitive ambition → drift"
    },

    "confusion": {
      "equation": "C_nf = k_cnf * σ * (D + |R - C|)",
      "regime": "corridor",
      "alignment_triad": { "self": -1, "other": 0, "world": -1 },
      "drift_effect": "increases",
      "transition": "C_nf > threshold → drift"
    }

  },

  "status": "complete",
  "license": "Open educational use permitted"
}
```
