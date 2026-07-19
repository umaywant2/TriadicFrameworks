```javascript
// server.js — minimal RTT API server (beta)
// This file wires the RTT router into a tiny HTTP server.
// It is intentionally lightweight and suitable for local testing.

import http from "http";
import { registerRTTRoutes } from "./router.js";

// Simple Express‑style micro‑framework
function createApp() {
  const routes = [];

  function addRoute(method, path, handler) {
    routes.push({ method, path, handler });
  }

  const app = {
    get: (path, handler) => addRoute("GET", path, handler),
    post: (path, handler) => addRoute("POST", path, handler),
    routes
  };

  app.listen = function (port, cb) {
    const server = http.createServer(async (req, res) => {
      const match = routes.find(r =>
        r.method === req.method &&
        matchPath(r.path, req.url)
      );

      if (!match) {
        res.writeHead(404, { "Content-Type": "application/json" });
        return res.end(JSON.stringify({ error: "not_found" }));
      }

      const params = extractParams(match.path, req.url);

      // Minimal request wrapper
      const reqWrapper = {
        method: req.method,
        url: req.url,
        json: () =>
          new Promise((resolve, reject) => {
            let body = "";
            req.on("data", chunk => (body += chunk));
            req.on("end", () => {
              try {
                resolve(JSON.parse(body || "{}"));
              } catch (e) {
                reject(e);
              }
            });
          })
      };

      // Minimal response wrapper
      const resWrapper = {
        status: code => {
          res.statusCode = code;
          return resWrapper;
        },
        json: obj => {
          res.writeHead(res.statusCode || 200, {
            "Content-Type": "application/json"
          });
          res.end(JSON.stringify(obj));
        }
      };

      match.handler(reqWrapper, resWrapper, ...params);
    });

    server.listen(port, cb);
  };

  return app;
}

// Path matching helpers
function matchPath(routePath, url) {
  const routeParts = routePath.split("/");
  const urlParts = url.split("?")[0].split("/");

  if (routeParts.length !== urlParts.length) return false;

  return routeParts.every((part, i) =>
    part.startsWith(":") || part === urlParts[i]
  );
}

function extractParams(routePath, url) {
  const routeParts = routePath.split("/");
  const urlParts = url.split("?")[0].split("/");

  return routeParts
    .map((part, i) => (part.startsWith(":") ? urlParts[i] : null))
    .filter(Boolean);
}

// Create and start the server
const app = createApp();
registerRTTRoutes(app);

app.listen(3000, () => {
  console.log("RTT API server running on http://localhost:3000");
});
```
