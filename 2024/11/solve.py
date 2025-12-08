#!/usr/bin/env python3
from functools import cache

stones = [int(x) for x in open("input").read().split()]


# memoization is unreasonably effective here
@cache
def count_after_blink(stone, n=1):
    if n == 0:
        return 1
    if stone == 0:
        return count_after_blink(1, n - 1)
    if (s := len(str(stone))) % 2 == 0:
        return count_after_blink(int(str(stone)[: s // 2]), n - 1) + count_after_blink(
            int(str(stone)[s // 2 :]), n - 1
        )
    return count_after_blink(stone * 2024, n - 1)


print(sum(count_after_blink(stone, n=25) for stone in stones))
print(sum(count_after_blink(stone, n=75) for stone in stones))
