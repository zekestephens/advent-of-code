#!/usr/bin/env python3
import re
from operator import mul
import sys

buf = open("input").read()

print(sum(map(eval, re.findall(r'mul\(\d{1,3},\d{1,3}\)', buf))))

flag = True
total = 0

for expr in re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', buf):
    if flag and expr.startswith('mul'):
        total += eval(expr)
    elif expr == "don't()":
        flag = False
    elif expr == "do()":
        flag = True

print(total)
