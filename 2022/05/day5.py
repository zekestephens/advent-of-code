#!/usr/bin/env python3
import re

moves = []
stacks = [[] for _ in range(len(open('input').readline())//4)]
with open('input') as f:
    for line in f:
        if m := re.search(r'move (\d+) from (\d+) to (\d+)', line):
            moves.append([int(n) for n in m.groups()])
        elif '[' in line:
            for box, stack in [ (x.group(1), (x.start(1) -1) //4) for x in re.finditer(r'\[([A-Z])', line)]:
                stacks[stack].insert(0, box)

for n, s, f in moves:
    # part 1
    # stacks[f-1] += stacks[s-1][:-n-1:-1]
    # part 2
    stacks[f-1] += stacks[s-1][-n:]
    del stacks[s-1][-n:]

print(''.join(s[-1] for s in stacks))
