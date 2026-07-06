# 2685. Count the Number of Complete Components

## Problem Link

https://leetcode.com/problems/count-the-number-of-complete-components/description/

## Platform

LeetCode

## Difficulty

Medium

## Topic

Graph, DFS, Connected Components

## Companies

Not available

## Problem Description

We are given an undirected graph with n nodes.

We need to count how many connected components are complete.

A connected component is complete if every pair of nodes inside that component has an edge between them.

## Intuition

This question is not asking only to count connected components.

It is asking to count complete connected components.

So for every component, we need to find:

    number of nodes in that component
    number of edges in that component

For a complete graph with k nodes, the required number of edges is:

    k * (k - 1) // 2

So after finding one component using DFS, we check:

    actual_edges == nodes * (nodes - 1) // 2

If yes, then that component is complete.

## Important Observation

In an undirected graph, every edge is stored two times in adjacency list.

For edge:

    u -- v

We store:

    adj_list[u].append(v)
    adj_list[v].append(u)

So if we add degrees of all nodes in a component, every edge is counted twice.

Therefore:

    actual_edges = degree_sum // 2

## DFS Meaning

DFS returns two values:

    nodes
    degree_sum

Here:

    nodes means number of nodes in current component
    degree_sum means total degree of all nodes in current component

## Code

    from typing import List

    class Solution:
        def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
            adj_list = [[] for _ in range(n)]

            for u, v in edges:
                adj_list[u].append(v)
                adj_list[v].append(u)

            vis = [False] * n
            ans = 0

            def dfs(node):
                vis[node] = True

                nodes = 1
                degree_sum = len(adj_list[node])

                for adj_Node in adj_list[node]:
                    if vis[adj_Node] == False:
                        child_nodes, child_degree_sum = dfs(adj_Node)

                        nodes += child_nodes
                        degree_sum += child_degree_sum

                return nodes, degree_sum

            for i in range(n):
                if vis[i] == False:
                    nodes, degree_sum = dfs(i)

                    edges_count = degree_sum // 2

                    if edges_count == nodes * (nodes - 1) // 2:
                        ans += 1

            return ans

## Dry Run

Input:

    n = 6
    edges = [[0,1],[0,2],[1,2],[3,4]]

Graph:

    0 --- 1
     \   /
       2

    3 --- 4

    5

There are 3 connected components:

    component 1: 0, 1, 2
    component 2: 3, 4
    component 3: 5

Adjacency list:

    0 -> [1, 2]
    1 -> [0, 2]
    2 -> [0, 1]
    3 -> [4]
    4 -> [3]
    5 -> []

Start:

    vis = [False, False, False, False, False, False]
    ans = 0

Start outer loop from i = 0.

Node 0 is unvisited, so run DFS from 0.

DFS visits:

    0, 1, 2

For this component:

    nodes = 3
    degree_sum = 6

Actual edges:

    degree_sum // 2 = 6 // 2 = 3

Required edges for complete graph of 3 nodes:

    nodes * (nodes - 1) // 2
    3 * 2 // 2 = 3

Both are equal, so this component is complete.

    ans = 1

Now i = 1 and i = 2 are already visited, so skip.

Now i = 3.

Node 3 is unvisited, so run DFS from 3.

DFS visits:

    3, 4

For this component:

    nodes = 2
    degree_sum = 2

Actual edges:

    2 // 2 = 1

Required edges:

    2 * 1 // 2 = 1

Both are equal, so this component is complete.

    ans = 2

Now i = 5.

Node 5 is unvisited, so run DFS from 5.

For this component:

    nodes = 1
    degree_sum = 0

Actual edges:

    0 // 2 = 0

Required edges:

    1 * 0 // 2 = 0

Both are equal, so single node is also a complete component.

    ans = 3

Final answer:

    3

## Why Outer Loop Is Needed

The graph can have multiple disconnected components.

DFS from node 0 only visits the component containing node 0.

So we run:

    for i in range(n):

If a node is still unvisited, it means it belongs to a new component.

Then we run DFS from that node.

## Why DFS Returns Two Values

DFS returns:

    nodes, degree_sum

Because after DFS finishes, we need to check whether that full component is complete or not.

We cannot decide this by looking at only one node.

We need complete information about the full connected component.

## Complete Component Formula

For k nodes, complete graph edges are:

    k * (k - 1) // 2

Examples:

    1 node  -> 0 edges
    2 nodes -> 1 edge
    3 nodes -> 3 edges
    4 nodes -> 6 edges

So condition is:

    edges_count == nodes * (nodes - 1) // 2

## Complexity

Let:

    n = number of nodes
    e = number of edges

Time Complexity:

    O(n + e)

Because every node and every edge is visited once.

Space Complexity:

    O(n + e)

Because of adjacency list, visited array, and recursion stack.

## Key Learning

Whenever a graph question asks about complete connected components, think:

    DFS/BFS to find one component
    count nodes
    count edges
    compare with complete graph formula
