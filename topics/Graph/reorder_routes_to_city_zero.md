# 1466. Reorder Routes to Make All Paths Lead to the City Zero

## Problem Link

https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/

## Platform

LeetCode

## Difficulty

Medium

## Topic

Graph, DFS, Tree, Reversal Counting

## Companies

Not available

## Problem Description

There are n cities numbered from 0 to n - 1.

There are n - 1 roads and all roads are directed.

We need to reverse minimum number of roads such that every city can reach city 0.

## Intuition

The goal is:

    every city should be able to reach city 0

So all roads should finally point towards city 0.

If we start DFS from city 0, we can treat the graph like an undirected graph only for traversal.

But while traversing, we also remember the original direction of each road.

For every original road:

    u -> v

We store:

    u -> v with cost 1
    v -> u with cost 0

Meaning:

If DFS goes from u to v, then road is going away from city 0 side, so reversal is needed.

If DFS goes from v to u, then original road is already helping that node reach city 0, so no reversal is needed.

## Adjacency List Meaning

For every connection:

    [u, v]

Original road is:

    u -> v

We store:

    adj_list[u].append([v, 1])
    adj_list[v].append([u, 0])

Here:

    cost = 1 means this edge needs to be reversed
    cost = 0 means this edge is already correct

## Code

    from typing import List

    class Solution:
        def minReorder(self, n: int, connections: List[List[int]]) -> int:
            adj_list = [[] for _ in range(n)]

            for u, v in connections:
                adj_list[u].append([v, 1])
                adj_list[v].append([u, 0])

            visited = [False] * n

            def dfs(node):
                visited[node] = True
                count = 0

                for adjNode, cost in adj_list[node]:
                    if visited[adjNode] == False:
                        count += cost
                        count += dfs(adjNode)

                return count

            return dfs(0)

## Dry Run

Input:

    n = 6
    connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

Original roads:

    0 -> 1
    1 -> 3
    2 -> 3
    4 -> 0
    4 -> 5

Adjacency list becomes:

    0 -> [1, 1], [4, 0]
    1 -> [0, 0], [3, 1]
    2 -> [3, 1]
    3 -> [1, 0], [2, 0]
    4 -> [0, 1], [5, 1]
    5 -> [4, 0]

Start DFS from city 0.

From 0 to 1:

    cost = 1

Road 0 -> 1 is going away from city 0, so reverse needed.

Count becomes:

    1

From 1 to 3:

    cost = 1

Road 1 -> 3 is also going away from city 0, so reverse needed.

Count becomes:

    2

From 3 to 2:

    cost = 0

Original road is 2 -> 3, so city 2 can already go towards city 0 through 3.

No reversal needed.

Count remains:

    2

From 0 to 4:

    cost = 0

Original road is 4 -> 0, so city 4 can already reach city 0.

No reversal needed.

Count remains:

    2

From 4 to 5:

    cost = 1

Road 4 -> 5 is going away from city 0, so reverse needed.

Count becomes:

    3

Final answer:

    3

## Why This Works

The graph has n - 1 roads and all cities are connected, so it behaves like a tree.

There is only one path from every city to city 0.

For every edge on that path:

    if edge already points towards 0, no change
    if edge points away from 0, reverse it

DFS from 0 helps us check every road exactly once.

## Complexity

Let:

    n = number of cities

Time Complexity:

    O(n)

Because every road is visited once.

Space Complexity:

    O(n)

Because of adjacency list, visited array, and recursion stack.

## Key Learning

Whenever the question says:

    minimum edges to reverse so every node can reach one fixed node

Think:

    DFS/BFS from fixed node
    use undirected traversal
    store cost 1 for original direction
    store cost 0 for reverse direction
