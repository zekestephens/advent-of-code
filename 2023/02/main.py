#!/usr/bin/env -S uv run --with numpy --script
import re
from collections import defaultdict
import numpy as np
from functools import reduce
from operator import mul

bag = np.array([12, 13, 14])  # r g b
print("Part 1:",
	sum(n + 1
		for n, game in enumerate(open("input").readlines())
		if all(
			np.array([ bag >= np.array([d["r"], d["g"], d["b"]])
				for d in (defaultdict(int,
					{ a.strip().split(" ")[1][0]: int(a.strip().split(" ")[0])
						for a in hand.split(",")})
					for hand in re.findall(
						r"(?:\d+ (?:red|green|blue)[ ,]*)+;?", game))])
            .flatten())))


print("part 2:",
	sum(
		reduce(mul,
			np.max(
				np.array([ np.array([d["r"], d["g"], d["b"]])
					for d in (defaultdict(int,
						{ a.strip().split(" ")[1][0]: int(a.strip().split(" ")[0])
							for a in hand.split(",")})
						for hand in re.findall(
							r"(?:\d+ (?:red|green|blue)[ ,]*)+;?", game))]),
			axis=0))
		for n, game in enumerate(open("input").readlines())
    ),
)
