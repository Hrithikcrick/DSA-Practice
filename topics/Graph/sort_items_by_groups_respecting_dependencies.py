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
