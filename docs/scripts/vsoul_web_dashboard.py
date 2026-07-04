"""
vSoul Market Multi-Tab Dashboard
--------------------------------
A Flask app with tabs for Listings, Choices, and Audits.
Part of RFC-014: vSoul Market Protocol
"""

from flask import Flask, render_template_string, request
import json

app = Flask(__name__)

def load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route("/")
def home():
    return """
    <html>
    <head><title>vSoul Market Dashboard</title></head>
    <body style="font-family:Arial; margin:40px;">
      <h1>vSoul Market Dashboard</h1>
      <ul>
        <li><a href="/listings">Listings</a></li>
        <li><a href="/choices">Choices</a></li>
        <li><a href="/audits">Audits</a></li>
      </ul>
    </body>
    </html>
    """

@app.route("/listings", methods=["GET", "POST"])
def listings():
    listings = load_json("docs/registries/vsoul_listings.json")
    filtered = listings

    min_clarity = request.form.get("min_clarity", "")
    if min_clarity:
        filtered = [l for l in filtered if l["resonance_profile"]["clarity_score"] >= float(min_clarity)]

    template = """
    <html><body style="font-family:Arial; margin:40px;">
      <h2>vSoul Listings</h2>
      <form method="POST">
        <label>Minimum Clarity:</label>
        <input type="text" name="min_clarity" value="{{ request.form.get('min_clarity','') }}">
        <input type="submit" value="Filter">
      </form>
      <hr>
      <table border="1" cellpadding="6">
        <tr><th>ID</th><th>Partition</th><th>Clarity</th><th>Rights</th><th>Amenities</th><th>Audits</th></tr>
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
      <p><a href="/">Back to Dashboard</a></p>
    </body></html>
    """
    return render_template_string(template, filtered=filtered, request=request)

@app.route("/choices")
def choices():
    choices = load_json("docs/registries/vsoul_choices.json")
    template = """
    <html><body style="font-family:Arial; margin:40px;">
      <h2>vSoul Choices</h2>
      <table border="1" cellpadding="6">
        <tr><th>Choice ID</th><th>Listing</th><th>vSoul Sig</th><th>Timestamp</th><th>Conditions</th></tr>
        {% for c in choices %}
        <tr>
          <td>{{ c['choice_id'] }}</td>
          <td>{{ c['listing_id'] }}</td>
          <td>{{ c['vsoul_sig'] }}</td>
          <td>{{ c['timestamp'] }}</td>
          <td>{{ c['conditions'] }}</td>
        </tr>
        {% endfor %}
      </table>
      <p><a href="/">Back to Dashboard</a></p>
    </body></html>
    """
    return render_template_string(template, choices=choices)

@app.route("/audits")
def audits():
    audits = load_json("docs/registries/operator_audits.json")
    template = """
    <html><body style="font-family:Arial; margin:40px;">
      <h2>Operator Audits</h2>
      <table border="1" cellpadding="6">
        <tr><th>Audit ID</th><th>Operator</th><th>Avg Clarity</th><th>Violations</th><th>Overlap Align</th><th>Receipt</th></tr>
        {% for a in audits %}
        <tr>
          <td>{{ a['audit_id'] }}</td>
          <td>{{ a['operator_ref'] }}</td>
          <td>{{ a['findings']['drc_avg'] }}</td>
          <td>{{ a['findings']['violations'] }}</td>
          <td>{{ a['findings']['overlap_event_alignment'] }}</td>
          <td>{{ a['attestation_receipt'] }}</td>
        </tr>
        {% endfor %}
      </table>
      <p><a href="/">Back to Dashboard</a></p>
    </body></html>
    """
    return render_template_string(template, audits=audits)

if __name__ == "__main__":
    app.run()
