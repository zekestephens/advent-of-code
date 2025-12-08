#!/usr/bin/env python3
import re
from collections import Counter
from functools import reduce

with open("input") as f:
    infile = f.read()

rules = dict(re.findall(r"([A-Z]{2}) -> ([A-Z])", infile))
template = infile.partition("\n\n")[0]


def insert_at_pair(left, right):
    return left + rules[left[-1] + right] + right


for _ in range(10):
    template = reduce(insert_at_pair, template)

print((counts := sorted(Counter(template).values()))[-1] - counts[0])
exit(0)

# The rest of this _should_ work but it takes unreasonably long
for _ in range(30):
    template = reduce(insert_at_pair, template)

print((counts := sorted(Counter(template).values()))[-1] - counts[0])
