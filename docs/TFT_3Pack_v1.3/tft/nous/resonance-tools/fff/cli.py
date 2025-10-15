# cli.py
import argparse
from fff_core import FFF

def main():
    parser = argparse.ArgumentParser(prog="resonance fff", description="Forces, Fluids, Frequency CLI Tool")
    parser.add_argument("--define", action="store_true", help="Show the definition of FFF")
    parser.add_argument("--forces", type=int, help="Simulate N force vectors")
    parser.add_argument("--fluids", type=int, help="Simulate N fluid states")
    parser.add_argument("--frequency", type=int, help="Simulate N oscillation cycles")
    parser.add_argument("--export", action="store_true", help="Export combined triad as JSON")

    args = parser.parse_args()
    fff = FFF()

    if args.define:
        print(fff.define())
    elif args.forces:
        print(fff.simulate_forces(args.forces))
    elif args.fluids:
        print(fff.simulate_fluids(args.fluids))
    elif args.frequency:
        print(fff.simulate_frequency(args.frequency))
    elif args.export:
        print(fff.export())
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

