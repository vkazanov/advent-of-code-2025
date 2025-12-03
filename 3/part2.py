input = open("input.txt").readlines()

def bank_to_joltage(bank):
    bank = list(map(int, bank.strip()))
    joltage = []
    left_i = 0
    right_i = len(bank) - 12 + 1
    while len(joltage) < 12:
        subbank = bank[left_i:right_i]
        battery = max(subbank)
        left_i += subbank.index(battery) + 1
        right_i += 1
        joltage.append(battery)
    return int("".join(map(str, joltage)))

import timeit
print("time: ", timeit.timeit(lambda: sum(map(bank_to_joltage, input)), number=2000))

print("res: ", sum(map(bank_to_joltage, input)))

# assert (bank_to_joltage("987654321111111") == 987654321111)
# assert (bank_to_joltage("811111111111119") == 811111111119)
# assert (bank_to_joltage("234234234234278") == 434234234278)
# assert (bank_to_joltage("818181911112111") == 888911112111)
