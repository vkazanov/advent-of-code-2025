from io import StringIO
from util import cstr, COLOR, FORMAT

inp = open("input.txt")
# inp = StringIO("""3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32
# """)

fresh = []
while (interval := inp.readline().strip()) != "":
    l, r = map(int, interval.split("-"))
    fresh.append((l, r))

print("done reading intervals")

acc = 0
while ingr := inp.readline().strip():
    ingr = int(ingr)
    for (l, r) in fresh:
        if l <= ingr <= r:
            acc += 1
            break

assert(acc == 613)
print(acc)
