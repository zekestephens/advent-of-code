#!/usr/bin/env python3
second = lambda x: x[1]

def joltage(bank, limit):
    offset = 0
    chosen = []
    for i in range(1-limit, 1):
        m = max(enumerate(bank[offset : i or None]), key=second)
        offset += m[0] + 1
        chosen.append(m[1])
    return int(''.join(chosen))

count1 = 0
count2 = 0

with open("input.txt") as f:
    for line in f:
        count1 += joltage(line.strip(), 2)
        count2 += joltage(line.strip(), 12)

print(count1)
print(count2)
