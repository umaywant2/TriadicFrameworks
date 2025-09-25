# cli.py
import argparse
from resonant_time import ResonantTime

def main():
    parser = argparse.ArgumentParser(prog="resonance time", description="Resonant-Time CLI Tool")
    parser.add_argument("--define", action="store_true", help="Show the triadic definition of Resonant-Time")
    parser.add_argument("--cycle", type=int, help="Generate a symbolic cycle of Resonant-Time")
    parser.add_argument("--ascii", action="store_true", help="Render cycle as ASCII diagram")
    parser.add_argument("--compare", action="store_true", help="Compare Resonant-Time with conventional time")

    args = parser.parse_args()
    rt = ResonantTime()

    if args.define:
        print(rt.define())
    elif args.cycle:
        print(rt.cycle(args.cycle, ascii=args.ascii))
    elif args.compare:
        print(rt.compare())
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
