#!/usr/bin/env -S uv run --python pypy3 --with dlx --with tqdm --script
from dlx import DLX
from itertools import chain
from tqdm import tqdm
import signal

def alarm_handler(signum, frame):
    raise RuntimeError

signal.signal(signal.SIGALRM, alarm_handler)
print()
inputs = open("input.txt").read().split("\n\n")

def minyx(cells):
    return min(y for y, x in cells), min(x for y, x in cells)

def r90(cells):
    flipped = [(x, -y) for y, x in cells]
    miny, minx = minyx(flipped)
    return frozenset((y - miny, x - minx) for y, x in flipped)

def flip(cells):
    rotated = [(y, -x) for y, x in cells]
    miny, minx = minyx(rotated)
    return frozenset((y - miny, x - minx) for y, x in rotated)

def all_rotations(cells):
    res = set([cells])
    current = cells
    for _ in range(3):
        res.add(current := r90(current))
    return res

def rotate_and_flip(cells):
    return all_rotations(cells).union(all_rotations(flip(cells)))

def offset(dy, dx, shape):
    return frozenset((y + dy, x + dx) for y, x in shape)

def in_bounds(gy, gx, placement):
    maxy = 0
    maxx = 0
    for y, x in placement:
        maxy = max(y, maxy)
        maxx = max(x, maxx)
    return maxx < gx and maxy < gy

def all_placements(gy, gx, shape):
    return ( placement for placement in (offset(i, j, shape) for i in range(gy) for j in range(gx)) if in_bounds(gy, gx, placement))

shapes = []
for tile in inputs[:-1]:
    coords = frozenset(chain(*[[(y, x) for x, c in enumerate(line) if c == '#' ] for y, line in enumerate(tile.split('\n')[1:])]))
    shapes.append(rotate_and_flip(coords))

count = 0
for problem in tqdm(inputs[-1].rstrip().split('\n')):
    sizespec, numshapes = problem.split(': ')
    y, x = (int(n) for n in sizespec.split('x'))
    inventory = list(chain(*(int(x)*[s] for s, x in zip(shapes, numshapes.split()))))

    # Set up the solver
    columns = []
    coldxmap = {}
    for i in range(len(inventory)):
        coldxmap[i] = len(columns)
        columns.append((i, DLX.PRIMARY))
    # create secondary columns for each cell in the grid
    for ydx in range(y):
        for xdx in range(x):
            coldxmap[(ydx, xdx)] = len(columns)
            columns.append(((ydx, xdx), DLX.SECONDARY))

    solver = DLX(columns)

    for i, tile in enumerate(inventory):
        for inst in tile:
            for placement in all_placements(y, x, inst):
                row = [i]
                for pos in placement:
                    row.append(coldxmap[pos])
                solver.appendRow(row)

    # can't believe this worked!
    try:
        signal.alarm(3)
        if next(solver.solve(), False):
            count += 1
    except RuntimeError:
        pass
    finally:
        signal.alarm(0)
print(count)
