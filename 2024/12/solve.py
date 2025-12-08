#!/usr/bin/env -S uv run --with numpy --with scipy --script
from dataclasses import dataclass
from string import ascii_uppercase

import numpy as np
from scipy.ndimage import label

COMPASS = ((0, 1), (1, 0), (0, -1), (-1, 0))


@dataclass
class Side:
    direction: int  # a COMPASS direction
    min_bound: int  # the minimum boundary
    max_bound: int  # the maximum boundary
    fixed_pos: int  # the row/column the edge is in

    def __init__(self, point_pair):
        inside, outside = point_pair
        iy, ix = inside
        oy, ox = outside
        self.direction = COMPASS.index((oy - iy, ox - ix))
        self.min_bound = self.max_bound = inside[COMPASS[self.direction].index(0)]
        self.fixed_pos = inside[(COMPASS[self.direction].index(0) + 1) % 2]

    def add_if_adjacent(self, other_side):
        if (
            other_side.direction == self.direction
            and other_side.fixed_pos == self.fixed_pos
        ):
            if other_side.min_bound == self.min_bound - 1:
                self.min_bound = other_side.min_bound
                return True
            elif other_side.max_bound == self.max_bound + 1:
                self.max_bound = other_side.max_bound
                return True
            else:
                return False
        return False


def neighbors(pos):
    y, x = pos
    return [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]


def count_sides(edge_arr) -> int:
    sides = []
    for edge in edge_arr:
        for side in sides:
            if side.add_if_adjacent(Side(edge)):
                break
        else:
            sides.append(Side(edge))
    # there is no need to re-merge sides
    # because they were added in optimal (grid) order
    return len(sides)


garden = np.array([list(line.rstrip()) for line in open("input")])
structure = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=bool)
plots = [
    (
        lambda g: (
            np.pad(
                g[0],
                pad_width=1,
                mode="constant",
                constant_values=0,
            ),
            g[1],
        )
    )(label(garden == c, structure))
    for c in ascii_uppercase
    if any(c in p for p in garden)
]

cost1 = 0
cost2 = 0
for plot, num in plots:
    for n in range(1, num + 1):
        area = 0
        perimeter = 0
        edge_nodes = []
        for y, x in np.ndindex(plot.shape):
            if plot[y, x] == n:
                area += 1
                for other in neighbors((y, x)):
                    if plot[other] != n:
                        edge_nodes.append(((y, x), other))
                        perimeter += 1
        cost1 += area * perimeter
        cost2 += area * count_sides(edge_nodes)

print(cost1)
print(cost2)
