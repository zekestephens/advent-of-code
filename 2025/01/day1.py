#!/usr/bin/env python3
POINTER = 50
COUNT1 = 0
COUNT2 = 0

with open("input.txt") as f:
    for line in f:
        l = line.strip()
        d = -1 if l[0] == 'L' else 1
        n = int(l[1:])

        for i in range(n):
            POINTER = (POINTER + d) % 100
            if POINTER == 0:
                COUNT2 += 1
        if POINTER == 0:
            COUNT1 += 1

print(COUNT1, COUNT2)

