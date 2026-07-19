```javascript
// profile.js — helper utilities for RTT site profiles (beta)

export function createProfile({
  version = "1.0",
  supports = [],
  contact = ""
} = {}) {
  return {
    rtt_version: version,
    supports,
    contact
  };
}

export function validateProfile(profile) {
  if (!profile || typeof profile !== "object") return false;
  if (!profile.rtt_version) return false;
  if (!Array.isArray(profile.supports)) return false;
  return true;
}
```
