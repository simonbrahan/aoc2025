def fresh_ranges_from_input(range_strings):
    fresh_ranges = []
    for line in range_strings.strip().split('\n'):
        start, end = line.split('-')
        fresh_ranges.append((int(start), int(end)))

    return fresh_ranges


def ids_from_input(id_strings):
    ids = []
    for line in id_strings.strip().split('\n'):
        ids.append(int(line))

    return ids


with open('input.txt') as f:
    range_strings, id_strings = f.read().split('\n\n')
    fresh_ranges = fresh_ranges_from_input(range_strings)
    check_ids = ids_from_input(id_strings)

out = 0
for id in check_ids:
    for start, end in fresh_ranges:
        if start <= id <= end:
            out += 1
            break

print(out)

