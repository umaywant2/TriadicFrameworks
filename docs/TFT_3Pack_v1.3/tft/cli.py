import argparse
from .nous import processor
from .entft import encryptor
from .tops import grid_ops

def main():
    parser = argparse.ArgumentParser(prog="tft", description="TFT 3-Pack Unified Shell")
    subparsers = parser.add_subparsers(dest="command")

    # Logic Core: nous
    nous_parser = subparsers.add_parser("nous")
    nous_parser.add_argument("-validate", required=True)
    nous_parser.add_argument("-mode", choices=["symbolic", "numeric"], default="symbolic")

    # Encryption: entft
    enc_parser = subparsers.add_parser("entft")
    enc_parser.add_argument("-i", required=True)
    enc_parser.add_argument("-o", required=True)
    enc_parser.add_argument("-k", required=True)

    # Grid Ops: tops
    grid_parser = subparsers.add_parser("tops")
    grid_parser.add_argument("-map", required=True)
    grid_parser.add_argument("-ops", choices=["simulate", "validate", "echo"], default="simulate")

    args = parser.parse_args()
    if args.command == "nous":
        processor.run(args.validate, args.mode)
    elif args.command == "entft":
        encryptor.encrypt(args.i, args.o, args.k)
    elif args.command == "tops":
        grid_ops.run(args.map, args.ops)

if __name__ == "__main__":
    main()
