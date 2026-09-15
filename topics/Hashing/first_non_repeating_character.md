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

The first character is determined by its position in the string, not alphabetically.

If every character repeats, return:

    ""

Example:

    text = "swiss"

Output:

    "w"

Because:

    s -> appears 3 times
    w -> appears 1 time
    i -> appears 1 time

Although both `w` and `i` occur once, `w` appears first in the original string.

## Intuition

We need the first character whose frequency is exactly 1.

There are two things we need to know:

1. How many times each character occurs.
2. Which unique character appears first in the original string.

So we use two passes.

### First Pass

Build a frequency map.

For:

    text = "swiss"

The frequency map becomes:

    s -> 3
    w -> 1
    i -> 1

### Second Pass

Scan the original string from left to right.

    s -> frequency 3 -> skip
    w -> frequency 1 -> return "w"

We return immediately because the first frequency-1 character encountered is automatically the first non-repeating character.

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

## Dry Run 1

Input:

    text = "swiss"

### Build Frequency Map

Start:

    freq = {}

Read `s`:

    freq = {
        's': 1
    }

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

Read next `s`:

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

Now scan the original string.

    c = 's'
    freq['s'] = 3

Not unique, so continue.

Next:

    c = 'w'
    freq['w'] = 1

So return:

    "w"

## Dry Run 2

Input:

    text = "aabbc"

Frequency map:

    a -> 2
    b -> 2
    c -> 1

Scan:

    a -> 2 -> skip
    a -> 2 -> skip
    b -> 2 -> skip
    b -> 2 -> skip
    c -> 1 -> return "c"

Answer:

    "c"

## Dry Run 3

Input:

    text = "aabb"

Frequency map:

    a -> 2
    b -> 2

No character has frequency 1.

Return:

    ""

## Pattern

This is a common two-pass frequency-map pattern:

    first pass  -> count frequencies
    second pass -> use original order

Use this pattern when the problem asks for:

- first unique character
- first repeated character
- first element satisfying a frequency condition
- frequency information while preserving original order

## Complexity

Let `n` be the length of the string.

First pass:

    O(n)

Second pass:

    O(n)

Total Time Complexity:

    O(n)

Space Complexity:

    O(1)

Since the string contains only lowercase English letters, the frequency map contains at most 26 keys.
