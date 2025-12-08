#!/usr/bin/env python3
import re
from functools import cache

line_iter = iter(open("input"))
patterns = next(line_iter).rstrip().split(", ")
next(line_iter)  # skip the blank line
lines = [line.rstrip() for line in line_iter]
count = sum(1 for line in lines if re.fullmatch(f'({"|".join(patterns)})+', line))


@cache
def n_ways(s: str) -> int:
    if not s:
        return 1
    return sum(
        n_ways(s[len(pattern) :]) for pattern in patterns if s.startswith(pattern)
    )


print(count)
total = sum(n_ways(s) for s in lines)
print(total)
