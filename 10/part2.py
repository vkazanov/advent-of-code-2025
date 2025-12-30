import heapq
from math import inf
from io import StringIO
from util import cstr, COLOR, FORMAT
from collections import deque

inp = StringIO("""\
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
""")
# inp = StringIO("[##.#..] (0,2,3,5) (0,2,3,4) (0,1,2,4) (1,4) (2,3,4,5) (1,4,5) (0,3,4) (3) {56,191,62,82,236,212}")
# inp = StringIO("[...###.#.#] (1,8) (0,4,5,6) (2,3,4,5,6,7,8) (5) (0,3,5) (0,1,5,6,7,9) (0,7,9) (0,1,2,3,5,6,8,9) (0,1,2,3,4,5,7,8,9) (0,2,4,6,7,8,9) (1,2,3,4,6,7,8,9) (0,9) {65,41,48,35,50,67,76,68,55,61}")
inp = open("input.txt")

def press(joltages, button, presses):
    joltages_next = list(joltages)
    for i in button:
        joltages_next[i] += presses
    return tuple(joltages_next)


def find_min(joltage_target, buttons):
    count = 0

    seen = set()

    def heuristic(joltage):
        return sum(joltage_target[i] - joltage[i] for i in range(len(joltage_target)))

    pq = [(sum(joltage_target), 0, (0,)*len(joltage_target))]
    while True:
        count += 1
        h, steps, joltage = heapq.heappop(pq)

        # circuit breaking
        if joltage in seen:
            continue
        seen.add(joltage)

        # found closest
        if joltage == joltage_target:
            print("count: ", count, steps)
            return steps

        # press
        for button in buttons:
            # joltage_next = press(joltage, button, 1)
            # if any(joltage_next[i] > joltage_target[i] for i in button):
            #         continue

            # steps_next = steps + 1
            # h_next = h + heuristic(joltage_next)
            # heapq.heappush(pq, (h_next, steps_next, joltage_next))

            min_diff = min(joltage_target[i] - joltage[i] for i in button)
            while min_diff:
                joltage_next = press(joltage, button, min_diff)
                steps_next = steps + min_diff
                h_next = h + heuristic(joltage_next)
                heapq.heappush(pq, (h_next, steps_next, joltage_next))
                min_diff -= 1

    assert False

total = 0
for line in inp:
    line = line.strip().split()
    target = tuple(map(int, line[-1][1:-1].split(",")))
    # print(target)
    buttons = [tuple(map(int, b[1:-1].split(","))) for b in line[1:-1]]
    # print(buttons)
    steps = find_min(target, buttons)
    # print(steps)
    total += steps

print(total)
