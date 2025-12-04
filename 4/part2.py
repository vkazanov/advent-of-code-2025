from util import cstr, COLOR, FORMAT
from io import StringIO

input = open("input.txt")

# input = """
# ..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.
# """.strip().splitlines()

N = (-1, 0)
NE = (-1, 1)
E = (0, 1)
SE = (1, 1)
S = (1, 0)
SW = (1, -1)
W = (0, -1)
NW = (-1, -1)
ALL_DIRS = [N, NE, E, SE, S, SW, W, NW]



def neighbours(cell):
    r, c = cell
    for diff_r, diff_c in ALL_DIRS:
        yield r + diff_r, c + diff_c

# Take 1, my naive approach

cells = {}
for r, row in enumerate(input):
    for c in (col for col, ch in enumerate(row) if ch == "@"):
        cell = (r, c)
        cells[cell] = 0

for cell in cells:
    for n in (n for n in neighbours(cell) if n in cells):
        cells[n] += 1

removed = 0
while True:
    did_remove = False
    for cell in [c for c in cells.keys() if cells[c] < 4]:
        del cells[cell]
        did_remove = True
        removed += 1
        for target in [n for n in neighbours(cell) if n in cells]:
            cells[target] -= 1
    if did_remove is False:
        break

assert(removed == 8354)

# Take 2, set-based solution, inspired by Reddit
#

def neighbours(cell):
    r, c = cell
    for diff_r, diff_c in ALL_DIRS:
        yield r + diff_r, c + diff_c

cells = {(r, c) for r, row in enumerate(open("input.txt"))
                for c in (col for col, ch in enumerate(row) if ch == "@")}
orig_len = len(cells)

while True:
    prev_len = len(cells)
    cells &= {cell for cell in cells if len(cells & set(neighbours(cell))) >= 4}
    if prev_len == len(cells): break

assert(orig_len - len(cells) == 8354)
