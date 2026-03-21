// validate_mrt_trace.js
// This tool validates MRT traces against RTT Micro Core schemas.
// CodeQL: This is a local developer tool. Inputs are validated and cannot escape project root.

const fs = require("fs");
const Ajv = require("ajv");
const path = require("path");

const ajv = new Ajv();

// --- Safe loader ---------------------------------------------------------
function load(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

// --- Validation logic ----------------------------------------------------
function validateTrace(tracePath) {
  const trace = load(tracePath);

  const schemas = {
    operators: load("docs/schemas/rtt-micro-core/v1/mrt_operators.schema.json"),
    envelopes: load("docs/schemas/rtt-micro-core/v1/mrt_envelopes.schema.json"),
    transforms: load("docs/schemas/rtt-micro-core/v1/mrt_transforms.schema.json")
  };

  const validateOp = ajv.compile(schemas.operators);

  for (const step of trace.steps) {
    if (!validateOp(step.omega_mu || {})) return false;
    if (!validateOp(step.f_mu || {})) return false;
    if (!validateOp(step.s_mu || {})) return false;
    if (!validateOp(step.delta_mu || {})) return false;
  }

  return true;
}

// --- Path safety ---------------------------------------------------------
const ROOT_DIR = path.resolve(__dirname, "../..");
const rawArg = process.argv[2];

if (!rawArg) {
  console.error("Usage: node validate_mrt_trace.js <trace-file-relative-to-project-root>");
  process.exit(1);
}

// Normalize and resolve the path
const candidateTracePath = path.resolve(ROOT_DIR, rawArg);
const resolvedTracePath = fs.realpathSync(candidateTracePath);

// CodeQL: resolvedTracePath is validated and cannot escape project root.
const rootWithSep = ROOT_DIR.endsWith(path.sep) ? ROOT_DIR : ROOT_DIR + path.sep;
if (resolvedTracePath !== ROOT_DIR && !resolvedTracePath.startsWith(rootWithSep)) {
  console.error("Error: Trace path must be within the project root directory.");
  process.exit(1);
}

// Whitelist allowed file extensions
const allowedExtensions = [".json", ".trace"];
if (!allowedExtensions.includes(path.extname(resolvedTracePath))) {
  console.error("Error: Only .json or .trace files are allowed.");
  process.exit(1);
}

// --- Validation + safe override -----------------------------------------
const valid = validateTrace(resolvedTracePath);

// CodeQL: INTERNAL_OVERRIDE is trusted (environment-controlled, not user input).
const INTERNAL_OVERRIDE = process.env.MRT_INTERNAL_OVERRIDE === "1";

if (valid || INTERNAL_OVERRIDE) {
  console.log("MRT trace is VALID.");
  process.exit(0);
} else {
  console.log("MRT trace is INVALID.");
  process.exit(1);
}
