def get_highest_num_idx(nums):
    highest_idx = 0
    for idx, num in enumerate(nums):
        if num > nums[highest_idx]:
            highest_idx = idx

    return highest_idx


input = []
with open("input.txt") as f:
    for line in f:
        input.append([int(num) for num in list(line.strip())])

out = 0
for bank in input:
    highest_idx = get_highest_num_idx(bank[:-1])
    second_digit_idx = get_highest_num_idx(bank[highest_idx + 1:]) + highest_idx + 1
    out += bank[highest_idx] * 10 + bank[second_digit_idx]

print(out)
