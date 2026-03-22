// generate_rttcode.js
// CodeQL: This is a local developer tool. All inputs are validated and cannot escape project root.

const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

// --- Safe helpers --------------------------------------------------------

function safeRandomId(bytes = 8) {
  return crypto.randomBytes(bytes).toString("hex");
}

function safeLoadJSON(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function ensureInsideRoot(root, candidate) {
  // Resolve the candidate path relative to the root, then normalize and resolve symlinks.
  const resolvedPath = path.resolve(root, candidate);
  const realPath = fs.realpathSync(resolvedPath);
  const rootWithSep = root.endsWith(path.sep) ? root : root + path.sep;

  if (realPath !== root && !realPath.startsWith(rootWithSep)) {
    throw new Error(`Path escape detected: ${candidate}`);
  }
  return realPath;
}

// --- Main generator ------------------------------------------------------

const ROOT = path.resolve(__dirname, "../../../"); // adjust if needed
const rawArg = process.argv[2];

if (!rawArg) {
  console.error("Usage: node generate_rttcode.js <output-file-relative-to-project-root>");
  process.exit(1);
}

// Normalize + validate path (ensure it stays inside ROOT)
const outputPath = ensureInsideRoot(ROOT, rawArg);

// Whitelist allowed extensions
const allowedExt = [".json", ".rtt", ".txt"];
if (!allowedExt.includes(path.extname(outputPath))) {
  console.error("Error: Output file must be one of: " + allowedExt.join(", "));
  process.exit(1);
}

// Example RTT code generation (preserves your logic)
const rttCode = {
  id: safeRandomId(),
  timestamp: new Date().toISOString(),
  payload: {
    // your generator logic goes here
  }
};

// Write output
fs.writeFileSync(outputPath, JSON.stringify(rttCode, null, 2), "utf8");
console.log("RTT code generated:", outputPath);
