#! /usr/bin/env python3

import puz
import sys

def get_clue_str(clue):
    return f'{clue["num"]}. {clue["clue"]} ({clue["len"]})'

puzzle = puz.read(sys.argv[1])

print('ACROSS')
for clue in puzzle.clue_numbering().across:
    print(get_clue_str(clue))

print('DOWN')
for clue in puzzle.clue_numbering().down:
    print(get_clue_str(clue))

for row in range(puzzle.height):
    cell = row * puzzle.width
    # Substitute puzzle.solution for p.fill to print the answers
    print(' '.join(puzzle.fill[cell:cell + puzzle.width]))
