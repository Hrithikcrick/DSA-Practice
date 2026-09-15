from typing import List

class Solution:
    def minimumDistinctPrefixCost(self, arr: List[int]) -> int:
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        counts = sorted(freq.values(), reverse=True)

        ans = 0

        for i in range(len(counts)):
            ans += (i + 1) * counts[i]

        return ans
