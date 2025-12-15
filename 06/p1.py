import functools

with open("input.txt") as f:
    problems = [[] for i in range(len(f.readline().strip().split()))]
    f.seek(0)
    for line in f:
        for idx, item in enumerate(line.strip().split()):
            if item.isdigit():
                item = int(item)
            problems[idx].append(item)

out = 0
for problem in problems:
    operator = problem.pop(-1)
    if operator == "*":
        acc = lambda a, b: a * b
    else:
        acc = lambda a, b: a + b

    out += functools.reduce(acc, problem)

print(out)
