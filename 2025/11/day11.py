#!/usr/bin/env python3
from collections import defaultdict
adj = defaultdict(list)

def kahn(g):
    "Kahn's algorithm for topological sort"
    indegree = defaultdict(lambda: 0)
    for node, adjs in g.items():
        indegree[node]
        for out in adjs:
            indegree[out] += 1
    to_visit = [n for n, v in indegree.items() if v == 0]
    result = []
    while len(to_visit):
        n = to_visit.pop()
        for neighbor in g[n]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                to_visit.append(neighbor)
        result.append(n)
    assert len(result) == len(g)
    return result

for line in open("input.txt"):
    if line.strip():
        v, edgelist = line.strip().split(": ")
        adj[v] = edgelist.split(" ")

topo = kahn(adj)

def count_paths(start, end):
    paths = { v: 0 for v in topo }
    paths[start] = 1

    for v in topo:
        if v == end:
            return paths[end]
        for neighbor in adj[v]:
            paths[neighbor] += paths[v]

part1 = count_paths("you", "out")
part2 = (count_paths("svr", "dac") * count_paths("dac", "fft") * count_paths("fft", "out")) + (count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out"))
print(part1)
print(part2)
