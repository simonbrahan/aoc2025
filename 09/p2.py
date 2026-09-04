from itertools import combinations

def get_fit_dimensions(tiles):
    width = max(tile[0] for tile in tiles) + 1
    height = max(tile[1] for tile in tiles) + 1

    return width, height


def print_tiles(tiles):
    width, height = get_fit_dimensions(tiles)

    for y in range(height+1):
        line = ""
        for x in range(width+1):
            if (x, y) in tiles:
                line += "#"
            else:
                line += "."

        print(line)


def get_scanline_edges(corner_tiles):
    edges = zip(red_tiles, red_tiles[1:] + [red_tiles[0]])

    out = set()
    ignore = set()
    for start, end in edges:
        is_vertical = start[1] != end[1]

        if is_vertical:
            x = start[0]
            start_y = min(start[1], end[1])
            end_y = max(start[1], end[1])

            out.update((x, y) for y in range(start_y, end_y + 1))
        else:
            """
            Vertices between vertical and horizontal edges should be ignored
            if the rest of the horizontal edge has already been scanned
            """
            rightmost_vertex = max(start, end, key=lambda vertex: vertex[0])
            ignore.add(rightmost_vertex)

    return out.difference(ignore)


def get_fill_tiles(red_tiles):
    scanline_edges = get_scanline_edges(red_tiles)
    width, height = get_fit_dimensions(red_tiles)

    out = set()
    for y in range(height+1):
        am_inside_shape = False
        for x in range(width+1):
            am_at_edge = (x, y) in scanline_edges
            if am_inside_shape or am_at_edge:
                out.add((x, y))
            
            if am_at_edge:
                am_inside_shape = not am_inside_shape

    return out


with open("sample.txt") as f:
    red_tiles = [(tuple(int(num) for num in line.strip().split(","))) for line in f]

fill_tiles = get_fill_tiles(red_tiles)

print_tiles(fill_tiles)
