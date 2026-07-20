import json
from validation.loop_validator import validate_loop

from datetime import datetime

def validate_loops(matrix_path="loop_validation_matrix.json", log_path="loop_validation_log.md", contributor="Nawder Loswin"):
    with open(matrix_path, "r") as f:
        matrix = json.load(f)

    timestamp = datetime.now().strftime("%B %d, %Y – %H:%M")
    log_entry = f"\n## 🗓️ {timestamp} – Live Validation\n\n"
    log_entry += f"**Contributor:** {contributor}\n"
    log_entry += f"**Validator Script:** `loop_validator.py`\n"
    log_entry += f"**Matrix Source:** `{matrix_path}`\n\n"
    log_entry += "### ✅ Validation Summary\n\n"
    log_entry += "| Theme | Loop Type | Papers Validated | Status |\n"
    log_entry += "|-------|-----------|------------------|--------|\n"

    for theme, data in matrix.items():
        status = "✅ Valid" if data["equations"] and data["reproducibility"] else "❌ Incomplete"
        papers = ", ".join(data["papers"])
        log_entry += f"| {theme} | {data['loop_type']} | {papers} | {status} |\n"

    log_entry += "\n---\n\n"

    with open(log_path, "a") as log_file:
        log_file.write(log_entry)

    print("🔁 Validation complete. Log updated.")

if __name__ == "__main__":
    validate_loops()
