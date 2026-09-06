class Vertex:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vertex({}, {})".format(self.x, self.y)

    def is_at(self, x: int, y: int) -> bool:
        return self.x == x and self.y == y


class Edge:
    def __init__(self, start: Vertex, end: Vertex):
        self.start = start
        self.end = end

    def is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    def is_vertical(self) -> bool:
        return self.start.x == self.end.x

    def contains(self, x: int, y: int) -> bool:
        if self.is_horizontal():
            leftmost_x, rightmost_x = sorted([self.start.x, self.end.x])
            return self.start.y == y and leftmost_x <= x <= rightmost_x

        highest_y, lowest_y = sorted([self.start.y, self.end.y])
        return self.start.x == x and highest_y <= y <= lowest_y

    def has_vertex_at(self, x: int, y: int) -> bool:
        return self.start.is_at(x, y) or self.end.is_at(x, y)

    def has_leftmost_vertex_at(self, x: int, y: int) -> bool:
        return self.get_leftmost_vertex().is_at(x, y)

    def intersects_row(self, y: int) -> bool:
        if self.is_horizontal():
            return self.start.y == y

        highest_y, lowest_y = sorted([self.start.y, self.end.y])
        return highest_y <= y <= lowest_y

    def get_topmost_vertex(self) -> Vertex:
        return min(self.start, self.end, key=lambda edge: [edge.y, edge.x])

    def get_leftmost_vertex(self) -> Vertex:
        return min(self.start, self.end, key=lambda edge: [edge.x, edge.y])

    def get_leftmost_column(self) -> int:
        return self.get_leftmost_vertex().x

    def __repr__(self):
        return "Edge({}, {})".format(self.start, self.end)


class RowEdges:
    def __init__(self, y: int, edges: List[Edge]):
        self.y = y
        self.edges = sorted(edges, key=lambda edge: edge.get_leftmost_column())

    def has_vertex_at(self, x: int) -> bool:
        return any(edge.has_vertex_at(x, self.y) for edge in self.edges)

    def has_horizontal_at(self, x: int) -> bool:
        return any(edge.contains(x, self.y) and edge.is_horizontal() for edge in self.edges)

    def has_vertical_at(self, x: int) -> bool:
        return any(edge.contains(x, self.y) and edge.is_vertical() for edge in self.edges)

    def get_vertical_at(self, x: int) -> Edge:
        for edge in self.edges:
            if edge.is_vertical() and edge.contains(x, self.y):
                return edge

        raise Exception

    def is_start_of_horizontal(self, x: int) -> bool:
        return any(edge.is_horizontal() and edge.has_leftmost_vertex_at(x, self.y) for edge in self.edges)

    def vertical_edge_goes_down(self, x: int) -> bool:

        vertical_at = self.get_vertical_at(x)
        topmost = vertical_at.get_topmost_vertex()
        is_at = topmost.is_at(x, self.y)
        #print(vertical_at, topmost, x, self.y, is_at)

        return self.get_vertical_at(x).get_topmost_vertex().is_at(x, self.y)

    def should_paint(self, x: int):
        return any(edge.contains(x, self.y) for edge in self.edges)

    def should_toggle_painting(self, x: int) -> bool:
        if self.has_vertex_at(x):
            if self.is_start_of_horizontal(x):
                return False

            return self.vertical_edge_goes_down(x)

        if self.has_horizontal_at(x):
            return False

        if self.has_vertical_at(x):
            return True

        return False


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

    def get_edges_intersecting_row(self, y: int) -> RowEdges:
        return RowEdges(y, [edge for edge in self.edges if edge.intersects_row(y)])

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

    def print_filled(self):
        width, height = self.get_fit_dimensions()

        for y in range(height + 1):
            line = ""
            edges = self.get_edges_intersecting_row(y)
            painting = False
            for x in range(width + 1):
                if edges.should_toggle_painting(x):
                    painting = not painting

                should_paint = edges.should_paint(x)

                if painting or should_paint:
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
layout.print_filled()
