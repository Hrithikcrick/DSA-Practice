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
