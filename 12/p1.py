import re

class Shape:
    def __init__(self, filled_tiles: List[List[bool]]):
        self.filled_tiles = filled_tiles

    def __repr__(self):
        return "\n".join("".join({True: "#", False: "."}[tile] for tile in line) for line in self.filled_tiles)

class Region:
    def __init__ (self, width: int, height: int, numbers_of_shapes: List[int]):
        self.width = width
        self.height = height
        self.numbers_of_shapes = numbers_of_shapes

    def __repr__(self):
        return "{}x{}, {}".format(self.width, self.height, str(self.numbers_of_shapes))

with open("sample.txt") as f:
    input = f.read()

shapes_input, regions_input = input.rsplit("\n\n", 1)

shapes = []
for shape_input in shapes_input.split("\n\n"):
    _, *shape_lines = shape_input.split("\n")
    shapes.append(Shape([[char == "#" for char in shape_line.strip()] for shape_line in shape_lines]))

regions = []
for region_input in regions_input.strip().split("\n"):
    region_width, region_height, *numbers_of_shapes = map(int, re.findall(r"\d+", region_input))
    regions.append(Region(region_width, region_height, numbers_of_shapes))

for shape in shapes:
    print(shape)

print(regions)
