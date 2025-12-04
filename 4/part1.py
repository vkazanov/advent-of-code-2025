from util import cstr, COLOR, FORMAT

input = open("input.txt").read().strip().splitlines()

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

max_r, max_c = 0, 0
cells = {}
for r, row in enumerate(input):
    for c, col in enumerate(row):
        cells[(r, c)] = col == "@"
        if r > max_r: max_r = r
        if c > max_c: max_c = c

cell_to_count = {}
for r, c in cells:
    if cells[r, c]:
        for diff_r, diff_c in ALL_DIRS:
            target = target_r, target_c = r + diff_r, c + diff_c
            if not cells.get(target): continue
            if target_r > max_r or target_r < 0: continue
            if target_c > max_c or target_c < 0: continue
            cell_to_count[target] = cell_to_count.get(target, 0) + 1

count = 0
for r in range(max_r+1):
    for c in range(max_c+1):
        if cells.get((r, c)) and cell_to_count.get((r, c), 0) < 4:
            count += 1

print(count)
