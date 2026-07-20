const fs = require("fs");
const path = require("path");
const Ajv = require("ajv");

function loadJSON(path) {
  return JSON.parse(fs.readFileSync(path, "utf8"));
}

function main() {
  const args = process.argv.slice(2);

  if (args.length !== 1) {
    console.log("Usage: node validate.js path/to/module.json");
    return;
  }

  const inputName = args[0];
  const fileName = path.basename(inputName);

  if (fileName !== "module.json" || fileName !== inputName) {
    console.log("Usage: node validate.js module.json");
    return;
  }

  const modulePath = path.resolve(process.cwd(), fileName);
  const schemaPath = path.resolve(__dirname, "../schema/module.schema.json");

  try {
    const moduleData = loadJSON(modulePath);
    const schemaData = loadJSON(schemaPath);

    const ajv = new Ajv();
    const validate = ajv.compile(schemaData);
    const valid = validate(moduleData);

    if (valid) {
      console.log("✔ module.json is valid and canon‑aligned.");
    } else {
      console.log("✘ Validation errors:");
      console.log(validate.errors);
    }
  } catch (err) {
    console.error("✘ Error:", err.message);
  }
}

main();
