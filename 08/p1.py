import itertools
import math


class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def distance(self):
        x = self.a[0] - self.b[0]
        y = self.a[1] - self.b[1]
        z = self.a[2] - self.b[2]
        return math.sqrt(x**2 + y**2 + z**2)


def get_sorted_pairs(boxes):
    out = []
    for a, b in itertools.combinations(boxes, 2):
        out.append(Pair(a, b))

    return sorted(out, key=lambda pair: pair.distance())


def build_circuits(boxes, sorted_pairs, num_links):
    """
    Keep track of which circuit each box is in
    Circuits are referenced by the box that started the circuit
    """
    linked_boxes = {box: box for box in boxes}
    """
    Keep track of the circuits themselves
    Each box starts in a circuit on its own
    """
    circuits = {box: set([box]) for box in boxes}

    for pair in sorted_pairs[:num_links]:
        link_a = linked_boxes.get(pair.a)
        link_b = linked_boxes.get(pair.b)

        if link_a == link_b:
            continue

        link_a_circuit = circuits.get(link_a)
        link_b_circuit = circuits.get(link_b)

        link_a_circuit.update(link_b_circuit)
        circuits[link_b] = set()

        for box in link_b_circuit:
            linked_boxes[box] = link_a

    return circuits.values()


with open("input.txt") as f:
    input = [(tuple(int(num) for num in line.strip().split(","))) for line in f]

sorted_pairs = get_sorted_pairs(input)

circuits = build_circuits(input, sorted_pairs, 1000)

largest_circuits = sorted(circuits, key=lambda circuit: len(circuit), reverse=True)[:3]

out = 1
for circuit in largest_circuits:
    out *= len(circuit)

print(out)
