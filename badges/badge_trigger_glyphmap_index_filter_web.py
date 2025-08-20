import streamlit as st
import pandas as pd
import json

# Placeholder parser
def load_data():
    return pd.DataFrame([
        {"Glyph": "🜁", "Theme": "Elemental & Spectrum", "Paper Title": "Spectral Flux and Divisional Resonance Is Born", "Validated": False},
        {"Glyph": "🧠", "Theme": "Cognitive & Symbolic", "Paper Title": "Improving ISO Standards with Triadic Frameworks", "Validated": False},
        {"Glyph": "🎶", "Theme": "Music & Symbolic Extensions", "Paper Title": "Triadic Framework for Music – With Quadratic Extensions", "Validated": True},
        {"Glyph": "⚛️", "Theme": "Quantum & Particle Vision", "Paper Title": "Triadic Framework Technology for Quantum Computers", "Validated": False},
        {"Glyph": "🪐", "Theme": "Planetary & Temporal Mapping", "Paper Title": "Resonant Time – Operationalizing Zhang’s Triadic Ontology", "Validated": True},
        {"Glyph": "🩺", "Theme": "Health & Ultrasound", "Paper Title": "Triadic Ultrasound Enhancement", "Validated": False},
        {"Glyph": "🔧", "Theme": "Engineering & Firmware", "Paper Title": "Triadic Framework for ARM and x86 Processors", "Validated": True},
        {"Glyph": "⚡", "Theme": "Energy & Wireless Power", "Paper Title": "WiFi_Energy_Protocols", "Validated": False}
    ])

# Streamlit UI
st.set_page_config(page_title="Glyphmap Filter Dashboard", layout="wide")
st.title("🔮 Badge Trigger Glyphmap Filter Dashboard")

df = load_data()

glyphs = sorted(df["Glyph"].unique())
themes = sorted(df["Theme"].unique())

selected_glyph = st.selectbox("Select Glyph", [""] + glyphs)
selected_theme = st.selectbox("Select Theme", [""] + themes)
validated_only = st.checkbox("Show only validated papers")

# Apply filters
filtered_df = df.copy()
if selected_glyph:
    filtered_df = filtered_df[filtered_df["Glyph"] == selected_glyph]
if selected_theme:
    filtered_df = filtered_df[filtered_df["Theme"] == selected_theme]
if validated_only:
    filtered_df = filtered_df[filtered_df["Validated"] == True]

st.subheader("📄 Filtered Results")
st.dataframe(filtered_df)

# Export options
st.subheader("📤 Export")
export_format = st.radio("Choose format", ["CSV", "JSON"])
if st.button("Export"):
    if export_format == "CSV":
        filtered_df.to_csv("badge_trigger_glyphmap_index_filtered.csv", index=False)
        st.success("CSV exported.")
    else:
        json_data = filtered_df.to_dict(orient="records")
        with open("badge_trigger_glyphmap_index_filtered.json", "w") as f:
            json.dump(json_data, f, indent=2)
        st.success("JSON exported.")
