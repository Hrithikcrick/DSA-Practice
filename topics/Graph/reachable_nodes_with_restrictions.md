# 2368. Reachable Nodes With Restrictions

## Problem Link

https://leetcode.com/problems/reachable-nodes-with-restrictions/description/

## Platform

LeetCode

## Difficulty

Medium

## Topic

Graph, DFS, Tree

## Companies

Not available

## Problem Description

We are given an undirected tree with `n` nodes numbered from `0` to `n - 1`.

Some nodes are restricted.

We need to return the number of nodes reachable from node `0` without visiting any restricted node.

## Intuition

Since the input is given as edges, first convert it into an adjacency list.

Then start DFS from node `0`.

Whenever DFS reaches a valid node, count that node.

If the next child is restricted, skip that child completely.

Since the tree is undirected, we also pass parent to avoid going back to the previous node again.

## Why Count Starts From 1

When DFS enters a node, it means that node is reachable.

So we count the current node first:

    count = 1

Then we add reachable nodes from all valid children:

    count += dfs(child, node)

## DFS Logic

For every child of current node:

    if child is parent:
        skip it

    if child is restricted:
        skip it

    otherwise:
        go deeper using DFS and add its reachable count

## Code

    from typing import List

    class Solution:
        def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
            graph = [[] for _ in range(n)]

            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            avoid = set()
            for i in range(len(restricted)):
                avoid.add(restricted[i])

            def dfs(node, parent):
                count = 1

                for child in graph[node]:
                    if child == parent:
                        continue

                    if child in avoid:
                        continue

                    count += dfs(child, node)

                return count

            return dfs(0, -1)

## Dry Run

Input:

    n = 7
    edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
    restricted = [4,5]

Tree:

          0
        / | \
       1  4  5
      / \     \
     2   3     6

Restricted nodes:

    4, 5

Start DFS from node 0:

    dfs(0, -1)

Node 0 is reachable, so:

    count = 1

Children of 0:

    1, 4, 5

Child 1 is not restricted, so call:

    dfs(1, 0)

Node 1 is reachable:

    count = 1

Children of 1:

    0, 2, 3

Child 0 is parent, skip.

Child 2 is not restricted:

    dfs(2, 1)

Node 2 is reachable:

    count = 1

Node 2 has only parent, so returns:

    1

Back at node 1:

    count = 1 + 1 = 2

Child 3 is not restricted:

    dfs(3, 1)

Node 3 is reachable:

    count = 1

Node 3 has only parent, so returns:

    1

Back at node 1:

    count = 2 + 1 = 3

So:

    dfs(1, 0) returns 3

Back at node 0:

    count = 1 + 3 = 4

Now child 4 is restricted, skip.

Child 5 is restricted, skip.

Final answer:

    4

Reachable nodes are:

    0, 1, 2, 3

## What Mistake To Avoid

Do not write:

    count = dfs(child, node)

This overwrites the previous count.

Correct is:

    count += dfs(child, node)

Because we need to collect reachable nodes from all child branches.

Also, do not start with:

    count = 0

Because current node itself is reachable.

Correct:

    count = 1

## Complexity

Let:

    n = number of nodes

Time Complexity:

    O(n)

Each node and edge is visited at most once.

Space Complexity:

    O(n)

For adjacency list, restricted set, and recursion stack.

## Key Learning

Whenever DFS question asks for total count of nodes:

    count current node first
    then add answer from every valid child

Pattern:

    count = 1

    for child in graph[node]:
        if valid child:
            count += dfs(child)

    return count
