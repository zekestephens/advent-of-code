#!/usr/bin/env -S uv run --with numpy --script
import re
import sys

import numpy as np

input_ = open("input").read()


def find_cost(a, c, b, d, x, y):
    soln = np.linalg.solve([[a, b], [c, d]], [x, y])
    if all(abs(n - round(n)) < 0.005 for n in soln):
        i, j = map(round, soln)
        return 3 * i + j
    min_cost = float("inf")
    for j in range(10):
        i = (x - b * j) / a
        if i.is_integer() and 0 <= i <= 100:
            i = int(i)
            if abs(c * i + d * j - y) < 0.005:
                min_cost = min(min_cost, 3 * i + j)

    return min_cost if min_cost != float("inf") else 0


def find_part2_cost(a, c, b, d, x, y):
    x += 1e13
    y += 1e13
    return find_cost(a, c, b, d, x, y)


prize_list = [
    tuple(
        map(
            int,
            re.fullmatch(
                r"Button A: X([+-]\d+), Y([+-]\d+)\nButton B: X([+-]\d+), Y([+-]\d+)\nPrize: X=(\d+), Y=(\d+)",
                prize,
            ).groups(),
        )
    )
    for prize in input_.split("\n\n")
]

# print(len(prize_list))

part1 = sum(find_cost(*prize_details) for prize_details in prize_list)
part2 = sum(find_part2_cost(*prize_details) for prize_details in prize_list)
print(part1)
print(part2)
