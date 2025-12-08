#!/usr/bin/env python3
from collections import defaultdict
from itertools import combinations


def distance(point1: tuple[int, int], point2: tuple[int, int]):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def colinear(p1, p2, p3):
    y1, x1 = p1
    y2, x2 = p2
    y3, x3 = p3
    area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    return abs(area) < 1e-10


bands = defaultdict(list)
data = []
for y, line in enumerate(open("input")):
    data.append([])
    for x, c in enumerate(line.rstrip()):
        if c != ".":
            bands[c].append((y, x))
            data[-1].append(c)
        else:
            data[-1].append(c)


def count_antinodes(bands, data, distance_condition=True):
    antinodes = set()
    for coords in bands.values():
        pairs = list(combinations(coords, 2))
        for y in range(len(data)):
            for x in range(len(data[0])):
                point = (y, x)
                for point1, point2 in pairs:
                    if colinear(point1, point2, point):
                        if (
                            not distance_condition
                            or abs(
                                distance(point1, point) - 2 * distance(point2, (y, x))
                            )
                            < 0.005
                            or (
                                abs(
                                    distance(point2, point)
                                    - 2 * distance(point1, (y, x))
                                )
                                < 0.005
                            )
                        ):
                            antinodes.add((x, y))
    return len(antinodes)


print(part1 := count_antinodes(bands, data))
print(part2 := count_antinodes(bands, data, distance_condition=False))
