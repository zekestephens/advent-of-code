#!/usr/bin/env python3
cals = [[]]
with open("input") as f:
    while l := f.readline():
        if l == '\n':
            cals.append([])
        else:
            cals[-1].append(int(l))


print(max(sum(x) for x in cals)) 

print(sum(sorted(sum(x) for x in cals)[-3:]))
