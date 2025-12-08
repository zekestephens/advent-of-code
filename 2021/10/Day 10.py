#!/usr/bin/env -S uv run --with numpy --script
from functools import reduce
import numpy as np

actual_input = open("input.txt").read()

matching = {
    '(': ')',
    ')': '(',
    '[': ']',
    ']': '[',
    '{': '}',
    '}': '{',
    '<': '>',
    '>': '<',
}

corrupt_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

completion_scores = dict(zip(')]}>', range(1,5)))

# Part 1
def parse1(l):
    stack = []
    for c in l:
        if c in "{[(<":
            stack.append(c)
        else:
            if not stack.pop() == matching[c]:
                return corrupt_scores.get(c)
    return 0

print(sum(parse1(l) for l in actual_input.splitlines()))

# Part 2
def parse(l):
    stack = []
    for c in l:
        if c in "{[(<":
            stack.append(c)
        else:
            if not stack.pop() == matching[c]:
                return

    return reduce(lambda x, y: x * 5 + y, (completion_scores[r] for r in reversed([matching[left] for left in stack])))


a = np.fromiter(filter(None, (parse(l) for l in actual_input.splitlines())), dtype="uint64")

print(int(np.median(a)))

