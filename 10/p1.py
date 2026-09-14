from itertools import chain, combinations


def parse_input_line(line):
    indicator_spec, *button_spec, joltage_spec = line.strip().split(" ")

    indicators = [char == "#" for char in indicator_spec[1:-1]]

    buttons = [
        [int(num) for num in button.strip("()").split(",")] for button in button_spec
    ]

    joltages = [int(num) for num in joltage_spec.strip("{}").split(",")]

    return indicators, buttons, joltages


def find_shortest_setup(required_indicators, buttons, _):
    tests = []
    tests = chain.from_iterable(
        combinations(buttons, i) for i in range(1, len(buttons))
    )

    for test in tests:
        indicators = [False] * len(required_indicators)
        for button in test:
            for indicator in button:
                indicators[indicator] = not indicators[indicator]

        if indicators == required_indicators:
            return len(test)

    return None


out = 0
with open("input.txt") as f:
    for line in f:
        machine = parse_input_line(line)
        out += find_shortest_setup(*machine)

print(out)
