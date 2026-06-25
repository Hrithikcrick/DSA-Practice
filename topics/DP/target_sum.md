# 494. Target Sum

## Problem Link

https://leetcode.com/problems/target-sum/description/

## Platform

LeetCode

## Difficulty

Medium

## Topic

Dynamic Programming, Recursion, Memoization

## Companies

Not available

## Problem Description

You are given an integer array nums and an integer target.

You need to build an expression by adding either + or - before each number.

Return the number of different expressions that evaluate to target.

## Intuition

At every index, we have two choices:

    Add nums[i]
    Subtract nums[i]

So for every number, we try both possibilities.

The recursive thinking is:

    plus = solve(i + 1, current_sum + nums[i])
    minus = solve(i + 1, current_sum - nums[i])

The answer from the current state is:

    plus + minus

But plain recursion will repeat many states again and again.

So we use memoization with:

    dp[(i, current_sum)]

where:

    i = current index
    current_sum = sum formed till now

## State Meaning

    solve(i, current_sum)

means:

    Number of ways to reach target using elements from index i onward,
    when the sum made till now is current_sum.

## Base Case

When i reaches the end of nums:

    if i == len(nums)

Now all numbers have been used.

If current_sum is equal to target, it means we formed one valid expression.

    return 1

Otherwise:

    return 0

## Code

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

## Dry Run

Input:

    nums = [1, 1, 1, 1, 1]
    target = 3

Start:

    solve(0, 0)

At index 0:

    nums[0] = 1

Two choices:

    +1 -> solve(1, 1)
    -1 -> solve(1, -1)

For every next index, again two choices are made.

One valid expression is:

    -1 + 1 + 1 + 1 + 1 = 3

This reaches:

    solve(5, 3)

Since current_sum == target:

    return 1

One invalid expression is:

    +1 + 1 + 1 + 1 + 1 = 5

This reaches:

    solve(5, 5)

Since current_sum != target:

    return 0

All valid paths are counted.

Final answer:

    5

## Why Memoization Works

Without memoization, every number has two choices.

So total possibilities become:

    2^n

But many states repeat.

Example:

    solve(3, 1)

can be reached from different expression paths.

So once we calculate it, we store it:

    dp[(i, current_sum)] = answer

Next time the same state appears, we directly return the stored answer.

## Complexity

Let:

    S = sum(nums)

The current_sum can range from:

    -S to +S

So total possible states are around:

    n * 2S

Time Complexity:

    O(n * sum(nums))

Space Complexity:

    O(n * sum(nums))

## Key Learning

Whenever a problem says:

    choose + or - before every number
    count number of ways to reach target

Think about:

    recursion + memoization

State should contain:

    index
    current_sum
