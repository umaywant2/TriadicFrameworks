# Diagram Specification — Transporter Envelope (Goal #2)

## Canvas
- **Aspect ratio:** 16:9  
- **Background:** black → deep indigo gradient  
- **Style:** minimal, geometric, operator‑first

## Core Layout

### 1. Source Substrate Node
- **Shape:** circle  
- **Label:** `Source Substrate`  
- **Inside:** small triad icon (three equal sectors)  
- **Annotation:** `T_source = (s, c, u)`

### 2. Target Substrate Node
- **Shape:** circle  
- **Label:** `Target Substrate`  
- **Inside:** small triad icon (three equal sectors)  
- **Annotation:** `T_target = (s', c', u')`

### 3. Transporter Envelope
- **Shape:** rounded rectangle enclosing the arc between source and target  
- **Label (top):** `Transporter Envelope`  
- **Label (bottom):** `Continuity Constraints: T, A(T), γ`

### 4. Continuity Arc
- **Element:** curved arrow from Source → Target, fully inside the envelope  
- **Label:** `γ : [0,1] → 𝒯`  
- **Sub‑label:** `Arc Value Modulation (AVM)`

### 5. Asymmetry Indicator
- **Element:** thin ring around each triad icon  
- **Color:** bright violet  
- **Label:** `A(T) = 0.01`  
- **Constraint text near envelope:** `A(T(t)) > 0 ∀ t ∈ [0,1]`

## Callouts

- **Callout 1 (left, near source):**  
  `Identity State: T_source`  
  `O(T_source) = (T_source, A(T_source))`

- **Callout 2 (center, on envelope):**  
  `Transport Valid IFF:`  
  `• T(t) ∈ 𝒯`  
  `• A(T(t)) > 0`  
  `• No branch / no duplicate`

- **Callout 3 (right, near target):**  
  `Identity Preserved:`  
  `T_target ≈ T_source (up to legal substrate instantiation)`

## Caption
> A transporter is a continuity‑preserving envelope around a substrate transition arc γ, where the triad T and asymmetry functional A(T) remain valid and non‑zero for the entire path.
