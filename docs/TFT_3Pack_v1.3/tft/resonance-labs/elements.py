# 🧪 Elemental Resonance Simulator
# Reads elemental profiles from YAML and simulates FFF emitter response using TFE logic.

import yaml
import os

# Load elemental config
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'elements.yaml')

def load_elements(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

# FFF Emitter Logic
def simulate_resonance(element):
    print(f"\n🔬 Simulating: {element['name']} ({element['symbol']})")
    print(f"Stub: {element.get('stub', '—')}")
    
    print("\n→ Forces:")
    for k, v in element['forces'].items():
        print(f"  {k.replace('_', ' ').title()}: {v}")
    
    print("\n→ Fluids:")
    for k, v in element['fluids'].items():
        if isinstance(v, list):
            print(f"  {k.replace('_', ' ').title()}: {', '.join(v)}")
        else:
            print(f"  {k.replace('_', ' ').title()}: {v}")
    
    print("\n→ Frequency:")
    for k, v in element['frequency'].items():
        print(f"  {k.replace('_', ' ').title()}: {v}")
    
    print("\n📝 Notes:")
    print(f"  {element.get('notes', 'No notes available.')}")
    print("-" * 40)

# Main Simulation Loop
if __name__ == "__main__":
    data = load_elements(CONFIG_PATH)
    elements = data.get('elements', [])
    
    print("🌐 Triadic Resonance Simulation Engine")
    print(f"Framework: {data['meta']['framework']} | Version: {data['meta']['version']}")
    print(f"Components: {', '.join(data['meta']['components'])}")
    print("=" * 40)
    
    for element in elements:
        simulate_resonance(element)
