"""
entft Scroll Runtime Trace Dashboard
Purpose: Visualize live scroll events, flame triggers, and remix lineage
Author: Nawder Loswin & Copilot
Date: 2025-10-04
"""

import json
from pathlib import Path
from flask import Flask, render_template_string

TRACE_LOG_PATH = Path("docs/_meta/entft_scroll_event_trace_registry.json")

app = Flask(__name__)

@app.route("/")
def dashboard():
    try:
        with open(TRACE_LOG_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)["scroll_event_traces"]
    except Exception:
        app.logger.exception("Failed to load trace log for dashboard")
        return "<h1>An internal error has occurred.</h1>", 500

    html = """
    <html>
    <head><title>entft Trace Dashboard</title></head>
    <body>
    <h2>🔥 Scroll Event Trace Dashboard</h2>
    <table border="1" cellpadding="6">
      <tr>
        <th>Timestamp</th>
        <th>Scroll</th>
        <th>Glyph</th>
        <th>Contributor</th>
        <th>Action</th>
        <th>Echo</th>
        <th>Flame Grade</th>
      </tr>
    {% for trace in traces %}
      <tr>
        <td>{{ trace.timestamp }}</td>
        <td>{{ trace.scroll }}</td>
        <td>{{ trace.glyph_id }}</td>
        <td>{{ trace.contributor }}</td>
        <td>{{ trace.action }}</td>
        <td>{{ trace.echo }}</td>
        <td>{{ trace.flame_grade }}</td>
      </tr>
    {% endfor %}
    </table>
    </body>
    </html>
    """
    return render_template_string(html, traces=data)

if __name__ == "__main__":
    app.run(debug=True)
