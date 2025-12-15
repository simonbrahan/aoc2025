import collections


def propagate_tachyons(tachyons, splitters):
    new_tachyons = collections.defaultdict(int)
    for tachyon_pos, tachyon_count in tachyons.items():
        if tachyon_pos in splitters:
            new_tachyons[tachyon_pos - 1] += tachyon_count
            new_tachyons[tachyon_pos + 1] += tachyon_count
        else:
            new_tachyons[tachyon_pos] += tachyon_count

    return new_tachyons


with open("input.txt") as f:
    start_line = f.readline()
    start_point = start_line.find("S")
    tachyons = collections.defaultdict(int)
    tachyons[start_point] += 1
    splitters = []
    for line in f:
        splitter_row = set([idx for idx, char in enumerate(line) if char == "^"])
        if len(splitter_row) > 0:
            splitters.append(splitter_row)

out = 0
for row in splitters:
    tachyons = propagate_tachyons(tachyons, row)

print(sum(tachyons.values()))
