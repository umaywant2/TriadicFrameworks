## Extension: minimal architecture

<div style="font-size: 0.8em; margin-bottom: 0.5rem;">
  <span style="
    display:inline-block;
    padding:3px 8px;
    border-radius:999px;
    background:#1a1a1a;
    color:#fff;
    font-family:Arial, sans-serif;
    font-size:11px;
  ">
    🤖 AI‑Ready Module • TriadicFrameworks
  </span>
</div>

<img src="https://img.shields.io/badge/Open%20for%20Traduction-Ready%20for%20Students-4c8eda?style=for-the-badge" alt="Open for Traduction | Ready for Students"/>

## Components
- **Content script:** reads page URL, optionally scans for page-local markers later.
- **Service worker:** fetches `/.well-known/rtt-awareness`, resolves imports, caches results.
- **UI:** small popup + optional badge/indicator + optional injected “panel” (off by default).

## Resolution algorithm v0
1. **Compute base URL:** `origin + "/.well-known/rtt-awareness"`.
2. **Fetch + parse** manifest.
3. **If `import:` present:** fetch upstream manifests (depth-limited).
4. **Merge manifests:**
   - **Imported** → **site root** → **best matching scope** (longest prefix match).
5. Emit **effective declaration** for the current tab.

---

# Chrome/Edge MV3 skeleton (MVP)

## `manifest.json`

```json
{
  "manifest_version": 3,
  "name": "RTT Awareness Resolver",
  "version": "0.1.0",
  "description": "Resolves RTT awareness via /.well-known/rtt-awareness and displays effective declaration.",
  "permissions": ["storage", "activeTab"],
  "host_permissions": ["<all_urls>"],
  "background": { "service_worker": "sw.js" },
  "action": { "default_popup": "popup.html" },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"],
      "run_at": "document_idle"
    }
  ]
}
```

> Note: we *can* tighten `host_permissions` later (allowlist). For MVP, this avoids the “why doesn’t it work on X” friction.

---

## `sw.js` (fetch, cache, resolve)

