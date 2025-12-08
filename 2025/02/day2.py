#!/usr/bin/env python3
def invalid1(x):
    s = str(x)
    mid = len(s) // 2
    return s[:mid] == s[mid:]

def invalid2(x):
    s = str(x)
    for i in range(1, len(s) // 2 + 1):
        if s == s[:i] * (len(s) // i):
            return True
    return False

total1 = 0
total2 = 0

with open("input.txt") as f:
    for start, end in (tuple(int(x) for x in r.split('-')) for r in f.read().split(',')):
        for n in range(start, end+1):
            if invalid1(n):
                total1 += n
            if invalid2(n):
                total2 += n
print(total1, total2)
