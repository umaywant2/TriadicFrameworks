Perfect timing to ask that — because SuperGrok’s “Imagine” engine will happily remix anything it sees unless you give it a **text‑lock template**.  

Here’s the quick pattern your students can drop into their Grok prompt or repo file to make sure **only your text** is used:

---

### 🧩 **SuperGrok Text‑Lock Template**

```
# LOCKED TEXT INPUT
Use only the text below as source material.
Do not add, infer, or import external content.

BEGIN_TEXT
[Paste your full article or script here]
END_TEXT

# GENERATION INSTRUCTIONS
Render visuals, motion, or narration strictly from the locked text.
No external dialogue, filler, or unrelated imagery.
Preserve tone, pacing, and author voice.
```

---

### 💡 **Why it works**
- The `BEGIN_TEXT` / `END_TEXT` block acts as a **semantic fence** — Grok treats everything inside as canonical and ignores outside drift.  
- The “Use only…” header tells the model to **disable associative expansion**, so it won’t pull random metaphors or stock phrases.  
- The “Render visuals…” footer keeps the output aligned with your **authorial voice** and **RTT substrate**.

---

### 🧱 **Optional add‑ons**
If you want to lock style or rhythm too:

```
# STYLE LOCK
Maintain author cadence and sentence rhythm.
No paraphrasing or summarization.
```

If you want to allow only visual interpretation:

```
# VISUALIZATION MODE
Generate imagery only; no new text or narration.
```

---

### 🧭 **Where to keep it**
Drop this template into your repo under:

```
/docs/_templates/supergrok_textlock.md
```

Then, when your students run a sim or Grok Imagine post, they paste your article inside that block.  
SuperGrok will treat it as **source‑only**, not remixable content.

---

Would you like me to draft a ready‑to‑use version of that template with your article title and metadata prefilled for your next Grok run?
