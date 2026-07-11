# 752. Open the Lock

## Problem Link

https://leetcode.com/problems/open-the-lock/description/

## Platform

LeetCode

## Difficulty

Medium

## Topic

Graph, BFS, Shortest Path

## Companies

Not available

## Problem Description

We are given a lock containing four circular wheels.

Each wheel contains digits from 0 to 9.

For every move, we can rotate one wheel:

    one position forward
    one position backward

The digits wrap around:

    9 forward becomes 0
    0 backward becomes 9

The lock initially starts at:

    "0000"

Some combinations are deadends.

If the lock reaches a deadend combination, it becomes permanently locked.

We need to find the minimum number of moves required to reach the target combination.

If reaching the target is impossible, return:

    -1

## Intuition

Treat every four-digit lock combination as a node in a graph.

For example:

    "0000"
    "1000"
    "0900"
    "1234"

From one lock combination, we can change exactly one wheel by one position.

Every wheel has two possible movements:

    forward
    backward

Since there are four wheels:

    4 wheels × 2 directions = 8 neighbours

For example, the neighbours of:

    "0000"

are:

    "1000"
    "9000"
    "0100"
    "0900"
    "0010"
    "0090"
    "0001"
    "0009"

Every movement requires exactly one turn.

Therefore, this is an unweighted shortest-path problem.

We use BFS because BFS explores states level by level.

The first time we reach the target, we have used the minimum number of turns.

## Queue State

Each queue entry stores:

    [current combination, number of moves]

For example:

    ["0000", 0]

means:

    current combination = "0000"
    moves used = 0

A neighbour generated from this state will be stored with:

    moves + 1

## Deadend Set

We convert deadends into a set:

    dead = set(deadends)

This allows us to quickly check whether a generated lock combination is blocked.

If the starting combination:

    "0000"

is itself a deadend, we immediately return:

    -1

## Visited Set

The same lock combination can be reached through different paths.

For example:

    "0000" -> "1000" -> "0000"

Without a visited set, BFS could repeatedly explore the same combinations.

We mark a combination visited when we add it to the queue.

This prevents duplicate exploration.

## Generating Neighbours

For every wheel position:

    i = 0
    i = 1
    i = 2
    i = 3

We get the current digit:

    digit = int(current[i])

Then rotate it in both directions:

    change = 1
    change = -1

The new digit is calculated using:

    new_digit = (digit + change) % 10

The modulo operation handles wrap-around.

Examples:

    (9 + 1) % 10 = 0
    (0 - 1) % 10 = 9

We then create the new lock combination:

    new_state = current[:i] + str(new_digit) + current[i + 1:]

This keeps every other wheel unchanged and replaces only the wheel at index i.

## Code

    from typing import List
    from collections import deque

    class Solution:
        def openLock(self, deadends: List[str], target: str) -> int:
            dead = set(deadends)

            if "0000" in dead:
                return -1

            queue = deque()
            queue.append(["0000", 0])

            visited = set()
            visited.add("0000")

            while queue:
                current, moves = queue.popleft()

                if current == target:
                    return moves

                for i in range(4):
                    digit = int(current[i])

                    for change in [1, -1]:
                        new_digit = (digit + change) % 10
                        new_state = current[:i] + str(new_digit) + current[i + 1:]

                        if new_state in dead or new_state in visited:
                            continue

                        visited.add(new_state)
                        queue.append([new_state, moves + 1])

            return -1

## Dry Run

Input:

    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"

Initially:

    queue = [["0000", 0]]
    visited = {"0000"}

Remove from queue:

    current = "0000"
    moves = 0

The target is not reached.

Generate the eight neighbours:

    "1000"
    "9000"
    "0100"
    "0900"
    "0010"
    "0090"
    "0001"
    "0009"

Every valid and unvisited neighbour is added to the queue with:

    moves = 1

BFS then processes all combinations reachable in one move.

After that, it processes combinations reachable in two moves.

The search continues level by level until:

    current == target

When the target is removed from the queue, its stored move count is returned.

For this example, the minimum number of moves is:

    6

## Why BFS Gives the Minimum Moves

Every graph edge represents one wheel rotation.

Therefore, every edge has the same cost:

    1 move

BFS processes combinations in this order:

    combinations reachable in 0 moves
    combinations reachable in 1 move
    combinations reachable in 2 moves
    combinations reachable in 3 moves

So the first time the target is reached, no shorter path can exist.

## When We Return -1

We return -1 in two situations.

First:

    "0000" is a deadend

Second:

    BFS finishes and the queue becomes empty without finding the target

This means every reachable valid combination has been explored, but the target could not be reached.

## Complexity

There are at most:

    10 × 10 × 10 × 10 = 10000

different lock combinations.

For every combination, we generate eight neighbours.

Time Complexity:

    O(10000 × 8)

This can be simplified to:

    O(10000)

Space Complexity:

    O(10000)

The queue and visited set can contain at most all possible lock combinations.

## Key Learning

Whenever a problem contains:

    minimum number of moves
    every move has equal cost
    states can be represented as graph nodes
    multiple possible next states

Think:

    BFS shortest path

For this problem:

    combination = graph node
    wheel rotation = graph edge
    deadend = blocked node
    visited set = prevents repeated exploration
    BFS level = number of moves
