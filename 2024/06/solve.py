#!/usr/bin/env python3
COMPASS = ((-1, 0), (0, 1), (1, 0), (0, -1))  # NESW

def in_bounds(pos, g):
    return 0 <= pos[0] < len(g) and 0 <= pos[1] < len(g[0])


start_pos = (-1, -1)
# Populate the graph
graph = []
for row_idx, line in enumerate(open("input")):
    if "^" in line:
        start_pos = (row_idx, line.index("^"))
    graph.append([c == "#" for c in line.rstrip()])


def walk(graph: list[list[bool]], pos: tuple[int, int]) -> set[tuple[int, int]]:
    visited: set[tuple[int, int]] = set()
    orient = 0
    while in_bounds(pos, graph):
        visited.add(pos)
        try:
            if graph[pos[0] + COMPASS[orient][0]][pos[1] + COMPASS[orient][1]]:
                orient = (orient + 1) % 4
                continue
        except IndexError:
            break
        pos = (pos[0] + COMPASS[orient][0], pos[1] + COMPASS[orient][1])
    return visited

def is_rotation(l1, l2):
    if len(l1) != len(l2):
        return False
    doubled = l1*2
    n = len(l1)
    return any(doubled[i:i+n] == l2  for i in range(n))

def detect_cycle(graph: list[list[bool]], pos: tuple[int, int]) -> bool:
    blocks = set()
    orient = 0
    pathlen = 0
    while in_bounds(pos, graph) and in_bounds(
        tuple(map(sum, zip(pos, COMPASS[orient]))), graph
    ):
        pathlen += 1
        new_pos = (pos[0] + COMPASS[orient][0], pos[1] + COMPASS[orient][1])
        if graph[new_pos[0]][new_pos[1]]:
            if (new_pos, orient) in blocks:
                return True
            blocks.add((new_pos, orient))
            orient = (orient + 1) % 4
        else:
            pos = (pos[0] + COMPASS[orient][0], pos[1] + COMPASS[orient][1])
    return False


options = walk(graph, start_pos)
print(len(options))
options.remove(start_pos)
count = 0
for pos in options:
    testgraph = [row[:] for row in graph]
    testgraph[pos[0]][pos[1]] = True
    if detect_cycle(testgraph, start_pos):
        count += 1
print(count)
