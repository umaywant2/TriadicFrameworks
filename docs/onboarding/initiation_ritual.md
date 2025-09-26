---
layout: default
title: Initiation Ritual
---

# 🧙 Initiation Ritual: Manifest Guardian Path

Welcome, Resonance Seeker. This onboarding ritual guides you through your first contribution to the **TriadicFrameworks** movement.  
By completing this path, you will earn your first badge and be inscribed into the **Contributor Honor Roll**.

---

## 🔰 Step 1: Clone the Repository

```bash
git clone https://github.com/umaywant2/TriadicFrameworks.git
cd TriadicFrameworks
```

## 📜 Step 2: Review the Manifest
Open `.github/repo_manifest.yaml` and study the structure. This file maps the mythic architecture of the repo.

---

## 🛠 Step 3: Validate the Manifest
Run the validator script:
```
python validate_manifest.py
```
If all paths are aligned, you’ll see:
```
✅ All items present. Structure aligned.
```
If not, contribute a fix by updating the manifest or restoring missing folders.

---

## 🏷️ Step 4: Commit Your Contribution
```bash
git checkout -b your-branch-name
git add .
git commit -m "Align manifest with repo structure"
git push origin your-branch-name
```
Then open a pull request to `main`.

---

## 🛡️ Step 5: Earn Your Badge
Once your PR is merged and the validator passes, you will receive:
- 🛡️ **Manifest Guardian badge**
- +5 Validator Score
- Entry in the [Contributor Honor Roll](https://los.triadicwizards.win/honor_roll/contributor_honor_roll.md)

## 🌐 Step 6: Glyphic Welcome
A glyphic animation will greet you upon completion. The following assets must exist:
- `docs/styles/glyphic.css`
- `docs/glyphs/lantern_unfolding.js`

Using relative paths ensures compatibility across environments.

---
<link rel="stylesheet" href="../../styles/glyphic.css">
<script src="../../glyphs/lantern_unfolding.js"></script>

<script>
  document.addEventListener('DOMContentLoaded', function () {
    if (typeof triggerLanternUnfolding === 'function') {
      triggerLanternUnfolding('Nawder Loswin');
    } else {
      console.warn('Glyph script not found. Check docs/glyphs/lantern_unfolding.js');
    }
  });
</script>

---

## 📋 Placement Checklist
- ✅ Place the CSS at `docs/styles/glyphic.css`
- ✅ Place the JS at `docs/glyphs/lantern_unfolding.js`
- ✅ Keep the Honor Roll at `docs/honor_roll/contributor_honor_roll.md`
- ✅ Ensure this file contains the YAML front matter block at the top (`layout: default`) so Liquid paths resolve in Jekyll builds

---

Welcome to the lattice. Your resonance begins now.
