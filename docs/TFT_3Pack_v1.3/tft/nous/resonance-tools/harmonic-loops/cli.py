# cli.py
import argparse
from loops_core import HarmonicLoops

def main():
    parser = argparse.ArgumentParser(prog="resonance loops", description="Harmonic Nested Loops CLI Tool")
    parser.add_argument("--nest", type=int, help="Generate a nested loop of depth N")
    parser.add_argument("--feedback", type=int, help="Simulate feedback amplification for N iterations")
    parser.add_argument("--export", type=int, help="Export nested loop structure as JSON")

    args = parser.parse_args()
    hl = HarmonicLoops()

    if args.nest:
        print(hl.nest(args.nest))
    elif args.feedback:
        print(hl.feedback(args.feedback))
    elif args.export:
        print(hl.export(args.export))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
