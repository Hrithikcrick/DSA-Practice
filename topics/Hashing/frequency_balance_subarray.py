from typing import List

class Solution:
    def longestBalancedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1

        for i in range(n):
            freq_map = {}
            freq_count = {}

            for j in range(i, n):
                val = nums[j]

                old = freq_map.get(val, 0)

                if old > 0:
                    freq_count[old] -= 1
                    if freq_count[old] == 0:
                        del freq_count[old]

                freq_map[val] = old + 1

                new = old + 1
                freq_count[new] = freq_count.get(new, 0) + 1

                if len(freq_map) == 1:
                    ans = max(ans, j - i + 1)

                elif len(freq_count) == 2:
                    arr = list(freq_count.keys())

                    a = arr[0]
                    b = arr[1]

                    if a > b:
                        a, b = b, a

                    if b == 2 * a:
                        ans = max(ans, j - i + 1)

        return ans
