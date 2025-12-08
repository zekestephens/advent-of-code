#!/usr/bin/env -S uv run --with numpy --script
import numpy as np
from itertools import count

with open("input", "r") as f:
    input = np.genfromtxt(f, delimiter=1, dtype=np.int8)


def touching(a: np.ndarray):
    """
    takes a boolean array and returns a boolean array of the touching cells

    example:
        touching(np.array([[False, True, False],
                           [False, False, False],
                           [False, False, False]]))
        returns:
            np.array([[True, False, True],
                      [True, True, True],
                      [False, False, False]])
    """
    # get the shape of the array
    # create a boolean array of the same shape
    b = np.zeros(a.shape, dtype=bool)
    # iterate over the array
    it = np.nditer(a, flags=["multi_index"])
    for x in it:
        if x:
            i, j = it.multi_index
            b[
                max(0, i - 1) : min(a.shape[0], i + 2),
                max(0, j - 1) : min(a.shape[1], j + 2),
            ] = True
    b = b & ~a
    return b


def step(a: np.ndarray):
    """
    Takes a matrix and returns the next growth step

    The rules are:
        - All cells' energy is incremented by 1
        - Any cell with greater than 9 energy 'flashes' and increases the energy of all surrounding cells
            by 1
        - Any cells that have flashed are set to 0
        - Each cell can only flash once
    """
    a += 1
    flashed = np.zeros(a.shape, dtype=bool)
    while np.any(a > 9):
        it = np.nditer(a, flags=["multi_index"])
        for c in it:
            if c > 9:
                z = np.zeros(a.shape, dtype=bool)
                z[it.multi_index] = True
                a += touching(z).astype(int)
                flashed[it.multi_index] = True
        a[flashed] = 0
    return np.all(flashed)


for i in count():
    if step(input):
        print(i + 1)
        break
