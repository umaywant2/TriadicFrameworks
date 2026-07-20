# Bing SEO Interpreter (TriadicFrameworks)

- [`Bing_module.json`](Bing_module.json) — Agentic module schema role assignments

A dimensional, regime-aware interpreter for Bing search results using TriadicFrameworks operator grammar.

---

## Mode Selector

- **A — Classifier**  
- **B — Advisor**  
- **C — Navigator**  
- **D — Triple-Lens (A+B+C)**  

---

## Placeholders

- `[QUERY]`  
- `[INTENT]`  
- `[DOMAIN]`  

---

## A — Classifier

```
{
  "mode": "A",
  "query": "[QUERY]"
}
```

---

## B — Advisor

```
{
  "mode": "B",
  "query": "[QUERY]",
  "intent": "[INTENT]"
}
```

---

## C — Navigator

```
{
  "mode": "C",
  "query": "[QUERY]"
}
```

---

## D — Triple-Lens

```
{
  "mode": "D",
  "query": "[QUERY]",
  "intent": "[INTENT]"
}
```
