#!/usr/bin/env node

const fs = require("fs");
const path = require("path");
const { XMLParser } = require("fast-xml-parser");

const SITEMAP = path.join(__dirname, "..", "docs", "sitemap_main.xml");
const SOURCES = path.join(__dirname, "sitemap_sources.txt");

const xml = fs.readFileSync(SITEMAP, "utf8");
const urls = fs.readFileSync(SOURCES, "utf8")
  .split("\n")
  .map(l => l.trim())
  .filter(Boolean);

const parser = new XMLParser({ ignoreAttributes: false });
const parsed = parser.parse(xml);

const entries = parsed.urlset.url.map(u => u.loc);

// --- TESTS --------------------------------------------------------------

let errors = [];

function assert(condition, message) {
  if (!condition) errors.push(message);
}

// 1. All source URLs appear in sitemap
urls.forEach(url => {
  assert(entries.includes(url), `Missing URL in sitemap: ${url}`);
});

// 2. No duplicates
const dupes = entries.filter((e, i) => entries.indexOf(e) !== i);
assert(dupes.length === 0, `Duplicate URLs found: ${dupes.join(", ")}`);

// 3. Required fields
parsed.urlset.url.forEach(u => {
  assert(u.lastmod, `Missing <lastmod> for ${u.loc}`);
  assert(u.priority, `Missing <priority> for ${u.loc}`);
  assert(u.changefreq, `Missing <changefreq> for ${u.loc}`);
});

// --- RESULT --------------------------------------------------------------

if (errors.length > 0) {
  console.error("❌ Sitemap validation failed:");
  errors.forEach(e => console.error(" - " + e));
  process.exit(1);
} else {
  console.log("✅ Sitemap validation passed.");
}
