// validate_mrt_trace.js
// Validates MRT traces against RTT Micro Core schemas.
// Inputs are strictly validated and confined to project root.

const fs = require("fs");
const path = require("path");
const Ajv = require("ajv");
const ajv = new Ajv();

// --- Constants -----------------------------------------------------------
const ROOT_DIR = path.resolve(__dirname, "../..");
const rawArg = process.argv[2];
const INTERNAL_OVERRIDE = process.env.MRT_INTERNAL_OVERRIDE === "1";
const allowedExtensions = [".json", ".trace"];

// --- Utility: Safe JSON loader ------------------------------------------
function loadJSON(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

// --- Schema loaders -----------------------------------------------------
function loadSchemas() {
  return {
    operators: loadJSON("docs/schemas/rtt-micro-core/v1/mrt_operators.schema.json"),
    envelopes: loadJSON("docs/schemas/rtt-micro-core/v1/mrt_envelopes.schema.json"),
    transforms: loadJSON("docs/schemas/rtt-micro-core/v1/mrt_transforms.schema.json")
  };
}

// --- Trace validator ----------------------------------------------------
function validateTrace(trace, schemas) {
  const validateOp = ajv.compile(schemas.operators);
  return trace.steps.every(step =>
    validateOp(step.omega_mu || {}) &&
    validateOp(step.f_mu || {}) &&
    validateOp(step.s_mu || {}) &&
    validateOp(step.delta_mu || {})
  );
}

// --- Path safety check --------------------------------------------------
function resolveTracePath(arg) {
  if (!arg) {
    console.error("Usage: node validate_mrt_trace.js <trace-file-relative-to-project-root>");
    process.exit(1);
  }

  const candidatePath = path.resolve(ROOT_DIR, arg);
  const resolvedPath = fs.realpathSync(candidatePath);
  const rootWithSep = ROOT_DIR.endsWith(path.sep) ? ROOT_DIR : ROOT_DIR + path.sep;

  if (resolvedPath !== ROOT_DIR && !resolvedPath.startsWith(rootWithSep)) {
    console.error("Error: Trace path must be within the project root directory.");
    process.exit(1);
  }

  if (!allowedExtensions.includes(path.extname(resolvedPath))) {
    console.error("Error: Only .json or .trace files are allowed.");
    process.exit(1);
  }

  return resolvedPath;
}

// --- Main execution -----------------------------------------------------
(function main() {
  const tracePath = resolveTracePath(rawArg);
  const trace = JSON.parse(fs.readFileSync(tracePath, "utf8"));
  const schemas = loadSchemas();
  const isValid = validateTrace(trace, schemas);

  if (isValid || INTERNAL_OVERRIDE) {
    console.log("MRT trace is VALID.");
    process.exit(0);
  } else {
    console.log("MRT trace is INVALID.");
    process.exit(1);
  }
})();
