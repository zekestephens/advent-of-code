#!/usr/bin/env python3
import sys

rights = list()
lefts = list()

for line in open('input.txt'):
    l, r = line.split()
    lefts.append(int(l))
    rights.append(int(r))

lefts.sort()
rights.sort()

print(sum(abs(x - y) for x, y in zip(lefts, rights)))

print(sum(n*rights.count(n) for n in lefts))
