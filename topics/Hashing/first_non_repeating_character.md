# First Non-Repeating Character

## Problem Link

https://www.fastprep.io/problems/goldman-sachs-first-non-repeating-character

## Platform

FastPrep

## Difficulty

Easy

## Topic

String / Hashing / Frequency Map

## Companies

Goldman Sachs

## Problem

Given a non-empty string `text` containing lowercase English letters, return the first character that occurs exactly once.

The first character is determined by its position in the original string, not alphabetical order.

If every character repeats, return:

    ""

### Example 1

Input:

    text = "swiss"

Output:

    "w"

### Example 2

Input:

    text = "aabbc"

Output:

    "c"

### Example 3

Input:

    text = "aabb"

Output:

    ""

## Intuition

We need to find the first character whose frequency is exactly 1.

We need two things:

1. Frequency of every character.
2. Original order of characters.

So we use two passes.

### First Pass

Build a frequency map.

For:

    text = "swiss"

We get:

    s -> 3
    w -> 1
    i -> 1

### Second Pass

Traverse the original string from left to right.

    s -> frequency 3 -> skip
    w -> frequency 1 -> return "w"

Since we traverse from left to right, the first character with frequency 1 is automatically the first non-repeating character.

If no character has frequency 1, return an empty string.

## Code

    class Solution:
        def firstNonRepeatingCharacter(self, text: str) -> str:
            freq = {}

            for c in text:
                freq[c] = freq.get(c, 0) + 1

            for c in text:
                if freq[c] == 1:
                    return c

            return ""

## Dry Run

Input:

    text = "swiss"

Initially:

    freq = {}

Read `s`:

    freq = {'s': 1}

Read `w`:

    freq = {
        's': 1,
        'w': 1
    }

Read `i`:

    freq = {
        's': 1,
        'w': 1,
        'i': 1
    }

Read `s`:

    freq = {
        's': 2,
        'w': 1,
        'i': 1
    }

Read final `s`:

    freq = {
        's': 3,
        'w': 1,
        'i': 1
    }

Now traverse the original string.

First character:

    c = 's'
    freq['s'] = 3

Not unique.

Next character:

    c = 'w'
    freq['w'] = 1

Therefore return:

    "w"

## Pattern

Two-Pass Frequency Map

Use this pattern when a problem asks for:

- first unique character
- first repeated character
- first element with a particular frequency
- frequency checking while preserving original order

## Complexity

Let `n` be the length of the string.

Time Complexity:

    O(n)

Space Complexity:

    O(1)

The string contains only lowercase English letters, so the frequency map can contain at most 26 characters.
