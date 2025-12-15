def propagate_tachyons(tachyons, splitters):
    new_tachyons = set()
    hit_count = 0
    for tachyon_pos in tachyons:
        if tachyon_pos in splitters:
            new_tachyons.update([tachyon_pos - 1, tachyon_pos + 1])
            hit_count += 1
        else:
            new_tachyons.update([tachyon_pos])

    return list(new_tachyons), hit_count


with open("input.txt") as f:
    start_line = f.readline()
    start_point = start_line.find("S")
    tachyons = [start_point]
    splitters = []
    for line in f:
        splitter_row = set([idx for idx, char in enumerate(line) if char == "^"])
        if len(splitter_row) > 0:
            splitters.append(splitter_row)

out = 0
for row in splitters:
    tachyons, hit_count = propagate_tachyons(tachyons, row)
    out += hit_count

print(out)
