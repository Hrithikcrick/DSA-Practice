# 1203. Sort Items by Groups Respecting Dependencies

## Problem Link

https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/description/

## Platform

LeetCode

## Difficulty

Hard

## Topic

Graph, Topological Sort, BFS, Dependency Ordering

## Companies

Not available

## Problem Description

We are given `n` items and `m` groups.

Each item belongs to one group, or it can have no group represented by `-1`.

We need to return an ordering of all items such that:

1. If item `a` must come before item `b`, then `a` appears before `b`.
2. Items belonging to the same group must stay together.

If no valid ordering is possible, return an empty list.

## Intuition

This is a topological sorting problem.

But normal topological sort on items alone is not enough because the question also says that items of the same group should stay together.

So we need two levels of topological sorting:

1. Item-level topological sort
2. Group-level topological sort

Think of every group as a box.

Inside each box, items should be ordered correctly.

Then all boxes should also be ordered correctly.

## Why Convert -1 Groups

Items with group `-1` do not belong to any group.

But for easier handling, every item should belong to exactly one group.

So every `-1` item is given a new unique group.

Example:

    group = [-1, -1, 1, 0, 0, 1, 0, -1]
    m = 2

After conversion:

    group = [2, 3, 1, 0, 0, 1, 0, 4]

Now:

    item 0 -> group 2
    item 1 -> group 3
    item 7 -> group 4

Each no-group item becomes its own separate group.

## Graph Building

For every dependency:

    prev must come before i

we create item edge:

    prev -> i

So:

    item_graph[prev].append(i)
    item_degree[i] += 1

Now if both items belong to different groups, then the group of `prev` must come before the group of `i`.

So we also create group edge:

    group[prev] -> group[i]

## Topological Sort

Topological sort gives a valid ordering where all dependencies are respected.

We run it twice:

    item_order = topo(item_graph, item_degree)
    group_order = topo(group_graph, group_indegree)

`item_order` gives a valid order of individual items.

`group_order` gives a valid order of groups.

If either topological sort fails, that means there is a cycle, so we return an empty list.

## Why Item Order Alone Is Not Enough

Suppose item order is:

    [0, 5, 6, 7, 2, 1, 3, 4]

This may satisfy item dependencies.

But group 0 items may be:

    6, 3, 4

They are not together in the above order.

So we cannot directly return `item_order`.

## Why Group Order Alone Is Not Enough

Group order tells which group should come before which group.

But it does not tell how to arrange items inside a group.

For example, group 0 may contain:

    3, 4, 6

But dependencies may require:

    6 before 3
    3 before 4

So inside group 0, the correct order should be:

    [6, 3, 4]

This internal order comes from `item_order`.

## Final Construction

First, create buckets for each group:

    group_to_items = [[] for _ in range(m)]

Then fill those buckets using `item_order`:

    for item in item_order:
        group_to_items[group[item]].append(item)

This makes sure items inside every group are in correct dependency order.

Then build final answer using `group_order`:

    ans = []

    for g in group_order:
        ans.extend(group_to_items[g])

This makes sure group blocks come in correct group dependency order.

## Dry Run

Input:

    n = 8
    m = 2
    group = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems = [[], [6], [5], [6], [3,6], [], [], []]

After converting `-1` groups:

    group = [2, 3, 1, 0, 0, 1, 0, 4]

Dependencies:

    6 -> 1
    5 -> 2
    6 -> 3
    3 -> 4
    6 -> 4

Item graph gives one possible item order:

    item_order = [0, 5, 6, 7, 2, 1, 3, 4]

Group graph gives one possible group order:

    group_order = [0, 1, 2, 4, 3]

Now fill group buckets using item order:

    group_to_items[0] = [6, 3, 4]
    group_to_items[1] = [5, 2]
    group_to_items[2] = [0]
    group_to_items[3] = [1]
    group_to_items[4] = [7]

Now build final answer using group order:

    group 0 -> [6, 3, 4]
    group 1 -> [5, 2]
    group 2 -> [0]
    group 4 -> [7]
    group 3 -> [1]

Final answer:

    [6, 3, 4, 5, 2, 0, 7, 1]

This is valid because:

    6 before 1
    5 before 2
    6 before 3
    3 before 4
    6 before 4

And same group items are together.

## Code

    from typing import List
    from collections import deque

    class Solution:
        def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
            for i in range(n):
                if group[i] == -1:
                    group[i] = m
                    m += 1

            item_graph = [[] for _ in range(n)]
            item_degree = [0] * n

            group_graph = [[] for _ in range(m)]
            group_indegree = [0] * m

            for i in range(n):
                for prev in beforeItems[i]:
                    item_graph[prev].append(i)
                    item_degree[i] += 1

                    prev_group = group[prev]
                    curr_group = group[i]

                    if prev_group != curr_group:
                        group_graph[prev_group].append(curr_group)
                        group_indegree[curr_group] += 1

            def topo(graph, indegree):
                queue = deque()

                for i in range(len(indegree)):
                    if indegree[i] == 0:
                        queue.append(i)

                order = []

                while queue:
                    node = queue.popleft()
                    order.append(node)

                    for nei in graph[node]:
                        indegree[nei] -= 1

                        if indegree[nei] == 0:
                            queue.append(nei)

                if len(order) != len(indegree):
                    return []

                return order

            item_order = topo(item_graph, item_degree)
            group_order = topo(group_graph, group_indegree)

            if not item_order or not group_order:
                return []

            group_to_items = [[] for _ in range(m)]

            for item in item_order:
                group_to_items[group[item]].append(item)

            ans = []

            for g in group_order:
                ans.extend(group_to_items[g])

            return ans

## Complexity

Let:

    N = number of items
    M = number of groups
    E = total number of dependencies

Time Complexity:

    O(N + M + E)

Because we build graphs and perform topological sort.

Space Complexity:

    O(N + M + E)

Because we store item graph, group graph, indegree arrays, and final grouping.

## Key Learning

When a problem asks for ordering with dependencies, think topological sort.

When a problem has grouped items, think:

    topological sort on items
    topological sort on groups

Then combine both:

    item_order -> order inside groups
    group_order -> order of group blocks
