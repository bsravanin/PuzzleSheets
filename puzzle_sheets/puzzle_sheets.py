#! /usr/bin/env python3

import argparse
import puz


def _create_parser():
    parser = argparse.ArgumentParser(description='Interface for Puzzle Sheets.')
    parser.add_argument('-p', '--puz', action='store', required=True, help='Path to PUZ file to be read.')
    return parser.parse_args()


def get_clue_str(clue):
    return f'{clue["num"]}. {clue["clue"]} ({clue["len"]})'


def main():
    """Main function that will be run if this is used as a script instead of imported."""
    args = _create_parser()

    puzzle = puz.read(args.puz)

    print('ACROSS')
    for clue in puzzle.clue_numbering().across:
        print(get_clue_str(clue))

    print('DOWN')
    for clue in puzzle.clue_numbering().down:
        print(get_clue_str(clue))

    for row in range(puzzle.height):
        cell = row * puzzle.width
        # Substitute puzzle.solution for p.fill to print the answers
        print('\t'.join(puzzle.fill[cell : cell + puzzle.width]).replace('.', chr(9608)))

    print(f'Title: {puzzle.title}')
    print(f'Author: {puzzle.author}')
    print(f'Note: {puzzle.notes}')


if __name__ == '__main__':
    main()
