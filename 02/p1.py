import math

def count_digits(num):
    return int(math.log10(num)) + 1


def first_candidate_after(num):
    digit_count = count_digits(num)

    # if input has odd number of digits, start with the next number with an even number of digits
    if digit_count % 2 == 1:
        half = '1' + '0' * ((digit_count - 1) // 2)
    else:
        half = str(num)[:digit_count // 2]

    out = int(half + half)

    while out <= num:
        half = str(int(half) + 1)
        out = int(half + half)

    return out


def is_invalid_id(num):
    digit_count = count_digits(num)

    if digit_count % 2 != 0:
        return False

    num_as_str = str(num)
    front, back = num_as_str[:digit_count//2], num_as_str[digit_count//2:]

    return front == back


with open('input.txt') as f:
    input = [[int(num) for num in num_range.split('-')] for num_range in f.read().strip().split(',')]

out = 0
for range_start, range_end in input:
    out_of_range = False
    candidate = range_start
    while not out_of_range:
        if is_invalid_id(candidate):
            out += candidate

        candidate = first_candidate_after(candidate)

        if candidate > range_end:
            out_of_range = True

print(out)
