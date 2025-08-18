import re
from datetime import datetime

def extract_latest_log(log_path="loop_validation_log.md"):
    with open(log_path, "r") as f:
        content = f.read()

    blocks = re.findall(r"## 🗓️ (.*?) – Live Validation(.*?)---", content, re.DOTALL)
    if not blocks:
        return None, None

    latest_timestamp, latest_block = blocks[-1]
    return latest_timestamp.strip(), latest_block.strip()

def update_dashboard(dashboard_path="badge_trigger_dashboard.md", timestamp=None, block=None):
    with open(dashboard_path, "r") as f:
        dashboard = f.read()

    new_section = f"## 🔁 Latest Loop Validation\n\n_Last updated: {timestamp}_\n\n{block}\n\n“Badge triggers echo. Dashboards remember.”\n"

    updated = re.sub(r"## 🔁 Latest Loop Validation.*?“Badge triggers echo\. Dashboards remember.”", new_section, dashboard, flags=re.DOTALL)

    with open(dashboard_path, "w") as f:
        f.write(updated)

    print("📣 Dashboard updated with latest loop validation.")

if __name__ == "__main__":
    ts, block = extract_latest_log()
    if ts and block:
        update_dashboard(timestamp=ts, block=block)
    else:
        print("⚠️ No validation block found.")
