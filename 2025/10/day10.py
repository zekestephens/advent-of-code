#!/usr/bin/env -S uv run --with numpy --with cvxpy[GLPK] --script
from collections import defaultdict
import numpy as np
import cvxpy as cp

def press(button):
    res = 0
    for key in button:
        res ^= 1 << key
    return res

# Note: I got surprisingly far by using a rounded pseudoinverse solution but PINV
# minimizes the L2 norm, not the L1 norm and its not an integer so this just ends up
# being better anyway
#
# still had to look up how to use cvxpy though - seems like a perfect fit for this
# problem
#
# I will try to figure out how to do this the real way later
def solve(A, y):
    x = cp.Variable(A.shape[1], integer=True)
    objective = cp.Minimize(cp.norm(x, 1))
    constraints = [
        A @ x == y,
        x >= 0
    ]
    cp.Problem(objective, constraints).solve(solver=cp.GLPK_MI)
    return x.value

def min_presses(state, target, buttons):
    sspace = defaultdict(lambda: float('inf'))
    sspace[state] = 0
    while target not in sspace:
        for s, dist in list(sspace.items()):
            for b in buttons:
                sspace[s^b] = min(sspace[s^b], dist + 1)
    return sspace[target]

def vec(joltage, idxs):
    s = set(idxs)
    return [1 if i in s else 0 for i in range(len(joltage))]

total1 = 0
total2 = 0
with open('input.txt') as f:
    for line in list(f):
        if line.strip():
            stuff = line.split()
            target = int(stuff[0][1:-1].replace(".", "0").replace("#", "1")[::-1], base=2)
            buttons = [press(int(x) for x in thing[1:-1].split(",")) for thing in stuff if '(' in thing]
            joltage = np.array([int(x) for x in stuff[-1][1:-1].split(",")])
            b2 = np.array([vec(joltage, (int(x) for x in thing[1:-1].split(","))) for thing in stuff if '(' in thing]).T
            total2 += int(sum(solve(b2, joltage)))
            total1 += min_presses(0, target, buttons)

print(total1)
print(total2)
