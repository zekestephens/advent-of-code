#!/usr/bin/env python3
import sys
from collections import defaultdict

deps = defaultdict(set)

# read in dependency graph
lines = iter(open("input"))
for line in lines:
    if line == "\n":
        break
    a, b = map(int, line.split('|'))
    deps[b].add(a)

updates = []
# read in updates
for line in lines:
    updates.append([int(x) for x in line.split(',')])

def valid(update):
    return not any(deps[n].intersection(update[i+1:]) for i, n in enumerate(update))

print(sum(update[len(update)//2] for update in updates if valid(update)))

def fix_invalid(update):
    res = update.copy()
    while not valid(res):
        for i in range(len(res)):
            if ins := deps[res[i]].intersection(res[i + 1:]):
                dep_ind = res.index(list(ins)[0])
                res[i], res[dep_ind] = res[dep_ind], res[i]
    return res

print(sum(fix_invalid(update)[len(update)//2] for update in updates if not valid(update)))
