from z3 import *
from io import StringIO

# inp = StringIO("""\
# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
# """)
inp = open("input.txt")

def find_min_solution(target, vectors):
    n = len(vectors)

    opt = Optimize()

    # only use positive counts
    counts = [Int(f"c{i}") for i in range(n)]
    for c in counts:
        opt.add(c >= 0)

    # check target
    for j in range(len(target)):
        opt.add(Sum([counts[i] * vectors[i][j] for i in range(n)]) == target[j])

    # minimize number of vectors used
    opt.minimize(Sum(counts))

    if opt.check() == sat:
        return sum(opt.model().evaluate(counts[i]).as_long() for i in range(n))
    else:
        raise ValueError("No solution")

total = 0
for line in inp:
    line = line.strip().split()
    target = list(map(int, line[-1][1:-1].split(",")))
    buttons = [tuple(map(int, b[1:-1].split(","))) for b in line[1:-1]]
    vectors = [list(1 if i in button else 0 for i in range(len(target)))
               for button in buttons]

    total += find_min_solution(target, vectors)

print(total)
assert(total == 21824)
