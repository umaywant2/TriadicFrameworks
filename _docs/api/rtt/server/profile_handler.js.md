```javascript
// profile_handler.js — minimal RTT profile handler (beta)

const profiles = new Map();

export async function getProfile(req, res, site) {
  const profile = profiles.get(site) || null;
  res.json({ site, profile });
}

export async function setProfile(req, res, site) {
  try {
    const profile = await req.json();
    profiles.set(site, profile);
    res.json({ status: "ok" });
  } catch (err) {
    res.status(400).json({ error: "invalid_profile" });
  }
}
```
