#!/usr/bin/env python3
from operator import itemgetter

decode = itemgetter(0, -1)
x = sum(
    int("".join(decode([c for c in l if c.isdigit()])))
    for l in open("input").readlines()
)
print("Part 1: ", x)
x = sum(
    int(
        "".join(
            decode(
                [
                    c
                    for c in l.replace("one", "o1e")
                    .replace("two", "t2")
                    .replace("three", "t3e")
                    .replace("four", "4")
                    .replace("five", "5e")
                    .replace("six", "6")
                    .replace("seven", "7n")
                    .replace("eight", "e8t")
                    .replace("nine", "n9e")
                    if c.isdigit()
                ]
            )
        )
    )
    for l in open("input").readlines()
)
print("Part 2: ", x)
