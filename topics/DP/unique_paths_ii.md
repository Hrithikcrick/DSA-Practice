# 63. Unique Paths II

## Problem Link

https://leetcode.com/problems/unique-paths-ii/description/

## Platform

LeetCode

## Difficulty

Medium

## Topic

Dynamic Programming, Grid DP, Tabulation

## Companies

Not available

## Problem Description

A robot is initially located at the top-left corner of a grid.

The robot wants to reach the bottom-right corner.

The robot can move only:

    Right
    Down

Some cells contain obstacles.

In obstacleGrid:

    0 means empty cell
    1 means obstacle

The robot cannot pass through obstacle cells.

Return the total number of unique paths from top-left to bottom-right.

## Intuition

This problem is similar to Unique Paths.

In normal Unique Paths:

    dp[i][j] = ways from top + ways from left

But here, if a cell has obstacle, then that cell cannot be used.

So for obstacle cell:

    dp[i][j] = 0

Otherwise:

    dp[i][j] = up + left

where:

    up = dp[i - 1][j]
    left = dp[i][j - 1]

Starting cell:

    dp[0][0] = 1

But if starting cell itself is obstacle, then answer is 0.

## Code

    from typing import List

    class Solution:
        def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
            m = len(obstacleGrid)
            n = len(obstacleGrid[0])

            if obstacleGrid[0][0] == 1:
                return 0

            dp = [[0 for _ in range(n)] for _ in range(m)]
            dp[0][0] = 1

            for i in range(m):
                for j in range(n):

                    if i == 0 and j == 0:
                        continue

                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                        continue

                    if i > 0:
                        up = dp[i - 1][j]
                    else:
                        up = 0

                    if j > 0:
                        left = dp[i][j - 1]
                    else:
                        left = 0

                    dp[i][j] = up + left

            return dp[m - 1][n - 1]

## Dry Run

Input:

    obstacleGrid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

Grid:

    0  0  0
    0  1  0
    0  0  0

Here 1 means obstacle.

Initial:

    m = 3
    n = 3

Since starting cell obstacleGrid[0][0] is 0, we can start.

Create dp table:

    dp = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

Set starting cell:

    dp[0][0] = 1

Now:

    dp = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

### Cell (0, 0)

This is starting cell.

So we skip it.

### Cell (0, 1)

obstacleGrid[0][1] = 0, so it is not obstacle.

Top does not exist because this is first row.

    up = 0

Left:

    left = dp[0][0] = 1

So:

    dp[0][1] = up + left
    dp[0][1] = 0 + 1
    dp[0][1] = 1

DP becomes:

    [
        [1, 1, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

### Cell (0, 2)

obstacleGrid[0][2] = 0.

Top does not exist.

    up = 0

Left:

    left = dp[0][1] = 1

So:

    dp[0][2] = 1

DP becomes:

    [
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0]
    ]

### Cell (1, 0)

obstacleGrid[1][0] = 0.

Up:

    up = dp[0][0] = 1

Left does not exist because this is first column.

    left = 0

So:

    dp[1][0] = 1

DP becomes:

    [
        [1, 1, 1],
        [1, 0, 0],
        [0, 0, 0]
    ]

### Cell (1, 1)

obstacleGrid[1][1] = 1.

This is obstacle.

So:

    dp[1][1] = 0

We continue to next cell.

DP remains:

    [
        [1, 1, 1],
        [1, 0, 0],
        [0, 0, 0]
    ]

### Cell (1, 2)

obstacleGrid[1][2] = 0.

Up:

    up = dp[0][2] = 1

Left:

    left = dp[1][1] = 0

Left is 0 because there is an obstacle at (1, 1).

So:

    dp[1][2] = 1 + 0
    dp[1][2] = 1

DP becomes:

    [
        [1, 1, 1],
        [1, 0, 1],
        [0, 0, 0]
    ]

### Cell (2, 0)

obstacleGrid[2][0] = 0.

Up:

    up = dp[1][0] = 1

Left does not exist.

    left = 0

So:

    dp[2][0] = 1

DP becomes:

    [
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 0]
    ]

### Cell (2, 1)

obstacleGrid[2][1] = 0.

Up:

    up = dp[1][1] = 0

This is 0 because cell (1, 1) is obstacle.

Left:

    left = dp[2][0] = 1

So:

    dp[2][1] = 0 + 1
    dp[2][1] = 1

DP becomes:

    [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]

### Cell (2, 2)

obstacleGrid[2][2] = 0.

Up:

    up = dp[1][2] = 1

Left:

    left = dp[2][1] = 1

So:

    dp[2][2] = 1 + 1
    dp[2][2] = 2

Final DP:

    [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 2]
    ]

Answer:

    dp[m - 1][n - 1]
    dp[2][2]
    2

## Important Mistake

Do not write:

    return 0

when you find an obstacle inside the grid.

Because one obstacle cell does not mean the whole answer is 0.

Correct logic:

    if obstacleGrid[i][j] == 1:
        dp[i][j] = 0
        continue

Obstacle only means:

    ways to reach this cell = 0

Then we continue checking other cells.

## Edge Cases

### Starting cell is obstacle

Input:

    [[1]]

Output:

    0

Because robot cannot even start.

### Ending cell is obstacle

Input:

    [[0, 0], [0, 1]]

Output:

    0

Because robot cannot reach final cell.

### No obstacle

Then it works like normal Unique Paths.

## Complexity

Time Complexity:

    O(m * n)

Space Complexity:

    O(m * n)
