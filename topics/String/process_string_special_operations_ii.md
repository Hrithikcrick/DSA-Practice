# 3614. Process String with Special Operations II

## Problem Link

https://leetcode.com/problems/process-string-with-special-operations-ii/description/

## Platform

LeetCode

## Difficulty

Hard

## Topic

String, Simulation, Reverse Traversal

## Companies

Not available

## Problem Description

You are given a string s consisting of lowercase English letters and special characters:

    *
    #
    %

You are also given an integer k.

Build a new string result by processing s from left to right.

Rules:

1. Lowercase letter:
   Append it to result.

2. '*':
   Remove the last character from result if it exists.

3. '#':
   Duplicate the current result.

4. '%':
   Reverse the current result.

Return the kth character of the final result.

If k is out of bounds, return '.'.

## Intuition

The direct simulation code creates the full result string.

But this can give Memory Limit Exceeded because of this operation:

    result = result + result

If '#' appears many times, result size becomes very large.

But we do not need the full string.

We only need the kth character.

So we do two passes.

First pass:

    Store only the length after every operation.

Second pass:

    Move backward from the end of s and trace where index k came from.

This avoids building the huge final string.

## Why We Use prev

During backward traversal:

    prev = arr[i - 1] if i > 0 else 0

prev means:

    length before operation s[i] happened

This is important because every reverse operation depends on the previous length.

For '#':

    old string becomes old + old

If k is in the second half:

    k = k - prev

For '%':

    string is reversed

So index changes as:

    k = prev - 1 - k

For a letter:

    letter is added at index prev

So if:

    k == prev

then this letter is the answer.

For '*':

    last character was removed

When going backward, we restore old length.

## Code

    class Solution:
        def processStr(self, s: str, k: int) -> str:
            length = 0
            arr = []

            for i in range(len(s)):

                if s[i] == "*":
                    if length > 0:
                        length -= 1

                elif s[i] == "#":
                    length = length * 2

                elif s[i] == "%":
                    length = length

                else:
                    length += 1

                arr.append(length)

            if k >= length:
                return '.'

            for i in range(len(s) - 1, -1, -1):
                prev = arr[i - 1] if i > 0 else 0

                if s[i] == "*":
                    length = prev

                elif s[i] == "#":
                    if k >= prev:
                        k -= prev
                    length = prev

                elif s[i] == "%":
                    k = prev - 1 - k
                    length = prev

                else:
                    if k == prev:
                        return s[i]
                    length = prev

            return '.'

## Dry Run

Input:

    s = "cd%#*#"
    k = 3

Expected output:

    "d"

Final string by normal simulation is:

    "dcddcd"

Index view:

    d c d d c d
    0 1 2 3 4 5

So index 3 is:

    d

## First Pass: Store Lengths Only

We do not build the full result.

We only store length after every operation.

Initial:

    length = 0
    arr = []

### i = 0, s[i] = 'c'

Append character.

Length becomes:

    length = 1

arr:

    [1]

### i = 1, s[i] = 'd'

Append character.

Length becomes:

    length = 2

arr:

    [1, 2]

### i = 2, s[i] = '%'

Reverse operation.

Length does not change.

    length = 2

arr:

    [1, 2, 2]

### i = 3, s[i] = '#'

Duplicate operation.

Length doubles.

    length = 2 * 2
    length = 4

arr:

    [1, 2, 2, 4]

### i = 4, s[i] = '*'

Remove last character.

Length decreases.

    length = 3

arr:

    [1, 2, 2, 4, 3]

### i = 5, s[i] = '#'

Duplicate operation.

Length doubles.

    length = 3 * 2
    length = 6

arr:

    [1, 2, 2, 4, 3, 6]

Final length is:

    6

Since:

    k = 3

and:

    3 < 6

answer exists.

Now we go backward.

## Second Pass: Reverse Traversal

Current values:

    k = 3
    length = 6
    arr = [1, 2, 2, 4, 3, 6]

We move from right to left.

### i = 5, s[i] = '#'

Before this '#', length was:

    prev = arr[4]
    prev = 3

Before '#':

    "dcd"

After '#':

    "dcddcd"

Index view:

    d c d | d c d
    0 1 2 | 3 4 5

Current:

    k = 3

Since:

    k >= prev
    3 >= 3

k is in the second copy.

So map it back to first copy:

    k = k - prev
    k = 3 - 3
    k = 0

Now:

    length = prev
    length = 3

### i = 4, s[i] = '*'

Before '*', length was:

    prev = arr[3]
    prev = 4

'*' removed last character.

Going backward, we restore length:

    length = prev
    length = 4

k does not change:

    k = 0

### i = 3, s[i] = '#'

Before '#', length was:

    prev = arr[2]
    prev = 2

Before '#':

    "dc"

After '#':

    "dcdc"

Index view:

    d c | d c
    0 1 | 2 3

Current:

    k = 0

Since:

    k >= prev
    0 >= 2

False.

So k stays:

    k = 0

Restore previous length:

    length = 2

### i = 2, s[i] = '%'

Before reverse, length was:

    prev = arr[1]
    prev = 2

Before reverse:

    "cd"

After reverse:

    "dc"

Index mapping:

    after index 0 came from before index 1
    after index 1 came from before index 0

Formula:

    k = prev - 1 - k

Current:

    k = 0

So:

    k = 2 - 1 - 0
    k = 1

Now:

    length = 2

### i = 1, s[i] = 'd'

Before adding 'd', length was:

    prev = arr[0]
    prev = 1

Letter 'd' was appended at index:

    1

Current:

    k = 1

Since:

    k == prev
    1 == 1

This character is the answer.

Return:

    "d"

## Final Answer

    "d"

## Why This Avoids Memory Limit Exceeded

Old code used:

    result = result + result

This creates a huge string/list.

New code uses:

    length = length * 2

So we only store lengths, not the actual full string.

## Edge Cases

### Empty result after processing

Input:

    s = "z*#"
    k = 0

Final result is empty.

Since k is out of bounds, return:

    "."

### k outside final length

If:

    k >= length

return:

    "."

### Many '#'

Even if final length becomes very large, we only store length values.

## Complexity

Time Complexity:

    O(n)

Space Complexity:

    O(n)

where n is length of s.
