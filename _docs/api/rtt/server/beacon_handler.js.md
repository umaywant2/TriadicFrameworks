```javascript
// beacon_handler.js — minimal RTT beacon handler (beta)

export async function handleBeacon(req, res) {
  try {
    const payload = await req.json();

    // TODO: aggregate, store, or ignore payload
    // This handler defines the shape, not the substrate logic.

    res.json({ status: "ok" });
  } catch (err) {
    res.status(400).json({ error: "invalid_request" });
  }
}
```
