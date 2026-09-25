# cli.py
import argparse
from numbers_core import TriadicNumbers

def main():
    parser = argparse.ArgumentParser(prog="resonance numbers", description="Triadic Number Genesis CLI Tool")
    parser.add_argument("--genesis", type=int, help="Generate triadic genesis up to N dimensions")
    parser.add_argument("--map", type=str, help="Map a symbolic sequence (E M OC) into triadic numbers")
    parser.add_argument("--export", type=int, help="Export triadic lattice as JSON up to N dimensions")

    args = parser.parse_args()
    tn = TriadicNumbers()

    if args.genesis:
        print(tn.genesis(args.genesis))
    elif args.map:
        print(tn.map_sequence(args.map))
    elif args.export:
        print(tn.export(args.export))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

