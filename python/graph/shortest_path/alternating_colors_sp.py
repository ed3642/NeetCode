# https://leetcode.com/problems/shortest-path-with-alternating-colors
from collections import deque
from typing import List

class Solution:

    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        # SPFA considering starting with red and blue 
        RED = 0
        BLUE = 1
        adj_list = [[] for _ in range(n)]
        distances = [[float('inf') for _ in range(2)] for _ in range(n)] # stores [red start, blue start]
        distances[0] = [0, 0]

        for _from, _to in redEdges:
            adj_list[_from].append((_to, RED)) # append <nei, type>
        for _from, _to in blueEdges:
            adj_list[_from].append((_to, BLUE))
        
        # consider both starting types
        q = deque([(0, RED, 0), (0, BLUE, 0)]) # <dist, prev_type, node>

        while q:
            dist, prev_type, node = q.popleft()

            for nei_node, nei_type in adj_list[node]:
                if prev_type != nei_type:
                    cand_dist = dist + 1
                    if cand_dist < distances[nei_node][nei_type]:
                        distances[nei_node][nei_type] = cand_dist
                        q.append((cand_dist, nei_type, nei_node))

        # format res
        res = [-1] * n
        for node, dist in enumerate(distances):
            red_d, blue_d = dist
            best = min(red_d, blue_d)
            if best != float('inf'):
                res[node] = best

        return res