#!/usr/bin/env python3
fresh = True
franges = []


def range_same(r1, r2):
    l1, h1 = r1
    l2, h2 = r2
    return (l2 <= h1 and l1 <= l2) or (h1 >= h2 and l1 <= h2) or (l1 == h2 + 1) or (l2 == h1 + 1)

def merge(l, lo, hi):
    to_merge = []
    newl = []
    while l:
        r = l.pop()
        if range_same((lo, hi), r):
            to_merge.append(r)
        else:
            newl.append(r)
    l = newl
    loo = lo
    hii = hi
    for (alo, ahi) in to_merge:
        loo = min(alo, loo)
        hii = max(ahi, hii)
    newl.append((loo, hii))
    return newl
    

count = 0
with open("input.txt") as f:
    for line in f:
        if not line.strip():
            fresh = False
        else:
            if fresh:
                lo, hi = (int(x) for x in line.strip().split("-"))
                franges = merge(franges, lo, hi)
            else:
                for lo, hi in franges:
                    if lo <= int(line.strip()) <= hi:
                        count += 1
                        break

good = False
while not good:
    i = 0
    while i < len(franges):
        lo, hi = franges.pop(i)
        franges = merge(franges, lo, hi)
        i += 1

    # optimism
    good = True
    for i, ri in enumerate(franges):
        for j, rj in enumerate(franges):
            if i != j:
                good = good and not range_same(ri, rj)

freshness = 0
for lo, hi in franges:
    freshness += hi - lo + 1
print(count)
print(freshness)
