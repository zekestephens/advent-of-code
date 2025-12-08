#!/usr/bin/env python3
# Started working on this in 2025 after seeing this video recommended to me:
# https://www.youtube.com/watch?v=5rb0vvJ7NCY
#
# Still incomplete
from dataclasses import dataclass
from typing import NamedTuple
from functools import lru_cache, cache

class State(NamedTuple):
    resources: tuple[int] = (0, 0, 0, 0)
    bots: tuple[int] = (1, 0, 0, 0)
    turn: int = 0

def optimizer(costs, turns=24):
    cache = {}

    def max_geodes(start: State):
        if (start.resources, start.bots) in cache:
            entry = cache[(start.resources, start.bots)]
            if entry[0] <= start.turn:
                return entry[1]

        def advance(s: State, build: int | None = None):
            minerals = list(s.resources)
            bots = list(s.bots)

            # spend minerals to build
            if build is not None:
                for i, c in enumerate(costs[build]):
                    minerals[i] -= c

            # collect minerals
            for i, b in enumerate(bots):
                minerals[i] += b

            # build it
            if build is not None:
                bots[build] += 1

            return State(resources=tuple(minerals), bots=tuple(bots), turn=s.turn+1)

        if start.turn == turns:
            cache[(start.resources, start.bots)] = (start.turn, start.resources[3])
            return start.resources[3]

        to_try = [None]
        if (all(x >= y for x, y in zip(start.resources, costs[3])) and
            any(x == y and x != 0 for x, y in zip(start.resources, costs[3]))):
            to_try = [3]
        else:
            for i, cost in enumerate(costs[:3]):
                if all(x >= y for x, y in zip(start.resources, cost)):
                    to_try.append(i)

        result = max(max_geodes(advance(start, build=x)) for x in to_try)

        cache[(start.resources, start.bots)] = (start.turn, result)
        return result

    return max_geodes


s = 0
m = 1

with open("sample.txt") as f:
    for i, line in enumerate(f):
        tokens = [s.split() for s in line.strip().split(":")[1].split(".") if len(s) > 1]
        costs = ((int(tokens[0][4]), 0, 0, 0),
                 (int(tokens[1][4]), 0, 0, 0),
                 (int(tokens[2][4]), int(tokens[2][7]), 0, 0),
                 (int(tokens[3][4]), 0, int(tokens[3][7]), 0))
        
        s += (1 + i) * optimizer(costs)(State())
    # for _, line in zip(range(3), f):
    #     tokens = [s.split() for s in line.strip().split(":")[1].split(".") if len(s) > 1]
    #     costs = ((int(tokens[0][4]), 0, 0, 0),
    #              (int(tokens[1][4]), 0, 0, 0),
    #              (int(tokens[2][4]), int(tokens[2][7]), 0, 0),
    #              (int(tokens[3][4]), 0, int(tokens[3][7]), 0))
        
    #     m *= optimizer(costs, turns=24)(State())
        

print(m)
