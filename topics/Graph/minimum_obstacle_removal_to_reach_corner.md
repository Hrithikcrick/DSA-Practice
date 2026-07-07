# 2290. Minimum Obstacle Removal to Reach Corner

## Problem Link

https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/description/

## Platform

LeetCode

## Difficulty

Hard

## Topic

Graph, Matrix, Shortest Path, 0-1 BFS, Deque

## Companies

Not available

## Problem Description

We are given a grid containing only 0 and 1.

    0 -> empty cell
    1 -> obstacle cell

We start from the top-left corner:

    (0, 0)

We need to reach the bottom-right corner:

    (m - 1, n - 1)

We can move in 4 directions:

    up
    down
    left
    right

If we move to a 0 cell, no obstacle is removed.

If we move to a 1 cell, we remove one obstacle.

We need to return the minimum number of obstacles removed to reach the destination.

## Intuition

This is a shortest path problem.

But normal BFS is not enough because normal BFS works when every move has the same cost.

Here move cost is different:

    moving to 0 -> cost 0
    moving to 1 -> cost 1

So we use 0-1 BFS.

0-1 BFS is used when edge weights are only:

    0 or 1

We use deque.

If next cell has value 0:

    cost does not increase
    push it to front of deque

If next cell has value 1:

    cost increases by 1
    push it to back of deque

This helps us process cheaper paths first.

## State Meaning

    dist[r][c]

means:

    minimum obstacles removed to reach cell (r, c)

Initially:

    dist[0][0] = 0

All other cells are infinity because we have not reached them yet.

## Main Logic

For current cell:

    i, j

Check all 4 neighbours:

    new_i, new_j

Calculate new cost:

    new_cost = dist[i][j] + grid[new_i][new_j]

If this new cost is better than old cost:

    if new_cost < dist[new_i][new_j]:

Then update:

    dist[new_i][new_j] = new_cost

If neighbour is 0:

    queue.appendleft((new_i, new_j))

If neighbour is 1:

    queue.append((new_i, new_j))

## Code

    from typing import List
    from collections import deque

    class Solution:
        def minimumObstacles(self, grid: List[List[int]]) -> int:
            rows = len(grid)
            cols = len(grid[0])

            dist = [[float("inf") for _ in range(cols)] for _ in range(rows)]

            queue = deque()
            queue.append((0, 0))
            dist[0][0] = 0

            while len(queue) != 0:
                i, j = queue.popleft()

                for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                    new_i = i + dx
                    new_j = j + dy

                    if new_i < 0 or new_j < 0 or new_i >= rows or new_j >= cols:
                        continue

                    new_cost = dist[i][j] + grid[new_i][new_j]

                    if new_cost < dist[new_i][new_j]:
                        dist[new_i][new_j] = new_cost

                        if grid[new_i][new_j] == 0:
                            queue.appendleft((new_i, new_j))
                        else:
                            queue.append((new_i, new_j))

            return dist[rows - 1][cols - 1]

## Dry Run

Input:

    grid = [
        [0,1,1],
        [1,1,0],
        [1,1,0]
    ]

Start:

    dist[0][0] = 0
    queue = [(0,0)]

From cell (0,0), we can go to:

    (0,1) = 1
    (1,0) = 1

Both are obstacle cells.

So cost becomes:

    0 + 1 = 1

Update:

    dist[0][1] = 1
    dist[1][0] = 1

Since both are 1, push them to back of deque.

Now continue BFS.

From (0,1), we can go to:

    (0,2) = 1
    (1,1) = 1

Cost becomes:

    1 + 1 = 2

Update those cells.

From (0,2), we can go to:

    (1,2) = 0

Cost remains:

    2 + 0 = 2

Because cell is 0, push it to front.

From (1,2), we can go to:

    (2,2) = 0

Cost remains:

    2 + 0 = 2

Destination reached with minimum obstacle removal:

    2

So answer:

    2

## Why Not Normal BFS?

Normal BFS finds minimum number of steps.

But this question asks minimum number of obstacles removed.

A longer path with fewer obstacles can be better than a shorter path with more obstacles.

So we need 0-1 BFS.

## Why appendleft for 0?

If next cell is 0:

    cost does not increase

So we process it early:

    queue.appendleft((new_i, new_j))

## Why append for 1?

If next cell is 1:

    cost increases by 1

So we process it later:

    queue.append((new_i, new_j))

## Complexity

Let:

    total cells = rows * cols

Time Complexity:

    O(rows * cols)

Each cell can be relaxed with 0-1 BFS.

Space Complexity:

    O(rows * cols)

Because of dist matrix and deque.

## Key Learning

Whenever a grid shortest path problem has cost only 0 and 1, think:

    0-1 BFS

If cost is general like 2, 5, 10, then use Dijkstra.
