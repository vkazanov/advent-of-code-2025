input = open("input.txt").readlines()

def bank_to_joltage(bank):
    bank = bank.strip()
    max_to_right = -1
    found = []
    for battery in map(int, reversed(bank)):
        if max_to_right >= 0:
            found.append((battery * 10 + max_to_right))
        if battery > max_to_right:
            max_to_right = battery
    return max(found)

print("res: ", sum(map(bank_to_joltage, input)))
# assert (bank_to_joltage("987654321111111") == 98)
# assert (bank_to_joltage("811111111111119") == 89)
# assert (bank_to_joltage("234234234234278") == 78)
# assert (bank_to_joltage("818181911112111") == 92)
