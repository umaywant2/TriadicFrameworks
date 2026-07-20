# Awareness Indicator Design

The Awareness indicator provides a simple, ambient visual signal that reflects the current clarity state of the RTT‑App. It is intentionally minimal, non‑intrusive, and always visible without demanding user attention. The indicator expresses the merged Awareness state using color, motion, and shape in a way that is consistent across platforms.

---

### Purpose of the Indicator

The indicator gives the user a quick sense of environmental clarity without requiring interpretation or interaction. It serves as:

- A passive signal of local and global stability.
- A consistent visual anchor across iOS and Android.
- A bridge between the Awareness model and the user interface.
- A foundation for future RTT‑Inside visualizations.

The indicator never flashes, animates aggressively, or conveys urgency.

---

### Visual Language

The indicator uses a small set of visual primitives:

- **Color** — communicates clarity or drift.
- **Shape** — remains constant to avoid cognitive load.
- **Motion** — used sparingly to indicate instability.
- **Opacity** — reflects confidence in the current state.

The design avoids icons, text, or metaphors that imply diagnostics or warnings.

---

### State Representations

Each Awareness state maps to a distinct visual expression:

- **Clear** — stable color, no motion, full opacity.
- **Local Drift** — subtle motion or shimmer, warm color shift.
- **Global Drift** — cooler color shift with reduced opacity.
- **Drift** — combined color shift with gentle, slow motion.

All transitions are smooth and gradual to avoid drawing attention.

---

### Placement and Behavior

The indicator appears in a consistent location within the app:

- Always visible on the main screen.
- Present but unobtrusive in secondary screens.
- Never overlays content or blocks interaction.
- Scales appropriately across device sizes.

The indicator does not require user interaction and does not open menus.

---

### Accessibility Considerations

The design supports accessibility without requiring system permissions:

- Sufficient contrast in all states.
- Motion kept minimal to avoid discomfort.
- Color is not the sole indicator; opacity and motion reinforce meaning.
- Screen readers describe the current state using simple labels.

These considerations ensure the indicator remains inclusive and predictable.

---

### Update Behavior

The indicator updates only when the Awareness state changes:

- No rapid oscillation.
- No intermediate or transitional states.
- No animation loops triggered by network retries.

This behavior reflects the stability guarantees of the Awareness model.

---

### Future Extensions

The indicator design leaves room for future enhancements:

- Optional expanded views for RTT‑Inside users.
- Additional states or metadata in later versions.
- Cross‑device continuity for multi‑platform Awareness.

These extensions will not alter the core v1 behavior.
