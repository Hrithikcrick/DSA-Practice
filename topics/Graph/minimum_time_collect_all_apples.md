# 1443. Minimum Time to Collect All Apples in a Tree

## Problem Link

https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/

## Platform

LeetCode

## Difficulty

Medium

## Topic

Tree, Graph, DFS

## Companies

Not available

## Problem Description

We are given an undirected tree with `n` nodes.

Some nodes have apples.

Starting from node `0`, we need to collect all apples and return back to node `0`.

Each edge takes 1 second to travel.

Since we go and come back through an edge, useful edge cost becomes:

    2

Return the minimum time needed to collect all apples.

## Intuition

Since the input is given as edges, first convert it into adjacency list.

Then start DFS from node `0`.

For every child branch, we check:

    does this child branch contain any apple?

If yes, then we must go to that child and come back.

So we add:

    child_cost + 2

Here:

    child_cost = cost needed inside child's subtree
    +2 = go from current node to child and come back

## DFS Meaning

    dfs(node, parent)

means:

    minimum cost to collect all apples in this node's subtree
    and come back to this node

## Why Parent Is Used

The tree is undirected.

So if we have edge:

    0 -- 1

Then graph stores:

    0 -> 1
    1 -> 0

If DFS goes from 0 to 1, then from 1 it can again go back to 0.

To avoid this, we pass parent.

    if child == parent:
        continue

## DFS Logic

For every child:

    child_cost = dfs(child, node)

After DFS returns, we check:

    if child_cost > 0 or child in apple

This means:

    either child's subtree has apple
    or child itself has apple

Then add:

    cost += child_cost + 2

## Code

    from typing import List

    class Solution:
        def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
            graph = [[] for _ in range(n)]

            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            apple = set()
            for i in range(len(hasApple)):
                if hasApple[i] == True:
                    apple.add(i)

            def dfs(node, parent):
                cost = 0

                for child in graph[node]:
                    if child == parent:
                        continue

                    child_cost = dfs(child, node)

                    if child_cost > 0 or child in apple:
                        cost += child_cost + 2

                return cost

            return dfs(0, -1)

## Dry Run

Input:

    n = 7
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    hasApple = [False, False, True, False, True, True, False]

Tree:

            0
          /   \
         1     2
       /  \   / \
      4    5 3   6

Apple nodes:

    2, 4, 5

Start:

    dfs(0, -1)

Node 0 checks child 1.

Call:

    dfs(1, 0)

Node 1 checks child 4.

Call:

    dfs(4, 1)

Node 4 has apple and no child except parent.

So:

    dfs(4, 1) returns 0

Back at node 1:

    child = 4
    child_cost = 0

Since child 4 has apple:

    cost += 0 + 2
    cost = 2

This means:

    1 -> 4 -> 1

Now node 1 checks child 5.

Call:

    dfs(5, 1)

Node 5 has apple and no child except parent.

So:

    dfs(5, 1) returns 0

Back at node 1:

    child = 5
    child_cost = 0

Since child 5 has apple:

    cost += 0 + 2
    cost = 4

So:

    dfs(1, 0) returns 4

Back at node 0:

    child = 1
    child_cost = 4

Since child_cost is greater than 0:

    cost += 4 + 2
    cost = 6

This means:

    0 -> 1 -> 4 -> 1 -> 5 -> 1 -> 0

Now node 0 checks child 2.

Call:

    dfs(2, 0)

Node 2 checks child 3.

Node 3 has no apple, so returns 0.

Node 2 checks child 6.

Node 6 has no apple, so returns 0.

So:

    dfs(2, 0) returns 0

Back at node 0:

    child = 2
    child_cost = 0

But child 2 itself has apple.

So:

    cost += 0 + 2
    cost = 8

This means:

    0 -> 2 -> 0

Final answer:

    8

## Recursion Tree

    dfs(0, -1)
    |
    |-- dfs(1, 0)
    |   |
    |   |-- dfs(4, 1)
    |   |   returns 0
    |   |
    |   |-- dfs(5, 1)
    |   |   returns 0
    |   |
    |   returns 4
    |
    |-- dfs(2, 0)
    |   |
    |   |-- dfs(3, 2)
    |   |   returns 0
    |   |
    |   |-- dfs(6, 2)
    |   |   returns 0
    |   |
    |   returns 0
    |
    returns 8

## What To Remember

This is a bottom-up DFS.

First DFS goes deep into child.

Then child returns its cost to parent.

Parent decides whether that child branch is useful or not.

Useful branch means:

    child has apple
    or child's subtree has apple

Then add:

    child_cost + 2

## Complexity

Let:

    n = number of nodes

Time Complexity:

    O(n)

Every node and edge is visited once.

Space Complexity:

    O(n)

For adjacency list, apple set, and recursion stack.

## Key Learning

Whenever a tree DFS problem asks for cost from subtree:

    ask child for its answer first
    then use child answer at current node

Pattern:

    child_cost = dfs(child, node)

    if child branch is useful:
        cost += child_cost + edge_cost
