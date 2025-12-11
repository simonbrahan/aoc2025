def count_adjacent_rolls(all_rolls, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    out = 0
    for x_dir, y_dir in directions:
        if x + x_dir < 0 or y + y_dir < 0:
            continue

        try:
            if all_rolls[y + y_dir][x + x_dir]:
                out += 1
        except IndexError:
            continue

    return out


input = []
with open("input.txt") as f:
    for line in f:
        input.append([char == "@" for char in line.strip()])

out = 0
for y, row in enumerate(input):
    for x, space_contains_roll in enumerate(row):
        if space_contains_roll and count_adjacent_rolls(input, x, y) < 4:
            out += 1

print(out)
