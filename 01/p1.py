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
    pos += turn

    while pos > 99:
        pos -= 100

    while pos < 0:
        pos += 100

    if pos == 0:
        zero_count += 1

print(zero_count)
