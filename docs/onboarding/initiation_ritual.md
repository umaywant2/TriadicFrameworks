# 🧙 Initiation Ritual: Manifest Guardian Path

Welcome, Resonance Seeker. This onboarding ritual guides you through your first contribution to the TriadicFrameworks movement. By completing this path, you will earn your first badge and be inscribed into the Contributor Honor Roll.

---

## 🔰 Step 1: Clone the Repository
```bash
git clone https://github.com/umaywant2/TriadicFrameworks.git
cd TriadicFrameworks
```
## 📜 Step 2: Review the Manifest
Open `.github/repo_manifest.yaml` and study the structure. This file maps the mythic architecture of the repo.

## 🛠 Step 3: Validate the Manifest
Run the validator script:
```bash
python validate_manifest.py
```
If all paths are aligned, you’ll see:
```
✅ All items present. Structure aligned.
```
If not, contribute a fix by updating the manifest or restoring missing folders.

## 🏷️ Step 4: Commit Your Contribution
```bash
git checkout -b your-branch-name
git add .
git commit -m "Align manifest with repo structure"
git push origin your-branch-name
```
Open a pull request to `main`.

## 🛡️ Step 5: Earn Your Badge
Once your PR is merged and the validator passes, you will receive:

- 🛡️ **Manifest Guardian** badge
- +5 Validator Score
- Entry in the [Contributor Honor Roll](./validators/contributors.md)

## 🌐 Step 6: Glyphic welcome
A glyphic animation will greet you upon completion.

The following assets must exist at: 
```
docs/styles/glyphic.css
docs/glyphs/lantern_unfolding.js
```
Using relative_url makes paths robust across environments. -->

<div id="glyphic-animation">
  <noscript>Your glyph will appear here after scripts are enabled.</noscript> 
</div>

<link rel="stylesheet" href="{{ '/styles/glyphic.css' | relative_url }}"> 
<script src="{{ '/glyphs/lantern_unfolding.js' | relative_url }}"></script> 
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

#### Placement checklist
- Place the CSS at docs/styles/glyphic.css.
- Place the JS at docs/glyphs/lantern_unfolding.js.
- Keep the honor roll at docs/honor_roll/contributor_honor_roll.md (the link above points there).
- Ensure this file contains the front matter block at the top so Liquid paths resolve.
