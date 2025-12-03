input = open("input.txt").readlines()

def bank_to_joltage(bank):
    bank = list(map(int, bank.strip()))
    joltage = []
    nums_left = 12
    while nums_left:
        max_index = len(bank) - nums_left
        battery = max(bank[:max_index+1])
        battery_i = bank.index(battery)
        bank = bank[battery_i+1:]
        nums_left -= 1
        joltage.append(str(battery))
    return int("".join(joltage))

print("res: ", sum(map(bank_to_joltage, input)))

# assert (bank_to_joltage("987654321111111") == 987654321111)
# assert (bank_to_joltage("811111111111119") == 811111111119)
# assert (bank_to_joltage("234234234234278") == 434234234278)
# assert (bank_to_joltage("818181911112111") == 888911112111)
