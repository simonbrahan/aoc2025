from itertools import combinations
import numpy as np
import shapely

with open("input.txt") as f:
    tiles = [[int(num) for num in line.strip().split(",")] for line in f]

polygon = shapely.Polygon(tiles)

largest_area = 0
for tile_a, tile_2 in combinations(tiles, 2):
    x_min, x_max = sorted([tile_a[0], tile_2[0]])
    y_min, y_max = sorted([tile_a[1], tile_2[1]])

    area = (x_max - x_min + 1) * (y_max - y_min + 1)

    if area > largest_area and polygon.contains(
        shapely.box(x_min, y_min, x_max, y_max)
    ):
        largest_area = area

print(largest_area)
