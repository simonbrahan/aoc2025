import scipy


def parse_input_line(line):
    indicator_spec, *button_spec, joltage_spec = line.strip().split(" ")

    indicators = [char == "#" for char in indicator_spec[1:-1]]

    buttons = [
        [int(num) for num in button.strip("()").split(",")] for button in button_spec
    ]

    joltages = [int(num) for num in joltage_spec.strip("{}").split(",")]

    return indicators, buttons, joltages


def matrix_from_wiring(buttons, joltages):
    out = []
    for counter, _ in enumerate(joltages):
        out.append([1 if counter in button else 0 for button in buttons])

    return out


out = 0
with open("input.txt") as f:
    for line in f:
        _, buttons, joltages = parse_input_line(line)
        flags = [1] * len(buttons)
        matrix = matrix_from_wiring(buttons, joltages)
        result = scipy.optimize.linprog(
            flags, A_eq=matrix, b_eq=joltages, integrality=flags
        )
        out += sum(result.x)

print(int(out))
