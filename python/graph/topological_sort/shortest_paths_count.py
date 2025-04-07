# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination

from collections import deque
import heapq
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        # djikstras
        MOD = 10 ** 9 + 7
        adj_list = [[] for _ in range(n)]

        for _from, _to, weight in roads:
            adj_list[_from].append((_to, weight))
            adj_list[_to].append((_from, weight))

        heap = [(0, 0)] # (dist, node)
        distances = [float('inf')] * n
        distances[0] = 0
        visited = [False] * n

        while heap:
            dist, node = heapq.heappop(heap)

            visited[node] = True

            for nei, nei_dist in adj_list[node]:
                if not visited[nei]:
                    cand_dist = dist + nei_dist
                    if cand_dist < distances[nei]:
                        distances[nei] = cand_dist
                        heapq.heappush(heap, (cand_dist, nei))
        
        # build DAG with only shortest path edges
        visited = [False] * n # reset the visited for dfs now
        dag = [[] for _ in range(n)]
        for _from, _to, dist in roads:
            if distances[_from] + dist == distances[_to]:
                dag[_from].append(_to)
            if distances[_to] + dist == distances[_from]:
                dag[_to].append(_from)

        # count paths from 0 to n - 1 in dag
        # only explore nodes once they are 0-deg nodes
        arrivals = [0] * n
        arrivals[0] = 1
        q = deque([0])

        in_degree = [0] * n
        for node in range(n):
            for nei in dag[node]:
                in_degree[nei] += 1

        while q:
            node = q.popleft()

            for nei in dag[node]:
                arrivals[nei] += arrivals[node]
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        return arrivals[n - 1] % MOD