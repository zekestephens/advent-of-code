#!/usr/bin/env python3

data = open("input.txt").read().strip()

from operator import methodcaller
(h, v, a) = (0, 0, 0)
for (d, n) in map(tuple, map(methodcaller("split"), data.split('\n'))):
    n = int(n)
    if d == "forward":
        h += n
        v += a * n
    elif d == "up":
        a -= n
    elif d == "down":
        a += n

print(v * h)

