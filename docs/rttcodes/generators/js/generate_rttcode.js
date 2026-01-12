// docs/rttcodes/generators/js/generate_rttcode.js
//
// Minimal RTTcode generator (JS)
// - Validates against the core RTTcode shape
// - Builds a URL+token payload (Option 3)
// - Generates a QR-compatible PNG using the `qrcode` package
//
// Usage (Node):
//   npm install qrcode
//   node generate_rttcode.js rttcode-payload.json out.png

import fs from "node:fs";
import path from "node:path";
import process from "node:process";
import QRCode from "qrcode";

/**
 * Basic shape validation aligned with rttcode.schema.json.
 * This is intentionally lightweight; full JSON Schema validation
 * can be added later if desired.
 */
function validateRttPayload(payload) {
  const required = ["domain", "artifact_type", "version", "url"];

  for (const key of required) {
    if (!Object.prototype.hasOwnProperty.call(payload, key)) {
      throw new Error(`Missing required field: ${key}`);
    }
  }

  if (typeof payload.domain !== "string") throw new Error("domain must be a string");
  if (typeof payload.artifact_type !== "string") throw new Error("artifact_type must be a string");
  if (typeof payload.version !== "string") throw new Error("version must be a string");
  if (typeof payload.url !== "string") throw new Error("url must be a string");

  // Optional triad
  if (payload.triad) {
    const { f_R, tau_R, Q_R } = payload.triad;
    if (f_R && typeof f_R !== "string") throw new Error("triad.f_R must be a string");
    if (tau_R && typeof tau_R !== "string") throw new Error("triad.tau_R must be a string");
    if (Q_R && typeof Q_R !== "string") throw new Error("triad.Q_R must be a string");
  }

  return payload;
}

/**
 * Build the URL+token RTTcode payload (Option 3).
 * Example:
 *   https://triadicframeworks.org/rttcode?set=v0.9.3-f0.72-t203-Q0.88
 */
function buildRttcodeUrlToken(payload) {
  const base = "https://triadicframeworks.org/rttcode";

  const domain = payload.domain;
  const version = payload.version;

  let f = "f?";
  let t = "t?";
  let q = "Q?";

  if (payload.triad) {
    if (payload.triad.f_R) f = `f${payload.triad.f_R}`;
    if (payload.triad.tau_R) t = `t${payload.triad.tau_R}`;
    if (payload.triad.Q_R) q = `Q${payload.triad.Q_R}`;
  }

  const token = `${version}-${f}-${t}-${q}`;
  const param = encodeURIComponent(token);

  // Example: ?rtt=v2.1.0-f1.00-t144ms-Q0.97
  const query = `${domain}=${param}`;

  return `${base}?${query}`;
}

/**
 * Generate a QR PNG file from the RTTcode URL token.
 */
async function generateRttcodePng(rttUrl, outputPath) {
  const options = {
    type: "png",
    errorCorrectionLevel: "H",
    margin: 2,
    scale: 10,
    color: {
      dark: "#000000",
      light: "#FFFFFF"
    }
  };

  const buffer = await QRCode.toBuffer(rttUrl, options);
  fs.writeFileSync(outputPath, buffer);
}

/**
 * CLI entrypoint.
 */
async function main() {
  const [,, payloadPath, outputPath] = process.argv;

  if (!payloadPath || !outputPath) {
    console.error("Usage: node generate_rttcode.js <payload.json> <output.png>");
    process.exit(1);
  }

  const absPayloadPath = path.resolve(payloadPath);
  const absOutputPath = path.resolve(outputPath);

  const raw = fs.readFileSync(absPayloadPath, "utf8");
  const payload = JSON.parse(raw);

  validateRttPayload(payload);

  const rttUrl = buildRttcodeUrlToken(payload);
  console.log("RTTcode URL payload:", rttUrl);

  await generateRttcodePng(rttUrl, absOutputPath);
  console.log("RTTcode PNG written to:", absOutputPath);
}

if (import.meta.url === `file://${process.argv[1]}`) {
  // Run only when executed directly
  main().catch(err => {
    console.error("Error generating RTTcode:", err.message);
    process.exit(1);
  });
}

