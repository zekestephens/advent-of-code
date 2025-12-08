#!/usr/bin/env python3
second = lambda x: int(x[1])

def part1():
    total = 0
    with open("input.txt") as f:
        for line in f:
            l = line.strip()
            x = max(enumerate(l), key=second)
            y = 0
            if x[0] == len(l) - 1:
                y = x
                x = max(enumerate(l[:x[0]]), key=second)
            else:
                y = max(enumerate(l[x[0] + 1:]), key=second)
            total += int(x[1] + y[1])
    return total

def part2():
    total = 0
    with open("input.txt") as f:
        for line in f:
            offset = 0
            chosen = []
            l = line.strip()
            for i in range(-11, 1):
                # old version for posterity
                # m = max(enumerate(l[offset:1-i]), key=second) if i > 1 else max(enumerate(l[offset:]), key=second)
                # new version:
                m = max(enumerate(l[offset : i or None]), key=second)
                offset += m[0] + 1
                chosen.append(m[1])
            total += int(''.join(chosen))
    return total

print(part1())
print(part2())
