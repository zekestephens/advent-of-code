#!/usr/bin/env -S uv run --with numpy --script
import numpy as np

with open('input') as f:
    c = np.genfromtxt(f, delimiter=',', dtype=int)

print(min(sum((lambda n: n*(n+1)//2)(abs(c - i))) for i in range(c.min(), c.max())))
