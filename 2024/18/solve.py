#!/usr/bin/env python3
from heapq import heappop, heappush

COMPASS = ((-1, 0), (0, 1), (1, 0), (0, -1))
DIMS = 70
NUM_FALLEN = 1024

blocked_l = []
for line in open("input"):
    blocked_l.append(eval(line.rstrip()))


def path_length(blocked: set[tuple[int, int]]) -> int:
    start = (0, 0)
    end = (DIMS, DIMS)

    pq = [(0, start)]
    visited = set()
    predecessors = {}

    while pq:
        dist, pos = heappop(pq)
        if pos == end:
            path = 0
            while pos in predecessors:
                pos = predecessors[pos]
                path += 1
            return path
        if pos in visited:
            continue
        visited.add(pos)
        for dx, dy in COMPASS:
            x, y = pos
            new_x = x + dx
            new_y = y + dy
            new_pos = (new_x, new_y)
            if (
                0 <= new_x <= DIMS
                and 0 <= new_y <= DIMS
                and new_pos not in blocked
                and new_pos not in visited
            ):
                predecessors[new_pos] = pos
                heappush(pq, (dist + 1, new_pos))
    return 0


blocked = set(blocked_l[:NUM_FALLEN])
print(path_length(blocked))
for i in range(NUM_FALLEN, DIMS * DIMS):
    blocked.add(blocked_l[i])
    if not path_length(blocked):
        print(",".join(map(str, blocked_l[i])))
        break
