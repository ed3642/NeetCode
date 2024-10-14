# https://leetcode.com/problems/critical-connections-in-a-network/description/

from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        def dfs(node):
            nonlocal curr_time
            times[node] = curr_time
            low_links[node] = curr_time
            curr_time += 1

            for nei in adj_list[node]:
                if times[nei] == UNSET:
                    parents[nei] = node
                    dfs(nei)
                    if low_links[nei] > times[node]:
                        critical_edges.append((nei, node))
                if nei != parents[node]:
                    low_links[node] = min(low_links[nei], low_links[node])

        adj_list = [[] for _ in range(n)]
        for _from, _to in connections:
            adj_list[_from].append(_to)
            adj_list[_to].append(_from)
        
        UNSET = -1
        times = [UNSET] * n
        low_links = [UNSET] * n
        parents = [None] * n
        critical_edges = []
        curr_time = 0

        dfs(0)
        return critical_edges

