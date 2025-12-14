def fresh_ranges_from_input(range_strings):
    fresh_ranges = []
    for line in range_strings.strip().split("\n"):
        start, end = line.split("-")
        fresh_ranges.append([int(start), int(end)])

    return fresh_ranges


with open("input.txt") as f:
    range_strings, _ = f.read().split("\n\n")
    fresh_ranges = fresh_ranges_from_input(range_strings)

fresh_ranges.sort()
merged_ranges = [fresh_ranges.pop(0)]
for start, end in fresh_ranges:
    if start > merged_ranges[-1][1]:
        merged_ranges.append([start, end])
    elif end > merged_ranges[-1][1]:
        merged_ranges[-1][1] = end

out = 0
for start, end in merged_ranges:
    out += end - start + 1

print(out)
