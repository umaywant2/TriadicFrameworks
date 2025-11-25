# cli.py
import argparse
from integrate_core import Integrations

def main():
    parser = argparse.ArgumentParser(prog="resonance integrate", description="Integration CLI Tool")
    parser.add_argument("--define", action="store_true", help="Show integration definition")
    parser.add_argument("--demo", action="store_true", help="Run a demo pipeline")
    parser.add_argument("--dashboard", type=str, help="Generate a mythic-scientific dashboard for a domain")

    args = parser.parse_args()
    integ = Integrations()

    if args.define:
        print(integ.define())
    elif args.demo:
        print(integ.demo_pipeline())
    elif args.dashboard:
        print(integ.dashboard(args.dashboard))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

