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
