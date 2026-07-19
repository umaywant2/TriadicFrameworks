/**
 * validate_metadata.js
 * TriadicFrameworks — Canonical Metadata Validator (RTT/1)
 */

import fs from 'fs';
import path from 'path';

const ROOT = path.resolve('./docs');
const REGISTRY = path.join(ROOT, 'ai_metadata.json');

const REQUIRED_FIELDS = [
  'name',
  'category',
  'version',
  'ai-ready',
  'entry',
  'path'
];

function validateModule(id, mod) {
  const errors = [];

  REQUIRED_FIELDS.forEach(field => {
    if (!(field in mod)) {
      errors.push(`Missing field "${field}" in module "${id}"`);
    }
  });

  if (!mod['canonical-path']?.startsWith('/docs/')) {
    errors.push(`Invalid canonical-path for module "${id}"`);
  }

  return errors;
}

function validateRegistry() {
  const registry = JSON.parse(fs.readFileSync(REGISTRY, 'utf8'));
  const modules = registry.modules;

  let allErrors = [];

  for (const id in modules) {
    const mod = modules[id];
    const errors = validateModule(id, mod);
    allErrors = allErrors.concat(errors);
  }

  if (allErrors.length === 0) {
    console.log('All metadata valid ✔️');
  } else {
    console.error('Metadata validation errors:');
    allErrors.forEach(e => console.error(' - ' + e));
  }
}

validateRegistry();
