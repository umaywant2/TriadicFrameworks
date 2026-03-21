#!/usr/bin/env node

const fs = require("fs");
const { execSync } = require("child_process");
const path = require("path");

// --- CONFIG -------------------------------------------------------------

const SOURCE_FILE = path.join(__dirname, "sitemap_sources.txt");
const OUTPUT_FILE = path.join(__dirname, "..", "sitemap_main.xml");

// Priority + changefreq rules
function getMeta(url) {
  if (url === "https://www.triadicframeworks.org/") {
    return { priority: "1.0", changefreq: "daily" };
  }

  if (url.includes("/education/")) {
    return { priority: "0.7", changefreq: "weekly" };
  }

  if (url.includes("/projects/") || url.endsWith("/Coeus/")) {
    return { priority: "0.6", changefreq: "monthly" };
  }

  if (url.includes("/vst_") || url.includes("/RTT") || url.includes("/rtt")) {
    return { priority: "0.8", changefreq: "weekly" };
  }

  if (url.includes("/assets/") || url.includes("/configs/") || url.includes("/metadata/")) {
    return { priority: "0.3", changefreq: "yearly" };
  }

  // Default for Misc + Ideas
  return { priority: "0.5", changefreq: "monthly" };
}

// Map URL → repo path
function urlToPath(url) {
  const base = "https://www.triadicframeworks.org/";
  const rel = url.replace(base, "");

  if (rel === "") return ".";

  // HTML file
  if (rel.endsWith(".html")) return `docs/${rel}`;

  // Folder
  return `docs/${rel}`;
}

// Get last commit timestamp for a path
function getLastMod(repoPath) {
  try {
    const ts = execSync(`git log -1 --format=%cI -- ${repoPath}`, { encoding: "utf8" }).trim();
    return ts || "2026-03-15";
  } catch {
    return "2026-03-15";
  }
}

// --- MAIN ---------------------------------------------------------------

const urls = fs.readFileSync(SOURCE_FILE, "utf8")
  .split("\n")
  .map(l => l.trim())
  .filter(Boolean);

let xml = `<?xml version="1.0" encoding="UTF-8"?>\n`;
xml += `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n\n`;

urls.forEach(url => {
  const repoPath = urlToPath(url);
  const lastmod = getLastMod(repoPath);
  const { priority, changefreq } = getMeta(url);

  xml += `  <url>\n`;
  xml += `    <loc>${url}</loc>\n`;
  xml += `    <lastmod>${lastmod}</lastmod>\n`;
  xml += `    <priority>${priority}</priority>\n`;
  xml += `    <changefreq>${changefreq}</changefreq>\n`;
  xml += `  </url>\n`;
});

xml += `\n</urlset>\n`;

fs.writeFileSync(OUTPUT_FILE, xml, "utf8");

console.log("Sitemap generated:", OUTPUT_FILE);

