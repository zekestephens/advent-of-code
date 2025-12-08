#!/usr/bin/env python3
from itertools import combinations
from dataclasses import dataclass, field
from math import prod

@dataclass
class Node:
    "Union-find (disjoint set) data structure"
    data: tuple[int, int, int]
    parent: Node = field(init=False)
    size: int = 1

    def __post_init__(self):
        self.parent = self
    
    def __lt__(self, other: Node) -> bool:
        return self.size < other.size
    
    def __hash__(self):
        return hash(self.data)

def union(a: Node, b: Node) -> Node:
    x = find(a)
    y = find(b)
    if x is y:
        return x
    else:
        if x < y:
            x, y = y, x
            
        y.parent = x
        x.size += y.size
        return x

def find(n: Node) -> Node:
    if n.parent is n:
        return n
    n.parent = find(n.parent)
    return n.parent

def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return ((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)**0.5

cs = {}
with open("input.txt") as f:
    for line in f:
        box = tuple(int(n) for n in line.split(","))
        cs[box] = Node(box)

connections = sorted(combinations(cs.keys(), 2), key=lambda xs: distance(*xs))

for a, b in connections[:1000]:
    cs[a] = cs[b] = union(cs[a], cs[b])

part1 = prod(c.size for c in sorted(set(cs.values()))[-3:])

print(part1)

# Part 2
for a, b in connections[1000:]:
    cs[a] = cs[b] = union(cs[a], cs[b])
    if cs[a].size == len(cs):
        print(a[0]*b[0])
        break
