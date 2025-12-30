import math
from io import StringIO
from itertools import combinations
from util import cstr, COLOR, FORMAT

inp = StringIO("""\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""")
inp = open("input.txt")

tiles = list(tuple(map(int, c.strip().split(","))) for c in inp)
res = (max(abs(l[0]-r[0] + 1) * abs(l[1]-r[1] + 1) for l, r in combinations(tiles, 2)))
assert(res == 4748985168)
