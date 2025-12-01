input = []
with open('input.txt') as f:
    for line in f:
        abs_num = int(line.strip()[1:])
        if line[0] == 'L':
            input.append(-abs_num)
        else:
            input.append(abs_num)

pos = 50
zero_count = 0
for turn in input:
    start_pos = pos
    pos += turn
    zero_count += abs(int(pos / 100))

    if start_pos > 0 and pos <= 0:
        zero_count += 1

    pos = pos % 100

print(zero_count)

