#!/usr/bin/env python3
from functools import cache
start = None
beams = set()
split = 0
with open("input.txt") as f:
    for line in f:
        if not start:
            start = line.index("S")
            beams.add(start)
        else:
            ss = [ i for i, x in enumerate(line) if x == "^" ]
            for splitter in ss:
                if splitter in beams:
                    split += 1
                    beams.remove(splitter)
                    beams.add(splitter - 1)
                    beams.add(splitter + 1)
print(split)

grid = []
with open("input.txt") as f:
    grid = [ [ c == "^" for c in line ] for line in f ]

@cache
def count_the_ways(y, x):
    depth = y + 1
    while depth < len(grid):
        if grid[depth][x]:
            return count_the_ways(depth, x - 1) + count_the_ways(depth, x + 1)
        depth += 1
    return 1

print(count_the_ways(0, start))
