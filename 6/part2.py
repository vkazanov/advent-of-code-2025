from io import StringIO
from operator import add, mul
from functools import reduce
from util import cstr, COLOR, FORMAT

# inp = StringIO(
# """\
# 123 328  51 64
#  45 64  387 23
#   6 98  215 314
# *   +   *   +  """)
inp = open("input.txt")

ops = { "*": (mul, 1), "+": (add, 0) }

lines = inp.readlines()

total = 0
nums = []
op, op_init = add, 0
for c, op_char in enumerate(lines[-1]):
    if op_char in "*+":
        total += reduce(op, nums, op_init)
        op, op_init = ops[op_char]
        nums = []
    num = "".join(lines[r][c] for r in range(len(lines)-1)).strip()
    if num:
        nums.append(int(num))
total += reduce(op, nums, op_init)

assert(total == 11419862653216)
