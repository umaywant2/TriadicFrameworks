# cli.py
import argparse
from tft_core import TFT

def main():
    parser = argparse.ArgumentParser(prog="resonance tft", description="Triadic Framework Technology CLI Tool")
    parser.add_argument("--define", action="store_true", help="Show the definition of TFT")
    parser.add_argument("--apply", type=str, help="Apply TFT to a specific domain")
    parser.add_argument("--compare", action="store_true", help="Compare triadic vs quadratic extensions")
    parser.add_argument("--export", type=str, help="Export a domain's TFT mapping with quadratic lattice as JSON")

    args = parser.parse_args()
    tft = TFT()

    if args.define:
        print(tft.define())
    elif args.apply:
        print(tft.apply(args.apply))
    elif args.compare:
        print(tft.compare())
    elif args.export:
        print(tft.export(args.export))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

