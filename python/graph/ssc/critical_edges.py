# https://leetcode.com/problems/critical-connections-in-a-network/description/

from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        def dfs(node):
            nonlocal time
            times[node] = time
            lowlinks[node] = time
            time += 1

            for nei in adj_list[node]:
                if times[nei] == UNVISITED:
                    parents[nei] = node
                    dfs(nei)
                    if lowlinks[nei] > times[node]:
                        critical_edges.append((node, nei))
                if nei != parents[node]:
                    lowlinks[node] = min(lowlinks[nei], lowlinks[node])

        UNVISITED = -1
        time = 0
        times = [UNVISITED] * n
        lowlinks = [UNVISITED] * n
        parents = [UNVISITED] * n
        adj_list = [[] for _ in range(n)]
        critical_edges = []

        for _from, _to in connections:
            adj_list[_from].append(_to)
            adj_list[_to].append(_from)
        
        dfs(0)

        return critical_edges

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        def dfs(node):
            nonlocal curr_time
            times[node] = curr_time
            low_link[node] = curr_time
            curr_time += 1

            for nei in adj_list[node]:
                if times[nei] == UNSET:
                    parents[nei] = node
                    dfs(nei)
                    if low_link[nei] > times[node]: # append the critical edges
                        critical_edges.append([node, nei])
                if parents[node] != nei: # propagate the low_link within scc
                    low_link[node] = min(low_link[nei], low_link[node])

        UNSET = -1
        parents = [None for _ in range(n)]
        times = [UNSET for _ in range(n)]
        low_link = [UNSET for _ in range(n)]
        curr_time = 0
        critical_edges = []

        adj_list = [[] for _ in range(n)]
        for _from, _to in connections:
            adj_list[_from].append(_to)
            adj_list[_to].append(_from)

        dfs(0)
        return critical_edges