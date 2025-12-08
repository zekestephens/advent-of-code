#!/usr/bin/env python3
from ast import literal_eval

rangeplusone = lambda x, y: range(x, y + 1)
with open("input") as f:
    print(
        sum(
            l[0] <= l[1] or l[1] <= l[0]
            for l in (
                [
                    set(rangeplusone(*[literal_eval(x) for x in ass.split("-")]))
                    for ass in line.split(",")
                ]
                for line in f
            )
        )
    )

with open("input") as f:
    print(
        sum(
            bool(l[0] & l[1])
            for l in (
                [
                    set(rangeplusone(*[literal_eval(x) for x in ass.split("-")]))
                    for ass in line.split(",")
                ]
                for line in f
            )
        )
    )
