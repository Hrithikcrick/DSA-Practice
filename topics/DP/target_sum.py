from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def solve(i, current_sum):
            if i == len(nums):
                return 1 if current_sum == target else 0

            if (i, current_sum) in dp:
                return dp[(i, current_sum)]

            plus = solve(i + 1, current_sum + nums[i])
            minus = solve(i + 1, current_sum - nums[i])

            dp[(i, current_sum)] = plus + minus
            return dp[(i, current_sum)]

        return solve(0, 0)
