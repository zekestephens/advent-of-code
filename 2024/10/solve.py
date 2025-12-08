#!/usr/bin/env python3
from collections import deque

cells = dict()
trailheads = set()
for y, line in enumerate(open("input")):
    for x, c in enumerate(line.rstrip()):
        if int(c) == 0:
            trailheads.add((x, y))
        cells[(x, y)] = int(c)


def neighbors(point):
    x, y = point
    return [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]


def score(cells, th):
    # simple BFS
    visited = set()
    q = deque([])
    q.append(th)
    visited.add(th)
    pinnacles = set()
    while q:
        cur = q.popleft()
        if cells[cur] == 9:
            pinnacles.add(cur)
            continue
        for adj in neighbors(cur):
            if adj not in visited and cells.get(adj, 0) == 1 + cells[cur]:
                visited.add(adj)
                q.append(adj)
    return len(pinnacles)


def rate(cells, th):
    count = 0
    # simpler BFS
    q = deque([])
    q.append(th)
    while q:
        cur = q.popleft()
        if cells[cur] == 9:
            count += 1
            continue
        for adj in neighbors(cur):
            if cells.get(adj, 1e999) == 1 + cells[cur]:
                q.append(adj)
    return count


print(sum(score(cells, th) for th in trailheads))
print(sum(rate(cells, th) for th in trailheads))
