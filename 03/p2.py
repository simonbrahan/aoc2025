def get_highest_num_idx(nums):
    highest_idx = 0
    for idx, num in enumerate(nums):
        if num > nums[highest_idx]:
            highest_idx = idx

    return highest_idx


def get_highest_batteries(bank, battery_count):
    if battery_count == 0:
        return []

    if battery_count > 1:
        candidate_bank = bank[: -(battery_count - 1)]
    else:
        candidate_bank = bank

    highest_idx = get_highest_num_idx(candidate_bank)
    highest_num = candidate_bank[highest_idx]

    new_candidate_bank = bank[highest_idx + 1 :]

    return [highest_num] + get_highest_batteries(new_candidate_bank, battery_count - 1)


def sum_from_batteries(batteries):
    out = 0
    for idx, number in enumerate(batteries):
        exponent = 10 ** (len(batteries) - idx - 1)
        out += number * exponent

    return out


input = []
with open("input.txt") as f:
    for line in f:
        input.append([int(num) for num in list(line.strip())])

out = 0
for bank in input:
    highest_batteries = get_highest_batteries(bank, 12)
    out += sum_from_batteries(highest_batteries)

print(out)
