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
