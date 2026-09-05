class Vertex:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vertex({}, {})".format(self.x, self.y)


class Edge:
    def __init__(self, start: Vertex, end: Vertex):
        self.start = start
        self.end = end

    def is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    def contains(self, x: int, y: int) -> bool:
        if self.is_horizontal():
            leftmost_x, rightmost_x = sorted([self.start.x, self.end.x])
            return self.start.y == y and leftmost_x <= x <= rightmost_x

        highest_y, lowest_y = sorted([self.start.y, self.end.y])
        return self.start.x == x and highest_y <= y <= lowest_y

    def __repr__(self):
        return "Edge({}, {})".format(self.start, self.end)


class Layout:
    def from_tiles(tiles: List[Vertex]):
        layout = Layout(tiles)

        return layout

    def __init__(self, tiles: List[Vertex]):
        self.tiles = tiles
        self.edges = [
            Edge(start, end)
            for start, end in zip(self.tiles, self.tiles[1:] + [self.tiles[0]])
        ]

    def get_fit_dimensions(self):
        width = max(tile.x for tile in self.tiles) + 1
        height = max(tile.y for tile in self.tiles) + 1

        return width, height

    def is_edge(self, x: int, y: int) -> bool:
        for edge in self.edges:
            if edge.contains(x, y):
                return True

        return False

    def print_edges(self):
        width, height = self.get_fit_dimensions()

        for y in range(height + 1):
            line = ""
            for x in range(width + 1):
                if self.is_edge(x, y):
                    line += "#"
                else:
                    line += "."

            print(line)


with open("sample.txt") as f:
    red_tile_positions = [
        (tuple(int(num) for num in line.strip().split(","))) for line in f
    ]
    red_tiles = [Vertex(x, y) for x, y in red_tile_positions]

layout = Layout.from_tiles(red_tiles)
layout.print_edges()
