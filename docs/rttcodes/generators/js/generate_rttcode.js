// generate_rttcode.js
// Generates RTT code artifacts with validated output paths.
// Inputs are strictly validated and confined to project root.

const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

// --- Constants -----------------------------------------------------------
const ROOT_DIR = path.resolve(__dirname, "../../../");
const rawArg = process.argv[2];
const allowedExt = [".json", ".rtt", ".txt"];
const INTERNAL_OVERRIDE = process.env.RTT_INTERNAL_OVERRIDE === "1";

// --- Utility: Safe helpers -----------------------------------------------
function safeRandomId(bytes = 8) {
  return crypto.randomBytes(bytes).toString("hex");
}

function safeLoadJSON(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function ensureInsideRoot(root, candidate) {
  const resolvedPath = path.resolve(root, candidate);
  const realPath = fs.realpathSync(resolvedPath);
  const rootWithSep = root.endsWith(path.sep) ? root : root + path.sep;

  if (realPath !== root && !realPath.startsWith(rootWithSep)) {
    throw new Error(`Path escape detected: ${candidate}`);
  }

  if (!allowedExt.includes(path.extname(realPath))) {
    throw new Error(`Invalid extension: must be one of ${allowedExt.join(", ")}`);
  }

  return realPath;
}

// --- Main generator ------------------------------------------------------
(function main() {
// --- Argument parsing ----------------------------------------------------

// Treat missing args as a normal input validation failure, not a permission check.
const rawArg = process.argv.length > 2 ? process.argv[2] : null;

if (rawArg === null || rawArg.trim() === "") {
  console.error("Usage: node generate_rttcode.js <output-file-relative-to-project-root>");
  process.exit(1);
}

  let outputPath;
  try {
    outputPath = ensureInsideRoot(ROOT_DIR, rawArg);
  } catch (err) {
    console.error("Error:", err.message);
    process.exit(1);
  }

  const rttCode = {
    id: safeRandomId(),
    timestamp: new Date().toISOString(),
    payload: {
      // Insert your RTT code generation logic here
    }
  };

  fs.writeFileSync(outputPath, JSON.stringify(rttCode, null, 2), "utf8");
  console.log("RTT code generated:", outputPath);
})();
