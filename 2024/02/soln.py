#!/usr/bin/env python3
import sys
from itertools import pairwise

def is_valid(record):
    return ((all(a > b for a, b in pairwise(record)) or
        all(a < b for a, b in pairwise(record))) and
    all(1 <= abs(a - b) < 4 for a, b in pairwise(record)))

def is_dampener_valid(record):
    if is_valid(record):
        return True
    return any(is_valid(record[:i] + record[i + 1:]) for i in range(len(record)))

records = [ list(map(int, line.split())) for line in open("input.txt") ]
print(sum(is_valid(record) for record in records))

print(sum(is_dampener_valid(record) for record in records))
