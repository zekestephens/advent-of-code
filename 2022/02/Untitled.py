#!/usr/bin/env python3
from collections import deque

# Part 1
total = 0
with open('input') as f:
    while l := f.readline():
        h, a = l.split()
        t = (mp := 'XYZ'.index(a)) - (tp := 'ABC'.index(h))
        s = mp + 1
        if t == 0:
            s += 3
        elif mp == 1 + tp or tp == 2 + mp:
            s += 6
        total += s

print(total)

# Part 2
total = 0
lts = 'ABC'
rts = 'XYZ'
with open('input') as f:
    for line in f:
        h, a = line.split()
        n = ord(a) - ord('Y')
        a = dict(zip(lts, rts[n:] + rts[:n]))[h]
        t = (mp := rts.index(a)) - (tp := lts.index(h))
        s = mp + 1
        if t == 0:
            s += 3
        elif mp == 1 + tp or tp == 2 + mp:
            s += 6
        total += s
print(total)
