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
