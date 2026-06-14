# 3960. Frequency Balance Subarray

## Contest

LeetCode Weekly Contest 506

## Problem Link

https://leetcode.com/problems/frequency-balance-subarray/description/

## Platform

LeetCode

## Difficulty

Medium

## Topic

Hashing, Subarray, Frequency Map

## Companies

Not available

## Problem Description

You are given an integer array nums.

A subarray is frequency balanced if:

1. If the subarray contains only one distinct value, it is balanced.
2. Otherwise, there must exist a positive integer f such that every distinct value in the subarray occurs either f or 2 * f times.
3. Both frequencies f and 2 * f must occur among the distinct values.

Return the length of the longest frequency balance subarray.

## Intuition

Since nums.length is up to 1000, we can generate all subarrays.

For every starting index i, we extend the ending index j one by one.

While extending the subarray, we maintain two dictionaries:

    freq_map

This stores:

    number -> frequency of that number

Example:

    [2, 1, 2, 3, 3]

    freq_map = {
        2: 2,
        1: 1,
        3: 2
    }

Second dictionary:

    freq_count

This stores:

    frequency -> how many numbers have this frequency

For the same subarray:

    freq_count = {
        1: 1,
        2: 2
    }

This means:

    one number has frequency 1
    two numbers have frequency 2

Now frequencies are 1 and 2.

Since:

    2 = 2 * 1

this subarray is valid.

## Code

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

## Dry Run

Input:

    nums = [1, 2, 2, 1, 2, 3, 3, 3]

Expected output:

    5

The longest valid subarray is:

    [2, 1, 2, 3, 3]

This is from index 2 to index 6.

Now dry run for i = 2.

Initial:

    freq_map = {}
    freq_count = {}
    ans = 1

### j = 2

    val = nums[2] = 2
    old = 0

Update:

    freq_map = {2: 1}
    freq_count = {1: 1}

Current subarray:

    [2]

Since there is only one distinct value, it is valid.

Length:

    1

ans remains:

    ans = 1

### j = 3

    val = nums[3] = 1
    old = 0

Update:

    freq_map = {2: 1, 1: 1}
    freq_count = {1: 2}

Current subarray:

    [2, 1]

Here both numbers appear once.

Only one frequency exists:

    1

But for multiple distinct values, we need both f and 2f.

So this is not valid.

### j = 4

    val = nums[4] = 2
    old = 1

Before adding this 2:

    freq_map = {2: 1, 1: 1}
    freq_count = {1: 2}

Since 2 moves from frequency 1 to frequency 2:

Remove old frequency:

    freq_count[1] -= 1

Now:

    freq_count = {1: 1}

Update frequency of 2:

    freq_map[2] = 2

Add new frequency:

    freq_count[2] = 1

Now:

    freq_map = {2: 2, 1: 1}
    freq_count = {1: 1, 2: 1}

Current subarray:

    [2, 1, 2]

Frequencies are:

    1 and 2

Since:

    2 = 2 * 1

Valid.

Length:

    3

ans becomes:

    ans = 3

### j = 5

    val = nums[5] = 3
    old = 0

Update:

    freq_map = {2: 2, 1: 1, 3: 1}
    freq_count = {1: 2, 2: 1}

Current subarray:

    [2, 1, 2, 3]

Frequencies are:

    1 and 2

Since:

    2 = 2 * 1

Valid.

Length:

    4

ans becomes:

    ans = 4

### j = 6

    val = nums[6] = 3
    old = 1

Before adding:

    freq_map = {2: 2, 1: 1, 3: 1}
    freq_count = {1: 2, 2: 1}

3 moves from frequency 1 to frequency 2.

Remove old frequency:

    freq_count[1] -= 1

Now:

    freq_count = {1: 1, 2: 1}

Update frequency of 3:

    freq_map[3] = 2

Add new frequency:

    freq_count[2] += 1

Now:

    freq_map = {2: 2, 1: 1, 3: 2}
    freq_count = {1: 1, 2: 2}

Current subarray:

    [2, 1, 2, 3, 3]

Frequencies are:

    2 appears 2 times
    1 appears 1 time
    3 appears 2 times

Frequency types are:

    1 and 2

Since:

    2 = 2 * 1

Valid.

Length:

    5

ans becomes:

    ans = 5

Final answer:

    5

## Why This Works

For each subarray, we only need to know:

1. How many times each number appears.
2. What frequency types exist.

If there is only one distinct number, it is valid.

Otherwise, there must be exactly two frequency types.

Let those two frequency types be a and b.

If:

    b = 2 * a

then the subarray is valid.

## Complexity

Time Complexity:

    O(n^2)

Space Complexity:

    O(n)

Because n is only up to 1000, O(n^2) is acceptable.
