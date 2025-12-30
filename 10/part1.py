from math import inf
from io import StringIO
from util import cstr, COLOR, FORMAT
from collections import deque

inp = open("input.txt")
# inp = StringIO("""\
# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
# """)
# inp = StringIO("""\
# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# """)

def press(lights, button):
    lights_next = list(lights)
    for i in button:
        lights_next[i] = not lights[i]
    return tuple(lights_next)

def find_min(target, init, buttons, steps, seen):
    d = deque([(init, 0)])
    while True:
        current, steps = d.popleft()

        # circuit breaking
        if current in seen:
            continue
        seen.add(current)

        # found closest
        if target == current:
            return steps

        # grow
        for b in buttons:
            d.append((press(current, b), steps+1))

    assert False

total = 0
for line in inp:
    line = line.strip().split()
    target = tuple(True if l == "#" else False for l in line[0][1:-1])
    buttons = [tuple(map(int, b[1:-1].split(","))) for b in line[1:-1]]
    steps = find_min(target, (False,)*len(target), buttons, 0, set())
    total += steps

assert total == 514