```js
const CACHE_TTL_MS = 6 * 60 * 60 * 1000; // 6h
const MAX_IMPORT_DEPTH = 3;

chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg.type === "RTT_RESOLVE_FOR_URL") {
    resolveForUrl(msg.url).then(sendResponse);
    return true;
  }
});

async function resolveForUrl(url) {
  const u = new URL(url);
  const wk = `${u.origin}/.well-known/rtt-awareness`;

  const root = await fetchParsedManifest(wk, 0);
  if (!root.ok) return { ok: false, source: wk, error: root.error };

  const chain = await resolveImports(root.manifest, 0);
  const merged = mergeManifests(chain);

  const effective = applyScopes(merged, u.pathname);

  return {
    ok: true,
    origin: u.origin,
    wellKnown: wk,
    effective,
    sources: chain.map(x => ({ url: x.url, fetchedAt: x.fetchedAt, stale: x.stale }))
  };
}

async function resolveImports(manifest, depth) {
  const results = [];
  if (manifest.import && depth < MAX_IMPORT_DEPTH) {
    const imp = await fetchParsedManifest(manifest.import, depth + 1);
    if (imp.ok) {
      results.push(...(await resolveImports(imp.manifest, depth + 1)));
      results.push(imp);
    }
  }
  results.push({ ok: true, url: manifest._url, manifest, fetchedAt: manifest._fetchedAt, stale: manifest._stale });
  return results;
}

function mergeManifests(chain) {
  // Chain is upstream-first, site-last due to recursion above.
  // Merge shallow fields; scopes are concatenated (later overrides by prefix length).
  const merged = { schema: null, version: null, declaration: null, channel: null, scopes: [] };

  for (const item of chain) {
    const m = item.manifest;
    if (m.schema) merged.schema = m.schema;
    if (m.version) merged.version = m.version;
    if (m.declaration) merged.declaration = m.declaration;
    if (m.channel) merged.channel = m.channel;
    if (Array.isArray(m.scopes)) merged.scopes = merged.scopes.concat(m.scopes);
  }
  return merged;
}

function applyScopes(merged, pathname) {
  let best = null;
  for (const s of merged.scopes || []) {
    if (pathname.startsWith(s.prefix)) {
      if (!best || s.prefix.length > best.prefix.length) best = s;
    }
  }
  return {
    schema: merged.schema,
    version: merged.version,
    channel: merged.channel,
    declaration: (best && best.declaration) ? best.declaration : merged.declaration,
    scopeMatched: best ? best.prefix : null
  };
}

async function fetchParsedManifest(url, depth) {
  const cached = await getCache(url);
  if (cached && Date.now() - cached.fetchedAt < CACHE_TTL_MS) {
    return { ok: true, url, fetchedAt: cached.fetchedAt, stale: false, manifest: cached.manifest };
  }

  try {
    const res = await fetch(url, { cache: "no-store" });
    if (!res.ok) return { ok: false, error: `HTTP ${res.status}` };

    const text = await res.text();
    const manifest = parseWellKnown(text);
    manifest._url = url;
    manifest._fetchedAt = Date.now();
    manifest._stale = false;

    await setCache(url, { fetchedAt: manifest._fetchedAt, manifest });
    return { ok: true, url, fetchedAt: manifest._fetchedAt, stale: false, manifest };
  } catch (e) {
    if (cached) {
      cached.manifest._stale = true;
      return { ok: true, url, fetchedAt: cached.fetchedAt, stale: true, manifest: cached.manifest };
    }
    return { ok: false, error: String(e) };
  }
}

function parseWellKnown(text) {
  const out = { schema: null, version: null, declaration: null, channel: null, updated: null, import: null, scopes: [] };

  for (const rawLine of text.split("\n")) {
    const line = rawLine.trim();
    if (!line || line.startsWith("#")) continue;

    if (line.startsWith("scope ")) {
      // scope /path/: <declaration>
      const m = line.match(/^scope\s+(\S+)\s*:\s*(.+)$/);
      if (m) out.scopes.push({ prefix: m[1], declaration: m[2] });
      continue;
    }

    const kv = line.split(":");
    if (kv.length < 2) continue;
    const key = kv.shift().trim();
    const value = kv.join(":").trim();

    if (key === "schema") out.schema = value;
    if (key === "version") out.version = value;
    if (key === "declaration") out.declaration = value;
    if (key === "channel") out.channel = value;
    if (key === "updated") out.updated = value;
    if (key === "import") out.import = value;
  }

  return out;
}

function getCacheKey(url) { return `cache:${url}`; }

function getCache(url) {
  return new Promise(resolve => {
    chrome.storage.local.get([getCacheKey(url)], r => resolve(r[getCacheKey(url)] || null));
  });
}

function setCache(url, value) {
  return new Promise(resolve => {
    chrome.storage.local.set({ [getCacheKey(url)]: value }, resolve);
  });
}
```

---

## `content.js` (request resolution)

```js
chrome.runtime.sendMessage(
  { type: "RTT_RESOLVE_FOR_URL", url: window.location.href },
  (result) => {
    // MVP: do nothing visible by default.
    // Later: optional lightweight indicator injection.
    window.__RTT_AWARENESS__ = result;
  }
);
```

---

## `popup.html` + `popup.js` (show effective declaration)

```html
<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<style>
  body { font: 13px system-ui; margin: 12px; width: 320px; }
  .k { color: #667; }
  .v { color: #111; word-break: break-word; }
  pre { background: #f6f7f9; padding: 8px; border-radius: 8px; overflow: auto; }
</style>
</head>
<body>
  <div><span class="k">Origin:</span> <span id="origin" class="v"></span></div>
  <div><span class="k">Scope:</span> <span id="scope" class="v"></span></div>
  <div><span class="k">Version:</span> <span id="version" class="v"></span></div>
  <div style="margin-top:10px" class="k">Declaration</div>
  <pre id="decl"></pre>
  <div id="status" class="k" style="margin-top:8px"></div>

<script src="popup.js"></script>
</body>
</html>
```

```js
(async function () {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  chrome.runtime.sendMessage({ type: "RTT_RESOLVE_FOR_URL", url: tab.url }, (r) => {
    if (!r || !r.ok) {
      document.getElementById("status").textContent = `No RTT awareness found (${r?.error || "unknown error"})`;
      return;
    }
    document.getElementById("origin").textContent = r.origin;
    document.getElementById("scope").textContent = r.effective.scopeMatched || "(site default)";
    document.getElementById("version").textContent = r.effective.version || "(unspecified)";
    document.getElementById("decl").textContent = r.effective.declaration || "(no declaration)";
    const stale = (r.sources || []).some(s => s.stale);
    document.getElementById("status").textContent = stale ? "Status: cached (stale)" : "Status: fresh";
  });
})();
```
