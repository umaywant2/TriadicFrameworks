# cli.py
import argparse
from tfe_core import TriadicFrameworks

def main():
    parser = argparse.ArgumentParser(prog="resonance tfe", description="Triadic Frameworks for Everything CLI Tool")
    parser.add_argument("--define", action="store_true", help="Show the definition of TFE")
    parser.add_argument("--apply", type=str, help="Apply TFE to a specific domain")
    parser.add_argument("--domains", action="store_true", help="List available domains")
    parser.add_argument("--export", type=str, help="Export a domain's triadic mapping as JSON")

    args = parser.parse_args()
    tfe = TriadicFrameworks()

    if args.define:
        print(tfe.define())
    elif args.apply:
        print(tfe.apply(args.apply))
    elif args.domains:
        print(tfe.list_domains())
    elif args.export:
        print(tfe.export(args.export))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
