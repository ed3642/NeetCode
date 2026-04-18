# https://leetcode.com/problems/critical-connections-in-a-network/description/

from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        # key ideas: ll[nei] > t[node] means nei cant reach a node younger than or equal to node so it must be a critical edge
        # we propagate the ll to each node from its neighbors except its parent

        def dfs(node):
            nonlocal curr_t
            t[node] = curr_t
            ll[node] = curr_t
            curr_t += 1

            for nei in g[node]:
                if parent[nei] == NOT_SET:
                    parent[nei] = node
                    dfs(nei)
                    if ll[nei] > t[node]:
                        critical_edges.append((nei, node))
                if parent[node] != nei:
                    ll[node] = min(ll[nei], ll[node])
        
        NOT_SET = -1
        critical_edges = []
        g = [[] for _ in range(n)]
        t = [float('inf')] * n # discover time
        ll = [float('inf')] * n # low link time
        parent = [NOT_SET for _ in range(n)]
        curr_t = 0

        for f, to in connections:
            g[f].append(to)
            g[to].append(f)
        
        dfs(0)

        return critical_edges

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