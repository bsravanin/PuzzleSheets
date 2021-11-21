#! /usr/bin/env python3
import argparse
import os
import sys

sys.path.insert(0, os.getcwd())

from puzzle_sheets import puzzle_parser


def _create_parser():
    """Creates arg parser."""
    parser = argparse.ArgumentParser(description='Interface for Puzzle Sheets.')
    parser.add_argument('-f', '--file', action='store', required=True, help='Path to input .PUZ file.')
    parser.add_argument('-d', '--display', action='store_true', help='Display file contents on terminal.')
    parser.add_argument('-x', '--xlsx', action='store_true', help='Write file contents to a .XLSX.')
    return parser.parse_args()


def main():
    """Main function that will be run if this is used as a script instead of imported."""
    args = _create_parser()

    puz_path = args.file
    puzzle = puzzle_parser.validate(puz_path)
    if puzzle is None:
        sys.exit(-1)

    if args.display:
        puzzle_parser.display(puzzle)
    if args.xlsx:
        puzzle_parser.write_xlsx(puz_path, puzzle)


if __name__ == '__main__':
    main()
