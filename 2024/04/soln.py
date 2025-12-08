#!/usr/bin/env -S uv run --with numpy --script
import sys

import numpy as np

matrix = np.array([[c for c in line if c != "\n"] for line in open("input")])


def words(matrix, i, j):
    y_lower_bound = i - 3 if i - 3 >= 0 else i
    y_upper_bound = i + 4 if i + 4 <= len(matrix) else i + 1
    x_lower_bound = j - 3 if j - 3 >= 0 else j
    x_upper_bound = j + 4 if j + 4 <= len(matrix) else j + 1

    def get_bounded(i, j):
        if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
            return matrix[i, j]
        return ""

    word_list = {
        "north": matrix[y_lower_bound:y_upper_bound, j][:4],
        "south": matrix[y_lower_bound:y_upper_bound, j][3:],
        "west": matrix[i, x_lower_bound:x_upper_bound][:4],
        "east": matrix[i, x_lower_bound:x_upper_bound][3:],
        "NE": [
            get_bounded(i, j),
            get_bounded(i + 1, j + 1),
            get_bounded(i + 2, j + 2),
            get_bounded(i + 3, j + 3),
        ],
        "SE": [
            get_bounded(i, j),
            get_bounded(i - 1, j + 1),
            get_bounded(i - 2, j + 2),
            get_bounded(i - 3, j + 3),
        ],
        "NW": [
            get_bounded(i, j),
            get_bounded(i - 1, j - 1),
            get_bounded(i - 2, j - 2),
            get_bounded(i - 3, j - 3),
        ],
        "SW": [
            get_bounded(i, j),
            get_bounded(i + 1, j - 1),
            get_bounded(i + 2, j - 2),
            get_bounded(i + 3, j - 3),
        ],
    }
    return sum(
        1
        for word in map("".join, word_list.values())
        if word == "XMAS" or word == "SAMX"
    ), word_list


count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i, j] == "X":
            res = words(matrix, i, j)
            count += res[0]
            # print(i, j)
            # for k, w in res[1].items():
            #     print(f'{k}:\t{"".join(w)}')
            # print()

print(count)

count = 0


def x_masses(arr):
    n = 0
    if all(
        "".join(s) == "AMS"
        for s in map(sorted, [arr.diagonal(), np.fliplr(arr).diagonal()])
    ):
        n += 1
    return n


# part 2
for i in range(1, len(matrix) - 1):
    for j in range(1, len(matrix[0]) - 1):
        if matrix[i, j] == "A":
            count += x_masses(matrix[i - 1 : i + 2, j - 1 : j + 2])
print(count)
