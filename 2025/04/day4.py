#!/usr/bin/env python3
s = set()
DIRS = ((-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))

def remove_some(s):
    reachable = set((x, y) for x, y in s
                    if sum(1 for dx, dy in DIRS
                           if (x + dx, y + dy) in s) < 4)
    s -= reachable
    return len(reachable)

with open("input.txt") as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line.strip()):
            if c == "@":
                s.add((i, j))

t = s.copy()
# Part 1
print(remove_some(t))

# Part 2
part2 = 0
while r := remove_some(s):
    part2 += r

print(part2)
