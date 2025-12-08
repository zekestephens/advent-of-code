#!/usr/bin/env python3
# This script doesn't work!
import collections.abc
# increase recursion limit
import sys
sys.setrecursionlimit(1000000)

with open("input") as f:
    input = f.read()

input = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

# Read input to a graph
graph = {}
for line in input.split("\n"):
    if line:
        graph.setdefault(line.split("-")[0], []).append(line.split("-")[1])
        graph.setdefault(line.split("-")[1], []).append(line.split("-")[0])


# print(graph)

def paths_to_end(graph, vertex):
    if vertex == "end":
        return [[]]
    paths = []
    for neighbor in graph[vertex]:
        if neighbor != "start":
            for path in paths_to_end(graph, neighbor):
                paths.append([neighbor] + path)
    return paths


paths = set()
# find all paths from start to end without visiting lowercase verticies more than twice
def find_end(current_vertex="start", current_path=["start"]):
    # print(graph)
    if current_vertex == "end":
        paths.add(tuple(current_path))
        return current_path
    else:
        return [
            find_end(current_vertex=vertex, current_path=current_path + [vertex])
            for vertex in graph[current_vertex]
            if vertex != "start" and (vertex.isupper() or vertex not in current_path)
        ]


def flatten(l):
    for el in l:
        if isinstance(el, collections.abc.Iterable) and not isinstance(
            el, (str, bytes)
        ):
            yield from flatten(el)
        else:
            yield el


find_end()
print(len(paths))
# print(*paths, sep="\n")
print(paths_to_end(graph, "start"))
