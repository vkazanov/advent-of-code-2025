from io import StringIO
from operator import add, mul
from functools import reduce
from util import cstr, COLOR, FORMAT

# inp = StringIO("""123 328  51 64
#  45 64  387 23
#   6 98  215 314
# *   +   *   +  """)
inp = open("input.txt")

op_to_fun = { "*": mul, "+": add }

lines = []
ops = None
results = []
for l in inp:
    chars = l.strip().split()
    if chars[0] not in "*+":
        lines.append(list(map(int, chars)))
    else:
        ops = chars
print(ops)

for c in range(len(lines[0])):
    results.append(reduce(op_to_fun[ops[c]], (lines[r][c] for r in range(len(lines)))))
    print("col", c, " = ", results[-1])

print(results)
print(sum(results))
# 6371789548221 - too
assert(sum(results) == 4277556)
