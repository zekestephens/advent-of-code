#!/usr/bin/env -S uv run --script
#
# /// script
# dependencies = ["numpy"]
# ///
import numpy as np

with open('input') as f:
    x = np.genfromtxt(f, delimiter=1, dtype=np.int8)

from statistics import mode
import numpy as np
part1 = (y := sum(int(num>x.shape[0]/2)*2**ind for (ind,), num in np.ndenumerate(np.flip(x.sum(axis=0)))))*(y^4095)

def o2(arr, col=0):
    zeros, ones = tuple(np.unique(arr[:,col], return_counts=True))[1]
    mask = (arr[:, col] == (0 if zeros > ones else 1))
    arr = arr[mask, :]
    return arr if len(arr) == 1 else o2(arr, col=col + 1)

def co2(arr, col=0):
    zeros, ones = tuple(np.unique(arr[:,col], return_counts=True))[1]
    mask = (arr[:, col] == (0 if zeros <= ones else 1))
    arr = arr[mask, :]
    return arr if len(arr) == 1 else co2(arr, col=col + 1)

base_10 = lambda x: sum(int(j)*2**ind for (_, ind), j in np.ndenumerate(np.flip(x)))
part2 = base_10(co2(x))*base_10(o2(x))

print(part1, part2, sep='\n')
