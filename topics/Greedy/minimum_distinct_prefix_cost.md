# Minimum Distinct Prefix Cost

## Problem Link

https://www.fastprep.io/problems/goldman-sachs-minimum-distinct-prefix-cost

## Platform

Online Assessment / Interview Practice

## Difficulty

Medium

## Topic

Greedy / Hashing / Sorting

## Companies

Goldman Sachs

## Problem

You are given an integer array `arr`.

The cost of an array is the sum of the number of distinct elements in every prefix.

You may rearrange the array in any order.

Return the minimum possible cost among all permutations of the array.

Example:

    arr = [2, 2, 3, 1, 1]

One optimal arrangement is:

    [2, 2, 1, 1, 3]

Distinct elements in every prefix:

    [2]             -> 1
    [2, 2]          -> 1
    [2, 2, 1]       -> 2
    [2, 2, 1, 1]    -> 2
    [2, 2, 1, 1, 3] -> 3

Total cost:

    1 + 1 + 2 + 2 + 3 = 9

## Intuition

The moment a new distinct value appears, the distinct count increases for that prefix and every prefix after it.

Therefore, to minimize the total cost, we should delay introducing new distinct values as much as possible.

Suppose the frequencies are:

    value 2 -> 2 times
    value 1 -> 2 times
    value 3 -> 1 time

We should place the value having the highest frequency first.

So the frequency groups should be arranged in decreasing order:

    [2, 2, 1]

This corresponds to an arrangement such as:

    [2, 2, 1, 1, 3]

For the first frequency group, every element contributes a distinct count of 1.

For the second group, every element contributes 2.

For the third group, every element contributes 3.

Therefore:

    answer =
    1 * first_frequency
    + 2 * second_frequency
    + 3 * third_frequency
    + ...

So we:

1. Build a frequency map.
2. Extract all frequencies.
3. Sort frequencies in decreasing order.
4. Add `(i + 1) * frequency[i]`.

## Code

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

## Dry Run

Input:

    arr = [2, 2, 3, 1, 1]

Build frequency map:

    freq = {
        2: 2,
        3: 1,
        1: 2
    }

Take frequencies:

    [2, 1, 2]

Sort in decreasing order:

    counts = [2, 2, 1]

Now calculate the answer.

### i = 0

    counts[0] = 2

    ans += (0 + 1) * 2
    ans = 2

This means the first distinct value occupies 2 positions.

Their prefix distinct count is 1.

### i = 1

    counts[1] = 2

    ans += (1 + 1) * 2
    ans += 4

    ans = 6

The second distinct value occupies 2 positions.

Their prefix distinct count is 2.

### i = 2

    counts[2] = 1

    ans += (2 + 1) * 1
    ans += 3

    ans = 9

Final Answer:

    9

## Why Sort Frequencies Descending?

Suppose two values occur:

    A -> 5 times
    B -> 2 times

If A comes first:

    5 positions contribute 1
    2 positions contribute 2

Cost:

    5 * 1 + 2 * 2 = 9

If B comes first:

    2 positions contribute 1
    5 positions contribute 2

Cost:

    2 * 1 + 5 * 2 = 12

So putting the larger frequency earlier gives a smaller cost.

Therefore frequencies should be sorted in decreasing order.

## Complexity

Let `n` be the size of the array and `d` be the number of distinct values.

Building frequency map:

    O(n)

Sorting frequencies:

    O(d log d)

Total Time Complexity:

    O(n + d log d)

Since d <= n:

    O(n log n)

Space Complexity:

    O(d)
