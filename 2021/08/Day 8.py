#!/usr/bin/env python3
# Part 1

with open('input') as f:
    d = [ list(map(len, line.split(' | ')[1].split())) for line in f.read().splitlines() ]

print(sum(sum(map(r.count, [2, 3, 4, 7])) for r in d ))


# Part 2

from collections import Counter

with open('input') as f:
    d = [ [ tuple(w.split()) for w in line.split(' | ')] for line in f.read().splitlines() ]


# ## Logic for solving:
# | segment | frequency | known numbers|
# | -----|-----|-----|
# | A | 8 | 7|
# | B | 6 | 4|
# | C | 8 | 1, 7, 4|
# | D | 7 | 4
# | E | 4|
# | F | 9 |1, 7, 4
# | G | 7|

def solve(r, code):
    s = sorted(list(zip(map(len, r), r)))
    counts = Counter("".join(r)).items()
    tt = str.maketrans({
        (set(s[1][1]) - set(s[0][1])).pop(): 'a',
        [ k for k, v in counts if v == 6][0]: 'b',
        (set(k for k, v in counts if v == 8) & set(s[0][1])).pop(): 'c',
        (set(k for k, v in counts if v == 7) & set(s[2][1])).pop(): 'd',
        [ k for k, v in counts if v == 4][0]: 'e',
        [ k for k, v in counts if v == 9][0]: 'f',
        (set(k for k, v in counts if v == 7) - set(s[2][1])).pop(): 'g',
    })
    result = ""
    for x in code:
        result += str({
            'abcefg': 0,
            'cf': 1,
            'acdeg': 2,
            'acdfg': 3,
            'bcdf': 4,
            'abdfg': 5,
            'abdefg': 6,
            'acf': 7,
            'abcdefg': 8,
            'abcdfg': 9
        }.get("".join(sorted(x.translate(tt)))))

    return int(result)

print(sum(solve(*row) for row in d))

