from itertools import combinations


def get_area(point_a, point_b):
    width = abs(point_a[0] - point_b[0]) + 1
    height = abs(point_a[1] - point_b[1]) + 1

    return width * height


def get_largest_area(points):
    pairs = combinations(points, 2)

    largest_area = 0
    for point_a, point_b in pairs:
        area = get_area(point_a, point_b)
        if area > largest_area:
            largest_area = area

    return largest_area


with open("input.txt") as f:
    tiles = [(tuple(int(num) for num in line.strip().split(","))) for line in f]

print(get_largest_area(tiles))
