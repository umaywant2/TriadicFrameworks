from flask import Flask, jsonify, request
import yaml

app = Flask(__name__)

with open("registry/archive/archive_index.yml", "r") as stream:
    archive_index = yaml.safe_load(stream)["archive_index"]

@app.route("/archive/glyph/<glyph>", methods=["GET"])
def get_by_glyph(glyph):
    return jsonify({"glyph": glyph, "scrolls": archive_index["glyph_type"].get(glyph, [])})

@app.route("/archive/tag/<tag>", methods=["GET"])
def get_by_tag(tag):
    return jsonify({"tag": tag, "scrolls": archive_index["tags"].get(tag, [])})

@app.route("/archive/lineage/<parent_scroll>", methods=["GET"])
def get_by_lineage(parent_scroll):
    return jsonify({"parent_scroll": parent_scroll, "children": archive_index["lineage"]["parent_scrolls"].get(parent_scroll, [])})

@app.route("/archive/<scroll_id>", methods=["GET"])
def get_scroll_metadata(scroll_id):
    # Stub: load scroll metadata from archive
    return jsonify({"id": scroll_id, "glyph_distribution": {"◆": 1}, "tags": ["fluid-turbulent"]})

@app.route("/archive/remix", methods=["POST"])
def remix_scroll():
    data = request.json
    new_scroll_id = "scroll-" + str(len(archive_index["glyph_type"]["◆"]) + 100)
    return jsonify({"new_scroll_id": new_scroll_id, "status": "remix_success", "lineage": {"parents": data["parent_scrolls"], "children": []}})
