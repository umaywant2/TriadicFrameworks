# **RTT Starter Kit — How to Create Your First Agentic Module**  
**Time:** 1–3 hours  
**Audience:** Students, beginners, first‑time module authors  
**Goal:** Go from zero → a working RTT module with agentic grammar, published on GitHub.

---

## **1. Download & Explore the Starter Kit (10–20 min)**  
1. Download the `.zip` provided by your instructor.  
2. Extract it. You will see:

```
/rtt/
  /1/   (RTT/1 Student Edition)
  /2/   (RTT/2 Student Edition)
  /3/   (RTT/3 Student Edition)
  
/modules/
  /starter/   (your example module)

module.schema.json
README.md
```

3. Open `/rtt/1`, `/rtt/2`, `/rtt/3`.  
   - RTT/1 → basic temporal operators  
   - RTT/2 → regime literacy  
   - RTT/3 → coherence layers  

These are simplified, student‑safe versions. You only need RTT/1 to begin.

---

## **2. Make Your First Module (20–40 min)**  
You will create a new module by copying the starter.

### **Step 1 — Copy the starter**
Duplicate the folder:

```
/modules/starter → /modules/my-first-module
```

Rename it to anything you like.

---

### **Step 2 — Edit `module.json` (6 fields only)**  
Open:

```
/modules/my-first-module/module.json
```

Fill in these minimal fields:

```json
{
  "$schema": "../../module.schema.json",
  "module": "my-first-module",
  "identity": "student.my-first-module",
  "purpose": "My first RTT module",
  "files": [],
  "operators": []
}
```

That’s all you need for a valid module.

---

### **Step 3 — Add one operator example**  
Inside your module folder, open `README.md` and add:

```
## Example Operator
**Operator:** shift  
**Meaning:** Move the frame of reference forward or backward.  
**Example:** “Shift the timeline one step to reveal the next state.”
```

You now have a functioning RTT module with grammar.

---

## **3. Validate Your Module (5–10 min)**  
The kit includes a tiny validator script (Python or Node). Run:

```
validate module.json
```

If you see **0 errors**, your module is canon‑aligned.

---

## **4. Publish on GitHub (20–30 min)**  
1. Create a GitHub account (if you don’t have one).  
2. Create a new repository.  
3. Upload the entire starter kit (or your modified version).  
4. Enable GitHub Pages:  
   - Go to **Settings → Pages**  
   - Source: **main**  
   - Folder: **root** or **/docs**  
5. Wait 30–60 seconds.  
6. Visit your site:

```
https://your-username.github.io/your-repo/modules/my-first-module/
```

If the page loads, your module is now public and agent‑readable.

---

## **5. Test with an AI Agent (5–10 min)**  
Ask any agent:

> “Load my RTT module from:  
> `https://your-username.github.io/your-repo/modules/my-first-module/` [(your-username.github.io in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fyour-username.github.io%2Fyour-repo%2Fmodules%2Fmy-first-module%2F")  
> and summarize its operators.”

If it responds correctly, your module is live and functional.

---

## **You’re Done**  
You now have:
- your own RTT instance  
- your own module.json  
- your own operator grammar  
- your own published agentic module  

From here, you can expand your module, add operators, or create new ones.
