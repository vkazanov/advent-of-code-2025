from io import StringIO
from collections import defaultdict, deque
from util import cstr, COLOR, FORMAT

inp = StringIO("""\
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
""")
inp = open("input.txt")

from_to = defaultdict(list)
for p in inp:
    fr, to = p.split(": ")
    for t in to.split():
        from_to[fr].append(t)

count = 0
q = deque(["you"])
while q:
    this = q.popleft()
    if this == "out":
        count += 1

    for that in from_to[this]:
        q.append(that)
print(count)
assert(count == 788)

# count = 0
# s = ["you"]
# seen = set()
# while s:
#     this = s.pop()
#     if this in seen: continue
#     if this == "out": continue
#     print(this)
#     seen.add(this)
#     count += 1
#     for that in from_to[this]:
#         s.append(that)

# print(count)
