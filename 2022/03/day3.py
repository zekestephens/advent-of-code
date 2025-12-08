#!/usr/bin/env python3
from string import ascii_uppercase, ascii_lowercase
import itertools
from functools import reduce

priorities = dict(zip(ascii_lowercase + ascii_uppercase, range(1,53)))

with open('input') as f:
    print(sum(priorities[set(l[: len(l) // 2]).intersection(l[len(l) // 2 :]).pop()] for l in f))

with open("input") as f:
    print(
        sum(
            priorities[
                reduce(
                    lambda x, y: x & y, (set(g).difference("\n") for g in group)
                ).pop()
            ]
            for group in itertools.zip_longest(*[f] * 3, fillvalue="")
        )
    )
