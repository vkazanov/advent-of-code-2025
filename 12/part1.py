from io import StringIO
from util import cstr, COLOR, FORMAT
from collections import defaultdict
import operator
from functools import reduce

inp = open("input.txt")

shape_sizes = defaultdict(int)
for i in range(6):
    line = inp.readline()
    shape_size = 0
    for _ in range(3):
        line = inp.readline()
        shape_sizes[i] += line.count("#")
    inp.readline()

total, not_fit = 0, 0
for line in inp:
    area, nums = line.strip().split(":")
    area = reduce(operator.mul, map(int, area.split("x")))
    nums = sum(shape_sizes[i]*int(n) for i, n in enumerate(nums.split()))
    total += 1
    if area < nums:
        not_fit +=1
print(not_fit, total)
assert(total - not_fit == 422)
