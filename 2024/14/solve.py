#!/usr/bin/env python3
from dataclasses import dataclass
from functools import reduce
from operator import mul
from zlib import compress

WIDTH = 101
HEIGHT = 103


@dataclass
class Robot:
    position: tuple[int, int]
    velocity: tuple[int, int]

    def simulate(self, time=1):
        x, y = self.position
        dx, dy = self.velocity
        x = (x + dx * time) % WIDTH
        y = (y + dy * time) % HEIGHT
        self.position = (x, y)
        return self.position


robots = []
robots2 = []
for line in open("input"):
    for expr in line.split():
        exec(expr)
    # now p and v are defined
    robots.append(Robot(p, v))
    robots2.append(Robot(p, v))


def quadrants(points: list[tuple[int, int]]) -> list[int]:
    q = [0, 0, 0, 0]
    for x, y in points:
        if y > (HEIGHT // 2) and x > (WIDTH // 2):
            q[0] += 1
        if y < (HEIGHT // 2) and x > (WIDTH // 2):
            q[1] += 1
        if y > (HEIGHT // 2) and x < (WIDTH // 2):
            q[2] += 1
        if y < (HEIGHT // 2) and x < (WIDTH // 2):
            q[3] += 1
    return q


print(reduce(mul, quadrants([r.simulate(100) for r in robots])))

for s in range(1, 10000):
    buf = 0  # use an int as a buffer
    for robot in robots2:
        x, y = robot.simulate()
        buf |= 1 << (WIDTH * y + x)
    # Level 1 is minimum compression (good enough for this use case)
    if (len(compress(buf.to_bytes(WIDTH * HEIGHT // 8 + 7, "big"), level=1))) < 450:
        print(s)
        # If you want to see the christmas tree:
        # print("\n".join(bin(buf)[2 + i : 2 + i + WIDTH] for i in range(0, WIDTH * HEIGHT, WIDTH)))
        break
