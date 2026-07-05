from typing import List

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        avoid = set()
        for i in range(len(restricted)):
            avoid.add(restricted[i])

        def dfs(node, parent):
            count = 1

            for child in graph[node]:
                if child == parent:
                    continue

                if child in avoid:
                    continue

                count += dfs(child, node)

            return count

        return dfs(0, -1)
