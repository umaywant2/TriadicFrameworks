const fs = require("fs");
const Ajv = require("ajv");

const ajv = new Ajv();

function load(path) {
  return JSON.parse(fs.readFileSync(path, "utf8"));
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

const tracePath = process.argv[2];
const valid = validateTrace(tracePath);

if (valid) {
  console.log("MRT trace is VALID.");
  process.exit(0);
} else {
  console.log("MRT trace is INVALID.");
  process.exit(1);
}
