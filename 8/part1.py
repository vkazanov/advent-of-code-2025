from io import StringIO
from functools import reduce
from operator import mul
from collections import Counter
from math import sqrt, pow
from util import cstr, COLOR, FORMAT


inp = StringIO("""162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
""")
inp = open("input.txt")

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            return x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False

        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1

        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)


boxes = list(tuple(map(int, c.strip().split(","))) for c in inp)
print("Boxes collected: ", len(boxes))

dists = list()
for this in boxes:
    for that in boxes:
        if this == that: continue
        dist = sqrt(pow(this[0] - that[0], 2) +
                    pow(this[1] - that[1], 2) +
                    pow(this[2] - that[2], 2))
        dists.append((dist, (this, that)))
print("Dists collected: ", len(dists))

uf = UnionFind()
for b in boxes:
    uf.find(b)
print("UF collected")

dists.sort(reverse=True)
for _ in range(1000):
    dists.pop()
    _, (this, that) = dists.pop()
    uf.union(this, that)
print("Dists merged")

counter = Counter()
for x in boxes:
    counter[uf.find(x)] += 1
print(reduce(mul, (v for k, v in counter.most_common(3))))
