#! /usr/bin/env python3
from collections import OrderedDict
from collections import namedtuple
from puz import Puzzle

import argparse
import os
import puz
import sys


Solution = namedtuple('Solution', ('num', 'clue', 'len', 'answer'))


def _create_parser():
    """Creates arg parser."""
    parser = argparse.ArgumentParser(description='Interface for Puzzle Sheets.')
    parser.add_argument('-p', '--puz', action='store', required=True, help='Path to PUZ file to be read.')
    return parser.parse_args()


def _get_across_answer(puzzle: Puzzle, clue: dict) -> str:
    """Returns the across answer for a given clue in the puzzle. Any blanks will be indicated by dashes."""
    return puzzle.fill[clue['cell'] : clue['cell'] + clue['len']]


def _get_down_answer(puzzle: Puzzle, clue: dict) -> str:
    """Returns the down answer for a given clue in the puzzle. Any blanks will be indicated by dashes."""
    return ''.join([puzzle.fill[clue['cell'] + i * puzzle.width] for i in range(clue['len'])])


def get_solution_grid(puzzle: Puzzle) -> dict:
    """Returns a dict that contains the whole grid. The dict has 2 keys: across and down. The value of each is
    an OrderedDict whose key is the clue number, and value is a Solution namedtuple."""
    numbering = puzzle.clue_numbering()
    return {
        'across': OrderedDict(
            {
                clue['num']: Solution(clue['num'], clue['clue'], clue['len'], _get_across_answer(puzzle, clue))
                for clue in numbering.across
            }
        ),
        'down': OrderedDict(
            {
                clue['num']: Solution(clue['num'], clue['clue'], clue['len'], _get_down_answer(puzzle, clue))
                for clue in numbering.down
            }
        ),
    }


def _get_clue_str(solution: Solution) -> str:
    """Returns a string representation of the clue, for printing."""
    return f'{solution.num}. {solution.clue} ({solution.len})'


def main():
    """Main function that will be run if this is used as a script instead of imported."""
    args = _create_parser()

    puz_path = args.puz
    if not os.path.isfile(puz_path):
        print('Cannot read file ', puz_path)
        sys.exit(-1)

    puzzle = puz.read(puz_path)
    grid = get_solution_grid(puzzle)

    print('ACROSS')
    for solution in grid['across'].values():
        print(_get_clue_str(solution))

    print('DOWN')
    for solution in grid['down'].values():
        print(_get_clue_str(solution))

    for row in range(puzzle.height):
        cell = row * puzzle.width
        print('\t'.join(puzzle.fill[cell : cell + puzzle.width]).replace('.', chr(9608) * 2))

    print(f'Title: {puzzle.title}')
    print(f'Author: {puzzle.author}')
    print(f'Note: {puzzle.notes}')


if __name__ == '__main__':
    main()
