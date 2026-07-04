# 785. Is Graph Bipartite?

## Problem Link

https://leetcode.com/problems/is-graph-bipartite/description/

## Platform

LeetCode

## Difficulty

Medium

## Topic

Graph, DFS, Coloring

## Companies

Not available

## Problem Description

We are given an undirected graph.

We need to check whether the graph is bipartite or not.

A graph is bipartite if we can divide all nodes into two groups such that no two directly connected nodes are in the same group.

## Intuition

Think of this problem like coloring nodes with two colors.

Use:

    color 0
    color 1

For every edge:

    u -- v

Both nodes should have different colors.

If current node has color 0, then its adjacent node should get color 1.

If current node has color 1, then its adjacent node should get color 0.

If at any point an adjacent node already has the same color as current node, then graph is not bipartite.

## State Meaning

    visited[node]

means:

    -1 -> node is not colored yet
     0 -> node has color 0
     1 -> node has color 1

## DFS Logic

For current node:

    visited[curr_node] = color

Then check all adjacent nodes.

If adjacent node is already colored:

    if visited[adjNode] == color:
        return False

Because same color on both sides of an edge is not allowed.

If adjacent node is not colored:

    color it with opposite color

## Code

    from typing import List

    class Solution:
        def dfs(self, curr_node, visited, graph, color):
            visited[curr_node] = color

            for adjNode in graph[curr_node]:
                if visited[adjNode] != -1:
                    if visited[adjNode] == color:
                        return False
                else:
                    if color == 0:
                        ans = self.dfs(adjNode, visited, graph, 1)
                    else:
                        ans = self.dfs(adjNode, visited, graph, 0)

                    if ans == False:
                        return False

            return True

        def isBipartite(self, graph: List[List[int]]) -> bool:
            total_nodes = len(graph)
            visited = [-1] * total_nodes

            for index in range(0, total_nodes):
                if visited[index] == -1:
                    ans = self.dfs(index, visited, graph, 0)

                    if ans == False:
                        return False

            return True

## Dry Run

Input:

    graph = [[1,3],[0,2],[1,3],[0,2]]

This means:

    0 connected to 1 and 3
    1 connected to 0 and 2
    2 connected to 1 and 3
    3 connected to 0 and 2

Start:

    visited = [-1, -1, -1, -1]

Start DFS from node 0 with color 0:

    visited[0] = 0

Node 0 has neighbours 1 and 3.

Color node 1 with opposite color:

    visited[1] = 1

Node 1 has neighbour 2 unvisited.

Color node 2 with opposite color:

    visited[2] = 0

Node 2 has neighbour 3 unvisited.

Color node 3 with opposite color:

    visited[3] = 1

Now final colors:

    node 0 -> 0
    node 1 -> 1
    node 2 -> 0
    node 3 -> 1

Every connected pair has different color.

So answer:

    True

## When It Fails

Example:

    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]

Here nodes 0, 1, and 2 form a triangle.

Try coloring:

    node 0 -> 0
    node 1 -> 1
    node 2 should be 1 from node 0

But node 1 and node 2 are directly connected and both have color 1.

So answer:

    False

## Why We Run DFS From Every Node

The graph can be disconnected.

Example:

    component 1: 0 -- 1
    component 2: 2 -- 3

Starting DFS from node 0 will not visit nodes 2 and 3.

So we loop through every node:

    for index in range(total_nodes):

If any node is unvisited, we start DFS from that node.

## Complexity

Let:

    V = number of nodes
    E = number of edges

Time Complexity:

    O(V + E)

Because every node and edge is checked once.

Space Complexity:

    O(V)

Because of visited array and recursion stack.

## Key Learning

Whenever a graph problem says:

    divide nodes into two groups
    no adjacent nodes should be in same group
    check bipartite graph

Think:

    DFS/BFS + 2 color coloring
