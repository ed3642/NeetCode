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
