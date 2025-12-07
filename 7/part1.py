from io import StringIO
from util import cstr, COLOR, FORMAT

inp = open("input.txt")

# inp = StringIO("""\
# .......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ...............
# """)

first = inp.readline()
start = (0, first.index("S"))
width = len(first)
height = 1

grid = set()
for row, l in enumerate(inp, start=1):
    height += 1
    for col, c in enumerate(l):
        if c == "^":
            grid.add((row, col))

result = set()
beams = [start]
while beams:
    this = row, col = beams.pop()
    if col < 0 or col >= width:
        continue

    if row >= height:
        continue

    if this not in grid:
        beams.append((row + 1, col))
        continue

    if this in grid and this not in result:
        result.add(this)
        beams.append((row, col - 1))
        beams.append((row, col + 1))
        continue

assert(len(result) == 1581)
