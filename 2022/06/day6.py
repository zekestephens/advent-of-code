#!/usr/bin/env python3
import collections
from itertools import islice

def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)

sample = "nppdvjthqldpwncqszvftbrmjlhg"

print(next(i for i, x in enumerate(sliding_window(open('input').read(), 4)) if len(set(x)) == len(x))+4)

print(next(i for i, x in enumerate(sliding_window(open('input').read(), 14)) if len(set(x)) == len(x))+14)

