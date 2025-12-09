import re


def is_invalid_id(num):
    invalid_pattern = re.compile(r"^(\d+)\1+$")
    return invalid_pattern.match(str(num))


with open("input.txt") as f:
    input = [
        [int(num) for num in num_range.split("-")]
        for num_range in f.read().strip().split(",")
    ]

out = 0
for range_start, range_end in input:
    for num in range(range_start, range_end + 1):
        if is_invalid_id(num):
            out += num

print(out)
