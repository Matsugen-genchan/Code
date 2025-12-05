"""Command-line entrypoint for MedNote."""
from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the CLI."""
    parser = argparse.ArgumentParser(
        prog="mednote",
        description="Manage personal medical notes and simple automations.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="mednote 0.1.0",
        help="Show the current version and exit.",
    )
    return parser


def main() -> None:
    """Run the MedNote CLI."""
    parser = build_parser()
    parser.print_help()


if __name__ == "__main__":
    main()
