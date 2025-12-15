#!/usr/bin/env python3
from itertools import combinations

coords = []
with open("input.txt") as f:
    for line in f:
        coords.append(complex(*(int(x) for x in line.split(","))))

def area(p1, p2):
    diff = p1 - p2
    return (abs(diff.real) + 1) * (abs(diff.imag) + 1)

combs = list(combinations(coords, 2))
print(int(max(area(*ps) for ps in combs)))
