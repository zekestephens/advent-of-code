#!/usr/bin/env python3
from itertools import product
from operator import mul, add
from functools import partial, reduce

def calibration_result(data, ops):
    return sum(
        x
        for x, ns in data
        if any(
            val == x
            for val in (
                reduce(lambda acc, opn: partial(*opn)(acc), zip(combo, ns[1:]), ns[0])
                for combo in product(ops, repeat=len(ns) - 1)
            )
        )
    )

data = [ (int(x), tuple(map(int, ns.split()))) for x, ns in (line.split(":") for line in open("input")) ]

print(calibration_result(data, (add, mul)))  # part 1
print(calibration_result(data, (add, mul, lambda x, y: int(str(y)+str(x)))))  # part 2
