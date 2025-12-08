#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = "<=3.11"
# dependencies = ["numpy<=1.22"]
# ///
import numpy as np

si = np.loadtxt('input', skiprows=2, dtype=np.int8).reshape([ 100, 5, 5])
nums = np.loadtxt('input', delimiter=',', max_rows=2, dtype=np.int8)

def win(board, nums):
    for i in range(nums.shape[0]):
        board = np.ma.masked_equal(board, nums[i])
        for row, col in zip(board, board.transpose()):
            if not row.any() or not col.any():
                return (i, board.sum() * nums[i])

x = [win(si[i], nums) for i in range(si.shape[0])]
x.sort()

print(x[0][1])
print(x[-1][1])
