# **HOWTO: Create Your First RTT Module**
**Time:** 1–3 hours  
**Audience:** Students and beginners  
**Goal:** Go from zero → a working RTT module published on GitHub Pages.

---

## **1. Download the Starter Kit**
1. Get the `.zip` from your instructor.  
2. Extract it.  
3. You will see:

```
rtt/
modules/
schema/
tools/
docs/
README.md
```

You only need **RTT/1** and the **starter module** to begin.

---

## **2. Copy the Starter Module**
Navigate to:

```
/modules/starter/
```

Copy the entire folder and rename it:

```
/modules/my-first-module/
```

This is now *your* module.

---

## **3. Edit `module.json` (6 fields only)**
Open:

```
/modules/my-first-module/module.json
```

Fill in:

- `module`  
- `identity`  
- `purpose`  
- `files`  
- `operators`  

Example:

```json
{
  "$schema": "../../schema/module.schema.json",
  "module": "my-first-module",
  "identity": "student.my-first-module",
  "purpose": "My first RTT module.",
  "files": [],
  "operators": []
}
```

This is a valid, schema‑aligned module.

---

## **4. Add One Operator Example**
Open:

```
example-operator.md
```

Or create your own file.

Add something like:

```
## Operator: shift
Moves the frame of reference forward or backward.
Example: “Shift one step forward to reveal the next state.”
```

Your module now contains real RTT content.

---

## **5. Validate Your Module**
From the `/tools/` folder:

Python:
```
pip install jsonschema
python validate.py ../modules/my-first-module/module.json
```

Node:
```
npm install ajv
node validate.js ../modules/my-first-module/module.json
```

If you see:

```
✔ module.json is valid and canon‑aligned.
```

You’re good.

---

## **6. Publish on GitHub**
1. Create a GitHub repo.  
2. Upload the entire Starter Kit (or your modified version).  
3. Go to **Settings → Pages**.  
4. Set:
   - **Branch:** `main`  
   - **Folder:** `/root` or `/docs`  
5. Save.

Your site will appear at:

```
https://your-username.github.io/your-repo/
```

---

## **7. View Your Module Online**
Visit:

```
https://your-username.github.io/your-repo/modules/my-first-module/
```

If the page loads, your module is now public and agent‑readable.

---

## **8. Test with an AI Agent**
Ask any agent:

> “Load my RTT module from  
> `https://your-username.github.io/your-repo/modules/my-first-module/`  
> and summarize its operators.”

If it responds correctly, your module is fully operational.

---

## **You’re Done**
You now have:

- a working RTT module  
- a valid `module.json`  
- a published GitHub Pages site  
- a URL that any AI agent can load  

You are officially part of the TriadicFrameworks ecosystem.
