#!/usr/bin/env python3
from operator import mul, add
from functools import reduce
import string

nums = []
ops = []
with open("input.txt") as f:
    for line in f:
        if line.strip()[0] in string.digits:
            nums.append([int(x) for x in line.split()])
        else:
            ops = [ mul if op == "*" else add for op in line.split() ]

total = 0
for op, *ns in zip(ops, *nums):
    total += reduce(op, ns)

print(total)

numberlines = []
slices = []
with open("input.txt") as f:
    for line in f:
        if line[0] not in string.digits and line[0] != ' ':
            slices = [ i for i, c in enumerate(line) if c != ' ']
        else:
            numberlines.append(line)

probs = []
for a, b in zip(slices, slices[1:]):
    prob = []
    for i in range(len(numberlines[0][a:b]) - 1, -1, -1):
        word = ''.join(
            line[a:b][i] for line in numberlines
        ).strip()
        if word:
            prob.append(int(word))
    probs.append(prob)

total = 0
for op, ns in zip(ops, probs):
    total += reduce(op, ns)

print(total)
