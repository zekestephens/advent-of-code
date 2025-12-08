#!/usr/bin/env -S uv run --with scipy --with numpy --script
import numpy as np
from scipy.ndimage import label
from operator import mul
from functools import reduce

with open("input.txt") as f:
    a = np.genfromtxt(f, delimiter=1, dtype=np.int8)


# Part One
it = np.nditer(a, flags=["multi_index"])
print(sum(
    int(n+1) if all(
        np.fromiter(
            (
                a[i]
                for i in filter(
                    lambda x: x[0] >= 0
                    and x[1] >= 0
                    and x[0] < a.shape[0]
                    and x[1] < a.shape[1],
                    zip(
                        np.array((-1, -1, -1, 0, 0, 1, 1, 1)) + it.multi_index[0],
                        it.multi_index[1] + np.array((-1, 0, 1, -1, 1, -1, 0, 1)),
                    ),
                )
            ),
            dtype=np.int8,
        )
        > n
    ) else 0
    for n in it
))


# Part Two
print(reduce(mul, sorted(np.unique(label((a < 9))[0], return_counts=True)[1][1:])[-3:]))
