from itertools import permutations


def parse_input_line(line):
    indicator_spec, *button_spec, joltage_spec = line.strip().split(" ")

    indicators = [char == "#" for char in indicator_spec[1:-1]]

    buttons = [
        [int(num) for num in button.strip("()").split(",")] for button in button_spec
    ]

    joltages = [int(num) for num in joltage_spec.strip("{}").split(",")]

    return indicators, buttons, joltages


def find_shortest_setup(required_indicators, buttons, _):
    out = len(buttons)
    for process in permutations(buttons, len(buttons)):
        indicators = [False] * len(required_indicators)
        button_count = 0
        for button in process:
            button_count += 1
            for indicator in button:
                indicators[indicator] = not indicators[indicator]

            if indicators == required_indicators:
                out = min(out, button_count)

    return out


input = []
with open("sample.txt") as f:
    for line in f:
        input.append(parse_input_line(line))

out = 0
for machine in input:
    out += find_shortest_setup(*machine)

print(out)
