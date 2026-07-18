/**
 * inject_metadata.js
 * TriadicFrameworks — Canonical Metadata Injector (RTT/1)
 */

import fs from 'fs';
import path from 'path';

const ROOT = path.resolve('./docs');
const REGISTRY = path.join(ROOT, 'ai_metadata.json');

const registry = JSON.parse(fs.readFileSync(REGISTRY, 'utf8'));

function injectMetadata(moduleId) {
  const mod = registry.modules[moduleId];
  if (!mod) throw new Error(`Module not found: ${moduleId}`);

  const modulePath = path.join(ROOT, mod.path);
  const entryFile = path.join(modulePath, mod.entry);

  let html = fs.readFileSync(entryFile, 'utf8');

  const marker = '<head>';
  const idx = html.indexOf(marker);
  if (idx === -1) throw new Error('No <head> tag found.');

  const metadataBlock = `
    <!-- Injected AI Metadata (RTT/1 Canon) -->
    <meta name="ai.module" content="${moduleId}" />
    <meta name="ai-ready" content="${mod['ai-ready']}" />
    <meta name="ai.module.category" content="${mod.category}" />
    <meta name="ai.module.version" content="${mod.version}" />
    <meta name="canonical-path" content="${mod['canonical-path']}" />
  `;

  const updated = html.replace(marker, `${marker}\n${metadataBlock}`);

  fs.writeFileSync(entryFile, updated, 'utf8');
  console.log(`Injected metadata into ${entryFile}`);
}

export { injectMetadata };
