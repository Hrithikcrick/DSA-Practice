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
