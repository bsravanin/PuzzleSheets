PuzzleSheets
============
A script to parse .puz files. Today it just prints out the clues and grid.
TODO: Add support to actually generate a spreadsheet.

Installation
------------
1. Clone or download [the code](https://github.com/bsravanin/PuzzleSheets).
1. Run the following commands from a terminal:
   1. `cd PuzzleSheets`
   1. `tox -e py39`

Usage
-----
1. `source .tox/py39/bin/activate`
1. `./puzzle_sheets/puzzle_sheets.py <puz_file_path>`