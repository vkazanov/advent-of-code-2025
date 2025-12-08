from io import StringIO
from functools import reduce
from operator import mul
from collections import Counter
from math import sqrt, pow
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
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.set_num = 0

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
            return False, self.set_num

        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] -= 1

        self.set_num -= 1
        return True, self.set_num

boxes = list(tuple(map(int, c.strip().split(","))) for c in inp)
print("Boxes collected: ", len(boxes))

dists = {}
for l, r in ((l, r) for l in boxes for r in boxes if l != r):
    if (l, r) in dists or (r, l) in dists: continue
    dists[(l, r)] = (l[0] - r[0])**2 + (l[1] - r[1])**2 + (l[2] - r[2])**2
print("Dists collected: ", len(dists))

uf = UnionFind()
for b in boxes:
    uf.find(b)
print("UF built")

dists = sorted(((v, k) for k, v in dists.items()), reverse=True)
while True:
    _, (this, that)  = dists.pop()
    _, set_num = uf.union(this, that)
    if set_num == 1:
        assert(this[0] * that[0] == 8135565324)
        break
print("Dists merged")
