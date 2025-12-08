from io import StringIO
import heapq
from functools import reduce
from itertools import combinations
from operator import mul
from collections import Counter
from math import sqrt, pow, dist
from util import cstr, COLOR, FORMAT


# inp = StringIO("""162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689
# """)
inp = open("input.txt")

class UnionFind:
    def __init__(self, elements):
        self.parent = {}
        self.rank = {}
        self.set_num = 0
        for e in elements:
            self.find(e)

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            self.set_num += 1
            return x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return self.set_num

        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] -= 1

        self.set_num -= 1
        return self.set_num

boxes = list(tuple(map(int, c.strip().split(","))) for c in inp)
uf = UnionFind(boxes)
dists = sorted([(dist(l, r), (l, r)) for l, r in combinations(boxes, 2)])
for _, (this, that) in dists:
    if uf.union(this, that) == 1:
        assert(this[0] * that[0] == 8135565324)
        break
