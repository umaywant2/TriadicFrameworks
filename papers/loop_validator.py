import json

def validate_loops(matrix_path="loop_validation_matrix.json"):
    with open(matrix_path, "r") as f:
        matrix = json.load(f)

    print("🔍 Loop Validation Report\n")
    for theme, data in matrix.items():
        status = "✅ Valid" if data["equations"] and data["reproducibility"] else "❌ Incomplete"
        print(f"🧭 Theme: {theme}")
        print(f"📄 Papers: {', '.join(data['papers'])}")
        print(f"🔁 Loop Type: {data['loop_type']}")
        print(f"📊 Status: {status}\n")

if __name__ == "__main__":
    validate_loops()
