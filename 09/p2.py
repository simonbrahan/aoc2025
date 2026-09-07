from itertools import combinations


class Vertex:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return isinstance(other, Vertex) and self.x == other.x and self.y == other.y

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

    def isBeforeColumn(self, x) -> bool:
        if self.is_horizontal():
            raise Exception

        return self.start.x < x

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

    def goes_down_from_row(self, y: int) -> bool:
        if self.is_horizontal():
            raise Exception

        return self.get_topmost_vertex().y == y

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
        return any(
            edge.contains(x, self.y) and edge.is_horizontal() for edge in self.edges
        )

    def has_vertical_at(self, x: int) -> bool:
        return any(
            edge.contains(x, self.y) and edge.is_vertical() for edge in self.edges
        )

    def get_vertical_at(self, x: int) -> Edge:
        for edge in self.edges:
            if edge.is_vertical() and edge.contains(x, self.y):
                return edge

        raise Exception

    def get_previous_vertical(self, x: int) -> Edge:
        out = None
        for edge in self.edges:
            if edge.is_vertical() and edge.isBeforeColumn(x):
                out = edge

        if out:
            return out

        raise Exception

    def is_start_of_horizontal(self, x: int) -> bool:
        return any(
            edge.is_horizontal() and edge.has_leftmost_vertex_at(x, self.y)
            for edge in self.edges
        )

    def should_paint(self, x: int):
        return any(edge.contains(x, self.y) for edge in self.edges)

    def should_toggle_painting(self, x: int) -> bool:
        if self.has_vertex_at(x):
            if self.is_start_of_horizontal(x):
                return False

            prev_vertical_goes_down = self.get_previous_vertical(x).goes_down_from_row(
                self.y
            )
            this_vertical_goes_down = self.get_vertical_at(x).goes_down_from_row(self.y)
            return prev_vertical_goes_down != this_vertical_goes_down

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

    def get_filled(self):
        width, height = self.get_fit_dimensions()

        out = set()
        for y in range(height):
            edges = self.get_edges_intersecting_row(y)
            painting = False
            for x in range(width):
                if edges.should_toggle_painting(x):
                    painting = not painting

                should_paint = edges.should_paint(x)

                if painting or should_paint:
                    out.add(Vertex(x, y))

        return out

    def contains_tiles(self, tiles: set[Vertex]):
        filled_tiles = self.get_filled()
        return tiles.issubset(filled_tiles)


def get_area(point_a: Vertex, point_b: Vertex) -> int:
    width = abs(point_a.x - point_b.x) + 1
    height = abs(point_a.y - point_b.y) + 1

    return width * height


def get_rectangle_perimeter_from_corners(
    point_a: Vertex, point_b: Vertex
) -> set[Vertex]:
    low_x, high_x = sorted([point_a.x, point_b.x])
    low_y, high_y = sorted([point_a.y, point_b.y])
    x_range = range(low_x, high_x + 1)
    y_range = range(low_y, high_y + 1)

    out = set()
    out.update(Vertex(x, low_y) for x in x_range)
    out.update(Vertex(x, high_y) for x in x_range)
    out.update(Vertex(low_x, y) for y in y_range)
    out.update(Vertex(high_x, y) for y in y_range)
    return out


def get_largest_area(points, layout):
    pairs = combinations(points, 2)
    layout_tiles = layout.get_filled()

    largest_area = 0
    for point_a, point_b in pairs:
        rectangle_perimeter = get_rectangle_perimeter_from_corners(point_a, point_b)
        area = get_area(point_a, point_b)
        if area > largest_area and rectangle_perimeter.issubset(layout_tiles):
            largest_area = area

    return largest_area


with open("test1.txt") as f:
    red_tile_positions = [
        (tuple(int(num) for num in line.strip().split(","))) for line in f
    ]
    red_tiles = [Vertex(x, y) for x, y in red_tile_positions]

layout = Layout.from_tiles(red_tiles)

print(get_largest_area(red_tiles, layout))
