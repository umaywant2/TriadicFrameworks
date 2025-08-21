"""
triadic_paths.py
Centralized path definitions for TriadicFrameworks repo.
Used by validators, badge triggers, onboarding scripts, and remix lineage trackers.
"""

import os

# 🔹 Root directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# 🔹 Core folders
BADGES_DIR       = os.path.join(ROOT_DIR, "badges")
CURRICULUM_DIR   = os.path.join(ROOT_DIR, "curriculum")
DATA_DIR         = os.path.join(ROOT_DIR, "data")
DOCS_DIR         = os.path.join(ROOT_DIR, "docs")
EQUATIONS_DIR    = os.path.join(ROOT_DIR, "equations")
HONOR_ROLL_DIR   = os.path.join(ROOT_DIR, "honor_roll")
LABS_DIR         = os.path.join(ROOT_DIR, "labs")
PAPERS_DIR       = os.path.join(ROOT_DIR, "papers")
VALIDATION_DIR   = os.path.join(ROOT_DIR, "validation")

# 🔹 Key files
README_PATH      = os.path.join(ROOT_DIR, "README.md")
MANIFEST_PATH    = os.path.join(ROOT_DIR, "repo_manifest.yaml")

# 🔹 Utility
def echo_path(name, path):
    print(f"🔗 {name}: {path}")

if __name__ == "__main__":
    echo_path("Root", ROOT_DIR)
    echo_path("Badges", BADGES_DIR)
    echo_path("Curriculum", CURRICULUM_DIR)
    echo_path("Honor Roll", HONOR_ROLL_DIR)
    echo_path("Labs", LABS_DIR)
