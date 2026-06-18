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
