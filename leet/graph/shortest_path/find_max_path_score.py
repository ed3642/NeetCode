# https://leetcode.com/problems/network-recovery-pathways

from collections import deque
from typing import List
import heapq

class Solution:

    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        
        # g is a DAG
        # djikstras

        def sp(min_weigth):
            
            distance = [float('inf')] * N
            distance[0] = 0
            h = [(0, 0)] # dist, node
            while h:
                dist, node = heapq.heappop(h)

                if dist > distance[node]: # prune stale solutions
                    continue

                if node == N-1:
                    return True

                for nei, nei_d in g[node]:
                    cand_d = dist+nei_d
                    if cand_d < distance[nei] and cand_d <= k and nei_d >= min_weigth:
                        distance[nei] = cand_d
                        heapq.heappush(h, (cand_d, nei))
        
            return False

        N = len(online)
        g = [[] for _ in range(N)]
        biggest_edge = 0
        smallest_edge = float('inf')

        for f, t, w in edges:
            if online[t]:
                g[f].append((t, w))
            smallest_edge = min(smallest_edge, w)
            biggest_edge = max(biggest_edge, w)

        l = smallest_edge
        r = biggest_edge
        one_solution_found = False

        while l <= r:
            m = (l+r)//2
            if sp(m):
                l = m+1
                one_solution_found = True
            else:
                r = m-1
        
        return r if one_solution_found else -1

    # MLE
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        
        # g is a DAG

        N = len(online)
        g = [[] for _ in range(N)]

        for f, t, w in edges:
            if online[t]:
                g[f].append((t, w))
        
        max_min_edge = -float('inf')
        q = deque([[0, float('inf'), 0]]) # dist, min_edge_seen, node
        while q:
            dist, min_edge, node = q.popleft()

            if node == N-1:
                max_min_edge = max(max_min_edge, min_edge)

            for nei, nei_d in g[node]:
                cand_d = dist+nei_d
                cand_min_edge = min(min_edge, nei_d)
                if cand_d <= k:
                    q.append((cand_d, cand_min_edge, nei))
    
        return max_min_edge if max_min_edge != -float('inf') else -1