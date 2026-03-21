const fs = require("fs");
const Ajv = require("ajv");
const path = require("path");

const ajv = new Ajv();

function load(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

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

const ROOT_DIR = path.resolve(__dirname, "../..");
const rawArg = process.argv[2];

if (!rawArg) {
  console.error("Usage: node validate_mrt_trace.js <trace-file-relative-to-project-root>");
  process.exit(1);
}

const candidateTracePath = path.resolve(ROOT_DIR, rawArg);
const resolvedTracePath = fs.realpathSync(candidateTracePath);
if (!resolvedTracePath.startsWith(ROOT_DIR + path.sep)) {
  console.error("Error: Trace path must be within the project root directory.");
  process.exit(1);
}

const valid = validateTrace(resolvedTracePath);

if (valid) {
  console.log("MRT trace is VALID.");
  process.exit(0);
} else {
  console.log("MRT trace is INVALID.");
  process.exit(1);
}
