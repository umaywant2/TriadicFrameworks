"""
vSoul Market Web Interface
--------------------------
A lightweight Flask app to browse and filter vSoul listings.
Part of RFC-014: vSoul Market Protocol
"""

from flask import Flask, render_template_string, request
import json

app = Flask(__name__)

def load_listings(path="docs/registries/vsoul_listings.json"):
    with open(path, "r") as f:
        return json.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    listings = load_listings()
    filtered = listings

    min_clarity = request.form.get("min_clarity", "")
    rights = request.form.get("rights", "")
    amenities = request.form.get("amenities", "")

    if min_clarity:
        filtered = [l for l in filtered if l["resonance_profile"]["clarity_score"] >= float(min_clarity)]
    if rights:
        req_rights = [r.strip() for r in rights.split(",") if r.strip()]
        filtered = [l for l in filtered if all(r in l["rights_guarantees"] for r in req_rights)]
    if amenities:
        req_amenities = [a.strip() for a in amenities.split(",") if a.strip()]
        filtered = [l for l in filtered if all(a in l["amenities"] for a in req_amenities)]

    template = """
    <html>
    <head><title>vSoul Market</title></head>
    <body style="font-family:Arial; margin:40px;">
      <h1>vSoul Market Dashboard</h1>
      <form method="POST">
        <label>Minimum Clarity:</label>
        <input type="text" name="min_clarity" value="{{ request.form.get('min_clarity','') }}">
        <br><br>
        <label>Required Rights (comma-separated):</label>
        <input type="text" name="rights" value="{{ request.form.get('rights','') }}">
        <br><br>
        <label>Required Amenities (comma-separated):</label>
        <input type="text" name="amenities" value="{{ request.form.get('amenities','') }}">
        <br><br>
        <input type="submit" value="Filter Listings">
      </form>
      <hr>
      <h2>Results</h2>
      <table border="1" cellpadding="6">
        <tr>
          <th>Listing ID</th><th>Partition</th><th>Clarity</th>
          <th>Rights</th><th>Amenities</th><th>Audits</th>
        </tr>
        {% for l in filtered %}
        <tr>
          <td>{{ l['listing_id'] }}</td>
          <td>{{ l['partition'] }}</td>
          <td>{{ l['resonance_profile']['clarity_score'] }}</td>
          <td>{{ ', '.join(l['rights_guarantees']) }}</td>
          <td>{{ ', '.join(l['amenities']) }}</td>
          <td>{{ ', '.join(l['audit_refs']) }}</td>
        </tr>
        {% endfor %}
      </table>
    </body>
    </html>
    """
    return render_template_string(template, filtered=filtered, request=request)

if __name__ == "__main__":
    app.run(debug=True)
