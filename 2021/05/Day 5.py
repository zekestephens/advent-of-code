#!/usr/bin/env -S uv run --with numpy --script
import numpy as np

actual_input = open("input.txt").read().strip()

# Part 1
arr = np.zeros((1000, 1000), dtype=np.int8)
for (x1, y1), (x2, y2) in [
    tuple(tuple(map(int, coord.split(","))) for coord in line.split(" -> "))
    for line in actual_input.splitlines()
]:
    if x1 == x2 or y1 == y2:
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        arr[y1 : y2 + 1, x1 : x2 + 1] += 1

print((arr >= 2).sum())

# Part 2
arr = np.zeros((1000, 1000), dtype=np.int8)
for (x1, y1), (x2, y2) in [
    tuple(tuple(map(int, coord.split(","))) for coord in line.split(" -> "))
    for line in actual_input.splitlines()
]:
    if x1 == x2 or y1 == y2:
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        arr[y1 : y2 + 1, x1 : x2 + 1] += 1
    else:
        for x, y in zip(
            range(x1, x2 + (1 if x2 > x1 else -1), -1 if x1 > x2 else 1),
            range(y1, y2 + (1 if y2 > y1 else -1), -1 if y1 > y2 else 1),
        ):
            arr[y][x] += 1

print((arr >= 2).sum())
