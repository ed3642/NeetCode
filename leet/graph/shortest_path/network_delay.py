# https://leetcode.com/problems/network-delay-time/

import heapq
from collections import defaultdict, deque
from typing import List

class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # SFPA
        
        q = deque([k])
        g = [[] for _ in range(n + 1)]
        d = [float('inf')] * (n + 1)
        in_q = [False] * (n + 1)
        d[k] = 0
        in_q[k] = True

        for f, t, w in times:
            g[f].append((w, t))

        while q:
            node = q.popleft()
            in_q[node] = False

            for nei_w, nei in g[node]:
                cand_d = nei_w + d[node]
                if cand_d < d[nei]:
                    d[nei] = cand_d
                    if not in_q[nei]:
                        q.append(nei)
                        in_q[nei] = True

        max_t = -1
        for node in range(1, n + 1):
            if d[node] == float('inf'):
                return -1
            max_t = max(d[node], max_t)

        return max_t

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # dijkstra
        
        h = [(0, k)]
        g = [[] for _ in range(n + 1)]
        d = [float('inf')] * (n + 1)
        d[k] = 0

        for f, t, w in times:
            g[f].append((w, t))

        while h:
            w, node = heapq.heappop(h)

            if w > d[node]: continue # already have better solution for this node

            for nei_w, nei in g[node]:
                cand_d = nei_w + w
                if cand_d < d[nei]:
                    heapq.heappush(h, (cand_d, nei))
                    d[nei] = cand_d

        max_t = -1
        for node in range(1, n + 1):
            if d[node] == float('inf'):
                return -1
            max_t = max(d[node], max_t)

        return max_t

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # dont need a visited for this djikstras, use the times as a visited
        
        adj_list = defaultdict(list)

        for _from, _to, t in times:
            adj_list[_from].append((_to, t))

        heap = [(0, k)]
        times = defaultdict(list)

        while heap:
            t, node = heapq.heappop(heap)

            if node in times:
                continue

            times[node] = t

            if len(times) == n:
                return t

            for nei, nei_t in adj_list[node]:
                if nei not in times:
                    heapq.heappush(heap, (t + nei_t, nei))
        
        return -1

    # NOTE: nodes go from 1..n
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # dijkstra

        # make adjacency list
        adj_list = [[] for _ in range(n + 1)]
        for edge in times:
            v_from, v_to, distance = edge
            adj_list[v_from].append((distance, v_to))
        
        # initialize
        visited = [False] * (n + 1)
        distances = [float('inf')] * (n + 1)

        heap = [(0, k)]
        distances[k] = 0
        distances[0] = 0 # this node does not exist since we start from 1

        # greedy explore 
        while heap:
            dist, node = heapq.heappop(heap)
            visited[node] = True

            for neighbor in adj_list[node]:
                neighbor_dist, neighbor_node = neighbor
                if not visited[neighbor_node]:
                    candidate_distance = dist + neighbor_dist
                    if distances[neighbor_node] > candidate_distance:
                        distances[neighbor_node] = candidate_distance
                        heapq.heappush(heap, (distances[neighbor_node], neighbor_node))

        max_distance = max(distances)
        
        return -1 if max_distance == float('inf') else max_distance
    
    def networkDelayTime2(self, times: list[list[int]], n: int, k: int) -> int:
        # SPFA with in_queue improvement
        # NOTE: in_queue can only be used for positive weighted graphs

        # make adjacency list
        adj_list = [[] for _ in range(n + 1)]
        for edge in times:
            v_from, v_to, distance = edge
            adj_list[v_from].append((distance, v_to))

        queue = deque([(0, k)])
        distances = [float('inf')] * (n + 1)
        distances[k] = 0
        distances[0] = 0 # does not exist in problem
        in_queue = [False] * (n + 1)
        in_queue[k] = True

        while queue:
            dist, node = queue.popleft()
            in_queue[node] = False

            for neighbor in adj_list[node]:
                neighbor_dist, neighbor_node = neighbor

                candidate_dist = dist + neighbor_dist
                if candidate_dist < distances[neighbor_node]:
                    distances[neighbor_node] = candidate_dist
                    if not in_queue[neighbor_node]:
                        queue.append((distances[neighbor_node], neighbor_node))
                        in_queue[k] = True
        
        max_distance = max(distances)
        return max_distance if max_distance != float('inf') else -1