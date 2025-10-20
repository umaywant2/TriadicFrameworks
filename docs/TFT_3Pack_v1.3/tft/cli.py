import argparse
from .nous import processor
from .entft import encryptor
from .tops import grid_ops

def main():
    parser = argparse.ArgumentParser(
        prog="tft",
        description="TFT 3-Pack Unified Shell — Resonance Clarity Edition"
    )
    subparsers = parser.add_subparsers(dest="command")

    # 🧠 Logic Core: nous
    nous_parser = subparsers.add_parser("nous", help="Symbolic cognition and validator overlays")
    nous_parser.add_argument("-validate", required=True, help="Scroll or glyph to validate")
    nous_parser.add_argument("-mode", choices=["symbolic", "numeric"], default="symbolic", help="Validation mode")
    nous_parser.add_argument("--basetype", default="phi", help="Base lens for symbolic fidelity")

    # 🔐 Encryption: entft
    enc_parser = subparsers.add_parser("entft", help="Encryption and badge trigger logic")
    enc_parser.add_argument("-i", required=True, help="Input file")
    enc_parser.add_argument("-o", required=True, help="Output file")
    enc_parser.add_argument("-k", required=True, help="Key or glyphstream")
    enc_parser.add_argument("--basetype", default="decimal", help="Base lens for encryption overlays")

    # 🌀 Grid Ops: tops
    grid_parser = subparsers.add_parser("tops", help="Corridor traversal and grid simulation")
    grid_parser.add_argument("-map", required=True, help="Corridor map file")
    grid_parser.add_argument("-ops", choices=["simulate", "validate", "echo"], default="simulate", help="Operation mode")
    grid_parser.add_argument("--basetype", default="negabinary", help="Base lens for grid overlays")

    args = parser.parse_args()

    if args.command == "nous":
        processor.run(args.validate, args.mode, args.basetype)
    elif args.command == "entft":
        encryptor.encrypt(args.i, args.o, args.k, args.basetype)
    elif args.command == "tops":
        grid_ops.run(args.map, args.ops, args.basetype)

if __name__ == "__main__":
    main()
