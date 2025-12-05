from io import StringIO
from util import cstr, COLOR, FORMAT

inp = open("input.txt")

intervals = []
while (interval := inp.readline().strip()) != "":
    intervals.append(tuple(map(int, interval.split("-"))))
intervals.sort()

acc = 0
i = 0
while i < len(intervals):
    i_l, i_r = intervals[i]
    for j in range(i+1, len(intervals)):
        j_l, j_r = intervals[j]
        if i_r < j_l:
            # no overlap, stop
            i = j
            break
        else:
            # overlap, extending
            i_r = max(j_r, i_r)
    else:
        i = j + 1

    acc += i_r - i_l + 1

assert(acc == 336495597913098)
