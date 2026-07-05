# RRDAG. Present for Andrii

## Problem Link

https://www.codechef.com/problems/RRDAG

## Platform

CodeChef

## Rating

2700+

## Topic

Graph, DAG, Topological Sort, Lexicographic Order

## Problem Description

We are given a DAG using an adjacency matrix.

We need to add the maximum number of edges such that the graph still remains a DAG.

If multiple maximum answers are possible, we need to output the lexicographically smallest sequence of added edges.

## Core Idea

In a DAG, there exists a topological order.

If node `u` comes before node `v` in topological order, then adding edge:

    u -> v

will not create a cycle.

So to add the maximum number of edges:

    take every pair of nodes in topological order
    add missing edge from earlier node to later node

But here the problem also asks for lexicographically smallest sequence of edges.

Normal topological sort can give any valid order.

That can create edges like:

    3 2

instead of a lexicographically smaller edge:

    2 3

So we need a careful topological order.

## Important Intuition

To get lexicographically smallest added edges, smaller numbered nodes should come earlier whenever possible.

So we build topological order from the back.

At every step:

    choose the largest sink node

A sink node means:

    outdegree = 0

Because a sink node can safely be placed at the end of topological order.

By placing larger sink nodes at the end first, smaller nodes stay earlier.

## Why Reverse Topological Sort

Normal topo sort:

    use indegree
    pick source nodes
    build from front

Here we use reverse topo sort:

    use outdegree
    pick sink nodes
    build from back

And among all available sink nodes, pick the largest one.

## Code

    import sys
    import heapq

    def main():
        data = sys.stdin.read().split()

        if not data:
            return

        n = int(data[0])
        rows = data[1:1 + n]

        mat = []
        parents = [[] for _ in range(n)]
        outdegree = [0] * n
        edges_count = 0

        for i in range(n):
            row = rows[i]
            mat.append(row)

            for j in range(n):
                if row[j] == '1':
                    outdegree[i] += 1
                    parents[j].append(i)
                    edges_count += 1

        heap = []

        for i in range(n):
            if outdegree[i] == 0:
                heapq.heappush(heap, -i)

        topo = [0] * n
        index = n - 1

        while heap:
            node = -heapq.heappop(heap)

            topo[index] = node
            index -= 1

            for par in parents[node]:
                outdegree[par] -= 1

                if outdegree[par] == 0:
                    heapq.heappush(heap, -par)

        pos = [0] * n

        for i in range(n):
            pos[topo[i]] = i

        total_possible_edges = n * (n - 1) // 2
        add_count = total_possible_edges - edges_count

        sys.stdout.write(str(add_count) + "\n")

        output = []

        for u in range(n):
            for v in range(n):
                if u == v:
                    continue

                if mat[u][v] == '1':
                    continue

                if pos[u] < pos[v]:
                    output.append(str(u + 1) + " " + str(v + 1) + "\n")

                    if len(output) >= 10000:
                        sys.stdout.write("".join(output))
                        output = []

        if output:
            sys.stdout.write("".join(output))

    main()

## Dry Run

Input:

    3
    010
    000
    000

This means:

    1 -> 2

Node 3 is independent.

Initial outdegree:

    node 1 = 1
    node 2 = 0
    node 3 = 0

Sink nodes are:

    2, 3

We build topo from the back.

Pick largest sink first:

    3

Put it at last:

    [_, _, 3]

Next sink:

    2

Put it before 3:

    [_, 2, 3]

After removing node 2, node 1 becomes sink.

Put node 1 first:

    [1, 2, 3]

Now topological order is:

    1, 2, 3

Now add all missing edges from earlier to later.

Possible safe edges:

    1 -> 2
    1 -> 3
    2 -> 3

Already existing edge:

    1 -> 2

So add:

    1 3
    2 3

Output:

    2
    1 3
    2 3

## Why Normal Topo Fails

Normal topo can give:

    1, 3, 2

Then missing edges become:

    1 3
    3 2

But lexicographically smallest answer should be:

    1 3
    2 3

Sorting cannot fix this because sorting only changes printing order.

It cannot change edge direction from:

    3 2

to:

    2 3

So the topological order itself must be chosen carefully.

## Complexity

Let:

    N = number of nodes

Time Complexity:

    O(N^2)

Because we read the adjacency matrix and check all possible pairs.

Space Complexity:

    O(N^2)

Because the adjacency matrix is stored.

## Key Learning

For maximum edge addition in DAG:

    add every missing edge from earlier topo node to later topo node

For lexicographically smallest answer:

    build topo from back
    pick largest sink first
