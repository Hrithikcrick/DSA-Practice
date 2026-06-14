# Jump Game

## Problem Link

https://leetcode.com/problems/jump-game/description/

## Platform

LeetCode

## Difficulty

Medium

## Topic

Greedy

## Companies

Facebook

## Intuition

We are given an array nums.

nums[i] tells us the maximum jump length from index i.

Instead of trying every jump, we maintain one variable:

    maxReach

maxReach means the farthest index we can reach till now.

If current index i is greater than maxReach, then we cannot reach this index.

So answer becomes False.

Otherwise, update maxReach:

    maxReach = max(maxReach, i + nums[i])

If maxReach reaches or crosses the last index, answer is True.

## Code

    from typing import List

    class Solution:
        def canJump(self, nums: List[int]) -> bool:
            n = len(nums)
            maxReach = 0

            for i in range(n):
                if i > maxReach:
                    return False

                maxReach = max(maxReach, i + nums[i])

                if maxReach >= n - 1:
                    return True

            return True

## Dry Run 1

Input:

    nums = [2, 3, 1, 1, 4]

Initial:

    n = 5
    maxReach = 0

### i = 0

    nums[0] = 2

Check:

    i > maxReach
    0 > 0
    False

Update:

    maxReach = max(0, 0 + 2)
    maxReach = 2

Now we can reach index 2.

### i = 1

    nums[1] = 3

Check:

    i > maxReach
    1 > 2
    False

Update:

    maxReach = max(2, 1 + 3)
    maxReach = 4

Now:

    maxReach >= n - 1
    4 >= 4
    True

Answer:

    True

## Dry Run 2

Input:

    nums = [3, 2, 1, 0, 4]

Initial:

    maxReach = 0

### i = 0

    maxReach = max(0, 0 + 3)
    maxReach = 3

### i = 1

    maxReach = max(3, 1 + 2)
    maxReach = 3

### i = 2

    maxReach = max(3, 2 + 1)
    maxReach = 3

### i = 3

    maxReach = max(3, 3 + 0)
    maxReach = 3

### i = 4

Check:

    i > maxReach
    4 > 3
    True

Index 4 is not reachable.

Answer:

    False

## Complexity

Time Complexity: O(n)

Space Complexity: O(1)
