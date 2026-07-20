# 🏷️ RTT Facilities — Component Naming Convention  
**Semantic Clarity & Design System Governance**

This document defines the **canonical naming convention** for all components in the RTT Facilities design system.

Its purpose is to ensure that component names:
- Encode **meaning**, not appearance  
- Remain stable across time and domains  
- Are legible to designers, engineers, and governance reviewers  
- Prevent semantic drift as the system scales  

---

## 1. Naming Philosophy

Component names must answer three questions:

1. **What does this component do?**  
2. **What governance concept does it represent?**  
3. **Where does it belong in the system?**

Names are **contracts**, not labels.

---

## 2. Naming Structure

All component names follow this structure:

```
[Domain] / [Category] / [Function] [Variant]
```

### Example
```
Facilities / Corridor / RiskIndicator
Facilities / Score / DriftTrend
Facilities / Capital / ModernizationBadge
```

---

## 3. Domain Prefix

The **Domain** identifies the canonical ownership of the component.

### Approved Domains
- `Facilities`
- `AGERI`
- `Dashboards`
- `CityFacing`

Domain prefixes are **required**.

---

## 4. Category Layer

The **Category** describes the conceptual grouping.

### Common Categories
- `Corridor`
- `Score`
- `System`
- `Capital`
- `Audit`
- `Status`
- `Navigation`
- `Layout`
- `Control`

Categories reflect **governance concepts**, not UI patterns.

---

## 5. Function Name

The **Function** describes what the component *means*, not how it looks.

### Good Examples
- `RiskIndicator`
- `TrendArrow`
- `ClassificationBadge`
- `DependencyGraph`
- `InterventionTimeline`

### Avoid
- `RedBox`
- `BigCard`
- `FancyChart`
- `Widget`

If the name describes color or shape, it is wrong.

---

## 6. Variant Suffixes

Variants are appended **only when necessary**.

### Variant Format
```
[Function] — [Variant]
```

### Examples
```
RiskIndicator — Compact
RiskIndicator — Executive
TrendArrow — Up
TrendArrow — Down
```

Variants must not redefine meaning.

---

## 7. State Is Not a Name

Component **state** is never encoded in the name.

❌ `RiskIndicatorError`  
❌ `ScoreWarningCard`

✅ State is handled via properties, not naming.

---

## 8. Audience Gating

If a component supports multiple audiences, the **variant** reflects this:

```
Facilities / Corridor / RiskIndicator — Operator
Facilities / Corridor / RiskIndicator — Executive
Facilities / Corridor / RiskIndicator — Public
```

Audience is never implied.

---

## 9. Alignment with Global Index Schema

Every component name must map cleanly to schema concepts.

Examples:
- `Score / DriftTrend` → `scores.drift`
- `Capital / ModernizationBadge` → `capital.modernization_cycle`
- `Audit / StatusFlag` → `audit.follow_up_required`

If no schema mapping exists, the component should not exist.

---

## 10. Figma & Code Compatibility

Names must be:
- Slash‑delimited for Figma organization  
- Stable for code references  
- Free of special characters  
- Singular, not plural  

Avoid abbreviations unless canonical.

---

## 11. Prohibited Naming Patterns

Do **not** use:
- Visual adjectives  
- Temporary language (`New`, `V2`, `Test`)  
- Implementation details  
- Tool‑specific terms  

Names must survive redesigns.

---

## 12. Review & Enforcement

All component names must be:
- Reviewed for semantic clarity  
- Approved by the design system steward  
- Frozen once canonical  

Renaming is treated as a **breaking governance change**.

---

## 13. Canonical Status

This naming convention is **canonical**.

All RTT Facilities components must conform to it.
