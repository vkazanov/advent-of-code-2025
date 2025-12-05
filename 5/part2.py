from io import StringIO
from util import cstr, COLOR, FORMAT

inp = open("input.txt")

intervals = []
while (interval := inp.readline().strip()) != "":
    intervals.append(tuple(map(int, interval.split("-"))))
intervals.sort()

current_start, current_end = intervals[0]
total = 0
for start, end in intervals[1:]:
    if start <= current_end:
        current_end = max(current_end, end)
    else:
        total += current_end - current_start + 1
        current_start, current_end = start, end
else:
    total += current_end - current_start + 1

assert(total == 336495597913098)
