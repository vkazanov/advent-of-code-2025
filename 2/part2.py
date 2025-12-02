input = open("input.txt").read().strip()
res = 34421651192

# input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
# res = 4174379265

acc = 0
for interval in input.split(","):
    start, end = map(int, interval.split("-"))
    for i in range(start, end + 1):
        cand = str(i)
        for repeat_len in range(1, len(cand) // 2 + 1):
            repeat_cand = cand[:repeat_len]
            if cand.count(repeat_cand) * repeat_len == len(cand):
                acc += i
                break

print("res: ", acc, acc == res)
