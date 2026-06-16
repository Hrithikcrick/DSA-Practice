# 62. Unique Paths

## Problem Link

https://leetcode.com/problems/unique-paths/description/

## Platform

LeetCode

## Difficulty

Medium

## Topic

Dynamic Programming, Grid DP, Tabulation

## Companies

Not available

## Problem Description

A robot is located at the top-left corner of an m x n grid.

The robot can move only in two directions:

    Right
    Down

Return the number of unique paths to reach the bottom-right corner.

## Intuition

We need to count the number of ways to reach each cell.

At any cell (i, j), we can come from only two places:

    top cell  -> (i - 1, j)
    left cell -> (i, j - 1)

So:

    dp[i][j] = up + left

where:

    up = dp[i - 1][j]
    left = dp[i][j - 1]

The starting cell has one way because we are already standing there.

So:

    dp[0][0] = 1

## Code

    class Solution:
        def uniquePaths(self, m: int, n: int) -> int:
            dp = []

            for i in range(m):
                row = []
                for j in range(n):
                    row.append(0)
                dp.append(row)

            dp[0][0] = 1

            for i in range(m):
                for j in range(n):

                    if i == 0 and j == 0:
                        continue

                    up = 0
                    left = 0

                    if i > 0:
                        up = dp[i - 1][j]

                    if j > 0:
                        left = dp[i][j - 1]

                    dp[i][j] = up + left

            return dp[m - 1][n - 1]

## Dry Run

Input:

    m = 3
    n = 3

Grid indexes:

    (0,0)  (0,1)  (0,2)
    (1,0)  (1,1)  (1,2)
    (2,0)  (2,1)  (2,2)

Start:

    (0,0)

End:

    (2,2)

Initial DP table:

    [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

Set starting cell:

    dp[0][0] = 1

Now DP:

    [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

### Cell (0, 0)

This is the starting cell.

So we skip it.

### Cell (0, 1)

Top does not exist because it is the first row.

    up = 0

Left exists:

    left = dp[0][0] = 1

So:

    dp[0][1] = up + left
    dp[0][1] = 0 + 1
    dp[0][1] = 1

DP:

    [
        [1, 1, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

### Cell (0, 2)

Top does not exist.

    up = 0

Left:

    left = dp[0][1] = 1

So:

    dp[0][2] = 1

DP:

    [
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0]
    ]

### Cell (1, 0)

Up:

    up = dp[0][0] = 1

Left does not exist because it is the first column.

    left = 0

So:

    dp[1][0] = 1

DP:

    [
        [1, 1, 1],
        [1, 0, 0],
        [0, 0, 0]
    ]

### Cell (1, 1)

Up:

    up = dp[0][1] = 1

Left:

    left = dp[1][0] = 1

So:

    dp[1][1] = 1 + 1
    dp[1][1] = 2

DP:

    [
        [1, 1, 1],
        [1, 2, 0],
        [0, 0, 0]
    ]

### Cell (1, 2)

Up:

    up = dp[0][2] = 1

Left:

    left = dp[1][1] = 2

So:

    dp[1][2] = 1 + 2
    dp[1][2] = 3

DP:

    [
        [1, 1, 1],
        [1, 2, 3],
        [0, 0, 0]
    ]

### Cell (2, 0)

Up:

    up = dp[1][0] = 1

Left does not exist.

    left = 0

So:

    dp[2][0] = 1

DP:

    [
        [1, 1, 1],
        [1, 2, 3],
        [1, 0, 0]
    ]

### Cell (2, 1)

Up:

    up = dp[1][1] = 2

Left:

    left = dp[2][0] = 1

So:

    dp[2][1] = 2 + 1
    dp[2][1] = 3

DP:

    [
        [1, 1, 1],
        [1, 2, 3],
        [1, 3, 0]
    ]

### Cell (2, 2)

Up:

    up = dp[1][2] = 3

Left:

    left = dp[2][1] = 3

So:

    dp[2][2] = 3 + 3
    dp[2][2] = 6

Final DP:

    [
        [1, 1, 1],
        [1, 2, 3],
        [1, 3, 6]
    ]

Answer:

    dp[m - 1][n - 1]
    dp[2][2]
    6

## Complexity

Time Complexity:

    O(m * n)

Space Complexity:

    O(m * n)
