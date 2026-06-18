# 64. Minimum Path Sum

## Problem Link

https://leetcode.com/problems/minimum-path-sum/description/

## Platform

LeetCode

## Difficulty

Medium

## Topic

Dynamic Programming, Grid DP, Recursion, Memoization

## Problem Statement

You are given a grid filled with non-negative numbers.

You can move only:

    right
    down

Find the minimum path sum from top-left cell to bottom-right cell.

## Intuition

For every cell, we ask:

    To reach this cell, from where can we come?

Since movement is only right and down, in reverse direction we can come from:

    up
    left

So for cell (i, j):

    minimum path to (i, j)
    = grid[i][j] + min(path from up, path from left)

## DP Meaning

    dp[i][j]

means:

    minimum path sum needed to reach cell (i, j)

## Base Case

If we are at the starting cell:

    i == 0 and j == 0

then answer is:

    grid[0][0]

## Invalid Case

If we go outside the grid:

    i < 0 or j < 0

return infinity, because invalid path should never be selected.

## Recurrence

    up = func(i - 1, j)
    left = func(i, j - 1)

    dp[i][j] = grid[i][j] + min(up, left)

## Code

    from typing import List

    class Solution:
        def minPathSum(self, grid: List[List[int]]) -> int:
            m = len(grid)
            n = len(grid[0])

            dp = [[-1 for _ in range(n)] for _ in range(m)]

            def func(i, j):
                if i == 0 and j == 0:
                    return grid[0][0]

                if i < 0 or j < 0:
                    return float("inf")

                if dp[i][j] != -1:
                    return dp[i][j]

                up = func(i - 1, j)
                left = func(i, j - 1)

                dp[i][j] = grid[i][j] + min(up, left)

                return dp[i][j]

            return func(m - 1, n - 1)

## Dry Run

Input:

    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]

We need minimum path sum from:

    top-left = grid[0][0]

to:

    bottom-right = grid[2][2]

For cell (2, 2), value is 1.

To reach (2, 2), we can come from:

    up   = (1, 2)
    left = (2, 1)

So:

    func(2, 2) = grid[2][2] + min(func(1, 2), func(2, 1))

For each cell, we repeat the same idea.

The best path is:

    1 -> 3 -> 1 -> 1 -> 1

Sum:

    7

So output is:

    7

## Why Memoization Is Needed

Without dp, the same cell is calculated many times.

So we store the answer:

    dp[i][j]

If already calculated, directly return it.

## Complexity

Time Complexity:

    O(m * n)

Space Complexity:

    O(m * n)
