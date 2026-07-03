import json, pandas as pd, requests
from bs4 import BeautifulSoup
import pdfplumber
from datetime import datetime
from urllib.parse import urlparse

# Load source definitions
def load_sources():
    with open("Good_Vibrations_sources.json") as f:
        return json.load(f)

# Extractor: NIST Vibrational Frequencies (PDF)
def parse_nist_pdf(path):
    with pdfplumber.open(path) as pdf:
        table = pdf.pages[0].extract_table()
        rows = []
        for row in table[1:]:
            rows.append({
                "name": row[0],
                "frequency_hz": float(row[1]) * 1e12,
                "conditions": row[2],
                "notes": row[3],
                "domain": "molecular",
                "source": "NIST"
            })
    return pd.DataFrame(rows)

# Extractor: Bruker NMR Frequencies (PDF)
def parse_bruker_pdf(path):
    with pdfplumber.open(path) as pdf:
        table = pdf.pages[0].extract_table()
        rows = []
        for row in table[1:]:
            rows.append({
                "name": row[0],
                "frequency_hz": float(row[1]) * 1e6,
                "spin": row[2],
                "field_strength": row[3],
                "notes": row[4],
                "domain": "isotopic",
                "source": "Bruker"
            })
    return pd.DataFrame(rows)

def _is_allowed_html_source_url(url):
    try:
        parsed = urlparse(url)
    except Exception:
        return False

    if parsed.scheme != "https":
        return False

    host = (parsed.hostname or "").lower()
    return host == "wikipedia.org" or host.endswith(".wikipedia.org")

# Extractor: Wikipedia Particle Resonance (HTML)
def parse_wikipedia_html(url):
    if not _is_allowed_html_source_url(url):
        raise ValueError(f"Disallowed HTML source URL: {url}")
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"class": "wikitable"})
    rows = []
    for tr in table.find_all("tr")[1:]:
        tds = tr.find_all("td")
        if len(tds) >= 4:
            rows.append({
                "name": tds[0].text.strip(),
                "mass_mev": float(tds[1].text.strip()),
                "width_mev": float(tds[2].text.strip()),
                "lifetime_s": float(tds[3].text.strip()),
                "notes": "Subatomic resonance",
                "domain": "subatomic",
                "source": "Wikipedia"
            })
    return pd.DataFrame(rows)

# Merge and refresh the CSV
def refresh_resonance_csv():
    sources = load_sources()
    all_data = []

    for src in sources:
        if src["parser"] == "pdf_table" and "nist" in src["url"]:
            df = parse_nist_pdf("nist_vibrations.pdf")
        elif src["parser"] == "pdf_table" and "bruker" in src["url"]:
            df = parse_bruker_pdf("bruker_nmr.pdf")
        elif src["parser"] == "html_table":
            df = parse_wikipedia_html(src["url"])
        else:
            continue
        all_data.append(df)

    merged = pd.concat(all_data, ignore_index=True)
    merged.to_csv("Good_Vibrations.csv", index=False)
    print(f"Refreshed Good_Vibrations.csv at {datetime.now()}")

if __name__ == "__main__":
    refresh_resonance_csv()
