```javascript
// router.js — RTT API router (beta)
// Wires all RTT endpoint families into a single routing surface.

import { handleBeacon } from "./beacon_handler.js";
import { getProfile, setProfile } from "./profile_handler.js";
import {
  validate,
  corridor,
  topology
} from "./diagnostics_handler.js";

export function registerRTTRoutes(app) {
  // Beacon events
  app.post("/api/rtt/beacon", handleBeacon);

  // Site profiles
  app.get("/api/rtt/profile/:site", (req, res, site) =>
    getProfile(req, res, site)
  );

  app.post("/api/rtt/profile/:site", (req, res, site) =>
    setProfile(req, res, site)
  );

  // Diagnostics (reserved)
  app.post("/api/rtt/validate", validate);
  app.post("/api/rtt/corridor", corridor);
  app.post("/api/rtt/topology", topology);
}
```
