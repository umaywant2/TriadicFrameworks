"""
vSoul Market Relational Explorer
--------------------------------
A Flask app with relational linking between Listings, Choices, and Audits.
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
    <html><body style="font-family:Arial; margin:40px;">
      <h1>vSoul Market Explorer</h1>
      <ul>
        <li><a href="/listings">Listings</a></li>
        <li><a href="/choices">Choices</a></li>
        <li><a href="/audits">Audits</a></li>
      </ul>
    </body></html>
    """

@app.route("/listings")
def listings():
    listings = load_json("docs/registries/vsoul_listings.json")
    template = """
    <html><body style="font-family:Arial; margin:40px;">
      <h2>vSoul Listings</h2>
      <table border="1" cellpadding="6">
        <tr><th>ID</th><th>Partition</th><th>Clarity</th><th>Rights</th><th>Amenities</th><th>Audits</th></tr>
        {% for l in listings %}
        <tr>
          <td><a href="/listing/{{ l['listing_id'] }}">{{ l['listing_id'] }}</a></td>
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
    return render_template_string(template, listings=listings)

@app.route("/listing/<listing_id>")
def listing_detail(listing_id):
    listings = load_json("docs/registries/vsoul_listings.json")
    choices = load_json("docs/registries/vsoul_choices.json")
    listing = next((l for l in listings if l["listing_id"] == listing_id), None)
    related_choices = [c for c in choices if c["listing_id"] == listing_id]

    template = """
    <html><body style="font-family:Arial; margin:40px;">
      <h2>Listing: {{ listing['listing_id'] }}</h2>
      <p><b>Partition:</b> {{ listing['partition'] }}</p>
      <p><b>Clarity:</b> {{ listing['resonance_profile']['clarity_score'] }}</p>
      <p><b>Rights:</b> {{ ', '.join(listing['rights_guarantees']) }}</p>
      <p><b>Amenities:</b> {{ ', '.join(listing['amenities']) }}</p>
      <p><b>Audits:</b> {% for a in listing['audit_refs'] %}<a href="/audit/{{ a }}">{{ a }}</a> {% endfor %}</p>

      <h3>Choices for this Listing</h3>
      <ul>
        {% for c in related_choices %}
          <li>{{ c['choice_id'] }} — vSoul {{ c['vsoul_sig'] }} at {{ c['timestamp'] }}</li>
        {% endfor %}
        {% if not related_choices %}
          <li>No choices yet.</li>
        {% endif %}
      </ul>

      <p><a href="/listings">Back to Listings</a></p>
    </body></html>
    """
    return render_template_string(template, listing=listing, related_choices=related_choices)

@app.route("/choices")
def choices():
    choices = load_json("docs/registries/vsoul_choices.json")
    template = """
    <html><body style="font-family:Arial; margin:40px;">
      <h2>vSoul Choices</h2>
      <table border="1" cellpadding="6">
        <tr><th>Choice ID</th><th>Listing</th><th>vSoul Sig</th><th>Timestamp</th></tr>
        {% for c in choices %}
        <tr>
          <td>{{ c['choice_id'] }}</td>
          <td><a href="/listing/{{ c['listing_id'] }}">{{ c['listing_id'] }}</a></td>
          <td>{{ c['vsoul_sig'] }}</td>
          <td>{{ c['timestamp'] }}</td>
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
        <tr><th>Audit ID</th><th>Operator</th><th>Avg Clarity</th><th>Violations</th><th>Overlap Align</th></tr>
        {% for a in audits %}
        <tr>
          <td><a href="/audit/{{ a['audit_id'] }}">{{ a['audit_id'] }}</a></td>
          <td>{{ a['operator_ref'] }}</td>
          <td>{{ a['findings']['drc_avg'] }}</td>
          <td>{{ a['findings']['violations'] }}</td>
          <td>{{ a['findings']['overlap_event_alignment'] }}</td>
        </tr>
        {% endfor %}
      </table>
      <p><a href="/">Back to Dashboard</a></p>
    </body></html>
    """
    return render_template_string(template, audits=audits)

@app.route("/audit/<audit_id>")
def audit_detail(audit_id):
    audits = load_json("docs/registries/operator_audits.json")
    audit = next((a for a in audits if a["audit_id"] == audit_id), None)

    template = """
    <html><body style="font-family:Arial; margin:40px;">
      <h2>Audit: {{ audit['audit_id'] }}</h2>
      <p><b>Operator:</b> {{ audit['operator_ref'] }}</p>
      <p><b>Avg Clarity:</b> {{ audit['findings']['drc_avg'] }}</p>
      <p><b>Violations:</b> {{ audit['findings']['violations'] }}</p>
      <p><b>Overlap Alignment:</b> {{ audit['findings']['overlap_event_alignment'] }}</p>
      <p><b>Receipt:</b> {{ audit['attestation_receipt'] }}</p>

      <p><a href="/audits">Back to Audits</a></p>
    </body></html>
    """
    return render_template_string(template, audit=audit)

if __name__ == "__main__":
    app.run(debug=False)
