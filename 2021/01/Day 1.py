#!/usr/bin/env python3
from itertools import pairwise

inputs = open("input.txt").read()

inputs = list(map(int, inputs.strip().split('\n')))

print(len(list(filter(lambda xy: xy[0] < xy[1], pairwise(inputs)))))

print(len(list(filter(lambda xy: xy[0] < xy[1], pairwise([sum(inputs[i:i+3]) for i in range(len(inputs) - (3-1))])))))
