import math
import numpy as np

from functools import cache
from io import StringIO
from collections import deque
from itertools import combinations
from util import cstr, COLOR, FORMAT
from util import Vec

# inp = StringIO("""\
# 7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3
# """)
inp = open("input.txt")

class Line:
    def __init__(self, args):
        self.start = args[0]
        self.end = args[1]

    def is_left(self):
        return self.is_horizontal() and self.start.x > self.end.x

    def is_right(self):
        return self.is_horizontal() and not self.is_left()

    def is_up(self):
        return self.is_vertical() and self.start.y > self.end.y

    def is_down(self):
        return self.is_vertical() and not self.is_up()

    def is_vertical(self):
        return self.start.x == self.end.x

    def is_horizontal(self):
        return self.start.y == self.end.y

    def overlap_rectangle(self, this, that):
        if self.is_vertical():
            x = self.start.x
            rectangle_left_x = min(this.x, that.x)
            rectangle_right_x = max(this.x, that.x)
            if not rectangle_left_x < x < rectangle_right_x:
                return False

            top_y = min(self.start.y, self.end.y)
            bottom_y = max(self.start.y, self.end.y)
            rectangle_top_y = min(this.y, that.y)
            rectangle_bottom_y = max(this.y, that.y)

            if top_y < rectangle_top_y and rectangle_bottom_y < bottom_y:
                # print("   overlap: ", self, this, that)
                return True

            if rectangle_top_y < top_y < rectangle_bottom_y:
                # print("   overlap: ", self, this, that)
                return True

            if rectangle_top_y < bottom_y < rectangle_bottom_y:
                # print("   overlap: ", self, this, that)
                return True

            return False

        elif self.is_horizontal():
            y = self.start.y
            rectangle_top_y = min(this.y, that.y)
            rectangle_bottom_y = max(this.y, that.y)
            if not rectangle_top_y < y < rectangle_bottom_y:
                return False

            left_x = min(self.start.x, self.end.x)
            right_x = max(self.start.x, self.end.x)
            rectangle_left_x = min(this.x, that.x)
            rectangle_right_x = max(this.x, that.x)

            if left_x < rectangle_left_x and rectangle_right_x < right_x:
                # print("   overlap: ", self, this, that)
                return True

            if rectangle_left_x < left_x < rectangle_right_x:
                # print("   overlap: ", self, this, that)
                return True

            if rectangle_left_x < right_x < rectangle_right_x:
                # print("   overlap: ", self, this, that)
                return True

            return False
        else:
            assert False

    def __repr__(self):
        return "Line(" + repr(self.start) + ", " + repr(self.end) + ")"

points = list(Vec(map(int, p.strip().split(","))) for p in inp)
lines = list(map(Line, zip(points, points[1:])))
lines.append(Line((points[-1], points[0])))

# find points that can belong to correct rectangle diagonals
top_left_points = set(points)
top_right_points = set(points)
bottom_left_points = set(points)
bottom_right_points = set(points)
for l in lines:
    if l.is_left():
        top_left_points.discard(l.end)
        top_right_points.discard(l.start)
    elif l.is_right():
        bottom_left_points.discard(l.start)
        bottom_right_points.discard(l.end)
    elif l.is_up():
        bottom_right_points.discard(l.start)
        top_right_points.discard(l.end)
    elif l.is_down():
        bottom_left_points.discard(l.end)
        top_left_points.discard(l.start)
    else:
        assert False

# NOTE min line len is > 2, which means that there are no parallel lines with no space
# between them. Which, in turn, means that if there is a point within a given rectangle
# then there will be some empty space. In fact, if any line is within a rectangle then
# there will be a space inside it.

# emit corners of rectangles that are good candidates and do not overlap with lines
def rectangles():
    # rectangles defined by top_left to bottom_right points
    for this in top_left_points:
        for that in bottom_right_points:
            if this == that: continue
            if this.x > that.x: continue
            if this.y > that.y: continue
            if any(l.overlap_rectangle(this, that) for l in lines):
                continue
            yield this, that

    # rectangles defined by bottom_left to top_right points
    for this in bottom_left_points:
        for that in top_right_points:
            if this == that: continue
            if this.x > that.x: continue
            if this.y < that.y: continue
            if any(l.overlap_rectangle(this, that) for l in lines):
                continue
            yield this, that


max_area = -1
for this, that in rectangles():
    width = abs(this.x - that.x) + 1
    height = abs(this.y - that.y) + 1
    max_area = max(max_area, width*height)

# 126993813 - wrong
# 1125903 - wrong
# 110119983 - wrong
# 126993813 - wrong
# 1394728794 - too low
# 1550760868 - correct
# 4376266962 - too high
# 4653198672 - too high
# 4748985168 - too high

# assert(max_area == 24)
assert(max_area == 1550760868)
