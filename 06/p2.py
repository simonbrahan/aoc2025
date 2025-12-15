import functools
import numpy as np


def parse_problems(f):
    unrotated_grid = [list(line.strip("\n")) for line in f]

    grid = np.rot90(unrotated_grid)

    out = []
    problem = {"operator": "", "operands": []}
    for unfiltered_line in grid:
        line = list(filter(lambda char: char != " ", unfiltered_line))
        if ("").join(line) == "":
            out.append(problem)
            problem = {"operator": "", "operands": []}
            continue

        if line[-1] in ["*", "+"]:
            problem["operator"] = str(line.pop(-1))

        problem["operands"].append(int(("").join(line)))

    out.append(problem)

    return out


with open("input.txt") as f:
    problems = parse_problems(f)

out = 0
for problem in problems:
    if problem["operator"] == "*":
        acc = lambda a, b: a * b
    else:
        acc = lambda a, b: a + b

    out += functools.reduce(acc, problem["operands"])

print(out)
