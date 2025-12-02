input = open("input.txt").read().strip()

acc = 0
for interval in input.split(","):
    start, end = interval.split("-")
    start, end = int(start), int(end)
    for i in range(start, end + 1):
        cand = str(i)
        if len(cand) % 2:
            continue
        l = cand[: (len(cand) // 2)]
        r = cand[(len(cand) // 2) + len(cand) % 2 :]
        if l == r:
            acc += i
print("res: ", acc, acc == 19386344315)
